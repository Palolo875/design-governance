# ACTION — Pipeline de livraison & preuves

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. ACTION transforme une direction ou une décision produit en trace de run, artefacts observables, preuves adaptées, gates proportionnés et verdicts inspectables.

## Responsabilité

`ACTION` est le propriétaire des preuves exécutables, des gates, des statuts de run, des verdicts et de la clôture. Pour une lecture rapide, commencez par `ACTION/RUN`, puis chargez seulement la route du mode et les gates correspondant au risque déclaré. `ACTION/FAST-PATH` est une vue de formalité réduite pour un delta local ; il ne supprime ni la preuve requise ni l’honnêteté du statut.

**Capacité positive d’ACTION.** ACTION ne sert pas seulement à filtrer ou accepter un résultat : elle transforme une direction en livraison observable et améliorable. Son chemin positif est **construire → observer → isoler le défaut dominant → corriger ou accepter avec raison → prouver → clôturer avec une limite et une prochaine preuve**. Les gates protègent ce chemin ; ils ne sont pas sa finalité. La qualité du premier rendu, la lisibilité de la décision et la possibilité de reprendre le run font partie de la valeur livrée.

### Carte de lecture par mode

| Mode | Chargement minimal dans ACTION | Sortie à conserver |
|---|---|---|
| `LITE` | `STATUS`, `PRECONDITION`, `RUN-LITE`, gates applicables | Artefact, risque, preuve, limite et prochaine action. |
| `ITER` | `STATUS`, `PRECONDITION`, `RUN-ITER`, non-régression pertinente | Diff, preuve du risque touché et décision. |
| `STANDARD` | `STATUS`, `RUN-STANDARD`, `BIBLIOTHEQUE/SELECT` si la structure est ouverte, gates ciblés | Artefact, hiérarchie, états, preuve et risque restant. |
| `DIRECTION` | `RUN-DIRECTION`, `PIPELINE-DIRECTION`, `VISUAL_PROOF`, gates A/B/C | Direction, ancre/spec, capture, écarts, verdict et prochaine preuve. |
| `SYSTÈME` | `RUN-SYSTEM`, puis `CHANGELOG` pour adoption ou migration | Décision, consumers, owner, migration, rollback et non-régression. |

Les sections `RUN_CARD`, `CLOSE-PACKAGE` et `CLOSE-EXIT-CHECK` s’ajoutent lorsque la trace est persistante ou que la clôture l’exige. `FAST-PATH` n’est pas une sixième voie : chaque occurrence de ce nom reste une vue locale du propriétaire qui l’emploie.

### ACTION/HANDOFF — sortie minimale commune

`ACTION` est propriétaire de la preuve, des gates, des statuts, des verdicts et de la clôture. Les façades peuvent préparer un handoff, mais toute sortie de run doit rendre résolubles les éléments suivants :

```text
MODE — DECISION — RISK — SCOPE — ARTIFACT
OBSERVATION/METHOD — PROOF/TRACE-LOCATOR — LIMIT/NOT-VERIFIED
DECISION-CHANGE — NEXT-ACTION — OWNER — NEXT-PROOF — EXIT-CONDITION
```

Ce bloc réutilise les champs existants ; il ne crée ni statut, ni gate, ni nouveau schéma. Les champs non applicables sont marqués `N/A-JUSTIFIED`. Un run persistant utilise la projection `RUN_CARD` et son validateur. Une sortie courte qui ne peut pas fournir ces éléments reste une préparation, une clarification ou une décision non clôturée ; elle ne doit pas être présentée comme une preuve complète.

**Condition d’arrêt de lecture :** arrêter lorsque le mode, le risque, la route, la preuve, la limite, le propriétaire et la prochaine action sont connus. Charger un registre, une route ou un gate supplémentaire uniquement s’il peut modifier l’un de ces éléments.

### Les quatre registres à ne pas mélanger

Pour naviguer dans ACTION, lire dans cet ordre : **route** pour savoir quoi faire ; **preuve** pour savoir ce qui a été observé et peut être affirmé ; **décision** pour savoir quoi changer, accepter, réserver ou retourner ; **persistance** pour rendre la décision, sa limite et sa prochaine preuve inspectables. Ces quatre registres structurent la trace ; ils ne créent ni états ni statuts supplémentaires.

| Registre | Question | Sortie minimale |
|---|---|---|
| **Observation** | Qu’est-ce qui a été regardé, par quelle méthode, dans quel scope et quelle version ? | Artefact, méthode, scope, version, date et capacité. |
| **Interprétation** | Que montre réellement l’observation, avec quelle couverture et quelle limite ? | Relation, effet, défaut dominant, incertitude et limite. |
| **Décision** | Que fait-on maintenant et pourquoi ? | Correction, retour, acceptation, réserve, reclassification ou escalade. |
| **Persistance** | Où la décision et ses limites restent-elles inspectables ? | `RUN_CARD`, trace locator, owner, prochaine preuve et condition de sortie. |

`STATE`, `ISSUE`, verdict d’axe, statut de direction et verdict global ne sont jamais des niveaux de maturité ni des synonymes. Le JSON Schema est l’autorité de structure de la projection ; les exemples YAML et textuels restent des vues de transport ou d’explication.

**Ordre de preuve.** Vérifie d’abord le risque dominant. Pour une surface identitaire sans risque critique, vérifie que la direction `P0` et le craft visuel sont réellement tenus ; vérifie ensuite le plancher `P1` d’usage et d’accessibilité ; adapte `P2` au runtime et à la plateforme réels ; déclenche `P3` pour la robustesse, la performance, la compatibilité et le maintien lorsque le risque le requiert. En présence d’un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité, la protection critique passe avant l’optimisation visuelle. P1 est non négociable, mais aucun gate ne transforme une interface conforme en interface réussie si la décision visuelle et la tâche ne tiennent pas.

ACTION ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Rôle, cinq absolus, classification, routage général et cadrage de capacité. |
| `SAVOIR.md` | Principes de jugement, craft, styles, contexte, outils et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, changements futurs, pilotes optionnels et décisions de gouvernance. |

**Chargement.** Dès qu’un build, une vérification ou un changement d’état est engagé, charge ACTION au niveau requis par le mode. Le contrat court suffit en `LITE` et `ITER`. Le pipeline et les gates complets sont chargés lorsque le périmètre les déclenche. Les recettes de code, prompts, packages et intégrations de stack sont des ressources techniques ; ils ne constituent jamais une preuve à eux seuls.

### ACTION/AUTHORITY — portée d’action et reprise

Une capacité indique ce qui peut être construit ou vérifié ; elle ne constitue pas une autorisation de décider. Lorsque l’agent, l’outil ou l’équipe agit au nom d’un owner, déclare seulement si cela peut changer la décision, le risque, la persistance ou une action externe : la portée d’action autorisée, la base de cette autonomie, la condition de reprise ou d’escalade, et le rôle qui reprend la décision si nécessaire. Ces éléments restent dans la trace existante d’ACTION ; ils ne créent ni état, ni issue, ni verdict, ni gate supplémentaire.

Un checkpoint indisponible ne réduit pas silencieusement le mode. Il rend la décision exploratoire, retournée ou escaladée selon le risque, la preuve disponible et la condition de sortie. `APPROVED`, lorsqu’un transport ou une trace le mentionne, signifie seulement qu’une décision d’autorité a été autorisée dans son scope ; il ne signifie ni résultat accepté, ni preuve complète, ni clôture.

### Parcours minimal en cinq minutes

1. Reprends le mode et le risque classés dans `DIRECTION/START`.
2. Formule `DECISION-INTENT`, déclare l’artefact, le scope, les capacités et la prochaine preuve ; pour une décision visuelle ouverte, active `DIRECTION/CREATIVE-BOOT` avant le build.
3. Construis un premier rendu suffisamment complet et jugeable pour le mode ; lorsque la décision visuelle est ouverte, il doit déjà être composé, crédible, spécifique et résolu à la bonne échelle, et rendre observables l’objet, la tension et les cibles créatives du boot.
4. Observe le rendu réel sans laisser la rationale remplacer l’objet ; inscris l’interprétation, les qualités prioritaires effectivement visibles ou non observées, le défaut dominant et la limite.
5. Corrige, résous, retourne, réserve ou accepte ; persiste `DECISION-CHANGE`, la preuve, l’owner et la prochaine action.

Ce parcours est une façade de lecture, non une procédure concurrente. Les contrats détaillés, les gates et les conditions de clôture restent applicables dès que le risque ou le mode les déclenche.

## ACTION/FIRST-RENDER — qualité initiale attendue

Le premier rendu n’est pas une simple ébauche destinée à être rendue présentable plus tard. Lorsqu’un run produit une surface, un composant, un flow ou une scène, le premier artefact doit déjà être **composé, crédible, spécifique au produit et suffisamment résolu pour être jugé comme un objet réel**, dans la proportion du mode et du risque. Le slop est un risque possible, mais la cible positive est la qualité : présence, hiérarchie, typographie, contenu, états, matière ou retenue, relation à la preuve et finition pertinente.

| Mode | Qualité initiale attendue au premier rendu |
|---|---|
| `LITE` | Le delta est propre, lisible, cohérent avec le système et ne dégrade pas le rendu existant. |
| `ITER` | Le delta est visible, intentionnel, fidèle à la direction retrouvable et inspectable dans les états touchés. |
| `STANDARD` | La vue ou le flow est déjà composé : contenu crédible, hiérarchie, typographie, états pertinents, responsive applicable et finition suffisante pour juger la proposition. |
| `DIRECTION` | La première scène porte déjà la présence, le point de vue, la composition, la typographie, la matière ou la retenue, l’objet de preuve et l’intégration d’asset nécessaires à la décision. |
| `SYSTÈME` | Le composant ou token est montré dans ses usages réels, avec baseline, états, consommateurs et risque de régression identifiables. |

Un rendu peut rester `EXPLORATORY` lorsqu’une preuve manque, mais ce statut ne justifie pas un artefact volontairement creux lorsque les capacités nécessaires sont disponibles. La qualité initiale est une cible de construction, non un score et non un verdict esthétique.

### ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble

Pour une surface UI/UX nouvelle ou substantiellement modifiée, le premier objet doit rendre observables, dans la proportion du mode et du risque : hiérarchie de contenu, premier geste, feedback, états `loading`, `empty`, `error`, `unavailable`, `disabled` et succès partiel lorsque pertinents, contenu long ou multilingue, responsive recomposé, focus et récupération. Une capture de l’état nominal ne suffit pas lorsque l’état, la tâche ou la récupération fait partie de la décision.

