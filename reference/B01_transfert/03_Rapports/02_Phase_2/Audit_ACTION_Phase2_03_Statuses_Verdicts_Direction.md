# DG-AUDIT-001 — Phase 2 — ACTION, bloc 3

## Périmètre examiné

- Cible : `V1/official/ACTION.md`
- Bloc : lignes 116–188 de la reconstruction de travail
- Section : `ACTION/STATUS` — états du run, issues et exceptions, séparation des registres, chemin minimal, principe positif, verdicts V/U/A/T et statut de direction
- Interfaces vérifiées : blocs ACTION 1–2, `DIRECTION/START`, `ACTION/PRECONDITION`, `ACTION/RUN_CARD`, routes de lecture, schéma `run_card.schema.json`, validateur `validate_run_card.py`, fixtures et suite complète
- Source d’observation : compilation `Design_Governance_V1.0.md`, reconstruction de travail et baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, lecture phrase par phrase, comparaison propriétaire/projection machine, simulation de transitions et mutations négatives ciblées
- Statut : diagnostic sectionnel provisoire ; aucun verdict global sur ACTION et aucun patch du corpus

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole, le plan maître et les deux rapports ACTION précédents ont été relus. Les constats transportés en priorité sont F-ACT-001 à F-ACT-008 et F-DIR-011, F-DIR-019, F-DIR-029, F-DIR-033 et F-DIR-035.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 116–134 | Définir les sept états du run | Progression compréhensible de l’entrée à la persistance ; critères d’entrée et de sortie concrets | La projection machine exige un verdict final dans tous les états, y compris avant observation et décision |
| 136–144 | Définir six issues et exceptions | Blocage, reprise, reclassification, exploration, échec assumé et escalade sont distingués | `RECLASSIFIED` ne transporte ni ancien mode, ni nouveau mode, ni run successeur |
| 146–153 | Séparer cinq registres | Refuse les synonymes et la fausse maturité ; distingue gates A/B/C et axes V/U/A/T ; fidélité et acceptation restent indépendantes | Aucune matrice canonique ne précise les cooccurrences autorisées entre issue, statut de direction et verdict global |
| 155–162 | Garder un chemin proportionné et positif | Évite le cérémonial ; protège un premier rendu ambitieux ; autorise le one-shot seulement après observation réelle | La qualité positive est correctement subordonnée au risque et à la preuve |
| 164–175 | Définir quatre axes de preuve et leurs statuts | Couvre visuel, usage, accessibilité et technique ; permet réserve, retour, non-applicabilité justifiée et non-vérification | Les axes bloquants ne sont pas sérialisés dans RUN_CARD ; le verdict global ne peut pas être recalculé ou protégé structurellement |
| 177–188 | Séparer fidélité de direction et acceptation | `HELD` n’implique ni beauté, ni préférence, ni réussite U/A/T, ni acceptation | `PARTIALLY-HELD` peut néanmoins coexister avec `ACCEPTED` dans le validateur actuel |

## Passage A — architecture visible

La section place dans un même propriétaire les vocabulaires nécessaires à la clôture sans les fusionner. L’architecture logique comporte cinq plans :

1. état courant du run ;
2. issue ou exception ;
3. verdicts par axe V/U/A/T ;
4. statut de fidélité de direction ;
5. verdict global.

Cette séparation est l’un des points structurants les plus solides du système. Elle évite notamment d’utiliser `HELD` comme état de workflow, `PASS` comme acceptation globale ou `CLOSED` comme preuve de réussite.

Le chemin d’état est lisible :

```text
INTAKE → CLASSIFIED → SPECCED → BUILDING → CHECKING → DECIDED → CLOSED
```

La prose n’impose pas que tout run matérialise sept tickets ou sept transitions administratives. Elle définit un vocabulaire commun et permet un chemin minimal proportionné. Pour un micro-delta, plusieurs états peuvent être brefs, à condition que la classification, l’observation et la décision restent réelles.

`ACTION/STATUS` est toutefois absent de READING_MAP et rejeté par `read_route.py`, comme `ACTION/PRECONDITION`. Le propriétaire existe et est nommé depuis d’autres sections, mais le lecteur officiel ne peut pas l’ouvrir par son locator normatif. Ce résultat confirme F-ACT-001 et F-DIR-028 ; aucun nouvel ID n’est créé pour une nouvelle occurrence du même défaut.

