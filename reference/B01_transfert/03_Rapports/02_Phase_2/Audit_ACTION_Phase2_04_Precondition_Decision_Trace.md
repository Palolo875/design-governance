# DG-AUDIT-001 — Phase 2 — ACTION, bloc 4

## Périmètre examiné

- Cible : `V1/official/ACTION.md`
- Bloc : lignes 190–240 de la reconstruction de travail
- Section : `ACTION/PRECONDITION` — mode, capacité et preuve ; contrat minimal par mode ; décision et preuve ; trace post-build d’`EXTERNAL-START` ; raccord `DESIGN-ATLAS`
- Interfaces vérifiées : `DIRECTION/START`, `DIRECTION/EXTERNAL-START`, `SAVOIR/DESIGN-ATLAS`, `ACTION/STATUS`, `ACTION/FAST-PATH`, `ACTION/RUN_CARD`, routes de lecture, schéma `run_card.schema.json`, validateur `validate_run_card.py`, exemples et fixtures
- Source d’observation : compilation `Design_Governance_V1.0.md`, reconstruction de travail et baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, lecture phrase par phrase, comparaison amont/aval, résolution des locators, inspection de la projection machine et mutations négatives ciblées
- Statut : diagnostic sectionnel provisoire ; aucun verdict global sur ACTION et aucun patch du corpus

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole, le plan maître et le rapport ACTION bloc 3 ont été relus. Les constats transportés en priorité sont F-ACT-001, 002, 005, 007, 009 et 012, ainsi que F-DIR-003, 006, 011, 015, 017, 019, 029 et 035.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 190–202 | Séparer classification, capacités et preuve ; fixer un contrat par mode | Le mode dépend de la tâche et du blast radius, jamais de la capacité disponible ; les cinq modes ont une profondeur distincte | La table appelée `PRECONDITION` mélange éléments de lancement, d’exécution et de clôture ; le minimum SYSTÈME n’est pas transporté par RUN_CARD |
| 204–218 | Distinguer intention initiale et conséquence observée | `DECISION-INTENT` existe au lancement ; aucun changement n’est déclaré avant observation | `DECISION-CHANGE` reste optionnel et non typé dans la projection ; le fallback N/A générique reste plus large que la distinction détaillée ultérieure |
| 220–230 | Mesurer la conséquence d’EXTERNAL-START après le build | La vue de démarrage n’est ni un gate ni un statut ; elle doit produire une conséquence ou s’arrêter | `OMISSION-AVOIDED` et `REMAINING-LIMIT` n’ont aucun transport structuré ; `NOT-OBSERVED` reste un token de trace |
| 232–238 | Raccorder DESIGN-ATLAS à la décision réelle | Les champs avant build sont explicitement des hypothèses ; seul l’observé peut nourrir décision et verdict ; une absence de famille est valide | Le champ pré-build `DECISION-MODIFIED` porte un nom rétrospectif ; les locators ACTION, DIRECTION et SAVOIR appelés ne sont pas résolubles |

## Passage A — architecture visible

Le bloc construit une frontière saine entre trois responsabilités :

1. `DIRECTION/START` classe le mode à partir de la tâche, du risque et du blast radius ;
2. les capacités disponibles déterminent la méthode et la force de la preuve réellement accessible ;
3. ACTION décide si le run peut être livré, retourné, réservé ou escaladé.

Cette architecture empêche un contournement courant : transformer une tâche DIRECTION en STANDARD ou ITER parce que l’agent ne possède ni navigateur, ni capture, ni regard externe. La capacité réduit le claim atteignable, jamais la responsabilité initiale.

La section s’appelle `PRECONDITION`, mais sa table ne contient pas uniquement des préconditions. Elle mélange :

- éléments présents avant le build : intention, JTBD, risque, direction retrouvable, décision, owner ;
- éléments produits pendant le run : build, comparaison, migration, rollback ;
- éléments disponibles après observation : capture, statut de direction, V/U/A/T, non-régression, entrée CHANGELOG, réserve ou prochaine action.

