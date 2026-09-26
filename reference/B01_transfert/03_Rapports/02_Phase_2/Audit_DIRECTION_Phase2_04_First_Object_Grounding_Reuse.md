# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 4

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 314–369 de la reconstruction de travail
- Sections : `DIRECTION/FIRST-OBJECT`, contrat positif du premier objet, relation avec `DOUBLE-LOOP`, `GROUNDING-DECISION` et `REUSE-CHALLENGE`
- Interfaces vérifiées : architecture d’activation de DIRECTION, `EXTERNAL-START`, `VISUAL_TARGET`, `DIRECTION-ATELIER`, `DOUBLE-LOOP`, `ACTION/UI-UX-REALITY`, `ACTION/PIPELINE-DIRECTION`, `SAVOIR/SOURCE`, `SAVOIR/TOOLS`, QUICKSTART, READING_MAP et GLOSSAIRE
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des grilles, scénarios de vérité/grounding/réemploi et reprise des constats antérieurs
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole a été relue avant ce bloc : architecture visible, contrat sémantique, usage réel et résistance. Le rapport précédent a également été repris, en particulier F-DIR-001, F-DIR-006, F-DIR-011 et F-DIR-018.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 314–318 | Compiler le cadrage en un objet jugeable | Relation promesse–preuve–geste ; vérité locale ; CTA non fictif | Les labels de vérité ne distinguent pas clairement trace interne et divulgation visible |
| 320–335 | Définir huit dimensions de suffisance | Contrat positif, retours vers les décisions responsables, aucun score | Une dimension applicable mais non observée n’a pas de sortie locale ; grille concurrente dans QUICKSTART |
| 337–339 | Relier grille complète et contrôle compact | Mapping explicite ; interdiction de lancer deux checklists | « Vérité de scène » est à la fois incluse dans preuve précoce et test transversal, mais le doublon est déclaré |
| 341–354 | Décider si un grounding est utile | Recherche conditionnelle ; refus rendu contestable ; inconnue résiduelle conservée | La branche `NO` ne rappelle pas les cas où source ou grounding sont obligatoires, notamment à risque critique |
| 356–369 | Challenger le réemploi disponible | Refuse nouveauté obligatoire et répétition de confort ; différence et limite explicites | Les contrôles de public, contexte, droits et fraîcheur restent dépendants de SAVOIR/ACTION et doivent rester résolubles |

## Passage A — architecture visible

Le bloc suit un enchaînement logique : matérialiser la décision, juger la qualité du premier objet, choisir si un grounding peut modifier le résultat, puis tester le réemploi d’un antécédent. Chaque module affirme rester local à la décision et ne pas créer de gate ou de trace concurrente.

La première phrase de `FIRST-OBJECT` fournit surtout une clarification causale importante. La vue **référence** `VISUAL_TARGET` et `DIRECTION-ATELIER`, puis demande de convertir le brief en premier objet. Elle confirme donc l’ordre :

```text
START → VISUAL_TARGET / position → FIRST-OBJECT → observation
```

Il n’existe pas de circularité nécessaire dans le modèle. La circularité apparente provenait des façades qui plaçaient `FIRST-OBJECT` avant `VISUAL_TARGET` ou avant `DIRECTION`. F-DIR-001 reste un défaut réel de routage documentaire, mais la présente section permet d’identifier l’ordre causal à préserver lors de la correction.

Le bloc est cependant entouré de trois représentations différentes de la qualité du premier objet :

1. la grille complète à huit dimensions de DIRECTION ;
2. le contrôle compact à cinq tests de `DOUBLE-LOOP`, correctement mappé à cette grille ;
3. une seconde grille à huit dimensions dans QUICKSTART, présentée comme l’opérationnalisation de `DIRECTION/FIRST-OBJECT`, sans mapping vers la première.

Le contrôle compact n’est pas concurrent puisqu’il explique sa relation. La grille QUICKSTART, en revanche, change la couverture sans signaler qu’il s’agit d’une autre lentille.

