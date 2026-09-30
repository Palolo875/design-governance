# V1.2 refonte — Unité R7-3 — Garde « ancre absente → FAIL-ASSUMED » bornée ; mesure rectifiée

**Date :** 30-09-2026. **Origine :** revue externe transmise par l'owner (vérifiée). **Décision :** « Allons-y ». **PATCH-DECISION :** `audit/tools/V12R_Patch_R73.py`. Seul `validate_structure.py` est remplacé ; aucun texte du package ne change. **Diff :** `audit/diffs/V12R_R73_garde_bornee.diff` (1 fichier).

## 1. Changements

- **Garde bornée.** La garde de vocabulaire de R7-2 refusait toute phrase « passe par `FAIL-ASSUMED` ». Elle ne vise plus que le raccourci « sans ancre » ou « ancre absente / manquante » suivi de « passe par » ou « possible par » `FAIL-ASSUMED`, ainsi que l'ancienne entrée du CHANGELOG.
- **Mesure rectifiée** (`V12R_24`, CLAUDE.md, plan de reprise) :

  | Périmètre | Avant R7-2 | Après R7-2 |
  |---|---|---|
  | Section avec son titre (périmètre des rapports précédents) | 3 861 | **3 889** |
  | Compilation seule | 3 857 | 3 885 |

  Soit **+28 mots** dans les deux périmètres. L'ancien écart annoncé (+24) venait d'un mélange des deux.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | la garde de R7-2 refuse la phrase légitime « Une diffusion limitée d'un échec connu et observé passe par `FAIL-ASSUMED` si les conditions d'`ACTION/OVERRIDE` sont réunies ; le verdict reste non accepté. » |
| Après | les trois anciens raccourcis restent **rouges** (3/3) ; la phrase légitime est **acceptée** |
| Structure et noyau | verts, noyau conforme |
| Suivi complet | vert : 369 maintenus, 20 migrés ; `validate_all` vert ; instantané `V12R_Instantane_suivi_R73.json` |
| 13.01 | 6/6 et 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |

## 3. Écarts déclarés

- **Aucun texte du package modifié.**
- **Limite de la garde** : elle reste lexicale. Une formulation nouvelle qui relie autrement une ancre absente à `FAIL-ASSUMED` serait couverte par la garde de fidélité (« échec connu » exigé), pas par la liste de vocabulaire.
