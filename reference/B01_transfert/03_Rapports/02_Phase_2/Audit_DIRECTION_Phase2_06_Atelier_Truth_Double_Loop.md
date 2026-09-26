# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 6

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 449–541 de la reconstruction de travail
- Sections : `DIRECTION/DIRECTION-ATELIER`, vérité de scène, `DIRECTION/DOUBLE-LOOP`, contrôle compact du premier objet, one-shot, signaux de réouverture, résilience visuelle et apprentissage expérimental
- Interfaces vérifiées : constitution et architecture d’activation de DIRECTION, `CREATIVE-BOOT`, `FIRST-OBJECT`, `SAVOIR/CRAFT — CFT-00`, `ACTION/FIRST-RENDER`, `ACTION/PIPELINE-DIRECTION`, `ACTION/RUN_CARD`, QUICKSTART, READING_MAP, skill pratique, schéma et validateur de `RUN_CARD`, scripts `read_route.py`, `validate_reading_map.py` et `validate_all.py`
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, scénarios de vérité et de one-shot, comparaison des propriétaires et contrôles machine ciblés
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et les conclusions du bloc 5 ont été relues avant l’examen. Les constats repris directement sont F-DIR-006, F-DIR-009, F-DIR-011, F-DIR-019, F-DIR-020, F-DIR-021 et F-DIR-024.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 449–466 | Activer un cadrage créatif situé et retenir une position | Activation conditionnelle, même trace, pas de questionnaire ni quota, contre-choix utile | Locator absent ; frontière de craft avec SAVOIR et ACTION ; sortie sans effet mal typée |
| 468–480 | Protéger la vérité de scène et fermer la critique locale | Les labels ne deviennent ni statut, ni ancre, ni verdict ; la critique nomme un effet et une réserve | Audience et transport non définis ; taxonomie non orthogonale ; fin de module sans statut canonique |
| 482–521 | Organiser création, observation, correction et one-shot | Correction réelle, branche one-shot explicite, signaux de retour, séparation de la clôture ACTION | `Preuve précoce` réactive la collision de vocabulaire ; les responsabilités de jugement se superposent |
| 525–541 | Éprouver la résilience et apprendre entre runs | Transformation choisie par le risque, pas de quota ; limites de preuve explicites | Le gain est surtout formulé comme visible, alors que certaines corrections portent tâche ou robustesse |

## Passage A — architecture visible

Le bloc poursuit correctement la séquence causale déjà établie : la position est approfondie si nécessaire, le premier objet est construit, le rendu réel est observé, puis une correction ou un arrêt est décidé. `DIRECTION-ATELIER` reste facultatif et rejoint la même trace que `VISUAL_TARGET`. `DOUBLE-LOOP` ne crée ni gate, ni statut, ni verdict. ACTION conserve la preuve, la réinspection et la clôture.

Le système présente ici cinq lentilles proches :

1. le noyau d’ATELIER — moment, tension, geste, position/exclusion ;
2. la grille complète à huit dimensions de `FIRST-OBJECT` ;
3. les cinq tests compacts de `DOUBLE-LOOP` ;
4. les huit dimensions de `SAVOIR/CRAFT — CFT-00` ;
5. la revue créative et la repasse d’`ACTION/PIPELINE-DIRECTION`.

Le mapping entre la grille complète de DIRECTION et ses cinq tests compacts est explicite à la ligne 339. La relation entre DIRECTION, SAVOIR et ACTION est aussi décrite globalement : DIRECTION choisit et formule le défaut, SAVOIR fournit le jugement, ACTION exécute la preuve et la clôture. En revanche, le bloc local emploie à nouveau les expressions « module de craft », « critique de craft » et « défaut dominant de craft ». Sous contrainte de temps, un lecteur peut donc exécuter plusieurs revues similaires ou ne plus savoir laquelle constitue la méthode propriétaire.

Un défaut de routage est directement exécutable : la skill pratique demande de charger `DIRECTION/DIRECTION-ATELIER`, mais ce locator n’apparaît pas dans la table des locators de READING_MAP. `read_route.py` ne résout que les routes listées, malgré la phrase selon laquelle les routes non listées restent résolues par préfixe et titre exact. Le module officiel existe dans le fichier propriétaire mais n’est pas chargeable par le mécanisme fourni.

