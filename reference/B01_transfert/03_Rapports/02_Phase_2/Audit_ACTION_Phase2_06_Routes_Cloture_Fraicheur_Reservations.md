# Audit ACTION — Phase 2, bloc 6 — Routes, clôture, fraîcheur et réserves

## Périmètre examiné

- Source propriétaire : `V1/official/ACTION.md`
- Lignes : 335–441
- Sections :
  - `ACTION/RUN` ;
  - `ACTION/RUN-LITE` ;
  - `ACTION/RUN-ITER` ;
  - `ACTION/RUN-STANDARD` ;
  - `ACTION/RUN-DIRECTION` ;
  - `ACTION/RUN-SYSTEM` ;
  - `ACTION/CLOSE-PACKAGE` ;
  - fraîcheur de la preuve ;
  - cycle de vie des réserves ;
  - responsabilité, droits et confidentialité ;
  - condition d’arrêt du polish.
- Interfaces relues : `ACTION/HANDOFF`, `ACTION/FAST-PATH`, `ACTION/RUN_CARD`, `ACTION/STATUS`, `DIRECTION/START`, `READING_MAP.md`, `CHANGELOG.md`, schéma et validateur `RUN_CARD`.
- Limite : lecture de phase 2, sans verdict global et sans patch.

## Baseline et continuité

| Élément | Valeur vérifiée |
|---|---|
| Audit | `DG-AUDIT-001` |
| Baseline | `B01` |
| Hash système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé | ACTION bloc 5, lignes 242–334 |
| Constats ACTION transportés | F-ACT-001 à F-ACT-020 |
| Patches autorisés | Aucun |

Les empreintes correspondent à B01. La phase 2 du protocole, le plan maître et le rapport ACTION bloc 5 ont été relus avant l’analyse. La source et le protocole n’ont pas changé.

## Résumé du bloc

Le bloc fournit une architecture humaine solide : chaque mode reçoit une entrée, une action, une sortie et une règle de clôture ; le paquet de clôture est proportionné ; la fraîcheur de la preuve, l’ownership final, les droits, la confidentialité et l’arrêt du polish sont explicitement protégés.

La faiblesse principale se situe dans le raccord à la persistance machine. À l’exception de `DIRECTION`, le schéma ne distingue presque pas les paquets de clôture par mode. Les obligations de fraîcheur, de réservation, de droits et d’arrêt ne gouvernent pas effectivement le verdict structuré. Les avertissements humains sont donc meilleurs que les invariants exécutables.

## Passage A — architecture visible

### Organisation

Le bloc suit une progression lisible :

1. cinq routes d’exécution parallèles ;
2. un paquet de clôture proportionné au mode ;
3. quatre protections transversales après production : fraîcheur, réserves, responsabilité/droits/confidentialité et arrêt du polish.

Chaque route reprend la même structure `Entrée → Faire → Sortie → Clôture`. Cette symétrie réduit le coût de lecture et rend les différences de mode comparables. `CLOSE-PACKAGE` évite ensuite de recopier une procédure entière : il indique ce qui doit survivre à la fin du run.

### Résolution des routes

| Locator demandé | Résultat |
|---|---|
| `ACTION/RUN` | Échec — locator absent |
| `ACTION/RUN-LITE` | Résolu |
| `ACTION/RUN-ITER` | Résolu |
| `ACTION/RUN-STANDARD` | Résolu |
| `ACTION/RUN-DIRECTION` | Résolu |
| `ACTION/RUN-SYSTEM` | Résolu |
| `ACTION/CLOSE-PACKAGE` | Résolu |

Les cinq routes utilisables et le paquet de clôture sont donc accessibles. En revanche, la façade d’ouverture d’ACTION conseille de commencer par `ACTION/RUN`, alors que le lecteur de routes ne connaît que les cinq sous-routes. Cette preuve renforce F-ACT-001 sans créer une sixième route.

### Interfaces amont et aval

