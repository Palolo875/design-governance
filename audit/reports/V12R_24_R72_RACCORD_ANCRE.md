# V1.2 refonte — Unité R7-2 — Raccord ancre / FAIL-ASSUMED (erratum de R7)

**Date :** 30-09-2026. **Origine :** revue externe transmise par l'owner, vérifiée dans le dépôt au commit `44cc5b9`. **Décision de l'owner :** « Allons-y ». **PATCH-DECISION :** `audit/tools/V12R_Patch_R72.py` (3 entrées ; `validate_structure.py` remplacé). **Diff :** `audit/diffs/V12R_R72_raccord_ancre.diff` (4 fichiers, 10 insertions, 4 suppressions).

## 1. Constat (certain)

- **Ce que disait DIRECTION.** Deux lieux :
  - `ANC-01`, compilé dans le noyau : « Une diffusion limitée sans l'ancre requise **passe par** `FAIL-ASSUMED` » ;
  - paragraphe final de l'absolu 2 : « une diffusion limitée **reste possible par** `FAIL-ASSUMED` ».
- **Ce que dit `ACTION/OVERRIDE`.** `FAIL-ASSUMED` vaut pour **un échec connu** : `failure_evidence` doit figurer dans `proof.observed`, « jamais un `NOT-VERIFIED` requalifié ». Le validateur l'exige (cas B1-5).
- **La contradiction.** Une ancre absente laisse les axes visuels `NOT-VERIFIED`. C'est précisément le cas que `FAIL-ASSUMED` exclut.
- **Le chemin correct existe déjà.** La direction reste `EXPLORATORY` (issue et verdict). Le validateur accepte des ancres vides dans ce cas (fixture `NO_ANCHOR`).

## 2. Changements

| Lieu | Nouveau texte |
|---|---|
| `ANC-01` (DIRECTION, noyau recompilé, skill à jour) | « Sans l'ancre requise, la direction reste `EXPLORATORY` : elle peut être montrée ou partagée comme proposition, avec sa limite. `FAIL-ASSUMED` (`ACTION/OVERRIDE`) ne vaut que pour un échec connu et observé, jamais pour une ancre absente, qui reste `NOT-VERIFIED` ; le verdict reste non accepté. » |
| Absolu 2, paragraphe final | « … la direction ne peut pas être acceptée ; elle reste `EXPLORATORY` avec sa limite. Une ancre absente n'est pas un échec connu : `FAIL-ASSUMED` ne s'y applique pas (`ACTION/OVERRIDE`). » |
| CHANGELOG, entrée R7 | Alignée |

Hors package :
- erratum ajouté à `V12R_21` ;
- inventaire (D-04), CLAUDE.md et plan de reprise mis à jour.

**Gardes** (`validate_structure.py`) :
- vocabulaire retiré : « passe par `FAIL-ASSUMED` », « reste possible par `FAIL-ASSUMED` », « `FAIL-ASSUMED` ne permet qu'une diffusion limitée » ;
- résumé fidèle : tout paragraphe qui relie une ancre absente à `FAIL-ASSUMED` contient « échec connu ».

## 3. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 4 formulations retirées (DIRECTION ×2, copie compilée dans la skill, CHANGELOG) et 4 résumés infidèles |
| Après patch | gardes vertes (20 vocabulaires retirés, 16 résumés fidèles) ; noyau conforme ; `validate_reading_map` et `validate_run_card` verts |
| Mutations | **4/4 rouges** (3 inverses ; 1 mutation « FAIL-ASSUMED ouvert à l'ancre absente ») |
| 13.01 | texte 6/6 ; non-régression 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |
| Suivi complet | **vert** sur l'arbre stable (second passage) : 389 cas, 369 maintenus verts, 20 migrés, aucune nouvelle migration ; négations 814 ; `validate_all` vert ; instantané `V12R_Instantane_suivi_R72.json` |
| Mesures | chemin prescrit 12 839 → **12 867 mots** ; trace complète 17 600 ; noyau 3 861 → **3 889** (+28 ; section compilée avec son titre, périmètre des rapports précédents — rectifié le 30-09, voir `V12R_26`) ; 24/25 ; doublons 148 |

## 4. Écarts déclarés

- **Garde de fidélité resserrée avant application (certain).**
  - Le premier déclencheur (« ancre » à moins de 200 caractères de `FAIL-ASSUMED`) attrapait une entrée historique du CHANGELOG, qui énumère les champs de la `RUN_CARD`.
  - Déclencheur retenu : « sans ancre » ou « ancre absente / manquante ».
- **Incident de méthode (certain).**
  - Pendant le premier suivi, un `git stash` a retiré les modifications un court instant, pour mesurer le noyau avant patch.
  - Un harnais qui aurait copié le package à ce moment aurait testé la version non patchée.
  - Le suivi a été relancé après coup sur l'arbre stable ; seul le second compte.
- **Pas de changement** du schéma, du validateur ni de `ACTION/OVERRIDE`.

## 5. Lecture

- **Certain.** Le noyau ne présente plus `FAIL-ASSUMED` comme la voie d'une ancre absente. DIRECTION, ACTION et le validateur disent la même chose.
- **Probable.** L'agent qui manque d'ancre livre une proposition `EXPLORATORY` avec sa limite, au lieu de chercher une exception.
- **Limite.** Auto-comparaison. La revue qui a signalé le défaut est externe au dépôt, mais n'est pas un observateur D3 déclaré.

## Rectification (30-09-2026, R7-3)

- **Mesure du noyau.** Le rapport annonçait « 3 861 → 3 885 (+24) », en mêlant deux périmètres : 3 861 inclut le titre de la section, 3 885 ne l'inclut pas. Mesure juste : **+28**, soit 3 857 → 3 885 sans le titre et **3 861 → 3 889** avec le titre (périmètre retenu).
- **Garde de vocabulaire trop large.** Elle refusait aussi une phrase légitime (« une diffusion limitée d'un échec connu … passe par `FAIL-ASSUMED` »). Elle a été bornée au contexte de l'ancre absente par R7-3 (`V12R_26`).
