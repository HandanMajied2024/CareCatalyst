# Demo

The challenge needs a **working live demo** (slides are not enough, 15 % of the score).
The demo code lives in **[`concepts/today`](../concepts/today)** (submodule → `devstar7674-beep/CareCatalyzer`, internal name POLKU-3). No separate demo code here.

## What is built

| Tab | What it shows | Challenge criterion |
|---|---|---|
| **1 · Calling Agent** | Agent calls a synthetic patient, asks why the appointment was cancelled, classifies the barrier. Voice via Gemini Live, fallback browser speech | Insight (who + why) |
| **2 · Regional Barrier Map** | 3 focus regions (Lapland/OYS, North Savo/KYS, Uusimaa/HUS), barriers per region | Gap + where in the pathway |
| **3 · Intervention Simulator** | Shuttle, Kela vouchers, navigator: effect vs. cost | Actionability (30 %) |
| **Simulation Lab** | Budget model: chairs, cars, mobile unit | Actionability |

## Run locally

```bash
cd concepts/today
npm install
echo "GEMINI_API_KEY=..." > .env   # never commit
npm run dev                        # http://localhost:3000
```

## Demo script (2 minutes, for the jury)

1. **Uusimaa/HUS** region: synthetic patient cancelled the diagnostic appointment.
2. **Calling Agent** asks why → "too far / can't drive" or "scared".
3. Agent offers help: **Kela taxi**, a fitting slot, video visit.
4. **Barrier Map** updates: reason × pathway step × region.
5. **Simulator**: "what if HUS adds navigator calls" → fewer drop-outs, cost per patient (business case: [docs/business-case.md](../docs/business-case.md)).
6. Point to the **Goal 3 indicator** with source.

## Open

| | | Status |
|---|---|---|
| Goal 3 indicator visible in the UI, with source | see [data/README.md](../data/README.md) | ⬜ |
| Sources shown under every number in the UI | business-case figures | ⬜ |
| Fix unverified evidence lines | list in [data/README.md](../data/README.md#evidence-lines-in-the-demo-code-that-need-fixing) | ⬜ |
| Live URL (opens in a private window) | `[TODO]` | ⬜ |
| Backup: screen recording in case Wi-Fi fails | [video/](../video) | ⬜ |
