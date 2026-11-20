<!--
DRAFT – NOT PUBLISHED. MLH x DEV Writing Challenge (monthly, Nov 1–30, 2026 ET, $100 per selected project).
Publish on dev.to while signed in with the MLH account linked to the Junction registration.
Easiest: open the official template (dev.to/mlh-hackathon -> "Open submission template") and paste the body below.
Keep the required tags exactly: mlhacks, devchallenge, hackathon (max 4 tags on DEV; optional 4th: ai or healthcare).
Remove all TODO lines and HTML comments before publishing.
-->

---
title: "CareCatalyst: a voice agent that asks cancer patients why they cancel – and shows Finland where care breaks"
published: false
tags: mlhacks, devchallenge, hackathon, ai
---

_This is a submission for the [MLH x DEV Writing Challenge](https://dev.to/mlh-hackathon)_

![Cover: CareCatalyst dashboard](TODO-cover-screenshot.png)

## What I Built

Imagine you live in Inari, in Finnish Lapland. You have a diagnostic appointment for suspected cancer, 415 km away. It's November, it's dark, the roads are icy, and you don't have a car. So you cancel.

In the hospital system, that cancellation looks exactly like one in Espoo. Nobody calls. Nobody asks why.

We kept asking ourselves one question: *what if someone just called and asked?* That's what we built.

Finland has a national cancer strategy (2026–2035). Its Goal 3 is simple to say and hard to deliver: equal and effective cancer care everywhere in the country. One of its indicators is that **patients start treatment within the target times**.

When we started at Junction 2026 in Espoo, working on AstraZeneca's challenge "Equal Care Across Finland", one thing stood out. The system has a rough idea of *why* people drop out of the cancer pathway: distance, transport, weather, scheduling, language, fear, caring for someone at home. It roughly knows *how many* are affected. What nobody knows is *who* it is, at the moment it happens. The patient falls out of the pathway quietly, and that is where regional inequality starts.

So our team, **CareCatalyst** ("Closing gaps. Connecting care."), built a tool for the wellbeing services counties (hyvinvointialueet) that does three things:

1. **Calling Agent**: when a synthetic patient cancels an appointment, an AI care coordinator calls them, asks why, and classifies the reason into a barrier category (Transport, Weather, Scheduling, Accessibility, Language, Other). Then it proposes a concrete next step, for example keeping the slot and arranging Kela-subsidised patient transport, or queuing a human callback from a named care coordinator.
2. **Regional Barrier Map**: every classified call updates an aggregated view of barriers by region and pathway stage. The demo covers three focus regions: Lapland / OYS North, KYS Savo and HUS Uusimaa.
3. **Intervention Simulator + Simulation Lab**: county planners compare interventions (more treatment chairs, a shuttle/transport service, a mobile unit) against a monthly budget and see the expected effect on the Goal 3 target-time risk, with the assumptions shown openly.

All patients in the demo are **synthetic**. No real patient data was used.

## Demo

![Calling agent mid-conversation](TODO-screenshot-calling-agent.png)
![Regional Barrier Map](TODO-screenshot-barrier-map.png)
![Intervention Simulator](TODO-screenshot-simulator.png)

- Video: TODO (YouTube/Loom link, ≤ 2 min)
- Live demo: TODO
- Source code: TODO (repo link – make sure it is public)

The demo flow: a synthetic patient cancels a diagnostic appointment → the agent calls and asks why ("it's too far, I can't drive in this weather") → the reason is classified as Transport/Weather → the agent offers to keep the slot and arrange transport → the regional map and the simulator update.

## How we built it

- **Frontend**: React 19 + TypeScript, Vite, Tailwind CSS 4, Motion and lucide icons.
- **Backend**: a small Express server with a WebSocket (`ws`) bridge. The Gemini API key stays on the server and is never sent to the browser.
- **Risk engine**: a transparent, rule-based score per patient (pathway urgency, age/frailty, distance and weather, language/equity). We deliberately kept this deterministic so a county planner can see why a patient is flagged.
- **Simulation engine**: deterministic and uncertainty-bounded, driven by the live barrier rates from the calls, so the planning view reacts to what the agent has just learned.
- **Tests** for the cancellation flow and the policy model.

## Partner Technologies

**Gemini API (Google DeepMind)** is the core of the agent:

- **Gemini Live** handles the spoken conversation. The browser streams microphone audio over our WebSocket to the server, which keeps a Live session open and streams the agent's audio back. If Live is unavailable, browser speech recognition feeds the same Gemini chat endpoint.
- **Gemini Flash with structured output** (a JSON response schema plus a coordinator system prompt) returns each conversation turn *and* the barrier classification in one machine-readable object. That was the key design decision: the voice conversation stays natural, but what reaches the dashboard is a clean category we can aggregate per region and pathway step.
- No silent fallbacks: if the key, model access or quota fails, the UI shows an error instead of pretending with scripted answers. For a health use case we preferred honest failure over a fake demo.

**Codex (OpenAI)** was our fourth team member. With three people and less than two days, we wrote much of the code together with Codex, and our repo ships an `AGENTS.md` so the agent knows our stack, commands and conventions. TODO: name 1–2 concrete parts Codex built or refactored (e.g. a component or the tests) and add one screenshot of a Codex session.

**ElevenLabs**: TODO – only keep this if the ElevenLabs voice integration is merged before publishing; describe where it is used.

## Challenges we ran into

- **Operator question.** Our first idea was an app run by insurers. Fact-checking showed that private insurers in Finland do not see public cancer appointments, so we reframed the tool for the counties, which already hold the appointment data and are responsible for the Goal 3 waiting-time targets.
- **Real-time voice.** Getting Live audio, a WebSocket bridge and a text fallback to share one conversation state took most of a night. Talking to your laptop at 3 a.m. while pretending to be a patient from Lapland is a special kind of hackathon experience.
- **Privacy by design.** The concept depends on personal health data, so the demo uses only synthetic personas, and the dashboard works with anonymised, aggregated reasons. A real deployment would need per-county integration and explicit, purpose-bound consent (GDPR Art. 9), with no automated decisions about care.
- TODO: one honest, personal bug story from the team (what broke, how you fixed it).

## What's next

- Connect the agent to real "pathway stalled" signals in one pilot county (referral not booked, appointment cancelled, no-show) for one cancer type.
- Put public, aggregate data with a source next to every number (THL waiting-time follow-up, Finnish Cancer Registry). TODO: list the datasets actually used in the final demo.
- Let Gemini read the national cancer strategy documents and cite the page behind each recommendation.
- Longer term: a patient's own health agent that talks agent-to-agent with the county's coordinator, so nobody has to explain their life situation twice.

## Hackathon Experience

We built CareCatalyst at **Junction 2026: European Tech Renaissance** in Espoo, Finland (13–15 November 2026), as a team of three: Youcef Jerbi (team lead), Handan Majied and Hazem Dhaouadi.

Fun fact: this team didn't exist when the hackathon started. Handan switched teams *and* challenges on Saturday, halfway through Junction. Our advice to future hackers: don't do that. Our second piece of advice: if you do it anyway, find teammates who say "great, here's the repo" instead of "are you sure?".

What we'll remember most: TODO 1–2 personal sentences (a mentor conversation with the AstraZeneca team, the night shift, the moment the agent first understood "it's too far" and offered transport).

And the most important lesson wasn't technical. A cancelled appointment is not just a data point. Behind every one of them is a person with a reason, and sometimes all it takes is someone asking.

<!-- After publishing: share the link with the team, on LinkedIn/X and in the Junction community – community response is part of the selection. -->
