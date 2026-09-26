# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 10

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 766–817 de la reconstruction de travail
- Sections : `3. Invariants de jugement`, `Clôture de direction`, `Entrée prioritaire — à lire avant le détail`, `Lecture instrumentée et règle de passage`
- Interfaces vérifiées : constitution et architecture d’activation de DIRECTION, `DIRECTION/START`, les cinq absolus, `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`, `ACTION/RUN-SYSTEM`, `BIBLIOTHEQUE/EVOLUTION`, READING_MAP, CHANGELOG, schéma et validateur `RUN_CARD`, lecteur et validateur de routes
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des propriétaires, simulation de lecteurs, inspection du schéma, exécution de la suite officielle et tests de résolution des locators finaux
- Statut : dernier diagnostic sectionnel provisoire de DIRECTION ; aucun patch du corpus avant lecture complète du périmètre et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et le rapport du bloc 9 ont été relus avant le présent bloc. Les constats repris directement sont F-DIR-006, F-DIR-007, F-DIR-008, F-DIR-010, F-DIR-018, F-DIR-027, F-DIR-028, F-DIR-031, F-DIR-032, F-DIR-033, F-DIR-034 et F-DIR-035.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 766–782 | Empêcher le jugement par ressemblance, conformité technique ou liste de recettes | Convention admise ; spécificité reliée au produit ; technique, direction et usage séparés ; listes non canoniques | Le critère de preuve U répète une méthode hors d’ACTION/SAVOIR |
| 786–792 | Préparer une clôture DIRECTION sans la posséder | `ACTION/CLOSE-EXIT-CHECK` explicitement unique ; registres séparés ; limites visibles | `limitations` est nommé au mauvais niveau de la projection structurée |
| 794–804 | Résumer les protections à lire en priorité | Responsabilités, modes, premier objet et prudence probatoire condensés | La prétendue entrée se trouve à la fin, n’est pas routée et simplifie plusieurs contrats avec pertes |
| 806–815 | Éviter de présenter la proportionnalité de lecture comme un gain mesuré | Audit exclu du coût de run ; méthode, périmètre et limite exigés pour tout claim de réduction | Les quatre catégories mélangent motif, recommandation et fait de lecture ; elles se chevauchent |
| 817 | Rappeler les propriétaires et la chaîne d’évolution | Ordre structurel cohérent pour une route BIBLIOTHEQUE ; aucun statut accordé par la chaîne seule | BIBLIOTHEQUE/EVOLUTION est imposé à toute route partagée, même non structurelle |

## Passage A — architecture visible

Le bloc termine DIRECTION par quatre fonctions différentes : invariants de jugement, préparation de la clôture, façade récapitulative et instrumentation de lecture. La clôture est correctement placée après les contenus détaillés. L’« entrée prioritaire », en revanche, est placée après cette clôture et après 793 lignes de détail, alors que son propre titre exige de la lire avant le détail.

La constitution mentionne bien l’entrée prioritaire comme vue dérivée de START, mais la carte de lecture canonique ne donne ni lien, ni locator, ni étape pour l’ouvrir. Un lecteur linéaire la découvre trop tard ; un lecteur outillé ne peut pas la résoudre ; seul un lecteur qui connaît déjà son existence peut rechercher son titre.

La section de lecture instrumentée est également présentée comme canonique pour BIBLIOTHEQUE. Pourtant son titre n’est pas une route stable, READING_MAP ne la liste pas, et le lecteur officiel ne la résout pas. Le problème d’accès est donc distinct de la qualité de la taxonomie elle-même.

La dernière phrase présente une chaîne unique pour les routes partagées ou candidates à promotion. Cette chaîne est saine pour une structure : START classe le blast radius, ACTION prépare la preuve et la migration, BIBLIOTHEQUE examine les usages et CHANGELOG persiste la décision autorisée. Elle devient architecturalement trop large lorsqu’elle s’applique à une règle de preuve ACTION, une heuristique SAVOIR ou une évolution de schéma qui ne possède aucune responsabilité structurelle.

