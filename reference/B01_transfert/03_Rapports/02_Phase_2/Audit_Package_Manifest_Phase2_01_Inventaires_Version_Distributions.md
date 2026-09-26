# DG-AUDIT-001 — Phase 2 — `package_manifest.json` : inventaires, version et distributions

## Cadrage et intégrité B01

**Cible :** lecture complète **1–124/124** de `scripts/package_manifest.json` suivant les passages A–D du protocole externe v2.0 §12. **Rôle :** déclarer la version du package et les chemins attendus dans les exports GitHub et Local ; les validateurs et le build consomment ses deux listes. **Échelle :** manifeste, fichiers sources reconstruits, `validate_design_governance.py`, `build_distributions.sh`, `validate_all.py`, sorties `dist` et archives. **Risque dominant :** un inventaire annoncé complet, numériquement trompeur ou incohérent avec la version livrée. L'audit exhaustif du build et du workflow appartient aux deux unités suivantes ; leur interface concrète est néanmoins éprouvée ici. Aucun patch, verdict global ou publication ne fait partie de cette phase.

Empreintes recalculées avant le bloc : compilation `Design_Governance_V1.0.md` SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole v2.0 SHA-256 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, manifeste SHA-256 `bef40232b2cbb1fdc8fda4d2bfc6bb752e9abbc3705d9a662eb44aa8da266f8b`. La reconstruction des 60 unités de B01 conserve les tailles et nombres de lignes recensés dans la baseline. Toutes les épreuves ci-dessous se font dans des copies temporaires ; le corpus reçu ne change pas.

Rapports d'interface relus : `Audit_Validate_Design_Governance_Phase2_01_Inventaire_Liens_Conventions.md` (F-VDG-001 à 004), `Audit_Validate_ALL_Phase2_01_Orchestration_Oracles_Build_Reprise.md` (F-ALL-001/002), `Audit_Read_Route_Phase2_01_Resolution_Extraction_GitHub_Local.md` (F-RRT-001), et plan maître actif. Le protocole §12 impose de distinguer l'existence d'un fichier, le contenu livré et le résultat opérationnel du système.

## Passage A — architecture visible, lignes 1–124

| Lignes | Contenu déclaré | Interface réelle |
|---|---|---|
| 1–3 | Racine JSON, `version: "1.0.0"`, début de `github`. | Les scripts lisent `github` et `local` ; aucun contrôle observé ne lit `version` pour comparer README ou release notes. |
| 4–17 | Métadonnées du dépôt et dix textes `V1/official`. | Le GitHub déclare workflow, `.gitignore`, README et release notes. Les dix textes officiels couvrent cinq propriétaires et cinq façades/entrées. |
| 18–50 | Schémas, exemples, fixtures. | Trente-trois chemins `schemas/`, dont le schéma RUN_CARD, ses exemples et les fixtures ; leur justesse métier reste celle des rapports de schémas et du validateur. |
| 51–64 | Huit scripts et cinq fichiers de skill pratique. | Le build et le workflow figurent parmi les chemins GitHub ; la liste elle-même n'exécute ni ne valide leur comportement. |
| 65–76 | Début de `local` : README généré et dix textes sous `official/`. | Le contenu du README Local est écrit par le build ; les autres textes proviennent de `V1/official`. |
| 77–109 | Les trente-trois chemins `schemas/` avec la même orthographe qu'en GitHub. | Transfert de schémas et fixtures dans l'export autonome. |
| 110–124 | Sept scripts sous `scripts/` et cinq références sous `skill/`, fin du JSON. | `scripts/build_distributions.sh` est absent de Local à dessein ; le lecteur de routes, le validateur de carte et les contrats y sont conservés. |