## Passage B — contrat sémantique

### Les états du run

Les critères de sortie décrivent une progression fondée sur la réduction d’incertitude :

- `INTAKE` se termine lorsque mode, décision dominante, risque et prochaine preuve sont connus ;
- `CLASSIFIED` se termine lorsque le build direct est autorisé ou que le contrat requis existe ;
- `SPECCED` se termine lorsque le build peut commencer ;
- `BUILDING` se termine lorsque les contrôles applicables peuvent être exécutés ;
- `CHECKING` se termine lorsque verdicts, réserves et prochaine action sont déclarés ;
- `DECIDED` se termine lorsque la trace est persistée, retournée ou escaladée ;
- `CLOSED` signifie que l’artefact et la trace minimale sont persistés.

Cette temporalité implique qu’un verdict global n’est pas encore connu pendant `INTAKE`, `CLASSIFIED`, `SPECCED` ou `BUILDING`. Il devient une sortie du contrôle, puis une donnée de `DECIDED` et `CLOSED`.

La projection machine inverse cette relation. `closure` exige toujours `state`, `issue`, `verdict` et `limitations`; `verdict` n’accepte pas `null`. Une RUN_CARD en `INTAKE` doit donc prétendre à `ACCEPTED`, `RETURN`, `EXPLORATORY` ou un autre verdict final avant que le système n’ait observé ou décidé. Le validateur accepte par exemple `INTAKE + RETURN`, `CLASSIFIED + EXPLORATORY`, `BUILDING + SYSTEM-ESCALATION` et `CHECKING + RETURN`.

Ce n’est pas une simple préférence de sérialisation. La documentation dit explicitement que le verdict est connu à l’entrée de `DECIDED`; rendre ce champ obligatoire avant cette étape force une information prématurée ou une valeur de remplissage.

### `CLOSED` comme persistance, non comme réussite

La définition de `CLOSED` est excellente et doit être protégée. Un run peut être clôturé administrativement avec une issue `RETURNED`, `EXPLORATORY` ou `BLOCKED`, ou un verdict `RETURN`, `EXPLORATORY` ou `SYSTEM-ESCALATION`, lorsque la limite, la reprise ou l’escalade sont persistées.

Cette règle empêche trois erreurs fréquentes :

- garder indéfiniment un run ouvert alors qu’une décision de retour est déjà prise ;
- confondre fermeture de la trace et acceptation de l’artefact ;
- effacer les échecs ou les preuves manquantes pour obtenir un statut terminal propre.

La fixture `valid_closed_return.json` confirme que la machine sait représenter cette séparation. Le problème n’est donc pas que `CLOSED` autorise des issues négatives ; c’est que les compatibilités complètes entre les cinq registres ne sont pas définies.

### Issues et exceptions

Les six issues répondent à des causes différentes : condition manquante, reprise dans le même mode, changement de mode, preuve manquante malgré un rendu, échec connu temporairement diffusé ou dépassement du périmètre du run.

`RETURNED` et `RECLASSIFIED` sont correctement distingués en prose : le premier reprend une étape dans le même mode, le second impose un autre mode. Mais la projection ne possède qu’un unique champ `mode` et une issue `RECLASSIFIED`. Elle ne conserve ni :

- le mode quitté ;
- le mode cible ;
- la raison structurée de reclassification ;
- l’identifiant du run successeur si un nouveau run est ouvert.

Une carte `mode: STANDARD`, `issue: RECLASSIFIED` est donc ambiguë : STANDARD peut être le mode d’origine ou le nouveau mode. La trace libre peut compenser, mais le mécanisme canonique de reprise ne garantit pas que l’information reste retrouvable.

### Cinq registres strictement séparés

La section interdit explicitement les synonymes concurrents. Elle précise aussi que :

- A/B/C sont des gates de contrôle ;
- V/U/A/T sont des axes de question et de preuve ;
- un statut de direction décrit la fidélité ;
- un verdict global décrit la disposition du run ;
- l’outil de projet ne doit pas créer un autre état du run.

