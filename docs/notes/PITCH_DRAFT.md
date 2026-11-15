# CareCatalyst – Pitch Draft v1

Stand: So 15.11. ~03:30 FI. Lokal, nicht committen (Vertraulichkeit bis zur Abgabe).
Zahlen gegengeprüft → `pitch/FACTCHECK.md` (✅ eingearbeitet). Deck: https://claude.ai/artifact/QusGuDBgCPz9xC1WGwtFsd

---

## Die rote Linie: „Center of Gravity“

> **Heute liegt der Schwerpunkt der Krebsversorgung bei der Institution.**
> Der Patient fährt hin, wartet und erklärt sein Leben jedes Mal neu. Wer das nicht schafft, fällt still heraus.
>
> **Wir bauen dort, wo der Schwerpunkt heute liegt** (Teil A, beim Wohlfahrtsbezirk, funktioniert jetzt, mit heutiger Agentic AI).
> **Und wir zeigen, wohin er sich bewegt** (Teil B, zum Menschen, jeder hat einen eigenen Agenten).
> Die Pointe: **Teil A ist die Landebahn für Teil B.** Der Bezirks-Agent, den wir heute bauen, ist genau der, mit dem morgen die persönlichen Agenten sprechen.

Visuelles Leitmotiv für alle Folien: **ein Punkt auf einer Linie** `Institution ●────────○ Mensch`.
Auf jeder Folie steht der Punkt woanders. Im Finale wandert er nach rechts.

**Ein Satz zum Merken (Clarity-Kriterium, „in 2 Minuten verstanden“):**
> *We know why patients drop out of cancer care, and how many. We don't know **who**. CareCatalyst finds them the moment their pathway stalls.*

---

## Pitch-Script, 5 Minuten (Peer Review + AZ-Jury), Englisch

| # | Zeit | Folie | Wer |
|---|---|---|---|
| 0 | 0:00–0:25 | Cold Open: der Anruf | Speaker 1 + Demo-Laptop |
| 1 | 0:25–1:05 | Problem: „We don't know who“ | Speaker 1 |
| 2 | 1:05–1:30 | Wo es bricht + Ziel-3-Indikator | Speaker 1 |
| 3 | 1:30–3:00 | Lösung heute + **Live-Demo** | Speaker 2 (Demo) |
| 4 | 3:00–3:40 | 4 Vorschläge + Business Case + Pilot | Speaker 3 |
| 5 | 3:40–4:35 | Der Schwerpunkt verschiebt sich: Eero & Jenny | Speaker 1 |
| 6 | 4:35–5:00 | Agent-zu-Agent + Schluss | Speaker 1 |

### 0 · Cold Open (0:25): Der Anruf, den heute niemand macht
*Bühne dunkel bzw. Folie schwarz. Vom Demo-Laptop läuft der echte Agent-Anruf (Gemini Live), 2–3 Sätze:*

> **Agent:** „Hei Matti, this is your care team. Your CT scan is on Thursday. Is everything okay for getting there?“
> **Matti:** „I have to cancel… there's no bus from Kemi that morning.“
> **Agent:** „I understand. Kela can cover a taxi. Shall I book one for you?“
> (= exakt der Demo-Patient Matti Heikkinen, Kemi, aus Teil A)

**Speaker 1:** *„This phone call doesn't exist in Finland today.
Matti would simply… not show up. And nobody would ever know why.“*

> Fallback: Audio vorher aufnehmen (MP4/WAV), falls Netz/Gemini hängt.

### 1 · Problem (0:40)
> *„Every year, almost **39,000** people in Finland hear the word cancer.* ⚑
> *We actually know a lot about the ones who get lost on the way to treatment. We know **why**: fear, distance, no car, cost, caring for someone at home. We know roughly **how many**.*
> *What we don't know is **who**. And without a name, nobody can call. Nobody can help.*
> ***That is where inequality starts.**“*

Folie: drei Wörter groß, zwei abgehakt, eins rot: **WHY ✓ · HOW MANY ✓ · WHO ✗**

### 2 · Wo es bricht (0:25)
> *„It happens between the steps: detection, referral, diagnosis, treatment start.
> **Almost one in three** Finnish cancer patients feel their diagnosis came too late.* *Distance matters: in one Finnish study, lung cancer patients living more than 50 km away had about **1.5×** the risk of dying within a year.* (31 % fliegt raus: Roche-Umfrage von 2017)
> *And it's not only Lapland: screening participation is lowest right here, in **Helsinki and Uusimaa**.* ⚑
> *The national cancer strategy wants every patient to **start treatment within the target times**. That's Goal 3. But that indicator has **no public number yet**. Finland can't see where patients drop out. Our pathway events produce exactly that data.“*

Folie: Pfad mit 4 Schritten, rote Lücken zwischen den Schritten, Badge „Goal 3 · Treatment within target times (THL 21/2016)“.

