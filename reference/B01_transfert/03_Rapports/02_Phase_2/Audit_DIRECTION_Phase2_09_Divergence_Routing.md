# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 9

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 701–762 de la reconstruction de travail
- Sections : `1. Direction divergente — déclenchement DIRECTION`, `2. Routage — quoi charger et quand`, `Déclencheurs critiques`, `Index à la demande`
- Interfaces vérifiées : `DIRECTION/START`, `CREATIVE-BOOT`, `VISUAL_TARGET`, `DIRECTION-ATELIER`, les cinq absolus, `ACTION/AUTHORITY`, `ACTION/PRECONDITION`, `ACTION/PIPELINE-DIRECTION`, `ACTION/ROUTING`, `ACTION/ANTI-SLOP`, `SAVOIR/ROUTING`, `SAVOIR/CRAFT/CFT-01–02`, `SAVOIR/INTEGRITY`, `BIBLIOTHEQUE/SELECT`, QUICKSTART, READING_MAP, ORCHESTRATION_MAP, schéma et validateur `RUN_CARD`, lecteur et validateur de routes
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des propriétaires, scénarios de choix et de routage, contrôle machine du paquet d’alternative et résolution de quinze locators concrets
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et le rapport du bloc 8 ont été relus. Les constats repris directement sont F-DIR-006, F-DIR-010, F-DIR-023, F-DIR-027, F-DIR-028, F-DIR-030, F-DIR-035 et F-DIR-037.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 701–714 | Situer une première idée et ouvrir une divergence proportionnée | Positions plutôt que styles ; aucun catalogue ni quota de nouveauté ; matière plate ou absente admise | La grille reproduit SAVOIR/CFT-02 et ACTION avec des périmètres légèrement différents |
| 716–720 | Définir l’alternative, la sélection et l’axe matière | Alternative liée à public/JTBD/contrainte ; matérialisation proportionnée ; cosmétique refusé | Paquet exigé dans RUN_CARD non représentable ; « direction modale » non définie |
| 722 | Protéger l’autorité humaine avant build | Autonomie explicite comme exception ; absence de regard jamais assimilée à une validation | « statut » regroupe une issue et un verdict ; transport de l’autonomie laissé à la trace externe |
| 726–743 | Charger les routes forcées par des signaux critiques | ACTION toujours chargé pour livraison ; modules spécialisés conditionnels ; absence de fichier/preuve visible | Plusieurs lignes déplacent ou simplifient le propriétaire réel du test, de la scène ou du craft |
| 745–760 | Fournir un index par besoin | Accès rapide aux routes SAVOIR/BIBLIOTHEQUE | « Nouvelle structure d’écran » présélectionne STANDARD ; dix routes SAVOIR ne sont pas résolues par le lecteur officiel |
| 762 | Interdire les anciennes routes actives | Règle de migration claire | Le contrôle livré ne garantit pas que toutes les routes quotidiennes actuelles soient résolubles |

## Passage A — architecture visible

Le bloc forme un enchaînement cohérent : **ouvrir une décision DIRECTION → sélectionner une position → obtenir l’autorité nécessaire → charger les propriétaires utiles**. Il protège à la fois l’ambition créative et la proportionnalité de lecture.

La première section n’est pas un générateur de variantes. Elle définit un test de différence réelle avant le build. La seconde est une façade de routage général, responsabilité annoncée de DIRECTION dans la constitution. ACTION possède néanmoins sa propre table `ACTION/ROUTING`, presque parallèle, et SAVOIR possède `SAVOIR/ROUTING`. Cette architecture peut fonctionner si :

- DIRECTION ne classe et ne déclenche que le premier propriétaire ;
- ACTION ajoute les routes requises par la construction et la preuve ;
- SAVOIR conserve le propriétaire exact des méthodes de jugement ;
- BIBLIOTHEQUE reste propriétaire de la structure.

Les écarts apparaissent lorsque la table DIRECTION ne se contente plus de déclencher mais attribue la méthode au mauvais propriétaire, impose un mode depuis un besoin structurel ou référence une route que le lecteur officiel ne sait pas résoudre.

