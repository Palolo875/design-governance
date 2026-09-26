# DG-AUDIT-001 — Phase 11.00 — Décisions de l'owner et sortie de la phase 10

**Date :** 25 septembre 2026. **Source des décisions :** réponses de l'owner (Junior) aux quatre questions posées à l'issue de 10.05. Baseline B01 inchangée ; B02 reste une hypothèse gelée.

| # | Décision | Réponse de l'owner | Effet |
|---|---|---|---|
| 1 | F-RM-003 (granularité des locators) | **Confirmée** | Le registre compte **158 fiches** ; F-RM-003 est dans la grappe C4, après F-VRM-001 |
| 2 | Arbitrage des 8 abaissements à portée réelle | **Tout accepter** | Les gravités du registre consolidé sont définitives pour la phase 11 : 14 Majeurs, 87 Significatifs, 48 Mineurs, 9 Observations |
| 3 | **D-ACT-1** : autorité d'une RUN_CARD validée | **c. Mixte** | Seuls les invariants déterministes et à fort risque deviennent machine. Les autres obligations sont déclarées « forme seule » dans la promesse du validateur |
| 4 | **D-FAC-1** : statut d'une façade lue seule | **c. Bornée et testée** | Façades courtes, règles normatives marquées « voir propriétaire », test de cohérence façade ↔ propriétaire au build, porté par F-VRM-003 |

## Conséquences pour la phase 11

- **Sortie de la phase 10 : satisfaite.** 158/158 fiches classées, gravités arbitrées, registre de référence `DG_AUDIT_001_Phase10_05_REGISTRE_CONSOLIDE_158.csv`.
- **D-ACT-1 = c** impose un premier livrable en grappe B2 : la **liste close** des invariants qui passent en machine. Elle devra être justifiée fiche par fiche parmi F-ACT-010, 012, 017, 018, 022, 023, 024, 038 et F-RC-001, et les autres seront déclarées « forme seule ».
- **D-FAC-1 = c** fait de F-VRM-003 le lieu du test de cohérence : la grappe C5 se réduit à des marquages courts plus ce test.
- **Ordre retenu (proposé en 10.05, non contesté) :** A1 → A2 → B1–B5 → C1–C9 → D1–D4 → lots E1/E2 ; observations F sans patch. **Une PATCH-DECISION par grappe.**
- **Interdits maintenus :** aucun patch avant la PATCH-DECISION de sa grappe ; phase 12 interdite tant que la phase 11 n'est pas conforme ; aucun verdict global.

**Prochaine unité : 11.01 PATCH-DECISION A1** (autorité du schéma : F-VRC-007, F-VCT-001, F-VRC-008, F-VRC-006). Sources : rapports VRC 03–04 et VCT 01 de phase 2, 4.04–4.07, protocole §21.