### 3 · Lösung heute + Live-Demo (1:30)
> *„So we built where the center of gravity is **today**: at the welfare county. It already has the appointment data and the treatment relationship. No new app. CareCatalyst docks onto **Apotti and Maisa** via FHIR.*
> *Four steps: **Signal** – a referral not booked, a cancelled scan, a no-show. **Reach out** – the agent calls. **Ask why.** **Help** – with what already exists: a slot that fits, a Kela taxi, a video visit, home hospital.*
> *Let me show you.“*

**Live-Demo (Klickpfad kommt aus dem Demo-Check, siehe unten):**
1. Synthetische Patientin, Bezirk Uusimaa: Überweisung da, CT **abgesagt** → Signal rot.
2. Agent ruft an (live) → Grund wird erkannt: **Transport**.
3. Angebot: Kela-Taxi + passender Termin.
4. Dashboard: Zähler „Transport @ Referral → Diagnosis“ springt hoch, daneben der **Ziel-3-Indikator** pro Bezirk **mit Quelle**.
5. Support-Plan: „Shared transport“ für 32 Patienten in Lapland speichern (Budget sichtbar). Der Simulator ist im aktuellen Stand nicht erreichbar.

**Konkreter Klickpfad (Stand Hazem origin/main):** Patients → Filter Lapland + Pending Call → Matti Heikkinen (Kemi) → Call patient (Gemini Live, Mikro) → Regional summary → Plan support → Save. **Plan B ohne Gemini:** Classification Override → Transport („human in the loop“) → „Other attendance barriers“ aufklappen.

> *„Every call makes the map smarter. For the first time, a county sees not just **how many** patients are late, but **why**, and at **which step**. Anonymised. Aggregated. Patient data never leaves the county.“*

### 4 · Vorschläge + Business Case (0:40)
> *„Four things a county can start on Monday:*
> *1. **Pilot at HUS**, one cancer type, **lung**, 90 days, Apotti FHIR sandbox first.*
> *2. **Transport by default**: if the reason is distance, the agent starts the Kela taxi.*
> *3. **Care comes home** where it's medically possible: video visits, kotisairaala.*
> *4. **Report the why** next to the Goal 3 indicator in the county's cancer monitoring.*
>
> *Does it pay? Hospitals lose around **4 %** of appointments to no-shows.* ⚑ *In a randomized trial, targeted navigator calls cut cancer-care no-shows by **over 40 %**.* ⚑ *Kela already spends **€364 million** a year on travel* ⚑ *– the money is there; what's missing is the moment someone notices. And a stage-IV lung cancer costs **2.6×** more per month than stage I.“* ⚑

> 🔁 **Platzhalter Businessplan**: Preismodell / Kunde / Skalierung aus dem Businessplan mit dem Wirtschaftler hier einsetzen (1 Satz + 1 Zahl).

### 5 · Der Schwerpunkt verschiebt sich (0:55)
*Folie: der Punkt wandert langsam von „Institution“ nach „Mensch“.*

> *„But here's the thing. Today the institution calls the patient. Tomorrow, it's the other way around.*
> *Ten years ago, not everyone had a smartphone. Soon, everyone will have a personal agent. And with the **European Health Data Space**, patients get the right to share their health record with services they choose.*
>
> *Meet **Eero**. 78, Espoo, visually impaired. And this is **Jenny**.* (Foto Hund)
> *Eero is making coffee, asking his assistant about dog food. He bends down – and groans. His back. **Again**.*
> *His agent remembers: he's already seen an orthopedist for this. It came back. Nobody in the system connects those two visits. His agent does.*
> *„Eero, your back is hurting again. I think you should get it checked. The centre is in Helsinki – but don't worry, I know you don't like the bus. Kela can cover a taxi. **Shall I book tomorrow at 8, before your bingo class?**“*
> *„Yes. Thank you.“ – And he goes back to playing with Jenny.“*

> Wichtig (Medical Guardrail, sagen falls gefragt): *„The agent never diagnoses. It only says: this should be checked – and books the check-up.“*

### 6 · Agent-zu-Agent + Schluss (0:25)
> *„And who does Eero's agent talk to, to book that slot and that taxi?
> **The county agent we built today.** Agent to agent. Eero shares only what's needed. He never has to explain his life again.*
> *Today, we close the gaps the system can see. Tomorrow, we close the ones only **you** can see.*
> ***CareCatalyst. Closing gaps. Connecting care.**“*

Letzte Folie: `Institution ○────────● Mensch` + Logo + QR zur Live-Demo.

---

## 3-Minuten-Version (Top 5 / Overall Winner, 3 Min + 3 Min Q&A)
Gleiche Linie, Gewicht auf **Spannung + Vision** (Overall-Jury bewertet weniger die AZ-Kriterien, mehr Story und Wirkung):
| Zeit | Teil |
|---|---|
| 0:00–0:20 | Cold Open: der Anruf (Audio) + „This call doesn't exist today.“ |
| 0:20–0:45 | WHY ✓ HOW MANY ✓ WHO ✗ |
| 0:45–1:45 | Lösung heute: 4 Schritte + Demo im Zeitraffer (Anruf → Dashboard springt) |
| 1:45–2:40 | Schwerpunkt verschiebt sich → Eero & Jenny (kurz) |
| 2:40–3:00 | Agent-zu-Agent + Claim |

