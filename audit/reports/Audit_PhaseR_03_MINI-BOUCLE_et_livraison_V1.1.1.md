# DG-AUDIT-001 — Retour R.03 — Mini-boucle et livraison de V1.1.1

**Date :** 26 septembre 2026.
**Décision de l'owner :** option A de R.02 §5, « R.03 courte ».
**Candidate :** B04 = V1.1.1.
**Références :** B01 est intacte (218/218), B02 reste gelée, B03 est inchangée.
**Statut d'audit :** `AUDIT-RETURN` jusqu'à la réévaluation de l'owner (§6).
**Format :** rapport allégé.

**Fichiers produits :**
- `DG_AUDIT_001_Patch_R03.py` : 22 entrées, P-37 à P-58, dont deux passes (§2) ;
- `R03_harnais_non_regression.py` : 18 cas ;
- `DG_AUDIT_001_B04_R03_diff.diff` : le diff R.02 → R.03 ;
- `DG_AUDIT_001_Instantane_harnais_B04_R03.json` ;
- `DG_AUDIT_001_Journaux_R03.zip`, qui contient les contrôles et la revue `T_revue.md`.

**Système livré :**
- `Design_Governance_V1.1.1_GITHUB.zip` (60 fichiers) ;
- `Design_Governance_V1.1.1_LOCAL.zip` (56 fichiers) ;
- `Design_Governance_V1.1.1.md`, fichier compilé, 60 sections, aller-retour vérifié 60/60 ;
- `DG_AUDIT_001_B04_package_R03_V1.1.1.zip` (sources).

## 1. Périmètre décidé

Les trois constats significatifs de R.02 sont traités, avec les mineurs peu coûteux qui touchent les mêmes textes :

| Point | Correction | Garde |
|---|---|---|
| **Q-01** | Droits inconnus : la machine ne contrôle l'exclusion d'`ACCEPTED` que pour une `RUN_CARD` `DIRECTION`. Dans les autres modes, le contrôle reste à la trace | LCF-36 |
| **Q-02** | Le paquet `SYSTÈME` porte la conséquence décisionnelle ; les cinq paquets sont alignés, ce qui rend le CHANGELOG exact | LCF-37 |
| **Q-03** | SAVOIR l. 30 et l. 879 suivent la triade (`N/A-JUSTIFIED` / `NOT-OBSERVED`), à la clôture | LCF-38 (toutes sources et façades) |
| **Q-05** | QUICKSTART §9 : `CHANGE:` devient `CORRECTION:` ; l'état passe à `CHECKING` ; `DECISION-CHANGE` vaut `ABANDONED`, fondé sur la seule capture observée, et la recomposition reste à réobserver | LCF-42 |
| **Q-06** | QUICKSTART §5 : Gate A applicable et Gate B du risque chargés en LITE et ITER | LCF-39 |
| **Q-10** | Réserve à sept attributs (« date ou version ») dans le GLOSSAIRE et dans `ACTION/CLOSE-EXIT-CHECK` (ligne « Réserves » et question 7) | LCF-40 |
| **O-1** | `null` n'est admis que pour `closure.issue`, `closure.verdict` et `risk.critical_protection`, liste calculée depuis le schéma. Un champ facultatif sans valeur est omis ; un champ requis suit sa règle propre | LCF-41 |
| Versions | CHANGELOG et notes : « 42 conditions de façade » ; droits et `null` mentionnés | — |

La liste close des conditions de façade passe de 35 à **42 conditions**.

## 2. Déroulé : deux passes, une revue chacune

1. **Première passe (P-37 à P-52), commit `422f0e0`, étiquette `R.03-patch`.**
   - Garde rouge avant la correction : 0/14.
   - Écart constaté avant le premier vert : la première version de LCF-38 signalait BIBLIOTHEQUE l. 11, qui renvoie correctement « au contrat ACTION ». J'ai affiné la garde avant le commit ; le texte n'a pas changé.
2. **Revue bornée de ce diff** (sous-agent, même auteur déclaré) : 0 bloquant, 1 significatif, 3 mineurs.
   - T-01 (S) : dans l'exemple §9, une recomposition non observée était présentée comme acquise (`CHANGED`).
   - T-02 : la règle d'omission était trop large, puisqu'elle couvrait aussi les champs requis.
   - T-03 : dans SAVOIR, la triade n'était pas située dans le temps (« à la clôture »).
   - T-04 : ACTION/CLOSE-EXIT-CHECK gardait une réserve à six attributs.

   Tous ces défauts portent sur des textes de R.03 ou de son périmètre.
3. **Seconde passe (P-53 à P-58), commit `f157dca`, étiquette `R.03b-seconde-passe`.** Elle corrige T-01 à T-04 et renforce les gardes LCF-38, 40, 41 et 42. Chaque entrée de la seconde passe a sa propre mutation rouge (R3-15 à R3-18).
4. **Critère d'arrêt appliqué.** La seconde passe (6 lignes de texte) a été vérifiée par moi, mot à mot, et par ses gardes. Il n'y a pas eu de troisième revue par agent, pour ne pas ouvrir une boucle sans fin sur des corrections de corrections. C'est un écart déclaré (§5).

## 3. Contrôles sur B04 final (`f157dca`), sur copies

