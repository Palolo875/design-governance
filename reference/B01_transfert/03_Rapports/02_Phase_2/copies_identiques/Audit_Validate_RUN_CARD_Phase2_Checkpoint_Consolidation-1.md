# DG-AUDIT-001 — Phase 2 — Checkpoint cumulatif du validateur RUN_CARD

## Fonction, méthode et intégrité

Cette synthèse consolide la lecture **complète des 590 lignes** de `audit_work/package/scripts/validate_run_card.py`. Elle reprend les quatre diagnostics sectionnels, les rapproche du checkpoint des 25 fixtures et vérifie l'interface avec le lanceur `validate_all.py` et le workflow. Il s'agit d'un checkpoint **provisoire de phase 2**, sans verdict système, décision de patch ni approbation d'une carte réelle. Le protocole externe v2.0 §12 a été relu : passages A (architecture), B (contrat), C (lecteurs) et D (résistance). Les contre-épreuves détaillées restent dans les rapports de plage ; cette synthèse n'en remplace pas les sources.

| Plage contiguë | Objet principal | Rapport de preuve et SHA-256 |
|---|---|---|
| 1–149 | Sous-ensemble JSON Schema, chargement, diagnostic `HELD` | `Audit_Validate_RUN_CARD_Phase2_01_Chargement_Schema_Diagnostic_HELD.md` — `6a59f2abb6bfc8a6d4162a5b452ad189e159f838f16da67246fc46154fa87cdb` |
| 150–326 | Métier, direction, preuve, risques, strict | `Audit_Validate_RUN_CARD_Phase2_02_Contrat_Metier_Mode_Strict.md` — `acbdf852093da1cb7f9f7de3c8fb63b3338e54274579c806300f4acd8119c5a4` |
| 327–381 | Assemblage, oracles, contrôle d'autorité, fichier ciblé | `Audit_Validate_RUN_CARD_Phase2_03_Assemblage_Oracles_Cible.md` — `9cb3c5ffac2197d5bbc95cb7927b9b4afd807ecb4d412e3ccee209586dd36114` |
| 382–590 | CLI, suite intégrée, gestion du schéma | `Audit_Validate_RUN_CARD_Phase2_04_CLI_Suite_Schema_Manquant.md` — `28be73abb8a10939489d0f003a8d3cf324fc5ae60346f3731bd7a9e79f7ea317` |
| **Total** | **1–590/590, aucune ligne manquante ni chevauchement** | Quatre rapports A–D |

Baseline `B01` recalculée et stable : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. La suite autonome normale rend aujourd'hui **code 0, `RUN_CARD VALIDATION PASSED`**. Aucun fichier du package audité n'a été modifié pour ce checkpoint.

## Passage A — décisions et couverture exercées

`load_json` lit la projection ; `validate_card` applique dans l'ordre le diagnostic `HELD`, le contrat métier, le contrôle strict facultatif, puis le sous-ensemble de schéma. `check_fixture` pilote des cas positifs et négatifs ; `check_schema_authority` vérifie qu'un mode ajouté dans une copie du schéma est accepté ; `main` distingue fichier ciblé et suite autonome. Cette architecture valide une **forme déclarée** et certains enchaînements, sans observer l'artefact livré, les tests utilisateurs, la fraîcheur réelle de la preuve ou l'autorité d'une décision.

La suite autonome appelle **25 fois** `check_fixture` : l'exemple officiel et **24 des 25** fichiers du dossier, soit **21 négatifs** et **trois positifs** ; **20 des 21** négatifs appelés exigent un fragment de diagnostic. Les 22 négatifs sur disque échouent chacun en ciblé et les trois positifs passent ; **17 des 22** négatifs ont plus d'un défaut après réparation du défaut annoncé. Elle n'exécute pas automatiquement `--strict` sur les fixtures. Le succès normal de la baseline confirme ces appels seulement.

