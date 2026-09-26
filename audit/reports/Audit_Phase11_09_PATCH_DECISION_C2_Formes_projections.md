# DG-AUDIT-001 — Phase 11.09 — PATCH-DECISION C2 : formes et projections

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.09 ».

**Grappe C2 : 14 fiches, toutes Significatif, plus un transfert.**

| Sous-groupe | Fiches | Objet |
|---|---|---|
| **P. Projection** | F-ACT-002, F-DIR-006, F-DIR-039, F-ACT-028, + **F-ACT-017 (1)** transférée de B1 | Ce que la RUN_CARD JSON porte, ce qui va dans la trace, ce qui se perd |
| **F. Façades concurrentes** | F-DIR-010, F-DIR-013, F-DIR-034, F-DIR-035 | Résumés de clôture et de preuve minimale hors du propriétaire |
| **V. Cible visuelle** | F-DIR-023 | Quatre représentations de la cible DIRECTION |
| **K. Contrats structurés** | F-ACT-005, F-ACT-006, F-ACT-007, F-ACT-029, F-ACT-030 | Scope attendu ou observé, activation, vocabulaire, phase des champs |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C2_harnais_non_regression.py` : RUN_CARD, contrats de production et gardes textuelles ;
- 4 lignes ajoutées à la liste close ;
- l'**inventaire à date** de la migration de schéma unique (§6).

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 à 11.08 ; D-ACT-1 = c (machine pour les seuls invariants déterministes à haut risque) ; D-FAC-1 = c (façades bornées, « voir propriétaire ») ; règle A2 (motif exigé) ; « qui accepte prouve » |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` : **218/218 OK**, vérifiés après les contrôles directs |
| Sources relues | ACTION 23–36 (HANDOFF), 93–114 (UI-UX-REALITY), 204–218, 252–334 (RUN_CARD), 339–347 (RUN-LITE), 391–406 (CLOSE-PACKAGE), 527–603 (STRUCTURED-PROOF), 915–932 (CLOSE-EXIT-CHECK) ; DIRECTION 217–240 (ligne de run), 247–258 (DAILY), 372–446 (VISUAL_TARGET), 656–670 (section 0), 712–719 (alternative située), 788 ; BIBLIOTHEQUE 22–40 ; README 13 |
| Machine relue | `run_card.schema.json` (`risk`, `direction`, `anchors`, `artifact`, `proof`) ; `production_contracts.schema.json` et son exemple ; `validate_contracts.py` (`validate`, `semantic_check`, `expect_invalid`, `name_for_path`) |
| Antécédents | 9.08 (quatre éléments de clôture DAILY contre treize champs HANDOFF ; six champs sur dix de VISUAL_TARGET conservés) ; 11.03 §4 (transfert F-ACT-017 (1)) ; 11.07 (contrat de composant déplacé vers BIBLIOTHEQUE) ; 11.08 (triade N/A-JUSTIFIED / NOT-OBSERVED / NOT-VERIFIED) |

## 2. Re-vérification

**Harnais C2 sur B01 :**
- témoins **3/3** ;
- RUN_CARD **0/6** ;
- contrats **0/10** ;
- gardes textuelles **0/12**.

Les échecs portent le bon motif (règle A2). Les deux premières lignes du tableau ci-dessous ont aussi été vérifiées par contrôle direct, par import en lecture seule.