En amont, `DIRECTION/START` choisit le mode et le risque. En aval, chaque route doit produire un paquet de clôture puis, si la trace est persistante, une `RUN_CARD`. Le prochain bloc ouvre `ACTION/PIPELINE-DIRECTION`, qui détaillera l’exécution de la route DIRECTION.

Cette architecture est correcte sur le papier. Le point fragile est la frontière entre paquet humain, trace externe et projection JSON : elle n’indique pas quelle obligation de chaque mode doit être présente dans la carte elle-même, laquelle peut rester dans la trace et comment le validateur vérifie que le locator contient réellement le paquet attendu.

## Passage B — contrat sémantique

### `RUN-LITE`

L’entrée protège un delta réellement local : système et direction retrouvables, décision dominante connue. L’action reste proportionnée : ligne de run, intention, modification, gates A applicables et preuve B du risque dominant. Le chargement de SAVOIR ou BIBLIOTHEQUE est conditionné à un effet possible sur le correctif.

La sortie demande artefact, axes touchés, diff, verdict, réserve ou prochaine action. La reclassification est explicite lorsque le delta touche une règle partagée, la direction antérieure ou l’identité.

Deux tensions subsistent :

- `RUN-LITE` demande `DECISION-CHANGE` seulement si une décision a changé et `N/A-JUSTIFIED` « lorsque cela est pertinent » ;
- `CLOSE-PACKAGE` exige ensuite `DECISION-CHANGE/N/A-JUSTIFIED` dans tout paquet LITE.

La seconde règle est plus forte, mais la priorité entre elles n’est pas dite. Cette divergence confirme F-ACT-013 et le risque de clôture anticipée de F-ACT-016.

### `RUN-ITER`

La route exige une mémoire antérieure retrouvable, rappelle la direction, produit un diff et vérifie la non-régression pertinente. `RETURNED` conserve le mode lorsque la correction doit être reprise ; `RECLASSIFIED` est réservé à une remise en cause de l’identité, de la portée ou du système.

Le contrat humain est bon. La projection ne possède cependant aucun champ dédié à la direction rappelée, au diff, à la non-régression, au risque restant ou à la cible du nouveau mode. Elle peut seulement renvoyer à une trace libre. F-DIR-036, F-ACT-011, F-ACT-013 et F-ACT-020 restent donc actifs.

### `RUN-STANDARD`

La route différencie correctement un écran ou flow nouveau d’une direction identitaire et d’un changement systémique. Elle appelle `BIBLIOTHEQUE/SELECT` seulement si la structure reste ouverte et impose un premier rendu jugeable plutôt qu’un wireframe volontairement creux.

La sortie demande hiérarchie, typographie, états, axes, verdict, risque restant, prochaine action et conséquence décisionnelle. Ces éléments sont pour l’essentiel absents du schéma `RUN_CARD` comme propriétés distinctes. Le validateur ne peut donc pas déterminer si un STANDARD clôturé respecte son paquet propre.

### `RUN-DIRECTION`

C’est la route la plus riche et la mieux raccordée à la projection. Elle relie positions, alternative, ancre, cible, spec, build, capture, comparaison, gates, statut de direction et creative close. Le schéma possède des protections dédiées pour `direction`, `anchors`, `direction_status`, `trace_locator` et `creative_close`.

Les éléments suivants restent toutefois hors structure dédiée : capture, écarts, gates A/B/C, axes V/U/A/T, risque restant, trace locale des assets et prochaine action générale. La route est donc mieux protégée que les quatre autres, mais elle dépend toujours de chaînes libres et de la trace externe pour une partie de son contrat.

### `RUN-SYSTEM`

Le contrat humain est précis : impact, consumers, décision, owner, migration, rollback, non-régression et entrée CHANGELOG. La clôture n’est permise que lorsque consumers et réserves sont traçables.

