#!/usr/bin/env python3
"""Vídeos do Radar de IA — um vídeo de 3 a 5 min por repositório, do mais estrelado para o menos.

Tarefa agendada do Claude (sem rede para o YouTube nem para a voz):
  python scripts/video.py proximo            # .radar/video_proximo.json com o próximo da fila + contexto
  (o Claude escreve .radar/video_roteiro.json)
  python scripts/video.py salvar .radar/video_roteiro.json   # valida e grava videos/roteiros/NNN-nome.json
  python scripts/video.py disparar           # pede a renderização ao GitHub Actions

GitHub Actions (video-render.yml):
  python scripts/video.py renderizar         # narração (edge-tts) + quadros + ffmpeg → saida/NNN-nome/
  python scripts/video.py publicar           # release com o vídeo + issue "🎬 Vídeo #N pronto"

Teste local sem voz: python scripts/video.py renderizar videos/roteiros/001-x.json --sem-voz
"""
import argparse
import asyncio
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import wave
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ARQ_CFG = RAIZ / "config-videos.yml"
DIR_VID = RAIZ / "videos"
DIR_ROT = DIR_VID / "roteiros"
ARQ_PROD = DIR_VID / "produzidos.json"
ARQ_REPOS = RAIZ / "data" / "repos.json"
ARQ_EXPL = RAIZ / "data" / "explicacoes.json"
DIR_YT = RAIZ / "data" / "youtube"
DIR_TMP = RAIZ / ".radar"
ARQ_PROX = DIR_TMP / "video_proximo.json"
DIR_SAIDA = RAIZ / "saida"
REPO = os.environ.get("GITHUB_REPOSITORY") or "marcelojacint/radar-github-50k"
HOJE = dt.datetime.now(ZoneInfo("America/Sao_Paulo")).date().isoformat()

W, H, FPS = 1920, 1080, 30
SR = 24000                      # taxa de amostragem da narração
PAUSA_FALA, ENTRADA_CENA, SAIDA_CENA = 0.38, 0.5, 0.45
TIPOS = ["abertura", "topicos", "terminal", "comparacao", "destaque", "ficha", "encerramento"]
RE_EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿️]")


# ───────────────────────────── utilidades ─────────────────────────────

def log(msg):
    print(f"[video] {msg}", flush=True)


def ler_json(caminho, padrao=None):
    try:
        return json.loads(Path(caminho).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return padrao


def salvar_json(caminho, dados):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40]


def ler_cfg():
    return yaml.safe_load(ARQ_CFG.read_text(encoding="utf-8"))


def fmt_estrelas(n):
    if not n:
        return "—"
    if n >= 1000:
        return f"{n / 1000:.0f} mil"
    return str(n)


def fmt_tempo(seg):
    seg = int(seg)
    return f"{seg // 3600}:{seg % 3600 // 60:02d}:{seg % 60:02d}" if seg >= 3600 else f"{seg // 60}:{seg % 60:02d}"


def fmt_data(iso):
    try:
        a, m, d = iso[:10].split("-")
        return f"{d}/{m}/{a}"
    except (AttributeError, ValueError):
        return "—"


def rodar(cmd, entrada=None):
    p = subprocess.run(cmd, input=entrada, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"{cmd[0]} falhou: {p.stderr.decode('utf-8', 'replace')[-800:]}")
    return p.stdout


# ───────────────────────────── fila ─────────────────────────────

def fila(cfg):
    base = ler_json(ARQ_REPOS, {}).get("repos", {})
    expl = ler_json(ARQ_EXPL, {})
    itens = []
    for rid, r in base.items():
        if not r.get("ativo", True) or r.get("arquivado"):
            continue
        e = expl.get(rid, {})
        if cfg.get("fila", "foco") == "foco" and not e.get("foco"):
            continue
        itens.append((r, e))
    itens.sort(key=lambda x: -(x[0].get("estrelas") or 0))
    return itens


def baixar_readme(nome, limite=9000):
    for arq in ("README.md", "readme.md", "Readme.md", "README.MD", "README.rst", "README"):
        try:
            req = urllib.request.Request(f"https://raw.githubusercontent.com/{nome}/HEAD/{arq}",
                                         headers={"User-Agent": "radar-github-50k"})
            with urllib.request.urlopen(req, timeout=30) as r:
                txt = r.read().decode("utf-8", "replace")
            txt = re.sub(r"<img[^>]*>|!\[[^\]]*\]\([^)]*\)", "", txt)       # imagens e badges
            txt = re.sub(r"<[^>]+>", "", txt)
            txt = re.sub(r"\n{3,}", "\n\n", txt)
            return txt.strip()[:limite]
        except (urllib.error.URLError, TimeoutError, OSError):
            continue
    return ""


def videos_relacionados(nome):
    """Vídeos do radar do YouTube sobre o repositório (só como pesquisa para o roteiro)."""
    curto = nome.split("/")[1].lower()
    achados = {}
    fontes = [ler_json(DIR_YT / "videos.json", {}).values()]
    for f in sorted((DIR_YT / "coleta").glob("20*.json")):
        fontes.append(ler_json(f, {}).get("videos", []))
    for lista in fontes:
        for v in lista:
            txt = f"{v.get('titulo', '')} {v.get('descricao', '')}".lower()
            ligado = any(f"(repo {nome.lower()})" in fo.lower() for fo in v.get("fontes", []))
            if ligado or (len(curto) >= 5 and re.search(rf"\b{re.escape(curto)}\b", txt)):
                achados[v["id"]] = {"titulo": v.get("titulo"), "canal": v.get("canal"),
                                    "url": f"https://youtu.be/{v['id']}",
                                    "descricao": (v.get("descricao") or "")[:400]}
    return list(achados.values())[:8]


def proximo(cfg, forcar=None):
    prod = ler_json(ARQ_PROD, {})
    itens = fila(cfg)
    if not itens:
        sys.exit("Fila vazia: rode o radar antes.")
    ranks = {r["nome"]: i + 1 for i, (r, _) in enumerate(itens)}
    pendentes = [(r, e) for r, e in itens if r["nome"] not in prod]
    if forcar:
        escolha = next(((r, e) for r, e in itens if r["nome"].lower() == forcar.lower()), None)
        if not escolha:
            sys.exit(f"{forcar} não está na fila.")
    elif not pendentes:
        sys.exit("Todos os repositórios da fila já têm vídeo.")
    else:
        escolha = pendentes[0]
    r, e = escolha
    depois = next(((x, y) for x, y in pendentes if x["nome"] != r["nome"]), (None, None))
    ep = max([p.get("episodio", 0) for p in prod.values()] + [0]) + 1
    ultimos = sorted(prod.values(), key=lambda p: p.get("episodio", 0))[-5:]
    saida = {
        "data": HOJE, "episodio": ep, "rank": ranks[r["nome"]], "total_fila": len(itens),
        "repo": {k: r.get(k) for k in ("nome", "descricao", "estrelas", "forks", "linguagem", "licenca",
                                        "topicos", "homepage", "criado_em", "ultimo_push", "url")},
        "explicacao": {k: e.get(k) for k in ("resumo", "categoria", "por_que_importa", "areas",
                                             "segmentos", "maturidade")},
        "readme": baixar_readme(r["nome"]),
        "videos_relacionados": videos_relacionados(r["nome"]),
        "proximo_da_fila": {"nome": depois[0]["nome"], "resumo": (depois[1] or {}).get("resumo")} if depois[0] else None,
        "ultimos_episodios": [{"episodio": p.get("episodio"), "repo": p.get("repo"), "titulo": p.get("titulo"),
                               "abertura": p.get("abertura")} for p in ultimos],
        "limites": {"palavras_min": cfg["roteiro"]["palavras_min"], "palavras_max": cfg["roteiro"]["palavras_max"],
                    "tipos_de_cena": TIPOS},
    }
    salvar_json(ARQ_PROX, saida)
    log(f"Próximo: episódio {ep} — {r['nome']} ({fmt_estrelas(r.get('estrelas'))} estrelas, "
        f"{ranks[r['nome']]}º de {len(itens)}). README: {len(saida['readme'])} caracteres; "
        f"{len(saida['videos_relacionados'])} vídeo(s) relacionados.")


