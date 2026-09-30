# V1.2 refonte — R11 ciblé — Diagnostic (avant correction)

**Date :** 30-09-2026 · **Périmètre :** amendement §7 et plan de reprise §4 (ordre 4).
- Q-04, Q-07, Q-08, Q-09, avec Q-11 et Q-12 maintenus.
- Q-13, puis R-16 à R-32, lus un par un dans leurs traces : `audit/logs/DG_AUDIT_001_Journaux_R02.zip` (`Q_revue.md`) et `DG_AUDIT_001_Epreuves_13-02_traces.zip` (`agents/R.md`).
- Cas négatifs manquants : provenance, `observed` / `not_verified`, protection critique.

**Méthode :** chaque constat d'origine est confronté au texte actuel de la candidate (B05 après R7). Auto-lecture déclarée. Aucun fichier du package n'est modifié par ce diagnostic.

**Dispositions :** *déjà corrigé* (avec preuve), *à corriger* (texte proposé), *maintenu* (justification), *affecté* (à un lot ultérieur).

## 1. Points déjà corrigés par des lots antérieurs (certain)

| Point | Constat d'origine | Preuve actuelle |
|---|---|---|
| Q-05 | L'exemple du QUICKSTART employait `CHANGE` au sens de « correction à faire » | QUICKSTART : champ `CORRECTION` distinct, puis `DECISION-CHANGE: ABANDONED — …` après observation |
| Q-06 | La table de chargement du QUICKSTART omettait les gates en LITE et ITER | La table n'existe plus. Chargement unique `DIRECTION/CHARGE` (R4) ; QUICKSTART y renvoie (garde CHARGE) |
| Q-10 / R-22 | Réserve à six attributs dans le GLOSSAIRE | GLOSSAIRE `CLOSED` : sept attributs, dont « date ou version » |
| R-25a | SKILL : « `STRUCTURED-PROOF` organise les contrats avant build » | Libellé absent de la skill (noyau R4) |
| R-32 | Ancre requise ou absence déclarée ? | Fermé par R7 (`ANC-01`, `V12R_21`) |

## 2. Points à corriger

### 2.1 Bloquants P2

Ces points créent une contradiction sur une règle d'acceptation ou de classement, ou rendent inexacte la promesse du validateur.

**Q-04 — portée du contrôle machine (certain).**
- Le validateur exige `decision_change` à la clôture en ITER et STANDARD. Il exige `trace_locator` en ITER et STANDARD, et un rappel de direction en ITER. Il contrôle les axes et le verdict dans tous les modes.
- `ACTION/CLOSE-PACKAGE` écrit pourtant « Forme seule, dans la trace » pour LITE, ITER et STANDARD.
- La promesse du validateur (`VAL-01`, ACTION) dit : « le paquet de clôture vit dans la trace et la machine ne le vérifie pas ».

| Lieu | Texte proposé |
|---|---|
| CLOSE-PACKAGE, LITE | « Invariants communs de la `RUN_CARD` si elle existe (états, axes, verdict, preuve) ; le reste du paquet vit dans la trace. » |
| CLOSE-PACKAGE, ITER | « Invariants communs ; à la clôture, `decision_change`, `trace_locator` et rappel de direction (`direction.thesis`) ; le reste vit dans la trace. » |
| CLOSE-PACKAGE, STANDARD | « Invariants communs ; à la clôture, `decision_change` et `trace_locator` ; le reste vit dans la trace. » |
| VAL-01 | « pour `LITE`, `ITER` et `STANDARD`, la machine vérifie les invariants communs et les champs de mode nommés dans la colonne « Contrôle machine » d'`ACTION/CLOSE-PACKAGE` ; le reste du paquet vit dans la trace et n'est pas vérifié. » |

**Q-09 — arrêt one-shot et B1b (probable).**
- Le one-shot est décrit trois fois : `ACTION` « Boucle de qualité et branche one-shot » (propriétaire), `ACTION/RUN_CARD` (intention) et `DIRECTION` (one-shot). Aucun de ces textes ne cite B1b.
- Lu à la lettre, « Tu peux t'arrêter après cette observation » permet d'accepter une surface `DIRECTION` avec V positif sans la paire B1b.
- Le noyau est déjà juste : B1b s'applique dans son scope, en trace complète.

