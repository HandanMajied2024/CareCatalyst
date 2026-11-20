"""ElevenLabs SFX for video v3, cached (skips existing files).  usage: python sfx_v3.py"""
import json, os, time, sys, urllib.request, urllib.error
from pathlib import Path
HERE = Path(__file__).resolve().parent
ENV = HERE.parents[1] / "CareCatalyst/concepts/today/.env"
KEY = os.environ.get("ELEVENLABS_API_KEY") or [l.split("=",1)[1].strip().strip('"') for l in ENV.read_text().splitlines() if l.startswith("ELEVENLABS_API_KEY")][0]
SFX = {
 "jazz": ("Quiet mellow jazz trio playing softly from a small kitchen radio, brushed drums, upright bass, warm piano, lo-fi, relaxed, loopable", 22),
 "drop": ("A plastic dog food bowl with dry kibble slips and falls onto a kitchen tile floor, short clatter", 1.5),
 "shimmer": ("Soft airy glassy shimmer swell, thin smoke forming into glass, subtle premium UI sound", 2),
 "dog": ("A small dog gives one soft curious whine, close, quiet room", 1),
}
def post(url, body, out):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"xi-api-key": KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=120) as r: out.write_bytes(r.read())
def main():
    sd = HERE / "sfx"; sd.mkdir(exist_ok=True); fail = 0
    for k, (p, s) in SFX.items():
        f = sd / f"{k}.mp3"
        if f.exists(): print("skip", k); continue
        for i in range(5):
            try:
                print("sfx", k); post("https://api.elevenlabs.io/v1/sound-generation", {"text": p, "duration_seconds": s, "prompt_influence": 0.5}, f); break
            except urllib.error.HTTPError as e:
                msg = e.read().decode(errors="replace")[:400]; print("HTTP", e.code, msg)
                if e.code == 429 and "quota" not in msg.lower(): time.sleep(5); continue
                fail += 1; break
        else: fail += 1
    sys.exit(1 if fail else 0)
if __name__ == "__main__": main()
