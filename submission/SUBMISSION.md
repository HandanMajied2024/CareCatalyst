# Junction submission form: copy-paste source

Form: hackjunction.app → Event 45 → Project. **Deadline: Sun 15.11. 10:00 Finnish time** (the platform partly shows 09:00, so aim for 09:00).
Fields marked ⬜ are still open.

---

## Project Name (required, ≤ 30 characters)

```
CareCatalyst
```

## Punchline (required, ≤ 200 characters)

```
Finland knows why patients drop out of the cancer pathway, but not who. CareCatalyst finds them at the moment their pathway stalls, asks why and helps, and shows counties where care breaks.
```

## Challenge (required, exactly 1 main challenge)

```
Equal Care Across Finland (AstraZeneca)
```

## Description (required, ≤ 5000 characters, Markdown)

> ⬜ Update the parts marked [TODO] once the demo, data and tech are final. Check the length before pasting (`wc -m`).

```markdown
## The problem
Finland knows **why** people drop out of the cancer pathway (fear, distance, transport, cost, caring for relatives) and roughly **how many** are affected. Nobody knows **who** it is at the moment it happens. Without a person, nobody can reach out and solve the problem together. That is where inequality starts: between referral, diagnosis and treatment start, patients get lost silently, and more often in regions far from the treatment centres.

## Our solution today: the Care Pathway Agent
A layer for the **wellbeing services counties**, built on top of the patient portals they already run (first of all **Maisa / Apotti**: HUS, Helsinki, Vantaa-Kerava). No new app for patients.

1. **Signal**: the portal shows that the pathway stalls: referral received but not booked, appointment cancelled, no-show.
2. **Reach out**: the agent contacts the patient (chat or call) and **asks why**.
3. **Help**: it offers what already exists: a slot that fits, **Kela travel reimbursement / Kela taxi**, home hospital (**kotisairaala**) or video visits where medically possible, support programs.
4. **Learn**: the reasons flow back **anonymised and aggregated** into a county dashboard: drop-outs by **pathway step × reason × region**, next to the national Goal 3 indicator.

The county is the right operator: it already holds the appointment data, has the treatment relationship as legal basis and is responsible for the Goal 3 waiting-time targets. Private insurers do not see cancer appointments in Finland (we checked: Data Protection Ombudsman 2022, KHO 2025:86), so they can only join as an opt-in channel. Kela is the partner for transport.

## Goal 3 indicator
We track **"patients start treatment within the target times"** (National Cancer Strategy 2026–2035, Goal 3; THL Ohjaus 21/2016) per county and show which pathway step and which reason drive the delays.
[TODO: name the counties/years and the exact figure source used in the demo]

## Concrete proposals
1. **Pilot in one county (HUS/Uusimaa)**: connect the agent to Maisa signals (not booked, cancelled, no-show) for one cancer type.
2. **Transport by default**: when the reason is distance or mobility, the agent starts the Kela taxi / travel reimbursement process directly.
3. **Care to the patient**: route suitable follow-ups to video visits and home hospital; keep surgery, radiotherapy and imaging in the clinic with arranged transport.
4. **Reason reporting**: add anonymised drop-out reasons per pathway step to the county's cancer monitoring next to the THL waiting-time indicator.

## Demo
[TODO: one sentence on what the live demo shows + link]
A synthetic patient cancels a diagnostic appointment → the agent asks why ("too far, can't drive") → offers Kela taxi and a fitting slot → the county dashboard updates the drop-out reason at that pathway step, next to the Goal 3 indicator.

## Data and limits
- Public, aggregate data only, with a source for every number: [TODO: list the datasets actually used, e.g. THL/Sotkanet, Finnish Cancer Registry, Kela open data].
- All people in the demo are **synthetic**. No patient data was used.
- Real deployment needs per-county integration (Apotti, Lifecare …) and explicit, purpose-bound consent (GDPR Art. 9); no automated decisions about care (Art. 22).

## The vision: everyone has their own agent
Tomorrow, the patient's **personal health agent**, linked to their digital health record (MyKanta, European Health Data Space), notices symptoms in daily life, knows their limits and schedule, and books care that fits. It talks **agent-to-agent** with the county's Care Pathway Agent. Nobody has to explain their life situation again.

## Tech
[TODO: stack + which tech challenges and **how** each was used]

## Team
Youcef Jerbi · Handan Majied · Hazem Dhaouadi
```

## Links (optional fields)

| Field | Value | Status |
|---|---|---|
| Project Demo URL | `[TODO]` (live URL of the demo) | ⬜ |
| Source Code URL | `https://github.com/HandanMajied2024/CareCatalyst` (**make public or give judges access before submitting**) | ⬜ |
| Video URL | `[TODO]` (see [`video/`](../video)) | ⬜ |
| Other Link | `[TODO]` (e.g. dashboard or concept B demo) | ⬜ |
| Presentation | `presentation/CareCatalyst.pdf` (≤ 20 MB, see [`presentation/`](../presentation)) | ⬜ |

## Tech Challenge Participation (multi-select)

Only tick what is really used, and explain **how** in the description.

| Tech challenge | Possible use | Used? |
|---|---|---|
| Gemini API | Agent dialogue, reason classification, strategy PDFs with page citations | ⬜ |
| MLH ElevenLabs | Agent's voice for the outreach call / Espoo scene | ⬜ |
| Oxylabs | Web search for support programs, sources shown | ⬜ |
| Modal | Hosting the live demo | ⬜ |
| Codex | Code written with Codex (proof: commits) | ⬜ |
| MLH DEV | Blog post about the project | ⬜ |

## Before clicking "Submit Final"

- [ ] All ⬜ above filled, no `[TODO]` left in the description
- [ ] Description ≤ 5000 characters, punchline ≤ 200
- [ ] Repo is accessible for judges
- [ ] Demo URL opens in a private browser window
- [ ] Table saved in the team tab on Sunday (A115), whole team at peer review by 10:30
