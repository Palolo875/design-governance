# DG-AUDIT-001 — Phase 2 — Validateur documentaire : inventaire, liens et conventions

## Cadrage et intégrité

**Cible :** `scripts/validate_design_governance.py`, lecture **1–229/229** selon les quatre passages du protocole externe v2.0 §12. **Échelle :** intra-script avec interfaces immédiates au manifeste, au build, aux deux distributions et à `validate_all.py`. **Responsabilité pressentie :** vérifier l'inventaire déclaré, les liens Markdown relatifs et des conventions textuelles du package. **Risque dominant :** attribuer un PASS de package à une distribution qui contient des fichiers non déclarés, ou laisser contourner les conventions sans diagnostic. **Condition de sortie de ce bloc :** rapport sectionnel, tests discriminants, garanties conservées et prochaine cible explicite ; aucun verdict système ou patch.

Baseline B01 recalculée : compilation `Design_Governance_V1.0.md` SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole SHA-256 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`. Le script est incorporé à la compilation sous `## Fichier : scripts/validate_design_governance.py` ; sa reconstruction compte **229 lignes, 9 977 octets**, SHA-256 `8853fcd4300bdf0f45431deda538f053f48292064d1161e6518c8ab7b932bb4b`. La reconstruction de travail des 60 unités correspond aux tailles et lignes de l'inventaire B01 ; les contre-épreuves utilisent des copies temporaires de cette reconstruction. Les fichiers reçus restent intacts ; aucun dépôt Git authentifié ni run de workflow hébergé n'a été inspecté.

Entrées de continuité : plan maître actif (131 fiches provisoires avant ce bloc), `Audit_Validate_ALL_Phase2_01_Orchestration_Oracles_Build_Reprise.md`, checkpoint `Audit_Validate_RUN_CARD_Phase2_Checkpoint_Consolidation.md`, protocole §12. Le manifeste, le build et les textes normatifs ont été ouverts aux interfaces requises ici ; leur audit exhaustif reste prévu dans leurs unités propres.

## Passage A — architecture visible

| Lignes | Contrôle | Frontière de preuve |
|---|---|---|
| 1–27 | Détection GitHub/Local par présence de `official` et absence de `V1/official`, chargement du manifeste et de la liste du profil ; erreur de chargement captée. | Le manifeste est l'autorité déclarative des chemins attendus. Cette lecture ne prouve pas la provenance de la version ni la présence d'un workflow réellement exécuté. |
| 29–48 | Ensembles de valeurs `STATE`, `ISSUE`, `VERDICT`, `DIRECTION-STATUS`, collecte d'erreurs. | Ces ensembles servent au repérage textuel ; ils ne jugent pas une `RUN_CARD` réelle. |
| 51–70 | Existence des fichiers du manifeste et absence de fichiers supplémentaires, hors chemins contenant `dist`, `.build`, `__pycache__` et deux archives à la racine. | Le filtrage de dossiers générés s'applique à **n'importe quel segment** du chemin, y compris dans des sources copiées au build. |
| 73–93 | Extraction par regex des liens Markdown, confinement à la racine, existence du fichier, présence d'un fragment calculé depuis les titres. | Liens externes ignorés volontairement ; les ancres sont obtenues par `strip/lower/replace` et non par l'observation d'un navigateur. |
| 96–109 | ACTION doit mentionner l'exemple RUN_CARD canonique et éviter une projection YAML/JSON embarquée avec ouverture de bloc reconnaissable. | La détection de l'ouverture est sensible à la casse et aux étiquettes exactement `yaml`, `yml`, `json`. |
| 112–136 | Énumérations structurées en début de ligne et séparation de `STATE` et `HELD`. | Les enums ne sont recherchés que sous labels **majuscules exacts** ; le test spécial `state: HELD` accepte pourtant la casse variable. |
| 139–200 | Langage canonique, cycle de vie, lecture ACTION, mention expérimentale, autonomie Local. | Beaucoup de clauses sont des présences de chaînes exactes ; la sémantique et la cohérence des passages réclament la lecture des sources propriétaires. |
| 203–229 | Appels de tous les contrôles, erreurs accumulées, code 1 ou PASS profilé. | Une disparition de source lue plus tard peut provoquer une exception avant l'affichage des erreurs déjà collectées. |

