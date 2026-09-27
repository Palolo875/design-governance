# V1.2 refonte — Unité R6a — Façades (partie sûre)

**Date :** 2026-09-27 · **PATCH-DECISION :** `audit/tools/V12R_Patch_R6a.py` (3 entrées). **Diff :** `audit/diffs/V12R_R6a_facades.diff`.

## 1. Changements

- **README (racine) :** la séquence « Observer → isoler… » devient un renvoi à la boucle d'édition (`DIRECTION/DOUBLE-LOOP`, noyau). **Dernière exemption levée :** la garde « boucle unique » n'admet plus que DIRECTION (propriétaire), la skill (copie compilée) et CHANGELOG (historique).
- **GLOSSAIRE :** cinq termes de la refonte ajoutés et gardés (`GLOSSARY_TERMS`, 16 termes) : trace légère, trace complète, première proposition, trame modale, profil de surface.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 6 erreurs : 1 vocabulaire retiré, 5 termes absents |
| Vert après | `validate_structure` ; `validate_reading_map` |
| Mutations | 2/2 rouges |
| Suivi | Vert : 372 cas maintenus, aucune migration ; doublons 147 → 144 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Reste (R6b, plan de reprise)

- **Fusion des deux README.** `validate_design_governance.py` exige « la `RUN_CARD` rassemble » dans le README officiel, et des LCF lisent les deux fichiers : une rectification déclarée est à prévoir.
- **QUICKSTART humain :** une activation et un chemin.
- **READING_MAP** réduit au chemin et à l'index ; **ORCHESTRATION_MAP** fondu si les harnais le permettent.
