#!/usr/bin/env python3
"""Radar de vídeos do YouTube — IA para construir e entregar software.

Fluxo diário (custo zero):
  1. GitHub Actions:  python scripts/youtube.py coletar
     Lê os canais seguidos (RSS), roda as buscas fixas e as buscas tiradas do radar de
     repositórios e grava só os vídeos nunca vistos em data/youtube/coleta/AAAA-MM-DD.json.
     Sem chave usa o yt-dlp; com o secret YOUTUBE_API_KEY usa a API oficial (cota grátis).
  2. Tarefa agendada do Claude:
       python scripts/youtube.py revisar DONO/REPO      # aplica o que você marcou nas issues
       python scripts/youtube.py exportar               # .radar/youtube_pendentes.json
       (o Claude escreve .radar/youtube_avaliacoes.json)
       python scripts/youtube.py importar .radar/youtube_avaliacoes.json
       python scripts/youtube.py abrir-issue DONO/REPO  # issue de revisão do dia

Arquivos de dados (a coleta só escreve em data/youtube/coleta/; o resto é da tarefa do Claude):
  data/youtube/videos.json       vídeos aprovados no catálogo
  data/youtube/descartados.json  vídeos avaliados e recusados (não voltam)
  data/youtube/consultas.json    buscas criadas a partir dos repositórios do radar
  data/youtube/canais_auto.json  canais seguidos/bloqueados automaticamente
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ARQ_CFG = RAIZ / "config-youtube.yml"
ARQ_CFG_RADAR = RAIZ / "config.yml"
DIR_DADOS = RAIZ / "data" / "youtube"
DIR_COLETA = DIR_DADOS / "coleta"
ARQ_IDS = DIR_COLETA / "canais_ids.json"
ARQ_ESTADO = DIR_COLETA / "estado.json"
ARQ_VIDEOS = DIR_DADOS / "videos.json"
ARQ_DESC = DIR_DADOS / "descartados.json"
ARQ_CONS = DIR_DADOS / "consultas.json"
ARQ_AUTO = DIR_DADOS / "canais_auto.json"
ARQ_REPOS = RAIZ / "data" / "repos.json"
ARQ_EXPL = RAIZ / "data" / "explicacoes.json"
DIR_PAG = RAIZ / "youtube"
DIR_TMP = RAIZ / ".radar"
ARQ_PEND = DIR_TMP / "youtube_pendentes.json"

API_GH = "https://api.github.com"
API_YT = "https://www.googleapis.com/youtube/v3"
ROTULO = "youtube-revisao"
REPO = os.environ.get("GITHUB_REPOSITORY") or "marcelojacint/radar-github-50k"
NIVEIS = ["iniciante", "intermediário", "avançado"]
IDIOMAS = {"pt": "🇧🇷 português", "en": "🇺🇸 inglês"}
# Filtros da busca do YouTube (parâmetro sp): tipo vídeo + data de envio.
SP = {"semana": "EgQIAxAB", "mes": "EgQIBBAB"}
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

HOJE = dt.datetime.now(ZoneInfo("America/Sao_Paulo")).date().isoformat()


# ───────────────────────────── utilidades ─────────────────────────────

def log(msg):
    print(f"[youtube] {msg}", flush=True)


def ler_json(caminho, padrao):
    try:
        return json.loads(Path(caminho).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return padrao


def salvar_json(caminho, dados):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def dias_desde(data_iso):
    try:
        return (dt.date.fromisoformat(HOJE) - dt.date.fromisoformat(data_iso[:10])).days
    except (TypeError, ValueError):
        return None


def fmt_data(iso):
    try:
        a, m, d = iso[:10].split("-")
        return f"{d}/{m}/{a}"
    except (AttributeError, ValueError):
        return "—"


def fmt_duracao(seg):
    if not seg:
        return ""
    m = int(round(seg / 60))
    return f"{m} min" if m < 60 else f"{m // 60}h{m % 60:02d}"


def fmt_views(n):
    if n is None:
        return ""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}".replace(".0", "").replace(".", ",") + " mi views"
    if n >= 1000:
        return f"{n / 1000:.0f} mil views"
    return f"{n} views"


def limpar(texto, limite=None):
    t = re.sub(r"\s+", " ", texto or "").strip()
    return t[:limite] if limite else t


def titulo_md(texto):
    """Título seguro para usar dentro de [link](url) no Markdown."""
    return (texto or "").replace("[", "(").replace("]", ")")


def ler_cfg():
    cfg = yaml.safe_load(ARQ_CFG.read_text(encoding="utf-8"))
    radar = yaml.safe_load(ARQ_CFG_RADAR.read_text(encoding="utf-8")) if ARQ_CFG_RADAR.exists() else {}
    cfg["areas"] = radar.get("areas") or ["Engenharia e produtividade"]
    return cfg


def http(url, metodo="GET", corpo=None, cab=None, tentativas=3, timeout=30, texto=True):
    h = {"User-Agent": UA}
    h.update(cab or {})
    dados = None
    if corpo is not None:
        dados = json.dumps(corpo).encode("utf-8")
        h.setdefault("Content-Type", "application/json")
    for t in range(tentativas):
        try:
            req = urllib.request.Request(url, data=dados, headers=h, method=metodo)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                b = r.read()
                return r.status, (b.decode("utf-8", "replace") if texto else b)
        except urllib.error.HTTPError as e:
            corpo_erro = e.read().decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503, 504) and t < tentativas - 1:
                time.sleep(5 * (t + 1))
                continue
            return e.code, corpo_erro
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            if t < tentativas - 1:
                time.sleep(3 * (t + 1))
                continue
            return 0, str(e)
    return 0, "sem resposta"


def gh(metodo, caminho, corpo=None):
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    st, txt = http(f"{API_GH}{caminho}", metodo, corpo, h)
    try:
        return st, json.loads(txt) if txt else None
    except json.JSONDecodeError:
        return st, txt


# ───────────────────────── coleta (GitHub Actions) ─────────────────────────

NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
      "m": "http://search.yahoo.com/mrss/"}


def ler_feed(xml_texto):
    """Converte o RSS (Atom) de um canal ou playlist do YouTube em lista de vídeos."""
    raiz = ET.fromstring(xml_texto)
    videos = []
    for e in raiz.findall("a:entry", NS):
        vid = e.findtext("yt:videoId", namespaces=NS)
        if not vid:
            continue
        link = e.find("a:link", NS)
        href = link.get("href", "") if link is not None else ""
        st = e.find("m:group/m:community/m:statistics", NS)
        views = None
        if st is not None and (st.get("views") or "").isdigit():
            views = int(st.get("views"))
        videos.append({
            "id": vid,
            "titulo": limpar(e.findtext("a:title", namespaces=NS)),
            "canal": limpar(e.findtext("a:author/a:name", namespaces=NS)),
            "canal_id": e.findtext("yt:channelId", namespaces=NS) or "",
            "publicado": (e.findtext("a:published", namespaces=NS) or "")[:10] or None,
            "descricao": limpar(e.findtext("m:group/m:description", namespaces=NS), 1500),
            "views": views,
            "duracao_s": None,
            "short": "/shorts/" in href,
        })
    return videos


def video_de_ytdlp(ent):
    """Converte uma entrada do yt-dlp (busca em modo --flat-playlist) no formato do radar."""
    vid = ent.get("id") or ""
    if not re.fullmatch(r"[\w-]{11}", vid):
        return None
    url = ent.get("url") or ""
    pub = None
    if ent.get("timestamp"):
        pub = dt.datetime.fromtimestamp(ent["timestamp"], dt.timezone.utc).date().isoformat()
    elif ent.get("upload_date"):
        u = str(ent["upload_date"])
        pub = f"{u[:4]}-{u[4:6]}-{u[6:8]}"
    dur = ent.get("duration")
    return {
        "id": vid,
        "titulo": limpar(ent.get("title")),
        "canal": limpar(ent.get("channel") or ent.get("uploader")),
        "canal_id": ent.get("channel_id") or "",
        "publicado": pub,
        "descricao": limpar(ent.get("description"), 1500),
        "views": ent.get("view_count"),
        "duracao_s": int(dur) if dur else None,
        "short": "/shorts/" in url,
        "ao_vivo": ent.get("live_status") in ("is_live", "is_upcoming"),
    }


def ytdlp_json(url, n):
    cmd = ["yt-dlp", "--flat-playlist", "-J", "--playlist-end", str(n), "--no-warnings", "--ignore-errors", url]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        raise RuntimeError(f"yt-dlp: {e}") from e
    if p.returncode != 0 and not p.stdout.strip():
        raise RuntimeError(limpar(p.stderr, 200) or f"yt-dlp saiu com código {p.returncode}")
    dados = json.loads(p.stdout or "null")
    if not isinstance(dados, dict):
        raise RuntimeError(limpar(p.stderr, 200) or "yt-dlp não retornou dados")
    return dados


def buscar_ytdlp(q, cfg):
    c = cfg["coleta"]
    url = ("https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(q)
           + "&sp=" + SP.get(c.get("janela", "semana"), SP["semana"]))
    dados = ytdlp_json(url, int(c.get("resultados_por_busca", 8)))
    return [v for v in (video_de_ytdlp(e) for e in dados.get("entries") or []) if v]


def duracao_iso(txt):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", txt or "")
    if not m:
        return None
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def buscar_api(q, cfg, chave):
    c = cfg["coleta"]
    dias = 7 if c.get("janela", "semana") == "semana" else 31
    depois = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=dias)).strftime("%Y-%m-%dT%H:%M:%SZ")
    params = urllib.parse.urlencode({"part": "snippet", "type": "video", "q": q, "order": "relevance",
                                     "maxResults": int(c.get("resultados_por_busca", 8)),
                                     "publishedAfter": depois, "key": chave})
    st, txt = http(f"{API_YT}/search?{params}")
    if st != 200:
        raise RuntimeError(f"API do YouTube HTTP {st}: {limpar(txt, 160)}")
    out = []
    for it in json.loads(txt).get("items", []):
        sn = it.get("snippet", {})
        vid = it.get("id", {}).get("videoId")
        if not vid:
            continue
        out.append({"id": vid, "titulo": limpar(html.unescape(sn.get("title") or "")),
                    "canal": limpar(html.unescape(sn.get("channelTitle") or "")),
                    "canal_id": sn.get("channelId", ""), "publicado": (sn.get("publishedAt") or "")[:10] or None,
                    "descricao": limpar(html.unescape(sn.get("description") or ""), 1500),
                    "views": None, "duracao_s": None,
                    "short": False, "ao_vivo": sn.get("liveBroadcastContent") in ("live", "upcoming")})
    return out


def detalhar_api(videos, chave):
    """Completa duração, views e descrição completa (1 unidade de cota a cada 50 vídeos)."""
    ids = [v["id"] for v in videos]
    por_id = {v["id"]: v for v in videos}
    for i in range(0, len(ids), 50):
        params = urllib.parse.urlencode({"part": "contentDetails,statistics,snippet",
                                         "id": ",".join(ids[i:i + 50]), "key": chave})
        st, txt = http(f"{API_YT}/videos?{params}")
        if st != 200:
            log(f"Falha ao detalhar vídeos (HTTP {st})")
            continue
        for it in json.loads(txt).get("items", []):
            v = por_id.get(it["id"])
            if not v:
                continue
            v["duracao_s"] = duracao_iso(it.get("contentDetails", {}).get("duration"))
            vc = it.get("statistics", {}).get("viewCount")
            v["views"] = int(vc) if vc and vc.isdigit() else v.get("views")
            desc = it.get("snippet", {}).get("description")
            if desc:
                v["descricao"] = limpar(desc, 1500)
            idioma = it.get("snippet", {}).get("defaultAudioLanguage") or it.get("snippet", {}).get("defaultLanguage")
            if idioma:
                v["idioma_declarado"] = idioma


def resolver_canal(handle):
    """Descobre o ID (UC…) e o nome de um canal a partir do @."""
    h = handle if handle.startswith("@") else "@" + handle
    st, pagina = http(f"https://www.youtube.com/{urllib.parse.quote(h, safe='@')}",
                    cab={"Cookie": "CONSENT=YES+cb; SOCS=CAI", "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"})
    if st == 200:
        m = (re.search(r'"externalId":"(UC[\w-]{22})"', pagina)
             or re.search(r'<link rel="canonical" href="https://www\.youtube\.com/channel/(UC[\w-]{22})"', pagina))
        if m:
            nome = re.search(r'<meta property="og:title" content="([^"]*)"', pagina)
            return m.group(1), (html.unescape(nome.group(1)) if nome else h)
    try:
        d = ytdlp_json(f"https://www.youtube.com/{h}/videos", 1)
        cid = d.get("channel_id") or d.get("uploader_id") or ""
        if re.fullmatch(r"UC[\w-]{22}", cid):
            return cid, d.get("channel") or d.get("uploader") or h
    except Exception as e:  # noqa: BLE001 — canal com problema não pode derrubar a coleta
        log(f"Canal {h} não encontrado: {e}")
    return None, None


def feed_canal(cid):
    """Vídeos recentes de um canal. A playlist UULF traz só vídeos longos (sem Shorts e lives)."""
    for url in (f"https://www.youtube.com/feeds/videos.xml?playlist_id=UULF{cid[2:]}",
                f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"):
        st, xml_texto = http(url)
        if st == 200 and "<feed" in xml_texto:
            return ler_feed(xml_texto)
    raise RuntimeError(f"RSS indisponível para {cid}")


def buscas_radar(cfg):
    """Buscas criadas a partir dos repositórios do radar, em rodízio (as mais antigas primeiro)."""
    cons = ler_json(ARQ_CONS, {}).get("repos", {})
    estado = ler_json(ARQ_ESTADO, {}).get("buscas", {})
    itens = [(estado.get(d["busca"], ""), repo, d["busca"]) for repo, d in cons.items() if d.get("busca")]
    itens.sort()
    return [(repo, q) for _, repo, q in itens[: int(cfg["coleta"].get("max_buscas_radar", 15))]]


def coletar(cfg):
    c = cfg["coleta"]
    chave = os.environ.get("YOUTUBE_API_KEY", "").strip()
    metodo = "api" if chave else "yt-dlp"
    dur_min = float(c.get("duracao_min_minutos", 4)) * 60
    dur_max = float(c.get("duracao_max_minutos", 180)) * 60
    validade = int(c.get("validade_dias", 21))
    dias_canal = int(c.get("dias_canal", 10))

    vistos = set(ler_json(ARQ_VIDEOS, {})) | set(ler_json(ARQ_DESC, {}))
    arq_hoje = DIR_COLETA / f"{HOJE}.json"
    for f in DIR_COLETA.glob("20*.json"):
        if f != arq_hoje:
            vistos |= {v["id"] for v in ler_json(f, {}).get("videos", [])}
    anterior = ler_json(arq_hoje, {})
    novos = {v["id"]: v for v in anterior.get("videos", [])}
    auto = ler_json(ARQ_AUTO, {})
    bloqueados = set(auto.get("bloquear", {}))
    erros, stats = [], Counter()

    def adicionar(v, fonte):
        stats["vistos"] += 1
        if v["id"] in vistos or v.get("canal_id") in bloqueados:
            return
        if v.get("short") or v.get("ao_vivo"):
            return
        d = v.get("duracao_s")
        if d is not None and not (dur_min <= d <= dur_max):
            return
        idade = dias_desde(v["publicado"]) if v.get("publicado") else None
        if idade is not None and idade > validade:
            return
        if v["id"] in novos:
            if fonte not in novos[v["id"]]["fontes"]:
                novos[v["id"]]["fontes"].append(fonte)
            return
        v.pop("short", None)
        v.pop("ao_vivo", None)
        v["fontes"] = [fonte]
        v["coletado_em"] = HOJE
        novos[v["id"]] = v

    # 1) Canais seguidos (RSS, sem chave e sem cota)
    ids = ler_json(ARQ_IDS, {})
    nao_encontrados = []
    for handle in cfg.get("canais") or []:
        if handle not in ids:
            try:
                cid, nome = resolver_canal(handle)
            except Exception as e:  # noqa: BLE001
                log(f"Canal {handle}: {e}")
                cid, nome = None, None
            if cid:
                ids[handle] = {"id": cid, "nome": nome}
                log(f"Canal {handle} → {cid} ({nome})")
            else:
                nao_encontrados.append(handle)
                continue
            time.sleep(1)
    canais = [(h, d["id"]) for h, d in ids.items() if h in (cfg.get("canais") or [])]
    canais += [(d.get("nome") or cid, cid) for cid, d in auto.get("seguir", {}).items()
               if cid not in {x for _, x in canais}]
    for rotulo, cid in canais:
        try:
            for v in feed_canal(cid):
                idade = dias_desde(v["publicado"]) if v.get("publicado") else None
                if idade is None or idade <= dias_canal:
                    adicionar(v, f"canal {rotulo}")
            stats["canais_ok"] += 1
        except Exception as e:  # noqa: BLE001
            erros.append(f"canal {rotulo}: {e}")
        time.sleep(0.5)

    # 2) Buscas fixas + buscas tiradas do radar de repositórios
    buscas = [(None, q) for q in cfg.get("buscas") or []] + buscas_radar(cfg)
    estado = ler_json(ARQ_ESTADO, {})
    estado.setdefault("buscas", {})
    falhas_seguidas = 0
    for repo, q in buscas:
        try:
            achados = buscar_api(q, cfg, chave) if chave else buscar_ytdlp(q, cfg)
            fonte = f"busca \"{q}\"" + (f" (repo {repo})" if repo else "")
            for v in achados:
                adicionar(v, fonte)
            stats["buscas_ok"] += 1
            falhas_seguidas = 0
            if repo:
                estado["buscas"][q] = HOJE
        except Exception as e:  # noqa: BLE001
            erros.append(f"busca \"{q}\": {e}")
            falhas_seguidas += 1
            if falhas_seguidas >= 5:
                erros.append("5 buscas seguidas falharam — coleta de buscas interrompida hoje.")
                break
        time.sleep(1.5)

    if chave:
        faltando = [v for v in novos.values() if v.get("duracao_s") is None]
        if faltando:
            detalhar_api(faltando, chave)
        for vid in [k for k, v in novos.items()
                    if v.get("duracao_s") is not None and not (dur_min <= v["duracao_s"] <= dur_max)]:
            del novos[vid]

    salvar_json(ARQ_IDS, ids)
    estado["ultima_coleta"] = HOJE
    salvar_json(ARQ_ESTADO, estado)
    saida = {
        "data": HOJE,
        "gerado_em": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "metodo": metodo,
        "estatisticas": {"canais": len(canais), "canais_ok": stats["canais_ok"], "buscas": len(buscas),
                         "buscas_ok": stats["buscas_ok"], "resultados": stats["vistos"], "novos": len(novos)},
        "canais_nao_encontrados": nao_encontrados,
        "erros": erros[:40],
        "videos": sorted(novos.values(), key=lambda v: v["id"]),
    }
    salvar_json(arq_hoje, saida)
    log(f"Método {metodo}: {stats['canais_ok']}/{len(canais)} canais, {stats['buscas_ok']}/{len(buscas)} buscas, "
        f"{len(novos)} vídeos novos. Erros: {len(erros)}")
    for e in erros[:10]:
        log(f"  erro: {e}")
    if nao_encontrados:
        log(f"Canais não encontrados: {', '.join(nao_encontrados)}")


# ───────────────────────── curadoria (tarefa do Claude) ─────────────────────────

def radar_repos():
    base = ler_json(ARQ_REPOS, {}).get("repos", {})
    return {r["nome"].lower(): r for r in base.values() if r.get("nome")}


def candidatos(cfg):
    """Todos os vídeos coletados e ainda não avaliados, dentro da validade."""
    julgados = set(ler_json(ARQ_VIDEOS, {})) | set(ler_json(ARQ_DESC, {}))
    validade = int(cfg["coleta"].get("validade_dias", 21))
    cand = {}
    for f in sorted(DIR_COLETA.glob("20*.json")):
        for v in ler_json(f, {}).get("videos", []):
            if v["id"] in julgados or (dias_desde(v.get("coletado_em", f.stem)) or 0) > validade:
                continue
            if v["id"] in cand:
                for fo in v.get("fontes", []):
                    if fo not in cand[v["id"]]["fontes"]:
                        cand[v["id"]]["fontes"].append(fo)
            else:
                cand[v["id"]] = dict(v)
    return cand


def pontuacao(v):
    p = 0.0
    if any(f.startswith("canal ") for f in v.get("fontes", [])):
        p += 3
    p += 0.5 * (len(v.get("fontes", [])) - 1)
    views = v.get("views") or 0
    idade = max(dias_desde(v.get("publicado") or v.get("coletado_em")) or 1, 1)
    if views:
        p += min(3.0, len(str(int(views / idade))) * 0.6)
    d = v.get("duracao_s")
    if d and 8 * 60 <= d <= 60 * 60:
        p += 0.5
    return p


def exportar(cfg, n):
    cand = sorted(candidatos(cfg).values(), key=pontuacao, reverse=True)
    coletas = sorted(DIR_COLETA.glob("20*.json"))
    ultima = ler_json(coletas[-1], {}) if coletas else {}
    # Repositórios do foco do radar que ainda não viraram busca
    expl = ler_json(ARQ_EXPL, {})
    base = ler_json(ARQ_REPOS, {}).get("repos", {})
    cons = ler_json(ARQ_CONS, {})
    feitos = {k.lower() for k in cons.get("repos", {})} | {k.lower() for k in cons.get("sem_busca", [])}
    foco = []
    for rid, e in expl.items():
        r = base.get(rid)
        if e.get("foco") and r and r.get("ativo", True) and r["nome"].lower() not in feitos:
            novo = (dias_desde(r.get("primeira_vez", "")) or 99) <= 7
            foco.append((not novo, -(r.get("estrelas") or 0), r, e))
    foco.sort(key=lambda x: (x[0], x[1]))
    repos_busca = [{"repo": r["nome"], "estrelas": r.get("estrelas"), "categoria": e.get("categoria"),
                    "resumo": e.get("resumo") or limpar(r.get("descricao"), 200)}
                   for _, _, r, e in foco[:15]]
    saida = {
        "data": HOJE,
        "foco": limpar(cfg.get("foco")),
        "idiomas": cfg.get("idiomas", ["pt", "en"]),
        "max_por_dia": int(cfg.get("max_por_dia", 10)),
        "areas": cfg["areas"],
        "niveis": NIVEIS,
        "coleta": {"ultima": ultima.get("data"), "metodo": ultima.get("metodo"),
                   "estatisticas": ultima.get("estatisticas"), "erros": ultima.get("erros", [])[:10],
                   "canais_nao_encontrados": ultima.get("canais_nao_encontrados", [])},
        "total_pendentes": len(cand),
        "candidatos": [{
            "id": v["id"], "url": f"https://youtu.be/{v['id']}", "titulo": v.get("titulo"),
            "canal": v.get("canal"), "publicado": v.get("publicado"),
            "duracao": fmt_duracao(v.get("duracao_s")) or "?", "views": v.get("views"),
            "idioma_declarado": v.get("idioma_declarado"), "fontes": v.get("fontes", [])[:4],
            "descricao": limpar(v.get("descricao"), 600)} for v in cand[:n]],
        "repos_para_busca": repos_busca,
    }
    salvar_json(ARQ_PEND, saida)
    aviso = "" if ultima.get("data") == HOJE else f" ⚠️ a última coleta é de {ultima.get('data') or 'nunca'}"
    log(f"{len(saida['candidatos'])} candidatos exportados de {len(cand)} pendentes; "
        f"{len(repos_busca)} repositórios do radar para virar busca.{aviso}")


def canonico_area(nome, areas):
    for a in areas:
        if (nome or "").strip().lower() == a.lower():
            return a
    return None


def atualizar_canais_auto(videos, auto, cfg):
    ids_cfg = {d["id"] for h, d in ler_json(ARQ_IDS, {}).items() if h in (cfg.get("canais") or [])}
    rej = auto.setdefault("rejeicoes", {})
    seguir = auto.setdefault("seguir", {})
    auto.setdefault("bloquear", {})
    cont = Counter(v["canal_id"] for v in videos.values() if v.get("canal_id"))
    nomes = {v["canal_id"]: v.get("canal") for v in videos.values() if v.get("canal_id")}
    for cid, n in cont.items():
        if n >= 2 and cid not in seguir and cid not in ids_cfg and rej.get(cid, 0) < 2:
            seguir[cid] = {"nome": nomes.get(cid), "desde": HOJE}
            log(f"Agora seguindo sozinho: {nomes.get(cid)}")


def importar(arq, cfg):
    dados = ler_json(arq, None)
    if dados is None:
        sys.exit(f"Arquivo {arq} não encontrado.")
    cand = candidatos(cfg)
    videos = ler_json(ARQ_VIDEOS, {})
    desc = ler_json(ARQ_DESC, {})
    repos = radar_repos()
    areas = cfg["areas"]
    mantidos = descartados = ignorados = 0
    for it in dados.get("videos", []):
        vid = str(it.get("id", ""))
        v = cand.get(vid)
        if not v:
            ignorados += 1
            continue
        if not it.get("manter"):
            desc[vid] = {"data": HOJE, "motivo": limpar(it.get("motivo"), 200), "titulo": v.get("titulo"),
                         "canal_id": v.get("canal_id")}
            descartados += 1
            continue
        area = canonico_area(it.get("area"), areas)
        resumo, porque = limpar(it.get("resumo")), limpar(it.get("por_que_assistir"))
        if not area or not resumo or not porque:
            log(f"Ignorado {vid}: área inválida ou texto faltando")
            ignorados += 1
            continue
        repo = repos.get(str(it.get("repo") or "").strip().lower())
        videos[vid] = {
            "id": vid, "url": f"https://youtu.be/{vid}", "titulo": v.get("titulo"),
            "titulo_pt": limpar(it.get("titulo_pt")) or v.get("titulo"),
            "canal": v.get("canal"), "canal_id": v.get("canal_id"), "publicado": v.get("publicado"),
            "duracao_s": v.get("duracao_s"), "views": v.get("views"), "area": area,
            "nivel": it.get("nivel") if it.get("nivel") in NIVEIS else "intermediário",
            "idioma": str(it.get("idioma") or "").lower()[:2] or None,
            "resumo": resumo, "por_que_assistir": porque, "repo": repo["nome"] if repo else "",
            "fontes": v.get("fontes", []), "entrada": HOJE,
        }
        mantidos += 1
    hoje = sum(1 for v in videos.values() if v.get("entrada") == HOJE)
    if hoje > int(cfg.get("max_por_dia", 10)):
        log(f"Aviso: {hoje} vídeos entraram hoje (máximo configurado: {cfg.get('max_por_dia')})")

    cons = ler_json(ARQ_CONS, {"repos": {}, "sem_busca": []})
    cons.setdefault("repos", {})
    cons.setdefault("sem_busca", [])
    novas = 0
    for c in dados.get("consultas", []):
        repo = repos.get(str(c.get("repo") or "").strip().lower())
        if not repo:
            continue
        busca = limpar(c.get("busca"), 80)
        if busca:
            cons["repos"][repo["nome"]] = {"busca": busca, "desde": HOJE}
            novas += 1
        elif repo["nome"] not in cons["sem_busca"]:
            cons["sem_busca"].append(repo["nome"])

    auto = ler_json(ARQ_AUTO, {})
    atualizar_canais_auto(videos, auto, cfg)
    salvar_json(ARQ_VIDEOS, videos)
    salvar_json(ARQ_DESC, desc)
    salvar_json(ARQ_CONS, cons)
    salvar_json(ARQ_AUTO, auto)
    limpar_coletas_antigas(cfg)
    gerar_paginas(cfg)
    preparar_issue()
    log(f"{mantidos} vídeos aprovados, {descartados} descartados, {ignorados} ignorados; "
        f"{novas} buscas novas do radar. Catálogo: {len(videos)} vídeos.")


def limpar_coletas_antigas(cfg):
    limite = int(cfg["coleta"].get("validade_dias", 21)) + 14
    for f in DIR_COLETA.glob("20*.json"):
        if (dias_desde(f.stem) or 0) > limite:
            f.unlink()


# ───────────────────────────── revisão (issues) ─────────────────────────────

RE_MARCADO = re.compile(r"^\s*[-*]\s+\[[xX]\].*?<!--\s*yt:([\w-]{11})\s*-->", re.M)


def revisar(repo, cfg):
    desde = (dt.date.fromisoformat(HOJE) - dt.timedelta(days=30)).isoformat() + "T00:00:00Z"
    st, issues = gh("GET", f"/repos/{repo}/issues?labels={ROTULO}&state=all&per_page=50&since={desde}")
    if st != 200 or not isinstance(issues, list):
        log(f"Não consegui ler as issues de revisão (HTTP {st}). Seguindo sem revisão hoje.")
        return
    videos = ler_json(ARQ_VIDEOS, {})
    desc = ler_json(ARQ_DESC, {})
    auto = ler_json(ARQ_AUTO, {})
    rej = auto.setdefault("rejeicoes", {})
    ids_cfg = {d["id"] for h, d in ler_json(ARQ_IDS, {}).items() if h in (cfg.get("canais") or [])}
    removidos, fechadas = [], 0
    for iss in issues:
        if "pull_request" in iss:
            continue
        for vid in RE_MARCADO.findall(iss.get("body") or ""):
            v = videos.pop(vid, None)
            if not v:
                continue
            desc[vid] = {"data": HOJE, "motivo": "rejeitado na revisão", "titulo": v.get("titulo"),
                         "canal_id": v.get("canal_id")}
            removidos.append(v.get("titulo_pt") or v.get("titulo"))
            cid = v.get("canal_id")
            if cid:
                rej[cid] = rej.get(cid, 0) + 1
                if rej[cid] >= 2 and cid not in ids_cfg:
                    auto.setdefault("seguir", {}).pop(cid, None)
                    auto.setdefault("bloquear", {})[cid] = {"nome": v.get("canal"), "desde": HOJE}
        if iss.get("state") == "open" and (dias_desde(iss.get("created_at", "")) or 0) >= 7:
            st2, _ = gh("PATCH", f"/repos/{repo}/issues/{iss['number']}",
                        {"state": "closed", "state_reason": "completed"})
            fechadas += st2 == 200
    salvar_json(ARQ_VIDEOS, videos)
    salvar_json(ARQ_DESC, desc)
    salvar_json(ARQ_AUTO, auto)
    if removidos:
        gerar_paginas(cfg)
    DIR_TMP.mkdir(exist_ok=True)
    (DIR_TMP / "youtube_revisao.txt").write_text("\n".join(removidos), encoding="utf-8")
    log(f"Revisão: {len(removidos)} vídeo(s) removido(s) por você; {fechadas} issue(s) antiga(s) fechada(s).")
    for t in removidos:
        log(f"  removido: {t}")


def linha_issue(v):
    meta = " · ".join(x for x in [v.get("canal"), fmt_duracao(v.get("duracao_s")),
                                  IDIOMAS.get(v.get("idioma"), v.get("idioma") or ""), v.get("area")] if x)
    return (f"- [ ] **[{titulo_md(v['titulo_pt'])}]({v['url']})** — {meta} <!-- yt:{v['id']} -->\n"
            f"  {v['resumo']}")


def preparar_issue():
    videos = ler_json(ARQ_VIDEOS, {})
    hoje = sorted((v for v in videos.values() if v.get("entrada") == HOJE),
                  key=lambda v: (v["area"], v.get("titulo_pt") or ""))
    DIR_TMP.mkdir(exist_ok=True)
    (DIR_TMP / "youtube_abrir_issue.txt").write_text("true" if hoje else "false")
    if not hoje:
        return
    titulo = f"🎬 Revisão YouTube — {fmt_data(HOJE)} ({len(hoje)} vídeo{'s' if len(hoje) > 1 else ''})"
    corpo = ("Vídeos que entraram hoje no [catálogo](../blob/main/youtube/README.md).\n\n"
             "**Marque só o que NÃO serve.** O que ficar sem marcar está aprovado. "
             "A tarefa de amanhã remove os marcados; canais com 2 vídeos recusados deixam de aparecer. "
             "Não precisa fechar a issue: ela fecha sozinha em 7 dias.\n\n"
             + "\n".join(linha_issue(v) for v in hoje) + "\n")
    (DIR_TMP / "youtube_issue_titulo.txt").write_text(titulo, encoding="utf-8")
    (DIR_TMP / "youtube_issue.md").write_text(corpo, encoding="utf-8")


def abrir_issue(repo):
    flag = DIR_TMP / "youtube_abrir_issue.txt"
    if not flag.exists() or flag.read_text().strip() != "true":
        log("Nenhum vídeo novo hoje — nenhuma issue aberta.")
        return
    gh("POST", f"/repos/{repo}/labels", {"name": ROTULO, "color": "c4302b",
                                          "description": "Revisão diária do radar de vídeos do YouTube"})
    corpo = (DIR_TMP / "youtube_issue.md").read_text(encoding="utf-8").replace(
        "](../blob/main/", f"](https://github.com/{repo}/blob/main/")
    st, r = gh("POST", f"/repos/{repo}/issues", {
        "title": (DIR_TMP / "youtube_issue_titulo.txt").read_text(encoding="utf-8").strip(),
        "body": corpo, "labels": [ROTULO]})
    if st == 201:
        log(f"Issue aberta: {r.get('html_url')}")
    else:
        log(f"Falha ao abrir issue (HTTP {st}): {str(r)[:200]}")


# ───────────────────────────── páginas ─────────────────────────────

def ordem(v):
    return (v.get("publicado") or v.get("entrada") or "", v.get("entrada") or "")


def bloco_video(v, link_area=False):
    meta = " · ".join(x for x in [
        f"**{v.get('canal')}**" if v.get("canal") else "", fmt_data(v["publicado"]) if v.get("publicado") else "",
        fmt_duracao(v.get("duracao_s")), IDIOMAS.get(v.get("idioma"), v.get("idioma") or ""),
        v.get("nivel"), fmt_views(v.get("views"))] if x)
    linhas = [f"### [{titulo_md(v['titulo_pt'])}]({v['url']})", meta, "",
              f"{v['resumo']}", "", f"**Por que assistir:** {v['por_que_assistir']}"]
    extras = []
    if v.get("repo"):
        extras.append(f"Repositório relacionado: [{v['repo']}](https://github.com/{v['repo']})")
    if link_area:
        extras.append(f"Área: [{v['area']}](areas/{slug(v['area'])}.md)")
    if extras:
        linhas += ["", " · ".join(extras)]
    return "\n".join(linhas) + "\n"


def gerar_paginas(cfg):
    videos = ler_json(ARQ_VIDEOS, {})
    auto = ler_json(ARQ_AUTO, {})
    areas = cfg["areas"]
    por_area = {a: [] for a in areas}
    for v in videos.values():
        por_area.setdefault(v["area"], []).append(v)
    (DIR_PAG / "areas").mkdir(parents=True, exist_ok=True)

    for area, lista in por_area.items():
        lista.sort(key=ordem, reverse=True)
        txt = [f"# 🎬 {area}", "",
               f"{len(lista)} vídeo(s) · atualizado em {fmt_data(HOJE)} · "
               f"[todas as áreas](../README.md) · "
               f"[repositórios desta área no radar](../../areas/{slug(area)}.md)", ""]
        if not lista:
            txt.append("_Nenhum vídeo nesta área ainda._\n")
        for v in lista:
            txt += [bloco_video(v), "---", ""]
        (DIR_PAG / "areas" / f"{slug(area)}.md").write_text("\n".join(txt), encoding="utf-8")

    ultimos = sorted(videos.values(), key=lambda v: (v.get("entrada") or "", ordem(v)), reverse=True)[:30]
    seguidos = len(cfg.get("canais") or []) + len(auto.get("seguir", {}))
    txt = ["# 🎬 Radar de vídeos — IA para entregar software", "",
           "Vídeos do YouTube escolhidos e explicados em português todos os dias, com o mesmo foco do "
           "[radar de repositórios](../CATALOGO.md): agentes de código, skills, MCP, RAG e IA aplicada a "
           "arquitetura, backend, frontend, banco de dados, segurança, testes e DevOps.", "",
           f"**{len(videos)} vídeos** no catálogo · atualizado em {fmt_data(HOJE)} · {seguidos} canais seguidos", "",
           "Este catálogo também serve de pesquisa para os roteiros da [série de vídeos](../videos/README.md).", "",
           "## Por área", ""]
    for area in areas:
        txt.append(f"- [{area}](areas/{slug(area)}.md) — {len(por_area.get(area, []))} vídeo(s)")
    txt += ["", "## Últimos que entraram", ""]
    if not ultimos:
        txt.append("_O catálogo começa a encher na primeira execução diária._")
    for v in ultimos:
        txt += [bloco_video(v, link_area=True), "---", ""]
    txt += ["", "_Canais, buscas e limites ficam em [config-youtube.yml](../config-youtube.yml)._", ""]
    (DIR_PAG / "README.md").write_text("\n".join(txt), encoding="utf-8")


# ───────────────────────────── main ─────────────────────────────

def main():
    global HOJE
    ap = argparse.ArgumentParser(description="Radar de vídeos do YouTube")
    ap.add_argument("comando", choices=["coletar", "exportar", "importar", "revisar", "abrir-issue", "gerar"])
    ap.add_argument("arg", nargs="?", help="arquivo (importar) ou DONO/REPO (revisar, abrir-issue)")
    ap.add_argument("--max", type=int, default=60, help="exportar: máximo de candidatos")
    ap.add_argument("--data", help="força a data (AAAA-MM-DD), útil para testes")
    a = ap.parse_args()
    if a.data:
        HOJE = a.data
    cfg = ler_cfg()
    if a.comando == "coletar":
        coletar(cfg)
    elif a.comando == "exportar":
        exportar(cfg, a.max)
    elif a.comando == "importar":
        importar(a.arg or str(DIR_TMP / "youtube_avaliacoes.json"), cfg)
    elif a.comando == "revisar":
        revisar(a.arg or REPO, cfg)
    elif a.comando == "abrir-issue":
        abrir_issue(a.arg or REPO)
    else:
        gerar_paginas(cfg)


if __name__ == "__main__":
    main()
