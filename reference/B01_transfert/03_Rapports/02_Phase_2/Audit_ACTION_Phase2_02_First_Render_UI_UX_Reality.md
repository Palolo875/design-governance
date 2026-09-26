# DG-AUDIT-001 — Phase 2 — ACTION, bloc 2

## Périmètre examiné

- Cible : `V1/official/ACTION.md`
- Bloc : lignes 79–112 de la reconstruction de travail
- Sections : `ACTION/FIRST-RENDER`, qualité initiale par mode, statut exploratoire, `ACTION/UI-UX-REALITY`, contrat de production et règle de classification lorsque la capacité manque
- Interfaces vérifiées : bloc ACTION 1, `DIRECTION/START`, `DIRECTION/FIRST-OBJECT`, boucle one-shot, `ACTION/STATUS`, `ACTION/PRECONDITION`, routes STANDARD/DIRECTION/SYSTÈME, `SAVOIR/CONTEXT`, `SAVOIR/TECH`, READING_MAP, QUICKSTART, schéma et validateur des contrats de production
- Source d’observation : compilation `Design_Governance_V1.0.md`, reconstruction de travail et baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des propriétaires, simulation de lecteurs, résolution des routes, inspection du contrat machine UI/UX et mutations négatives ciblées
- Statut : diagnostic sectionnel provisoire ; aucun verdict global sur ACTION et aucun patch du corpus

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. Le protocole, le plan maître et le rapport ACTION bloc 1 ont été relus. Les constats transportés en priorité sont F-ACT-001 à F-ACT-003 et F-DIR-004, F-DIR-009, F-DIR-018, F-DIR-019, F-DIR-024, F-DIR-028, F-DIR-030, F-DIR-035, F-DIR-037 et F-DIR-038.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 79–81 | Fixer une barre positive de qualité initiale | Refuse le wireframe creux ; cible située, proportionnée au mode et au risque ; qualité avant anti-slop | La barre doit rester une cible de construction, pas une prétention de réussite |
| 83–89 | Traduire la qualité initiale dans les cinq modes | LITE protège le delta ; ITER la fidélité ; STANDARD la composition ; DIRECTION la présence ; SYSTÈME les usages réels | Les modes non visuels doivent rester couverts par la condition d’applicabilité de la ligne 81 |
| 91 | Séparer qualité initiale et preuve | `EXPLORATORY` n’autorise pas un artefact volontairement faible ; qualité ≠ score ≠ verdict | Le mot « statut » ne précise pas s’il s’agit de l’issue ou du verdict global `EXPLORATORY` |
| 93–95 | Construire l’interface avec la tâche et les états réels | Tâche, feedback, états critiques, contenu extrême, responsive, focus et récupération deviennent observables | Les items « lorsque pertinents » restent proportionnés dans la prose, mais pas dans la projection machine associée |
| 97–108 | Relier décisions de construction et couverture | Huit dimensions compactes couvrent contenu, tâche, geste, états, responsive, accessibilité, robustesse et scope | `PROOF-SCOPE` est décrit comme effectivement observé alors que la phrase suivante parle de couverture attendue |
| 110–112 | Maintenir ownership, chargement conditionnel et classification | ACTION garde preuve/limite/verdict ; capacité manquante → `NOT-VERIFIED` ; mode inchangé sans reclassification silencieuse | Le déclencheur SAVOIR est réduit au prochain artefact, pas à la preuve, la limite ou la prochaine action ; les routes appelées ne sont pas résolubles |

## Passage A — architecture visible

Le bloc prolonge correctement le parcours minimal du bloc 1. Il définit d’abord le niveau de qualité du premier artefact, puis le rend concret pour une interface : contenu, tâche, premier geste, feedback, états, responsive, accessibilité, robustesse et scope de preuve. Cette architecture évite de séparer artificiellement « beau rendu » et « produit habitable ».

`ACTION/FIRST-RENDER` et `ACTION/UI-UX-REALITY` sont tous deux présents dans READING_MAP et résolus par `read_route.py`. Ce point est important : contrairement à plusieurs sections du bloc 1, les deux entrées principales de ce bloc sont directement activables.

