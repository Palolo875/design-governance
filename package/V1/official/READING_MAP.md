# READING_MAP — carte dérivée de lecture et d’activation

**Statut :** guide dérivé non normatif. Les cinq sources normatives, le schéma `RUN_CARD` et les validateurs propriétaires font foi en cas de divergence.

## Utilisation

Cette carte réduit la recomposition mentale du lecteur. Elle ne crée ni mode, ni gate, ni axe, ni statut, ni verdict, ni owner de décision supplémentaire. Elle indique seulement où commencer, quoi charger, ce qui doit sortir et quand transmettre.

Pour composer plusieurs capacités selon un résultat recherché — direction, beauté située, créativité, usage, preuve, vitesse ou système — voir la section « Combinaisons par résultat recherché » ci-dessous : elle aide à ajuster la combinaison et l’intensité sans remplacer les propriétaires normatifs.

## Chemin canonique de démarrage

1. Localiser la version V1 réellement fournie.
2. Lire `QUICKSTART.md` ou cette carte si le besoin est déjà identifiable.
3. Ouvrir `DIRECTION/START` pour classer le mode et le risque dominant.
4. Charger uniquement le propriétaire capable de modifier la prochaine décision.
5. Ouvrir `ACTION` dès qu’un artefact, une observation, une preuve, un état ou une clôture est concerné.
6. Persister la sortie selon le contrat `RUN_CARD` lorsque le run doit être repris, comparé ou fermé.

`DIRECTION/START` reste la seule classification. Cette carte ne reclassifie pas.

## Constitution minimale

Les cinq absolus de `DIRECTION` protègent chaque run : résumé dans la section « Constitution minimale » du README du package, formulation canonique dans [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).

## Routage minimal par décision

| Décision dominante | Première lecture | Ajouter seulement si nécessaire |
|---|---|---|
| Brief vague ou risque inconnu | `DIRECTION/START` | `DIRECTION/EXTERNAL-START` |
| Correction locale | `DIRECTION/START` → `ACTION/RUN-LITE` ou `RUN-ITER` | `SAVOIR` ou `BIBLIOTHEQUE` si la décision change |
| Nouvelle surface opérationnelle | `DIRECTION/START` → `ACTION/RUN-STANDARD` | `BIBLIOTHEQUE/SELECT`, `SAVOIR/CONTEXT` |
| Direction identitaire | `DIRECTION/START` → `DIRECTION/CHARGE` (mode `DIRECTION`) | `SAVOIR/CRAFT`, `DIRECTION/DIRECTION-ATELIER` |
| Structure ou composant partagé | `DIRECTION/START` → `ACTION/RUN-SYSTEM` | `BIBLIOTHEQUE/COMPONENTS`, `SAVOIR/SYSTEM`, `CHANGELOG` |
| Preuve, vérification ou clôture | `ACTION` | Gate et route correspondant au risque |
| Règle ou route durable | `CHANGELOG` et source propriétaire | `ACTION` pour preuve et `BIBLIOTHEQUE/EVOLUTION` si structure |

Sortie : réponse visible et trace légère par défaut ; handoff et clôture (`ACTION/CLOSE-PACKAGE`) en trace complète (`ACTION/HANDOFF`).

## Combinaisons par résultat recherché

Cette section aide à combiner plusieurs capacités lorsque chacune peut **modifier la même décision** ou **protéger un risque déclaré**. Elle ne crée ni mode, ni route, ni gate, ni statut, ni verdict, ni champ machine. Le mode est d’abord classé par `DIRECTION/START` ; la combinaison est ensuite choisie selon le résultat recherché et le scope réel.

> **Principe :** ne pas charger le maximum de routes ; composer le maximum de contribution pertinente. Toute capacité activée doit avoir une contribution nommable et être retirée si elle ne change ni la décision, ni l’artefact, ni la preuve, ni la limite, ni la prochaine action.

La combinaison choisie reste dans la trace existante du run, seulement si elle peut modifier la décision. Ne crée pas une trace par capacité et ne transforme pas une table d’orientation en preuve.

