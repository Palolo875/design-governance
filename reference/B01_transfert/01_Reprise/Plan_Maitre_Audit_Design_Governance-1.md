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

## Tableau de bord — reprise immédiate

| Question | Réponse au dernier checkpoint |
|---|---|
| Où en est la campagne ? | Phases 0 à 5 terminées dans leur périmètre documentaire B01 ; phase 6 ouverte, **6.02 mise de côté à la demande de l'utilisateur**, preuve perceptuelle absente ; phase 7 documentaire/machine couverte par 7.01–7.02, efficacité non vérifiée ; phase 8 **8.01–8.02 terminées documentairement**, efficacité humaine non observée ; phase 9 ouverte, **9.01 inventaire 20/20, 9.02–9.05 six scénarios éprouvés en contrat sans clôture `FULL`**. **Neuf phases numérotées, 6 à 14, restent à achever** au sens de la clôture intégrale ; leur nombre d'unités internes n'est pas fixé. |
| Quelle est la baseline ? | `B01`. Revérifier les empreintes du système compilé et du protocole contre les sources exactes avant le prochain bloc. |
| Quelle est la dernière cible terminée ? | **9.05** : `Audit_Phase9_05_RESISTANCE_RESULTS_Migration_Aliases_Routes_Promotion.md` ; scénario 18, cinq cartes en mémoire (quatre admises/un refus), aliases refusés par le lecteur mais sélection dépréciée et promotion alléguée admises dans la projection ; aucune migration ni adoption réelle, aucun nouvel ID. |
| Que signifie le registre actuel ? | 157 **fiches provisoires**, dont F-RDR-001 ; ce nombre n'est ni le nombre de défauts indépendants ni celui des corrections décidées. |
| Quelle est la prochaine unité ? | **9.06**, scénario 19 « Surcharge procédurale » : confronter micro-delta et cas à risque exigeant réellement des protections, en suivant leurs propriétaires et la prochaine preuve ; **6.02 reste de côté** jusqu'à nouvelle demande. |
| Que reste-t-il interdit ? | Aucun verdict global, classement définitif des constats ou patch du système à ce stade. |

**Entrées nécessaires pour reprendre :** ce plan ; rapport 9.05 immédiatement précédent et matrice 9.01, rapports 5.01–5.04 et 9.02 selon risque ; protocole indépendant v2.0 §19, `DIRECTION/START`, `ACTION/CLOSE-EXIT-CHECK`, les déclencheurs SAVOIR et les façades de route courte. Les réserves perceptuelles 6.02 demeurent dans l'historique sans nouvelle action sur les pilotes. Avant un scénario de stress, rouvrir la règle propriétaire exacte, les voisins et la preuve antérieure.

**Sortie du prochain bloc :** `RESISTANCE-RESULTS` 9.06, contraste entre étapes sans effet sur un delta local et étapes nécessaires pour le risque/claim d'un second cas ; preuves exactes, limites de charge humaine et protections maintenues. Ne compter comme « exécuté » que le scénario réellement rejoué dans son scope. Garder 6.02 de côté ; ne déduire aucun verdict global d'un schéma accepté.

## Situation actuelle