Le contrat de production relie :

```text
CONTENT-MODEL: données et hiérarchie réellement portées
PRIMARY-TASK: tâche et résultat attendu
FIRST-GESTURE: action initiale et feedback associé
CRITICAL-STATES: états, erreurs, permissions et récupération applicables
RESPONSIVE-RELATION: ce qui est préservé, recomposé ou remplacé selon le viewport
ACCESSIBILITY-BASIS: sémantique, nom, focus, clavier, contraste et alternative selon le risque
ROBUSTNESS-BASIS: contenu extrême, chargement, compatibilité, performance ou non-régression selon le risque
PROOF-SCOPE: surface, état, viewport, données, population ou runtime réellement observé
```

Ces lignes décrivent les décisions de construction et la couverture attendue ; elles ne créent pas un nouveau gate ni un formulaire universel. `ACTION` garde les preuves, les limites et le verdict ; `SAVOIR/CONTEXT` et `SAVOIR/TECH` sont chargés seulement lorsque leurs questions peuvent modifier le prochain artefact. Lorsque la capacité nécessaire manque, déclare `NOT-VERIFIED` ou l’issue appropriée au lieu de réduire silencieusement l’ambition de protection.

**Source de classification.** Le mode est classé par `DIRECTION/START`. ACTION ne reclassifie pas silencieusement une tâche parce qu’une capacité, un outil ou une preuve manque. Il déclare alors la limite, le statut et la prochaine preuve.

---

## ACTION/STATUS — états, issues et verdicts

Cette section définit le vocabulaire canonique d’ACTION. Les documents voisins peuvent expliquer ces statuts, mais ne doivent pas créer de synonymes concurrents.

### États du run

| État | Entrer lorsque… | Quitter lorsque… |
|---|---|---|
| `INTAKE` | La demande est reçue, mais périmètre ou inconnue restent ouverts. | Mode, décision dominante, risque et prochaine preuve sont connus. |
| `CLASSIFIED` | La ligne de run et le mode sont nommés. | Le build direct est autorisé ou le contrat/spec requis existe. |
| `SPECCED` | Direction, hiérarchie, contrat ou ancre nécessaires sont disponibles. | Le build peut commencer. |
| `BUILDING` | L’artefact est en production. | Les contrôles applicables peuvent être exécutés. |
| `CHECKING` | Capture, tests, comparaison, gates ou regard pertinent sont en cours. | Verdicts, réserves et prochaine action sont déclarés. |
| `DECIDED` | Le verdict et le compromis sont connus. | La trace est persistée, clôturée, retournée ou escaladée. |
| `CLOSED` | Artefact et trace minimale sont persistés. | Une nouvelle demande ou une reprise `ITER` commence. |

`CLOSED` décrit la persistance et la clôture de la trace ; il ne signifie ni réussite, ni preuve complète, ni acceptation globale. Il peut coexister avec une issue `RETURNED`, `EXPLORATORY` ou `BLOCKED`, et avec un verdict global `RETURN`, `EXPLORATORY` ou `SYSTEM-ESCALATION` lorsque la limite, la reprise ou l’escalade est conservée dans la trace.

### Issues et exceptions

| Issue | Signification |
|---|---|
| `BLOCKED` | Une condition nécessaire manque ; l’owner et la prochaine preuve sont nommés. |
| `RETURNED` | Le run revient à une étape antérieure pour corriger un écart ou obtenir une preuve dans le même mode. |
| `RECLASSIFIED` | Le périmètre ou le risque impose un autre mode. |
| `EXPLORATORY` | Un rendu observable existe, mais une preuve requise manque encore. |
| `FAIL-ASSUMED` | Un échec connu est explicitement journalisé et diffusé dans un périmètre limité et temporaire. |
| `ESCALATED` | Une décision, un owner, un droit, une capacité ou un risque dépasse le périmètre du run. |

### Règle de lecture des statuts

ACTION sépare strictement : **état du run**, **issue**, **verdict V/U/A/T**, **statut de direction** et **verdict global**. Il n’existe pas de plan de « maturité » à renseigner par défaut.

> **Plans à ne pas confondre.** `A/B/C` désignent les gates de contrôle ; `V/U/A/T` désignent les axes de questions et de preuve. Ils ne sont ni interchangeables ni combinés en un nouveau statut.

Un statut de direction décrit la fidélité de la direction dans le rendu. Un verdict global décrit la possibilité d’accepter, de retourner, d’explorer ou d’escalader le run dans son périmètre. `HELD` ne produit donc pas automatiquement `ACCEPTED`.

Si une équipe doit suivre un handoff ou une archive, elle le fait dans son outil de projet sans créer un statut concurrent du run.

### Chemin minimal

`DIRECTION` classe le mode et le risque ; `ACTION` conserve la trace, obtient la preuve adaptée et clôt le run. Pour un delta local, garde la ligne de run et le contrôle proportionné. N’ajoute une route, une capture ou un contrat que si cela peut modifier la décision ou lever une incertitude déclarée.

### Principe positif de qualité

La méthode ne vise pas seulement à éviter une sortie générique. Elle prépare et construit une proposition qui peut être belle, ambitieuse, spécifique et cohérente dès le premier rendu. Avant le build, déclare la relation produit à rendre perceptible, le niveau de résolution attendu et le défaut dominant à éviter. Après le build, juge cette intention sur l’artefact réel. Un rendu one-shot peut être clôturé après la première observation si la qualité attendue est atteinte, les risques sont couverts et aucune correction ne promet un gain réel ; il ne peut jamais être clôturé sans observation du rendu.


### Verdicts V/U/A/T

V/U/A/T est une **taxonomie interne de questions et de preuves**. Elle n’est pas une nomenclature normative externe.

| Axe | Couvre | Statuts autorisés |
|---|---|---|
| **V — caractère visuel** | Point de vue, hiérarchie, typographie, composition, matière et retenue. | `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED`, `NOT-VERIFIED`. |
| **U — compréhension / usage** | JTBD, architecture, parcours, action critique, contenu, états et résultats de tâche. | Même liste. |
| **A — accessibilité / conformité** | Contraste, clavier, focus, cibles, sémantique, information non chromatique, motion et technologies d’assistance selon le périmètre. | Même liste. |
| **T — robustesse technique** | Média, responsive, performance, chargement, erreur, intégration et non-régression. | Même liste. |

Le verdict global est l’un des suivants : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Il nomme toujours le risque ou conflit le plus important. Aucune moyenne ne compense un axe bloquant.

### Statut de direction

| Statut | Signification |
|---|---|
| `HELD` | La direction se retrouve dans le rendu sans écart majeur non résolu. |
| `HELD-WITH-ACCEPTED-DIFFERENCE` | L’écart est explicite, utile et préserve l’axe touché autrement. |
| `PARTIALLY-HELD` | Une partie de la direction est affaiblie ou non résolue. |
| `LOST-IN-BUILD` | Le rendu ne porte plus la direction retenue. |

`HELD` signifie fidèle à la direction et approprié au contexte ; il ne signifie ni « beau », ni « préféré », ni accepté globalement, ni validé sur U, A ou T.

---

## ACTION/PRECONDITION — mode, capacité et preuve

Le mode est classé dans `DIRECTION/START`. Le type de tâche et son blast radius déterminent le mode ; les capacités disponibles déterminent la voie de preuve, le statut de vérification et la possibilité de livrer. Une capacité absente ne rétrograde jamais silencieusement une tâche `DIRECTION`.

| Mode | Contrat ACTION minimal |
|---|---|
| **LITE** | Intention, artefact touché, gates A applicables, `Gate B` du risque dominant, axes `V/U/A/T` concernés et réserve ou prochaine action. |
| **ITER** | Direction retrouvable, diff, non-régression du périmètre, Gate A applicable, Gate B du risque touché et Gate C seulement si le craft change. |
| **STANDARD** | JTBD, arbitrage, hiérarchie, typographie, états pertinents, Gates A et B ciblés ; ancre ou asset seulement si le risque le requiert. |
| **DIRECTION** | Alternative située lorsque nécessaire, ancre utile, cible, build, capture, comparaison, gates A/B/C, trace locale des assets pertinents, statut de direction et V/U/A/T. |
| **SYSTÈME** | Impact, consumers, décision, owner, migration, rollback, non-régression et entrée CHANGELOG. |

Un gate non applicable est `N/A-JUSTIFIED`. Un gate nécessaire mais non vérifiable est `NOT-VERIFIED`, jamais `PASS` par défaut.

### Contrat de décision et de preuve

Au lancement, la `RUN_CARD` contient :

```text
DECISION-INTENT — décision que la procédure doit permettre de trancher.
```

Après une observation qui modifie, confirme ou abandonne effectivement une décision, la trace contient :

```text
DECISION-CHANGE — décision effectivement changée, confirmée ou abandonnée grâce au run.
```

Si aucune décision ne change, la clôture utilise `N/A-JUSTIFIED` lorsque cela est justifié, avec la raison et la prochaine preuve éventuelle. Ne déclare jamais un changement avant qu’une observation ne l’ait rendu réel.

### Trace post-build de `DIRECTION/EXTERNAL-START`

Lorsque `DIRECTION/EXTERNAL-START` a été activée, conserve après le premier artefact ou la première capture, dans la trace existante et sans créer de nouveau statut :

```text
DECISION-CHANGE — ce que le démarrage a effectivement changé, confirmé ou abandonné.
OMISSION-AVOIDED — omission concrète évitée, ou NOT-OBSERVED.
REMAINING-LIMIT — limite persistante après le premier artefact.
```

Ces trois lignes ne sont pas un gate supplémentaire. Elles vérifient que la vue de démarrage a changé une décision, rendu une omission visible ou exposé une limite. Si aucune conséquence n’est obtenue, utilise `N/A-JUSTIFIED` ou `NOT-OBSERVED` dans la trace existante ; ne transforme pas le préflight en rituel.

### Raccord de trace pour la section `DESIGN-ATLAS` de `SAVOIR.md`

