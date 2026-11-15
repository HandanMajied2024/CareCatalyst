---
name: pitch-deck
description: How the CareCatalyst team builds and edits the pitch deck - story from docs/pitch.md, look from the carecatalyst-design skill, one HTML file with 1920x1080 slides, exported to PDF and optionally PPTX. Use when someone asks for the pitch deck, slides, Folien, Präsentation, a single slide, speaker notes, or a PDF of the deck.
---

# Pitch deck workflow

1. **Story first.** Read `docs/pitch.md` (timing, parts, demo script), `docs/business-case.md`, `docs/sources.md`.
   The red line: today the centre of gravity is the institution (Part 1, counties, our live demo), tomorrow it is the
   person (Part 2, Eero and Jenny, personal agent). Part 1 is the runway for Part 2: agent to agent.
2. **Look.** Load skill `carecatalyst-design` and follow it strictly (badges for Part 1 / Part 2, organic airbrush,
   ≤ 12 words per slide, no eyebrows).
3. **Build** `presentation/deck.html`: one self-contained file, each slide a `<section class="slide">` of
   1920x1080 scaled to the window, arrow keys / click to move, `?s=N` opens slide N, speaker notes in
   `<aside class="notes">` (press `N` to show). Images from `presentation/assets/`, app screenshots from the real app
   (Playwright), never invented UI.
4. **Slide order (5 min):** Cold open (the call) → Problem: WHY ✓ HOW MANY ✓ WHO ✗ → Where it breaks + Goal 3
   indicator → Part 1 today + live demo → proposals, business case, pilot (HUS) → bridge: the dot moves →
   Part 2: Eero and Jenny → agent to agent + claim "Closing gaps. Connecting care." + QR to the live demo.
5. **Check** every slide at 1920x1080 and at a phone width with Playwright screenshots; run the checklist at the end
   of `carecatalyst-design`; every number has a source line.
6. **Export:** PDF with Playwright (`page.pdf` with width 1920px, height 1080px, printBackground) to
   `presentation/CareCatalyst-deck.pdf`. Only if someone asks for PowerPoint, use the pptx skill.
7. **Parallel work:** one person owns `deck.html` at a time; others send slide changes as small edits.
   Commit `deck.html` and assets, not renders.
