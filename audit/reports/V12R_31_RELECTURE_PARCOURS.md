# V1.2 refonte — Relecture de parcours (avant la porte P2)

**Date :** 30-09-2026.
**Cadre :** plan de reprise §4, « Relecture de parcours ». C'est une inspection sans production : on suit ce que le système fait lire et faire, pas à pas. Auto-lecture déclarée.
**Candidate :** `b1f3864` (après les restes R5).

**Parcours suivis :**

| Profil | Chemin lu |
|---|---|
| 1. Agent, brief vague | skill et noyau compilé (lu en entier) → `DIRECTION/CHARGE` → `DIRECTION/EXTERNAL-START` → boucle d'édition → réponse visible |
| 2. Agent, brief riche avec photos | même chemin ; prise de brief « aucune demande » ; ancre venue du projet (`ANC-01`) ; traitement des assets moyens ; texte sur image |
| 3. Humain novice | README du package, section « Commencer » → ce qu'il reçoit → comment poursuivre |
| 4. Expert qui reprend un run | guide opérateur → `ACTION/HANDOFF` → `DIRECTION` « ITER se souvient » → `ACTION/RUN-ITER` → sorties des routes `RUN-*` |

**Contrôles demandés par le plan :**
- retours de la double boucle (défaut local, direction à rouvrir, risque changé, preuve insuffisante, arrêt justifié) : **présents** dans le noyau §7 ;
- observation par interaction quand la capture ne suffit pas : **présente** via Gate C (`RCV-01`, `PRC-01`) ;
- passage d'une proposition exploratoire à une acceptation pour un produit réel (R7) : **trou relevé** (G1).

## 1. Constats

### Bloquants P2 proposés : ils compromettent l'usage ou faussent l'évaluation

**G1 — « Valider » n'a pas de sens défini (certain).**
- `CHK-01` (noyau §8) : « la personne valide, réoriente ou arrête ».
- README, question 4 : « Validez, réorientez ou arrêtez ».
- Aucun texte ne dit ce que « valider » déclenche : continuer à affiner, ou demander l'acceptation ?

Or une acceptation exige la trace complète (`TRA-01`) et, pour un produit réel, une ancre observée ou fournie (`ANC-01`). Un novice peut donc croire que « valider » vaut acceptation, et un agent ne sait pas quand passer en trace complète. C'est exactement le passage « exploratoire → acceptation » que le plan demande de vérifier. Parcours touchés : 2 et 3.

**G2 — Moment des demandes de brief ambigu (certain).**

La prise de brief (`DIRECTION`, bloc BRIEF, dans le noyau) dit :
- « Au plus trois demandes, en un seul échange » ;
- « Humain absent : hypothèses nommées… demandes listées à la livraison », ce qui laisse entendre que, humain présent, les demandes partent **avant** ;
- mais aussi « La personne reçoit directement une proposition principale ».

`CHK-01` ajoute : « une hypothèse nouvelle… ne bloque pas le build ». Le README annonce : « l'agent vous pose au plus trois questions… Il construit la proposition dans tous les cas ».

Deux lectures sont possibles : demander puis construire, ou construire et joindre les demandes. L'effet sur le premier rendu est majeur, puisque les intrants sont le premier levier observé en P1 (12/12). Parcours touchés : 1 et 3. **Décision de l'owner requise.**

**G4 — Sortie en trace légère non dite pour LITE, ITER, STANDARD et SYSTÈME ; reprise impossible depuis une trace légère (certain).**
- `TRA-01` fait de la trace légère le défaut pour tous les runs : une proposition, ni verdict ni clôture.
- Les routes `ACTION/RUN-LITE`, `RUN-ITER`, `RUN-STANDARD` et `RUN-SYSTEM` ne donnent que « Sortie : paquet … d'`ACTION/CLOSE-PACKAGE` » et une clôture `DECIDED` → `CLOSED`. Seule `RUN-DIRECTION` dit qu'en trace légère « la réponse visible et la trace légère en tiennent lieu ».
- « ITER se souvient » et `RUN-ITER` exigent une direction retrouvable « dans la session, la `RUN_CARD` ou le manifeste ». Ils ne citent pas la trace légère, qui ne produit pas de `RUN_CARD`.
- Conséquence : l'expert qui reprend un run né en trace légère (le cas ordinaire) ne sait pas si la ligne « thèse » suffit, et un correctif `LITE` n'a pas de sortie dite. Parcours touché : 4.

### Non bloquants, mais peu coûteux à corriger

| # | Constat | Lieu |
|---|---|---|
| F1 (probable) | « Pour chaque alternative, préciser dans la trace existante » cinq éléments : c'est un reste de la trace non graduée. Il contredit la trace légère (six lignes), que les restes R5 ont posée pour l'alternative | noyau §7 (SAVOIR, bloc BOUCLE-AXE) |
| F2 (probable) | Le checkpoint doit présenter « l'alternative écartée », mais les quatre rubriques de la réponse visible ne la mentionnent pas | noyau §8 (`ACTION/HANDOFF`, sortie) |
| F3 (probable) | Dans `DIRECTION/CHARGE`, la ligne DIRECTION liste `CREATIVE-BOOT` avant `EXTERNAL-START`. Or la prise de brief précède le boot, et `EXTERNAL-START` se place « après START, avant le premier code » | `DIRECTION/CHARGE` (copie compilée dans la skill) |

