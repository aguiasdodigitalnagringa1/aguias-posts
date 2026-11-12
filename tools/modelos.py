"""Modelos de post por série (padrão a partir de 19/11/2026).

Cada função devolve o HTML completo de UM slide (1080x1350) ou de UMA cena de Reel (1080x1920).
Use em specs com "raw": true — o render.py/reel.py então não aplica a moldura antiga.
Placeholders trocados na renderização: {{LOGO}}, {{N}} (nº do slide/cena), {{T}} (total).

Séries de carrossel/imagem (12:00):
  A tutorial  · Tutorial com tela   — passo a passo com ilustração de tela (anúncio, painel, lista)
  B errado    · Errado x Certo      — comparação lado a lado
  C metrica   · Métrica da semana   — uma métrica em destaque, fórmula e leitura
  D checklist · Checklist (claro)   — fundo creme, título serifado, itens numerados
  E mito      · Mito x Verdade      — metade escura (mito) / metade laranja (verdade)
  F frase     · Frase de domingo    — imagem única, tipografia editorial
Séries de Reel (19:00):
  G tela      · Reel com tela de celular (escuro)
  H lista     · Reel em lista (claro), itens aparecendo um a um
  R rosto     · Reel gravado pelo dono (roteiro escrito por nós; ver PROCESSO.md)
"""
import base64, pathlib

_F = "/usr/share/fonts/truetype/google-fonts/"
_LORA = base64.b64encode(pathlib.Path(_F + "Lora-Variable.ttf").read_bytes()).decode()
_LORAI = base64.b64encode(pathlib.Path(_F + "Lora-Italic-Variable.ttf").read_bytes()).decode()

OR, OR_D, CREAM = "#FF7A1A", "#D9620B", "#F5F0E8"

CSS = f"""
@font-face{{font-family:Ser;src:url(data:font/ttf;base64,{_LORA}) format('truetype');font-weight:400 700}}
@font-face{{font-family:Ser;font-style:italic;src:url(data:font/ttf;base64,{_LORAI}) format('truetype');font-weight:400 700}}
body{{width:auto;height:auto}}
.pg{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#0B0B0C;color:#F4F1EC}}
.pg.lt{{background:{CREAM};color:#141414}}
.pg.lt p,.rl.lt p{{color:#3a3a3a}} .pg.lt p b,.rl.lt p b{{color:#141414}}
.rl{{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(1000px 900px at 80% 8%,rgba(255,122,26,.24),transparent 60%),#070707;color:#F4F1EC}}
.rl.lt{{background:{CREAM};color:#141414}}
.hdr{{position:absolute;z-index:5;top:64px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:center;font-family:Pop;font-weight:700;font-size:24px;letter-spacing:1px}}
.hdr .b{{display:flex;align-items:center;gap:14px}} .hdr img{{width:52px;height:52px;border-radius:50%}}
.hdr .sr{{opacity:.6}}
.ftr{{position:absolute;z-index:5;bottom:60px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:24px;color:#8a8a8a}}
.ftr .sw{{color:{OR};font-family:Pop;font-weight:700}} .lt .ftr .sw{{color:{OR_D}}}
.in{{position:absolute;top:180px;left:80px;right:80px;bottom:140px;display:flex;flex-direction:column;justify-content:center}}
.tag{{display:inline-block;align-self:flex-start;padding:10px 22px;border-radius:999px;font-family:Pop;font-weight:700;font-size:24px;letter-spacing:2px;text-transform:uppercase;background:{OR};color:#120800}}
.tag.ln{{background:none;border:2px solid {OR};color:{OR}}}
.h{{font-family:Pop;font-weight:800;font-size:66px;line-height:1.08;letter-spacing:-1px;margin:28px 0 40px}}
.hc{{font-family:Pop;font-weight:900;font-size:104px;line-height:1.02;letter-spacing:-2px;margin:30px 0 36px}}
.ser{{font-family:Ser;font-weight:600;letter-spacing:-1.5px}} .ser i{{color:{OR_D}}}
.card{{background:#fff;border-radius:28px;padding:40px 46px;color:#202124;font-family:Int;box-shadow:0 30px 80px rgba(0,0,0,.55)}}
.hl{{outline:4px dashed {OR};outline-offset:8px;border-radius:12px}}
.cmp{{display:grid;grid-template-columns:1fr 1fr;gap:28px}}
.cmp>div{{border-radius:28px;padding:40px}}
.bad{{background:rgba(255,70,70,.08);border:2px solid #ff5a5a}} .good{{background:rgba(60,200,120,.08);border:2px solid #3cc878}}
.cmp .l{{font-family:Pop;font-weight:800;font-size:32px;margin-bottom:24px}} .bad .l{{color:#ff6b6b}} .good .l{{color:#4fdc8c}}
.cmp .m{{font-family:Pop;font-weight:700;font-size:42px;line-height:1.2;margin-bottom:20px}}
.cmp p{{font-size:32px}}
.big{{font-family:Pop;font-weight:900;line-height:1;color:{OR};text-shadow:0 0 60px rgba(255,122,26,.5)}}
.fx{{display:inline-flex;align-self:center;align-items:center;gap:24px;padding:34px 48px;border-radius:28px;background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.12);font-family:Pop;font-weight:700;font-size:42px}}
.fx i{{font-style:normal;color:{OR}}}
.dl{{display:flex;flex-direction:column;gap:26px}}
.di{{display:flex;gap:28px;align-items:flex-start;background:#fff;border-radius:26px;padding:34px 38px;box-shadow:0 14px 40px rgba(0,0,0,.06)}}
.di .n{{font-family:Pop;font-weight:900;font-size:64px;line-height:1;color:{OR_D};min-width:56px}}
.di .t{{font-family:Pop;font-weight:700;font-size:40px;line-height:1.2;color:#141414}}
.di p{{font-size:32px;margin-top:10px}}
.di.off{{opacity:.3}}
.ctab{{display:inline-block;margin-top:44px;padding:30px 56px;border-radius:999px;background:{OR};color:#120800;font-family:Pop;font-weight:800;font-size:40px;box-shadow:0 0 50px rgba(255,122,26,.45)}}
.lt .ctab{{background:#141414;color:{CREAM};box-shadow:none}}
.phone{{position:relative;width:720px;margin:0 auto;border-radius:70px;background:#121212;border:10px solid #2a2a2a;box-shadow:0 40px 120px rgba(0,0,0,.7);padding:64px 40px 56px}}
.kp{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.kp>div{{background:#1c1c1c;border-radius:22px;padding:24px 26px}}
.kp .k{{font-size:24px;color:#9a9a9a}} .kp .v{{font-family:Pop;font-weight:800;font-size:44px;margin-top:6px}}
.kp .on{{border:3px solid {OR}}} .kp .on .v{{color:{OR}}}
.cap{{position:absolute;z-index:6;left:90px;right:90px;bottom:300px;text-align:center;font-family:Pop;font-weight:800;font-size:52px;line-height:1.2;background:rgba(0,0,0,.65);padding:26px 30px;border-radius:22px}}
.rbar{{position:absolute;z-index:6;left:90px;right:90px;bottom:200px;display:flex;gap:12px}}
.rbar i{{flex:1;height:8px;border-radius:8px;background:rgba(127,127,127,.25)}} .rbar i.on{{background:{OR}}}
.lt .rbar i.on{{background:{OR_D}}}
"""

