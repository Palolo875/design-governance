# READING_MAP — carte dérivée de lecture et d’activation

**Statut :** guide dérivé non normatif. Les cinq sources normatives, le schéma `RUN_CARD` et les validateurs propriétaires font foi en cas de divergence.

## Utilisation

Cette carte réduit la recomposition mentale du lecteur. Elle ne crée ni mode, ni gate, ni axe, ni statut, ni verdict, ni owner de décision supplémentaire. Elle indique seulement où commencer, quoi charger, ce qui doit sortir et quand transmettre.

Pour composer plusieurs capacités selon un résultat recherché — direction, beauté située, créativité, usage, preuve, vitesse ou système — consulter [`ORCHESTRATION_MAP.md`](ORCHESTRATION_MAP.md). Cette carte d’orchestration est dérivée et complémentaire : `READING_MAP` résout le premier chemin ; `ORCHESTRATION_MAP` aide à ajuster la combinaison et l’intensité sans remplacer les propriétaires normatifs.

## Chemin canonique de démarrage

1. Localiser la version V1 réellement fournie.
2. Lire `QUICKSTART.md` ou cette carte si le besoin est déjà identifiable.
3. Ouvrir `DIRECTION/START` pour classer le mode et le risque dominant.
4. Charger uniquement le propriétaire capable de modifier la prochaine décision.
5. Ouvrir `ACTION` dès qu’un artefact, une observation, une preuve, un état ou une clôture est concerné.
6. Persister la sortie selon le contrat `RUN_CARD` lorsque le run doit être repris, comparé ou fermé.

`DIRECTION/START` reste la seule classification. Cette carte ne reclassifie pas.

## Constitution minimale

Les cinq absolus de `DIRECTION` protègent la baseline : direction perceptible, ancre inspectable, preuves applicables, mode et prochaine preuve déclarés avant l’exécution, coordination du réel et du beau. La conformité ne remplace ni la direction ni la preuve. Pour le contrat complet, ouvrir [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).

## Routage minimal par décision

| Décision dominante | Première lecture | Ajouter seulement si nécessaire |
|---|---|---|
| Brief vague ou risque inconnu | `DIRECTION/START` | `DIRECTION/EXTERNAL-START` |
| Correction locale | `DIRECTION/START` → `ACTION/RUN-LITE` ou `RUN-ITER` | `SAVOIR` ou `BIBLIOTHEQUE` si la décision change |
| Nouvelle surface opérationnelle | `DIRECTION/START` → `ACTION/RUN-STANDARD` | `BIBLIOTHEQUE/SELECT`, `SAVOIR/CONTEXT` |
| Direction identitaire | `DIRECTION/START` → `DIRECTION/VISUAL_TARGET` → `DIRECTION/FIRST-OBJECT` → `ACTION/RUN-DIRECTION` (dès qu’il y a un build) | `SAVOIR/CRAFT`, `DIRECTION/DIRECTION-ATELIER` |
| Structure ou composant partagé | `DIRECTION/START` → `ACTION/RUN-SYSTEM` | `BIBLIOTHEQUE/COMPONENTS`, `SAVOIR/SYSTEM`, `CHANGELOG` |
| Preuve, vérification ou clôture | `ACTION` | Gate et route correspondant au risque |
| Règle ou route durable | `CHANGELOG` et source propriétaire | `ACTION` pour preuve et `BIBLIOTHEQUE/EVOLUTION` si structure |

Sortie : réponse visible et handoff (`ACTION/HANDOFF`) ; clôture : `ACTION/CLOSE-PACKAGE`.

## Activation multi-perspective

Une perspective ne se charge que si son déclencheur peut modifier la décision. `N/A-JUSTIFIED` est une sortie valide lorsque la perspective est examinée et non applicable. Ne pas charger une lecture ne rend jamais `N/A` un contrôle applicable du propriétaire.