## Passage B — contrat réellement exercé et contre-épreuves

Le package GitHub reconstruit rend **code 0, `VALIDATION PASSED — GitHub, 60 fichiers attendus`**. L'export Local issu du build rend **code 0, `VALIDATION PASSED — Local, 56 fichiers attendus`**. Retirer le workflow sans changer le manifeste rend code 1 avec « fichier attendu absent » ; ajouter `unlisted.txt` à la racine rend code 1 avec « fichier inattendu ». La présence d'un build manquant dans le package complet est ainsi bloquée par le manifeste avant que `validate_all.py` puisse annoncer un PASS Local, comme établi au bloc précédent.

Les mutations suivantes ont été isolées, exécutées, puis abandonnées avec leurs copies temporaires :

| Modification ciblée | Résultat | Portée |
|---|---|---|
| Ajouter `V1/official/.build/rogue.txt`, absent du manifeste. | Validateur documentaire **code 0** ; `build_distributions.sh` **code 0** et archive GitHub contenant `V1/official/.build/rogue.txt`. La suite entière `validate_all.py` retourne **code 0, `FULL VALIDATION PASSED`**, tandis que l'archive contient toujours le fichier. | F-VDG-001 : un fichier source non déclaré traverse le build en échappant à l'inventaire et aux contrôles de la distribution. |
| Ajouter à ACTION un bloc de projection dont l'ouverture porte l'étiquette `JSON`, contenant `{"run_card": {}}`. | **Code 0** ; le même bloc étiqueté `json` donne **code 1** avec « projection YAML/JSON embarquée ». | F-VDG-002 : l'interdiction documentaire est contournée par la casse de l'étiquette, sans changer la nature du bloc. |
| Ajouter `state: UNKNOWN` à ACTION ; voisin `STATE: UNKNOWN`. | Le premier donne **code 0**, le second **code 1** pour valeur non canonique. `state: HELD` en minuscules donne bien code 1 par l'autre contrôle. | F-VDG-003 : deux règles du même script interprètent différemment la casse du label `state`. Sa portée normative exacte sera recoupée avec ACTION. |
| Retirer `V1/official/README.md` sans modifier le manifeste. | **Code 1 avec `FileNotFoundError` et traceback**, sans bannière `VALIDATION FAILED` ni message déjà collecté « fichier attendu absent ». | F-VDG-004 : une entrée précisément couverte par l'inventaire sort du chemin de diagnostic gouverné. |
| Retirer le workflow et son entrée du manifeste. | Le **validateur documentaire seul** rend code 0 et annonce 59 attendus. | Limite d'autorité du manifeste, **pas un nouveau constat de PASS de la suite complète** : le build recopie explicitement le workflow et devra être audité comme propriétaire de cette interface. |

Pour F-VDG-001, la conclusion de faux `FULL VALIDATION PASSED` est une observation sur une **copie mutée**, non une propriété observée de la baseline intacte. Le code de build copie récursivement `V1`, puis zippe tous les fichiers de son stage ; les validations en stage réutilisent le filtre du validateur documentaire. La source compilée B01 elle-même passe sans fichier caché ajouté.

## Passage C — lecteurs et effets pratiques

**Mainteneur et release :** les refus d'absence et de fichier ordinaire supplémentaire protègent une partie réelle de l'inventaire. L'exception globale `any(part in generated …)` peut toutefois faire passer un contenu d'origine sous un nom réservé, puis le distribuer. Le nombre « 60 attendus » est la taille de la liste manifeste, pas une preuve que chaque fichier de l'archive est déclaré.

**Rédacteur d'ACTION et reviewer :** les règles de projection et d'état sont des garde-fous textuels. Un bloc `JSON` ou `state: UNKNOWN` peut contourner l'un de ces garde-fous sans que le script n'établisse la validité de la projection ou de la décision. Il faut vérifier la source propriétaire avant d'inférer une obligation de normaliser toute prose en majuscules.