Cette séparation résout conceptuellement une partie de F-DIR-033 et F-DIR-035. Elle clarifie aussi l’occurrence du bloc 2 : `EXPLORATORY` peut exister dans deux registres distincts, comme issue et comme verdict global. Le double emploi n’est pas nécessairement un défaut si chaque champ est nommé et si les cooccurrences sont définies.

Or la section liste les valeurs du verdict global sans définir précisément chacune d’elles. Elle n’établit pas non plus la matrice minimale entre issue, statut de direction, axes et verdict global. Les garde-fous machine couvrent seulement quelques incompatibilités :

- `BLOCKED` ou `FAIL-ASSUMED` avec un verdict accepté sont rejetés ;
- `LOST-IN-BUILD` avec un verdict accepté est rejeté ;
- un verdict accepté exige un état `DECIDED` ou `CLOSED`, une preuve observée, une provenance et au moins une limitation.

Mais les combinaisons suivantes sont acceptées :

```text
issue EXPLORATORY   + verdict ACCEPTED
issue RETURNED      + verdict ACCEPTED
issue RECLASSIFIED  + verdict ACCEPTED
issue ESCALATED     + verdict ACCEPTED
direction_status PARTIALLY-HELD + verdict ACCEPTED
```

Certaines pourraient être recevables dans un cas très particulier, mais le propriétaire ne donne pas la règle permettant de le déterminer. `RETURN-DIRECTION` n’est pas relié formellement à un statut ou à une issue ; `SYSTEM-ESCALATION` n’est pas relié formellement à `ESCALATED`; `ACCEPTED-WITH-RESERVATION` n’est pas distingué ici d’une acceptation pleine par un contrat de réserve. Des règles apparaissent plus loin dans ACTION, mais le bloc qui se déclare vocabulaire canonique ne les consolide pas.

### Chemin minimal et principe positif

Le chemin minimal est proportionné : DIRECTION classe, ACTION obtient la preuve et clôt, et une route supplémentaire n’est chargée que si elle peut modifier la décision ou lever une incertitude déclarée. Cette règle protège l’utilisabilité quotidienne du système.

Le principe positif évite une gouvernance uniquement défensive. Il demande une relation produit perceptible, un niveau de résolution et un défaut dominant avant le build, puis juge cette intention sur l’artefact réel. La règle one-shot est bien bornée : une première observation peut suffire si qualité et risques sont couverts et si aucune correction n’a de gain réel, mais aucune clôture sans observation du rendu n’est admise.

Ce passage atténue encore F-DIR-009. Il ne crée ni quota d’itérations, ni correction décorative obligatoire.

### Axes V/U/A/T

La taxonomie est compacte et pertinente :

- V : caractère visuel ;
- U : compréhension et usage ;
- A : accessibilité et conformité ;
- T : robustesse technique.

Chaque axe accepte `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`. La présence simultanée de non-applicabilité justifiée et non-vérification est essentielle : hors périmètre et preuve manquante ne sont pas confondus. La règle « aucune moyenne ne compense un axe bloquant » empêche une note visuelle forte de masquer un échec critique d’usage, d’accessibilité ou de robustesse.

La projection RUN_CARD ne sérialise pourtant aucun de ces axes. ACTION/RUN_CARD dira plus loin qu’ils restent dans la trace complète référencée par `trace_locator`. Ce choix peut garder la projection compacte, mais il empêche le schéma et le validateur d’établir que le verdict global respecte les axes.

Le test le plus révélateur conserve un verdict `ACCEPTED` tout en ajoutant à `proof.not_verified` la mention « A — accessibilité obligatoire non vérifiée ». La carte reste valide. À l’inverse, l’ajout d’un objet structuré `axes` est rejeté comme champ inconnu. La projection sait donc transporter une phrase de non-vérification, mais pas l’utiliser comme blocage calculable du verdict.

La documentation précise que la validation de structure ne prouve pas la qualité réelle. Cette réserve est juste, mais elle ne résout pas la cohérence interne de la décision transportée : une machine qui accepte la structure d’un verdict global devrait au minimum empêcher une acceptation pleine lorsqu’une preuve explicitement obligatoire reste non vérifiée.

### Statut de direction

Les quatre valeurs forment une échelle de fidélité, non de beauté :