| Constat | Résultat B01 | Fiche |
|---|---|---|
| Contrat avec `proof_status: not_applicable` **sans raison** | **accepté** | F-ACT-007 |
| `proof_scope` réécrit en cible future (« à observer après build ») alors que des exigences sont `observed` | **accepté** | F-ACT-005 |
| **L'exemple officiel lui-même** : `proof_scope` annonce « desktop 1440, **tablette 834**, … » alors que l'entrée `responsive_matrix: tablette` est `not_verified` | le scope prévu est présenté comme observé, **dans l'exemple canonique** | F-ACT-005 |
| `UI_UX_REALITY_PACK` seul | **rejeté** : `champ obligatoire absent: creative_direction_set` | F-ACT-006 |
| Carte avec `risk.statement` (le « risque principal » d'ACTION 271) | **rejetée** : `champs inconnus : statement` ; le schéma ne porte que le niveau | F-ACT-017 (1) |
| Carte avec `next_action` | rejetée (`champs inconnus`). **Comportement conservé** par la décision : témoin T-CONS | F-ACT-002 |

**Relecture des textes : trois constats qui orientent la décision.**

1. **La table de correspondance existe déjà, en prose et incomplète.** ACTION 278 décrit comment les champs de la RUN_CARD humaine deviennent `closure.*`, `artifact.*` et `proof.*`. Elle ne dit rien de HANDOFF (NEXT-ACTION, EXIT-CONDITION, METHOD) ni des vues DIRECTION. La correction **transforme ce paragraphe en table** au lieu d'ajouter un second texte.
2. **La projection perd un seul champ du minimum RUN_CARD.** Sur les quinze champs de la table ACTION 256–274, quatorze ont une projection. `RISK` (« risque principal et impact potentiel ») n'est projeté que par son **niveau**. NEXT-ACTION et EXIT-CONDITION ne sont pas des champs du minimum RUN_CARD : ce sont des champs HANDOFF.
3. **Les façades de clôture divergent du canon.** Exemples :
   - DAILY LITE (251) omet le verdict et `DECISION-CHANGE`, que CLOSE-PACKAGE LITE exige ;
   - la section 0 omet PARTIALLY-HELD et mélange statut, issue et verdict dans sa « condition d'arrêt » ;
   - VISUAL_TARGET a une décision, « **Résolution initiale** », qui n'a **aucune ligne** dans sa propre table, et SPECCED (443) exige un « rendu attendu » qui n'y figure pas non plus.

## 3. Les sept questions du §21

| Question | P. Projection | F. Façades | V. Cible | K. Contrats |
|---|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : reprise d'un run par un autre agent ; un champ glissé dans un voisin change le sens de la carte | **Oui** : une clôture LITE conforme à DAILY omet le verdict | **Oui** : `SPECCED` peut être déclaré sur deux listes différentes | **Oui** : une couverture prévue est lue comme observée (dans l'exemple officiel) |
| Défaut réel ? | Oui (§2, et 9.08) | Oui (matrice DAILY × CLOSE-PACKAGE) | Oui | Oui (§2 : trois acceptations fautives, un rejet fautif) |
| Gain > charge ? | Oui : un paragraphe devient une table ; **un** champ nouveau | **Oui, avec réduction** : deux tableaux et une colonne supprimés | **Oui, avec réduction** : une table en moins, une ligne en plus | Oui : un champ renommé en deux, un enum, une règle de racine |
| Nouvelle autorité ? | **Non** : ACTION reste propriétaire ; la table est déclarée descriptive (comme 278) | **Non** : l'autorité revient à ACTION et START | **Non** : la table existante devient la seule forme | **Non** : jetons de la triade canonique ; activation reprise des déclencheurs existants |
| Testable ? | Oui : machine (C2-01 à 03) plus épreuve de projection | Gardes textuelles plus matrice façade × canon | Garde plus épreuve de projection | Machine (K-01 à K-P5) plus gardes |
| Positif / défensif équilibré ? | Oui : aucun nouveau champ HANDOFF ; LITE non persistant garde une forme courte | Oui | Oui | **Oui, gain positif** : un paquet UI/UX seul devient valide ; un pack « avant build » honnête aussi |
| Suppression ou fusion ? | **Fusion** (paragraphe → table) | **Suppression** (tableaux et colonne) | **Fusion** (quatre formes → une) | **Clarification** et **alignement** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Principe : **une forme canonique par fonction**, les autres déclarées projections avec leurs pertes.

