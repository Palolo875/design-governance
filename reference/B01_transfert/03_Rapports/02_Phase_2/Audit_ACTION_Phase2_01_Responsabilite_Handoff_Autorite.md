# DG-AUDIT-001 — Phase 2 — ACTION, bloc 1

## Périmètre examiné

- Cible : `V1/official/ACTION.md`
- Bloc : lignes 1–77 de la reconstruction de travail
- Sections : titre et positionnement, responsabilité, carte de lecture par mode, `ACTION/HANDOFF`, quatre registres, ordre de preuve, frontières documentaires, chargement, `ACTION/AUTHORITY`, parcours minimal en cinq minutes
- Interfaces vérifiées : `DIRECTION/START`, `DIRECTION/CREATIVE-BOOT`, `ACTION/STATUS`, `ACTION/PRECONDITION`, `ACTION/RUN_CARD`, les cinq routes `ACTION/RUN-*`, `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`, `READING_MAP`, schéma et validateur `RUN_CARD`, lecteur et validateur de routes
- Source d’observation : compilation `Design_Governance_V1.0.md`, reconstruction de travail et baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison des propriétaires, simulation de lecteurs humains et outillés, inspection du schéma, exécution de la suite officielle, tests de résolution des locators et tests ciblés de projection
- Statut : diagnostic sectionnel provisoire ; aucun verdict global sur ACTION et aucun patch du corpus

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole, le checkpoint consolidé DIRECTION et le plan maître ont été relus avant le bloc. Les constats DIRECTION transportés en priorité sont F-DIR-003, F-DIR-006, F-DIR-008, F-DIR-009, F-DIR-010, F-DIR-013, F-DIR-015, F-DIR-017, F-DIR-024, F-DIR-028, F-DIR-030, F-DIR-031, F-DIR-034, F-DIR-035 et F-DIR-045.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 1–9 | Définir ACTION comme propriétaire de l’exécution probante et de la clôture | Owner net ; expérimentation déclarée ; chemin positif de construction et d’amélioration | L’entrée recommandée `ACTION/RUN` n’est pas résoluble par le lecteur officiel |
| 11–21 | Réduire le chargement selon les cinq modes | Une route et une sortie sont données pour chaque mode ; FAST-PATH n’est pas un sixième mode | Plusieurs sections demandées sont absentes de READING_MAP ; `STATUS` et `PRECONDITION` ne sont chargés que pour LITE/ITER malgré leur portée générale |
| 23–35 | Définir un handoff commun et une condition d’arrêt de lecture | Mode, décision, risque, preuve, limite, owner et reprise sont réunis ; les sorties incomplètes ne sont pas surqualifiées | Le mapping vers `RUN_CARD` n’est pas explicite ; `NEXT-ACTION` et `EXIT-CONDITION` n’existent pas dans le schéma ; plusieurs labels avec `/` fusionnent des notions distinctes |
| 37–50 | Séparer navigation, preuve, décision et persistance ; ordonner les protections | Observation, interprétation, décision et persistance sont distinguées ; risque critique prioritaire ; P1 non négociable | La phrase d’ouverture et le tableau ne nomment pas les mêmes quatre registres |
| 52–67 | Délimiter les propriétaires et l’autorité d’action | Frontières DIRECTION/SAVOIR/BIBLIOTHEQUE/CHANGELOG nettes ; capacité ≠ autorisation ; `APPROVED` ≠ acceptation | `ACTION/AUTHORITY` n’est pas résoluble ; les éléments d’autonomie ne sont pas explicitement mappés vers une projection persistante |
| 69–77 | Donner une façade d’exécution en cinq minutes | Premier rendu jugeable, observation réelle, correction ou acceptation raisonnée, persistance | `DIRECTION/CREATIVE-BOOT` est appelé comme route mais rejeté par le lecteur ; la façade dépend donc d’une recherche manuelle ou du chargement complet de START |

## Passage A — architecture visible

