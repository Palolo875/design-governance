# DG-AUDIT-001 — Phase 2 — Validateur RUN_CARD, plage 2/4 : contrat métier et mode strict

## Périmètre, reprise et baseline

Lecture intégrale A–D des **lignes 150–326/590** de `audit_work/package/scripts/validate_run_card.py` : `check_semantic_contract` (150–274) et `check_strict_contract` (276–325). Les lignes 1–149 sont couvertes par `Audit_Validate_RUN_CARD_Phase2_01_Chargement_Schema_Diagnostic_HELD.md` ; l'assemblage `validate_card` commence à 327 et sa lecture exhaustive suivra. Le protocole externe v2.0 §12, le checkpoint des 25 fixtures, le checkpoint du schéma/exemple RUN_CARD et le plan maître ont été repris. Interfaces propriétaires relues : ACTION/STATUS et RUN_CARD, DIRECTION pour le mode et les ancres, SAVOIR pour le profil. Les fixtures positives sont conservées comme contre-exemples aux corrections trop larges.

Baseline B01 stable : compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucun changement dans le package.

## Passage A — carte des décisions réellement encodées

| Lignes | Contrôle | Autorité et frontière |
|---|---|---|
| 151–166 | Ignore les racines hors objet jusqu'au schéma ; exige une `basis` non vide si des capacités sont `available`. | ACTION définit le profil comme avertisseur de capacité, non comme preuve exécutée (F-ACT-018). |
| 167–182 | Risque `critical` : objet `critical_protection`, cinq chaînes non vides, rejet de quelques placeholders exacts, `failure_action` parmi RETURNED/BLOCKED/ESCALATED. | Vérifie la déclaration, pas l'application de l'action après un échec ; F-ACT-017. |
| 183–232 | DIRECTION : thèse, anti-direction, premier objet, trace, statut en DECIDED/CLOSED, ancres structurées, règle ancre transformée/verdict, éventuel profil décidé, close créatif en CLOSED, champs et listes des ancres. | DIRECTION/SAVOIR possèdent la signification de l'ancre et du profil ; F-RC-001 porte l'interdiction excessive entre ancre transformée et retour/exploration. |
| 233–243 | Trace STANDARD/SYSTÈME ; rejet de l'acceptation avec LOST-IN-BUILD, BLOCKED ou FAIL-ASSUMED. | ACTION sépare état, issue, direction et verdict ; matrice restante F-ACT-010. |
| 244–274 | Répétition textuelle dans deux listes de preuve ; acceptation seulement après DECIDED/CLOSED, avec `observed`, provenance et limitation ; conséquence décisionnelle généralement exigée pour DIRECTION fermée. | ACTION possède adéquation et fraîcheur de la preuve ; F-ACT-009/012/013/022/034 restent ouverts. |
| 276–302 | Strict : parcours récursif contre huit chaînes placeholders exactes ; artefact non vide, trace requise pour tous les modes, hôtes de démonstration interdits pour **la trace**. | La trace LITE/ITER du mode strict diverge des règles de persistance du mode ordinaire : F-ACT-020/F-DIR-036. |
| 303–325 | Strict : existence d'un artefact commençant par `file://` ou ayant une syntaxe de chemin local ; les URI à schéma et les autres identifiants échappent à ce contrôle d'existence. | `source_path` est reçu par la fonction mais n'est jamais consulté pour résoudre un chemin relatif ; voir F-VRC-005. |

Le contrôle métier précède le schéma dans l'appel `validate_card` observé comme interface ; cette priorité explique des messages utiles pour les fixtures connues, mais elle crée aussi des erreurs brutes sur certaines entrées d'un mauvais type. Le mode strict complète le mode ordinaire, sans inspection de capture, de résultat de tâche, de contenu distant ou de version réellement observée.

## Passage B — contre-épreuves ciblées et garanties à préserver

Les essais ci-dessous utilisent des **copies JSON en mémoire** des trois positifs du dossier, soumises à `validate_card(document, schema)` et, selon le cas, `strict=True`. Les deux expériences de chemins utilisent un dossier temporaire externe au package ; aucune fixture ni source normative n'est modifiée.