HTML_HEAD = "<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


# ---------- moldura comum ----------
def _hdr(serie, lt=False):
    return (f"<div class='hdr'><div class='b'><img src='{{{{LOGO}}}}'>ÁGUIAS DO DIGITAL</div>"
            f"<div class='sr'>{serie} · {{{{N}}}}/{{{{T}}}}</div></div>")


def _ftr(swipe=True):
    sw = "<span class='sw'>Arrasta →</span>" if swipe else "<span></span>"
    return f"<div class='ftr'><span>@aguiasdodigitalads</span>{sw}</div>"


def slide(serie, inner, lt=False, swipe=True, bg=""):
    cls = "pg lt" if lt else "pg"
    st = f" style='{bg}'" if bg else ""
    return f"<div class='{cls}'{st}>{_hdr(serie, lt)}<div class='in'>{inner}</div>{_ftr(swipe)}</div>"


def cta(serie, lt=False, titulo="Quer aprender o <span class='o'>passo a passo</span>?"):
    t = titulo.replace("class='o'", "style='color:#D9620B'") if lt else titulo
    inner = ("<div style='display:flex;flex-direction:column;align-items:center;text-align:center'>"
             "<img src='{{LOGO}}' style='width:300px;height:300px;border-radius:50%;box-shadow:0 0 70px rgba(255,122,26,.4);margin-bottom:50px'>"
             f"<div class='h' style='margin:0 0 24px'>{t}</div>"
             "<p>Na comunidade <b>Águias do Digital</b> você aprende com quem roda campanhas todos os dias.</p>"
             "<span class='ctab'>Link na bio</span>"
             "<p style='margin-top:36px;font-size:30px;opacity:.7'>Salva este post para consultar depois</p></div>")
    return slide(serie, inner, lt=lt, swipe=False)