Le début d’ACTION possède une architecture conceptuelle convaincante. Il répond successivement à six questions utiles : qui possède la livraison et la preuve ; quelle route charger ; quelle sortie transporter ; quels registres ne pas confondre ; qui peut agir ; comment démarrer en cinq minutes. Cette progression donne à ACTION une fonction positive : produire un objet observable et améliorable, pas seulement appliquer des gates.

La carte de lecture par mode est également une bonne façade de réduction. Elle évite d’exiger le pipeline DIRECTION complet pour un delta local et rappelle que `FAST-PATH` est une vue locale, non une voie supplémentaire. La condition d’arrêt de lecture est particulièrement saine : on arrête lorsque mode, risque, route, preuve, limite, owner et prochaine action sont connus, et on ne charge un bloc supplémentaire que s’il peut modifier l’un de ces éléments.

L’architecture outillée ne soutient toutefois pas complètement cette façade.

Premièrement, la responsabilité demande de commencer par `ACTION/RUN`, mais ce locator n’existe pas dans READING_MAP et le lecteur officiel le rejette.

Deuxièmement, les routes LITE et ITER exigent `STATUS` et `PRECONDITION`, mais ces deux sections ne sont pas enregistrées comme locators. Le lecteur peut les retrouver par recherche de titre ou en lisant le fichier linéairement, pas par le chemin court annoncé.

Troisièmement, les modes STANDARD, DIRECTION et SYSTÈME omettent `STATUS` et `PRECONDITION` de leur chargement minimal, alors que ces sections définissent le vocabulaire canonique, les capacités, la preuve et le contrat minimal des cinq modes. Le problème subsisterait donc même si tous les locators étaient ajoutés : la carte elle-même ne transporte pas les mêmes préconditions vers les modes à plus fort blast radius.

Quatrièmement, la route DIRECTION demande `PIPELINE-DIRECTION`, `VISUAL_PROOF` et les gates A/B/C. Seul `GATE-A` est résolu directement par le lecteur. `PIPELINE-DIRECTION`, `VISUAL_PROOF`, `GATE-B` et `GATE-C` échouent.

Cinquièmement, `RUN_CARD`, `CLOSE-PACKAGE` et `CLOSE-EXIT-CHECK` sont présentés comme des ajouts conditionnels. La persistance rend clairement `RUN_CARD` applicable, mais la formule « lorsque la clôture l’exige » ne dit pas dans cette façade que `CLOSE-EXIT-CHECK` est le test canonique avant toute clôture. La ligne 77 conserve les conditions détaillées, ce qui limite le risque sans rendre le chemin court autonome.

L’échec des locators relève du constat systémique F-DIR-028, qui avait précisément décidé de ne pas créer un nouvel ID par route manquante. L’incomplétude sémantique de la carte par mode est distincte et reçoit un constat ACTION propre.

## Passage B — contrat sémantique

### Responsabilité et capacité positive

La responsabilité d’ACTION est nette : preuves exécutables, gates, statuts de run, verdicts et clôture. Cette propriété est cohérente avec DIRECTION, qui classe et route, et avec SAVOIR, qui possède les principes de jugement et de craft.

La capacité positive est un point fort. Le chemin :

```text
construire → observer → isoler le défaut dominant → corriger ou accepter avec raison → prouver → clôturer
```

empêche ACTION de devenir une police de conformité détachée de la qualité produite. La qualité du premier rendu, la lisibilité de la décision et la reprise du run sont reconnues comme valeur livrée. La possibilité « corriger ou accepter avec raison » protège aussi le one-shot valide : aucune modification décorative n’est imposée lorsque l’observation ne promet pas de gain.

### Carte de lecture par mode

Les cinq modes restent alignés sur `DIRECTION/START`. ACTION ne crée donc pas de classification concurrente. Les sorties proposées sont proportionnées : delta et preuve locale pour LITE/ITER ; hiérarchie et états pour STANDARD ; ancre, capture et écarts pour DIRECTION ; consumers, migration et rollback pour SYSTÈME.