Les dépendances conditionnelles ne le sont pas. La ligne 110 appelle `SAVOIR/CONTEXT` et `SAVOIR/TECH`, mais le lecteur officiel rejette ces deux locators alors que les sections existent dans SAVOIR. Un lecteur humain peut ouvrir SAVOIR et rechercher les titres ; un lecteur conditionnel outillé ne peut pas exécuter la route telle qu’elle est écrite. Cette occurrence étend F-DIR-028 et F-ACT-001 sans créer un nouvel ID par locator.

La structure machine associée est moins proportionnée que la façade humaine. `production_contracts.schema.json` regroupe obligatoirement trois objets — direction créative, réalité UI/UX et cas d’évaluation — et rend obligatoires toutes les matrices du paquet UI/UX. L’architecture documentaire dit pourtant que le contrat n’est pas un formulaire universel et que les états sont activés selon le mode et le risque. Cette divergence reçoit un constat propre, mais sa disposition finale attendra l’audit complet des schémas et scripts.

## Passage B — contrat sémantique

### Qualité initiale positive

Le contrat principal est fort : le premier artefact doit déjà être composé, crédible, spécifique au produit et suffisamment résolu pour être jugé comme un objet réel. La qualité n’est pas définie uniquement par absence de slop ; elle comprend présence, hiérarchie, typographie, contenu, états, matière ou retenue, relation à la preuve et finition pertinente.

La formule « dans la proportion du mode et du risque » protège contre une interprétation maximaliste. Un delta LITE n’a pas à devenir une refonte complète ; il doit être propre, lisible et non régressif. Un composant SYSTÈME n’a pas à devenir une scène de marque ; il doit être montré dans ses usages réels avec baseline, états, consumers et risque de régression.

Cette table est compatible avec une phase d’exploration en amont : elle s’applique lorsqu’un run produit une surface, un composant, un flow ou une scène comme premier artefact jugeable. Elle ne dit pas qu’aucune esquisse, hypothèse ou recherche ne peut précéder cet artefact. La distinction devra rester visible afin qu’« exiger un premier rendu fort » ne devienne pas « interdire toute exploration préparatoire ».

La ligne 91 protège une frontière essentielle : un rendu peut rester `EXPLORATORY` faute de preuve, mais il ne doit pas être volontairement creux lorsque les capacités de construction sont disponibles. Elle sépare donc :

- qualité intrinsèque visée ;
- qualité du rendu effectivement observable ;
- qualité ou résultat prouvé par une méthode adaptée.

SAVOIR formule explicitement ces trois niveaux. ACTION reste cohérent avec cette séparation en précisant que la qualité initiale n’est ni score ni verdict esthétique.

Le seul point ouvert est lexical : `EXPLORATORY` existe ensuite comme issue et comme verdict global. « Ce statut » ne dit pas quel registre est visé. Le bloc STATUS doit être lu intégralement avant de décider si cette occurrence exige un constat ACTION autonome ; à ce stade elle met à jour F-DIR-035.

### Qualité par mode

Les cinq formulations produisent des critères observables sans imposer un style :

- LITE : intégrité locale et absence de régression ;
- ITER : intention visible et fidélité à une direction retrouvable ;
- STANDARD : composition, contenu crédible, hiérarchie, typographie, états et responsive ;
- DIRECTION : présence, point de vue, composition, matière, objet de preuve et intégration d’asset ;
- SYSTÈME : usages réels, baseline, états, consumers et risque de régression.

La table résout une partie de F-DIR-037 : la capacité positive ne se limite plus à produire du style ; elle couvre construction, usage et robustesse selon le mode. Elle réduit aussi F-DIR-018 en rendant tâche, contenu, états et usages réels constitutifs du premier objet, plutôt que secondaires derrière une scène décorative.

### Construire l’interface et la tâche ensemble

Le contrat UI/UX est l’un des passages les plus solides du corpus lu jusqu’ici. Il refuse l’état nominal comme preuve suffisante lorsque la décision concerne erreur, permission, récupération ou tâche. Il exige un contenu assez réel pour révéler les problèmes de hiérarchie, de longueur et de localisation. Le responsive est décrit comme recomposition, non comme réduction géométrique. Focus, feedback, récupération et succès partiel sont intégrés à l’objet produit.

