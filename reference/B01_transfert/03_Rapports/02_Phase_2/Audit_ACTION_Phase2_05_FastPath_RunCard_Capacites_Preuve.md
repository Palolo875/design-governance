# DG-AUDIT-001 — Phase 2 — ACTION, bloc 5

## Périmètre examiné

- Cible : `V1/official/ACTION.md`
- Bloc : lignes 242–334 de la reconstruction de travail
- Sections : `ACTION/FAST-PATH`, `ACTION/RUN_CARD`, profil de capacités, mode agent seul et preuve dégradée, `EXECUTION-SNAPSHOT`, projection machine-readable optionnelle, frontière de validation et de preuve
- Interfaces vérifiées : ACTION/HANDOFF, STATUS, PRECONDITION, RUN-LITE, RUN-ITER, RUN-SYSTEM, CLOSE-PACKAGE, schéma `run_card.schema.json`, exemple, fixtures, validateur normal et strict, READING_MAP et GLOSSAIRE
- Source d’observation : compilation `Design_Governance_V1.0.md`, reconstruction de travail et baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, lecture phrase par phrase, matrice humain/machine, résolution des routes, simulation de lecteurs, mutations sémantiques et contrôles normal/strict
- Statut : diagnostic sectionnel provisoire ; aucun verdict global sur ACTION et aucun patch du corpus

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole, le plan maître et le rapport ACTION bloc 4 ont été relus. Les constats transportés en priorité sont F-ACT-002, 003, 009, 010 et 012 à 015, ainsi que F-DIR-003, 006, 010, 013, 015, 036, 037 et 045.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 242–248 | Fournir un chemin court pour LITE et petit ITER | Quatre questions décisionnelles ; refus des captures et routes sans conséquence ; reclassification si le risque s’élargit | « Arrête le protocole » peut supprimer owner, artefact, axes, verdict, trace et prochaine action exigés à la clôture |
| 252–280 | Définir RUN_CARD et son mapping JSON | Séparation state/issue/verdict/direction ; chemins JSON explicites ; alias STATUS interdit dans les nouveaux runs | Minimum humain et minimum machine divergent ; risque et changement de décision perdent du sens ; route RUN_CARD introuvable |
| 282–299 | Borner la conclusion par les capacités disponibles | Capacité ≠ preuve ; auto-comparaison ≠ regard indépendant ; absence de runtime interdit le PASS correspondant | Le profil n’est relié ni aux claims, ni à la provenance, ni au verdict ; ses contradictions passent la validation |
| 301–317 | Préparer une vue éphémère pour démarrer, déléguer ou reprendre | N’ajoute aucune autorité ; conserve sources, faits, capacités, axes, limites et prochaine preuve | Elle expire sur changement mais ne transporte ni ID, version source, état, owner, date de génération ou empreinte permettant de détecter cette expiration |
| 319–325 | Autoriser une vue machine sans taxonomie concurrente | JSON canonique unique ; champs et registres non fusionnés ; valeurs esthétiques parasites interdites | YAML est permis sans exemple ni validation directe ; la projection dite extensible reste fermée par `additionalProperties: false` |
| 327–331 | Borner exactement ce que prouve la validation | Sépare conformité structurelle, implémentation, usage, accessibilité, performance et qualité ; impose cible, méthode, scope, résultat, limite et prochaine preuve | Le validateur contrôle pourtant certains invariants métier tout en laissant passer des contradictions critiques qu’un lecteur peut croire couvertes |

## Passage A — architecture visible

Le bloc assemble trois couches qu’il faut maintenir distinctes :

1. un chemin humain court pour LITE et petit ITER ;
2. une carte de run humaine, locale et extensible ;
3. une projection JSON fermée, accompagnée d’un validateur structurel et de quelques invariants métier.

Cette architecture est raisonnable. Tous les détails locaux ne doivent pas devenir des champs JSON et une validation de schéma ne doit jamais être confondue avec une observation du produit. Le bloc dit explicitement que la trace complète peut rester dans un ticket, un manifeste, un paquet de preuve ou un autre espace inspectable.