# ───────────────────────────── roteiro ─────────────────────────────

def norm_falas(falas):
    out = []
    for f in falas or []:
        if isinstance(f, str):
            f = {"texto": f}
        out.append({"texto": re.sub(r"\s+", " ", str(f.get("texto", ""))).strip(),
                    "falado": re.sub(r"\s+", " ", str(f.get("falado") or "")).strip(),
                    "mostra": f.get("mostra")})
    return out


def itens_da_cena(c):
    if c["tipo"] == "comparacao":
        return list((c.get("esquerda") or {}).get("itens", [])) + list((c.get("direita") or {}).get("itens", []))
    if c["tipo"] == "terminal":
        return list(c.get("linhas", []))
    return list(c.get("itens", []))


def validar(rot, cfg, prox):
    erros = []

    def checa(cond, msg):
        if not cond:
            erros.append(msg)

    checa(rot.get("repo", "").lower() == prox["repo"]["nome"].lower(),
          f"\"repo\" deve ser {prox['repo']['nome']}")
    checa(0 < len(rot.get("titulo_youtube", "")) <= 95, "titulo_youtube: 1 a 95 caracteres")
    checa(50 <= len(rot.get("descricao_youtube", "")) <= 2500, "descricao_youtube: 50 a 2500 caracteres")
    tags = rot.get("tags", [])
    checa(isinstance(tags, list) and 3 <= len(tags) <= 20 and len(",".join(tags)) <= 400,
          "tags: 3 a 20 itens, até 400 caracteres no total")
    capa = rot.get("capa") or {}
    checa(0 < len(capa.get("linha1", "")) <= 26, "capa.linha1: 1 a 26 caracteres")
    checa(0 < len(capa.get("linha2", "")) <= 38, "capa.linha2: 1 a 38 caracteres")
    cenas = rot.get("cenas") or []
    checa(5 <= len(cenas) <= 10, "cenas: de 5 a 10")
    if cenas:
        checa(cenas[0].get("tipo") == "abertura", "a primeira cena tem de ser \"abertura\"")
        checa(cenas[-1].get("tipo") == "encerramento", "a última cena tem de ser \"encerramento\"")
    palavras = 0
    for i, c in enumerate(cenas):
        tipo = c.get("tipo")
        onde = f"cena {i + 1} ({tipo})"
        if tipo not in TIPOS:
            erros.append(f"{onde}: tipo inválido")
            continue
        falas = norm_falas(c.get("falas"))
        c["falas"] = falas
        checa(1 <= len(falas) <= 8, f"{onde}: de 1 a 8 falas")
        for f in falas:
            checa(10 <= len(f["texto"]) <= 320, f"{onde}: cada fala com 10 a 320 caracteres")
            checa(not RE_EMOJI.search(f["texto"] + f["falado"]), f"{onde}: sem emoji nas falas")
            palavras += len(f["texto"].split())
        if tipo != "abertura":
            checa(0 < len(c.get("titulo", "")) <= 48, f"{onde}: \"titulo\" de 1 a 48 caracteres")
        itens = itens_da_cena(c)
        if tipo in ("topicos", "encerramento"):
            checa(1 <= len(itens) <= 5, f"{onde}: de 1 a 5 itens")
            checa(all(0 < len(str(x)) <= 95 for x in itens), f"{onde}: itens com até 95 caracteres")
        if tipo == "terminal":
            checa(1 <= len(itens) <= 9, f"{onde}: de 1 a 9 linhas")
            checa(all(len(str(x)) <= 64 for x in itens), f"{onde}: linhas com até 64 caracteres")
        if tipo == "comparacao":
            for lado in ("esquerda", "direita"):
                d = c.get(lado) or {}
                checa(0 < len(d.get("titulo", "")) <= 30 and 1 <= len(d.get("itens", [])) <= 4,
                      f"{onde}: {lado} precisa de titulo (até 30) e 1 a 4 itens")
                checa(all(len(str(x)) <= 70 for x in d.get("itens", [])), f"{onde}: itens com até 70 caracteres")
        if tipo == "abertura":
            checa(0 < len(c.get("titulo", "")) <= 60, f"{onde}: \"titulo\" (gancho) de 1 a 60 caracteres")
            checa(len(c.get("subtitulo", "")) <= 90, f"{onde}: \"subtitulo\" até 90 caracteres")
        if tipo == "destaque":
            checa(0 < len(c.get("texto", "")) <= 140, f"{onde}: \"texto\" de 1 a 140 caracteres")
        for f in falas:
            m = f.get("mostra")
            if m is not None:
                checa(isinstance(m, int) and 0 <= m < max(len(itens), 1), f"{onde}: \"mostra\" fora da lista de itens")
        for x in itens:
            checa(not RE_EMOJI.search(str(x)), f"{onde}: sem emoji nos itens")
    lim = cfg["roteiro"]
    checa(lim["palavras_min"] <= palavras <= lim["palavras_max"],
          f"narração com {palavras} palavras; precisa ficar entre {lim['palavras_min']} e {lim['palavras_max']}")
    return erros, palavras


def salvar(arq, cfg):
    rot = ler_json(arq)
    prox = ler_json(ARQ_PROX)
    if rot is None or prox is None:
        sys.exit("Rode `proximo` e grave o roteiro antes.")
    erros, palavras = validar(rot, cfg, prox)
    if erros:
        for e in erros:
            log(f"ERRO: {e}")
        sys.exit(f"Roteiro inválido ({len(erros)} problema(s)). Corrija e rode de novo.")
    ep = prox["episodio"]
    nome = prox["repo"]["nome"]
    destino = DIR_ROT / f"{ep:03d}-{slug(nome.split('/')[1])}.json"
    rot.update({"repo": nome, "episodio": ep, "rank": prox["rank"], "total_fila": prox["total_fila"],
                "dados": prox["repo"], "proximo": (prox.get("proximo_da_fila") or {}).get("nome"),
                "gerado_em": HOJE, "palavras": palavras})
    salvar_json(destino, rot)
    prod = ler_json(ARQ_PROD, {})
    prod[nome] = {"episodio": ep, "repo": nome, "arquivo": str(destino.relative_to(RAIZ)), "status": "roteiro",
                  "data": HOJE, "titulo": rot["titulo_youtube"], "abertura": rot["cenas"][0].get("titulo")}
    salvar_json(ARQ_PROD, prod)
    log(f"Roteiro salvo em {destino.relative_to(RAIZ)}: {palavras} palavras, "
        f"~{fmt_tempo(palavras / 2.5 + len(rot['cenas']) * 1.5)} de vídeo.")


