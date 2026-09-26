# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 5

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 373–445 de la reconstruction de travail
- Sections : `DIRECTION/VISUAL_TARGET`, compilation de la première proposition, qualification de la direction, test d’utilité de l’ancre, routes de production, réserve `ANCHOR-GENERATED` et passage à `SPECCED`
- Interfaces vérifiées : `DIRECTION/FIRST-OBJECT`, `DIRECTION/ATELIER`, `ACTION/PIPELINE-DIRECTION`, `ACTION/RUN_CARD`, `ACTION/STRUCTURED-PROOF`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE`, READING_MAP, GLOSSAIRE, schéma JSON, exemple et validateur de `RUN_CARD`
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des représentations de la cible, scénarios d’asset et quatre tests ciblés du contrat machine
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et les conclusions du bloc 4 ont été relues avant l’examen, notamment F-DIR-001, F-DIR-003, F-DIR-006, F-DIR-010, F-DIR-018 et F-DIR-020.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 373–390 | Définir la cible avant build | Sort d’une logique d’adjectif/palette ; lie promesse, composition, matière, type, preuve et anti-direction | Le champ `Preuve` peut être confondu avec la preuve exécutée d’ACTION |
| 392–409 | Compiler une proposition cohérente et située | Relation plutôt qu’addition décorative ; registre traité comme hypothèse ; propriété du craft respectée | Trois représentations non équivalentes de la cible sans mapping explicite |
| 411–419 | Tester l’utilité d’une ancre | Décision, contre-indication, attributs rejetés et limites de transfert | Le contrat textuel n’est pas représentable fidèlement dans la projection machine |
| 421–437 | Choisir une route d’asset | Routes diverses, révisables et liées aux droits/performance/fidélité | Aucune route pour l’absence intentionnelle ; négation universelle sur la génération ; temporalité du « crop réel » |
| 439–445 | Protéger l’identité et autoriser le build | Réserve claire ; `SPECCED` séparé du construit/observé/accepté | Le validateur ne contrôle pas la réserve et refuse la branche sans ancre pourtant autorisée ailleurs |

## Passage A — architecture visible

`VISUAL_TARGET` remplit une fonction centrale : transformer une direction verbale en décisions pilotables avant le build. Le bloc ne se contente pas d’une ambiance. Il exige thèse, conséquence, silhouette, relation de plans, opération dominante, matière, typographie, objet de preuve et anti-direction, puis relie ces décisions au premier rendu.

L’ordre causal est clair : la cible existe avant le build, puis `FIRST-OBJECT` la matérialise et ACTION compare le rendu réel à cette cible. Ce bloc confirme donc encore que les façades plaçant `FIRST-OBJECT` avant `VISUAL_TARGET` sont mal ordonnées.

La cible est toutefois décrite sous trois formes différentes :

1. **table principale à dix champs** : thèse, conséquence observable, ancre, silhouette, relations de plans, opération dominante, matière/asset, typographie, preuve et anti-direction ;
2. **compilation à dix étapes** : contexte réel, promesse, tension, relation, objet de preuve, geste, composition, matière/type/asset, états/contraintes et premier rendu jugeable ;
3. **quatre décisions avant build** : promesse, relation, composition et résolution initiale.

La condition `SPECCED` fournit ensuite une quatrième liste : thèse, conséquence, ancre, silhouette, plans, opération, preuve, route d’asset si nécessaire, anti-direction et rendu attendu.

Ces formes peuvent correspondre à champ, processus, synthèse et test de sortie. Le texte ne fournit cependant aucun mapping. La tension et le geste n’existent pas comme champs principaux ; typographie et matière ne sont plus explicites dans la condition `SPECCED`; états et contraintes apparaissent dans la compilation ; le rendu attendu apparaît seulement à la sortie. Un lecteur ne sait pas si les quatre décisions remplacent les dix champs, les complètent ou les résument.

## Passage B — contrat sémantique

### La cible avant build

La table possède une bonne qualité de décision. La thèse relie monde, public et promesse. La conséquence observable empêche une direction purement rhétorique. Silhouette, plans et opération dominante forcent une relation perceptible. La matière native au code est reconnue comme choix complet, ce qui évite de transformer l’asset externe en obligation esthétique. L’anti-direction protège contre le retour automatique à un gabarit ou un effet.

L’expression « conséquence observable » reste correctement formulée comme attente avant build : ce que la personne **doit** percevoir, comprendre ou pouvoir faire si la thèse tient. Elle ne constitue pas encore une observation réelle.

Le champ nommé simplement `Preuve` pose en revanche une collision de vocabulaire. Ici, il désigne un objet, média, état ou fenêtre produit qui répond à la promesse — autrement dit un **objet de preuve produit**. Dans ACTION, le glossaire et READING_MAP, la preuve désigne une observation, une capture, un test, une mesure ou une comparaison exécutée dans un scope.

La phrase d’ouverture précise que la cible ne remplace pas les preuves d’ACTION, mais le nom du champ reste identique. Cette collision est particulièrement risquée lors du handoff ou de la sérialisation : une fenêtre produit visible peut être transportée comme `proof.observed` alors qu’elle ne prouve ni usage, ni accessibilité, ni performance, ni résultat externe.

### Compilation de la première proposition

La compilation est l’un des meilleurs éléments du bloc. Elle demande une relation visible et un premier rendu jugeable plutôt qu’un dossier de décisions entourant un artefact générique. Elle traite les registres naturel, éditorial, tactile ou technique comme hypothèses situées, jamais comme presets. Elle autorise les composants authored tout en protégeant les primitives critiques contre une originalité artificielle.

La règle de retrait — supprimer ce qui ne change aucune relation visible ou nommer sa limite — est saine contre l’ornement. Sa portée doit néanmoins rester visuelle et créative. Elle ne peut pas autoriser le retrait d’une sémantique, d’une protection, d’un état, d’un comportement ou d’une information nécessaire dont la conséquence est fonctionnelle, accessible, juridique ou technique plutôt que immédiatement visible. Les règles globales protègent ces éléments ; la formulation locale gagnerait à dire « aucune relation perceptible, décision, tâche, preuve ou contrainte ».

La qualification de la direction sépare correctement créativité, goût, craft et preuve. Une thèse forte ou une référence ne promet pas à elle seule le polish du rendu.

### Test d’utilité de l’ancre

L’ancre n’est pas un moodboard décoratif. Elle doit modifier une décision structurelle ou perceptuelle, fournir une contre-indication et distinguer attributs retenus, rejetés et non transférables. Une référence ne prouve ni efficacité, ni droit, ni adéquation au public.

La projection structurée ne conserve toutefois pas ce contrat de façon explicite. L’objet `anchors[]` contient : `role`, `source`, `date`, `scope`, `retained`, `rejected`, `transformation`, `transformation_status` et `limitation`. Il ne contient :

- ni type d’ancre `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` ou `ANCHOR-PROVIDED` ;
- ni identifiant d’ancre ;
- ni champ distinct pour la contre-indication ;
- ni attributs non transférables distincts des éléments rejetés ou de la limitation.

ACTION affirme pourtant conserver le type et l’identifiant de l’ancre. Les informations peuvent être fusionnées dans `source`, `rejected` ou `limitation`, mais aucun mapping canonique ne l’indique.

### Routes de production

La décision de route avant build est utile : `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` et `HYBRIDE` couvrent de nombreux moyens sans les transformer en classement de qualité. La route peut évoluer lorsque la direction reste stable et que la modification réduit un risque.

#### Absence intentionnelle sans route

La ligne 423 exige une route lorsque l’asset **ou son absence** porte une décision perceptible. Pourtant, aucune valeur ne représente directement l’absence intentionnelle. `CODE-NATIVE` couvre type, donnée, matière, SVG, layout ou mouvement ; il ne décrit pas toujours une décision de ne produire aucun asset ou traitement directeur.

ACTION reconnaît explicitement « absence intentionnelle » dans la fiche d’asset, et SAVOIR traite l’absence d’asset comme une sortie valide. La table de DIRECTION possède donc un trou de classification. Forcer `CODE-NATIVE` créerait un faux choix de production.

#### Négation universelle pour la génération

`GÉNÉRÉ-DIRIGÉ` est autorisé lorsqu’« aucune source autorisée ne résout mieux le besoin ». Cette condition est impossible à démontrer sans borner l’univers de recherche. Elle peut provoquer deux échecs : recherche indéfinie pour prouver une absence mondiale, ou affirmation non fondée après quelques résultats.

Le contrat devrait comparer la génération aux sources autorisées **réellement observées ou disponibles dans le scope et le délai déclarés**, puis conserver la limite. L’objectif — ne pas générer par facilité — serait préservé sans exiger une négation universelle.

#### Temporalité du crop réel

La route doit être nommée avant le build, mais elle est déclarée insuffisante si elle n’explique pas pourquoi l’asset, « à son crop réel et dans son contexte réel », augmente preuve, compréhension ou singularité. Avant le build, crop et contexte sont attendus ou spécifiés ; après le build, ils sont observés.

La révision sur preuve suggère bien deux moments, mais ils ne sont pas nommés : justification pré-build sur crop prévu, puis vérification post-build sur crop réellement observé. La phrase actuelle peut encourager une affirmation prématurée ou rendre la route pré-build impossible à satisfaire littéralement.

### Réserve generated-only et SPECCED

La protection identitaire est conceptuellement bonne : une direction à enjeu identitaire élevé calibrée uniquement sur hypothèse générée conserve une réserve explicite. `HELD` ne doit pas masquer l’absence de référence observée ou de contrainte réelle.

La définition de `SPECCED` est également saine : prêt à construire ne signifie ni construit, ni observé, ni accepté.

Deux contradictions apparaissent cependant au niveau machine et inter-document :

1. SAVOIR autorise une ancre non applicable avec `N/A-JUSTIFIED`, alors que le validateur exige toujours au moins une ancre structurée en mode DIRECTION.
2. Le schéma ne peut distinguer les trois types d’ancre, donc le validateur ne peut contrôler la réserve spécifique d’une ancre générée seule.

La cible complète ne peut pas non plus être ajoutée directement à l’objet `direction` de la projection JSON : celui-ci autorise seulement `thesis`, `anti_direction`, `first_object`, `scope` et `constraint`. Les autres informations peuvent rester dans la trace pointée par `trace_locator`, puisque la projection est volontairement partielle. La phrase « la cible peut vivre dans la RUN_CARD » doit donc préciser si elle désigne la trace humaine extensible ou la projection JSON contrôlée.

## Contrôles machine ciblés

### Test 1 — type et identifiant d’ancre explicites

Ajout de `anchor_type: ANCHOR-GENERATED` et `anchor_id: generated-01` à l’exemple officiel :

```text
RUN_CARD VALIDATION FAILED
run_card.anchors[0] : champs inconnus : anchor_id, anchor_type
```

Le schéma interdit donc les informations qu’ACTION dit conserver explicitement.

### Test 2 — generated-only identitaire, HELD sans réserve spécifique

L’exemple officiel a été modifié avec : décision d’identité à enjeu élevé, source `ANCHOR-GENERATED`, `direction_status: HELD`, limitation générique et aucune réserve indiquant l’absence de calibration externe.

```text
RUN_CARD VALIDATION PASSED
```

Le validateur accepte la configuration interdite par la ligne 441. Cela ne prouve pas qu’un reviewer humain l’accepterait, mais confirme que la protection n’est pas contrôlable avec la projection actuelle.

### Test 3 — aucune ancre applicable, N/A justifié

L’exemple a été placé en décision exploratoire avec `anchors: []` et une limitation `N/A-JUSTIFIED` :

```text
RUN_CARD VALIDATION FAILED
DIRECTION exige au moins un ancrage structuré
```

La branche permise par `SAVOIR/SOURCE` n’est pas représentable dans le contrat machine.

### Test complémentaire — champs essentiels de VISUAL_TARGET

L’ajout de `observable_consequence`, `silhouette` et `dominant_operation` dans `run_card.direction` produit :

```text
RUN_CARD VALIDATION FAILED
run_card.direction : champs inconnus : dominant_operation, observable_consequence, silhouette
```

La cible complète doit donc vivre hors de cette projection ou obtenir un mapping dédié.

## Passage C — usage simulé

### Agent préparant une direction

Il peut suivre la table à dix champs, puis ne conserver que les quatre décisions, ou utiliser la condition `SPECCED` comme paquet minimal. Selon son choix, typographie, états, tension, geste ou route d’asset peuvent disparaître. La clause de relation mutuelle améliore la qualité, mais ne résout pas la mémoire du run.

### Reviewer

Le reviewer peut lire `Preuve : fenêtre produit` et croire que la preuve d’ACTION existe. En réalité, il ne dispose peut-être que d’un objet de démonstration. Sans séparation lexicale, la preuve de production et la preuve de vérification se mélangent.

### Designer choisissant l’absence d’image

L’absence d’asset est une décision forte : retenue, type et contenu portent seuls la promesse. La table lui demande une route, mais aucune valeur ne décrit honnêtement cette absence. `CODE-NATIVE` suggère qu’un traitement est produit, même si le choix réel est de ne pas en avoir.

### Agent recherchant un asset

Pour satisfaire `GÉNÉRÉ-DIRIGÉ`, il devrait savoir qu’aucune source autorisée ne fait mieux. Il ne connaît jamais l’ensemble des sources possibles. Il peut soit chercher sans condition d’arrêt, soit masquer la limite de sa recherche.

### Système automatique

Il ne peut ni sérialiser explicitement le type d’ancre, ni représenter l’absence d’ancre, ni contrôler la réserve generated-only. Il accepte pourtant une direction identitaire `HELD` qui viole la protection textuelle. Le contrat humain et le contrat machine prennent donc des décisions différentes.

## Passage D — constats

### F-DIR-023 — VISUAL_TARGET possède plusieurs paquets non équivalents sans mapping

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau documentaire**
- Preuve : table lignes 377–388, compilation ligne 394, quatre décisions lignes 396–403 et condition `SPECCED` ligne 443
- Risque : omission variable de typographie, matière, état, contrainte, tension, geste, ancre ou anti-direction selon la représentation choisie
- Propriétaire pressenti : DIRECTION
- Test futur : un exemple unique doit pouvoir être projeté sans perte dans les quatre représentations

### F-DIR-024 — le champ `Preuve` confond objet produit et preuve exécutée

- Gravité provisoire : **Significatif**
- État : **confirmé sémantiquement**
- Preuve : ligne 387 contre le glossaire, READING_MAP et ACTION, où preuve signifie observation/test/mesure dans un scope
- Risque : fenêtre produit ou média déclaré comme preuve d’usage, accessibilité, performance ou résultat
- Facteur atténuant : ligne 375 indique que la cible ne remplace pas les preuves d’ACTION
- Propriétaire pressenti : DIRECTION pour renommer `Objet de preuve` ou qualifier le champ ; ACTION conserve `PROOF`

### F-DIR-025 — aucune route ne représente l’absence intentionnelle d’asset

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : ligne 423 déclenche une route pour l’asset ou son absence ; table 427–433 sans valeur d’absence ; ACTION ligne 575 et SAVOIR reconnaissent l’absence intentionnelle
- Risque : faux `CODE-NATIVE`, asset ajouté pour remplir la route ou décision de retenue non traçable
- Propriétaire pressenti : DIRECTION pour la taxonomie ; ACTION pour la fiche exécutée

### F-DIR-026 — la route GÉNÉRÉ-DIRIGÉ dépend d’une négation non bornée

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau logique**
- Preuve : ligne 432 exige qu’aucune source autorisée ne résolve mieux le besoin
- Risque : recherche sans condition d’arrêt ou affirmation impossible à étayer
- Propriétaire pressenti : DIRECTION/SOURCE
- Correction probable à éprouver : borner la comparaison aux sources réellement observées ou disponibles dans le scope, le délai et les droits déclarés

### F-DIR-027 — le contrat machine des ancres diverge du contrat humain

- Gravité provisoire : **Majeur provisoire**
- État : **confirmé par trois tests ciblés ; gravité finale à confirmer lors de l’audit machine**
- Preuve : type et identifiant rejetés ; `ANCHOR-GENERATED` identitaire `HELD` sans réserve accepté ; absence d’ancre N/A rejetée
- Risque : protection identitaire non contrôlée, surcharge de `source`/`limitation`, faux ancrage pour satisfaire le validateur et divergence entre reviewer humain et système automatique
- Facteur atténuant : la projection JSON est déclarée partielle et la trace complète peut vivre ailleurs
- Propriétaires pressentis : DIRECTION pour les voies d’ancrage ; ACTION pour la trace ; schéma et validateur pour la projection
- Tests futurs : ajout d’un `anchor_type` canonique, branche `N/A-JUSTIFIED`, réserve generated-only et compatibilité descendante

### Mise à jour de F-DIR-001 — ordre VISUAL_TARGET / FIRST-OBJECT

Le bloc confirme explicitement que la cible rassemble les décisions avant build et qu’ACTION compare ensuite le rendu construit. F-DIR-001 demeure **Significatif confirmé** : seules les façades dérivées inversent encore l’ordre.

### Mise à jour de F-DIR-003 — temporalité des champs

La route d’asset est décidée avant build, mais son test d’insuffisance parle de crop et contexte « réels ». La distinction entre valeur attendue pré-build et observation post-build n’est pas explicitée. Le constat transversal de temporalité est renforcé.

### Mise à jour de F-DIR-006 — mapping entre vues et projection

Les quatre représentations de la cible, l’absence de mapping vers `run_card.direction` et l’absence de type d’ancre structurée renforcent F-DIR-006. F-DIR-023 et F-DIR-027 isolent respectivement la dérive documentaire et la divergence machine.

### Mise à jour de F-DIR-010 — formes dérivées divergentes

La cible possède désormais plusieurs paquets minimaux ou synthétiques dans une même section. Le problème de formes concurrentes ne se limite donc plus au lancement et à la clôture ; il touche aussi la spécification pré-build.

## Éléments conformes à préserver

1. `VISUAL_TARGET` existe avant le build et empêche de commencer avec un adjectif ou une palette.
2. La cible relie public, promesse, conséquence, composition, matière, type, preuve et anti-direction.
3. La matière native au code est reconnue comme choix complet.
4. La compilation vise une relation visible, pas un dossier autour d’un artefact générique.
5. Les registres stylistiques restent des hypothèses situées, jamais des presets.
6. Les composants authored sont autorisés sans rendre les primitives critiques inhabituelles.
7. Créativité, goût, craft et preuve restent séparés.
8. Une ancre sans conséquence de décision est refusée comme décoration.
9. Une référence n’est ni preuve d’efficacité, ni droit de réemploi, ni validation du public.
10. Les routes d’asset sont des décisions situées, révisables et non des classements de qualité.
11. La génération reste une hypothèse comparable, jamais une autorité esthétique.
12. `SPECCED` est correctement séparé de construit, observé et accepté.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Effectué sur les lignes 373–445 et les routes amont/aval |
| B — Contrats | FULL | Cible, ancre, asset, temporalité et projection comparés aux propriétaires |
| C — Usage | TARGETED | Agent, reviewer, designer, chercheur d’asset et système automatique simulés |
| D — Résistance | FULL | Cinq nouveaux constats et quatre mises à jour enregistrés |
| Contrôles machine | TARGETED | Quatre mutations de l’exemple officiel exécutées ; quatre divergences confirmées |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `DIRECTION/DIRECTION-ATELIER`, la vérité de scène et le début de `DOUBLE-LOOP`. Il devra vérifier les responsabilités de craft, les alternatives situées, le transport des labels de vérité et l’articulation entre correction, one-shot et preuve ACTION.