Texte proposé, au lieu propriétaire, en fin de paragraphe :

> Sur une surface `DIRECTION` acceptée avec V positif, l'arrêt suppose `ACTION/GATE-B/B1b` fait ou l'un de ses deux motifs `N/A-JUSTIFIED` ; la comparaison peut confirmer la décision initiale (`confirmed`). En trace légère, la proposition reste `EXPLORATORY` et B1b ne s'applique pas.

Les deux autres lieux reçoivent un renvoi court : « (B1b dans son scope, `ACTION/GATE-B/B1b`) ». Les deux exceptions de B1b sont conservées.

**R-16 — protection de niveau : absolue ou conditionnelle ? (probable)**
- `ACTION` (protection critique) dit « Un risque critique exclut `LITE` et `ITER` », sans condition. Le validateur applique la même règle.
- Le propriétaire (`DIRECTION/START`, « Protection de niveau ») est conditionnel : l'exclusion vaut dès que le changement touche le risque, et LITE ou ITER restent possibles pour un delta démontré strictement local et sans effet sur ce risque.
- Conciliation proposée, sans toucher au validateur :

> Un risque critique que le changement touche exclut `LITE` et `ITER` (`DIRECTION/START`, « Protection de niveau ») ; un delta démontré strictement local et sans effet sur ce risque ne le déclare pas comme risque du run.

- **À confirmer par l'owner :** c'est la lecture du propriétaire, mais elle fixe le sens de `risk.level` (risque touché par le run, non risque de la surface).

**R-21 — « Une ancre `transformed` … requise pour l'acceptation » (certain).**
- Le texte d'`ACTION/STATUS` ne limite pas l'exigence à un mode.
- Le validateur ne l'applique qu'en `DIRECTION`, sur chaque ancre, avec le terme `transformation_status: transformed`. Des exemples LITE et STANDARD acceptés n'ont pas d'ancre.

Texte proposé :

> En `DIRECTION`, un verdict accepté exige que chaque ancre soit `transformation_status: transformed`.

### 2.2 Non bloquants, corrigés dans le même lot (coût faible)

