---
name: pitch-video
description: Handan's workflow for making a pitch / demo video for any product: script first, images with Codex, a realism check on every image, animation in HTML by default and Google Flow only for motion that cannot be coded, ElevenLabs (or a cheaper equal option) for sound, rendered to mp4. Use when Handan asks for a pitch video, demo video, Pitch-Video, Video erstellen, Animationen, or to update/re-render one.
---

# Pitch video workflow

Handan dictates in German by voice: answer short, in German, read typos generously.
Paid tools (Codex, Google Flow, ElevenLabs) are used sparingly: small samples, and confirm with Handan before each paid
generation. Show her intermediate results (open them in the browser / player) at every step.

## 1. Brief and script first (nothing is generated before this)
- Clarify: product, audience, length (default 120 s, 1920x1080), rules of the event/challenge (allowed tools,
  licences).
- **Design style = Handan's own projects on GitHub** (account `HandanMajied2024`, `gh repo list HandanMajied2024`).
  Look at their UIs/pages (colours, fonts, spacing, components, motion) and derive the video's look from them. Write
  the derived style (palette, font, radii, shadows, motion feel) at the top of `SCRIPT.md` so she can correct it.
- Write `SCRIPT.md`: scene table with start/end, voiceover text, what is on screen, source of every number/claim.
  Plus `voiceover.txt` (about 1.8 words/s). Get Handan's OK on the script.
- For each scene decide **how** it is made and note it in the table:
  - **HTML/CSS/JS (default):** UI, text, charts, overlays, zooms, Ken-Burns, taps/ripples, crossfades, match cuts.
  - **Google Flow (exception):** only motion that cannot be coded convincingly: real people, hands moving,
    camera moves through a real-looking scene. Mark each Flow scene with a reason.
- Real product screens come from the real app (Playwright screenshots), never invented UI.

## 2. Rough draft (Entwurf) for the flow of the story
Goal: Handan decides whether the sequence works. Cheap and fast, nothing paid beyond a few first images.
- Only the first few images (step 3, a handful) plus real app screenshots; placeholder cards for missing scenes.
- Voice only with the cheap/free TTS.
- No real transitions: hard cuts, at most simple HTML transitions (fade, slide). No Flow, no ElevenLabs.
- Render it, open it for Handan, adjust the script with her. Only after her OK continue to the full production.

## 3. Images with Codex
- Generate stills / start frames with Codex image generation (green screen for devices and hands so real screens can
  be composited in). Few variants, not dozens.
- **Devices** (phone, tablet, laptop) must look real, premium and sharp: current high-end hardware, correct
  proportions, thin bezels, realistic materials and reflections, crisp edges, the real app screen composited sharp
  at full resolution (no blurry or stretched screenshot).

- **Hand poses from real photos:** before generating a hand pose, find 2–3 real photos of exactly that pose (Unsplash
  free licence), name the anatomy rules they show (e.g. thumb starts at the phone edge, bends at its knuckle, only the
  tip touches; palm/thenar stays behind the phone) and pass the best photo to Codex as pose reference next to the
  identity reference. Compare the result side by side with the real photo.
- Codex CLI: `codex exec --skip-git-repo-check -s read-only --image=a.png --image=b.png -- "prompt"` (use `--image=`
  and `--`, otherwise `-i` swallows the prompt). Output lands in `~/.codex/generated_images/<newest>/`.

## 4. Realism and quality check (every image, before it is used or animated)
Look at each image yourself (open it, plus zoomed crops of hands, faces, text, edges). Reject and regenerate if any fails:
- **Hands:** five fingers, correct thumb side, left/right hand plausible, fingers not merged or bent wrong, grip
  physically possible, gloves/sleeves consistent.
- **Faces and bodies:** no warped eyes/teeth, proportions right.
- **Objects:** devices have straight edges and right proportions, screens flat and in perspective, no melted parts.
- **Text:** no garbled letters or fake logos (put real text in later with HTML).
- **Light and perspective:** shadows and light direction consistent, composite screen matches angle and brightness.
- **Quality:** at least 1920 px wide, sharp, no artefacts, no watermark, no "AI glossy" look.
For important images also ask an independent reviewer agent with only the image and this checklist. Note the result
per image (pass / regenerated why). Show the passed images to Handan.

## 5. Google Flow (sparingly)
- Only after the rough draft is approved, the app design is final and the start frames passed the check.
- Only the scenes marked "Flow" in step 1. Settings: 1 output, confirm before each generation, short clips.
- Flow (flow.google.com) works via its chat agent: attach start + end frame, choose Veo 3.1 Fast, it asks for
  approval (~20 credits per 8 s clip). Prompt must say "ONE continuous shot, no cuts, same hand and phone, the back of
  the phone is never shown, no logos" – otherwise Veo cuts mid-clip and morphs the phone into an iPhone with logo.
- Flow outputs 24 fps; for smooth motion interpolate locally for €0:
  `ffmpeg -i in.mp4 -an -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -crf 16 out.mp4`
  (ffmpeg via `pip install imageio-ffmpeg`; ~4 min per 8 s clip on the laptop).
- Check the clip with the same checklist (extract a few frames with ffmpeg). Keep the still + an HTML/CSS motion
  fallback in the page so a missing or bad clip never breaks the video.

## 6. Sound
- Voice and sound effects with **ElevenLabs**, unless a cheaper option is good enough. Before paying, compare:
  free/neural TTS (e.g. Edge TTS, OpenAI TTS), a real person reading `voiceover.txt`, and check the event rules
  (some forbid a tool). Drafts always with a free TTS. Final voice only when Handan says so.
- Mux the audio onto the 120 s timeline (one clip per scene placed at its start time).

## 7. Assemble and render
- One HTML page plays the whole video: all scene times and numbers in a `CONFIG` object, `?t=SEC` jumps to a time,
  embedded fonts (no network). Flow clips are `<video>` elements with the still as fallback.
- Render with Playwright Chromium + ffmpeg: first PNG stills at key times for checking, then the real-time video
  (exact length), then mux the voice. Renders and generated clips are not committed.
- Reference implementation to copy from: `video/` in this repo (`video.html`, `record.py`, `voice.py`). Brand and look: skill `carecatalyst-design`.
  (`video.html`, `record.py`, `capture_app.py`, `prep_devices.py`, `voice/`).

## 8. Final check
Watch the whole video: length, every number matches the script sources, text readable long enough, no AI artefacts,
audio in sync. Then open the mp4 for Handan.

## Practical
- Windows: always `PYTHONUTF8=1`; `python -m ...` if `uv` is missing.
- Never commit keys or solution details to public repos.
- With several Claude sessions: one session owns the video folder; use one logged-in browser at a time and
  `browser_close` when done.

## Keep this skill up to date
Whenever a session finds a workflow rule or trick that worked (or Handan states a new preference) for video, images,
animation, voice or style, edit this file right away and tell her in one line what changed. Only general workflow,
never what one specific video shows.