Le lecteur peut comprendre « contrat ACTION minimal sur l’ensemble du run », mais le titre peut aussi lui faire exiger une capture ou un statut de direction avant de commencer. Cette tension est documentée sans nouveau constat autonome pour l’instant ; elle sera rejouée avec les routes RUN et CLOSE-PACKAGE.

Les trois locators nommés par le bloc échouent dans le lecteur officiel :

```text
ACTION/PRECONDITION       FAIL
DIRECTION/EXTERNAL-START FAIL
SAVOIR/DESIGN-ATLAS      FAIL
```

Les sections existent et peuvent être trouvées manuellement. `ACTION/RUN-DIRECTION` et `ACTION/RUN-SYSTEM` passent. Le défaut est donc une omission ciblée de READING_MAP, déjà couverte par F-ACT-001 et F-DIR-028.

## Passage B — contrat sémantique

### Mode, capacité et possibilité de livrer

La première phrase est un invariant à préserver. Le type de tâche et le blast radius classent le mode ; la capacité choisit la voie de preuve, le statut de vérification et la possibilité de livrer. Elle ne réécrit pas silencieusement la nature de la tâche.

Cette séparation produit quatre comportements corrects :

- une tâche DIRECTION sans capture reste DIRECTION ;
- une capacité manquante produit une limite ou `NOT-VERIFIED`, pas un PASS simulé ;
- la preuve peut être dégradée sans que le risque déclaré disparaisse ;
- le run peut être retourné ou escaladé lorsque la capacité empêche une conclusion nécessaire.

Le contrat prolonge donc correctement le bloc UI/UX et atténue F-DIR-037 : la capacité positive n’est pas confondue avec l’outillage disponible.

### Contrat minimal des cinq modes

La table proportionne raisonnablement l’effort :

- LITE protège le delta, les gates A applicables, le risque dominant et les axes touchés ;
- ITER ajoute direction retrouvable, diff et non-régression ;
- STANDARD exige JTBD, arbitrage, composition et états, sans imposer ancre ou asset par défaut ;
- DIRECTION active alternative située si utile, ancre, cible, build, capture, comparaison, gates, fidélité et axes ;
- SYSTÈME exige impact, consumers, owner, migration, rollback, non-régression et CHANGELOG.

La proportion est bonne. Elle évite de traiter un fix local comme une campagne de direction et empêche aussi une décision partagée d’être réduite à une correction visuelle.

Deux raccords restent ouverts.

Premièrement, Gate C est absent de la ligne LITE, alors que la section canonique GATE-C précise qu’il est `N/A-JUSTIFIED` lorsque le craft n’est pas concerné — ce qui implique qu’il peut devenir applicable à la zone touchée lorsque le craft constitue précisément le risque. RUN-LITE n’appelle que les gates A applicables et une preuve B du risque dominant. Il faudra déterminer si un delta visuel de craft reste LITE avec contrôle C ciblé ou s’il doit toujours devenir ITER ; aucune règle explicite ne tranche encore ce cas.

Deuxièmement, le contrat SYSTÈME est riche dans la prose mais presque absent de la projection machine. Le schéma ne contient aucun champ dédié pour consumers, migration, rollback, non-régression ou entrée CHANGELOG. Un `trace_locator` peut pointer vers ces informations, mais la RUN_CARD valide ne garantit ni leur présence ni leur retrouvabilité.

### `N/A-JUSTIFIED`, `NOT-VERIFIED` et `NOT-OBSERVED`

Le bloc établit enfin une distinction opérationnelle claire :

- `N/A-JUSTIFIED` : contrôle, conséquence ou décision réellement non applicable dans le scope ;
- `NOT-VERIFIED` : propriété ou preuve nécessaire impossible à vérifier avec les capacités disponibles ;
- `NOT-OBSERVED` : conséquence attendue mais absente de l’observation déclarée.

Les lignes 230 et 236 corrigent une partie importante de F-DIR-011 et F-DIR-019. Une absence d’effet attendu ne doit plus être déguisée en non-applicabilité. La définition est également cohérente avec le GLOSSAIRE.

