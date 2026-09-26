# DG-AUDIT-001 — Phase 11.16 — PATCH-DECISION C9 : contrats de production et de cadrage

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ». **Dernière grappe C.**

**Grappe C9 : 4 fiches, toutes Significatif. Deux reports hérités de C3 s'y ajoutent.**

| Objet | Contenu |
|---|---|
| F-ACT-008 | Le CLI ciblé ne valide que les chemins exacts des exemples : une copie valide est rejetée comme « chemin non canonique » |
| F-DF-001 | DOMAIN_FRAME : la cohérence risque ↔ contrôle se réduit à **un** élément identique entre deux listes, sensible à la casse |
| F-PC-002 | UI_UX_REALITY_PACK : les mots d'une exigence sont cherchés dans la matrice **concaténée**, si bien qu'une exigence fabriquée à partir de deux lignes passe |
| F-RB-001 | RESEARCH_BRIEF : une source est un texte libre, sans statut, date, locator ni owner ; les ajouts structurés sont rejetés |
| Report C3 (a) | Inventaire des **contrôles existants** de `validate_contracts` dans la liste close (lacune signalée en 11.10) |
| Report C3 (b) | `directions.maxItems = 3`, borne sans source textuelle |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C9_harnais_non_regression.py` ;
- 18 lignes ajoutées à la liste close (3 invariants nouveaux et l'inventaire K01–K15) ;
- la mise à jour de l'inventaire de migration.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | D-ACT-1 = c ; A2 ; C2 (racine « au moins un », scope attendu / observé, jetons canoniques ; dépendance déclarée à F-ACT-008) ; C3 (quota retiré, authenticité ; lacune d'inventaire) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; contrôles sur copie |
| Sources relues | `validate_contracts.py` (218 lignes, en entier) ; les trois schémas de contrats et leurs exemples ; DIRECTION 190–215 (DOMAIN-FRAME) ; SAVOIR 471–520 (SOURCE, fiche minimale) ; ACTION 93–114 (UI-UX-REALITY) ; README racine 123 |

## 2. Re-vérification

**Harnais C9 sur B01 :**
- témoins **2/2** ;
- contrats **0/11** ;
- CLI **0/3**.

**Contrôles directs sur copie :**

| Cas (forme B01) | B01 | Fiche |
|---|---|---|
| Risque nouveau « exposition de données personnelles » sans aucun contrôle | **accepté** | F-DF-001 (4.05) |
| « focus clavier » et « récupération après erreur » retirés des contrôles | **accepté** | F-DF-001 (4.05) |
| Déclencheur « Alerte critique » au lieu de « alerte critique » | **rejeté** : casse | F-DF-001 |
| Exigence « state_matrix: source indisponible données » (mots pris à deux lignes) | **accepté** | F-PC-002 |
| Source de recherche « ? » | **accepté** | F-RB-001 (4.06) |
| Entrée de recherche avec un `source_status` | **rejetée** : champ inconnu | F-RB-001 |
| Copie valide de l'exemple hors du dossier `schemas/examples` | **rejetée** : « chemin non canonique » ; `--type` inconnu | F-ACT-008 |

**Relecture : deux constats décisifs.**
1. **La forme canonique existe pour les sources.** SAVOIR/SOURCE définit une fiche minimale : SOURCE (origine, date, portée), ROLE, **STATUS** (vérifié dans ce run, connaissance non revérifiée, source utilisateur non revérifiée), observé, retenu, rejeté, transformé, décision, limite, **TRACE-LOCATOR**, OWNER / NEXT-PROOF, **RIGHTS**. Une entrée de `RESEARCH_BRIEF` en porte déjà sept (observed, retained, rejected, transformed, decision_changed, limit, reliability_basis). **Il ne lui manque que le statut, la date et le locator.** C'est une projection incomplète, le même cas que la RUN_CARD en C2.
2. **Le contrôle risque ↔ contrôle compare deux listes au lieu de relier chaque risque.** Tant qu'un seul risque reste identique, tout le reste peut disparaître.

## 3. Les sept questions du §21

| Question | F-ACT-008 | F-DF-001 | F-PC-002 | F-RB-001 |
|---|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : le contrat est inutilisable en production | **Oui** : profil de domaine « valide » qui a perdu des protections | **Oui** : un état est crédité d'une preuve inexistante | **Oui** : une connaissance non revérifiée passe pour une observation |
| Défaut réel ? | Oui (4.05, 4.06) | Oui (4.05) | Oui (4.07, 4.08) | Oui (4.06) |
| Gain > charge ? | Oui : un argument | Oui : une liste de couverture (une ligne par risque) | Oui : liaison exacte ; couverture des seuls états | Oui : trois champs |
| Nouvelle autorité ? | Non | **Non** : c'est la relation que DOMAIN-FRAME décrit déjà (risques → contrôles requis) | **Non** : CRITICAL-STATES d'ACTION 97 | **Non** : fiche SAVOIR/SOURCE |
| Testable ? | Oui (L-01 à L-03) | Oui (D-01 à D-P2) | Oui (P-01 à P-P1) | Oui (R-01 à R-P1) |
| Positif / défensif équilibré ? | **Oui, gain positif** : l'intégrateur valide son propre fichier | Oui : libellé équivalent accepté ; un contrôle peut couvrir plusieurs risques | Oui : les autres matrices restent en couverture libre | Oui : une connaissance non revérifiée reste **valide si elle est déclarée comme telle** |
| Suppression ou fusion ? | **Correction d'outil** | **Alignement** (D-ACT-1) | **Correction d'outil** | **Alignement** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

### 4.1 Invariants (liste close D-ACT-1)

| ID | Règle | Schéma | Motif (A2) |
|---|---|---|---|
| **INV-C9-1** | `policy_profile.risk_coverage` : chaque `domain_risk` a au moins une entrée. Chaque entrée cite un risque déclaré et soit un `control` de `required_controls`, soit une `review` non vide. Identité **normalisée** (casse, espaces), **pas** d'inclusion de mots | **nouveau** champ requis | « risque sans contrôle ni revue » ; « contrôle inconnu » |
| **INV-C9-3** | `coverage_map.requirement` = `<matrice>: <élément exact>` (identité normalisée). **Chaque élément de `state_matrix`** a une entrée de couverture ; statut `OBSERVED`, `NOT-VERIFIED` ou `N/A-JUSTIFIED` (C2) | inchangé | « exigence absente des matrices » ; « état non couvert » |
| **INV-C9-4** | Entrée de recherche : `source_status` ∈ {`verified_in_run`, `unverified_knowledge`, `user_source_unverified`} (les trois STATUS de SAVOIR/SOURCE). `source` sans placeholder (`?`, tbd, todo, inconnu, n/a). `source_date` ISO (année, mois ou jour) ou `unknown`. `verified_in_run` ⇒ `source_locator` non vide et date connue | **nouveaux** champs | « source placeholder » ; « exige un locator » |

**Sous-décisions :**
- **F-DF-001, couverture et non appariement.** La recommandation écarte l'appariement lexical. `risk_triggers` reste une liste de signaux pour DIRECTION ; **INV-K01** (intersection lexicale) est remplacé. Une identité normalisée entre un risque et **son** entrée n'est pas un appariement lexical : c'est une référence explicite.
- **F-PC-002, périmètre de la complétude.** La complétude est exigée pour les **états** seulement. Ce sont les CRITICAL-STATES d'ACTION 97, et le cas-test de la fiche porte sur un « état critique omis ». Pour les autres matrices, la liaison est exacte mais la couverture reste libre (proportion). Avec les jetons de C2, une entrée non vérifiée coûte une ligne et **déclare** le trou au lieu de le taire.
- **F-RB-001, champs minimaux plutôt qu'un pointeur.** La recommandation offrait les deux voies. Un pointeur vers une fiche SOURCE hors du contrat n'est pas vérifiable par la machine. Trois champs, projection de la fiche, le sont. OWNER / NEXT-PROOF restent au niveau du run : **perte déclarée**, portée par la trace (principe C2). RIGHTS : `rights_status` facultatif, avec l'énumération de B2 lorsque la source est un asset.

**Limite déclarée (F-DF-001).** Un contrôle rattaché à **aucun** risque déclaré (dans l'exemple : « focus clavier », « récupération après erreur ») peut encore être retiré sans alerte. La machine protège la relation risque → contrôle, pas une liste de contrôles orphelins. La migration de l'exemple rattache chaque contrôle à un risque, ou déclare explicitement le contrôle orphelin : forme seule.

### 4.2 CLI (F-ACT-008)

| # | Correction |
|---|---|
| O-1 | `validate_contracts.py [--type {domain_frame,research_brief,production_contracts}] <chemin>`. Sans `--type`, le type est **détecté** par les clés racines : une seule famille doit correspondre, sinon « type ambigu : utiliser --type ». Chemins absolus et relatifs, **hors du package** compris. `name_for_path` et le refus « chemin non canonique » sont retirés |
| O-2 | Sans argument, la suite complète actuelle est inchangée (T-1 et T-2 restent verts) |
| T-1 | README racine 123 et QUICKSTART documentent la commande ciblée avec `--type` |

**Levée de dépendance.** C2 avait noté que INV-C2-2 à C2-4 ne protégeraient les projections des équipes qu'après F-ACT-008. **O-1 lève cette dépendance.**

### 4.3 Inventaire des contrôles existants (report C3 a)

Les quinze contrôles de `validate_contracts.py` et des schémas sont inventoriés dans la liste close (INV-K01 à K15) :

| Statut | Contrôles |
|---|---|
| **Conservé** | K03 à K07, K09, K13, K15. K02 est **modifié** (normalisation de la casse et des espaces) |
| **Remplacé** | K01 (par C9-1), K10 et K11 (par C9-3), K12 (par C2-4) |
| **Retiré** | K08 (quota « deux leviers », C3) |
| **Conservé sans source** | K14 (`maxItems 3`) |

**Report C3 (b) : `maxItems 3`.** La borne n'a pas de source textuelle. Elle **ne force aucune fabrication** et aucune friction n'a été observée. Elle est **conservée**, marquée « sans source », et versée au lot F (observation). La retirer serait un changement sans défaut constaté.

## 5. Inventaire de migration : ajouts C9 et état

| Objet | Changement | Grappe |
|---|---|---|
| `domain_frame.schema.json` : `policy_profile.risk_coverage` | Nouveau, requis : `[{risk, control?, review?}]` | C9 |
| `research_brief.schema.json` : `entries[]` | Nouveaux : `source_status` (requis), `source_date` (requis), `source_locator` ; `rights_status` facultatif | C9 |
| `validate_contracts.py` | INV-C9-1, C9-3, C9-4 ; K02 normalisé ; K01, K10 et K11 retirés du code ; CLI (O-1) | C9 |
| Exemples `domain_frame`, `research_brief`, `production_contracts` | Migrés : couverture des risques, champs de source, cinq états couverts avec exigences exactes | C9 |

**Après C9, un seul candidat de schéma reste ouvert : D2 (F-DIR-036, référence de direction pour ITER).** L'inventaire sera clos à la fin de D4, comme prévu.

## 6. Conditions du patch et de sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Dans la migration unique**, avec C2 et C3 : même passe sur `validate_contracts.py` et sur les trois schémas |
| C2 | **A1 d'abord** : les nouveaux champs passent la prévalidation du schéma et le parcours des mots-clés. Aucun mot-clé hors du sous-ensemble supporté |
| C3 | **A2** : chaque invariant avec son cas unitaire et son motif ; les quatre mutations négatives actuelles (`check_negative_mutations`) passent dans la table d'oracles avec leur motif |
| C4 | **Exemples** : chaque exemple migré garde son rôle de témoin positif. `valid_*` reste valide, et chaque cas négatif garde **un seul** défaut |

**Sortie (phase 13) :**
1. `C9_harnais_non_regression.py` : témoins **2/2**, contrats **11/11**, CLI **3/3**. Harnais A1 à C8 verts.
2. **Épreuve d'intégrateur** : une équipe valide son propre `DOMAIN_FRAME`, `RESEARCH_BRIEF` et pack UI/UX **hors du package**, avec le seul README.

**Limite déclarée.** Les invariants vérifient que chaque risque est relié à un contrôle, que chaque état est couvert et que chaque source est qualifiée. Ils ne vérifient pas que le contrôle **protège réellement** le risque, que la couverture « OBSERVED » a été **observée**, ni que la source dit ce que l'entrée lui attribue. Ces points restent de la lecture et de la preuve (forme seule).

## 7. Sortie

- **PATCH-DECISION C9 : CORRIGER.**
  - 3 invariants ;
  - 1 correction de CLI ;
  - inventaire des contrats clos (15 contrôles) ;
  - 2 changements de schéma ;
  - 1 limite déclarée (contrôles orphelins).
- **Liste close : 88 lignes, 79 actifs** (RUN_CARD et contrats). **LCF : 16 entrées**, inchangée.
- **Lot C clos : les neuf grappes C1 à C9 sont décidées.**
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Deux contrôles « de cohérence » étaient des **intersections de listes**, qu'un seul élément suffisait à satisfaire. Ils deviennent des **relations par entrée**.
- La source de recherche retrouve la forme que SAVOIR lui donnait déjà.
- Le CLI peut enfin servir à ceux qui écrivent des contrats, pas seulement aux exemples.

**Prochaine unité : 11.17 PATCH-DECISION D1** (frontière du jugement de craft : 3 fiches, F-DIR-020, F-DIR-030, F-DIR-042). Le lot D compte 13 fiches en 4 grappes.