---

## Keyword-Checkliste für die AZ-Jury (bewusst wörtlich im Pitch und auf den Folien)

| Kriterium (Gewicht) | Keyword, das fallen muss | Wo |
|---|---|---|
| **Identify the gap** | „who, not just how many“, „regional and socioeconomic differences“ | Folie 1–2 |
| **Locate the gap** | „detection → referral → diagnosis → treatment start“, „between the steps“ | Folie 2, Dashboard |
| **Recommend (am wichtigsten)** | „four things a county can start on Monday“, „county-level and national“ | Folie 4 |
| **Actionability 30 %** | named operator **HUS**, **Apotti/FHIR sandbox**, **Kela taxi**, **kotisairaala**, 90-Tage-Pilot, KPIs | Folie 4 |
| **Insight 25 %** | „why × which step × which region“, „data that doesn't exist today“ | Demo-Dashboard |
| **Data quality & transparency 20 %** | „public, aggregate data only“, „source under every number“, „synthetic personas“, **Limits**-Folie | Dashboard + Anhang |
| **Execution 15 %** | „live demo“, echter Anruf mit Gemini | Folie 3 |
| **Clarity 10 %** | Ein-Satz-Kernbotschaft, WHY/HOW MANY/WHO | Folie 1 |
| **Ziel 3** | „**patients start treatment within the target times**“ (THL Ohjaus 21/2016) | Folie 2 + Demo |
| Formate der Challenge | **early-warning system** (Signal), **monitoring dashboard with recommendations**, **intervention simulation** (Simulator), **AI analyst** | Folie 3 |
| AZ-Business | Lung (AZ-Kernindikation, +14 pp Ziel), Folgeprojekt mit **einem Bezirk**, AZ sieht nur Aggregate (Compliance) | Folie 4 |

---

## Pitch-Deck (Struktur, 10 Folien + Anhang)

| # | Folie | Inhalt (so wenig Text wie möglich) | Visual |
|---|---|---|---|
| 1 | Cold Open | schwarz, nur Waveform des Anrufs | Audio-Wellenform |
| 2 | „This call doesn't exist today.“ | 1 Satz | Telefon-Icon durchgestrichen |
| 3 | WHY ✓ HOW MANY ✓ WHO ✗ | 3 Wörter | groß, WHO rot |
| 4 | Wo es bricht | 4 Pfadschritte, rote Lücken, 1 in 3 · 31 % · Uusimaa | Pfad + 3 Zahlen-Kacheln mit Quelle |
| 5 | Center of Gravity: heute | Institution ●──○ Mensch, „We build where it is today“ | Linie mit Punkt links |
| 6 | Signal → Ask why → Help → Learn | 4 Icons | Flow, Apotti/Maisa/Kela-Logos klein |
| 7 | LIVE DEMO | Screenshot als Fallback | Dashboard-Screenshot |
| 8 | 4 Vorschläge | HUS · Transport · Home · Report | 4 Kacheln |
| 9 | Business Case | 4 % · −42 % · €364 m · 2.6× + Businessplan-Zahl | 4 große Zahlen mit Quelle |
| 10 | Der Schwerpunkt bewegt sich | Punkt wandert nach rechts | Linie animiert |
| 11 | Eero & Jenny | 1 Foto/Illustration + Handy-Screen aus CarePulse | Bild |
| 12 | Agent ↔ Agent | Eero-Agent ↔ Bezirks-Agent ↔ Kela | 3 Knoten |
| 13 | Claim | „Closing gaps. Connecting care.“ + QR | Logo |
| A1 | Data & Limits | Quellen, synthetische Personas, GDPR Art. 9/22, kein Diagnose-Tool | Tabelle |
| A2 | Team | 3 Namen | – |

---

## Q&A-Vorbereitung (wahrscheinliche Fragen)

| Frage | Antwort in 1 Satz |
|---|---|
| Datenschutz? | Läuft beim Bezirk innerhalb der Behandlungsbeziehung; raus gehen nur anonyme Aggregate (GDPR Art. 9), keine automatisierten Entscheidungen (Art. 22). |
| Warum nicht Versicherungen? | Private Versicherer sehen in Finnland keine Krebstermine (Tietosuojavaltuutettu 2022, KHO 2025:86); sie sind nur ein Opt-in-Zusatzkanal. |
| Espoo hat kein Apotti? | Stimmt, aber HUS behandelt Krebs für ganz Uusimaa und läuft auf Apotti, deshalb HUS als erster Pilot. |
| Beweis, dass Anrufe wirken? | RCT (Percac-Lima 2015): Navigator-Anrufe senken No-shows um >40 %; KI senkt die Kosten pro Patient. |
| Ist der Risiko-Score ein Medizinprodukt? | Ja, deshalb heute nicht im Produkt; Teil B ist Vision, der Agent stellt nie eine Diagnose. |
| Was kostet das? | 🔁 aus Businessplan |
| Woher kommen die Zahlen im Dashboard? | THL/Sotkanet, Syöpärekisteri, Kela Open Data – Quelle steht unter jeder Zahl, Personen sind synthetisch. |