La frontière entre « RUN_CARD locale extensible » et « projection JSON contrôlable » demeure cependant implicite. Le schéma interdit toute propriété supplémentaire. Une extension locale est donc possible uniquement hors de la projection canonique, ou dans un artefact référencé, mais aucun namespace d’extension ni règle de transport n’est fourni. Cette tension prolonge F-ACT-002 sans exiger automatiquement que le schéma accepte tous les champs libres.

Les routes donnent un résultat mixte :

```text
ACTION/FAST-PATH      PASS
ACTION/RUN-LITE       PASS
ACTION/CLOSE-PACKAGE  PASS
ACTION/RUN_CARD       FAIL
ACTION/STATUS         FAIL
ACTION/PRECONDITION   FAIL
```

Le chemin court et les routes d’exécution sont accessibles. Le propriétaire central du schéma et ses deux prérequis restent introuvables par leur locator normatif. F-ACT-001 et F-DIR-028 sont donc confirmés.

## Passage B — contrat sémantique

### FAST-PATH — décision utile, clôture insuffisamment explicite

Les quatre réponses sont bien choisies :

```text
décision touchée
risque dominant
preuve la moins coûteuse
conséquence de la preuve
```

Elles empêchent un protocole décoratif. Si rien ne peut changer, aucune capture ou comparaison n’est produite pour remplir un paquet ; la non-applicabilité réelle est journalisée. Si une responsabilité partagée, identitaire, critique, sécuritaire ou d’accessibilité apparaît, le lecteur revient à START et choisit une route plus protectrice.

Le problème vient de la formule « arrête le protocole après quatre réponses ». Lue seule, elle autorise la clôture sans :

- artefact ou diff retrouvable ;
- owner ;
- état et verdict ;
- axes V/U/A/T touchés ;
- réserve ou prochaine action ;
- ligne de run persistée ;
- `DECISION-CHANGE` ou sortie N/A correctement localisée.

RUN-LITE, CLOSE-PACKAGE et HANDOFF exigent pourtant plusieurs de ces éléments. La meilleure lecture est que FAST-PATH arrête le chargement supplémentaire après quatre décisions et s’appuie sur une ligne de run déjà existante. Le texte ne le dit pas. Sous contrainte de temps, un agent peut traiter les quatre réponses comme paquet de clôture complet.

L’expression « mode plus riche » est aussi à surveiller. Les modes protègent des responsabilités différentes ; ils ne forment pas une maturité ascendante. Le sens local reste compréhensible — route plus protectrice — et ne justifie pas un constat séparé.

### RUN_CARD humaine

La table possède les identifiants, responsabilités et décisions nécessaires à une reprise : ID, owner, date/version, mode, état, issue, verdict, statut de direction, décision, intention, conséquence, risque, artefact, trace et prochaine preuve.

Elle préserve correctement plusieurs distinctions :

- `ISSUE: null` signifie qu’aucune issue n’est déclarée ;
- le verdict global n’absorbe pas V/U/A/T ;
- le statut de direction reste distinct du verdict ;
- `DECISION-INTENT` précède `DECISION-CHANGE` ;
- l’artefact et la trace sont deux locators différents ;
- STATUS n’est plus un champ unificateur pour les nouveaux runs.

Le validateur rejette bien un champ `status` ajouté à la projection. Cette protection est conforme.

### Mapping exact entre table humaine et projection

| Champ humain | Projection | Résultat de l’audit |
|---|---|---|
| ID | `id` | Exact et obligatoire |
| OWNER | `owner` | Exact et obligatoire |
| DATE / VERSION | `date_version` | Exact et obligatoire |
| MODE | `mode` | Exact et obligatoire |
| STATE | `closure.state` | Exact, mais verdict final exigé dès les états précoces |
| ISSUE | `closure.issue` | Exact ; `null` est admis |
| VERDICT | `closure.verdict` | Enum exact ; temporalité incompatible avec F-ACT-009 |
| DIRECTION-STATUS | `closure.direction_status` | Exact ; requis par le validateur pour DIRECTION décidée/clôturée |
| DECISION | `decision` | Exact et obligatoire |
| DECISION-INTENT | `decision_intent` | Exact et obligatoire |
| DECISION-CHANGE | `decision_change.value/evidence` | Objet optionnel et résultat non typé ; F-ACT-013 |
| RISK | `risk.level/critical_protection` | Le risque principal et son impact ne peuvent pas être sérialisés |
| ARTIFACT | `artifact.locator/scope` | Projection plus précise et obligatoire |
| TRACE-LOCATOR | `trace_locator` | Exigences divergentes selon mode et mode strict |
| NEXT-PROOF | `next_proof` | Exact et obligatoire |