# ---------- ilustrações de tela (genéricas, sem marcas reais) ----------
def tela_anuncio(titulo="Título do anúncio | Benefício principal",
                 desc="Descrição com a ideia da busca e uma chamada para ação clara.",
                 site="www.exemplo-produto.com", sitelinks=None, destaque=""):
    """destaque: 'titulo', 'desc', 'url' ou 'sitelinks' recebe contorno laranja."""
    h = lambda k: " hl" if destaque == k else ""
    sl = ""
    if sitelinks:
        cells = "".join(f"<span>{s}</span>" for s in sitelinks)
        sl = (f"<div class='{h('sitelinks')}' style='margin-top:24px;padding:18px 4px;display:grid;grid-template-columns:1fr 1fr;"
              f"gap:12px;font-size:28px;color:#1a0dab'>{cells}</div>")
    return ("<div class='card'>"
            f"<div class='{h('url')}' style='display:flex;align-items:center;gap:16px;font-size:24px;color:#5f6368'>"
            "<div style='width:42px;height:42px;border-radius:50%;background:#e8eaed'></div>"
            f"<div><b style='color:#202124'>Patrocinado</b><br>{site}</div></div>"
            f"<div class='{h('titulo')}' style='font-size:38px;color:#1a0dab;margin:20px 0 10px;line-height:1.25'>{titulo}</div>"
            f"<div class='{h('desc')}' style='font-size:27px;color:#4d5156;line-height:1.45'>{desc}</div>{sl}</div>")


def tela_tabela(cols, linhas, destaque_linha=None, titulo="Ilustração · valores fictícios"):
    """Tabela estilo painel (ex.: termos de pesquisa, palavras-chave). linhas = listas de células."""
    th = "".join(f"<th style='text-align:left;padding:14px 12px;font-weight:600;color:#5f6368;font-size:24px'>{c}</th>" for c in cols)
    rows = ""
    for i, l in enumerate(linhas):
        bg = "background:#FFF1E6;outline:3px solid #FF7A1A;" if i == destaque_linha else ""
        tds = "".join(f"<td style='padding:16px 12px;border-top:1px solid #eee;font-size:27px;color:#202124'>{c}</td>" for c in l)
        rows += f"<tr style='{bg}'>{tds}</tr>"
    return (f"<div class='card' style='padding:30px 30px 22px'><table style='width:100%;border-collapse:collapse'>"
            f"<tr>{th}</tr>{rows}</table><div style='margin-top:14px;font-size:22px;color:#9aa0a6'>{titulo}</div></div>")


# ---------- A · Tutorial com tela ----------
def a_capa(titulo, sub, tela=""):
    t = f"<div style='margin-top:10px'>{tela}</div>" if tela else ""
    return slide("TUTORIAL", f"<span class='tag'>Tutorial</span><div class='hc' style='font-size:92px'>{titulo}</div><p>{sub}</p>{t}")


def a_passo(n, titulo, tela, nota):
    return slide("TUTORIAL", f"<span class='tag'>Passo {n}</span><div class='h'>{titulo}</div>{tela}"
                 f"<div style='display:flex;gap:20px;margin-top:40px'><div class='big' style='font-size:56px;text-shadow:none'>↑</div><p>{nota}</p></div>")


# ---------- B · Errado x Certo ----------
def b_capa(titulo, sub):
    return slide("ERRADO X CERTO", f"<span class='tag'>Errado x Certo</span><div class='hc'>{titulo}</div><p>{sub}</p>")


def b_par(titulo, errado, errado_txt, certo, certo_txt, porque=""):
    box = f"<div class='box' style='margin-top:40px'><div class='lbl'>Por que importa</div>{porque}</div>" if porque else ""
    return slide("ERRADO X CERTO", f"<div class='h'>{titulo}</div><div class='cmp'>"
                 f"<div class='bad'><div class='l'>✕ EVITE</div><div class='m'>{errado}</div><p>{errado_txt}</p></div>"
                 f"<div class='good'><div class='l'>✓ PREFIRA</div><div class='m'>{certo}</div><p>{certo_txt}</p></div></div>{box}")


# ---------- C · Métrica da semana ----------
_CBG = "background:radial-gradient(900px 800px at 50% 30%,rgba(255,122,26,.22),transparent 65%),#070707"


