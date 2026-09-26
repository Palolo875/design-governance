# DG-AUDIT-001 — Phase 2 — Mémoire de migration : inventaire, archives et autorité

## Cadrage et intégrité B01

**Question examinée :** l'intitulé « mémoire de migration » dans le plan désigne-t-il une source résiduelle du package B01, une archive historique accessible, ou une pièce absente ? **Portée :** inventaire complet des fichiers sources de B01 ; passages utiles des textes B01 et de deux témoins historiques accessibles séparément ; comparaison des mappings des cinq anciennes routes `REFERENCES/*`. Les archives ne sont pas élevées au rang de sources normatives B01. Cette unité qualifie le périmètre, elle n'audite ni tout l'historique ancien ni les distributions comme artefacts livrés.

Empreintes revérifiées : compilation B01 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole externe v2.0 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; `V1/official/CHANGELOG.md` `0876654994f063ebb670392a5967044ad483bbdb8ebf6b5ce8a156609f08df45` ; `README.md` racine `baea59563bdde0ad3683c2a96514df0d37b68a4944b39103e9dac6925c913a5c`. Sources normatives inchangées. L'inventaire et les recherches sont en lecture seule.

**Dépendances reprises :** `Audit_README_Racine_Phase2_01_Entree_Modes_Liens_Validation_Exports.md`, `Audit_Release_Notes_Phase2_01_Version_Distributions_Controles_Limites.md`, `Audit_CHANGELOG_Phase2_01_Baseline_Autorite_Cycle_Migration_Limites.md`, `Audit_Package_Manifest_Phase2_01_Inventaires_Version_Distributions.md`, `Audit_Build_Distributions_Phase2_01_Stages_Archives_Reprise.md`, baseline B01 et protocole §12. Le rapport de manifeste avait déjà établi 60 chemins GitHub et 56 Local, avec concordance des sources non générées et des builds isolés ; la présente unité contrôle la question supplémentaire de l'existence et de l'autorité d'une mémoire de migration.

## Passage A — Architecture visible et inventaire

| Pièce / locator | Observation vérifiée | Statut pour B01 |
|---|---|---|
| `scripts/package_manifest.json`, `github` lignes 3–64 ; arborescence `audit_work/package/` | Les **60 chemins déclarés** sont uniques et coïncident exactement avec les **60 sources non générées** sur disque : aucun fichier manquant ni supplémentaire dans cet ensemble. Aucun chemin `migration`, `memory` ou `REFERENCES.md`. | Périmètre déclaré des sources GitHub B01 ; l'export Local en déclare 56, à contrôler comme objet livré dans l'unité suivante. |
| `V1/official/CHANGELOG.md` 24–29, 44–56 | Cinq propriétaires normatifs, détail de construction et de travail annoncé **hors distribution publique** ; table publique de migration des cinq aliases et statut ambigu `NOT-VERIFIED`/`EXPLORATORY`. | Autorité B01 pour ces règles et mappings. |
| `RELEASE_NOTES.md` 58 ; compilation `Design_Governance_V1.0.md` 2121, 2136–2150 | Même frontière déclarée pour l'historique ; la compilation contient aussi la table de migration du `CHANGELOG`. | Confirme une absence annoncée de l'historique détaillé, sans créer de document B01 supplémentaire. |
| `REFERENCES_—_Corpus_visuel,_exemples_et_mémoire_de (1).md`, ID `libfile_6e6e30faa15c8191ac8cf27c4757a9e6`, titre et lignes 1–35 | Ancien texte « Corpus visuel, exemples et **mémoire de décision** », version interne 2.5 datée du 14 août 2026, avec routes `REFERENCES/QUERY`, `/SOURCE`, `/ASSET`, `/MEMORY`, `/CORPUS`. Le mot « migration » n'y qualifie pas son titre. | Témoin historique **extérieur** aux 60 sources B01, pas une « mémoire de migration » autonome. |
| `CHANGELOG_—_Système_de_design_senior (11).md`, ID `libfile_3bb189dfeeb48191bed50196f85d8ba4`, lignes 1–5, 149–183 | Ancien registre v2.6 daté du 16 août 2026 ; vraie rubrique `CHANGELOG/MIGRATION` avec ancien mapping des documents et aliases, et indication que les anciens artefacts de migration n'étaient plus des sources concurrentes à cette époque. | Archive historique extérieure à B01 ; explique une partie de l'origine possible de l'expression, sans prouver qu'un fichier B01 de ce nom ait existé. |

**Trace locale distincte :** l'arborescence de travail contient actuellement `scripts/__pycache__/read_route.cpython-312.pyc`, produit par une exécution Python antérieure. Ce binaire n'est ni une 61e source ni une pièce de migration. `.gitignore` exclut `__pycache__/` et `*.py[cod]` ; `build_distributions.sh` lignes 143–144 nettoie les caches dans les deux stages. Il faut donc qualifier les « 60 » comme **sources non générées**, et conserver ce cache comme observation d'état du dossier, pas comme chemin du manifeste. F-VDG-001 rappelle séparément qu'une exclusion déclarée ne garantit pas à elle seule l'absence de tout autre contenu parasite dans un export construit.

## Passage B — Contrat sémantique et comparaison des versions