La machine exige en outre `sources`, `proof` et `closure.limitations`, absents de la table minimale. Ces ajouts sont utiles, mais confirment que la table humaine et la projection ne sont pas deux formes exactement équivalentes d’un même minimum.

### RISK — perte du risque principal et protection critique déclarative

La table humaine définit RISK comme « risque principal et impact potentiel ». Le schéma ne transporte que :

```text
level: normal | important | critical
critical_protection: control, owner, scope, failure_action, evidence_locator
```

Ajouter `summary` ou `impact` est rejeté comme propriété inconnue. Pour un risque normal ou important, la projection ne possède donc aucun emplacement canonique pour dire ce qui peut échouer ni quelle conséquence est redoutée. Le texte peut être placé dans `decision`, `artifact.scope`, `limitations` ou la trace, mais aucun mapping ne le garantit.

La protection critique est structurée et refuse les placeholders, ce qui est positif. Son `failure_action` n’est cependant pas relié au résultat de preuve ni à la clôture. Une carte peut déclarer :

```text
level = critical
control = validation clavier obligatoire
failure_action = RETURNED
proof.not_verified = validation clavier obligatoire
verdict = ACCEPTED
issue = null
```

et passer. La présence du garde-fou est contrôlée ; son exécution ne l’est pas.

### TRACE-LOCATOR — quatre contrats différents

La prose dit :

- requis pour STANDARD, DIRECTION, SYSTÈME et ITER persistant ;
- l’artefact localement évident peut servir de locator en LITE.

Le schéma et le validateur normal exigent `trace_locator` pour STANDARD, DIRECTION et SYSTÈME, mais pas ITER. Ils ne possèdent aucun indicateur distinguant ITER éphémère et persistant.

Le validateur strict exige ensuite `trace_locator` pour tous les modes. Résultats ciblés :

```text
LITE sans trace_locator — normal  ACCEPTED
LITE sans trace_locator — strict  REJECTED
ITER sans trace_locator — normal  ACCEPTED
ITER sans trace_locator — strict  REJECTED
```

Le contrat LITE autorisant l’artefact comme locator n’existe donc pas en mode strict, tandis que la précondition ITER persistante n’est pas contrôlable en mode normal.

### Profil de capacités

La sémantique humaine est excellente :

- seules les capacités pertinentes sont déclarées ;
- disponible, indisponible et non requis ne sont pas confondus ;
- une capacité soutenant un claim cite sa base ;
- une déclaration non attestée n’est pas une observation ;
- le profil n’est ni un score, ni un gate, ni une preuve.

La structure machine garantit seulement que les quatre listes existent si le profil est présent, et qu’une liste `available` non vide possède au moins une chaîne dans `basis`. Elle ne relie aucune capacité à un claim, une méthode, un résultat ou un axe.

Trois mutations passent :

```text
capture déclarée indisponible
+ qualité perceptuelle sur capture déclarée observed
+ verdict ACCEPTED

runtime/capture déclarés disponibles
+ seule base = déclaration non attestée
+ preuve observed
+ verdict ACCEPTED

suppression complète du capability_profile
+ preuve dépendante d’une capture
+ verdict ACCEPTED
```

Le profil peut donc documenter honnêtement une limite, mais il n’empêche pas structurellement la conclusion qu’il interdit en prose.

### Mode agent seul et preuve dégradée

La table est une bonne politique de prudence : une auto-comparaison n’est pas indépendante ; aucune qualité perceptuelle n’est prétendue sans rendu réel ; l’absence de regard externe devient réserve et prochaine preuve ; une capacité critique manquante ne modifie ni mode ni responsabilité.