| Variation minimale ou paire | Résultat vérifié | Portée et owner |
|---|---|---|
| `valid_closed_return.json` inchangé : risque critique et `CLOSED + RETURNED + RETURN` | PASS | Une clôture administrative ne force pas un verdict accepté. |
| Protection critique `null`, puis `control="todo"` | Deux REJECT ciblés | La structure et le placeholder exact sont protégés ; l'efficacité réelle du contrôle reste F-ACT-017. |
| `failure_action="RETURNED"` du cas valide et `closure.issue=null` | PASS | La consigne critique déclarée ne gouverne pas l'issue ; F-ACT-017 déjà propriétaire. |
| Même claim exact dans `observed` et `not_verified`, puis même texte changé seulement de casse | REJECT, puis PASS | L'anti-contradiction est littérale ; la liaison à l'axe et la preuve réelle restent F-ACT-012. |
| Acceptation DIRECTION en état CHECKING ; `profile_decision` sans `evidence` | Deux REJECT ciblés | Temporalité de l'acceptation et présence des quatre champs du profil fonctionnent. |
| DIRECTION fermée acceptée, `decision_change` supprimé, issue `RETURNED` | PASS | Issue et verdict peuvent entrer en tension et contourner la conséquence exigée ; F-ACT-010/013, déjà ouverts. |
| Risque critique avec mode LITE et trace retirée | PASS en normal | Ce résultat ne classe pas le mode légitime ; F-DIR-007/F-ACT-017. |
| LITE sans trace ; même document en strict | PASS normal ; REJECT strict | Divergence déjà documentée F-ACT-020/F-DIR-036. |
| Exploration DIRECTION avec ancre non transformée ; même ancre déclarée transformée | PASS, puis REJECT | Reproduit F-RC-001 : ne pas effacer la vérité de l'ancre pour passer. |

La vérification stricte d'une `trace_locator` URL sur `example.invalid` rejette bien l'hôte de démonstration. Un artefact local en chemin absolu existant passe le contrôle strict d'existence. Ces protections sont à conserver. Les locators textuels libres et les URL distantes ne sont pas derechef réinspectés comme artefacts ; un PASS strict n'est pas une preuve d'accessibilité du rendu.

## Passage C — lecteurs et déroulement en situation

L'agent qui construit une carte à risque critique peut fournir cinq chaînes cohérentes et obtenir une structure valide même si l'échec aurait dû retourner le run : le reviewer doit reprendre la trace, les tests et le comportement réel avant d'accepter. Le designer qui a transformé une ancre mais attend encore un test mobile ne doit pas réécrire cette transformation comme `unknown` pour sérialiser un retour : la règle actuelle l'y incite, déjà F-RC-001. Le mainteneur reçoit des diagnostics pertinents sur les exemples connus ; une entrée mal typée ou une URL mal formée peut cependant rompre le contrat de diagnostic au moment précis où la CLI doit expliquer le rejet. L'intégrateur qui active `--strict` attend une interprétation stable du fichier soumis, en particulier pour la provenance de l'artefact et la résolution des chemins locaux.

## Passage D — résistance et constats nouveaux

### F-VRC-003 — exceptions brutes pendant les contrôles métier et stricts

- **Épreuves :** dans `valid_closed_return.json`, mettre `proof.observed=[{"claim":"x"}]` produit `TypeError: unhashable type: 'dict'` à l'intersection des ensembles (246–251). Mettre `closure.issue=[]` ou `mode=[]` produit aussi `TypeError` à une appartenance dans un ensemble (241 et 233). En strict, `trace_locator="https://["` produit `ValueError: Invalid IPv6 URL` à `urlparse` (300). Les fichiers temporaires soumis à la CLI rendent code 1 avec traceback en sortie d'erreur et **sans** `RUN_CARD VALIDATION FAILED`.
- **Cause et effet :** les contrôles sémantiques précèdent la validation des types par le schéma, et l'analyse de l'URL n'encadre pas ses propres erreurs. Ce sont des **rejets incontrôlés**, pas des acceptations invalides ; un simple code non nul ne permet pas à l'automatisation de distinguer un document incorrect d'un crash de validation. La lecture des lignes 327–381 confirmera l'étendue du traitement d'exceptions en CLI.
- **Owner pressenti :** contrat d'entrée du validateur métier/strict et sortie contrôlée de la CLI. **Gravité provisoire significative** pour la fiabilité et le diagnostic sur des entrées soumises ; futur test de frontière : types illégaux pour `mode`, `issue`, `verdict`, tableaux de preuves non textuels et URL mal formée, tous rejetés proprement avant interprétation métier. Distinct de F-VRC-002 (échec de décodage UTF-8 avant parsing JSON).

