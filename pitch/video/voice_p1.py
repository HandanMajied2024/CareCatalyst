"""ElevenLabs voice + SFX, cached. Builds timeline.js and voice.wav.  usage: python voice.py"""
import json, hashlib, subprocess, re, os
from pathlib import Path
import urllib.request, urllib.error
import imageio_ffmpeg
HERE = Path(__file__).resolve().parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
ENV = HERE.parents[1] / "CareCatalyst/concepts/today/.env"
KEY = os.environ.get("ELEVENLABS_API_KEY") or [l.split("=",1)[1].strip().strip('"') for l in ENV.read_text().splitlines() if l.startswith("ELEVENLABS_API_KEY")][0]
VOICES = {"nar": "JBFqnCBsd6RMkjVDRZzb", "agent": "EXAVITQu4vr4xnSDxMaL", "matti": "iP95p4xoKVk53GoZ742B", "eero": "pqHfZKP75CvOlQylNhV4"}
SET = {"nar": dict(stability=0.55, similarity_boost=0.8, style=0.2), "agent": dict(stability=0.5, similarity_boost=0.8, style=0.25),
       "matti": dict(stability=0.4, similarity_boost=0.8, style=0.3), "eero": dict(stability=0.45, similarity_boost=0.8, style=0.3)}
SFX = {
 "ring": ("Modern soft smartphone ringtone, two gentle marimba rings, clean, no music", 3),
 "whoosh": ("Very soft clean airy whoosh transition, subtle, premium UI", 1.2),
 "pop": ("Soft subtle UI pop click, clean, premium app interface", 0.6),
 "chime": ("Gentle positive notification chime, two soft bell notes, clean, premium", 1.5),
 "tick": ("Soft single tick confirmation sound, clean UI", 0.5),
 "hangup": ("Soft phone call end beep, short, clean", 0.8),
 "bed": ("Calm warm minimal ambient piano and soft pad, hopeful, slow, no drums, loopable background", 22),
}

def post(url, body, out):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    import time
    for k in range(6):
        try:
            with urllib.request.urlopen(req, timeout=120) as r: out.write_bytes(r.read()); return
        except urllib.error.HTTPError as e:
            if e.code == 429 and k < 5: print("429, retry"); time.sleep(5); continue
            print("HTTP", e.code, e.read()[:300]); raise

def dur(p):
    o = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", o).groups(); return int(h)*3600 + int(m)*60 + float(s)

def main():
    vd = HERE / "voice"; vd.mkdir(exist_ok=True)
    lines = json.loads((HERE / "lines_p1.json").read_text(encoding="utf-8"))
    t = 0.6; tl = []
    for L in lines:
        h = hashlib.md5((L["who"] + L["text"]).encode()).hexdigest()[:8]
        f = vd / f"{L['id']}_{h}.mp3"
        if not f.exists():
            print("tts", L["id"]); post(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICES[L['who']]}?output_format=mp3_44100_128",
                 {"text": L["text"], "model_id": "eleven_multilingual_v2", "voice_settings": SET[L["who"]]}, f)
        t += L["gap"]; d = dur(f)
        tl.append({**L, "file": f.name, "start": round(t, 2), "dur": round(d, 2)}); t += d
    total = round(t + 1.8, 2)
    sd = HERE / "sfx"; sd.mkdir(exist_ok=True)
    for k, (p, s) in SFX.items():
        f = sd / f"{k}.mp3"
        if not f.exists():
            print("sfx", k); post("https://api.elevenlabs.io/v1/sound-generation", {"text": p, "duration_seconds": s, "prompt_influence": 0.5}, f)
    facts = {}
    try: facts = json.loads((HERE / "facts.json").read_text(encoding="utf-8"))
    except Exception as e: print("no facts", e)
    def pick(*c):
        for x in c:
            if (HERE / x).exists(): return x
        return ""
    assets = {"slide": pick("img/az_reasons_slide.png"),
              "a1": pick("img/v3/a_patients.png", "../screens/LIVE-A-01-patients.png"),
              "a2": pick("img/v3/a_regional.png", "../screens/LIVE-A-05-regional-summary.png"),
              "b": pick("img/v3/b_today.png", "../screens/B-01-today.png")}
    (HERE / "timeline_p1.js").write_text("window.TL=" + json.dumps({"lines": tl, "total": total, "facts": facts, "assets": assets}, indent=1) + ";", encoding="utf-8")
    print("total", total)

if __name__ == "__main__": main()
