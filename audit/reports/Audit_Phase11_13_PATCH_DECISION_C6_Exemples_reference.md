# DG-AUDIT-001 — Phase 11.13 — PATCH-DECISION C6 : exemples de référence

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.13 ».

**Grappe C6 : 3 fiches, toutes Significatif.** Même risque : **les agents imitent les exemples** (10.04a, preuve d'objet). Un exemple qui contredit ACTION enseigne donc la contradiction mieux que la règle n'enseigne la règle.

| Fiche | Exemple | Défaut | Majeur d'ACTION lié |
|---|---|---|---|
| F-EX-001 | `references/examples.md` 17, 38 ; GLOSSAIRE 57 | Une liste de propriétés modifiées tient lieu de `DECISION-CHANGE`, sans décision tranchée ni observation | F-ACT-013 / F-ACT-014 (C1) |
| F-EX-002 | `references/examples.md` 62–63 | Une paire de captures est étendue à la mémorisation et à la tâche | F-ACT-018 (B2) |
| F-GLO-002 | GLOSSAIRE 59 | `CLOSED` + `ACCEPTED-WITH-RESERVATION` « sur l'accessibilité non vérifiée », sans portée, owner ni sortie | F-ACT-023 (B2) |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C6_harnais_non_regression.py` ;
- 4 entrées ajoutées à la liste close des conditions de façade (LCF).

Aucun patch, aucun prototype : les textes cibles du §4.2 sont des formulations de décision. Ils n'ont pas été appliqués à une copie du package, seulement confrontés, **en tant que chaînes**, aux expressions régulières de la LCF.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | B2 (réserve commune à sept attributs, axes, `basis` typée) ; C1 (triade, `decision_change.outcome`, verdict nul avant décision, `profile_decision.phase`) ; C5 (LCF, validateur « carte et façades ») |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; contrôles sur copie |
| Sources relues | `references/examples.md` (90 lignes, en entier) ; `references/canonical_minimum.md`, `flow.md`, `machine_projection.md` (recherche ciblée) ; GLOSSAIRE 30–66 ; skill 40, 143 |

## 2. Re-vérification

**Harnais C6 sur B01 :**
- témoin **1/1** ;
- conditions LCF **0/4** ;
- mutations au rouge **0/4** ;
- garde **0/1**.

Les trois fiches sont **confirmées**. La relecture intégrale d'`examples.md` montre que les quatre exemples contredisent, chacun à sa manière, des décisions de la phase 11 :

| Exemple | Ce qu'il enseigne | Contredit |
|---|---|---|
| LITE (11–19) | `DECISION-CHANGE: couleur du texte et de la bordure` : une propriété, pas une décision ; `STATE: CLOSED` **sans verdict** | F-EX-001 ; INV-C1-4 (CLOSED ⇒ verdict) ; CLOSE-PACKAGE LITE (verdict exigé) |
| DIRECTION (29–43) | « la matière sonore a changé la scène » : aucune décision nommée ; `ACCEPTED-WITH-RESERVATION` **sans réserve** | F-EX-001 ; INV-B2-9 (réserve à sept attributs) |
| DIRECTION + STYLE (55–65) | « plus mémorable sans perdre la tâche », sur une paire de captures | F-EX-002 ; F-ACT-018 ; `profile_decision` sans phase (INV-C1-6) |
| SYSTÈME (75–85) | `NOT-OBSERVED: tous les écrans, plateformes et thèmes` : le jeton de la triade sert de « non vérifié » | **Triade C1**. `canonical_minimum.md` 17 et GLOSSAIRE 42 disent pourtant le contraire, juste à côté |

**Deux constats hors fiche, rattachés sans nouvelle fiche :**
1. **Le mauvais usage de `NOT-OBSERVED`** (SYSTÈME, 81) est le défaut que C1 a décidé de rendre impossible dans la carte. Je le corrige ici comme **application de C1 à un exemple**.
2. **L'exemple YAML de `machine_projection.md`** (12–88) est une projection RUN_CARD qui devra suivre la migration unique : nouveaux champs B1–C4. Je le verse à l'**inventaire de migration**, comme les fixtures. Son défaut propre (**F-MP-001**, E1) reste en E1 et sera appliqué dans le même cycle.

## 3. Les sept questions du §21

| Question | F-EX-001 | F-EX-002 | F-GLO-002 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : des clôtures listent des modifications sans décision | **Oui** : un avis visuel est présenté comme un effet chez l'utilisateur | **Oui** : un formulaire critique peut être accepté avec un focus non testé |
| Défaut réel ? | Oui (7.01 : le validateur accepte aussi « explication seulement ») | Oui (même claim que 4.07) | Oui (9.07 : l'a11y non vérifiée cachait des défauts réels) |
| Gain > charge ? | Oui : une ligne par exemple | Oui : deux lignes | Oui : une cellule |
| Nouvelle autorité ? | **Non** : les exemples prennent la forme décidée en C1 | **Non** : B2 et F-ACT-018 | **Non** : réserve commune de B2 |
| Testable ? | LCF-11 | LCF-14 | LCF-12 et garde |
| Positif / défensif équilibré ? | Oui : l'exemple montre **comment bien faire**, pas seulement ce qu'il faut éviter | Oui : le claim visuel reste valide | Oui : le cas éligible reste montré (option « cas éligible », pas « retrait ») |
| Suppression ou fusion ? | **Correction d'exemple** | **Correction d'exemple** | **Correction d'exemple** et **clarification** (état ≠ verdict) |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

### 4.1 Statut des exemples : des façades d'ACTION, gouvernées par la LCF

Les exemples ne sont pas normatifs (examples.md 3 ; GLOSSAIRE 50), mais ils sont **copiés**. D-FAC-1 = c s'applique donc à eux comme aux autres façades :
- ils restent courts ;
- ils ne peuvent pas contredire le propriétaire ;
- un test le vérifie.

La phrase d'en-tête d'`examples.md` (« une omission dans une condensation n'est pas une suppression ») est conservée. Elle ajoute : « **les champs affichés respectent les contrats d'ACTION** ; un champ omis reste dû dans la RUN_CARD ».

**Quatre entrées LCF (règle d'entrée de C5 : source propriétaire et mutation rouge) :**

| ID | Condition vérifiée au build | Source | Mutation rouge |
|---|---|---|---|
| **LCF-11** | Toute ligne `DECISION-CHANGE:` d'exemple a la forme `issue — décision (observation : …)`, avec une issue de la triade C1. L'exemple du GLOSSAIRE contient une issue et une observation | ACTION 206–236 ; INV-C1-1 | M-7 |
| **LCF-12** | Tout exemple `ACCEPTED-WITH-RESERVATION` (bloc ou cellule du GLOSSAIRE) porte une réserve avec owner, prochaine preuve, date de revue et condition de sortie | INV-B2-9 ; ACTION 413–427 | M-8 |
| **LCF-13** | `NOT-OBSERVED` n'apparaît que comme issue de `DECISION-CHANGE`, jamais comme champ. Tout bloc `STATE: CLOSED` porte un `VERDICT:` | Triade C1 ; INV-C1-4 | M-9 |
| **LCF-14** | Une ligne `EVIDENCE:` fondée sur des captures ne revendique ni mémorisation, ni tâche, ni usage, sauf si elle nomme un protocole ou des participants | F-ACT-018 ; ACTION 329–331 | M-10 |

**La LCF passe à 16 entrées.**

**Forme seule (déclarée).** Que l'observation citée **soutienne réellement** la décision n'est pas vérifiable par expression régulière. L'épreuve de lecture du §6 couvre ce point.

### 4.2 Textes cibles

| # | Où | Ligne(s) cible(s) |
|---|---|---|
| T-1 | **LITE** (13–19) | `RISK: libellé secondaire illisible en contraste faible` · `OBSERVED: ratio 3,1:1 → 5,2:1 ; focus visible ; structure et interaction conservées` · `LIMIT: autres thèmes hors scope` · `AXES: V PASS · A PASS (contraste, focus) · U N/A-JUSTIFIED · T N/A-JUSTIFIED` · `DECISION-CHANGE: CONFIRMED — garder la hiérarchie du bouton secondaire et ne corriger que sa couleur (observation : snapshot avant/après, ratio mesuré)` · `VERDICT: ACCEPTED` · `STATE: CLOSED` |
| T-2 | **DIRECTION** (35–42) | `AXES: V PASS · U NOT-VERIFIED · A NOT-VERIFIED · T PASS` · `DECISION-CHANGE: CHANGED — la topographie sonore remplace la carte à pins comme premier objet (observation : paire v1/v1b, le premier geste est lu en premier dans le viewport inspecté)` · `RESERVATION: accessibilité exécutée non vérifiée — owner : lead design ; scope : hero ; impact : parcours clavier de la topographie inconnu ; prochaine preuve : parcours clavier et lecteur d'écran ; revue : 2026-10-09 ; condition de sortie : parcours clavier observé sans blocage` |
| T-3 | **DIRECTION + STYLE** (58–64) | `PROFILE-PHASE: observed` · `EVIDENCE: paire de captures avec et sans traitement pixel/raster : les pièces se distinguent des contrôles et les métadonnées restent lisibles (claim visuel seulement)` · `PROOF-LIMIT: mémorisation et tâche NOT-VERIFIED (elles exigeraient un protocole utilisateur : participants, tâche, mesure) ; droits des fragments externes non validés` · `DECISION-CHANGE: CHANGED — le traitement numérique est limité aux pièces et retiré des contrôles critiques (observation : paire de captures)` |
| T-4 | **SYSTÈME** (80–84) | `OBSERVED: libellé long, erreur, focus et clavier dans trois consommateurs ; troncature observée sur mobile dans le consommateur 2` · `NOT-VERIFIED: autres écrans, plateformes et thèmes` · `DECISION-CHANGE: ABANDONED — l'extension du Select en l'état est abandonnée jusqu'à correction de la troncature mobile (observation : consommateur 2)`. L'annotation narrative 87 est absorbée par ces lignes et supprimée |
| T-5 | **GLOSSAIRE 57** (`DECISION-CHANGE`) | « `CHANGED` — après observation à 390 px, la décision « deux CTA de même poids » est abandonnée au profit d'un CTA principal unique (observation : capture avant/après). » |
| T-6 | **GLOSSAIRE 59** (`CLOSED`) | « La trace et les artefacts sont persistés. `CLOSED` ne dit rien du verdict : un run peut être clos en `RETURN`. Clos en `ACCEPTED-WITH-RESERVATION`, il porte une réserve complète (owner, portée, impact, prochaine preuve, date de revue, condition de sortie) sur un risque **secondaire**. Un risque critique non vérifié n'est pas éligible. » |
| T-7 | **examples.md 3** (en-tête) | Ajout : « les champs affichés respectent les contrats d'ACTION ; un champ omis reste dû dans la RUN_CARD ». |

**Sur F-GLO-002, choix entre « cas éligible » et « retrait ».** Je retiens **le cas éligible**, avec la frontière explicite (« un risque critique non vérifié n'est pas éligible »). Le retirer priverait le glossaire du seul exemple qui montre que `CLOSED` et le verdict sont deux registres distincts. Cette confusion est l'objet même de F-ACT-009 (C1).

**Le test de la fiche F-GLO-002 est couvert :**
- formulaire de santé : non éligible (T-6 ; B1 : risque critique, protection et `result`) ;
- livraison bornée avec réserve : éligible, réserve complète ;
- archive `EXPLORATORY` : issue, aucune acceptation (INV-B2-1).

## 5. Inventaire à date : ajouts C6

| Objet | Changement |
|---|---|
| `validate_reading_map.py` | LCF-11 à LCF-14 (16 entrées au total) |
| Données d'exemple | `references/machine_projection.md` (YAML) ajouté à la migration unique, avec F-MP-001 (E1) |
| Schémas, validateurs RUN_CARD et contrats | **Aucun** |

Candidats de migration de schéma encore ouverts : C9, D2.

## 6. Conditions du futur patch et de sortie

| # | Condition |
|---|---|
| C1 | **Après la migration unique** : un exemple ne peut montrer que des champs qui existent. T-1 à T-4 suivent B2, C1 et C2 |
| C2 | **Un cycle pour la skill** : `examples.md`, `machine_projection.md` (F-MP-001) et les copies de façade de C3 et C5 ensemble |
| C3 | **Exemples courts** : chaque bloc garde sa longueur à ±3 lignes. Aucun exemple ne devient un formulaire complet |
| C4 | **Distribution Local** : `skill/references/examples.md` est corrigé à l'identique (manifest 119) |

**Sortie (phase 13) :**
1. `C6_harnais_non_regression.py` : témoin **1/1**, conditions **4/4**, mutations au rouge **4/4**, garde **1/1**. Harnais A1 à C5 verts.
2. **Épreuve de lecture**, conduite par un lecteur qui ne connaît pas ce rapport :
   - chaque extrait est d'abord lu seul, puis confronté à ACTION : quel choix a été tranché, sur quelle observation (F-EX-001) ?
   - la paire seule, puis la paire avec un protocole utilisateur : quels claims sont soutenables à chaque étape (F-EX-002) ?
   - la ligne 59 appliquée à un formulaire de santé, à une livraison bornée et à une archive `EXPLORATORY` (F-GLO-002).
3. **Épreuve d'imitation** (la raison d'être de la grappe) : un agent reçoit un brief LITE et un brief DIRECTION avec les **seuls exemples**. Ses cartes, sérialisées, doivent passer le validateur RUN_CARD migré.

**Limite déclarée.** L'épreuve d'imitation mesure un cas, pas une tendance (N = 2). Elle montre si les exemples enseignent la forme, pas si les agents jugent mieux.

## 7. Sortie

- **PATCH-DECISION C6 : CORRIGER.**
  - 4 entrées LCF (16 au total) ;
  - 7 corrections d'exemple ;
  - 2 rattachements déclarés : `NOT-OBSERVED` (C1) et le YAML de `machine_projection.md` (migration, F-MP-001) ;
  - 1 choix documenté : le cas éligible plutôt que le retrait.
- La liste close RUN_CARD et contrats est inchangée : **70 lignes, 66 actifs**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Les exemples étaient la **dernière couche** où les décisions de la phase 11 n'étaient pas propagées.
- Ils deviennent des façades testées, et chacun **montre la bonne forme** au lieu d'illustrer seulement une séquence.

**Prochaine unité : 11.14 PATCH-DECISION C7** (homogénéisation et ablation : 3 fiches, F-BIB-005, F-SAV-002 — candidate au relèvement en 10.03 —, F-SAV-006).