- `HELD` ;
- `HELD-WITH-ACCEPTED-DIFFERENCE` ;
- `PARTIALLY-HELD` ;
- `LOST-IN-BUILD`.

La phrase finale protège la distinction la plus importante : `HELD` n’est ni une préférence esthétique, ni une validation U/A/T, ni une acceptation globale. Le validateur protège `LOST-IN-BUILD`, mais pas `PARTIALLY-HELD`. Une acceptation pleine avec direction partiellement tenue peut être légitime si la partie affaiblie est explicitement hors périmètre ou sans impact, mais le nom de la valeur dit précisément qu’un écart demeure. Sans règle ou réserve obligatoire, l’acceptation pleine est trop facile.

## Contrôles machine ciblés

### Contrôle 0 — baseline et suite officielle

Les deux hashes B01 sont inchangés. `validate_all.py` passe entièrement : package, RUN_CARD, contrats, carte de lecture, distributions et reproductibilité restent intègres.

Ce PASS confirme que les fichiers satisfont les contrôles actuels. Il ne contredit pas les défauts ci-dessous : les combinaisons testées ne font pas partie des fixtures négatives actuelles.

### Test 1 — accès par route

```text
ACTION/STATUS        FAIL — locator inconnu
ACTION/PRECONDITION  FAIL — locator inconnu
```

Les sections existent mais ne sont pas des entrées résolubles de READING_MAP.

### Test 2 — verdict obligatoire avant décision

Mutations d’une RUN_CARD valide :

```text
INTAKE     + RETURN             ACCEPTED BY VALIDATOR
CLASSIFIED + EXPLORATORY        ACCEPTED BY VALIDATOR
BUILDING   + SYSTEM-ESCALATION  ACCEPTED BY VALIDATOR
CHECKING   + RETURN             ACCEPTED BY VALIDATOR
INTAKE sans verdict             REJECTED — champ obligatoire absent
INTAKE avec verdict null        REJECTED — valeur non canonique
```

La structure ne permet donc pas de représenter honnêtement « verdict pas encore produit ».

### Test 3 — cooccurrences inter-registres

```text
EXPLORATORY  + ACCEPTED  ACCEPTED BY VALIDATOR
RETURNED     + ACCEPTED  ACCEPTED BY VALIDATOR
RECLASSIFIED + ACCEPTED  ACCEPTED BY VALIDATOR
ESCALATED    + ACCEPTED  ACCEPTED BY VALIDATOR
PARTIALLY-HELD + ACCEPTED  ACCEPTED BY VALIDATOR
BLOCKED      + ACCEPTED  REJECTED
LOST-IN-BUILD + ACCEPTED REJECTED
```

Le validateur contient donc des protections utiles, mais partielles.

### Test 4 — axe obligatoire non vérifié

```text
verdict = ACCEPTED
proof.not_verified = ["A — accessibilité obligatoire non vérifiée"]
```

Résultat : validation réussie.

Mutation supplémentaire :

```text
axes = {"A": "NOT-VERIFIED"}
```

Résultat : rejet pour champ inconnu.

La règle « aucune moyenne ne compense un axe bloquant » ne possède pas de projection machine vérifiable.

## Passage C — usages simulés

### Run reçu mais non classé

Le designer crée une RUN_CARD en `INTAKE`. Il connaît l’owner et la prochaine question, mais aucun verdict n’existe. Le schéma l’oblige à choisir un verdict global. Il peut soit mentir avec `EXPLORATORY` ou `RETURN`, soit différer la création de la carte alors que la ligne de run doit déjà exister. Le contrat humain et la projection machine donnent deux comportements opposés.

### Run exploratoire avec artefact observable

Un prototype existe, mais la preuve d’usage est absente. L’issue `EXPLORATORY` est correcte. Sans matrice de compatibilité, le producteur peut néanmoins conserver `ACCEPTED`; le validateur ne distingue pas acceptation de l’artefact, acceptation du scope limité ou simple persistance de la trace.

### Retour dans le même mode

Une correction est nécessaire après CHECKING. `RETURNED` indique correctement une reprise locale. Une clôture administrative avec verdict `RETURN` est cohérente. `RETURNED + ACCEPTED` est aussi accepté par la machine sans réserve ou explication obligatoire, ce qui rend la disposition ambiguë.

