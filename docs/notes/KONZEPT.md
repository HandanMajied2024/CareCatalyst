# CareCatalyst – Pitch-Konzept (Junction 2026, AstraZeneca „Equal Care Across Finland“)

Stand: 2026-11-14. Der Pitch selbst ist auf Englisch, Dialogzeilen deshalb im Original.

## Kernidee in einem Satz

**Convenience: Niemand soll seine Lebenssituation immer wieder neu erklären müssen.**
So wie heute jeder ein Handy hat, hat in Zukunft jeder einen persönlichen KI-Agenten. Der Pitch startet aber mit einer Lösung, die heute schon umsetzbar ist.

## 1. Das Problem (Ist-Zustand)

- Firmen wie AstraZeneca erforschen die Ungleichheit beim Zugang zur Krebsversorgung und schlagen Lösungen vor.
- AZ weiß, **welche Gründe** es gibt, warum Menschen nicht in Behandlung gehen (z. B. Angst, Behandlungszentrum zu weit weg), und **wie viele** Menschen pro Grund betroffen sind.
- AZ weiß aber nicht, **wen** es konkret betrifft („John Doe hat Angst vor der Krebsbehandlung“).
- Deshalb kann niemand John Doe kontaktieren und mit ihm eine Lösung finden. **Genau dort beginnt die Ungleichheit.**

## 2. Unsere Lösung heute (aktueller Schwerpunkt, „center of gravity“)

Ein **KI-Agent, den jede Versicherung für sich umsetzen kann** (Blueprint, kein FICAN-Projekt):
- Versicherte melden sich **freiwillig (Opt-in)** in der App der Versicherung an und erlauben, dass ihr Behandlungsweg begleitet wird
- die App erfasst den Status selbst: Termin gebucht / abgesagt / nicht erschienen / Behandlung begonnen (Eingabe durch den Patienten, Erinnerungen, Kalender, später geteilte Daten aus MyKanta)
- stockt der Weg (Termin abgesagt, keine Buchung), meldet sich der Agent beim Patienten (Anruf/Chat) und **fragt, warum** es nicht geklappt hat (Angst, Entfernung, Transport, Kosten, Pflege von Angehörigen …)
- er informiert über Behandlungen, buchbare Termine und Hilfen (z. B. Kela-Fahrtkostenerstattung, Kela-Taxi), beantwortet Fragen und sucht im Web nach Hilfsprogrammen
- die Gründe fließen **anonymisiert und aggregiert** zurück, z. B. an AstraZeneca oder Wohlfahrtsbezirke → so wird sichtbar, **wo im Pfad** und **warum** Menschen verloren gehen

### Rechtlicher Faktencheck (Recherche 14.11.2026)

| Frage | Antwort |
|---|---|
| Sehen private Versicherungen (If, LähiTapiola, Pohjola …) automatisch, ob jemand einen Krebstermin gemacht, abgesagt oder wahrgenommen hat? | **Nein.** Kein allgemeiner Zugriff auf Kanta oder Klinikdaten. Zugriff gibt es nur mit **spezifischer Einwilligung** und nur für die Prüfung von Anträgen und Leistungen, begrenzt auf den konkreten Fall bzw. die konkrete Krankheit (Datenschutzbeauftragter 2022, KHO 2025:86). |
| Warum sehen sie es auch praktisch nicht? | Krebsbehandlung läuft in Finnland fast komplett **öffentlich** über die Wohlfahrtsbezirke. Private Zusatzversicherungen sind wenig verbreitet und zahlen dafür meist nichts, also landet nichts bei ihnen. |
| Kela (gesetzliche Krankenversicherung, deckt alle ab)? | Sieht Erstattungsdaten (Medikamente, Fahrtkosten, Kela-Taxi), aber keine Termine in öffentlichen Kliniken. Kela-Daten sind gesetzlich zweckgebunden. |
| Darf man Gesundheitsdaten für proaktive Ansprache nutzen? | Nur mit **ausdrücklicher, zweckgebundener Einwilligung** (DSGVO Art. 9). Findata-Daten (Sekundärnutzungsgesetz 552/2019) sind nur für Forschung/Statistik und **nicht** zur Kontaktaufnahme mit Einzelnen. Automatisches Risiko-Profiling ist heikel (DSGVO Art. 22). |
| Wer hat die Termindaten wirklich? | Die **Wohlfahrtsbezirke** als Behandler und der **Patient selbst** (MyKanta). |