| Perspective | Déclencheur | Lecture minimale | Sortie | Non-chargement |
|---|---|---|---|---|
| Direction | Identité, présence, premier objet ou composition ouverte | `DIRECTION` + cible | Thèse, objet, ancre, relation, défaut dominant | Décision visuelle intacte et delta strictement local |
| Production | Artefact ou modification à construire | `ACTION` + route du mode | Artefact, scope, état et prochaine preuve | Aucun artefact ou simple clarification |
| Usage | JTBD, action, confiance, récupération ou tâche critique | `ACTION/UI-UX-REALITY` | Geste, résultat, état, limite | Aucun impact sur usage déclaré |
| Contenu | Données, longueur, langue, claim ou état | `SAVOIR/TYPE` ou `STATE` | Contenu crédible, hiérarchie, limite | Contenu inchangé et non déterminant |
| Responsive | Mobile, zoom, reflow ou viewport critique | `ACTION/UI-UX-REALITY` + `SAVOIR/CONTEXT` | Recomposition, priorité, preuve de scope | Aucun changement de viewport ou risque déclaré |
| Accessibilité | Focus, clavier, sémantique, contraste, motion ou population critique | `SAVOIR/CONTEXT` + `ACTION/GATE-A` | Méthode, scope, résultat, limite | Aucun risque d’accessibilité au-delà des contrôles `ACTION/GATE-A` applicables, qui restent dus |
| Runtime | Compatibilité, performance, fallback ou plateforme | `SAVOIR/TECH` + `ACTION` | Runtime, méthode, erreur, fallback, preuve | Aucun claim technique |
| Preuve | Claim, capture, mesure, verdict ou clôture | `ACTION` | Claim, méthode, scope, date, limite, locator | Aucune affirmation de résultat |
| Maintenance | Consumer partagé, trace, migration ou reprise | `ACTION` + `CHANGELOG` si durable | Owner, diff, compatibilité, revue, réouverture | Delta local sans conséquence future |
| Coordination | Handoff, escalade, action externe ou owner suivant | `ACTION/AUTHORITY` et sortie | Destinataire, autonomie, confirmation, prochaine action | Aucun transfert |
| Mémoire | Décision durable, version, réserve ou migration | `RUN_CARD` et `CHANGELOG` si promotion | Décision, date, statut, preuve, réserve, revue | Décision strictement éphémère |

## Handoff minimal commun

Ce bloc est une copie du handoff canonique (voir `ACTION/HANDOFF`) ; il ne remplace pas `ACTION` ni le schéma `RUN_CARD`.

```text
MODE:
DECISION:
RISK:
SCOPE:
ARTIFACT:
OBSERVATION / METHOD:
PROOF / TRACE-LOCATOR:
LIMIT / NOT-VERIFIED:
DECISION-CHANGE:
NEXT-ACTION:
OWNER:
NEXT-PROOF:
EXIT-CONDITION:
```

Les champs non applicables doivent être marqués `N/A-JUSTIFIED` ; ils ne doivent pas être inventés. Si un run est persistant, la projection `RUN_CARD` et son validateur restent obligatoires selon le mode et le risque.

## Résolution des routes

Les noms de route sont des locators documentaires. Pour les résoudre, utiliser le fichier propriétaire, puis son titre exact. Un renvoi qui ne résout pas doit être déclaré obsolète, conceptuel ou `NOT-VERIFIED`; il ne doit jamais être traité comme une instruction active par supposition.

| Préfixe | Propriétaire |
|---|---|
| `DIRECTION/*` | `DIRECTION.md` |
| `ACTION/*` | `ACTION.md` |
| `SAVOIR/*` | `SAVOIR.md` |
| `BIBLIOTHEQUE/*` | `BIBLIOTHEQUE.md` |
| `CHANGELOG/*` | `CHANGELOG.md` |
| `RUN_CARD` | `schemas/run_card.schema.json`, exemple et validateur |

`RUN_CARD` est un **adaptateur machine**, pas un locator Markdown résolvable par `scripts/read_route.py`. Pour l’inspecter ou le valider, utiliser le schéma, l’exemple et `scripts/validate_run_card.py`; ne pas l’invoquer comme une route documentaire.

## Locators principaux