## Passage B — contrat sémantique

### DIRECTION-ATELIER

L’activation est bien protégée. Le module ne doit être chargé que lorsque la première scène, l’identité, la confiance culturelle ou la relation promesse–preuve demandent une position située, et seulement s’il peut changer une décision. Il ne devient ni questionnaire adressé à la personne, ni formulaire parallèle, ni générateur obligatoire de variantes.

Les quatre éléments du noyau sont complémentaires : le moment humain situe la rencontre avec la promesse sans inventer un persona ; la tension doit changer une décision visible ; le geste produit montre une action ou une transformation sans promettre un résultat externe ; la position conserve aussi ce qui est exclu. La règle des familles internes est proportionnée : une proposition principale est rendue à la personne, une alternative n’est matérialisée que si elle peut modifier l’arbitrage, et aucun quota de familles ou de builds n’est introduit.

La frontière de propriété reste toutefois imparfaite. La constitution attribue exclusivement à SAVOIR les principes de jugement et le craft ; `CREATIVE-BOOT` précise que `SAVOIR/CRAFT` possède le jugement des qualités de présence et de fabrication. Ici, DIRECTION nomme pourtant ATELIER « module de craft officiel », impose une méthode de critique de craft et formule un défaut dominant « de direction ou de craft ». ACTION définit ensuite sa propre revue créative et sa repasse.

Cette superposition peut être interprétée sainement : DIRECTION cadre la position et le défaut de direction, SAVOIR donne les critères de jugement, ACTION exécute l’observation et persiste `creative_close`. Mais cette interprétation doit être reconstruite depuis plusieurs sections ; le bloc ne la formule pas avec cette précision.

La condition de fin du module crée une seconde ambiguïté. Le module est « terminé » s’il a changé une décision visible **ou** documenté qu’il ne pouvait pas le faire. Un résultat négatif peut être utile, mais les causes ne sont pas équivalentes :

- la conséquence attendue ne s’est pas manifestée : `NOT-OBSERVED` ;
- le contrôle n’a pas pu être exécuté : `NOT-VERIFIED` ;
- le module était réellement non applicable : `N/A-JUSTIFIED` ;
- la décision initiale a été confirmée par l’observation : `DECISION-CHANGE` peut enregistrer cette confirmation.

Le verbe « documenter » ne choisit aucune de ces branches. Il permet donc de considérer le module comme terminé sans rendre l’issue canonique ni la prochaine conséquence explicite.

### Vérité de scène

La règle locale poursuit un objectif essentiel : empêcher qu’un exemple, une donnée, un comportement ou une scène hypothétique soit pris pour une preuve réelle. Elle sépare correctement le marquage de vérité des statuts ACTION, des voies d’ancrage et des verdicts.

La taxonomie mélange cependant deux axes différents :

| Label | Axe réellement décrit |
|---|---|
| `TRUTH/OBSERVED` | Base épistémique : quelque chose a réellement été observé dans un scope |
| `TRUTH/ILLUSTRATIVE` | Base épistémique : le contenu ou l’objet est hypothétique ou fictif |
| `TRUTH/MECHANISM` | Nature du claim : la scène matérialise une relation, une action ou une transformation produit |

Un mécanisme peut être observé ou illustratif. Une maquette générée avec données fictives peut matérialiser honnêtement le mécanisme tout en restant illustrative. Or `FIRST-OBJECT` demande à une démonstration générée ou hypothétique de porter `TRUTH/ILLUSTRATIVE` **ou** `TRUTH/MECHANISM`. Cette alternative autorise un agent à choisir seulement `MECHANISM` et à ne plus rendre visible le caractère fictif des personnes, données ou résultats.

`TRUTH/OBSERVED` demande aussi une lecture prudente. Observer une capture, un test ou une source ne valide pas universellement le claim : la définition conserve bien base et scope dans ACTION, mais le mot `TRUTH` peut être lu plus fortement que « base observée ». La protection dépend donc de la proximité réelle de la limitation et de sa formulation compréhensible.