Le schéma ne possède aucun champ propre à ces obligations. Une carte `SYSTÈME` générique, clôturée et acceptée, sans impact, consumer, migration, rollback, non-régression, CHANGELOG ni conséquence décisionnelle est valide. Le présent bloc clôt la vérification différée de F-ACT-015 : la divergence est confirmée au niveau de la route propriétaire et du paquet de clôture.

### Comparaison des paquets humains et de la projection

| Mode | Minimum distinctif du bloc | Couverture structurée observable |
|---|---|---|
| LITE | Diff, axes touchés, réserve/prochaine action, décision ou N/A | Pas de diff, axes, réserve ou prochaine action distincte |
| ITER | Direction rappelée, diff, non-régression, risque restant, décision | Aucun de ces éléments n’est dédié ; trace libre possible |
| STANDARD | Hiérarchie, typographie, états, axes, risque restant, prochaine action | Artefact/scope génériques seulement ; pas de profil STANDARD |
| DIRECTION | Direction, ancre/spec, capture, écarts, gates, axes, statut, creative close | Direction, anchors, statut et creative close structurés ; capture/gates/axes/écarts restent externes |
| SYSTÈME | Impact, consumers, owner, migration/rollback, non-régression, CHANGELOG | Owner et locator génériques ; aucun contrat système dédié |

Le schéma fermé interdit aussi d’ajouter librement ces profils. Un transport externe est légitime, mais aucune matrice normative ni contrôle du contenu pointé ne garantit aujourd’hui la conservation du paquet.

### `CLOSE-PACKAGE`

Le principe « livrer l’artefact d’abord, enregistrer le paquet ensuite » évite que la procédure remplace le résultat. La phrase interdisant un PASS implicite pour un paquet incomplet est nette et doit être conservée.

Le paquet DIRECTION reçoit un `creative_close` structuré et effectivement exigé pour une carte clôturée. C’est le meilleur exemple du bloc d’une exigence humaine reliée à un invariant machine. Les autres modes ne disposent pas d’un mécanisme équivalent.

### Fraîcheur de la preuve

Le contrat humain est rigoureux : verdict lié à l’artefact, à la version, au scope et à l’état observés ; retour à `NOT-VERIFIED` après changement substantiel ; conservation des axes non touchés ; réutilisation seulement si l’identité et l’absence de changement pertinent sont établies.

La projection possède une base utile : pour un verdict accepté, `proof.provenance` exige locator, version d’artefact, méthode et date d’observation ; le locator doit correspondre à celui de l’artefact.

Elle ne relie cependant pas :

- `proof.provenance.artifact_version` à la version réellement livrée ;
- la date d’observation à un format ou à une chronologie ;
- le scope observé au scope actuel de l’artefact ;
- une modification substantielle aux axes à réinitialiser ;
- la réutilisation d’une preuve à un contrôle d’identité documenté.

Une carte datée/versionnée `2026-09-22 / V99`, une preuve portant sur `2025-01-01 / V0`, une date d’observation invalide et un scope déclaré comme substantiellement modifié reste `ACCEPTED`. Comme l’artefact ne possède pas de version courante structurée, le validateur n’a même pas de valeur d’autorité à comparer à `proof.provenance.artifact_version`. La présence d’une provenance n’établit donc pas sa fraîcheur.

### Cycle de vie des réserves

La liste `OWNER, SCOPE, DATE/VERSION, IMPACT, NEXT-PROOF, REVIEW-DATE, EXIT-CONDITION` est complète et opérationnelle pour une réserve durable.

Le bloc applique cette structure à quatre objets appartenant à des registres différents :

- `PASS-WITH-RESERVATION` — résultat d’axe ;
- `ACCEPTED-WITH-RESERVATION` — verdict global ;
- `REMAINING-RISK` — issue d’écart ou risque conservé dans la trace ;
- `FAIL-ASSUMED` — issue de run.