La phrase générique de la ligne 218 reste toutefois moins précise : « si aucune décision ne change », elle propose `N/A-JUSTIFIED` lorsque cela est justifié, sans nommer `NOT-OBSERVED` ni `NOT-VERIFIED`. La restriction « lorsque cela est justifié » empêche d’en faire une règle automatique, mais un lecteur qui s’arrête à ce contrat général ne reçoit pas encore l’arbre complet fourni quelques lignes plus loin.

### DECISION-INTENT et DECISION-CHANGE

La temporalité humaine est saine :

```text
lancement       → DECISION-INTENT
observation     → conséquence réelle
après preuve    → DECISION-CHANGE ou sortie justifiée
```

`DECISION-CHANGE` couvre trois résultats : décision modifiée, confirmée ou abandonnée. Le mot « change » est donc un nom de champ historique plus large que son sens littéral. Cette largeur reste compréhensible en prose, mais elle devient fragile pour une machine : modifier, confirmer et abandonner produisent des conséquences différentes et ne devraient pas être indistinguables dans une instrumentation.

Le schéma rend `decision_intent` obligatoire pour toute RUN_CARD, ce qui respecte le lancement. Il rend `decision_change` optionnel et lui donne seulement deux chaînes libres : `value` et `evidence`. Aucun champ ne qualifie le résultat comme `changed`, `confirmed`, `abandoned`, `not_applicable` ou `not_observed`.

Le validateur impose un `decision_change` seulement à une DIRECTION `CLOSED` acceptée sans issue. Un STANDARD ou un SYSTÈME `CLOSED + ACCEPTED` peut l’omettre. Une valeur arbitraire est également valide. L’ajout d’un `outcome_type` structuré est rejeté comme propriété inconnue.

On peut inscrire `N/A-JUSTIFIED` dans `decision_change.value`, avec une raison dans `evidence`, et la carte passe. Ce mécanisme permet un transport textuel minimal, mais il ne rend pas la catégorie inspectable ni vérifiable. La projection ne peut pas distinguer un vrai changement, une confirmation, un abandon et une absence justifiée sans interpréter librement le texte.

### Trace post-build d’EXTERNAL-START

La trace demandée est bien placée après le premier artefact ou la première capture. Elle ne tente pas de prouver à l’avance que la vue de démarrage a été utile. Elle demande :

- ce qui a réellement changé, été confirmé ou abandonné ;
- quelle omission concrète a été évitée ;
- quelle limite demeure.

Cette architecture réduit le risque d’un préflight cérémoniel. Si la vue ne produit aucune conséquence, elle doit être arrêtée ou classée correctement au lieu d’être valorisée par sa seule complétude.

`OMISSION-AVOIDED` exige néanmoins une lecture prudente. Il s’agit d’une trace causale située, pas d’une preuve expérimentale que l’omission se serait nécessairement produite sans le module. La formulation « omission concrète évitée » est acceptable si elle cite la décision ou l’élément ajouté/retiré ; elle deviendrait un claim exagéré si elle était agrégée comme impact causal sans comparaison.

Ces champs sont volontairement conservés dans la trace existante. Le schéma RUN_CARD rejette `omission_avoided` et `remaining_limit` comme propriétés inconnues. Cela ne constitue pas en soi une contradiction, puisque `trace_locator` peut pointer vers une trace plus riche. Mais aucune convention contrôlable ne garantit leur forme ou leur présence.

### Raccord DESIGN-ATLAS

Le raccord corrige une confusion fréquente entre présélection et résultat. Avant le build :

```text
DECISION-MODIFIED
WHEN-USEFUL
COUNTERINDICATION
MEDIUM-SCOPE
PROOF-LIMIT
```

sont explicitement des hypothèses de sélection. Une cible, une ancre, une rationale, une référence, un asset ou un composant ne prouvent rien par leur seule existence.

Après observation, le vocabulaire revient à ACTION : `DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`. Le polish visuel soutient seulement une preuve perceptuelle ; il ne devient pas preuve d’usage, d’accessibilité, de performance ou d’efficacité. Cette frontière est robuste et doit être préservée.

