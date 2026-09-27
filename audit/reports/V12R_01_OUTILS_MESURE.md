# V1.2 refonte — Unité R1 — Outils de mesure et cartographie des harnais

**Date :** 2026-09-27 · **Plan :** `plans/Plan_V1.2_Refonte.md`, lot R1 · **Décisions :** `V12R_00`
**Périmètre :** outils d'audit **hors package**. `package/` n'est pas modifié ; B01 est à 218/218.

## 1. Livrables

| Fichier | Rôle |
|---|---|
| `audit/tools/V12R_Mesures.py` | Cinq mesures déterministes : budget sur trois périmètres, atteignabilité des 25 outils de fabrication, indicateurs par fichier (méthode unique), doublons (amas), listes de chargement `DIRECTION` |
| `audit/data/V12R/V12R_perimetres.json` | Périmètres ACTUEL, TABLE et LETTRE. **Chaque élément est justifié par une citation du package** ; une citation disparue est signalée « PÉRIMÉ » |
| `audit/data/V12R/V12R_outils_fabrication.json` | Les 25 outils de `V12_11` §3, chacun repéré par une citation distinctive |
| `audit/data/V12R/V12R_listes_chargement.json` | Les six listes « première lecture » `DIRECTION` des façades |
| `audit/tools/V12R_Carto_harnais.py` | Cartographie des 389 cas de harnais par **test de sensibilité à la prose** |
| `audit/data/V12R/V12R_Carto_harnais.csv` (+ `_brut.json`) | Par cas : catégorie, fichiers sensibles, voie, libellé |
| `audit/data/V12R/V12R_Mesures_B05.json`, `audit/logs/V12R/` | Mesures de référence B05 et sorties des harnais |

## 2. Mesures de référence B05

### Budget d'un run `DIRECTION`

| Périmètre | Définition | Lignes | Mots |
|---|---|---|---|
| ACTUEL | Périmètre de `V12_Budget_lecture.py` | 614 | 9 591 |
| TABLE | Table de charge de la skill + renvois impératifs de `RUN-DIRECTION` (pipeline, preuve visuelle, clôture) + handoff | 1 069 | 16 339 |
| **LETTRE** | TABLE + README, QUICKSTART, ORCHESTRATION_MAP et `DOUBLE-LOOP`, que la skill prescrit aussi | **1 662** | **23 891** |

Le chiffre estimé à la main en `V12_11` (≈ 23 600 mots) est confirmé à 1 % près. **La cible du plan (≤ 14 000 mots) se mesure sur LETTRE.**

### Atteignabilité des 25 outils de fabrication

| Périmètre | Sur le chemin | Outils |
|---|---|---|
| ACTUEL | 3 / 25 | F01, F02, F07 |
| TABLE | **7 / 25** | + F03 à F06 (CFT-00, B1b, Gate C, passe créative) |
| LETTRE | 10 / 25 | + F23 à F25 (table de diagnostic, six questions, « un axe à la fois ») |

Hors d'atteinte sur tous les périmètres : **F08 à F22**. Cela couvre la tension, la grammaire positive, la singularité, la forme située, la composition, la question de convergence, le vocabulaire perceptuel, les calibrations, la repasse, **les marqueurs de vague**, **la carte des moyens**, et les outils structurels de BIBLIOTHEQUE. D-07 est détecté par l'outil.

### Indicateurs (méthode unique, 16 fichiers)

| Total | Mots | Négations défensives | Auto-limitation | Jetons distincts (par fichier, sommés) | Champs de trace (blocs de code) | « beau » |
|---|---|---|---|---|---|---|
| B05 | 69 457 | **863** | 234 | 1 053 | 177 | 36 |

Le détail par fichier est dans le journal. Les comptes de `V12_05` à `V12_10`, faits avec des expressions différentes, **sont remplacés** par ceux-ci pour toute comparaison future (déclaré).

### Doublons

**79 amas, 190 occurrences** : des phrases ou lignes de table quasi identiques, dans des fichiers différents ou éloignés. L'outil retrouve les doublons établis à la main :
- boucle (×4) ;
- promesse du validateur (×3) ;
- réponse visible (×3) ;
- paragraphe one-shot SAVOIR / BIBLIOTHEQUE ;
- définition du polish ;
- table des cinq questions de QUICKSTART ;
- réserve sur `ANCHOR-GENERATED` ;
- lignes des 8 dimensions.

### Listes de chargement `DIRECTION`

- **6 listes, 5 distinctes.**
- **Correction de `V12_08` §3.3** (« aucune identique ») : READING_MAP et ORCHESTRATION_MAP portent le même ensemble de routes, dans un ordre différent.
- `ACTION/FIRST-RENDER` et `ACTION/ROUTING` n'apparaissent que dans la skill.
- La mention « gates A/B/C » n'est pas un jeton de route. Elle n'est pas comptée (limite déclarée).

