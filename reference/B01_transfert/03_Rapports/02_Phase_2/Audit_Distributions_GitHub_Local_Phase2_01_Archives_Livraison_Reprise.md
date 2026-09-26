# DG-AUDIT-001 — Phase 2 — Distributions GitHub et Local : répertoires, archives et reprise

**Date :** 24 septembre 2026. **Baseline :** B01. **Profondeur :** FULL sur les deux distributions comme objets livrés ; passages A–D du protocole maître externe v2.0 §12. **Rôle :** confronter chemins et octets du stage, des ZIP et de leur extraction aux 60 sources déclarées GitHub et aux 56 fichiers Local dérivés. Les distributions sont des sorties, pas des propriétaires normatifs. Aucune correction B01, aucune publication externe.

Empreintes des entrées revérifiées : compilation `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; manifeste `bef40232b2cbb1fdc8fda4d2bfc6bb752e9abbc3705d9a662eb44aa8da266f8b` ; build `558167c41d066df1ed82f9a6ec9b294b3e6270309be874731bbc85b3aae1d956`. Rapports rouverts : manifeste, build, validateur documentaire, skill, README racine, notes de release et inventaire des archives de migration ; sources exactes du manifeste, de `.gitignore`, du build et de la skill confrontées. Exécution dans une copie de `audit_work/package` sous `/tmp/dg-audit-distributions-ZZndV2/package`, puis extraction sous `/tmp/dg-audit-distributions-ZZndV2/unpacked/` ; ce répertoire temporaire est une preuve de session, pas un livrable durable. Les 60 sources B01 originales ne sont pas modifiées.

## Passage A — Architecture des deux livrables

| Interface | GitHub | Local | Propriétaire et lecture |
|---|---|---|---|
| Inventaire déclaré, manifeste `github` et `local` | 60 chemins ; `README.md`, `RELEASE_NOTES.md`, `.gitignore`, workflow, cinq propriétaires sous `V1/official/`, skill sous `skills/design-governance-practice/`, schémas et huit scripts. | 56 chemins ; README généré, propriétaires sous `official/`, skill sous `skill/`, mêmes schémas/fixtures et sept scripts. | Le manifeste décrit les deux profils. Les quatre omissions Local — release notes, `.gitignore`, workflow, script de build — sont intentionnelles ; les autres renvois de racine sont réécrits par le build. |
| `dist/github/`, `dist/local/` | Copie sous arborescence versionnée. | Export autonome avec chemins directs. | `build_distributions.sh` 13–43 copie et 44–105 écrit le README Local ; 107–140 valide les stages ; 143–166 nettoie, archive et promeut. |
| `Design_Governance_V1_GITHUB.zip`, `Design_Governance_V1_LOCAL.zip` | Archive des fichiers du stage GitHub. | Archive des fichiers du stage Local. | Les fichiers ZIP sont générés séparément avant la promotion de `dist` ; leur existence ne prouve pas à elle seule un build achevé. |

Le `README.md` Local **n'est pas** une copie du README GitHub : il guide vers `official/*`, annonce l'absence du build/reproductibilité Local et donne les commandes utilisables dans cet export. La skill et ses quatre références sont copiées à octets identiques, sous des chemins différents. Le `CHANGELOG.md` actuel avec les cinq anciennes routes `REFERENCES/*` est livré dans les deux profils ; les archives historiques hors package ne sont pas introduites dans les exports.

## Passage B — Mesures du build, des octets et des ZIP

Commande sur copie isolée : `bash scripts/build_distributions.sh`, **code 0** ; la validation du stage GitHub annonce 60 attendus, celle du Local 56, avec validateurs documentaires, RUN_CARD, contrats et carte. Contrôle **indépendant** réalisé en ouvrant les archives par `zipfile` : inventaire de chaque entrée, doublons, mode de fichier, test CRC, comparaison des octets de chaque entrée avec le stage, puis comparaison des fichiers copiés avec leur origine B01.

| Mesure de cette reconstruction | GitHub | Local |
|---|---:|---:|
| Chemins attendus par le manifeste | 60 | 56 |
| Fichiers réguliers dans `dist` | 60 | 56 |
| Entrées fichier dans ZIP | 60 | 56 |
| Manquants / supplémentaires dans `dist` et ZIP ; doublons ZIP | 0 / 0 ; 0 | 0 / 0 ; 0 |
| Octets divergents stage ↔ source ou ZIP ↔ stage | 0 sur les 60 sources | 0 sur les 55 fichiers copiés et 0 sur 56 entrées ZIP ; README généré contrôlé comme tel |
| Liens symboliques, types ZIP inattendus, cache `__pycache__` ou `.pyc` dans archive | 0 | 0 |
| `ZipFile.testzip()` | Aucun membre défaillant | Aucun membre défaillant |
| SHA-256 du ZIP de cette copie | `a1891557ced4ed1481e509986c84d4c56ad3dbcd381a0c388267d59c9b3cdc97` | `8dc4a4483a6723cad3faad88f275aa8d40940e961c3357a896629e574a3307b0` |

Le README GitHub conserve exactement son empreinte source `baea59563bdde0ad3683c2a96514df0d37b68a4944b39103e9dac6925c913a5c` ; le README Local généré porte `693c3cb08c508105202b9bd1fc1cf2161faad45e8caad65c923d28084a872441`. Les **sept liens relatifs** du README GitHub et les **trois** du README Local extraits pointent vers des fichiers présents ; les deux manifests déclarent `1.0.0`, et les deux README affichent `V1.0.0`. `read_route.py DIRECTION/START` retourne **code 0** depuis chacune des deux racines extraites. Les contrôles précédents de l'ancre GitHub (1/1) restent rapportés dans le rapport du README et ne sont pas transformés ici en contrôle de tous les fragments Markdown.

Deuxième exécution du build **sans modification** dans la même copie : **code 0** ; les deux SHA-256 ZIP ci-dessus sont identiques avant et après. L'extraction des deux archives dans de nouveaux dossiers est suivie de `python3 scripts/validate_all.py` depuis chaque racine : GitHub **code 0 / `FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité`** ; Local **code 0 / `LOCAL VALIDATION PASSED`**, qui exclut explicitement build et reproductibilité. Ces tests exécutent les scripts livrés dans l'archive ; ils n'exécutent pas le workflow GitHub sur une plateforme hébergée. Les fichiers de cache apparus pendant cette exécution *après extraction* ne sont pas comptés comme contenus du ZIP initial.

## Passage C — Lecture des consommateurs

**Destinataire du ZIP GitHub :** l'extraction fournit `V1/official/READING_MAP.md`, notes de release, script de build et workflow. Le README, la skill et `read_route.py` orientent correctement vers `DIRECTION/START` ; la suite complète fonctionne sur ce ZIP extrait. Il s'agit du paquet reconstruit de B01 dans ce poste, sans vérification d'une version publiée sur Git distant.

**Destinataire du ZIP Local :** l'extraction fournit `official/READING_MAP.md` et un README qui y mène. La skill partagée contient toujours le chemin littéral `V1/official/READING_MAP.md` à sa ligne 16 : ce chemin manque dans le Local extrait, alors que la carte existe sous `official/`. **F-SK-002 est reproduit sur l'archive extraite**, avec atténuation par le README Local ; il n'y a pas de deuxième carte manquante. La suite Local marche depuis cette archive extraite, mais ne peut pas prétendre vérifier la reproductibilité d'un build qu'elle ne contient pas.

**Mainteneur de release :** le succès de la présente reconstruction démontre une correspondance entre source, dossier et archive pour **ce B01 propre**. Le manifeste et le build sont les mêmes déclarations/logiciels que ceux inclus dans le paquet ; le contrôle indépendant des entrées ZIP donne une preuve supplémentaire de composition dans cette unité, mais n'est pas un gate du build actuel. Les contre-épreuves antérieures F-VDG-001, F-BLD-001/004 montrent comment un ZIP sur copie modifiée peut être contaminé ou incomplet malgré un PASS ; F-BLD-002/003 montrent des générations mixtes ou une sauvegarde perdue en cas de panne. Le deuxième build identique ne réfute aucun de ces scénarios.

**Reviewer de qualité produit :** la validation des textes, chemins et projections ne mesure ni efficacité sur runs réels, ni rendu observé, ni accessibilité exécutée, ni adoption. Le `CHANGELOG.md` et les notes de release déclarent ces limites. Les routes, règles et migrations publiques doivent être jugées dans les sources normatives B01, pas dans les artefacts dérivés.

## Passage D — Résistance, rattachements et sortie

| Résistance vérifiée | Résultat de B01 et réserve conservée |
|---|---|
| ZIP périmé, entrée supplémentaire ou fixture manquante | Aucun dans la présente reconstruction : chemins exacts, octets exacts, zéro doublon et zéro symlink. La suite automatisée ne fait pas ce contrôle ZIP indépendant ; F-VDG-001 et F-BLD-001/004 restent provisoires sur mutations déjà documentées. |
| Identité de version et doublons du manifeste | `version: 1.0.0` et 60/56 chemins uniques dans B01 ; F-MAN-001/002 restent des tests de résistance à un manifeste modifié, sans fausse déclaration sur ce ZIP. |
| Paire de ZIP et dossier lors d'une panne | Aucun échec dans ces deux builds propres ; F-BLD-002/003 portent des pannes injectées dans le rapport du build, non une panne observée ici. |
| Chemin de carte selon la distribution | GitHub et Local comportent chacun une carte ; le chemin GitHub conservé dans la skill Local est inexistant : F-SK-002 confirmé après extraction. |
| Publication, workflow CI, autonomie absolue | Provenance d'un dépôt externe et CI hébergée non observées ; F-WF-001 reste une réserve de configuration du workflow. « Autonome » signifie ici que l'extraction et les contrôles Local fonctionnent dans cette copie sans dépôt distant ; cela ne certifie pas tous les environnements. |

Les raccourcis du README `ITER` (F-RDR-001) et la gouvernance des routes du CHANGELOG (F-CHG-001) restent inchangés dans les octets livrés ; aucune différence transport introduite par cette reconstruction ne les résout. Aucun nouveau constat propre aux distributions propres n'est isolé : **157 fiches provisoires avant et après**, sans décision de patch ni verdict global.

**Sortie :** comparaison complète stage ↔ manifestes ↔ ZIP ↔ extraction pour B01, tests d'usage par les deux suites extraites, frontière entre preuve du paquet courant et résistance aux mutations/pannes. **Prochaine unité :** checkpoint final de couverture et d'interfaces de la phase 2, avec condition d'entrée de la phase 3. Aucun changement du package B01.
