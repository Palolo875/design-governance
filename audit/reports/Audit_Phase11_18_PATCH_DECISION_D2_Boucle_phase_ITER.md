# DG-AUDIT-001 — Phase 11.18 — PATCH-DECISION D2 : boucle, phase et ITER

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ».

**Grappe D2 : 3 fiches, toutes Significatif. Elle porte le dernier candidat de schéma des lots C et D.**

| Fiche | Objet |
|---|---|
| F-DIR-003 | DIRECTION réunit des données de cadrage, d'observation et de clôture sans les ranger par phase. Risque : un `DECISION-CHANGE` prématuré |
| F-DIR-009 | Le Creative Boot (184) exige « la modification réelle apportée et la ré-observation », alors que DOUBLE-LOOP, ACTION et QUICKSTART autorisent l'arrêt après une première observation suffisante |
| F-DIR-036 | Une RUN_CARD ITER sans direction, trace ni preuve antérieure est acceptée. **Candidat de schéma**, en partie traité en C4 |

**Sorties :**
- cette `PATCH-DECISION` ;
- `D2_harnais_non_regression.py` ;
- 2 lignes ajoutées à la liste close ;
- **une rectification** : le lot E2 porte encore deux candidats de schéma (§5).

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | C1 (triade ; `decision_change.outcome` ; verdict nul avant décision, INV-C1-4 ; « STOP — raison » valide) ; C2 (colonne Phase : avant build / après observation / clôture) ; C3 (réponse visible et handoff) ; C4 (**INV-C4-1 : ITER ⇒ `trace_locator`** ; F-DIR-036 gardait la seule « référence de direction ») ; D1 (contrôle DOUBLE-LOOP : « correction substantielle, sans quota ») |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; contrôles sur copie |
| Sources relues | DIRECTION 25–40 (sortie vers ACTION, trois contrats), 161–187 (Creative Boot), 217–244 (ligne de run, DECISION-INTENT / CHANGE), 482–505 (DOUBLE-LOOP, one-shot), 672–674 (ITER se souvient) ; ACTION 204–218, 349–357 (RUN-ITER), 449–455 (one-shot) ; QUICKSTART 179–190 |

## 2. Re-vérification

**Harnais D2 sur B01 :**
- témoin **1/1** ;
- RUN_CARD **0/6** ;
- gardes **0/4**.

**Contrôles directs sur copie (forme B01) :**

| Cas | B01 |
|---|---|
| ITER sans `direction`, sans `trace_locator` | **acceptée** |
| STANDARD en `state: BUILDING` portant un `decision_change` (le verdict est imposé par B01) | **acceptée** : une conséquence est déclarée avant toute observation |

**Relecture : trois constats.**
1. **La phase est déjà écrite là où c'est important, et manque ailleurs.**
   - DIRECTION 219–234 (ligne de run) sépare déjà les phases : `DECISION-INTENT` au lancement, `DECISION-CHANGE` après observation, `N/A-JUSTIFIED` à la clôture.
   - En revanche, DIRECTION 27 réénumère les treize champs HANDOFF **sans phase**. La ligne `HANDOFF` du tableau des trois contrats (37) mélange ce qui précède le build et ce qui suit l'observation.
   - Depuis C2, la phase de chaque champ est définie **une fois** : colonne Phase de la table de correspondance d'ACTION/RUN_CARD. **Il suffit que DIRECTION y renvoie.**
2. **La machine ne connaît pas la phase.** Rien n'empêche une carte `BUILDING` de porter une conséquence de décision ou un `creative_close`. C'est le risque nommé par la fiche. Il est **déterministe** et **à haut risque** (lignée C1 / F-ACT-014).
3. **Le Boot est la seule forme qui exige toujours une modification.** DOUBLE-LOOP 502, ACTION 453 et QUICKSTART 179–190 autorisent l'arrêt motivé. En 9.06, DOUBLE-LOOP permet l'arrêt pour le pilote B et l'interdit pour A. La discrimination est donc correcte partout, sauf dans le Boot.

## 3. Les sept questions du §21