def disparar():
    corpo = json.dumps({"ref": "main"}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/actions/workflows/video-render.yml/dispatches", data=corpo,
        method="POST", headers={"Accept": "application/vnd.github+json", "Content-Type": "application/json",
                                "User-Agent": "radar-github-50k",
                                **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
                                   if os.environ.get("GITHUB_TOKEN") else {})})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            log(f"Renderização disparada (HTTP {r.status}).")
    except urllib.error.HTTPError as e:
        log(f"Não consegui disparar (HTTP {e.code}): {e.read()[:200]!r}. "
            "O agendamento das 09:37 renderiza os pendentes.")


# ───────────────────────────── narração ─────────────────────────────

async def _tts(texto, voz, velocidade, destino):
    import edge_tts
    c = edge_tts.Communicate(texto, voz, rate=velocidade)
    await c.save(str(destino))


def narrar(texto, destino, cfg):
    """Gera a fala e devolve as amostras PCM 16 bits mono em SR Hz."""
    for t in range(4):
        try:
            asyncio.run(_tts(texto, cfg["voz"]["nome"], cfg["voz"].get("velocidade", "+0%"), destino))
            if destino.stat().st_size > 1000:
                break
        except Exception as e:  # noqa: BLE001
            log(f"Voz falhou ({e}); tentando de novo")
        import time
        time.sleep(3 * (t + 1))
    else:
        raise RuntimeError("edge-tts não respondeu")
    corte = "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.06"   # tira o silêncio das pontas
    return rodar(["ffmpeg", "-v", "error", "-i", str(destino), "-af", f"{corte},areverse,{corte},areverse",
                  "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"])


def silencio_estimado(texto):
    """Sem voz (teste local): silêncio com a duração aproximada da fala."""
    seg = max(1.2, len(texto.split()) / 2.6)
    return bytes(int(seg * SR) * 2)


# ───────────────────────────── desenho ─────────────────────────────