Le qualificatif « dans la proportion du mode et du risque » et la mention « lorsque pertinents » empêchent théoriquement une checklist universelle. Le contrat ne demande pas de fabriquer tous les états pour chaque micro-delta ; il demande de rendre observables ceux qui peuvent modifier la décision ou la protection.

### Les huit lignes du contrat de production

Les huit lignes couvrent deux temporalités différentes.

Avant ou pendant le build :

```text
CONTENT-MODEL
PRIMARY-TASK
FIRST-GESTURE
CRITICAL-STATES
RESPONSIVE-RELATION
ACCESSIBILITY-BASIS
ROBUSTNESS-BASIS
```

Elles décrivent ce qui doit être construit, protégé ou rendu observable.

Après observation :

```text
PROOF-SCOPE — surface, état, viewport, données, population ou runtime réellement observé
```

La ligne 110 affirme pourtant que l’ensemble décrit « les décisions de construction et la couverture attendue ». Une couverture attendue et un scope réellement observé ne sont pas la même information. Avant le build, le champ ne peut être qu’un `EXPECTED-PROOF-SCOPE`; après observation, il peut devenir un scope observé. Sans transition explicite, un lecteur peut préremplir une intention comme observation, ou écraser l’intention initiale et perdre l’écart de couverture.

Ce problème peut être résolu sans créer nécessairement deux formulaires : une trace vivante peut conserver cible puis observation, à condition que les états ou les champs soient distincts et que l’historique soit inspectable. Le contrat actuel ne l’explicite pas.

### Chargement conditionnel de SAVOIR

La ligne 110 charge CONTEXT et TECH seulement lorsque leurs questions peuvent modifier « le prochain artefact ». Cette condition est plus étroite que la règle du bloc 1, qui autorise un chargement lorsqu’il peut modifier mode, risque, route, preuve, limite, owner ou prochaine action.

Or CONTEXT et TECH peuvent être nécessaires sans changer l’artefact :

- choisir la méthode de vérification adaptée au médium ;
- identifier un référentiel de conformité ;
- reconnaître qu’un runtime ou une population n’a pas été observé ;
- établir une limite ou un fallback ;
- décider que le résultat doit rester `NOT-VERIFIED` ;
- définir `NEXT-PROOF`.

Le filtre « prochain artefact » peut donc supprimer exactement la lecture qui protège l’honnêteté de la preuve. La règle correcte du système semble être : charger la source si elle peut modifier la décision, la construction, la preuve, la limite ou la prochaine action — pas uniquement le rendu suivant.

### Capacité manquante et classification

La fin du bloc est robuste. Une capacité, un outil ou une preuve manquante ne reclassifie pas silencieusement la tâche. ACTION conserve le mode classé par DIRECTION, déclare la limite, le statut et la prochaine preuve. Cette règle protège contre deux contournements : réduire un run DIRECTION en STANDARD parce qu’aucune capture n’est disponible, ou considérer une protection critique comme hors scope parce que le moyen de l’observer manque.

Elle confirme également que `NOT-VERIFIED` désigne une preuve absente, pas une autorisation de livrer n’importe quel artefact. La qualité de construction et l’honnêteté de preuve restent deux axes distincts.

## Interface machine du contrat UI/UX

### Granularité et proportionnalité

La projection `ui_ux_reality_pack` rend obligatoires :

```text
content_model
primary_task
first_gesture
state_matrix
responsive_matrix
accessibility_basis
robustness_basis
proof_scope
coverage_map
```

Chaque matrice exige au moins un élément. La projection racine exige en outre `creative_direction_set`, `ui_ux_reality_pack` et `evaluation_case` simultanément.

La projection ne peut donc pas représenter directement :

- un paquet UI/UX seul ;
- un cas réellement non responsive avec matrice vide ;
- une profondeur où robustesse ou accessibilité spécialisée sont examinées mais non applicables sans inventer une entrée ;
- une activation proportionnée indépendante de direction créative et d’évaluation complète.

Un système peut choisir de conserver un bundle de démonstration exhaustif, mais il doit alors le nommer comme exemple composite plutôt que projection directe de chaque run. La documentation actuelle le présente comme une projection machine des contrats de production sans expliquer cette granularité.

### Vocabulaire de preuve

`coverage_map.proof_status` accepte seulement :

```text
observed
not_verified
not_applicable
```

ACTION emploie ailleurs :

