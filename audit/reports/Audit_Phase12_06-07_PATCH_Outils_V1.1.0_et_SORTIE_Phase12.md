# DG-AUDIT-001 — Phases 12.06 et 12.07 — Cycle d'outils final, version V1.1.0 et sortie de la phase 12

**Date :** 26 septembre 2026. **Candidate :** B03, version **V1.1.0**. B01 reste en lecture seule ; B02 reste gelée. **Format :** rapport allégé.

Cette unité fusionne 12.06 et 12.07, sur décision de l'owner du 26 septembre.

**Commit :** `a6eeca8`, étiquette `12.06-outils-v1.1.0`.

**Fichiers produits :**
- `DG_AUDIT_001_B03_12-06.diff` ;
- `DG_AUDIT_001_B03_package_12-06_V1.1.0.zip`, les sources (SHA-256 `249fc751…e018`) ;
- `Design_Governance_V1.1.0_GITHUB.zip`, 60 fichiers (SHA-256 `7abb01a6…5793`) ;
- `Design_Governance_V1.1.0_LOCAL.zip`, 56 fichiers (SHA-256 `05f78db1…fa15`) ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-06.json` ;
- `C4_harnais_non_regression.py`, rectifié (R-15).

**Décisions de l'owner prises au début de l'unité :**
- version **V1.1.0** ;
- budget de `DIRECTION/START` porté à **76 lignes** ;
- les cas négatifs des quelque 14 invariants existants ne sont pas ajoutés : ils passent **en réserve**.

---

# Partie A — 12.06 : cycle d'outils final

## A.1 Corrections appliquées (12 fichiers, +243 / −54)

| Décision | Outil | Ce qui change |
|---|---|---|
| **C8 O-1** | `build_distributions.sh` | Les archives sont créées dans `.build/archives`, à partir d'un fichier absent, puis déplacées à la racine seulement à la publication. Un build échoué ne touche plus aux archives précédentes |
| **C8 O-2** | idem | Avant publication, les membres de chaque archive sont comparés au manifeste (GitHub, Local), à l'identique. Motif d'échec : « membres de l'archive ≠ manifeste » |
| **C8 O-3** | `validate_design_governance.py` | Tout lien symbolique dans le package est refusé (« lien symbolique »). Le parcours ne suit plus les liens |
| **C8 O-4** | idem | `dist` et `.build` ne sont exclus qu'**à la racine** ; `__pycache__` reste exclu partout |
| **E2 O-1** | `validate_all.py` | Les chemins des fixtures sont résolus depuis `ROOT` : le script donne le même résultat lancé depuis n'importe quel dossier |
| **E2 O-2** | — | Réglé par C8 O-1 (cas E2-02) |
| **E2 O-3** | `build_distributions.sh` | Promotion transactionnelle : si le déplacement échoue, la sauvegarde est restaurée avant tout nettoyage. Au démarrage, une sauvegarde laissée par un échec est restaurée, jamais supprimée |
| **E2 O-4** | `validate_design_governance.py` | Toute entrée en double dans le manifeste est refusée (« doublon ») |
| **E2 O-6** | `validate_contracts.py` | Une lecture non UTF-8 est un échec contrôlé (« CONTRACT VALIDATION FAILED ») |
| **E2 O-7** | `validate_design_governance.py` | La détection d'une projection embarquée ignore la casse (`JSON`, `Yaml`…) |
| **E2 O-8** | idem | Une source requise absente est citée ; les autres contrôles continuent ; le code de sortie est non nul, sans traceback |
| **E2 O-9, O-10** | `validate_run_card.py` | Les clés JSON répétées sont refusées à toute profondeur (« clé répétée ») ; une lecture non UTF-8 est un échec contrôlé |
| **E2 O-11** | idem | Une pré-passe de types précède l'interprétation métier. Pour les fixtures valides, l'ordre des diagnostics est inchangé : les 25 motifs attendus sont conservés |
| **E2 O-13** | `validate_design_governance.py`, manifeste, titres | Source unique de version : le CHANGELOG. Le manifeste porte la même version, sans le « V » ; les titres du README (racine et officiel), de QUICKSTART et de RELEASE_NOTES la citent. Motif : « version » |
| **E1 O-1** | `build_distributions.sh` | Dans l'export Local, `V1/official/` devient `official/` et `skills/design-governance-practice/` devient `skill/`, dans la skill, ses références et QUICKSTART. Le contrôle de liens Local couvre aussi les chemins `.md` cités entre accents graves |
| **F-WF-001** | `.github/workflows/validate.yml` | `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1) et `actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97` (v7.0.0), toutes deux déclarées `node24` dans leur `action.yml`. Relevé le 26 septembre 2026 par `git ls-remote` et une copie de chaque tag |
| **Version V1.1.0** | CHANGELOG, RELEASE_NOTES, README, QUICKSTART, manifeste, README Local | La section « V1.1.0 » du CHANGELOG et les notes de version sont rédigées à partir du journal des unités 12.01 à 12.06. La section V1.0.0 est conservée comme historique |