FONTES = {
    "bold": ["/usr/share/fonts/opentype/inter/Inter-Bold.otf", "/usr/share/fonts/truetype/inter/Inter-Bold.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "semi": ["/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", "/usr/share/fonts/truetype/inter/Inter-SemiBold.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "reg": ["/usr/share/fonts/opentype/inter/Inter-Regular.otf", "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "mono": ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"],
}
_cache_fontes = {}


def fonte(peso, tam):
    from PIL import ImageFont
    k = (peso, tam)
    if k not in _cache_fontes:
        for p in FONTES[peso]:
            if Path(p).exists():
                _cache_fontes[k] = ImageFont.truetype(p, tam)
                break
        else:
            _cache_fontes[k] = ImageFont.load_default(tam)
    return _cache_fontes[k]


def quebrar(d, texto, f, largura):
    linhas, atual = [], ""
    for p in str(texto).split():
        teste = f"{atual} {p}".strip()
        if d.textlength(teste, font=f) <= largura or not atual:
            atual = teste
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


class Pintor:
    def __init__(self, rot, cfg, larg=W, alt=H):
        from PIL import Image, ImageDraw
        self.Image, self.ImageDraw = Image, ImageDraw
        self.rot, self.cfg, self.W, self.H = rot, cfg, larg, alt
        self.c = cfg["cores"]
        self._fundo = None

    def cor(self, nome, alpha=255):
        h = self.c[nome].lstrip("#")
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)

    def fundo(self):
        if self._fundo is None:
            im = self.Image.new("RGB", (self.W, self.H), self.cor("fundo")[:3])
            d = self.ImageDraw.Draw(im)
            a, b = self.cor("fundo"), self.cor("fundo2")
            for y in range(self.H):                     # gradiente vertical suave
                t = y / self.H
                d.line([(0, y), (self.W, y)], fill=tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3)))
            passo = 48 if self.W >= 1900 else 36         # grade de pontos discreta
            pt = tuple(min(255, x + 14) for x in b[:3])
            for y in range(passo, self.H, passo):
                for x in range(passo, self.W, passo):
                    d.point((x, y), fill=pt)
            self._fundo = im
        return self._fundo.copy()

    def estrela(self, d, cx, cy, r, cor):
        import math
        pts = []
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            rr = r if i % 2 == 0 else r * 0.45
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        d.polygon(pts, fill=cor)

    def pilula(self, d, x, y, texto, f, cor_txt, cor_fundo, estrela=False, pad=22):
        tw = d.textlength(texto, font=f)
        alt = f.size + pad
        extra = alt * 0.8 if estrela else 0
        d.rounded_rectangle([x, y, x + tw + pad * 2 + extra, y + alt], radius=alt // 2, fill=cor_fundo)
        if estrela:
            self.estrela(d, x + pad + alt * 0.3, y + alt / 2, alt * 0.3, self.cor("alerta"))
        d.text((x + pad + extra, y + alt / 2), texto, font=f, fill=cor_txt, anchor="lm")
        return x + tw + pad * 2 + extra

    def topo(self, d, cena_idx, total):
        r = self.rot
        canal = (self.cfg.get("canal") or {}).get("nome") or "Radar de IA"
        d.ellipse([140, 62, 158, 80], fill=self.cor("destaque"))
        d.text((172, 71), f"{canal.upper()}  ·  EP. {r['episodio']:03d}", font=fonte("semi", 26),
               fill=self.cor("suave"), anchor="lm")
        dados = r.get("dados") or {}
        txt = f"{fmt_estrelas(dados.get('estrelas'))}   ·   {r.get('rank')}º de {r.get('total_fila')}"
        f = fonte("semi", 26)
        tw = d.textlength(txt, font=f)
        self.estrela(d, self.W - 140 - tw - 26, 71, 13, self.cor("alerta"))
        d.text((self.W - 140, 71), txt, font=f, fill=self.cor("suave"), anchor="rm")
        larg = self.W - 280                                  # progresso das cenas
        d.rounded_rectangle([140, 104, 140 + larg, 108], radius=2, fill=self.cor("borda"))
        d.rounded_rectangle([140, 104, 140 + larg * (cena_idx + 1) / total, 108], radius=2,
                            fill=self.cor("destaque"))

    def titulo(self, d, texto, y=150):
        d.text((140, y), texto, font=fonte("bold", 66), fill=self.cor("texto"))

    # ── cenas ──
    def desenhar(self, cena, idx, total, estado):
        im = self.fundo()
        d = self.ImageDraw.Draw(im, "RGBA")
        self.topo(d, idx, total)
        getattr(self, "c_" + cena["tipo"])(d, cena, estado, im)
        return im

    def c_abertura(self, d, c, estado, im):
        r = self.rot
        dados = r.get("dados") or {}
        dono, nome = r["repo"].split("/", 1)
        y = 255
        d.text((140, y), f"#{r.get('rank')} ENTRE OS REPOSITÓRIOS DE IA MAIS ESTRELADOS DO GITHUB",
               font=fonte("semi", 30), fill=self.cor("destaque"))
        d.text((140, y + 62), f"{dono} /", font=fonte("semi", 54), fill=self.cor("suave"))
        tam = 170
        while d.textlength(nome, font=fonte("bold", tam)) > self.W - 280 and tam > 70:
            tam -= 8
        d.text((132, y + 120), nome, font=fonte("bold", tam), fill=self.cor("texto"))
        yb = y + 120 + tam + 40
        x = self.pilula(d, 140, yb, f"{fmt_estrelas(dados.get('estrelas'))} estrelas", fonte("semi", 32),
                        self.cor("texto"), self.cor("painel"), estrela=True)
        if dados.get("linguagem"):
            x = self.pilula(d, x + 16, yb, dados["linguagem"], fonte("semi", 32), self.cor("texto"), self.cor("painel"))
        if dados.get("licenca"):
            self.pilula(d, x + 16, yb, dados["licenca"], fonte("semi", 32), self.cor("texto"), self.cor("painel"))
        yt = yb + 110
        for ln in quebrar(d, c.get("titulo", ""), fonte("bold", 54), self.W - 280)[:2]:
            d.text((140, yt), ln, font=fonte("bold", 54), fill=self.cor("texto"))
            yt += 68
        for ln in quebrar(d, c.get("subtitulo", ""), fonte("reg", 36), self.W - 280)[:2]:
            d.text((140, yt + 8), ln, font=fonte("reg", 36), fill=self.cor("suave"))
            yt += 48

    def _cartoes(self, d, itens, x, y, larg, alt_max, cor_num, marcador="num"):
        tam = 42
        while tam >= 30:
            f = fonte("semi", tam)
            blocos = [quebrar(d, t, f, larg - 140) for t in itens]
            altura = sum(len(b) * (tam + 12) + 44 for b in blocos) + 20 * (len(itens) - 1)
            if altura <= alt_max:
                break
            tam -= 3
        for i, linhas in enumerate(blocos):
            h = len(linhas) * (tam + 12) + 44
            d.rounded_rectangle([x, y, x + larg, y + h], radius=22, fill=self.cor("painel"),
                                outline=self.cor("borda"), width=2)
            cx, cy = x + 58, y + h / 2
            if marcador == "num":
                d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=cor_num)
                d.text((cx, cy), str(i + 1), font=fonte("bold", 28), fill=self.cor("fundo"), anchor="mm")
            else:
                d.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=cor_num)
                d.line([(cx - 11, cy + 1), (cx - 3, cy + 10), (cx + 12, cy - 9)], fill=self.cor("fundo"), width=6)
            ty = y + 22
            for ln in linhas:
                d.text((x + 110, ty), ln, font=f, fill=self.cor("texto"))
                ty += tam + 12
            y += h + 20
        return y

    def c_topicos(self, d, c, estado, im):
        self.titulo(d, c["titulo"])
        itens = c.get("itens", [])[:max(estado, 0)]
        if itens:
            self._cartoes(d, itens, 140, 270, self.W - 280, 640, self.cor("destaque"))

    def c_encerramento(self, d, c, estado, im):
        self.titulo(d, c["titulo"])
        itens = c.get("itens", [])[:max(estado, 0)]
        fim = self._cartoes(d, itens, 140, 270, self.W - 280, 470, self.cor("destaque2"), marcador="check") if itens else 270
        if estado > len(c.get("itens", [])):
            y = max(fim + 10, 760)
            prox = self.rot.get("proximo")
            d.rounded_rectangle([140, y, self.W - 140, y + 120], radius=24, fill=self.cor("destaque", 40),
                                outline=self.cor("destaque"), width=2)
            linha = f"Próximo episódio: {prox}" if prox else "Fim da fila — obrigado por acompanhar!"
            d.text((180, y + 38), linha, font=fonte("bold", 40), fill=self.cor("texto"), anchor="lm")
            chamada = (self.cfg.get("canal") or {}).get("chamada_final", "")
            d.text((180, y + 88), chamada, font=fonte("reg", 30), fill=self.cor("suave"), anchor="lm")

    def c_terminal(self, d, c, estado, im):
        self.titulo(d, c["titulo"])
        x0, y0, x1, y1 = 140, 270, self.W - 140, 900
        d.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(13, 17, 23, 255), outline=self.cor("borda"), width=2)
        for i, cor in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
            d.ellipse([x0 + 30 + i * 34, y0 + 26, x0 + 50 + i * 34, y0 + 46], fill=cor)
        d.text(((x0 + x1) / 2, y0 + 36), "terminal", font=fonte("semi", 24), fill=self.cor("suave"), anchor="mm")
        f = fonte("mono", 38)
        y = y0 + 90
        for ln in c.get("linhas", [])[:max(estado, 0)]:
            ln = str(ln)
            if ln.startswith("$ "):
                d.text((x0 + 40, y), "$", font=f, fill=self.cor("destaque2"))
                d.text((x0 + 40 + d.textlength("$ ", font=f), y), ln[2:], font=f, fill=self.cor("texto"))
            elif ln.lstrip().startswith("#"):
                d.text((x0 + 40, y), ln, font=f, fill=self.cor("suave"))
            else:
                d.text((x0 + 40, y), ln, font=f, fill=(200, 210, 235))
            y += 56

    def c_comparacao(self, d, c, estado, im):
        self.titulo(d, c["titulo"])
        esq, dir_ = c["esquerda"], c["direita"]
        n_esq = len(esq["itens"])
        mostrar_esq = esq["itens"][:max(estado, 0)]
        mostrar_dir = dir_["itens"][:max(estado - n_esq, 0)]
        meio = self.W // 2
        for (x0, x1), lado, itens, cor in (((140, meio - 20), esq, mostrar_esq, self.cor("alerta")),
                                           ((meio + 20, self.W - 140), dir_, mostrar_dir, self.cor("destaque2"))):
            d.rounded_rectangle([x0, 270, x1, 900], radius=26, fill=self.cor("painel"), outline=cor, width=3)
            d.text((x0 + 40, 300), lado["titulo"], font=fonte("bold", 46), fill=cor)
            y = 390
            f = fonte("semi", 36)
            for t in itens:
                linhas = quebrar(d, t, f, x1 - x0 - 120)
                d.ellipse([x0 + 42, y + 14, x0 + 58, y + 30], fill=cor)
                for ln in linhas:
                    d.text((x0 + 80, y), ln, font=f, fill=self.cor("texto"))
                    y += 48
                y += 26

    def c_destaque(self, d, c, estado, im):
        if c.get("titulo"):
            d.text((self.W / 2, 300), c["titulo"].upper(), font=fonte("semi", 32), fill=self.cor("destaque"), anchor="mm")
        tam = 76
        while tam > 44:
            linhas = quebrar(d, c.get("texto", ""), fonte("bold", tam), self.W - 400)
            if len(linhas) * (tam + 18) <= 420:
                break
            tam -= 4
        y = 590 - len(linhas) * (tam + 18) / 2
        d.rectangle([self.W / 2 - 60, y - 50, self.W / 2 + 60, y - 44], fill=self.cor("destaque"))
        for ln in linhas:
            d.text((self.W / 2, y + tam / 2), ln, font=fonte("bold", tam), fill=self.cor("texto"), anchor="mm")
            y += tam + 18

    def c_ficha(self, d, c, estado, im):
        self.titulo(d, c.get("titulo") or "Ficha técnica")
        dados = self.rot.get("dados") or {}
        cartoes = [("Estrelas", fmt_estrelas(dados.get("estrelas"))),
                   ("Linguagem", dados.get("linguagem") or "—"),
                   ("Licença", dados.get("licenca") or "não informada"),
                   ("Criado em", fmt_data(dados.get("criado_em"))),
                   ("Último commit", fmt_data(dados.get("ultimo_push"))),
                   ("Forks", fmt_estrelas(dados.get("forks")))]
        larg = (self.W - 280 - 2 * 40) / 3
        for i, (rot_, val) in enumerate(cartoes):
            x = 140 + (i % 3) * (larg + 40)
            y = 290 + (i // 3) * 300
            d.rounded_rectangle([x, y, x + larg, y + 260], radius=26, fill=self.cor("painel"),
                                outline=self.cor("borda"), width=2)
            d.text((x + 40, y + 50), rot_.upper(), font=fonte("semi", 28), fill=self.cor("suave"))
            tam = 66
            while d.textlength(str(val), font=fonte("bold", tam)) > larg - 80 and tam > 34:
                tam -= 4
            d.text((x + 40, y + 120), str(val), font=fonte("bold", tam), fill=self.cor("texto"))

    # ── capa ──
    def capa(self):
        r = self.rot
        p = Pintor(r, self.cfg, 1280, 720)
        im = p.fundo()
        d = p.ImageDraw.Draw(im, "RGBA")
        d.rounded_rectangle([60, 60, 330, 210], radius=28, fill=p.cor("destaque"))
        d.text((195, 135), f"#{r.get('rank')}", font=fonte("bold", 104), fill=p.cor("fundo"), anchor="mm")
        p.pilula(d, 360, 100, f"{fmt_estrelas((r.get('dados') or {}).get('estrelas'))} estrelas",
                 fonte("bold", 40), p.cor("texto"), p.cor("painel"), estrela=True)
        p.estrela(d, 1110, 560, 230, p.cor("alerta", 38))          # estrela grande decorativa
        p.estrela(d, 1110, 560, 120, p.cor("alerta", 70))
        capa = r.get("capa") or {}
        tam = 118
        while tam > 76:
            l1 = quebrar(d, capa.get("linha1", "").upper(), fonte("bold", tam), 1120)
            if len(l1) <= 2:
                break
            tam -= 6
        y = 250
        for ln in l1[:2]:
            d.text((60, y), ln, font=fonte("bold", tam), fill=p.cor("destaque2"))
            y += tam + 10
        d.rectangle([62, y + 20, 262, y + 30], fill=p.cor("alerta"))
        y += 54
        for ln in quebrar(d, capa.get("linha2", ""), fonte("bold", 66), 1100)[:2]:
            d.text((60, y), ln, font=fonte("bold", 66), fill=p.cor("texto"))
            y += 78
        d.text((60, 670), r["repo"], font=fonte("semi", 34), fill=p.cor("suave"), anchor="lm")
        return im


# ───────────────────────────── montagem ─────────────────────────────

def linha_tempo(rot, cfg, pasta, sem_voz):
    """Gera a narração de cada fala e calcula quando cada uma começa e termina."""
    pasta.mkdir(parents=True, exist_ok=True)
    t = 0.0
    cenas, trechos = [], []
    for i, c in enumerate(rot["cenas"]):
        inicio = t
        t += ENTRADA_CENA + (0.35 if i == 0 else 0)
        falas = []
        for j, f in enumerate(norm_falas(c["falas"])):
            texto = f["falado"] or f["texto"]
            pcm = silencio_estimado(texto) if sem_voz else narrar(texto, pasta / f"f{i:02d}_{j:02d}.mp3", cfg)
            dur = len(pcm) / 2 / SR
            falas.append({**f, "ini": t, "fim": t + dur})
            trechos.append((t, pcm))
            t += dur + PAUSA_FALA
        t += SAIDA_CENA
        cenas.append({"ini": inicio, "fim": t, "falas": falas})
    total = t + 0.6
    amostras = bytearray(int(total * SR) * 2)
    for ini, pcm in trechos:
        k = int(ini * SR) * 2
        amostras[k:k + len(pcm)] = pcm
    with wave.open(str(pasta / "narracao.wav"), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(bytes(amostras))
    cenas[-1]["fim"] = total
    return cenas, total


def eventos_cena(c, info):
    """Quando cada item da cena aparece: lista de (instante, quantidade de itens visíveis)."""
    n = len(itens_da_cena(c))
    falas = info["falas"]
    if c["tipo"] in ("abertura", "destaque", "ficha") or n == 0:
        return [(info["ini"], 0)]
    vis = []
    explicito = any(f.get("mostra") is not None for f in falas)
    for j, f in enumerate(falas):
        if explicito:
            if f.get("mostra") is not None:
                vis.append((f["ini"] - 0.15, f["mostra"] + 1))
        elif j < n:
            vis.append((f["ini"] - 0.15, j + 1))
    if not explicito and n > len(falas):
        vis.append((falas[-1]["ini"] + 0.6, n))
    out, atual = [(info["ini"], 0)], 0
    for tt, k in sorted(vis):
        k = max(k, atual)
        if k != atual:
            out.append((max(tt, out[-1][0] + 0.3), k))
            atual = k
    if c["tipo"] == "encerramento" and atual < n + 1:
        out.append((max(falas[-1]["ini"], out[-1][0] + 0.3), n + 1))   # cartão do próximo episódio
    return out


def encode_segmento(destino, prev, atual, frames, trans):
    """Um arquivo por segmento: transição (quadros gerados) + o quadro final parado."""
    trans = min(trans, frames) if prev is not None else 0
    parado = frames - trans
    png = destino.with_suffix(".png")
    atual.save(png)
    tmp = destino.with_name(destino.stem + ".tmp.mp4")
    enc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS)]
    if trans:
        from PIL import Image
        dados = b"".join(Image.blend(prev, atual, (k + 1) / (trans + 1)).tobytes() for k in range(trans))
        filtro = (f"[0:v]setsar=1[t];[1:v]format=rgb24,loop=-1:1,trim=end_frame={max(parado, 1)},"
                  f"setpts=N/{FPS}/TB,setsar=1[h];[t][h]concat=n=2:v=1,format=yuv420p[v]")
        cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
               "-r", str(FPS), "-i", "pipe:0", "-framerate", str(FPS), "-i", str(png),
               "-filter_complex", filtro, "-map", "[v]", "-frames:v", str(frames)] + enc + [str(tmp)]
        rodar(cmd, entrada=dados)
    else:
        cmd = ["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(png), "-vf",
               f"format=yuv420p,loop=-1:1,trim=end_frame={frames},setpts=N/{FPS}/TB",
               "-frames:v", str(frames)] + enc + [str(tmp)]
        rodar(cmd)
    tmp.rename(destino)
    png.unlink()