Lorsque la section `DESIGN-ATLAS` de `SAVOIR.md` est chargée, ses champs de présélection restent des éléments locaux de décision et ne remplacent pas la `RUN_CARD`. Elle n’est appelée qu’après classification, décision et risque ; si aucune famille ne peut modifier la prochaine décision, elle n’est pas chargée. Avant le build, `DECISION-MODIFIED`, `WHEN-USEFUL`, `COUNTERINDICATION`, `MEDIUM-SCOPE` et `PROOF-LIMIT` décrivent une hypothèse de sélection, non une observation indépendante. Une rationale, une cible visuelle, une ancre, une référence ou la présence d’un asset ou d’un composant ne prouve ni l’implémentation, ni l’utilité, ni la qualité, ni l’accessibilité, ni l’efficacité.

Après observation, la sortie canonique est `DECISION-CHANGE` si la décision a effectivement changé, été confirmée ou abandonnée ; sinon, utilise `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable ou `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. Seul un résultat observé dans le scope déclaré peut alimenter `DECISION-CHANGE` et un verdict. Le polish visuel peut soutenir une revue perceptuelle, mais ne devient pas une preuve de tâche, d’usage, de performance ou d’accessibilité exécutée. `WHY-NOW` et `REUSE-CHALLENGE` sont ajoutés lorsque la famille ou le profil est repris d’un run précédent. Aucun de ces éléments ne crée un nouveau mode, gate, statut, score ou formulaire.

Pour réduire le slop procédural, préfère une proposition principale et une alternative située seulement lorsqu’elle peut changer une décision. Produis ou conserve un détail, un asset, une variante ou une rationale seulement si sa conséquence sur l’artefact, la preuve, la limite ou la prochaine action est identifiable.

---

## ACTION/FAST-PATH — preuve minimale sans rituel

Pour `LITE` et les petits `ITER`, arrête le protocole après quatre réponses : décision touchée, risque dominant, preuve la moins coûteuse et conséquence de la preuve.

Si aucune décision ne peut changer, n’ajoute pas de capture, comparaison ou route uniquement pour remplir le paquet. Journalise `N/A-JUSTIFIED` lorsque la procédure ne peut rien modifier.

Reviens à un mode plus riche si le changement touche une règle partagée, l’identité, la sécurité, l’accessibilité, le comportement critique ou une décision coûteuse.

---

## ACTION/RUN_CARD — carte de run minimale

La `RUN_CARD` est un format local extensible, non un document canonique séparé. Elle peut vivre dans un ticket, un manifeste, un espace de travail ou un fichier local.

Quel que soit son support, elle conserve au minimum :

| Champ | Contenu |
|---|---|
| `ID` | Identifiant du run. |
| `OWNER` | Responsable de la décision, de la reprise ou de l’escalade. |
| `DATE / VERSION` | Date, version et contexte de preuve. |
| `MODE` | Route de run classée par `DIRECTION/START`. |
| `STATE` | `INTAKE`, `CLASSIFIED`, `SPECCED`, `BUILDING`, `CHECKING`, `DECIDED` ou `CLOSED`. |
| `ISSUE` | `BLOCKED`, `RETURNED`, `RECLASSIFIED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED`, si applicable ; `null` si aucune issue n’est déclarée. |
| `VERDICT` | Verdict global uniquement dans la projection `RUN_CARD` : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Les verdicts V/U/A/T restent dans leur registre d’axes et dans la trace de preuve ; ils ne sont jamais rangés dans ce champ. |
| `DIRECTION-STATUS` | Statut de fidélité de la direction : `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE`, `PARTIALLY-HELD` ou `LOST-IN-BUILD`, si applicable. |
| `DECISION` | Décision dominante à prendre ou à vérifier. |
| `DECISION-INTENT` | Décision que la procédure doit permettre de trancher. |
| `DECISION-CHANGE` | Décision effectivement changée, confirmée ou abandonnée ; `N/A-JUSTIFIED` si aucune conséquence n’est obtenue ou attendue. |
| `RISK` | Risque principal et impact potentiel. |
| `ARTIFACT` | Lien vers rendu, code, capture, test ou diff. |
| `TRACE-LOCATOR` | URL, chemin, ticket, commit ou identifiant qui rend la trace et ses artefacts réinspectables. Requis en `STANDARD`, `DIRECTION`, `SYSTÈME` et `ITER` persistant ; en `LITE`, l’artefact localement évident peut servir de locator. |
| `NEXT-PROOF` | Preuve suivante attendue. |

Dans la projection JSON contrôlable, les noms composés sont sérialisés en `snake_case` : `DATE / VERSION` devient `date_version`, `DIRECTION-STATUS` devient `direction_status`, `TRACE-LOCATOR` devient `trace_locator`, `NEXT-PROOF` devient `next_proof` et `CAPABILITY-PROFILE` devient `capability_profile`. Cette sérialisation ne change pas la signification canonique des champs.

La projection imbrique les champs de run sous `run_card` et regroupe l’état de clôture sous `closure` : `STATE` devient `closure.state`, `ISSUE` devient `closure.issue`, `VERDICT` devient `closure.verdict`, `DIRECTION-STATUS` devient `closure.direction_status` et les limites deviennent `closure.limitations`. `ARTIFACT` devient `artifact.locator` et son périmètre devient `artifact.scope` ; les observations et absences de preuve deviennent `proof.observed` et `proof.not_verified`. Les axes V/U/A/T qui ne sont pas sérialisés dans cette projection restent dans la trace complète référencée par `trace_locator` ou dans le paquet de preuve. Cette table de correspondance est descriptive : le schéma livré et le validateur restent les autorités de structure et de contrôle.

`STATUS` peut rester lisible comme alias d’archive ou d’affichage pour compatibilité avec des traces existantes. Il est interdit dans une nouvelle `RUN_CARD` comme champ unificateur : les nouveaux runs utilisent séparément `STATE`, `ISSUE`, `VERDICT` et `DIRECTION-STATUS`. Aucun alias ne remplace cette séparation.

### Profil de capacités

Quand une conclusion dépend d’un moyen d’observation, la `RUN_CARD` ajoute un `CAPABILITY-PROFILE` concis : **disponible**, **indisponible** ou **non requis**. Déclare seulement les capacités pertinentes au risque : artefact textuel, inspection DOM/CSS, navigateur/capture, calcul de contraste, clavier/AT, participant/tâche, runtime/données réelles. Toute capacité qui soutient un claim ajoute sa `BASIS` : résultat d’outil, environnement attesté, source utilisateur ou déclaration non attestée.

Ce profil n’est ni un score, ni un gate, ni une preuve. Il sert à empêcher qu’une vérification absente soit rédigée comme accomplie. Une `BASIS` déclarative ne vaut pas attestation ; elle interdit seulement de présenter la capacité comme observée. Une capacité indisponible conduit à la preuve disponible la plus faible ou à `NOT-VERIFIED`; elle ne réduit jamais silencieusement le mode, le risque ou le verdict requis.

### Mode agent seul et preuve dégradée

Lorsque le run est exécuté par un agent sans regard indépendant, sans capture réelle ou sans runtime vérifiable, applique les limites suivantes. Ce mode ne constitue ni un nouveau mode de run, ni une permission de réduire le niveau de protection ; il rend seulement explicite le niveau de conclusion atteignable avec les capacités présentes.

| Capacité disponible | Ce que l’agent peut faire | Ce qu’il ne peut pas conclure seul |
|---|---|---|
| Runtime et capture réels, sans second regard | Construire, capturer, comparer et corriger l’artefact ; documenter une auto-comparaison. | Une revue indépendante, aveugle ou externe ; une calibration complète d’une décision identitaire importante. |
| Pas de capture ou de runtime réel | Formuler une hypothèse, préparer l’artefact et déclarer la preuve attendue. | Une qualité perceptuelle observée, un `PASS` de rendu ou une preuve de comportement non exécuté. |
| Pas de regard externe lorsque B3 est dans le scope | Conserver la capture, la comparaison, la limite, la réserve et la prochaine preuve. | Étiqueter l’auto-comparaison comme regard indépendant, comparatif ou aveugle. |
| Capacité manquante sur un risque critique | Déclarer la limite, nommer l’owner et préparer `NEXT-PROOF`. | Rétrograder silencieusement le mode, le risque ou le verdict requis. |

Une auto-comparaison B1b peut soutenir une correction de craft, mais elle ne satisfait jamais un claim de revue indépendante. Si une preuve obligatoire manque, le run reste `NOT-VERIFIED` sur l’axe concerné et adopte l’issue ou le verdict approprié — notamment `EXPLORATORY`, `RETURN-DIRECTION`, `ACCEPTED-WITH-RESERVATION` ou `ESCALATED` — selon le périmètre et le risque. `ACCEPTED` n’est pas disponible lorsque la preuve obligatoire manque.

### Vue d’exécution dérivée

Une `EXECUTION-SNAPSHOT` peut être construite pour démarrer, déléguer ou reprendre un run. C’est une vue locale et éphémère de la `RUN_CARD` et des sections canoniques ; elle ne remplace ni ACTION, ni les sources qu’elle cite. Elle expire lorsqu’un mode, un risque, une capacité ou un artefact change.

```text
MODE — valeur classée par DIRECTION/START
DECISION / RISK — choix à trancher et coût d’erreur
SOURCES — sections canoniques réellement nécessaires
CAPABILITIES — disponible / indisponible / non requis
CAPABILITY-BASIS — résultat d’outil / environnement attesté / source utilisateur / déclaration non attestée, si une capacité soutient un claim
FACTS — artefacts et observations déjà fournis
AXES — V / U / A / T dans le scope de preuve actuel
LIMIT — ce que la trace ne permet pas d’affirmer
TRACE-LOCATOR / NEXT-PROOF — reprise et prochaine vérification
```

Une snapshot ne crée aucun statut, owner, route ou claim. Pour une décision ouverte, elle conserve les alternatives et organise la preuve suivante ; elle ne choisit pas une variante sans artefact applicable.

### Projection machine-readable optionnelle

Pour un agent ou un script, la `RUN_CARD` ou l’`EXECUTION-SNAPSHOT` peut être représentée en YAML. Cette projection est une vue de transport lisible ; elle ne crée aucun contrat, statut, route, gate, axe ou owner supplémentaire. `ACTION` reste la seule source d’autorité et les champs doivent conserver leurs significations canoniques.

La projection canonique se trouve dans `schemas/run_card.example.json`. Utilisez-la comme exemple machine-readable et validez-la avec `python3 scripts/validate_run_card.py schemas/run_card.example.json`. ACTION ne duplique pas ici un exemple YAML partiel : la projection JSON est la source unique de l’exemple structuré, tandis que cette section précise seulement son rôle de transport.

