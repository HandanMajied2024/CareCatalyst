# CareCatalyst Design System (shared by Concept A and B)

One look for both concepts. Every rule here is binding.

## Tokens

```css
:root {
  --font: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #ffffff;          /* page background: always white */
  --fg: #0a0a0a;          /* text: black */
  --muted: #6b6b6b;       /* secondary text, use sparingly */
  --line: #e6e6e6;        /* borders, dividers */
  --surface: #f5f5f5;     /* subtle card fill, chips */
  --red: #e5262b;         /* accent: risk, missed, cancelled, alert */
  --blue: #1f5eff;        /* accent: primary action, links, agent, info */
  --green: #14a44d;       /* accent: done, booked, started, improvement */
  --yellow: #ffc400;      /* accent: pending, waiting, warning (text on it: black) */
  --red-soft: #fdeaea; --blue-soft: #e8efff; --green-soft: #e6f6ec; --yellow-soft: #fff6d6;
  --radius: 20px; --radius-sm: 12px; --pill: 999px;
  --gutter: clamp(20px, 5vw, 72px); /* left/right page margin */
}
```

Font loading (both apps), in index.html `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

## Rules

1. **Inter everywhere.** No Plus Jakarta, DM Sans, JetBrains Mono, or other fonts. Numbers may use `font-variant-numeric: tabular-nums`.
2. **White background, black text.** No tinted page backgrounds (no slate, no blue-grey, no green-grey). Cards are white with a `--line` border or `--surface` fill. Colored blocks only as small accents.
3. **No eyebrows.** No small uppercase / letter-spaced label above a headline ("REGIONAL OVERVIEW", "DEMO", "STEP 1"). Delete them. A headline stands alone. No `text-transform: uppercase` + `letter-spacing` micro labels anywhere.
4. **Accents = primary colors only:** red, blue, green, yellow (tokens above), each with a fixed meaning (see comments). Remove indigo, violet, teal, orange, emerald, amber, sky, slate-blue, etc. Map them to the nearest primary by meaning.
5. **Minimal text.** Remove sentences that explain what the UI already shows. Prefer icon + number + 1–3 word label. Buttons and pills: icon first, short label or icon-only with `aria-label`/`title`. Long explanations go behind a click (details/overlay), not on the page.
6. **Visual over verbal.** Turn lists of numbers into bars, rings, progress bars (number inside the bar), dot rows, or icon tiles. Use lucide icons (Concept A has `lucide-react`; Concept B uses inline SVG).
7. **Bigger type.** Body min 16px (mobile 16, desktop 17–18). Labels min 14px. Headlines: h1 32–48px (clamp), h2 24–32px, h3 20px. Weights 600–800 for headings, 400–500 body. Line-height 1.5 body, 1.15 headings, letter-spacing -0.02em on headings.
8. **Generous margins.** Page content uses `padding-inline: var(--gutter)`; max-width ~1440px on desktop dashboards, centered. Lots of white space between sections (32–64px).
9. **Responsive: mobile (<640), tablet (640–1024), desktop (>1024).** No horizontal page scroll at 360px. Grids collapse to 1 column on mobile, 2 on tablet. Touch targets ≥44px. Tables become cards or scroll inside their own container on mobile. The phone-frame mockup (fixed 430px app shell) should only appear as a frame on desktop; on mobile it is full-bleed; on tablet/desktop the app may use wider multi-column layouts.
10. **Soft, flat surfaces.** Radius 20px cards, pills fully rounded. Shadows very light or none. Optional: one organic airbrush gradient blob behind the hero (very low opacity primary colors), never behind data.
11. **Charts:** the 4 primary colors with their meaning; grey (`#d4d4d4`) for baseline/other. Labels in black/`--muted`, 14px+.