## Passage B — contrat sémantique

### FIRST-OBJECT : promesse, preuve, geste et vérité

La chaîne `promesse → objet de preuve → geste` est forte. Elle évite qu’une première scène vende des bénéfices avant de rendre le mécanisme perceptible. Contrairement à `EXTERNAL-START`, cette section ne proscrit pas navigation ou cartes en tant que formes : le glossaire définit le premier objet comme un objet, une scène, un composant, une interaction ou une relation de contenu. Une navigation, une carte de données ou une collection peut donc constituer le premier objet si elle matérialise réellement la promesse et le geste.

Cette lecture localise F-DIR-018 : le problème appartient à la formulation absolue d’`EXTERNAL-START`, pas au concept de premier objet. La correction devra viser les navigations ou cartes génériques, décoratives ou prématurées, et non ces formes par principe.

La règle des CTA est également solide. Un CTA produit un comportement local réel, mène à une action réellement disponible ou déclare sa limite. Elle protège contre les liens vides, inscriptions fictives et conséquences externes simulées.

Le marquage de vérité protège aussi le système contre le faux réalisme, mais son transport est ambigu. Les labels `TRUTH/ILLUSTRATIVE` et `TRUTH/MECHANISM` sont des termes techniques locaux ; `DIRECTION-ATELIER` demande de les placer à proximité du claim ou de l’objet. Le texte ne distingue pas :

- le statut interne dans la trace ou l’annotation de design ;
- la formulation compréhensible réellement visible par la personne exposée à l’artefact.

Si le label reste seulement dans la trace, l’utilisateur final peut prendre la démonstration pour une capacité réelle. Si la chaîne technique brute est affichée dans l’interface, elle peut être inadaptée au produit. Le contrat a besoin d’une règle de projection : statut canonique interne et divulgation humaine locale lorsque le risque de méprise existe.

### Contrat positif à huit dimensions

Les huit dimensions couvrent bien le jugement perceptuel de DIRECTION : présence, foyer, signature, intégration, résolution, désirabilité située, vérité de scène et résilience visible. Les retours sont dirigés vers cible, structure, asset, contenu, type, état ou build, jamais vers un score esthétique. C’est une bonne propriété à préserver.

La phrase de sortie ne propose toutefois que deux cas : conserver une observation ou utiliser `N/A-JUSTIFIED` lorsque la dimension ne peut pas changer la décision. Elle ne dit pas quoi enregistrer lorsque la dimension est applicable mais non observable avec le scope ou les capacités présents.

Exemple : la résilience mobile peut modifier la décision, mais aucune capture mobile n’est disponible. Elle n’est pas N/A ; elle n’est pas observée non plus. ACTION et le glossaire imposent alors `NOT-VERIFIED`, et `NOT-OBSERVED` lorsque la conséquence attendue n’apparaît pas dans le scope déclaré. L’omission locale recrée une sortie binaire incomplète.

La formule « grille complète » manque aussi de qualification. Elle est complète pour le jugement créatif et perceptuel de DIRECTION, pas pour l’ensemble du premier objet UI/UX. `ACTION/UI-UX-REALITY` ajoute tâche, feedback, erreurs, permission, focus, récupération, responsive, accessibilité et robustesse. Les phrases de non-substitution limitent le risque, mais le mot « complète » devrait être borné à son registre.

#### Comparaison des deux grilles à huit dimensions

| DIRECTION/FIRST-OBJECT | QUICKSTART §6 | Relation |
|---|---|---|
| Présence | Présence | Identique |
| Foyer | Silhouette | Recouvrement partiel |
| Signature | Spécificité | Recouvrement partiel |
| Intégration | Relation produit | Recouvrement partiel |
| Résolution | Résolution | Identique |
| Désirabilité située | — | Propre à DIRECTION |
| Vérité de scène | — | Propre à DIRECTION |
| Résilience visible | — | Propre à DIRECTION |
| — | Premier objet | Propre à QUICKSTART |
| — | Contenu | Propre à QUICKSTART |
| — | Retenue | Propre à QUICKSTART |

