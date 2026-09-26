# V1.2 — Unité 02 — PATCH-DECISION des chantiers A, B et D (porte G2)

**Date :** 2026-09-26 · **Owner :** Junior (Kamel) · **Statut : rédigée, gardes G2 tenues sur maquette ; à valider par l'owner avant application (G3).**
**Base :** V1.1.1 (`package/`). **B05** = branche `v1.2/patch-decision-abd` ; `package/` y reste V1.1.1 jusqu'à l'application en G3.
**Décisions amont :** `V12_01_DECISIONS_G1.md` (G1, et les trois contraintes validées par l'owner le 26-09-2026).

## 1. Périmètre, critères

- **Inclus :** A (bilan de fabrication, trace seule), B (prise de brief minimale), D (anti-slop vivant : `MODAL`/`PARTI`, marqueurs datés), plus des coupes de doublons (C-) au titre de la contrainte « réduire le budget ».
- **Exclus :** C et E (après G4) ; version, CHANGELOG et notes de version (écrits en G3) ; schéma `RUN_CARD` inchangé (décision 1 : trace seule).
- **Réussite G2 :** gardes rouges sur V1.1.1, vertes après patch, rouges sous mutation ; non-régression complète verte sur maquette ; budget de lecture en baisse.
- **Arrêt :** un ancien texte introuvable ou non unique ; une régression de harnais qu'on ne peut résoudre sans rectification non déclarée.

## 2. Artefacts

| Artefact | Rôle |
|---|---|
| `audit/tools/V12_Patch_ABD.py` | Textes exacts (29 entrées), gardes LCF-43 à 46, modes `--verifier`, `--inverse`, `--mutations` |
| `audit/tools/V12_Budget_lecture.py` | Mesure déterministe du budget d'un run `DIRECTION` (outil nouveau, déclaré) |
| `audit/diffs/V12_PATCH_ABD_maquette.diff` | Diff complet V1.1.1 → maquette patchée (7 fichiers, 256 lignes) |
| `audit/snapshots/V12_Instantane_harnais_patch_ABD_maquette.json` | Instantané des 22 harnais sur la maquette |

## 3. Contenu du patch

| Entrées | Chantier | Où | Effet |
|---|---|---|---|
| P-A1 | A | `DIRECTION/START`, entrée minimale | `CONSTRAINT` inclut la destination (démo, prototype, produit réel) et l'enjeu identitaire |
| P-A2 | A | Creative Boot | `FABRICATION` remplace `ANCHOR-BASIS` et `ANCHOR-LIMIT` (les absorbe) : moyens → plafond par couche → décision |
| P-A3, P-A6 | A | Boot ; `ACTION/FIRST-RENDER` | Capacités absentes : plafond déclaré avant le build, le rendu sort quand même |
| P-A4 | A | `VISUAL_TARGET`, route de production | La destination tranche : produit réel → jamais de faux asset ; démo → approximation marquée ; contenu absent → emplacement illustratif |
| P-A5 | A | `ACTION`, profil de capacités | Observation (profil) distincte de fabrication (`FABRICATION`) |
| P-B1 | B | `DIRECTION/EXTERNAL-START` | Prise de brief : au plus trois demandes, ordre contenu réel → marque → asset principal → destination ; humain absent : hypothèses, plafond déclaré ; construire dans tous les cas |
| P-B2, P-B3 | B | QUICKSTART, skill | Même ordre, renvoi à `EXTERNAL-START` |
| P-D1, P-D2, P-D3 | D | Boot, tableau d'architecture | `MODAL` / `PARTI` remplacent `ANTI-DIRECTIONS` ; projeté dans `direction.anti_direction` (schéma inchangé) |
| P-D4, P-D5, P-D6 | D | QUICKSTART, skill | Copies du boot : `MODAL`/`PARTI`, `FABRICATION` |
| P-D7, P-D8 | D | QUICKSTART §9, exemples de la skill | Exemples formulés en décisions (modal nommé, parti), sans style nommé |
| P-D9 | D | SAVOIR, `[VEILLE 2026-09]` | Marqueurs de vague 1 et 2 datés, sourcés, « pour nommer, jamais pour interdire », à revoir avant 2027-03 |
| P-C1 à P-C9 | C- | Boot, EXTERNAL-START, VISUAL_TARGET, skill | Coupes de doublons (propriétaires déjà dans `START`, liste des 8 dimensions répétée, paragraphe de qualité condensé, etc.) |
| P-L1, P-L2 | Gardes | `scripts/validate_reading_map.py` | LCF-43 à 46 |

**Gardes :**

| LCF | Vérifie | Mutation |
|---|---|---|
| LCF-43 | Destination dans l'entrée, `FABRICATION` dans le boot sans `ANCHOR-*`, « jamais un faux asset » dans la route de production, renvoi dans ACTION, QUICKSTART, skill | inverse de P-A2 |
| LCF-44 | Même ordre de demandes et « au plus trois » dans EXTERNAL-START, QUICKSTART, skill | inverse de P-B1 |
| LCF-45 | `MODAL:` et `PARTI:` dans le boot, sans `ANTI-DIRECTIONS:` ; copies dans QUICKSTART, skill, exemples | inverse de P-D1 |
| LCF-46 | Aucun marqueur de vague hors d'une ligne `[VEILLE 20..]` dans les textes et façades ; au moins une telle ligne dans SAVOIR | inverse de P-D7 |

## 4. Résultats (maquette = copie de V1.1.1 + patch)

| Contrôle | Résultat |
|---|---|
| `--verifier` sur V1.1.1 | 29/29 anciens textes présents une fois |
| Gardes sur V1.1.1 (gardes seules injectées) | **4/4 rouges** |
| Gardes sur maquette | **vertes** ; `validate_reading_map` 46 conditions vertes |
| Mutations | **4/4 rouges** |
| `validate_all` | FULL VALIDATION PASSED |
| 22 harnais (suivi, comparé à B04 R03) | **300/300**, témoins 40/40, 0 rouge |
| Harnais R ; R03 | 30/30 (témoin 1/1) ; 18/18 |
| 13.01 texte ; non-régression B01 | 6/6 ; 5/5 |
| 13.02 épreuves déterministes | 38/38 |

**Budget de lecture** (`V12_Budget_lecture.py`, skill + READING_MAP + 7 routes `DIRECTION`) : **614 → 614 lignes ; 9 608 → 9 604 mots (−4, −0,04 %).**

## 5. Écarts déclarés

1. **Deux collisions résolues sans toucher aux harnais.** (a) Le harnais R (R-17) utilise comme mutation un texte posé par R01 dans QUICKSTART ; P-D4 et P-D6 ont été réécrits pour ajouter `MODAL`/`PARTI` sans modifier ce texte (29/30 → 30/30). (b) Le harnais C4 plafonne `DIRECTION/START` à 76 lignes ; la destination a été fusionnée dans `CONSTRAINT` au lieu d'une ligne `DESTINATION` (299/300 → 300/300). Aucune rectification de harnais.
2. **Garde E1-08 devenue en partie vide.** Elle lit la ligne `ANTI-DIRECTIONS:` du boot, qui disparaît ; sa condition « pas de nombre » reste vraie sur une ligne vide. Pas de rouge, mais une vérification sans objet : **à rectifier en G3** (proposer : lire `PARTI:`), rectification à déclarer.
3. **Garde B placée sur `EXTERNAL-START`, pas sur `START`.** Le plan (§5) visait `START` ; la prise de brief concerne le brief vague, dont `EXTERNAL-START` est la vue ; `START` et son plafond de 76 lignes restent intacts.
4. **Coupes de doublons (C-).** Elles ne découlent pas d'un défaut, mais de la contrainte « réduire le budget » validée par l'owner ; elles sont listées une par une dans le script et le diff, et soumises à la même validation.
5. **Branche et étiquette.** B05 est la branche `v1.2/patch-decision-abd` (créée par erreur puis retenue par l'owner) ; la session ne peut pas pousser d'étiquette.
6. **Gardes en auto-comparaison.** Textes, gardes et contrôles sont du même auteur ; aucune revue extérieure du diff.

## 6. Lecture

- **Certain :** le patch est applicable (29/29), non régressif sur tous les outils existants, et gardé (4 LCF rouges puis vertes, mutations rouges).
- **Certain :** le budget ne baisse que de 4 mots. La contrainte « réduire » est tenue au sens strict, pas de façon significative. Une vraie baisse demande de fusionner des vues qui se recouvrent (`START`, `DAILY`, `FAST-PATH`, `EXTERNAL-START`, boot et `VISUAL_TARGET`) : c'est un chantier en soi, hors de A, B, D.
- **Probable :** A et D rendent explicite ce que l'épreuve B-DLA a montré (la palette modale ; le signalement du contenu d'exemple). Le gain déjà observé de V1.1.1 (l'honnêteté) est renforcé, pas affaibli.
- **Hypothétique :** que A, B, D améliorent la qualité perçue. Seule l'épreuve G4 peut le dire ; la référence B-DLA donne C4 ≈ C1.

## 7. Décision attendue de l'owner (pour ouvrir G3)

1. Valider la PATCH-DECISION telle quelle (29 entrées, 4 gardes), ou demander des changements entrée par entrée.
2. Accepter la rectification déclarée de E1-08 en G3 (écart 2).
3. Dire si l'on ouvre un chantier « budget » dédié (fusion de vues), puisque A, B, D ne peuvent pas à eux seuls réduire le budget de façon significative.

## 8. Non-régression de l'unité

`package/` et `reference/` non modifiés. B01 218/218 en début et en fin d'unité.