| Fonction | Forme canonique | Propriétaire |
|---|---|---|
| Lancement | Ligne de run | DIRECTION 219–237 (mémoire de lancement, déjà déclarée) |
| Transmission | `ACTION/HANDOFF` | ACTION |
| Clôture par mode | `ACTION/CLOSE-PACKAGE` | ACTION |
| Sortie | `ACTION/CLOSE-EXIT-CHECK` | ACTION |
| Projection persistante | RUN_CARD JSON, selon la table de correspondance (T-1) | ACTION ; schéma et validateur pour la structure |
| Cible DIRECTION | Table `VISUAL_TARGET` | DIRECTION |

Types §21 :
- **fusion** (T-1, T-7) ;
- **suppression** (T-4, T-5, T-7) ;
- **clarification** (T-3, T-9, T-10) ;
- **alignement humain/machine** (INV-C2-1 à INV-C2-4, T-6).

### 4.1 P. Projection

**T-1. ACTION/RUN_CARD, paragraphe 278 → table de correspondance.** La table conserve la mention de 278 « descriptive : le schéma et le validateur restent les autorités de structure ».

Elle a une colonne **Phase**, avec trois valeurs : `avant build`, `après observation`, `clôture`.
- Ce vocabulaire est fixé ici.
- **F-DIR-003 (D2)** le réutilisera pour les champs DIRECTION. La fiche reste en D2 : rien n'est déplacé (même coordination que B5 / F-SAV-004).

Contenu de la table (noms de projection indicatifs pour les champs nouveaux) :

| Champ canonique | Phase | Projection RUN_CARD | Sinon |
|---|---|---|---|
| MODE, DECISION, DECISION-INTENT, OWNER, ID, DATE / VERSION | avant build | `mode`, `decision`, `decision_intent`, `owner`, `id`, `date_version` | — |
| RISK (risque principal et impact potentiel) | avant build | `risk.level` + **`risk.statement`** (INV-C2-1) ; protection critique : `risk.critical_protection` | — |
| SCOPE, ARTIFACT | avant build, puis clôture | `artifact.scope`, `artifact.locator`, `artifact.version` | — |
| OBSERVATION | après observation | `proof.observed` | — |
| METHOD | après observation | `proof.provenance.method` (+ `capability`, `observed_at`) | — |
| PROOF / TRACE-LOCATOR | clôture | `trace_locator` | preuve détaillée : trace |
| LIMIT / NOT-VERIFIED | clôture | `closure.limitations`, `proof.not_verified` ; axes : `closure.axes` | — |
| STATE, ISSUE, VERDICT, DIRECTION-STATUS | chaque transition | `closure.state`, `.issue`, `.verdict`, `.direction_status` | — |
| DECISION-CHANGE | après observation | `decision_change` (outcome, C1) | — |
| NEXT-PROOF | clôture | `next_proof` | — |
| NEXT-ACTION | clôture | DIRECTION : `creative_close.next_polish_action` ; sinon `next_proof` lorsque l'action suivante est une preuve | **hors projection : trace** |
| EXIT-CONDITION | clôture | `closure.reservations[].exit_condition` lorsqu'une réserve existe | **hors projection : trace** |
| VISUAL_TARGET : thèse, anti-direction, premier objet, périmètre, contrainte | avant build | `direction.thesis`, `.anti_direction`, `.first_object`, `.scope`, `.constraint` | — |
| VISUAL_TARGET : ancre | avant build | `anchors[]` (type, date : B4) | — |
| VISUAL_TARGET : objet de preuve | avant build → après observation | `next_proof` avant, `proof.observed` après | — |
| VISUAL_TARGET : matière / asset | avant build | droits : `artifact.rights_status` (B2) | route, cadrage, fallback : **trace** |
| VISUAL_TARGET : conséquence observable, silhouette, relations de plans, opération dominante, typographie, résolution initiale | avant build | — | **hors projection : trace** |
| Enjeu identitaire, calibration | avant build, puis clôture | `direction.identity_stake`, `direction.calibration` (B4) | — |
| Paquet d'alternative (DIRECTION 716) | avant build | — | **hors projection : trace** (T-6) |
| Creative close, B1b, paquet SYSTÈME, profil de style | clôture | `creative_close.*`, `closure.b1b`, `closure.system_package`, `profile_decision` | — |
| Sources, statut de source | avant build | `sources[]` (section canonique ou locator) | statut vérifié / non revu : **trace** |
| Manifeste externe | clôture | résolu par `trace_locator` | — |