```text
NOT-VERIFIED
NOT-OBSERVED
N/A-JUSTIFIED
```

Le problème ne se limite pas à la casse. `not_applicable` omet la justification requise par `N/A-JUSTIFIED`; `observed` décrit un fait, pas un résultat ou un verdict ; `not_verified` peut correspondre à la valeur canonique, mais aucun mapping n’est déclaré. La projection crée donc une petite taxonomie parallèle alors qu’ACTION/STATUS interdit aux documents voisins de créer des synonymes concurrents.

### Validateur ciblé

Le script annonce qu’un chemin JSON fourni est validé. En pratique, il reconnaît uniquement les trois chemins d’exemples canoniques du package. Une copie byte-identique de `production_contracts.example.json` placée ailleurs est rejetée comme « chemin non canonique » avant lecture du contenu.

Le script fonctionne donc comme test interne des exemples, pas comme validateur d’une projection utilisateur. Cette limitation est importante pour l’utilisabilité machine du contrat, mais distincte de la qualité normative du bloc ACTION.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle complète

`validate_all.py` passe : package, contrats, exemples, fixtures, distributions et reproductibilité restent intègres.

Ce PASS montre que les fichiers respectent les contrôles actuels. Il ne détecte pas les divergences de proportionnalité, de temporalité ou de vocabulaire décrites ci-dessus, car les exemples fournis satisfont précisément le schéma fermé.

### Test 1 — routes du bloc et de ses dépendances

```text
ACTION/FIRST-RENDER      PASS
ACTION/UI-UX-REALITY     PASS
DIRECTION/START          PASS
ACTION/RUN-STANDARD      PASS
ACTION/RUN-DIRECTION     PASS
ACTION/RUN-SYSTEM        PASS
SAVOIR/CONTEXT           FAIL — locator inconnu
SAVOIR/TECH              FAIL — locator inconnu
ACTION/STATUS            FAIL — locator inconnu
ACTION/PRECONDITION      FAIL — locator inconnu
```

Les deux façades principales sont accessibles. Les propriétaires conditionnels de contexte, technique, statuts et préconditions restent inaccessibles par leurs noms normatifs.

### Test 2 — proportionnalité de la projection UI/UX

Mutations ciblées :

```text
responsive_matrix = []              REJECTED — minItems non atteint
projection contenant UI/UX seule    REJECTED — creative_direction_set absent
```

Le schéma ne sait pas exprimer directement le non-chargement ou l’activation isolée annoncés par la prose.

### Test 3 — vocabulaire canonique

Mutation :

```text
coverage_map.proof_status = NOT-VERIFIED
```

Résultat :

```text
REJECTED — valeur non canonique
```

La valeur acceptée par ce schéma est `not_verified`; aucun mapping explicite vers ACTION n’est fourni.

### Test 4 — fichier utilisateur

Une copie valide de l’exemple a été soumise depuis un chemin temporaire.

Résultat :

```text
CONTRACT VALIDATION FAILED — chemin non canonique
```

Le contenu n’est pas évalué lorsque le chemin ne correspond pas à l’un des exemples embarqués.

## Passage C — usages simulés

### Premier rendu STANDARD

Le designer construit un écran avec contenu crédible, hiérarchie, typographie, états applicables et responsive jugeable. Le bloc produit une cible concrète sans lui imposer une direction artistique particulière. Le comportement attendu est robuste.

### Premier rendu visuellement fort mais preuve U absente

Le rendu peut être composé, spécifique et présentable tout en restant `EXPLORATORY` ou `NOT-VERIFIED` sur l’usage. Le bloc interdit de transformer sa force visuelle en preuve de tâche. La séparation qualité/probation fonctionne.

### Prototype exploratoire volontairement creux

Si les capacités de construction sont disponibles et que le prototype est présenté comme premier artefact du run, `EXPLORATORY` ne justifie pas sa faiblesse. S’il s’agit seulement d’une esquisse préparatoire non présentée comme objet jugeable, le contrat FIRST-RENDER ne devrait pas être détourné pour l’interdire. La frontière doit rester liée au statut réel de l’artefact.

### État d’erreur critique

Une capture nominale ne suffit pas. Le premier objet doit montrer ou rendre inspectable erreur, permission, feedback et récupération selon le scope. Ce comportement protège correctement les tâches critiques.