Le nom `DECISION-MODIFIED` reste trompeur pour un champ pré-build qui signifie « décision que la famille pourrait modifier ». ACTION neutralise explicitement le risque en l’appelant hypothèse, mais la forme grammaticale peut pousser un consommateur à le lire comme résultat acquis. Comme le propriétaire réel est SAVOIR/DESIGN-ATLAS, la disposition est différée à la lecture de SAVOIR plutôt que d’ouvrir ici un constat ACTION autonome.

La dernière phrase est une bonne règle anti-slop : variante, asset, détail ou rationale ne sont conservés que si leur conséquence sur l’artefact, la preuve, la limite ou la prochaine action est identifiable. Elle ne transforme pas l’absence de famille ou d’effet en défaut automatique.

## Interface machine et contrôles ciblés

### Contrôle 0 — baseline et suite officielle

Les empreintes B01 sont inchangées. La suite officielle complète reste verte avant modification du corpus. Ce PASS démontre la conformité aux contrôles actuels, non la couverture des divergences décrites ici.

### Test 1 — routes appelées

```text
ACTION/PRECONDITION        FAIL — locator inconnu
DIRECTION/EXTERNAL-START  FAIL — locator inconnu
SAVOIR/DESIGN-ATLAS       FAIL — locator inconnu
ACTION/RUN-DIRECTION      PASS
ACTION/RUN-SYSTEM         PASS
```

Les interfaces conceptuelles principales du bloc ne sont donc pas directement activables par le lecteur officiel.

### Test 2 — présence et typage de DECISION-CHANGE

À partir de l’exemple RUN_CARD :

```text
DIRECTION CLOSED ACCEPTED sans decision_change   REJECTED
DIRECTION decision_change = N/A-JUSTIFIED         ACCEPTED
DIRECTION decision_change = NOT-OBSERVED          ACCEPTED
DIRECTION decision_change = VALEUR-ARBITRAIRE     ACCEPTED
STANDARD CLOSED ACCEPTED sans decision_change     ACCEPTED
SYSTÈME CLOSED ACCEPTED sans decision_change      ACCEPTED
decision_change avec outcome_type structuré       REJECTED
```

Le contrôle DIRECTION est utile mais localisé. Le contenu du résultat n’est pas typé et le contrat générique n’est pas appliqué aux autres modes.

### Test 3 — transport d’EXTERNAL-START

Mutation : ajout direct de `omission_avoided` et `remaining_limit` dans la RUN_CARD.

Résultat : rejet comme champs inconnus.

La seule voie conforme est donc la trace externe référencée par `trace_locator` ou une reformulation dans des champs génériques. Aucune structure canonique de cette trace n’est validée.

### Test 4 — minimum SYSTÈME

Une carte `mode: SYSTÈME`, `state: CLOSED`, `verdict: ACCEPTED`, sans consumers, migration, rollback, non-régression, entrée CHANGELOG ni `decision_change`, est acceptée dès lors que les champs génériques et la preuve minimale du validateur sont présents.

Le validateur confirme une projection générale, mais ne contrôle pas le contrat ACTION minimal du mode le plus exposé au blast radius partagé.

## Passage C — usages simulés

### DIRECTION sans capture réelle

Le mode reste DIRECTION. La capture et le jugement perceptuel deviennent `NOT-VERIFIED`; le run reçoit une limite et une prochaine preuve ou une issue adaptée. Le contrat empêche correctement la rétrogradation silencieuse.

### Contrôle réellement hors périmètre

Une surface statique ne comporte aucun comportement motion et aucune décision ne dépend de ce médium. Le contrôle peut être `N/A-JUSTIFIED` avec la justification. Il ne faut ni produire une animation artificielle ni écrire `NOT-VERIFIED` pour un contrôle inexistant.

### Conséquence attendue mais absente

DESIGN-ATLAS a été chargé parce qu’une famille devait améliorer la relation preuve/action. Après observation, aucune différence perceptible n’apparaît. La sortie correcte est `NOT-OBSERVED`, pas `N/A-JUSTIFIED`, puisque la conséquence était applicable et attendue.

### Preuve impossible à exécuter

