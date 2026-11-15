"""Remove background locally (rembg), trim, defringe, write PNG/WebP + preview HTML.
Usage: python cutout.py IN [IN ...] -o OUTDIR [--model birefnet-portrait] [--matting] [--max 2048] [--webp]
"""
import argparse, html, pathlib, subprocess, tempfile
from PIL import Image, ImageFilter
from rembg import remove, new_session

ap = argparse.ArgumentParser()
ap.add_argument("inputs", nargs="+")
ap.add_argument("-o", "--out", default="cutouts")
ap.add_argument("--model", default="birefnet-portrait")
ap.add_argument("--matting", action="store_true", help="alpha matting for hair/fur")
ap.add_argument("--max", type=int, default=0, help="cap longest side in px")
ap.add_argument("--pad", type=int, default=8)
ap.add_argument("--webp", action="store_true")
ap.add_argument("--upscale", type=int, default=0, choices=[0, 2, 3, 4],
                help="Real-ESRGAN upscale factor before cut-out (0 = off)")
ap.add_argument("--no-cut", action="store_true", help="only upscale, keep background")
a = ap.parse_args()

out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
sess = None if a.no_cut else new_session(a.model)
ESRGAN = pathlib.Path.home() / ".claude/tools/realesrgan/realesrgan-ncnn-vulkan.exe"

def upscale(img, factor):
    with tempfile.TemporaryDirectory() as t:
        src, dst = pathlib.Path(t, "in.png"), pathlib.Path(t, "out.png")
        img.save(src)
        subprocess.run([str(ESRGAN), "-i", str(src), "-o", str(dst), "-n", "realesrgan-x4plus"],
                       check=True, capture_output=True)
        up = Image.open(dst).convert("RGB")
    if factor != 4:
        up = up.resize((img.width * factor, img.height * factor), Image.LANCZOS)
    return up
done = []
for p in map(pathlib.Path, a.inputs):
    img = Image.open(p).convert("RGB")
    if a.upscale:
        img = upscale(img, a.upscale)
    if a.no_cut:
        dst = out / f"{p.stem}_x{a.upscale}.png"; img.save(dst); print("ok", dst, img.size); continue
    rgba = remove(img, session=sess, alpha_matting=a.matting,
                  alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10,
                  alpha_matting_erode_size=10)
    r, g, b, al = rgba.split()
    # defringe: shrink alpha by 1px and soften, kills colour halo of old background
    al = al.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.6))
    rgba = Image.merge("RGBA", (r, g, b, al))
    bbox = al.point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        x0, y0, x1, y1 = bbox
        rgba = rgba.crop((max(0, x0 - a.pad), max(0, y0 - a.pad),
                          min(rgba.width, x1 + a.pad), min(rgba.height, y1 + a.pad)))
    if a.max and max(rgba.size) > a.max:
        rgba.thumbnail((a.max, a.max), Image.LANCZOS)
    dst = out / f"{p.stem}.png"
    rgba.save(dst, optimize=True)
    if a.webp:
        rgba.save(out / f"{p.stem}.webp", quality=90, method=6)
    done.append(dst.name); print("ok", dst, rgba.size)

bgs = ["repeating-conic-gradient(#ddd 0 25%,#fff 0 50%) 0 0/24px 24px", "#fff", "#000",
       "radial-gradient(circle at 30% 30%,#c7d2fe,#fbcfe8 45%,#fef3c7)"]
cells = "".join(f'<div style="background:{b}"><img src="{html.escape(n)}"></div>' for n in done for b in bgs)
(out / "preview.html").write_text(f"""<!doctype html><meta charset=utf-8><title>Cutouts</title>
<style>body{{margin:0;font-family:Inter,sans-serif;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:8px}}
div{{aspect-ratio:1;display:grid;place-items:center;border-radius:12px}}img{{max-width:90%;max-height:90%}}</style>{cells}""",
    encoding="utf-8")
print("preview:", (out / "preview.html").resolve())