La table porte aussi **une règle** : un champ hors projection n'est **jamais** glissé dans un champ voisin (par exemple NEXT-ACTION dans `limitations`) ; il reste dans la trace, que `trace_locator` rend retrouvable.

**T-2. Table minimale ACTION 271.** La ligne `RISK` ajoute : « projection : `risk.level` et `risk.statement` ».

**T-3. ACTION/HANDOFF.** Trois phrases, pas de tableau :
1. Situer les formes : la ligne de run est la mémoire de lancement ; HANDOFF est la transmission ; CLOSE-PACKAGE est la clôture par mode ; la RUN_CARD JSON est la projection persistante, selon la table de RUN_CARD.
2. **Forme courte LITE non persistante** : le paquet LITE de `CLOSE-PACKAGE`. Les autres champs HANDOFF sont `N/A-JUSTIFIED` par défaut. Pertes déclarées : METHOD, EXIT-CONDITION. TRACE-LOCATOR est l'artefact, comme ACTION 273 l'admet déjà en LITE.
3. Une reprise par un autre agent exige OWNER et NEXT-ACTION ; sinon la forme courte reste une préparation (règle actuelle, conservée).

**T-6. DIRECTION 716.** « Avant le build, la `RUN_CARD` nomme… » devient : « Avant le build, **la trace du run** (retrouvable par `trace_locator`) nomme la position retenue, l'alternative considérée, la raison de son niveau de matérialisation et la preuve attendue. La projection JSON ne porte pas ce paquet (voir `ACTION/RUN_CARD`). »

**Sous-décisions (fiches qui divergent de la décision de grappe) :**

| Fiche | Sous-décision | Raison |
|---|---|---|
| **F-ACT-017 (1)** | **Nouveau champ** `risk.statement`, requis **dans tous les modes**. C'est une exception déclarée à « qui accepte prouve » | Ce n'est pas un champ de preuve mais un champ de **lancement**, comme `decision_intent`, requis partout. ACTION 256 le met dans le minimum de toute RUN_CARD. C'est le seul champ de ce minimum sans projection. Coût : une chaîne par fixture, dans la migration unique |
| **F-DIR-039** | **Aucun champ** : transport par la trace | Le paquet d'alternative n'est dû que si la décision est ouverte et qu'une alternative plausible existe (716). Ce déclencheur n'est pas déterministe. D-ACT-1 = c : **forme seule** |
| **F-ACT-028** | **Aucun invariant nouveau** | Les invariants déterministes utiles existent déjà : type et date d'ancre (B4-1, B4-2), droits (B2-10), `trace_locator` par mode (existant, et D2 pour ITER). Statut de source, route d'asset et résolution d'un manifeste : **forme seule**, portés par la table |
| **F-ACT-002 (champs HANDOFF)** | **Aucun champ** `next_action` ou `exit_condition` | La recommandation elle-même (« sans nouveau champ par défaut », F-DIR-006) l'exclut. Le témoin T-CONS garde le rejet actuel |

### 4.2 F. Façades concurrentes (D-FAC-1 = c)

