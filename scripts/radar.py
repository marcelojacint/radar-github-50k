#!/usr/bin/env python3
"""
Radar GitHub 50k
Busca diária de repositórios open source com 50 mil+ estrelas, detecta os
novos, explica cada um e avalia a importância por segmento de negócio.

Saídas (todas commitadas no próprio repositório):
  data/repos.json          base completa (estado entre execuções)
  data/explicacoes.json    cache das explicações (não reprocessa o que já foi feito)
  CATALOGO.md              todos os repositórios ativos, por categoria técnica
  segmentos/<slug>.md      visão por segmento de negócio
  relatorios/AAAA-MM-DD.md o que mudou no dia (novos, saíram, crescimento)
"""

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"
ARQ_REPOS = DADOS / "repos.json"
ARQ_EXPL = DADOS / "explicacoes.json"
DIR_REL = RAIZ / "relatorios"
DIR_SEG = RAIZ / "segmentos"
DIR_TMP = RAIZ / ".radar"

API = "https://api.github.com"
URL_ANTHROPIC = "https://api.anthropic.com/v1/messages"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
BRT = dt.timezone(dt.timedelta(hours=-3))
HOJE = dt.datetime.now(BRT).date().isoformat()

CATEGORIAS = {
    "IA e Machine Learning": ["machine-learning", "deep-learning", "llm", "llms", "ai", "artificial-intelligence",
                              "neural-network", "pytorch", "tensorflow", "gpt", "chatgpt", "transformers", "agent",
                              "agents", "ai-agents", "rag", "diffusion", "stable-diffusion", "nlp", "computer-vision",
                              "openai", "ollama", "langchain", "generative-ai", "mcp", "claude", "gemini"],
    "Frontend e UI": ["react", "vue", "angular", "svelte", "frontend", "css", "ui", "components", "web-components",
                      "tailwindcss", "design-system", "nextjs", "html", "css-framework", "ui-components", "animation"],
    "Backend e APIs": ["backend", "api", "web-framework", "server", "http", "rest", "graphql", "django", "flask",
                       "spring", "spring-boot", "express", "fastapi", "laravel", "rails", "microservices", "orm"],
    "Mobile e Desktop": ["android", "ios", "flutter", "react-native", "mobile", "electron", "desktop", "tauri",
                         "cross-platform", "windows", "macos"],
    "DevOps e Cloud": ["devops", "kubernetes", "docker", "containers", "ci", "cd", "cloud", "terraform",
                       "infrastructure", "monitoring", "deployment", "serverless", "ansible", "observability", "k8s"],
    "Dados e Bancos de dados": ["database", "sql", "data", "analytics", "big-data", "etl", "redis", "postgres",
                                "postgresql", "data-visualization", "visualization", "spreadsheet", "search-engine"],
    "Segurança": ["security", "hacking", "pentest", "penetration-testing", "privacy", "encryption", "vpn", "proxy",
                  "authentication", "cybersecurity", "infosec"],
    "Ferramentas de desenvolvimento": ["editor", "ide", "vscode", "cli", "terminal", "developer-tools", "devtools",
                                       "git", "shell", "linter", "testing", "build-tool", "bundler", "code-editor"],
    "Linguagens e runtimes": ["programming-language", "compiler", "runtime", "interpreter", "language"],
    "Sistemas operacionais e infraestrutura": ["operating-system", "linux", "kernel", "os", "embedded"],
    "Aprendizado e listas de recursos": ["awesome", "awesome-list", "list", "roadmap", "interview", "tutorial",
                                         "course", "learn", "books", "cheatsheet", "guide", "education",
                                         "algorithms", "resources", "free", "interview-questions"],
    "Apps prontos e self-hosted": ["self-hosted", "selfhosted", "alternative", "home-automation", "no-code",
                                   "low-code", "workflow-automation", "automation", "productivity", "notes"],
    "Outros": [],
}


# ───────────────────────────── utilidades ─────────────────────────────

def log(msg):
    print(f"[radar] {msg}", flush=True)


def ler_json(caminho, padrao):
    if caminho.exists():
        return json.loads(caminho.read_text(encoding="utf-8"))
    return padrao