Il manque un objet transversal clairement nommé auquel ces registres peuvent rattacher la même réserve sans les fusionner. La `RUN_CARD` ne possède pas de collection `reservations`; `closure.limitations` n’est qu’une liste de chaînes et `next_proof` est global.

Une acceptation avec réserve portant seulement `limitations: ["À revoir."]` et `next_proof: "Plus tard."` est valide. L’ajout d’une réserve structurée avec owner, scope, impact, review date et exit condition est rejeté comme propriété inconnue.

### Responsabilité finale, droits et confidentialité

Le root `owner` est obligatoire dans toute `RUN_CARD`, ce qui protège un responsable final identifiable. Le texte ajoute correctement qu’un protocole ne peut absorber silencieusement un risque critique et qu’une provenance ne vaut pas licence.

Les droits et le canal autorisé ne possèdent cependant aucun transport structuré général. `anchors[].limitation`, `sources`, `proof.provenance` et `closure.limitations` peuvent porter une narration, mais ils ne distinguent pas autorisation, licence, restriction, fallback, donnée personnelle ou canal permis.

Une DIRECTION pleinement `ACCEPTED` dont l’ancre déclare « droits d’utilisation inconnus » et dont la limitation déclare licence, ressemblance de marque et contenu client non vérifiés passe le validateur. Cela contredit le contrat humain selon lequel le doute ne devient pas acceptable par simple mention. Ce constat reste provisoire jusqu’à la lecture de la fiche d’asset, de GATE-B5 et des politiques aval.

### Condition d’arrêt du polish

La règle est excellente : arrêter lorsque le défaut dominant est corrigé ou accepté, les risques couverts ou réservés, et qu’une nouvelle itération ne promet aucun changement utile. Elle interdit le quota, les effets gratuits et la perfection abstraite.

Une tension subsiste avec `creative_close.next_polish_action`, obligatoire pour toute DIRECTION clôturée. Si aucune nouvelle action n’est utile, le contrat ne dit pas explicitement d’y écrire un arrêt justifié. Le champ peut donc encourager une action artificielle ou une formule vide. Le validateur accepte d’ailleurs une prochaine action disant d’ajouter des effets uniquement pour remplir un quota. Ce n’est pas un défaut que le validateur ne juge pas le goût ; le défaut est l’absence d’une sortie canonique `STOP/N/A-JUSTIFIED` pour ce champ obligatoire.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

Exécutée depuis la racine canonique du package :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

Ce PASS décrit les contrôles existants. Il ne couvre pas les contradictions introduites par les mutations ci-dessous.

### Test 1 — routes

```text
ACTION/RUN              FAIL — locator inconnu
ACTION/RUN-LITE         PASS
ACTION/RUN-ITER         PASS
ACTION/RUN-STANDARD     PASS
ACTION/RUN-DIRECTION    PASS
ACTION/RUN-SYSTEM       PASS
ACTION/CLOSE-PACKAGE    PASS
```

### Test 2 — profils de clôture par mode

Des cartes génériques `CLOSED`, acceptées, privées des sorties propres à leur mode ont été validées :

```text
LITE       ACCEPTED — sans diff, axes, réserve/action ni decision_change
ITER       ACCEPTED — sans direction rappelée, diff, non-régression, risque restant, trace ni decision_change
STANDARD   ACCEPTED — sans hiérarchie, typographie, états, axes, risque restant ni decision_change
SYSTÈME    ACCEPTED — sans impact, consumers, migration, rollback, non-régression, CHANGELOG ni decision_change
```

Le test ne prétend pas qu’une projection doit recopier toute la trace. Il établit que ni la carte ni le validateur ne garantissent actuellement que le paquet externe possède ces éléments.

### Test 3 — fraîcheur

```text
RUN_CARD date/version : 2026-09-22 / V99
Preuve : 2025-01-01 / V0
observed_at : date-invalide
Scope : modification substantielle déclarée
Verdict : ACCEPTED
Résultat : ACCEPTED par le validateur
```