## Passage B — contrat sémantique

### Divergence proportionnée

Le contrat de base est solide : une comparaison n’est requise que lorsque la décision est ouverte et qu’une position différente peut modifier le choix. Il n’existe ni nombre minimal de directions, ni quota de nouveauté, ni obligation de construire plusieurs rendus complets.

Les six axes sont utiles : structure, matière, voix, temporalité, densité, rapport texte/image. Ils correspondent exactement au noyau de `SAVOIR/CRAFT/CFT-02`; SAVOIR ajoute la question de jugement associée. ACTION reprend ces axes et ajoute rythme ou émotion traduite en levier visible lorsqu’ils sont pertinents.

La répétition a ici une fonction possible : DIRECTION active la divergence, SAVOIR aide à juger et ACTION l’exécute. Elle reste maintenable seulement si un propriétaire de la liste et une règle d’extension sont identifiables. Le corpus ne les déclare pas explicitement pour ces axes, mais aucun conflit concret suffisant ne justifie encore un nouveau constat autonome.

### Alternative située

La définition est bonne : une alternative n’est distincte que si elle répond à un public, un JTBD, une contrainte ou une opportunité différents. Une palette, un adjectif ou une variation cosmétique ne suffit pas. Le niveau de matérialisation — phrase, schéma, cible ou rendu — dépend uniquement de ce qui est nécessaire pour comparer la décision.

La branche d’absence est également proportionnée. Si aucune alternative plausible ne peut changer le choix, le run nomme la raison puis passe à la spec. Cette sortie évite la variante artificielle.

La phrase « la `RUN_CARD` nomme la position retenue, l’alternative considérée, la raison de son niveau de matérialisation et la preuve attendue » crée toutefois un contrat impossible à projeter directement :

- l’objet `direction` ne possède que `thesis`, `anti_direction`, `first_object`, `scope` et `constraint` ;
- une alternative plausible n’est pas une `anti_direction` ;
- `materialization_reason` et le lien alternative/preuve n’existent pas ;
- les propriétés supplémentaires sont rejetées.

Ces informations peuvent être condensées dans `direction.thesis`, `next_proof` ou une trace externe, mais aucun mapping canonique ne le dit. La formulation « dans la RUN_CARD » est donc plus forte que la capacité réelle de la projection structurée.

### Sélection de la direction

La règle de sélection exige un avantage vérifiable relié à tâche, compréhension, preuve, singularité ou contrainte. Elle évite que « premium », « dynamique » ou « bleu plutôt que vert » deviennent une décision.

Le terme **direction modale** n’apparaît nulle part ailleurs dans le corpus et n’est pas défini. Il peut signifier la direction dominante, retenue, la plus probable ou issue d’un vote. À l’endroit précis où le système demande de sélectionner une position, cette ambiguïté est inutile. `Direction retenue`, terme déjà canonique dans ACTION, serait non ambigu.

### Axe matière

L’obligation de déclarer la matière est correctement bornée. Déclarer `plat`, `hérité`, `absent` ou `inchangé` satisfait l’axe ; aucune texture n’est imposée. Cette formulation protège le système contre le biais « direction forte = ajout d’effet » et doit être conservée.

La matière n’a pas de champ structuré dédié. Elle peut vivre dans la thèse, la spec ou la trace. Ce point renforce le besoin de mapping de F-DIR-006 sans établir qu’un nouveau champ machine est indispensable.

### Checkpoint humain et autonomie

Le checkpoint protège correctement l’autorité : une capacité ne vaut pas permission de décider. ACTION/AUTHORITY précise que l’autonomie doit posséder une base, un périmètre, une condition de reprise et un rôle de reprise ; ACTION/PIPELINE-DIRECTION exige que l’autonomie couvre explicitement le périmètre DIRECTION.

En l’absence de cette autonomie, la position, l’alternative, la raison et la preuve attendue sont présentées avant le build. Une nouvelle marque, un nouveau public, une nouvelle surface autonome ou une nouvelle hypothèse peuvent rouvrir le checkpoint. Cette granularité évite qu’un accord ancien devienne une délégation générale.