| Contrôle | Résultat |
|---|---|
| 22 harnais, suivi comparé à l'instantané R.02 | **300/300, témoins 40/40**, aucune alerte |
| Harnais R | **31/31** (sur B03 : 3/31 inchangé) |
| Harnais R03 | **18/18** (sur B04 avant R.03 : 0/18) |
| X (A1) et Y (A2) | Tous rouges pour leur motif |
| 13.01 : texte, mutations, distributions (Python 3.10 et 3.13), non-régression B01 → B04 | 6/6, 6/6, **9/9**, 5/5 |
| 13.02, épreuves déterministes | **38/38** |
| `validate_all` | FULL VALIDATION PASSED (build GitHub et Local, reproductibilité) |
| Zips livrés | Contiennent le texte final (vérifié) ; version 1.1.1 ; membres = manifeste (60 et 56) |

## 4. Bilan du retour (R.01 à R.03)

**Certain :**
- **RET-1 à RET-6** sont verts, chacun avec une preuve rouge sur V1.1.0 (harnais R).
- Les trois constats significatifs de la revue R.02 sont corrigés, avec une preuve rouge avant et verte après (harnais R03).
- **Aucune régression :** 300/300, 38/38, fixtures au même verdict que B01.
- **Aucun changement machine :** schéma, invariants et fixtures sont inchangés ; les cartes valides en V1.1.0 le restent.

**Revues :**
- revue R.02 : 0 bloquant ;
- revue R.03 : 0 bloquant ;
- l'unique significatif de la revue R.03 est corrigé.

**Probable :** les mineurs transmis (ci-dessous) relèvent de la lecture, pas de la règle.

**Transmis sans correction :**
- Q-04 : « forme seule » pour ITER et STANDARD, alors que `decision_change` est contrôlé. La promesse du validateur (ACTION l. 391-392) dit encore que la machine ne vérifie pas le paquet LITE/ITER/STANDARD.
- Q-07 : `SCOPE` a deux projections.
- Q-08 : « une seule fois » n'est pas littéral (ancrages DIRECTION, table PRECONDITION).
- Q-09 : B1b face au one-shot.
- Q-11 : droits face à ACTION l. 500.
- Q-12 : forme du tag partagé.
- Q-13 : autres phrases de cohérence non bornées.
- Mineurs R-16 à R-32 de 13.02.
- `DIRECTION/DAILY` sans gates en LITE/ITER.

**Imitation.** Elle n'est pas rejouée après R.03. Son résultat en R.02 reste 0/2. O-1, qui expliquait l'échec LITE, est désormais écrit ; l'effet n'est pas mesuré.

## 5. Écarts de méthode déclarés

1. **Garde LCF-38 affinée avant son premier vert** (§2, point 1). Motif : un faux positif sur un renvoi correct. Aucun texte n'a été adapté pour faire passer la garde.
2. **Rectification déclarée du harnais R.** Sa mutation inverse d'abord l'entrée R.03 qui a réécrit une partie du texte posé par R.01 (LCF-32 via P-37, LCF-35 via P-45), puis l'entrée R.01. Motif : des patchs empilés rendaient l'inversion directe impossible. Le résultat sur B03 est inchangé (3/31).
3. **Seconde passe sans troisième revue par agent** (§2, point 4).
4. **Dépendances d'outils.** `DG_AUDIT_001_Patch_R03.py` et `R03_harnais_non_regression.py` importent le patch R.01 et le harnais R. Les quatre fichiers vont ensemble.

## 6. Réévaluation du statut (décision de l'owner)

**Conditions de sortie du retour (phase 14 §5) :**
- RET-1 à RET-6 verts, chacun avec une preuve rouge sur V1.1.0 : **tenu** ;
- aucune régression : **tenu** ;
- revue bornée sans contradiction bloquante : **tenu**, en R.02 comme en R.03.

**Proposition : `AUDIT-PASS-WITH-RESERVATION`**, avec les réserves suivantes :

| # | Réserve | Qui peut la lever |
|---|---|---|
| 1 | **Efficacité sur des runs réels : `NOT-VERIFIED`** (aucun observateur indépendant ; mesure M non concluante ; imitation 0/2) | Owner : pilotes avec un observateur répondant aux critères D3 |
| 2 | Run CI hébergé du workflow épinglé non observé | Owner : push de la distribution GitHub |
| 3 | Environ 14 invariants existants sans cas négatif | Owner |
| 4 | Seize limites déclarées : une garde prouve une forme, pas un effet | Pilotes |
| 5 | Promesse du validateur : ce que la machine n'atteste pas | Permanente, déclarée |
| 6 | F-DIR-044 et coût d'un run (environ 1 300 lignes de règles pour un run DIRECTION) | Mesure sur pilotes |
| 7 | Placeholders acceptés dans les champs libres des contrats | Décision éventuelle |
| 8 | Mineurs transmis (§4) | Prochaine version |
| 9 | V1.1.1 non publiée | Owner |

Il n'y a pas de verdict global d'efficacité. Le statut porte sur la conformité du système à ses propres contrats et sur la tenue du protocole d'audit, pas sur la qualité des designs produits.

**Prochaine unité :** la clôture finale. Si l'owner retient ce statut, elle met à jour le dossier de clôture de la phase 14 (statut, réserves, pointeurs vers V1.1.1).
