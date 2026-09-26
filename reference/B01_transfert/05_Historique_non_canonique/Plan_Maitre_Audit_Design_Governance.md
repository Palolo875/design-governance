# Plan maître — Audit complet de Design Governance V1

## Fonction de ce document

Ce fichier est le point de reprise durable de la campagne `DG-AUDIT-001`. Il ne remplace ni le protocole, ni les sources, ni les rapports de preuve. Il indique :

- où nous sommes ;
- ce qui a été lu ;
- ce qui reste à lire ;
- quand chaque phase peut commencer ;
- quels artefacts font foi ;
- comment reprendre après compaction, nouvelle session ou perte du contexte conversationnel.

Le protocole externe reste la source de méthode. Le package Design Governance reste la cible. Aucun résumé, y compris ce plan, ne remplace la relecture d’une source lorsqu’une conclusion en dépend.

## Baseline active

- Audit : `DG-AUDIT-001`
- Profil : `DEEP`, avec profondeur adaptative par cible
- Baseline : `B01`
- Système compilé : `Design_Governance_V1.0.md`
- Hash système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`
- Protocole : `Protocole maître d’audit — Design Governance`, version 2.0
- Hash protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`
- Règle actuelle : aucun patch avant lecture complète du périmètre et diagnostic propriétaire

## Situation actuelle