Les valeurs `state`, `issue`, `verdict`, `gate`, `axis`, `decision_change`, `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` ne doivent pas être fusionnées. `null` signifie qu’aucune valeur n’est déclarée dans cette projection ; il ne signifie ni réussite ni preuve absente. La projection ne doit jamais introduire `SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE` ou un score esthétique. La projection machine ne remplace ni la trace complète, ni l’observation, ni la clôture d’ACTION.

### Frontière de validation et de preuve

La validation JSON, la validation CLI, les fixtures, la compilation, le build et l’intégrité d’une archive établissent seulement que la projection, le package ou l’artefact de distribution respecte les contrôles exécutés. Ils ne prouvent ni que l’artefact est réellement implémenté dans son runtime, ni son usage, ni son accessibilité exécutée, ni sa performance, ni sa qualité visuelle, ni la préférence humaine. Une `RUN_CARD` valide peut donc rester `NOT-VERIFIED` sur un axe ou porter une limitation substantielle.

Pour chaque claim important, séparer explicitement : **cible de conformité** ou décision visée ; **méthode** ; **scope et runtime observés** ; **résultat** ; **limite** ; **prochaine preuve**. Si l’un de ces éléments manque, ne l’inférer pas depuis la validation de structure : conserver le verdict, l’issue ou `NOT-VERIFIED` approprié selon le contrat existant. La projection machine transporte ces distinctions lorsqu’elle possède les champs correspondants ; les dimensions non sérialisées restent dans la trace complète, le ticket, le manifeste ou le paquet de preuve cité.

---

## ACTION/RUN — routes d’exécution

Les blocs `RUN-*` donnent l’entrée, la sortie et le contrôle minimal de chaque mode. Les sections détaillées ci-dessous sont canoniques lorsque le bloc les appelle.

### `ACTION/RUN-LITE`

**Entrée.** Système et direction retrouvables ; delta local ou fix ; décision dominante connue.

**Faire.** Écrire la ligne de run, déclarer `DECISION-INTENT`, modifier, contrôler les gates A applicables et obtenir une preuve B du risque dominant. Charger `SAVOIR` ou `BIBLIOTHEQUE` uniquement si cela peut changer le correctif. Une alternative n’est documentée que si un choix plausible peut modifier le delta ou le risque.

**Sortie.** Artefact touché, V/U/A/T concernés, diff, verdict, réserve ou prochaine action. Ajoute `DECISION-CHANGE` si une décision a effectivement changé ; sinon justifie `N/A-JUSTIFIED` lorsque cela est pertinent.

**Clôture.** Passer à `DECIDED`, puis `CLOSED`. Reclassifier en `SYSTÈME` si une règle partagée est touchée, en `ITER` si la direction précédente doit être réévaluée ou en `DIRECTION` si une nouvelle décision identitaire apparaît.

### `ACTION/RUN-ITER`

**Entrée.** Direction, composants, tokens et périmètre précédent retrouvables dans la `RUN_CARD`, le manifeste ou le projet.

**Faire.** Rappeler la direction en une phrase, déclarer `DECISION-INTENT`, appliquer le delta et vérifier la non-régression pertinente : visuelle, fonctionnelle, responsive, typographique ou systémique.

**Sortie.** Direction toujours retrouvable, diff observable, preuve du risque touché, V/U/A/T mis à jour, verdict, risque restant et `DECISION-CHANGE` ou `N/A-JUSTIFIED`.

**Clôture.** Passer à `DECIDED`, puis `CLOSED`. Utiliser `RETURNED` si une preuve ou correction doit être reprise dans le même mode, `RECLASSIFIED` si l’identité, la portée ou le système sont remis en cause.

### `ACTION/RUN-STANDARD`

**Entrée.** Écran ou flow nouveau, sans charge identitaire autonome ni blast radius systémique.

**Faire.** Cadrer le JTBD et la décision dominante. Appeler `BIBLIOTHEQUE/SELECT` si support, grille, scène ou objet restent ouverts. Produire dès le premier rendu une composition jugeable : contenu crédible, hiérarchie, typographie appropriée, états pertinents, responsive applicable et détail de finition utile. Exécuter les Gates A et B ciblés. Utiliser une ancre visuelle seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le rend utile.

**Sortie.** Rendu ou artefact, hiérarchie, typographie, états, V/U/A/T, verdict, risque restant, prochaine action et `DECISION-CHANGE` ou `N/A-JUSTIFIED`.

**Clôture.** Passer à `DECIDED`, puis `CLOSED`. Passer à `EXPLORATORY` si une preuve requise manque, à `RETURNED` si une correction doit être reprise dans le même mode ou à `DIRECTION` si la surface devient identitaire.

### `ACTION/RUN-DIRECTION`

**Entrée.** Identité, surface de marque, premier contact ou hypothèse de direction autonome.

**Faire.** Exécuter le pipeline `ACTION/PIPELINE-DIRECTION` : positions distinctes lorsque la décision est ouverte, alternative située lorsque nécessaire, ancre utile, `DIRECTION/VISUAL_TARGET`, spec, checkpoint si nécessaire, build de la première scène significative, `ACTION/VISUAL_PROOF`, capture et comparaison. La première scène significative doit être présentable par défaut : elle porte déjà la direction, la hiérarchie, la typographie, la composition, la palette, la matière ou l’asset pertinent, les composants authored nécessaires et un niveau de finition suffisant pour juger la proposition comme un objet réel plutôt qu’un wireframe générique. Les détails sans rôle produit restent exclus. Lorsque la direction est nouvelle, ambiguë ou exposée à la convergence générique, le sourcing Web ou documentaire est recommandé ; s’il soutient un claim, une tendance, une provenance ou une décision non fondée en mémoire, il devient une ancre à ouvrir, dater, borner et transformer.

**Sortie.** Direction écrite, ancre/spec, capture, trace locale des assets pertinents, écarts, gates A/B/C, V/U/A/T, statut de direction, verdict global, owner, risque restant, prochaine preuve et `DECISION-CHANGE` ou `N/A-JUSTIFIED`. Pour chaque ancrage mobilisé, distinguer si nécessaire son rôle de direction, de production ou de vérification, les attributs retenus et rejetés, la transformation effectuée et les limites de transfert ; une référence Web n’est ni une preuve de réussite, ni une autorisation de copie.

