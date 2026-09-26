# DG-AUDIT-001 — Phase 2 — ACTION, bloc 12

## Périmètre et continuité

- Cible : `V1/official/ACTION.md`, lignes 870–935 de la reconstruction B01 ; dernier bloc de lecture linéaire d’ACTION.
- Sections : `ACTION/ROUTING` (870–887), `ACTION/MAINTENANCE` (891–912), `ACTION/CLOSE-EXIT-CHECK` (915–930) et mesure expérimentale (932–934).
- Interfaces : `DIRECTION/START`, `SAVOIR/ROUTING` et ses routes, `BIBLIOTHEQUE/SELECT` et `/COMPONENTS`, `ACTION/RUN-SYSTEM`, `READING_MAP`, `CHANGELOG`, schéma, exemple, validateur `RUN_CARD` et suite officielle.
- Méthode : quatre passages du §12 du protocole, confrontation aux onze premiers rapports ACTION et au checkpoint DIRECTION ; inspection de la source exacte et tests ciblés sans modification du corpus.
- Baseline système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`. Ces deux empreintes correspondent à B01.
- État : diagnostic **sectionnel provisoire** ; F-DIR-001 à 046 et F-ACT-001 à 039 repris, sans verdict global, sans nouvel ID ni patch. Le checkpoint ACTION est l’unité suivante.

## Synthèse du bloc

La fin d’ACTION maintient trois protections utiles. Le jugement spécialisé se charge selon la décision active ; une modification documentaire substantielle exige une recette, un owner et un essai en run réel avant adoption élargie ; la clôture vérifie à la fois l’artefact, la preuve, le risque restant et la prochaine action. La mesure pilote porte sur l’efficacité de la méthode en série et ne transforme ni le goût ni le nombre d’itérations en score individuel.

La frontière fragile est la mise en œuvre de ces protections. Le tableau normatif cite des sections SAVOIR qui existent dans leur propriétaire, mais que le lecteur livré ne charge pas par leur locator ; la suite officielle reste verte. Le test de sortie est accessible et compréhensible pour un reviewer humain, mais sa projection structurée n’impose pas plusieurs réponses décisives : risque dominant/protection, axes V/U/A/T, prochaine action, cycle de réserve, preuve du premier rendu et effet réel de la dernière modification. Il s’agit d’occurrences et de recoupements de constats déjà établis, pas d’une nouvelle famille de défauts.

## Passage A — architecture visible et routes

| Segment | Propriété et rôle | Charge ou sortie | Limite testée |
|---|---|---|---|
| 870–887 | ACTION oriente vers les propriétaires de jugement SAVOIR et de structure BIBLIOTHEQUE après classification DIRECTION | Routes conditionnelles selon spec, états, contraste, risque, technique, claims, intégrité, famille et blast radius | Une majorité des locators SAVOIR cités ne figure pas dans la table exécutable |
| 891–912 | ACTION prescrit la recette documentaire avant adoption | Onze contrôles, automation partielle, jugement humain sur intention/risque et risque explicite si contradiction non résolue | Le PASS du package ne certifie pas ces onze conditions ni l’essai réel |
| 915–930 | ACTION possède le test canonique de fin de run | Dix questions et statut honnête lorsque réponse inconnue | Une carte valide ne prouve pas que les dix questions ont reçu réponse |
| 932–934 | ACTION propose des observations pour pilotes ou séries | Vitesse, premier rendu, corrections utiles, preuves absentes, défauts et regards situés | Aucun protocole comparatif ni données observées dans ce passage ; proposition à éprouver, pas résultat |

Comparaison locale du tableau de routing avec `READING_MAP` et `read_route.py` : `ACTION/ROUTING`, `ACTION/CLOSE-EXIT-CHECK`, `SAVOIR/CRAFT`, `BIBLIOTHEQUE/SELECT`, `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` sont résolus ; `ACTION/MAINTENANCE`, `SAVOIR/TYPE`, `/SOURCE`, `/STYLE`, `/STATE`, `/SYSTEM`, `/CONTEXT`, `/TECH`, `/TOOLS` et `/INTEGRITY` ne le sont pas. Les dix sections non résolues possèdent néanmoins un titre dans leurs fichiers propriétaires : la recherche humaine par fichier puis titre, prévue par `READING_MAP`, demeure possible. `ACTION/RUN-SYSTEM` est bien accessible ; son titre utilise des backticks, qu’une recherche naïve par préfixe de titre manquerait. Ce constat étend F-ACT-001 et F-DIR-028 sans confondre absence de clé CLI et absence de contenu.

Le routing de ce bloc ne reclassifie pas lui-même la tâche. La section d’adoption appartient à ACTION pour la recette et à CHANGELOG pour la décision de cycle de vie et le statut de route ; la sélection structurelle demeure à BIBLIOTHEQUE. Les anciens aliases `REFERENCES/*` sont publiquement migrés dans CHANGELOG et restent exclus des nouveaux runs.

## Passage B — contrat sémantique phrase et section par section

### `ACTION/ROUTING`

La première phrase réserve à DIRECTION la classification et à ACTION la sélection des prérequis qui **peuvent modifier la prochaine décision**. Le tableau donne un déclencheur situé plutôt qu’une obligation universelle. `SAVOIR/ROUTING` précise en plus qu’une route peut modifier la preuve, la limite ou le statut ; une lecture littérale étroite d’ACTION risque d’omettre une route après que l’artefact est fixé mais avant qu’un claim soit tranché. Cette nuance prolonge F-ACT-004 ; elle ne prouve pas qu’il faut charger toute la bibliothèque.

Les lignes sur contraste et risque critique doivent se lire conjointement : `SAVOIR/CRAFT` et `/SYSTEM` guident la construction ; `SAVOIR/CONTEXT` et ACTION/GATE-A restent pertinents dès que l’accessibilité ou le risque l’exige. Le tableau ne dispense pas les contrôles du gate. Les claims datés requièrent source, date, portée et limite, et la maintenance ajoute la prochaine preuve lorsque le run en dépend : F-ACT-022/028 portent déjà la question de leur fraîcheur et de leur transport. Le renvoi `DESIGN-ATLAS` reste conditionné à une modification possible de la décision ; il n’institue pas une recherche exhaustive.

### `ACTION/MAINTENANCE`

« Tout cycle qui modifie ACTION ou un contrat connexe » déclenche une recette **avant adoption**. Les onze lignes du tableau couvrent, dans l’ordre, existence/portée, vocabulaires canoniques, scope, exemples, claims, route principale/miroirs, quotas artificiels, contournement théâtral, essai réel si changement substantiel, ownership et cycle des réserves. La phrase suivante borne l’automatisation : liens, routes et statuts peuvent être testés mécaniquement ; intention, scope, proportionnalité et jugement de risque demandent une revue humaine. Une contradiction non résolue devient un risque explicite, sans règle concurrente silencieuse.

Ce contrat n’affirme pas que `validate_all.py` couvre ces onze contrôles. Sa réussite actuelle atteste le package, les fixtures, le build et sa reproductibilité. CHANGELOG déclare expressément l’efficacité sur runs réels et l’adoption `NOT-VERIFIED`. Il faut donc conserver cette distinction lors de toute future adoption : une modification substantielle demandera une démonstration située et une décision de propriétaire en plus de la validation de package. La recette est générale ; la carte de run n’est pas nécessairement le registre unique d’adoption, mais la trace doit rester retrouvable.

### `ACTION/CLOSE-EXIT-CHECK`

Les questions 1–2 relient mode, risque, artefact et décision. Les questions 3–4 demandent preuve adaptée ou absence déclarée, puis scope et limite lorsque nécessaires. La question 5 exige les axes touchés et le risque restant ; la 6 sépare statut de direction, verdict global, owner et action suivante. La 7 décrit une réserve avec son cycle complet ; la 8 demande la conséquence réelle de la procédure ; la 9 exige l’objectif et un indice observable de qualité **au premier rendu** ; la 10 vérifie que la dernière modification a affecté autre chose que son récit. La phrase finale interdit le PASS implicite et toute compensation entre dossier rempli, faiblesse de l’objet et preuve manquante.

La question 8 doit être lue avec PRECONDITION 206–218 : une décision **confirmée** ou **abandonnée** est aussi un résultat utile, et l’absence d’un changement peut être justifiée `N/A-JUSTIFIED` lorsque le one-shot était déjà suffisant. Exiger une modification de l’artefact pour satisfaire la question 8 serait un contournement théâtral, lié à F-DIR-009 et F-ACT-013/025. À l’inverse, écrire « aucune » sans raison ni conséquence n’est pas une preuve. Les questions 9–10 renforcent la distinction entre l’objet initial, sa version finale et un simple embellissement du compte rendu ; elles ne prescrivent pas une itération obligatoire.

L’expression « utilise le statut approprié » est un garde-fou humain, pas une matrice machine des réponses inconnues. Elle appelle selon le cas `NOT-VERIFIED`, retour, exploration, blocage ou escalade dans le registre adéquat. La compatibilité exacte entre issue, axes, direction et verdict reste ouverte (F-ACT-003/010/012/021), y compris pour la diffusion limitée sous F-ACT-039.

### Mesure expérimentale

Le niveau de mesure est le pilote ou la série de runs. Le temps jusqu’au premier rendu jugeable, la part de corrections structurelles, la part de corrections matérielles, les preuves encore non vérifiées et les défauts par mode pourraient révéler coût et qualité du processus. Les regards situés complètent les métriques sans faire passer le goût pour une loi. Avant d’inférer une amélioration, un futur pilote devra rendre comparables le point de départ, le mode, le scope, les dénominateurs, les versions du premier rendu et du rendu corrigé et la composition des évaluateurs. Le texte actuel n’avance ni valeur chiffrée ni résultat ; c’est une **question d’instrumentation pour phases 8/9 et pilotes**, sans constat autonome en phase 2.

## Passage C — usages réels sous contrainte de temps

1. Un agent reçoit un changement de contraste et charge `ACTION/ROUTING`. Il lit correctement le besoin de craft/système, mais `SAVOIR/SYSTEM` échoue dans la CLI ; il doit ouvrir `SAVOIR.md` et retrouver son titre. Le gate applicable reste à consulter selon le risque.
2. Un designer a achevé l’artefact mais doit qualifier une claim de performance ou de conformité. La question ne modifie plus l’artefact ; elle modifie cependant méthode, preuve, limite ou verdict. La route SAVOIR ciblée reste utile, même si la formule d’entrée ACTION se lit plus étroitement.
3. Un mainteneur corrige un contrat partagé. Il peut exécuter la suite officielle et vérifier les renvois, puis demande à un reviewer humain la portée, les échappatoires et la proportionnalité ; si changement substantiel, il documente un run réel avant adoption élargie et nomme owner/revue. La réussite actuelle de la suite ne remplace aucune de ces étapes.
4. Un reviewer d’un run STANDARD accepté lit `CLOSE-EXIT-CHECK`. Il doit revenir à la trace pour vérifier axes, réserve, prochain geste et premier rendu ; la carte JSON seule peut rester valide sans ces réponses.
5. Une équipe conserve un excellent premier rendu sans correction utile. Elle vérifie les preuves requises, puis justifie l’absence de modification ; la mesure pilote compte ce cas sans le punir ni exiger une variante.
6. Un intégrateur agrège des cartes acceptées : la valeur `CLOSED` et un texte `limitations` ne distinguent pas à eux seuls réserve assignée, preuve manquante admissible ou claim périmé. Il doit interroger la trace et le propriétaire avant de prendre une décision de livraison.

## Passage D — résistance, contre-exemples et rattachement

Une mutation isolée de l’exemple `RUN_CARD` en mode STANDARD a été clôturée avec `ACCEPTED-WITH-RESERVATION`, une observation limitée à une capture desktop nominale, des états mobiles/clavier/contraste/performance/premier rendu déclarés non vérifiés, une limitation vague, sans `decision_change`, `next_action` ni cycle de réserve. `validate_card` l’accepte. Des ajouts structurés `next_action`, `reservations` et `first_render` sont rejetés individuellement comme champs inconnus. La carte peut néanmoins pointer vers une trace externe complète ; l’essai établit **la non-opposabilité de ces réponses dans la projection**, pas que tout run réel qui utilise cette projection est nécessairement dépourvu de trace.

La suite officielle `python3 scripts/validate_all.py` se termine par `FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité` tout en laissant les dix locators du tableau de routing hors de la table de `read_route.py`. Les contrôles automatiques vérifient leurs fixtures et les locators principaux enregistrés, sans vérifier que chaque appel normatif est chargé par la CLI. Ceci confirme F-ACT-001, F-ACT-008 et F-DIR-028 ; le PASS n’est pas une preuve de recette humaine, de run réel ou de conformité du test de sortie.

| Question de résistance | Observation | Registre existant |
|---|---|---|
| Locator normatif de maintenance ou SAVOIR chargé tel quel | Rejet CLI, titre présent pour recherche humaine | F-ACT-001 ; F-DIR-028 |
| Route spécialisée utile à la preuve après build | Déclencheur « prochaine décision » plus étroit selon lecture littérale | F-ACT-004 ; F-DIR-030 |
| Risque/axes inconnus mais carte acceptée | Ni axes V/U/A/T ni dominance du risque ne gouvernent toute acceptation | F-ACT-010, 012, 017, 021 |
| Réserve acceptée sans cycle nominatif | `limitations` et owner racine ne suffisent pas à rendre chaque réserve suivable | F-ACT-023 |
| Prochaine action et conséquence de run absentes | `next_proof` n’est pas `next_action` ; `decision_change` facultatif hors DIRECTION accepté | F-ACT-002, 013, 021 |
| Premier rendu et dernier delta sans version/relation | Une capture finale nominale ne démontre ni objectif initial ni correction réelle | F-ACT-022, 025, 030 et F-DIR-009 |
| Essai réel d’une modification substantielle | Exigé par la prose avant adoption élargie ; pas certifié par `validate_all` | F-ACT-008 ; frontière de validation déclarée dans CHANGELOG |

**Nouveaux constats : aucun.** Les contre-exemples sont spécifiques à cette section, mais leurs causes et leurs risques ont déjà une fiche ouverte. Cette absence de nouvel ID ne vaut ni validation du système ni réduction automatique de la gravité provisoire.

## Protections positives à conserver

1. Une seule classification DIRECTION, puis des routes de jugement/structure activées par une question réelle.
2. Une route principale et des miroirs dérivés, sans chargement total de SAVOIR ou catalogue de formes automatique.
3. Les claims datés accompagnés de source, date, portée et limite lorsqu’ils affectent le run.
4. Une recette avant adoption, avec contrôles automatiques bornés et revue humaine sur l’intention et le risque.
5. Un run réel pour toute modification substantielle avant adoption élargie ; l’absence actuelle de ce type de preuve reste déclarée.
6. Une contradiction persistante visible comme risque et non comme règle concurrente implicite.
7. Un test de sortie commun, qui relie décision, objet, preuve, axes, ownership et reprise, sans substituer la trace à la qualité.
8. Une confirmation ou un one-shot bien justifié recevables sans créer une correction artificielle.
9. La preuve du premier rendu et l’effet de la dernière modification comme questions, pas quota d’itérations.
10. Des observations de pilotes et des regards situés, sans score individuel ni verdict esthétique automatique.

## Couverture et passage

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL ciblé | Trois locators ACTION, tableau des routes et propriétaires comparés ; 10 clés non chargées mais titres présents |
| B — Sémantique | FULL | Déclencheurs, onze contrôles de recette, dix questions de sortie et six familles de mesure lus |
| C — Usage | TARGETED | Six simulations agent, designer, mainteneur, reviewer, équipe et intégrateur |
| D — Résistance | FULL ciblé | Mutation STANDARD, trois champs rejetés, recoupement de la suite officielle et des fiches existantes |
| Machine | FULL ciblé | Schéma, exemple, `validate_card`, lecture de routes et `validate_all.py` inspectés/exécutés |
| Sources externes | N/A-JUSTIFIED | Aucune affirmation nouvelle sur un standard externe dans ce bloc |

La lecture des lignes 1–935 d’ACTION est achevée par ses douze rapports sectionnels. **ACTION n’est pas encore consolidé** : le prochain pas du protocole est un checkpoint propriétaire qui vérifiera couverture exacte, séquence F-ACT-001 à 039, dédoublonnage, dépendances amont/aval, protections positives, gravités toujours provisoires et point de reprise avant de passer à `SAVOIR.md`. Aucun correctif système n’est appliqué à cette étape.
