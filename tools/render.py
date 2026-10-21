"""Renderiza slides de carrossel (1080x1350, JPEG) no padrão visual Águias do Digital."""
import base64, json, sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
LOGO = "data:image/png;base64," + base64.b64encode((ROOT / "assets/logo.png").read_bytes()).decode()

FONT_FILES = {
 "PB": "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",
 "IXB": "/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf",
 "IBK": "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf",
 "IR": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
 "ISB": "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
}
FONT = {k: base64.b64encode(pathlib.Path(v).read_bytes()).decode() for k, v in FONT_FILES.items()}

CSS = """
@font-face{font-family:Pop;src:url(data:font/ttf;base64,@@PB@@) format('truetype');font-weight:700}
@font-face{font-family:Pop;src:url(data:font/otf;base64,@@IXB@@) format('opentype');font-weight:800}
@font-face{font-family:Pop;src:url(data:font/otf;base64,@@IBK@@) format('opentype');font-weight:900}
@font-face{font-family:Int;src:url(data:font/otf;base64,@@IR@@) format('opentype');font-weight:400}
@font-face{font-family:Int;src:url(data:font/otf;base64,@@ISB@@) format('opentype');font-weight:600}
*{margin:0;padding:0;box-sizing:border-box}
:root{--or:#FF7A1A;--or2:#FFA25C;--bg:#070707;--gr:#9A9A9A;--wh:#F4F1EC}
body{width:1080px;height:1350px;background:var(--bg);overflow:hidden;font-family:Int;color:var(--wh)}
.s{position:relative;width:1080px;height:1350px;padding:170px 96px 150px;display:flex;flex-direction:column;
 background:radial-gradient(900px 700px at 85% 10%,rgba(255,122,26,.20),transparent 60%),
            radial-gradient(700px 600px at 0% 100%,rgba(255,122,26,.10),transparent 60%),var(--bg)}
.s:before{content:'';position:absolute;inset:34px;border:2px solid rgba(255,122,26,.35);border-radius:28px;pointer-events:none}
.top{position:absolute;z-index:5;top:70px;left:96px;right:96px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:18px;font-family:Pop;font-weight:700;font-size:26px;letter-spacing:.5px}
.brand img{width:64px;height:64px;border-radius:50%;box-shadow:0 0 24px rgba(255,122,26,.55)}
.num{font-family:Pop;font-weight:700;font-size:26px;color:var(--gr)}
.kick{font-family:Pop;font-weight:700;font-size:30px;color:var(--or);letter-spacing:3px;text-transform:uppercase;margin-bottom:28px}
h1{font-family:Pop;font-weight:900;font-size:104px;line-height:1.02;letter-spacing:-2px}
h2{font-family:Pop;font-weight:800;font-size:72px;line-height:1.08;letter-spacing:-1px;margin-bottom:44px}
.o{color:var(--or);text-shadow:0 0 28px rgba(255,122,26,.55)}
p{font-size:42px;line-height:1.42;color:#D9D4CC}
p b{color:var(--wh);font-weight:600}
.mid{margin-top:auto;margin-bottom:auto}
.list{display:flex;flex-direction:column;gap:30px;margin-top:8px}
.it{display:flex;gap:30px;align-items:flex-start;font-size:40px;line-height:1.35;color:#D9D4CC}
.it .n{flex:0 0 78px;height:78px;border-radius:20px;background:rgba(255,122,26,.12);border:2px solid var(--or);
 display:flex;align-items:center;justify-content:center;font-family:Pop;font-weight:800;font-size:38px;color:var(--or)}
.it b{color:var(--wh);font-weight:600}
.box{margin-top:44px;padding:40px 44px;border-radius:24px;background:rgba(255,255,255,.04);border:2px solid rgba(255,122,26,.45);font-size:38px;line-height:1.4}
.box .lbl{font-family:Pop;font-weight:700;font-size:26px;color:var(--or);letter-spacing:2px;text-transform:uppercase;margin-bottom:14px}
.swipe{position:absolute;z-index:5;bottom:84px;right:96px;font-family:Pop;font-weight:700;font-size:30px;color:var(--or);display:flex;align-items:center;gap:14px}
.swipe span{font-size:44px}
.foot{position:absolute;z-index:5;bottom:84px;left:96px;font-size:26px;color:var(--gr)}
.cover h1{font-size:118px}
.biglogo{width:360px;height:360px;border-radius:50%;box-shadow:0 0 80px rgba(255,122,26,.45);margin-bottom:56px}
.cta{display:inline-block;margin-top:52px;padding:30px 54px;border-radius:999px;background:var(--or);color:#120800;font-family:Pop;font-weight:800;font-size:40px;box-shadow:0 0 50px rgba(255,122,26,.5)}
.center{align-items:center;text-align:center}
"""
for _k, _v in FONT.items():
    CSS = CSS.replace(f"@@{_k}@@", _v)


def page(body, idx, total, swipe=True):
    top = f'<div class="top"><div class="brand"><img src="{LOGO}">Águias do Digital</div><div class="num">{f"{idx}/{total}" if total > 1 else ""}</div></div>'
    sw = '<div class="swipe">Arrasta <span>→</span></div>' if swipe else ''
    return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{top}{body}{sw}<div class="foot">@aguiasdodigitalads</div></body></html>'


def render(spec_path, out_dir):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    slides = spec["slides"]; n = len(slides)
    files = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, html in enumerate(slides, 1):
            html = html.replace("{{LOGO}}", LOGO)
            pg.set_content(page(html, i, n, swipe=i < n), wait_until="load")
            pg.wait_for_timeout(150)
            f = out / f"{spec['id']}_{i:02d}.jpg"
            pg.screenshot(path=str(f), type="jpeg", quality=92)
            files.append(str(f))
        b.close()
    print("\n".join(files))


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
