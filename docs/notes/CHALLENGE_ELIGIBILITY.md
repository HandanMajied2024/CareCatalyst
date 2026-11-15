# CareCatalyst – Challenges & Eligibility

Stand: Sa 14.11.2026 abends. Quellen: Challenge-Seite AZ (hackjunction.app/participate/45/challenges/344, Snapshot in `.playwright-mcp/page-2026-11-14T17-57-24-971Z.yml`), CONTEXT.md, KONZEPT.md, `C:\Users\tutuh\Hack-Junction-2026-Finland\junction-kb\` (event.md, main-challenges.md, tech-challenges.md), Krebsstrategie in `resources/`.

## 1. Hauptchallenge: „Equal Care Across Finland“ (AstraZeneca, Healthcare Track)

**Aufgabe:** KI-gestütztes System für gleichwertige, wirksame Krebsversorgung in ganz Finnland.
1. **Identify the gap** – Unterschiede bei Zugang oder Ergebnissen erkennen
2. **Locate the gap** – wo im Pfad: Erkennung, Überweisung Primär→Facharzt, Diagnose, Behandlungsbeginn
3. **Recommend** (am wichtigsten) – konkrete, evidenzbasierte Vorschläge, national oder auf Bezirksebene umsetzbar

Formate (offen): KI-Analyst, Monitoring-Dashboard mit Empfehlungen, Frühwarnsystem, Interventions-Simulation.

**Mindestanforderungen**
- Nur öffentliche Daten und/oder Insights der AZ-Mentoren, **Quelle für jede Aussage**. Keine Patientendaten („public, aggregate data only“).
- Mind. **1 Indikator aus Ziel 3** der Krebsstrategie 2026–2035
- Konkrete Vorschläge, nicht nur Analyse
- **Funktionierende Demo** (Slides reichen nicht)

**Bewertung:** Actionability 30 % · Insight 25 % · Data quality & transparency 20 % · Execution (Live-Demo) 15 % · Clarity (Entscheider versteht es in 2 Min) 10 %

**Preise:** 1000 € / 750 € / 250 €. AZ möchte ein Folgeprojekt mit einem Wohlfahrtsbezirk. Judging So 14:00 (Rusila, Aaltonen, Tuormaa).

**Ziel-3-Indikatoren** (Strategie, Kuva 1): 5-J-Überleben bei Krebs mit schlechter Prognose auf nordisches Niveau (+14 pp Lunge, +6 Pankreas, +14 Leber ggü. NORDCAN 2023) · Krebssterblichkeit −10 % (heute 13 300/Jahr) · **Behandlungsbeginn innerhalb der Zielzeiten** (THL Ohjaus 21/2016). Querschnitt: regionale/sozioökonomische Unterschiede sichtbar machen.

**Daten (AZ-Quellenliste):** Syöpärekisteri, THL/Sotkanet, Tilastokeskus (Todesursachen), Kela Open Data, Kela/Fimea Arzneimittelstatistik, NORDCAN 2.0, FICAN. Findata/Biobanken: nur Forschung mit Genehmigung → für uns nicht nutzbar.

## 2. Weitere Preise / Tracks

| Track | Preis | Regel |
|---|---|---|
| **Junction 2026 Overall Winner** | 10 000 € | Top 5 aus dem Peer Review So → 3 Min Pitch + 3 Min Q&A vor 7 Juroren. **Ganzes Team muss beim Peer Review sein** (Tisch A115, bis 10:30) |
| Andere Main Challenges (18, z. B. Aalto „Beyond the Clinic“ 2000 €) | – | Im Formular nur **1 Main Challenge** wählbar |
| **Tech Challenges** (beliebig viele, zusätzlich) | siehe unten | Im Formular ankreuzen und in der Beschreibung erklären, **wie** die Tech genutzt wurde |

Tech Challenges: Codex ($10k/5k/2.5k Credits) · Verda ($10k Credits) · Gemini API (4000/2000/1000 € + GCP-Credits) · Gemma (3× 1000 €) · Modal ($2k + $3k Credits; 40 % effective use, 15 % Live-URL) · Oxylabs (1000 € Apple-Gutschein + Credits; Use 30 %, Value 25 %, Trust 20 %) · Nemotron (2× RTX 5080) · Aiven (1000/750/500 €) · Context.dev (750/250 €) · Cloudinary ($500 p. P., Pflichtformular) · CRACI (LEGO u. a.) · Arduino UNO Q · Atech · MLH-Sachpreise: MongoDB, ElevenLabs (Earbuds), Solana, Tiger Data, Vultr, Entire, DEV ($100 für einen Blogpost), Gemini (Swag).

## 3. Eligibility unseres Konzepts

Unser Konzept: Opt-in-App/Agent (heute: „jede Versicherung“) begleitet den Behandlungsweg, fragt bei Abbruch nach dem Grund, hilft (Termine, Kela-Fahrtkosten/Kela-Taxi, Hilfsprogramme) und meldet Gründe **anonymisiert und aggregiert** zurück. Vision: persönlicher Agent (Alexa-Szene), Agent-zu-Agent.

| Challenge | Eligible? | Warum | Was fehlt |
|---|---|---|---|
| **AZ Equal Care** | **Teilweise** | Thema passt genau (Pfad, „wo/warum gehen Menschen verloren“), Vorschläge angelegt, Daten-Lücke wird adressiert (AZ: „addressing this data gap is part of the challenge“) | (1) ~~Keine Demo nachweisbar~~ → Update 23:40: Repo erreichbar, Demo existiert (Calling Agent, Barrier Map, Simulator), siehe Abschnitt 5. (2) **Kein Ziel-3-Indikator** in der Lösung, nur als Kandidat (Behandlung in Zielzeit). (3) **Keine öffentliche Datenquelle** eingebunden, keine Quellen pro Zahl. (4) Kern basiert auf Personendaten → Demo nur mit **synthetischen Personas** + öffentlichen Aggregaten, klar sagen. (5) **Actionability (30 %)**: Betreiber „Versicherung“ ist schwach (private Versicherer sehen Krebstermine nicht, Behandlung ist öffentlich – eigener Faktencheck) → als Werkzeug für Wohlfahrtsbezirk/Gesundheitszentrum framen, 3–5 konkrete Maßnahmen mit Quelle. (6) Alexa/Agent-zu-Agent-Vision zählt kaum für Kriterien – kurz halten. (7) Limits/Annahmen offen nennen (20 %). |
| **Overall Winner** | **Ja, wenn** FINAL abgegeben + alle 3 beim Peer Review | Automatisch im Rennen | Starke 5-Min-Demo für Peer Review; Tisch So im Team-Tab speichern |
| Aalto Beyond the Clinic / andere Main | **Nein** | Nur 1 Main Challenge; Thema (Depression/TMS zuhause) passt nicht | – |
| Gemini API | **Möglich** (nichts gebaut) | Agent-Dialog, Grund-Klassifikation, Strategie-PDFs mit Seitenzitaten | Gemini als Kern einbauen + im Formular erklären „warum Gemini“ |
| MLH ElevenLabs | **Möglich** | Agent „ruft an“ = Sprachausgabe passt zur Pitch-Story | Stimme im Demo-Flow, MLH-Code |
| Oxylabs Web API | **Möglich** | Agent sucht im Web nach Hilfsprogrammen (steht im Konzept) | Oxylabs-API im Flow, Quellen anzeigen (Trust 20 %) |
| Modal | **Möglich** | Live-Demo-URL zählt 15 % | Backend/Demo auf Modal deployen |
| Codex | **Möglich** | Falls Code mit Codex entsteht | Nachweis (Commits/Tasks) |
| MLH DEV | **Leicht** | Blogpost über das Projekt | Post schreiben ($100) |
| Gemma / Context.dev / Aiven / MongoDB / Tiger Data | Optional | Klassifikator als offenes Modell / Hilfsprogramme strukturiert / DB für Aggregat-Gründe | Nur wenn ohnehin genutzt |
| Nemotron, Verda, Cloudinary, CRACI, Arduino, Atech, Solana, Vultr, Entire | **Nein** (realistisch) | Kein Bezug zum Konzept | – |

## 4. Top-Lücken bis zur Abgabe (So 09:00 Plattform / 10:00 Regeln)

1. **Live-Demo** (Pflicht, 15 %): synthetische Persona sagt Termin ab → Agent fragt warum → bietet Hilfe → Aggregat-Zähler pro Bezirk/Pfadschritt steigt.
2. **Ziel-3-Indikator** sichtbar: „Behandlungsbeginn innerhalb der Zielzeiten“ (THL) pro Bezirk mit Quelle; Fallback: Sterblichkeit/Überleben aus Syöpärekisteri/NORDCAN.
3. **Öffentliche Daten + Quelle unter jeder Zahl** + Abschnitt „Limits“.
4. **3–5 konkrete Maßnahmen** für einen Wohlfahrtsbezirk (z. B. Kela-Fahrtkosten-Info bei Überweisung, Rückruf bei abgesagtem Termin), je mit Quelle.
5. **Betreiber klären**: Bezirk/Gesundheitszentrum statt Versicherung (oder beides, Bezirk zuerst).
6. **Submission**: Repo-Zugang + MIT-Lizenz, Texte, Challenge-Auswahl, Video ≤2 Min, Tech Challenges ankreuzen, FINAL setzen.
7. Mentor fragen (TODO): Daten zu Abbruchgründen? bevorzugter Ziel-3-Indikator?

## 5. Tech-Challenges (aktualisiert)

Stand: So 15.11.2026 früh. Geprüft gegen den aktuellen Code beider Teile (read-only, nichts gepusht). Regeln der Tech-Challenges: siehe frühere Prüfung (hackjunction.app/participate/45/tech-challenges/48 Gemini, /49 Codex, /50 ElevenLabs; `junction-kb/tech-challenges.md`).

**Repos**

| Teil | Repo | Sichtbar | Lizenz | Stand |
|---|---|---|---|---|
| Haupt-Repo | `HandanMajied2024/CareCatalyst` | öffentlich | MIT | Submodule `concepts/today` + `concepts/vision` |
| **A · heute** (Anruf-Agent für Bezirke) | `devstar7674-beep/CareCatalyzer` (lokal `./repo`) | **privat** → Owner muss öffentlich machen | MIT | `a534e47` (README, LICENSE, AGENTS.md). Achtung: Submodule-Zeiger im Haupt-Repo steht noch auf `69c2cb2` (vor README/LICENSE) |
| **B · Vision** (CarePulse, persönlicher Agent) | `youcefjerbi/mobile_app_new` | öffentlich | **keine** → TODO MIT-`LICENSE` | `0f756a0` „first push“ (1 Commit) |

**Nachweise pro Teil**

| Tech-Challenge | Teil A (CareCatalyzer) | Teil B (CarePulse) | Urteil |
|---|---|---|---|
| **Gemini API** (€4.000) | **Echte API-Calls**: `server.ts` mit `@google/genai` → Gemini 3.8 Flash mit JSON-`responseSchema` (`/api/call-turn`, `/api/classify-call`) + Gemini 3.8 Live Audio über WebSocket (`/api/live-call`). README-Abschnitt „Built with Gemini“ (Problem, Integration, warum Gemini). `metadata.json` = Google-AI-Studio-Projekt. | React-App: **kein API-Call**, „Gemini“ nur als Auswahl im Agent-Menü (`frontend/src/main.jsx`, `preview/pitch.js`). Alte Android-App: `PersonalHealthAgentService.kt` ruft `Firebase.ai.generativeModel("gemini-3.8-flash")` auf, ist aber laut README „unconnected“ und nicht gebaut. | **Eligible (stark), getragen von Teil A.** Im Video den Live-Anruf zeigen. |
| MLH Gemini | wie oben | – | **Eligible**, nur ankreuzen |
| **Codex** ($10k Credits) | `AGENTS.md` („Instructions for coding agents (OpenAI Codex …)“) + README „Built with Codex“, beide aber erst nachträglich von Handan/Claude angelegt (`a534e47`). Commits (devstar7674, Youcef, Hazem): **keine** Codex-Trailer oder `.codex`-Dateien. README hat noch `TODO: add Codex session screenshots`. | **Keine Spur im Repo** (kein `AGENTS.md`, 1 Commit ohne Trailer). „Codex“ nur als Menüpunkt bzw. `AgentProvider.CODEX` (Default-Anbieter in der Story). | **Eligible laut Team-Aussage** (Regel verlangt kein festes Format). Nachweis fehlt im Code → **TODO:** 2–3 Screenshots der Codex-Sessions (Codex-App/CLI-Verlauf oder chatgpt.com/codex Tasks) je Teil, Liste „welche Dateien Codex gebaut hat“ in Beschreibung + README, 5 s im Video. |
| **MLH ElevenLabs** | **Nicht gelandet.** Kein ElevenLabs-Code, keine Dependency, kein Commit/Branch (Remote `main` = `a534e47`, `git fetch` geprüft). Stimme = Gemini Live bzw. Browser-`speechSynthesis`. | nichts | **Noch nicht eligible.** Nur wenn der Teamkollege vor Feature-Stopp pusht. |
| MLH DEV ($100) | – | – | **Geplant nach Abgabe** (Entwurf `DEV_BLOGPOST.md`, veröffentlichen bis 30.11.) |
| Modal / Oxylabs / Rest | nicht genutzt | nicht genutzt | Nein |

**Quick Wins (nur Empfehlung, nicht umgesetzt)**
1. **Codex-Nachweis** (15 Min, €0): Screenshots + 2 Sätze pro Teil, welche Teile mit Codex gebaut wurden. Größter Hebel ($10k).
2. **Teil B mit echtem Gemini-Call** (~30–45 Min, €0 im Free Tier): Ein kleiner Vite-Dev-Proxy oder Express-Endpunkt, der beim Menüpunkt „Gemini“ eine Antwort von `gemini-3.8-flash` holt (z. B. Risiko-Hinweis/Terminvorschlag als JSON-Schema), Key nur server-seitig. Alternativ den Agent-Chat von B gegen `/api/call-turn` aus Teil A laufen lassen. Ohne das zählt für Gemini nur Teil A, was reicht.
3. **Submodule-Zeiger** im Haupt-Repo auf `a534e47` heben, damit die Juroren README/LICENSE von Teil A sehen.
4. **MIT-`LICENSE`** in `youcefjerbi/mobile_app_new` (Youcef).

Im Formular: Gemini API + MLH Gemini + Codex ankreuzen, je 2–3 Sätze „wie genutzt“. ElevenLabs nur ankreuzen, wenn der Code bis zur Abgabe im Repo ist.
