"""Deploy CareCatalyst Concept A (Care Pathway Agent) to Modal as one Node process.

Run from anywhere:  PYTHONUTF8=1 python -m modal deploy pitch/deploy/modal_app.py
Secrets are read from concepts/today/.env at deploy time (never baked into the repo).
"""
import pathlib
import subprocess

import modal

_here = pathlib.Path(__file__).resolve()
# Locally: <workspace>/pitch/deploy/modal_app.py. In the container the file sits at /root, where APP_DIR is unused.
APP_DIR = _here.parents[2] / "CareCatalyst" / "concepts" / "today" if len(_here.parents) > 2 else pathlib.Path("/app")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("curl", "ca-certificates")
    .run_commands(
        "curl -fsSL https://deb.nodesource.com/setup_22.x | bash -",
        "apt-get install -y nodejs",
    )
    .add_local_dir(
        str(APP_DIR),
        remote_path="/app",
        copy=True,
        ignore=["node_modules", "dist", ".env", ".env.*", ".git", "*.log", "coverage"],
    )
    .run_commands("cd /app && npm ci --legacy-peer-deps --no-audit --no-fund && npm run build")
)

app = modal.App("carecatalyst-demo")


@app.function(
    image=image,
    secrets=[modal.Secret.from_dotenv(str(APP_DIR))],
    min_containers=1,
    timeout=3600,
)
@modal.concurrent(max_inputs=100)
@modal.web_server(port=8000, startup_timeout=180)
def web():
    subprocess.Popen(
        "cd /app && NODE_ENV=production PORT=8000 npx tsx server.ts",
        shell=True,
    )