def salvar_json(caminho, dados):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def ancora(texto):
    return re.sub(r"[^\w\- ]", "", texto.lower()).replace(" ", "-")


def fmt_estrelas(n):
    if n is None:
        return "—"
    if n >= 1000:
        return f"{n / 1000:.1f}".replace(".0", "").replace(".", ",") + " mil"
    return str(n)


def fmt_data(iso):
    try:
        a, m, d = iso.split("-")
        return f"{d}/{m}/{a}"
    except ValueError:
        return iso


def celula(texto):
    return (texto or "").replace("|", "\\|").replace("\n", " ").strip()


# ─────────────────────────────── HTTP ───────────────────────────────

def _espera(headers, tentativa, codigo):
    """Segundos para esperar antes de tentar de novo, ou None para desistir."""
    ra = headers.get("Retry-After") or headers.get("retry-after")
    if ra and ra.isdigit():
        s = int(ra) + 1
        return s if s <= 120 else None
    if headers.get("X-RateLimit-Remaining") == "0" and headers.get("X-RateLimit-Reset"):
        s = int(headers["X-RateLimit-Reset"]) - int(time.time()) + 2
        return max(s, 1) if s <= 120 else None
    if codigo >= 500:
        return 5 * (tentativa + 1)
    if codigo == 429:
        return 20 * (tentativa + 1)
    return None


def http(url, metodo="GET", corpo=None, cabecalhos=None, tentativas=4, timeout=60):
    cab = {"User-Agent": "radar-github-50k"}
    cab.update(cabecalhos or {})
    dados = None
    if corpo is not None:
        dados = json.dumps(corpo).encode("utf-8")
        cab.setdefault("Content-Type", "application/json")
    for t in range(tentativas):
        req = urllib.request.Request(url, data=dados, headers=cab, method=metodo)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read().decode("utf-8", "replace"), dict(r.headers)
        except urllib.error.HTTPError as e:
            txt = e.read().decode("utf-8", "replace")
            hdr = dict(e.headers)
            if e.code in (403, 429, 500, 502, 503, 504) and t < tentativas - 1:
                s = _espera(hdr, t, e.code)
                if s is not None:
                    log(f"HTTP {e.code} em {url.split('?')[0]} — aguardando {s}s")
                    time.sleep(s)
                    continue
            return e.code, txt, hdr
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if t < tentativas - 1:
                time.sleep(5 * (t + 1))
                continue
            return 0, str(e), {}
    return 0, "sem resposta", {}