Seuls `Présence` et `Résolution` sont identiques. Trois paires peuvent être rapprochées, mais leurs critères ne sont pas équivalents. Trois dimensions sont propres à chaque grille. Un agent suivant QUICKSTART peut donc omettre vérité et résilience ; un agent suivant DIRECTION peut ne pas expliciter contenu et retenue sous les mêmes noms.

### Relation avec DOUBLE-LOOP

Le mapping entre huit dimensions et cinq tests est explicite et utile. Le système dit clairement d’utiliser le contrôle compact pour orienter le retour, puis de revenir à la dimension responsable, sans exécuter deux checklists. Cette architecture résout le risque de duplication pour `DOUBLE-LOOP`.

`Vérité de scène` est reliée à `Preuve précoce` puis conservée comme contrôle transversal. Cette redondance est assumée ; elle peut être acceptable parce que la vérité traverse intégration, contenu et démonstration. Elle ne doit cependant pas devenir deux statuts ou deux preuves distinctes.

### GROUNDING-DECISION

Le déclencheur est proportionné : le module ne se charge que lorsqu’un fait, claim, asset, terme métier, droit, contrainte ou capacité peut modifier scène, preuve, action ou limite. La branche `NO` est intéressante parce qu’elle oblige à nommer contre-hypothèse, effet si elle était vraie, base du refus et inconnue résiduelle. Le refus devient contestable au lieu de disparaître.

Le risque se situe dans l’absence d’un garde-fou local. La branche `NO` reste disponible avec une base `SELF-ASSESSED`, sans rappeler qu’elle ne peut pas neutraliser :

- un claim mesuré, daté, réglementaire ou dépendant d’un outil ;
- une source requise par le contrat du run ;
- un risque critique de santé, sécurité, conformité, permission, confidentialité ou accessibilité ;
- une incapacité d’observer, qui doit devenir limite, `NOT-VERIFIED`, blocage ou escalade plutôt qu’un refus de grounding.

Les protections existent ailleurs dans ACTION et SAVOIR, et la ligne 354 affirme que le module ne les remplace pas. Il n’est donc pas établi que le système autorise globalement ce contournement. Mais une vue portable doit empêcher qu’un `NO` auto-évalué soit interprété comme une dispense. Ce point reste à tester sur les scénarios critiques.

### REUSE-CHALLENGE

Le contrat combat correctement deux erreurs opposées : changer uniquement pour paraître original, ou répéter un ancien choix uniquement parce qu’il est disponible. `KEEP-IF`, `CHANGE-BECAUSE`, `NON-REUSE` et `LIMIT` forcent une conséquence située et rendent possible une continuité légitime.

Le bloc ne répète pas toutes les protections de réemploi : comparabilité du public et du contexte, fraîcheur de la preuve, droits, provenance, compatibilité et consumers. Ce n’est pas automatiquement un défaut, car SAVOIR, ACTION et BIBLIOTHEQUE possèdent ces contrôles. La séparation reste valide à condition que `REUSE-CHALLENGE` ne soit jamais interprété comme une autorisation de réemployer un asset, une preuve ou un composant. Les lignes générales du corpus l’interdisent déjà.

La sémantique de `KEEP-IF` et `CHANGE-BECAUSE` recouvre en grande partie `WHY-NOW`, mais le mapping n’est pas déclaré. Cela renforce le besoin transversal de mapping de F-DIR-006 sans créer à ce stade un nouveau défaut autonome.

## Passage C — usage simulé

### Agent externe produisant une démonstration générée