| Point | Écart actuel | Texte proposé |
|---|---|---|
| Q-07 (probable) | La ligne « Direction qualifiée » projette `direction.scope` sans le distinguer d'`artifact.scope`. Elle rattache la contrainte à « Qualifier la direction » plutôt qu'au champ `CONSTRAINT` de `DIRECTION/START` | « … contrainte (`CONSTRAINT` de `DIRECTION/START`) ; surfaces couvertes par la direction (facultatif ; distinct d'`artifact.scope`, scope observé de l'artefact) ». Schéma inchangé (décision 3) |
| Q-08 (certain) | « La sortie à conserver de chaque mode est définie une seule fois » ; or `RUN-DIRECTION` (ancrages) et `RUN-SYSTEM` (`closure.system_package`) précisent leur paquet. `PRECONDITION` est un contrat d'entrée, pas une sortie | « Le paquet de sortie de chaque mode est défini par `ACTION/CLOSE-PACKAGE` ; `RUN-DIRECTION` (ancrages) et `RUN-SYSTEM` (`closure.system_package`) en précisent le détail. » |
| R-17 (certain) | B1b : `modified` ; `decision_change` : `CHANGED`, pour la même notion | Schéma inchangé (décision 3). Déclarer la correspondance dans le paragraphe B1b de `RUN_CARD` : « (`modified` correspond à `CHANGED` de `decision_change`) » |
| R-18 (certain) | Les harnais nomment « triade » les trois issues « changée, confirmée ou abandonnée » (E1-10). Pourtant, six lieux appellent « triade » les deux valeurs de repli, et le terme n'est défini nulle part dans le package | Définir le terme une fois dans `ACTION/STATUS` : « changée · confirmée · abandonnée (la triade) ». Ailleurs, remplacer « la triade d'`ACTION/STATUS` s'applique » par « les valeurs de repli d'`ACTION/STATUS` s'appliquent ». Pour `outcome` : « porte la triade et les deux valeurs de repli » |
| R-19 (certain) | Table de correspondance : `decision_change` (`outcome`, `reason`) ; le schéma exige `outcome`, `value` et `evidence` | « `decision_change` (`outcome`, `value`, `evidence` ; `reason` si `N/A-JUSTIFIED`) » |
| R-20 (certain) | DIRECTION écrit « `direction.calibration` : `real_constraint` … » comme une valeur ; c'est un objet `{basis, detail}` | « `direction.calibration.basis` : `real_constraint` … » |
| R-23 (probable) | GLOSSAIRE, exemple `CHANGED` : « la décision … est abandonnée au profit d'un CTA principal unique » | « … est remplacée par un CTA principal unique » |
| R-24 (probable) | Exemple SYSTÈME : `ABANDONED` « jusqu'à correction » avec `ISSUE: RETURNED` (report plutôt qu'abandon) | « `ABANDONED` — l'extension du Select en l'état est abandonnée : la troncature mobile casse le consommateur 2 (observation) ; une version corrigée reprend dans le même mode. » |
| R-26 (certain, résiduel) | `ORCHESTRATION_MAP` charge `BIBLIOTHEQUE/COMPONENTS` sans condition ; `DIRECTION/CHARGE` et la skill disent « si un composant change » | Ajouter « si un composant change » dans `ORCHESTRATION_MAP` |
| R-27 (certain) | QUICKSTART : le lecteur « vérifie le titre exact » ; `READING_MAP` décrit trois étapes | « Le lecteur résout le locator selon `READING_MAP.md` (raccourci, titre propriétaire, puis sous-locator) et n'affiche que le bloc demandé. » |
| R-28 (certain) | Validateur : locators numériques périmés (« DIRECTION 140 », « ACTION 483 », « DIRECTION 672 »). LCF-08 attribue « OWNER et SCOPE jamais omis » à `ACTION/RUN_CARD` au lieu de `DIRECTION/START` | Locators nommés : `DIRECTION/START`, « Protection de niveau » ; `ACTION/PIPELINE-DIRECTION` ; locator de « ITER se souvient ». Libellé LCF-08 : `DIRECTION/START`. Les préfixes des messages restent inchangés : les harnais qui les comparent restent verts |
| R-29 (probable) | « Zéro contrat est valide » face à « `production_contracts` exige au moins un contrat » | « … : aucun fichier `production_contracts` n'est alors produit ; un fichier présent en porte au moins un. » |
| R-30 (probable) | « aucun glissement dans un champ voisin », alors que la même table projette NEXT-ACTION dans deux champs | « … dans un champ voisin **non prévu par cette table** … » |
| R-31 (certain) | SAVOIR : « sinon la direction est traitée d'abord ». START limite cela au cas où le changement partagé découle d'une décision de direction, sauf décisions inséparables | « … si elle découle d'une décision de direction, la direction est traitée d'abord et le run système dépendant ouvert ensuite, sauf décisions inséparables (`DIRECTION/START/TREE`). » |

## 3. Points affectés à un autre lot

| Point | Constat | Lot | Raison |
|---|---|---|---|
| Q-13 (probable) | Le README (« Ces contrôles établissent la cohérence du package… ») et les RELEASE_NOTES font des affirmations de cohérence non bornées | README : **R6b** (fusion des README) ; RELEASE_NOTES : **R12** (réécrites pour V1.2.0) | Texte cible : « Ces contrôles vérifient la forme du package, de ses projections et de ses distributions, et la liste close des conditions de façade ; une divergence hors de cette liste n'est pas détectée. » Non bloquant P2 : ces documents ne sont pas sur le chemin d'un run |
| R-25b (certain) | README : « Le parcours **minimal** est », alors que QUICKSTART parle de parcours **complet** | **R6b** | Réécriture du README dans la fusion |

## 4. Points maintenus

- **Q-11 (maintenu, décidé).** « pas acceptable par simple mention dans la trace » et `ACCEPTED-WITH-RESERVATION` avec réserve structurée ne se contredisent pas : une réserve structurée n'est pas une simple mention. Le validateur interdit `ACCEPTED` avec des droits `unknown`. Aucune preuve nouvelle.
- **Q-12 (maintenu, décidé).** La légende commune ne vaut que pour trois tags partagés ; SAVOIR tient sa table pour les autres. Aucune preuve nouvelle.

## 5. Cas négatifs manquants (certain)

