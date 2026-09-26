# DG-AUDIT-001 — Phase 12.02 — PATCH A2 : oracles de test

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée.

**Décision de l'owner :** « Oui, enchaîne avec 12.02 ».

**Décision appliquée :** 11.02, PATCH-DECISION A2. Elle couvre quatre fiches :
- F-FIX-002 : négatifs composites ;
- F-FIX-003 : négatif sans motif ;
- F-ALL-001 : orchestrateur sans motif ;
- F-FIX-001 : fixture orpheline, rattachée à A2.

**Sorties :**
- commit B03 `3bae037`, étiquette `12.02-A2`, sur un diff distinct de celui d'A1 (condition C1) ;
- `DG_AUDIT_001_B03_12-02_A2.diff` ;
- ce rapport ;
- `A2_verifications_complementaires_12-02.py` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-02.json` ;
- `DG_AUDIT_001_B03_package_12-02.zip`.

---

## 1. Fichiers touchés

| Fichier | Lignes | Nature |
|---|---|---|
| `scripts/validate_run_card.py` | +125 / −155 (621 → 591 lignes) | Les 24 appels écrits un par un sont remplacés par une table, des cas unitaires et trois fonctions |
| `scripts/validate_all.py` | +14 / −7 | Motif obligatoire dans `expect_failure`, déclaré par ses huit usages |

**Conditions de 11.02, respectées :**
- **C2** : aucun fichier ajouté ni supprimé ; les 25 fixtures sont inchangées.
- **C5** : bibliothèque standard seulement.
- **C6** : table et mutations regroupées ; aucune refactorisation hors de la suite.

**Écart de charge, déclaré.** 11.02 annonçait que la suite passerait d'environ 155 lignes à environ 90–100. Résultat réel :
- la suite elle-même tient désormais en **3 appels** ;
- mais la table (25 entrées), les **23** cas unitaires et les trois fonctions font environ **125 lignes**.

Le gain net est de **−30 lignes**, et non d'environ −60. La prévision était optimiste d'environ 25 lignes. La couverture, elle, dépasse l'annonce : 25 fixtures (contre 24 appelées) et 23 cas unitaires (contre N ≥ 20).

## 2. Raisonnement de diff

### 2.1 Table déclarative des fixtures (F-FIX-001, F-FIX-003)

| Changement | Décision (11.02) | Effet |
|---|---|---|
| `FIXTURE_TABLE` : 25 entrées, `nom → None` (valide) ou motif attendu | §4.1-1 | La liste des fixtures et leurs oracles se lisent en un seul endroit |
| Motif **obligatoire** pour tout négatif, dans `check_fixture` | §4.1-2 | Un négatif sans motif fait échouer la suite : « oracle sans motif ». La branche qui acceptait n'importe quel échec (`expected_message and …`) disparaît |
| `check_fixture_table` : découverte de `schemas/fixtures/*.json` | §4.1-3 | « fixture non déclarée » si un fichier manque dans la table ; « fixture déclarée absente » si une entrée n'a pas de fichier |
| Fixture orpheline déclarée (`invalid_capability_profile_missing_basis.json`) avec son motif | §4.1-4 | F-FIX-001 : 25/25 fichiers exécutés par la suite native |

**Motifs (condition C4).** Chaque motif est une **sous-chaîne d'un diagnostic déjà émis**, relevé sur B03 fixture par fixture. **Aucun message du validateur n'a été réécrit.**

Deux motifs sont nouveaux, faute de message déclaré dans B01 :
- `invalid_missing_proof.json` ;
- l'orpheline.

Le premier suit la remarque de 11.02 §2.3. Cette fixture échoue sur le **contrôle sémantique** (« un verdict accepté exige au moins une preuve observed »), jamais sur le `required: proof` du schéma. Son motif le dit, au lieu de laisser croire que la fixture teste le schéma. Le `required: proof` reçoit son propre cas unitaire (U-03, §2.2).

### 2.2 Cas unitaires à faute unique (F-FIX-002)

**Méthode.** Chaque cas part d'une base valide et suit quatre étapes :
1. **La base est validée d'abord.** C'est le témoin positif : si elle échoue, le cas signale « base invalide ».
2. **Une seule faute** est ensuite appliquée en mémoire.
3. Le rejet est exigé **avec son motif**.
4. Un chemin de faute introuvable est signalé, jamais transformé en trace Python.

**Bases utilisées :**
- l'exemple canonique (DIRECTION, clôturé, accepté avec réserve) ;
- `valid_closed_return` (SYSTÈME, retour) ;
- `valid_direction_with_profile_decision` ;
- pour U-20, une base retouchée **qui reste valide** : un risque critique avec une protection complète.

| Cas | Faute unique | Invariant (fixture composite qui le couvrait) |
|---|---|---|
| U-01 | `state = HELD` | HELD (`invalid_state_held`) |
| U-02 | `proof` supprimé, verdict accepté | Preuve observée (`invalid_missing_proof`) |
| U-03 | `proof` supprimé, base retour | `required: proof` du schéma (même fixture : la faute qu'elle **nommait**) |
| U-04 | `observed = []` | Preuve observée (`invalid_empty_proof`, `…_without_observed`) |
| U-05 | `verdict = PASS` | Verdict global canonique (`invalid_global_axis_verdict`) |
| U-06 à U-10 | `direction`, `trace_locator`, `creative_close`, `direction_status`, `craft_detail` supprimés | Les cinq fixtures DIRECTION correspondantes |
| U-11 | `profile_decision.evidence` supprimé | `invalid_profile_decision_missing_evidence` |
| U-12 | `state = CHECKING` | `invalid_accepted_before_decision` |
| U-13 | `provenance` supprimée | `invalid_accepted_without_provenance` |
| U-14 | `limitations = []` | `invalid_accepted_without_limitations` |
| U-15, U-16 | `issue = FAIL-ASSUMED`, puis `BLOCKED` | `invalid_fail_assumed_accepted` (U-16 couvre la seconde branche de la même règle) |
| U-17, U-18 | `basis = []`, puis `basis` supprimée | `invalid_capability_available_without_basis`, orpheline |
| U-19 | `level = critical` sans protection | `invalid_critical_without_protection` |
| U-20 | `control = TODO` sur une protection complète | `invalid_critical_placeholder_protection` |
| U-21 | `direction_status = LOST-IN-BUILD` | `invalid_accepted_lost_in_build` |
| U-22 | `risk` supprimé | `invalid_lite_missing_minimum` |
| U-23 | ancre `not_transformed`, verdict accepté | `invalid_direction_untransformed_anchor` |

**Résultat : 23/23**, chaque base valide et chaque faute rejetée pour son motif. C'est la condition de sortie 11.02 §6.4 : **chaque mutation seule suffit à produire son message.** Le sondage de 11.02 §2.2 avait trouvé que 8 fixtures sur 10 restaient invalides pour une autre raison. Il est ici remplacé par une preuve exhaustive, invariant par invariant.

**Hors liste, déclarés (compte fait par script).** `check_semantic_contract` émet 31 diagnostics. **Environ quatorze** n'étaient couverts par **aucun** négatif :
- champs manquants de la protection critique, et `failure_action` hors des trois valeurs ;
- champs de la direction et `anti_direction` ;
- ancres absentes, non structurées ou incomplètes ;
- `profile_decision` non objet ;
- `trace_locator` en STANDARD et SYSTÈME ;
- champs de la provenance ;
- correspondance `artifact_locator` / `artifact.locator` ;
- recouvrement `observed` / `not_verified` ;
- DIRECTION clôturée sans `decision_change` ;
- ancre `transformed` sous un verdict de retour.

A2 ne vise que les invariants **déjà couverts** par un négatif (§4.2-1). Ces diagnostics n'ont donc pas de cas unitaire ici. Ce n'est pas une régression : ils étaient déjà sans preuve dans B01.

**Proposition, non décidée.** En 12.04, la migration ajoute de toute façon un cas par invariant **nouveau**. J'y propose aussi un cas pour chacun de ces invariants existants **conservés** par la liste close. Le coût est d'environ une ligne par invariant. L'ancre `transformed` sous un retour en est exclue, puisqu'elle sera **retirée** (B2, F-RC-001). Sans votre accord, je ne l'ajoute pas.

**Règle pour la suite (11.02 §4.2-4) :** tout invariant ajouté en migration (12.04) arrive avec son cas dans `UNIT_CASES`. L'orpheline montre au passage que la découverte fonctionne.

La suite imprime :
- `+ fixtures déclarées : 25/25` ;
- `+ cas unitaires : 23/23`, qui est le contrat testé par A2-05.

### 2.3 Orchestrateur avec motif (F-ALL-001)

`expect_failure(command, label, expected_message)` : le motif est un **paramètre obligatoire**. Un échec pour un autre motif fait échouer l'orchestrateur, avec « a échoué pour un autre motif ». Le contrôle « pas de trace Python » est conservé.

| Usage | Motif déclaré |
|---|---|
| Locator inconnu | `locator inconnu : DIRECTION/UNKNOWN` |
| 4 fixtures | Leurs motifs de la table |
| Placeholder strict | `strict : placeholder` |
| JSON malformé | `lecture JSON impossible` |
| Fichier absent | `lecture JSON impossible` |

**Limite déclarée.** « JSON malformé » et « fichier absent » partagent un motif : c'est le diagnostic de lecture du validateur. Des motifs plus fins existent (`Expecting value`, `No such file`), mais ce sont des messages de Python et du système, pas du validateur. C4 demande des sous-chaînes **stables des diagnostics existants**. Les deux scénarios restent distingués par leur entrée, préparée par l'orchestrateur lui-même.

## 3. Validation

| Contrôle | Résultat | Attendu (11.02 §6) |
|---|---|---|
| `A2_harnais_non_regression.py` | Témoins **2/2** ; tests A2 **5/5** | 2/2 et 5/5 |
| `A1_harnais_non_regression.py` | **4/4 et 11/11** | Pas de régression d'A1 |
| `validate_all.py` (copie de B03) | **FULL VALIDATION PASSED** ; 8 échecs attendus, tous pour leur motif, dans chaque distribution construite | Vert |
| Verdicts ciblés (25 fixtures, exemple, 3 contrats) | **29/29 identiques à B01** | C3 |
| Suivi (`--compare` avec 12.01) | Témoins **40/40** ; cas **19/300** (+5, tous A2) ; **aucune alerte** | Rouges décroissants |
| B01 | 218/218 ; aucun fichier généré dans B01 ni dans B03 | Intacte |

### 3.1 Vérifications complémentaires

Il s'agit de sept mutations, hors harnais, chacune exigeant son motif. **Résultat sur B03 : 7/7.**

| # | Mutation | B03 |
|---|---|---|
| Y-1 | **Code** : invariant LOST-IN-BUILD retiré | « cas unitaire U-21 : faute unique acceptée » |
| Y-2 | **Code** : invariant « limitation non vide » retiré | « cas unitaire U-14 : faute unique acceptée » |
| Y-3 | **Code** : diagnostic HELD retiré (le schéma rejette encore, pour un autre motif) | « cas unitaire U-01 : attendu … obtenu … » |
| Y-4 | Table : négatif sans motif | « oracle sans motif » |
| Y-5 | Fichier : fixture déclarée supprimée | « fixture déclarée absente » |
| Y-6 | Base de cas unitaire rendue invalide | « cas unitaire U-03 : base invalide » |
| Y-7 | Orchestrateur : message de `read_route` changé | « a échoué pour un autre motif » |

**Ce que montre la comparaison avec B01.** Y-1 à Y-3 sont aussi rouges sur B01, mais **via les fixtures composites**, dont le message ne nomme pas l'invariant perdu. Sur B03, **le cas unitaire nomme exactement la règle retirée.** C'est le gain d'A2 : la localisation.

Y-4 à Y-6 n'ont pas d'équivalent dans B01, qui n'avait ni table ni cas unitaires. Y-7 correspond à A2-04, déjà rouge sur B01.

## 4. Réévaluation des fiches (§22)

| Fiche | Avant (B01) | Après (B03 à 12.02) |
|---|---|---|
| F-FIX-003 (négatif sans motif) | Suite verte avec une fixture réparée de sa faute | **Levée** (A2-01, Y-4) |
| F-FIX-001 (orpheline, fichiers non déclarés) | 24/25 exécutées ; fichier nouveau ignoré | **Levée** (A2-02, A2-03, Y-5) |
| F-FIX-002 (négatifs composites) | Aucune preuve qu'un invariant agit seul | **Levée** : 23 cas à faute unique (A2-05, Y-1 à Y-3) ; les 22 composites sont conservés comme scénarios nommés |
| F-ALL-001 (orchestrateur sans motif) | Échec pour n'importe quel motif accepté | **Levée** (A2-04, Y-7) |

## 5. Suite de la phase 12

- **Grappe A appliquée.** L'instrument a maintenant un schéma dont l'autorité est vérifiée (A1) et des oracles qui vérifient les motifs (A2). Toute la migration (12.04) s'y appuiera.
- **R-6 (12.01 §4.1)** reste en attente de votre objection éventuelle. Sans objection, elle s'applique en 12.04.
- **Journal des notes de version (B03), ligne ajoutée :**
  > 12.02 — La suite RUN_CARD déclare chaque fixture avec son motif attendu, refuse une fixture non déclarée et exécute un cas unitaire à faute unique par invariant ; l'orchestrateur exige le motif de chaque échec attendu.

## 6. Sortie

- **PATCH A2 appliqué à B03.**
  - 4 fiches levées côté machine.
  - Harnais A2 à 5/5, A1 toujours à 11/11.
  - Suite intégrée verte ; verdicts inchangés.
- Rouges restants : **281/300**.
- B01 intacte (218/218). B02 non touchée.

**§32.**
- **Ce qui a été utile :** l'écart de charge est déclaré plutôt que masqué. Les trois invariants sans négatif sont nommés : ils n'étaient visibles qu'en écrivant la table.
- **Ce qui aurait pu être évité :** relever les motifs réels, fixture par fixture, aurait pu se faire en 11.02. Cela aurait donné une estimation de charge plus juste.

**Prochaine unité : 12.03, cycle de garde.** Elle est écrite **avant** les textes, conformément à 11.23 §6 et §7 :
- C4 O-1 et O-2 dans un seul diff : résolveur en trois étapes dans `read_route.py`, et validateur de carte qui l'importe ;
- E2 O-5 : lecteur conscient des blocs de code ;
- la table LCF (21 entrées) dans `validate_reading_map.py`, écrite **rouge**, sauf LCF-20 ;
- D4 O-1 : `SEED` exigé par `validate_design_governance.py`, écrit **rouge**.

**Première unité à produire des rouges voulus.** À partir de 12.03, `validate_all.py` sera rouge par construction sur la LCF et `SEED`. Le suivi devra montrer que **seuls** ces cas-là sont rouges.

**Charge.** C'est une unité **moyenne à lourde** : 21 conditions LCF, chacune avec sa mutation rouge. Si elle dépasse une unité raisonnable, je la découperai en 12.03a (résolveur et carte) et 12.03b (LCF et `SEED`), en le déclarant.
