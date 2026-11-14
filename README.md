# CareCatalyst

## ⏰ TODO before submission: Sun 15.11. 09:00 (hard deadline 10:00 Finnish time)

Form texts to copy-paste: [submission/SUBMISSION.md](submission/SUBMISSION.md)

**Required by the form / challenge**

- [x] Project name, punchline, challenge: drafted in [submission/SUBMISSION.md](submission/SUBMISSION.md)
- [ ] **Description**: draft is there, fill the `[TODO]` parts (demo, datasets, tech), keep ≤ 5000 characters
- [ ] **Working live demo** (challenge requirement, 15 % of the score): [demo/](demo) is a placeholder
- [ ] **Goal 3 indicator with real public data** (treatment start within target times, THL): [data/](data) is a placeholder
- [ ] **Source for every number** + limits section: [data/README.md](data/README.md)
- [ ] **Link the two concept repos** (Concept A / Concept B): `./scripts/link-concepts.sh <A-url> <B-url>`
- [ ] **Give judges access to this repo** (make public or add collaborators) and invite Youcef + Hazem

**Optional fields (strongly recommended)**

- [ ] Demo URL (live, opens in a private window)
- [ ] Presentation PDF ≤ 20 MB: [presentation/](presentation) is a placeholder
- [ ] Video URL: [video/](video) is a placeholder
- [ ] Tech challenges: tick only what's used and explain how ([list](submission/SUBMISSION.md#tech-challenge-participation-multi-select))

**Sunday on site**

- [ ] Click "Submit Final" (not just "Save Draft")
- [ ] Save table A115 in the team tab, whole team at peer review by 10:30

---

**Closing gaps. Connecting care.**
Junction 2026 · AstraZeneca challenge *"Equal Care Across Finland"*

> Nobody should have to explain their life situation again and again to get cancer care.

This is the **main repository** of team CareCatalyst. It holds the shared story, the architecture and the pitch, and links the two concept repositories:

| | Concept | Horizon | Who runs it | Repo |
|---|---|---|---|---|
| **A** | **Care Pathway Agent**: the welfare area notices when a patient's pathway stalls and helps | **Today** (buildable now) | Wellbeing services counties (hyvinvointialueet), docked onto existing portals like **Maisa** | [`concepts/today`](concepts/today) |
| **B** | **Personal Health Agent**: the patient's own agent, linked to their digital health record, reacts in daily life and books care | **Tomorrow** (vision) | The patient (their own agent, consent-based, EHDS) | [`concepts/vision`](concepts/vision) |

```
   TODAY (A)                                     TOMORROW (B)
   Institution reaches out to the patient   →    The patient's own agent talks to institutions
   ┌──────────────────────────┐                  ┌──────────────────────────┐
   │ Welfare area / Maisa     │                  │ Personal agent           │
   │ signal: referral not     │   same pathway   │ knows daily life, health │
   │ booked, cancelled,       │   signals, same  │ record, limits, schedule │
   │ no-show                  │   help catalog   │                          │
   │ → agent calls, asks why, │  ─────────────►  │ → books, arranges Kela   │
   │   offers help            │                  │   taxi, talks agent-to-  │
   │ → anonymous aggregates   │                  │   agent with A           │
   └──────────────────────────┘                  └──────────────────────────┘
```

**A is the product we pitch for the challenge. B is where it goes.** In B, the patient's agent talks to the agent from A. That is the closing scene of the pitch.

## Quick links

| Doc | What's inside |
|---|---|
| [docs/overview.md](docs/overview.md) | Problem, both concepts, how they connect (2-minute read) |
| [docs/concept-today.md](docs/concept-today.md) | Concept A in detail: operator, signals, help catalog, legal check |
| [docs/concept-vision.md](docs/concept-vision.md) | Concept B in detail: personal agent, digital health record, the Espoo scene |
| [docs/architecture.md](docs/architecture.md) | Shared building blocks and data flow of A and B |
| [docs/pitch.md](docs/pitch.md) | 5-minute pitch arc and demo script |
| [docs/challenge-fit.md](docs/challenge-fit.md) | Requirements, judging criteria, Goal 3 indicator, open gaps |
| [docs/sources.md](docs/sources.md) | Public data sources and references |

## Repository layout

```
CareCatalyst/
├── README.md            ← you are here
├── submission/          ← copy-paste texts for the Junction form
├── demo/                ← live demo (required)          [placeholder]
├── data/                ← public datasets + synthetic personas [placeholder]
├── presentation/        ← pitch deck PDF                [placeholder]
├── video/               ← demo / pitch video link       [placeholder]
├── docs/                ← shared concept, architecture, pitch
├── concepts/
│   ├── today/           ← Concept A repo (git submodule)
│   └── vision/          ← Concept B repo (git submodule)
└── scripts/
    └── link-concepts.sh ← links the two concept repos as submodules
```

## Getting started

```bash
git clone --recurse-submodules <this-repo-url>
# already cloned without submodules:
git submodule update --init --recursive
```

Link the concept repos (one-time, once the URLs are known):

```bash
./scripts/link-concepts.sh <url-of-concept-A-repo> <url-of-concept-B-repo>
```

## Team

Youcef Jerbi (lead) · Handan Majied · Hazem Dhaouadi

## Data rule

The challenge allows **public, aggregate data only**. All demos use public aggregates (with a source for every number) and **synthetic personas**. No real patient data in any repo.