| Élément | État |
|---|---|
| Phase 0 — cadrage | Terminée |
| Phase 1 — baseline | Terminée ; hashes B01 stables |
| Phase 2 — lecture complète | En cours |
| `DIRECTION.md` | Lecture complète, 10 rapports, checkpoint consolidé |
| Constats DIRECTION | F-DIR-001 à F-DIR-046, tous provisoires jusqu’aux phases ultérieures |
| `ACTION.md` | Lecture complète, 12 rapports et `Audit_ACTION_Phase2_Checkpoint_Consolidation.md` |
| Constats ACTION | F-ACT-001 à F-ACT-039, provisoires ; dépendances DIRECTION, SAVOIR, BIBLIOTHEQUE, standards externes et machine transportées |
| `SAVOIR.md` | Lecture sectionnelle complète, quinze blocs et 941 lignes ; rapports `Audit_SAVOIR_Phase2_01_Responsabilite_Autorite_Routage.md` à `Audit_SAVOIR_Phase2_15_Regles_Or_Methodologie_Studio.md` ; `Audit_SAVOIR_Phase2_Checkpoint_Consolidation.md` terminé |
| Constats SAVOIR | F-SAV-001 : plafond implicite de routes ; F-SAV-002 : prescription possible de neutres/accent ; F-SAV-003 : revue indépendante susceptible de remplacer à tort calibration externe ou réserve d’ancre générée ; F-SAV-004 : route SAVOIR/SYSTEM omise dans la famille structure/composant partagé de l’atlas ; F-SAV-005 : `PROFILE-DECISION` confond intention et décision observée ; F-SAV-006 : test de masquage invalide potentiellement un style porté par image ou couleur ; F-SAV-007 : reclassification SYSTÈME fondée sur un impact partagé sans distinguer l’objet direct du run ; F-SAV-008 : filtre CONTEXT trop étroit pour motion narrative ou scène spatiale porteuse d'une direction ; F-SAV-009 : exigences d'approbation et de dossier appliquées indistinctement aux scripts locaux sans dépendance et packages externes ; F-SAV-010 : règle rapide pouvant faire déclarer la spec DIRECTION non applicable malgré son obligation propriétaire ; tous provisoires |
| `BIBLIOTHEQUE.md` | Lecture sectionnelle **complète**, 791 lignes et 15 rapports `Audit_BIBLIOTHEQUE_Phase2_01_Responsabilite_Entree_READ.md` à `Audit_BIBLIOTHEQUE_Phase2_15_Test_Sortie_Selection.md` ; checkpoint `Audit_BIBLIOTHEQUE_Phase2_Checkpoint_Consolidation.md` terminé ; F-BIB-001 (exception B1b), F-BIB-002 (frontière local/contrat réduit, occurrence MICRO 550), F-BIB-003 (champs MOBILE de GRID hors scope), F-BIB-004 (contrat structurel de composant partagé promis mais absent dans COMPONENTS), F-BIB-005 (test d'ablation imposant une refonte structurelle malgré média ou contenu porteur), tous provisoires |
| `CHANGELOG.md` | Lecture propriétaire **complète**, 63 lignes, rapport `Audit_CHANGELOG_Phase2_01_Baseline_Autorite_Cycle_Migration_Limites.md` ; F-CHG-001 provisoire : statut initial des routes seed et dépréciation d'un PILOT avec consumers non résolus par les transitions ; rapport unique tenant lieu de checkpoint de cette source courte |
| Consolidation des cinq propriétaires | `Audit_Phase2_Checkpoint_Cinq_Proprietaires_Interfaces.md` terminé ; cinq sources 3 548 lignes, 101 IDs provisoires continus (46 DIR + 39 ACT + 10 SAV + 5 BIB + 1 CHG) ; chaînes d'épreuve et non-fusions transportées ; aucune décision finale |
| `QUICKSTART.md` | Lecture et checkpoint de façade **terminés en phase 2** : 313/313 lignes, neuf rapports, plages 1–313 adjacentes, `Audit_QUICKSTART_Phase2_Checkpoint_Consolidation.md` ; F-QS-001/002/003/004 maintenus provisoirement avec atténuations et tests ; cinq liens propriétaires corrects dans la source ; 101 propriétaires + quatre QS = **105 fiches provisoires** |
| `READING_MAP.md` | Lecture complète **1–127/127**, rapport `Audit_READING_MAP_Phase2_01_Carte_Complete_Routage_Perspectives_Handoff_Locators.md` ; validation documentaire passée, 24 titres principaux exacts, six locators nommés hors table toujours inaccessibles par CLI (F-DIR-028) ; F-RM-001 (RUN-DIRECTION dans ajout conditionnel) et F-RM-002 (a11y hors scope → N/A) provisoires ; 101 propriétaires + quatre QS + deux RM = **107 fiches provisoires** |
| `ORCHESTRATION_MAP.md` | Lecture complète **1–53/53**, rapport `Audit_ORCHESTRATION_MAP_Phase2_01_Combinaisons_Preuve_Variation.md` ; neuf profils confrontés aux propriétaires, 21 titres présents et huit locators non servis par CLI (F-DIR-028) ; F-OM-001 (minima ACTION en renfort facultatif) et F-OM-002 (variation « un axe à la fois ») provisoires ; **109 fiches provisoires** au total |
| `GLOSSAIRE.md` | Lecture complète **1–71/71**, rapport `Audit_GLOSSAIRE_Phase2_01_Termes_Statuts_Preuve_Persistance.md` ; 40 définitions et six exemples, deux titres préfixés dont `SAVOIR/STATE` non servi par CLI (F-DIR-028) ; F-GLO-001 (RUN_CARD et persistance) et F-GLO-002 (exemple de réserve accessibilité) provisoires ; **111 fiches provisoires** au total |
| `README.md` officiel | Lecture complète **1–52/52**, rapport `Audit_README_Officiel_Phase2_01_Entree_Autorite_Liens_Promesses.md` ; neuf liens valides, cinq responsabilités conformes, cinq contrats annoncés présents et validateur de contrats vert avec limites ; intensité annoncée par la carte à tester comme imprécision possible, **aucun nouvel ID**, registre toujours **111 provisoires** |
| Contrat machine `DOMAIN_FRAME` | Schéma **1–15/15** et exemple **1–24/24** lus A–D, rapport `Audit_DOMAIN_FRAME_Phase2_01_Schema_Exemple_Couverture_Preuve.md` ; exemple officiel passe, six copies en mémoire révèlent une liaison textuelle partielle des risques/contrôles et un plan de preuve seulement non vide ; F-DF-001/002 provisoires ; **113 fiches provisoires** |
| Contrat machine `RESEARCH_BRIEF` | Schéma **1–39/39** et exemple **1–24/24** lus A–D, rapport `Audit_RESEARCH_BRIEF_Phase2_01_Schema_Exemple_Sources_Incertitude.md` ; exemple officiel passe, onze copies en mémoire montrent un défaut de transport de source vérifiable et le couplage de profondeur, entrée et incertitude ; F-RB-001/002 provisoires ; **115 fiches provisoires** |
| Contrats machine de production | Schéma **1–12/12** et exemple **1–42/42** lus A–D, rapport `Audit_PRODUCTION_CONTRACTS_Phase2_01_Schema_Exemple_Trois_Objets.md` ; exemple officiel passe, douze variantes en mémoire isolent l'obligation de deux directions même sans alternative utile (F-PC-001) et une fausse liaison dans `coverage_map` par mots dispersés entre lignes (F-PC-002). Les autres limites renforcent F-ACT-005/006/007/008/012/018/021/022 ; **117 fiches provisoires** |
| Contrat machine `RUN_CARD`, segment 1 | Schéma **1–45/180** et exemple **1–18/102** lus A–D, rapport `Audit_RUN_CARD_Phase2_01_Enveloppe_Mode_Risque_Sources.md` ; exemple officiel passe, douze variantes en mémoire reproduisent F-DIR-007 et F-ACT-017/028 sans nouvel ID ; **117 fiches provisoires**, reste du contrat à lire |
| Contrat machine `RUN_CARD`, segment 2 | Schéma **46–97/180** et exemple **19–65/102** lus A–D, cumul adjacent schéma 1–97/180 et exemple 1–65/102 ; rapport `Audit_RUN_CARD_Phase2_02_Direction_Ancres_Artefact_Capacites.md` ; exemple ordinaire passe, mode strict refuse ses placeholders, des copies en mémoire isolent le refus d'une ancre réellement transformée dans un run exploratoire/retourné : **F-RC-001 provisoire, 118 fiches provisoires** |
| Contrat machine `RUN_CARD`, segment 3 | Schéma **98–153/180** et exemple **66–90/102** lus A–D, cumul adjacent schéma 1–153/180 et exemple 1–90/102 ; rapport `Audit_RUN_CARD_Phase2_03_Preuve_Provenance_Close_Decision.md` ; exemple ordinaire passe, quinze variantes en mémoire confirment les garde-fous et les limites F-ACT-012/013/018/022/025/034 et F-SAV-005, sans nouvel ID : **118 fiches provisoires** |
| Contrat machine `RUN_CARD`, segment 4 | Schéma **154–180/180** et exemple **91–102/102** lus A–D, cumul complet schéma **180/180** et exemple **102/102** ; rapport `Audit_RUN_CARD_Phase2_04_Cloture_Conditions_Finales.md` ; exemple + trente mutations en mémoire confirment protections et écarts déjà ouverts F-ACT-009/010/011/012/013/020/021/023 et F-RC-001 ; **aucun nouvel ID, 118 fiches provisoires** |
| Checkpoint cumulatif `RUN_CARD` | `Audit_RUN_CARD_Phase2_Checkpoint_Consolidation.md` terminé : quatre plages adjacentes schéma **180/180**, exemple **102/102**, protections réelles et matrice lacunes/owners/preuves ; F-RC-001 distinct provisoirement de F-ACT-010 ; **118 fiches provisoires** |
| Fixtures `RUN_CARD`, plage 1 | Huit premières fixtures **1–8/25** lues intégralement A–D, rapport `Audit_RUN_CARD_Fixtures_Phase2_01_Acceptation_Capacite_Close.md` ; huit rejets ciblés avec diagnostics adéquats, cinq scénarios à double invalidité ; `invalid_capability_profile_missing_basis.json` est la seule des 25 absente de la suite native du validateur (la suite supérieure l'appelle sans vérifier le motif, précision établie au checkpoint du validateur) : **F-FIX-001 provisoire, 119 fiches provisoires à cette étape** |
| Fixtures `RUN_CARD`, plage 2 | Fixtures **9–16/25** lues intégralement A–D, rapport `Audit_RUN_CARD_Fixtures_Phase2_02_Risque_Direction_Preuve.md` ; huit rejets ciblés et huit diagnostics attendus enregistrés, mais chaque correction ciblée rencontre une autre invalidité ; **13/16** cas des deux plages cumulant des défauts, F-FIX-002 provisoire, **120 fiches provisoires** |
| Fixtures `RUN_CARD`, plage 3 | Fixtures **17–25/25** lues intégralement A–D, rapport `Audit_RUN_CARD_Fixtures_Phase2_03_Exceptions_Verdicts_Cas_Valides.md` ; six négatifs rejetés avec diagnostic voulu, trois positifs acceptés ; **17/22** négatives cumulant des invalidités et **24/25** fichiers appelés par la suite ; F-FIX-001/002 et F-RC-001 conservés, **120 fiches provisoires** |
| Checkpoint cumulatif fixtures `RUN_CARD` | `Audit_RUN_CARD_Fixtures_Phase2_Checkpoint_Consolidation.md` terminé : 25/25 noms, fichiers et hashes revérifiés ; une empreinte de fixture corrigée dans la plage 2 et l'empreinte de l'exemple complétée dans six rapports antérieurs ; 22 rejets et trois acceptations ciblés, suite intégrée verte ; **24/25** appelés, **20/21** négatifs inscrits ont un diagnostic attendu, **17/22** négatifs sont composites. `invalid_missing_proof.json` est appelée sans diagnostic attendu ; mutation en mémoire confirmant le faux succès de l'oracle, **F-FIX-003 provisoire, 121 fiches provisoires**. Le rapport de plage 3 a été rectifié. |
| Validateur RUN_CARD, plage 1 | Lignes **1–149/590** lues A–D, rapport `Audit_Validate_RUN_CARD_Phase2_01_Chargement_Schema_Diagnostic_HELD.md` ; sous-ensemble de schéma confronté à ses deux `if`, à `anyOf`, aux types/enum/chaînes et au diagnostic `HELD` ; F-VRC-001 (clés JSON répétées perdues) et F-VRC-002 (UTF-8 invalide non converti en diagnostic) ouverts provisoirement, **123 fiches provisoires**. |
| Validateur RUN_CARD, plage 2 | Lignes **150–326/590** lues A–D, rapport `Audit_Validate_RUN_CARD_Phase2_02_Contrat_Metier_Mode_Strict.md` ; contrôles métier et strict confrontés aux cas positifs et à leurs mutations en mémoire ; F-VRC-003 (exceptions brutes sur entrées invalides), F-VRC-004 (artefact sur URL de démonstration accepté en strict) et F-VRC-005 (artefact relatif ancré sur le package) ouverts provisoirement, **126 fiches provisoires**. F-RC-001 et constats ACTION conservés sans duplication. |
| Validateur RUN_CARD, plage 3 | Lignes **327–381/590** lues A–D, rapport `Audit_Validate_RUN_CARD_Phase2_03_Assemblage_Oracles_Cible.md` ; ordre métier/strict/schéma, oracles positifs et négatifs, erreurs ciblées contrôlées ; une mutation en mémoire désactivant **seulement l'enum principal du mode** laisse `check_schema_authority` et la suite intégrée verts tout en acceptant un mode inconnu : **F-VRC-006 provisoire, 127 fiches provisoires**. F-FIX-003 et F-VRC-002/003 confirmés. |
| Validateur RUN_CARD, plage 4 | Lignes **382–590/590** lues A–D, rapport `Audit_Validate_RUN_CARD_Phase2_04_CLI_Suite_Schema_Manquant.md` ; 25 appels dont l'exemple officiel et 24/25 fixtures sur disque, 20/21 négatives appelées avec diagnostic attendu ; branches CLI et codes de sortie vérifiés ; schéma `{}` → **succès sans validation** (F-VRC-007), schéma absent ou incomplet → exception brute (F-VRC-008). **129 fiches provisoires** ; quatre plages adjacentes couvrent 590/590 lignes. |
| Checkpoint cumulatif du validateur RUN_CARD | `Audit_Validate_RUN_CARD_Phase2_Checkpoint_Consolidation.md` terminé : quatre plages adjacentes **1–590/590**, huit F-VRC provisoires et protections positives consolidées ; B01 stable, suite autonome verte. Recoupement avec `validate_all.py` et le workflow : F-FIX-001 manque à la suite **native** mais est appelée par la suite supérieure avec oracle code non nul/absence de traceback, sans diagnostic ciblé. **129 fiches provisoires**, aucune correction normative. |
| Prochaine cible | Lecture complète **1–97/97 de `validate_all.py`**, puis les autres scripts d'intégration et leur chaîne build/workflow |
| Phases 3–14 | Non ouvertes formellement au niveau système |
| Patches système | Aucun |

Les cinq sources normatives principales sont entièrement lues : **3 548/3 548 lignes** couvertes par leurs rapports sectionnels. Ce 100 % décrit uniquement la lecture de ces cinq textes ; il ne mesure pas l'avancement de l'audit total, car les artefacts dérivés, la machine, les distributions, les épreuves et les autres phases restent à auditer.

## Les quinze phases du protocole

### Phase 0 — Préparer le cycle

But : définir la cible, l’échelle, la source canonique, l’owner, les consommateurs, les dépendances, les non-goals, le scope, le risque dominant, la preuve attendue et la condition de sortie.

Sortie : `AUDIT-FRAME`.

État : **terminée pour la campagne globale**. Elle sera rappelée brièvement au début de chaque sous-cible sans créer un nouvel audit concurrent.

### Phase 1 — Établir la baseline

But : capturer l’état réel avant correction — version, hash, lignes, titres, routes, schémas, fixtures, validateurs, distributions et divergences.

Sortie : `BASELINE + DIVERGENCES`.

État : **terminée pour B01**. Les hashes sont revérifiés avant chaque bloc important. Toute modification inattendue suspendrait l’analyse jusqu’à rebaselining.

### Phase 2 — Lire entièrement le périmètre

But : lire les sources et interfaces avant le diagnostic final, avec quatre passages :

1. architecture visible ;
2. contrat sémantique ;
3. usage réel simulé ;
4. résistance active aux ambiguïtés, contradictions, contournements et répétitions.

Sortie : `READING-MAP + SECTIONAL-DIAGNOSTIC`.

État : **en cours**.

Ordre restant de la phase 2 :

1. `ACTION.md` — 935 lignes, 12 blocs et checkpoint achevés ;
2. checkpoint ACTION — `Audit_ACTION_Phase2_Checkpoint_Consolidation.md` ;
3. `SAVOIR.md` — 941 lignes, 15 blocs de lecture terminés ;
4. checkpoint SAVOIR — `Audit_SAVOIR_Phase2_Checkpoint_Consolidation.md`, achevé ;
5. `BIBLIOTHEQUE.md` — 791 lignes, quinze blocs et checkpoint terminés ;
6. checkpoint BIBLIOTHEQUE — `Audit_BIBLIOTHEQUE_Phase2_Checkpoint_Consolidation.md` ;
7. `CHANGELOG.md` — 63 lignes, rapport propriétaire complet tenant lieu de checkpoint ;
8. consolidation des cinq propriétaires normatifs — `Audit_Phase2_Checkpoint_Cinq_Proprietaires_Interfaces.md` achevé ;
9. façades et documents dérivés : QUICKSTART 1–313 lu en neuf blocs et checkpoint consolidé ; READING_MAP 1–127, ORCHESTRATION_MAP 1–53, GLOSSAIRE 1–71 et README officiel 1–52 lus intégralement ; **616/616 lignes** de ces cinq documents d'entrée ;
10. contrats machine : schémas, exemples et fixtures ; DOMAIN_FRAME, RESEARCH_BRIEF et contrats de production schémas+exemples lus ; RUN_CARD schéma 1–180/180 et exemple 1–102/102 lus en quatre plages A–D, checkpoint cumulatif achevé ; fixtures 1–25/25 lues et checkpoint cumulatif achevé ;
11. scripts : lecteurs, validateurs, build, manifeste et workflow ;
12. skill pratique et ses références ;
13. release notes, package racine et mémoire de migration ;
14. distributions GitHub et Local, comparaison à la source et reproductibilité ;
15. checkpoint final de phase 2.

Chaque cible reçoit une profondeur `LIGHT`, `TARGETED`, `FULL`, `N/A-JUSTIFIED` ou `ESCALATED`. Les copies et distributions ne seront pas traitées comme sources propriétaires.

### Phase 3 — Cartographier les rôles

But : déterminer, pour chaque cible, propriété, décision, exécution, preuve, jugement, coordination, lecture, mémoire et garde-fou. Ajouter si nécessaire input, output, owner, escalade, non-goal, prochaine preuve et condition de sortie.

Sortie : `ROLE-MAP`.

État : **en attente de la fin de la phase 2**. Les rapports actuels contiennent des indices d’ownership, mais ils ne constituent pas encore la carte système finale.

### Phase 4 — Auditer les contrats

But : vérifier responsabilité, entrée, transformation, sortie, preuve, escalade et mémoire.

Sortie : `CONTRACT-DIAGNOSTIC`.

État : **en attente**. Les interfaces prioritaires seront DIRECTION → ACTION, DIRECTION → SAVOIR, DIRECTION → BIBLIOTHEQUE, ACTION → RUN_CARD, schémas → validateurs et sources → distributions.

### Phase 5 — Auditer l’architecture de l’information

But : tester façade, hiérarchie, chargement conditionnel, navigation, charge cognitive et relation façade/source.

Sortie : `INFORMATION-ARCHITECTURE-DIAGNOSTIC`.

État : **en attente formelle**. Plusieurs preuves préliminaires existent déjà, notamment l’entrée prioritaire tardive, les vues concurrentes et les routes non résolues.

### Phase 6 — Auditer la capacité positive

But : vérifier non seulement ce que le système empêche, mais ce qu’il permet de produire de meilleur : présence, point de vue, spécificité, composition, matière/type, désirabilité située, résolution, retenue, habitabilité et transfert.

Sortie : `POSITIVE-CAPABILITY-DIAGNOSTIC`.

État : **en attente formelle**. Les qualités positives identifiées dans les rapports DIRECTION seront protégées contre toute correction défensive excessive.

### Phase 7 — Auditer les boucles de création et de gouvernance

But : éprouver la boucle créative, la boucle de gouvernance, le one-shot et la double boucle. Une itération ne compte que si elle change artefact, décision, preuve, portée ou robustesse.

Sortie : `LOOP-DIAGNOSTIC`.

État : **en attente**. F-DIR-009 sur l’itération artificielle sera rejoué ici.

### Phase 8 — Audit multi-perspectives

But : couvrir douze perspectives : création visuelle, produit/usage, accessibilité/inclusion, contenu/communication, technique/runtime, preuve/épistémologie, agentique, équipe, gouvernance, production/opérations, expérimentation et migration.

Sortie : `PERSPECTIVE-COVERAGE-MATRIX`.

État : **en attente**. Chaque perspective recevra un niveau de couverture explicite ; aucune perspective ne disparaîtra silencieusement.

### Phase 9 — Tests de résistance

But : rejouer des scénarios difficiles — brief vague, one-shot, correction locale, direction identitaire, surface opérationnelle, composant partagé, mobile, contenu long, état critique, asset absent, preuve absente, action externe, changement post-verdict, migration, surcharge procédurale et divergence texte/schéma.

Sortie : `RESISTANCE-RESULTS`.

État : **en attente formelle**. Certains scénarios ont déjà servi localement ; ils seront rejoués au niveau système après les cartes de rôles et contrats.

### Phase 10 — Classer les constats

But : attribuer la gravité finale — Bloquant, Majeur, Significatif, Mineur ou Observation — à partir de l’impact réel, avec owner, preuve, risque, recommandation, dépendances, test de non-régression et décision.

Sortie : registre final `FINDINGS`.

État : **en attente**. Les gravités actuelles sont provisoires. Les 46 constats DIRECTION ne seront ni automatiquement conservés, ni automatiquement patchés.

### Phase 11 — Décider s’il faut corriger

But : décider pour chaque constat si une correction apporte un gain réel, appartient bien à la cible, reste proportionnée, évite une nouvelle autorité et possède une preuve testable. Une fusion, suppression ou simplification est préférée à un ajout lorsque suffisante.

Sortie : `PATCH-DECISION`.

État : **en attente**.

### Phase 12 — Appliquer les corrections

But : modifier uniquement la source propriétaire, avec diff attribuable, lisible, réversible, compatible et testable. Les consommateurs ne changent que pour rester alignés.

Sortie : `PATCH + DIFF-REASONING`.

État : **interdite pour l’instant**. Elle ne commencera qu’après les décisions de phase 11.

### Phase 13 — Valider

But : valider à cinq couches : texte, contrats, machine, distributions et non-régression. Une validation verte qui ne couvre pas le défaut corrigé n’est pas une preuve suffisante.

Sortie : `VALIDATION-RESULT`.

État : **en attente**. Les validations actuelles caractérisent B01 ; elles ne valident aucune correction future.

### Phase 14 — Clôturer

But : produire un dossier où cible, source, owner, baseline, couverture, résistances, constats, décisions, validations, réserves, prochaine preuve et condition de sortie sont retrouvables.

Statuts possibles : `AUDIT-PASS`, `AUDIT-PASS-WITH-RESERVATION`, `AUDIT-RETURN`, `AUDIT-NOT-VERIFIED`, `AUDIT-EXPLORATORY`.

État : **en attente**.

## Après la stabilisation documentaire

La clôture documentaire ne démontrera pas à elle seule l’efficacité réelle. Après une stabilisation suffisante :

1. micro-runs contrôlés ;
2. pilotes sur plusieurs contextes ;
3. mesure d’adoption, charge cognitive, temps de décision, erreurs de classification, qualité du premier rendu et corrections réellement utiles ;
4. audit d’efficacité séparé.

Une réussite isolée ne deviendra jamais une preuve générale.

## Prochaine unité de travail

### Orchestrateur `validate_all.py` — lecture complète 1–97/97

- Point de reprise : `Audit_Validate_RUN_CARD_Phase2_Checkpoint_Consolidation.md`, les quatre rapports du validateur, le checkpoint des fixtures, le plan et le protocole externe v2.0 §12 ; recalculer B01. **129 constats provisoires**. Phase 2 ouverte, aucun verdict global ni patch du package.
- Lire les 97 lignes en passages A–D : ordre des scripts, `expect_failure`, garde de code/traceback contre erreur attendue, quatre fixtures ciblées dont F-FIX-001, strict, absence de schéma, dépendance build/reproductibilité, modes d'échec et conditions de PASS. Recouper le workflow exact et les distributions annoncées ; préserver les cas positifs.
- Éviter l'exécution directe de l'orchestrateur pour une lecture non mutante : les deux builds écrivent les archives ; épreuves isolées si nécessaires. Produire le rapport et fixer l'ordre des validateurs restants, lecteur, manifeste/build et workflow, sans classer définitivement les constats.

## Architecture anti-perte de contexte

### Ce qui peut être perdu

La fenêtre de contexte est finie. Quand un long fil la dépasse, le système peut compacter l’historique : les éléments anciens sont résumés pour conserver l’état utile. Cette opération permet de continuer, mais un résumé n’est pas une copie bit-à-bit. Des formulations exactes, alternatives écartées ou justifications secondaires peuvent être compressées.

Un RAG peut retrouver des passages pertinents depuis un corpus externe, mais il dépend de la requête, du découpage, de l’index, du classement des résultats et de la version du corpus. Il peut omettre un passage important ou retrouver une version inadéquate. Il ne doit donc pas être la seule preuve d’un audit normatif.

### Ce qui fait foi ici

Ordre d’autorité pour reprendre le travail :

1. source normative exacte ;
2. protocole exact ;
3. baseline et hashes ;
4. dernier checkpoint consolidé ;
5. rapport sectionnel concerné ;
6. plan maître ;
7. résumé conversationnel ou mémoire personnelle.

La conversation aide à collaborer ; elle n’est pas l’archive canonique de l’audit.

### Rituel obligatoire avant chaque bloc

1. ouvrir le plan maître ;
2. ouvrir le dernier checkpoint du propriétaire ;
3. revérifier les hashes système et protocole ;
4. relire la phase du protocole applicable ;
5. lire la source exacte du bloc avec ses interfaces amont et aval ;
6. charger les constats antérieurs concernés par leurs IDs ;
7. exécuter les tests pertinents ;
8. rédiger le rapport sectionnel ;
9. vérifier couverture, IDs et absence de patch ;
10. sauvegarder le rapport et mettre à jour ce plan lorsque l’état change.

### Reprise après compaction

Après une compaction, ne pas continuer uniquement depuis le résumé reçu. Revalider :

- cible actuelle ;
- dernier bloc terminé ;
- prochain bloc ;
- baseline ;
- registre des constats ;
- décisions interdites ou différées ;
- fichiers produits.

Puis rouvrir les sources nécessaires avant toute nouvelle conclusion.

### Reprise dans une nouvelle conversation

La commande humaine minimale peut être :

> Reprends `DG-AUDIT-001` depuis `Plan_Maitre_Audit_Design_Governance.md` et le dernier checkpoint consolidé. Revérifie B01 avant de continuer.

Le travail ne doit pas dépendre d’une mémoire implicite de la conversation précédente.

### Usage du RAG et de la recherche

Pour ce corpus :

- lecture exacte et recherche textuelle servent aux obligations, termes, routes et champs ;
- recherche sémantique ou RAG peut aider à retrouver des thèmes transversaux ;
- tout résultat RAG important doit être rouvert dans sa source exacte ;
- une absence dans les résultats RAG ne prouve pas qu’une règle n’existe pas ;
- les conclusions inter-fichiers reposent sur les sources propriétaires, pas sur les extraits récupérés.

Le volume actuel ne justifie pas de remplacer la lecture structurée par un RAG. Un index sémantique pourra devenir utile pour les interfaces transversales, mais restera un outil de rappel, jamais l’autorité.

## Tests de continuité

À chaque checkpoint de propriétaire :

- séquence des IDs sans trou ;
- chaque constat présent dans une famille ou un registre ;
- couverture des lignes sans intervalle normatif oublié ;
- hash de la source inchangé ou nouvelle baseline explicite ;
- réserves transportées vers les propriétaires suivants ;
- éléments positifs à préserver ;
- prochaine cible et condition de sortie écrites.

## Références OpenAI sur le contexte long

- [Compaction](https://developers.openai.com/api/docs/guides/compaction)
- [Run long horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- [Codex glossary — context, context window, compaction](https://learn.chatgpt.com/docs/glossary)
- [Codex best practices — external context and MCP](https://learn.chatgpt.com/guides/best-practices)

## Condition de mise à jour de ce plan

Mettre à jour ce fichier uniquement lorsqu’un état de campagne change : propriétaire terminé, phase ouverte ou fermée, baseline remplacée, décision de patch prise, correction appliquée, validation obtenue, réserve créée ou audit clôturé.

Les observations locales restent dans les rapports sectionnels et les checkpoints ; elles ne doivent pas gonfler ce plan.