La conséquence pourrait modifier la décision, mais aucun runtime ou support d’observation n’est disponible. La sortie correcte est `NOT-VERIFIED` avec `NEXT-PROOF`, et non `NOT-OBSERVED`, car l’absence de résultat n’a pas été réellement observée.

### Décision confirmée

Une comparaison conserve l’option initiale parce qu’elle résout mieux le risque. La trace peut employer DECISION-CHANGE pour la confirmation, mais la projection ne distingue pas cette confirmation d’une modification de l’artefact. Une métrique « décisions changées » compterait donc potentiellement les deux.

### EXTERNAL-START sans conséquence

Le préflight n’a modifié aucun artefact, claim, risque, preuve ou limite. S’il n’était pas applicable, `N/A-JUSTIFIED` est correct. S’il était applicable mais sans effet visible, `NOT-OBSERVED` est correct. Le bloc évite ainsi de transformer l’exécution du module en preuve de sa valeur.

### SYSTÈME partagé

Un composant affecte plusieurs consumers. La prose exige impact, owner, migration, rollback, non-régression et CHANGELOG. Une RUN_CARD acceptée peut pourtant ne contenir aucun de ces éléments et seulement pointer vers une trace libre. Un pipeline automatique ne peut pas déterminer si le minimum SYSTÈME a été respecté.

## Passage D — constats

### F-ACT-013 — la conséquence décisionnelle est optionnelle et non typée dans la projection machine

- Gravité provisoire : **Significatif**
- État : **divergence humain/machine confirmée**
- Preuve : lignes 206–218 établissent le contrat DECISION-INTENT → observation → DECISION-CHANGE ou sortie justifiée ; le schéma rend `decision_change` optionnel et limite sa structure à deux chaînes libres ; le validateur ne l’exige que pour une DIRECTION clôturée et acceptée sans issue
- Comportement observable : STANDARD et SYSTÈME peuvent être clôturés et acceptés sans conséquence décisionnelle ; une valeur arbitraire, `N/A-JUSTIFIED` ou `NOT-OBSERVED` passe de la même manière ; un `outcome_type` structuré est rejeté
- Risque : modification, confirmation, abandon, non-applicabilité et absence d’effet impossibles à distinguer automatiquement ; audit et métriques de conséquence peu fiables ; clôture acceptée sans résultat décisionnel retrouvé
- Facteur atténuant : `value` et `evidence` permettent une trace textuelle ; `trace_locator` peut pointer vers une trace plus riche ; DIRECTION possède déjà un garde-fou partiel
- Relations : F-DIR-003, F-DIR-006, F-DIR-015, F-ACT-002, F-ACT-005 et F-ACT-009
- Propriétaires pressentis : ACTION pour la sémantique ; schéma et validateur pour le transport et les invariants
- Test futur : changed, confirmed, abandoned, N/A, not-observed, résultat absent par mode et compatibilité avec state/verdict

### F-ACT-014 — `NOT-OBSERVED` possède un sens canonique mais aucun emplacement structuré ou registre explicite dans ACTION/STATUS

- Gravité provisoire : **Significatif**
- État : **lacune de transport confirmée**
- Preuve : lignes 226, 230 et 236 utilisent `NOT-OBSERVED` pour une conséquence attendue mais absente ; le GLOSSAIRE le définit ; ACTION/STATUS ne le place dans aucun de ses cinq registres et RUN_CARD ne possède aucun champ ou enum correspondant
- Comportement observable : le producteur doit insérer le token dans une chaîne libre, une trace externe ou un champ dont la sémantique principale est différente ; les champs structurés dédiés sont rejetés
- Risque : confusion avec `NOT-VERIFIED` ou `N/A-JUSTIFIED`, absence non agrégable, conséquence attendue effacée lors du transfert
- Facteur atténuant : le bloc donne une définition humaine correcte et `trace_locator` permet de conserver le détail hors projection
- Relations : F-DIR-011, F-DIR-019, F-DIR-029, F-ACT-003, F-ACT-007 et F-ACT-013
- Propriétaires pressentis : ACTION/STATUS pour le registre ; RUN_CARD ou convention de trace pour le transport
- Test futur : applicable non observé, non vérifiable, non applicable, observation négative, conséquence partielle et mapping vers preuve/decision_change

