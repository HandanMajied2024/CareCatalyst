"""Render video_p2.html (v3 Part 2) to p2.mp4, frame-exact, 3 parallel capture workers.

usage (PYTHONUTF8=1):
  python record_p2.py stills 3 15 40   # JPG stills -> frames_p2/
  python record_p2.py audio            # voice_p2.wav (voice + sfx + jazz + bed)
  python record_p2.py frames           # parallel capture -> _frames_p2/ -> p2_noaudio.mp4
  python record_p2.py mux              # -> p2.mp4
  python record_p2.py all
"""
import json, subprocess, sys
from pathlib import Path
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
URL = (HERE / "video_p2.html").as_uri()
FF = imageio_ffmpeg.get_ffmpeg_exe()
VW, VH, FPS, WORKERS = 1920, 1080, 30, 3
TMP = HERE / "_frames_p2"; NOA = TMP / "p2_noaudio.mp4"


def ff(*args):
    subprocess.run([FF, "-y", "-loglevel", "error", *map(str, args)], check=True)


def page(p):
    b = p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": VW, "height": VH})
    pg.goto(URL + "?seek=1"); pg.wait_for_function("window.__ready === true")
    pg.wait_for_timeout(400)
    return b, pg


def stills(times):
    out = HERE / "frames_p2"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b, pg = page(p)
        for t in times:
            pg.evaluate(f"window.__render({t})")
            f = out / f"still_{float(t):06.2f}.jpg"; pg.screenshot(path=str(f), type="jpeg", quality=85); print(f)
        b.close()


def audio():
    with sync_playwright() as p:
        b, pg = page(p)
        cues = pg.evaluate("window.__cues"); total = pg.evaluate("window.__total"); end_a = pg.evaluate("window.__endA")
        b.close()
    tl = json.loads((HERE / "timeline_p2.js").read_text(encoding="utf-8")[len("window.TL="):].rstrip().rstrip(";"))
    ins, flt, labels = [], [], []
    for i, L in enumerate(tl["lines"]):
        ins += ["-i", HERE / "voice" / L["file"]]
        flt.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={int(L['start']*1000)}|{int(L['start']*1000)}[v{i}]"); labels.append(f"[v{i}]")
    n = len(tl["lines"]); missing = []
    for j, (name, t, vol) in enumerate(cues):
        f = HERE / "sfx" / f"{name}.mp3"
        if not f.exists(): missing.append(name); f = HERE / "sfx" / ("whoosh.mp3" if name == "shimmer" else "pop.mp3")
        ins += ["-i", f]
        k = n + j
        flt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={int(t*1000)}|{int(t*1000)}[s{j}]"); labels.append(f"[s{j}]")
    k = n + len(cues)
    # kitchen radio: soft jazz, band-limited, fades out into the music bed for the end slide
    jazz = HERE / "sfx" / "jazz.mp3"
    if jazz.exists():
        ins += ["-stream_loop", "-1", "-t", "70", "-i", jazz]
        flt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{end_a + 1.2},highpass=f=220,lowpass=f=4200,volume=0.15,afade=t=in:d=0.8,afade=t=out:st={end_a - 1.0}:d=2.2[jz]"); labels.append("[jz]"); k += 1
    else: missing.append("jazz")
    ins += ["-stream_loop", "-1", "-t", "70", "-i", HERE / "sfx" / "bed.mp3"]
    d0 = int((end_a - 0.8) * 1000)
    flt.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{total - end_a + 0.8},volume=0.16,afade=t=in:d=1.8,adelay={d0}|{d0}[bed]"); labels.append("[bed]")
    flt.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:dropout_transition=0,atrim=0:{total},afade=t=out:st={total - 1.6}:d=1.6,alimiter=limit=0.9[out]")
    ff(*ins, "-filter_complex", ";".join(flt), "-map", "[out]", "-ar", "44100", "-ac", "2", "-t", total, HERE / "voice_p2.wav")
    print("voice_p2.wav", total, "missing sfx:", missing)


def worker(a, b):
    with sync_playwright() as p:
        br, pg = page(p)
        for i in range(a, b):
            pg.evaluate(f"window.__render({i / FPS})")
            pg.screenshot(path=str(TMP / f"f{i:05d}.jpg"), type="jpeg", quality=92)
        br.close()


def frames():
    TMP.mkdir(exist_ok=True)
    for f in TMP.glob("f*.jpg"): f.unlink()
    with sync_playwright() as p:
        b, pg = page(p); total = pg.evaluate("window.__total"); b.close()
    n = int(round(total * FPS)); step = -(-n // WORKERS)
    procs = [subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "worker", str(a), str(min(n, a + step))]) for a in range(0, n, step)]
    for pr in procs:
        if pr.wait() != 0: raise SystemExit("worker failed")
    got = len(list(TMP.glob("f*.jpg")))
    if got != n: raise SystemExit(f"frames {got} != {n}")
    ff("-framerate", FPS, "-i", TMP / "f%05d.jpg", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-r", FPS,
       "-movflags", "+faststart", NOA)
    for f in TMP.glob("f*.jpg"): f.unlink()
    print("frames", n)


def mux():
    ff("-i", NOA, "-i", HERE / "voice_p2.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
       "-map", "0:v:0", "-map", "1:a:0", "-shortest", "-movflags", "+faststart", HERE / "p2.mp4")
    print(HERE / "p2.mp4")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "stills": stills([float(x) for x in sys.argv[2:]])
    elif cmd == "audio": audio()
    elif cmd == "worker": worker(int(sys.argv[2]), int(sys.argv[3]))
    elif cmd == "frames": frames()
    elif cmd == "mux": mux()
    elif cmd == "all": audio(); frames(); mux()