La ligne 722 emploie toutefois « `BLOCKED`, `EXPLORATORY` ou le statut prévu par ACTION ». `BLOCKED` est une issue ; `EXPLORATORY` peut être une issue ou un verdict global ; aucun des deux n’est un état générique nommé « statut ». ACTION/AUTHORITY donne la formulation plus exacte : décision exploratoire, retournée ou escaladée selon risque, preuve et sortie. Cette dérive renforce F-DIR-035 sur la séparation des registres, sans exiger un constat autonome.

### Déclencheurs critiques

Plusieurs routes sont exactes et utiles :

- surface identitaire ou mode DIRECTION → `ACTION/RUN-DIRECTION` ;
- toute livraison → route ACTION du mode et gates applicables ;
- doute d’application → `SAVOIR/INTEGRITY` ;
- ancre absente → retour à l’ancrage ou issue ACTION ;
- échec assumé → protocole `FAIL-ASSUMED` ;
- claim daté → `SAVOIR/TOOLS` avec source, date, portée et limite.

Trois lignes brouillent néanmoins la propriété :

1. **Asset, motion, scène ou type spécifique** appelle un contrat ACTION et « une route SAVOIR nécessaire ». Une scène structurelle appartient aussi à BIBLIOTHEQUE ; la ligne ne le rend pas visible.
2. **Motif générique ou réflexe** appelle le « test motivation/construction d’ACTION ». ACTION dit explicitement que la matrice canonique appartient à `SAVOIR/CRAFT/CFT-01` et qu’ACTION n’en contrôle que la conséquence.
3. **Détail final** pouvant modifier caractère, hiérarchie ou densité appelle `SAVOIR/STATE`, `SAVOIR/INTEGRITY` et capture, mais omet `SAVOIR/CRAFT`, propriétaire direct de composition et densité.

Ces erreurs ne sont pas seulement terminologiques : elles peuvent charger une méthode inadéquate ou laisser le vrai propriétaire silencieux.

### Index à la demande

L’index est majoritairement aligné avec `SAVOIR/ROUTING` et `ACTION/ROUTING`. Une ligne est trop large :

> Nouvelle structure d’écran → après START et la classification `ACTION/RUN-STANDARD`, `BIBLIOTHEQUE/SELECT`.

Une nouvelle structure peut relever de :

- `STANDARD` pour une vue opérationnelle sans identité autonome ni partage ;
- `DIRECTION` pour un premier contact ou une structure identitaire ;
- `SYSTÈME` pour un gabarit, composant ou convention partagés.

START reste déclaré prioritaire, mais la cellule encode déjà le résultat `STANDARD`. La route robuste est : `START → route du mode classé → BIBLIOTHEQUE/SELECT si la structure reste ouverte`.

### Résolution effective des routes

Le bloc emploie quinze locators exacts testables par `read_route.py`. Résultat :

- 5 résolus : `DIRECTION/START`, `ACTION/RUN-DIRECTION`, `ACTION/RUN-STANDARD`, `SAVOIR/CRAFT`, `BIBLIOTHEQUE/SELECT` ;
- 10 rejetés : `SAVOIR/TYPE`, `SOURCE`, `INTEGRITY`, `STATE`, `FRAME`, `STYLE`, `SYSTEM`, `CONTEXT`, `TECH`, `TOOLS`.

Les dix sections existent réellement dans SAVOIR. READING_MAP explique que les routes non listées doivent être résolues par préfixe et titre exact, mais `read_route.py` ne sait résoudre que la table fermée des locators principaux. Le validateur de la carte ne détecte pas cette divergence.

Le défaut F-DIR-028, d’abord observé sur ATELIER, est donc systémique : le lecteur automatisé ne couvre pas une grande partie des routes quotidiennes que DIRECTION lui-même recommande.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle complète

`validate_reading_map.py` et `validate_all.py` passent, y compris contrôles documentaires, schémas, contrats, distributions et reproductibilité.

Ce résultat confirme l’intégrité de la baseline. Il ne prouve pas la résolution des routes non listées, car la suite ne les exerce pas.