L’agent construit une scène montrant une fonctionnalité hypothétique. Il dispose d’un bon contrat : marquage de vérité, interdiction du faux CTA et limite sur les résultats externes. Il peut toutefois placer `TRUTH/MECHANISM` uniquement dans sa trace et livrer une interface qui semble fonctionnelle. À l’inverse, afficher littéralement ce label technique peut dégrader la communication. Il manque une règle sur la visibilité et la formulation humaine.

### Designer sans capture mobile

La résilience mobile est pertinente et peut changer la décision, mais ne peut pas être observée. Le designer ne peut honnêtement ni fournir une observation ni déclarer N/A. Il doit connaître ACTION pour choisir `NOT-VERIFIED`; la section locale ne lui donne pas cette sortie.

### Reviewer pressé utilisant QUICKSTART

Le reviewer inspecte présence, relation produit, silhouette, premier objet, contenu, résolution, spécificité et retenue. Il peut considérer la grille complète alors qu’il n’a pas explicitement contrôlé vérité de scène ou résilience visible. Un autre reviewer suivant DIRECTION emploie une couverture différente. Les verdicts ne devraient pas dépendre de la façade choisie.

### Équipe santé ou service réglementé

Un claim de sécurité peut modifier l’action. `GROUNDING-DECISION` est activé. Sans lecture des propriétaires, l’équipe peut renseigner `NO`, une contre-hypothèse et `SELF-ASSESSED`, alors que la source ou la protection devrait être obligatoire. Le corpus global devrait bloquer cette lecture, mais la vue locale ne le rend pas explicite.

### Mainteneur réutilisant une ancienne direction

`REUSE-CHALLENGE` lui demande correctement ce qui mérite continuité, ce qui change et ce que la comparaison ne prouve pas. S’il s’agit d’un asset ou d’un composant, il doit encore passer par les propriétaires des droits, de la compatibilité et de la preuve. Le module fonctionne donc comme cadrage, pas comme autorisation.

## Passage D — constats

### F-DIR-019 — le contrat du premier objet omet les statuts applicables mais non observés

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : ligne 322 propose observation ou `N/A-JUSTIFIED`; ACTION et le glossaire distinguent `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED`
- Risque : transformer une capacité manquante en N/A, ignorer une dimension applicable ou prétendre une couverture inexistante
- Propriétaire pressenti : ACTION pour les statuts ; DIRECTION pour reproduire la triade sans réduction
- Test futur : mobile applicable sans capture, état critique non construit et vérité attendue non observée

### F-DIR-020 — deux grilles non alignées de huit dimensions encadrent le premier objet

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : lignes 324–333 de DIRECTION contre QUICKSTART lignes 160–175, qui affirme opérationnaliser `DIRECTION/FIRST-OBJECT`
- Risque : couverture différente selon la façade ; vérité, résilience, contenu ou retenue omis sans intention
- Propriétaire pressenti : DIRECTION pour la grille canonique ; QUICKSTART pour une projection exacte ou un mapping explicite
- Test futur : un exemple unique évalué par les deux grilles doit produire la même liste de questions et de lacunes

### F-DIR-021 — le marquage de vérité ne distingue pas statut interne et divulgation visible

- Gravité provisoire : **Significatif / à éprouver**
- État : **ambiguïté confirmée, impact à tester**
- Preuve : lignes 316 et 470–476 imposent un marquage près du claim ou de l’objet sans définir son audience ni sa formulation visible
- Risque : faux réalisme conservé si le label reste interne, ou jargon de gouvernance affiché littéralement dans le produit
- Propriétaire pressenti : DIRECTION pour le marquage ; ACTION pour la preuve et le scope
- Test futur : démo générée, données fictives, CTA simulé et mécanisme réellement implémenté avec résultat externe non prouvé

### F-DIR-022 — la branche de refus de grounding n’explicite pas ses interdictions

