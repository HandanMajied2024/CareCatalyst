# Video

| | |
|---|---|
| Video URL | `[TODO: YouTube unlisted link]` |
| Length | 2:25 |

Pitch / demo video, rendered from code: `video.html` is the whole video (open it in a browser to preview,
`?t=60` jumps to 60 s, `?audio` plays the mixed sound), `record.py all` renders `CareCatalyst-demo.mp4`.

- Voice and sound effects: ElevenLabs (`voice.py`, cached mp3s in `voice/` and `sfx/`), timing comes from the audio.
- Persona images (Eero and Jenny): generated with Codex image generation, checked for realism.
- App screens: real screenshots of the live demos (Part 1 counties, Part 2 CarePulse).
- Look: skill `carecatalyst-design`, workflow: skill `pitch-video` (both in `.claude/skills/`).

```bash
pip install playwright imageio-ffmpeg && python -m playwright install chromium
PYTHONUTF8=1 python record.py stills 10 60 120   # check frames
PYTHONUTF8=1 python record.py all                # ~25 min
```