def gh_headers(accept="application/vnd.github+json"):
    h = {"Accept": accept, "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


# ───────────────────────────── coleta ─────────────────────────────

def normalizar(it):
    return {
        "id": it["id"],
        "nome": it["full_name"],
        "url": it["html_url"],
        "descricao": (it.get("description") or "").strip(),
        "estrelas": it["stargazers_count"],
        "forks": it.get("forks_count", 0),
        "linguagem": it.get("language") or "",
        "topicos": it.get("topics") or [],
        "licenca": ((it.get("license") or {}).get("spdx_id") or "").replace("NOASSERTION", "outra"),
        "homepage": it.get("homepage") or "",
        "criado_em": (it.get("created_at") or "")[:10],
        "ultimo_push": (it.get("pushed_at") or "")[:10],
        "arquivado": bool(it.get("archived")),
    }


def montar_query(lo, hi, cfg):
    partes = [f"stars:{lo}..{hi}" if hi else f"stars:>={lo}"]
    if not cfg["busca"].get("incluir_arquivados", False):
        partes.append("archived:false")
    extra = (cfg["busca"].get("filtro_extra") or "").strip()
    if extra:
        partes.append(extra)
    return " ".join(partes)


def buscar_pagina(q, pagina):
    params = urllib.parse.urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": 100, "page": pagina})
    st, txt, _ = http(f"{API}/search/repositories?{params}", cabecalhos=gh_headers())
    time.sleep(2.2 if TOKEN else 6.5)  # limite da busca: 30/min com token, 10/min sem
    if st != 200:
        raise RuntimeError(f"Busca no GitHub falhou (HTTP {st}): {txt[:300]}")
    return json.loads(txt)


def coletar(cfg):
    """Busca todos os repositórios acima do corte. A API devolve no máximo 1000
    por consulta, então faixas grandes são divididas automaticamente."""
    minimo = int(cfg["busca"]["min_estrelas"])
    faixas = [(minimo, None)]
    achados = {}
    while faixas:
        lo, hi = faixas.pop()
        q = montar_query(lo, hi, cfg)
        pag1 = buscar_pagina(q, 1)
        total = pag1["total_count"]
        if total > 1000:
            topo = hi or (pag1["items"][0]["stargazers_count"] if pag1["items"] else lo * 2)
            meio = (lo + topo) // 2
            if meio <= lo:
                raise RuntimeError(f"Não foi possível dividir a faixa {lo}..{topo}")
            faixas += [(lo, meio), (meio + 1, hi)]
            log(f"{total} resultados em '{q}' — dividindo a faixa em {lo}..{meio} e {meio + 1}..{hi or '∞'}")
            continue
        itens = list(pag1["items"])
        for p in range(2, math.ceil(total / 100) + 1):
            itens += buscar_pagina(q, p)["items"]
        for it in itens:
            achados[str(it["id"])] = normalizar(it)
        log(f"'{q}': {total} repositórios")
    return achados


def consultar_repo(rid):
    st, txt, _ = http(f"{API}/repositories/{rid}", cabecalhos=gh_headers(), tentativas=2)
    if st == 200:
        return normalizar(json.loads(txt))
    if st in (404, 451):
        return "removido"
    return None  # não deu para confirmar (rede, permissão etc.)


def ler_readme(nome, limite=1200):
    st, txt, _ = http(f"{API}/repos/{nome}/readme", cabecalhos=gh_headers("application/vnd.github.raw"),
                      tentativas=2, timeout=30)
    if st != 200:
        return ""
    t = re.sub(r"<!--.*?-->", " ", txt, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)          # imagens e badges
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)        # links -> texto
    t = re.sub(r"<[^>]+>", " ", t)                         # HTML
    t = re.sub(r"```.*?```", " ", t, flags=re.S)           # blocos de código
    t = re.sub(r"[#>*_`|=-]{2,}", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:limite]


# ───────────────────────────── base ─────────────────────────────

def atualizar_base(base, atuais, cfg):
    repos = base.get("repos", {})
    assinatura = montar_query(int(cfg["busca"]["min_estrelas"]), None, cfg)
    nova_base = not repos or base.get("assinatura_busca") != assinatura
    if repos and nova_base:
        log("Filtro de busca mudou — criando nova base de referência (sem marcar novidades).")
    minimo = int(cfg["busca"]["min_estrelas"])
    incluir_arq = cfg["busca"].get("incluir_arquivados", False)
    novos, voltaram, sairam = [], [], []

    for rid, r in atuais.items():
        ant = repos.get(rid)
        if ant is None:
            r.update(primeira_vez=HOJE, estrelas_ontem=None, ativo=True)
            if not nova_base:
                novos.append(rid)
        else:
            r.update(primeira_vez=ant.get("primeira_vez", HOJE), estrelas_ontem=ant.get("estrelas"), ativo=True)
            if not ant.get("ativo", True) and not nova_base:
                voltaram.append(rid)
        repos[rid] = r

    consultas = 0
    for rid, ant in list(repos.items()):
        if rid in atuais or not ant.get("ativo", True):
            continue
        motivo = "não aparece mais na busca"
        if not nova_base and consultas < 80:
            consultas += 1
            info = consultar_repo(rid)
            if info is None:
                continue  # não confirmado: mantém como ativo para evitar alarme falso
            if info == "removido":
                motivo = "removido ou tornado privado"
            elif info["arquivado"] and not incluir_arq:
                motivo = "foi arquivado"
            elif info["estrelas"] < minimo:
                motivo = f"caiu para {fmt_estrelas(info['estrelas'])} estrelas"
            else:  # ainda qualifica; a busca só não o trouxe hoje
                info.update(primeira_vez=ant.get("primeira_vez", HOJE), estrelas_ontem=ant.get("estrelas"), ativo=True)
                repos[rid] = info
                continue
        ant.update(ativo=False, motivo_saida=motivo, saiu_em=HOJE)
        if not nova_base:
            sairam.append(rid)

    base.update(repos=repos, atualizado_em=HOJE, assinatura_busca=assinatura)
    return {"novos": novos, "voltaram": voltaram, "sairam": sairam, "nova_base": nova_base}


