# DG-AUDIT-001 — Phase 11.02 — PATCH-DECISION A2 : oracles de test

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée (`016e6002…` revérifié après les essais). B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.02 ».

**Grappe :**
- F-FIX-002 (fixtures négatives composites) ;
- F-FIX-003 (négatif sans message attendu) ;
- F-ALL-001 (orchestrateur sans motif) ;
- F-FIX-001, fixture orpheline, rattachée ici (voir §4).

**Sorties :**
- cette `PATCH-DECISION` ;
- `A2_harnais_non_regression.py`, la preuve écrite avant toute modification.

Aucun patch et aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan et décision précédente | Plan maître ; 11.01 (A1) |
| Empreintes | B01 `016e6002…` conforme avant et après les essais (toujours sur copie temporaire) |
| Protocole | §21, §22, §32 |
| Sources de niveau 5 | Rapports Fixtures 01–03 et checkpoint Fixtures ; Validate_RUN_CARD 03 ; Validate_ALL 01 ; 4.04 ; 5.03 |
| Code relu | `validate_run_card.py` 337–356 (`check_fixture`) et 421–576 (la suite : 24 appels écrits un par un) ; `validate_all.py` en entier |

## 2. Re-vérification

### 2.1 Harnais A2 sur B01 : témoins 2/2, tests A2 0/5

| Test | Mutation | Attendu après correction | B01 aujourd'hui |
|---|---|---|---|
| T-POS-1 | aucune | suite RUN_CARD verte | vert |
| T-POS-2 | aucune | `validate_all` complet vert (build et reproductibilité) | vert |
| A2-01 (F-FIX-003) | `invalid_missing_proof` réparée de sa faute, mais `mode` invalide | suite rouge | **vert** : la suite accepte n'importe quelle erreur |
| A2-02 (F-FIX-001) | fixture orpheline rendue **valide** | suite rouge | **vert** : la suite native ne l'exécute pas |
| A2-03 (F-FIX-001) | nouveau fichier de fixture non déclaré | suite rouge | **vert** : ignoré |
| A2-04 (F-ALL-001) | `expect_failure` appelé sur une carte qui échoue pour un **autre** motif | motif refusé | **accepté** : la fonction ne prend même pas de motif attendu |
| A2-05 (F-FIX-002) | la suite doit exécuter des cas à faute unique | ligne « + cas unitaires : N/N », N ≥ 20 | absente |

### 2.2 F-FIX-002 : un sondage ajouté

La phase 2 a compté 17 négatifs composites sur 22, en réparant chacun à la main. J'ai re-vérifié sur un échantillon : **10 fixtures, réparées de leur seule faute nommée.**

- **2 deviennent valides** (faute unique) : `accepted_without_limitations` et `capability_available_without_basis`.
- **8 restent invalides pour une autre raison.** Le plus souvent, c'est la provenance manquante, qui masque la règle testée ; ailleurs, l'objet DIRECTION, l'ancrage, `owner` placeholder ou `sources`.

C'est cohérent avec la phase 2. **Pourquoi c'est le point central de la phase 12 :** quand un correctif de B2 ajoutera un invariant (D-ACT-1 = c), il faudra montrer qu'une carte **valide par ailleurs** est rejetée pour cette seule raison. Aujourd'hui, la suite ne le permet pas.

### 2.3 Deux remarques, sans nouvel ID

- **Le premier diagnostic masque parfois la faute nommée.** `invalid_missing_proof` échoue sur « un verdict accepté exige au moins une preuve observed » (contrôle sémantique), jamais sur le `required: proof` du schéma : le contrôle sémantique passe avant le schéma (`validate_card`). Le message à déclarer pour cette fixture devra le refléter en phase 12.
- **L'orchestrateur rapporte ses propres échecs par une trace Python.** Quand un sous-validateur échoue, `validate_all` lève `CalledProcessError`. Le code reste non nul, donc la CI reste rouge. Cela relève de la robustesse des diagnostics (lot E2) ; je le note, sans créer d'ID.

**Erreur corrigée en cours d'unité.** Ma première version du harnais retirait le script de build pour tester `validate_all` en « mode Local ». Or le package GitHub **exige** ce script dans son inventaire : le témoin échouait à cause de ma préparation, pas à cause de B01. Le témoin T-POS-2 lance désormais `validate_all` complet ; il est vert sur B01.

## 3. Les sept questions du §21