La colonne « Sortie à conserver » ne se présente cependant pas explicitement comme un résumé non exhaustif. Elle omet selon les modes plusieurs éléments que `ACTION/HANDOFF` déclare communs à toute sortie : owner, limite, prochaine preuve, condition de sortie ou décision. Un lecteur pressé peut raisonnablement interpréter chaque cellule comme le minimum suffisant du mode, puis ne jamais reconstruire le handoff commun.

Cette divergence confirme le problème des formes minimales concurrentes sans prouver encore quelle forme doit disparaître. Une correction éventuelle devra préférer un noyau commun et des extensions par mode plutôt qu’une nouvelle table.

### ACTION/HANDOFF

Le handoff commun constitue une amélioration substantielle par rapport aux vues DIRECTION : il rassemble décision, risque, scope, artefact, méthode, preuve, limite, changement réel, owner, prochaine preuve et condition de sortie. Il interdit aussi de présenter une préparation ou clarification courte comme preuve complète.

Le contrat humain n’est néanmoins pas mappé sans perte vers la projection déclarée pour les runs persistants.

| Élément HANDOFF | Projection plausible | État du mapping |
|---|---|---|
| `MODE` | `run_card.mode` | Exact |
| `DECISION` | `run_card.decision` | Exact |
| `RISK` | `run_card.risk` | Le texte court devient un objet structuré |
| `SCOPE` | `run_card.artifact.scope` | Possible, mais scope de run et scope d’artefact peuvent diverger |
| `ARTIFACT` | `run_card.artifact.locator` | Plausible |
| `OBSERVATION/METHOD` | `proof.observed` + `proof.provenance.method` | Le `/` masque deux destinations et la provenance n’est requise que dans certains cas |
| `PROOF/TRACE-LOCATOR` | `proof` + `trace_locator` | Deux notions et deux niveaux distincts |
| `LIMIT/NOT-VERIFIED` | `closure.limitations` + `proof.not_verified` | Limite et absence de preuve ne sont pas synonymes |
| `DECISION-CHANGE` | `run_card.decision_change` | Exact en intention, structure objet côté machine |
| `NEXT-ACTION` | — | Aucun champ générique dans le schéma |
| `OWNER` | `run_card.owner` | Exact |
| `NEXT-PROOF` | `run_card.next_proof` | Exact |
| `EXIT-CONDITION` | — | Aucun champ dans le schéma |

Le schéma interdit les propriétés supplémentaires. Une implémentation littérale de `next_action`, `exit_condition`, `observation_method` ou `limit` est donc rejetée. Ces éléments peuvent vivre dans une trace externe référencée par `trace_locator`, mais ACTION ne dit pas ici lesquels sont internes, externes ou dérivés, ni comment un consommateur doit les résoudre.

Le problème ne signifie pas que tous les éléments doivent devenir des champs JSON. Il signifie que le handoff doit distinguer : mapping exact, transformation structurée, information externe retrouvable et information non projetée volontairement.

La temporalité reste également importante. Le bloc s’appelle une « sortie minimale commune » et contient `DECISION-CHANGE`, alors que DIRECTION utilise aussi le terme handoff pour la mémoire de lancement. ACTION précise plus loin que le changement ne peut être déclaré qu’après observation. La frontière lancement / sortie / clôture doit donc rester explicite afin qu’un champ de sortie ne soit pas prérempli comme preuve au démarrage.

### Les quatre registres

La section veut séparer des notions qui sont effectivement différentes. Le tableau `Observation → Interprétation → Décision → Persistance` est cohérent : il distingue ce qui a été regardé, ce que cela permet de conclure, ce qui est décidé et où la décision demeure inspectable.

La phrase immédiatement précédente annonce pourtant une autre série : `route → preuve → décision → persistance`. Route n’est pas observation ; preuve ne distingue pas observation et interprétation ; le tableau ne possède aucune ligne route. La phrase finale affirme que « ces quatre registres » structurent la trace sans lever l’antécédent.

