# Design status (15 Nov, early morning)

Both concepts now share one look. The rules are in [design-system.md](design-system.md).

| | Concept A (`concepts/today`) | Concept B (`concepts/vision`) |
|---|---|---|
| Design unified | ✅ | ✅ |
| Branch | `design-unify` | `design-unify` |
| Pushed | Pitch session merges `origin/main` into it and pushes `origin/design-unify` | ✅ `origin/design-unify` (4c9f23b) |
| Patch backup | [design-patches/today](design-patches/today/) | [design-patches/vision](design-patches/vision/) |

## What changed

- Inter everywhere, white background, black text
- No small uppercase labels above headlines
- Accents only: red = risk / missed, blue = action / agent, green = done, yellow = pending
- Much less text: icon + number + short label, details behind ⓘ or a toggle
- Visuals: risk ring, pathway stepper, region map coloured by barrier rate, barrier tiles with bars, intervention comparison bars, progress bars with the number inside
- Text ≥ 16px, labels ≥ 14px, wide page margins (`clamp(20px, 5vw, 72px)`)
- Responsive: mobile (< 640), tablet (640–1024), desktop (> 1024 with a sidebar in B)

## How to continue

**Concept B:** `git checkout design-unify` (pushed). Or apply the patch on top of `main`:

```bash
cd concepts/vision
git checkout -b design-unify
git am ../../docs/design-patches/vision/*.patch
npm install && npm run dev   # http://127.0.0.1:4174
```

**Concept A:** use the `design-unify` branch once the pitch session has pushed it (`npx vite` for the UI only).

**New UI:** use the tokens (`cc-red`, `cc-blue`, `cc-green`, `cc-yellow`, `cc-*-soft`, `cc-line`, `cc-surface`, `cc-muted` in A; CSS variables from design-system.md in B). Don't add new fonts, colours or eyebrow labels.

## Open

- Demo data: all three regions are ≥ 38/100, so the map is all red.
- Card titles still show "Lapland / OYS North", while the map shows the short name.