F-DIR-021 est renforcé. « À proximité du claim ou de l’objet » n’indique toujours pas si le label technique doit vivre :

- dans une annotation ou une trace interne ;
- dans l’artefact présenté au reviewer ;
- dans une formulation visible et compréhensible par la personne exposée au produit ;
- dans plusieurs de ces couches avec un mapping entre label interne et copie visible.

Le contrat machine ne résout pas ce transport. Un champ structuré `truth_markings` est rejeté par le schéma. Le même label placé en texte libre dans `proof.observed` est accepté, alors qu’un marquage illustratif n’est pas une preuve observée. Une trace externe pointée par `trace_locator` peut porter l’information, mais aucun mapping canonique ne l’exige.

### DOUBLE-LOOP, premier objet et one-shot

La distinction des niveaux est largement correcte. `DIRECTION/DOUBLE-LOOP` porte l’apprentissage de la décision créative ; `ACTION/PIPELINE-DIRECTION` porte l’exécution livrable, la preuve, la correction, la comparaison et la clôture ; `ACTION/GATE-B/B1b` reste un contrôle spécialisé. ACTION précise explicitement qu’il ne s’agit pas de trois boucles concurrentes.

Le contrôle compact du premier objet est correctement relié à la grille complète. Les réponses ne demandent pas d’ajouter du polish par réflexe : elles renvoient à la hiérarchie, au contenu, à l’action, au contrat, au contre-choix, aux états ou à la déclaration de limite. « Une correction substantielle » ne signifie pas un quota maximal d’une itération, car la phrase ajoute expressément « sans quota d’itérations ».

L’intitulé `Preuve précoce` réactive néanmoins F-DIR-024. Sa question porte sur une scène qui rend le mécanisme plus clair que le texte, donc sur un **objet de preuve produit** ou une démonstration perceptuelle, pas sur une preuve exécutée d’ACTION. Le mot `preuve` reste employé pour deux contrats différents dans une zone qui insiste justement sur leur séparation.

La branche one-shot est, elle, formulée correctement. Elle exige une préparation, un premier rendu complet, une capture réelle, le contrôle du premier objet, la revue créative, le risque et les transformations pertinentes. Elle autorise l’arrêt après l’observation initiale si la qualité attendue est atteinte, les risques applicables couverts et aucune amélioration utile probable. Cette section confirme que l’obligation de modification et de réobservation du `CREATIVE-BOOT` est l’exception fautive, pas la règle générale du système.

La référence aux « huit dimensions du premier objet » reste claire à l’intérieur de DIRECTION grâce à la grille complète et au mapping de la ligne 339. Elle demeure ambiguë pour un lecteur venant de QUICKSTART, qui présente une autre grille de huit dimensions comme l’opérationnalisation de `FIRST-OBJECT`. F-DIR-020 reste donc actif.

La formule « beau, composé, crédible, spécifique et suffisamment résolu » constitue une cible d’ambition, non une preuve. Les quatre derniers termes sont rendus plus opératoires par les tests qui suivent. `Beau` reste le terme le moins contrôlable et peut réintroduire une préférence implicite ; les clauses de beauté située, d’absence de score et de refus du canon universel limitent toutefois ce risque. Ce point reste une observation éditoriale, pas un constat autonome à ce stade.

### Réouverture, résilience et apprentissage

Les signaux de réouverture renvoient au propriétaire pertinent sans créer de gate ou de statut. La direction ne ferme jamais le run ; l’absence de capture maintient la qualité perceptuelle en `NOT-VERIFIED`. Ces garde-fous sont cohérents avec ACTION.

La résilience est choisie selon le risque et sa capacité à modifier le jugement, non pour remplir un quota. Le singulier « une transformation pertinente » n’installe pas un maximum : la branche one-shot parle d’états et transformations pertinentes au pluriel, et ACTION exige la couverture proportionnée au risque. Le test perceptuel ne devient ni preuve d’utilisabilité, ni preuve de conformité.

