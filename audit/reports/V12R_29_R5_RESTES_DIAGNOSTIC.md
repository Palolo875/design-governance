# V1.2 refonte — Restes R5 — Diagnostic (avant correction)

**Date :** 30-09-2026.
**Périmètre :**
- amendement du 28-09, §9 ;
- plan de reprise §4, ordre 6 ;
- inventaire : ligne « R5 reste » et **D-15** (bloquant si le parcours ordinaire impose la charge).

**Méthode :**
- relevé ciblé des passages concernés ;
- dépendances vérifiées dans les validateurs et les harnais ;
- **maquette sur copie**, exécutable : `audit/tools/V12R_Maquette_R5.py` ; suivi complet et mesures exécutés sur la copie.

Auto-lecture déclarée. Aucun fichier du package n'est modifié.

## 1. Constats (certain)

| # | Constat | Lieu |
|---|---|---|
| H1 | **Copies du handoff.** SAVOIR (projection des hypothèses) et BIBLIOTHEQUE (sortie de sélection) recopient la liste des champs à transmettre. Chaque copie compte 12 champs, alors que le handoff canonique en a 13 (`DECISION` manque) : les copies ont déjà divergé. Leurs champs propres (nature et confiance, source et coût d'erreur ; décision structurelle, signature, contre-indication) sont utiles et restent | SAVOIR l.189 ; BIBLIOTHEQUE l.39 |
| D15 | **Instrumentation de lecture sur le parcours ordinaire.** La section « Charges de lecture à ne pas confondre » (`STARTUP-NOMINAL`… `AUDIT-READ`) et le « Contrat minimal par périmètre » (pilote, partagé, durable, statuts de cycle de vie) sont dans le préambule de BIBLIOTHEQUE, que « Entrée prioritaire — à lire avant le catalogue » fait lire **en premier** dès que BIBLIOTHEQUE est ouverte. DIRECTION impose aussi « Déclare dans la trace la catégorie de lecture », sans condition, en contradiction avec la trace légère de six lignes (`TRA-01`) | BIBLIOTHEQUE l.43-62 ; DIRECTION « Lecture instrumentée » |
| P1 | **`PRINT_FIELD` isolé.** Aucun lien avec les signaux de convergence, alors que P1 a observé **la même trame sur les rendus (9/9)** | BIBLIOTHEQUE `MODIFIER/PRINT_FIELD` ; signaux (noyau `STRUCT-SIGNAUX`) |
| A1 | **Alternative située décrite trois fois.** Le déclenchement et la matérialisation sont répétés dans DIRECTION (absolu 3 et « Direction divergente ») et dans ACTION (pipeline, étape 3). La trace « avant le build » vit dans DIRECTION, hors des routes chargées, et ne précise pas son niveau de trace. SAVOIR (CFT-02) porte déjà les leviers | DIRECTION l.672, l.765 ; ACTION l.547 |

## 2. Textes proposés (maquette)

Ils sont exécutables dans `V12R_Maquette_R5.py`.

- **H1 : renvoi.**
  - SAVOIR : « Lorsque le run passe à ACTION, ces champs rejoignent le handoff canonique (`ACTION/HANDOFF`) ; en trace complète, ils vont dans la `RUN_CARD` ou la trace équivalente. »
  - BIBLIOTHEQUE : « Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`). »
  - Les champs propres de chaque source restent en place.
- **D15.**
  - La section « Charges de lecture » est retirée de BIBLIOTHEQUE : elle doublait DIRECTION. Une ligne dans `BIBLIOTHEQUE/EVOLUTION` renvoie à DIRECTION pour mesurer un run instrumenté.
  - Le « Contrat minimal par périmètre » et les statuts de cycle de vie passent dans `BIBLIOTHEQUE/EVOLUTION`, avec leur titre, que le harnais C3 retrouve.
  - Le préambule garde une ligne : « En run local, le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` suffit, avec `N/A-JUSTIFIED` si aucune route ne change ; les exigences par périmètre (pilote, partagé, durable) et les statuts relèvent de `BIBLIOTHEQUE/EVOLUTION`. »
  - DIRECTION : « Dans un run instrumenté ou audité, déclare dans la trace la catégorie de lecture applicable (en trace légère, cette déclaration n'est pas demandée). »
- **P1** (dans le noyau) : une ligne de plus dans la table des signaux de convergence.

  > | Grain, trame d'impression ou texture repris d'un brief à l'autre | Quelle matière la thèse de ce produit appelle-t-elle, et que perd la page si on la retire (`MODIFIER/PRINT_FIELD`, test de retrait) ? |

  `PRINT_FIELD` y renvoie : « une question de jugement, jamais une interdiction ».
- **A1 : répartition par propriétaire.**

  | Propriétaire | Rôle | Lieu |
  |---|---|---|
  | DIRECTION | Déclenchement | « Direction divergente », qui garde le seul énoncé ; l'absolu 3 renvoie |
  | SAVOIR | Leviers | CFT-02, inchangé |
  | ACTION | Matérialisation, trace et comparaison | Pipeline, étapes 3 et 7 |

  La trace est **graduée** :
  - en trace complète, la trace du run nomme avant le build la position, l'alternative, son niveau de matérialisation et la preuve attendue ;
  - en trace légère, la première proposition nomme l'alternative écartée (`CHK-01`).

## 3. Coût et effet mesurés (maquette, certain)

| Mesure | Actuel | Maquette |
|---|---|---|
| Suivi complet | vert | **vert, 0 migration** (validateurs non modifiés) |
| Préambule de BIBLIOTHEQUE, lu en premier en STANDARD et en SYSTÈME | 1 066 mots | **804 (−25 %)** |
| Doublons (occurrences) | 145 | **134** |
| Chemin prescrit DIRECTION (trace légère) | 12 865 | 12 937 (+72) |
| Noyau (section) | 3 884 | 3 919 (+35 : ligne de signal `PRINT_FIELD`) |
| Outils sur le chemin | 24/25 | 24/25 |

**Lecture (certain) :**
- La charge **inutile** baisse là où D-15 la plaçait : −262 mots d'instrumentation et de promotion en tête de BIBLIOTHEQUE.
- Le chemin DIRECTION grandit de 72 mots, pour deux raisons utiles :
  - le signal de matière entre dans le noyau (P1 observé) ;
  - la règle de trace de l'alternative arrive dans la route chargée, graduée par niveau de trace. Avant, elle restait hors du chemin.

Conformément à la consigne « qualité avant nombre de mots », ce n'est pas un défaut.

## 4. Gardes prévues

- **Vocabulaire retiré :**
  - les deux copies du handoff (« conserve au minimum `MODE` », « Conservez aussi `MODE` ») ;
  - « Charges de lecture à ne pas confondre » ;
  - « Déclare dans la trace la nature de chaque lecture » ;
  - les copies du déclenchement de l'alternative (ACTION, absolu 3).
- **Préambule de BIBLIOTHEQUE (MNT-01)** : ni catégories de lecture ni contrat par périmètre avant `BIBLIOTHEQUE/READ`.
- **Fidélité :**
  - le paragraphe de lecture instrumentée de DIRECTION contient « run instrumenté ou audité » ;
  - l'étape 3 d'ACTION contient « En trace légère » ;
  - la table des signaux (noyau) contient `MODIFIER/PRINT_FIELD`.
- **Concept `ALT-01`** : le déclenchement de l'alternative située, au seul lieu propriétaire (DIRECTION, « Direction divergente »).
- **Mutations** rouges sous leur inverse. Suivi, 13.01, 13.02, B01.

## 5. Classement P2

- **D-15 : bloquant P2** (certain), car le parcours ordinaire imposait la charge. Il est fermé par ce lot.
- H1, P1 et A1 : non bloquants. Ils sont corrigés dans le même lot, à coût faible.

## 6. Décision de l'owner

Une seule décision : **appliquer la maquette telle quelle** (recommandé). Point à valider en particulier : la ligne de signal `PRINT_FIELD` entre dans le noyau (+35 mots), parce que c'est le défaut observé en P1. L'autre option est de la laisser dans `PRINT_FIELD` seulement, hors du noyau.

## 7. Arrêt

- Si l'application fait rougir des cas de harnais que la maquette n'a pas révélés, ou impose une migration non justifiée, le lot s'arrête au point concerné et l'écart est déclaré.

## 8. Revue du 30-09-2026 (transmise par l'owner, vérifiée) : retouches intégrées à la maquette

- **Validations de la revue.** Sur copie, la revue a exécuté la maquette, recompilé le noyau et relancé `validate_all` ; les mesures annoncées sont confirmées ; les propriétés contrôlées par C3 sont conservées.
- **Retouche 1 (certain).** L'ouverture de « Lecture instrumentée » restait inconditionnelle : « distingue dans la trace : ». Elle devient « …, dans un run instrumenté ou audité, distingue dans la trace : ».
- **Retouche 2 (certain).** « Direction divergente » : « sa trace avant le build » laissait croire que toute trace précède le build. Nouveau texte : « sa trace selon le niveau retenu ». ACTION (étape 3) porte la distinction entre trace complète et trace légère.
- **`PRINT_FIELD`.** La revue recommande aussi l'intégration au noyau.
- **Comptage.** Selon la convention du pilotage (section compilée avec son titre), le noyau passe de 3 888 à 3 923 mots (+35) ; 3 884 → 3 919 est la compilation seule.
- **Contrôles après retouches.** La maquette reste verte (structure, carte de lecture).