## Passage B — contrat sémantique

### Convergence de genre ≠ slop

Le contrat est juste et important : une structure conventionnelle n’est pas disqualifiée par sa seule familiarité. Le jugement porte sur le contenu, la microcopie, les états, les données, la résolution et la spécificité réelle du produit.

La correction proposée en cas de détails interchangeables est également proportionnée. Elle cherche d’abord la spécificité dans le produit — contenu, donnée, relation, interaction ou hiérarchie — et n’ajoute un signal distinctif que s’il améliore une tâche, une compréhension, une preuve ou un positionnement. Le texte évite ainsi de remplacer le slop par une obligation de nouveauté décorative.

### PASS technique ≠ direction tenue

La séparation entre Gate A et direction est nette : l’absence de certaines fautes ne prouve ni goût, ni adéquation, ni direction. Pour une surface identitaire, l’ancre, la cible, la capture et les écarts nommés restent requis dans la branche nominale.

Le texte protège aussi contre quatre substitutions fréquentes :

- une capture n’est pas une preuve d’utilisabilité globale ;
- une lecture perceptuelle n’est pas une observation de tâche ;
- une conformité WCAG ne prouve pas l’usage global ;
- un avis externe ne vaut pas automatiquement preuve utilisateur.

Lorsque U domine, la preuve doit relier utilisateur, objectif, tâche, contexte et résultat observé. Ce critère est utile, mais il vit dans DIRECTION alors que la méthode et la preuve sont attribuées à SAVOIR et ACTION quelques lignes plus bas. Il renforce donc le besoin de résoudre F-DIR-032 et F-DIR-033 : DIRECTION doit déclencher la question sans créer une méthode concurrente ni rendre un participant obligatoire pour une question technique ou experte.

### Les listes ne sont pas un canon

La règle est conforme : références, designers, matières, outils et registres sont des amorces de jugement. Leur application mécanique recréerait précisément la convergence qu’ils doivent aider à dépasser. Aucun catalogue, score ou quota implicite n’est créé.

### Clôture de direction

La section corrige localement plusieurs ambiguïtés antérieures :

- `ACTION/CLOSE-EXIT-CHECK` est l’unique test de sortie ;
- DIRECTION prépare des éléments observables mais ne ferme pas le run ;
- état, issue, statut de direction et verdict restent séparés ;
- `N/A-JUSTIFIED` et `NOT-VERIFIED` ne sont pas interchangeables ;
- les principes, structures, migrations et décisions partagées restent chez leurs propriétaires.

Cette clôture est plus robuste que la table locale de la section 0 et doit prévaloir sur elle. Elle confirme que F-DIR-034 ne doit pas être corrigé par un nouveau minimum DIRECTION, mais par un renvoi sans perte vers ACTION.

Un chemin de champ reste faux. Pour une RUN_CARD structurée, DIRECTION nomme :

```text
closure.state
closure.issue
closure.direction_status
closure.verdict
limitations
creative_close
```

Le schéma et ACTION nomment en réalité `closure.limitations`. La racine de `run_card` interdit les propriétés supplémentaires et ne contient aucune propriété `limitations`. Une implémentation littérale de la phrase produit donc une projection invalide.

La branche d’ancrage reste ambivalente. La phrase exige encore une « ancre utile », puis autorise génériquement une non-applicabilité réelle. Elle ne dit pas explicitement si cette branche peut concerner l’ancre d’une surface identitaire. Le résumé suivant remplace même l’ancre fraîche et inspectable par un ancrage « observable ou explicitement limité ». Ces formulations rendent la limite visible, mais ne réconcilient pas ABSOLU 2, SAVOIR et le schéma ; F-DIR-027 demeure ouvert.

### Entrée prioritaire

L’entrée résume correctement plusieurs protections : rôle des cinq propriétaires, classification générale, premier objet et prudence face aux preuves de substitution. Elle déclare aussi explicitement qu’elle n’est ni une nouvelle source, ni un gate, ni un schéma.