Cette table liste des **raccourcis et sous-locators** ; elle n’est pas un inventaire. `scripts/read_route.py` résout un locator en trois étapes : (1) la table ci-dessous, y compris les sous-locators écrits `titre › titre` ; (2) le préfixe propriétaire et le titre unique qui commence par le locator ; (3) le sous-locator `X/Y/Z`, cherché sous le titre `X/Y`. Un locator porté par deux titres est refusé comme ambigu. Un sous-bloc qui porte son propre locator est exclu du bloc parent et servi séparément. Une route qui ne résout pas ne doit pas être devinée.

| Locator | Destination exacte |
|---|---|
| `DIRECTION/START` | `DIRECTION.md` — `## DIRECTION/START — classer avant d’agir` |
| `DIRECTION/START/TREE` | `DIRECTION.md` — `## DIRECTION/START — classer avant d’agir` › `### Arbre de classification` |
| `DIRECTION/FIRST-OBJECT` | `DIRECTION.md` — `## DIRECTION/FIRST-OBJECT — compiler le brief et produire le premier objet` |
| `DIRECTION/VISUAL_TARGET` | `DIRECTION.md` — `## DIRECTION/VISUAL_TARGET — rendre la direction pilotable` |
| `DIRECTION/DOUBLE-LOOP` | `DIRECTION.md` — `## DIRECTION/DOUBLE-LOOP — créer puis apprendre` |
| `DIRECTION/FAST-PATH` | `DIRECTION.md` — `### DIRECTION/FAST-PATH — encadré d’exécution courte` |
| `ACTION/RUN-LITE` | `ACTION.md` — `### \`ACTION/RUN-LITE\`` |
| `ACTION/RUN-ITER` | `ACTION.md` — `### \`ACTION/RUN-ITER\`` |
| `ACTION/RUN-STANDARD` | `ACTION.md` — `### \`ACTION/RUN-STANDARD\`` |
| `ACTION/RUN-DIRECTION` | `ACTION.md` — `### \`ACTION/RUN-DIRECTION\`` |
| `ACTION/RUN-SYSTEM` | `ACTION.md` — `### \`ACTION/RUN-SYSTEM\`` |
| `ACTION/FIRST-RENDER` | `ACTION.md` — `## ACTION/FIRST-RENDER — qualité initiale attendue` |
| `ACTION/FAST-PATH` | `ACTION.md` — `## ACTION/FAST-PATH — preuve minimale sans rituel` |
| `ACTION/UI-UX-REALITY` | `ACTION.md` — `### ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble` |
| `ACTION/CLOSE-PACKAGE` | `ACTION.md` — `## ACTION/CLOSE-PACKAGE — paquet de clôture` |
| `ACTION/GATE-A` | `ACTION.md` — `## ACTION/GATE-A — plancher objectivable` |
| `ACTION/ROUTING` | `ACTION.md` — `## ACTION/ROUTING — prérequis de jugement et de structure` |
| `ACTION/CLOSE-EXIT-CHECK` | `ACTION.md` — `## ACTION/CLOSE-EXIT-CHECK — test de sortie canonique` |
| `SAVOIR/READ` | `SAVOIR.md` — `## SAVOIR/READ — comment utiliser cette bibliothèque` |
| `SAVOIR/ROUTING` | `SAVOIR.md` — `## SAVOIR/ROUTING — routes stables` |
| `SAVOIR/CRAFT` | `SAVOIR.md` — `# SAVOIR/CRAFT — anti-slop, composition et expression` |
| `BIBLIOTHEQUE/READ` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/READ — responsabilités et convention de route` |
| `BIBLIOTHEQUE/SELECT` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/SELECT — choisir avant de composer` |
| `BIBLIOTHEQUE/COMPONENTS` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/COMPONENTS — couches et dépendances` |
| `BIBLIOTHEQUE/EVOLUTION` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation` |

## Condition d’arrêt

Arrêter la lecture lorsque la décision, le risque, le propriétaire, la sortie, la prochaine preuve et la limite sont suffisamment explicites pour le prochain propriétaire. Continuer uniquement si une section supplémentaire peut modifier l’un de ces éléments. Une décision visuelle peut rester `EXPLORATORY` ; une validation documentaire ne devient pas une preuve d’usage, d’accessibilité, de performance ou de qualité réelle.

