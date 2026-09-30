# V1.2 refonte — Unité « restes R5 » — Répétitions retirées, maintenance hors du parcours ordinaire

**Date :** 30-09-2026.
**Diagnostic :** `V12R_29_R5_RESTES_DIAGNOSTIC.md`, avec les deux retouches de la revue du 30-09 (§8).
**Décision de l'owner :** « Allons-y » ; ligne de signal `PRINT_FIELD` dans le noyau.
**PATCH-DECISION :** `audit/tools/V12R_Patch_R5r.py` : 8 entrées ; BIBLIOTHEQUE remplacée par la sortie de `V12R_Maquette_R5.py` ; `validate_structure.py` remplacé.
**Diff :** `audit/diffs/V12R_R5r_restes.diff` (7 fichiers, 54 insertions, 30 suppressions).

## 1. Changements

- **Copies du handoff remplacées par des renvois** (SAVOIR, BIBLIOTHEQUE) : « ces champs rejoignent le handoff canonique (`ACTION/HANDOFF`) ». Les champs propres de chaque source restent.
- **D-15 : maintenance sortie du parcours ordinaire.**
  - Les catégories de lecture sont retirées du préambule de BIBLIOTHEQUE, qui doublait DIRECTION.
  - Le contrat par périmètre et les statuts de cycle de vie passent dans `BIBLIOTHEQUE/EVOLUTION`, avec une ligne « Mesure de lecture ».
  - Le préambule garde une ligne sur le contrat réduit en run local.
  - Dans DIRECTION, la lecture instrumentée est conditionnelle dès son ouverture et dans sa déclaration : run instrumenté ou audité ; rien en trace légère.
- **`PRINT_FIELD`.** Une ligne s'ajoute aux signaux de convergence du noyau (« Grain, trame d'impression ou texture repris d'un brief à l'autre » : quelle matière sert la thèse, que perd la page si on la retire ?). `PRINT_FIELD` y renvoie : question de jugement, jamais interdiction.
- **Alternative située.** Le déclenchement a un seul lieu, DIRECTION « Direction divergente » (`ALT-01`). L'absolu 3 renvoie. Les leviers sont dans `SAVOIR/CRAFT/CFT-02`. Matérialisation, trace et comparaison sont dans le pipeline d'ACTION (étapes 3 et 7), avec une trace graduée :
  - en trace complète, avant le build ;
  - en trace légère, la première proposition nomme l'alternative écartée.

  « Direction divergente » parle de « sa trace selon le niveau retenu ».
- **Gardes** (`validate_structure.py`) :
  - concept `ALT-01` ;
  - `MNT-01` : ni catégories de lecture ni contrat de promotion avant `BIBLIOTHEQUE/READ` ;
  - trois entrées de vocabulaire retiré : copies du handoff ; « Charges de lecture » et « Déclare dans la trace la nature de chaque lecture » ; copies du déclenchement et « sa trace avant le build » ;
  - quatre résumés fidèles : ouverture et déclaration de la lecture instrumentée, trace graduée de l'alternative, signal `PRINT_FIELD`.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | `ALT-01` absent ; 6 formulations retirées ; 6 résumés infidèles ; 3 alertes MNT-01 |
| Après | structure (25 concepts, 25 vocabulaires retirés, 20 résumés fidèles), carte de lecture, liens et noyau verts ; routes résolues |
| Mutations | **13/13 rouges** : 7 inverses et 6 mutations (copie du handoff, catégories et contrat dans le préambule, signal retiré, trace non graduée, `ALT-01` en double) |
| Suivi complet | vert : 389 cas, 363 maintenus, 26 migrés, **aucune nouvelle migration** ; instantané `V12R_Instantane_suivi_R5r.json` |
| 13.01 | 6/6 et 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |

**Mesures :**

| Mesure | Avant | Après |
|---|---|---|
| Préambule de BIBLIOTHEQUE, lu en premier en STANDARD et en SYSTÈME | 1 066 mots | **804 (−25 %)** |
| Doublons (occurrences) | 145 | **134** |
| Chemin DIRECTION | 12 865 mots | 12 937 (+72 : signal de matière et trace graduée de l'alternative, désormais sur la route chargée) |
| Trace complète | — | 17 670 mots |
| Noyau, section avec son titre (convention du pilotage) | 3 888 mots | **3 923** |
| Noyau, compilation seule | 3 884 mots | 3 919 |
| Outils de fabrication sur le chemin | 24/25 | 24/25 |

## 3. Écarts déclarés

1. **Motif de mutation corrigé en cours d'application.** L'inverse de R5r-A2 rougissait sur la garde « trace de l'alternative graduée », pas sur le vocabulaire retiré. Le motif attendu a été corrigé. Le vocabulaire retiré couvre maintenant les deux variantes recopiées (« comparer cette décision » et « comparer la décision »). Le patch a été réappliqué sur un package propre.
2. **BIBLIOTHEQUE remplacée par la sortie de la maquette** plutôt que par des entrées de texte, à cause des déplacements de sections. Le contenu est celui de `V12R_Maquette_R5.py`, contrôlé par empreinte.
3. **Le chemin DIRECTION grandit de 72 mots.** C'est déclaré et justifié : consigne « qualité avant nombre de mots ».

## 4. Lecture

- **Certain :**
  - la charge de maintenance ne précède plus les routes de BIBLIOTHEQUE ;
  - la déclaration de lecture n'est plus imposée en trace légère ;
  - les copies divergentes du handoff n'existent plus ;
  - l'alternative située a un propriétaire par responsabilité ;
  - **D-15 est fermé.**
- **Probable :** l'agent retrouve plus vite ce qui sert la fabrication, et le signal de matière réduit la trame répétée observée en P1. C'est à observer en R10.
- **Limite :** auto-comparaison.