| Question | F-DIR-003 | F-DIR-009 | F-DIR-036 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : `DECISION-CHANGE` prématuré, impression de preuve complète | **Oui** : itération rituelle sans gain | **Oui** : ITER sans baseline ; non-régression invérifiable |
| Défaut réel ? | Oui (contrôle direct) | Oui (texte, 9.06) | Oui (contrôle direct) |
| Gain > charge ? | Oui : un renvoi, deux étiquettes, un invariant | Oui : une proposition conditionnelle | **Oui, sans nouveau champ** |
| Nouvelle autorité ? | **Non** : la phase vient de C2 ; ACTION 204–218 dit déjà « ne déclare jamais un changement avant qu'une observation ne l'ait rendu réel » | **Non** : alignement sur DOUBLE-LOOP et ACTION | **Non** : RUN-ITER exige déjà « rappeler la direction en une phrase » |
| Testable ? | Machine (D2-01, D2-02, D2-P1) et gardes | Garde et épreuve (tests de la fiche) | Machine (D2-03, D2-P2, D2-P3) |
| Positif / défensif équilibré ? | Oui : `CHECKING` peut porter la conséquence | **Oui, gain positif** : l'arrêt motivé devient une sortie valide du Boot | Oui : LITE inchangé |
| Suppression ou fusion ? | **Clarification** et **alignement** | **Clarification** | **Alignement humain / machine** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

### 4.1 Invariants (liste close D-ACT-1)

| ID | Règle | Schéma | Motif (A2) |
|---|---|---|---|
| **INV-D2-1** | `closure.state` ∈ {`INTAKE`, `CLASSIFIED`, `SPECCED`, `BUILDING`} ⇒ **ni `decision_change` ni `creative_close`**. Ce sont les champs « après observation » de la colonne Phase (C2) | inchangé | « avant observation » |
| **INV-D2-2** | `mode: ITER` ⇒ `direction.thesis` non vide. C'est le rappel de direction exigé par RUN-ITER ; la trace est déjà exigée par INV-C4-1 | **inchangé** (champ existant) | « rappel de direction » |

**Sous-décision F-DIR-036 : aucun nouveau champ.** La fiche demandait une « référence de direction ». Un champ nouveau (`previous_run_ref`, par exemple) ferait double emploi :
- avec `trace_locator`, déjà exigé pour ITER (C4) ;
- avec `direction.thesis`, qui existe déjà et porte exactement la phrase que RUN-ITER demande (« rappeler la direction en une phrase »).

Si la direction est introuvable, DIRECTION 672 prescrit déjà de **reclassifier**. Le message d'INV-D2-2 le rappelle : « ITER exige le rappel de direction (`direction.thesis`) ; sinon reclassifier ».

**Conséquence pour la migration :** le dernier candidat des lots C et D est traité sans changement de schéma. La liste n'est pas encore close : voir la rectification du §5.

**Limites déclarées (forme seule).**
- INV-D2-1 ne couvre que deux champs. `proof.observed` n'est pas contraint, car une capture intermédiaire pendant `BUILDING` est légitime.
- INV-D2-2 vérifie qu'un rappel existe, pas qu'il est **fidèle** à la direction précédente. C'est le rôle de la non-régression ITER, qui reste un jugement.

### 4.2 Corrections de texte

| # | Où | Correction | Fiche |
|---|---|---|---|
| T-1 | **DIRECTION 27** | La réénumération des treize champs est remplacée par : « La sortie de DIRECTION vers ACTION réutilise `ACTION/HANDOFF` ; **la phase de chaque champ (avant build, après observation, clôture) est celle de la table de correspondance d'`ACTION/RUN_CARD`**. » La suite (cible, ancre, `creative_close`, « ne créez ni statut ni verdict ») est conservée | F-DIR-003 |
| T-2 | **DIRECTION 37** (ligne `HANDOFF` des trois contrats) | « **Avant build** : artefact, scope, preuve attendue, limite, prochaine action et owner. **Après observation** : défaut dominant, correction ou retour recommandé. » | F-DIR-003 |
| T-3 | **DIRECTION 184** (Creative Boot) | « Après observation, conserve dans la trace : ce qui est effectivement visible, les qualités prioritaires observées ou non observées, **un défaut dominant** et, **si une correction utile existe**, la modification réelle apportée et la ré-observation attendue ; **sinon, la raison de l'arrêt** (`DIRECTION/DOUBLE-LOOP`, one-shot). » Côté trace : `creative_close.next_polish_action` accepte « STOP — raison » (C1, F-ACT-025) | F-DIR-009 |
| T-4 | **ACTION RUN-ITER, Entrée** (351) | Ajout : « Dans une RUN_CARD, le rappel de direction est porté par `direction.thesis` et la trace par `trace_locator`. » | F-DIR-036 |

**Déjà conforme, sans changement :**
- DIRECTION 219–234 (ligne de run, phases de DECISION-INTENT et DECISION-CHANGE) ;
- DIRECTION 672–674 (reclassement si la direction est absente) ;
- DOUBLE-LOOP 502 (arrêt motivé).

## 5. Liste des changements de schéma : état et rectification