E2 O-5 et O-12 étaient déjà appliqués (en 12.03 et 12.04).

## A.2 Résultats

| Contrôle | Résultat |
|---|---|
| `validate_all.py` | **FULL VALIDATION PASSED**, deux builds identiques ; export Local validé avec ses chemins propres |
| **Harnais** (`--rectifies C4 --compare` 12.05c) | **Témoins 40/40 ; cas 300/300 ; aucun rouge, aucune alerte** |
| Vérifications X et Y (A1, A2) | 7/7 et 7/7 ; Y-7 redevient significatif depuis la fermeture de la fenêtre |
| Suite RUN_CARD | 25/25 fixtures avec leur motif inchangé ; 76/76 cas unitaires ; contrats 20/20 |
| Distributions V1.1.0 | Construites depuis l'étiquette, dans un dossier sans dépôt git : 60 et 56 fichiers, identiques au manifeste |
| B01 | 218/218, aucun fichier généré |

**Ce qui reste non vérifié (certain) : le run hébergé du workflow.** Les SHA sont relevés et le runtime `node24` est lu dans les sources des actions. Aucun run sur un runner GitHub n'a été observé. **Seul l'owner peut le produire,** en poussant la distribution GitHub. Le point est déclaré `NOT-VERIFIED` dans RELEASE_NOTES.

## A.3 Écarts et rectifications déclarés

| # | Écart | Traitement |
|---|---|---|
| **R-15** | Budget C4 R-04 : `DIRECTION/START` est servi en 76 lignes. La ligne en trop est le séparateur `---` de fin de section, pas du contenu (12.05c §3) | **Décision de l'owner** : le budget du harnais C4 passe de 75 à 76. L'empreinte du harnais est déclarée avec `--rectifies C4`. Aucun outil ne change |
| Nommage | En 12.03 et 12.05c, j'ai appelé ce point de budget « R-4 », alors que **R-4 désigne déjà en 11.23** une rectification d'ordre (D4 O-1 dans le cycle de garde) | Le point de budget s'appelle désormais **« budget C4 R-04 »**, et sa résolution **R-15**. Les rapports antérieurs ne sont pas réécrits : cette note fait foi |
| Sauvegarde `.dist.previous` | Le validateur l'aurait signalée comme « fichier inattendu » après un échec de promotion | Elle est exclue **à la racine seulement**, comme `dist` et `.build`, par cohérence avec C8 O-4. C'est une extension minimale, déclarée |
| Sauvegarde et `dist` présents ensemble | E2 O-3 interdit de supprimer une sauvegarde | Le build s'arrête et demande une résolution manuelle. Il ne supprime rien |
| Versions des actions | La décision fixait une règle (SHA complet, `node24`), pas de version | J'ai retenu la dernière version publiée de chaque action, v7.0.1 et v7.0.0. Les entrées utilisées (`python-version`) existent dans ces versions |
| « Date de publication » | V1.1.0 est une candidate que l'owner n'a pas encore publiée | Le CHANGELOG et RELEASE_NOTES disent « Date de la version ». La date de publication de V1.0.0 est conservée dans sa section |

**Journal des notes de version, ligne ajoutée :**

> 12.06 — Build atomique (archives dans le répertoire de travail, contrôle des membres, promotion transactionnelle), liens symboliques refusés, exclusions limitées à la racine ; manifeste sans doublon et version unique ; lectures non UTF-8, clés JSON répétées et types illégaux refusés proprement ; `validate_all.py` lançable depuis n'importe quel dossier ; chemins propres à l'export Local ; actions du workflow épinglées par SHA (node24). Version V1.1.0.

---

# Partie B — 12.07 : sortie de la phase 12

## B.1 Unités

| Unité | Étiquette | Commit | Contenu |
|---|---|---|---|
| 12.00 | `12.00-B03-ouverture` | `cf0af4f` | B03, copie conforme de B01 (60/60) |
| 12.01 | `12.01-A1` | `33db0da` | Autorité du schéma |
| 12.02 | `12.02-A2` | `3bae037` | Oracles de test |
| 12.03 | `12.03-garde` | `5ebdd3d` | Cycle de garde : résolveur, validateur de carte, 21 LCF, `SEED` |
| 12.04 | `12.04-migration` | `8eb95da` | Migration unique : 48 invariants, contrats, données |
| 12.05a | `12.05a-changelog-bibliotheque` | `d537083` | CHANGELOG, BIBLIOTHEQUE |
| 12.05b | `12.05b-action` | `c59783f` | ACTION |
| 12.05c | `12.05c-textes-facades` | `6de1f9b` | DIRECTION, SAVOIR, cartes, glossaire, façades ; fenêtre de garde fermée |
| 12.06 | `12.06-outils-v1.1.0` | `a6eeca8` | Outils, version V1.1.0 |