Couverture vérifiée dans trois sources : les 76 cas unitaires de `validate_run_card.py`, les exemples invalides, et les harnais (`B1`, `C2`, `C3`, `C9`, `E1`, `E2`, 13.02).

| # | Règle du validateur | Couverture actuelle | Cas proposé |
|---|---|---|---|
| N1 | `proof.provenance.artifact_locator` = `artifact.locator` | Positif seulement (E1-22 compare les deux dans l'exemple YAML) | Locator de provenance différent → rejet |
| N2 | `proof.observed` et `proof.not_verified` disjoints | Aucune | Même claim dans les deux listes → rejet |
| N3 | `critical_protection.failure_action` ∈ {`RETURNED`, `BLOCKED`, `ESCALATED`} | Aucune valeur invalide testée | `failure_action` = `CONTINUE` → rejet |
| N4 | `critical_protection` : chaque champ requis | `control` placeholder et `result` absent seulement | `owner` absent → rejet ; `evidence_locator` absent → rejet |
| N5 | `proof.provenance` : `method`, `artifact_locator`, `artifact_version`, `observed_at` | Provenance entière absente, version différente, date non ISO | `method` absent → rejet |

**Déjà couverts :**
- protection critique `NOT-VERIFIED` avec `ACCEPTED` (U-*), `FAIL` avec verdict accepté ou issue divergente (B1) ;
- LITE et ITER avec risque critique (B1-01, B1-02) ;
- capacité de provenance indisponible ou non attestée.

**Forme de l'ajout :**
- les cas N1 à N5 entrent dans la liste des cas unitaires de `validate_run_card.py` (même format que U-* et B1-*) ;
- chacun doit être rouge sous la mutation qui retire sa règle, et vert sur la règle actuelle ;
- aucun changement de comportement du validateur (décision 3).

## 6. Gardes prévues

- **Gardes de fidélité** (`validate_structure.py`) :
  - Q-04 : la colonne « Contrôle machine » ne dit plus « Forme seule » pour ITER et STANDARD ;
  - VAL-01 : elle nomme « invariants communs » ;
  - Q-09 : le paragraphe one-shot propriétaire cite `B1b` ;
  - R-16 : la ligne d'ACTION sur la protection critique garde « touche » ;
  - R-21 : elle garde « En `DIRECTION` ».
- **Vocabulaire retiré :**
  - « Forme seule, dans la trace » en ITER et STANDARD ;
  - « la machine ne le vérifie pas » ;
  - « la triade d'`ACTION/STATUS` s'applique » (le terme lui-même reste, défini dans `ACTION/STATUS`) ;
  - « est définie une seule fois, par `ACTION/CLOSE-PACKAGE` » ;
  - locators numériques dans les messages du validateur.
- **Mutations :** chaque correction rougit sous son inverse. N1 à N5 sont rouges quand leur règle est retirée.
- **Suivi complet,** 13.01, 13.02, B01 218/218.

## 7. Estimation

- Environ 20 remplacements de texte, dans :
  - ACTION, DIRECTION, SAVOIR, GLOSSAIRE, ORCHESTRATION_MAP, QUICKSTART ;
  - `references/examples.md` ;
  - `validate_run_card.py` : messages, plus 5 à 6 cas ;
  - `validate_reading_map.py` : libellé LCF-08.
- Noyau à recompiler seulement si un bloc compilé est touché. Aucun n'est prévu.
- Effet attendu sur le chemin prescrit : quelques dizaines de mots.
- **Dépendances vérifiées (certain) :**
  - aucun harnais ne lit « Forme seule », « ne le vérifie pas », « définie une seule fois », « Zéro contrat », l'exclusion LITE/ITER ou les exemples R-23 et R-24 ;
  - « triade » n'apparaît que dans des libellés de harnais, jamais dans un test ;
  - la vérification 13.01 V-2 lit « hors projection … jamais glissé dans un champ voisin » : l'ajout de R-30 vient après et garde la correspondance.
- **Risque résiduel (probable) :** un harnais lit une phrase voisine non repérée. Chaque rouge sera traité par rectification déclarée ou par le maintien du texte ancré.

## 8. Arrêt

- Si R-16 est refusé par l'owner, la ligne d'ACTION reste en l'état et le point est maintenu avec sa limite écrite.
- Si un harnais dépend d'une phrase non modifiable, le point est reporté et déclaré.
