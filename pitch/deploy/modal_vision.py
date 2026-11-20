"""Deploy CareCatalyst Concept B (CarePulse, personal agent vision) to Modal as a static site.

Build first, then deploy:
    cd CareCatalyst/concepts/vision && npm run build
    PYTHONUTF8=1 python -m modal deploy pitch/deploy/modal_vision.py
The app is fully scripted (no API keys, no network calls), so it only serves dist/.
"""
import pathlib
import subprocess

import modal

_here = pathlib.Path(__file__).resolve()
DIST = _here.parents[2] / "CareCatalyst" / "concepts" / "vision" / "dist" if len(_here.parents) > 2 else pathlib.Path("/site")

image = modal.Image.debian_slim(python_version="3.12").add_local_dir(str(DIST), remote_path="/site")

app = modal.App("carepulse-vision")


@app.function(image=image, min_containers=1, cpu=0.25, memory=256, timeout=3600)
@modal.concurrent(max_inputs=200)
@modal.web_server(port=8000, startup_timeout=60)
def web():
    subprocess.Popen("cd /site && python -m http.server 8000 --bind 0.0.0.0", shell=True)