Sa position et sa fidélité posent toutefois problème.

Premièrement, la section est située après la clôture, n’apparaît pas dans le chemin canonique de lecture et ne possède aucun locator résolvable. Sa fonction d’entrée dépend donc d’une connaissance préalable du document.

Deuxièmement, son résumé des absolus demande avant l’action : mode, scope, capacité, preuve, limite et prochaine action. ABSOLU 4 demande : mode, décision dominante, risque principal, preuve minimale et condition d’arrêt, avec contraintes de coût lorsque déterminantes. L’entrée ajoute trois notions et en retire trois autres, dont décision et risque. Cette perte renforce F-DIR-008 et F-DIR-010.

Troisièmement, « avant l’action » répète l’ambiguïté temporelle de F-DIR-031. L’intake, la clarification et l’inspection nécessaires au classement doivent rester possibles avant une déclaration complète.

Quatrièmement, la synthèse de routage améliore START en interdisant LITE sous risque critique, mais elle reste une vue humaine. Le schéma et le validateur ne protègent toujours pas ce classement ; F-DIR-007 n’est donc pas résolu.

Cinquièmement, la formule `PROMESSE → OBJET DE PREUVE → GESTE` est à nouveau placée avant « les bénéfices, la navigation ou le polish » sans qualifier les cas où navigation, relation entre cartes ou bénéfice structuré constituent eux-mêmes l’objet de preuve. Elle renforce F-DIR-018.

Enfin, l’interdiction de renseigner `DECISION-CHANGE` avant observation est saine. Elle aligne le résumé sur START et évite que l’exécution du protocole soit déclarée comme changement réel.

### Lecture instrumentée

L’intention est excellente : la proportionnalité de lecture reste une hypothèse nominale, pas une preuve de gain. Un audit ne doit pas gonfler artificiellement le coût déclaré d’un run, et toute affirmation de réduction doit indiquer méthode, périmètre et limite.

Les quatre catégories ne forment cependant pas une partition exploitable :

| Lecture réelle | Étiquettes simultanément vraies |
|---|---|
| START recommandé puis effectivement lu au démarrage | `STARTUP-NOMINAL` + `ACTUAL-READ` |
| CRAFT ouvert parce que le risque peut changer la décision | `CONDITIONAL-READ` + `ACTUAL-READ` |
| DIRECTION ouvert pendant le présent audit | `AUDIT-READ` + lecture effectivement réalisée |

`STARTUP-NOMINAL` décrit une recommandation ou une phase, `CONDITIONAL-READ` et `AUDIT-READ` décrivent un motif, tandis que `ACTUAL-READ` décrit un fait. La phrase « la catégorie applicable », au singulier, ne dit ni s’il faut enregistrer plusieurs étiquettes, ni laquelle prévaut.

Dans BIBLIOTHEQUE, la contradiction devient encore plus visible : le lecteur doit déclarer la nature de chaque route « effectivement lue », puis choisir parmi trois motifs et `ACTUAL-READ`. Si toutes les lignes consignées sont déjà effectives, `ACTUAL-READ` est soit tautologique, soit concurrent des motifs nécessaires à l’analyse.

Une instrumentation robuste doit séparer au minimum :

- le fait : recommandé, ouvert, lu, partiellement lu ;
- le motif : démarrage nominal, condition du run, audit ;
- le contexte de mesure : run ou audit ;
- éventuellement l’unité et le périmètre si un gain de charge est étudié.

Ce constat n’exige pas nécessairement de nouveaux champs RUN_CARD. Il exige une taxonomie non ambiguë dans la trace et une règle de comptage.

### Règle de passage et promotion

Le rappel des propriétaires est cohérent avec la constitution. La chaîne finale est également correcte pour une route structurelle candidate :

```text
DIRECTION/START
→ ACTION/RUN-SYSTEM
→ BIBLIOTHEQUE/EVOLUTION
→ CHANGELOG
```