**Clôture.** Passer à `DECIDED`, puis `CLOSED` uniquement si la direction est tenue et les preuves applicables déclarées. Sinon, passer à `RETURNED`, `RETURN-DIRECTION`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` selon la preuve et le risque.

### `ACTION/RUN-SYSTEM`

**Entrée.** Règle, token, composant, convention, dépendance ou format partagé affecté.

**Faire.** Cartographier l’impact et les consumers. Nommer la décision, l’owner, la migration, le rollback et les tests de non-régression. Consulter `CHANGELOG.md` avant adoption, pilotage ou dépréciation.

**Sortie.** Décision de système, plan de migration, preuve de non-régression, réserves, verdict et entrée CHANGELOG.

**Clôture.** Passer à `DECIDED`, puis `CLOSED` lorsque consumers et réserves sont traçables. Passer à `ESCALATED` si owner, droit, décision externe ou risque externe manque.

---

## ACTION/CLOSE-PACKAGE — paquet de clôture

Livre d’abord l’artefact ou le lien de rendu. Enregistre ensuite le paquet minimal correspondant dans la ligne de run, la `RUN_CARD`, le ticket ou le manifeste.

| Mode | Paquet minimal |
|---|---|
| **LITE** | Artefact touché, risque, V/U/A/T touchés, verdict, réserve ou prochaine action, et `DECISION-CHANGE`/`N/A-JUSTIFIED`. |
| **ITER** | Direction rappelée, diff, non-régression, verdict touché, risque restant, prochaine action et décision. |
| **STANDARD** | Artefact, hiérarchie, typographie, états pertinents, V/U/A/T, verdict, risque restant et prochaine action. |
| **DIRECTION** | Artefact, direction, ancre/spec, capture, écarts, revue créative, creative close, gates A/B/C, V/U/A/T, statut de direction, verdict et prochaine preuve. |
| **SYSTÈME** | Décision, impact, consumers, owner, migration/rollback, non-régression, verdict et entrée CHANGELOG. |

Un paquet incomplet ne reçoit pas de `PASS` implicite. Utilise `NOT-VERIFIED`, `EXPLORATORY`, `RETURNED`, `FAIL-ASSUMED` ou `ESCALATED` selon le cas.

Pour un run `DIRECTION`, le paquet comprend aussi un **creative close** bref : présence effectivement produite, signature ou élément spécifique, détail ou état révélant le niveau de craft, défaut dominant restant et prochaine action de polish. Dans une `RUN_CARD` structurée, ces éléments sont transportés par `creative_close.presence`, `creative_close.signature`, `creative_close.craft_detail`, `creative_close.dominant_defect` et `creative_close.next_polish_action`. Ce close cite un artefact ou une observation ; il ne devient ni verdict esthétique, ni score, ni preuve d’usage. Une `RUN_CARD` DIRECTION clôturée qui omet ce bloc est incomplète.

### Fraîcheur de la preuve

Chaque verdict est rattaché à l’artefact, à la version, au scope et à l’état réellement observés. Après un changement substantiel qui touche l’axe couvert, ce verdict revient à `NOT-VERIFIED` jusqu’à réinspection, nouvelle preuve ou justification explicite que la modification est hors scope. Les axes non touchés conservent leur dernière preuve valide.

Une preuve reste réutilisable lorsque l’artefact a seulement été déplacé ou relocalisé et que `TRACE-LOCATOR` permet de constater son identité et son absence de changement pertinent. Une capture, un test, une revue ou un avis portant sur une version antérieure ne peut jamais être cité comme preuve de la version livrée sans ce contrôle de fraîcheur.

### Cycle de vie des réserves

Toute réserve qui affecte la livraison conserve :

```text
OWNER
SCOPE
DATE / VERSION
IMPACT
NEXT-PROOF
REVIEW-DATE
EXIT-CONDITION
```

Cette structure s’applique à `PASS-WITH-RESERVATION`, `ACCEPTED-WITH-RESERVATION`, `REMAINING-RISK` et `FAIL-ASSUMED`.

### Responsabilité, droits et confidentialité

Chaque run conserve un **owner de décision finale**, même lorsque plusieurs personnes, agents ou prestataires ont contribué à l’artefact, à la direction ou à la preuve. L’owner répond de la décision et de la prochaine action ; il ne peut pas déléguer silencieusement un risque critique au protocole.

Tout asset fourni, curaté, généré ou transformé déclare, lorsque le contexte le requiert, sa provenance, son statut d’autorisation, sa portée d’utilisation, ses restrictions et son fallback. Une provenance tracée ne vaut pas licence d’utilisation. En cas de doute sur un droit, une ressemblance, une marque, une donnée personnelle ou un contenu client, la sortie reste limitée, bloquée ou escaladée selon le risque ; elle ne devient pas acceptable par simple mention dans la trace.

Les données sensibles, captures internes, informations personnelles et artefacts confidentiels ne sont utilisés que dans le périmètre autorisé. Si un outil, un agent ou un export ne permet pas de garantir ce périmètre, déclare la limitation et n’envoie pas la donnée vers ce canal. `NOT-VERIFIED` décrit une preuve manquante ; il ne constitue pas une autorisation de partager un contenu sensible.

### Condition d’arrêt du polish

Le polish s’arrête lorsque le défaut dominant identifié est corrigé ou accepté par l’owner, que les risques applicables sont couverts ou explicitement réservés, et qu’une itération supplémentaire ne promet pas de modifier une relation visible, une tâche, une preuve ou une contrainte importante. Si le défaut persiste mais qu’une nouvelle action est disproportionnée, conserve la réserve avec owner, impact, prochaine preuve et condition de sortie. Ne poursuis pas le polish pour remplir un quota, ajouter des effets ou atteindre une perfection abstraite.

---

## ACTION/PIPELINE-DIRECTION — direction vérifiable

Ce pipeline s’applique au mode `DIRECTION`. Il vise une direction réellement choisie, non un catalogue de variantes.

`DIRECTION/DOUBLE-LOOP` décrit la boucle de décision créative et d’apprentissage : observer, isoler, modifier, réobserver et décider. `ACTION/PIPELINE-DIRECTION` décrit son exécution livrable : préparer, construire, produire la preuve, appliquer les corrections, comparer et clôturer ou retourner. `ACTION/GATE-B/B1b` est un contrôle spécialisé déclenché dans ce pipeline lorsque son scope est actif ; ces trois niveaux ne sont pas trois boucles concurrentes.

### Boucle de qualité et branche one-shot

Pour tout run qui produit un rendu, la séquence de référence est : **préparer la qualité attendue → construire un premier rendu complet → observer le rendu réel sans se laisser guider par la rationale → isoler le défaut dominant → corriger l’artefact ou la décision → réobserver → comparer l’effet → clôturer ou retourner**. La correction doit changer une relation visible, une tâche, une preuve, une contrainte ou une propriété de robustesse ; une nouvelle explication ne constitue pas une correction.

La branche `one-shot` est une exécution raccourcie de cette même boucle, jamais une suppression de la boucle. Elle permet de clôturer après l’observation initiale lorsque le premier rendu atteint la qualité attendue du mode, que la direction est identifiable, que les risques applicables sont couverts et qu’aucune amélioration utile n’est probable. Si le premier rendu est faible, générique ou incomplet, la branche one-shot ne s’applique pas : corrige, retourne ou déclare honnêtement la limite.

### 1. Situer les positions

Lorsque la décision est ouverte, formule des positions distinctes sur les axes pertinents : structure, matière, voix, temporalité, densité, rapport texte/image, rythme ou émotion traduite en levier visuel.

Il n’existe aucun quota obligatoire de directions. Une position retenue et une alternative située suffisent lorsque le risque dominant et les tensions sont déjà clairs.

### 2. Traduire l’émotion

Une émotion n’est une direction que lorsqu’elle change une décision visible : composition, contraste, densité, échelle typographique, rythme de motion, contenu, relation texte/image ou traitement matériel.

« Premium », « chaleureux » ou « dynamique » sont des intentions à traduire, non des options de design autonomes.

### 3. Développer une alternative située

Lorsque la décision est ouverte et qu’une position différente peut réellement changer le choix, considère une proposition crédible répondant à un public, un JTBD, une contrainte ou une opportunité différente.

Matérialise l’alternative seulement au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou rendu. Ne construis pas une variante qui ne peut modifier aucune décision. Si aucune alternative située ne change raisonnablement le choix, note cette condition et passe à la spec après avoir nommé la raison.

### 4. Produire la spec visuelle

Une spec visuelle synthétique existe avant le premier code ou rendu d’une surface `DIRECTION`. La définition des voies `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` et `ANCHOR-PROVIDED` appartient à `DIRECTION/VISUAL_TARGET` ; ACTION en conserve seulement la trace opératoire : type et identifiant de l’ancre, cible ou hypothèse, attributs observés, éléments retenus et rejetés, contre-indications, limites de transfert et preuve attendue.

`ANCHOR-GENERATED` reste une hypothèse visuelle comparable, non une calibration externe suffisante par défaut. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe.

La spec décrit uniquement les décisions utiles : structure, hiérarchie, relation texte/preuve, traitement perceptible, typographie lorsque pertinente, contenu réel, actions, états, contre-indications et palette lorsque la couleur porte une décision.

Une ancre est utile seulement si elle apporte une décision structurelle ou perceptuelle, une contre-indication et une liste d’attributs retenus, rejetés et non transférables.

Sans ancre utile et spec exploitable, les axes concernés sont `NOT-VERIFIED`. Le run devient `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` selon le périmètre.

### 5. Sourcer et tracer

Trace dans la `RUN_CARD` ou le manifeste les références, requêtes, images ou assets réellement observés, avec leur rôle et leur statut. `BIBLIOTHEQUE.md` fournit des structures de décision ; il ne devient ni ancre visuelle, ni source d’asset, ni preuve de comparaison.

Pour toute recherche substantielle, distingue : `VERIFIED-THIS-RUN`, `MODEL-KNOWLEDGE-NOT-RECHECKED` et `USER-SOURCED-NOT-RECHECKED`. Les claims mesurés, datés, réglementaires ou dépendants d’un outil portent source, date, portée et limite dans la trace locale du run ; ils ne deviennent partagés qu’après décision de gouvernance.

Pour un asset directeur, trace aussi la route `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE`, sa raison, son traitement prévu, ses droits ou incertitudes et l’alternative refusée. Une requête ou un prompt ne prouve pas qu’un asset est adéquat : observe l’asset à son ratio, son crop, son contraste et son voisinage de texte réels.

### 6. Sélectionner contre la facilité

Si plusieurs solutions restent plausibles, nomme ce qui distingue le choix retenu. Si la solution est la plus simple à implémenter, défends-la par le JTBD, le risque, les droits, la performance, la maintenance ou une contrainte réelle.

> La faisabilité immédiate n’est pas une preuve d’appropriation.

### 7. Écrire la direction et demander une décision si nécessaire

Écris la direction retenue en une phrase : position, intention, décision dominante et contrainte servie. Compare-la à l’alternative située et formule l’avantage vérifiable du choix.

En session interactive, demande une validation avant le build lorsque le périmètre n’est pas couvert par une autonomie explicite. L’autonomie doit nommer le périmètre `DIRECTION` couvert. Une nouvelle marque, un nouveau public, une nouvelle surface identitaire autonome ou une nouvelle hypothèse déclenche un nouveau checkpoint, sauf instruction explicite couvrant ce périmètre.

Si aucun regard externe n’est disponible, déclare cette absence dans la `RUN_CARD` et compense par capture, comparaison, réserve et prochaine preuve ; ne transforme pas l’absence en validation implicite.

### 8. Vérifier le rendu réel

Après le build, capture le rendu et compare-le à la spec. Pour chaque écart significatif, nomme l’observation, la cause probable, l’effet sur la tâche ou la direction et l’issue : `CORRECTED`, `ACCEPTED-DIFFERENCE` ou `REMAINING-RISK`. Inspecte en priorité la structure, la hiérarchie, la typographie, la composition, la spécificité, la qualité des assets, les composants authored, les états et la cohérence de finition ; ne corrige pas un défaut structurel par un effet décoratif terminal.

### Passe créative et polish

Lorsque la qualité perceptuelle est une décision du run, effectue après la première scène une revue créative courte, puis une repasse ciblée avant la clôture. La revue ne produit ni score esthétique ni statut concurrent ; elle identifie ce qui est présent, ce qui porte le point de vue, ce qui est spécifique au produit, ce qui transforme réellement une référence, ce qui reste générique, ce qui manque de résolution et quel geste de polish modifiera le plus le rendu. Elle vérifie aussi si le premier rendu atteignait déjà la qualité attendue du mode, ou si la boucle est en train de réparer une préparation insuffisante.

La repasse examine les rapports entre masses, vides, échelles, rythme, typographie, matière, lumière ou profondeur, contenu, objet de preuve, états, responsive, transitions et détails de finition. Elle corrige d’abord le défaut dominant. Ajouter des effets, des variantes ou des assets sans améliorer une relation observable ne constitue pas une passe de polish.

Pour un run `DIRECTION`, la clôture créative doit pouvoir répondre à quatre questions : **quelle présence est effectivement produite, quelle signature rend la proposition spécifique, quel détail ou état montre le niveau de craft, et quel défaut reste prioritaire ?** Les réponses citent le rendu ou un objet inspectable et restent distinctes des preuves d’usage, d’accessibilité et de robustesse.

La comparaison vérifie notamment silhouette, opération dominante, matière/asset, typographie, objet de preuve, états et retenue. « Plus beau », « plus premium » ou « ressemble à la référence » ne sont pas des observations suffisantes.

Lorsque le risque visuel ou identitaire le requiert, la preuve doit être représentative de l’artefact construit et de son scope : elle montre, selon la décision, hiérarchie, composition, typographie, matière, spécificité, cohérence, retenue, états et résolution réelle. Une capture idéale ne masque pas un état, un viewport, un contenu ou un comportement non inspecté. La trace peut qualifier le niveau de craft observé — `Correction`, `Précision` ou `Intention` — mais cette qualification reste une lentille locale de jugement ; elle ne devient ni un score esthétique, ni un verdict global, ni un statut de direction. Une qualité visuelle observée ne prouve pas à elle seule la fidélité de la direction, la réussite d’usage, l’accessibilité ou la robustesse technique.

Retourne à la direction, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsqu’une correction locale ne change plus réellement le résultat. Aucun nombre fixe d’itérations n’est requis.

---

## ACTION/STRUCTURED-PROOF — contrats avant build

Ces artefacts rendent les décisions inspectables. Ils sont obligatoires seulement lorsque le mode ou le risque les déclenche.

### Carte de hiérarchie

- **Public prioritaire :**
- **Contexte et tâche dominante :**
- **Contenu primaire :**
- **Action critique :**
- **Contenu secondaire :**
- **Contenu à la demande :**
- **Risque de mauvaise lecture :**
- **Signal visuel prévu :**
- **Preuve U attendue :**

Lorsque U est dominant, la preuve U attendue peut être structurée ainsi :

```text
USER / PROFILE
TASK
CONTEXT
SUCCESS-CRITERION
OBSERVATION / MEASURE
SATISFACTION-OR-QUALITATIVE-RETURN
LIMIT
NEXT-PROOF
```

Une capture ou une inspection experte peut formuler un risque U ; elle ne doit pas être nommée test d’utilisabilité si aucune tâche représentative n’a été exécutée avec un utilisateur ou un profil concerné.

### Partition typographique

La partition complète est requise lorsque famille, registre, langue, données ou hiérarchie typographique peuvent changer la décision. Sinon, le système existant et la raison de sa conservation suffisent.

| Rôle | Fonction | Famille / registre | Mesure / interligne | Poids / axe | Contextes | Fallback | Justification |
|---|---|---|---|---|---|---|---|
| Fonctionnel | Corps, lecture longue |  |  |  |  |  |  |
| Éditorial | Titre, rythme, angle |  |  |  |  |  |  |
| Microcopie | Labels, métadonnées, actions |  |  |  |  |  |  |
| Donnée | Chiffres, tableaux, comparaisons |  |  |  |  |  |  |
| Signature | Usage expressif limité, si nécessaire |  |  |  |  |  |  |

La partition vérifie aussi reflow, zoom et ajustements d’espacement utilisateur : aucun rôle critique ne doit être tronqué, recouvert ou rendu illisible lorsque ces conditions sont dans le périmètre.

### Fiche d’asset directeur

- **ID et rôle dans la promesse :**
- **Route de production et statut :** `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE` ; image, illustration, SVG, vidéo, Rive, 3D ou absence intentionnelle.
- **Raison et alternative refusée :** quelle relation devient plus lisible, crédible ou singulière avec cette route ?
- **Source, disponibilité et droits :** observé, licence documentée, autorisation requise ou inconnu.
- **Provenance et transformations :** origine, créateur, génération ou édition connue.
- **Usage et intégration :** informatif, décoratif ou mixte ; relation au type, cadrage, grade, masque, composition ou donnée ; alt, description longue ou justification décorative.
- **Desktop et mobile :** ratio, crop, focal point, zone sûre, suppression ou alternative.
- **Format, poids cible, fallback, mouvement et reduced motion :**
- **Preuve V/U/A/T et contre-indication :**

La provenance informe l’origine ; elle ne constitue pas une autorisation de réemploi. Un droit inconnu ou non autorisé déclenche `RETURNED`, `ESCALATED` ou le statut prévu par le contexte avant diffusion.

### Contrat de composant et baseline

Pour un nouveau pattern réutilisable ou un composant critique, documente : intention, non-usage, sémantique, clavier, focus, anatomie, slots, tokens, modes, variants, états pertinents, responsive, stories ou captures de baseline.

Une baseline visuelle est une image versionnée d’un état réel. Elle signale un écart ; elle ne produit pas automatiquement un `PASS`.

Une différence est une régression seulement si elle s’écarte de l’intention, du comportement attendu ou du contrat de compatibilité. Une différence intentionnelle doit être reliée à une décision et à une preuve ; elle ne doit pas être supprimée comme régression visuelle par défaut.

Toute différence est revue contre l’intention, l’usage, l’accessibilité et le risque de régression.

### Contrat de motion ou scène spatiale

Toute motion non triviale, animation interactive ou scène 3D porte : rôle utilisateur ou narratif, état initial, déclencheurs, transitions, interruptions, clavier/tactile, reduced motion, fallback statique, performance, contenu alternatif, capture de référence et contre-indication.

Un effet qui ne produit ni feedback, ni information, ni relation spatiale ni décision de direction est candidat à la suppression.

---

## ACTION/VISUAL_PROOF — rendre la direction vérifiable

Visual Proof relie `DIRECTION/VISUAL_TARGET`, l’ancre, la spec et le rendu observé. Il s’exécute dès qu’une première scène significative est disponible.

Avant la preuve, déclare le périmètre : viewport, états, scènes, contenu, devices et axes couverts. Les éléments hors couverture sont mentionnés dans `COVERAGE-LIMIT` ou `NEXT-PROOF`.

| Preuve | Vérifie | Si absente ou inadaptée |
|---|---|---|
| Capture desktop entière | Support, silhouette, masses, vide, foyer, opération dominante et rapport scène/preuve. | V `NOT-VERIFIED` sur la surface. |
| Capture mobile entière | Recomposition, voisinage, priorité et action. | U/T `NOT-VERIFIED` si mobile est dans le périmètre ou le risque. |
| Vue de détail | Type, matière, cadrage, bordure, état ou contenu extrême lorsque pertinent. | `N/A-JUSTIFIED` seulement si aucun détail ne porte une décision. |
| Vue de masses | Foyer, poids relatifs, vides et foyer parasite sur une surface à risque hiérarchique. | `N/A-JUSTIFIED` si la hiérarchie n’est pas un risque du run. |
| État significatif | Loading, empty, error, focus, contenu long ou état dominant. | U/A/T `NOT-VERIFIED` sur l’état absent. |
| Comparaison d’écarts | Spec/ancre face au build sur les axes touchés. | `EXPLORATORY` ou `RETURN-DIRECTION`. |

Une capture prouve le rendu, pas l’indépendance du jugement, l’accessibilité complète ou la réussite d’une tâche. Un regard humain ou externe prouve un avis situé, pas une mesure technique. Un asset généré est une ancre possible, jamais une preuve de rendu.

---

## ACTION/GATE-A — plancher objectivable

Gate A vérifie les fautes mesurables ou observables. Exécute uniquement les contrôles applicables au composant, à l’appareil et au contexte.

### Contrat de portée

Lorsque l’accessibilité ou la conformité est dans le périmètre, déclare avant le contrôle :

```text
MEDIUM — médium réel de la surface et périmètre effectivement observé ; déclare le support applicable. Pour le Web, le médium peut rester implicite seulement si le périmètre est sans ambiguïté ; pour tout autre médium, il est explicite.
SCOPE — vues, composants, états ou chemins couverts.
CONFORMANCE-TARGET — référentiel et niveau visé, adapté au médium déclaré.
SAMPLE — échantillon représentatif ou raison de l’exhaustivité.
METHOD — AUTOMATED, MANUAL, EXPERT, USER ou combinaison, adaptée au médium.
BUDGET-UNIT — unité de budget pertinente : load/INP, lancement/frame rate/mémoire, confort motion, encre/contraste ou équivalent déclaré.
COVERAGE-LIMIT — éléments hors couverture, incluant toute preuve web indisponible.
NEXT-PROOF — preuve suivante attendue.
```

Pour le web, utilise WCAG 2.2 comme base normative actuelle lorsque le projet n’impose pas un autre référentiel applicable. Pour un autre médium, déclare le référentiel applicable dans `CONFORMANCE-TARGET` : guideline de plateforme, référentiel légal, standard émergent ou critère de lisibilité pertinent. WCAG 3.0 reste une `[VEILLE]` tant que sa recommandation et son modèle de conformance ne sont pas stabilisés. Les critères de conformité ne valident ni la direction visuelle, ni l’utilisabilité globale, ni l’adéquation du positionnement.

### Familles de méthodes

| Méthode | Couvre prioritairement | Limite |
|---|---|---|
| `AUTOMATED` | Défauts détectables par outil et règles codées. | Ne couvre pas tous les problèmes d’usage, de contexte ou d’interprétation. |
| `MANUAL` | Structure, clavier, focus, états et situations que l’outil ne comprend pas. | Dépend de la méthode et de l’expertise de l’inspecteur. |
| `EXPERT` | Interprétation, risque, cohérence et problèmes contextuels. | Ne remplace pas une tâche utilisateur. |
| `USER` | Expérience réelle et difficultés de personnes concernées. | Échantillon, tâche et contexte doivent être déclarés. |

Un `PASS` décrit la preuve obtenue par la méthode, le médium et le périmètre déclarés. Il ne devient pas un `PASS` global par glissement. Ce qui n’existe pas dans le médium est `N/A-JUSTIFIED` ; ce qui le remplace est testé. Une preuve web indisponible n’est jamais simulée : elle devient `NOT-VERIFIED` avec `NEXT-PROOF`, ou est traduite en équivalent du médium.

Pour un verdict global `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, la `RUN_CARD` doit rattacher la preuve observée à une provenance minimale : `artifact_locator`, `artifact_version`, `method` et `observed_at`. Cette provenance établit où, sur quelle version, par quelle méthode et à quel moment l’observation a été obtenue ; elle ne prouve pas à elle seule la véracité de l’artefact, la qualité du design ou la réussite d’usage. Si la provenance ne peut pas être établie, le verdict reste non accepté ou la limite est explicitement déclarée selon le mode et le risque.