Les signaux d’apprentissage expérimental sont bien séparés des scores et verdicts. L’expression « gain visible » est toutefois plus étroite que la définition précédente d’une correction, qui peut changer une tâche, une preuve, une contrainte ou une propriété de robustesse. Pour un pilote créatif, cette focalisation peut être volontaire ; elle devra être confrontée à CHANGELOG et aux mécanismes d’apprentissage de série avant toute correction.

## Contrôles machine ciblés

### Test 1 — locator officiel ATELIER

Commande :

```text
python scripts/read_route.py DIRECTION/DIRECTION-ATELIER
```

Résultat :

```text
ROUTE READ FAILED — locator inconnu : DIRECTION/DIRECTION-ATELIER
```

Le contrôle témoin `DIRECTION/DOUBLE-LOOP` est correctement résolu et retourne la section complète.

### Test 2 — couverture du validateur de READING_MAP

`validate_reading_map.py` passe alors que le locator ATELIER manque. Le script vérifie les destinations **déjà listées**, un seuil minimal de lignes et quelques locators obligatoires ; il ne compare pas les routes invoquées par la skill et les sources avec la table résoluble.

La suite complète `validate_all.py`, exécutée depuis la racine du package, passe également. Le défaut n’est donc pas signalé par les validations officielles.

### Test 3 — marquage de vérité structuré

L’ajout d’un objet racine `truth_markings` à l’exemple officiel produit :

```text
RUN_CARD VALIDATION FAILED
run_card : champs inconnus : truth_markings
```

Cette absence n’est pas automatiquement une erreur de schéma puisque la trace complète peut être externe. Elle confirme néanmoins qu’aucun transport structuré du marquage n’existe dans la projection.

### Test 4 — label de vérité enfoui dans la preuve

L’ajout du texte `TRUTH/ILLUSTRATIVE — exemple de données` à `proof.observed` produit :

```text
RUN_CARD VALIDATION PASSED
```

Le schéma accepte donc une sérialisation sémantiquement trompeuse : le label illustratif est transporté comme observation. Cela ne signifie pas que le texte normatif l’autorise, mais le contrat machine ne peut ni distinguer ni rejeter cette confusion.

## Passage C — usage simulé

### Agent activé par la skill

La skill lui demande de charger ATELIER lorsque ce module peut modifier la direction. S’il utilise le lecteur de route fourni, le locator échoue. Sous contrainte de temps, il peut ignorer le module, deviner le titre dans le fichier complet ou inventer un chemin. Le principe de lecture minimale devient alors moins fiable précisément pour un module optionnel.

### Designer construisant une démonstration fictive

Le designer montre un workflow plausible avec données et personnes fictives. La scène matérialise bien le mécanisme : `TRUTH/MECHANISM` paraît approprié. Elle est aussi illustrative. Comme le système formule l’alternative avec « ou » et n’autorise pas explicitement la combinaison, le designer peut omettre la fiction et laisser la scène paraître réelle.

### Reviewer d’une capture réelle

Une capture montre qu’un bouton et un état existent dans l’artefact observé. `TRUTH/OBSERVED` peut décrire cette présence, mais ne prouve ni tâche réussie, ni préférence, ni disponibilité générale, ni effet externe. Le reviewer doit retrouver la base, le scope et les limites dans ACTION ; le label seul est insuffisant.

### Agent exécutant un one-shot valide

Le premier rendu atteint la cible, le risque dominant est couvert et aucune correction utile n’est probable. `DOUBLE-LOOP`, ACTION et SAVOIR autorisent l’arrêt après l’observation initiale. `CREATIVE-BOOT` demande pourtant de conserver une modification réelle et une réobservation attendue. L’agent peut produire une modification artificielle uniquement pour satisfaire cette phrase.

### Équipe répartissant les responsabilités

Le directeur de création utilise ATELIER, le reviewer ouvre `SAVOIR/CRAFT — CFT-00`, puis ACTION demande sa revue créative et sa repasse. Sans un mapping explicite, les trois personnes peuvent répéter la même critique, produire des défauts dominants concurrents ou traiter le résultat de DIRECTION comme la méthode propriétaire de craft.

### Système automatique

Il ne peut pas transporter les marquages de vérité dans un champ dédié. Il peut les laisser uniquement dans l’artefact ou la trace externe, ou les enfouir dans un champ texte. Le second choix passe le validateur même s’il confond illustration et preuve observée.

