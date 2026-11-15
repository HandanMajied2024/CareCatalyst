---
name: cutout-images
description: Handan's workflow for realistic people / hands / objects with a transparent background (PNG cut-outs) for designs, decks, videos and UIs. Sources images legally (free-licence stock without watermark, AI generation, own photos), removes the background locally for €0 with rembg/BiRefNet, cleans edges, upscales/sharpens locally with Real-ESRGAN (€0), checks realism, logs licences. Use when Handan asks for Freisteller, freigestellte Personen/Hände, transparenter Hintergrund, PNG ohne Hintergrund, cut-out, remove background, Qualität erhöhen, hochskalieren, upscale.
---

# Cut-out images (transparent PNGs of people, hands, objects)

Answer short, in German. Show results in the browser (on a checkerboard + on the target background).

## Rule: no watermark removal
Never remove or retouch watermarks from stock images (Shutterstock, Getty, Adobe Stock, iStock, …). A watermark
means "not licensed". If Handan brings such an image, use it only as a **reference** for pose/composition and get the
real image from one of the sources below (or buy the licence – the licensed download has no watermark).

## 1. Source (in this order, €0 first)
| Source | Licence | Note |
|---|---|---|
| Unsplash, Pexels, Pixabay | free, commercial OK, no attribution needed | best for real people & hands; download "Original" size |
| Own photos / team photos | own | ask consent of people shown |
| AI generation (Codex image gen, Gemini/Imagen, Figma generate_image) | own output | paid → small samples; prompt **"on plain solid light-grey studio background, soft even light"** – makes the cut-out much cleaner |
| Bought stock licence | per licence | download the licensed file, not the preview |
- Only watermark-free images (rule above).
- Prefer images that already have a plain/studio background, sharp focus, high resolution (≥2000 px).
- Log every image in `assets/cutouts/SOURCES.md`: file, source URL, author, licence, date.
- Avoid recognisable real people in sensitive contexts (e.g. "cancer patient") unless the licence allows it
  (Unsplash/Pexels forbid implying a person endorses something or has a condition in a misleading way) → for patient
  scenes prefer AI-generated, synthetic people.

## 2. Increase quality (local, free) – before the cut-out
Real-ESRGAN portable at `~/.claude/tools/realesrgan/realesrgan-ncnn-vulkan.exe` (model `realesrgan-x4plus`, runs on
the GPU via Vulkan). Use when the image is < 2000 px or soft/noisy. Upscaling first gives cleaner mask edges.
```
python cutout.py IN.jpg -o assets/cutouts --upscale 4            # upscale + cut-out
python cutout.py IN.jpg -o assets/cutouts --upscale 4 --no-cut   # only upscale
```
- Check faces/hands afterwards: ESRGAN can make skin waxy → if so use `--upscale 2` or the original.
- Upscaling does not invent real detail; a bad source stays bad → choose another image.

## 3. Remove background (local, free)
Script: `~/.claude/skills/cutout-images/scripts/cutout.py`
```
pip install "rembg[cpu]" pillow          # once; models download on first run (~200 MB)
PYTHONUTF8=1 python ~/.claude/skills/cutout-images/scripts/cutout.py IN.jpg [IN2 …] -o assets/cutouts --model birefnet-portrait
```
Models: `birefnet-portrait` (people, hair) · `birefnet-general` (hands, objects) · `isnet-general-use` (fast) ·
`u2net_human_seg` (fallback). Hair/fur fuzzy → add `--matting`. Output: trimmed PNG + preview HTML.
Fallbacks if rembg fails on an image: remove.bg / Photoroom (free preview size, paid HD → ask first), or Figma.

## 4. Clean-up
- Script trims to content (+ small padding), defringes the edge (removes the old background colour halo),
  optionally `--max 2048` to cap size, `--webp` for web.
- Check at 200 % zoom: halo, cut-off fingertips, holes between fingers/arms, leftover floor shadow.
- Add a soft contact shadow in CSS/design (not baked into the PNG), so the cut-out can be reused.

## 5. Realism check (every image, before use)
- Hands: 5 fingers, correct joints/nails, no merged or extra fingers, natural skin texture.
- Faces/eyes symmetric, teeth normal, no AI artefacts, text/logos on clothing gibberish-free or removed.
- Light direction fits the target design; colour temperature matched (adjust in CSS: `filter`).
- Fail → regenerate / pick another image, don't patch.

## 6. Deliver
- Files in `assets/cutouts/<name>.png` (+ `.webp`), `SOURCES.md` updated.
- Open the preview page (checkerboard, white, black, gradient) for Handan.
