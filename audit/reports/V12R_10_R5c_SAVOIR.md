# V1.2 refonte — Unité R5c (hors ancre) — SAVOIR alignée

**Date :** 2026-09-27 · **PATCH-DECISION :** `audit/tools/V12R_Patch_R5c.py` (5 entrées ; textes remplacés extraits dans `V12R_Patch_R5c_textes.py`). **Diff :** `audit/diffs/V12R_R5c_savoir.diff`.

## 1. Changements

| Défaut | Changement |
|---|---|
| **D-16** : deux modèles à trois niveaux | La triade « visée / construite observée / prouvée » devient **trois moments de la qualité**. Un seul **modèle de niveaux** reste : `Correction`, `Précision`, `Intention` (« Jugement visuel situé »), auquel les trois moments renvoient |
| Boucle en double | « La boucle de jugement est… » devient un renvoi à `DIRECTION/DOUBLE-LOOP`. **Exemption SAVOIR retirée** de la garde « boucle unique » |
| One-shot en double | Renvoi à la branche one-shot d'`ACTION/PIPELINE-DIRECTION`, avec la règle utile gardée : un premier objet faible se corrige ou se retourne |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 3 erreurs de vocabulaire retiré (SAVOIR l.207, 209, 211) |
| Vert après | `validate_structure` : 11 vocabulaires retirés ; `validate_reading_map` : vert |
| Mutations | 3/3 rouges |
| Suivi | Vert : 372 cas maintenus, aucune migration ; **doublons 150 → 145** ; négations 807 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Écarts et reste à faire

- **Reste en attente de décision :**
  - l'ancre, avec ses trois positions à aligner (décision 6) ;
  - les lois de SAVOIR, inchangées (décision 8).
- **Non traités :**
  - « champs de trace sortis vers ACTION » : sa ligne d'ACTION (« Raccord de trace pour `DESIGN-ATLAS` ») existe déjà ; la partie restante demande une lecture dédiée, reportée au plan de reprise ;
  - doublons liés à l'ancre.
- **Exemption provisoire** de la garde « one-shot » pour BIBLIOTHEQUE, à retirer en R5d.
- **Lecture :**
  - certain : un seul modèle de niveaux et deux doublons de moins ;
  - probable : moins d'ambiguïté pour l'agent qui lit SAVOIR ;
  - effet sur le rendu : indirect.