Le raccord du locator est contrôlé ; le raccord version/scope/temps ne l’est pas.

### Test 4 — réservation

```text
ACCEPTED-WITH-RESERVATION
limitations = ["À revoir."]
next_proof = "Plus tard."
owner/scope/impact/review-date/exit-condition de la réserve absents
Résultat : ACCEPTED
```

Puis :

```text
reservations = [{owner, scope, date_version, impact, next_proof, review_date, exit_condition}]
Résultat : REJECTED — propriété inconnue
```

### Test 5 — droits et confidentialité

```text
anchors[].limitation = "Droits d’utilisation inconnus."
closure.limitations = ["Licence, ressemblance de marque et contenu client non vérifiés."]
verdict = ACCEPTED
issue = null
Résultat : ACCEPTED
```

### Test 6 — arrêt du polish

```text
dominant_defect = "Aucun défaut dominant restant."
next_polish_action = "Ajouter des effets uniquement pour remplir un quota."
verdict = ACCEPTED
Résultat : ACCEPTED
```

Ce test caractérise l’absence de sortie d’arrêt structurée ; il ne demande pas au validateur d’évaluer automatiquement la qualité artistique.

## Passage C — usages simulés

### Correctif LITE pressé

Le lecteur peut suivre FAST-PATH, produire quatre réponses, appliquer le correctif et considérer le run terminé. `RUN-LITE` et `CLOSE-PACKAGE` demandent davantage, mais la frontière de priorité n’est pas explicitée. Le résultat risque de perdre axes, owner, décision N/A ou prochaine action.

### ITER repris par un autre agent

La direction et le diff existent dans le projet mais aucune trace n’est fournie dans la carte. La validation normale accepte la clôture. Le repreneur ne sait pas quelle non-régression a été exécutée ni quel risque reste.

### STANDARD apparemment complet

Une carte comporte artefact, preuve générique et verdict, mais aucune hiérarchie, aucun état critique et aucun résultat V/U/A/T. Elle valide malgré un paquet STANDARD humain incomplet.

### Changement SYSTÈME partagé

Le composant affecte plusieurs consumers. La carte est clôturée sans liste de consumers, migration, rollback ou test de non-régression. Elle valide, confirmant F-ACT-015 au niveau le plus directement propriétaire.

### Preuve antérieure après modification mobile

Une capture de V0 est conservée après recomposition du viewport mobile en V99. Le texte exige le retour à `NOT-VERIFIED`; la projection accepte `ACCEPTED` tant que le locator est identique et les chaînes sont non vides.

### Réserve sans échéance

Une limite « à revoir » accompagne `ACCEPTED-WITH-RESERVATION`, sans responsable propre, date de revue ni condition de sortie. Le run devient durablement acceptable sans mécanisme de résolution de la réserve.

### Asset aux droits inconnus

La limite est déclarée mais le verdict reste pleinement accepté. Un intégrateur peut prendre la carte verte comme autorisation implicite alors que le texte l’interdit explicitement.

### Polish sans prochaine amélioration utile

Le défaut dominant est résolu, mais le champ obligatoire `next_polish_action` pousse le producteur à inventer une action. Une sortie d’arrêt explicite éviterait ce rituel tout en conservant la décision.

## Passage D — constats

### F-ACT-021 — les paquets de clôture propres aux modes ne gouvernent pas la projection persistante

