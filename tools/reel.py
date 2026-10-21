"""Gera Reels animados (1080x1920, MP4 H.264) no padrão Águias do Digital.
Uso: python3 reel.py <spec.json> <out_dir>
spec = {"id": "...", "scenes": [{"kick": "...", "html": "...", "dur": 3.2}, ...]}
"""
import json, sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
import render  # reaproveita fontes, logo e cores

W, H, FPS, FADE = 1080, 1920, 30, 0.45

CSS = render.CSS.replace("width:1080px;height:1350px", "width:1080px;height:1920px") + """
.r{position:relative;width:1080px;height:1920px;padding:300px 90px 420px;display:flex;flex-direction:column;justify-content:center;
 background:radial-gradient(1000px 900px at 90% 8%,rgba(255,122,26,.22),transparent 60%),
            radial-gradient(800px 800px at 0% 100%,rgba(255,122,26,.12),transparent 60%),var(--bg)}
.r:before{content:'';position:absolute;inset:40px;border:2px solid rgba(255,122,26,.35);border-radius:34px}
.rtop{position:absolute;z-index:5;top:150px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:20px;
 font-family:Pop;font-weight:700;font-size:34px}
.rtop img{width:84px;height:84px;border-radius:50%;box-shadow:0 0 28px rgba(255,122,26,.55)}
.r .kick{font-size:36px;margin-bottom:36px}
.r .t{font-family:Pop;font-weight:900;font-size:96px;line-height:1.06;letter-spacing:-1.5px}
.r .t.m{font-size:90px;font-weight:800}
.r .sub{margin-top:48px;font-size:54px;line-height:1.4;color:#D9D4CC}
.r .sub b{color:var(--wh);font-weight:600}
.bar{position:absolute;z-index:5;left:90px;right:90px;bottom:330px;display:flex;gap:12px}
.bar i{flex:1;height:8px;border-radius:8px;background:rgba(255,255,255,.14)}
.bar i.on{background:var(--or);box-shadow:0 0 14px rgba(255,122,26,.7)}
.rcta{display:inline-block;margin-top:60px;padding:34px 64px;border-radius:999px;background:var(--or);color:#120800;
 font-family:Pop;font-weight:800;font-size:46px;box-shadow:0 0 50px rgba(255,122,26,.5)}
.rlogo{width:420px;height:420px;border-radius:50%;box-shadow:0 0 90px rgba(255,122,26,.45);margin:0 auto 60px}
"""


def frame(scene, i, n):
    bar = "".join(f"<i class='{'on' if k <= i else ''}'></i>" for k in range(n))
    kick = f"<div class='kick'>{scene['kick']}</div>" if scene.get("kick") else ""
    top = "" if scene.get("cta") else f"<div class='rtop'><img src='{render.LOGO}'>Águias do Digital</div>"
    body = scene["html"].replace("{{LOGO}}", render.LOGO)
    align = "text-align:center;align-items:center" if scene.get("cta") else ""
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{top}"
            f"<div class='r' style='{align}'>{kick}{body}</div><div class='bar'>{bar}</div></body></html>")


def build(spec_path, out_dir):
    spec = json.loads(pathlib.Path(spec_path).read_text())
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    tmp = out / f"_{spec['id']}"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir()
    scenes = spec["scenes"]; n = len(scenes)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        for i, sc in enumerate(scenes):
            pg.set_content(frame(sc, i, n), wait_until="load"); pg.wait_for_timeout(120)
            pg.screenshot(path=str(tmp / f"s{i:02d}.png"))
        b.close()
    # um clipe por cena com zoom lento; depois encadeia com crossfade
    durs = [float(sc.get("dur", 3.2)) for sc in scenes]
    clips = []
    for i, d in enumerate(durs):
        c = tmp / f"c{i:02d}.mp4"; frames = int(round((d + FADE) * FPS))
        vf = (f"scale=1188:2112,zoompan=z='min(1+0.0009*on,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d={frames}:s={W}x{H}:fps={FPS},format=yuv420p")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(tmp / f"s{i:02d}.png"),
                        "-vf", vf, "-frames:v", str(frames), "-c:v", "libx264", "-preset", "medium", "-crf", "18", str(c)], check=True)
        clips.append(c)
    inputs = sum((["-i", str(c)] for c in clips), [])
    chain, last, t = [], "[0:v]", 0.0
    for i in range(1, n):
        t += durs[i - 1]
        lab = f"[v{i}]"
        chain.append(f"{last}[{i}:v]xfade=transition=fade:duration={FADE}:offset={t:.3f}{lab}")
        last = lab
    final = out / f"{spec['id']}.mp4"
    # faixa de áudio silenciosa: o Instagram lida melhor com vídeos que têm trilha
    total = sum(durs) + FADE
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo",
           "-filter_complex", ";".join(chain) if chain else "[0:v]null[vout]",
           "-map", last if chain else "[vout]", "-map", f"{n}:a",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(final)]
    subprocess.run(cmd, check=True)
    # capa (primeira cena)
    shutil.copy(tmp / "s00.png", out / f"{spec['id']}_capa.png")
    print(final)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
