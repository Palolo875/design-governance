# DG-AUDIT-001 — Phase 11.21 — PATCH-DECISION E2 : lot technique

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec E2 ». L'owner a accepté l'ordre proposé en 11.20 : E2 avant E1, parce qu'E2 ferme la liste des schémas.

**Lot E2 : 18 fiches, toutes Mineur.** Le registre de 10.05 en annonçait 20 ; F-VCT-003 et F-FIX-001 ont été déplacées vers A1 et A2 (11.00). Le lot est traité **par une décision de lot**. Une sous-décision n'est écrite que pour les fiches qui en demandent une : deux fiches de schéma, une décision de version et deux fiches déjà décidées ailleurs.

**Sorties :**
- cette `PATCH-DECISION` ;
- `E2_harnais_non_regression.py` : **23 cas exécutés sur l'outillage réel** (validateurs, lecteur, build, workflow) ;
- la liste close mise à jour ;
- **la liste des changements de schéma, close.**

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | A1 et A2 (autorité du schéma, oracles) ; C4 (résolveur, profil strict, `source_path`) ; C5 (LCF-C1) ; C8 (archives créées puis publiées, O-1) ; C9 (inventaire des contrats, CLI `--type`) ; D2 (rectification : deux candidats de schéma en E2) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218. **Tous les cas sur copie** ; aucun build dans le dossier source |
| Sources relues | `validate_all.py` 20–36 ; `build_distributions.sh` 1–166 ; `validate_design_governance.py` 12–31, 96–112, 139–185 ; `validate_run_card.py` 127–136, 276–325 ; `validate_contracts.py` (en entier, déjà lu en C9) ; `read_route.py` ; `package_manifest.json` ; `.github/workflows/validate.yml` ; DIRECTION 196–212 (gabarit DOMAIN-FRAME) ; CHANGELOG 3 |

## 2. Re-vérification : harnais sur B01

**Résultat : témoin et conservation 2/2 ; lot 0/22.** Durée environ 9 secondes, en comptant `validate_all` et les builds sur copies.

