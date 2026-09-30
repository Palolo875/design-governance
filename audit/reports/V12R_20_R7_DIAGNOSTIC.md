# V1.2 refonte — R7 — Diagnostic de l'ancre (avant correction)

**Date :** 30-09-2026 · **Décision à appliquer :** décision 6 (a), ancre graduée (`V12R_14`), précisée par l'amendement du 28-09 §6.
- Une première proposition peut commencer sans ancre, avec une limite déclarée et le statut `EXPLORATORY`.
- L'**acceptation** d'une direction destinée à un produit réel exige une ancre observée ou fournie, pertinente et inspectée.
- Une ancre peut venir du projet lui-même.
- Répartition des rôles : DIRECTION porte la règle, SAVOIR son exploitation, ACTION les observations et la conséquence sur l'acceptation.

**Méthode :** relevé de toutes les mentions d'ancre (DIRECTION 32, ACTION 25, SAVOIR 16, façades 8, skill 0 règle). Auto-lecture déclarée. Défauts visés : D-03 et D-04 (inventaire, bloquants P2).

## 1. Formulations actuelles et écarts à la décision

| # | Lieu | Formulation actuelle | Écart |
|---|---|---|---|
| A1 | DIRECTION, absolu 2 (titre) | « Ne dessine jamais une surface identitaire uniquement de mémoire. » | **Contradiction** : interdit l'exploration sans ancre que la décision autorise |
| A2 | DIRECTION, absolu 2 | « **Avant le premier code ou le premier rendu** d'une surface `DIRECTION`, établis une ancre fraîche et inspectable par l'une des voies suivantes » (générée, observée, fournie) | **Double écart** : moment (avant le rendu au lieu d'avant l'acceptation) et type (une ancre générée suffit, alors que l'acceptation pour un produit réel demande observée ou fournie) |
| A3 | DIRECTION, absolu 2 (fin) | « Sans ancre fraîche et utile… bloque la livraison validée, sauf `FAIL-ASSUMED` » | Compatible sur le moment ; ne distingue pas la destination |
| A4 | DIRECTION, déclencheurs critiques | « Ancre absente pour une surface identitaire → retour à l'ancrage [FORCÉ] » | **Contradiction** : force un retour là où l'exploration est permise |
| A5 | DIRECTION, récapitulatif de protection | « son ancrage doit être observable ou explicitement limité » | Presque aligné ; à préciser (limite en exploration, ancre avant l'acceptation) |
| A6 | SAVOIR/SOURCE | « Pour une surface identitaire, l'ancre est requise (voir ABSOLU 2) » | **Position 1 de D-04** (requise, sans moment) |
| A7 | SAVOIR/TOOLS | Sourcing Web « recommandé… requis seulement si le contrat dépend d'un claim… » | **Position 2 de D-04** ; porte sur le sourcing Web, compatible une fois le lien fait |
| A8 | SAVOIR, test de sortie (item 6) | « l'ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée) » | **Position 3 de D-04** ; juste en exploration, muette sur l'acceptation |
| A9 | ACTION/PIPELINE-DIRECTION, étape 4 | « Sans ancre utile et spec exploitable… `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` » | Compatible (issue graduée) |
| A10 | ACTION, précondition `DIRECTION` | « ancre utile » dans la liste | Compatible si l'on lit « utile » selon le moment |
| A11 | QUICKSTART | « ancre fraîche et inspectable » (absolus) | Reprend A2 : **à aligner** |
| A12 | READING_MAP, README officiel | « ancre inspectable » | **D-03** : résumé infidèle, sans moment ni destination |
| A13 | Skill et noyau | Aucune règle d'ancre (hors table `VISUAL_TARGET`, chargée via `CHARGE`) | L'agent ne lit pas l'absolu 2 pendant la fabrication. **À ajouter** : une phrase compilée |
| A14 | Validateur `RUN_CARD` (inchangé, décision 3) | DIRECTION acceptée sans ancre refusée ; enjeu `high` avec ancres générées seules : `real_constraint` ou `generated_only_reserved` (ce dernier interdit `ACCEPTED`) | **Limite à déclarer** : la machine ne connaît pas la destination « produit réel » ; elle raisonne sur `identity_stake`. L'exigence « observée ou fournie » pour un produit réel relève de la revue d'acceptation |

## 2. Textes proposés

**Lieu propriétaire : DIRECTION, absolu 2** (concept `ANC-01`, compilé dans le noyau §6).

> ### [ABSOLU 2 — ANCRAGE OBSERVABLE] Ne fais jamais accepter une direction identitaire calibrée uniquement de mémoire.
>
> Une première proposition peut commencer sans ancre : elle déclare cette limite et reste `EXPLORATORY`. Pour explorer, une hypothèse générée (`ANCHOR-GENERATED`) aide à comparer. L'**acceptation** d'une direction destinée à un produit réel exige une ancre observée ou fournie (`ANCHOR-OBSERVED`, `ANCHOR-PROVIDED`), pertinente, inspectée et datée, avec les autres preuves applicables. L'ancre peut venir du projet lui-même : identité existante, produit, photographies, interface actuelle. Pour une démonstration ou un modèle, une hypothèse générée ou une absence déclarée suffit, avec sa limite.

La table des trois voies et les paragraphes suivants de l'absolu sont conservés. Le paragraphe final devient :

> Sans ancre observée ou fournie, les axes visuels concernés restent `NOT-VERIFIED` ; pour une direction destinée à un produit réel, cela bloque l'acceptation, sauf `FAIL-ASSUMED` journalisé selon `ACTION`. Le validateur de `RUN_CARD` ne connaît pas la destination : cette exigence relève de la revue d'acceptation.

**Renvois alignés (sans second énoncé de la règle) :**

| Lieu | Nouveau texte |
|---|---|
| DIRECTION, déclencheurs critiques (A4) | « Acceptation visée pour un produit réel sans ancre observée ou fournie → obtenir l'ancre, ou garder le run `EXPLORATORY` avec sa limite (`[FORCÉ]`) » |
| DIRECTION, récapitulatif (A5) | « …son ancrage est déclaré comme limite en exploration, et observé ou fourni avant l'acceptation pour un produit réel… » |
| SAVOIR/SOURCE (A6) | « L'exigence suit l'absolu 2 de DIRECTION : exploration possible sans ancre, limite déclarée ; acceptation pour un produit réel avec une ancre observée ou fournie. » |
| SAVOIR, test de sortie (A8) | « …(utile, ou absence déclarée en exploration ; observée ou fournie avant l'acceptation pour un produit réel, absolu 2) » |
| QUICKSTART, READING_MAP, README officiel (A11, A12) | « ancre observée ou fournie avant d'accepter une direction pour un produit réel » |

A7, A9 et A10 restent en l'état, car ils sont compatibles.

## 3. Gardes prévues

- **`ANC-01`** : concept au lieu propriétaire.
- **Vocabulaire retiré :**
  - « ancre fraîche et inspectable » ;
  - « Avant le premier code ou le premier rendu… établis une ancre » ;
  - « Ne dessine jamais une surface identitaire uniquement de mémoire ».
- **Fidélité** : tout paragraphe qui cite l'absolu 2 garde « produit réel ».
- **Mutations** : chaque correction rougit sous son inverse.
- **Aucun changement** du validateur ni du schéma (décision 3).

## Rectifications (30-09-2026, avant application)

La vérification de l'owner a corrigé quatre points ; le texte appliqué est celui de `V12R_21` §1 et §2.

- **FAIL-ASSUMED** est une diffusion limitée non acceptée, pas une exception d'acceptation.
- **« Absence déclarée »** vaut pour explorer seulement.
- **A4** est une clarification (le texte offrait déjà une issue graduée), pas une interdiction nette d'explorer.
- **La garde de fidélité « produit réel »** est abandonnée : un renvoi suffit.

**Omission constatée à l'application :** le README Local généré par `build_distributions.sh` portait aussi « ancre inspectable ».
