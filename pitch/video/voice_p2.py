"""ElevenLabs voice for Part 2 (v3), cached. Builds timeline_p2.js.  usage: python voice_p2.py"""
import json, hashlib, subprocess, re, os, time
from pathlib import Path
import urllib.request, urllib.error
import imageio_ffmpeg
HERE = Path(__file__).resolve().parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
ENV = HERE.parents[1] / "CareCatalyst/concepts/today/.env"
KEY = os.environ.get("ELEVENLABS_API_KEY") or [l.split("=",1)[1].strip().strip('"') for l in ENV.read_text().splitlines() if l.startswith("ELEVENLABS_API_KEY")][0]
VOICES = {"nar": "JBFqnCBsd6RMkjVDRZzb", "agent": "EXAVITQu4vr4xnSDxMaL", "eero": "pqHfZKP75CvOlQylNhV4"}
SET = {"nar": dict(stability=0.55, similarity_boost=0.8, style=0.2), "agent": dict(stability=0.5, similarity_boost=0.8, style=0.25),
       "eero": dict(stability=0.45, similarity_boost=0.8, style=0.3)}
TAIL = 2.8

def post(url, body, out):
    for k in range(6):
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r: out.write_bytes(r.read()); return
        except urllib.error.HTTPError as e:
            msg = e.read()[:300]
            if e.code == 429 and k < 5: print("429, retry"); time.sleep(5); continue
            raise SystemExit(f"ElevenLabs HTTP {e.code}: {msg}")

def dur(p):
    o = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", o).groups(); return int(h)*3600 + int(m)*60 + float(s)

def main():
    vd = HERE / "voice"; vd.mkdir(exist_ok=True)
    lines = json.loads((HERE / "lines_p2.json").read_text(encoding="utf-8"))
    t = 0.4; tl = []
    for L in lines:
        h = hashlib.md5((L["who"] + L["text"]).encode()).hexdigest()[:8]
        f = vd / f"{L['id']}_{h}.mp3"
        if not f.exists():
            print("tts", L["id"]); post(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICES[L['who']]}?output_format=mp3_44100_128",
                 {"text": L["text"], "model_id": "eleven_multilingual_v2", "voice_settings": SET[L["who"]]}, f)
        t += L["gap"]; d = dur(f)
        tl.append({**L, "file": f.name, "start": round(t, 2), "dur": round(d, 2)}); t += d
        print(L["id"], round(t - d, 2), round(d, 2))
    total = round(t + TAIL, 2)
    (HERE / "timeline_p2.js").write_text("window.TL=" + json.dumps({"lines": tl, "total": total}, indent=1) + ";", encoding="utf-8")
    print("total", total)

if __name__ == "__main__": main()
