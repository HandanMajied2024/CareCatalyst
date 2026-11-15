# Data

Rule of the challenge: **public, aggregate data only, a source for every number.** No patient data in any repo.

## Where the data lives today

| What | Where | Status |
|---|---|---|
| Synthetic patients (3 focus regions: Lapland/OYS, North Savo/KYS, Uusimaa/HUS) | [`concepts/today/src/data/patients.ts`](../concepts/today/src/data/patients.ts) | ✅ in the demo, marked synthetic |
| Barrier categories (reason taxonomy) | [`concepts/today/src/types/careconnect.ts`](../concepts/today/src/types/careconnect.ts) | ✅ |
| Intervention model (shuttle, Kela vouchers, navigator) | [`concepts/today/src/utils/simulationEngine.ts`](../concepts/today/src/utils/simulationEngine.ts), [`policyModel.ts`](../concepts/today/src/utils/policyModel.ts) | ⚠️ numbers are model assumptions, some evidence lines need a real source (see below) |
| Strategy PDFs | [`concepts/today/public/assets/aistudio/`](../concepts/today/public/assets/aistudio) | ✅ |
| Business-case figures with sources | [`docs/business-case.md`](../docs/business-case.md) | ✅ |

## Public figures we can show (all verified, 14.11.2026)

| Figure | Value | Source | Use in demo |
|---|---|---|---|
| New cancers / deaths 2024 | 38 853 / 13 490 | Finnish Cancer Registry, Syöpä 2024 | Header / problem slide |
| Screening participation lowest in | Helsinki, Vantaa-Kerava, Länsi-Uusimaa (lowest area < 68 %, target ≥ 80 %) | Cancer Registry screening 2024 | HUS region card |
| Stage recorded | 42 % national, 60 % best region | Cancer Registry 2024 | "data gap" argument |
| Kela travel reimbursements 2025 | €364 m, 610 000 people, €224 m to 65+ | Kela | Kela-voucher intervention |
| Kela taxi 2025 | 3.8 m trips, €227 m, pooling saved > €7 m | Kela | Shared-shuttle intervention (**replace** the unverified "Lapland & Kainuu pooling pilot" line) |
| Unused hospital appointments | 4.0 % (Pirkanmaa 2025) | Pirha | No-show baseline |
| Navigator calls in cancer clinics | no-shows 17.5 % → 10.2 % | Percac-Lima 2015 (RCT) | Navigator intervention effect |

## Evidence lines in the demo code that need fixing

| File | Claim | Problem | Fix |
|---|---|---|---|
| `simulationEngine.ts` | "Kela medical transport pooling pilot benchmarks in Lapland & Kainuu" | no source found | Use Kela 2025: pooling saved > €7 m nationwide |
| `patients.ts` (KYS) | "Highest 75+ frailty share in Finland" | not verified | Check Sotkanet (share 75+ by area) or soften to "high 75+ share" |
| `patients.ts` (OYS) | ">150–415 km" | plausible, not sourced | Add distance source or say "up to ~400 km" |
| `policyModel.ts` | cost per hospital slot 4 200 €, car 2 800 €, mobile unit 32 000 € | model assumptions | Label "assumption" in the UI |

## Still open (not yet in the repo)

| File | What | Source to use | Status |
|---|---|---|---|
| `goal3_treatment_start.csv` | **Goal 3 indicator**: treatment start within target times per area | THL hoitoonpääsy (Ohjaus 21/2016); if no clean table → use HUS waiting lists ("hoitoa odottavat potilaat erikoisaloittain", hus.fi) and say so | ⬜ |
| `screening_by_area.csv` | Screening participation per welfare area | Cancer Registry yearly screening reports | ⬜ |
| `lung_pathway_by_area.csv` | Lung cancer diagnostics/treatment by area | Cancer Registry *Keuhkosyöpä Suomessa* (2024) | ⬜ |

## Limits

- Regional Goal 3 waiting-time figures are not published as one clean open table; THL notes referral and first-treatment data still need reliability checks.
- All patients in the demo are synthetic. Intervention effects are model estimates based on the studies above, not measured in Finland.