BIBLIOTHEQUE décrit précisément cette chaîne et CHANGELOG conserve le cycle de vie. ACTION demande en outre de consulter CHANGELOG avant adoption, pilotage ou dépréciation ; cette consultation d’état n’empêche pas CHANGELOG de persister la décision autorisée en fin de chaîne.

Le problème vient du quantificateur « une route partagée ou candidate à la promotion ». READING_MAP limite BIBLIOTHEQUE/EVOLUTION au cas où la règle durable concerne une structure. DIRECTION et BIBLIOTHEQUE possèdent pourtant des responsabilités exclusives : une méthode de preuve ACTION, une règle de jugement SAVOIR ou une évolution de schéma ne devient pas structurelle parce qu’elle est partagée. La chaîne finale doit donc router vers BIBLIOTHEQUE/EVOLUTION seulement si la responsabilité structurelle est active ; sinon, source propriétaire + preuve adaptée + CHANGELOG suffisent.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle complète

`validate_all.py` passe, y compris contrôles documentaires, schémas, contrats, distributions et reproductibilité.

Ce résultat confirme l’intégrité de la baseline. Il ne détecte ni le locator non enregistré, ni le chevauchement sémantique des catégories, ni le chemin `limitations` erroné dans la prose.

### Test 1 — locators propriétaires de clôture et d’évolution

Résultats :

```text
ACTION/CLOSE-EXIT-CHECK   PASS
BIBLIOTHEQUE/EVOLUTION   PASS
```

Les routes propriétaires invoquées par la clôture et la chaîne structurelle sont donc accessibles par le lecteur officiel.

### Test 2 — locator canonique de lecture instrumentée

Le renvoi utilisé par BIBLIOTHEQUE a été exécuté tel qu’il est écrit :

```text
DIRECTION/lecture instrumentée
```

Résultat :

```text
ROUTE READ FAILED — locator inconnu
```

Le titre existe, mais le lecteur ne le résout pas. La façade prioritaire échoue de la même manière avec `DIRECTION/Entrée prioritaire`.

### Test 3 — structure de la clôture JSON

Inspection du schéma :

```text
run_card.additionalProperties = false
run_card.closure.properties =
  direction_status, issue, limitations, state, verdict
run_card.properties ne contient pas limitations
```

Le chemin valide est donc `run_card.closure.limitations`. La formulation DIRECTION `limitations` ne peut pas être interprétée comme un champ racine valide.

### Test 4 — angle mort des validateurs

Après l’échec des deux locators finaux, la suite officielle et `validate_reading_map.py` restent vertes. Comme au bloc 9, le validateur contrôle la table fermée des locators déclarés, pas tous les renvois normatifs ou quasi-locators réellement écrits dans le corpus.

## Passage C — usage simulé

### Structure conventionnelle mais spécifique

Le designer conserve une structure familière, puis améliore contenu, données, relations, états et détail. Le bloc résiste correctement à la recherche artificielle d’originalité.

### Gate A réussi, direction faible

Le contrôle technique passe, mais la surface identitaire reste générique. Le lecteur ne peut pas fermer sur ce seul PASS : il doit confronter cible, capture, ancre et écarts. Le comportement attendu est robuste.

### Screenshot conforme présenté comme preuve d’usage

Le bloc refuse l’inférence. Si U domine, la preuve doit revenir à une tâche, un contexte et un résultat observé, avec la méthode et les limites possédées par ACTION/SAVOIR.

### Clôture DIRECTION structurée

Le lecteur suit correctement `ACTION/CLOSE-EXIT-CHECK`, sépare state, issue, direction status, verdict et creative close. S’il sérialise littéralement `limitations` au niveau racine comme le suggère DIRECTION, le schéma doit rejeter la propriété inconnue. Le bon chemin doit être recherché dans ACTION ou le schéma.

### Nouveau lecteur sous contrainte de temps

