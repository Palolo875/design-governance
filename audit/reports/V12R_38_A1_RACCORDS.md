# V1.2 refonte — A1 : raccords d'audit sans arbitrage (AUD-03, 04, 09, 10, 14, 15)

**Date :** 30-09-2026 · **Décision de l'owner :** « Allons-y », sur la suite proposée par l'audit (`V12R_37` §6, point 1).
**Patch :** `audit/tools/V12R_Patch_A1.py` (+ `_fichiers/`). **Diff :** `audit/diffs/V12R_A1_raccords.diff`. **Instantané :** `audit/snapshots/V12R_Instantane_suivi_A1.json`.

Chaque raccord aligne un passage sur une règle déjà décidée (`ANC-01`, `TRA-01`, `CNT-01`, lecture de l'agent) ; aucune règle nouvelle.

## 1. Diff

| Constat | Lieu | Changement |
|---|---|---|
| AUD-03 | ACTION, pipeline étape 4 | « Sans ancre utile et spec exploitable… » : le run devient `RETURNED`, `EXPLORATORY` ou `ESCALATED` ; « `FAIL-ASSUMED` ne vaut que pour un échec connu (`ACTION/OVERRIDE`), jamais pour une ancre absente » |
| AUD-03 | DIRECTION, absolu 4 (preuve indisponible) | Même alignement : `FAIL-ASSUMED` seulement pour un échec connu |
| AUD-04 | DIRECTION, mémoire de lancement | Un run `STANDARD`, `DIRECTION` ou `SYSTÈME` persistant, partagé ou audité conserve une trace persistante (trace complète) ; sinon, la trace légère suffit |
| AUD-04 | `ACTION/FAST-PATH` | Clôture LITE en trace complète ; en trace légère, la proposition suffit |
| AUD-04 | BIBLIOTHEQUE (sélection par mode ; test de sortie 8) | « En trace complète, la sélection structurelle est persistée… » |
| AUD-04 | `references/flow.md` | Nœud final « Proposer ou fermer » ; « présenter la proposition (trace légère) ou décider et fermer (trace complète) » |
| AUD-04 | `references/examples.md` | Paragraphe « Niveau de trace » : les exemples en `CLOSED` sont en trace complète ; le brief flou montre la sortie par défaut |
| AUD-09 | DIRECTION, règle CTA (FIRST-OBJECT) | « Une action principale dont la valeur manque reste présente avec une valeur d'exemple marquée (`CNT-01`) : c'est une limite déclarée, pas un retrait » |
| AUD-10 | DIRECTION (constitution, orientation) ; `flow.md` | L'agent lit le noyau et les routes de `CHARGE` ; READING_MAP est la vue d'une personne, ouverte par l'agent si une personne le demande |
| AUD-14 | SAVOIR, marqueurs de vague (noyau) | Signal P1 (Archivo) « non retrouvé en R10 » ; signal R10 : même objet central par brief et même grotesque de titre sur un brief, avec ou sans système |
| AUD-15 | README, entrée humaine, question 3 | Redite retirée ; la mention « retenir pour un vrai produit » reste à la question 4 |
| — | CHANGELOG | Entrée « Raccords d'audit (refonte, audit A1) » |

**Gardes ajoutées** (`scripts/validate_structure.py`) :
- 10 résumés fidèles : AUD-03 ×2, AUD-04 ×5, AUD-09, AUD-10, AUD-14 ;
- 2 vocabulaires retirés (AUD-10) ;
- une règle ENT-01 contre la redite (AUD-15).

## 2. Résultats

- **Gardes :** 16 erreurs avant, 0 après.
- **Mutations :** 14/14 rouges.
- **Suivi complet** (sur copie, puis sur le package) : voir §4.

## 3. Écart déclaré et rectification

**Première version d'AUD-04 pour `examples.md` : suivi rouge.**
- Symptôme : 362 cas maintenus sur 363 ; le cas **R-24** du harnais R était KO.
- Cause (certain) : R-24 rejoue la mutation historique P-32 sur la phrase exacte d'en-tête des exemples. Mon ajout était collé à cette phrase, donc la mutation ne trouvait plus son texte.
- Correction : la note devient un paragraphe distinct (« **Niveau de trace.** »), placé après le paragraphe « Trace, pas sérialisation ».
- Aucun harnais modifié ; suivi vert ensuite.
- Ce défaut a été vu sur copie, avant toute application.

**Doublons 139 → 142 :**
- Un amas nouveau : la règle « `FAIL-ASSUMED` ne vaut que pour un échec connu » est rappelée à l'identique dans ACTION, DIRECTION et le CHANGELOG. Même règle, chacune à sa place ; pas de contradiction.
- Deux amas existants modifiés dans leur texte.

**Mesures :** chemin prescrit 13 153 → 13 238 mots (+85, dont le signal de veille dans le noyau).

## 4. Contrôles finaux

Voir le bloc ajouté après exécution.

## 5. Suites de l'audit : décisions de l'owner

| Constat | Options | Recommandation |
|---|---|---|
| **AUD-01** : quatre prescriptions de chargement | (a) `CHARGE` reste la seule liste. La « Carte de lecture par mode » d'ACTION, les « Déclencheurs critiques » de DIRECTION et `ACTION/ROUTING` deviennent des renvois ; leurs déclencheurs conditionnels passent dans la colonne « Ajouter seulement si » de `CHARGE`. La garde s'étend aux tables par mode. (b) Ajouter à `CHARGE` tout ce que ces tables forcent (`PIPELINE-DIRECTION`, `VISUAL_PROOF`, `CFT-03`, `STATE`, `INTEGRITY`) : chemin plus long | **(a)** : une seule liste, déclencheurs conservés |
| **AUD-02** : obligations SAVOIR hors du chemin | (a) Compiler dans le noyau le plancher manquant, en quelques lignes (palette par rôles et contraste calculé, `CFT-05` ; licence, glyphes et fallback de la police, `TYPE` ; contrôle d'intégrité avant verdict en trace complète). Les autres `[REQUIS]` s'appliquent quand leur route est chargée, ce qui est dit dans SAVOIR/READ. (b) Tout compiler : environ 600 mots | **(a)** |
| **AUD-05** : lieu de la trace légère | (a) À côté de l'artefact quand l'agent écrit des fichiers (fichier de trace ou en-tête du fichier livré) ; sinon après la réponse visible, sous « Trace ». (b) Toujours après la réponse visible | **(a)** : la réponse visible reste sans jargon ; la trace devient observable et reprenable |
| AUD-06, 08, 13 : façades et exemples | Lot « façades » : QUICKSTART (trace légère, checkpoint, noyau) ; un exemple conforme à la trace légère ; exemple déplacé hors du domaine boulangerie ; fusion de la « forme courte LITE » dans la trace légère | Après les décisions ci-dessus |
| AUD-07 : convergence de concept | Étendre la question de convergence à l'objet central (« l'objet que n'importe quel modèle choisirait ici »), sans prescrire d'écart | Effet non mesurable sans run |