| Résultat recherché | Noyau possible | Renforcement seulement si nécessaire | Preuve à privilégier |
|---|---|---|---|
| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) | `DIRECTION/CREATIVE-BOOT`, `DIRECTION/DOMAIN-FRAME`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE`, `SAVOIR/STYLE`, `BIBLIOTHEQUE/SELECT` | Premier objet réel, revue créative, observation du défaut dominant et correction réellement observée. |
| **Beauté, goût et craft situés** | `DIRECTION/FIRST-OBJECT` + `SAVOIR/CRAFT` + `ACTION/FIRST-RENDER` | `SAVOIR/STYLE`, contenu crédible, matière, typographie ou ancre lorsque chacun peut modifier le jugement | Rendu réel dans le scope ; jugement créatif séparé des preuves d’usage, d’accessibilité et de robustesse. |
| **Créativité variée mais utile** | `DIRECTION/CREATIVE-BOOT` + `DIRECTION/VISUAL_TARGET` + une alternative située | `DIRECTION/DOMAIN-FRAME`, `SAVOIR/SOURCE` ou atelier seulement si l’axe de divergence change une décision | Comparaison dans le même scope par public, JTBD, promesse, geste, structure ou expression. |
| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + `ACTION/GATE-A` (contrôles applicables) + contenu et états réels | Responsive, focus, récupération, runtime ou `SAVOIR/CONTEXT` selon le risque | Tâche, états, viewports, contenu extrême, clavier ou méthode adaptée au claim. |
| **Preuve et décision fiables** | `ACTION/STRUCTURED-PROOF` + artefact réel + gate correspondant au risque + `ACTION/CLOSE-EXIT-CHECK` | Preuve croisée ou `RUN_CARD` stricte si la persistance l’exige | Claim, méthode, scope, date, artefact, limite et `TRACE-LOCATOR` retrouvables. |
| **Vitesse sans appauvrissement** | `DIRECTION/START` + `ACTION/FAST-PATH` + `LITE` ou `ITER` correctement classé | Ajouter une seule capacité si elle peut changer la décision ; reclassifier si le risque ou le périmètre augmente | Artefact réel, observation ciblée, preuve minimale applicable et prochaine action. |
| **Système maintenable** | `ACTION/RUN-SYSTEM` + `BIBLIOTHEQUE/COMPONENTS` si un composant change + migration, rollback et `CHANGELOG` (paquet SYSTÈME) | `BIBLIOTHEQUE/EVOLUTION` ou `SAVOIR/SYSTEM` selon la décision partagée | Consumers, compatibilité, non-régression, owner, migration et condition de reprise. |
| **Domaine sensible ou incertain** | `DIRECTION/DOMAIN-FRAME` + `SAVOIR/SOURCE` + `ACTION/STRUCTURED-PROOF` | Contexte culturel, conventions, confiance ou recherche seulement si un déclencheur peut changer la décision | Source ou observation reliée à la décision, transformation, rejet et limite. |
| **Agent contrôlé** | `DIRECTION/START` + `ACTION/AUTHORITY` + `SKILL.md` + owner | Cette carte seulement si plusieurs capacités sont réellement nécessaires ; `RUN_CARD` en trace complète (run persistant, partagé, audité ou acceptation demandée), quel que soit le nombre de capacités | Artefact livré, autonomie exercée, décision, preuve, limite, escalade et prochaine action. |

Ces combinaisons ne sont pas des parcours obligatoires. Elles indiquent des capacités compatibles ; les sources propriétaires définissent le contenu exact des routes.

### Variation créative

Pour produire du beau varié sans bruit : `SAVOIR/CRAFT/CFT-02` (un axe situé à la fois).

Une alternative est utile si elle peut modifier le choix. Une référence, une ancre, une rationale ou une variante ne constitue pas une preuve indépendante.

### Garde-fous de la combinaison

- `ITER` signifie une itération sur une direction ou un système existant retrouvable, dans son périmètre ; il ne signifie pas simplement « quelque chose existe déjà ».
- Un chemin court ne réduit jamais la protection d’un risque critique.
- Une capacité indisponible limite le claim correspondant ; elle ne justifie pas une baisse silencieuse du mode.
- Ne pas remplir toutes les routes d’une combinaison si une route principale suffit.
- Ne pas ajouter de trace, de variante ou de preuve qui ne peut changer la décision, l’artefact, la limite ou l’action suivante.

Arrêter l’orchestration lorsque la décision, le risque, le scope, l’owner, l’artefact, la preuve, la limite et la prochaine action sont suffisamment explicites. La richesse de lecture n’est pas un résultat ; **l’effet positif observable dans le périmètre déclaré** est le résultat recherché.

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