| # | Où | Quoi |
|---|---|---|
| T-4 | **DIRECTION DAILY 251–257** | La colonne « Clôture minimale » est **supprimée**. Sous la table : « La clôture minimale de chaque mode est `ACTION/CLOSE-PACKAGE`. » DAILY garde son rôle : une vue de chargement (démarrage, ajouts) |
| T-5 | **DIRECTION section 0, 662–668** | Le tableau est **supprimé**. Il est remplacé par une phrase : « Portée : `DIRECTION/START`. Preuve minimale : `ACTION/PRECONDITION` et `ACTION/RUN-<MODE>`. Condition d'arrêt : `ACTION/CLOSE-EXIT-CHECK`. » Les paragraphes sur les capacités (658–660), « HELD n'équivaut jamais à ACCEPTED » et la règle des axes (670) restent. Cette suppression règle aussi F-DIR-035 : la condition d'arrêt DIRECTION qui mélangeait les statuts disparaît |
| T-11 | **DIRECTION 237** | La ligne de run est déclarée « **sous-ensemble de lancement** de `ACTION/HANDOFF` ». La ligne compacte de 221 en est l'affichage. Owner et limite restent exigés « lorsque le risque ou la reprise l'exige » (223, inchangé) |

**Conforme, sans changement :**
- la sortie de sélection BIBLIOTHEQUE (≈ 38), déjà déclarée « projection structurelle locale vers le handoff canonique » ;
- l'entrée prioritaire BIBLIOTHEQUE, déjà déclarée « résumé de protection ».

**Résultat pour F-DIR-010.** Des six formes minimales concurrentes, il reste :
- deux formes canoniques (HANDOFF, CLOSE-PACKAGE) ;
- une mémoire de lancement ;
- une projection tabulée ;
- deux résumés BIBLIOTHEQUE déjà bornés.

### 4.3 V. Cible visuelle (F-DIR-023)

| # | Où | Quoi |
|---|---|---|
| T-7 | **VISUAL_TARGET** | La table de dix champs est la **seule représentation canonique**. Elle reçoit une ligne **« Résolution initiale »** : niveau de contenu réel, d'états, de responsive, d'asset et de détail attendu au premier rendu. C'est la **fusion** de la quatrième décision et du « rendu attendu » de SPECCED 443 : pas de contenu nouveau. **La table des quatre décisions est supprimée.** Une phrase la remplace : « promesse = thèse + conséquence observable ; relation = opération dominante + relations de plans ; composition = silhouette + relations de plans ; résolution initiale = ligne du même nom. » Le paragraphe « Compilation » est déclaré **ordre de travail sur les champs de la table**, pas une seconde liste |
| T-8 | **SPECCED 443** | L'énumération concurrente devient : « prête à construire lorsque **chaque champ de la table** est renseigné ou `N/A-JUSTIFIED` ; la route d'asset seulement si nécessaire » |

### 4.4 K. Contrats structurés

| # | Où | Quoi |
|---|---|---|
| T-9 | **ACTION/STRUCTURED-PROOF** (529 et titre) | Nouveau titre : « **contrats de décision et leur preuve** ». La phrase 529 (« obligatoires seulement lorsque le mode ou le risque les déclenche », sans dire lesquels) devient une **matrice d'activation** : contrat / déclencheur / sinon `N/A-JUSTIFIED` avec raison. **Règle de phase :** les lignes de preuve sont marquées « après observation » (U : OBSERVATION / MEASURE, SATISFACTION, LIMIT, NEXT-PROOF ; asset : « Preuve V/U/A/T »). Avant observation, elles restent vides ou `NOT-VERIFIED`, **jamais préremplies par l'attendu**. Après observation, la cible est **conservée** et l'observation s'ajoute à côté (F-ACT-030) |
| T-10 | **ACTION/UI-UX-REALITY 107** | `PROOF-SCOPE` devient `EXPECTED-SCOPE` (avant build) et `OBSERVED-SCOPE` (après observation). La couverture emploie `OBSERVED`, `NOT-VERIFIED` et `N/A-JUSTIFIED` (avec raison). `OBSERVED` n'est pas `PASS` : une observation peut être négative, et son résultat vit dans `EVALUATION_CASE` ou la trace. `NOT-OBSERVED` n'y est pas employé : il qualifie une conséquence de décision (C1) |