**Trajectoire des cas verts significatifs :** 3 → 14 → 19 → 27 → 149 → 160 → 190 → 282 → **300/300**. Il n'y a jamais eu de régression ni de témoin rouge hors de la fenêtre de garde.

## B.2 Critères de sortie

| Critère (11.23, 12.00) | État |
|---|---|
| Toutes les corrections décidées en phase 11 sont appliquées dans la passe de leur propriétaire, dans l'ordre de 11.23 §7 | **Tenu.** A1, A2, B1 à B5, C1 à C9, D1 à D4, E1 et E2. L'oubli de B4 T-5 en 12.05b a été rattrapé en 12.05c |
| Aucune correction non décidée | **Tenu.** Les écarts de rédaction sont déclarés unité par unité. Les incohérences relevées hors décision ne sont pas corrigées (B.3) |
| Chaque invariant nouveau a son cas unitaire et son motif (A2) | **Tenu** : 76 cas RUN_CARD, 20 cas contrats |
| Harnais rouge → vert, témoins toujours verts | **Tenu** : 300/300, 40/40 |
| Un harnais ne change que par rectification déclarée | **Tenu** : R-8 à R-15, chacune avec son motif ; B01 reste rouge sur chaque harnais rectifié |
| B01 intacte, B02 gelée | **Tenu** : 218/218 à chaque unité ; B02 non utilisée |
| Aucun verdict global | **Tenu** : ce rapport décrit l'état de la phase 12, pas la qualité du système |

**Phase 12 : terminée.** Ce n'est pas un verdict : cela veut dire que le patch décidé est appliqué et que ses gardes de forme sont vertes. Les effets restent à éprouver en phase 13.

## B.3 Réserves transmises aux phases 13 et 14

| # | Réserve | Nature | Ce qui la lèverait |
|---|---|---|---|
| 1 | **Run CI hébergé** du workflow épinglé | `NOT-VERIFIED` (F-WF-001) | Un run vert sur GitHub, lancé par l'owner, avec son lien |
| 2 | **Environ 14 invariants existants sans cas négatif** (12.02 §2.2) | Réserve décidée par l'owner le 26 septembre | Une décision future d'ajout |
| 3 | **Trois incohérences relevées, non corrigées :** QUICKSTART 45 et skill 103 (« deux anti-directions, une tension ») ; table d'architecture de DIRECTION (« preuve ») ; redondance `PILOT` dans BIBLIOTHEQUE | Hors décision de phase 11 | Une PATCH-DECISION |
| 4 | **Seize limites déclarées** par les grappes (11.23 §3.4) : une garde prouve une **forme**, pas un **effet** | Bornes de la preuve | Les épreuves de la phase 13 |
| 5 | **Efficacité sur des runs réels** | `NOT-VERIFIED`, déclaré dans le package | Épreuves de la phase 13 menées par un observateur qui satisfait les critères D3. Sans lui : auto-comparaison différée, aucune clôture FULL |
| 6 | F-DIR-044 (blocs extraits trop larges) | Non traité (Lot 1) | À résoudre avant la conception des pilotes (plan maître) |
| 7 | La promesse du validateur liste ce que la machine **n'atteste pas** (observations réelles, justesse des jugements, portée réelle des claims, identité de l'autorisant, droits, fraîcheur d'une ancre, qualité perceptuelle, consumers réels, baseline, paire équivalente) | Limite de conception, assumée | Trace, revue et owner |
| 8 | LCF-21 détecte deux formulations précises seulement | Limite déclarée (D4) | Revue bornée de release |
| 9 | V1.1.0 est une **candidate** construite et contrôlée, **non publiée** | État | Publication par l'owner |

## B.4 Suite : phase 13, valider

Le plan maître prévoit une validation à cinq couches (texte, contrats, machine, distributions, non-régression) et les épreuves d'efficacité. **Je propose deux unités :**
- **13.01, validation des cinq couches.** Pour chaque correction, on vérifie que la preuve verte **couvre bien le défaut corrigé** : c'est l'exigence du plan (« une validation verte qui ne couvre pas le défaut corrigé n'est pas une preuve suffisante »). L'unité produit une matrice fiche → garde → cas, sur B03 V1.1.0.
- **13.02, épreuves d'efficacité.** Elles comprennent la mesure M de C7, l'épreuve d'imitation de C6, l'épreuve « un run, une revue » de D1 et les épreuves de lecture. Chacune déclare son observateur selon D3. Sans observateur indépendant, elles sont conduites en **auto-comparaison différée**, avec réserve, comme convenu.

Puis la **phase 14**, clôture, en une unité.
