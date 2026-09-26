# DG-AUDIT-001 — Phase 10.04a — FINDINGS : FAÇADES (18 fiches + 1 nouvelle)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** découper 10.04 en deux passes et commencer par les façades (« Oui, enchaîne avec 10.04a »).

**Sortie :** `DG_AUDIT_001_Phase10_04a_FINDINGS_FACADES.csv`, soit 19 fiches avec les 15 champs du §20 :
- QUICKSTART : 4 ;
- READING_MAP : 2, plus 1 nouvelle ;
- ORCHESTRATION_MAP : 2 ;
- GLOSSAIRE : 2 ;
- skill : 2 ;
- README racine : 1 ;
- références de la skill : 5 (flow 1, examples 3, machine_projection 1).

**Ce que ce rapport n'est pas :** ni une décision de correction, ni un patch, ni un verdict global.

---

## 1. Ajustement du périmètre (annoncé)

En 10.03, j'avais estimé environ 21 fiches de façades, en y rangeant F-ALL et F-WF « à vérifier ». Leurs rapports d'origine montrent que ce sont :
- F-ALL : l'orchestrateur `validate_all` ;
- F-WF : le workflow CI.

Ce sont donc des objets **machine**, qui passent en 10.04b. À l'inverse, F-EX, F-FLOW et F-MP sont des **références de lecture** de la skill : elles restent ici.

**Nouveau découpage :**
- 10.04a : 18 fiches existantes + 1 nouvelle ;
- 10.04b : 38 fiches.

## 2. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan | Plan maître, état 10.03 |
| Empreintes | B01 et protocole conformes (revérifiés en 10.03, aucune écriture depuis) |
| Checkpoint | QUICKSTART, relu pour la disposition des quatre F-QS. Les autres façades n'ont pas de checkpoint propre : leurs rapports uniques font foi, recoupés par le checkpoint final de phase 2 |
| Sources de niveau 5 | Les 18 sections de définition (rapports QS 02/03/08/09, READING_MAP 01, ORCHESTRATION_MAP 01, GLOSSAIRE 01, Skill 01, README racine 01, Flow 01, Examples 01, Machine Projection 01), relues en entier |
| Dispositions ultérieures | 3.01, 4.09, 5.01–5.04, 8.01–8.02, et mes unités 9.07 et 9.08 |

**Deux remarques sur les sources :**
- Sept fiches (skill, README racine, flow, examples, machine_projection) **n'ont pas de gravité en phase 2**. Leur classement ici est un premier classement, pas un écart ; la colonne le dit (« Non fixée en phase 2 »).
- Les gravités du pré-tri 10.00 ne sont **pas** utilisées : ce document est requalifié en index exploratoire (R01).

## 3. Résultat

| Gravité | Nombre | IDs |
|---|---:|---|
| Bloquant, Majeur | 0 | — |
| **Significatif** | **11** | QS-002, QS-003, RM-001, RM-002, **RM-003 (nouvelle)**, OM-001, GLO-002, SK-001, RDR-001, EX-001, EX-002 |
| **Mineur** | **7** | QS-001, QS-004, GLO-001, SK-002, FLOW-001, EX-003, MP-001 |
| **Observation** | **1** | OM-002 |

**Décisions :**
- 11 fiches `RETENU → phase 11` ;
- 7 fiches `RETENU (mineur) → lot éditorial` ;
- 1 fiche `OBSERVATION`.

**Pourquoi aucun Majeur.** Une façade ne porte pas d'autorité propre : chaque document rappelle la primauté des propriétaires, et la lecture complète corrige presque toujours la cellule fautive. Mais ces documents sont justement faits pour être lus **seuls et vite** (QUICKSTART, skill, cartes). C'est pourquoi les raccourcis qui touchent le mode, l'accessibilité, les minima ou la clôture restent Significatif, et ne descendent pas à Mineur.

## 4. Écarts avec la phase 2

**Une fiche est relevée, pour la première fois dans la phase 10 :**

