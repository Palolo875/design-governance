# V1.2 refonte — R11c : clôture des routes `RUN-*` en trace complète

**Date :** 30-09-2026 · **Décision de l'owner :** « Allons-y » (application du raccord préparé, `V12R_33` §5).
**Origine :** revue externe de `9cbdcc2`, transmise par l'owner : bloquant PAR-G4b, manqué par l'examen P2.
**Patch :** `audit/tools/V12R_Patch_R11c.py` (+ `_fichiers/`). **Diff :** `audit/diffs/V12R_R11c_cloture.diff`. **Instantané :** `audit/snapshots/V12R_Instantane_suivi_R11c.json`.

## 1. Défaut (certain)

Les rubriques « Clôture » de `RUN-LITE`, `RUN-ITER`, `RUN-STANDARD` et `RUN-SYSTEM` prescrivaient `DECIDED` puis `CLOSED` sans condition, et `ACTION/STATUS` exige alors un verdict. Or `TRA-01` dit qu'une trace légère livre une proposition sans verdict ni clôture. Seule `RUN-DIRECTION` disait « En trace complète ». La règle du noyau était donc contredite par l'instruction locale, sur le chemin d'un run.

## 2. Diff

| Entrée | Lieu | Changement |
|---|---|---|
| R11c-L, -I, -S, -Y | ACTION, rubriques « Clôture » des quatre routes | « Passer à `DECIDED`, puis `CLOSED` » devient « En trace complète, passer à `DECIDED`, puis `CLOSED` ». Les règles de retour et de reclassification sont inchangées |
| R11c-H | CHANGELOG, entrée R11b | « … dit sa sortie en trace légère et ne clôt qu'en trace complète » |
| Garde | `scripts/validate_structure.py` | Fidélité « clôture des routes en trace complète (G4b) » : toute rubrique « Clôture » qui prescrit `DECIDED` contient « En trace complète » |

Aucune modification du noyau compilé (`build_core --check` conforme).

## 3. Résultats

- **Garde :** rouge avant (4 routes), verte après.
- **Mutations :** 5/5 rouges (inverse de chaque entrée, et retrait de la condition dans `RUN-DIRECTION`).
- **Suivi complet :** VERT (389 cas, 363 maintenus, 26 migrés, aucune migration nouvelle ; `validate_all` vert).
- **13.01 :** texte 6/6, non-régression 5/5. **13.02 :** 38/38.
- **B01 :** 218/218.
- **Mesures :**
  - chemin prescrit 13 105 mots (inchangé) ;
  - noyau inchangé.

## 4. Écarts déclarés

- **Doublons 134 → 139.** C'est un amas formel : les cinq phrases de clôture partagent désormais une même tournure, chacune à sa route. Il n'y a ni copie de contenu ni contradiction. Le cliquet reste vert (référence 190).
- **Méthode :** le patch a d'abord été préparé et testé sur une copie, avec le suivi complet. Il a ensuite été appliqué au package après la décision de l'owner.

## 5. Porte P2

- **Contrôles finaux sur le package appliqué :** suivi vert, 13.01 6/6 et 5/5, 13.02 38/38, B01 218/218.
- **Inventaire :** PAR-G4b est fermé. Aucun bloquant P2 ne reste ouvert.
- **Conclusion :** l'axe « cohérence opérationnelle » est tenu sur texte, rubriques « Clôture » comprises. **P2 est conclue** (décision de l'owner du 30-09, confirmée après R11c).
- **Décision distincte, toujours ouverte :** lever la consigne « pas de run » (protocole R10, §9).