| Question | Réponse |
|---|---|
| Le défaut change-t-il une preuve ou la maintenance ? | **Oui.** Les phases 12–13 doivent prouver que chaque correctif agit **seul**. Avec des négatifs composites et des oracles sans motif, un correctif peut être « vert » sans rien démontrer |
| Le fichier possède-t-il le défaut ? | **Oui**, re-vérifié (§2) |
| Le gain dépasse-t-il la charge ? | **Oui, et la charge est négative.** La suite actuelle fait environ 155 lignes d'appels un par un. Une table déclarative plus des mutations en mémoire la ramènent à environ 90–100 lignes, avec plus de couverture |
| Nouvelle autorité ? | **Non.** Les messages attendus sont ceux que le validateur émet déjà. Aucune règle métier n'est ajoutée |
| Testable ? | **Oui** : harnais A2 (2 témoins + 5 tests) |
| Positif et défensif équilibrés ? | Oui. Les positifs gagnent un témoin systématique (la base valide de chaque mutation est validée d'abord) |
| Suppression ou fusion plutôt qu'ajout ? | **Oui, en partie.** On remplace 24 appels écrits un par un par une table, et on fusionne la déclaration de la fixture orpheline dans la même table. On ne réécrit pas les 22 fichiers de fixtures (voir 4.2) |

## 4. PATCH-DECISION

**Décision : CORRIGER.** Types §21 : **test** et **simplification**.

**Propriétaire :** le mainteneur du package (`validate_run_card.py`, `validate_all.py`). Aucune source normative n'est touchée ; aucun fichier de fixture n'est ajouté ni supprimé.

### 4.1 Table déclarative des fixtures (F-FIX-001, F-FIX-003)

1. Les 24 appels de la suite native sont remplacés par **une table** : `nom de fichier → valide | invalide, message attendu`.
2. **Tout négatif doit déclarer un message attendu.** Un négatif sans message fait échouer la suite (« oracle sans motif »). C'est ce qui corrige F-FIX-003.
3. **Découverte :** la suite liste `schemas/fixtures/`.
   - Un fichier présent mais absent de la table fait échouer la suite (« fixture non déclarée »).
   - Une entrée de table sans fichier fait aussi échouer la suite.
4. **F-FIX-001 rattachée :** la fixture orpheline entre dans la table, avec son message (`capability_profile exige basis non vide…`). Cela ne vaut pas un cycle séparé (§32) ; le registre est mis à jour (A2 : 4 fiches, E2 : 18).

### 4.2 Cas unitaires à faute unique, en mémoire (F-FIX-002)

1. Chaque **invariant** aujourd'hui couvert par un négatif reçoit un **cas unitaire** : une base valide (l'exemple canonique ou une fixture `valid_*` adaptée au mode), **une** mutation, et le message attendu. La base est d'abord validée (témoin positif), puis la mutation doit être rejetée avec ce message.
2. **Les 22 fichiers négatifs existants sont conservés**, déclarés comme **tests composites nommés** (scénarios d'interaction), comme la phase 2 le recommandait. On ne les réécrit pas : cela coûterait 22 fichiers modifiés et laisserait les manifestes intacts, mais n'apporterait rien de plus que les cas unitaires.
3. La suite imprime **« + cas unitaires : N/N »** (contrat testé par A2-05).
4. **Règle pour les phases suivantes :** tout invariant ajouté au validateur, notamment en B2, arrive avec son cas unitaire. C'est le motif que la phase 12 devra suivre.

### 4.3 Orchestrateur avec motif (F-ALL-001)

1. `expect_failure` reçoit un **motif attendu** : une sous-chaîne du diagnostic.
2. Ses huit usages le déclarent : quatre fixtures, locator inconnu, placeholder strict, JSON malformé, fichier absent.
3. Un échec pour un autre motif fait échouer l'orchestrateur. Le contrôle « pas de traceback » est conservé.

### 4.4 Hors périmètre

| Point | Où |
|---|---|
| Autorité du schéma (schéma vide, enum) | A1, décidée en 11.01 |
| Trace Python de l'orchestrateur quand un sous-validateur échoue (§2.3) | E2 (robustesse) |
| Contenu des invariants eux-mêmes (ce que la RUN_CARD doit refuser) | B1–B3, sous D-ACT-1 = c |

## 5. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Ordre : A1 d'abord, puis A2**, en deux diffs distincts sur `validate_run_card.py`. A2 s'appuie sur le témoin de schéma d'A1 |
| C2 | Aucun fichier ajouté ni supprimé : les manifestes 60/56 restent inchangés |
| C3 | Les 25 fixtures gardent leur verdict (valide ou rejetée) ; seuls les motifs deviennent obligatoires |
| C4 | Les messages attendus sont des sous-chaînes stables des diagnostics existants ; un message de diagnostic n'est pas réécrit pour faciliter un test |
| C5 | Bibliothèque standard seulement |
| C6 | Diff lisible : table et mutations regroupées, sans refactorisation hors suite |

## 6. Condition de sortie

Le correctif A2 sera accepté en phase 13 si :
1. `A2_harnais_non_regression.py` donne **2/2 témoins et 5/5 tests** ;
2. `A1_harnais_non_regression.py` reste à **4/4 et 11/11** (pas de régression d'A1) ;
3. `validate_all.py` rend `FULL VALIDATION PASSED`, avec des archives reproductibles ;
4. le sondage du §2.2, rejoué sur les cas unitaires, montre que **chaque** mutation seule suffit à produire son message.

## 7. Sortie

- **PATCH-DECISION A2 : CORRIGER** (test, simplification), sous les conditions C1 à C6.
- **Grappe A : A1 et A2 décidées.** L'instrument de validation a une spécification complète et deux harnais de preuve.
- Registre : F-FIX-001 rattachée à A2 ; les totaux par gravité ne changent pas.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- une correction qui **réduit** le code de la suite tout en augmentant sa couverture ;
- une règle posée pour la suite (un invariant, un cas unitaire) ;
- une fiche mineure rattachée ;
- une erreur de mon propre harnais détectée par son témoin et corrigée ;
- deux remarques transmises au bon lot, sans nouvel ID.

**Prochaine unité : 11.03 PATCH-DECISION B1** (protection critique et exception : F-DIR-007, F-DIR-016, F-ACT-017, F-ACT-038, F-ACT-039, F-QS-003). C'est la première grappe normative, avec 3 Majeur. Elle sera traitée sous D-ACT-1 = c : il faudra dire ce qui devient invariant machine et ce qui reste au texte.