| ID | Phase 2 → 10.04a | Raison |
|---|---|---|
| F-QS-001 | Observation → **Mineur** | Le checkpoint QUICKSTART avait réduit la portée, car les lignes 150–152 lèvent le cas LITE/ITER. Mais 5.01 et 5.04 confirment le **mécanisme résiduel** à deux endroits : QUICKSTART 154 et skill 83 chargent COMPONENTS pour tout SYSTÈME, même pour un token sans composant. Et 9.08 a montré que la surcharge est le coût principal de DG. Défaut textuel confirmé, correction locale : Mineur |

**Une fiche est abaissée :**

| ID | Phase 2 → 10.04a | Raison |
|---|---|---|
| F-GLO-001 | Significatif → **Mineur** | Le lexique n'est pas normatif, et l'étape 64 renvoie à START. La règle de persistance est portée sans ambiguïté par DIRECTION 241 et ACTION. Correction d'une définition |

Toutes les autres fiches notées en phase 2 gardent leur niveau.

**Signal cumulé** (10.01 à 10.04a) : 29 abaissements, 1 relèvement.

## 5. Nouvelle fiche : F-RM-003, granularité des locators

C'est la candidate transmise par la rectification de 10.01. Je la crée ici, parce qu'elle a désormais **une preuve déterministe**, en plus de la mesure de run :

| Source | Mesure |
|---|---|
| 5.02 | Le CLI sert START en 125 lignes, CRAFT en 181, SELECT en 94 |
| 5.04 | La skill 79 demande « l'arbre seulement », mais l'extraction sert tout le bloc parent, Boot et Domain Frame compris : « la condition de lecture n'est pas portée par l'extraction » |
| 9.08 (run réel) | START = 130 des 163 lignes de la route LITE (**80 %**) ; l'arbre utile tient en une quinzaine de lignes |

Le CLI sert toujours ce même bloc : la mesure ne dépend pas du nombre de runs.

- **Gravité : Significatif.** C'est le coût de contexte le plus lourd mesuré sur les routes courtes, là où la proportionnalité devait être le point fort de DG.
- **Propriétaires :** READING_MAP (granularité de la table) et `read_route.py` (extraction).
- **Distinctions :** ce n'est ni F-DIR-044 (taxonomie de lecture), ni F-DIR-028/F-ACT-001 (locators refusés). Ici le locator est **accepté**, mais sert trop.

**À confirmer par l'owner :** si vous refusez ce nouvel ID, la mesure reste une observation transversale sans ID, comme en 5.02. Le registre passerait alors de 158 à 157 fiches.

## 6. Constat transversal : une deuxième décision préalable (D-FAC-1)

**Huit fiches ont la même cause :** RM-001, RM-002, OM-001, QS-002, RDR-001, QS-001, GLO-001 et FLOW-001. Une cellule de façade, lue seule, **perd la condition** que le propriétaire attache à la règle :
- une route forcée devient facultative ;
- une exclusion déclarée devient N/A ;
- le craft devient un critère de mode ;
- un minimum SYSTÈME devient un renfort ;
- ITER perd sa direction existante.

5.01 et 5.04 l'avaient déjà nommé (« une cellule isolée peut s'interpréter comme permission concurrente »).

Corriger ces cellules une à une traite les symptômes. La cause est une question d'architecture.