def c_capa(sigla, nome, formula, leitura):
    """formula: lista de termos; use '÷', '×', '−', '=' como operadores."""
    fx = "".join(f"<i>{x}</i>" if x in "÷×−+=" else f"<span>{x}</span>" for x in formula)
    return slide("MÉTRICA DA SEMANA",
                 "<div style='text-align:center;display:flex;flex-direction:column'>"
                 "<span class='tag ln' style='align-self:center'>Glossário prático</span>"
                 f"<div class='big' style='font-size:{240 if len(sigla) <= 4 else 150}px;margin:46px 0 12px'>{sigla}</div>"
                 f"<div style='font-family:Pop;font-weight:700;font-size:44px;margin-bottom:56px'>{nome}</div>"
                 f"<div class='fx'>{fx}</div><p style='margin-top:56px'>{leitura}</p></div>", bg=_CBG)


def c_texto(kick, titulo, corpo):
    return slide("MÉTRICA DA SEMANA", f"<span class='tag ln'>{kick}</span><div class='h'>{titulo}</div>{corpo}")


# ---------- D · Checklist (claro) ----------
def d_capa(kick, titulo, itens_preview):
    li = "".join(f"<div>☐&nbsp; {i}</div>" for i in itens_preview)
    return slide("CHECKLIST", f"<div style='font-family:Pop;font-weight:700;font-size:28px;letter-spacing:3px;color:{OR_D}'>{kick.upper()}</div>"
                 f"<div class='ser' style='font-size:104px;line-height:1.03;margin:24px 0 46px'>{titulo}</div>"
                 f"<div style='display:flex;flex-direction:column;gap:24px;font-size:38px;color:#2b2b2b'>{li}</div>", lt=True)


def d_itens(itens, inicio=1):
    """itens: lista de (titulo, texto). Até 3 por slide."""
    rows = "".join(f"<div class='di'><div class='n'>{inicio + i}</div><div><div class='t'>{t}</div><p>{p}</p></div></div>"
                   for i, (t, p) in enumerate(itens))
    return slide("CHECKLIST", f"<div class='dl'>{rows}</div>", lt=True)


# ---------- E · Mito x Verdade ----------
def e_par(mito, verdade, swipe=True):
    return ("<div class='pg'><div style='position:absolute;inset:0;display:grid;grid-template-rows:1fr 1fr'>"
            "<div style='background:#141414;padding:190px 80px 0'><span class='tag' style='background:#2a2a2a;color:#bdbdbd'>Mito</span>"
            "<div style='font-family:Ser;font-style:italic;font-size:64px;line-height:1.18;margin-top:32px;color:#cfcfcf;"
            f"text-decoration:line-through;text-decoration-color:#ff5a5a;text-decoration-thickness:6px'>“{mito}”</div></div>"
            "<div style='background:linear-gradient(160deg,#FF7A1A,#E0560A);padding:64px 80px 0;color:#120800'>"
            "<span class='tag' style='background:#120800;color:#FF7A1A'>Verdade</span>"
            f"<div style='font-family:Pop;font-weight:900;font-size:58px;line-height:1.12;margin-top:32px'>{verdade}</div></div></div>"
            f"{_hdr('MITO X VERDADE')}<div class='ftr' style='color:#3a1a00'><span>@aguiasdodigitalads</span>"
            f"{'<span style=\"font-family:Pop;font-weight:700\">Arrasta →</span>' if swipe else '<span></span>'}</div></div>")


def e_capa(titulo, sub):
    return slide("MITO X VERDADE", f"<span class='tag'>Mito x Verdade</span><div class='hc'>{titulo}</div><p>{sub}</p>")


# ---------- F · Frase de domingo ----------
def f_frase(texto_html):
    """Use <i>...</i> no trecho que deve ficar em laranja itálico."""
    return ("<div class='pg' style='background:#070707'>"
            "<div style='position:absolute;inset:60px;border:1px solid rgba(255,122,26,.4);border-radius:8px'></div>"
            "<div style='position:absolute;top:0;bottom:0;left:120px;right:120px;display:flex;flex-direction:column;justify-content:center'>"
            "<div style='font-family:Ser;font-size:260px;line-height:.6;color:#FF7A1A'>“</div>"
            f"<div class='ser' style='font-weight:500;font-size:84px;line-height:1.15'>{texto_html.replace('<i>', '<i style=\"color:#FF7A1A\">')}</div>"
            "<div style='margin-top:60px;display:flex;align-items:center;gap:20px;font-family:Pop;font-weight:700;font-size:28px;letter-spacing:2px;color:#9a9a9a'>"
            "<img src='{{LOGO}}' style='width:64px;height:64px;border-radius:50%'>ÁGUIAS DO DIGITAL · DOMINGO</div></div></div>")


# ---------- Reels ----------
def _rbar():
    return "<div class='rbar'>{{BAR}}</div>"


