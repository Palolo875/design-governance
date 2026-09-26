# DG-AUDIT-001 — Phase 12.04 — PATCH : migration unique

**Date :** 25 septembre 2026. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée. **Format :** rapport allégé.

**Commit :** `8eb95da`, étiquette `12.04-migration`.

**Fichiers produits :**
- `DG_AUDIT_001_B03_12-04_migration.diff` ;
- `12-04_scripts_migration/`, qui contient le script de migration des données et l'écrivain JSON qui préserve la mise en forme ;
- `DG_AUDIT_001_B03_package_12-04.zip` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-04.json`.

**Décisions appliquées.** La liste des schémas de 11.21 §5 est appliquée **en entier**, avec :
- les **48 invariants nouveaux** de la liste close : RUN_CARD 38 (B1 7, B2 10, B3 4, B4 6, C1 6, C2 1, C4 2, D2 2) et contrats 10 (C2 3, C3 2, C9 3, E2 2) ;
- les retraits E11, K01, K04, K08, K10, K11 et K12, et les généralisations E02, E17 et E24 ;
- la CLI des contrats (C9 O-1 et O-2) ;
- E2 O-12 (R-3 de 11.23) ;
- la rectification R-6 (12.01 §4.1), appliquée faute d'objection.

## 1. Diff (36 fichiers, +1181 / −290)

| Fichier | Contenu |
|---|---|
| `run_card.schema.json` | Les 19 changements de B1 à C2 : `risk.statement`, `critical_protection.result`, `direction.identity_stake` et `calibration`, `anchors[].type`, `artifact.version` et `rights_status`, `basis` typée, `provenance.capability`, `profile_decision.phase`, `decision_change.outcome` et `reason`, `closure.verdict` nullable, `axes`, `reservations`, `exception`, `system_package`, `b1b`, `reclassification` ; ITER ajouté à l'exigence de `trace_locator`. « Au moins un ancrage » n'était pas dans le schéma, mais dans le validateur : il est remplacé par INV-B4-6 |
| `production_contracts`, `domain_frame`, `research_brief` (schémas) | `required` racine vidé ; `expected_scope` et `observed_scope` ; jetons `OBSERVED`, `NOT-VERIFIED` et `N/A-JUSTIFIED` avec `reason` ; `structural_changes` en `minItems 1` ; `risk_coverage` ; `evidence_plan` en objets à cinq composantes ; `source_status`, `source_date`, `source_locator`, `rights_status` ; `entries` en `minItems 0` |
| `validate_run_card.py` (+424 / −103) | Contrôle sémantique réorganisé en fonctions par grappe (protection critique, temps, exception, acceptation, conséquence, paquet SYSTÈME, B1b, DIRECTION). Profil strict INV-C4-2 : exigences du mode, hôtes de démonstration pour les deux locators, locators locaux résolus **depuis le dossier de la carte**. **53 cas unitaires nouveaux** (76 au total) |
| `validate_contracts.py` (+231 / −94) | Contrôles par contrat ; règle R-6 au chargement ; `check_negative_mutations` remplacé par une **table de 20 cas unitaires** avec motif ; CLI `--type`, détection par les clés racines, fichiers hors du package acceptés |
| `validate_all.py` | Consommateur de INV-C4-2 : la carte stricte de test référence l'exemple par un chemin absolu |
| Données | L'exemple RUN_CARD, les **25 fixtures**, les 3 exemples de contrats et le YAML de `machine_projection.md` (F-MP-001 : `provenance.artifact_locator` = `artifact.locator`) |

**Mise en forme des données.** Les fichiers JSON sont réécrits dans leur style d'origine : indentation standard, ou « une ligne par champ » pour cinq fixtures. Le diff ne montre donc que les champs ajoutés. Les exemples de contrats, écrits à la main, ont été édités en texte.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Suite RUN_CARD | Fixtures **25/25** déclarées ; cas unitaires **76/76** |
| Suite contrats | 3 exemples valides ; cas unitaires **20/20** |
| Verdicts ciblés (29 documents) | **Identiques à B01** : aucune fixture ne change de verdict, chacune garde son motif |
| Harnais RUN_CARD | B1 **12/12** ; B2 **19/19** ; B3 **12/12** ; B4 **12/12** ; C1 machine **13/13** ; C2 RUN_CARD **6/6** ; C4 RUN_CARD **6/6** ; D2 RUN_CARD **6/6** |
| Harnais contrats | C2 contrats **10/10** ; C3 **6/6** ; C9 **11/11**, CLI **3/3** ; E2 contrats **5/5** (E2-04 à E2-08) |
| A1, A2, vérifications X et Y | A1 11/11, A2 5/5, X **7/7**, Y **6/7** (Y-7 n'est pas significatif pendant la fenêtre : `validate_all` s'arrête plus tôt, sur `SEED`) |
| Contre-épreuve (gardes neutralisées) | **FULL VALIDATION PASSED** : 76/76 et 20/20 dans chaque distribution construite ; double construction identique |
| Suivi (`--fenetre --rectifies C2,C3,C4,C9,E2 --compare 12.03`) | **Cas verts significatifs : 27 → 149/300**, aucune alerte. Les huit témoins rouges sont ceux de la fenêtre ; la contre-épreuve les rend tous verts |
| B01 | 218/218, aucun fichier généré |

**Tous les cas machine des grappes B1 à D2 sont verts.** Ce qui reste rouge relève d'autres étapes :
- les gardes textuelles (12.05) ;
- les budgets de lecture et le titre en double de C4 (12.05, T-4 et T-5) ;
- les outils de 12.06 ;
- la LCF (12.05).

## 3. Écarts et rectifications déclarés

| # | Écart | Traitement |
|---|---|---|
| **R-6** | Conflit A1 × C2 sur la racine de `production_contracts` (12.01 §4.1) | Appliquée : `required` vide n'est admis que pour un contrat déclaré « au moins un », dont la racine est typée et fermée. Le témoin injecte alors une valeur de mauvais type (`$.creative_direction_set: type attendu`). A1 reste à 11/11, X-6 reste rouge pour son motif |
| **R-8** | Les harnais C2, C3 et C9 convertissaient l'**ancien** exemple (`proof_scope`, jetons en minuscules). Contre l'exemple migré, ils auraient planté ; et K-04 supposait que l'exemple garde `proof_scope` | **Rectification de harnais** : la conversion ne s'applique qu'à l'ancienne forme. K-04 réinjecte `proof_scope` dans l'exemple migré et exige toujours son refus, pour le même motif. **Aucun motif ni verdict attendu n'est changé** |
| **R-9** | C4-P4 (« ITER avec trace → acceptée ») a été écrit **avant** D2, qui exige ensuite le rappel `direction.thesis` d'un ITER (INV-D2-2) | **Rectification de harnais** : la carte ITER de C4 reçoit une thèse. C4-01 continue d'isoler la seule faute de trace |
| **R-10** | E2-06 (« depth none, aucune entrée → acceptée ») gardait l'incertitude modifiée de l'exemple, alors que la décision E2 (INV-E2-2) exige « aucune entrée ⇒ incertitude inchangée » | **Rectification de harnais**, alignée sur la décision : l'incertitude d'arrivée est celle de départ |
| Exception FAIL-ASSUMED | B1 (I-B1-4) liste six champs de réserve, sans `date_version`. B2 dit que l'exception « étend » la réserve à sept champs. Le cas positif de B1 (B1-P3) n'a pas de `date_version` | **Choix de B1** : l'exception reprend la réserve commune **sans** `date_version`, puisque la date est celle de la carte. La structure est définie une seule fois dans le validateur (`RESERVATION_FIELDS`, `EXCEPTION_FIELDS`). Le schéma la répète, car le sous-ensemble de schéma ne gère pas les références |
| E17 généralisé par B2-1 | La fixture FAIL-ASSUMED et deux cas unitaires attendent « issue bloquante ou FAIL-ASSUMED » | **Une seule règle**, « issue non nulle interdit un verdict accepté ». Pour BLOCKED et FAIL-ASSUMED, le message garde l'ancienne formulation en complément : aucun motif existant n'est réécrit (A2 C4) |
| Placeholders | La liste était propre à la protection critique ; les nouveaux champs en demandent une plus large (« à compléter », « à déterminer », « ? ») | **Une liste unique** par validateur. La protection critique refuse donc aussi ces nouvelles formes (léger durcissement, déclaré) |
| INV-C4-2 | « Existence des locators locaux » : la décision emploie le pluriel | L'existence est vérifiée pour `artifact.locator` **et** `trace_locator`, quand ils ont une forme de chemin. Cela reste une interprétation, déclarée |
| E2 O-11 (partiel) | L'analyse d'URL est désormais protégée dans le profil strict réécrit | Appliquée ici ; E2-20 est vert. Le reste d'O-11 (pré-passe de types) reste en 12.06 |
| Mutations négatives des contrats | Deux des quatre anciennes mutations testaient K01 et K04, qui sont **retirés** | Elles sont remplacées dans la table de cas unitaires par les invariants de remplacement (C9-1, E2-2). K-06 et K-09 sont conservés |

**Contenu de l'exemple canonique, migré.** Une `basis` déclarative apparaissait dans l'exemple. B2 C4 le relevait : elle enseignait le cas même que F-ACT-018 décrit. Elle est remplacée par deux bases attestées. L'exemple déclare aussi :
- les axes V PASS, U NOT-VERIFIED, A NOT-VERIFIED et T PASS, cohérents avec son `not_verified` et ses capacités indisponibles ;
- une réserve complète sur la transition mobile, qui est son défaut dominant ;
- une paire B1b réalisée ;
- `identity_stake: normal`, `rights_status: not_applicable` et un ancrage `observed`.

**Non ajouté, faute d'accord :** les cas unitaires des environ quatorze invariants existants sans négatif (12.02 §2.2).

## 4. Fiches

**Levées côté machine (certain) :** toutes les fiches des grappes B1 à B4, C1 (partie machine), C2 (projection et contrats), C3, C4 (profil strict et ITER), C9, D2 (partie machine) et E2 (F-DF-002, F-RB-002, F-VRC-004), ainsi que F-MP-001.

**Leur partie texte reste à faire en 12.05 :** gardes G-xx, ACTION/RUN_CARD, promesse du validateur, `machine_projection.md` pour la prose.

**Journal des notes de version (B03), ligne ajoutée :**

> 12.04 — Migration unique des schémas RUN_CARD et contrats : protection critique à résultat, exception FAIL-ASSUMED structurée, axes, réserves, capacité et version de la preuve, droits, paquet SYSTÈME, B1b, ancres typées, conséquence décisionnelle, temps du verdict, reclassement ; contrats à objets facultatifs, scopes séparés, jetons canoniques, couverture risque → contrôle, sources qualifiées, plan de preuve structuré ; CLI des contrats ouverte aux fichiers externes avec --type. Chaque invariant nouveau a son cas unitaire.

## 5. Suite

**Prochaine unité : 12.05, les passes de texte.** Ordre de 11.23 §7 : CHANGELOG → BIBLIOTHEQUE → ACTION → DIRECTION → SAVOIR → cartes et glossaire → façades.

**Charge : lourde.** ACTION et DIRECTION concentrent la plupart des corrections. Je propose **trois unités :**

| Unité | Passes |
|---|---|
| **12.05a** | CHANGELOG et BIBLIOTHEQUE. `SEED` y devient vert |
| **12.05b** | ACTION |
| **12.05c** | DIRECTION, SAVOIR, cartes, glossaire, façades |

**La fenêtre de garde se ferme à la fin de 12.05c.** À ce moment, la LCF et les gardes textuelles doivent être vertes, ou leurs écarts déclarés.
