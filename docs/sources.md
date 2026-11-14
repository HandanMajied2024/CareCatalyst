# Sources

## Strategy

- National Cancer Strategy 2026–2035 (Kansallinen syöpästrategia), STM
- Implementation roadmap 2026–2031 (toimeenpanon tiekartta)
- THL Ohjaus 21/2016: monitoring access to cancer treatment (hoitoonpääsyn seuranta)

## Public data (AZ source list)

| Source | Use |
|---|---|
| Finnish Cancer Registry (Syöpärekisteri) | Incidence, survival, stage by region |
| THL / Sotkanet | Regional indicators, waiting times |
| Statistics Finland (Tilastokeskus) | Causes of death |
| Kela open data | Travel reimbursements, Kela taxi |
| Kela / Fimea medicine statistics | Treatment use |
| NORDCAN 2.0 | Nordic comparison |
| FICAN | Regional cancer centres |

Not usable for us: Findata, biobanks (research permits only).

## Legal

- GDPR Art. 9 (health data), Art. 22 (automated decisions)
- Act on Secondary Use of Health and Social Data 552/2019
- Data Protection Ombudsman decision 2022 and KHO 2025:86 (insurers' access to health data)
- European Health Data Space regulation (patient right to share data)

## Evidence

- Cochrane review: home-based vs. hospital chemotherapy (cost similar, safety evidence uncertain)

## Portals and integration (checked 14.11.2026)

- [Maisa FAQ](https://ukk.maisa.fi/en/): booking permit, Events (upcoming/past appointments), cancel/reschedule for some appointments, proxy rights
- [HUS digital development](https://hus.fi/en/about-us/development/digital-development): FHIR first policy
- [FHIR Demo 2024: Apotti](https://fhir.fi/en/demo2024/apotti/): FHIR recommended for new integrations, sandbox without real patient data
- [Finnish SMART App Launch: Apotti CapabilityStatement](https://hl7.fi/fhir/finnish-smart/CapabilityStatement-apotti-eko01.html): Appointment resource
- [Verkkouutiset: "Apotti oli kallis virhe"](https://www.verkkouutiset.fi/a/apotti-oli-kallis-virhe/): Espoo / Länsi-Uusimaa did not adopt Apotti (opinion piece, verify with luvn.fi)

## Business case (checked 14.11.2026, details in [business-case.md](business-case.md))

- Finnish Cancer Registry, Syöpä 2024 (38 853 new cancers, 13 490 deaths, stage recorded 42 %) and screening report 2024
- Syöpäsäätiö: cancer cost ~€1.4 bn (2024)
- Kela: travel reimbursements 2025 (€364 m), Kela taxi 2025 (€227 m, pooling > €7 m)
- Pirha: unused hospital appointments 2025 (4.0 %)
- Percac-Lima et al. 2015 (RCT, navigator calls, no-shows 17.5 % → 10.2 %); Kim et al. 2018 (navigation cost $148–359); Parikh et al. 2010
- Zai, Moretti, Martikainen et al. 2025 (socioeconomic disparities, Finland)
- Syöpäpotilaat ry + Roche survey (31 % believe care is regionally equal)
- Lung cancer cost by stage (NL 2012–2021), Gaceta Sanitaria (ES), EFPIA 2025