### Atelier activé sans effet

Le module était applicable, mais l’exploration ne modifie pas la décision. La ligne 480 permet de terminer en documentant l’absence d’effet. Selon la cause, le résultat devrait être confirmation, `NOT-OBSERVED`, `NOT-VERIFIED` ou erreur d’activation ; l’instruction locale ne permet pas de choisir.

## Passage D — constats

### F-DIR-028 — le module officiel ATELIER n’est pas résolvable par le lecteur de routes

- Gravité provisoire : **Significatif**
- État : **confirmé par exécution**
- Preuve : la skill invoque `DIRECTION/DIRECTION-ATELIER`; READING_MAP ne le liste pas ; `read_route.py` le rejette ; `validate_reading_map.py` et `validate_all.py` passent
- Risque : module optionnel ignoré, lecture intégrale forcée, locator deviné ou activation différente selon l’outil
- Facteur atténuant : le titre exact existe dans DIRECTION et le préfixe indique le propriétaire
- Propriétaires pressentis : READING_MAP et script de validation, avec DIRECTION comme source du titre
- Test futur : toute route invoquée par la skill ou une façade doit être résoluble, ou l’outil doit implémenter la résolution par préfixe et titre annoncée par READING_MAP

### F-DIR-029 — les labels de vérité mélangent base épistémique et nature du claim

- Gravité provisoire : **Significatif**
- État : **confirmé sémantiquement**
- Preuve : `OBSERVED` et `ILLUSTRATIVE` décrivent la base réelle ou fictive ; `MECHANISM` décrit ce que la scène matérialise ; la ligne 316 autorise `ILLUSTRATIVE` ou `MECHANISM`
- Risque : une démonstration fictive étiquetée seulement `MECHANISM` paraît réelle ; impossibilité de décrire proprement un mécanisme à la fois illustratif et observé dans un scope partiel
- Propriétaire pressenti : DIRECTION pour la taxonomie et la règle de combinaison ; ACTION pour base, scope et preuve
- Test futur : matrice généré/fictif × mécanisme implémenté/non implémenté × effet externe observé/non observé
- Correction probable à éprouver : séparer le statut de factualité du type de claim, ou autoriser explicitement des labels cumulables avec priorité à la divulgation de fiction

### F-DIR-030 — la propriété du jugement de craft est localement brouillée

- Gravité provisoire : **Significatif**
- État : **ambiguïté de frontière confirmée**
- Preuve : constitution et ligne 182 donnent le jugement de craft à SAVOIR ; lignes 451, 478 et 484 attribuent à DIRECTION un module, une critique et un défaut de craft ; ACTION lignes 513–521 définit la revue créative et la repasse
- Risque : trois revues exécutées comme procédures concurrentes, défauts dominants divergents ou autorité de jugement attribuée au mauvais document
- Facteurs atténuants : ACTION ligne 447 sépare explicitement décision créative, exécution et gate ; la skill charge `SAVOIR/CRAFT — CFT-00` dans le noyau DIRECTION
- Propriétaires pressentis : DIRECTION pour le cadrage et le défaut de direction ; SAVOIR pour la méthode de jugement ; ACTION pour l’exécution et la persistance
- Test futur : un run DIRECTION doit produire une seule revue créative traçable, sans dupliquer les grilles ni changer de propriétaire selon la façade

### Mise à jour de F-DIR-006 — mapping des vues locales

ATELIER réutilise la trace de `VISUAL_TARGET` sans mapping de ses champs, les labels de vérité ne possèdent pas de transport structuré et la clôture réelle finit dans `creative_close`. F-DIR-006 est renforcé. Le problème ne justifie pas automatiquement d’ajouter tous les champs au schéma ; il exige au minimum un mapping clair vers artefact, trace externe ou projection existante.

### Mise à jour de F-DIR-009 — incompatibilité du Creative Boot avec le one-shot

`DOUBLE-LOOP`, ACTION et SAVOIR convergent : une correction n’est pas requise si le premier rendu tient déjà après observation et qu’aucun gain utile n’est probable. F-DIR-009 reste **Significatif confirmé**, désormais strictement localisé à la ligne 184 du Creative Boot, qui exige encore une modification réelle et une réobservation attendue.

