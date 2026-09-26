# V1.2 — Unité 03 — G3 : application de la PATCH-DECISION A, B, D sur B05

**Date :** 2026-09-26 · **Owner :** Junior (Kamel)
**Décision :** l'owner a délégué les trois choix de `V12_02` §7 (« À toi le choix ») ; l'auteur a retenu : (1) PATCH-DECISION validée telle quelle ; (2) rectification de E1-08 en G3 ; (3) pas de chantier « budget » avant une mini-épreuve V1.2.
**Branche :** `v1.2/patch-decision-abd` (B05), synchronisée avec la branche de session. `main` reste en V1.1.1.

## 1. Ce qui a été fait

1. `python3 audit/tools/V12_G3_Application.py package` : 29 entrées de `V12_Patch_ABD.py`, plus l'entrée CHANGELOG « Non publié — candidate V1.2 (B05) » (texte exact dans le script).
2. **Rectification déclarée V12-03 du harnais E1** (`E1_harnais_non_regression.py`, cas E1-08) : `boot_anti` lit `PARTI:` et, à défaut, `ANTI-DIRECTIONS:`. Motif : la ligne `ANTI-DIRECTIONS:` disparaît du boot, et la vérification serait devenue vide ; elle reste valable sur V1.1.1 comme sur B05.
3. Nouvel instantané : `audit/snapshots/V12_Instantane_harnais_B05_G3.json`.

**Version affichée : V1.1.1, inchangée.** Le passage à V1.2.0 (titres, `package_manifest.json`, notes de version) se fait à la publication, après G4. Motif : les harnais R et R03 lisent la chaîne de version ; la changer maintenant imposerait des rectifications sans bénéfice.

## 2. Résultats sur `package/` (B05)

| Contrôle | Résultat |
|---|---|
| `validate_all` | FULL VALIDATION PASSED |
| `validate_reading_map` | vert, 46 conditions |
| Mutations LCF-43 à 46 | 4/4 rouges |
| 22 harnais (suivi, comparé à B04 R03) | **300/300**, témoins 40/40, 0 rouge ; alerte attendue « E1 : harnais modifié » (rectification V12-03) |
| Harnais R ; R03 | 30/30 (témoin 1/1) ; 18/18 |
| 13.01 texte ; non-régression B01 | 6/6 ; 5/5 |
| 13.02 épreuves déterministes | 38/38 |
| Budget de lecture (`V12_Budget_lecture.py`) | 614 → 614 lignes ; 9 608 → 9 604 mots |
| B01 | 218/218 |

## 3. Écarts déclarés

1. **Rectification de harnais V12-03** (E1-08), ci-dessus.
2. **Version non incrémentée** en G3 (ci-dessus) ; le CHANGELOG porte une section « Non publié ».
3. **Choix délégués** : les trois décisions de `V12_02` §7 ont été prises par l'auteur sur délégation explicite de l'owner.
4. **La branche de session contient désormais le package patché.** La fusionner dans `main` reviendrait à publier la candidate : à ne faire qu'après G4.

## 4. Lecture

- **Certain :** B05 porte V1.2 candidate ; tous les contrôles existants sont verts ; le budget est stable (−4 mots).
- **Hypothétique :** l'effet de A, B, D sur la qualité perçue et sur la palette modale. Rien ne l'établit encore.

## 5. Suite proposée

**Mini-épreuve V1.2 (C3) sur B-DLA**, avant G4 complet et avant tout chantier « budget » :
- 2 rendus C3 (brief vague + V1.2 candidate), même consigne que C4, producteurs neufs ;
- comparaison avec les 6 rendus existants, **même modèle** (condition de réutilisation, protocole §8) ;
- juge : un modèle neuf, avec le **brief riche intégral** (correction de l'écart 3 de `V12_00`), et captures avec défilement ;
- mesures : paires C3/C4 et C3/C1, palette (M2), signalement du contenu d'exemple, lignes lues (M4), tokens.

Coût estimé (probable) : environ 400 000 tokens (2 runs de ~190 000) et un juge (~160 000).
