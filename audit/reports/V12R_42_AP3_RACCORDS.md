# V1.2 — AP3 : raccords de procédure et de fabrication (C08, C05, C06, C07, C09, C10, D-26)

**Date :** 01-10-2026.
**Décisions de l'owner :**
- « (a), allons-y pour AP3 » : D-26 option (a), une clause dans `CNT-01` ;
- textes soumis avant application, comme convenu en `V12R_41` §7, puis « Allons-y » (01-10-2026) : appliqués tels quels.

**Pièces :**
- patch : `audit/tools/V12R_Patch_AP3.py` (+ `_fichiers/scripts/validate_structure.py`) ;
- diff : `audit/diffs/V12R_AP3_raccords.diff` ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP3.json`.

## 1. Vérifications préalables (certain)

- **C08, nuance.** La route `ACTION/FIRST-RENDER` porte la mention « `ACTION/UI-UX-REALITY` : servi séparément ». Aucun déclencheur ne l'appelle avant fabrication : ni `CHARGE` (STANDARD, DIRECTION), ni le noyau, ni `RUN-STANDARD`. En trace complète, `CLOSE-PACKAGE` la cite déjà dans ses paquets. Le défaut porte donc sur le moment : absence de déclencheur **avant fabrication**.
- **C05.** RUN-DIRECTION dit « `CLOSED` uniquement si la direction est tenue ». `ACTION/STATUS` dit au contraire que `CLOSED` décrit la persistance et peut coexister avec `RETURNED`. Le texte est hérité de V1.1.1.
- **C06.** Le FAST-PATH envoie les petits `ITER` vers la forme courte LITE (hérité). C'est le seul lieu concerné.
- **C07.** Le bloc compilé de l'atelier d'édition ne dit ni la portée de B1b ni ses deux exceptions. Garder l'original y figure déjà.
- **C09, neuf lieux relus :**
  - **4 défauts** : SAVOIR, ligne du niveau « requis par le module » ; SAVOIR, recherche sans effet ; SAVOIR, module sans effet ; QUICKSTART, liste « Avant de fermer ». Dans ces lieux, `N/A-JUSTIFIED` peut masquer une preuve manquante ou une confirmation, et `NOT-OBSERVED` y est appliqué à une preuve.
  - **5 vrais N/A, maintenus sans changement** : BIBLIOTHEQUE l. 27 (zéro route), l. 43 et l. 762 (aucune route ne change), l. 172 (pas d'objet de rythme) ; DIRECTION l. 393 (culture visuelle sans référence, conservée comme le demande la disposition de l'audit).
- **C10.** La règle d'or 8 (« si un risque reste… ») exclut la réserve structurée que `ACTION/STATUS` admet.
- **D-26.** `CNT-01` couvre la destination réelle sans contenu, mais pas les fonctions affirmées d'un produit fictif.

## 2. Textes (avant → après)

| Id | Lieu | Après |
|---|---|---|
| C08a, C08b | `CHARGE`, colonne « Charger d'abord », lignes STANDARD et DIRECTION (compilées dans le noyau) | « `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée », après `RUN-STANDARD` et après `FIRST-RENDER`. La ligne LITE reste sans déclencheur |
| C08c, C08d | Carte d'ACTION (vue de `CHARGE`), lignes STANDARD et DIRECTION | Même ajout, pour que la vue reste fidèle |
| C05 | RUN-DIRECTION, Clôture | « En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque l'artefact et la trace sont persistés : `CLOSED` ne dit pas que la direction est tenue (`ACTION/STATUS`). Le résultat se déclare à part : une direction tenue, preuves applicables déclarées, peut recevoir un verdict accepté ; sinon, l'issue est `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` (échec connu) ou `ESCALATED`, avec le verdict `RETURN-DIRECTION` si la direction doit être reprise, selon la preuve et le risque. » |
| C06 | FAST-PATH | « …puis, en trace complète, clôture avec le paquet de son mode : forme courte LITE pour `LITE`, paquet `ITER` pour un `ITER` (`ACTION/CLOSE-PACKAGE`) ; en trace légère, la proposition suffit. » |
| C07 | Tête du bloc compilé de l'atelier (ACTION/B1b) | « Dans le scope de B1b (surface `DIRECTION` qui accepte avec l'axe V positif, en trace complète : `ACTION/B1b`), cet atelier est requis, sauf deux motifs `N/A-JUSTIFIED` : aucune décision principale éditable, ou une paire équivalente encore valide qui couvre la même décision. Hors de ce scope, il ne s'impose pas. » |
| C09a | SAVOIR, niveau requis | « Exécuter dans le scope ; sinon déclarer `NOT-VERIFIED` (preuve manquante), ou `N/A-JUSTIFIED` avec sa raison si l'obligation ne s'applique pas. » |
| C09b | SAVOIR, recherche | « Lorsque la recherche ne peut modifier aucune décision, déclare `N/A-JUSTIFIED`… ; une recherche faite qui confirme la décision est une confirmation (`ACTION/STATUS`), pas un `N/A-JUSTIFIED`. » |
| C09c | SAVOIR, module sans effet | « …arrête ou simplifie. Une décision que le module a confirmée se déclare comme confirmation ; `N/A-JUSTIFIED` reste réservé au module qui ne pouvait rien changer. » |
| C09d | QUICKSTART, avant de fermer | « 2. la preuve attendue est obtenue ou déclarée `NOT-VERIFIED` ; une conséquence attendue non observée est `NOT-OBSERVED` ; `N/A-JUSTIFIED`, avec sa raison, ne vaut que si la preuve ne s'applique pas ; » |
| C10 | SAVOIR, règle d'or 8 | « 8. Si un risque bloquant reste, retourne, passe en `EXPLORATORY` ou journalise un `FAIL-ASSUMED` autorisé (échec connu) ; un risque non bloquant peut rester en réserve structurée (`ACCEPTED-WITH-RESERVATION`, `ACTION/STATUS`) ; ne compense jamais un axe bloquant par une moyenne. » |
| D-26 | `CNT-01` (noyau) | Ajout : « Pour un produit fictif ou non encore construit, les fonctions, intégrations et conformités affirmées sont aussi des contenus d'exemple, marqués comme le nom et le prix. » |
| H | CHANGELOG | Entrée « Raccords de procédure et de fabrication (audit progressif, unité 3) » |