La phrase finale protège explicitement l’acceptation pleine : si une preuve obligatoire manque, `ACCEPTED` n’est pas disponible. Elle autorise selon le risque `EXPLORATORY`, `RETURN-DIRECTION`, `ACCEPTED-WITH-RESERVATION` ou `ESCALATED`. Cette souplesse peut être légitime pour une preuve obligatoire au paquet mais non bloquante dans un scope limité ; elle requiert cependant la matrice de compatibilité manquante de F-ACT-010 pour éviter qu’une preuve critique soit transformée en simple réserve.

Le test du contrôle critique montre que cette frontière n’est pas appliquée. F-ACT-012 est donc renforcé au niveau le plus sensible.

### EXECUTION-SNAPSHOT

La snapshot contient les informations cognitives utiles : mode, décision/risque, sources, capacités, faits, axes, limite, trace et prochaine preuve. Elle interdit de choisir une variante sans artefact applicable et n’ajoute aucune autorité.

Son usage annoncé est cependant « démarrer, déléguer ou reprendre ». Pour ces trois usages, il manque :

- ID du run ;
- owner courant ;
- state et issue ;
- date/version de la RUN_CARD source ;
- version de l’artefact ou empreinte de faits ;
- instant de génération ;
- condition permettant de constater l’expiration.

La prose dit que la snapshot expire dès qu’un mode, un risque, une capacité ou un artefact change, mais la vue ne transporte aucune référence de fraîcheur pour comparer ces valeurs à la source actuelle. `TRACE-LOCATOR` permet théoriquement de rouvrir la RUN_CARD, mais le consommateur ne sait pas quelle version de cette carte a produit la snapshot. Une vue périmée peut donc paraître valide.

### Projection machine-readable optionnelle

Le bloc refuse correctement les taxonomies inventées : state, issue, verdict, gate, axe et décision restent distincts ; `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` ne sont pas fusionnés ; aucun score esthétique ou pseudo-statut n’est introduit.

La phrase autorisant YAML est faible mais non contradictoire si YAML est seulement un transport qui conserve exactement la structure JSON. Aucun exemple YAML ni commande de conversion/validation n’est fourni. Le seul exemple canonique et le validateur sont JSON. Ce point est documenté comme limite d’usage, sans constat autonome.

Le mot « extensible » s’applique à la RUN_CARD locale, pas au JSON fermé. L’ajout d’une propriété `extension` est rejeté. Une future correction doit clarifier la frontière plutôt que simplement ouvrir `additionalProperties`, ce qui affaiblirait les contrôles existants.

### Frontière validation / preuve

Les lignes 327–331 sont exemplaires. Elles disent précisément qu’une validation verte prouve seulement le respect des contrôles exécutés, jamais :

- l’implémentation réelle ;
- l’usage ;
- l’accessibilité exécutée ;
- la performance ;
- la qualité visuelle ;
- la préférence humaine.

Elles exigent pour chaque claim cible, méthode, scope/runtime, résultat, limite et prochaine preuve. Cette formulation doit être conservée.

La réserve ne neutralise toutefois pas les défauts du validateur. Celui-ci se présente comme contrôlant aussi des invariants métier : risque critique, capacité disponible, verdict accepté, direction perdue, état de décision. Lorsqu’il accepte une contradiction entre ses propres champs, le problème n’est pas qu’il ne prouve pas le monde réel ; il ne prouve pas la cohérence interne de la projection qu’il valide.

## Contrôles machine ciblés

### Contrôle 0 — baseline et suite officielle

Les empreintes B01 sont inchangées. La suite officielle passe. Les fixtures couvrent notamment protection critique absente, placeholder critique, capacité disponible sans base, acceptation sans preuve observée, acceptation avant décision et direction perdue acceptée.

La suite ne couvre pas la relation entre protection critique et preuve, ni la contradiction entre capacité déclarée et claim observé.

### Test 1 — routes

```text
ACTION/FAST-PATH      PASS
ACTION/RUN-LITE       PASS
ACTION/CLOSE-PACKAGE  PASS
ACTION/RUN_CARD       FAIL
ACTION/STATUS         FAIL
ACTION/PRECONDITION   FAIL
```

### Test 2 — RISK et protection critique