**Folgerung:** Das Konzept funktioniert, wenn die **App die Datenlücke schließt**: Der Patient willigt ein und teilt seinen Status selbst. Die Versicherung zieht nichts heimlich aus Kanta. Rückmeldungen an Institutionen gibt es nur anonymisiert und aggregiert. Das passt auch zur Vision: Der Mensch kontrolliert seine Daten (Rückenwind durch den **European Health Data Space**, der Patienten das Recht gibt, ihre Daten an selbst gewählte Stellen weiterzugeben).

→ Überleitung: Der Schwerpunkt wandert von der Gegenwart in die Zukunft.

### Wer betreibt es? (Stand 14.11. abends)

| Betreiber | Termindaten? | Fazit |
|---|---|---|
| **Wohlfahrtsbezirk (hyvinvointialue)** | ✅ Ja. Eigene Patientenakte (Termine, Absagen, No-shows), Behandlungsbeziehung = Rechtsgrundlage, Messung der Ziel-3-Wartezeiten liegt bei ihnen | **Hauptkunde.** Passt zu AZ (möchte ein Folgeprojekt mit einem Bezirk) |
| Private Versicherung | ❌ Nein, nur über die Opt-in-App | Zusatzkanal für eigene Versicherte |
| Kela | Teilweise (Erstattungen, Kela-Taxi) | Partner für Transport und Kosten |

### Andocken an bestehende Termin-Apps statt neuer App

Die Termindaten liegen schon in bestehenden Portalen → unser Agent ist eine **Schicht darüber** (Modul/Integration), keine Konkurrenz-App:
- **Maisa** (Apotti-Portal): HUS + Helsinki + Vantaa-Kerava (+ Kauniainen). HUS macht die Krebsbehandlung für ganz Uusimaa → Termine, Buchungen, Nachrichten liegen dort. Maisa kennt schon **Vertretungsrechte** (Angehörige dürfen Termine buchen und Nachrichten schicken, sehen aber keine Diagnosen) → Vorbild für „Agent handelt im Auftrag“.
- **Omaolo**: Symptom-Check, leitet an das Gesundheitszentrum weiter.
- Private Ketten (Terveystalo, Mehiläinen, Pihlajalinna): eigene Apps, sehen nur Termine in der eigenen Kette.

**Faktencheck 14.11. spät:** Maisa zeigt Buchungserlaubnis, Termine (kommende und vergangene) und erlaubt bei manchen Terminen Absagen. No-shows und Behandlungsbeginn liegen im Klinik-System **Apotti**, nicht sichtbar in Maisa. Der Agent hängt deshalb per **FHIR** an Apotti (Standard dort, es gibt eine Sandbox ohne echte Daten), Maisa ist die Oberfläche für Patienten. ⚠️ **Espoo/Länsi-Uusimaa nutzt kein Apotti.** Die Krebsbehandlung macht aber **HUS** (Apotti) für ganz Uusimaa → erster Pilot-Betreiber: **HUS**. Lücke: Überweisung vom Espooer Gesundheitszentrum zu HUS läuft systemübergreifend.

Signale für den Agenten: Überweisung erhalten, aber kein Termin gebucht · Termin abgesagt · nicht erschienen · Behandlung begonnen. Kein Krebstermin wird in Kanta zentral gespeichert → Integration läuft pro Bezirk/System (Apotti, Lifecare, Omni360 …).

### Idee: Die Versorgung kommt zum Patienten

Wenn der Agent als Grund „kann nicht hinkommen“ erkennt (körperlich eingeschränkt, sehbehindert, weit weg), schlägt er statt nur Transport auch **Versorgung vor Ort** vor:
- ✅ geht schon heute: **Kotisairaala** (Heimkrankenhaus der Bezirke, z. B. Keusote), Teile der Chemo- und Supportivtherapie zu Hause, Blutabnahme, Pflegebesuche, Video-Sprechstunde, mobile Screening-Einheiten
- ❌ geht nicht zu Hause: OP, Bestrahlung, CT/MRT/PET → dafür Kela-Taxi und Begleitung organisieren
- Evidenz: Laut Cochrane kostet Chemo zu Hause ungefähr gleich viel wie ambulant, die Sicherheitsdaten sind noch unsicher → als Pilot im Bezirk vorschlagen