### Runtime non disponible

Le mode reste inchangé ; la preuve technique ou perceptuelle devient `NOT-VERIFIED`, avec limite et prochaine preuve. L’équipe ne peut ni simuler un PASS ni reclasser silencieusement la tâche.

### CONTEXT nécessaire seulement pour la preuve

L’artefact est déjà construit et aucune modification n’est probable, mais le choix de la méthode d’accessibilité ou du support d’observation dépend de SAVOIR/CONTEXT. La règle « peut modifier le prochain artefact » permettrait de ne pas charger la section alors qu’elle peut modifier le verdict, la limite et NEXT-PROOF.

### Projection d’un cas UI/UX proportionné

Le run ne concerne aucun responsive. La prose permet de ne pas charger la perspective ou de la déclarer non applicable avec justification. Le schéma exige quand même un élément dans `responsive_matrix`; le producteur doit inventer une ligne ou renoncer à la projection.

### Validation d’un paquet réel

L’intégrateur copie l’exemple, l’adapte à son projet et appelle le validateur officiel avec son nouveau chemin. Le script rejette le chemin avant de lire le JSON. Il ne peut donc pas servir de contrôle de livraison tel quel.

## Passage D — constats

### F-ACT-004 — le chargement conditionnel de CONTEXT et TECH est borné trop étroitement au prochain artefact

- Gravité provisoire : **Significatif**
- État : **confirmé dans le bloc 2**
- Preuve : ligne 110 charge SAVOIR seulement si ses questions peuvent modifier le prochain artefact ; le bloc 1, READING_MAP et SAVOIR montrent que ces sources peuvent modifier méthode, preuve, limite, runtime et prochaine action sans modifier l’artefact
- Comportement observable : la source spécialisée n’est pas chargée lorsque le rendu reste identique mais que la conclusion probatoire doit changer
- Risque : PASS ou clôture sur méthode inadéquate, scope mal déclaré, preuve manquante non reconnue, fallback ou prochain test omis
- Facteur atténuant : ACTION garde explicitement preuve, limite et verdict ; la capacité manquante conduit à `NOT-VERIFIED`
- Relations : F-ACT-001 pour le chargement ; F-DIR-037 et F-DIR-038 pour capacité et médium
- Propriétaires pressentis : ACTION pour le déclencheur ; SAVOIR pour les questions spécialisées
- Test futur : artefact inchangé mais changement de méthode, de limite, de référentiel, de runtime observé ou de NEXT-PROOF

### F-ACT-005 — `PROOF-SCOPE` fusionne couverture attendue et scope réellement observé

- Gravité provisoire : **Significatif**
- État : **contradiction temporelle confirmée**
- Preuve : ligne 107 définit le scope réellement observé ; ligne 110 décrit les huit lignes comme décisions de construction et couverture attendue ; le schéma ne possède qu’un `proof_scope`
- Comportement observable : un scope planifié est présenté comme observé, ou l’observation finale écrase la cible et masque l’écart de couverture
- Risque : surqualification de preuve, non-vérification invisible, impossibilité d’expliquer ce qui était prévu mais non exécuté
- Facteur atténuant : `coverage_map` distingue certaines exigences observées et non vérifiées ; ACTION exige déjà limite et prochaine preuve
- Relations : F-DIR-003 sur la temporalité et F-ACT-002 sur le mapping humain/machine
- Propriétaires pressentis : ACTION pour la sémantique ; schéma de contrats pour la projection
- Test futur : scope attendu avant build, observation partielle, viewport omis, population non testée, runtime remplacé et comparaison cible/réel

### F-ACT-006 — la projection machine universalise et agrège un contrat déclaré proportionné