**Intégrateur :** la CLI rend un diagnostic groupé pour certaines erreurs, mais la suppression d'une source officielle que le script lit ensuite produit un traceback brut. Un code non nul reste un échec réel ; son motif peut devenir invisible au lecteur et à un oracle qui attend une bannière.

## Passage D — constats provisoires, limites et suite

### F-VDG-001 — exclusion trop large de `.build` et fuite dans l'archive

**Mécanisme :** lignes 56–70 ignorent tout segment `.build`; le build copie récursivement les sources. **Preuve discriminante :** source supplémentaire non listée, validateur vert, build vert, archive GitHub contenant la source et `FULL VALIDATION PASSED` sur la copie mutée. **Owner pressenti :** frontière inventaire du validateur en interface avec l'inclusion du build et le manifeste. **Risque provisoire :** prioritaire pour une validation de release, gravité finale en phase 10. **Épreuve de résolution :** rejeter ou exclure explicitement un fichier source supplémentaire sous un dossier de nom réservé ; vérifier son absence de l'archive et préserver les vrais dossiers générés à la racine.

### F-VDG-002 — bloc JSON à étiquette majuscule non reconnu

**Mécanisme :** regex sensible à la casse, lignes 96–109. **Preuve :** voisin `json` rejeté, `JSON` accepté avec le même contenu et la même source ACTION. **Owner pressenti :** garde de projection canonique du validateur, avec ACTION propriétaire du contrat. **Épreuve de résolution :** les étiquettes de langage équivalentes doivent suivre la même décision, tout en maintenant l'exemple canonique et les blocs qui ne portent pas une seconde projection. Gravité finale ouverte.

### F-VDG-003 — valeur d'état non canonique masquée par un label minuscule

**Mécanisme :** regex des valeurs avec `STATE:` exact, lignes 112–127, alors que la séparation `HELD` emploie `re.I` aux lignes 130–136. **Preuve :** `state: UNKNOWN` accepté, `STATE: UNKNOWN` et `state: HELD` refusés. **Owner pressenti :** syntaxe documentaire côté ACTION puis contrôle textuel du script. **Réserve :** établir si une ligne `state:` minuscule est une représentation active de contrat ; si elle est explicitement hors scope, requalifier ce constat en observation au lieu d'ajouter une règle inutile. Gravité finale ouverte.

### F-VDG-004 — disparition d'un fichier requis suivie d'une exception brute

**Mécanisme :** `check_expected_files` cumule les erreurs, mais `check_canonicity_language` lit immédiatement `README.md` officiel aux lignes 139–145 sans condition ni gestion d'absence. **Preuve :** suppression isolée du README officiel → code 1 et traceback, sans erreurs accumulées affichées par `main`. **Owner pressenti :** orchestration et diagnostic du validateur documentaire. **Épreuve de résolution :** toute source requise absente doit donner code non nul avec son chemin et une sortie contrôlée, tout en préservant l'agrégation des autres erreurs et un package valide. Gravité finale ouverte.

**Non-fusions :** F-VDG-001 concerne l'inventaire réel et la distribution, F-VDG-002/003 des frontières textuelles distinctes, F-VDG-004 le diagnostic d'une absence. F-ALL-001/002 portent l'orchestrateur supérieur ; F-VRC-002/003/008 portent les erreurs du validateur RUN_CARD, non celles de ce script. L'essai de manifeste modifié montre une limite de preuve du validateur seul ; il ne démontre pas que le workflow peut manquer et obtenir un PASS complet, car cette hypothèse requiert aussi l'audit du build.

**Registre :** 131 fiches provisoires avant ce bloc ; F-VDG-001 à 004 portent le total à **135**. Aucun patch normatif, aucune fusion ou gravité finale, aucun verdict système. **Prochaine unité :** `validate_contracts.py` **1–218/218**, en recoupant schémas/exemples DOMAIN_FRAME, RESEARCH_BRIEF et production, faux positifs de chaînes et messages d'erreur ; ensuite `validate_reading_map.py`, `read_route.py`, manifeste, build et workflow selon les dépendances. Revérifier B01, relire §12 et le présent rapport avant ce bloc.