Deux lectures sont donc possibles :

1. route, preuve, décision, persistance sont les quatre registres et le tableau les détaille mal ;
2. observation, interprétation, décision, persistance sont les quatre registres et la phrase d’ouverture décrit seulement un ordre de navigation.

La seconde lecture paraît la plus cohérente, mais elle est inférée. Un système d’action ne devrait pas demander au lecteur de deviner si la route appartient à la trace ou si preuve est un registre unique.

La séparation ultérieure de `STATE`, `ISSUE`, verdict d’axe, statut de direction et verdict global est en revanche claire et doit être préservée.

### Ordre de preuve et frontières

L’ordre P0–P3 récapitule correctement la hiérarchie définie dans DIRECTION et SAVOIR. Il refuse deux erreurs symétriques : sacrifier une protection critique au craft, ou présenter une interface techniquement conforme comme réussie lorsque direction et tâche ne tiennent pas. La priorité du risque dominant empêche l’ordre visuel nominal de devenir rigide.

Les frontières documentaires sont nettes : DIRECTION classe et route ; SAVOIR possède jugement et intégrité ; BIBLIOTHEQUE possède la structure ; CHANGELOG possède l’évolution. ACTION garde preuve, gates, statuts et clôture. La phrase sur les recettes, prompts, packages et stacks est également probatoirement saine : une ressource ou une méthode disponible n’est pas une preuve exécutée.

Le terme « contrat court » pour LITE et ITER n’est toutefois pas défini localement. Il peut désigner la ligne de run, le handoff, FAST-PATH, le contrat minimal de PRECONDITION ou leur combinaison. Cette ambiguïté est enregistrée sous la carte de chargement plutôt que comme constat autonome à ce stade.

### ACTION/AUTHORITY

La distinction entre capacité et autorisation est robuste. ACTION demande de déclarer la portée d’action, la base de l’autonomie, la condition de reprise ou d’escalade et le rôle qui reprend la décision. `APPROVED` est borné à une autorisation dans un scope ; il ne vaut ni acceptation, ni preuve, ni clôture.

Le comportement en cas de checkpoint indisponible répond directement à F-DIR-017 : aucune baisse silencieuse de mode ; la décision devient exploratoire, retournée ou escaladée selon le risque et la preuve. La terminologie devra encore être confrontée aux registres canoniques — issue `RETURNED`, verdict `RETURN`, issue `ESCALATED`, verdict `SYSTEM-ESCALATION` — mais la protection de fond est correcte.

La section affirme que les éléments d’autorité restent dans la trace existante, sans dire où ils sont projetés. Cette lacune est reliée au mapping de handoff et ne reçoit pas un ID séparé.

### Parcours minimal en cinq minutes

Le parcours est actionnable et correctement orienté vers l’objet réel. Il reprend mode et risque ; formule l’intention ; construit un premier rendu suffisamment résolu ; observe l’artefact plutôt que la rationale ; puis corrige, retourne, réserve ou accepte et persiste la décision.

Il protège le one-shot : l’étape finale autorise l’acceptation après observation, et la façade ne demande pas une itération pour elle-même. Il protège aussi le craft initial en exigeant un premier objet composé, crédible et spécifique lorsque la décision visuelle est ouverte.

Le renvoi `DIRECTION/CREATIVE-BOOT` n’est pas résoluble sous ce nom. Son contenu se trouve à l’intérieur du bloc `DIRECTION/START`, que le lecteur sait ouvrir. Un lecteur humain complet peut donc récupérer la règle ; un agent qui exécute littéralement le locator échoue. Cela étend F-DIR-028 sans créer un nouveau constat local.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle complète

`validate_all.py` passe : package, documents, schémas, fixtures, contrats, distributions, CLI et reproductibilité sont validés.

Ce résultat confirme l’intégrité de la baseline. Il ne prouve pas que tous les locators normatifs écrits dans ACTION sont présents dans READING_MAP, ni que le handoff humain possède un mapping exhaustif vers le schéma.