## 3. Gardes (`validate_structure.py`)

- **UIX-01** (nouvelle) : dans `CHARGE` et dans le noyau compilé, les lignes STANDARD et DIRECTION appellent `UI-UX-REALITY` ; la ligne LITE ne l'appelle pas.
- **Vocabulaire retiré** (C05) : « `CLOSED` uniquement si la direction est tenue ».
- **8 résumés fidèles** : C05, C06, C09 ×4, C10, D-26.
- **CORE-01 étendue** : portée de l'atelier, déclencheur UI/UX, fonctions d'un produit fictif.
- **Garde AUD-04 du FAST-PATH** : son déclencheur suit le nouveau texte, la propriété « en trace complète » est conservée.

## 4. Résultats sur copie

- **Gardes :** rouges avant (16 erreurs, dont 4 UIX-01), vertes après.
- **Mutations :** 14/14 rouges : 11 inversions, LITE avec déclencheur, déclencheur retiré de la ligne compilée, résultat sans renvoi à STATUS.
- **Suivi (rectifié en AP2) :** VERT. 389 cas, aucune migration, doublons 142 (inchangé), `validate_all` vert.
- **Mesures :** chemin prescrit 13 614 → 13 774 mots (+160) ; noyau 4 444 → 4 541 mots (+97).

## 5. Écarts, limites et points à valider

- **Corrections de méthode faites pendant la préparation.**
  - Première garde C09 trop large : elle visait aussi le paragraphe « Chemin minimal » de SAVOIR, qui est correct. Elle a été restreinte à la ligne du tableau.
  - Une mutation de la section compilée restait verte, car le déclencheur subsistait sur la ligne STANDARD. UIX-01 contrôle désormais ligne par ligne.
- **C07, conséquence connue.** « Hors de ce scope, il ne s'impose pas » reprend la règle d'ACTION/B1b. Cela peut réduire l'usage de l'atelier dans les runs qui ne visent pas une acceptation DIRECTION. L'étendre ailleurs reste un arbitrage distinct, non proposé.
- **C08, placement.** Le déclencheur est placé dans « Charger d'abord », avec sa condition, sur le modèle de `EXTERNAL-START` (« si le brief est vague »). Il ne va pas dans « Ajouter seulement si », car c'est un contrat requis quand la condition est vraie, pas une option.
- **Effet sur les rendus :** non observable sans run (R10 arrêté).

## 6. Application et contrôles finaux, sur le package

- **Application :** 14 entrées, textes identiques à ceux du §2 ; noyau recompilé, conforme à sa compilation.
- **Gardes :** vertes. **Mutations :** 14/14 rouges.
- **Suivi (rectifié en AP2) :** VERT. 389 cas, 363 maintenus, 26 obsolètes avec gardes établies, aucune migration ; `validate_all` vert.
- **Cliquets :** chemin 13 774 mots, négations 817, doublons 142, une liste de chargement.
- **13.01, par sous-contrôle :**
  - texte 6/6 ;
  - mutations 6/6 ;
  - non-régression 5/5 ;
  - distributions 9/9 (Linux, Python 3.10 et 3.13, archives construites depuis une copie ; pas de CI hébergée).
- **13.02 :** 38/38. **Sonde AP1 (C01, C02) :** verte. **B01 :** 218/218.
- **Effet sur les rendus :** non observé (R10 arrêté).