# ─────────────────────────── explicações ───────────────────────────

def classificar(r):
    topicos = set(r.get("topicos") or [])
    palavras = set(re.findall(r"[a-z0-9\-]+", f"{r['nome']} {r.get('descricao', '')}".lower()))
    melhor, pontos = "Outros", 0
    for cat, chaves in CATEGORIAS.items():
        p = 2 * len(topicos.intersection(chaves)) + len(palavras.intersection(chaves))
        if p > pontos:
            melhor, pontos = cat, p
    return melhor


def alerta_maturidade(r):
    try:
        ultimo = dt.date.fromisoformat(r.get("ultimo_push") or "")
    except ValueError:
        return ""
    anos = (dt.date.fromisoformat(HOJE) - ultimo).days / 365
    return f"Sem commits há {anos:.0f} anos — verifique se ainda é mantido." if anos >= 2 else ""


def explicacao_por_regras(r):
    return {
        "resumo": r.get("descricao") or "Sem descrição no GitHub.",
        "categoria": classificar(r),
        "por_que_importa": "",
        "segmentos": [],
        "maturidade": alerta_maturidade(r),
        "gerado_por": "regras",
        "gerado_em": HOJE,
    }


SISTEMA = (
    "Você é um arquiteto de software sênior que explica repositórios open source para desenvolvedores "
    "brasileiros que constroem sistemas para clientes de vários segmentos. Seja concreto e honesto: só "
    "relacione um repositório a um segmento quando houver uso real. Responda APENAS com JSON válido."
)


def montar_prompt(lote, cfg):
    itens = []
    for r in lote:
        itens.append({
            "id": str(r["id"]), "nome": r["nome"], "descricao": r.get("descricao", ""),
            "linguagem": r.get("linguagem", ""), "topicos": r.get("topicos", [])[:12],
            "estrelas": r["estrelas"], "licenca": r.get("licenca", ""), "ultimo_commit": r.get("ultimo_push", ""),
            "readme_inicio": r.get("_readme", ""),
        })
    cats = " | ".join(CATEGORIAS)
    segs = " | ".join(cfg["segmentos"])
    return f"""Analise cada repositório abaixo e devolva, em português do Brasil:
- "id": o mesmo id recebido
- "resumo": o que é, em 1 ou 2 frases
- "categoria": exatamente uma destas: {cats}
- "por_que_importa": 1 ou 2 frases sobre o valor prático num projeto real (que problema resolve, o que economiza, quando escolher)
- "segmentos": de 0 a 3 itens, só onde a relação for real; cada item com
    "segmento": exatamente um nome desta lista: {segs}
    "relevancia": "alta" ou "média"
    "como_usar": 1 frase com um uso concreto nesse segmento
- "maturidade": 1 frase curta de alerta se houver (projeto parado, é lista de links e não biblioteca, licença restritiva para uso comercial); "" se não houver

Formato da resposta: {{"repos": [{{...}}, ...]}}

Repositórios:
{json.dumps(itens, ensure_ascii=False, indent=1)}"""


class LimiteIA(Exception):
    """A IA recusou por limite, permissão ou chave — para de tentar nesta execução."""