Le lecteur commence en haut du document, suit START et les chemins courts, puis découvre l’« entrée prioritaire » seulement après la clôture. La façade ne remplit pas son rôle d’entrée. S’il utilise le lecteur de routes pour l’ouvrir directement, il échoue.

### Run instrumenté

START est recommandé et effectivement lu ; CRAFT est conditionnel et effectivement lu. Une catégorie unique fait perdre soit la raison, soit la réalité de la lecture. Plusieurs catégories sauvent l’information, mais aucun ordre de priorité ni règle de comptage n’est défini.

### Route structurelle partagée

Un composant ou gabarit partagé suit correctement START, RUN-SYSTEM, EVOLUTION et CHANGELOG. Consumers, compatibilité, migration, rollback, usages contrastés et maintenance sont examinés.

### Règle de preuve ACTION candidate à adoption

La chaîne finale envoie aussi cette règle vers BIBLIOTHEQUE/EVOLUTION, dont les critères portent sur structure, premier objet et non-homogénéisation. Le détour est sans propriétaire légitime. ACTION, le schéma éventuel et CHANGELOG sont les sources concernées ; BIBLIOTHEQUE n’est requis que si une structure change.

## Passage D — constats

### F-DIR-043 — l’« entrée prioritaire » n’est pas architecturalement une entrée

- Gravité provisoire : **Observation à risque**
- État : **contradiction architecturale confirmée**
- Preuve : section située lignes 794–804, après la clôture ; aucune étape de la carte canonique ne l’ouvre ; `read_route.py` rejette `DIRECTION/Entrée prioritaire`
- Risque : résumé découvert trop tard, duplication ignorée, ou dépendance à une connaissance préalable du document
- Facteur atténuant : la constitution la nomme comme vue dérivée et START reste la source normative ; le lecteur peut rechercher manuellement le titre
- Propriétaire pressenti : DIRECTION pour la place et le statut de la façade ; READING_MAP/lecteur seulement si un locator stable est réellement voulu
- Test futur : lecteur linéaire novice, lecteur par carte et agent utilisant uniquement `read_route.py`

### F-DIR-044 — les catégories de lecture mélangent des axes non exclusifs

- Gravité provisoire : **Significatif**
- État : **ambiguïté taxonomique confirmée dans DIRECTION et BIBLIOTHEQUE**
- Preuve : `STARTUP-NOMINAL` décrit une recommandation/phase, `CONDITIONAL-READ` et `AUDIT-READ` un motif, `ACTUAL-READ` un fait ; une même lecture satisfait plusieurs catégories
- Risque : double comptage, perte du motif, comparaison de runs impossible, claim de réduction fondé sur des unités différentes
- Facteur atténuant : le texte interdit déjà de présenter la proportionnalité comme un gain mesuré et exige méthode, périmètre et limite
- Propriétaire pressenti : DIRECTION pour la taxonomie de lecture ; la trace ou l’instrumentation de pilote pour le transport
- Test futur : route recommandée et lue, route conditionnelle et lue, route auditée, lecture partielle, fichier ouvert sans lecture utile et comparaison run/audit

### F-DIR-045 — la clôture structurée référence `limitations` au mauvais niveau

- Gravité provisoire : **Significatif**
- État : **divergence humain/machine confirmée**
- Preuve : lignes 658 et 788 nomment `limitations` avec des chemins structurés ; ACTION et le schéma imposent `closure.limitations`; `run_card.additionalProperties` vaut `false`
- Risque : RUN_CARD invalide, limite perdue ou correction manuelle obligatoire par un lecteur qui connaît déjà le schéma
- Facteur atténuant : le renvoi vers `ACTION/CLOSE-PACKAGE` permet de retrouver le chemin exact
- Propriétaires pressentis : ACTION et le schéma pour la structure ; DIRECTION pour corriger sa projection
- Test futur : `DECIDED`, `CLOSED`, issue nulle, réserve, plusieurs limitations et creative close DIRECTION

### F-DIR-046 — la chaîne de promotion force BIBLIOTHEQUE sur des routes non structurelles

