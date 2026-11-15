---
name: carecatalyst-design
description: CareCatalyst brand and look for everything the team makes - pitch deck, video, UI, posters, social images. Inter, white background, black text, soft organic airbrush shapes (never circles), the four primary accents with fixed meaning, the wordmark, and the visual split between Part 1 (for welfare counties) and Part 2 (a personal agent for one person). Use whenever someone builds or edits slides, a pitch deck, a video frame, a UI screen, a thumbnail or any visual for CareCatalyst, or asks for "unser Design", "Branding", "Look", "Folien", "Pitch Deck".
---

# CareCatalyst design

Source of truth: `docs/design-system.md` (tokens and UI rules, binding for both apps) and Handan's GitHub projects
(`gh repo list HandanMajied2024`). This skill adds what the deck, video and other visuals need on top.
If the two disagree, `docs/design-system.md` wins for app UI, this file wins for slides and video.

## 1. Look in one sentence
Apple-like, calm, white. Inter, black type, lots of white space, one soft organic airbrush glow per frame,
icons instead of words, color only as small accents that mean something.

## 2. Tokens (copy as is)
```css
:root{
  --font:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --bg:#ffffff; --fg:#0a0a0a; --muted:#6b6b6b; --line:#e6e6e6; --surface:#f5f5f5;
  --red:#e5262b;    /* risk, missed, cancelled, the gap */
  --blue:#1f5eff;   /* agent, action, link, info */
  --green:#14a44d;  /* done, booked, treatment started, improvement */
  --yellow:#ffc400; /* waiting, pending, warning (black text on it) */
  --red-soft:#fdeaea; --blue-soft:#e8efff; --green-soft:#e6f6ec; --yellow-soft:#fff6d6;
  --radius:20px; --radius-sm:12px; --pill:999px;
}
```
Font: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap`
(for offline video renders embed the woff2 files).

## 3. Type on slides and video (1920x1080)
| Use | Size | Weight |
|---|---|---|
| Headline | 72–112 px, letter-spacing -0.03em, line-height 1.05 | 800 |
| Sub line | 36–44 px, `--muted` | 500 |
| Big number | 160–240 px, tabular-nums | 800 |
| Label / caption | 28–32 px (never below 24) | 500–600 |

- One message per slide, max ~12 words on screen. The rest goes into the speaker notes or the voiceover.
- **No eyebrows**: no small uppercase letter-spaced label above a headline. A headline stands alone.
- Margins: at least 120 px left/right on 1920 px. Content aligned to a simple left edge or centred, not both.

## 4. Organic airbrush (signature effect)
Soft, blurred, **irregular organic shapes** (like Lovable / Gemini glows). Never perfect circles, never rings,
never hard gradients, never behind data or small text.
- Build them from SVG blob paths (random smooth curves), filled with a primary color, `filter: blur(80–140px)`,
  opacity 0.25–0.45, 1–3 shapes per frame, bleeding off an edge or a corner.
- Colors per meaning: blue + green = agent and care working; a touch of yellow = warmth, personal life (Part 2);
  red only for the problem slide.
- In video, let the shapes drift and morph slowly (8–20 s per loop, transform + path morph), never pulse.

```html
<svg class="air" viewBox="0 0 800 600" aria-hidden="true">
  <defs><filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter></defs>
  <path filter="url(#b)" fill="#1f5eff" opacity=".35"
    d="M420 80C560 60 700 150 690 290 680 420 560 470 450 520 330 575 170 540 120 420 70 300 150 210 240 150 300 110 350 90 420 80Z"/>
  <path filter="url(#b)" fill="#14a44d" opacity=".25"
    d="M200 330C260 260 400 280 460 360 520 440 470 560 360 570 250 580 120 520 130 440 135 390 160 370 200 330Z"/>
</svg>
<style>.air{position:absolute;inset:-20%;width:140%;height:140%;pointer-events:none;z-index:0}</style>
```

## 5. Brand
- Name: **CareCatalyst**. Claim: **Closing gaps. Connecting care.**
- Wordmark: "CareCatalyst" in Inter 800, black, letter-spacing -0.03em, preceded by the mark.
- Mark = the story's leitmotiv, a dot on a line: `Institution ●────○ Person`. Line `--line` grey 4 px, filled
  dot `--blue`, hollow dot black outline. In the deck the filled dot moves from left (today, institution) to right
  (tomorrow, the person). The closing slide shows `○────●`.
- Product names: Part 1 = **CareCatalyst for counties** (Care Pathway Agent, repo `concepts/today`).
  Part 2 = **CarePulse**, the personal agent (repo `concepts/vision`).
- No partner logos (AstraZeneca, Kela, HUS, Maisa) as decoration. Name them in text only when needed.

## 6. Part 1 vs Part 2 must be visible at a glance
Every slide, frame or screen that belongs to one part carries its badge top-left (a pill with icon, not an eyebrow)
and follows that part's visual language.

| | Part 1 · For welfare counties | Part 2 · For one person |
|---|---|---|
| Badge | pill `--blue-soft`, icon *building-2* + "For counties" | pill `--yellow-soft`, icon *user* + "For you" |
| Who | the county care team (HUS first), many patients | Eero, 78, and his dog Jenny |
| Mark | dot left: `●────○` | dot right: `○────●` |
| Visuals | dashboard, map of Finland, patient list, counters, bars | one phone or speaker, home photos, a day plan |
| Airbrush | cool: blue + green | warm: blue + a touch of yellow |
| Framing | wide, many dots/people, laptop or desktop screen | close, one person, phone or smart speaker |
| Time | **Today** (works now, our demo) | **Tomorrow** (vision) |

The bridge slide between them shows both: the dot travels along the line from left to right, and the closing
slide joins them: Eero's agent (Part 2) talks to the county agent (Part 1), agent to agent.

## 7. Icons, images, data
- Icons: lucide (stroke 1.75–2, black or the accent of their meaning). Icon + 1–3 words beats a sentence.
- Photos: realistic, warm Finnish winter light, no AI gloss, no fake text or logos (check with skill `cutout-images`
  and the realism check in `pitch-video`). The Part 2 persona images live in `presentation/assets/eero/`.
- Numbers: big and alone, with a small source line at the bottom (24 px, `--muted`). Every number needs a source
  from `docs/sources.md`.
- Charts: the four primaries with their meaning, grey `#d4d4d4` for baseline. Progress = filled bar with the
  number inside.

## 8. Checklist before you share a slide or frame
- [ ] White background, Inter, black text, no eyebrow labels
- [ ] Only red/blue/green/yellow accents, each with its meaning
- [ ] Airbrush shapes are organic blobs, not circles, and not behind text
- [ ] Part badge present and correct (counties vs you)
- [ ] ≤ 12 words on screen, text ≥ 24 px
- [ ] Every number has a source