def legendas(cenas):
    """Divide cada fala em trechos curtos (até 2 linhas), com tempo proporcional ao tamanho."""
    blocos = []
    for c in cenas:
        for f in c["falas"]:
            palavras = f["texto"].split()
            trechos, atual = [], []
            for p in palavras:
                if len(" ".join(atual + [p])) > 74 and atual:
                    trechos.append(" ".join(atual))
                    atual = []
                atual.append(p)
            if atual:
                trechos.append(" ".join(atual))
            total = sum(len(x) for x in trechos) or 1
            t = f["ini"]
            for x in trechos:
                d = (f["fim"] - f["ini"]) * len(x) / total
                blocos.append((t, t + d, x))
                t += d
    return blocos


def quebra_legenda(texto, limite=40):
    if len(texto) <= limite:
        return [texto]
    meio = len(texto) // 2
    esp = [i for i, ch in enumerate(texto) if ch == " "]
    k = min(esp, key=lambda i: abs(i - meio)) if esp else meio
    return [texto[:k].strip(), texto[k:].strip()]


def ts_srt(s):
    ms = int(round(s * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def ts_ass(s):
    cs = int(round(s * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def escrever_legendas(blocos, pasta):
    srt, ass = [], [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 2", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
        "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding",
        # BorderStyle 4 = uma caixa só por legenda (libass 0.17+)
        "Style: Legenda,Inter SemiBold,44,&H00FFFFFF,&H00FFFFFF,&H00000000,&H28000000,0,0,0,0,100,100,0,0,4,16,0,2,"
        "160,160,52,1", "",
        "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for i, (a, b, txt) in enumerate(blocos, 1):
        linhas = quebra_legenda(txt)
        srt += [str(i), f"{ts_srt(a)} --> {ts_srt(b)}", *linhas, ""]
        texto_ass = "\\N".join(linhas)
        ass.append(f"Dialogue: 0,{ts_ass(a)},{ts_ass(b)},Legenda,,0,0,0,,{texto_ass}")
    (pasta / "legendas.srt").write_text("\n".join(srt), encoding="utf-8")
    (pasta / "legendas.ass").write_text("\n".join(ass) + "\n", encoding="utf-8")


def capitulos(rot, cenas):
    nomes = {"abertura": "Abertura", "ficha": "Ficha técnica", "encerramento": "Resumo"}
    caps = []
    for c, info in zip(rot["cenas"], cenas):
        nome = c.get("capitulo") or ("Abertura" if c["tipo"] == "abertura" else c.get("titulo")) \
            or nomes.get(c["tipo"], c["tipo"])
        ini = 0 if not caps else int(info["ini"])
        if caps and ini - caps[-1][0] < 10:            # o YouTube exige 10 s por capítulo
            continue
        caps.append((ini, nome))
    return caps


def descricao_final(rot, caps, duracao):
    dados = rot.get("dados") or {}
    linhas = [rot["descricao_youtube"].strip(), "",
              f"🔗 Repositório: https://github.com/{rot['repo']}",
              f"⭐ {fmt_estrelas(dados.get('estrelas'))} estrelas no GitHub em {fmt_data(rot.get('gerado_em'))} "
              f"({rot.get('rank')}º entre {rot.get('total_fila')} repositórios de IA)",
              f"📋 Ranking completo: https://github.com/{REPO}/blob/main/CATALOGO.md", ""]
    if len(caps) >= 3:
        linhas += ["Capítulos"] + [f"{fmt_tempo(t)} {n}" for t, n in caps] + [""]
    linhas += ["Narração com voz sintética. Roteiro feito com ajuda de IA a partir do repositório e da "
               "documentação oficial; confira o projeto antes de usar em produção.", "",
               " ".join("#" + re.sub(r"[^\w]", "", t) for t in rot.get("tags", [])[:3])]
    return "\n".join(linhas)


def renderizar_um(arq, cfg, sem_voz=False):
    rot = ler_json(arq)
    pasta = DIR_SAIDA / Path(arq).stem
    tmp = pasta / "tmp"
    if pasta.exists():
        shutil.rmtree(pasta)
    tmp.mkdir(parents=True)
    log(f"Renderizando {Path(arq).name}: narração…")
    cenas, total = linha_tempo(rot, cfg, tmp, sem_voz)
    pintor = Pintor(rot, cfg)
    lista, prev, n_seg = [], None, 0
    log(f"Narração com {fmt_tempo(total)}; desenhando {len(cenas)} cenas…")
    for i, (c, info) in enumerate(zip(rot["cenas"], cenas)):
        evs = eventos_cena(c, info)
        for k, (t0, estado) in enumerate(evs):
            t1 = evs[k + 1][0] if k + 1 < len(evs) else info["fim"]
            f0, f1 = round(t0 * FPS), round(t1 * FPS)
            if f1 - f0 <= 0:
                continue
            img = pintor.desenhar(c, i, len(cenas), estado)
            seg = tmp / f"s{n_seg:03d}.mp4"
            encode_segmento(seg, prev, img, f1 - f0, 12 if k == 0 else 8)
            lista.append(seg)
            prev, n_seg = img, n_seg + 1
    (tmp / "lista.txt").write_text("".join(f"file '{p.name}'\n" for p in lista))
    rodar(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "lista.txt"),
           "-c", "copy", str(tmp / "base.mp4")])
    escrever_legendas(legendas(cenas), pasta)
    fontsdir = next((str(Path(p).parent) for p in FONTES["semi"] if Path(p).exists()), "/usr/share/fonts")
    final = pasta / "video.tmp.mp4"
    rodar(["ffmpeg", "-y", "-v", "error", "-i", str(tmp / "base.mp4"), "-i", str(tmp / "narracao.wav"),
           "-vf", f"ass={pasta / 'legendas.ass'}:fontsdir={fontsdir}", "-map", "0:v", "-map", "1:a",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-shortest", str(final)])
    final.rename(pasta / "video.mp4")
    pintor.capa().convert("RGB").save(pasta / "capa.jpg", quality=92)
    dur = float(rodar(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                       str(pasta / "video.mp4")]).decode().strip())
    caps = capitulos(rot, cenas)
    meta = {"arquivo": str(Path(arq).relative_to(RAIZ)) if Path(arq).is_absolute() else str(arq),
            "repo": rot["repo"], "episodio": rot["episodio"], "titulo": rot["titulo_youtube"],
            "descricao": descricao_final(rot, caps, dur), "tags": rot.get("tags", []),
            "duracao": round(dur, 1), "capitulos": caps,
            "tamanho_mb": round((pasta / "video.mp4").stat().st_size / 1e6, 1)}
    salvar_json(pasta / "meta.json", meta)
    if not sem_voz:
        shutil.rmtree(tmp)
    log(f"Pronto: {pasta / 'video.mp4'} — {fmt_tempo(dur)}, {meta['tamanho_mb']} MB, {len(lista)} segmentos.")
    return pasta


def renderizar(arquivos, cfg, sem_voz=False):
    if not arquivos:
        prod = ler_json(ARQ_PROD, {})
        arquivos = [RAIZ / p["arquivo"] for p in sorted(prod.values(), key=lambda p: p["episodio"])
                    if p.get("status") == "roteiro"]
    if not arquivos:
        log("Nenhum roteiro pendente.")
    for a in arquivos:
        renderizar_um(Path(a), cfg, sem_voz)


# ───────────────────────────── publicação (Actions) ─────────────────────────────

def gh(*args):
    return rodar(["gh", *args]).decode().strip()


def publicar():
    prod = ler_json(ARQ_PROD, {})
    for meta_arq in sorted(DIR_SAIDA.glob("*/meta.json")):
        meta = ler_json(meta_arq)
        pasta = meta_arq.parent
        ep = meta["episodio"]
        tag = f"video-{ep:03d}"
        (pasta / "descricao.txt").write_text(meta["descricao"], encoding="utf-8")
        notas = (f"**{meta['titulo']}**\n\nDuração: {fmt_tempo(meta['duracao'])} · {meta['tamanho_mb']} MB\n\n"
                 f"Título, descrição e tags estão na issue do episódio.")
        (pasta / "notas.md").write_text(notas, encoding="utf-8")
        arquivos = [str(pasta / x) for x in ("video.mp4", "capa.jpg", "legendas.srt", "descricao.txt")]
        try:
            gh("release", "view", tag)
            gh("release", "upload", tag, *arquivos, "--clobber")
        except RuntimeError:
            gh("release", "create", tag, *arquivos, "--title", f"#{ep:03d} — {meta['titulo']}",
               "--notes-file", str(pasta / "notas.md"))
        base = f"https://github.com/{REPO}/releases/download/{tag}"
        corpo = "\n".join([
            f"## 🎬 Episódio #{ep} — {meta['repo']}",
            f"Duração **{fmt_tempo(meta['duracao'])}** · {meta['tamanho_mb']} MB", "",
            f"**Baixar:** [vídeo (mp4)]({base}/video.mp4) · [capa]({base}/capa.jpg) · "
            f"[legendas .srt]({base}/legendas.srt) (opcional: o vídeo já tem legenda na tela)", "",
            "🤖 Com a postagem automática configurada, o episódio sobe sozinho para o YouTube e esta issue "
            "fecha com o link. Sem ela, poste manualmente:",
            "1. Baixe o vídeo.",
            "2. No YouTube Studio, toque em **+ → Enviar vídeo** e escolha o arquivo.",
            "3. Cole o título e a descrição abaixo. Em **Miniatura**, use a capa.",
            "4. Publique na hora ou agende. Depois feche esta issue.", "",
            "### Título", "```", meta["titulo"], "```",
            "### Descrição", "```", meta["descricao"], "```",
            "### Tags", "```", ", ".join(meta["tags"]), "```"])
        (pasta / "issue.md").write_text(corpo, encoding="utf-8")
        try:
            gh("label", "create", "video-pronto", "--color", "7C9CFF", "--description", "Vídeo pronto para postar",
               "--force")
        except RuntimeError:
            pass
        titulo = f"🎬 Vídeo #{ep} pronto — {meta['titulo']}"
        existentes = json.loads(gh("issue", "list", "--label", "video-pronto", "--state", "all", "--limit", "200",
                                   "--json", "number,title,url") or "[]")
        antiga = next((x for x in existentes if x["title"].startswith(f"🎬 Vídeo #{ep} pronto")), None)
        if antiga:                                   # episódio refeito: atualiza a mesma issue
            gh("issue", "edit", str(antiga["number"]), "--title", titulo, "--body-file", str(pasta / "issue.md"))
            gh("issue", "reopen", str(antiga["number"]))
            url = antiga["url"]
        else:
            url = gh("issue", "create", "--title", titulo, "--body-file", str(pasta / "issue.md"),
                     "--label", "video-pronto")
        log(f"Episódio {ep}: release {tag} e issue {url}")
        if meta["repo"] in prod:
            prod[meta["repo"]].update({"status": "pronto", "release": f"https://github.com/{REPO}/releases/tag/{tag}",
                                       "issue": url, "duracao": meta["duracao"], "renderizado_em": HOJE})
        salvar_json(ARQ_PROD, prod)


# ───────────────────────────── postagem no YouTube (Actions) ─────────────────────────────
# Precisa dos secrets YT_CLIENT_ID, YT_CLIENT_SECRET e YT_REFRESH_TOKEN (escopo youtube.upload).
# Sem eles, nada é postado e a issue continua com o passo a passo manual.

def _yt_req(url, metodo="GET", corpo=None, cab=None, timeout=60):
    req = urllib.request.Request(url, data=corpo, method=metodo, headers=cab or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, dict(r.headers), r.read()


def token_youtube():
    cid, seg, ref = (os.environ.get(k, "").strip() for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN"))
    if not (cid and seg and ref):
        return None
    corpo = urllib.parse.urlencode({"client_id": cid, "client_secret": seg, "refresh_token": ref,
                                    "grant_type": "refresh_token"}).encode()
    try:
        _, _, r = _yt_req("https://oauth2.googleapis.com/token", "POST", corpo,
                          {"Content-Type": "application/x-www-form-urlencoded"}, 30)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"o Google recusou o token ({e.code}: {e.read()[:200]!r}). Se for invalid_grant, "
                           "gere um refresh token novo e atualize o secret YT_REFRESH_TOKEN.") from e
    return json.loads(r)["access_token"]


DIAS_SEMANA = {"seg": 0, "ter": 1, "qua": 2, "qui": 3, "sex": 4, "sab": 5, "sáb": 5, "dom": 6}


def proximo_horario(cfg, prod):
    """Próximo horário livre de publicação: um episódio por dia de postagem, no horário do config."""
    tz = ZoneInfo("America/Sao_Paulo")
    post = cfg.get("postagem") or {}
    h, m = (int(x) for x in str(post.get("horario", "18:00")).split(":"))
    dias = {DIAS_SEMANA[str(d).lower()[:3]] for d in post.get("dias", ["seg", "qua", "sex"])} or set(range(7))
    agora = dt.datetime.now(tz)
    ocupados = {dt.datetime.fromisoformat(p["agendado_para"]).astimezone(tz).date()
                for p in prod.values() if p.get("agendado_para")}
    ultimo = max(ocupados) if ocupados else None
    alvo = agora.replace(hour=h, minute=m, second=0, microsecond=0)
    if alvo < agora + dt.timedelta(minutes=20):
        alvo += dt.timedelta(days=1)
    while alvo.weekday() not in dias or (ultimo and alvo.date() <= ultimo):
        alvo += dt.timedelta(days=1)
    return alvo


def enviar_video(token, caminho, meta, publicar_em):
    status = {"privacyStatus": "private", "publishAt": publicar_em.astimezone(dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"), "selfDeclaredMadeForKids": False} if publicar_em else \
        {"privacyStatus": "public", "selfDeclaredMadeForKids": False}
    corpo = {"snippet": {"title": meta["titulo"][:100], "description": meta["descricao"][:5000],
                         "tags": meta.get("tags", []), "categoryId": "28", "defaultLanguage": "pt-BR",
                         "defaultAudioLanguage": "pt-BR"},
             "status": status}
    tamanho = Path(caminho).stat().st_size
    _, cab, _ = _yt_req("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                        "POST", json.dumps(corpo).encode(),
                        {"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8",
                         "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(tamanho)})
    destino = cab.get("Location") or cab.get("location")
    _, _, r = _yt_req(destino, "PUT", Path(caminho).read_bytes(),
                      {"Authorization": f"Bearer {token}", "Content-Type": "video/mp4"}, timeout=900)
    return json.loads(r)["id"]


def enviar_capa(token, video_id, capa):
    try:
        _yt_req(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={video_id}&uploadType=media",
                "POST", Path(capa).read_bytes(), {"Authorization": f"Bearer {token}", "Content-Type": "image/jpeg"})
        return True
    except urllib.error.HTTPError as e:
        log(f"Capa não enviada ({e.code}). Capa personalizada exige o canal verificado por telefone.")
        return False


def reaplicar_capas(token, prod):
    """Tenta de novo a capa dos vídeos já enviados sem ela (funciona quando o canal for verificado)."""
    pendentes = [p for p in prod.values() if p.get("youtube_id") and not p.get("capa_ok")]
    for p in sorted(pendentes, key=lambda p: p["episodio"]):
        pasta = DIR_SAIDA / Path(p["arquivo"]).stem
        if not (pasta / "capa.jpg").exists():
            pasta.mkdir(parents=True, exist_ok=True)
            try:
                gh("release", "download", f"video-{p['episodio']:03d}", "-p", "capa.jpg", "-D", str(pasta), "--clobber")
            except RuntimeError:
                continue
        if enviar_capa(token, p["youtube_id"], pasta / "capa.jpg"):
            p["capa_ok"] = True
            salvar_json(ARQ_PROD, prod)
            log(f"Capa aplicada no episódio {p['episodio']}.")
        else:
            break                                       # canal ainda não verificado: tenta no próximo dia


def postar(cfg):
    if not (cfg.get("postagem") or {}).get("ativa", False):
        log("Postagem automática desligada no config-videos.yml.")
        return
    token = token_youtube()
    if not token:
        log("Sem os secrets YT_CLIENT_ID / YT_CLIENT_SECRET / YT_REFRESH_TOKEN: postagem fica manual.")
        return
    prod = ler_json(ARQ_PROD, {})
    reaplicar_capas(token, prod)
    fila_post = sorted((p for p in prod.values() if p.get("status") == "pronto" and not p.get("youtube_id")),
                       key=lambda p: p["episodio"])
    if not fila_post:
        log("Nada para postar.")
        return
    for p in fila_post:
        pasta = DIR_SAIDA / Path(p["arquivo"]).stem
        tag = f"video-{p['episodio']:03d}"
        if not (pasta / "video.mp4").exists() or not (pasta / "meta.json").exists():
            pasta.mkdir(parents=True, exist_ok=True)
            gh("release", "download", tag, "-p", "video.mp4", "-p", "capa.jpg", "-D", str(pasta), "--clobber")
        meta = ler_json(pasta / "meta.json") or {}
        if not meta:                                      # episódio renderizado em outro dia: refaz o meta do release
            rot = ler_json(RAIZ / p["arquivo"])
            corpo_rel = json.loads(gh("release", "view", tag, "--json", "assets"))
            if any(a["name"] == "descricao.txt" for a in corpo_rel.get("assets", [])):
                gh("release", "download", tag, "-p", "descricao.txt", "-D", str(pasta), "--clobber")
            meta = {"titulo": rot["titulo_youtube"], "tags": rot.get("tags", []),
                    "descricao": (pasta / "descricao.txt").read_text(encoding="utf-8")
                    if (pasta / "descricao.txt").exists() else rot["descricao_youtube"]}
        quando = proximo_horario(cfg, prod)
        vid = enviar_video(token, pasta / "video.mp4", meta, quando)
        capa_ok = enviar_capa(token, vid, pasta / "capa.jpg") if (pasta / "capa.jpg").exists() else False
        p.update({"status": "agendado", "youtube_id": vid, "youtube": f"https://youtu.be/{vid}",
                  "agendado_para": quando.isoformat(), "postado_em": HOJE, "capa_ok": capa_ok})
        salvar_json(ARQ_PROD, prod)
        quando_txt = quando.strftime("%d/%m às %H:%M")
        log(f"Episódio {p['episodio']} enviado: https://youtu.be/{vid} — público em {quando_txt}")
        if p.get("issue"):
            num = p["issue"].rstrip("/").split("/")[-1]
            aviso = (f"✅ **Postado automaticamente:** https://youtu.be/{vid}\n\n"
                     f"Fica **público em {quando_txt}** (horário de Brasília). Até lá está agendado e só você vê no "
                     f"YouTube Studio; se quiser segurar, troque para privado por lá."
                     + ("" if capa_ok else "\n\n⚠️ A capa não foi aplicada: no YouTube, capa personalizada exige "
                        "verificar o canal por telefone (youtube.com/verify). Depois disso, suba a capa do "
                        "release pelo Studio."))
            gh("issue", "comment", num, "--body", aviso)
            gh("issue", "close", num)


# ───────────────────────────── main ─────────────────────────────

def main():
    global HOJE
    ap = argparse.ArgumentParser(description="Vídeos do Radar de IA")
    ap.add_argument("comando", choices=["proximo", "salvar", "disparar", "renderizar", "publicar", "postar",
                                        "quadros"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--repo", help="proximo: força um repositório da fila")
    ap.add_argument("--sem-voz", action="store_true", help="renderizar sem narração (teste local)")
    ap.add_argument("--data")
    a = ap.parse_args()
    if a.data:
        HOJE = a.data
    cfg = ler_cfg()
    if a.comando == "proximo":
        proximo(cfg, a.repo)
    elif a.comando == "salvar":
        salvar(a.args[0] if a.args else DIR_TMP / "video_roteiro.json", cfg)
    elif a.comando == "disparar":
        disparar()
    elif a.comando == "renderizar":
        renderizar(a.args, cfg, a.sem_voz)
    elif a.comando == "publicar":
        publicar()
    elif a.comando == "postar":
        postar(cfg)
    elif a.comando == "quadros":                     # prévia: um quadro por estado de cada cena
        rot = ler_json(a.args[0])
        pasta = Path(a.args[1] if len(a.args) > 1 else DIR_TMP / "quadros")
        pasta.mkdir(parents=True, exist_ok=True)
        p = Pintor(rot, cfg)
        for i, c in enumerate(rot["cenas"]):
            n = len(itens_da_cena(c)) + (1 if c["tipo"] == "encerramento" else 0)
            p.desenhar(c, i, len(rot["cenas"]), n).convert("RGB").save(pasta / f"cena{i + 1:02d}.jpg", quality=90)
        p.capa().convert("RGB").save(pasta / "capa.jpg", quality=90)
        log(f"Quadros em {pasta}")


if __name__ == "__main__":
    main()
