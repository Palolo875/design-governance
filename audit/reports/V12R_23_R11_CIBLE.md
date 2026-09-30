# V1.2 refonte — Unité R11 ciblé — Cohérence ciblée (Q-04 à Q-13, R-16 à R-32, cas négatifs)

**Date :** 30-09-2026 · **Diagnostic :** `V12R_22_R11_DIAGNOSTIC.md`. **Décision de l'owner :** « Allons-y » (30-09-2026) ; lot appliqué tel que proposé, R-16 selon la lecture du propriétaire. **PATCH-DECISION :** `audit/tools/V12R_Patch_R11.py` (35 entrées ; `validate_structure.py` remplacé ; reproductible depuis `f37edaf`). **Diff :** `audit/diffs/V12R_R11_cible.diff` (11 fichiers, 77 insertions, 33 suppressions).

## 1. Changements

**Bloquants P2 (fermés) :**
- **Q-04.** `ACTION/CLOSE-PACKAGE` nomme ce que la machine vérifie en LITE, ITER et STANDARD : invariants communs, puis `decision_change`, `trace_locator` et rappel de direction selon le mode. La promesse du validateur (`VAL-01`) renvoie à cette colonne.
- **Q-09.** La branche one-shot propriétaire (ACTION) relie l'arrêt à B1b sur une surface `DIRECTION` acceptée avec V positif :
  - les deux motifs `N/A-JUSTIFIED` sont conservés ;
  - la comparaison peut confirmer la décision initiale ;
  - en trace légère, B1b ne s'applique pas.

  Les deux autres lieux (ACTION, intention ; DIRECTION, one-shot) y renvoient.