### Test 1 — routes directement exploitables du bloc

Résultats positifs pertinents :

```text
DIRECTION/START          PASS
ACTION/RUN-LITE          PASS
ACTION/RUN-ITER          PASS
ACTION/RUN-STANDARD      PASS
ACTION/RUN-DIRECTION     PASS
ACTION/RUN-SYSTEM        PASS
BIBLIOTHEQUE/SELECT      PASS
ACTION/GATE-A            PASS
ACTION/CLOSE-PACKAGE     PASS
ACTION/CLOSE-EXIT-CHECK  PASS
```

Les routes principales par mode et les deux routes de clôture enregistrées sont donc accessibles.

### Test 2 — locators demandés mais inconnus

Le lecteur officiel rejette :

```text
ACTION/RUN
ACTION/STATUS
ACTION/PRECONDITION
ACTION/RUN_CARD
ACTION/HANDOFF
ACTION/AUTHORITY
ACTION/PIPELINE-DIRECTION
ACTION/VISUAL_PROOF
ACTION/GATE-B
ACTION/GATE-C
DIRECTION/CREATIVE-BOOT
```

Tous ces titres ou sous-sections existent dans les sources. L’échec porte sur leur résolution par le chemin de lecture officiel, pas sur leur absence documentaire.

### Test 3 — fidélité de projection du handoff

Le schéma expose au niveau `run_card` :

```text
anchors, artifact, capability_profile, closure, creative_close,
date_version, decision, decision_change, decision_intent, direction,
id, mode, next_proof, owner, profile_decision, proof, risk,
sources, trace_locator
```

Deux mutations ciblées ont été soumises au validateur :

```text
next_action + exit_condition    REJECTED — champs inconnus
observation_method + limit      REJECTED — champs inconnus
```

Le rejet est conforme à `additionalProperties: false`. Il confirme l’absence de mapping littéral ; il ne demande pas automatiquement l’ajout de quatre champs.

### Test 4 — angle mort de la validation de lecture

`validate_reading_map.py` passe alors que les onze locators ci-dessus échouent. Le validateur contrôle les routes déclarées dans sa table fermée, pas l’ensemble des quasi-locators et instructions de chargement réellement écrits dans les propriétaires normatifs.

## Passage C — usages simulés

### Correctif local LITE sous contrainte de temps

Le lecteur ouvre `ACTION/RUN-LITE`, mais la carte lui demande aussi `STATUS` et `PRECONDITION`. Le lecteur officiel ne résout pas ces deux noms. Un humain peut faire une recherche textuelle ; un agent strict doit soit charger tout ACTION, soit abandonner le chemin minimal. La réduction de charge annoncée n’est donc pas reproductible par l’outil fourni.

### Nouvelle surface STANDARD

La carte envoie le lecteur vers `RUN-STANDARD`, BIBLIOTHEQUE si structure ouverte et gates ciblés. Elle ne lui demande ni STATUS ni PRECONDITION, bien que PRECONDITION définisse le contrat STANDARD et que STATUS possède les états et verdicts. Le lecteur obtient une bonne route de construction mais peut manquer le vocabulaire de preuve et de clôture.

### Direction identitaire

Le chemin demande pipeline, preuve visuelle et gates A/B/C. RUN-DIRECTION et GATE-A sont résolubles ; quatre autres éléments échouent. La direction peut encore être reconstruite par lecture du fichier complet, mais la façade conditionnelle ne tient pas son contrat outillé.

### Handoff persistant vers un consommateur machine

Le producteur tente de transporter tous les éléments communs. S’il ajoute `next_action` et `exit_condition` à la RUN_CARD, le schéma les rejette. S’il les omet, le consommateur ne sait pas où les retrouver sans convention externe. S’il les place dans `proof.observed` ou `closure.limitations`, il mélange action, preuve et limite. Le bon comportement exige un mapping que le bloc ne fournit pas.

