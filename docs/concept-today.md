# Concept A: Care Pathway Agent (today)

Repo: [`concepts/today`](../concepts/today) (submodule → [devstar7674-beep/CareCatalyzer](https://github.com/devstar7674-beep/CareCatalyzer))

## Operator

| Operator | Has appointment data? | Role |
|---|---|---|
| **Wellbeing services county** (hyvinvointialue) | ✅ Own patient records (appointments, cancellations, no-shows). Treatment relationship = legal basis. Measures Goal 3 waiting times. | **Main customer.** Fits AZ's wish for a follow-up project with one county. |
| Private insurer (If, LähiTapiola, Pohjola …) | ❌ Only via opt-in app | Extra channel for own customers |
| Kela | Partly (reimbursements, Kela taxi) | Partner for transport and costs |

## Dock onto existing portals

The agent is a module on top of what exists, not a competing app.

- **Maisa** (Apotti): HUS, Helsinki, Vantaa-Kerava (+ Kauniainen). Already has **proxy rights** (relatives can book and message without seeing diagnoses), the model for "agent acts on behalf of the patient".

### Fact check: does Maisa / Apotti have the data we show? (14.11.2026)

| Signal in our demo | Where it lives | Verified |
|---|---|---|
| Booking permit issued (referral accepted) | Maisa: doctor appointments need a **booking permit** from a professional first | ✅ Maisa FAQ, hel.fi |
| Appointment booked / upcoming / past | Maisa **Events** section | ✅ Maisa FAQ |
| Cancelled / rescheduled | Maisa, **only for some appointment types**, otherwise by phone | ✅ partly visible |
| No-show | Recorded in Apotti (the record system), not shown as such in Maisa. FHIR `Appointment.status` has `noshow` / `cancelled` / `booked` / `fulfilled` | ⚠️ via Apotti, not via Maisa |
| Treatment started | Apotti record (HUS cancer centre) | ⚠️ via Apotti |

**Integration path:** Apotti recommends **HL7 FHIR** for all new integrations, offers a **sandbox without real patient data** and a partner ecosystem process. HUS has a "FHIR first" policy. The Finnish SMART App Launch guide lists the `Appointment` resource for Apotti. → The agent is an **Apotti/FHIR integration on the provider side**, Maisa is the patient-facing front end (and the proxy-rights model).

**Caveat (Espoo):** Länsi-Uusimaa (LUVN, incl. Espoo) does **not** use Apotti. Its health centres run another system. But **HUS treats cancer for all of Uusimaa** and runs Apotti, and Maisa is open to everyone living in the HUS area. → For cancer pathway steps at HUS (diagnostics, oncology) the data is in Apotti. The step **primary care referral → HUS** crosses systems for Espoo residents; HUS only sees the referral once it arrives. → Best first operator for the pilot: **HUS** (plus Helsinki / Vantaa-Kerava for the primary-care side).
- **Omaolo**: symptom check, forwards to the health centre.
- Other county systems (Lifecare, Omni360 …): integration per county, because cancer appointments are not stored centrally in Kanta.

## Flow

1. **Signal** from Apotti via FHIR: booking permit not used · cancelled · no-show · treatment started.
2. **Reach out**: the agent calls or chats with the patient.
3. **Ask why**: fear, distance, transport, cost, caring for relatives, unclear information.
4. **Help**:
   - book a free slot that fits
   - Kela travel reimbursement / Kela taxi
   - care comes to the patient: home hospital (kotisairaala), parts of chemo and supportive care at home, blood tests, nurse visits, video visits, mobile screening
   - not at home: surgery, radiotherapy, CT/MRI/PET → organise Kela taxi and escort
   - search for support programs (patient organisations, Cancer Society)
5. **Aggregate**: reasons go anonymised and aggregated into the county dashboard: which pathway step, which reason, which region.

## Legal check (research 14.11.2026)

| Question | Answer |
|---|---|
| Do private insurers see cancer appointments? | **No.** No general access to Kanta. Access only with case-specific consent for claims (Data Protection Ombudsman 2022, KHO 2025:86). Cancer care is almost fully public. |
| Kela? | Sees reimbursements only, purpose-bound by law. |
| Health data for proactive outreach? | Only with explicit, purpose-bound consent (GDPR Art. 9). Findata (Act 552/2019) is research/statistics only. Automated risk profiling is sensitive (GDPR Art. 22). |
| Who really has the appointment data? | The **county** as care provider and the **patient** (MyKanta). |

→ The county runs the agent within its treatment relationship. Everything leaving the county is anonymised and aggregated.