**Matrice d'activation (T-9)** : chaque déclencheur est **repris d'un texte existant**.

| Contrat | Déclencheur (source) |
|---|---|
| Carte de hiérarchie | STANDARD ou DIRECTION ; tout run dont la hiérarchie peut changer la décision (CLOSE-PACKAGE STANDARD et DIRECTION) |
| Preuve U structurée | U dominant (543) |
| Partition typographique | Famille, registre, langue, données ou hiérarchie typographique pouvant changer la décision (560) |
| Fiche d'asset directeur | Asset ou absence d'asset portant une décision perceptible (DIRECTION 423) |
| Contrat de composant partagé | Pattern réutilisable, composant critique ou partagé : **défini dans BIBLIOTHEQUE/COMPONENTS** (B5, T-1) |
| Motion ou scène spatiale | Motion non triviale, animation interactive, scène 3D (598) |
| `CREATIVE_DIRECTION_SET` | DIRECTION à décision ouverte avec alternative plausible (716) |
| `UI_UX_REALITY_PACK` | Surface UI/UX nouvelle ou substantiellement modifiée (95) |
| `EVALUATION_CASE` | Pilote ou série de runs (CLOSE-EXIT-CHECK, « Mesure expérimentale ») ; README 13 |

Zéro contrat est valide lorsque aucun déclencheur n'est actif, comme « zéro route est valide » dans BIBLIOTHEQUE.

### 4.5 Invariants machine (liste close D-ACT-1)

| ID | Invariant | Cible | Fiche |
|---|---|---|---|
| **INV-C2-1** | `risk.statement` requis dans tous les modes, non vide, sans placeholder (même ensemble que `critical_protection`) | `validate_run_card` | F-ACT-017 (1), F-ACT-002 |
| **INV-C2-2** | Racine des contrats : les trois objets sont individuellement facultatifs, **au moins un** présent ; `semantic_check` ne contrôle que les objets présents | `validate_contracts` | F-ACT-006 |
| **INV-C2-3** | `coverage_map[].proof_status` ∈ {`OBSERVED`, `NOT-VERIFIED`, `N/A-JUSTIFIED`} ; `N/A-JUSTIFIED` ⇒ `reason` non vide | `validate_contracts` | F-ACT-007 |
| **INV-C2-4** | `expected_scope` requis, `observed_scope` chaîne ou `null` ; une entrée `OBSERVED` ⇒ `observed_scope` non vide | `validate_contracts` | F-ACT-005, F-ACT-030 |

**Extension déclarée de la liste close.** C2 est la première grappe à ajouter des invariants au validateur des **contrats de production**. D-ACT-1 vaut pour toute la machine. La liste close les accueille donc, avec la famille « Contrats de production (validate_contracts) ». Le nom du fichier est gardé, pour la continuité.

**Forme seule (déclarée) :**
- un champ hors projection n'est jamais glissé dans un voisin ;
- `observed_scope` est inclus dans `expected_scope` ;
- un champ « après observation » n'est pas prérempli ;
- le statut de source ;
- la route d'asset.

Aucun de ces contrôles n'est déterministe sans lecture.

**Dépendance.** `validate_contracts` ne valide aujourd'hui que l'exemple canonique (`name_for_path` : « chemin non canonique »). Les invariants C2-2 à C2-4 ne protégeront les projections des équipes qu'après **F-ACT-008 (C9)**. C9 décidera aussi la liaison exacte `coverage_map` ↔ matrices (**F-PC-002**). C2 décide la **forme** ; C9 décidera l'**outil**.