- Gravité provisoire : **Significatif**
- État : **contradiction d’ownership confirmée**
- Preuve : ligne 817 vise toute route partagée ou candidate ; ligne 790 réserve BIBLIOTHEQUE aux structures ; READING_MAP n’ajoute `BIBLIOTHEQUE/EVOLUTION` que « si structure »
- Risque : méthode de preuve, règle de jugement ou évolution de schéma évaluée avec des critères structurels ; propriétaire réel contourné ; gouvernance inutilement lourde
- Facteur atténuant : BIBLIOTHEQUE/EVOLUTION est correct pour les composants, gabarits, scènes et autres responsabilités structurelles
- Propriétaires pressentis : source normative concernée pour la règle ; ACTION pour la preuve ; BIBLIOTHEQUE seulement si structure ; CHANGELOG pour le cycle de vie autorisé
- Test futur : composant partagé, token, heuristique CRAFT, gate ACTION, champ RUN_CARD, règle de migration et alias documentaire

### Mise à jour de F-DIR-006 — mapping humain / trace / projection

La clôture finale confirme la séparation des registres, mais emploie un chemin de limite non conforme. La taxonomie de lecture doit vivre dans une trace sans mapping défini. F-DIR-045 isole le chemin erroné ; F-DIR-006 reste le problème transversal de projections humaines non explicitement mappées.

### Mise à jour de F-DIR-007 — correctif critique local

L’entrée prioritaire ajoute enfin « delta local sans risque critique » à LITE. Cette protection corrige la façade humaine finale, mais ni les premières tables ni le contrat machine ne l’imposent. F-DIR-007 reste **Majeur confirmé** jusqu’à réconciliation de toutes les vues et protections machine applicables.

### Mise à jour de F-DIR-008 — invariants de responsabilité

Le résumé des absolus omet décision, risque, owner et condition de sortie alors que ces informations sont exigées ailleurs ; il ajoute scope, capacité, limite et prochaine action. La clôture, elle, rend les propriétaires plus nets. F-DIR-008 reste **Significatif confirmé**.

### Mise à jour de F-DIR-010 — vues minimales concurrentes

L’entrée prioritaire se déclare dérivée, mais reformule encore le paquet pré-action avec une sélection différente de champs. Son disclaimer de priorité normative limite le dommage sans rendre les pertes explicites. F-DIR-010 reste **Significatif confirmé**.

### Mise à jour de F-DIR-018 — priorité du premier objet

La façade finale répète que promesse, objet de preuve et geste précèdent bénéfices, navigation et polish sans qualifier les cas où ces formes constituent l’objet de preuve. F-DIR-018 reste ouvert.

### Mise à jour de F-DIR-027 — ancrage humain et machine

La clôture reconnaît `N/A-JUSTIFIED` de manière générale et le résumé accepte un ancrage « explicitement limité », mais ni l’une ni l’autre ne dit clairement si l’ancre elle-même peut être non applicable sur une surface identitaire. La tension avec ABSOLU 2, SAVOIR et la liste d’ancres requise demeure. F-DIR-027 reste **Majeur provisoire** jusqu’à l’audit complet des propriétaires et du contrat machine.

### Mise à jour de F-DIR-028 — couverture du lecteur de routes

Le renvoi canonique de BIBLIOTHEQUE vers `DIRECTION/lecture instrumentée` est rejeté par `read_route.py`, comme l’entrée prioritaire. La suite officielle passe malgré ces échecs. F-DIR-028 reste **Significatif confirmé** et sa portée inclut désormais aussi une section DIRECTION transversale, pas seulement les routes SAVOIR.

### Mise à jour de F-DIR-031 — déclaration avant action

L’entrée prioritaire répète « avant l’action » sans réserver l’intake, la clarification ou l’inspection nécessaire au classement. L’intention reste interprétable comme « avant production, vérification ou persistance », mais cette borne n’est pas écrite. F-DIR-031 demeure **Significatif**.

