# Overview

## The problem

AstraZeneca and others know **why** people drop out of the cancer pathway (fear, distance, transport, cost, caring for relatives) and **how many** are affected per reason.
Nobody knows **who** it is. Without a person, nobody can reach out and find a solution together. **That is where inequality starts.**

The pathway: detection → referral (primary care → specialist) → diagnosis → start of treatment. People get lost between the steps.

## Concept A: Care Pathway Agent (today)

- Run by the **wellbeing services county** (hyvinvointialue). It already has the appointment data and the treatment relationship as legal basis.
- **No new app.** The agent is a layer on top of existing portals, first of all **Maisa** (Apotti: HUS, Helsinki, Vantaa-Kerava). HUS treats cancer for all of Uusimaa.
- Signals: referral received but not booked · appointment cancelled · no-show · treatment started.
- When the pathway stalls, the agent reaches out (call/chat), **asks why**, and helps: free slots, Kela travel reimbursement / Kela taxi, home hospital (kotisairaala), video visits, support programs.
- The reasons flow back **anonymised and aggregated** to the county (and AZ): where in the pathway and why people get lost. That is the dashboard.
- Insurers can offer the same blueprint to their own customers as an opt-in channel. Kela is the transport partner.

Details: [concept-today.md](concept-today.md)

## Concept B: Personal Health Agent (vision)

- Everyone has a personal AI agent, like everyone has a phone today.
- The agent is linked to the person's **digital health record** (MyKanta today, the EHDS patient right to share data tomorrow). The person decides what it can see.
- It notices things in daily life (back pain, rising risk score), knows the person's limits (visually impaired, no public transport) and schedule (bingo class), and books care that fits.
- It talks **agent-to-agent** with the county's agent from Concept A, with the insurer and with the doctor's agent.

Details: [concept-vision.md](concept-vision.md)

## How A and B connect

| | A: today | B: tomorrow |
|---|---|---|
| Who starts the contact | Institution → patient | Patient's agent → institution |
| Knows the person's situation | Asks each time | Already knows it |
| Data access | County's own records + patient consent | Patient-controlled health record (EHDS) |
| Help catalog | Kela taxi, home care, slots, programs | **Same catalog**, booked by the personal agent |
| Output for decision makers | Aggregated drop-out reasons per county and pathway step | Same aggregates, fed by agents |

**The shift:** from "institutions reach out to individuals" to "individuals have agents that speak for them with institutions". A builds the institutional side that B's personal agents will talk to.