## 3. Die Zukunftsvision

Nicht mehr der Agent der Versicherung ruft mich an, sondern **mein eigener persönlicher KI-Assistent**, der meinen Alltag kennt und flexibel Termine für mich bucht.

### Die Szene (für Pitch/Video)

**Figur:** älterer, sehbehinderter Mann mit Hund (Jenny). Wohnt in **Espoo**.

1. Er macht Kaffee und spricht dabei mit Alexa über neues Hundefutter. Etwas fällt auf den Boden.
2. Er bückt sich, macht ein „ugh“, weil der Rücken wehtut.
3. Alexa: *„Oh yeah, I've ordered the dog food for Jenny.“*
4. Alexa: *„Oh, by the way, is your back hurting again? You've already been to the orthopedist, and your health risk score has increased to a level where you should get yourself checked out.“*
5. Er fragt, wo das Behandlungszentrum ist. Alexa: in **Helsinki** (sie sind in Espoo).
6. Alexa: *„And don't worry about transportation. I know you don't like using public transportation. The Finnish government has a transportation assistance program that you may be eligible for. Your insurance could also cover the transportation costs, so you can get the treatment you need.“*
7. Alexa: *„Should I book the appointment for tomorrow at 8 in the morning, before you go to your bingo class?“*
8. Er: *„Yes, thank you very much.“* Dann geht er seinem Tag nach und spielt mit dem Hund.

**Was der Agent in der Szene weiß:** bisherige Behandlungen (Orthopäde), Berechtigung für krebsbezogene Gesundheitsleistungen, Sehbehinderung, ÖPNV ist schwierig, Taxi nicht leistbar, Tagesablauf (Bingo-Kurs).

## 4. Das große Bild (Schluss des Pitches)

- Jeder Mensch hat einen persönlichen KI-Agenten, und auch Institutionen (Versicherungen, Ärzte, Behörden) haben eigene Agenten.
- Schluss-Interaktion: **der persönliche Agent des Mannes spricht direkt mit dem Agenten der Versicherung** (dem vom Anfang des Pitches, der anrufen und beraten kann).
- Der persönliche Agent sucht zusätzlich im Web nach Hilfsprogrammen und kann mit dem Agenten einer Ärztin bzw. eines Arztes kommunizieren.
- Ergebnis: Er muss seine Lebenssituation nie wieder neu erklären. Sein Agent kennt Bedürfnisse, Einschränkungen, Termine, Krankengeschichte und Tagesablauf.

**Die Verschiebung:** weg von „Institutionen gehen auf Einzelne zu“, hin zu „Einzelne haben eigene Agenten, die in ihrem Namen mit den Institutionen sprechen“.

## Pitch-Bogen (Kurzform)

| # | Teil | Kernbotschaft |
|---|------|---------------|
| 1 | Problem | AZ kennt Gründe und Zahlen, aber nicht die Personen |
| 2 | Heute | Versicherungs-Agent (Opt-in) begleitet den Behandlungsweg und fragt nach, wenn er stockt |
| 3 | Übergang | Schwerpunkt wandert in die Zukunft |
| 4 | Szene | Persönlicher Agent (Alexa-Szene, Espoo → Helsinki) |
| 5 | Vision | Agent-zu-Agent: persönlicher Agent ↔ Versicherung / Arzt |

## Offene Punkte / Risiken gegenüber den Challenge-Regeln (siehe CONTEXT.md)

- Die Challenge verlangt **nur öffentliche, aggregierte Daten** mit Quellenangabe → die Demo nutzt öffentliche Aggregatdaten (z. B. Gründe/Wartezeiten nach Bezirk) und **synthetische Personen**. Opt-in und Einwilligung im Pitch klar zeigen.
- Pflicht: mindestens 1 Indikator aus **Ziel 3** der Krebsstrategie (z. B. Behandlungsbeginn innerhalb der Zielzeiten) sichtbar einbauen.
- Pflicht: **funktionierende Live-Demo** (Slides reichen nicht) und konkrete, umsetzbare Vorschläge.