### Reviewer séparant fait et jugement

Le tableau observation/interprétation/décision/persistance aide le reviewer à ne pas confondre ce qui a été vu avec ce qui en est conclu. La phrase route/preuve/décision/persistance l’oblige toutefois à décider si route est une donnée de trace et si interprétation est contenue dans preuve.

### Checkpoint d’autorité indisponible

Le run ne rétrograde pas silencieusement. Il conserve risque et preuve disponible, puis devient exploratoire, retourné ou escaladé. Ce comportement est protecteur et fournit une base de correction à la façade EXTERNAL-START de DIRECTION.

### Premier rendu excellent sans correction utile

Le lecteur observe l’objet, ne laisse pas la rationale le remplacer, puis peut accepter avec raison. La méthode n’impose pas une seconde version décorative. Le chemin positif est donc compatible avec une boucle one-shot réelle.

## Passage D — constats

### F-ACT-001 — la carte de chargement minimal n’est ni entièrement résoluble ni complète selon le mode

- Gravité provisoire : **Significatif**
- État : **confirmé dans le bloc 1**
- Preuve : lignes 7 et 13–21 ; `ACTION/RUN`, `STATUS`, `PRECONDITION`, `PIPELINE-DIRECTION`, `VISUAL_PROOF`, `GATE-B`, `GATE-C` et `RUN_CARD` ne sont pas tous résolubles ; STANDARD, DIRECTION et SYSTÈME omettent STATUS/PRECONDITION malgré leur portée générale
- Comportement observable : un lecteur outillé ne peut pas exécuter le chargement minimal annoncé ; un lecteur des modes à fort impact peut ne pas charger les préconditions et statuts propriétaires
- Risque : réduction de charge non reproductible, clôture ou preuve reconstruite depuis des résumés incomplets, chargement forcé du fichier entier
- Facteur atténuant : les cinq routes RUN principales existent ; la lecture linéaire ou une recherche de titre permet de retrouver les sections ; la ligne 77 maintient les contrats détaillés
- Relations : occurrences de F-DIR-028 pour les échecs de locator ; manifestation de F-DIR-008 et F-DIR-010 pour les pertes de minimum
- Propriétaires pressentis : ACTION pour le contrat de chargement ; READING_MAP et lecteur pour les locators réellement promis
- Test futur : un scénario par mode, exécuté uniquement avec READING_MAP et `read_route.py`, puis comparaison des sections chargées au contrat minimal propriétaire

### F-ACT-002 — le handoff commun n’a pas de mapping sans perte vers `RUN_CARD`

- Gravité provisoire : **Significatif**
- État : **confirmé sur le contrat humain et le schéma courant**
- Preuve : lignes 23–33 ; `NEXT-ACTION` et `EXIT-CONDITION` n’existent pas dans le schéma ; `OBSERVATION/METHOD`, `PROOF/TRACE-LOCATOR` et `LIMIT/NOT-VERIFIED` fusionnent des destinations distinctes ; le schéma rejette les propriétés littérales supplémentaires
- Comportement observable : sérialisation littérale invalide, omission silencieuse ou placement ad hoc dans un champ sémantiquement voisin
- Risque : décision impossible à reprendre, condition de sortie perdue, limite confondue avec absence de preuve, trace humaine et machine divergentes
- Facteur atténuant : `trace_locator` peut référencer une trace complète ; plusieurs correspondances exactes existent ; ACTION précise plus loin les chemins `artifact`, `proof` et `closure`
- Relations : confirme F-DIR-006, F-DIR-008, F-DIR-010 et la nécessité révélée par F-DIR-045
- Propriétaires pressentis : ACTION pour le mapping sémantique ; schéma seulement si une information doit réellement être projetée plutôt que conservée dans la trace externe
- Test futur : handoff LITE non persistant, RUN_CARD STANDARD persistante, DIRECTION clôturée, run sans changement de décision, réserve avec exit condition et reprise par un autre agent