### F-ACT-015 — le contrat minimal SYSTÈME n’est pas représenté ni contrôlé par RUN_CARD

- Gravité provisoire : **Majeur provisoire**
- État : **divergence de couverture confirmée ; disposition différée au bloc RUN_CARD**
- Preuve : ligne 200 exige impact, consumers, décision, owner, migration, rollback, non-régression et CHANGELOG ; le schéma n’a aucun champ SYSTÈME dédié et le validateur n’exige que les champs génériques et `trace_locator`
- Comportement observable : une carte SYSTÈME clôturée et acceptée sans consumers, migration, rollback, non-régression, CHANGELOG ni decision_change est valide
- Risque : adoption d’un changement partagé sans plan de migration ou retour, consommateurs oubliés, rupture non détectée, gouvernance machine verte malgré un contrat métier absent
- Facteur atténuant : la trace externe peut porter toutes ces informations ; ACTION avertit plus loin que la validation structurelle ne prouve pas la conformité réelle
- Relations : F-DIR-006, F-DIR-010, F-DIR-013, F-ACT-002 et F-ACT-006
- Propriétaires pressentis : ACTION/RUN-SYSTEM et RUN_CARD ; schéma/validateur pour la couverture machine choisie
- Test futur : consumers vides, migration absente, rollback impossible justifié, non-régression partielle, CHANGELOG manquant et changement partagé critique

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — chargement et routes

Les trois propriétaires explicitement nommés par ce bloc — ACTION/PRECONDITION, DIRECTION/EXTERNAL-START et SAVOIR/DESIGN-ATLAS — sont introuvables par `read_route.py`. Les routes RUN-DIRECTION et RUN-SYSTEM passent. Le défaut reste confirmé et doit inclure ces trois locators dans ses fixtures futures.

### F-ACT-002 et F-DIR-006 — mapping humain / machine / trace

Le bloc dépend fortement de la trace externe pour les champs de sélection, l’omission évitée, la limite restante et les sorties sans effet. Ce choix peut être proportionné, mais aucun mapping contrôlable n’assure la conservation. F-ACT-013 à F-ACT-015 détaillent trois pertes précises sans conclure qu’il faut sérialiser chaque champ local.

### F-ACT-005 — temporalité du scope et de la preuve

Le raccord DESIGN-ATLAS sépare correctement hypothèse pré-build et conséquence post-observation. Il constitue une formulation positive à réutiliser pour distinguer couverture attendue et scope réellement observé. F-ACT-005 reste toutefois ouvert dans UI-UX-REALITY, où le même champ `PROOF-SCOPE` porte les deux temporalités.

### F-ACT-007 — vocabulaire de preuve

Le propriétaire ACTION clarifie nettement N/A, non-vérifié et non-observé. La taxonomie `coverage_map` du schéma de contrats reste non alignée et l’absence de transport de `NOT-OBSERVED` reçoit F-ACT-014.

### F-ACT-009 — verdict prématuré

Le bloc exige correctement `DECISION-INTENT` au lancement et interdit `DECISION-CHANGE` avant observation. Il renforce donc la preuve que les états précoces ne devraient pas porter un verdict final obligatoire. F-ACT-009 reste confirmé.

### F-ACT-012 — axes bloquants et acceptation

La règle ligne 202 interdit de transformer une impossibilité de vérification en PASS. Le mode ne baisse pas et l’axe doit rester `NOT-VERIFIED`. La projection accepte encore un verdict global `ACCEPTED` avec une preuve obligatoire déclarée non vérifiée, faute d’axes structurés. F-ACT-012 est renforcé par le contrat propriétaire.

### F-DIR-011 et F-DIR-019 — sorties sans effet

Les lignes 230 et 236 fournissent enfin l’arbre correct : N/A si aucune conséquence n’était applicable, NOT-OBSERVED si une conséquence attendue ne se manifeste pas, NOT-VERIFIED si l’observation nécessaire ne peut être menée. F-DIR-011 est fortement atténué par ACTION, mais la phrase générique de la ligne 218 et plusieurs occurrences DIRECTION devront être harmonisées.