### Reclassification STANDARD vers DIRECTION

L’identité devient l’objet direct du run. `RECLASSIFIED` est la bonne issue, mais le champ `mode: DIRECTION` ne dit pas si le changement a déjà eu lieu ni quel mode a été quitté. Sans lien de succession, une reprise automatique peut relancer la mauvaise route ou perdre la raison du changement.

### Direction partiellement tenue

La composition préserve la hiérarchie mais affaiblit la signature retenue. `PARTIALLY-HELD` décrit bien la fidélité. Un verdict global peut être `RETURN-DIRECTION` ou éventuellement `ACCEPTED-WITH-RESERVATION` si l’écart est explicitement accepté et compatible avec les autres axes. Une acceptation pleine ne devrait pas être produite sans règle qui démontre que la partie perdue est hors du périmètre décisif.

### One-shot réellement suffisant

Le premier rendu est observé, les quatre axes applicables sont couverts, aucun risque bloquant ne demeure et une correction supplémentaire n’apporterait pas de gain réel. La section autorise correctement `DECIDED`, puis `CLOSED`, sans itération artificielle.

### Fermeture d’un blocage documenté

Une dépendance externe manque, mais owner, limite et prochaine preuve sont persistés. `CLOSED + BLOCKED + SYSTEM-ESCALATION` peut être cohérent : la trace est fermée sans prétendre que le produit est accepté. La séparation state/issue/verdict fonctionne ici comme prévu.

## Passage D — constats

### F-ACT-009 — la projection exige un verdict final avant que le cycle ne l’ait produit

- Gravité provisoire : **Majeur**
- État : **contradiction humain/machine confirmée**
- Preuve : les lignes 121–132 placent la déclaration des verdicts à la sortie de `CHECKING` et leur connaissance à l’entrée de `DECIDED`; le schéma exige `closure.verdict` pour tous les états et refuse `null`
- Comportement observable : une RUN_CARD `INTAKE`, `CLASSIFIED`, `SPECCED`, `BUILDING` ou `CHECKING` doit porter un verdict prématuré ; les mutations de ces états passent lorsqu’un enum final est fourni
- Risque : fausse décision, information de remplissage, confusion entre disposition provisoire et verdict global, création tardive de la RUN_CARD pour contourner le schéma
- Facteur atténuant : le validateur interdit un verdict accepté avant `DECIDED`; le défaut concerne néanmoins tous les autres verdicts finaux et l’absence de valeur honnête
- Relations : F-DIR-003 sur la temporalité et F-ACT-002 sur le mapping humain/machine
- Propriétaires pressentis : ACTION pour la temporalité ; schéma et validateur pour la représentation
- Test futur : chaque état avec verdict absent, provisoire ou final ; transition CHECKING → DECIDED ; sérialisation sans information inventée

### F-ACT-010 — le vocabulaire canonique n’établit pas les compatibilités entre issue, fidélité et verdict global

- Gravité provisoire : **Majeur**
- État : **lacune contractuelle et garde-fous partiels confirmés**
- Preuve : le bloc sépare cinq registres et liste les verdicts globaux, mais ne définit pas leurs sémantiques ni leur matrice de cooccurrence ; le validateur accepte `EXPLORATORY`, `RETURNED`, `RECLASSIFIED` ou `ESCALATED` avec `ACCEPTED`, ainsi que `PARTIALLY-HELD + ACCEPTED`
- Comportement observable : deux producteurs peuvent sérialiser des dispositions opposées pour le même état de preuve tout en restant valides
- Risque : acceptation pleine malgré reprise, escalade ou preuve manquante ; tableaux de bord incohérents ; automatisations incapables de choisir la prochaine action
- Facteur atténuant : `BLOCKED`, `FAIL-ASSUMED` et `LOST-IN-BUILD` avec verdict accepté sont déjà rejetés ; des règles plus précises apparaissent plus loin dans ACTION
- Relations : F-DIR-011, F-DIR-029, F-DIR-033, F-DIR-035 et F-ACT-003
- Propriétaires pressentis : ACTION/STATUS pour la sémantique ; validateur pour les invariants vérifiables
- Test futur : matrice issue × verdict × direction_status, avec cas autorisés, interdits et autorisés seulement sous réserve explicite

