# DG-AUDIT-001 — Phase 11.23 — Clôture de la phase 11 : lot F, inventaires finaux, ordre de la phase 12, examen de conformité

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.23 ».

**Objet.** Cette unité ne décide aucune grappe nouvelle. Elle fait quatre choses :
1. traiter le **lot F** : 9 observations, plus celles versées en cours de route ;
2. produire les **inventaires finaux**, tous recalculés par script sur les fichiers (règle de 10.05) ;
3. fixer l'**ordre de la phase 12** ;
4. passer l'**examen de conformité** qui autorise ou non la phase 12.

**Sorties :**
- ce rapport ;
- `DG_AUDIT_001_Suivi_harnais.py`, outil de pilotage des phases 12 et 13 (§4.5) ;
- `DG_AUDIT_001_Instantane_harnais_B01.json`, l'instantané de référence ;
- le plan maître mis à jour.

Aucun patch, aucun verdict global.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` **218/218** ; aucun `__pycache__`, `dist`, `.build` ni ZIP sous `02_Sources_B01` |
| Sources relues | Les 22 PATCH-DECISION (11.01 à 11.22), leurs tableaux §21, leurs conditions de phase 12 et leurs sorties ; registre consolidé (158 fiches) ; décisions de l'owner (11.00) ; liste close ; LCF ; protocole §21, §22, §23, §32 |
| Recalcul | Couverture, gravités, listes et harnais recalculés par script. Aucun total n'est recopié d'un rapport |
| Harnais | Les **22** harnais ont été relancés sur B01. Chaque résultat est **identique** à celui que son rapport consignait |

## 2. Couverture de la phase 11

### 2.1 Toutes les fiches ont une décision

| Lot | Fiches | Majeur | Significatif | Mineur | Observation | Décision |
|---|---|---|---|---|---|---|
| A (instrument) | 9 | 2 | 5 | 2 | — | A1, A2 : CORRIGER |
| B (acceptation) | 23 | 12 | 11 | — | — | B1 à B5 : CORRIGER |
| C (formes, accès, façades) | 59 | — | 58 | 1 | — | C1 à C9 : CORRIGER |
| D (jugement, boucle, autorité, cycle de vie) | 13 | — | 13 | — | — | D1 à D4 : CORRIGER |
| E (lots éditorial et technique) | 45 | — | — | 45 | — | E1, E2 : CORRIGER (lot) |
| F (observations) | 9 | — | — | — | 9 | Pas de patch (§3) |
| **Total** | **158** | **14** | **87** | **48** | **9** | **22 PATCH-DECISION** |

- **Contrôle de citation :** chacune des 149 fiches des lots A à E est citée dans le rapport de **sa** grappe. **Aucun manquant.**
- **Les gravités sont celles que l'owner a arbitrées en 11.00.** Aucune gravité n'a été modifiée pendant la phase 11.

### 2.2 Décisions de l'owner portées par la phase 11

| Décision | Effet vérifié |
|---|---|
| D-ACT-1 = c (mixte) | Liste close : 82 invariants actifs, le reste « forme seule » déclaré dans la promesse du validateur |
| D-FAC-1 = c (façades bornées et testées) | LCF : 21 conditions, portées par le validateur « carte et façades » |
| Ordre E2 avant E1 (11.20) | Appliqué : 11.21 E2, puis 11.22 E1 |

## 3. Lot F — observations sans patch

### 3.1 Les 9 observations du registre

Pour chaque fiche, j'ai vérifié deux choses :
- aucune PATCH-DECISION ne l'a traitée ni rendue caduque ;
- son test futur reste exécutable après les patchs prévus.

| Fiche | Statut en fin de phase 11 | Interaction avec la phase 11 | Test futur : quand |
|---|---|---|---|
| F-ACT-035 (PASS ciblé ≠ claim WCAG) | **Maintenue** | D3 a relu Gate A et corrige ACTION 677 (F-ACT-033). Le résumé de conformité n'est pas touché | Au premier run qui publie un claim d'accessibilité |
| F-DIR-004 (portée web/natif ; corpus plus large) | **Maintenue** | D4 T-4 réécrit DIRECTION 74 (efficacité) **sans changer la portée**. La phase 12 ne doit pas élargir la portée implicitement | Au premier run hors web |
| F-DIR-017 (checkpoint pré-build invisible dans la vue externe) | **Maintenue** | **C5 T-2 réordonne RUN-PRIORITY (285–295), dans la même zone.** Il n'ajoute ni ne retire de checkpoint | Test agent externe avec et sans autonomie, **joué sur le texte patché** |
| F-DIR-022 (SELF-ASSESSED sans interdictions explicites) | **Maintenue** | Aucune | Claim réglementaire, conseil santé, droit d'asset |
| F-DIR-038 (contrôles web/mobile apparemment universels) | **Maintenue** | Aucune. F-BIB-003 (E1) conditionne déjà les familles MOBILE-* au scope | Au premier run hors web, avec F-DIR-004 |
| F-DIR-044 (catégories de lecture non exclusives) | **Maintenue ; prérequis de la phase 13** | Aucune | **Avant** de concevoir les pilotes de phase 13 : une taxonomie orthogonale (phase, motif, fait), sinon les mesures de lecture (C4 : ≤ 60 lignes) seront doublement comptées |
| F-OM-002 (« un axe à la fois ») | **Maintenue** | C5 modifie ORCHESTRATION_MAP 17, 20, 21, 23, **pas 31** | Comparaison de sorties, brief DIRECTION ouvert à deux publics |
| F-SAV-008 (CONTEXT peut exclure une motion narrative) | **Maintenue** | Aucune décision ne touche CONTEXT 736–740 ; E1 (F-SAV-001) le nomme seulement dans une liste | Au premier run avec motion ou scène spatiale |
| F-VDG-003 (`state:` minuscule accepté) | **Maintenue. Test préalable exécuté (§3.2)** | Aucune | Voir §3.2 |

### 3.2 F-VDG-003 : le test préalable, exécuté

Le test que la fiche exigeait avant toute correction était : « rechercher `state:` dans les sources ». Je l'ai exécuté sur B01.

- **Résultat certain :** une seule occurrence, `skills/…/references/machine_projection.md` 82 (`state: CLOSED`). C'est une **clé YAML** de la projection machine, avec une **valeur canonique**.
- **Conséquence :** la condition posée par la fiche est remplie : la forme minuscule **est** une représentation active, comme clé de la projection machine. Mais sa valeur est correcte : **aucun défaut n'est constaté** (§21, question 1).
- **Coût d'un correctif, mesuré :** j'ai rejoué en mémoire une variante de `check_structured_values` **insensible à la casse** sur B01. Elle lit 11 lignes, toutes canoniques (`issue: null` compris : `null` figure dans `ISSUE_VALUES`). Elle ne produit **aucun faux échec**. Le correctif tiendrait donc en un drapeau.
- **Décision de clôture :** **observation maintenue**, parce qu'aucune valeur non canonique n'est constatée. Le YAML est déjà versé à la migration unique (C6, F-MP-001) et sera aligné sur l'exemple canonique en phase 12.
- **Ce que ce test ne décide pas :** fermer la fiche par ce correctif demanderait une PATCH-DECISION, qu'une clôture ne prend pas. Si l'owner le veut, le correctif entrerait dans le cycle d'outil final (§7, étape 6) sans autre effet.
- **Incident déclaré :** le rejeu a importé le validateur depuis B01, ce qui a créé un `__pycache__` sous `scripts/`. Il a été supprimé aussitôt. Le dossier n'est pas dans `SHA256SUMS`, et les empreintes restent à 218/218. Les rejeux suivants doivent passer par une copie.

### 3.3 Observations versées en cours de phase 11

| ID | Origine | Observation | Décision |
|---|---|---|---|
| **OBS-F-1** | C3 (11.10), traitée en C9 (11.16) | `creative_direction_set.directions.maxItems = 3` n'a **aucune source textuelle**. La borne ne force aucune fabrication ; aucune friction observée | Conservée, marquée « sans source ». Test futur : un brief qui justifierait une quatrième direction |
| **OBS-F-2** | C8 (11.15) | Le contrôle des membres garantit **quels** fichiers sont dans l'archive, pas **leur contenu**. Des empreintes de release produites par le build seraient une capacité nouvelle | Proposée, **non décidée**. À reconsidérer si une divergence de contenu est constatée entre `dist` et les sources |

**Lot F clos : 11 observations, aucune ne donne lieu à un patch.** Aucune ne bloque la phase 12. F-DIR-044 est une **condition de conception** de la phase 13.

### 3.4 Ce qui n'est pas du lot F : les limites déclarées

Seize limites ont été déclarées par les grappes (B3, B5, C2, C3, C4, C5, C6, C7, C8, C9 ×2, D1, D2, D3, D4, E2). Ce ne sont pas des observations : ce sont les **bornes de la preuve** que chaque correction pourra apporter. Elles sont transportées **telles quelles** comme réserves de phase 13 et de phase 14.

Leur motif commun est le suivant : une garde textuelle ou machine prouve une **forme**, pas un **effet**. L'effet ne s'établit que par les épreuves (§4.6).

## 4. Inventaires finaux

### 4.1 Liste close D-ACT-1

`DG_AUDIT_001_Liste_close_invariants_RUN_CARD.csv`, recalculée :

| Mesure | Valeur |
|---|---|
| Lignes | **92** : 44 existants, 48 nouveaux |
| Actifs | **82** : 63 sur la RUN_CARD, 19 sur les contrats de production (`validate_contracts`) |
| Inactifs | 10 existants : E02 (remplacé par B2-6), E11 (retiré, F-RC-001), E17 (généralisé par B2-1), E24 (généralisé par C1-3), K01 (remplacé par C9-1), K04 (retiré, E2), K08 (retiré, C3 : quota sans source), K10 et K11 (remplacés par C9-3), K12 (remplacé par C2-4) |
| Nouveaux par grappe | B1 7, B2 10, B3 4, B4 6, C1 6, C2 4, C3 2, C4 2, C9 3, D2 2, E2 2 |

**Règle de phase 12 (A2) :** chaque invariant nouveau arrive avec son cas unitaire à faute unique et son motif.

### 4.2 Liste close des conditions de façade (LCF)

`DG_AUDIT_001_Liste_close_conditions_facade.csv` : **21 entrées**.
- **C5** (12) : LCF-01 à LCF-10, LCF-C1 et LCF-C2.
- **C6** (4) : LCF-11 à LCF-14.
- **D1** (3) : LCF-15 à LCF-17.
- **D4** (2) : LCF-20 et LCF-21.

LCF-20 est une **condition de conservation** : elle est déjà verte sur B01. LCF-09 a été élargie en E1 (point 4 du récapitulatif de protection).

**Règle :** une entrée n'entre que par une PATCH-DECISION, avec sa source propriétaire et sa mutation rouge.

### 4.3 Schémas : migration unique, liste close

| Fichier | Changements | Grappes |
|---|---|---|
| `run_card.schema.json` | `critical_protection.result`, `closure.exception` | B1 |
| | `closure.axes`, `closure.reservations`, `artifact.version`, `artifact.rights_status`, `proof.provenance.capability`, `basis` typée | B2 |
| | `closure.system_package`, `closure.b1b` | B3 |
| | `anchors[].type`, retrait de « au moins un ancrage » (devient INV-B4-6), `direction.identity_stake`, `direction.calibration` | B4 |
| | `decision_change.outcome` et `reason`, `closure.verdict` nullable, `closure.reclassification`, `profile_decision.phase` | C1 |
| | `risk.statement` (transféré de B1) | C2 |
| `production_contracts` | `required` racine vidé (« au moins un » dans le validateur), `expected_scope` et `observed_scope`, `proof_status` et `reason` canoniques | C2 |
| | `structural_changes` : `minItems 1` | C3 |
| `domain_frame` | `policy_profile.risk_coverage` | C9 |
| | `evidence_plan[]` en objets à cinq composantes | E2 |
| `research_brief` | `source_status`, `source_date`, `source_locator`, `rights_status` | C9 |
| | `entries` : `minItems 0`, activation selon `depth` | E2 |

**Aucune nouvelle valeur** de mode, d'état, d'issue ou de verdict (B1 C4, B2 C5).

**Données à migrer dans le même cycle :**
- l'exemple canonique ;
- les fixtures nommées par B1 C3, B2 C4, B3 C3, C1 C3 et C9 C4 ;
- les exemples des trois contrats ;
- le YAML de `machine_projection.md` (C6, F-MP-001).

### 4.4 Outils

| Fichier | Corrections | Étape de phase 12 (§5) |
|---|---|---|
| `validate_run_card.py` | A1 (chargement gouverné, témoin de schéma) | 1 |
| | A2 (table des fixtures, cas unitaires, motifs) | 2 |
| | Invariants de la migration, dont INV-C4-1/C4-2 ; E2 O-12 (hôtes de démonstration, avec INV-C4-2) | 4 |
| | E2 O-9, O-10, O-11 (clés répétées, non UTF-8, pré-passe de types) | 6 |
| `validate_contracts.py` | A1 (chargement gouverné, parcours statique des mots-clés, témoins) | 1 |
| | Invariants C2, C3, C9, E2 ; K02 normalisé ; C9 O-1 et O-2 (CLI `--type`) | 4 |
| | E2 O-6 (non UTF-8) | 6 |
| `validate_all.py` | A2 (motif attendu dans `expect_failure`) | 2 |
| | E2 O-1 (chemins depuis ROOT) | 6 |
| `read_route.py` | C4 O-1 (résolveur en trois étapes), E2 O-5 (blocs de code) | 3 |
| `validate_reading_map.py` | C4 O-2 (importe le résolveur), C5 (table LCF : validateur « carte et façades ») | 3 |
| `validate_design_governance.py` | D4 O-1 (terme requis `SEED`) | 3 |
| | C8 O-3 et O-4 (liens refusés ; exclusions à la racine seulement) ; E2 O-4, O-7, O-8 (doublons de manifeste, casse des projections, garde d'absence) | 6 |
| `build_distributions.sh` | C8 O-1 et O-2 (archives dans `.build`, contrôle des membres) ; E2 O-3 (promotion transactionnelle) ; E1 O-1 (chemins Local) | 6 |
| `package_manifest.json` | E2 O-13 (`version` = CHANGELOG) | 6 |
| `.github/workflows/validate.yml` | F-WF-001 (épinglage par SHA, versions natives Node 24 relevées au patch, run hébergé vert) | 6 |

**Résolue sans outil propre :** E2 O-2, soit F-BLD-002 (par C8 O-1).

**Aucun fichier ajouté ni supprimé :** les manifestes 60/56 restent inchangés (A1 C2, A2 C2, C8 C1).

### 4.5 Harnais

**22 harnais, relancés sur B01 :**
- témoins et conservations **40/40** ;
- **300 cas**, dont **3 verts** et **297 rouges**.

Les trois cas verts sont documentés, un par rapport :
- B2-P2 : proportion, `valid_closed_return` sans champ nouveau ;
- B3-P3 : proportion, retour SYSTÈME sans paquet ;
- LCF-20 : conservation.

Les 297 cas rouges sont la **preuve des défauts** que les patchs doivent lever.

**Nouvel outil : `DG_AUDIT_001_Suivi_harnais.py`.** Il lance les 22 harnais sur une racine et produit un instantané JSON. Il lève une alerte dans quatre cas :
- un témoin tombe ;
- un dénominateur change, ce qui signale un harnais modifié ;
- l'empreinte d'un harnais diffère de l'instantané comparé ;
- avec `--compare`, un harnais perd des cas verts.

Il a été éprouvé de deux façons :
- **sur B01** : sortie identique au tableau ci-dessus, code 0 ;
- **sur un instantané muté** (un cas vert en plus, une empreinte changée) : deux alertes, code 1.

La référence est `DG_AUDIT_001_Instantane_harnais_B01.json`.

**Règle de phase 12, rendue vérifiable :** un harnais ne change que par une **rectification déclarée** (comme G-01 de D1 en 11.19), **jamais pour épouser un patch**. Si le texte appliqué diffère de la cible, c'est le patch qui est revu, ou bien la rectification est déclarée avant.

### 4.6 Épreuves non machine (phase 13)

Voici les épreuves nommées dans les sorties des grappes :
- **Lecture** : B5, C1, C3, C5, C6, C7, D3 ; **relecture** E1.
- **Projection** : C2.
- **Épreuve outillée et mesure** : C4, avec la route LITE ≤ 60 lignes servies.
- **Imitation** : C6.
- **Mesure M, avec et sans DG, sur au moins trois briefs** : C7.
- **Intégrateur** : C9.
- **Un run, une revue ; un exemple, deux façades ; routage** : D1.
- **Phase, boucle, ITER** : D2.
- **Cycle de vie et propriétaire** : D4.

**Presque toutes exigent un lecteur qui ne connaît pas les rapports.** C'est la limite récurrente de l'audit (observateur unique). Elle est désormais opérationnalisée par D3 : REVIEWER-RELATION, RENDER-AUTHOR, CONFLICT.

**Rappel de la contrainte :** sans observateur conforme, une épreuve d'efficacité est une « auto-comparaison différée », et aucune clôture `FULL` ne peut être prononcée.

## 5. Examen de conformité de la phase 11

| # | Critère | Résultat | Preuve |
|---|---|---|---|
| K1 | Chaque fiche a une décision | **Conforme** | 158/158 : 149 dans 22 PATCH-DECISION, 9 en lot F ; contrôle de citation sans manquant |
| K2 | Une PATCH-DECISION par grappe, chacune approuvée par l'owner | **Conforme** | 22/22, une réponse de l'owner par unité |
| K3 | Les sept questions du §21 posées pour chaque grappe | **Conforme** | 22/22 rapports portent le tableau §21, les conditions de phase 12, la sortie et le bilan §32 |
| K4 | Preuve définie **avant** modification (§21, question 5) | **Conforme, avec limite** | 22 harnais, 297 cas rouges sur B01, épreuves nommées (§4.6). Limite : les corrections textuelles sont prouvées par des gardes de formulation et des épreuves de lecture, pas par la machine (16 limites déclarées) |
| K5 | Aucun patch appliqué ; B01 intacte ; B02 non utilisée comme base | **Conforme** | 218/218 ; aucun dossier généré (un `__pycache__` créé par un rejeu a été supprimé, §3.2) ; les cibles textuelles ont seulement été vérifiées comme chaînes. C4 a refusé la table de 70 locators de B02 |
| K6 | Aucune correction interdite sans nécessité démontrée (§21) | **Conforme** | Aucun gate concurrent (D1 **unifie** les revues), aucun score, un quota **retiré** (K08). La LCF est un test déclaré sous D-FAC-1. `SEED` nomme un état qui existe déjà de fait |
| K7 | Cohérence de l'ordre de phase 12 entre les rapports | **Non conforme tel qu'écrit → rectifié en §6** | Cinq contradictions entre conditions (R-1 à R-5) |
| K8 | Inventaires recalculés, sans recopie | **Conforme** | §2 et §4 recalculés par script sur les CSV et les rapports |
| K9 | Reprise possible hors de cette conversation | **Conforme** | Plan maître, archive de transfert, instantané de référence |

## 6. Rectifications de l'ordre de phase 12

L'examen K7 a trouvé cinq contradictions. **Aucune ne change une décision de correction.** Toutes portent sur la **place** d'une correction dans la séquence.

| # | Contradiction | Sources | Rectification |
|---|---|---|---|
| **R-1** | E2 range C4 (O-1, O-2) et C5 (LCF) dans le **cycle d'outil unique, en dernier**. Or C4 exige O-2 **avant toute modification de locator**, et C5 exige la table LCF écrite **rouge avant les textes** | E2 C1 et §4 (ligne 122) ; C4 C1 ; C5 C1 ; D1 C2 | **Le cycle d'outil est scindé.** Un **cycle de garde** (étape 3) passe **avant** la migration et les textes. Le **cycle d'outil final** (étape 6) garde le reste. **Mon erreur, en E2** : j'y ai recopié une formule de résumé sans relire les conditions de C4 et C5 |
| **R-2** | C4 C1 dit « O-2 d'abord, ensuite O-1 ». Mais O-2 **importe** le résolveur d'O-1 | C4 C1 et §4.1 | **O-1 et O-2 dans le même diff**, avant toute modification de locator. C'est l'intention de C4 C1 : le validateur de carte existe avant qu'un locator change |
| **R-3** | C4 C2 range F-VRC-004 dans le cycle d'outil. E2 O-12 le range « même cycle que INV-C4-2 », qui est dans la **migration unique** | C4 C2 ; E2 O-12 | **O-12 va dans la migration** (étape 4), dans le même diff que INV-C4-2. La liste des hôtes de démonstration est la même pour les deux champs |
| **R-4** | D4 C2 : « O-1 (`SEED`) dans le même cycle que T-1 » (CHANGELOG, texte). Cela n'a pas de place dans une séquence outils → textes | D4 C2 | **O-1 va dans le cycle de garde** (étape 3), écrit **rouge**, et T-1 le rend vert. C'est le même motif que la LCF : le validateur exige `SEED` **avant même** que le CHANGELOG le porte |
| **R-5** | C6 C2 range `machine_projection.md` dans le cycle de la skill (textes). Mais C6 §4 (ligne 115) et E1 C2 le rangent dans la **migration unique** | C6 C2 ; C6 §4 ; E1 C2 | **Le YAML va dans la migration** (étape 4), deux sources contre une. Le cycle de la skill garde `examples.md` et les copies de façade C3 et C5 |

**Conséquence (certaine) : un état intermédiaire rouge.** Entre l'étape 3 et la fin de l'étape 5, la suite intégrée (`validate_all.py`) est **rouge par construction**, sur la LCF et sur `SEED`. C'est voulu : un texte ne se corrige pas sans sa garde.

Chaque étape se contrôle donc autrement :
- par les harnais de ses grappes ;
- par `DG_AUDIT_001_Suivi_harnais.py --compare` : la liste des rouges ne doit **que décroître**, et les témoins restent verts.

**Après rectification : K7 conforme.**

## 7. Ordre de la phase 12

Deux principes, déjà fixés, s'appliquent à toutes les étapes :
- **un propriétaire par cycle** (§22) ;
- **canon avant renvoi et avant façade.**

| Étape | Contenu | Contrôle de sortie |
|---|---|---|
| **0. Ouverture** | Copie de travail de B01, avec un nom de candidate à fixer par l'owner (je propose **B03**, puisque B02 reste gelée). Empreintes consignées. Instantané de référence (§4.5) | 218/218 sur la source ; instantané identique à `…_B01.json` |
| **1. A1** | `validate_run_card.py`, `validate_contracts.py` : autorité du schéma | Harnais A1 11/11 ; aucun autre harnais ne recule |
| **2. A2** | Table des fixtures, cas unitaires, motifs de `validate_all.py` (diff distinct de A1, A2 C1) | A2 5/5 |
| **3. Cycle de garde** | C4 O-1 et O-2 (un diff, R-2) avec E2 O-5 ; table LCF de C5, avec les entrées de C6, D1 et D4 (21) écrites **rouges** ; D4 O-1 `SEED` (R-4) | Harnais C4, partie résolveur et carte, verts ; LCF rouges **pour leur motif** (sauf LCF-20) ; aucun locator existant ne cesse de résoudre |
| **4. Migration unique** | Les quatre schémas (§4.3) ; les invariants de la liste close dans les deux validateurs, chacun avec son cas unitaire ; E2 O-12 (R-3) ; exemple canonique, fixtures, exemples de contrats, YAML de `machine_projection.md` (R-5) | Harnais B1 à B4, C1, C2 (partie machine), C3 (contrats), C9, D2 et E2 (INV) verts ; fixtures : même verdict, motif obligatoire |
| **5. Textes, une passe par propriétaire** | **CHANGELOG** (D4) → **BIBLIOTHEQUE** (B3, B5, C3, C7, D4, E1) → **ACTION** (B1 à B5, C1 à C4, D1 à D3, E1) → **DIRECTION** (B1, B4, C1, C2, C4, C5, C6, D1, D2, D4, E1) → **SAVOIR** (B4, B5, C1, C7, D1, D3, E1) → **cartes et glossaire** (READING_MAP : C4, C5 ; ORCHESTRATION_MAP : C5 ; GLOSSAIRE : C6, E1) → **façades** (QUICKSTART, README des deux distributions, skill et `references/` : B1, B2, B3, C3, C4, C5, C6, C9, D1, E1) | Chaque passe fait tourner vers le vert les gardes de ses grappes. La relecture complète des zones listées dans les conditions est faite en fin de passe (§22) |
| **6. Cycle d'outil final** | E2 O-1, O-3, O-4, O-6 à O-11, O-13 ; C8 O-1 à O-4 ; E1 O-1 ; F-WF-001 ; manifeste et version à jour | Suivi : **40/40 et 300/300** ; `validate_all.py` vert ; double construction identique ; contrôle des membres GitHub et Local ; run hébergé vert |
| **7. Sortie** | `PATCH + DIFF-REASONING` par étape ; réévaluation des fiches touchées (§22) | Autorise la phase 13, pas davantage |

**Pourquoi cet ordre de passes (étape 5).** Chaque flèche suit une dépendance canon → renvoi relevée dans les conditions :
- **CHANGELOG avant BIBLIOTHEQUE** : les statuts sont recopiés, sous la garde de LCF-20.
- **BIBLIOTHEQUE avant ACTION et SAVOIR** : B5 fait de BIBLIOTHEQUE le canon du composant partagé, et ACTION et SAVOIR y renvoient.
- **ACTION avant DIRECTION** : conditions C1 C1 et C2 C1.
- **DIRECTION avant SAVOIR** : B4 et E1 (F-SAV-010) alignent SAVOIR sur l'absolu de DIRECTION.
- **Façades en dernier** : C3 C3, C5 C2, D1 C2.

**Limite de l'inventaire par passe (probable).** Les grappes affectées à chaque passe ont été extraites par script des tableaux de correction, puis complétées à la main pour C1 et E1. **Chaque passe commence donc par extraire des 22 rapports la liste exhaustive des corrections de son propriétaire.** C'est cette liste qui fait foi.

**Conditions d'entrée de la phase 12 :**
- accord de l'owner ;
- nom de la candidate ;
- instantané de référence identique à `…_B01.json` à l'ouverture.

## 8. Sortie

- **Phase 11 : CONFORME**, après les rectifications R-1 à R-5 (ordre seulement, aucune décision modifiée).
- **Phase 12 : AUTORISÉE.** Elle s'ouvre sur l'accord de l'owner.
- **Bilan :**
  - 158/158 fiches décidées ;
  - 22 PATCH-DECISION ;
  - lot F clos (11 observations, aucun patch) ;
  - liste close 92 lignes, 82 actifs ;
  - LCF 21 entrées ;
  - migration de schéma close (4 fichiers) ;
  - 22 harnais (40 témoins, 300 cas).
- Aucun patch, aucun verdict global. **Aucune efficacité n'est établie par la phase 11** : elle dépend des épreuves de phase 13, sous les critères d'observateur de D3.

**§32 : ce que cette unité a changé.**
1. **L'examen de conformité a trouvé un vrai défaut.** L'ordre de phase 12 était contradictoire en cinq points, dont un de mon fait (E2). Appliqué tel quel, il aurait corrigé des textes avant leurs gardes, c'est-à-dire exactement ce que C5 interdisait. Une clôture de pure forme ne l'aurait pas vu.
2. **Le test préalable de F-VDG-003 a changé la connaissance, pas la décision.** La forme est active et le correctif ne coûte qu'un drapeau, mais aucun défaut n'est constaté. J'avais d'abord supposé un faux échec sur `issue: null` : la vérification dans le code (`ISSUE_VALUES` contient `null`) l'a démenti avant publication.
3. **Ce qui aurait pu être fusionné :** l'inventaire des outils (§4.4) aurait pu être tenu au fil des grappes, comme la liste close. Il aurait alors révélé R-1 dès 11.21.

**Prochaine unité : 12.00 Ouverture de la phase 12** (copie de travail, nom de candidate, instantané), puis **12.01 A1.**
