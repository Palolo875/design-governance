# V1.2 refonte — Unité R11b parcours — Raccords issus de la relecture de parcours

**Date :** 30-09-2026.
**Relecture :** `V12R_31_RELECTURE_PARCOURS.md`.
**Décision de l'owner :** « Allons-y (a) » — G2 : humain présent, les demandes de brief partent avant le build.
**PATCH-DECISION :** `audit/tools/V12R_Patch_R11b.py` (15 entrées ; `validate_structure.py` remplacé).
**Diff :** `audit/diffs/V12R_R11b_parcours.diff` (8 fichiers, 33 insertions, 19 suppressions).

## 1. Changements

- **G1 — Valider n'est pas accepter.**
  - Dans `CHK-01` (noyau) : « Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce n'est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace complète, avec ancre observée ou fournie, gates et verdict. »
  - Dans le README (entrée humaine, reprise par le README Local) : « Validez pour continuer… Pour retenir cette direction pour votre vrai produit, dites-le. »
- **G2 (a) — Humain présent, demander d'abord.**
  - Prise de brief (noyau) : « Humain présent : les demandes partent avant le build, en un seul message ; le build suit la réponse, avec des hypothèses nommées pour ce qui manque encore. »
  - La proposition n'est pas « un compte rendu de cadrage ».
  - README : « l'agent vous pose d'abord… avant de construire ». Le QUICKSTART est aligné.
- **G4 — Trace légère dans toutes les routes ; reprise ITER.**
  - Les routes `RUN-LITE`, `RUN-ITER`, `RUN-STANDARD` et `RUN-SYSTEM` ajoutent « Trace légère : la proposition (`ACTION/HANDOFF`). ».
  - « ITER se souvient » et `RUN-ITER` comptent la trace légère (ligne de thèse) parmi les lieux où retrouver la direction.
- **F1** : la trace de l'alternative est graduée dans le noyau (bloc BOUCLE-AXE de SAVOIR).
- **F2** : la réponse visible nomme l'alternative écartée (rubrique « Pourquoi »).
- **F3** : `EXTERNAL-START` se charge avant `CREATIVE-BOOT` dans `DIRECTION/CHARGE`.
- **Gardes** (`validate_structure.py`) :
  - cinq résumés fidèles : valider n'est pas accepter (noyau, README) ; humain présent ; sortie des quatre routes ; alternative écartée ;
  - trois entrées de vocabulaire retiré : anciennes listes de reprise ITER ; trace de l'alternative non graduée ; ancien ordre dans CHARGE.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 6 formulations retirées et 11 résumés infidèles sur la candidate non patchée |
| Après | structure (28 vocabulaires retirés, 25 résumés fidèles), carte de lecture (LCF-34 incluse), liens et noyau verts |
| Mutations | **12/12 rouges** |
| Suivi complet | vert : 389 cas, 363 maintenus, 26 migrés, **aucune nouvelle migration** ; instantané `V12R_Instantane_suivi_R11b.json` |
| 13.01 | 6/6 et 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |

**Mesures :**

| Mesure | Avant | Après |
|---|---|---|
| Chemin DIRECTION (trace légère) | 12 937 mots | 13 105 |
| Trace complète | — | 17 838 mots |
| Noyau, section avec son titre (convention du pilotage) | 3 923 mots | **4 012** (+89) |
| Noyau, compilation seule | 3 919 mots | 4 008 |
| Doublons (occurrences) | 134 | 134 |
| Outils de fabrication sur le chemin | 24/25 | 24/25 |

## 3. Écarts déclarés

1. **Ancre de mesure rectifiée (déclaré).** `audit/data/V12R/V12R_perimetres.json` citait la ligne DIRECTION de `CHARGE` dans l'ancien ordre. F3 la rendait introuvable, et le suivi a signalé le périmètre comme « périmé ». La citation suit le nouvel ordre, comme en R11a pour F13. Les harnais ne sont pas modifiés.
2. **Libellé des sorties revu deux fois pendant l'application.**
   - La première version (« En trace légère… en tiennent lieu », répétée dans quatre routes) portait les doublons de 134 à 139, contre « une chose, un lieu ».
   - La deuxième (« … en trace complète ») faisait rougir LCF-34, qui exige « Paquet `X` d'`ACTION/CLOSE-PACKAGE`. ».
   - Texte retenu : une phrase courte après ce point, « Trace légère : la proposition (`ACTION/HANDOFF`). » LCF-34 reste verte et les doublons restent à 134.
   - Le patch a été réappliqué chaque fois sur un package propre.
3. **Le noyau grandit de 89 mots** (valider/accepter, humain présent, trace graduée de l'alternative). C'est justifié par la consigne « qualité avant nombre de mots ».
4. **Sans garde propre** : les alignements du README (« d'abord… avant de construire ») et du QUICKSTART. Leurs propriétaires sont gardés.

## 4. Lecture

- **Certain :**
  - le passage « proposition → acceptation » est dit et gardé ;
  - le moment des demandes est fixé ;
  - chaque route dit sa sortie en trace légère ;
  - `ITER` peut reprendre un run ordinaire ;
  - G1, G2 et G4 sont fermés.
- **Probable :** de meilleurs intrants avant le premier rendu quand la personne est présente. C'est l'effet attendu de G2 (a), à observer en R10.
- **Limite :** auto-comparaison.