### F-ACT-011 — `RECLASSIFIED` ne transporte pas la transition de mode

- Gravité provisoire : **Significatif**
- État : **contrat de reprise incomplet confirmé**
- Preuve : `RECLASSIFIED` signifie qu’un autre mode s’impose, mais RUN_CARD ne possède qu’un champ `mode` et aucun champ de mode précédent, mode cible ou run successeur
- Comportement observable : `mode: STANDARD` avec `issue: RECLASSIFIED` ne permet pas de savoir si STANDARD est le point de départ ou d’arrivée
- Risque : mauvaise route à la reprise, perte de l’historique de classification, double run non relié, métriques de reclassification non fiables
- Facteur atténuant : la trace libre et le `trace_locator` peuvent documenter la transition ; DIRECTION reste propriétaire de la classification
- Relations : F-DIR-011 sur les transitions et F-ACT-002 sur le handoff
- Propriétaires pressentis : ACTION pour le transport ; DIRECTION/START pour la décision de reclassement
- Test futur : LITE → STANDARD, STANDARD → DIRECTION, DIRECTION → SYSTÈME, reprise même carte et création d’un run successeur

### F-ACT-012 — un axe bloquant n’est pas représentable dans la base structurée du verdict global

- Gravité provisoire : **Majeur provisoire**
- État : **divergence humain/machine confirmée ; disposition différée à l’audit complet de RUN_CARD**
- Preuve : les lignes 164–175 rendent V/U/A/T canoniques et interdisent qu’une moyenne compense un blocage ; ACTION/RUN_CARD laisse ces axes hors schéma ; le validateur accepte `ACCEPTED` avec une preuve obligatoire A déclarée non vérifiée et rejette un objet `axes`
- Comportement observable : le verdict global est valide structurellement sans base d’axes inspectable ou sans blocage lorsque le texte de preuve annonce une non-vérification obligatoire
- Risque : acceptation automatisée incohérente avec la preuve, impossibilité de vérifier la règle du bloqueur, perte des réserves par axe lors d’un transfert
- Facteur atténuant : la trace complète référencée par `trace_locator` peut conserver les axes ; la validation JSON ne prétend pas prouver la qualité réelle
- Relations : F-DIR-019, F-DIR-033, F-ACT-002, F-ACT-005 et F-ACT-007
- Propriétaires pressentis : ACTION pour le contrat de verdict ; schéma/validateur pour la projection minimale
- Test futur : A ou T obligatoire `NOT-VERIFIED`, U `RETURN`, V `PASS-WITH-RESERVATION`, axe `N/A-JUSTIFIED` et agrégation vers chaque verdict global

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — chargement et routes

`ACTION/STATUS` et `ACTION/PRECONDITION` sont des propriétaires nommés mais des locators inconnus du lecteur officiel. Le défaut de navigation reste confirmé. La lecture manuelle du fichier fonctionne, mais le chargement conditionnel annoncé par le système ne fonctionne pas de bout en bout.

### F-ACT-002 — mapping entre trace humaine et RUN_CARD

Le bloc rend la frontière temporelle plus nette : le verdict n’est produit qu’après CHECKING. Le mapping actuel ne sait pas transporter cette absence antérieure. F-ACT-009 devient le cas précis à corriger lors de l’audit de RUN_CARD.

### F-ACT-003 — nombre et nature des registres

ACTION/STATUS confirme cinq plans conceptuels lorsque les verdicts V/U/A/T sont comptés séparément du verdict global : état, issue, axes, direction et verdict global. Le bloc 1 parlait de quatre registres tout en énumérant deux familles dans le quatrième. F-ACT-003 reste confirmé comme incohérence de comptage, sans défaut sur l’intention de séparation.

### F-ACT-005 — temporalité de la preuve

Le cycle d’état confirme qu’une couverture prévue, une observation en cours et un verdict décidé sont trois moments distincts. La fusion de `PROOF-SCOPE` attendu et observé devient plus risquée parce que CHECKING est précisément la frontière où l’information change de statut.

### F-ACT-007, F-DIR-019 et F-DIR-029 — statuts de preuve