### Test 1 — paquet d’alternative dans l’objet `direction`

Ajout de :

```text
direction.retained_position
direction.alternative
direction.materialization_reason
direction.expected_proof
```

Résultat :

```text
RUN_CARD VALIDATION FAILED
- run_card.direction : champs inconnus : alternative, expected_proof, materialization_reason, retained_position
```

### Test 2 — paquet condensé en prose

La position, l’alternative et la raison sont placées dans `direction.thesis`; la preuve attendue dans `next_proof`.

Résultat :

```text
RUN_CARD VALIDATION PASSED
```

Le contrat est donc transportable par convention textuelle, mais pas mappable ni vérifiable champ par champ.

### Test 3 — couverture du lecteur de routes

Quinze locators exacts du bloc ont été exécutés individuellement :

```text
TOTAL pass=5 fail=10
```

Les échecs retournent `ROUTE READ FAILED — locator inconnu`, même lorsque le titre propriétaire existe.

### Test 4 — contrôle de la carte après les échecs

Après les dix échecs :

```text
READING MAP VALIDATION PASSED — carte dérivée, propriétaires, handoff et liens contrôlés
```

Le test livré vérifie la cohérence des locators déclarés dans la carte, pas la couverture des routes réellement invoquées par les sources normatives.

## Passage C — usage simulé

### Choix visuel réellement ouvert

Le designer situe l’idée, formule une alternative liée à une contrainte distincte, la matérialise au niveau minimal puis choisit selon un avantage vérifiable. Le parcours évite à la fois le premier réflexe et le catalogue de variantes.

### Variation seulement cosmétique

Une palette ou un adjectif seul est rejeté comme direction distincte. Le designer revient à une différence de tâche, structure, preuve, public, matière ou contrainte. Le contrat résiste bien au théâtre de divergence.

### Aucune alternative plausible

La raison de non-comparaison est nommée et le run passe à la spec. Aucun rendu factice n’est exigé. Il faudra seulement unifier cette sortie avec le `N/A-JUSTIFIED` utilisé par ATELIER et les contrats ACTION pour éviter plusieurs formulations.

### Session sans autonomie DIRECTION

Le build s’arrête au checkpoint. Si l’owner est absent, la décision devient exploratoire, retournée ou escaladée. Le système ne transforme pas le silence humain en accord.

### Nouvelle homepage identitaire

START classe correctement `DIRECTION`. L’index « nouvelle structure d’écran » peut néanmoins orienter vers `RUN-STANDARD` si la cellule est lue isolément. La priorité déclarée de START évite l’erreur seulement si le lecteur réexécute réellement la classification.

### Nouveau gabarit partagé

START devrait classer `SYSTÈME`, puis charger BIBLIOTHEQUE et les contrats de migration. La cellule STANDARD décrit mal ce cas et peut masquer consumers, rollback et non-régression.

### Motif générique à auditer

Le lecteur suit « test motivation/construction d’ACTION », mais ACTION le renvoie à SAVOIR/CFT-01. Le parcours effectue un détour et peut donner à ACTION la propriété de la matrice, contrairement à la frontière déclarée.

### Agent utilisant uniquement le lecteur de routes

L’agent résout START, RUN-DIRECTION et CRAFT, puis échoue sur TYPE, SOURCE ou INTEGRITY. Il doit abandonner l’outil et rechercher manuellement dans SAVOIR. Sous contrainte, il peut omettre la route, deviner le titre ou lire tout le document, trois comportements que la carte devait précisément éviter.

## Passage D — constats

### F-DIR-039 — le paquet d’alternative exigé dans RUN_CARD n’a pas de mapping structuré