| Cas | Fiche | Comportement B01 observé |
|---|---|---|
| E2-01 | F-ALL-002 | `validate_all` lancé hors de la racine : « fixture absente » (faux échec) |
| E2-02 | F-BLD-002 | Échec du zip Local : **archive GitHub déjà modifiée** (code 12) |
| E2-03 | F-BLD-003 | Échec du déplacement de promotion : **`dist` absent** |
| E2-04, 05 | F-DF-002 | Plan de preuve « à déterminer » accepté ; un plan structuré est rejeté |
| E2-06 à 08 | F-RB-002 | Recherche non déclenchée rejetée (`entries` minItems 1) ; condition d'arrêt « à déterminer » acceptée ; incertitude inchangée rejetée |
| E2-09 à 11 | F-MAN-001, 002 | Doublon de manifeste, version 9.9.9 ou absente : **PASS** (« 61 fichiers attendus » pour 60) |
| E2-12 | F-RRT-001 | Titre factice dans un bloc de code servi ; bloc tronqué par un `#` de code (code 0) |
| E2-14 | F-VCT-002 | Octets non UTF-8 : `UnicodeDecodeError` brut |
| E2-15, 16 | F-VDG-002, 004 | Bloc ` ```JSON ` non reconnu ; README officiel absent : `FileNotFoundError` brut |
| E2-17 à 21 | F-VRC-001 à 004 | Clé répétée acceptée ; octet non UTF-8 : traceback ; types illégaux : `TypeError` ; URL « https://[ » : `ValueError` ; hôte de démonstration accepté pour l'artefact |
| E2-22 | F-VRM-002 | Section handoff de READING_MAP vidée : **PASS** |
| E2-23 | F-WF-001 | Actions `checkout@v4` et `setup-python@v5`, non épinglées |

**Nuance (certaine).** F-VCT-002 n'est reproduite **qu'à moitié**. Une racine `[]` est **déjà** rejetée proprement sur B01, en mode ciblé comme en mode suite (« type attendu object ») ; seule l'entrée non UTF-8 lève une exception brute. Le cas `[]` devient une **conservation** (C-01).

## 3. Les sept questions du §21 (lot)

| Question | Réponse pour le lot |
|---|---|
| Change une décision, une exécution ? | **Oui**, indirectement. Un outil qui échoue par traceback, publie un état mêlé ou accepte une donnée ambiguë (clé répétée, placeholder) rend la validation non fiable. Toutes les autres grappes s'appuient sur elle |
| Défaut réel ? | Oui : 22 cas reproduits sur l'outillage réel ; un demi-cas non reproduit (F-VCT-002, racine `[]`) |
| Gain > charge ? | Oui : corrections locales, sans règle nouvelle |
| Nouvelle autorité ? | **Non**, sauf deux décisions déclarées : la source unique de version (F-MAN-002) et les deux changements de schéma (F-DF-002, F-RB-002), qui reprennent chacun un texte existant |
| Testable ? | Oui : chaque correction a son cas exécuté |
| Positif / défensif équilibré ? | Oui : F-RB-002 rend **valide** une recherche non déclenchée et une incertitude honnêtement inchangée |
| Suppression ou fusion ? | **Correction d'outil** (15 fiches), **clarification** (2 schémas), **décision** (version) |

## 4. PATCH-DECISION

**Décision : CORRIGER (lot).**

### 4.1 Corrections d'outil (décision de lot)

| # | Fiche | Correction | Motif (A2) |
|---|---|---|---|
| O-1 | F-ALL-002 | `validate_all.py` résout chemins de fixtures et commandes **depuis ROOT**, jamais depuis le dossier courant | — (code 0 attendu) |
| O-2 | F-BLD-002 | **Résolue par C8 O-1** (archives créées dans `.build`, publiées ensemble après succès). E2-02 en est le cas d'épreuve | — |
| O-3 | F-BLD-003 | Promotion transactionnelle : si le déplacement de `STAGE` vers `DIST` échoue, **restaurer la sauvegarde avant tout nettoyage**. Au démarrage, une sauvegarde laissée par un échec précédent est restaurée, jamais supprimée | — |
| O-4 | F-MAN-001 | Le validateur refuse toute entrée dupliquée du manifeste (GitHub et Local) | « doublon » |
| O-5 | F-RRT-001 | Lecteur de routes **conscient des blocs de code** (titres ignorés dans les blocs, `#` de code sans effet). Même cycle que le résolveur C4 O-1 | — |
| O-6 | F-VCT-002 | `validate_contracts.py` : lecture non UTF-8 → échec contrôlé (« CONTRACT VALIDATION FAILED ») | « VALIDATION FAILED » |
| O-7 | F-VDG-002 | Détection de projection embarquée **insensible à la casse** (`json`, `JSON`, `Yaml`…) | « projection » |
| O-8 | F-VDG-004 | Garde d'absence : une source requise absente est citée, les autres erreurs restent affichées, code non nul | « README.md » |
| O-9 | F-VRC-001 | `load_json` refuse les **clés répétées** à toute profondeur (`object_pairs_hook`) | « clé répétée » |
| O-10 | F-VRC-002 | Lecture non UTF-8 → `ValidationError` contrôlée | « VALIDATION FAILED » |
| O-11 | F-VRC-003 | **Pré-passe de types** du schéma avant l'interprétation métier ; `urlparse` protégé. L'ordre actuel (messages métier d'abord, voir le commentaire de `validate_card`) est conservé **après** la pré-passe : les motifs A2 des fixtures ne changent pas, car chaque fixture n'a qu'un défaut | « VALIDATION FAILED » |
| O-12 | F-VRC-004 | Profil strict : **même liste d'hôtes de démonstration** pour `trace_locator` et `artifact.locator`. Même cycle que C4 (INV-C4-2) | « démonstration » |

### 4.2 Sous-décisions

**F-VRC-005 : déjà décidée en C4, rattachement déclaré.** En 11.11, j'ai décidé que le profil strict résout les chemins relatifs **depuis le dossier de la carte** (INV-C4-2). J'y présentais ce point comme une extension de F-ACT-020 **sans citer F-VRC-005**, qui existait dans ce lot. La décision est la même. **F-VRC-005 est close par C4**, et son épreuve est le cas C4-P3.

**F-VRM-002 : « contrôler », pas « réduire la promesse ».** La bannière annonce « handoff contrôlés ». Depuis C5, la condition **LCF-C1** vérifie les champs de la section handoff contre `ACTION/HANDOFF`. La promesse devient donc vraie ; E2-22 le vérifie.

**F-MAN-002 : source unique de version.** La source est **`CHANGELOG`** (« Version publique : `V1.0.0` », ligne 3), propriétaire normatif de la gouvernance du système.
- **O-13** : `package_manifest.json` doit porter `version`, égale à la version du CHANGELOG sans le « V » ;
- les titres de README (racine et officiel), QUICKSTART et RELEASE_NOTES doivent citer la même version ;
- motif : « version ».

**F-WF-001 : règle, pas version.** Les actions sont épinglées par **SHA complet** sur des versions qui s'exécutent nativement sous Node 24. Les versions exactes et leurs SHA sont **relevés et vérifiés en phase 12**, avec un run hébergé vert. **Je ne fixe ici aucune version** : je ne l'ai pas vérifiée en ligne dans cette unité, et une version non vérifiée écrite dans une décision serait un claim non observé.

### 4.3 Les deux changements de schéma

| ID | Schéma | Règle | Source |
|---|---|---|---|
| **INV-E2-1** | `domain_frame.evidence_plan[]` | Les éléments deviennent des objets à cinq composantes : `method`, `scope`, `artifact`, `limit`, `next_proof`. Chacune est non vide et sans placeholder. Un artefact **attendu** est admis (« captures attendues v1 ») | DIRECTION 207 (« méthode, scope, artefact, limite et prochaine preuve ») |
| **INV-E2-2** | `research_brief` | `depth: none` ⇒ `entries` peut être vide ; `depth` ∈ {targeted, deep} ⇒ au moins une entrée. **Aucune entrée ⇒ `uncertainty_after` = `uncertainty_before`** : une incertitude ne peut pas être « résolue » sans observation. `stop_condition` et les incertitudes sont sans placeholder | F-RB-002 ; SAVOIR/SOURCE (activation par déclencheur) |

**INV-K04 est retiré.** Il imposait que l'incertitude change, et rejetait donc une recherche honnêtement non concluante. C'était le cas « incertitude restante » de la fiche.

## 5. Liste des changements de schéma : close

**Aucune grappe ni aucun lot restant ne porte de fiche de schéma** : E1 est éditorial, F ne reçoit pas de patch ; vérifié sur les colonnes TARGET et RECOMMENDATION. **La liste de la migration unique est close :**

| Schéma | Changements | Grappes |
|---|---|---|
| `run_card.schema.json` | `risk.statement` ; `risk.critical_protection.result` ; `closure.exception` ; `closure.axes` ; `closure.reservations` ; `artifact.version` ; `artifact.rights_status` ; `proof.provenance.capability` ; `capability_profile.basis` typée ; `closure.system_package` ; `closure.b1b` ; `anchors[].type` ; « au moins un ancrage » retiré ; `direction.identity_stake` ; `direction.calibration` ; `decision_change.outcome` et `.reason` ; `closure.verdict` nullable ; `closure.reclassification` ; `profile_decision.phase` | B1–C2 |
| `production_contracts.schema.json` | racine `required` vidée ; `expected_scope` et `observed_scope` ; `proof_status` canonique et `reason` ; `structural_changes` minItems 1 | C2, C3 |
| `domain_frame.schema.json` | `policy_profile.risk_coverage` ; **`evidence_plan[]` en objets à cinq composantes** | C9, **E2** |
| `research_brief.schema.json` | `source_status`, `source_date`, `source_locator`, `rights_status` ; **`entries` minItems 0 (activation par `depth`)** | C9, **E2** |

**Données à migrer :** l'exemple RUN_CARD, les 25 fixtures, les trois exemples de contrats (`domain_frame` : plan de preuve en objets ; `research_brief` : champs de source) et le YAML de `machine_projection.md`.

## 6. Liste close et inventaire

**Liste close : 92 lignes, 82 actifs.**
- Ajouts : INV-E2-1 et INV-E2-2.
- INV-K04 passe à « EXISTANT — RETIRÉ (E2, F-RB-002) ».

Inventaire des outils à date : les corrections O-1 à O-13, **dans le cycle d'outil unique** de C8 (C1), avec C4 O-1 et O-2 et le validateur « carte et façades » de C5.

## 7. Conditions et sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Ordre** : A1 → A2 → **migration unique** (schémas, validateurs, données) → textes → **cycle d'outil unique** (C4, C5, C8, E2) en dernier, manifeste et version à jour |
| C2 | **A2** : chaque correction d'outil entre dans la table d'oracles avec son cas E2 et son motif |
| C3 | **F-WF-001** : versions et SHA relevés à la date du patch ; run hébergé vert, avec versions et SHA consignés dans la trace |

**Sortie (phase 13) :**
1. `E2_harnais_non_regression.py` : témoin et conservation **2/2**, lot **22/22**. Harnais A1 à D4 verts.
2. `validate_all.py` : `FULL VALIDATION PASSED`, lancé **depuis la racine et depuis un dossier externe**.
3. **Run hébergé** du workflow, vert (F-WF-001).

**Limite déclarée.** Ces corrections rendent l'outillage **fiable sur ses entrées**. Elles ne prouvent rien sur la qualité des runs ; ce n'est pas leur objet.

## 8. Sortie

- **PATCH-DECISION E2 : CORRIGER (lot de 18 fiches).**
  - 13 corrections d'outil, dont 1 résolue par C8 ;
  - 2 changements de schéma et leurs invariants ;
  - 1 décision de source de version ;
  - 2 rattachements déclarés (F-VRC-005 à C4, F-VRM-002 à C5) ;
  - 1 invariant retiré (K04).
- **Liste des changements de schéma close.**
- Listes : liste close **92 lignes, 82 actifs** ; LCF **21**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Dix-huit fiches Mineur tiennent en une décision de lot, parce que les décisions structurantes avaient déjà été prises dans les grappes (C4, C5, C8, C9).
- Le lot n'ajoute que ce qui manquait : deux schémas repris du texte, une source de version, et la robustesse d'entrée des outils.

**Prochaine unité : 11.22 PATCH-DECISION E1** (lot éditorial : 27 fiches).
