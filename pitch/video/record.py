"""Render video.html to mp4 (frame-exact) and mix ElevenLabs voice + SFX + music bed.

usage (PYTHONUTF8=1):
  python record.py stills 3 15 40      # PNG stills -> frames/
  python record.py audio               # voice.wav (voice + sfx + bed) from timeline.js + cues in the page
  python record.py frames [fps]        # frame-exact capture -> video_noaudio.mp4
  python record.py mux                 # -> CareCatalyst-demo.mp4
  python record.py all                 # audio + frames + mux
"""
import json, shutil, subprocess, sys
from pathlib import Path
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
URL = (HERE / "video.html").as_uri()
FF = imageio_ffmpeg.get_ffmpeg_exe()
VW, VH = 1920, 1080


def ff(*args):
    subprocess.run([FF, "-y", "-loglevel", "error", *map(str, args)], check=True)


def page(p):
    b = p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": VW, "height": VH})
    pg.goto(URL + "?seek=1"); pg.wait_for_function("window.__ready === true")
    pg.wait_for_timeout(400)
    return b, pg


def stills(times):
    out = HERE / "frames"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b, pg = page(p)
        for t in times:
            pg.evaluate(f"window.__render({t})")
            f = out / f"still_{float(t):06.2f}.png"; pg.screenshot(path=str(f)); print(f)
        b.close()


def audio():
    with sync_playwright() as p:
        b, pg = page(p)
        cues = pg.evaluate("window.__cues"); total = pg.evaluate("window.__total")
        b.close()
    tl = json.loads((HERE / "timeline.js").read_text(encoding="utf-8")[len("window.TL="):].rstrip().rstrip(";"))
    ins, flt, labels = [], [], []
    for i, L in enumerate(tl["lines"]):
        ins += ["-i", HERE / "voice" / L["file"]]
        flt.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={int(L['start']*1000)}|{int(L['start']*1000)}[v{i}]"); labels.append(f"[v{i}]")
    n = len(tl["lines"])
    for j, (name, t, vol) in enumerate(cues):
        ins += ["-i", HERE / "sfx" / f"{name}.mp3"]
        k = n + j
        flt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={int(t*1000)}|{int(t*1000)}[s{j}]"); labels.append(f"[s{j}]")
    # music bed: loop, quiet, fade in/out
    ins += ["-stream_loop", "-1", "-i", HERE / "sfx" / "bed.mp3"]
    k = n + len(cues)
    flt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{total},volume=0.14,afade=t=in:d=2,afade=t=out:st={total-3}:d=3[bed]"); labels.append("[bed]")
    flt.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:dropout_transition=0,atrim=0:{total},alimiter=limit=0.9[out]")
    ff(*ins, "-filter_complex", ";".join(flt), "-map", "[out]", "-ar", "44100", HERE / "voice.wav")
    print("voice.wav", total)


def frames(fps=30):
    out = HERE / "_frames"; shutil.rmtree(out, ignore_errors=True); out.mkdir()
    with sync_playwright() as p:
        b, pg = page(p)
        total = pg.evaluate("window.__total")
        n = int(round(total * fps))
        for i in range(n):
            pg.evaluate(f"window.__render({i / fps})")
            pg.screenshot(path=str(out / f"f{i:05d}.jpg"), type="jpeg", quality=92)
            if i % (fps * 10) == 0: print(f"{i / fps:.0f}s / {total:.0f}s", flush=True)
        b.close()
    ff("-framerate", fps, "-i", out / "f%05d.jpg", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
       "-movflags", "+faststart", HERE / "video_noaudio.mp4")
    shutil.rmtree(out, ignore_errors=True)
    print("video_noaudio.mp4")


def mux():
    ff("-i", HERE / "video_noaudio.mp4", "-i", HERE / "voice.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
       "-map", "0:v:0", "-map", "1:a:0", "-shortest", "-movflags", "+faststart", HERE / "CareCatalyst-demo.mp4")
    print(HERE / "CareCatalyst-demo.mp4")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "stills": stills([float(x) for x in sys.argv[2:]])
    elif cmd == "audio": audio()
    elif cmd == "frames": frames(int(sys.argv[2]) if len(sys.argv) > 2 else 30)
    elif cmd == "mux": mux()
    elif cmd == "all": audio(); frames(); mux()