### Vérifiés sans défaut (certain)
- **Parcours 3** : les quatre questions du README correspondent au noyau (prise de brief, contenu marqué, réponse visible), à G1 près.
- **Parcours 2** : la photo fournie peut servir d'ancre (`ANC-01` : « peut venir du projet lui-même ») ; le traitement des assets moyens, le texte sur image et la question de matière s'articulent. La ligne de signal `PRINT_FIELD` pose une question sans interdire le grain ou la trame que le traitement peut justifier.
- **Parcours 1** : la chaîne `RUN-PRIORITY` (vérité → direction → premier objet → finition), le test de trame, la question de convergence, le contenu d'exemple marqué et le plafond déclaré sont tous dans le noyau.
- **Boucle d'édition** : diagnostics et suites couvrent les cinq retours demandés ; la question 5 impose de réobserver la page entière.

## 2. Textes proposés (lot de raccords « R11b parcours »)

| Point | Lieu | Texte proposé |
|---|---|---|
| G1 | `CHK-01` (ACTION, noyau) | Après « la personne valide, réoriente ou arrête » : « Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce n'est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace complète, avec ancre observée ou fournie, gates et verdict (absolu 2). » |
| G1 | README, question 4 | « Validez pour continuer, réorientez ou arrêtez. Pour retenir cette direction pour votre vrai produit, dites-le : l'agent réunit alors les éléments réels et fait les vérifications nécessaires. » (le bloc est repris par le README Local) |
| G2 (a), recommandé | Prise de brief (DIRECTION, noyau) | « Humain présent : les demandes partent avant le build, en un seul message ; le build suit la réponse, avec des hypothèses nommées pour ce qui manque encore. Humain absent : … » ; « la personne reçoit directement une proposition principale » devient « la réponse est une proposition, pas un compte rendu de cadrage » |
| G2 (b) | Même lieu | « Les demandes accompagnent la première proposition ; le build n'attend pas la réponse. » |
| G4 | `RUN-LITE`, `RUN-ITER`, `RUN-STANDARD`, `RUN-SYSTEM` | Après « Sortie. Paquet … » : « En trace légère (`ACTION/HANDOFF`), la réponse visible et la trace légère en tiennent lieu. » |
| G4 | « ITER se souvient » et `RUN-ITER` | La liste des lieux devient « dans la session, la trace légère (ligne de thèse), la `RUN_CARD` ou le manifeste local » |
| F1 | SAVOIR, bloc BOUCLE-AXE (noyau) | « Pour chaque alternative, préciser en trace complète (en trace légère, la première proposition nomme l'alternative écartée) : » |
| F2 | `ACTION/HANDOFF`, réponse visible (noyau) | « Pourquoi : la thèse, l'alternative écartée et ce que le rendu permet de décider. » |
| F3 | `DIRECTION/CHARGE`, ligne DIRECTION | `DIRECTION/EXTERNAL-START` (si le brief est vague) avant `DIRECTION/CREATIVE-BOOT` |

**Gardes prévues :**
- fidélité : `CHK-01` contient « pas une acceptation » ; chaque « Sortie. Paquet » d'une route `RUN-*` contient « trace légère » ; la prise de brief contient « Humain présent » ; la rubrique « Pourquoi » contient « l'alternative écartée » ;
- ordre de la ligne DIRECTION dans CHARGE (`EXTERNAL-START` avant `CREATIVE-BOOT`) ;
- mutations rouges ; suivi, 13.01, 13.02, B01.

**Effet attendu sur le chemin :** quelques dizaines de mots, dont une partie dans le noyau.

## 3. Décision de l'owner

- **G2** : (a) demander avant de construire quand la personne est présente (recommandé : les intrants sont le premier levier observé), ou (b) construire tout de suite et joindre les demandes.
- **Le reste** : appliquer les textes tels quels.

## 4. Porte P2 : état après cette relecture

| Axe P2 | État |
|---|---|
| Hiérarchie et autorité | Tenu : propriétaires gardés, conflits résolus par renvoi |
| Organisation et accès | Tenu : une entrée agent, une entrée humaine, CHARGE unique, 24/25 outils |
| Cohérence opérationnelle | **Non tenu tant que G1, G2 et G4 restent ouverts** |
| Clarté et charge | Tenu : doublons 134, glossaire à jour ; F1 à F3 sont mineurs |
| Fiabilité | Tenu : suivi vert, 13.01, 13.02, distributions |

**Conclusion (certain) :** après le lot de raccords et la décision G2, les trois bloquants seront fermés. La porte P2 pourra alors être examinée. Les limites restantes, dont l'efficacité réelle et la facilité pour un novice, relèvent de R10 et de l'observation.