- Gravité provisoire : **Significatif**
- État : **divergence humain/machine confirmée**
- Preuve : ligne 716 exige position, alternative, raison de matérialisation et preuve attendue dans la RUN_CARD ; le schéma ne possède pas ces propriétés et les rejette
- Contrôle machine : quatre champs explicites rejetés ; condensation dans `direction.thesis` et `next_proof` acceptée
- Risque : alternative confondue avec anti-direction, justification perdue, ou conformité déclarée dans une prose impossible à contrôler
- Facteur atténuant : la trace externe peut porter le paquet sans nouveau champ JSON
- Propriétaires pressentis : DIRECTION pour le paquet décisionnel ; ACTION pour le mapping vers RUN_CARD ou trace
- Test futur : phrase, schéma, cible et rendu doivent tous pouvoir relier position, alternative, raison et preuve sans dupliquer la cible visuelle

### F-DIR-040 — « direction modale » est un terme unique et non défini

- Gravité provisoire : **Observation**
- État : **ambiguïté textuelle confirmée**
- Preuve : unique occurrence ligne 718 ; ACTION emploie déjà `direction retenue`
- Risque : interprétation comme direction dominante, moyenne, issue d’un vote ou simple variante majoritaire
- Propriétaire pressenti : DIRECTION
- Correction probable à éprouver : employer `direction retenue` ou définir explicitement le terme s’il porte une différence nécessaire

### F-DIR-041 — l’index « nouvelle structure d’écran » présélectionne STANDARD avant la nature réelle de la décision

- Gravité provisoire : **Significatif**
- État : **contradiction de routage confirmée**
- Preuve : ligne 749 contre START, qui réserve STANDARD à un écran/flow nouveau sans charge identitaire ni blast radius partagé
- Risque : homepage identitaire sous-classée ; gabarit partagé privé de migration, consumers et rollback ; priorité de START contournée par la façade courte
- Facteur atténuant : la cellule commence par « après DIRECTION/START » et START est déclaré prioritaire
- Propriétaire pressenti : DIRECTION/START pour le mode ; BIBLIOTHEQUE pour la structure ouverte
- Test futur : écran opérationnel, homepage de marque, template partagé, flow critique et modification structurelle locale

### F-DIR-042 — les déclencheurs critiques attribuent plusieurs méthodes au mauvais propriétaire

- Gravité provisoire : **Significatif**
- État : **écart d’ownership confirmé**
- Preuve : ligne 742 nomme le test motivation/construction « d’ACTION » alors qu’ACTION le déclare canonique dans SAVOIR/CFT-01 ; ligne 737 ne rend pas BIBLIOTHEQUE visible pour une scène ; ligne 743 omet CRAFT pour caractère, hiérarchie et densité
- Risque : méthode dupliquée ou cherchée au mauvais endroit, structure non chargée, revue finale incomplète
- Facteur atténuant : ACTION/ROUTING et SAVOIR/ROUTING permettent de retrouver les propriétaires corrects après lecture supplémentaire
- Propriétaires pressentis : DIRECTION pour le déclencheur ; SAVOIR/BIBLIOTHEQUE pour les méthodes et structures ; ACTION pour la conséquence et la preuve
- Test futur : motif générique, scène structurelle, motion d’état, détail typographique et correction de densité finale

### Mise à jour de F-DIR-006 — mapping humain / trace / projection

Le paquet d’alternative et l’axe matière peuvent vivre en prose ou dans une trace externe, mais la section ne déclare aucun mapping. Le checkpoint dépend aussi d’une autonomie conservée dans la trace ACTION plutôt que dans la projection. F-DIR-006 est renforcé sans conclure que chaque notion exige un champ JSON.

### Mise à jour de F-DIR-010 — vues et paquets concurrents

La divergence ajoute un nouveau paquet pré-build — position, alternative, raison de matérialisation, preuve — qui recoupe thèse, anti-direction, contre-choix, target, `DECISION-INTENT` et `NEXT-PROOF`. Sans mapping, la fragmentation des formes s’étend au choix créatif.

### Mise à jour de F-DIR-023 — paquets de cible et d’alternative

Le paquet d’alternative n’est pas identique à VISUAL_TARGET, mais il doit y être relié : la position retenue devient la thèse, tandis que l’alternative reste une comparaison située et non une anti-direction. Cette transformation n’est pas explicitée ; F-DIR-023 reste **Significatif**.

### Mise à jour de F-DIR-027 — ancre absente