Différence d'inventaires après réécriture `V1/official/* → official/*` et `skills/design-governance-practice/* → skill/*` : Local omet exactement **quatre** chemins GitHub (`.github/workflows/validate.yml`, `.gitignore`, `RELEASE_NOTES.md`, `scripts/build_distributions.sh`). `README.md` est conservé comme chemin mais généré dans Local. B01 déclare **60** chemins GitHub (60 distincts) et **56** chemins Local (56 distincts) ; `version` vaut `1.0.0` comme les textes de présentation reçus.

## Passage B — contrats éprouvés et contre-épreuves

**Baseline positive.** Les 60 chemins GitHub du manifeste sont exactement les 60 fichiers sources non générés, sans manquant ni supplémentaire. Un build isolé rend code 0 ; `dist/github` contient 60/60 chemins déclarés et son zip les mêmes 60, chacun une seule fois. `dist/local` contient 56/56 chemins déclarés et son zip les mêmes 56. Les 60 fichiers GitHub sont identiques octet pour octet aux sources ; les 55 fichiers Local copiés sont identiques à leurs sources correspondantes, et le README Local est le seul des 56 généré dans le build. Cela prouve la concordance des octets de **cette reconstruction** et de **ce build** ; pas la provenance d'un dépôt Git externe ni l'exécution du workflow distant.

Le validateur documentaire convertit la liste en `set(EXPECTED)` pour comparer les fichiers réels, tout en affichant `len(EXPECTED)` en sortie. Le build Local boucle sur les entrées du manifeste pour vérifier l'existence mais affiche lui aussi leur nombre brut. La clé `version` ne fait l'objet d'aucune comparaison dans ces contrôles. Résultats discriminants :

| Mutation isolée sur copie | Résultat observé | Interprétation bornée |
|---|---|---|
| Ajouter une deuxième fois `README.md` à la liste GitHub. | `validate_design_governance.py` code **0**, annonce « **61 fichiers attendus** » ; `validate_all.py` code **0 / FULL VALIDATION PASSED** ; l'archive GitHub contient **60 fichiers réels**. | F-MAN-001 : déclaration numérique de couverture erronée, sans perte de contenu B01. |
| Ajouter une deuxième fois `official/README.md` à la liste Local. | Le build code **0** ; vérification Local annonce « **57 fichiers attendus** », l'export contient **56 fichiers réels** ; suite complète code **0 / FULL VALIDATION PASSED**. | Même F-MAN-001 sur l'autre profil ; l'inventaire `set` masque la répétition tandis que le compteur brut l'affiche. |
| Changer seulement `version` en `9.9.9`, puis dans un second essai supprimer entièrement cette clé. | Chaque variante passe le validateur documentaire et `validate_all.py` avec **code 0 / FULL VALIDATION PASSED** ; les deux README continuent d'annoncer `1.0.0` et GitHub conserve ses release notes `1.0.0`. | F-MAN-002 : la métadonnée de version peut devenir contradictoire ou absente sans signal. Une lecture du manifeste seul ne prouve donc pas la version du package. |
| Remplacer le chemin GitHub `.github/workflows/validate.yml` par `missing/workflow.yml` sans toucher aux fichiers. | Validateur documentaire **code 1 / VALIDATION FAILED** : « fichier attendu absent » et « fichier inattendu » ; suite complète **code 1**. | Protection réelle contre une entrée ordinaire erronée ; la traceback de la suite vient de l'orchestration d'un sous-processus en échec, pas d'un faux PASS. |

Les mutants sont indépendants. Le fait qu'un compteur puisse être trompeur n'établit pas que le package B01 contient un fichier en moins. Le fait que `version` soit peu contrôlé n'établit pas que la version B01 est fausse : sa valeur reçue est cohérente avec les documents inspectés.

## Passage C — lecteurs et frontières de preuve

**Mainteneur et responsable de release :** la comparaison ensembliste refuse bien un chemin manifestement absent ou un fichier ordinaire supplémentaire. Elle ne garantit ni l'unicité des entrées de la liste ni l'égalité entre la version déclarée et les documents distribués. Un compteur « 61 attendus » sur un zip de 60 peut conduire à une mauvaise conclusion d'inventaire lors d'une revue ou d'une migration, même si les 60 fichiers attendus de B01 sont actuellement présents.