### Adéquation des preuves

| Question | Preuve adaptée | Limite |
|---|---|---|
| Ratio, taille, token, régression mesurable | Script ou test exécuté. | Ne prouve pas l’intention visuelle. |
| Hiérarchie, composition, densité, matière | Capture, détail et comparaison. | Ne crée pas seul un juge indépendant. |
| Préférence, clarté, fidélité au contexte | Regard humain, expert ou utilisateur selon le risque. | N’est pas une mesure technique par défaut. |
| Utilisabilité réelle | Utilisateur représentatif, tâche représentative, observation et résultat. | Ne se déduit pas d’une capture ou d’un avis expert seul. |
| Hypothèse sans runtime ou observateur | Déclaration structurée. | Reste `NOT-VERIFIED` si la preuve est requise. |

### Contrôles applicables

| Contrôle | `PASS` si… | Retour ou réserve si… |
|---|---|---|
| Contraste | Les cas représentatifs sont calculés selon la politique WCAG 2.2 AA du projet lorsqu’elle s’applique. | Estimé à l’œil, sous seuil ou non calculé lorsque requis. |
| Sémantique et nom accessible | Interactifs et contenus essentiels ont une sémantique et un nom adaptés. | Rôle, nom, structure ou alternative absents. |
| Focus clavier | Interactifs atteignables avec focus visible et testé. | Navigation ou focus indisponible. |
| États pertinents | Interaction, sélection, contenu et erreurs sont vérifiés ; événement, conséquence et action suivante sont explicites. | État critique absent, implicite ou dépendant de la couleur seule. |
| Contenu honnête | Pas de faux contenu, lorem ou promesse non étayée présenté comme réel. | Contenu de remplissage trompeur. |
| Stabilité média | Dimensions, fallback et chargement évitent les déplacements pertinents. | Instabilité visible ou espace non réservé. |
| Motion réduite | Alternative sans mouvement prévue lorsque la motion existe. | Motion imposée ou alternative absente. |
| Cibles d’interaction | Taille adaptée au device et au contexte selon la politique du projet. | Cible trop petite sans alternative ni justification. |
| Information non chromatique | L’information essentielle ne dépend pas de la couleur seule. | Statut ou action incompréhensible sans couleur. |
| Focus non masqué | Le composant recevant le focus reste visible selon le contexte applicable. | Focus masqué par contenu ou interface auteur. |
| Mouvement de glisser | Une alternative existe lorsque l’action de glisser n’est pas essentielle. | Action impossible autrement sans justification. |
| Aide cohérente | L’aide répétée apparaît de façon cohérente lorsque le produit en fournit. | Aide déplacée ou incohérente dans le périmètre. |
| Saisie redondante | L’utilisateur ne doit pas ressaisir inutilement une information déjà fournie dans le même processus. | Répétition évitable sans raison. |
| Authentification accessible | Le processus n’impose pas une charge cognitive ou sensorielle évitable. | Mémoire, perception ou interaction imposée sans alternative. |