Le déclencheur critique exige un retour à l’ancrage ou une issue ACTION pour toute surface identitaire sans ancre. Il renforce encore le caractère obligatoire de l’ancre, tandis que SAVOIR conserve une branche `N/A-JUSTIFIED`. F-DIR-027 reste **Majeur provisoire**.

### Mise à jour de F-DIR-028 — le lecteur de routes ne couvre pas les routes quotidiennes invoquées

Le défaut dépasse ATELIER. Dix des quinze locators exacts de ce bloc sont rejetés par `read_route.py`, alors que leurs sections existent et que `validate_reading_map.py` passe. F-DIR-028 reste **Significatif confirmé**, avec portée désormais systémique sur les routes SAVOIR non listées.

### Mise à jour de F-DIR-030 — frontière du jugement de craft

DIRECTION reproduit les axes de CFT-02, attribue par erreur le test CFT-01 à ACTION et omet parfois CRAFT dans les détails de caractère/densité. F-DIR-042 isole les erreurs de route ; F-DIR-030 reste le problème transversal de frontière entre cadrage, jugement et exécution.

### Mise à jour de F-DIR-035 — registres de clôture

Le checkpoint emploie « statut » pour `BLOCKED` et `EXPLORATORY`, qui appartiennent à des registres différents. ACTION/AUTHORITY fournit une formulation non ambiguë par conséquence — exploratoire, retournée ou escaladée. F-DIR-035 est renforcé sans nouveau défaut autonome.

### Mise à jour de F-DIR-037 — sélection de capacité

La ligne 737 force les routes spécialisées seulement « si la capacité est requise ». Comme le test d’activation de capacité exclut encore certains besoins de construction et de robustesse, une scène, un asset, une motion ou une typographie peuvent rester silencieux pour la mauvaise raison. F-DIR-037 reste **Significatif**.

## Éléments conformes à préserver

1. Une décision ouverte appelle des positions distinctes, pas un catalogue de variantes.
2. Aucun quota de directions, de nouveauté ou de builds n’est imposé.
3. L’alternative est liée à un public, un JTBD, une contrainte ou une opportunité distincts.
4. Le niveau de matérialisation dépend de la décision à comparer.
5. L’absence d’alternative plausible est une sortie valide si sa raison est nommée.
6. Une palette, un adjectif ou une variation cosmétique ne constituent pas une direction.
7. La direction retenue doit posséder un avantage vérifiable.
8. La matière plate, héritée, absente ou inchangée reste une position valide.
9. L’autonomie explicite, et non la capacité technique, détermine si le checkpoint peut être omis.
10. Le silence humain ne devient jamais une validation implicite.
11. ACTION est forcé pour toute livraison et conserve les gates applicables.
12. Les routes SAVOIR restent conditionnelles à leur capacité de modifier la décision.
13. Un fichier ou une preuve manquants produisent une limite, jamais un contenu inventé.
14. `FAIL-ASSUMED` reste routé vers son protocole propriétaire.
15. Les claims datés conservent source, date, portée et limite.
16. Les anciennes routes ne sont pas utilisables comme instructions actives.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Enchaînement divergence/autorité/routage et frontières des propriétaires examinés |
| B — Contrats | FULL | Axes, alternative, sélection, matière, checkpoint et chaque ligne de routage comparés |
| C — Usage | TARGETED | Choix ouvert, cosmétique, absence d’alternative, autonomie, structure identitaire/partagée et agent automatisé simulés |
| D — Résistance | FULL | Quatre nouveaux constats et huit mises à jour enregistrés |
| Contrôles machine | FULL ciblé | Suite officielle, paquet d’alternative, quinze locators et angle mort du validateur exécutés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain et dernier bloc de lecture de DIRECTION couvre `3. Invariants de jugement`, `Clôture de direction`, `Entrée prioritaire` et `Lecture instrumentée et règle de passage` — lignes 766–817. Il devra vérifier les invariants finaux, le test de sortie, les propriétaires, la dernière façade prioritaire, la mesure de charge réelle et la cohérence de clôture avant la synthèse complète de DIRECTION.
