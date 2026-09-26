# Quick Start — Design Governance V1

> **Ce guide aide à lire le système. Il n’ajoute aucune règle, route, gate, statut ou autorité. En cas de divergence, les cinq racines V1 font foi.**

## En une phrase

Utilisez V1 pour transformer un brief en décision de design vérifiable : choisissez le bon niveau de travail, chargez seulement les propriétaires nécessaires, construisez une preuve adaptée, puis fermez avec une limite honnête plutôt qu’un `PASS` supposé.

Dans une conversation, l’agent peut d’abord formuler une proposition de cadrage complète afin de rendre un brief vague discutable. Cette proposition ne remplace pas un run : elle doit nommer les hypothèses qui comptent et ne peut pas être présentée comme un artefact construit, une preuve obtenue ou une action réalisée. `EXPLORATORY` est un statut ACTION distinct, réservé à un rendu observable auquel manque encore une preuve requise. Ouvrez `START` dès qu’un build, une modification, une vérification, une action externe ou une décision persistante est engagé.

## Démarrer en trois décisions

Avant de choisir une couleur, une grille, une stack ou un composant, répondez : quelle décision doit changer ; quel risque coûte le plus cher si elle est mauvaise ; quelle preuve la moins coûteuse pourrait réellement la confirmer ou l’infirmer ? Si aucune décision ne change, ne démarrez pas un nouveau run : conservez l’existant ou documentez un `N/A-JUSTIFIED` dans la trace pertinente.

| Situation | Mode probable | Lire d’abord |
|---|---|---|
| Correction locale, contenu, contraste, bug ou petit ajustement | `LITE` ou `ITER` | `DIRECTION/START`, puis seulement le propriétaire concerné. |
| Nouvelle page ou décision de produit limitée | `STANDARD` | `DIRECTION/START`, `ACTION/RUN-STANDARD`, puis `SAVOIR` ou `BIBLIOTHEQUE` selon le risque. |
| Nouvelle direction, surface identitaire ou enjeu craft dominant | `DIRECTION` | `DIRECTION`, `ACTION`, `SAVOIR/CRAFT`, et `BIBLIOTHEQUE` si une relation spatiale change. |
| Pattern partagé, tokens, composants ou changement avec blast radius | `SYSTÈME` | `DIRECTION/START`, `ACTION`, `BIBLIOTHEQUE/COMPONENTS`, puis l’owner de système. |

Le mode est une hypothèse de travail, non un moyen de réduire le contrôle. Si une nouvelle information augmente le risque, reclassifiez le run plutôt que de conserver un mode confortable.

## Lire juste assez

| Besoin | Source à charger | Ce qu’elle décide |
|---|---|---|
| Mode, absolus, hypothèses et direction visuelle | `DIRECTION.md` | Le niveau de travail, la cible et les contraintes qui ne doivent pas être perdues. |
| Trace, preuve, gates, verdict et clôture | `ACTION.md` | Ce qui doit être observé, comment le statut est établi et comment la trace persiste. |
| Craft, contenu, style, contexte, source et intégrité | `SAVOIR.md` | Le jugement : ce qui est juste, risqué, trompeur ou hors de portée. |
| Support, grille, scène, objet, micro-interface et contrat | `BIBLIOTHEQUE.md` | La responsabilité spatiale et structurelle de la surface. |
| Version active, statut de package et changement futur | `CHANGELOG.md` | L’état officiel du système et la manière de le faire évoluer. |

Ne chargez pas la bibliothèque entière si aucune structure ne change. Ne chargez pas le craft complet pour corriger une erreur technique isolée. À l’inverse, une surface identitaire ne doit pas être réduite à une check-list technique parce que sa direction demande davantage de jugement.

## Garder la rigueur hors de l’interface

Pour une tâche locale et réversible, montrez directement la réponse ou le diff ; ne demandez pas à la personne de choisir un mode. Pour un brief vague, montrez une proposition de cadrage avant de demander une décision. Pour une conséquence externe, montrez l’effet, le périmètre et la confirmation nécessaire. `MODE`, `RUN_CARD`, `BASIS`, `V/U/A/T` et `TRACE-LOCATOR` servent à l’atelier de l’agent ; ils ne deviennent visibles que lorsqu’ils expliquent une limite, un compromis ou une action à conséquence.