### F-ACT-003 — deux ensembles différents sont appelés « quatre registres »

- Gravité provisoire : **Significatif provisoire**
- État : **ambiguïté interne confirmée**
- Preuve : ligne 39 annonce route/preuve/décision/persistance ; lignes 41–46 définissent observation/interprétation/décision/persistance ; aucune relation de dérivation n’est fournie
- Comportement observable : un lecteur persiste la route mais pas l’interprétation, ou considère preuve comme un bloc unique et mélange fait observé et conclusion
- Risque : traçabilité épistémique affaiblie, lecture non reproductible, mapping machine arbitraire
- Facteur atténuant : les sorties du tableau sont claires et la lecture observation → interprétation → décision → persistance est cohérente avec le reste d’ACTION
- Relation : renforce F-DIR-033 sans s’y réduire, car le conflit est interne au propriétaire ACTION et porte sur ses propres registres
- Propriétaire pressenti : ACTION
- Test futur : une observation ambiguë, une interprétation révisée, une décision inchangée et une reprise de run par un lecteur n’ayant pas participé à l’observation

## Mises à jour des constats DIRECTION transportés

### F-DIR-003 — temporalité du handoff

ACTION précise que son chargement commence dès qu’un build, une vérification ou un changement d’état est engagé, et appelle son bloc commun une sortie de run. Cela fournit une borne utile, mais DIRECTION emploie aussi handoff pour une mémoire de lancement et ACTION inclut `DECISION-CHANGE`, qui n’existe qu’après observation. Le constat reste ouvert ; F-ACT-002 en fournit l’interface exacte.

### F-DIR-006, F-DIR-008 et F-DIR-010 — mapping, invariants et formes minimales

ACTION améliore le noyau commun avec HANDOFF, mais la carte par mode, le handoff, la ligne de run, RUN_CARD et les paquets de clôture ne sont pas explicitement reliés champ par champ. F-ACT-002 confirme le mapping incomplet ; F-ACT-001 confirme que les minima chargés diffèrent selon la façade. Les trois constats restent ouverts et significatifs.

### F-DIR-009 — modification imposée au one-shot

Le chemin positif et l’étape 5 autorisent explicitement « corriger ou accepter avec raison ». ACTION ne requiert donc pas une modification lorsqu’aucun gain réel n’est attendu. Cette lecture atténue F-DIR-009 et fournit la règle propriétaire à préserver ; le constat DIRECTION reste ouvert jusqu’à réconciliation de Creative Boot et FIRST-OBJECT.

### F-DIR-013 et F-DIR-015 — clôture courte et `DECISION-CHANGE`

HANDOFF exige limite, owner, prochaine preuve et condition de sortie ; il transporte aussi `DECISION-CHANGE`. Ces éléments corrigent conceptuellement les pertes des façades DAILY et FAST-PATH. Leur bénéfice dépend toutefois du chargement réel du handoff et de son mapping. Les constats restent ouverts jusqu’à l’audit de FAST-PATH et des paquets de clôture.

### F-DIR-017 — checkpoint pré-build indisponible

`ACTION/AUTHORITY` interdit explicitement la réduction silencieuse du mode et exige une sortie exploratoire, retournée ou escaladée selon le risque. La protection propriétaire est présente. F-DIR-017 est fortement atténué, mais la façade EXTERNAL-START et la terminologie exacte des registres doivent encore être alignées.

### F-DIR-024 — objet et preuve

ACTION distingue artefact, observation, méthode, preuve et trace, puis précise que recettes, prompts, packages et intégrations ne sont jamais des preuves à eux seuls. Le propriétaire confirme donc la séparation recherchée. Le label « objet de preuve » de DIRECTION devra être interprété comme objet à observer, non comme preuve déjà obtenue.

### F-DIR-028 — couverture du lecteur de routes

Onze locators supplémentaires écrits ou demandés par le bloc sont rejetés par `read_route.py`. La suite officielle et `validate_reading_map.py` restent vertes. F-DIR-028 est confirmé et sa future matrice de fixtures doit inclure toutes ces occurrences sans créer onze constats dupliqués.