- **R-16.** La protection critique d'ACTION reprend l'exclusion conditionnelle de `DIRECTION/START` : un risque critique que le changement touche exclut LITE et ITER. Un delta démontré strictement local et sans effet sur ce risque ne le déclare pas comme risque du run. `risk.level` décrit donc le risque touché par le run (décision de l'owner).
- **R-21.** L'ancre `transformed` n'est exigée qu'en `DIRECTION`, sur chaque ancre, avec le terme du schéma.

**Non bloquants :**

| Point | Changement |
|---|---|
| Q-07 | Contrainte rattachée au champ `CONSTRAINT` de START ; `direction.scope` distingué d'`artifact.scope` |
| Q-08 | Le paquet de sortie est défini par CLOSE-PACKAGE ; RUN-DIRECTION et RUN-SYSTEM en précisent le détail |
| R-17 | `modified` correspond à `CHANGED` (écrit dans ACTION) |
| R-18 | Triade définie dans `ACTION/STATUS` (changée, confirmée, abandonnée) ; « valeurs de repli » dans six lieux |
| R-19 | `decision_change` projeté selon le schéma (`outcome`, `value`, `evidence`) |
| R-20 | `direction.calibration.basis` |
| R-23, R-24 | Exemples corrigés (GLOSSAIRE, exemple SYSTÈME) |
| R-26 | ORCHESTRATION_MAP : COMPONENTS « si un composant change » |
| R-27 | QUICKSTART : lecteur de routes décrit comme READING_MAP |
| R-28 | Trois locators nommés dans les messages du validateur ; LCF-08 attribuée à `DIRECTION/START` |
| R-29 | « zéro contrat » précisé : aucun fichier `production_contracts` |
| R-30 | « champ voisin non prévu par cette table » |
| R-31 | SAVOIR suit START (direction d'abord seulement si le changement partagé en découle, sauf décisions inséparables) |

**Cas négatifs (réserve 3 de la clôture) :** six cas unitaires dans `validate_run_card.py`.

| Cas | Règle testée |
|---|---|
| N1 | Locator de provenance différent de celui de l'artefact |
| N2 | Même claim dans `observed` et `not_verified` |
| N3 | `failure_action` invalide |
| N4a, N4b | Champ absent dans la protection critique (`owner`, `evidence_locator`) |
| N5 | Champ absent dans la provenance (`method`) |

Cas unitaires : 76 → 82. Comportement du validateur inchangé (décision 3).

**Gardes** (`validate_structure.py`) :
- 6 entrées de vocabulaire retiré (19 au total) ;
- 8 résumés fidèles (15 au total) ;
- nouvelle garde `LOC-01` : aucun locator numérique dans un message de `validate_run_card.py`.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Gardes sur la candidate non patchée | **rouges** : 31 signalements, un par défaut visé |
| Gardes après patch | vertes (24 concepts, 19 vocabulaires retirés, 15 résumés fidèles) |
| Mutations | **41/41 rouges** : 31 inverses, 2 mutations libres, 5 mutations de code (règle retirée → cas N rouge), 3 mutations LCF de migration |
| `validate_run_card` | 82/82 cas unitaires ; 25/25 fixtures |
| `validate_reading_map` | vert (voir écart 1) |
| Noyau | inchangé ; `build_core --check` conforme |
| 13.01 | texte 6/6 ; non-régression 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |
| Suivi complet | **vert** : 389 cas, 369 maintenus verts, 20 migrés (dont 3 en R11) ; cliquets en baisse ; `validate_all` vert ; instantané `V12R_Instantane_suivi_R11.json` |

**Mesures :**

| Mesure | Avant (R7) | Après |
|---|---|---|
| Chemin prescrit (trace légère) | 12 795 mots | 12 839 mots (+44) |
| Trace complète | ≈ 17 350 mots | 17 572 mots |
| Noyau | 3 861 mots | 3 861 mots |
| Outils de fabrication sur le chemin | 24/25 | 24/25 |
| Doublons (occurrences) | 148 | 148 |
| Négations | 808 | 810 |

## 3. Écarts déclarés

0. **Trois cas de harnais migrés (M1, certain).**
   - Au premier suivi, trois cas sont rouges : R R-15, R03 R3-10 et R3-17, tous `MAINTENU-JUSQU-A-REECRITURE`.
   - Chacun vérifiait qu'une condition de façade (LCF-22, LCF-38) rougit quand on inverse une entrée historique (R.01 P-01, R.03 P-40 et P-56). R-18 a réécrit le texte posé par ces entrées (« triade » → « valeurs de repli ») : l'inversion ne trouve plus son texte.
   - Aucune protection n'est perdue : LCF-22 et LCF-38 restent vertes sur la candidate.
   - Traitement selon la méthode de R4 : les trois cas passent `OBSOLETE` dans `V12R_Correspondance_harnais.csv`, avec garde de remplacement `lcf:LCF-22` ou `lcf:LCF-38` et justification.
   - Leur propriété est reprise par trois mutations équivalentes sur le texte courant (`LCF_MUTATIONS` de `V12R_Patch_R11.py`) : on retire `NOT-OBSERVED` de la même ligne, et la condition rougit (3/3).
   - Les harnais ne sont pas modifiés. Suivi : 369 maintenus verts, 20 migrés (17 auparavant).

1. **R-19 reformulé en cours d'application (certain).**
   - Le texte du diagnostic (« `reason` si `N/A-JUSTIFIED` ») faisait rougir LCF-22. Cette condition exige que toute ligne nommant `N/A-JUSTIFIED` près de `DECISION-CHANGE` nomme aussi `NOT-OBSERVED`.
   - La condition est juste : le texte a été corrigé, pas la condition. Texte appliqué : « `reason` exigé si `N/A-JUSTIFIED`, non exigé si `NOT-OBSERVED` » (exact : le validateur ne l'exige que pour `N/A-JUSTIFIED`).
   - Le patch a été réappliqué sur un package propre.
2. **Gardes au niveau de la table (probable, limite).** Les résumés fidèles de Q-07 et R-26 lisent un paragraphe entier, qui est une table. Elles rougissent sous leur inverse, mais une condition ailleurs dans la même table suffirait à les satisfaire.
3. **Sans garde propre (déclaré).**
   - R-18a (définition de la triade) : ajout ; ses emplois fautifs sont gardés.
   - R-28d (libellé de LCF-08) : étiquette d'outil.
   - CHANGELOG.
4. **Affectés à d'autres lots.**
   - Q-13 : README en R6b, RELEASE_NOTES en R12 ; texte cible dans `V12R_22` §3.
   - R-25b (« parcours minimal ») : R6b.
5. **Maintenus.** Q-11 et Q-12 (justification dans `V12R_22` §4).
6. **Locators numériques des libellés de LCF** (`validate_reading_map.py`, colonne des sources, par exemple « DIRECTION 72 »).
   - Hors du périmètre décidé, qui ne visait que les messages du validateur et LCF-08.
   - Signalé, non corrigé. Ce sont des étiquettes d'outil, jamais affichées à un agent pendant un run.

## 4. Lecture

- **Certain.**
  - Les quatre bloquants P2 de ce lot sont fermés, avec leurs gardes.
  - Les règles d'acceptation (B1b, ancre `transformed`, exclusion critique) disent la même chose dans ACTION, DIRECTION et le validateur.
  - Les cinq règles sans cas négatif en ont désormais un.
- **Probable.** L'effet sur un run est faible : aucun bloc du noyau n'est touché. Le gain porte sur la trace complète, l'acceptation et la lecture humaine des contrats.
- **Hors lot.** La promesse du validateur reste une limite de conception (réserve 5) : sa formulation est désormais exacte.