```text
risk.summary + risk.impact                           REJECTED — champs inconnus
critical control NOT-VERIFIED
+ failure_action RETURNED
+ issue null
+ verdict ACCEPTED                                  ACCEPTED BY VALIDATOR
```

### Test 3 — profil de capacités

```text
capture unavailable + claim capture observed + ACCEPTED       ACCEPTED
available sur déclaration non attestée + observed + ACCEPTED   ACCEPTED
profil supprimé + preuve dépendante du runtime + ACCEPTED      ACCEPTED
```

Le validateur exige une base lorsque `available` est non vide, mais ne qualifie ni sa force ni sa relation au claim.

### Test 4 — trace locator

```text
LITE sans trace_locator, validation normale   ACCEPTED
LITE sans trace_locator, validation stricte   REJECTED
ITER sans trace_locator, validation normale   ACCEPTED
ITER sans trace_locator, validation stricte   REJECTED
```

### Test 5 — minimum humain contre minimum machine

```text
champ STATUS ajouté              REJECTED — conforme à l’interdiction
extension locale ajoutée         REJECTED — projection fermée
sources omises                   REJECTED — requis machine, absent du tableau humain
closure.limitations omises       REJECTED — requis machine, absent du tableau humain
```

Les exigences supplémentaires sont utiles ; le défaut est l’absence d’une présentation unique du noyau commun et de ses extensions.

## Passage C — usages simulés

### Micro-correctif LITE sous contrainte de temps

L’agent répond aux quatre questions FAST-PATH puis s’arrête. Si la ligne de run, l’artefact, le verdict et l’owner existent déjà, le chemin est efficace. S’ils n’existent pas, le même texte permet une sortie non reprenable. La façade doit dire explicitement ce que les quatre réponses remplacent et ce qu’elles ne remplacent pas.

### Risque critique clavier

La protection critique exige un contrôle clavier et `RETURNED` en cas d’échec. Le contrôle reste `NOT-VERIFIED`, mais une autre observation visuelle existe. Le validateur accepte `ACCEPTED`. Un intégrateur peut alors croire la carte cohérente alors que sa propre action d’échec n’a pas été exécutée.

### Agent sans navigateur

Le profil déclare navigateur et capture indisponibles. La preuve affirme néanmoins qu’une qualité perceptuelle a été observée sur capture. La validation passe. La politique humaine est correcte ; la machine ne détecte pas la contradiction.

### ITER repris par un autre agent

La carte ITER n’a ni trace locator, ni direction transportée, ni décision-change. En validation normale elle passe. Le nouvel agent ne peut pas établir la baseline de direction ou la non-régression. Ce scénario confirme F-DIR-036 depuis le propriétaire ACTION.

### Snapshot périmée

Une snapshot est générée, puis l’artefact change. La vue ne porte ni version d’artefact, ni version de RUN_CARD, ni date de génération. Le délégué ne peut pas constater l’expiration sans rouvrir et comparer manuellement l’ensemble de la trace.

### Validation verte honnêtement limitée

Une carte porte un verdict non accepté, une preuve non vérifiée, une limitation et une prochaine preuve. La validation structurelle passe sans prétendre que le produit réussit. Ce comportement est conforme et montre que validation et preuve peuvent être séparées sans rendre la machine inutile.

## Passage D — constats

### F-ACT-016 — FAST-PATH peut arrêter le run avant son noyau de clôture

- Gravité provisoire : **Significatif**
- État : **ambiguïté opérationnelle confirmée**
- Preuve : lignes 244–246 ordonnent d’arrêter après quatre réponses ; RUN-LITE, HANDOFF et CLOSE-PACKAGE exigent aussi artefact/diff, axes, verdict, owner, réserve ou prochaine action et persistance
- Comportement observable : un lecteur pressé produit décision, risque, preuve et conséquence puis clôt sans paquet reprenable
- Risque : run sans owner, statut, verdict, artefact ou prochaine action ; perte de responsabilité et de mémoire sous couvert de proportionnalité
- Facteur atténuant : FAST-PATH est réservé à LITE et petits ITER ; une ligne de run ou un artefact local préexistant peut transporter les éléments manquants
- Relations : F-DIR-010, F-DIR-013, F-DIR-015, F-ACT-001 et F-ACT-002
- Propriétaires pressentis : ACTION/FAST-PATH pour préciser la condition d’arrêt ; RUN-LITE/CLOSE-PACKAGE pour le noyau non supprimable
- Test futur : correctif local avec et sans ligne de run préalable, owner différent, preuve négative, décision N/A et reprise après interruption