- Gravité provisoire : **Majeur provisoire**
- État : **divergence humain/machine confirmée**
- Preuve : lignes 339–405 définissent des sorties différentes par mode ; quatre cartes génériques LITE, ITER, STANDARD et SYSTÈME sans leurs sorties distinctives sont validées
- Comportement observable : un verdict vert ne permet pas de savoir si diff, non-régression, hiérarchie, états, consumers, migration ou rollback ont été conservés
- Risque : clôture déclarée conforme alors que le paquet propriétaire est incomplet ; perte de reprise et de non-régression ; automatisation incapable de distinguer les modes autrement que par leur enum
- Facteur atténuant : `trace_locator` peut pointer vers une trace complète ; DIRECTION possède déjà plusieurs invariants spécialisés ; la frontière de validation avertit qu’une carte valide ne prouve pas le monde réel
- Relations : F-ACT-002, F-ACT-006, F-ACT-013, F-ACT-015, F-ACT-016 et F-ACT-020
- Propriétaires pressentis : ACTION/CLOSE-PACKAGE pour le mapping ; RUN_CARD et validateur pour les invariants choisis ; trace externe pour le reste
- Test futur : matrice cinq modes × paquet complet/incomplet × trace présente/absente × normal/strict × verdict

### F-ACT-022 — la fraîcheur déclarée ne relie pas la preuve à la version livrée

- Gravité provisoire : **Majeur**
- État : **invariant de preuve non appliqué confirmé**
- Preuve : lignes 407–411 réinitialisent l’axe après changement substantiel ; une carte datée/versionnée V99 acceptée avec preuve V0, date invalide et scope modifié passe, faute de version courante d’artefact à comparer
- Comportement observable : la présence de `proof.provenance` est prise comme suffisante même lorsque sa version est explicitement antérieure à la livraison
- Risque : ancienne capture, test ou revue réutilisés pour approuver un artefact modifié ; axes non réinspectés présentés comme couverts
- Facteur atténuant : locator, version, méthode et date sont déjà collectés ; le locator de provenance doit correspondre à celui de l’artefact
- Relations : F-ACT-005, F-ACT-009, F-ACT-012, F-ACT-017, F-ACT-019 et F-DIR-034
- Propriétaires pressentis : ACTION/Fraîcheur pour la règle ; RUN_CARD pour l’identité de version/scope ; validateur pour les incompatibilités déterministes
- Test futur : version identique/différente, changement substantiel/hors scope, axes touchés/non touchés, artefact déplacé, date invalide et preuve réinspectée

### F-ACT-023 — le cycle de vie des réserves n’a aucun objet transportable ni contrôle de sortie

- Gravité provisoire : **Majeur**
- État : **lacune de persistance confirmée**
- Preuve : lignes 413–427 exigent sept attributs ; une acceptation avec réserve sans owner propre, scope, impact, review date ou exit condition passe ; une collection structurée `reservations` est rejetée
- Comportement observable : `closure.limitations` et `next_proof` globaux peuvent simuler une réserve, mais ne permettent ni attribution, échéance, revue ni résolution individuelle
- Risque : réserves permanentes ou oubliées, acceptation indéfinie, confusion entre résultat d’axe, verdict, issue et remaining risk
- Facteur atténuant : root owner, limitations et next proof conservent un minimum ; une trace externe peut porter la structure complète
- Relations : F-ACT-002, F-ACT-003, F-ACT-010, F-ACT-012, F-ACT-017 et F-DIR-014
- Propriétaires pressentis : ACTION pour définir un objet de réserve transversal sans créer un statut ; RUN_CARD/trace pour le transport
- Test futur : plusieurs réserves, owners différents, dates échues, réserve résolue, FAIL-ASSUMED, axe PASS-WITH-RESERVATION et verdict accepté avec réserve

### F-ACT-024 — une incertitude explicite de droits ou de confidentialité ne contraint pas le verdict