**Intégrateur Local :** l'export a volontairement un README généré et n'embarque pas le script de build ; les chemins relatifs `official/` et `skill/` sont correctement adaptés dans la baseline. La validation du Local et du GitHub consomme le **même manifeste** inclus dans chaque export ; une liste modifiée et son contrôle peuvent donc rester cohérents entre eux sans être indépendants de la déclaration. Le build apporte néanmoins des copies explicites, des tests Local et des archives dont les chemins ont été confrontés au manifeste dans cette unité.

**Agent, designer ou reviewer :** ni `version: 1.0.0`, ni `FULL VALIDATION PASSED` n'établissent la qualité d'une direction, la preuve d'usage, la compatibilité réelle d'une migration ou l'état d'un artefact. Le contenu des règles appartient aux cinq sources normatives, et le contrat de preuve à ACTION et aux schémas concernés. Cette frontière conserve la portée appropriée de l'inventaire.

## Passage D — fiches provisoires et suite

### F-MAN-001 — doublons admis et compteur de fichiers inexact

**Preuve :** deux copies distinctes avec un doublon GitHub ou Local gardent un PASS global ; le validateur transforme `EXPECTED` en ensemble pour l'écart de chemins mais imprime sa longueur brute, et le build Local fait la même annonce à partir de la liste. Les décomptes mutés **61/60** et **57/56** divergent des archives réelles. **Effet :** l'assertion de couverture chiffrée peut tromper une revue de distribution ; aucune perte réelle de fichier n'est démontrée par cette mutation. **Owner pressenti :** contrat de structure du manifeste et comptage du validateur/build. **Épreuve de résolution :** refuser toute entrée répétée dans chaque liste, conserver 60/56 sur B01 et rejeter les deux duplications ciblées, sans bloquer un ajout légitime accompagné de son fichier. Gravité finale ouverte, a priori inférieure à une disparition non détectée de règle.

### F-MAN-002 — version déclarée facultative et non corrélée au package

**Preuve :** `version` ligne 2 n'est pas lue par les validateurs ni par le build comme invariant ; les variantes `9.9.9` et clé absente produisent un PASS complet tout en distribuant des documents qui continuent d'annoncer `1.0.0`. **Effet :** version machine trompeuse ou absente pour un consommateur du manifeste, avec risque de mauvaise attribution de release ou de migration ; aucun écart de version n'est observé dans B01. **Owner pressenti :** contrat de version du manifeste, en interface avec README, release notes et sortie du build. **Épreuve de résolution :** décider si la clé est obligatoire et quelle source fixe la version, puis tester une valeur divergente ou absente et préserver le cas 1.0.0 valide ; ne pas créer une autorité de version concurrente. Gravité finale ouverte.

**Déduplication :** F-VDG-001 porte sur un fichier supplémentaire **hors inventaire** caché sous un nom de dossier exclu et néanmoins archivé ; F-MAN-001 porte sur des lignes **dupliquées dans l'inventaire** sans fichier supplémentaire. Le test antérieur où workflow et entrée du manifeste disparaissaient ne suffisait pas à établir un faux PASS global, car le build copie ce workflow explicitement ; ne pas l'attribuer à F-MAN-001. F-MAN-002 vise la version comme métadonnée de livraison, distincte des constats sur le fond des textes et de F-ALL-001 sur le motif d'échec. Ces candidats de fusion et gravités seront réexaminés aux phases 10–11.

**Registre :** **142 fiches provisoires avant** cette unité, **144 après F-MAN-001/002**. Ce nombre n'est pas un total de corrections décidées. **Prochaine unité :** lire `scripts/build_distributions.sh` **1–166/166** en passages A–D, puis `.github/workflows/validate.yml` **1–22/22** ; confronter copies, validations, publication atomique et reproductibilité aux deux profils du manifeste. Pas de patch ni de verdict global en phase 2.