**Rectification.** En 11.09 (C2), j'ai recensé les candidats restants **dans les lots C et D seulement**. En 11.16 (C9), j'ai écrit « seul candidat restant : D2 ». **C'est incomplet.** Relu sur les colonnes TARGET et RECOMMENDATION, le **lot E2** porte deux fiches qui visent un schéma de contrat :
- **F-DF-002** : schéma `domain_frame` 11, nommer les cinq composantes du plan de preuve ;
- **F-RB-002** : schéma `research_brief` 6, 11, 15–17, clarification d'activation et d'oracle.

D3 et D4 n'en portent aucune. Les autres fiches E2 qui citent un fichier machine (F-MAN-001/002, F-VRC-003, F-VRM-002) visent des **outils**, pas des schémas.

**État :**
- les **lots C et D** sont clos pour le schéma avec D2 ;
- la liste des changements de schéma **se fermera après E2**, dans la même migration unique ;
- l'inventaire des invariants et des outils reste ouvert jusqu'à la fin de la phase 11, comme prévu.

**Changements de schéma décidés à ce jour :**

| Schéma | Changements | Grappes |
|---|---|---|
| `run_card.schema.json` | `risk.statement` ; `risk.critical_protection.result` ; `closure.exception` ; `closure.axes` ; `closure.reservations` ; `artifact.version` ; `artifact.rights_status` ; `proof.provenance.capability` ; `capability_profile.basis` typée ; `closure.system_package` ; `closure.b1b` ; `anchors[].type` ; « au moins un ancrage » retiré ; `direction.identity_stake` ; `direction.calibration` ; `decision_change.outcome` et `.reason` ; `closure.verdict` nullable ; `closure.reclassification` ; `profile_decision.phase` | B1–C2 |
| `production_contracts.schema.json` | racine `required` vidée ; `expected_scope` et `observed_scope` ; `proof_status` canonique et `reason` ; `structural_changes` minItems 1 | C2, C3 |
| `domain_frame.schema.json` | `policy_profile.risk_coverage` (+ E2 F-DF-002, à décider) | C9 |
| `research_brief.schema.json` | `source_status`, `source_date`, `source_locator`, `rights_status` (+ E2 F-RB-002, à décider) | C9 |

**Données à migrer :** l'exemple RUN_CARD, les 25 fixtures, les trois exemples de contrats et le YAML de `machine_projection.md` (C6). **Vérifié :** aucune fixture existante n'a un état antérieur à `CHECKING` avec `decision_change` ou `creative_close`, et aucune n'est en mode ITER. INV-D2-1 et INV-D2-2 ne cassent donc aucune fixture.

## 6. Conditions et sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | INV-D2-1 et INV-D2-2 **dans la migration unique** (validateur RUN_CARD), avec leur cas unitaire et leur motif (A2) |
| C2 | **Fixtures** : vérifié (§5), aucune n'est touchée par INV-D2-1 ni INV-D2-2. Deux cas unitaires par invariant, selon A2 |
| C3 | **Passe DIRECTION** (T-1 à T-3) et **passe ACTION** (T-4) avec les passes déjà fixées |

**Sortie (phase 13) :**
1. `D2_harnais_non_regression.py` : témoin **1/1**, RUN_CARD **6/6**, gardes **4/4**. Harnais A1 à D1 verts.
2. **Épreuve de phase** (test de F-DIR-003) : une photo de la carte à chaque état d'un run. Aucun champ « après observation » n'est rempli avant l'observation.
3. **Épreuve de boucle** (test de F-DIR-009) : un run one-shot suffisant ne se voit exiger **aucune modification** ; un run faible voit un **retour exigé**.
4. **Épreuve ITER** (test de F-DIR-036) : un ITER sans référence de direction est refusé ; avec rappel et trace, il est accepté.

## 7. Sortie

- **PATCH-DECISION D2 : CORRIGER.**
  - 2 invariants, **sans champ nouveau** ;
  - 4 corrections de texte ;
  - 1 sous-décision : pas de `previous_run_ref`.
- **Liste close : 90 lignes, 81 actifs.** LCF inchangée : 19.
- **Lots C et D clos pour le schéma** ; rectification : deux candidats en E2 (F-DF-002, F-RB-002).
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Le dernier candidat de schéma des lots C et D se règle **sans champ** : la carte possédait déjà le champ qui porte le rappel de direction.
- Une vérification de clôture a trouvé deux candidats oubliés en E2. Ils sont rectifiés ici plutôt que découverts en phase 12.
- La phase, fixée une fois en C2, devient **exécutable** : une conséquence ne peut plus précéder l'observation.
- Le Boot rejoint la règle anti-rituel : il modifie seulement s'il y a une correction utile à faire.

**Prochaine unité : 11.19 PATCH-DECISION D3** (autorité, droits et gates spécialisés : F-ACT-026, F-ACT-033, F-ACT-037, F-SAV-009).
