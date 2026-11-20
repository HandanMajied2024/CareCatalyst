# CareCatalyst – Junction submission texts (LOCAL ONLY, never commit)

## Punchline (≤ 200 chars)

Finland knows why patients drop out of the cancer pathway, but not who. CareCatalyst calls them when their pathway stalls, asks why, helps, and shows counties where care breaks.

## Description (≤ 5000 chars, Markdown)

## The problem
Finland roughly knows **why** people drop out of the cancer pathway (distance, transport, weather, scheduling, language, fear, cost), but not **who** it is when it happens. A cancelled diagnostic visit in Lapland looks the same as one in Espoo: nobody calls, nobody asks why, the reason is never recorded. That is where regional inequality starts, between referral, diagnosis and treatment start.

## Solution today: the Care Pathway Agent
A tool for the **wellbeing services counties**, first pilot **HUS** (cancer care for all of Uusimaa), docked onto the portals they already run (Maisa / Apotti via FHIR). No new patient app.

**Demo flow (live, synthetic patients):**
1. A synthetic patient on a cancer fast-track cancels or misses an appointment.
2. An AI care coordinator calls (Gemini Live voice or text), asks for the reason exactly once and classifies the barrier: Transport, Weather, Scheduling, Accessibility, Language, Fear/Anxiety, Financial, Other. Acute symptoms raise a nurse alert.
3. It proposes a next step, e.g. keep the slot + Kela-subsidised transport, or a human coordinator callback. The patient's risk score updates.
4. **Regional summary**: reasons are aggregated on a map of Finland's 19 regions.
5. **Regional support**: planners compare shared transport, travel support and care coordination against a budget, assumptions shown openly.

## Goal 3 indicator
National Cancer Strategy 2026–2035, Goal 3: **"patients start treatment within the target times"** (THL Ohjaus 21/2016). Each cancellation or no-show threatens it; the risk engine flags patients whose target timeframe is at risk, and the dashboard shows which reason and region drive it.

## Concrete proposals for counties
1. **Pilot at HUS**: connect the agent to Apotti signals (referral not booked, cancelled, no-show) for one cancer type, e.g. lung cancer fast-track.
2. **Never cancel silently**: before a fast-track slot is released, one call asks why and offers help; unresolved cases go to a named human coordinator.
3. **Transport by default, with Kela**: for distance or mobility, start Kela travel reimbursement / Kela taxi during the call, not after a missed visit.
4. **Care to the patient**: route suitable steps to video visits or home hospital (kotisairaala); surgery, radiotherapy and imaging stay in the clinic with transport.
5. **Report reasons**: add anonymised, aggregated drop-out reasons per pathway step and region to county cancer monitoring, next to the Goal 3 indicator.

## Data and privacy
- All patients, appointments and transcripts are **synthetic**. No real patient data.
- Public sources: Statistics Finland, Regional division 2026 (boundaries, CC BY 4.0); National Cancer Strategy 2026–2035 and roadmap 2026–2031 (STM).
- Planner costs are labelled assumptions; map colours are outreach thresholds, not cancer prevalence.
- Real use needs county integration and purpose-bound consent (GDPR Art. 9). The agent never diagnoses or decides on care (Art. 22).

## Vision: everyone has their own agent
**CarePulse** (scripted prototype): Eero, visually impaired, in Espoo with his dog Jenny. His personal agent knows his limits, proposes an 08:00 visit in Helsinki before bingo with 07:00 transport, and shares data with clinic, insurer and transport agents only with consent per recipient. Tomorrow it talks **agent-to-agent** with the county's agent. Nobody has to explain their life again.

## Built with Gemini
**Problem:** cancellation reasons are lost in free-text calls, so regions cannot see what blocks patients.
**Integration** (server-side, `@google/genai`): **Gemini Live** runs the voice call; browser audio streams over a WebSocket to the server's Live session, which returns audio and transcriptions with barge-in. **Gemini Flash with structured output** handles text turns and end-of-call classification; a JSON schema forces reply, outcome, barrier category, summary, action and nurse alert. One shared coordinator prompt; no scripted fallback.
**Novel:** every conversation becomes a typed equity record that updates risk, the regional map and the planner.
**Why Gemini:** one SDK for low-latency native audio and schema-constrained JSON, so voice and data share one prompt and taxonomy; Flash keeps outreach cheap and fast.

## Built with Codex
We built the app with OpenAI Codex as our coding agent (frontend, Express/WebSocket server, risk and simulation models, tests). The repo ships an `AGENTS.md` for coding agents.