**Rectification de portée après recoupement inter-scripts :** F-FIX-001 signifie que `invalid_capability_profile_missing_basis.json` manque à la suite **propre à `validate_run_card.py`**, non qu'elle n'est jamais exécutée par le package. `validate_all.py` lignes 51–60 l'appelle explicitement par CLI et `expect_failure` contrôle un code non nul et l'absence de traceback, **sans exiger la raison de l'échec**. Le workflow `.github/workflows/validate.yml` lance `python3 scripts/validate_all.py` sur `push` et `pull_request`. Si ce workflow est réellement exécuté, il atténue le trou de lancement ; il ne protège pas l'invariant ciblé contre un autre motif de rejet, notamment la provenance composite de cette fixture. Les détails de l'orchestrateur et de sa disponibilité dans les distributions attendent son audit complet.

## Passage B — huit constats propres au validateur, garanties à préserver

| ID provisoire | Preuve et impact observé | Owner pressenti ; test discriminant à préparer |
|---|---|---|
| F-VRC-001 | Deux clés JSON identiques sont consommées avec la dernière valeur (`json.loads`) ; une carte dont le premier `mode` est illégal peut être acceptée une fois celui-ci écrasé. | Entrée/parsing ; détecter le doublon avant la construction de l'objet, tester plusieurs profondeurs et préserver un JSON ordinaire valide. |
| F-VRC-002 | Un octet UTF-8 invalide provoque `UnicodeDecodeError` et traceback CLI, sans bannière `FAILED`. | Chargement/diagnostic ; erreur de lecture contrôlée, code non nul, chemin lisible. |
| F-VRC-003 | `mode=[]`, `closure.issue=[]`, éléments objets dans `proof.observed`, ou URL de trace `https://[` en strict provoquent `TypeError`/`ValueError` avant le rejet structuré. | Frontière type/contrat métier/strict ; tous ces cas doivent échouer avec diagnostic gouverné, sans relâcher le contrôle du schéma. |
| F-VRC-004 | En strict, `https://example.invalid/artefact-demo` dans `artifact.locator` passe alors que le même hôte dans `trace_locator` est rejeté. | Validation des locators stricts ; test côte à côte artefact/trace, URL authentique admissible selon politique choisie. |
| F-VRC-005 | `./artifact.png` placé à côté d'une carte externe est résolu contre `ROOT` et rejeté ; le chemin absolu du même fichier passe, `source_path` n'est pas utilisé. | Résolution des chemins ; tester carte externe, interne, absolu et `file://` avec une règle explicite. |
| F-VRC-006 | Désactiver en mémoire seulement l'enum principal du mode permet `BOGUS-MODE` : l'auto-contrôle positif de l'enum et toute la suite restent verts. La baseline actuelle rejette correctement le mode inconnu. | Oracle de régression ; voisin négatif de mode illégal, preuve que la protection est perdue puis restaurée. |
| F-VRC-007 | Si le schéma vaut `{}`, `main` saute lecture cible et suite, puis annonce code 0 `PASSED`, y compris pour une carte invalide et `--strict`. | Chargement préalable du schéma ; schéma vide/inopérant doit produire un échec contrôlé avant toute annonce de validation. Risque provisoire prioritaire de faux succès. |
| F-VRC-008 | Schéma absent : erreur collectée mais `schema` non initialisé, `UnboundLocalError` ; schéma `{"type":"object"}` : `KeyError` dans le contrôle d'autorité. | Prévalidation du schéma et sortie CLI ; échec lisible, code non nul, sans traceback. Distinct de F-VRC-007 par résultat effectif. |

Préserver les propriétés actuellement vérifiées : exemples valides, champs et enums utiles, `HELD` hors `closure.state`, obligations conditionnelles de trace pour STANDARD/SYSTÈME/DIRECTION, besoin de preuve non vide, provenance structurée sous acceptation, risque critique avec protection non placeholder et refus de `LOST-IN-BUILD` accepté. Préserver explicitement `CLOSED + RETURNED + RETURN` et la DIRECTION exploratoire avec ancre non transformée. Pour F-RC-001, un retour motivé par une autre preuve doit pouvoir garder une **ancre réellement transformée**, sans accepter pour autant une ancre réellement non transformée.