| Élément | État |
|---|---|
| Phase 0 — cadrage | Terminée |
| Phase 1 — baseline | Terminée ; hashes B01 stables |
| Phase 2 — lecture complète | **Terminée pour le périmètre B01** : 60 sources qualifiées, distributions GitHub/Local contrôlées, checkpoint final rédigé ; ne pas confondre lecture close et audit global achevé. |
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
| Orchestrateur `validate_all.py` | Lecture A–D **1–97/97**, rapport `Audit_Validate_ALL_Phase2_01_Orchestration_Oracles_Build_Reprise.md` ; 60 fichiers reconstruits avec tailles/lignes conformes à B01, suite complète verte dans la copie ; F-ALL-001 (échec pour mauvais motif accepté) et F-ALL-002 (fixture cherchée dans le cwd appelant) provisoires. L'absence du build dans le package complet est déjà bloquée par l'inventaire ; **131 fiches provisoires**. |
| Validateur documentaire `validate_design_governance.py` | Lecture A–D **1–229/229**, rapport `Audit_Validate_Design_Governance_Phase2_01_Inventaire_Liens_Conventions.md` ; GitHub 60 et Local 56 passent sur B01, quatre F-VDG provisoires : F-VDG-001 (fichier sous `.build` source ignoré mais empaqueté, `FULL PASS` dans une copie mutée), F-VDG-002 (bloc `JSON` majuscule), F-VDG-003 (`state: UNKNOWN` minuscule, portée normative à confirmer), F-VDG-004 (README officiel absent → traceback). **135 fiches provisoires** ; aucun patch. |
| Validateur de contrats `validate_contracts.py` | Lecture A–D **1–218/218**, rapport `Audit_Validate_Contracts_Phase2_01_Schema_Oracles_CLI.md` ; trois exemples et quatre mutations passent sur B01. Des copies avec schémas `{}` donnent `FULL VALIDATION PASSED` (F-VCT-001), un schéma `[]` ou un document UTF-8 invalide produit un traceback (F-VCT-002), et la perte ciblée de l'enum `research_brief.depth` reste verte avec exemple invalide (F-VCT-003). **138 fiches provisoires**, aucun patch. |
| Validateur de la carte `validate_reading_map.py` | Lecture A–D **1–105/105**, rapport `Audit_Validate_READING_MAP_Phase2_01_Locators_Handoff_Autorite.md` ; B01 et suite complète verts, destination inexistante rejetée ; F-VRM-001 (dupliquer ou perdre des locators reste vert mais change l’accès CLI), F-VRM-002 (handoff vide déclaré contrôlé) et F-VRM-003 (frontière d’autorité contredite malgré mots requis) provisoires. **141 fiches provisoires**, aucun patch. |
| Lecteur de routes `read_route.py` | Lecture A–D **1–86/86**, rapport `Audit_Read_Route_Phase2_01_Resolution_Extraction_GitHub_Local.md` ; 24/24 routes B01 exactes dans GitHub et Local, quatre refus contrôlés par distribution ; F-RRT-001 : un titre dans un bloc de code ou une limite de section indentée peut donner un mauvais extrait avec `FULL PASS`. Mauvais owner dans le tableau : occurrence F-VRM-001 sans nouvel ID. **142 fiches provisoires**, aucun patch. |
| Manifeste `package_manifest.json` | Lecture A–D **1–124/124**, rapport `Audit_Package_Manifest_Phase2_01_Inventaires_Version_Distributions.md` ; B01 : 60 chemins GitHub et 56 Local, uniques et conformes aux sources, builds et archives ; F-MAN-001 (doublon admis, compteur 61/60 ou 57/56 avec `FULL PASS`) et F-MAN-002 (version absente ou divergente avec `FULL PASS`) provisoires. **144 fiches provisoires**, aucun patch. |
| Build `build_distributions.sh` | Lecture A–D **1–166/166**, rapport `Audit_Build_Distributions_Phase2_01_Stages_Archives_Reprise.md` ; B01 construit 60/56 fichiers correctement, mais copies mutées révèlent F-BLD-001 (entrée retirée conservée dans ZIP avec `FULL PASS`), F-BLD-002 (ZIP et `dist` de générations mixtes après panne), F-BLD-003 (sauvegarde effacée après reprise ratée), F-BLD-004 (symlink présent au stage mais absent des ZIP avec `FULL PASS`). **148 fiches provisoires**, aucun patch. |
| Workflow CI `.github/workflows/validate.yml` | Lecture A–D **1–22/22**, rapport `Audit_Workflow_Validate_Phase2_01_Declencheurs_Node24_Execution.md` ; YAML conforme, suite intégrée verte dans copie isolée sous Python 3.12, sans run hébergé ni preuve d'exécution sous Python 3.11. GitHub retire Node 20 le 23-09-2026 ; checkout@v4 et setup-python@v5 précèdent leurs versions natives Node 24 : **F-WF-001** provisoire (risque de compatibilité, aucun échec CI constaté). **149 fiches provisoires**, aucun patch. |
| Skill pratique `skills/design-governance-practice/SKILL.md` | Lecture A–D **1–149/149**, rapport `Audit_Skill_Pratique_Phase2_01_Activation_Routes_Sortie_Exports.md` ; 24 locators cités avec titres propriétaires, 16 accessibles par CLI et huit refus connus F-DIR-028 ; quatre liens de références existants ; deux exports construits dans une copie isolée. **F-SK-001** : ambiguïté portée de sortie courte/handoff et liste incomplète au regard d'ACTION ; **F-SK-002** : chemin de carte GitHub absent dans Local. **151 fiches provisoires**, aucun patch. |
| Référence `flow.md` | Lecture A–D **1–23/23**, rapport `Audit_Reference_Flow_Phase2_01_Branches_Critiques_Preuve.md` ; diagramme et prose confrontés à `DIRECTION/START`, `ACTION` et skill ; deux exports isolés contiennent la même référence et `ORCHESTRATION_MAP`. **F-FLOW-001** provisoire : branches « risque critique » et `NOT-VERIFIED` sans reprise figurée ; un one-shot simulé et le renvoi à la carte transportent F-DIR-009/F-SK-002 sans nouvel ID. **152 fiches provisoires**, aucun patch. |
| Référence `canonical_minimum.md` | Lecture A–D **1–25/25**, rapport `Audit_Reference_Canonical_Minimum_Phase2_01_Limites_Statuts_Priorite.md` ; huit distinctions confrontées à `ACTION`, `DIRECTION`, glossaire, skill et flux ; deux exports isolés livrent des octets identiques. Raccourcis de formulation `DECISION-CHANGE` et `N/A-JUSTIFIED` notés, propriétaires explicites : **aucun nouvel ID, 152 fiches provisoires** et F-FLOW-001 toujours ouvert. |
| Référence `examples.md` | Lecture A–D **1–90/90**, rapport `Audit_Reference_Examples_Phase2_01_Quatre_Parcours_Preuve_Cloture.md` ; quatre scénarios / trois modes, copies GitHub et Local identiques sur build isolé. F-EX-001 (modification d'artefact présentée comme changement de décision), F-EX-002 (captures élargies à mémoire et tâche) et F-EX-003 (`NOT-OBSERVED` pour surfaces non testées, retour sans régression localisée) provisoires ; F-SAV-005, F-FLOW-001 et F-SK-001/002 transportés. **155 fiches provisoires**, aucun patch. |
| Référence `machine_projection.md` | Lecture A–D **1–97/97**, rapport `Audit_Reference_Machine_Projection_Phase2_01_YAML_JSON_Provenance_Validation.md` ; YAML converti tel quel refusé par le validateur : locator de provenance différent de l'artefact ; alignement d'une seule valeur accepté en normal, placeholders refusés en strict. F-MP-001 provisoire, protections `CLOSED+RETURNED+RETURN` et profil vérifiées par fixtures, quatre références de la skill maintenant couvertes. **156 fiches provisoires**, aucun patch. |
| `RELEASE_NOTES.md` racine | Lecture A–D **1–59/59**, rapport `Audit_Release_Notes_Phase2_01_Version_Distributions_Controles_Limites.md` ; version/date concordantes avec CHANGELOG et README comme déclarations B01 ; `validate_all.py` passe sur copie isolée, stages et ZIP 60/56 correspondent au manifeste, notes incluses en GitHub et absentes de Local intentionnellement. F-MAN-002, F-BLD-001 à 004, F-ALL-001/002, F-CHG-001, F-SK-002 et F-MP-001 transportés sans doublon ; publication externe et CI hébergée non observées. **Aucun nouvel ID, 156 fiches provisoires**, aucun patch. |
| `README.md` racine | Lecture A–D **1–156/156**, rapport `Audit_README_Racine_Phase2_01_Entree_Modes_Liens_Validation_Exports.md` ; liens GitHub 7/7 et fragment 1/1, liens du README Local généré 3/3, `read_route.py DIRECTION/START` dans les deux exports. F-RDR-001 provisoire : la ligne courte `ITER` évoque une amélioration issue d'observation sans condition de direction précédente retrouvable ; F-QS-002, F-VRC-004/005, F-BLD et F-MAN-002 transportés. **157 fiches provisoires**, aucun patch. |
| Mémoire de migration et inventaire résiduel | `Audit_Memoire_Migration_Phase2_01_Inventaire_Archives_Autorite.md` : les **60 sources non générées** de B01 coïncident avec les 60 chemins du manifeste ; aucun fichier B01 intitulé « mémoire de migration ». Ancien `REFERENCES` v2.5 (« mémoire de décision ») et ancien `CHANGELOG/MIGRATION` v2.6 retrouvés **hors package** et qualifiés historiques ; quatre destinations de routes changées dans le tableau public `CHANGELOG.md` 48–54 de V1.0.0. Un cache Python généré dans le dossier de travail n'est pas une source. Aucun nouveau constat : **157 fiches provisoires**, aucun patch. |
| Distributions GitHub et Local | `Audit_Distributions_GitHub_Local_Phase2_01_Archives_Livraison_Reprise.md` : copie B01 construite deux fois sans changement, ZIP identiques au second build ; `dist/github` et ZIP **60/60**, `dist/local` et ZIP **56/56**, octets conformes, aucun doublon ou cache dans les archives. ZIP extraits : suites GitHub/Local code 0 dans leurs portées ; F-SK-002 confirmé dans Local extrait. Risques de mutations/pannes F-VDG-001 et F-BLD-001 à 004 maintenus. **Aucun nouvel ID, 157 fiches provisoires**, aucun patch. |
| Checkpoint final de phase 2 | `Audit_Phase2_Checkpoint_Final_Couverture_Interfaces_Entree_Phase3.md` : 60/60 sources déclarées qualifiées par catégorie et rapport, limites de lecture/validation explicitées, chaînes de responsabilité transmises à la phase 3 et scénarios aux phases 4–9. **157 fiches provisoires**, aucune décision finale. |
| Phase 3 — `ROLE-MAP` | `Audit_Phase3_01_ROLE_MAP_Proprietaires_Acteurs_Projections.md` : neuf rôles du protocole §13 attribués aux cinq sources, acteurs humains/agents, façades, skill, machine, build/CI et distributions ; entrée/sortie/owner suivant/escalade/non-goal et bornes de preuve explicités ; F-SAV-007, F-CHG-001, F-SK-002 et limites machine transportés sans doublon. **Aucun nouvel ID, 157 fiches provisoires**, aucun patch. |
| Phase 4.01 — Classification → HANDOFF → RUN_CARD | `Audit_Phase4_01_CONTRACT_DIAGNOSTIC_Classification_Handoff_RUN_CARD.md` : sept dimensions §14 ; voisins LITE local, consentement critique et direction à preuve mobile incomplète. Le JSON accepte un consentement critique déclaré LITE avec protection structurée sans vérifier le classement DIRECTION (F-DIR-007/F-ACT-017), rejette une ancre transformée lors d'une exploration pour autre preuve (F-RC-001) ; intake sans verdict rejeté (F-ACT-009), conséquence facultative en LITE accepté (F-ACT-013). Cas `CLOSED+RETURNED+RETURN` préservé ; 157 fiches provisoires, aucun nouvel ID ni patch. |
| Phase 4.02 — Décision partagée directe/induite | `Audit_Phase4_02_CONTRACT_DIAGNOSTIC_Decision_Partagee_Directe_Induite.md` : sept dimensions §14 et trois scénarios (token partagé objet direct, identité induisant token, décisions inséparables). START 131/138/144 prime ; SAVOIR/SYSTEM 694 reste ambigu malgré 696 (F-SAV-007). Renvoi SAVOIR 704 à COMPONENTS 611–657 insuffisant pour composant ordinaire (F-BIB-004). Variantes en mémoire : carte SYSTÈME sans preuve consumers/migration/rollback/non-régression acceptée (F-ACT-015/021), lien machine absent dans carte DIRECTION, mauvais mode texte accepté ; absence de trace_locator SYSTÈME rejetée. 157 fiches provisoires, aucun nouvel ID ni patch. |
| Phase 4.03 — Sélection et héritage structurel | `Audit_Phase4_03_CONTRACT_DIAGNOSTIC_Selection_Heritage_Composant.md` : sept dimensions §14 et trois cas (microcopie LITE avec héritage, catalogue de cours STANDARD avec états, Dialog partagé SYSTÈME). Sélection zéro légitime sans neutraliser ACTION ; F-BIB-002 sur temporalité local réduit/DERIVE, F-BIB-004 sur contrat de composant ordinaire, F-BIB-001 sur portée de la paire B1b conservés. Deux copies en mémoire de l'exemple RUN_CARD, l'une avec route SELECT existante, l'autre avec nom de route inventé dans `sources`, sont acceptées ; ce test de chaînes prépare F-ACT-002/F-DIR-028 sans nouvel ID. **157 fiches provisoires, aucun patch ni verdict.** |
| Phase 4.04 — Texte RUN_CARD → schéma → validateur → fixtures | `Audit_Phase4_04_CONTRACT_DIAGNOSTIC_RUN_CARD_Schema_Validateur_Fixtures.md` : sept dimensions §14 et voisins positifs/négatifs. Mode inconnu, sources vides, preuve acceptée absente et trace SYSTÈME absente rejetés ; source inventée, paquet SYSTÈME sans migration/rollback, RETURNED+ACCEPTED admis. `{}` annonce un succès sans validation et schéma absent/incomplet produit exceptions ou faux succès ciblé. Suite native verte mais oracle F-FIX-003 peut passer pour mauvais motif ; F-FIX-001 atténuée par suite supérieure sans motif. F-VRC-006/007/008, F-ACT-002/010/015/021 et F-RC-001 conservés. **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 4.05 — DOMAIN_FRAME → schéma → validateur | `Audit_Phase4_05_CONTRACT_DIAGNOSTIC_DOMAIN_FRAME_Schema_Validateur.md` : sept dimensions §14 et voisins. Forme et recoupement minimal protégés, mais risque/action/état nouveaux sans contrôle dédié acceptés, libellé équivalent avec majuscule rejeté (F-DF-001) ; plan « à déterminer » accepté (F-DF-002). Schéma du domaine `{}` avec suite native verte et mutant négatif accepté pour mauvais motif (F-VCT-001) ; exemple de projet refusé avant lecture par CLI ciblée (F-ACT-008). **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 4.06 — RESEARCH_BRIEF → schéma → validateur | `Audit_Phase4_06_CONTRACT_DIAGNOSTIC_RESEARCH_BRIEF_Sources_Incertitude_Validateur.md` : sept dimensions et quatre situations (non-activation légitime, recherche nécessaire non réalisée, incertitude restante, conséquence illustrative). Absence d'entrée ou profondeur inconnue rejetées ; `depth=none` avec entrée, source opaque, classe non déclarée, arrêt « à déterminer » et incertitude seulement reformulée acceptés ; `status`/`trace_locator` directs refusés (F-RB-001/002). Schéma `{}` ou enum `depth` retirée avec valeur invalide : suite autonome verte (F-VCT-001/003). **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 4.07 — Trois objets de production | `Audit_Phase4_07_CONTRACT_DIAGNOSTIC_Production_Creative_UIUX_Evaluation.md` : sept dimensions ; une direction unique refusée mais duplicata sous IDs différents admis (F-PC-001), exigence `state_matrix: loading error` composée de deux lignes admise (F-PC-002). Carte de couverture réduite à une entrée, `observed` avec locator fictif, `not_applicable` sans raison et résultats de tâche sous seule capacité « capture statique » admis (F-ACT-005/007/012/018/021/022) ; contrôles positifs d'IDs, enums et liste vide conservés. Schéma de production `{}` ou enum `proof_status` retirée avec `PASS` : suite autonome verte (F-VCT-001). **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 4.08 — Production → HANDOFF/RUN_CARD/clôture | `Audit_Phase4_08_CONTRACT_DIAGNOSTIC_Production_HANDOFF_RUN_CARD_Cloture.md` : sept dimensions ; suites natives vertes et voisins croisés sans contrôle d'identité de direction retenue, de statut d'état observé ou de méthode/capacité/claim ; V2 livré avec provenance V1 et réserve sans cycle complet également admis. RUN_CARD rejette correctement absence d'observation sous acceptation et locator de provenance différent ; `CLOSED+RETURNED+RETURN` admis, ancre réellement transformée avec retour toujours rejetée (F-RC-001). La trace extérieure porte des éléments du handoff non sérialisés ; sa seule adresse ne les prouve pas. **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 4.09 — Sources/façades → manifeste → distributions | `Audit_Phase4_09_CONTRACT_DIAGNOSTIC_Sources_Manifeste_Distributions.md` : sept dimensions ; copie B01 construite, deux ZIP exacts **60/60** et **56/56**, cinq témoins à octets identiques par profil ; START et CLOSE-EXIT accessibles dans les deux, HANDOFF présent dans ACTION mais hors table CLI, skill Local garde un chemin GitHub (F-SK-002). Omission de ACTION du manifeste Local bloquée ; lien symbolique ACTION injecté dans une copie : build/stages verts mais ACTION absent des deux ZIP, CLOSE-EXIT inaccessible après extraction, suite RUN_CARD verte (F-BLD-004). **157 fiches provisoires, aucun nouvel ID, patch ni verdict.** |
| Phase 5.01 — Parcours de lecture et première action | `Audit_Phase5_01_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Entrees_Parcours_Premiere_Action.md` : six parcours documentaires, de deux à trois transitions de fichiers sur les chemins retenus, six axes du §15 ; cinq locators principaux servis, trois titres présents hors table CLI. Fiches antérieures reprises sans nouvel ID ni preuve d'usage humain. **157 fiches provisoires**, aucun patch. |
| Phase 5.02 — Sections, usage opérationnel et charge | `Audit_Phase5_02_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Sections_Usage_Charge.md` : quatre propriétaires et leurs voisins recoupés ; seize locators éprouvés ; START extrait 125 lignes malgré le besoin « arbre seulement », CRAFT 181 lignes, SELECT 94 ; locators absents de la table mais titres présents distingués des blocs valides trop larges. Pas de mesure humaine ni d'ID nouveau. **157 fiches provisoires**, aucun patch. |
| Phase 5.03 — Nécessité et coût des 60 chemins | `Audit_Phase5_03_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Matrice_Necessite_60_Sources.md` : 60/60 chemins uniques dans l'ordre du manifeste, profils 60 GitHub / 56 Local ; 33 contrats/exemples/fixtures et 8 scripts/manifeste ne sont pas des chapitres à lire en run ordinaire. Effets et options provisoires par fichier, limites des oracles et quatre absences Local volontaires. Pas de lecture humaine mesurée ni d'ID nouveau. **157 fiches provisoires**, aucun patch. |
| Phase 5.04 — Synthèse des six axes §15 | `Audit_Phase5_04_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Synthese_Six_Axes.md` : façade, hiérarchie, chargement conditionnel, navigation, charge cognitive et façade/source recoupés avec 5.01–5.03 et les propriétaires B01 ; accès sélectif au propriétaire puis à la section et aux minima. Effets sur usagers et qualité ouverts ; **157 fiches provisoires**, aucun nouvel ID ni patch. Phase 5 close dans sa portée documentaire. |
| Phase 6.01 — Premier objet, dix dimensions et arrêt | `Audit_Phase6_01_POSITIVE_CAPABILITY_DIAGNOSTIC_Premier_Objet_Dix_Dimensions.md` : §16 confronté à la scène de cartographie sonore et à l'écran d'incidents des exemples B01 ; prescrit/illustré/testé/rendu observé distingués, one-shot borné par observation et B1b applicable. Aucune interface rendue ni tâche utilisateur vérifiée ici ; **157 fiches provisoires**, aucun nouvel ID ni patch. Phase 6 ouverte. |
| Phase 6.02 — Préparation d'épreuve sur pilotes | `Audit_Phase6_02_POSITIVE_CAPABILITY_DIAGNOSTIC_Pilotes_Preparation_Observation.md` : aucun rendu B01 existant ; deux HTML hors B01 et archive produits, syntaxe JS, IDs et ZIP vérifiés. Navigateur d'audit a refusé le protocole de fichier local et interdit le contournement : **aucune capture ni interaction réelle constatée**, dix axes §16 laissés non vérifiés sur rendu. **157 fiches provisoires**, aucun patch ; 6.02 perceptuelle ouverte. |
| Phase 7.01 — Boucles et one-shot | `Audit_Phase7_01_LOOP_DIAGNOSTIC_Boucles_Creation_Gouvernance_One_Shot.md` : règles créative, gouvernance du run et maintien du corpus distinguées ; one-shot conditionnel et B1b recoupés ; quatre appels en mémoire à `validate_card` : l'absence de `decision_change` sous clôture DIRECTION acceptée est rejetée, une simple « explication supplémentaire » non vide est acceptée. Ce résultat mesure la limite de l'oracle machine, non la qualité d'un rendu. **157 fiches provisoires**, aucun nouvel ID ni patch ; phase 7 ouverte. |
| Phase 7.02 — Transmission, retour et reclassement | `Audit_Phase7_02_LOOP_DIAGNOSTIC_Transmission_Retour_Reclassement.md` : 11 appels ciblés sur trajets DIRECTION→retour et LITE critique→reclassement ; protections `next_proof` et risque critique positives, choix A/B et continuation non liés, ancre `transformed` rejetée à tort lors du retour (F-RC-001), LITE critique accepté sur déclaration (F-DIR-007/F-ACT-017). Résultats **fictifs, structurels**, sans usage réel ; **157 fiches provisoires**, aucun nouvel ID ni patch. |
| Phase 8.01 — Douze perspectives | `Audit_Phase8_01_PERSPECTIVE_COVERAGE_MATRIX_Douze_Perspectives.md` : 12/12 applicables, six `FULL` (création, produit, inclusion, preuve, agentique, gouvernance) et six `TARGETED` (contenu, runtime, équipe, opérations, expérimentation, migration), avec source, preuve bornée et test suivant ; zéro `N/A` ou omission. Pas de test humain/rendu observé ; **157 fiches provisoires**, aucun nouvel ID ni patch. |
| Phase 8.02 — Cinq rôles et handoffs | `Audit_Phase8_02_PERSPECTIVE_COVERAGE_MATRIX_Cinq_Roles_Parcours_Handoff.md` : cinq vignettes fictives dans un même outil d'incidents ; dix locators testés dans B01 et agencement Local **isolé**, six servis et quatre titres existants hors table de chaque côté ; chemin skill GitHub absent de Local, sans test d'agent humain. Décisions, preuve et owner suivant attribués par rôle. **157 fiches provisoires**, aucun ID ni patch. |
| Phase 9.01 — Matrice des scénarios de résistance | `Audit_Phase9_01_RESISTANCE_RESULTS_Matrice_Vingt_Scenarios_Oracles.md` : **20/20** scénarios §19 inventoriés et orientés, dix `FULL` et dix `TARGETED`, avec owner, adverse, positif/négatif, antécédent et manque ; 0/20 stress complets nouveaux exécutés en 9.01. S21 stage/ZIP ajouté comme risque spécifique, résultat antérieur 4.09 réutilisé. 9.02 cible 15/17/20 ; **157 fiches provisoires**, aucun ID ni patch. |
| Phase 9.02 — Preuve, fraîcheur et divergence | `Audit_Phase9_02_RESISTANCE_RESULTS_Preuve_Fraicheur_Texte_Schema.md` : trois scénarios 15/17/20 éprouvés sur **11 appels machine** en mémoire, sept admissions/quatre refus ; retour sans preuve et plusieurs garde-fous passent, observation hors risque, preuve V1 pour carte V2, scope élargi et `ESCALATED+ACCEPTED-WITH-RESERVATION` passent aussi. Trois stress examinés **au niveau du contrat**, aucun `FULL` d'efficacité clos ; **157 fiches provisoires**, aucun ID ni patch. |
| Phase 9.03 — Composant partagé et deux décisions | `Audit_Phase9_03_RESISTANCE_RESULTS_Composant_Partage_Deux_Decisions.md` : scénario 06, huit validations B01 en mémoire (six admises/deux refusées), paire D-001→S-001 avec oracle externe parent/token cohérent, orphelin et divergent ; S-002 direct et déclassement en STANDARD admis, owner absent et champ `parent_run_id` ad hoc rejetés. Examen **de contrat seulement**, aucune migration réelle ni `FULL` d'efficacité ; **157 provisoires**, aucun ID ni patch. |
| Phase 9.04 — Action externe, permission et confidentialité | `Audit_Phase9_04_RESISTANCE_RESULTS_Action_Externe_Autorite_Confidentialite.md` : huit validations fictives en mémoire (sept admises/un refus) ; arrêt `CLOSED+BLOCKED+RETURN` admis, protection critique absente refusée, cartes d'acceptation admises même si l'oracle d'audit externe bloque faute de permission, scope, canal ou confirmation. `APPROVED` textuel ne prouve rien. **Aucune action, permission ou donnée sensible réelle**, cinq scénarios éprouvés en contrat au cumul ; **157 provisoires**, aucun ID ni patch. |
| Phase 9.05 — Migration, aliases et promotion | `Audit_Phase9_05_RESISTANCE_RESULTS_Migration_Aliases_Routes_Promotion.md` : cinq cartes en mémoire (quatre admises/un refus) ; cinq aliases refusés par le lecteur, dont `REFERENCES/SOURCE` admis en `RUN_CARD.sources` ; deux destinations SAVOIR présentes mais hors index CLI ; promotions textuelles admises sans preuve de consumers. GitHub 60 et Local 56 membres contrôlés dans des **exports reconstruits isolés**, sans migration réelle. F-CHG-001 et F-ALL-002 recoupés, **six scénarios en contrat au cumul, 157 fiches provisoires**, aucun ID ni patch. |
| Prochaine cible | 9.06, surcharge procédurale : delta local vs protections justifiées ; 6.02 mise de côté jusqu'à nouvelle instruction. |
| Phases 4–14 | Phases 4 et 5 **terminées dans leur périmètre documentaire B01** ; phase 6 **ouverte, 6.02 différée** ; phase 7 **7.01–7.02 terminées documentairement et en machine, efficacité réelle non vérifiée** ; phase 8 **8.01–8.02 terminées dans leur portée documentaire/machine, effet humain non mesuré** ; phase 9 **9.01 matrice, 9.02–9.05 six scénarios éprouvés en contrat, autres résistances ouvertes** ; phases 6–14 restent à achever, **neuf phases numérotées** au sens de la clôture intégrale, sans fixer leur durée. |
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

État : **terminée pour la lecture du périmètre B01 défini**. Les autres phases restent nécessaires pour décider de la valeur, de la gravité et des corrections.

Parcours de phase 2, séparé entre **couverture déjà rapportée** et **travail restant**. La table « Situation actuelle » conserve les plages, rapports et IDs détaillés ; les totaux ci-dessous ne prouvent pas à eux seuls la qualité des conclusions.

| Bloc | État rapporté | Prochaine condition de sortie |
|---|---|---|
| Cinq propriétaires normatifs : DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE, CHANGELOG | Terminé : 3 548/3 548 lignes, checkpoints et consolidation des interfaces. | Réutiliser leurs sources exactes et constats concernés lors des phases transversales. |
| Façades : QUICKSTART, READING_MAP, ORCHESTRATION_MAP, GLOSSAIRE, README officiel | Terminé : 616/616 lignes, avec rapports et checkpoint QUICKSTART. | Vérifier les routes et promesses lors des essais inter-fichiers. |
| Contrats et exemples machine : DOMAIN_FRAME, RESEARCH_BRIEF, production, RUN_CARD | Schémas et exemples désignés lus ; RUN_CARD 180/180 et 102/102, checkpoint achevé. | Recouper les règles avec scripts et distributions ; préserver les exemples valides. |
| Fixtures RUN_CARD et validateur `validate_run_card.py` | 25/25 fixtures lues ; script 590/590 lu ; checkpoints achevés. | Transporter F-FIX-001 à 003 et F-VRC-001 à 008 avec leurs oracles et limites. |
| Scripts d'intégration et workflow | `validate_all.py` 97/97, `validate_design_governance.py` 229/229, `validate_contracts.py` 218/218, `validate_reading_map.py` 105/105, `read_route.py` 86/86, `package_manifest.json` 124/124, `build_distributions.sh` 166/166 et workflow CI 22/22 achevés. Run CI hébergé non observé. | Couverture des sources exactes, essais discriminants et interfaces confrontées ; conserver la réserve sur la CI. |
| Skill pratique, références, release notes, package racine, mémoire de migration | Skill pratique 149/149, quatre références `flow.md` 23/23, `canonical_minimum.md` 25/25, `examples.md` 90/90, `machine_projection.md` 97/97, notes de release 59/59 et README racine 156/156 lus A–D. Mémoire de migration qualifiée par inventaire des 60 sources et comparaison des témoins historiques hors package : aucun fichier B01 séparé, table publique de cinq aliases dans CHANGELOG. | Les anciens runs et leur migration réelle attendent une épreuve ultérieure distincte si une trace est disponible. |
| Distributions GitHub et Local | **Terminées dans une copie B01 propre** : 60/60 et 56/56 dossiers, ZIP et octets exacts, extraction et suites correspondantes vertes ; rapport de distribution A–D. | Tester en phase 9 les résistances déjà isolées sous panne/mutation, distinguer CI hébergée et construction locale. |
| Checkpoint final de phase 2 | **Terminé** : `Audit_Phase2_Checkpoint_Final_Couverture_Interfaces_Entree_Phase3.md`. | Ouvrir la phase 3 sur ses chaînes et rouvrir les sources exactes avant chaque conclusion transversale. |

Chaque cible reçoit une profondeur `LIGHT`, `TARGETED`, `FULL`, `N/A-JUSTIFIED` ou `ESCALATED`. Les copies et distributions ne seront pas traitées comme sources propriétaires.

**Contrôle de passage entre deux cibles :** avant de quitter une cible, relever dans son rapport les promesses, dépendances, constats et tests qui exigent une autre source ; attribuer chaque point à la cible suivante ou à une cible ultérieure nommée. À l'ouverture de la nouvelle cible, confronter ses passages exacts aux passages pertinents des sources liées, même si celles-ci ont déjà été auditées. Indiquer dans le nouveau rapport ce qui est confirmé, contredit ou encore à vérifier, avec source, plage et ID de constat lorsque disponible. Si une source liée reste à lire ou si sa preuve manque, conserver la réserve et différer la conclusion sur l'interface. La proximité chronologique de deux fichiers ne suffit pas à créer une interface : conserver le rapport du bloc précédent pour la continuité et rouvrir sa source exacte lorsque le lien est réel.

### Phase 3 — Cartographier les rôles

But : déterminer, pour chaque cible, propriété, décision, exécution, preuve, jugement, coordination, lecture, mémoire et garde-fou. Ajouter si nécessaire input, output, owner, escalade, non-goal, prochaine preuve et condition de sortie.

Sortie : `ROLE-MAP`.

État : **terminée pour la cartographie documentaire B01** : `Audit_Phase3_01_ROLE_MAP_Proprietaires_Acteurs_Projections.md` couvre les neuf rôles et les consommateurs ; l'identité effective d'un owner de projet ou du corpus doit être renseignée dans le contexte d'un run réel. Les contrats entre rôles restent à éprouver en phase 4.

### Phase 4 — Auditer les contrats

But : vérifier responsabilité, entrée, transformation, sortie, preuve, escalade et mémoire.

Sortie : `CONTRACT-DIAGNOSTIC`.

État : **terminée pour les contrats documentaires B01**. Unités 4.01 à 4.04 sur classification, décision partagée, héritage et projection RUN_CARD ; 4.05/4.06 sur DOMAIN_FRAME et RESEARCH_BRIEF ; 4.07 sur les trois objets de production ; 4.08 sur le transfert vers HANDOFF/RUN_CARD/clôture ; 4.09 sur sources/façades → manifeste → distributions. Les neuf rapports traitent les sept dimensions et maintiennent les réserves ; qualité produit réelle, lecteurs humains, CI hébergée, adoption et résistance globale seront examinés dans les phases suivantes. Aucun verdict général n'en découle.

### Phase 5 — Auditer l’architecture de l’information

But : tester les six axes du protocole v2.0 §15 — façade, hiérarchie, chargement conditionnel, navigation, charge cognitive et relation façade/source — à trois échelles : parcours entre fichiers, organisation des sections dans chaque fichier, et usage effectif des sources selon leur consommateur. Vérifier l'accès à la première action, aux exceptions pertinentes, à la preuve et à la reprise, sans exiger d'un lecteur humain la consultation des fichiers réservés aux machines ou au build.

**Question explicite sur les 60 sources B01 :** leur inventaire et leur lecture 60/60 sont établis en phase 2, mais leur nécessité individuelle et leur coût collectif restent à examiner. Pour chacune des 60 sources non générées du manifeste GitHub (dont 56 distribuées en Local), établir une ligne traçable : famille et public, rôle distinct et moment d'activation, entrée → décision/action → sortie, sections nécessaires et ordre de lecture lorsqu'il s'agit d'un texte, dépendances et éventuels doublons, coût pour le lecteur et/ou la maintenance, effet vérifiable d'une fusion ou suppression, et option provisoire « conserver / charger sous condition / réorganiser / simplifier / fusionner / retirer / preuve manquante ». Adapter les critères aux cinq propriétaires, façades et références, schémas/exemples/fixtures, scripts, manifeste, workflow et distributions : une fixture ou un outil peut être indispensable sans être lu pendant un run ordinaire. Regrouper l'analyse par famille pour repérer les coûts transversaux, mais statuer provisoirement sur **chaque chemin** avec un renvoi aux sources et aux rapports antérieurs ; approfondir les cas où l'utilité ou le coût restent contestés.

Observer dans les textes le sommaire, le découpage, les titres, la progression prérequis → opération → exception, la densité des termes, les renvois, les répétitions protectrices ou inutiles et le nombre de choix simultanés. Simuler les parcours selon le rôle, noter les étapes et concepts avant l'action et distinguer charge de lecture, charge d'exécution et charge de maintenance. Une simulation documentaire ne démontre pas un temps réel ni la compréhension d'un lecteur ; réserver ces mesures aux essais ultérieurs. Le nombre de fichiers n'est pas un objectif de réduction en soi.

Sortie : `INFORMATION-ARCHITECTURE-DIAGNOSTIC`.

État : **terminée dans son périmètre documentaire B01 ; unités 5.01–5.04 livrées** (`Audit_Phase5_01_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Entrees_Parcours_Premiere_Action.md` ; `Audit_Phase5_02_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Sections_Usage_Charge.md` ; `Audit_Phase5_03_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Matrice_Necessite_60_Sources.md` ; `Audit_Phase5_04_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Synthese_Six_Axes.md`). Six parcours simulés ont éprouvé les six axes du §15 ; quatre propriétaires, leurs voisins et seize appels CLI ont précisé les volumes servis ; 60/60 chemins ont un consommateur et une option provisoire traçables. La synthèse distingue accès au propriétaire, accès à la section et minima obligatoires. Aucun temps de lecture, coût humain ou qualité produite mesurés. Les arbitrages de conservation, fusion ou suppression iront aux phases 10–11 ; la phase 6 protégera les capacités positives, la phase 8 éprouvera les différents consommateurs, la phase 9 les cas de charge, et la phase 13 validera toute modification décidée. **157 fiches provisoires**, aucun patch ni verdict global en phase 5.

### Phase 6 — Auditer la capacité positive

But : vérifier non seulement ce que le système empêche, mais ce qu’il permet de produire de meilleur : présence, point de vue, spécificité, composition, matière/type, désirabilité située, résolution, retenue, habitabilité et transfert.

Sortie : `POSITIVE-CAPABILITY-DIAGNOSTIC`.

État : **ouverte ; 6.01 terminée dans sa portée documentaire ; préparation 6.02 accomplie, conclusion perceptuelle en attente**. Rapports : `Audit_Phase6_01_POSITIVE_CAPABILITY_DIAGNOSTIC_Premier_Objet_Dix_Dimensions.md` et `Audit_Phase6_02_POSITIVE_CAPABILITY_DIAGNOSTIC_Pilotes_Preparation_Observation.md`. Les dix dimensions §16 ont été reliées à deux exemples contrastés, puis à deux pilotes fictifs hors B01 ; aucun rendu de ces pilotes, utilisateur, qualité produite ou durée n'a été observé. Le navigateur de contrôle a rejeté le fichier local selon sa politique ; aucun contournement effectué. Captures/version/états et méthode sont requis pour conclure 6.02. Les protections positives des propriétaires seront conservées ; **157 fiches provisoires**, aucun patch.

### Phase 7 — Auditer les boucles de création et de gouvernance

But : éprouver la boucle créative, la boucle de gouvernance, le one-shot et la double boucle. Une itération ne compte que si elle change artefact, décision, preuve, portée ou robustesse.

Sortie : `LOOP-DIAGNOSTIC`.

État : **examen documentaire et machine achevé en 7.01–7.02 ; efficacité réelle ouverte**. `Audit_Phase7_01_LOOP_DIAGNOSTIC_Boucles_Creation_Gouvernance_One_Shot.md` reprend F-DIR-009/F-PC-001 : quatre essais distinguent garde-fou de présence de décision et simple rationale acceptée. `Audit_Phase7_02_LOOP_DIAGNOSTIC_Transmission_Retour_Reclassement.md` ajoute onze validations ciblées et la lecture des retours/reclassements sans preuve de leur exécution terrain. Aucun one-shot **réussi**, amélioration perceptuelle ou fermeture empirique de boucle n'est inféré. Phase 8 documentaire parcourue, phase 9 ouverte ; 6.02 mise de côté sur demande.

### Phase 8 — Audit multi-perspectives

But : couvrir douze perspectives : création visuelle, produit/usage, accessibilité/inclusion, contenu/communication, technique/runtime, preuve/épistémologie, agentique, équipe, gouvernance, production/opérations, expérimentation et migration.

Sortie : `PERSPECTIVE-COVERAGE-MATRIX`.

État : **8.01–8.02 terminées dans leur portée documentaire et machine ; efficacité humaine ouverte**. `Audit_Phase8_01_PERSPECTIVE_COVERAGE_MATRIX_Douze_Perspectives.md` donne aux douze perspectives niveau, owner et limite (six `FULL`, six `TARGETED`). `Audit_Phase8_02_PERSPECTIVE_COVERAGE_MATRIX_Cinq_Roles_Parcours_Handoff.md` suit cinq rôles fictifs et contrôle vingt résolutions CLI ciblées (six locators servis, quatre refusés par agencement ; titres présents) sans transformer leurs décisions théoriques en compréhension ou adoption. Suite : phase 9 en cours ; 6.02 différée.

### Phase 9 — Tests de résistance

But : sélectionner et rejouer selon le risque les **vingt** scénarios §19 (dont contenu long, référence séduisante, style recyclé et accessibilité tardive) ; ajouter un risque propre à B01 s'il n'entre dans aucun des vingt.

Sortie : `RESISTANCE-RESULTS`.

État : **ouverte ; 9.01 matrice préparatoire, 9.02–9.05 épreuves de contrat terminées**. `Audit_Phase9_01_RESISTANCE_RESULTS_Matrice_Vingt_Scenarios_Oracles.md` recense 20/20 intitulés exacts, dix `FULL` et dix `TARGETED`, chacun avec propriétaire, positif, négatif, antécédent et limite. `Audit_Phase9_02_RESISTANCE_RESULTS_Preuve_Fraicheur_Texte_Schema.md` éprouve 15/17/20 via onze appels (sept acceptations, quatre rejets) ; `Audit_Phase9_03_RESISTANCE_RESULTS_Composant_Partage_Deux_Decisions.md` éprouve 06 via huit appels (six acceptations, deux rejets) ; `Audit_Phase9_04_RESISTANCE_RESULTS_Action_Externe_Autorite_Confidentialite.md` éprouve 16 par huit appels (sept acceptations, un rejet) et oracle d'autorité fictif ; `Audit_Phase9_05_RESISTANCE_RESULTS_Migration_Aliases_Routes_Promotion.md` éprouve 18 par cinq appels (quatre acceptations, un rejet), lecture CLI et exports reconstruits. **Six scénarios éprouvés en contrat, aucun clos en efficacité `FULL`** ; S21 stage/ZIP réutilise 4.09 ; prochaine unité 9.06 surcharge procédurale. Les effets perceptuels, humains et de migration restent ouverts et **6.02 reste mise de côté**.

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

## Discipline des conclusions

- **Lu** signifie que la plage source est couverte par un rapport ; ce statut ne valide ni la conformité ni l'efficacité réelle.
- **Observé en test** signifie qu'une entrée, une sortie et un oracle sont documentés ; une suite verte ne prouve que les comportements effectivement exercés.
- **Constat provisoire** signifie qu'un écart ou un risque possède une preuve à recouper ; son owner, sa gravité, sa fusion éventuelle et sa correction restent ouverts.
- **Décision de patch** n'existe qu'après le classement et l'arbitrage des phases 10–11. Une correction doit ensuite passer les validations de la phase 13.
- **Workflow déclaré** et **workflow effectivement exécuté sur une plateforme hébergée** sont deux preuves différentes. Conserver cette distinction dans les rapports d'intégration.

## Prochaine unité de travail

### Phase 5.01 — Entrée, chemin de lecture et première action : terminée

Rapport : `Audit_Phase5_01_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Entrees_Parcours_Premiere_Action.md`. Baseline et propriétaires exacts revérifiés ; novice, correctif local, agent en reprise et trois cas discriminants ; six axes du §15 renseignés, route CLI et voie manuelle distinguées. Aucun nouvel ID : **157 fiches provisoires**. Les chiffres de transitions désignent des parcours documentaires choisis et non du temps ou de la compréhension humaine.

### Phase 5.02 — Organisation interne et usage opérationnel : terminée

Rapport : `Audit_Phase5_02_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Sections_Usage_Charge.md`. Sources, voisins et rapports sectionnels recoupés ; classements, preuves, reprises et sorties situés dans les quatre propriétaires. Le CLI extrait parfois une branche parent large (START 125 lignes, CRAFT 181, SELECT 94) et refuse certains titres non indexés. Le volume de réponse n'est pas la charge vécue. Aucune fiche nouvelle : **157 provisoires**, aucun patch.

### Phase 5.03 — Nécessité et coût des 60 sources : terminée

Rapport : `Audit_Phase5_03_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Matrice_Necessite_60_Sources.md`. Matrice strictement 60/60, par chemin du manifeste B01 et par consommateur humain/machine/build ; quatre fichiers GitHub volontairement absents de Local et README Local généré ; options de lecture/maintien provisoires, dépendances et conditions de test avant toute fusion ou suppression. Une fixture peut être nécessaire à un oracle sans être lue dans un run. **157 fiches provisoires**, aucun ID ni patch nouveau.

### Phase 5.04 — Synthèse des six axes : terminée

Rapport : `Audit_Phase5_04_INFORMATION_ARCHITECTURE_DIAGNOSTIC_Synthese_Six_Axes.md`. Le protocole §15 est renseigné axe par axe, par preuves positives, tensions, limite de mesure et vérification suivante. Les parcours 5.01, sections/CLI 5.02 et 60 chemins 5.03 sont liés aux propriétaires et aux risques déjà identifiés ; aucune fusion de constat ni nouvel ID à ce stade. La phase 5 est terminée dans sa portée documentaire B01 : **157 fiches provisoires**, aucun patch ni nombre final de fichiers décidé.

### Phase 6.01 — Premier objet et dix dimensions : terminée documentairement

Rapport : `Audit_Phase6_01_POSITIVE_CAPABILITY_DIAGNOSTIC_Premier_Objet_Dix_Dimensions.md`. Scène identitaire de cartographie sonore et écran opérationnel d'incidents comparés selon les dix dimensions ; les exemples se déclarent illustratifs et ne livrent pas de rendu inspectable. Condition d'arrêt d'un objet suffisant recoupée avec capture, preuve fraîche, B1b lorsqu'applicable et gate C. F-DIR-009, F-PC-001, F-ACT-005/007/012/018/021/022 et F-BIB-005 repris sans ID nouveau ; **157 fiches provisoires**, aucun patch.

### Phase 6.02 — Préparation d'épreuve sur pilotes : achevée ; observation en attente

Rapport : `Audit_Phase6_02_POSITIVE_CAPABILITY_DIAGNOSTIC_Pilotes_Preparation_Observation.md`. Aucun artefact d'interface des deux exemples n'existait dans le dossier. Deux pilotes fictifs, scène sonore et incident, ont été produits hors B01 ; l'archive `Phase6_02_Pilotes_Controle.zip` réunit HTML principal et cadre à iframe mobile de 390 × 844 px. Parsing HTML, scripts, identifiants et intégrité de l'archive vérifiés. L'ouverture locale par le navigateur de contrôle a été refusée par sa politique, qui interdit une voie alternative de contournement ; **aucune capture ni épreuve de geste réalisée**. La matrice des dix dimensions a ses critères, aucune valeur « PASS » sur rendu.

### Phase 7.01 — Boucles, one-shot et modification substantielle : terminée documentairement

Rapport : `Audit_Phase7_01_LOOP_DIAGNOSTIC_Boucles_Creation_Gouvernance_One_Shot.md`. Protocole §17/§27, cinq propriétaires, schéma/validateur de RUN_CARD et rapports 4.07/4.08/6.01/6.02 recoupés. Boucle créative, gouvernance de run et maintien des règles du corpus séparés. Quatre appels en mémoire vérifient que `decision_change` absent sous acceptation est refusé, mais qu'une nouvelle rationale textuelle non vide passe : la correction substantielle dépend d'un jugement sur les versions et preuves. **157 fiches provisoires**, aucun ID ni patch ; phase 7 ouverte.

### Phase 7.02 — Transmission, retour et reclassement : terminée documentairement

Rapport : `Audit_Phase7_02_LOOP_DIAGNOSTIC_Transmission_Retour_Reclassement.md`. Deux trajets fictifs, onze appels en mémoire ; retour et reclassement structurés passent, mais l'identité de direction A/B et la continuité LITE→STANDARD ne sont pas reliées. L'ancre déclarée transformée sous retour reste rejetée malgré preuve mobile distincte ; protection critique structurée et prochaine preuve obligatoire gardent leur effet. Références F-DIR-007/F-ACT-010/017/021, F-PC-001 et F-RC-001 reprises sans nouvel ID. **157 fiches provisoires**, aucun patch. Efficacité des boucles réservée.

### Phase 8.01 — Douze perspectives : matrice documentaire terminée

Rapport : `Audit_Phase8_01_PERSPECTIVE_COVERAGE_MATRIX_Douze_Perspectives.md`. Douze perspectives du protocole §18 traitées sans omission ; six `FULL` et six `TARGETED` adaptés aux risques et aux preuves déjà obtenues, pas au score d'un produit. Quatre interfaces transversales relient création/tâche/inclusion, contenu/runtime/preuve, agent/équipe/autorité, et expérimentation/production/migration. Les effets de rendus, utilisateurs et équipes restent ouverts. **157 fiches provisoires**, aucun nouvel ID ni patch.

### Phase 8.02 — Cinq rôles, routes et handoffs : terminée documentairement

Rapport : `Audit_Phase8_02_PERSPECTIVE_COVERAGE_MATRIX_Cinq_Roles_Parcours_Handoff.md`. Novice, praticien, agent, reviewer et mainteneur ont chacun une vignette de décision, preuve, condition d'arrêt et owner suivant ; ce sont des **rôles fictifs**, pas des participants. Sur dix locators dans deux agencements, six sont servis et quatre titres présents ne sont pas indexés ; le chemin GitHub de la skill ne résout pas l'agencement Local isolé. Le test ne rejoue pas les ZIP B01 ni une navigation humaine. Phase 8 couverte documentairement ; efficacité de compréhension/adoption non mesurée. **157 fiches provisoires**, aucun ID ni patch.

### Phase 9.01 — Vingt scénarios et oracles : matrice préparatoire terminée

Rapport : `Audit_Phase9_01_RESISTANCE_RESULTS_Matrice_Vingt_Scenarios_Oracles.md`. Les vingt questions du protocole §19 sont représentées sans omission ; dix `FULL` et dix `TARGETED` signalent une profondeur nécessaire et non un taux de réussite. Chaque cas a un positif, un négatif, un owner, son précédent pertinent et sa preuve encore requise. S21 stage/ZIP est distinct de la divergence texte/schéma et déjà observé sur copie isolée en 4.09. **Zéro nouveau scénario complet rejoué dans 9.01**, **157 fiches provisoires**, aucun nouvel ID ni patch.

### Phase 9.02 — Preuve, fraîcheur, cohérence des statuts : épreuve de contrat terminée

Rapport : `Audit_Phase9_02_RESISTANCE_RESULTS_Preuve_Fraicheur_Texte_Schema.md`. Onze validations sur exemples/fixture copiés en mémoire (sept admises, quatre refusées) testent trois scénarios §19 au niveau machine. Retour sans preuve, rejet d'acceptation sans observation, égalité de locators, blocage avec acceptation et contradiction littérale des claims protègent la projection ; une observation sans rapport avec le risque critique, une carte V2 avec preuve V1, un scope étendu et une escalade de même décision combinée à un verdict accepté restent admis. Les écarts prolongent F-ACT-010/012/018/021/022 et voisins sans compter quatre nouveaux défauts. **Trois épreuves de contrat, zéro scénario d'efficacité `FULL` clos**, **157 fiches provisoires**, aucun ID ni patch.

### Phase 9.03 — Composant partagé : chaîne de contrat à deux décisions terminée

Rapport : `Audit_Phase9_03_RESISTANCE_RESULTS_Composant_Partage_Deux_Decisions.md`. D-001 propose un token sous décision identitaire, S-001 examine sa migration avec owner distinct et retour faute de tests, S-002 porte directement la décision partagée. Huit validations en mémoire donnent six admissions et deux refus ; l'oracle externe marque un parent orphelin ou un token divergent malgré deux cartes admises, et un objet partagé déclaré STANDARD passe. `owner` manquant et champ parent typé ad hoc sont refusés. La réussite du lien textuel ne prouve aucune migration réelle ; F-SAV-007/F-BIB-004/F-ACT-002/011/015/021 gardent leur statut provisoire. **Quatre scénarios éprouvés en contrat au cumul de 9.02–9.03, zéro clos en efficacité `FULL` ; 157 fiches provisoires**, aucun nouvel ID ni patch.

### Phase 9.04 — Action externe : simulation de contrat terminée

Rapport : `Audit_Phase9_04_RESISTANCE_RESULTS_Action_Externe_Autorite_Confidentialite.md`. `DIRECTION/SERVICE-BOUNDARY` 115–117 réserve autorisation/exécution/observation au système qui détient la permission ; `ACTION/AUTHORITY` et confidentialité bornent scope, owner et canal. Huit cartes en mémoire : sept admises, une refusée (`critical_protection` absente). Un oracle externe **fictif** bloque quatre variantes sans permission exacte, scope, confirmation ou canal, alors que la projection reste admise ; il ne constitue ni permission réelle ni défaut automatique du validateur. Aucun appel d'envoi/publication, aucun nouvel ID ni patch ; **157 fiches provisoires, cinq scénarios éprouvés en contrat, zéro stress complet d'efficacité clos**.

### Phase 9.05 — Migration : contrat et exports isolés contrôlés

Rapport : `Audit_Phase9_05_RESISTANCE_RESULTS_Migration_Aliases_Routes_Promotion.md`. Les cinq aliases historiques sont reclassés par `CHANGELOG` et interdits en nouveau run par `BIBLIOTHEQUE/EVOLUTION` ; le lecteur les refuse tous. Le schéma `RUN_CARD.sources` admet pourtant `REFERENCES/SOURCE` et un texte d'adoption sans preuve ; quatre admissions et un refus `owner` absent sur cinq cartes en mémoire. Les destinations `SAVOIR/SOURCE` et `SAVOIR/TOOLS` existent dans la source mais ne sont pas indexées par la CLI ; F-DIR-028/F-ACT-001 déjà ouverts. GitHub 60/60 et Local 56/56 ont été reconstruits dans une copie isolée ; aucune release distante ou migration réelle attestée. L'échec d'un lancement depuis un répertoire extérieur reproduit F-ALL-002 ; lancement depuis la racine de la copie passé. **157 fiches provisoires, six scénarios éprouvés en contrat, zéro stress complet d'efficacité clos ; aucun nouvel ID ni patch.**

### Suite prévue : phase 9.06 ; phase 6.02 mise de côté temporairement

- Rejouer le scénario 19 « Surcharge procédurale » : opposer un delta strictement local à un changement dont le risque ou la preuve demande des étapes supplémentaires. Ne retirer une étape que si elle ne modifie ni décision, ni artefact, ni preuve ; ne pas mesurer la charge humaine à partir du seul texte. Revoir propriétaires, voisins et rapport 9.01 avant essai.
- Conserver le rapport 6.02, ses deux pilotes hors B01 et la preuve perceptuelle manquante comme réserve ouverte. L'utilisateur a demandé de **mettre 6.02 de côté pour l'instant** : ne pas entreprendre son inspection pendant la suite documentaire sans nouvelle demande.
- Après phase 8, réserver les tests de résistance à la phase 9 puis classement/arbitrage aux phases 10–11, sans anticiper les patches.

### Conditions de reprise ultérieure de 6.02 (en attente d'une demande)

- Obtenir des captures produites par une ouverture autorisée des deux pilotes, ou des objets comparables accessibles, avec fichier/version, état, viewport, date/méthode et limite ; voir dans le rapport 6.02 la liste des vues nominales, indisponibles, succès et mobiles. Les pilotes ne constituent pas une preuve que le système produit régulièrement ces objets.
- Inspecter sans rationale, comparer les dix dimensions applicables, les gestes réellement exécutés et la recomposition ; séparer preuve perceptuelle, tâche, accessibilité et technique. Activer une paire B1b uniquement sous son déclencheur B01 et juger si garder l'original est justifié.
- Conclure 6.02 seulement après les observations requises et statuer alors sur la clôture de phase 6 ou une unité supplémentaire motivée. Tant que les captures manquent, conserver **phase 6 ouverte**, sans déduire la qualité du HTML seul.

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
2. ouvrir le rapport du bloc immédiatement précédent et le dernier checkpoint du propriétaire concerné, s'il existe ;
3. revérifier les hashes système et protocole ;
4. relire la phase du protocole applicable ;
5. lire la source exacte du bloc, identifier ses interfaces amont et aval, puis rouvrir dans leurs sources exactes les passages reliés, déjà lus ou nouveaux ;
6. charger les constats antérieurs concernés par leurs IDs et contrôler les dépendances ou réserves transmises par le bloc précédent ;
7. exécuter les tests pertinents ;
8. rédiger le rapport sectionnel, en consignant pour chaque interface examinée la preuve, la contradiction ou la vérification différée ;
9. vérifier couverture, IDs, points transmis à la suite et absence de patch ;
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
