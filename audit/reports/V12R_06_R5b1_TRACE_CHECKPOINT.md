# V1.2 refonte — Unité R5b-1 — Trace à deux niveaux, checkpoint, contenu absent, test de trame

**Date :** 2026-09-27 · **Branche :** `claude/init-repo-claude-md-gm6njm` (reportée sur `v1.2/patch-decision-abd`)
**PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R5b1.py` (13 entrées, 2 scripts remplacés, noyau recompilé). **Diff :** `audit/diffs/V12R_R5b1_trace_checkpoint.diff` (8 fichiers, +57 / −16).

## 1. Décisions de l'owner (27-09-2026, par questions groupées)

| Objet | Décision | Défaut traité |
|---|---|---|
| Décision 5 — checkpoint | (a) la première proposition vaut checkpoint, sauf action irréversible ou coûteuse | D-09 |
| Décision 11 — trace | (a) légère par défaut ; complète si le run est persistant, partagé ou audité | D-23 |
| D-20 — destination réelle sans contenu | contenu plausible **marqué comme exemple**, pas d'emplacements vides | D-20 |
| D-22 — trame convergente | **test de trame** dans le noyau, sans rendu supplémentaire | D-22 |

**Découpage de R5b (L) :** R5b-1 applique ces quatre décisions. R5b-2 reste à faire : craft d'ACTION en gestes, Gate A par profil, boucle unique, promesse du validateur.

## 2. Ce qui change pour l'agent

| Lieu propriétaire | Changement | Dans le noyau |
|---|---|---|
| `ACTION/HANDOFF` (concept `TRA-01`) | **Trace légère par défaut**, en six lignes au plus : mode ; thèse ; modal, trame et parti ; plafond et contenus marqués ; défaut dominant ; prochaine preuve. Les planchers s'appliquent toujours (vérité, Gate A, boucle d'édition) ; seule leur écriture s'allège. Le run livre une proposition `EXPLORATORY`, sans verdict, acceptation, clôture ni `RUN_CARD`. **Trace complète** si le run est persistant, partagé ou audité, ou si une acceptation est demandée | §8 |
| `ACTION/PIPELINE-DIRECTION`, étape 7 (`CHK-01`) | **La première proposition vaut checkpoint.** Un checkpoint avant le build n'est requis que sur demande ou pour une action irréversible ou coûteuse. Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition sans bloquer le build | §8 |
| `DIRECTION`, après la prise de brief (`CNT-01`) | **Destination réelle sans contenu** : contenu plausible marqué comme exemple (discret dans l'interface, explicite dans la réponse, avec la liste de ce qu'il faut fournir) | §3 |
| `BIBLIOTHEQUE`, signaux de convergence (`TRM-01`) | **Test de trame** : écrire la trame modale du brief en une ligne, puis la rompre ou la justifier par la tâche ; renommer ne suffit pas | §4 |
| `DIRECTION/CHARGE`, ligne `DIRECTION` | Gate B, `RUN_CARD` et `CLOSE-PACKAGE` ne sont chargés qu'**en trace complète** | §2 |
| ACTION (carte par mode, `RUN-DIRECTION`, `CLOSE-PACKAGE`), DIRECTION §1, SAVOIR (délégation) | Alignements et renvois vers les lieux propriétaires | — |

## 3. Résultats

| Mesure | Après R4 | **Après R5b-1** |
|---|---|---|
| Chemin prescrit d'un run `DIRECTION` (LETTRE, trace légère) | 13 537 mots | **11 740 (−13 %)** |
| Idem en trace complète (COMPLET, nouveau périmètre) | — | 16 351 |
| Outils de fabrication sur le chemin | 24/25 | 24/25 |
| Noyau compilé | 2 843 mots | **3 217** (voir écart 2) |
| Négations ; doublons ; listes distinctes | 813 ; 161 ; 1 | 812 ; 161 ; 1 |

| Contrôle | Résultat |
|---|---|
| Gardes, **rouge avant** (nouveau validateur sur le package non patché, sur copie) | 11 erreurs : 4 concepts absents, 4 vocabulaires retirés, 1 résumé infidèle, bloc `CONTENU` absent, CHG-08 |
| Gardes, vert après | `validate_structure` : 15 concepts, 4 vocabulaires retirés, 2 résumés fidèles, noyau conforme ; `validate_reading_map` : vert, 50 conditions, **aucune rectification** |
| Mutations | **9/9 rouges** : 7 inverses d'entrées ; réintroduction d'un « checkpoint avant le build » ; copie manuelle du noyau |
| Suivi (`V12R_Suivi`) | **Vert** : 372 cas maintenus verts, 17 migrés (inchangé), **aucune migration nouvelle** ; cliquets en baisse ; `validate_all` vert. Instantané : `V12R_Instantane_suivi_R5b1.json` |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 4. Écarts déclarés

1. **R5b découpé** en R5b-1 (décisions) et R5b-2 (restructuration d'ACTION). Le plan l'annonçait comme « à découper ».
2. **Noyau à 3 217 mots**, au-dessus du seuil d'arrêt de R4 (3 000) et de la cible du plan (2 500). Il a gagné quatre blocs (≈ 375 mots), dont trace et checkpoint, qui doivent être lus à chaque run.
   - Ce seuil était celui du lot R4 ; le critère de R5 (chemin ≤ 14 000 mots) est tenu.
   - **Proposition**, à décider par l'owner : compenser en R5a et R5b-2 (D-19, doublons du noyau), avec un plafond de noyau à 3 000 mots suivi comme cliquet.
3. **Outillage d'audit adapté :**
   - le périmètre TABLE/LETTRE suit la ligne `DIRECTION` en trace légère : Gate B et `CLOSE-PACKAGE` en sortent ;
   - le nouveau périmètre COMPLET mesure la trace complète (Gate B, `RUN_CARD`, `CLOSE-PACKAGE`) ;
   - la version R4 est archivée (`V12R_perimetres_R4.json`) ;
   - `V12R_Mesures.py` calcule COMPLET quand la clé existe.
   - Le cliquet `lettre_mots` porte désormais sur le run par défaut.
4. **Carte de lecture d'ACTION alignée sur CHARGE.**
   - Sa ligne `DIRECTION` (« Carte de lecture par mode ») était une liste de chargement partielle que la mesure R1 n'avait pas repérée (en-tête différent).
   - Elle a été alignée pour ne pas contredire la décision 11. Sa fusion dans `DIRECTION/CHARGE` relève de R5b-2 : défaut signalé, non traité ici.
5. **Exemple du test de trame pris hors du domaine de la référence** (SaaS, pas commerce alimentaire). Un exemple pris dans le brief B-DLA aurait contaminé les épreuves qui l'utilisent (R10).
6. **D-19 non traité** (lot R5a). Le bloc `CONTENU` est inséré juste après la phrase concernée, sans la toucher.

## 5. Lecture

- **Certain :**
  - le chemin prescrit par défaut baisse encore de 13 % ;
  - la contradiction « construire dans tous les cas » / « checkpoint avant build » (D-09) est levée, avec un seul lieu propriétaire ;
  - Gate B, `RUN_CARD` et la clôture ne sont plus lus sur un premier rendu ;
  - aucune propriété protégée n'a été perdue (suivi vert, sans migration).
- **Probable :**
  - moins d'appels d'outils par run : pas de paire B1b archivée, pas de gates écrits, pas de `trace.txt` imposé ;
  - des rendus « vrai commerce » lisibles comme des pages ;
  - une trame questionnée au moins en trace.
- **Hypothétique :**
  - que le coût tombe à ≤ 1,3 × C1 (les allers-retours de fabrication restent le poste principal) ;
  - que le test de trame change la structure produite, et pas seulement la trace.
  - **À mesurer en R10**, ou par une mini-épreuve si l'owner la demande.
- **Limite :** auto-comparaison ; aucun run réel observé depuis ce patch.

## 6. Suite

R5b-2 (restructuration d'ACTION), puis R5a (DIRECTION, D-19), R5c (SAVOIR, D-16, décision 6), R5d (BIBLIOTHEQUE, F22), R6 (façades). Décision à prendre : plafond du noyau (écart 2).