### F-DIR-015 — abandon d’une décision

ACTION confirme explicitement la triade « changée, confirmée ou abandonnée ». L’omission de l’abandon dans FAST-PATH est donc un défaut local de DIRECTION, pas une incertitude du propriétaire. F-DIR-015 reste confirmé.

### F-DIR-017 — checkpoint pré-build

La trace post-build d’EXTERNAL-START mesure les conséquences après le premier artefact. Elle ne rend pas plus visible le checkpoint d’autorité avant le build. F-DIR-017 reste ouvert jusqu’à l’audit de PIPELINE-DIRECTION et AUTHORITY.

## Éléments conformes à préserver

1. Le mode dépend de la tâche, du risque et du blast radius, pas des outils disponibles.
2. Une capacité absente ne rétrograde jamais silencieusement DIRECTION.
3. La capacité détermine la voie de preuve et la force du claim atteignable.
4. Les cinq modes reçoivent un contrat proportionné.
5. STANDARD n’exige ancre ou asset que si le risque le justifie.
6. DIRECTION exige une preuve du rendu réel et un statut de fidélité.
7. SYSTÈME nomme explicitement consumers, migration, rollback et non-régression.
8. Un gate non applicable est distingué d’un gate nécessaire mais non vérifiable.
9. Aucun PASS n’est créé par défaut lorsque la preuve manque.
10. DECISION-INTENT précède l’observation.
11. DECISION-CHANGE ne peut être déclaré avant une conséquence réelle.
12. Une décision confirmée ou abandonnée reste une conséquence mémorisable.
13. EXTERNAL-START ne crée ni gate, ni statut, ni formulaire supplémentaire.
14. L’utilité d’EXTERNAL-START est évaluée après le premier objet, pas supposée au lancement.
15. Une absence de conséquence applicable et une conséquence attendue non observée sont distinguées.
16. DESIGN-ATLAS reste conditionnel à une décision qu’il peut modifier.
17. Les champs pré-build de l’atlas sont des hypothèses, pas des observations.
18. Une rationale, une cible, une ancre ou un asset ne constituent pas une preuve par leur seule présence.
19. Seul un résultat observé dans le scope déclaré peut alimenter décision et verdict.
20. Le polish perceptuel ne devient pas une preuve d’usage, d’accessibilité ou de performance.
21. L’absence de style, technique, effet, asset ou composant est une sortie valide.
22. Une alternative n’est produite que si elle peut modifier une décision.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Responsabilités, temporalités, titre PRECONDITION, interfaces et routes examinés |
| B — Contrats | FULL | Cinq modes, trois sorties de preuve, décision, EXTERNAL-START et DESIGN-ATLAS analysés phrase par phrase |
| C — Usage | TARGETED | DIRECTION sans capture, N/A, non-observé, non-vérifiable, confirmation, préflight sans effet et SYSTÈME simulés |
| D — Résistance | FULL | Trois nouveaux constats ACTION et huit familles de constats antérieurs mises à jour |
| Contrôles machine | FULL ciblé | Routes, decision_change, typage des résultats, champs de trace et minimum SYSTÈME testés |

## Point de passage

Le bloc 4 d’ACTION est entièrement lu. Il fournit l’un des meilleurs contrats épistémiques du corpus : le mode reste indépendant des capacités, une hypothèse pré-build n’est pas une observation, et non-applicabilité, non-vérification et non-observation ne sont pas interchangeables. Les faiblesses se situent dans le transport : conséquence décisionnelle libre et optionnelle, `NOT-OBSERVED` sans registre structuré et minimum SYSTÈME invisible pour le validateur.

La prochaine unité est `ACTION.md`, lignes 242–334 : `ACTION/FAST-PATH`, `ACTION/RUN_CARD`, profil de capacités, mode agent seul, `EXECUTION-SNAPSHOT`, projection machine optionnelle et frontière entre validation de structure et preuve réelle. Elle devra confirmer ou reclasser F-ACT-013 à F-ACT-015, résoudre la temporalité de F-ACT-009, et auditer chaque champ humain contre le schéma et le validateur. Aucun patch n’est autorisé à ce stade.