- Gravité provisoire : **Significatif provisoire**
- État : **divergence humain/machine confirmée ; disposition différée à l’audit des schémas**
- Preuve : lignes 95 et 110 proportionnent les éléments et refusent un formulaire universel ; le schéma exige toutes les matrices non vides et les trois contrats racine simultanément
- Comportement observable : une dimension non applicable doit recevoir une entrée artificielle ; un paquet UI/UX isolé est invalide ; un run simple hérite de direction créative et évaluation complètes
- Risque : slop procédural, fausses données, abandon de la projection ou impression que toutes les dimensions ont été traitées
- Facteur atténuant : le fichier peut avoir été conçu comme exemple composite de capacités plutôt que format d’un run individuel, mais cette granularité n’est pas documentée
- Relations : F-DIR-010 sur les formes concurrentes et F-ACT-001 sur la proportion de chargement
- Propriétaires pressentis : schéma des contrats et documentation machine ; ACTION reste propriétaire de la proportion sémantique
- Test futur : UI/UX seul, micro-delta, non-applicabilité justifiée, run sans direction créative, run sans évaluation complète

### F-ACT-007 — `coverage_map.proof_status` crée une taxonomie parallèle de preuve

- Gravité provisoire : **Significatif**
- État : **divergence de vocabulaire confirmée**
- Preuve : le schéma accepte `observed`, `not_verified`, `not_applicable` et rejette `NOT-VERIFIED`; ACTION distingue `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED`
- Comportement observable : conversion ad hoc entre statuts, perte de la justification de non-applicabilité, confusion entre observation et verdict
- Risque : traces incompatibles, agrégation erronée, non-applicabilité utilisée comme absence de test sans raison
- Facteur atténuant : les valeurs vivent dans une sous-carte de couverture et pourraient être déclarées comme états locaux si un mapping normatif était fourni
- Relations : F-DIR-011, F-DIR-019, F-DIR-029 et F-ACT-003
- Propriétaires pressentis : ACTION pour le sens ; schéma pour les valeurs de transport
- Test futur : observé négatif, non observé, non vérifié, non applicable justifié, preuve partielle et conversion vers RUN_CARD

### F-ACT-008 — le validateur des contrats ne valide pas un fichier utilisateur hors des exemples canoniques

- Gravité provisoire : **Significatif**
- État : **comportement machine confirmé**
- Preuve : une copie valide de l’exemple est rejetée comme « chemin non canonique » ; le script associe le type de contrat uniquement aux chemins exacts des exemples embarqués
- Comportement observable : l’intégrateur ne peut pas valider sa propre projection avec la commande ciblée annoncée
- Risque : contrat machine non utilisable en production, validation remplacée par une inspection manuelle ou contournée
- Facteur atténuant : la suite interne valide correctement les exemples et mutations embarquées ; un validateur JSON Schema externe reste possible
- Relation : dépendance machine de F-ACT-006, mais correctif et test distincts
- Propriétaire pressenti : `validate_contracts.py` et documentation d’usage
- Test futur : fichier externe valide, invalide, type explicitement fourni, détection de schéma, chemins absolus/relatifs et trois familles de contrats

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — chargement et routes

Les deux façades principales du bloc sont résolubles, ce qui est positif. `SAVOIR/CONTEXT` et `SAVOIR/TECH`, explicitement appelés, échouent cependant comme `ACTION/STATUS` et `ACTION/PRECONDITION`. F-ACT-001 et F-DIR-028 restent confirmés ; leurs fixtures doivent inclure ces deux propriétaires SAVOIR.

### F-DIR-009 — one-shot et qualité initiale

FIRST-RENDER confirme qu’un objet fort peut rester en one-shot si l’observation et les risques tiennent. Il n’impose aucune correction décorative. F-DIR-009 est encore atténué par le propriétaire ACTION.

### F-DIR-018 — priorité du premier objet

UI-UX-REALITY rend contenu, geste, feedback, états, responsive, focus et récupération constitutifs du premier objet. Le premier objet n’est donc pas limité à une scène visuelle : il peut être la tâche et ses conditions réelles. Le risque de sur-contrainte dans DIRECTION demeure local, mais ACTION fournit une interprétation plus large à préserver.

### F-DIR-019 — absence de preuve et non-applicabilité

ACTION emploie correctement `EXPLORATORY` et `NOT-VERIFIED` lorsqu’une preuve manque, sans convertir l’absence en `N/A-JUSTIFIED`. La projection `coverage_map` réintroduit toutefois `not_applicable` sans justification, ce qui maintient le problème ouvert via F-ACT-007.

### F-DIR-024 — objet produit et preuve

La ligne 91 sépare explicitement qualité de construction, score et verdict ; UI-UX-REALITY distingue décisions de production, preuve, limite et verdict. Le propriétaire ACTION confirme que premier objet fort et preuve exécutée ne sont pas interchangeables. F-ACT-005 montre néanmoins que leur temporalité doit être mieux mappée.