Les scripts et recettes sont des ressources versionnées. Une recette exécutée ne suffit pas à valider un résultat visuel, produit ou utilisateur.

---

## ACTION/GATE-B — jugement contextualisé et risques

Gate B compare, observe et explique les risques restants. Il ne produit pas une moyenne décorative.

### B1 — Comparaison relationnelle

En `DIRECTION`, compare le build à l’ancre utile sur les axes réellement concernés. En `STANDARD`, utilise une ancre seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le justifie.

Pose des questions relationnelles : quel résultat conduit mieux à l’action critique, rend le rythme plus lisible, porte mieux l’intention ou maintient mieux la singularité du produit ?

Une différence significative sur un axe dominant déclenche une correction, un écart assumé ou une justification de non-transfert. Aucun nombre fixe de comparaisons ne constitue une condition de `PASS`.

### B1b — Discrimination sur capture, requise dans son scope

`B1b` est **requis par module** sur une surface `DIRECTION` lorsque le risque V/craft est dominant dans la ligne de run ou lorsque le verdict V repose sur une intention, une composition, une matière ou un traitement qui n’a pas encore été confronté à une variante. Le déclencheur porte sur le risque et la décision déclarés ; il ne dépend pas de l’affirmation qu’une comparaison « ne changerait rien ».

La preuve minimale est une paire de captures réelles : une capture initiale, puis une capture après l’édition réversible d’une seule décision principale. La variable doit être observable : masse, vide, silhouette, lumière, densité, cohérence de rayon, définition d’état, crop, vocabulaire, preuve, couleur ou action.

#### Atelier d’édition — opération observable

Après la première capture, effectuer une lecture légère en ignorant le texte explicatif et nommer en une phrase la catégorie, la marque et le niveau de preuve que la surface semble raconter. Nommer ensuite la décision principale qui sera mise à l’épreuve. Éditer cette décision par **retrait, réduction ou transformation** ; une décision peut coordonner plusieurs diffs, mais l’unité de compte n’est pas le nombre de changements. Ne rien ajouter pour compenser.

Conserver et comparer la capture suivante. La trace nomme le changement, sa direction, son effet et la décision qu’il confirme, modifie ou abandonne. Conserver l’original lorsqu’il résout mieux la décision est un résultat valide : la variante a alors confirmé une décision par comparaison plutôt que par déclaration.

`N/A-JUSTIFIED` n’est recevable que si aucune décision principale éditable n’existe dans le périmètre, ou si une paire équivalente, toujours valide après le dernier changement substantiel, couvre déjà exactement la même décision. La justification lie l’artefact concerné, l’owner et la prochaine preuve. Une thèse encore incertaine, un élément producteur introuvable ou une paire qui n’autorise aucune conclusion maintiennent le run en `EXPLORATORY` ; ils ne produisent pas un `PASS` indirect.

B1b n’est ni un sixième absolu, ni un score esthétique, ni un quota universel. Hors de son scope, il ne s’applique pas. Dans son scope, il ne peut être omis sans la sortie matérielle ci-dessus.