### F-ACT-017 — RISK perd le risque principal et sa protection critique ne gouverne pas la clôture

- Gravité provisoire : **Majeur**
- État : **perte de sens et invariant critique non appliqué confirmés**
- Preuve : ligne 271 exige risque principal et impact potentiel ; le schéma n’accepte que niveau/protection ; un contrôle critique NOT-VERIFIED avec `failure_action: RETURNED` et verdict `ACCEPTED` est validé
- Comportement observable : la carte ne dit pas ce qui peut échouer pour un risque normal/important ; pour un risque critique, elle peut annoncer une action d’échec sans l’exécuter
- Risque : décision sans coût d’erreur compréhensible, automatisation acceptant un danger critique non contrôlé, audit incapable de relier preuve et protection
- Facteur atténuant : owner, scope, contrôle, evidence locator et failure action sont structurés ; limitations et trace externe peuvent conserver le récit complet
- Relations : F-DIR-006, F-DIR-007, F-ACT-002, F-ACT-010 et F-ACT-012
- Propriétaires pressentis : RUN_CARD pour le sens de RISK ; schéma/validateur pour le raccord contrôle → preuve → action
- Test futur : risque normal/important/critique, contrôle PASS/RETURN/NOT-VERIFIED, evidence locator absent ou frais, action RETURNED/BLOCKED/ESCALATED et verdict incompatible

### F-ACT-018 — CAPABILITY-PROFILE n’empêche pas les claims qu’il déclare inobservables

- Gravité provisoire : **Majeur provisoire**
- État : **contradiction humain/machine confirmée**
- Preuve : lignes 284–299 interdisent de présenter comme observée une capacité indisponible ou seulement déclarée ; le validateur relie seulement `available` à une liste `basis` non vide
- Comportement observable : capture indisponible + qualité sur capture observed + ACCEPTED passe ; une déclaration non attestée suffit comme basis ; le profil peut être omis alors que la méthode dépend d’un runtime
- Risque : faux claim d’observation, confiance excessive dans une carte valide, preuve dégradée transformée en acceptation
- Facteur atténuant : la frontière de validation avertit qu’une carte valide ne prouve pas le monde réel ; provenance et limitation sont exigées pour un verdict accepté
- Relations : F-DIR-006, F-DIR-036, F-DIR-037, F-ACT-010 et F-ACT-012
- Propriétaires pressentis : ACTION pour le contrat de capacité ; schéma/validateur pour les relations vérifiables ; trace de preuve pour la méthode réelle
- Test futur : capability disponible/indisponible/non requise × basis attestée/déclarative × méthode/provenance × claim observed/not_verified × verdict

### F-ACT-019 — EXECUTION-SNAPSHOT ne peut pas détecter sa propre péremption

- Gravité provisoire : **Significatif**
- État : **contrat de reprise incomplet confirmé**
- Preuve : lignes 303–317 annoncent démarrage, délégation et reprise, puis expiration sur changement de mode, risque, capacité ou artefact ; la vue omet ID, owner, state, issue, version source, version d’artefact et instant de génération
- Comportement observable : une snapshot ancienne reste indistinguable d’une vue actuelle sans réouvrir manuellement toute la RUN_CARD et reconstruire la comparaison
- Risque : délégation sur décision, capacité ou artefact obsolète ; reprise du mauvais état ; action attribuée au mauvais owner
- Facteur atténuant : `TRACE-LOCATOR` peut ramener à la source canonique et la snapshot se déclare éphémère, sans autorité propre
- Relations : F-DIR-003, F-DIR-006, F-DIR-036 et F-ACT-002
- Propriétaires pressentis : ACTION pour l’identité et la fraîcheur de la vue ; RUN_CARD pour la source
- Test futur : snapshot puis changement de mode, risque, capacité, artefact ou owner ; reprise par un autre agent ; locator déplacé ; comparaison de versions