### Mise à jour de F-DIR-032 et F-DIR-033 — méthode et taxonomie de preuve

L’invariant d’utilisabilité relie correctement utilisateur, objectif, tâche, contexte et résultat, mais ajoute encore une formulation de méthode dans DIRECTION. Il ne mappe pas cette question vers les familles de méthode, axes et gates d’ACTION. Les deux constats restent ouverts ; la séparation de propriétaires aux lignes 790–792 fournit toutefois la règle de correction.

### Mise à jour de F-DIR-034 — minimum de preuve local

La clôture finale renvoie sans ambiguïté à l’unique `ACTION/CLOSE-EXIT-CHECK`. Elle fournit la meilleure règle locale et montre que la table de preuve minimale de la section 0 ne doit pas être interprétée comme un second contrat de sortie. F-DIR-034 reste confirmé jusqu’à suppression de la perte dans la façade antérieure.

### Mise à jour de F-DIR-035 — fidélité et clôture

Le dernier bloc sépare correctement state, issue, direction status, verdict, limitations et creative close, et interdit à DIRECTION de fermer le run. Il corrige conceptuellement la condition d’arrêt antérieure, mais F-DIR-045 révèle un chemin machine faux. F-DIR-035 reste **Significatif**, avec une base de correction claire : projection fidèle d’ACTION plutôt que logique locale.

## Éléments conformes à préserver

1. Une structure conventionnelle n’est pas du slop par sa seule familiarité.
2. La spécificité est cherchée d’abord dans le produit réel.
3. Un signal distinctif doit améliorer tâche, compréhension, preuve ou positionnement.
4. Gate A ne prouve ni direction, ni goût, ni adéquation produit.
5. Capture, WCAG, lecture perceptuelle et avis externe ne prouvent pas seuls l’utilisabilité globale.
6. Les listes sont des amorces de jugement, jamais un canon.
7. `ACTION/CLOSE-EXIT-CHECK` reste l’unique test de sortie.
8. DIRECTION prépare la clôture mais ne la possède pas.
9. State, issue, direction status et verdict restent séparés.
10. `N/A-JUSTIFIED` et `NOT-VERIFIED` gardent des sens distincts.
11. Les frontières ACTION/SAVOIR/BIBLIOTHEQUE/CHANGELOG sont explicitement rappelées.
12. `DECISION-CHANGE` reste vide jusqu’à une observation réelle.
13. Une validation de package ou une rationale n’est pas automatiquement une preuve d’usage, d’accessibilité, de performance ou de qualité visuelle.
14. La proportionnalité de lecture n’est pas présentée comme un gain mesuré.
15. Toute affirmation de réduction doit préciser méthode, périmètre et limite.
16. Une chaîne de promotion n’accorde aucun statut par sa seule exécution.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Position des sections, routes, façade finale et chaîne de promotion examinées |
| B — Contrats | FULL | Chaque phrase normative du bloc comparée aux propriétaires et projections |
| C — Usage | TARGETED | Convention, PASS technique, preuve U, clôture, lecteur pressé, instrumentation et promotion simulés |
| D — Résistance | FULL | Quatre nouveaux constats et douze mises à jour enregistrés |
| Contrôles machine | FULL ciblé | Suite officielle, locators finaux et structure de clôture inspectés |

## Point de passage

La lecture sectionnelle de `DIRECTION.md` est maintenant complète, de la constitution à la règle de passage finale. Cela ne constitue pas un verdict global sur DIRECTION ni sur le système : le protocole exige la lecture complète du périmètre avant diagnostic final.

Avant d’ouvrir `ACTION.md`, le prochain pas prudent est un **checkpoint de consolidation DIRECTION** : vérifier la continuité des dix rapports, dédupliquer les 46 constats, construire le registre provisoire des dépendances vers ACTION/SAVOIR/BIBLIOTHEQUE/CHANGELOG et marquer ce qui ne peut être confirmé ou reclassé qu’après lecture de son propriétaire. Aucun défaut ne sera corrigé à ce stade.