## 3. Cartographie des harnais

**Méthode :**
- Les harnais tournent sur des copies du package dont la prose est altérée **de façon invisible** : un caractère U+200B est inséré dans chaque mot de 3 lettres ou plus.
- Restent intacts : les titres, les blocs de code et les jetons entre backticks.
- Un cas qui passe au rouge dépend de la **formulation** exacte ; un cas qui reste vert dépend de la **structure** (titres, locators, jetons, schéma, scripts).
- Il y a huit variantes : témoin non altéré, tout altéré, puis chaque groupe de fichiers.

**Résultats (certain) :**

| | Cas |
|---|---|
| Total (22 harnais + R + R03, témoins compris) | 389 |
| Témoin non altéré | 389 verts |
| **Structure seule** (survivent à toute reformulation) | **233** |
| **Sensibles à la prose** | **156** |
| – dont par voie directe (garde qui lit une phrase) | 98 |
| – dont via le validateur de façade ou `validate_all` (les 50 LCF lisent des phrases) | 58 |

Fichiers dont dépend la sensibilité (un cas peut en avoir plusieurs) : façades 78, ACTION 53, DIRECTION 46, SAVOIR 29, skill 19, BIBLIOTHEQUE et CHANGELOG 21.

Harnais entièrement structurels :
- A1 ;
- B1 à B4 ;
- C9.

Harnais presque entièrement ancrés sur la prose :
- C5 (16/20) ;
- C6 (8/10) ;
- D1 (9/10) ;
- R (26/31) ;
- R03 (16/18) ;
- E1 (20/29).

**Conséquence pour R2 (probable) :**
- les 58 cas « via validateur » tombent ensemble dès que les LCF de phrases sont remplacées par des gardes de propriété ;
- les 98 cas directs demandent chacun une ligne dans la table de correspondance : propriété conservée (et garde qui la porte) ou obsolète par décision.

**Limites déclarées :**
1. Une garde qui vérifie une **absence** de phrase reste verte sous altération. Elle est classée « structure » alors qu'elle lit du texte, mais elle ne fige pas la prose.
2. Une garde qui ne lit que des jetons entre backticks est classée « structure ». Elle fige les jetons, pas la formulation.
3. Un cas (union des groupes 156, variante « tout » 155) n'échoue que lorsqu'un seul groupe est altéré. C'est une garde de cohérence entre deux fichiers : altérés ensemble, ils restent cohérents.
4. La voie (directe ou via validateur) est attribuée par mots-clés du libellé. C'est une heuristique, à revoir cas par cas en R2.

## 4. Écarts déclarés

1. **Premier détecteur de doublons rejeté** : les paragraphes entiers avec Jaccard ≥ 0,5 ne trouvaient que 11 paires et manquaient des doublons établis (critère d'arrêt de R1). Il est remplacé par une comparaison au niveau de la phrase (Jaccard ou inclusion) regroupée en amas.
2. **Correction de `V12_08` §3.3** : 5 listes distinctes sur 6, et non 6.
3. **Comptes d'indicateurs** : les chiffres des lectures sont remplacés par ceux de l'outil unique.
4. **Faux positifs connus des doublons** : les lignes de la table des locators de READING_MAP reprennent des titres d'ACTION et de DIRECTION. C'est de l'indexation voulue, pas une copie de contenu. R2 les exclura.

## 5. Lecture

- **Certain :** les mesures B05 ; la cartographie (témoin intact, 156 cas sensibles, 233 structurels) ; la confirmation outillée de D-05, D-07 et des doublons.
- **Probable :** que le remplacement des LCF de phrases par des gardes de propriété règle d'un coup les 58 cas indirects.
- **Limite :** outils écrits par le même modèle que l'auteur du plan ; leurs définitions (périmètres, ancres, seuils) sont des choix explicites, versionnés dans `audit/data/V12R/`.

## 6. Suite : R2 (PATCH-DECISION à soumettre)

1. Un **registre des concepts** (« une chose, un lieu ») : identifiant, fichier propriétaire, ancre, lieux de renvoi autorisés.
2. Des **gardes de propriété** dans le validateur :
   - unicité des définitions ;
   - listes de chargement égales ;
   - atteignabilité ;
   - vocabulaire `MODAL`/`PARTI` ;
   - fidélité de la prise de brief ;
   - honnêteté.
3. Pour chaque garde, un témoin rouge sur B05 là où un défaut est connu, et une mutation rouge.
4. La **table de correspondance** des 389 cas.