### F-DIR-030 — propriété du jugement de craft

ACTION définit la qualité initiale attendue par mode sans revendiquer un verdict esthétique. SAVOIR reste nécessaire au jugement de craft ; ACTION conserve observation, preuve et clôture. La frontière est saine dans ce bloc.

### F-DIR-035 — registres de statut

La formule « ce statut » appliquée à `EXPLORATORY` ne dit pas s’il s’agit de l’issue ou du verdict global. La section STATUS suivante doit être auditée avant de créer ou non un constat ACTION autonome. F-DIR-035 reste ouvert.

### F-DIR-037 — capacité positive

Le bloc corrige fortement le risque : construction, tâche, états, accessibilité, responsive et robustesse appartiennent à la capacité positive. Une capacité manquante ne réduit ni le mode ni l’ambition de protection. F-DIR-037 est atténué côté ACTION.

### F-DIR-004 et F-DIR-038 — portée et médiums

Le bloc vise explicitement les surfaces UI/UX et parle de viewport, focus, clavier, contenu et runtime. Il ne prétend pas couvrir seul le print, le spatial ou tous les médiums. SAVOIR/TECH fournit une traduction par médium, mais son locator échoue et son chargement est borné au prochain artefact. Les deux constats restent ouverts jusqu’à la lecture complète de SAVOIR et des routes.

## Éléments conformes à préserver

1. Le premier rendu vise une qualité positive, pas seulement l’absence de défaut.
2. La qualité initiale est proportionnée au mode et au risque.
3. Aucun style, palette, score ou verdict esthétique n’est imposé.
4. Les cinq modes reçoivent une cible initiale adaptée.
5. `EXPLORATORY` ne justifie pas un objet volontairement creux lorsque la capacité existe.
6. Un objet visuellement fort ne devient pas automatiquement une preuve d’usage.
7. L’interface et la tâche sont construites ensemble.
8. Le feedback, les états d’erreur, l’indisponibilité, les permissions et la récupération sont traités comme partie du produit.
9. Le contenu long ou multilingue sert à révéler les défauts réels.
10. Le responsive est une recomposition, pas une réduction mécanique.
11. Une capture nominale ne suffit pas lorsqu’un état ou une récupération porte la décision.
12. Le contrat relie contenu, tâche, geste, états, responsive, accessibilité, robustesse et scope.
13. ACTION conserve preuve, limite et verdict ; SAVOIR conserve les questions spécialisées.
14. Une capacité manquante conduit à `NOT-VERIFIED` ou à l’issue appropriée.
15. Une capacité manquante ne rétrograde jamais silencieusement le mode.
16. `DIRECTION/START` reste la source unique de classification.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Deux façades, dépendances, routes et projection machine examinées |
| B — Contrats | FULL | Qualité initiale, UI/UX réelle, huit dimensions, temporalité et classification analysées phrase par phrase |
| C — Usage | TARGETED | STANDARD, rendu fort non prouvé, exploration, erreur critique, runtime absent, preuve spécialisée et projection proportionnée simulés |
| D — Résistance | FULL | Cinq nouveaux constats ACTION et mises à jour des dépendances enregistrés |
| Contrôles machine | FULL ciblé | Suite officielle, dix routes, schéma, quatre mutations et validateur ciblé contrôlés |

## Point de passage

Le bloc 2 d’ACTION est entièrement lu. Il fournit l’une des meilleures capacités positives du système : construire dès le premier rendu un objet réel, habitable et jugeable, sans confondre ambition de qualité et preuve de résultat. Les défauts se concentrent aux interfaces : déclencheur de chargement trop étroit, temporalité du scope de preuve et divergence de la projection machine.

La prochaine unité est `ACTION.md`, lignes 116–188 : `ACTION/STATUS`, états du run, issues, séparation des registres, chemin minimal, principe positif, verdicts V/U/A/T et statut de direction. Elle devra notamment trancher l’ambiguïté de `EXPLORATORY`, vérifier les transitions d’état, les cooccurrences issue/verdict et l’absence de vocabulaire concurrent. Aucun patch n’est autorisé à ce stade.