Si l’équipe accepte consciemment l’écart narratif entre la thèse déclarée et le récit implicite de la capture, ne crée pas une nouvelle `ISSUE`. Utilise le statut de direction `HELD-WITH-ACCEPTED-DIFFERENCE` et, lorsque le périmètre permet la clôture, le verdict global `ACCEPTED-WITH-RESERVATION`. La trace doit nommer : `NARRATIVE-DIFFERENCE`, `REASON`, `PRODUCT-OR-PUBLIC-CONSTRAINT`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`. Cette issue n’est acceptable que si l’écart est explicite, assumé, compatible avec U/A/T et révisable ; elle ne convertit pas une preuve manquante en acceptation.

En l’absence de regard indépendant, déclarer cette limite selon B3. Une B1b menée par l’auteur du rendu est une **auto-comparaison** : elle peut soutenir une correction de craft, mais ne satisfait jamais un claim de revue indépendante. Une décision identitaire importante qui requiert un contrepoint externe reste avec réserve ou prochaine preuve tant que ce regard n’existe pas.

### B2 — Familles de preuve

Ajoute une preuve de contexte lorsque le risque produit est dominant : source de l’hypothèse, niveau de confiance, coût d’erreur, owner et prochaine preuve. Une direction peut être visuellement tenue et néanmoins répondre au mauvais problème ; ce cas doit rester visible dans U et dans le risque restant.

| Famille | Axes | Preuves privilégiées | Sortie principale |
|---|---|---|---|
| Caractère et perception | Point de vue, hiérarchie, typo/contenu, craft/états, singularité/retenue. | Capture, paires, détail, regard externe. | V |
| Compréhension et produit | UX, architecture, action critique et contenu. | Carte de hiérarchie, scénario, états, test ou retour de tâche. | U |
| Système et robustesse | Couleur, accessibilité, responsive, dark, performance et motion. | Tokens, inspection, tests, capture responsive. | A/T |
| Gouvernance | Best-fit, limites, délégation et arbitrages. | Journal, recherche, compromis, escalade. | Réserve ou prochaine action |

Chaque axe jugé porte une observation factuelle. Une note sur cinq peut localiser un risque, mais aucune note globale ne remplace V/U/A/T. Une note sans observation est invalide.

### B3 — Regard externe

Un regard humain, une seconde session ou un autre évaluateur peut réduire l’auto-préférence. Documente la source, l’expertise ou le profil, l’artefact regardé et la limite du jugement. Une B1b exécutée par le même auteur est une auto-comparaison et ne doit jamais être étiquetée regard externe, indépendant ou aveugle.

Un regard externe fournit un contrepoint situé ; il ne garantit ni indépendance parfaite ni exhaustivité. Pour une décision importante, triangule selon le risque : plusieurs évaluateurs, plusieurs méthodes, ou inspection et observation utilisateur.

Si aucun regard externe n’est disponible, déclare l’absence, conserve la capture et la comparaison, et inscris la réserve ou la prochaine preuve. L’absence de regard indépendant ne devient jamais une validation implicite.

Lorsqu’un regard est présenté comme **indépendant**, **comparatif** ou **aveugle**, la trace conserve aussi :

```text
REVIEWER-ROLE
ARTEFACTS-REVIEWED
REVIEW-EXPOSURE — BLIND / CODE-EXPOSED / PROMPT-EXPOSED / MAPPING-EXPOSED / NOT-BLIND
MAPPING-TIMING — BEFORE / AFTER / NOT-APPLICABLE
LIMIT
```

Une revue non aveugle reste une preuve située utile si son exposition est déclarée. Elle ne reçoit pas le poids d’une passe aveugle. Une divulgation du mapping après l’avis peut enrichir la passe d’interprétation, mais ne réécrit pas le jugement initial.

### B4 — Corrections ancrées

Une correction de direction répond à un écart ou une critique observable. Retourne à la divergence, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsque la correction locale dénature le produit.

Aucun nombre fixe d’itérations ne constitue une règle de qualité. Le run s’arrête lorsque la direction est tenue, l’écart est explicitement assumé, la preuve est impossible et statuée, ou le périmètre doit être reclassifié.

### B5 — Trace d’assets et statut de direction

Avant le verdict d’une surface `DIRECTION`, conserve dans la trace locale les éléments utiles : capacités vérifiées, ancre et références observées, attributs retenus/rejetés, direction, écarts, réserves et statut.

Si un asset est directeur, la trace relie aussi sa route de production, sa raison, son droit ou son incertitude, son traitement et l’observation de son intégration au rendu réel. Un asset techniquement disponible mais faible dans son crop final, hors récit, ou seulement « joli » reste un écart de direction, pas une preuve de finition.

### B6 — Format de sortie compact

Livre d’abord l’artefact ou le lien. Ensuite, expose le verdict adapté au mode : une ligne en `LITE`, quelques lignes en `ITER` ou `STANDARD`, et un bloc direction + risques en `DIRECTION`.

Les paires, logs, preuves et diffs vivent dans un artefact associé ou la `RUN_CARD`. Ne répète pas les mêmes valeurs en prose et en structure.

---

## ACTION/GATE-C — craft sur rendu réel

Gate C évalue la présence de décisions perceptibles et la qualité de leur résolution. Il est obligatoire en `DIRECTION`, ciblé au risque craft en `STANDARD`, limité à la zone touchée en `ITER` et `N/A-JUSTIFIED` en `LITE` lorsque le craft n’est pas concerné.

Une capture réelle est nécessaire pour un jugement C. Sans runtime ou capture, le craft reste `NOT-VERIFIED`.

Lorsque `ACTION/GATE-B — B1b` est déclenché, Gate C inspecte le rendu et s’appuie sur la paire B1b pour la décision mise à l’épreuve ; il ne recrée pas une seconde procédure de comparaison.

Chaque verdict C précise le périmètre : viewport, état, scène, contenu et élément observé.

| Critère | Présent si… | Retour ou réserve si… |
|---|---|---|
| **C1 — Stratégie de surface** | Photo, donnée, lumière, illustration, surface, trame, profondeur ou planéité assumée découle du produit. | Traitement par défaut sans relation observable. |
| **C2 — Typographie choisie** | Famille, système existant ou alternative est justifié ; rôles, échelle et fallback servent le contexte. | Choix par défaut non interrogé ou non calibré. |
| **C3 — Composition intentionnelle** | Structure de lecture identifiable sert l’action et le rythme. | Empilement uniforme sans décision spatiale. |
| **C4 — Densité optique** | Espace, masses et regroupements suivent la priorité et l’usage. | Espacement uniforme qui masque les relations. |
| **C5 — Stratégie de profondeur applicable** | Profondeur, lumière ou planéité est cohérente avec le registre et lisible au rendu. | Ombres, bordures ou flous par défaut sans logique. `N/A-JUSTIFIED` si la planéité est intentionnelle et suffisante. |
| **C6 — Résolution située** | Une difficulté réelle est résolue par microcopie, état, donnée, interaction, asset ou transition pertinente. | Assemblage de composants sans adaptation au cas. |

Chaque verdict C cite l’élément concret observé. Un critère bloquant absent, ou plusieurs signaux faibles convergeant sur le même risque, déclenchent un retour. La correction revient à la direction, à la spec ou au build ; elle n’ajoute pas un effet décoratif terminal.

---

## ACTION/ANTI-SLOP — conséquence de gate

La matrice canonique motivation/construction appartient à `SAVOIR/CRAFT/CFT-01`. ACTION ne la reproduit pas : il vérifie sa conséquence sur l’artefact. Lorsqu’un motif manque de motivation, de construction ou des deux, la trace nomme l’élément observé, la relation produit/lecture manquante et la sortie : correction, retrait, réserve ou `RETURN`.

Une couleur de marque, une contrainte de contenu ou une construction technique soignée n’immunisent pas un choix contre les autres gates. Les watchlists et tendances restent des aides de jugement dans `SAVOIR/CRAFT` ou la veille ; elles ne deviennent pas des interdits universels.

---

## ACTION/OVERRIDE — FAIL-ASSUMED et péremption

### FAIL-ASSUMED

Un utilisateur peut demander une diffusion limitée malgré un échec connu lorsque le risque est documenté, assigné et re-testable. Le FAIL ne devient jamais un PASS.

Journalise :

> `FAIL-ASSUMED — [gate / axe] — [mesure ou preuve] — [date] — [risque] — [périmètre de diffusion] — [owner] — [condition de re-vérification].`

Toute exception conserve également :

```text
SCOPE
IMPACT
REVIEW-DATE
NEXT-PROOF
EXIT-CONDITION
```

Un `FAIL-ASSUMED` ne peut pas autoriser la mise en production d’un risque de sécurité, de dommage grave, de conformité critique ou de défaillance qui rend l’action essentielle trompeuse ou dangereuse. Ces cas passent en `ESCALATED` ou restent non livrables.

Les risques d’accessibilité, de sécurité ou de conformité à fort impact sont rappelés factuellement. Un `FAIL-ASSUMED` est re-présenté à la prochaine modification du même périmètre.

### Péremption

La péremption d’un claim, d’un outil, d’une watchlist ou d’une ressource déclenche une revue lorsque le livrable en dépend. La trace conserve type de claim ou de ressource, source, version, date de vérification, portée, limite, owner, date de revue et prochaine preuve.

La péremption ne bloque pas un fix sans rapport, mais ne peut pas être silencieusement reconduite lors d’une prochaine utilisation.

Une réserve périmée conserve owner, date de revue, impact, nouvelle preuve attendue et condition de clôture.

---

## ACTION/POLICIES — contraste et inspection

### Politique de contraste

Calcule le contraste selon WCAG 2.2 et le référentiel applicable lorsque ce référentiel s’applique au projet. Ne valide jamais le contraste à l’œil.

APCA peut être documenté comme mesure complémentaire de lisibilité ou d’exploration lorsque son contexte, sa version et sa limite sont connus. APCA ne remplace pas un critère WCAG applicable et ne crée pas seul un verdict réglementaire.

Les seuils, outils, projections réglementaires et sources évolutives sont qualifiés dans `SAVOIR/TOOLS` et la trace locale du run. ACTION porte la politique de livraison ; un fait ne mérite une décision de gouvernance que lorsqu’il devient une règle partagée.

### Inspection et ressources techniques

Une inspection externe peut compléter le jugement sur l’accessibilité, la régression visuelle, les tokens et les motifs. Choisis l’outil selon l’environnement, sa documentation, sa version et son owner. Une commande, un package ou une intégration cités dans une ressource ne sont jamais exécutés aveuglément.

Toute ressource technique maintenue indique :

- stack et version ;
- date de vérification ;
- capacité résolue ;
- fallback ;
- limites ;
- owner ;
- prochaine revue.

L’automatisation détecte une partie des défauts mesurables. Elle ne remplace ni l’inspection de rendu, ni la capture, ni le jugement contextuel, ni l’observation utilisateur lorsque le risque la requiert.

Pour les composants critiques, maintiens une baseline d’états pertinents : variant, thème, viewport, données longues, loading, empty, error et focus lorsque nécessaires. Une capture versionnée et une revue explicite peuvent fournir une preuve proportionnée lorsqu’un pipeline de stories ou de tests visuels n’existe pas.

---

## ACTION/ROUTING — prérequis de jugement et de structure

DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui peuvent modifier la prochaine décision.

| Situation | Routes ciblées |
|---|---|
| Spec `DIRECTION` | `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/SOURCE`, `SAVOIR/STYLE` si registre, `BIBLIOTHEQUE/SELECT` si structure ouverte. |
| Craft ou états | `SAVOIR/STATE`. |
| Couleur, contraste ou theming | `SAVOIR/CRAFT`, `SAVOIR/SYSTEM` et politique de contraste ACTION. |
| Risque critique, responsive, performance ou motion | `SAVOIR/CONTEXT`. |
| Technique ou compatibilité | `SAVOIR/TECH`. |
| Claim, outil ou tendance datée | `SAVOIR/TOOLS` et trace locale indiquant source, date, portée et limite. |
| Doute d’application ou théâtre procédural | `SAVOIR/INTEGRITY`. |
| Une famille de design peut modifier la prochaine décision | Section `DESIGN-ATLAS` de `SAVOIR.md`, puis seulement la route propriétaire utile. |
| Structure d’un écran | `BIBLIOTHEQUE/SELECT`, puis routes retenues. |
| Token, composant ou blast radius | `SAVOIR/SYSTEM`, `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` si partagé. |

Les anciennes références de section ne sont pas des routes quotidiennes. Leur migration est documentée dans `CHANGELOG.md`, et un nouveau run utilise uniquement les routes stables.

---

## ACTION/MAINTENANCE — recette documentaire

Tout cycle qui modifie ACTION ou un contrat connexe se clôt par une recette avant adoption.

| Contrôle | Preuve attendue |
|---|---|
| Fichiers et renvois | Chaque fichier et route référencés existent et portent la bonne portée. |
| Statuts | Les états, issues, verdicts et statuts de direction appartiennent aux registres canoniques ; aucun plan de maturité concurrent n’est ajouté. |
| Scopes | Chaque obligation précise son mode, contexte ou niveau de proportionnalité. |
| Exemples | Aucun exemple ne propage un statut ou une règle dépréciée. |
| Claims datés | Source, version/date, portée, limite et prochaine preuve sont renseignées dans la trace locale quand le run en dépend. |
| Routage | Chaque signal a une route principale ; les miroirs sont dérivés explicitement. |
| Quotas artificiels | Aucun quota de variantes, retraits, comparaisons, itérations ou appels ne gouverne la qualité. |
| Échappatoire théâtrale | Chaque mécanisme est testé contre sa manière la plus facile d’être satisfait sans intention. |
| Run réel | Une modification substantielle est exercée sur un run réel avant adoption élargie. |
| Ownership | Owner du changement, statut d’adoption et prochaine revue sont nommés. |
| Réserves | Owner, périmètre, impact, date de revue, prochaine preuve et condition de sortie sont persistants. |

La recette peut être automatisée pour les fichiers, routes, statuts et renvois. Elle doit rester humaine pour le scope, l’intention, l’échappatoire théâtrale, la proportionnalité et le jugement du risque.

Une contradiction non résolue devient un risque explicite, jamais une règle silencieusement concurrente.

---

## ACTION/CLOSE-EXIT-CHECK — test de sortie canonique

Avant de clôturer un run, vérifie :

1. Le mode est-il celui qui protège le risque dominant ?
2. L’artefact et la décision sont-ils retrouvables ?
3. La preuve adaptée à la question a-t-elle été obtenue, ou son absence est-elle déclarée ?
4. Le scope et la limite de couverture sont-ils connus lorsque la preuve le requiert ?
5. Les V/U/A/T touchés et le risque restant sont-ils renseignés ?
6. Le statut de direction, le verdict global, l’owner et la prochaine action sont-ils persistants ?
7. La réserve, si elle existe, possède-t-elle owner, périmètre, impact, date de revue, prochaine preuve et condition de sortie ?
8. Quelle décision concrète a changé grâce à la procédure ? Si la réponse est « aucune », la procédure est-elle réellement justifiée ?
9. Quel niveau de qualité était visé au premier rendu, et quel élément observable démontre qu’il était composé, spécifique et suffisamment résolu pour le mode ?
10. La dernière modification a-t-elle changé une relation perceptible, produit, preuve, accessibilité ou robustesse, ou seulement la justification ?

Si une réponse reste inconnue, utilise le statut approprié. Ne transforme jamais une lacune de preuve en `PASS` implicite. Une trace complète ne compense pas un artefact faible ; un premier rendu très fort ne compense pas une preuve requise absente.

### Mesure expérimentale de la méthode

Au niveau d’un pilote ou d’une série de runs, et non comme score individuel, observe le temps jusqu’au premier rendu jugeable, la part des premiers rendus nécessitant une correction structurelle, la part des corrections qui changent réellement l’artefact, les preuves encore `NOT-VERIFIED` à la clôture, les défauts récurrents par mode et la perception de qualité par plusieurs regards situés. Ces mesures servent à améliorer V1 ; elles ne créent ni verdict esthétique, ni quota d’itérations, ni obligation de variante.