- Gravité provisoire : **Majeur provisoire**
- État : **contradiction humain/machine confirmée ; disposition différée aux contrats d’asset et gates aval**
- Preuve : lignes 429–435 interdisent l’acceptation par simple mention ; une carte DIRECTION avec droits, marque et contenu client déclarés non vérifiés reste pleinement `ACCEPTED`
- Comportement observable : la limitation est conservée comme texte, mais aucune relation ne force limitation, blocage ou escalade selon le risque
- Risque : prise d’une validation structurelle pour une autorisation de publication, fuite de donnée ou usage d’un asset non licencié
- Facteur atténuant : le texte ordonne explicitement de ne pas envoyer une donnée vers un canal non garanti ; l’application effective dépend aussi d’outils et de politiques externes au schéma
- Relations : F-ACT-010, F-ACT-012, F-ACT-017, F-ACT-018 et F-DIR-037
- Propriétaires pressentis : ACTION pour la conséquence de clôture ; SAVOIR/source et fiche d’asset pour la qualification ; runtime/outillage pour les contrôles de canal
- Test futur : asset fourni/curaté/généré, licence connue/inconnue, ressemblance de marque, donnée personnelle, canal autorisé/interdit, fallback et risque critique

### F-ACT-025 — la clôture DIRECTION exige une prochaine action même lorsque le polish doit s’arrêter

- Gravité provisoire : **Significatif provisoire**
- État : **tension de contrat confirmée**
- Preuve : ligne 405 rend `creative_close.next_polish_action` obligatoire ; lignes 437–439 demandent l’arrêt lorsqu’aucune itération utile n’est probable ; aucune valeur d’arrêt n’est définie
- Comportement observable : le producteur doit inventer une action, employer une phrase libre de stop ou laisser entendre qu’un polish reste requis ; une action de quota est structurellement valide
- Risque : itération rituelle, perfection abstraite, gonflement de trace ou information fausse pour satisfaire un champ
- Facteur atténuant : une chaîne comme `STOP — aucune modification utile attendue` peut déjà porter l’intention sans changement de schéma
- Relations : F-DIR-009, F-DIR-046, F-ACT-013 et F-ACT-016
- Propriétaires pressentis : ACTION/CLOSE-PACKAGE et condition d’arrêt ; RUN_CARD uniquement si une sortie typée est retenue
- Test futur : défaut corrigé, défaut accepté, action disproportionnée, réserve ouverte, aucune action utile et nouvelle preuve nécessaire sans polish

## Mises à jour des constats antérieurs

### F-ACT-001 — entrée ACTION/RUN

Les cinq sous-routes et CLOSE-PACKAGE sont résolubles, mais `ACTION/RUN` ne l’est pas alors que la responsabilité d’ACTION le désigne comme point de départ. Le constat reste ciblé sur une façade non routée et plusieurs propriétaires transversaux absents.

### F-ACT-002 — mapping trace / RUN_CARD

Le bloc ajoute diff, non-régression, hiérarchie, états, impact, consumers, migration, rollback, review date et exit condition sans mapping machine. F-ACT-021 et F-ACT-023 en isolent les conséquences de clôture et de réserve.

### F-ACT-009 — temporalité du verdict

Toutes les routes placent correctement la décision puis la clôture après exécution et observation. Cela renforce la preuve que le verdict final ne devrait pas être obligatoire dans une carte précoce. Le défaut reste ouvert.

### F-ACT-010 et F-ACT-012 — compatibilités et blocage

Le paquet incomplet ne doit recevoir aucun PASS implicite et les doutes de droits ne deviennent pas acceptables par mention. Les tests montrent pourtant que les obligations absentes ou explicitement non vérifiées ne gouvernent pas systématiquement le verdict. Les deux constats sont renforcés.

### F-ACT-013 — conséquence décisionnelle

LITE hésite entre une conséquence conditionnelle et une décision/N/A obligatoire dans le paquet. ITER et STANDARD demandent aussi une décision, tandis que les cartes correspondantes valident sans `decision_change`. Le constat reste confirmé.

### F-ACT-015 — minimum SYSTÈME

RUN-SYSTEM et CLOSE-PACKAGE répètent le minimum impact/consumers/migration/rollback/non-régression/CHANGELOG. Le test de carte générique confirme son absence totale du contrôle machine. La gravité **Majeur provisoire** est maintenue et la disposition différée au bloc RUN_CARD est maintenant achevée.

### F-ACT-016 — FAST-PATH et clôture