def _rtop(lt=False):
    return ("<div style='position:absolute;z-index:6;top:120px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;"
            "font-family:Pop;font-weight:700;font-size:32px'><img src='{{LOGO}}' style='width:76px;height:76px;border-radius:50%'>Águias do Digital</div>")


def g_titulo(kick, titulo, dur=3.0):
    html = (f"<div class='rl'>{_rtop()}<div style='position:absolute;top:0;bottom:0;left:90px;right:90px;display:flex;flex-direction:column;justify-content:center'>"
            f"<div class='kick' style='font-size:36px'>{kick}</div><div style='font-family:Pop;font-weight:900;font-size:100px;line-height:1.05;letter-spacing:-1.5px'>{titulo}</div></div>{_rbar()}</div>")
    return {"html": html, "dur": dur}


def g_tela(titulo, painel, legenda, dur=3.6):
    """painel: HTML dentro do celular — use g_kpis/g_grafico ou tela_anuncio/tela_tabela."""
    html = (f"<div class='rl'><div style='position:absolute;top:150px;left:80px;right:80px;text-align:center;font-family:Pop;font-weight:900;"
            f"font-size:76px;line-height:1.08'>{titulo}</div><div style='position:absolute;top:470px;left:0;right:0'>"
            f"<div class='phone'>{painel}</div></div><div class='cap'>{legenda}</div>{_rbar()}</div>")
    return {"html": html, "dur": dur}


def g_kpis(pares, ativo=None, cab="Visão geral · ilustração"):
    """pares: [(nome, valor_ou_seta)]; ativo: índice com contorno laranja."""
    cells = "".join(f"<div class='{'on' if i == ativo else ''}'><div class='k'>{k}</div><div class='v'>{v}</div></div>" for i, (k, v) in enumerate(pares))
    return f"<div style='font-family:Pop;font-weight:700;font-size:28px;color:#9a9a9a;margin-bottom:26px'>{cab}</div><div class='kp'>{cells}</div>"


def g_grafico(sobe=True):
    a = "0,230 100,215 200,200 300,160 400,140 500,100 600,70" if sobe else "0,70 100,90 200,80 300,130 400,170 500,200 600,230"
    return (f"<svg viewBox='0 0 600 300' style='width:100%;margin-top:36px'><polyline fill='none' stroke='#FF7A1A' stroke-width='8' points='{a}'/></svg>"
            "<div style='font-size:22px;color:#777'>Sem dados reais</div>")


def h_titulo(titulo, dur=3.0):
    html = (f"<div class='rl lt'>{_rtop(True)}<div style='position:absolute;top:0;bottom:0;left:90px;right:90px;display:flex;flex-direction:column;justify-content:center'>"
            f"<div class='ser' style='font-size:120px;line-height:1.02'>{titulo}</div></div>{_rbar()}</div>")
    return {"html": html, "dur": dur}


def h_lista(titulo, itens, ativo, dur=3.4):
    """Mostra a lista com itens até 'ativo' visíveis e os seguintes apagados. itens: [(titulo, sub)]."""
    rows = ""
    for i, (t, s) in enumerate(itens):
        off = " off" if i > ativo else ""
        tt, ss = (t, s) if i <= ativo else ("…", "")
        sub = f"<p>{ss}</p>" if ss else ""
        rows += f"<div class='di{off}'><div class='n'>{i + 1}</div><div><div class='t' style='font-size:46px'>{tt}</div>{sub}</div></div>"
    html = (f"<div class='rl lt'>{_rtop(True)}<div style='position:absolute;top:290px;left:90px;right:90px'>"
            f"<div class='ser' style='font-size:84px;line-height:1.05;margin-bottom:60px'>{titulo}</div><div class='dl'>{rows}</div></div>{_rbar()}</div>")
    return {"html": html, "dur": dur}


def r_cta(lt=False, dur=3.6):
    cls = "rl lt" if lt else "rl"
    html = (f"<div class='{cls}'><div style='position:absolute;top:0;bottom:0;left:90px;right:90px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center'>"
            "<img src='{{LOGO}}' style='width:400px;height:400px;border-radius:50%;box-shadow:0 0 90px rgba(255,122,26,.45);margin-bottom:60px'>"
            "<div style='font-family:Pop;font-weight:800;font-size:84px;line-height:1.1'>Quer aprender o passo a passo?</div>"
            "<div style='margin-top:40px;font-size:52px;opacity:.85'>Comunidade <b>Águias do Digital</b></div>"
            "<span class='ctab' style='margin-top:60px;font-size:46px'>Link na bio</span></div>{_rbar()}</div>").replace("{_rbar()}", _rbar())
    return {"html": html, "dur": dur}