## 5. Rectification

À la fin de 11.08, j'ai annoncé que C2 « bouclera la migration unique du schéma ». **C'est inexact.** Les autres grappes contiennent encore des candidats à des changements de schéma ou de validateur :

| Grappe | Candidats |
|---|---|
| C3 | F-PC-001 (exception motivée dans `creative_direction_set`) |
| C4 | F-ACT-020 (profil strict par mode) |
| C9 | F-ACT-008, F-DF-001, F-PC-002, F-RB-001 |
| D2 | F-DIR-036 (`trace_locator` pour ITER persistant) |

C2 **clôt la projection RUN_CARD** issue de HANDOFF et des vues DIRECTION. L'inventaire du §6 est un **inventaire à date**. Il sera clos à la fin de la phase 11 (après D4), avant toute phase 12.

## 6. Inventaire à date de la migration de schéma unique (phase 12)

**`run_card.schema.json`**

| Objet | Changement | Grappe |
|---|---|---|
| `risk.statement` | nouveau, requis | C2 |
| `risk.critical_protection.result` | nouveau, enum | B1 |
| `closure.exception` | nouveau (réserve commune + `gate_axis`, `failure_evidence`, `requested_by`, `disposition`) | B1 |
| `closure.axes`, `closure.reservations` | nouveaux (réserve commune : 7 attributs, **définie une seule fois**, réutilisée par l'exception) | B2 |
| `artifact.version`, `artifact.rights_status` | nouveaux | B2 |
| `proof.provenance.capability` ; `capability_profile.basis` | nouveau ; basis devient une liste d'objets typés | B2 |
| `closure.system_package`, `closure.b1b` | nouveaux | B3 |
| `anchors[].type` ; exigence « au moins un ancrage » | nouveau ; remplacée par INV-B4-6 | B4 |
| `direction.identity_stake`, `direction.calibration` | nouveaux | B4 |
| `decision_change.outcome`, `.reason` | nouveaux (`value` et `evidence` conservés) | C1 |
| `closure.verdict` | devient nullable | C1 |
| `closure.reclassification`, `profile_decision.phase` | nouveaux | C1 |

**`production_contracts.schema.json`**

| Objet | Changement | Grappe |
|---|---|---|
| racine `required` | vidé ; « au moins un » dans le validateur | C2 |
| `ui_ux_reality_pack.proof_scope` | remplacé par `expected_scope` + `observed_scope` | C2 |
| `coverage_map[].proof_status`, `.reason` | enum canonique ; raison | C2 |

**Validateurs**

| Script | Changement | Grappe |
|---|---|---|
| `validate_run_card.py` | **34 invariants nouveaux** : B1 7, B2 10, B3 4, B4 6, C1 6, C2 1 ; formats ISO (`observed_at`, `anchors[].date`, `review_date`) | B1–C2 |
| `validate_run_card.py` | INV-E02 remplacé ; INV-E11 retiré ; INV-E17 et INV-E24 généralisés ; INV-E10 modifié | B2, B4, C1 |
| `validate_contracts.py` | Prévalidation du schéma et parcours statique des mots-clés | A1 |
| `validate_contracts.py` | `semantic_check` par objet présent ; INV-C2-2 à C2-4 | C2 |
| Suite de tests | Table d'oracles déclarative, messages exigés, cas unitaires en mémoire (N ≥ 20) ; les cas de tous les harnais B1–C2 y entrent | A2 |

**Données**
- `run_card.example.json` ;
- les **25 fixtures** (22 invalides, 3 valides) ;
- `production_contracts.example.json`, dont le `proof_scope` fautif est corrigé en `expected_scope` + `observed_scope` sans la tablette.

Règle A2 : chaque fixture migrée garde **son seul défaut** voulu, et son motif.

**Candidats encore ouverts :** C3, C4, C9, D2 (§5).

## 7. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Ordre** : A1 → A2 → migration unique → textes. Dans les textes, le canon ACTION (T-1, T-2, T-3, T-9, T-10) passe **avant** les renvois DIRECTION (T-4 à T-8, T-11) |
| C2 | **Un cycle par propriétaire** : ACTION reçoit C1 T-1, C2 T-1 à T-3, T-9 et T-10 et B5 T-2 **dans la même passe** (STRUCTURED-PROOF est touchée par B5 et par C2) ; DIRECTION reçoit C1 T-2 et C2 T-4 à T-8 et T-11 dans la même passe |
| C3 | **Aucun contenu nouveau** : la ligne « Résolution initiale » fusionne deux textes existants ; chaque déclencheur de la matrice cite sa source |
| C4 | **Proportion** : la forme courte LITE reste valide ; zéro contrat structuré est valide ; aucun champ HANDOFF n'est ajouté au schéma |
| C5 | **Relecture complète** d'ACTION 23–36, 93–114, 252–334, 391–406, 527–603 et de DIRECTION 217–258, 372–446, 656–670, 712–719, 788 |

## 8. Condition de sortie (phase 13)

1. `C2_harnais_non_regression.py` : témoins **3/3**, RUN_CARD **6/6**, contrats **10/10**, gardes **12/12**. Les harnais A1 à C1 restent verts.
2. **Épreuve de projection**, rejouée par un lecteur qui ne connaît pas ce rapport :
   - un run LITE non persistant ;
   - un run STANDARD persistant ;
   - un run DIRECTION clôturé (rejeu 9.08) ;
   - un run sans changement de décision ;
   - une réserve avec condition de sortie ;
   - une **reprise par un autre agent** depuis la carte et la trace seules.

   Critère : chaque champ HANDOFF et chaque champ VISUAL_TARGET se retrouve dans la carte ou dans la trace. **Aucune perte non déclarée** dans la table T-1 (F-ACT-002, F-DIR-006, F-DIR-010).
3. **Matrices façade × canon** : DAILY × CLOSE-PACKAGE (plus de résumé divergent) ; section 0 → PRECONDITION et CLOSE-EXIT-CHECK, un cas par mode ; VISUAL_TARGET → quatre regroupements et SPECCED, sans perte (F-DIR-013, 023, 034, 035).
4. **Activation** : cinq modes × risques U/A/T/V × asset présent ou absent × composant neuf ou existant × motion triviale ou non. Chaque omission porte sa raison (F-ACT-029).

**Limite déclarée.** Les gardes textuelles détectent des formulations ; seule l'épreuve de projection prouve que la reprise fonctionne. Idéalement, un observateur indépendant la conduit (limite F-ACT-037).

## 9. Sortie

- **PATCH-DECISION C2 : CORRIGER.**
  - 4 invariants : 1 RUN_CARD, 3 contrats ;
  - 1 champ nouveau (`risk.statement`) ;
  - 11 corrections de texte ;
  - 4 sous-décisions ;
  - 1 rectification (§5).
- **Liste close : 66 lignes, 62 actifs.**
- **Inventaire à date** de la migration unique établi (§6).
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Le « mapping manquant » existait déjà en prose : il devient une table, sans second texte.
- Sur treize champs HANDOFF, **un seul** gagne un champ machine, parce qu'il appartient au minimum RUN_CARD. Les autres ont une place déclarée (projection ou trace).
- **Bilan :**
  - trois résumés concurrents disparaissent : la colonne DAILY, le tableau de la section 0, la table des quatre décisions ;
  - deux ajouts : la table de correspondance, à la place d'un paragraphe ; la matrice d'activation, à la place d'une phrase.
  - Le texte gagne quelques lignes, mais perd trois sources de divergence.
- L'exemple officiel des contrats enseignait lui-même le défaut F-ACT-005 ; la migration le corrige.

**Prochaine unité : 11.10 PATCH-DECISION C3.**