### F-ACT-020 — TRACE-LOCATOR obéit à trois règles incompatibles selon le niveau de validation

- Gravité provisoire : **Significatif**
- État : **divergence prose/schéma/strict confirmée**
- Preuve : ligne 273 autorise l’artefact comme locator en LITE et exige la trace pour ITER persistant ; schéma/validation normale n’exigent rien pour LITE/ITER ; validation stricte exige `trace_locator` pour tous les modes
- Comportement observable : le même LITE sans trace passe en normal et échoue en strict ; un ITER potentiellement persistant passe en normal sans trace
- Risque : pipelines incohérents, LITE inutilement alourdi en strict, ITER impossible à reprendre en normal, résultat dépendant de la commande choisie
- Facteur atténuant : la validation stricte vise une livraison plus inspectable et peut légitimement demander davantage, mais cette élévation n’est pas documentée comme profil distinct
- Relations : F-DIR-036, F-ACT-001, F-ACT-002 et F-ACT-016
- Propriétaires pressentis : ACTION/RUN_CARD pour la règle par mode ; validateur CLI pour les profils normal/strict
- Test futur : cinq modes × normal/strict × trace présente/absente × artefact local évident × ITER éphémère/persistant

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — routes

FAST-PATH, RUN-LITE et CLOSE-PACKAGE sont résolus. RUN_CARD, STATUS et PRECONDITION restent introuvables. Le défaut ne touche donc pas toutes les sections ACTION, mais précisément plusieurs propriétaires transversaux indispensables à l’interprétation des routes courtes.

### F-ACT-002 et F-DIR-006 — mapping humain / machine / trace

Le bloc confirme définitivement que le mapping n’est pas bijectif : RISK perd son récit, DECISION-CHANGE perd son type, NEXT-ACTION et EXIT-CONDITION restent externes, tandis que sources/proof/limitations deviennent obligatoires côté machine. Les extensions locales sont rejetées dans JSON. La correction devra publier une matrice normative de transport, non ajouter mécaniquement tous les champs au schéma.

### F-ACT-003 — registres

Le champ legacy STATUS est explicitement interdit dans les nouveaux runs et rejeté par le schéma. La séparation state/issue/verdict/direction_status est donc réellement protégée dans cette interface. Le problème de comptage des « quatre registres » du bloc 1 reste éditorial, pas machine.

### F-ACT-009 — verdict avant décision

RUN_CARD confirme que `closure.verdict` appartient au minimum de toute carte, tandis que le cycle ne le produit qu’après CHECKING. `null` n’est pas admis pour ce champ. F-ACT-009 reste Majeur provisoire.

### F-ACT-010 — compatibilités des registres

La règle de preuve dégradée ajoute des dispositions possibles, mais ne fournit toujours pas la matrice issue/verdict/direction/risque. En particulier, `ACCEPTED-WITH-RESERVATION` peut accompagner une preuve obligatoire manquante « selon le risque » sans seuil structuré. F-ACT-010 reste ouvert.

### F-ACT-012 — axe bloquant non structuré

La phrase « ACCEPTED n’est pas disponible lorsque la preuve obligatoire manque » est explicite. Le test critique démontre pourtant qu’ACCEPTED reste validable lorsque le contrôle obligatoire est copié dans `proof.not_verified`. F-ACT-012 est renforcé et sa gravité Majeur provisoire est confirmée.

### F-ACT-013 — conséquence décisionnelle

La table dit que toute RUN_CARD conserve DECISION-CHANGE au minimum, mais le schéma le rend optionnel. Le constat est confirmé et sera rejoué dans RUN-* et CLOSE-PACKAGE.

### F-ACT-014 — NOT-OBSERVED

La projection insiste sur la non-fusion de NOT-OBSERVED, mais ne lui fournit toujours aucun champ ou enum. Le token reste conservable uniquement dans une chaîne ou une trace externe. F-ACT-014 reste confirmé.

### F-ACT-015 — minimum SYSTÈME

RUN_CARD ne possède aucun champ consumers, migration, rollback, non-régression ou CHANGELOG. La lecture complète de RUN_CARD confirme la divergence ; le prochain bloc RUN-SYSTEM/CLOSE-PACKAGE déterminera sa disposition finale.