### F-VRC-004 — URL de démonstration refusée pour la trace, acceptée pour l'artefact en mode strict

- **Épreuve :** remplacer `artifact.locator` du positif fermé/retourné par `https://example.invalid/artefact-demo` et fournir une trace URL non démonstrative : `strict=True` rend PASS. Mettre ensuite `trace_locator=https://example.invalid/trace-demo` rend REJECT « URL de démonstration interdite ». Le set `placeholder_hosts` est consulté uniquement sur `trace_locator` (301–302) ; `artifact.locator` à schéma URL saute le test d'existence (307–325).
- **Effet :** un chemin d'artefact explicitement démonstratif peut être présenté comme validé en strict alors que la trace identiquement démonstrative est refusée. Cela n'établit pas qu'une URL HTTP extérieure serait vérifiable en ligne ; la règle cohérente minimale peut porter sur les hôtes de démonstration et l'intention du profil strict.
- **Owner pressenti :** validation stricte des locators, en interface avec l'artefact ACTION et la preuve. **Gravité provisoire significative** pour le signal « strict » ; test futur sur trace et artefact pour les mêmes hôtes, sans réclamer par défaut que toute URL soit ouverte ou que tout ticket soit un fichier. Distinct de F-ACT-022 (fraîcheur/version de preuve). 

### F-VRC-005 — chemin d'artefact relatif évalué depuis le package, pas depuis la carte soumise

- **Épreuve :** créer dans un dossier temporaire externe une carte et son fichier voisin `artifact.png`. Avec `artifact.locator="./artifact.png"`, la validation stricte rejette « artefact local absent » bien que le voisin existe. Avec le **chemin absolu du même fichier**, elle passe. Les lignes 315–323 ancrent le relatif sur `ROOT` du package ; l'argument `source_path`, fourni à `check_strict_contract`, n'est pas utilisé.
- **Effet :** une carte portable dont le chemin d'artefact est relatif à son propre emplacement échoue selon l'emplacement d'installation du validateur. L'intention d'ancrage des locators doit être déclarée par le propriétaire avant correction : si les chemins doivent être relatifs au package, documenter cette règle et fournir une route de carte externe ; s'ils sont relatifs à la carte, utiliser son dossier. Dans les deux cas, l'ancrage utilisé doit être explicite et stable pour le lecteur.
- **Owner pressenti :** contrat de chemin de RUN_CARD et `check_strict_contract`. **Gravité provisoire significative** pour la portabilité des fichiers utilisateur ; rééprouver une carte externe, une carte dans le package, un chemin absolu et les locators `file://` pertinents. Distinct de F-ACT-020 (obligation de trace selon mode) et de F-VRC-004 (hôtes d'URL).

F-ACT-017/020/022, F-DIR-007/036, F-SAV-005 et F-RC-001 conservent leurs mécanismes propres ; les occurrences connues (contrôle critique déclaré, trace imposée au LITE strict, preuve non fraîche, profil déclaratif et ancre transformée exploratoire) ne reçoivent pas de nouvel ID. F-VRC-001/002 et F-FIX-001/002/003 restent ouverts. La sévérité et les éventuelles fusions seront examinées aux phases prévues ; aucune correction anticipée.

Le registre passe de **123 à 126 fiches provisoires** : 101 propriétaires + 16 façades/contrats antérieurs + F-RC-001 + 3 F-FIX + **5 F-VRC**. La suite intégrée actuelle passe sur ses exemples ; elle ne teste pas les trois contre-épreuves nouvelles. Aucun patch normatif et aucun verdict global.

**Prochaine unité : lignes 327–381/590.** Lire l'ordre d'assemblage `validate_card`, les oracles `check_fixture`, le contrôle d'autorité du schéma et la validation ciblée ; revisiter F-VRC-002/003 pour la gestion des exceptions, F-FIX-001/002/003 pour la couverture et les diagnostics, ainsi que les positifs. Puis lire 382–590, appels CLI et suite complète ; checkpoint intégral du script ensuite.