RUN-LITE et CLOSE-PACKAGE démontrent que les quatre réponses de FAST-PATH ne suffisent pas toujours à une clôture reprenable. Le raccourci reste utile, mais sa condition d’arrêt doit distinguer décision locale et run clôturé.

### F-ACT-019 et F-ACT-022 — péremption

La snapshot ne peut pas comparer sa propre version ; la RUN_CARD collecte une provenance sans établir sa fraîcheur. Les deux constats sont complémentaires : vue de reprise périmable d’un côté, preuve périmée encore acceptable de l’autre.

### F-ACT-020 et F-DIR-036 — persistance ITER

RUN-ITER suppose une mémoire antérieure retrouvable, mais une carte ITER clôturée sans `trace_locator` reste valide en mode normal. Le bloc confirme la nécessité d’une règle de persistance cohérente.

## Éléments conformes à préserver

1. Les cinq routes sont symétriques et proportionnées.
2. Chaque route distingue entrée, action, sortie et clôture.
3. LITE reclassifie dès qu’une responsabilité partagée ou identitaire apparaît.
4. ITER vérifie la non-régression pertinente plutôt qu’une checklist universelle.
5. STANDARD vise un premier rendu jugeable et non un wireframe creux.
6. DIRECTION construit et observe une scène réelle avant clôture.
7. SYSTÈME nomme consumers, migration, rollback et non-régression.
8. L’artefact est livré avant le paquet procédural.
9. Un paquet incomplet ne reçoit aucun PASS implicite dans la prose.
10. Le creative close reste descriptif et ne devient ni score ni verdict esthétique.
11. La provenance minimale d’une preuve acceptée est déjà structurée.
12. Un changement substantiel invalide uniquement les axes touchés.
13. Le déplacement seul d’un artefact n’invalide pas mécaniquement sa preuve si son identité est contrôlée.
14. Toute réserve durable possède owner, scope, version, impact, prochaine preuve, revue et condition de sortie.
15. Les registres d’axe, verdict, issue et risque restant ne doivent pas être fusionnés.
16. Un owner final demeure responsable malgré les contributions multiples.
17. La provenance ne vaut jamais licence.
18. Une limitation de preuve n’autorise jamais le partage d’un contenu sensible.
19. Le polish s’arrête sur l’utilité marginale réelle, pas sur un quota.
20. Une action disproportionnée peut devenir réserve plutôt qu’itération artificielle.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Cinq routes, paquet, protections transversales et locators examinés |
| B — Contrats | FULL | Entrées, actions, sorties, clôtures, fraîcheur, réserves, droits et polish analysés phrase par phrase |
| C — Usage | TARGETED | Sept scénarios de run, reprise, preuve, réserve, asset et polish simulés |
| D — Résistance | FULL | Cinq nouveaux constats et dix familles antérieures consolidés |
| Contrôles machine | FULL ciblé | Routes, quatre modes génériques, fraîcheur, réserve, droits, polish et suite officielle testés |

## Point de passage

Le bloc 6 d’ACTION est entièrement lu. Il possède de très bonnes règles humaines de proportion, fraîcheur, responsabilité et arrêt. Les principaux défauts sont désormais localisés dans la persistance : paquets de mode non contrôlés, preuve ancienne encore acceptable, réserves sans cycle exécutable, incertitudes de droits sans effet obligatoire et prochaine action de polish exigée même lorsque l’arrêt est correct.

La prochaine unité est `ACTION.md`, lignes 443–525 : `ACTION/PIPELINE-DIRECTION`, boucle de qualité et branche one-shot, positions, émotion, alternative, spec, sourcing, sélection, décision, vérification du rendu et passe créative/polish. Elle devra confronter la boucle exécutable à `DIRECTION/DOUBLE-LOOP`, vérifier les conditions réelles du one-shot, la place du checkpoint humain, la transformation des ancres et la conséquence observable des corrections. Aucun patch n’est autorisé à ce stade.