**D-FAC-1 — Quel statut pour une façade lue seule ?** (à décider par l'owner en phase 11)

| Option | Effet | Coût |
|---|---|---|
| **a. Façades autosuffisantes** | Chaque cellule répète la condition du propriétaire | Façades plus longues ; risque de dérive entre copie et source |
| **b. Façades en pointeurs** | Plus de règles résumées, seulement « ouvrir START / ACTION/… » | Perd la vitesse d'entrée, qui est leur raison d'être |
| **c. Façades bornées et testées** | Les cellules gardent un résumé, mais toute règle normative y est marquée « condition : voir propriétaire », et un **test de cohérence** façade ↔ propriétaire tourne au build | Un test à écrire (à rapprocher de F-VDG en 10.04b) ; chaque cellule reste courte |

D-FAC-1 est à traiter avec D-ACT-1 : les deux posent la même question sous deux angles (**qu'est-ce qui fait autorité hors du propriétaire ?**). D-ACT-1 la pose pour la RUN_CARD, D-FAC-1 pour les façades.

## 7. Ce que les preuves d'objet ont changé

| Fiche | Observation |
|---|---|
| **F-SK-001** | 9.08 : pour une correction LITE, 9 champs HANDOFF sur 13 deviennent N/A-JUSTIFIED, alors que DAILY fixe 4 éléments de clôture. La fiche passe d'une ambiguïté de portée à un **coût mesuré** : Significatif |
| **F-RM-002, F-GLO-002** | 9.07 : sur le pilote B, les contrôles d'accessibilité appliqués tard ont trouvé des défauts réels (contraste, O4 ; bouton sans contour en couleurs forcées, O9). Un N/A déclaratif ou une réserve sans suivi aurait caché des défauts présents. Les deux restent Significatif |
| **F-RM-003** | 9.08 : 80 % de la route LITE (voir §5) |
| **F-QS-001** | 9.08 : la surcharge est le coût principal de DG ; le relèvement s'appuie sur cette mesure |

## 8. Déduplication et grappes pour la phase 11

Aucune fusion.

| Grappe | Fiches de ce lot | Rejoint |
|---|---|---|
| **0 — Décision D-FAC-1** | RM-001, RM-002, OM-001, QS-002, RDR-001 ; en éditorial : QS-001, GLO-001, FLOW-001 | D-ACT-1 |
| **1 — Protection critique et exception** | QS-003 | F-ACT-038, F-ACT-039, F-ACT-023 |
| **2 — Proportion** | SK-001, RM-003 ; QS-001 (m) | F-ACT-002, F-BIB-002 ; mesures 9.08 |
| **2 — Exemples de référence (nouvelle)** | EX-001, EX-002, GLO-002 ; EX-003 (m), MP-001 (m) | F-ACT-013, F-ACT-018, F-ACT-023 |
| **3 — Accès et distribution** | SK-002 (m), QS-004 (m) | F-DIR-028, F-ACT-001 ; F-BLD (10.04b) |
| **Observation** | OM-002 | Grappe homogénéisation (F-SAV-002) |

**Pourquoi une grappe « Exemples de référence ».** Les agents imitent les exemples plus fidèlement qu'ils n'appliquent les règles. Cinq exemples du corpus enseignent une forme fautive :
- un changement d'artefact présenté comme une décision ;
- une capture étendue à la tâche ;
- une réserve d'accessibilité sans suivi ;
- un NOT-OBSERVED mal employé ;
- un YAML qui échoue au validateur.

Un seul cycle de correction des exemples est bon marché. Il protège aussi plusieurs règles Majeur d'ACTION (F-ACT-018, F-ACT-023) du côté de l'apprentissage, là où la machine ne les protège pas.

## 9. Sortie

- **19/19 fiches classées** : 18 existantes + F-RM-003.
- **Registre : 120 classées sur 158** (157 + F-RM-003, sous réserve de confirmation). Restent 38 fiches machine (10.04b).
- Une décision d'architecture, D-FAC-1, est formulée pour l'owner.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- le premier relèvement de la phase 10 (F-QS-001) ;
- une nouvelle fiche appuyée par une mesure déterministe ;
- huit fiches de façade ramenées à une seule décision préalable ;
- une grappe « exemples » qui relie les exemples aux Majeur d'ACTION ;
- le périmètre 10.04a/b corrigé et annoncé.

**Prochaine unité : 10.04b machine** (38 fiches : F-VRC 8, F-BLD 4, F-VDG 4, F-FIX 3, F-VCT 3, F-VRM 3, F-DF 2, F-MAN 2, F-PC 2, F-RB 2, F-ALL 2, F-RC 1, F-RRT 1, F-WF 1). Arbitrages attendus :
- F-ACT-010 face à F-RC-001 ;
- F-ACT-008 face aux F-FIX ;
- le lien entre le test de cohérence de D-FAC-1 (option c) et F-VDG.