## Passage C — conséquences selon le lecteur

| Lecteur | Ce qu'il reçoit aujourd'hui | Frontière ou vérification nécessaire |
|---|---|---|
| Intégrateur soumettant une carte | Code et message ciblés quand une `ValidationError` est capturée ; contrôle strict sur demande. | Ne pas interpréter un code 0 sans assurance de schéma chargé et fichier réellement lu ; locators externes et chemins relatifs exigent une convention cohérente. |
| Mainteneur et CI | Suite native avec vingt diagnostics attendus ; suite supérieure appelle quatre cas CLI négatifs et teste aussi build/reproductibilité. | Un négatif composite peut échouer pour la mauvaise raison ; F-FIX-001 est déclenchée dans `validate_all.py` mais sans diagnostic ciblé, F-FIX-003 n'est gardée que par « erreur quelconque » dans la suite native. |
| Designer et reviewer | Carte structurée avec mode, risque, ancre, conséquence et preuve déclarée. | Une chaîne de provenance ne remplace ni capture datée, ni contrôle réellement exécuté, ni jugement sur une direction. |
| Owner ACTION/DIRECTION/SAVOIR | Projections de la décision, du statut de direction et du profil. | Les constats de sens restent propriétaires de leurs sources : ne pas attribuer au script la définition de la décision ou de la qualité. |

## Passage D — non-fusions, priorités et programme

Le registre reste à **129 constats provisoires** : 101 des cinq propriétaires, 16 des façades et contrats précédents, un F-RC-001, trois F-FIX-001 à 003 et huit F-VRC-001 à 008. F-FIX-001 est limité à la suite native et **atténué par l'appel de l'orchestrateur**, sans oracle de motif. F-FIX-002 porte les cas composites ; F-FIX-003, le négatif appelé sans diagnostic attendu ; F-VRC-006, l'autorité non protégée de l'enum. F-VRC-007 (faux PASS) et F-VRC-008 (exceptions brutes) peuvent partager un correctif mais ont des critères de test différents. F-RC-001 reste distinct provisoirement de F-ACT-010 ; les limites de mode, preuve, version, trace, risque et profil renvoient aux F-DIR/F-ACT/F-SAV déjà ouverts. Gravité et fusion finales relèvent des phases 10–11. **Aucun patch du package et aucun verdict global en phase 2.**

Inventaire des scripts d'intégration encore à lire entièrement : `validate_all.py` **97** lignes, `validate_contracts.py` **218**, `validate_design_governance.py` **229**, `validate_reading_map.py` **105**, `read_route.py` **86**, `package_manifest.json` **124**, `build_distributions.sh` **166**, et workflow `.github/workflows/validate.yml` **22**. Leur lecture suit les dépendances : commencer par **`validate_all.py` 1–97/97**, car il relie la fixture F-FIX-001 aux appels CLI, au contrôle des exceptions, à la compilation, au build et à la reproductibilité ; relire §12, ce checkpoint et la source exacte, puis simuler A–D. Ne pas lancer directement ce script pour une simple lecture : ses lignes 84–89 reconstruisent deux fois les archives dans le package. Examiner ensuite les validateurs de contrats et documentaires, le lecteur de routes, le manifeste/build et le workflow, puis skill, release notes et distributions selon le plan maître. Les résultats de F-FIX-001, F-VRC-006/007/008 et les positifs pertinents devront être transportés, sans convertir une analyse de code en preuve d'exécution du workflow hébergé.

Condition de reprise : ouvrir plan, ce checkpoint et le rapport de la plage 4 ; recalculer B01 ; relire protocole §12, puis `validate_all.py` complet et ses interfaces. Après cette unité, enregistrer le rapport, vérifier IDs, garanties et prochaine cible. Phase 2 ouverte.