## Un run compact

Dès qu’un build, une vérification ou un changement d’état commence, créez la ligne de run minimale : `ID`, `MODE`, décision, risque et prochaine preuve. Pour un run persistant, ajoutez la `RUN_CARD` complète d’ACTION : owner, date/version, état, issue, verdict, artefact et `TRACE-LOCATOR`. Quand une preuve est produite, conservez son scope et sa limite. Si l’artefact change substantiellement sur l’axe vérifié, la preuve de cet axe redevient `NOT-VERIFIED` jusqu’à réinspection.

Avant une conclusion dépendant d’un outil ou d’un environnement, notez le `CAPABILITY-PROFILE` utile : navigateur/capture, DOM/CSS, contraste calculé, clavier/AT, participant/tâche, runtime/données. Chaque capacité est `disponible`, `indisponible` ou `non requise`. Toute capacité soutenant un claim indique aussi sa `BASIS` : résultat d’outil, environnement attesté, source utilisateur ou déclaration non attestée. Une capacité absente ne rend pas le run invalide ; elle interdit seulement le claim correspondant.

Pour un handoff ou une première passe, préparez une `EXECUTION-SNAPSHOT` dérivée d’ACTION : `MODE`, `DECISION/RISK`, `SOURCES`, `CAPABILITIES`, `CAPABILITY-BASIS`, `FACTS`, `AXES V/U/A/T`, `LIMIT`, `TRACE-LOCATOR` et `NEXT-PROOF`. Elle sert à charger juste assez de contexte. Elle expire si le mode, le risque, la capacité ou l’artefact change, et ne remplace jamais les sections sources.

| Terme exact | Usage court |
|---|---|
| `MODE` | Une seule valeur : `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. |
| `V / U / A / T` | Portées distinctes : perceptible, usage, accessibilité, technique. Elles ne se compensent pas. |
| `NOT-VERIFIED` | La vérification nécessaire n’existe pas encore dans le scope déclaré. |
| `RETURN` | Une preuve mesurée ou une condition applicable échoue ; correction et nouvelle preuve requises. |

> **Exemple LITE.** Le brief fournit un ratio de contraste insuffisant. La snapshot déclare `MODE: LITE`, `A: RETURN`, `V/U/T: NOT-VERIFIED`, `CAPABILITY: ratio fourni; navigateur et AT indisponibles`, puis demande un diff, un nouveau calcul et une capture comme `NEXT-PROOF`. Elle ne prétend ni avoir vu le rendu, ni avoir testé le clavier ou un lecteur d’écran.

Pour une surface `DIRECTION` où le craft domine, faites l’opération B1b : retirez, réduisez ou transformez une décision principale ; comparez ; puis dites ce que cette opération a réellement changé. Pour une revue qualifiée d’indépendante ou aveugle, conservez l’exposition du reviewer et le moment de divulgation du mapping. Une revue non aveugle est utile, mais elle ne doit pas être présentée comme une passe aveugle.

## Fermer correctement

Un run ferme lorsque la décision a une conséquence observée, que les preuves applicables sont rattachées à l’artefact livré et que ses limites sont explicites. Une capture ne démontre pas une tâche utilisateur. Un build ne démontre pas un lecteur d’écran. Un avis expert ne devient pas une vérité universelle. Si une information nécessaire manque, utilisez le statut approprié — réserve, retour, exploration ou `NOT-VERIFIED` — au lieu de compenser par une moyenne ou une formulation rassurante.

## Ce que V1 ne fait pas

V1 ne choisit pas une esthétique, une bibliothèque frontend, une police, une palette ou une animation par défaut. Il ne remplace pas l’observation d’utilisateurs, la responsabilité d’une équipe, une validation juridique ou la connaissance d’une population concernée. Toute aide contextuelle reste subordonnée aux cinq sources actives et ne les remplace jamais.