def chamar_openai_compativel(prompt, cfg):
    """Qualquer API no formato chat/completions da OpenAI (OpenAI, Groq, OpenRouter, Gemini etc.)."""
    oc = cfg["ia"]["openai_compativel"]
    corpo = {
        "model": oc["modelo"],
        "messages": [{"role": "system", "content": SISTEMA}, {"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 4000,
        "response_format": {"type": "json_object"},
    }
    extras = dict(oc.get("parametros_extras") or {})
    corpo.update(extras)
    cab = {"Authorization": f"Bearer {os.environ.get('LLM_API_KEY', '')}"}
    st, txt, _ = http(oc["url"], "POST", corpo, cab, tentativas=3, timeout=180)
    if st == 400 and (extras or "response_format" in corpo):  # provedor recusou um parâmetro opcional
        for k in list(extras) + ["response_format"]:
            corpo.pop(k, None)
        log(f"Provedor recusou parâmetros opcionais; repetindo sem eles ({txt[:150]})")
        st, txt, _ = http(oc["url"], "POST", corpo, cab, tentativas=3, timeout=180)
    if st in (401, 403, 429):
        raise LimiteIA(f"HTTP {st}: {txt[:200]}")
    if st != 200:
        raise RuntimeError(f"HTTP {st}: {txt[:300]}")
    try:
        dados = json.loads(txt)
    except ValueError:
        raise RuntimeError(f"corpo não-JSON: {txt[:300]!r}")
    escolha = (dados.get("choices") or [{}])[0]
    conteudo = (escolha.get("message") or {}).get("content") or ""
    if not conteudo.strip():
        raise RuntimeError(f"resposta vazia (finish_reason={escolha.get('finish_reason')}, corpo={txt[:300]!r})")
    return conteudo


def chamar_anthropic(prompt, cfg):
    chave = os.environ.get("ANTHROPIC_API_KEY", "")
    if not chave:
        raise LimiteIA("secret ANTHROPIC_API_KEY não configurado")
    corpo = {
        "model": cfg["ia"]["modelo_anthropic"],
        "max_tokens": 4000,
        "temperature": 0.2,
        "system": SISTEMA,
        "messages": [{"role": "user", "content": prompt}],
    }
    cab = {"x-api-key": chave, "anthropic-version": "2023-06-01"}
    st, txt, _ = http(URL_ANTHROPIC, "POST", corpo, cab, tentativas=3, timeout=180)
    if st in (401, 403, 429, 529):
        raise LimiteIA(f"Anthropic HTTP {st}: {txt[:200]}")
    if st != 200:
        raise RuntimeError(f"Anthropic HTTP {st}: {txt[:300]}")
    try:
        dados = json.loads(txt)
    except ValueError:
        raise RuntimeError(f"corpo não-JSON: {txt[:300]!r}")
    conteudo = "".join(b.get("text", "") for b in dados.get("content", []))
    if not conteudo.strip():
        raise RuntimeError(f"resposta vazia (stop_reason={dados.get('stop_reason')})")
    return conteudo


def extrair_json(texto):
    texto = re.sub(r"^```(?:json)?|```$", "", texto.strip(), flags=re.M)
    inicio, fim = texto.find("{"), texto.rfind("}")
    if inicio < 0 or fim < inicio:
        raise ValueError(f"sem JSON na resposta: {texto[:200]!r}")
    return json.loads(texto[inicio:fim + 1])


def validar(item, r, cfg, modelo):
    segs_validos = {s.lower(): s for s in cfg["segmentos"]}
    cat = item.get("categoria", "")
    if cat not in CATEGORIAS:
        cat = classificar(r)
    segmentos = []
    for s in (item.get("segmentos") or [])[:3]:
        nome = segs_validos.get(str(s.get("segmento", "")).strip().lower())
        rel = str(s.get("relevancia", "")).strip().lower().replace("media", "média")
        if nome and rel in ("alta", "média"):
            segmentos.append({"segmento": nome, "relevancia": rel, "como_usar": str(s.get("como_usar", "")).strip()})
    maturidade = str(item.get("maturidade") or "").strip() or alerta_maturidade(r)
    return {
        "resumo": str(item.get("resumo") or r.get("descricao") or "").strip(),
        "categoria": cat,
        "por_que_importa": str(item.get("por_que_importa") or "").strip(),
        "segmentos": segmentos,
        "maturidade": maturidade,
        "gerado_por": modelo,
        "gerado_em": HOJE,
    }


def explicar(base, expl, cfg, novos, limite):
    ativos = [r for r in base["repos"].values() if r.get("ativo")]
    for r in ativos:  # garante que todo repositório tenha ao menos a explicação básica
        expl.setdefault(str(r["id"]), explicacao_por_regras(r))

    prov = cfg["ia"].get("provedor", "nenhum")
    if prov == "nenhum" or limite <= 0:
        return 0, "IA desativada"
    if prov == "anthropic":
        chamar, modelo, segredo = chamar_anthropic, cfg["ia"]["modelo_anthropic"], "ANTHROPIC_API_KEY"
    elif prov == "openai-compativel":
        chamar, modelo, segredo = chamar_openai_compativel, cfg["ia"]["openai_compativel"]["modelo"], "LLM_API_KEY"
    elif prov == "github-models":
        return 0, "o GitHub Models foi descontinuado em 30/07/2026; troque ia.provedor no config.yml"
    else:
        return 0, f"provedor desconhecido: {prov}"
    if not os.environ.get(segredo):
        return 0, f"configure o secret {segredo} em Settings → Secrets and variables → Actions"

    novos = set(novos)
    pend = [r for r in ativos if expl[str(r["id"])].get("gerado_por") == "regras"]
    pend.sort(key=lambda r: (str(r["id"]) not in novos, -r["estrelas"]))  # novos primeiro, depois os maiores
    pend = pend[:limite]
    tam = max(1, int(cfg["ia"].get("lote", 6)))
    feitos, motivo, falhas = 0, "", 0
    for i in range(0, len(pend), tam):
        lote = pend[i:i + tam]
        if cfg["ia"].get("ler_readme", True):
            for r in lote:
                r["_readme"] = ler_readme(r["nome"])
        try:
            resposta = extrair_json(chamar(montar_prompt(lote, cfg), cfg))
        except LimiteIA as e:
            motivo = str(e)
            log(f"IA indisponível ({motivo}). O restante fica para a próxima execução.")
            break
        except Exception as e:  # resposta inválida: pula o lote, tenta de novo amanhã
            falhas += 1
            log(f"Lote ignorado: {e}")
            if falhas >= 3:
                motivo = f"3 lotes seguidos falharam (último erro: {str(e)[:150]})"
                log("Parando a IA nesta execução para não gastar cota.")
                break
            continue
        finally:
            for r in lote:
                r.pop("_readme", None)
        falhas = 0
        por_id = {str(x.get("id")): x for x in resposta.get("repos", []) if isinstance(x, dict)}
        for r in lote:
            item = por_id.get(str(r["id"]))
            if item:
                expl[str(r["id"])] = validar(item, r, cfg, modelo)
                feitos += 1
        log(f"Explicados {feitos}/{len(pend)}")
        time.sleep(float(cfg["ia"].get("pausa_segundos", 2)))  # respeita o limite por minuto do provedor
    return feitos, motivo


# ─────────────────────────── relatórios ───────────────────────────

def linha_cabecalho(r):
    partes = [f"**[{r['nome']}]({r['url']})**", f"⭐ {fmt_estrelas(r['estrelas'])}"]
    if r.get("linguagem"):
        partes.append(r["linguagem"])
    if r.get("licenca"):
        partes.append(r["licenca"])
    return " · ".join(partes)


def bloco_repo(r, e):
    linhas = [linha_cabecalho(r), ""]
    linhas.append(f"- **O que é:** {e['resumo']}")
    if e.get("por_que_importa"):
        linhas.append(f"- **Por que importa:** {e['por_que_importa']}")
    if e.get("segmentos"):
        segs = "; ".join(f"**{s['segmento']}** ({s['relevancia']}) — {s['como_usar']}" for s in e["segmentos"])
        linhas.append(f"- **Segmentos:** {segs}")
    if e.get("maturidade"):
        linhas.append(f"- ⚠️ {e['maturidade']}")
    return "\n".join(linhas) + "\n"


def contagem_ia(ativos, expl):
    return sum(1 for r in ativos if expl.get(str(r["id"]), {}).get("gerado_por") != "regras")


def gerar_catalogo(base, expl, cfg):
    ativos = sorted((r for r in base["repos"].values() if r.get("ativo")), key=lambda r: -r["estrelas"])
    por_cat = {c: [] for c in CATEGORIAS}
    for r in ativos:
        por_cat.setdefault(expl[str(r["id"])]["categoria"], []).append(r)

    links_seg = " · ".join(f"[{s}](segmentos/{slug(s)}.md)" for s in cfg["segmentos"])
    out = [
        f"# Catálogo — repositórios com {fmt_estrelas(int(cfg['busca']['min_estrelas']))}+ estrelas",
        "",
        f"Atualizado em {fmt_data(HOJE)} · **{len(ativos)}** repositórios ativos · "
        f"explicados por IA: {contagem_ia(ativos, expl)}/{len(ativos)}",
        "",
        f"**Por segmento:** {links_seg}",
        "",
        "## Categorias",
        "",
    ]
    out += [f"- [{c}](#{ancora(c)}) ({len(rs)})" for c, rs in por_cat.items() if rs]
    for c, rs in por_cat.items():
        if not rs:
            continue
        out += ["", f"## {c}", ""]
        out += [bloco_repo(r, expl[str(r["id"])]) for r in rs]
    (RAIZ / "CATALOGO.md").write_text("\n".join(out), encoding="utf-8")


def gerar_segmentos(base, expl, cfg):
    DIR_SEG.mkdir(exist_ok=True)
    ativos = sorted((r for r in base["repos"].values() if r.get("ativo")), key=lambda r: -r["estrelas"])
    pendentes = len(ativos) - contagem_ia(ativos, expl)
    for seg in cfg["segmentos"]:
        grupos = {"alta": [], "média": []}
        for r in ativos:
            for s in expl[str(r["id"])].get("segmentos", []):
                if s["segmento"] == seg:
                    grupos[s["relevancia"]].append((r, s))
        out = [
            f"# {seg} — repositórios 50 mil+ estrelas que fazem sentido",
            "",
            f"Atualizado em {fmt_data(HOJE)} · {len(grupos['alta'])} de relevância alta · "
            f"{len(grupos['média'])} de relevância média · [voltar ao catálogo](../CATALOGO.md)",
        ]
        if pendentes:
            out += ["", f"> {pendentes} repositórios ainda aguardam análise da IA e entram aqui nas próximas execuções."]
        for rel in ("alta", "média"):
            if not grupos[rel]:
                continue
            out += ["", f"## Relevância {rel}", "", "| Repositório | ⭐ | Categoria | Como usar neste segmento |",
                    "|---|---|---|---|"]
            for r, s in grupos[rel]:
                cat = expl[str(r["id"])]["categoria"]
                out.append(f"| [{r['nome']}]({r['url']}) | {fmt_estrelas(r['estrelas'])} | {celula(cat)} | "
                           f"{celula(s['como_usar'])} |")
        (DIR_SEG / f"{slug(seg)}.md").write_text("\n".join(out) + "\n", encoding="utf-8")


def gerar_relatorio(base, expl, cfg, mud, ia_info):
    repos = base["repos"]
    ativos = [r for r in repos.values() if r.get("ativo")]
    feitos, motivo_ia = ia_info
    out = [f"# Radar 50k — {fmt_data(HOJE)}", ""]
    out.append(f"**{len(ativos)}** repositórios ativos · **{len(mud['novos'])}** novos · "
               f"**{len(mud['sairam'])}** saíram · explicados por IA: {contagem_ia(ativos, expl)}/{len(ativos)}"
               f" (+{feitos} hoje)")
    if motivo_ia and motivo_ia != "IA desativada":
        out += ["", f"> IA pausada nesta execução: {motivo_ia}"]

    if mud["nova_base"]:
        out += ["", f"Base de referência criada com {len(ativos)} repositórios. A partir da próxima execução, "
                    "este relatório mostra só o que mudou. Veja tudo no [catálogo](../CATALOGO.md)."]
    if mud["novos"]:
        out += ["", "## 🆕 Novos no clube", ""]
        for rid in sorted(mud["novos"], key=lambda i: -repos[i]["estrelas"]):
            r = repos[rid]
            out.append(bloco_repo(r, expl[rid]) + f"- Criado em {fmt_data(r.get('criado_em', ''))}\n")

    cresc = [r for r in ativos if r.get("estrelas_ontem") is not None]
    cresc.sort(key=lambda r: r["estrelas"] - r["estrelas_ontem"], reverse=True)
    top = [r for r in cresc[: int(cfg["relatorio"].get("top_crescimento", 10))] if r["estrelas"] > r["estrelas_ontem"]]
    if top:
        out += ["", "## 📈 Maior crescimento desde a última execução", "",
                "| # | Repositório | Categoria | ⭐ agora | Ganho |", "|---|---|---|---|---|"]
        for i, r in enumerate(top, 1):
            cat = expl[str(r["id"])]["categoria"]
            ganho = f"{r['estrelas'] - r['estrelas_ontem']:,}".replace(",", ".")
            out.append(f"| {i} | [{r['nome']}]({r['url']}) | {celula(cat)} | {fmt_estrelas(r['estrelas'])} | "
                       f"+{ganho} |")
    if mud["sairam"]:
        out += ["", "## 👋 Saíram do radar", ""]
        out += [f"- [{repos[i]['nome']}]({repos[i]['url']}) — {repos[i].get('motivo_saida', '')}" for i in mud["sairam"]]
    if mud["voltaram"]:
        out += ["", "## ↩️ Voltaram", ""]
        out += [f"- [{repos[i]['nome']}]({repos[i]['url']}) — ⭐ {fmt_estrelas(repos[i]['estrelas'])}"
                for i in mud["voltaram"]]
    texto = "\n".join(out) + "\n"
    DIR_REL.mkdir(exist_ok=True)
    (DIR_REL / f"{HOJE}.md").write_text(texto, encoding="utf-8")
    return texto


def publicar_saidas(texto, mud, cfg):
    """Prepara o corpo da issue e avisa o workflow se deve abri-la."""
    DIR_TMP.mkdir(exist_ok=True)
    modo = cfg["relatorio"].get("abrir_issue", "quando_houver_novos")
    n = len(mud["novos"])
    abrir = modo == "sempre" or (modo == "quando_houver_novos" and n > 0)
    titulo = f"Radar 50k — {fmt_data(HOJE)}: " + (f"{n} novo(s) repositório(s)" if n else "sem novidades")
    corpo = texto if len(texto) < 60000 else texto[:60000] + f"\n\n…relatório completo em relatorios/{HOJE}.md\n"
    (DIR_TMP / "issue.md").write_text(corpo, encoding="utf-8")
    (DIR_TMP / "titulo.txt").write_text(titulo, encoding="utf-8")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write(f"abrir_issue={'true' if abrir else 'false'}\nnovos={n}\n")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(texto)


# ─────────────────────────────── main ───────────────────────────────

def main():
    global HOJE
    ap = argparse.ArgumentParser(description="Radar diário de repositórios GitHub 50k+")
    ap.add_argument("--max-explicacoes", type=int, help="sobrescreve ia.max_por_execucao")
    ap.add_argument("--sem-ia", action="store_true", help="não chama a IA nesta execução")
    ap.add_argument("--data", help="força a data (AAAA-MM-DD), útil para testes")
    args = ap.parse_args()
    if args.data:
        HOJE = args.data

    cfg = yaml.safe_load((RAIZ / "config.yml").read_text(encoding="utf-8"))
    if not TOKEN:
        log("Aviso: sem GITHUB_TOKEN — a busca fica mais lenta.")

    base = ler_json(ARQ_REPOS, {})
    expl = ler_json(ARQ_EXPL, {})

    atuais = coletar(cfg)
    if not atuais:
        sys.exit("Nenhum repositório retornado — abortando para não apagar a base.")
    mud = atualizar_base(base, atuais, cfg)
    log(f"{len(atuais)} na busca · {len(mud['novos'])} novos · {len(mud['sairam'])} saíram")

    limite = 0 if args.sem_ia else int(args.max_explicacoes or cfg["ia"].get("max_por_execucao", 150))
    ia_info = explicar(base, expl, cfg, mud["novos"], limite)

    salvar_json(ARQ_REPOS, base)
    salvar_json(ARQ_EXPL, expl)
    gerar_catalogo(base, expl, cfg)
    gerar_segmentos(base, expl, cfg)
    texto = gerar_relatorio(base, expl, cfg, mud, ia_info)
    publicar_saidas(texto, mud, cfg)
    log("Concluído.")


if __name__ == "__main__":
    main()