Le bloc canonique réaffirme `N/A-JUSTIFIED` et `NOT-VERIFIED` comme valeurs distinctes par axe. Il n’emploie pas `NOT-OBSERVED` dans la table V/U/A/T. La projection `coverage_map` du bloc précédent reste une taxonomie parallèle ; le prochain bloc devra déterminer où `NOT-OBSERVED` appartient exactement.

### F-DIR-009 — itération artificielle

La règle one-shot est explicite : après observation, un run peut se clôturer sans nouvelle correction si qualité, risques et gain marginal sont satisfaisants. F-DIR-009 est fortement atténué par ACTION et devra être reclassé lors de la consolidation système.

### F-DIR-033 et F-DIR-035 — taxonomies et clôture

Le propriétaire sépare correctement les plans et explique que `CLOSED` ne vaut pas acceptation. L’ambiguïté d’`EXPLORATORY` est gérable par le nom du champ, mais devient réelle lorsque la matrice de compatibilité manque. F-ACT-010 remplace une inquiétude lexicale vague par un défaut testable de cooccurrence.

## Éléments conformes à préserver

1. ACTION possède un vocabulaire canonique et interdit les synonymes concurrents.
2. Les états décrivent une progression de décision plutôt qu’une échelle de maturité.
3. Les critères d’entrée et de sortie sont lisibles et orientés action.
4. `CLOSED` signifie persistance, pas réussite.
5. Une clôture peut conserver honnêtement un retour, un blocage, une exploration ou une escalade.
6. `RETURNED` et `RECLASSIFIED` sont distingués conceptuellement.
7. Blocage, échec assumé et escalade exigent owner, portée ou prochaine preuve.
8. État, issue, axes, statut de direction et verdict global ne sont pas fusionnés.
9. Les gates A/B/C ne sont pas confondus avec V/U/A/T.
10. Un outil de projet ne crée pas un état concurrent du run.
11. Le chemin minimal évite les routes ou contrats sans effet sur la décision.
12. La méthode vise une qualité positive, ambitieuse et spécifique dès le premier rendu.
13. Le one-shot est autorisé seulement après observation réelle et couverture des risques.
14. V/U/A/T couvrent ensemble expression, usage, accessibilité et robustesse.
15. Chaque axe distingue PASS, réserve, retour, non-applicabilité justifiée et non-vérification.
16. Aucune moyenne ne peut compenser un axe bloquant.
17. La fidélité de direction ne vaut ni beauté, ni préférence, ni acceptation globale.
18. `HELD` ne masque jamais une absence de validation U, A ou T.
19. Le validateur protège déjà plusieurs contradictions critiques : acceptation avant décision, blocage accepté, échec assumé accepté et direction perdue acceptée.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Hiérarchie, cinq plans, cycle d’état, route et articulation avec le bloc suivant examinés |
| B — Contrats | FULL | Chaque état, issue, séparation, chemin minimal, principe positif, axe, verdict et statut de direction analysé |
| C — Usage | TARGETED | Intake, exploration, retour, reclassification, fidélité partielle, one-shot et clôture bloquée simulés |
| D — Résistance | FULL | Quatre nouveaux constats ACTION et neuf familles de constats antérieurs mises à jour |
| Contrôles machine | FULL ciblé | Baseline, suite complète, routes, états précoces, cooccurrences et absence d’axes structurés testés |

## Point de passage

Le bloc 3 d’ACTION est entièrement lu. Sa conception humaine est forte : elle sépare les plans, rend la clôture honnête, protège la proportion et établit un modèle de preuve sans moyenne compensatoire. Les défauts se concentrent dans le raccord machine et la complétude du contrat : verdict obligatoire trop tôt, matrice de compatibilité absente, reclassification non transportée et axes non inspectables dans la décision structurée.

La prochaine unité est `ACTION.md`, lignes 190–240 : `ACTION/PRECONDITION`, contrat minimal par mode, différence entre `N/A-JUSTIFIED`, `NOT-VERIFIED` et `NOT-OBSERVED`, contrat de décision/preuve, trace `EXTERNAL-START` et raccord `DESIGN-ATLAS`. Elle devra notamment vérifier si ce bloc résout ou aggrave la temporalité de F-ACT-005/F-ACT-009, où vit `NOT-OBSERVED`, et si les traces préparatoires deviennent réellement des conséquences observées. Aucun patch n’est autorisé à ce stade.