### F-DIR-036 — mémoire ITER

Le propriétaire ACTION confirme la condition : ITER persistant exige une trace retrouvable. La validation normale accepte pourtant ITER clôturé et accepté sans trace locator ni décision-change. F-DIR-036 est confirmé depuis l’interface propriétaire.

### F-DIR-045 — chemin des limitations

ACTION donne le chemin exact `closure.limitations`. Le schéma l’exige et le validateur rejette son absence pour une acceptation. Le défaut de DIRECTION est donc localisé à sa projection fautive ; ACTION est conforme sur ce point.

## Éléments conformes à préserver

1. FAST-PATH évite les captures, comparaisons et routes sans conséquence.
2. FAST-PATH reste limité à LITE et aux petits ITER.
3. Une responsabilité partagée, identitaire ou critique force une reclassification.
4. RUN_CARD est un format local, non un document canonique concurrent.
5. ID, owner, date/version, mode et décision restent explicites.
6. État, issue, verdict d’axe, statut de direction et verdict global restent séparés.
7. `STATUS` legacy ne peut pas redevenir un champ unificateur.
8. L’issue nulle ne signifie ni réussite ni preuve absente.
9. L’artefact possède un locator et un scope distincts.
10. La trace complète peut rester hors projection si elle demeure retrouvable.
11. Le profil de capacités n’est ni score, ni gate, ni preuve.
12. Disponible, indisponible et non requis sont distingués.
13. Une déclaration non attestée n’est pas présentée comme attestation dans la prose.
14. Une capacité absente réduit la force du claim, pas le mode ou le risque.
15. Une auto-comparaison ne devient jamais un regard indépendant.
16. Sans capture ou runtime réel, aucun PASS perceptuel ou comportemental n’est autorisé.
17. L’absence de regard externe devient limite, réserve et prochaine preuve.
18. Une preuve obligatoire manquante interdit l’acceptation pleine dans le contrat humain.
19. EXECUTION-SNAPSHOT est explicitement dérivée, locale et éphémère.
20. Une snapshot ne crée ni statut, owner, route ou claim.
21. La projection JSON est l’unique exemple structuré canonique.
22. Les taxonomies et statuts parasites sont interdits.
23. La validation de structure est explicitement séparée de la preuve réelle.
24. Chaque claim important doit conserver cible, méthode, scope/runtime, résultat, limite et prochaine preuve.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Trois couches, extensibilité, routes et autorités examinées |
| B — Contrats | FULL | FAST-PATH, quinze champs, mapping JSON, capacité, agent seul, snapshot, projection et frontière de preuve analysés phrase par phrase |
| C — Usage | TARGETED | LITE pressé, risque critique, agent sans navigateur, reprise ITER, snapshot périmée et validation limitée simulés |
| D — Résistance | FULL | Cinq nouveaux constats ACTION et douze familles de constats antérieurs mises à jour |
| Contrôles machine | FULL ciblé | Routes, RISK, criticité, capacités, modes normal/strict, extensions et minima humain/machine testés |

## Point de passage

Le bloc 5 d’ACTION est entièrement lu. Son contrat humain est mature : il sait réduire le rituel, séparer capacité et preuve, borner l’agent seul, interdire les faux claims et expliquer exactement ce qu’une validation ne démontre pas. Les principaux défauts sont des contradictions internes à la projection : FAST-PATH peut s’arrêter trop tôt, RISK perd son contenu, les protections critiques et capacités ne gouvernent pas les claims, la snapshot ne peut détecter sa péremption et TRACE-LOCATOR change de règle selon le validateur.

La prochaine unité est `ACTION.md`, lignes 335–441 : les cinq routes RUN, `ACTION/CLOSE-PACKAGE`, fraîcheur de la preuve, cycle de vie des réserves, responsabilité/droits/confidentialité et condition d’arrêt du polish. Elle devra confronter chaque route au FAST-PATH et à RUN_CARD, confirmer la couverture SYSTÈME, vérifier la péremption de preuve et établir si les réserves possèdent un transport réellement exécutable. Aucun patch n’est autorisé à ce stade.
