# V1.2 refonte — Unité R5d — BIBLIOTHEQUE alignée

**Date :** 2026-09-27 · **PATCH-DECISION :** `audit/tools/V12R_Patch_R5d.py` (5 entrées ; textes remplacés extraits dans `V12R_Patch_R5d_textes.py`). **Diff :** `audit/diffs/V12R_R5d_bibliotheque.diff`.

## 1. Changements

| Défaut | Changement |
|---|---|
| Boucle structurelle et one-shot en double | Renvois à `DIRECTION/DOUBLE-LOOP` et à la branche one-shot d'`ACTION/PIPELINE-DIRECTION`, qui **gardent les critères propres à la structure** (foyer, rythme, hiérarchie, preuve, comportement, robustesse ; thèse structurelle). **Exemptions BIBLIOTHEQUE retirées** des deux gardes |
| **F22** : tests perceptifs hors chemin | Balisés `PRC-01` dans `BIBLIOTHEQUE/GATE`. Gate C, qui est sur le chemin, les appelle quand la structure est ouverte : non-généricité (« cinquante produits »), silhouette, grille, sur la même capture, pour nourrir C3 et C4. Garde RENVOIS `ACTION/GATE-C → PRC-01` |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 4 erreurs : `PRC-01` absent, renvoi absent, 2 vocabulaires retirés |
| Vert après | `validate_structure` : 19 concepts, 3 renvois ; `validate_reading_map` : vert |
| Mutations | 4/4 rouges |
| Suivi | Vert : 372 cas maintenus, aucune migration ; chemin 12 187 mots ; négations 803 ; doublons 145 → 147 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Écarts et reste à faire

- **Doublons +2.** Les renvois gardent volontairement des critères de structure proches du texte d'ACTION : la consigne de l'owner fait passer le contenu utile avant le compte.
- **F22 atteignable, mais pas compté sur le chemin.** L'outil le déclare hors chemin, car le renvoi est conditionnel (« lorsque la structure est ouverte ») : le périmètre de mesure ne compte que les lectures impératives. Il est désormais **atteignable en un renvoi**.
- **Non traités :**
  - instrumentation de lecture et contrats de promotion en annexe de maintenance ;
  - `PRINT_FIELD` relié aux marqueurs de vague.
  - Ils sont reportés au plan de reprise, sans effet direct sur le rendu.
- **Lecture :**
  - certain : F22 atteignable depuis le chemin ; boucle et one-shot sans copie ;
  - probable : tests « cinquante produits » et silhouette appliqués plus souvent sur une structure ouverte ;
  - hypothétique : l'effet sur le rendu (R10).