### F-DIR-030 et F-DIR-031 — propriété du craft et début de l’action

La frontière SAVOIR/ACTION est nette : SAVOIR possède jugement et craft ; ACTION possède observation, preuve, correction et clôture. ACTION commence lorsqu’un build, une vérification ou un changement d’état est engagé, ce qui laisse l’intake et la clarification préalables possibles. Ces règles donnent une base de correction solide aux formulations DIRECTION, sans effacer leurs occurrences locales.

### F-DIR-034, F-DIR-035 et F-DIR-045 — preuve minimale, registres et limite structurée

Le bloc réaffirme la séparation des statuts et l’existence d’un handoff commun, mais sa propre taxonomie de registres est ambiguë et le mapping de `LIMIT` reste implicite. Le schéma confirme que la limite machine vit sous `closure.limitations`. Ces constats restent ouverts ; F-ACT-002 et F-ACT-003 ajoutent leurs manifestations propriétaires.

## Éléments conformes à préserver

1. ACTION possède clairement preuve exécutable, gates, statuts, verdicts et clôture.
2. V1 est explicitement présentée comme expérimentation, non comme release stabilisée.
3. Le chemin positif part de la construction et de l’observation, pas du contrôle pour lui-même.
4. Une correction n’est requise que si elle promet un gain réel ; l’acceptation raisonnée reste possible.
5. La carte distingue les cinq modes et refuse de créer un sixième mode FAST-PATH.
6. La condition d’arrêt de lecture réduit le cérémonial sans réduire la protection.
7. Une sortie incomplète reste préparation ou clarification, pas preuve complète.
8. Observation, interprétation, décision et persistance sont utilement séparées dans le tableau.
9. State, issue, verdict d’axe, statut de direction et verdict global ne sont pas synonymes.
10. Le risque critique passe avant l’optimisation visuelle.
11. P1 reste non négociable sans être présenté comme preuve de réussite globale.
12. Les propriétaires DIRECTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG sont correctement bornés.
13. Une ressource technique, un prompt ou une recette n’est pas une preuve à lui seul.
14. Une capacité ne vaut pas autorisation de décider.
15. `APPROVED` ne vaut ni acceptation, ni preuve complète, ni clôture.
16. Un checkpoint manquant ne baisse jamais silencieusement le mode.
17. Le parcours cinq minutes exige un objet réel et empêche la rationale de remplacer l’observation.
18. La façade reste subordonnée aux contrats détaillés et aux conditions de clôture.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Responsabilité, carte de mode, ordre des façades, condition d’arrêt et résolubilité inspectés |
| B — Contrats | FULL | Chaque phrase normative des lignes 1–77 comparée aux propriétaires, sections ACTION et projection machine |
| C — Usage | TARGETED | LITE, STANDARD, DIRECTION, handoff machine, reviewer, autorité et one-shot simulés |
| D — Résistance | FULL | Trois nouveaux constats ACTION et mises à jour des dépendances DIRECTION enregistrés |
| Contrôles machine | FULL ciblé | Suite officielle, 21 routes pertinentes, schéma, mutations de projection et angle mort du validateur contrôlés |

## Point de passage

Le bloc 1 d’ACTION est entièrement lu. Il établit un propriétaire solide, une excellente orientation positive et des frontières d’autorité protectrices. Ses défauts principaux portent sur l’exécution de la façade de lecture, le mapping du handoff et la cohérence du nom des registres, non sur l’intention générale du pipeline.

La prochaine unité est `ACTION.md`, lignes 79–112 : `ACTION/FIRST-RENDER` et `ACTION/UI-UX-REALITY`. Elle devra vérifier la qualité initiale par mode, la frontière entre ambition de rendu et preuve, la couverture des états réels, l’adaptation au médium et la classification en cas de capacité manquante. Aucun patch n’est autorisé à ce stade.