L'ancien `REFERENCES` conserve cas, sources, assets, mémoire de session et corpus ; son en-tête déclare explicitement ne pas décider le mode, le pipeline ni les règles de craft. Il avertit qu'une fiche historique sans source observée reste illustrative (`REFERENCES`, lignes 1–12, 207–215). Sa présence dans les archives aide à interpréter les noms d'aliases, mais ses routes présentées comme actives en v2.5 **ne** décrivent **pas** le routage public V1.0.0.

| Ancien alias | Archive v2.6, `CHANGELOG/MIGRATION` 170–175 | B01, `CHANGELOG.md` 48–54 | Conséquence pour le lecteur |
|---|---|---|---|
| `REFERENCES/QUERY` | `MICRO/QUERY_HEALTH` | `SAVOIR/TOOLS` pour une recherche ou un claim à vérifier | Le routage ancien ne doit pas supplanter le propriétaire actuel. |
| `REFERENCES/SOURCE` | `SAVOIR/SOURCE` et source locale du run | `SAVOIR/SOURCE` pour ancre ou référence observée | Même owner principal ; la condition de source observée reste décisive. |
| `REFERENCES/ASSET` | Trace locale du run et artefact projet | `DIRECTION/VISUAL_TARGET` pour route/rôle ; `SAVOIR/SOURCE` pour provenance/limite | B01 répartit explicitement décision et provenance entre deux propriétaires. |
| `REFERENCES/MEMORY` | `RUN_CARD` | `TRACE-LOCATOR` et artefact local ; la mémoire n'est pas normative | Ancienne destination trop courte pour être reprise comme règle V1.0.0. |
| `REFERENCES/CORPUS` | `CHANGELOG/MIGRATION` ou archive | Propriétaire normatif réellement concerné ; `CHANGELOG` seulement si le package change | L'archive n'est pas propriétaire universel du corpus actuel. |

Les dates et mentions de version établissent que les deux témoins sont **antérieurs** à B01 ; elles ne permettent pas de démontrer toutes les étapes intermédiaires ni une filiation complète de chaque règle. Les 60 fichiers B01 suffisent à établir la table **publique actuelle** et la portée déclarée de l'historique externe ; ils ne prouvent pas que toutes les décisions historiques ont été conservées ou que la migration a été éprouvée en production. Il n'existe pas de document séparé « mémoire de migration » **dans le périmètre de 60 sources** ; la recherche de titres d'archives accessibles n'a pas découvert de pièce portant exactement ce nom, sans prétendre prouver une inexistence absolue dans tout historique ou espace externe.

## Passage C — Usage sous contrainte

**Agent ou intégrateur reprenant un ancien run :** identifier la version du run, lire la table `CHANGELOG.md` de B01, router chaque alias selon son objet et enregistrer la limite si le propriétaire n'est pas établi. Lire directement `REFERENCES` v2.5 comme guide actif risquerait de recréer une sixième source d'autorité ; substituer le mapping v2.6 au tableau B01 serait incorrect pour au moins QUERY, ASSET, MEMORY et CORPUS.

**Mainteneur d'audit :** garder le document v2.6 comme preuve historique pour la phase migration, avec son ID exact et ses lignes, puis revenir aux propriétaires B01 lorsque leur contrat est en cause. Une table d'archive n'est pas une preuve de comportement d'une distribution V1.0.0. Si un run réel ancien est fourni plus tard, l'épreuve de migration devra comparer ses anciens champs et traces à la reclassification actuelle, avec réserve lorsque le propriétaire n'est pas vérifié.

**Utilisateur de la distribution :** il dispose déjà dans B01 de la migration **des cinq anciens aliases** ; le texte lui dit que l'historique de travail est hors distribution et non requis pour l'usage/validation V1. L'absence de l'archive dans la livraison n'est donc pas, en elle-même, un fichier manquant du package. Cette conclusion reste bornée à l'inventaire déclaré et aux contrats de publication lus ; elle ne démontre pas l'exhaustivité historique d'une migration réelle.

## Passage D — Résistance, déduplication et sortie

- **Ambiguïté corrigée dans le plan :** « mémoire de migration » n'était pas un nom de fichier B01 attesté. Les pièces vérifiées sont un ancien `REFERENCES` qualifié « mémoire de décision », un ancien `CHANGELOG/MIGRATION` et le `CHANGELOG.md` public actuel. Les distinguer évite de déclarer à tort une source manquante.
- **Contradiction temporelle potentielle :** les destinations historiques ne coïncident pas toutes avec B01 ; la table B01 prévaut. Cette différence entre versions n'est pas une contradiction interne démontrée de B01 et ne crée donc **aucune nouvelle fiche de défaut**.
- **Preuve de migration réelle encore ouverte :** sans ancien run ni trajectoire complète entre les versions, ne pas affirmer que toute ancienne trace a été migrée correctement. Transporter cette question à la phase d'épreuves de migration ; ne pas diluer F-CHG-001 (cycle de vie des routes) et F-MAN-002 (version du manifeste).
- **Épreuve restante avant checkpoint de phase 2 :** inspecter les **distributions GitHub et Local comme livrables**, leurs chemins, octets, archives, exclusions, README distincts, déclarations de version, limites de validation et écarts éventuels. Reprendre F-BLD-001 à 004, F-VDG-001, F-MAN-001/002, F-SK-002 et les rapports de build/manifeste sans double compte.

**Registre :** 157 fiches provisoires avant et après cette unité ; aucun patch, aucune décision finale. **Sortie de cette unité :** inventaire qualifié, témoins historiques identifiés, frontière d'autorité explicitée, prochaine cible définie. La phase 2 demeure ouverte.