### Mise à jour de F-DIR-011 et F-DIR-019 — sémantique des sorties sans effet

La ligne 480 ajoute une nouvelle occurrence du problème. « Documenter que le module ne pouvait pas changer la décision » ne distingue pas non-applicabilité, vérification impossible, conséquence non observée ou confirmation. La correction devra réutiliser les statuts ACTION au lieu d’une fin générique.

### Mise à jour de F-DIR-020 — référence aux huit dimensions

Dans DIRECTION, la référence est résolue par la grille complète et le mapping vers le contrôle compact. Pour un lecteur passant par QUICKSTART, deux grilles de huit dimensions restent possibles. Le présent bloc n’aggrave pas la divergence, mais il rend son effet opérationnel dans la condition d’arrêt one-shot.

### Mise à jour de F-DIR-021 — audience et transport du marquage de vérité

Le constat est renforcé de deux manières : la taxonomie ne dit pas comment cumuler factualité et mécanisme, et la projection machine ne possède aucun transport structuré. Un champ dédié est rejeté ; un label illustratif dans `proof.observed` est accepté. F-DIR-021 reste **Significatif** et son impact machine est maintenant confirmé, sans imposer à ce stade que la solution soit un nouveau champ de `RUN_CARD`.

### Mise à jour de F-DIR-024 — collision autour du mot preuve

Le test `Preuve précoce` désigne une scène qui rend le mécanisme perceptible. Il ne désigne pas une preuve exécutée dans un scope. L’occurrence renforce la nécessité de réserver `PROOF` à ACTION et de nommer explicitement l’`objet de preuve` ou la `démonstration` dans DIRECTION.

## Éléments conformes à préserver

1. ATELIER reste activable et ne devient jamais automatique.
2. Le module ne crée ni mode, ni gate, ni statut, ni owner, ni seconde `RUN_CARD`.
3. Le moment humain n’est pas présenté comme persona ou donnée validée.
4. Une tension ne vaut que si elle change une décision visible.
5. Un geste de démonstration ne prouve pas un résultat produit réel.
6. Les familles restent internes et n’imposent ni catalogue de variantes ni quota de builds.
7. L’absence de contre-choix est admise lorsqu’aucun choix plausible ne peut modifier la décision.
8. Les labels de vérité ne sont ni statuts ACTION, ni voies d’ancrage, ni verdicts.
9. Une critique textuelle ou un adjectif de goût ne remplace pas l’artefact et la preuve.
10. La correction doit changer l’artefact, la décision, la tâche, la preuve, la contrainte ou la robustesse.
11. Le one-shot conserve préparation, artefact complet, observation, revue, risque et états pertinents.
12. L’arrêt après observation initiale est explicitement permis lorsqu’aucun gain utile n’est probable.
13. Les signaux de réouverture provoquent un retour de décision, jamais un gate ou un statut supplémentaire.
14. DIRECTION ne ferme jamais le run à la place d’ACTION.
15. La résilience est choisie selon le risque et ne devient pas un quota.
16. Un test perceptuel ne devient ni preuve d’utilisabilité, ni preuve de conformité.
17. Les signaux d’apprentissage expérimental ne deviennent ni score, ni verdict, ni quota.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Effectué sur les lignes 449–541, les routes et les mécanismes de lecture |
| B — Contrats | FULL | Activation, alternatives, vérité, propriété du craft, correction, one-shot, résilience et trace comparés |
| C — Usage | TARGETED | Agent, designer, reviewer, équipe, système automatique et one-shot simulés |
| D — Résistance | FULL | Trois nouveaux constats et six mises à jour enregistrés |
| Contrôles machine | TARGETED | Locator ATELIER, témoin DOUBLE-LOOP, validation READING_MAP, suite complète et deux sérialisations de vérité exécutés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `Rôle` et `LES CINQ RÈGLES ABSOLUES` — lignes 543–645. Il devra vérifier l’autorité réelle des absolus, leur testabilité, leurs exceptions, leur compatibilité avec les modes et leur articulation avec les contrats déjà lus.
