# DG-AUDIT-001 — Phase 12.01 — PATCH A1 : autorité du schéma

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée.

**Décision de l'owner :** « Oui, enchaîne avec 12.01 ».

**Décision appliquée :** 11.01, PATCH-DECISION A1. Elle couvre cinq fiches :
- F-VRC-007 et F-VCT-001 (Majeur) ;
- F-VRC-008 ;
- F-VRC-006 ;
- F-VCT-003, rattachée à A1.

**Sorties :**
- le commit B03 `33db0da`, étiqueté `12.01-A1` ;
- `DG_AUDIT_001_B03_12-01_A1.diff`, le diff brut ;
- `DG_AUDIT_001_B03_12-01_A1_lecture_w.diff`, le même diff sans les changements d'indentation, pour la lecture ;
- ce rapport (`PATCH + DIFF-REASONING`) ;
- `A1_verifications_complementaires_12-01.py` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-01.json` ;
- `DG_AUDIT_001_B03_package_12-01.zip`, l'archive de B03 à cet état.

---

## 1. Fichiers touchés

| Fichier | Lignes (diff sans espaces) | Diff brut |
|---|---|---|
| `scripts/validate_run_card.py` | +44 / −13 | +200 / −169 |
| `scripts/validate_contracts.py` | +56 / −3 | +56 / −3 |

**Pourquoi le diff brut de `validate_run_card.py` est gros.** La suite intégrée était placée sous `if schema:`. Or le chargement gouverné garantit désormais un schéma opérant, donc cette condition n'avait plus de sens. Je l'ai retirée, et le bloc des 24 appels a perdu un niveau d'indentation. **Aucun de ces appels n'a changé.** Le diff `-w` le montre : il ne garde que les 57 lignes réelles.

J'ai écarté une variante qui gardait l'indentation derrière une condition toujours vraie. Elle aurait rendu le diff plus court, mais elle aurait laissé dans le code une fausse condition.

**Respect des conditions de 11.01 :**
- **C2** : aucun fichier ajouté ; manifestes 60/56 inchangés.
- **C4** : bibliothèque standard seulement.
- **C5** : deux scripts, environ 50 lignes réelles chacun, dans la fourchette annoncée de 40 à 60.

## 2. Raisonnement de diff

### 2.1 `validate_run_card.py`

| Changement | Décision appliquée | Effet |
|---|---|---|
| `load_schema()` | 11.01 §4.1-1 | Trois refus gouvernés : « schéma absent » ; « schéma inopérant » (racine vide ou non objet) ; « schéma incomplet » (`properties.run_card.properties.mode.enum` absent, vide ou non liste). Le chemin est suivi avec des contrôles de type, jamais par indexation directe : **plus aucune trace Python** possible sur ces cas |
| `check_schema_witness()` | 11.01 §4.1-2 | L'exemple canonique, avec le mode `SCHEMA-WITNESS-INVALID-MODE`, doit être rejeté par `validate_node` **seul**. Si l'exemple est accepté : « le schéma n'impose pas l'enum de mode ». S'il est rejeté pour un **autre** motif que `run_card.mode` : « témoin de schéma non concluant » (règle de motif A2, appliquée dès maintenant) |
| `main()` | 11.01 §4.1-3 | Schéma et témoin **avant toute branche**. Une demande ciblée va directement à `validate_single_path` et ne retombe jamais sur la suite. Les messages de succès (suite et ciblé) sont inchangés |
| `check_schema_authority` | Conservé (§4.1-2) | Le test **positif** (un enum modifié change le résultat) reste appelé en fin de suite. Le témoin le complète dans le sens **négatif** |

**Condition C1 (pas de nouvelle autorité), vérifiée.** Le chargement ne contrôle que le chemin `…mode.enum`, que `check_schema_authority` déréférençait déjà. Le témoin n'emploie que l'exemple canonique, déjà lu par la suite et par le profil strict. Aucune valeur d'enum n'est recopiée dans le code.

### 2.2 `validate_contracts.py`

| Changement | Décision appliquée | Effet |
|---|---|---|
| `load_schema(name)` | 11.01 §4.2-1 | La racine doit être un objet non vide, déclarer `type: object` et un `required` non vide ; sinon, refus gouverné |
| `check_schema_keywords()` | 11.01 §4.2-1 | Parcours **statique** de `properties` et `items` : tout mot-clé hors du sous-ensemble supporté est refusé, **même dans une branche que l'exemple ne visite pas**. Un sous-schéma non objet est aussi refusé : le code le déréférence déjà comme objet |
| `check_schema_witness()` | 11.01 §4.2-2 et §4.2-3 | Par contrat, l'exemple privé de sa première clé requise doit être rejeté par `validate` seul, avec le motif « champ obligatoire absent: <clé> ». Pour `research_brief`, un voisin avec `depth = "IMPOSSIBLE"` doit être rejeté avec le motif « $.depth: valeur non canonique » (F-VCT-003) |
| Suite et validation ciblée | 11.01 §4.2 | Les deux chemins passent par `load_schema`. Une variable devenue inutile (`schema_path`) est retirée de la boucle |

**Hors périmètre, respecté.** Le CLI des contrats, qui refuse un fichier non canonique (F-ACT-008), est inchangé : il relève de C9. Les traces Python sur UTF-8 invalide ou sur un schéma `[]` relèvent d'E2 (O-6). Une racine `[]` est cependant déjà refusée ici, par la règle « objet non vide ».

## 3. Validation

| Contrôle | Résultat | Attendu (11.01 §6) |
|---|---|---|
| `A1_harnais_non_regression.py` sur B03 | Témoins **4/4** ; tests A1 **11/11** ; chaque échec est gouverné, sans trace | 4/4 et 11/11 |
| `validate_all.py` (copie de B03) | **FULL VALIDATION PASSED**, archives reproductibles | Vert |
| Verdicts ciblés : 25 fixtures, exemple RUN_CARD, 3 exemples de contrats | **29/29 identiques à B01** (même code de retour) | Inchangés |
| Diff | Deux scripts seulement | C5 |
| Suivi des harnais (`--compare` avec 12.00) | Témoins **40/40** ; cas **14/300** (+11, tous A1) ; **aucune alerte**, aucun autre harnais en recul | Rouges décroissants |
| B01 | 218/218 ; aucun fichier généré ni dans B01 ni dans B03 | Intacte |

### 3.1 Vérifications complémentaires

Le harnais A1 date d'avant la règle A2 : il ne vérifie pas les **motifs** des échecs. Et ses cas A1-05 et A1-06 (enum retiré du schéma) sont désormais arrêtés par le **chargement**, pas par le **témoin**. **Le témoin n'était donc exercé par aucun cas.**

J'ai ajouté sept mutations, hors harnais : le harnais n'est pas modifié (règle de 11.23). Chacune exige un échec gouverné **et** son motif.

| # | Mutation | B03 | B01 |
|---|---|---|---|
| X-1 | **Code** : contrôle d'enum retiré de `validate_node` (la mutation de phase 2 pour F-VRC-006), suite | Rouge, « le schéma n'impose pas l'enum de mode » | Rouge pour un autre motif (fixture) |
| X-2 | Idem, exemple ciblé | Rouge, même motif | **PASS** |
| X-3 | Schéma : enum `mode` transformé en chaîne | Rouge, « schéma incomplet » | Rouge pour un autre motif |
| X-4 | Code des contrats : contrôle d'enum retiré | Rouge, « n'impose pas l'enum de depth » | **PASS** |
| X-5 | Code des contrats : contrôle `required` retiré | Rouge, « n'impose pas la clé requise » | **PASS** |
| X-6 | `required` racine vidé, validation ciblée | Rouge, « schéma incomplet » | **PASS** |
| X-7 | Sous-schéma non objet | Rouge, « sous-schéma non objet » | **PASS** |

**B03 : 7/7.** Sur B01, cinq mutations sur sept donnent un faux PASS. **Le témoin négatif est donc la seule barrière contre la mutation d'origine de F-VRC-006, qui porte sur le code** (X-1, X-2). Le chargement seul ne l'aurait pas arrêtée.

## 4. Deux points à déclarer

### 4.1 Conflit A1 × C2 sur la racine de `production_contracts` (certain, à régler avant 12.04)

- **A1 (11.01 §4.2)** refuse un schéma de contrat dont le `required` racine est vide. Son témoin retire la **première clé requise**.
- **C2 (11.09, tableau de migration)** **vide** précisément ce `required` racine de `production_contracts`. La raison est que zéro contrat structuré doit rester valide (C2 C4). L'exigence « au moins un » passe dans le validateur (INV-C2-2).
- **Conséquence :** appliquée telle quelle en 12.04, la migration C2 serait refusée par A1, avec le message « schéma incomplet ».
- **Ce qui a manqué :** ni C2, ni C9, ni la clôture 11.23 n'ont vu ce conflit. Il est apparu à l'écriture du code.

**Rectification proposée (R-6), à appliquer dans le diff de 12.04.** Elle change la règle d'A1, pas son objectif, qui est de refuser un schéma inopérant. Elle a deux volets :
1. **Racine.** Un `required` racine non vide est exigé **sauf** pour un contrat dont le validateur déclare une règle « au moins un » (INV-C2-2). Dans ce cas, la racine doit porter des `properties` typées et `additionalProperties: false`.
2. **Témoin.** Quand `required` est vide, le témoin remplace la **première propriété** de l'exemple par une valeur de type incompatible. Elle doit être rejetée par `validate` seul, avec le motif « type attendu ».

**Ce qui ne change pas avec R-6 :** les cas A1-07 à A1-11 et X-1 à X-7 gardent leur verdict. Je le vérifierai en 12.04. **Sans objection de votre part, R-6 sera appliquée dans la migration.**

### 4.2 Documentation (C6) reportée à 12.06

Il y a une tension entre deux textes de 11.01 :
- **C6** demande une ligne dans les notes de version du prochain lot publié ;
- **§6.4** limite le diff d'A1 aux **deux scripts**.

Les deux se concilient ainsi : la ligne est inscrite **dès maintenant** au journal des notes de version ci-dessous, et elle sera écrite dans `RELEASE_NOTES.md` à l'étape 12.06, avec la version. Pas d'entrée CHANGELOG : C6 l'exclut.

> **Journal des notes de version (B03).**
> 12.01 — Les validateurs RUN_CARD et contrats refusent un schéma absent, vide, incomplet ou hors sous-ensemble. Ils vérifient, avant tout succès, qu'un témoin invalide est rejeté par le schéma.

## 5. Réévaluation des fiches (§22)

| Fiche | Avant (B01) | Après (B03 à 12.01) |
|---|---|---|
| F-VRC-007 (schéma `{}` → PASS) | Faux PASS, y compris sur une carte invalide ciblée | **Levée** (A1-01, A1-02) |
| F-VRC-008 (schéma absent ou incomplet → trace) | Trace Python | **Levée** (A1-03, A1-04) |
| F-VRC-006 (enum non gouverné) | Suite verte sans enum, dans le schéma comme dans le code | **Levée** (A1-05, A1-06, X-1 à X-3) |
| F-VCT-001 (schémas de contrats `{}`, branche non visitée) | Faux PASS | **Levée** (A1-07 à A1-10, X-7) |
| F-VCT-003 (enum `depth`) | Faux PASS | **Levée** (A1-11, X-4) |

**Statut :** « levée » vaut pour le **contrat machine**, vérifié sur B03. L'acceptation au sens de 11.01 §6 relève de la phase 13, qui rejouera tous les harnais sur la candidate finale.

## 6. Sortie

- **PATCH A1 appliqué à B03.**
  - 5 fiches levées côté machine.
  - Harnais A1 à 11/11, aucun recul ailleurs, suite intégrée verte.
  - Verdicts des 29 documents inchangés.
- **À décider ou à confirmer :** R-6 (§4.1), sinon elle s'applique en 12.04.
- B01 intacte (218/218). B02 non touchée.

**§32.** L'application a trouvé ce que la décision n'avait pas vu :
1. **Le conflit A1 × C2.** Écrire le code a obligé à confronter deux décisions qui ne se citaient pas.
2. **Un trou de preuve dans le harnais A1.** Aucun cas n'exerçait le témoin négatif. X-1 et X-2 le comblent, sans toucher au harnais.

**Prochaine unité : 12.02 A2.** Elle modifie `validate_run_card.py` et `validate_all.py` :
- table déclarative des fixtures, avec un motif obligatoire pour tout négatif ;
- cas unitaires à faute unique ;
- motif attendu dans `expect_failure`.

Sortie attendue : harnais A2 à 5/5, et A1 toujours à 11/11.
