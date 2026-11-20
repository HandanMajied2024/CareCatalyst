# Demo-Runbook: CareCatalyst Pitch (5 min + Live-Demo)

> Nicht pushen, enthält Pitch-Inhalt. Stand 15.11., ~05:00 FI.

## Vorher (10 min vor dem Pitch)

| ✔ | Was |
|---|---|
| ☐ | Laptop am Strom, Akku > 50 %, Benachrichtigungen aus |
| ☐ | Tab 1: Deck `presentation/deck.html` (Taste **F** = Vollbild, **N** = Notizen, Pfeiltasten) |
| ☐ | Tab 2: **App A** https://handan-majied1--carecatalyst-demo-web.modal.run (einmal laden, bleibt warm) |
| ☐ | Tab 3: **App B** https://handan-majied1--carepulse-vision-web.modal.run |
| ☐ | Tab 4: Backup-Video `pitch/video/demo-backup.mp4` (lokal, ohne WLAN abspielbar) |
| ☐ | Im Anruf-Panel **Turn-based** wählen (nicht „Voice live“, Hallen-WLAN und Mikro sind riskant) |

## Klickpfad A: für die Bezirke (Folie 7 „Live demo“, ca. 75 s)

| # | Klick | Satz, den du sagst |
|---|---|---|
| 1 | Tab **Patients**, oben steht **Matti Heikkinen** (Kemi, Pill „Demo“) | “This is the county's view. Matti, Kemi, Lapland. His CT was **cancelled**. Today, nobody would ask why.” |
| 2 | **Call patient** (Modus **Turn-based**) | “Our agent calls him. In Finnish, Swedish or English, any time of day.” |
| 3 | Antwort-Button **No bus from Kemi** | “Matti says: there's no bus that morning.” |
| 4 | Ergebnis zeigen: Barriere **Transport**, Status **Follow-up**, Score **41 → 56** | “The agent understands the reason: **transport**. It holds the appointment and queues a Kela taxi task for the coordinator. His risk score goes up, so he moves up the list.” |
| 5 | Tab **Regional summary**, Balken *Treatment started within target time* | “Every call feeds this. **Goal 3** of the cancer strategy, per region. Finland publishes no regional figure yet. Our pathway events produce it.” |
| 6 | Karte bzw. Barrieren für **Lapland** | “And now the county sees not just how many are late, but **why**, and at which step.” |
| 7 | Tab **Regional support** → **Plan support** → **Save** | “So it can act: shared transport for Lapland, with the budget visible. Synthetic patients, public aggregate data.” |

## Klickpfad B: für eine Person, die Vision (Folien 11–13, optional ca. 30 s)

Der Hintergrund ist warm. Das ist das Signal für „ab hier Vision, nicht heute“.

| # | Klick | Satz |
|---|---|---|
| 1 | **Agent** öffnen | “Tomorrow, Eero has his own agent. It knows his day: Espoo, bingo at eleven, his dog Jenny.” |
| 2 | **Where?** (chip) | “His back hurts again. His agent remembers the last visit. It never diagnoses, it just says: let's get this checked.” |
| 3 | **Transport** (chip) | “It knows he doesn't like the bus, so it asks for travel support.” |
| 4 | **Bingo time** (chip) | “Tomorrow at 8, pickup at 7, back before bingo.” |
| 5 | **Care plan** → Häkchen bei Clinic, Insurance, Transport → **Approve & run** | “Eero decides who may know what. One tap.” |
| 6 | Agent-zu-Agent läuft bis **5/5** | “And his agent talks to the **county agent we built today**. Agent to agent. He never has to explain his life again.” |

## Plan B

| Problem | Was du tust | Satz |
|---|---|---|
| Voice hängt („Connecting…“) | Auf **Turn-based** umschalten, weiter mit Schritt 3 | “Let's do it in text, same agent.” |
| Gemini antwortet nicht | Im Feld **Barrier** von Hand **Transport** wählen | “Human in the loop: the coordinator can always override.” |
| WLAN weg / App lädt nicht | Tab 4: **`pitch/video/demo-backup.mp4`** abspielen und live drüber sprechen | “Here's the same flow recorded an hour ago.” |
| Alles weg | Deck weiter, Folie 7 zeigt die Screens | Kein Entschuldigen, einfach weitererzählen. |

## Die 3 wahrscheinlichsten Jury-Fragen

| Frage | Kurzantwort (1–2 Sätze) |
|---|---|
| **Datenschutz / Opt-in?** | “It runs inside the county, within the existing care relationship. Patients can opt out, only anonymous aggregates (reason × step × region) ever leave, and the agent makes no automated decisions: a coordinator confirms (GDPR Art. 9 and 22).” |
| **Wer zahlt?** | “The welfare county: a yearly licence, about €150k for HUS, plus €50–100 per patient guided. We estimate about €300k of value per year from avoided no-shows and earlier stages. AstraZeneca funds the 90-day pilot and gets anonymised insight, never patient data.” |
| **Wie messt ihr Goal 3?** | “Goal 3 is ‘treatment starts within target times’ (THL 21/2016). Today there is no clean regional number. Our pathway events (referral, booked, cancelled, no-show, treatment started) give exactly those timestamps per region, and the reason why.” |

Weitere Antworten: `pitch/PITCH_DRAFT.md`, Abschnitt Q&A.
