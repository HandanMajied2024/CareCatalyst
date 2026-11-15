# Architecture: shared building blocks

Both concepts use the same core. A puts it on the institution's side, B on the patient's side.

```mermaid
flowchart LR
  subgraph Sources
    P[Portal signals<br/>Maisa / Apotti / Lifecare]
    H[Digital health record<br/>MyKanta / EHDS]
    D[Public aggregates<br/>THL, Syöpärekisteri, Kela, NORDCAN]
  end

  subgraph A[Concept A: Care Pathway Agent · county]
    A1[Pathway state<br/>referred → booked → treated]
    A2[Outreach agent<br/>call / chat, asks why]
  end

  subgraph B[Concept B: Personal Health Agent · patient]
    B1[Personal context<br/>health, limits, schedule]
    B2[Personal agent<br/>voice, books, applies]
  end

  C[(Shared help catalog<br/>slots · Kela taxi · kotisairaala<br/>video visit · programs)]
  R[(Reason taxonomy<br/>fear · distance · transport<br/>cost · caregiving · info)]
  DB[County dashboard<br/>drop-outs by step × reason × region<br/>+ Goal 3 indicator]

  P --> A1 --> A2
  H --> B1 --> B2
  A2 --> C
  B2 --> C
  A2 --> R
  B2 <-->|agent-to-agent| A2
  R -->|anonymised, aggregated| DB
  D --> DB
```

## Shared pieces

| Block | Used by | Notes |
|---|---|---|
| Pathway state model | A, B | Steps: detection → referral → diagnosis → treatment start. Events: booked, cancelled, no-show, started |
| Reason taxonomy | A, B | Same categories so aggregates are comparable |
| Help catalog | A, B | Kela travel/taxi, kotisairaala, video visit, free slots, support programs, each with source |
| Dashboard | A | Drop-outs per step × reason × county, next to the Goal 3 indicator (definition from the national strategy; values in the demo are synthetic) |
| Agent-to-agent protocol | B ↔ A | Minimal: request slot, confirm transport, share consented facts only |

## Data boundaries

- Personal data stays with its owner (county for A, patient for B).
- Only anonymised aggregates leave (to dashboards, AZ).
- Hackathon demo: synthetic patients and synthetic regional values. Public are only the region boundaries (Statistics Finland, CC BY 4.0) and the cited key figures.