- Gravité provisoire : **Significatif / ouvert**
- État : **risque de contournement local, contradiction globale non confirmée**
- Preuve : lignes 347–354 contre les obligations de sourcing et de protection critique d’ACTION et SAVOIR
- Risque : utiliser `SELF-ASSESSED` pour éviter une source requise, une incapacité de preuve ou un risque critique
- Facteur atténuant : la section déclare ne pas remplacer les sources, statuts ou preuves d’ACTION ; les règles globales interdisent le contournement
- Propriétaire pressenti : DIRECTION pour le garde-fou local ; SAVOIR/ACTION restent propriétaires du sourcing et de la preuve
- Test futur : claim réglementaire, conseil de santé, droit d’asset, capacité indisponible et terme métier à faible enjeu

### Mise à jour de F-DIR-001 — ordre causal résolu, façades toujours contradictoires

La section confirme que `FIRST-OBJECT` consomme `VISUAL_TARGET` et, lorsqu’il est activé, `DIRECTION-ATELIER`. Il n’existe donc pas de boucle causale obligatoire. Le défaut est une contradiction de routage entre façades : la correction doit aligner ligne 72 et `EXTERNAL-START` sur l’ordre cible/spec → premier objet. Gravité **Significatif** maintenue.

### Mise à jour de F-DIR-006 — mapping des vues locales

Le défaut est renforcé par deux éléments : la seconde grille de huit dimensions sans mapping et la proximité sémantique non déclarée entre `KEEP-IF`/`CHANGE-BECAUSE` et `WHY-NOW`. F-DIR-020 isole la divergence de grille ; F-DIR-006 reste le problème transversal de projection et de déduplication.

### Mise à jour de F-DIR-011 — sémantique des absences

La ligne 322 reproduit une sortie trop courte : une dimension applicable mais non vérifiée ou une conséquence attendue mais non observée ne peut pas devenir N/A. F-DIR-019 isole cette occurrence ; F-DIR-011 reste confirmé comme dérive répétée de la sémantique ACTION.

### Mise à jour de F-DIR-018 — navigation et cartes

Le concept canonique de premier objet accepte composant, interaction et relation de contenu. La section 314–318 exige seulement que l’objet de preuve précède les bénéfices génériques. L’interdiction générale de navigation ou de cartes dans `EXTERNAL-START` est donc une sur-contrainte locale confirmée. Gravité proposée : **Significatif localisé**, car elle peut dénaturer un explorateur, un hub, une recherche ou un dashboard opérationnel.

## Éléments conformes à préserver

1. Le premier objet matérialise promesse, preuve et geste au lieu d’ajouter une décoration.
2. Une démonstration hypothétique ne devient jamais preuve de client, performance, disponibilité, intégration, sécurité ou résultat.
3. Un CTA fictif ou un lien vide ne peut pas être présenté comme action disponible.
4. La suffisance est formulée positivement et renvoie aux décisions responsables, sans score esthétique.
5. `DOUBLE-LOOP` est une vue compacte explicitement mappée, pas une seconde checklist.
6. Le grounding est conditionnel à une décision modifiable.
7. Un refus de grounding conserve une contre-hypothèse et une inconnue résiduelle.
8. Le réemploi n’est ni automatique ni interdit par principe.
9. La nouveauté n’est pas transformée en quota.
10. `LIMIT` empêche une comparaison ou un antécédent de devenir une preuve universelle.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Effectué sur les lignes 314–369 et leurs routes amont/aval |
| B — Contrats | FULL | Grilles, statuts d’absence, vérité, grounding et réemploi comparés à leurs propriétaires |
| C — Usage | TARGETED | Agent externe, designer, reviewer, équipe à enjeu et mainteneur simulés |
| D — Résistance | FULL | Quatre nouveaux constats et quatre mises à jour enregistrés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `DIRECTION/VISUAL_TARGET` et la compilation de la première proposition. Il devra vérifier si la cible résout effectivement les dépendances du premier objet, si ses champs restent proportionnés et si ancre, preuve et direction conservent des sens distincts.
