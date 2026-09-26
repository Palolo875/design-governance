---
name: design-governance-practice
description: Usage pratique de Design Governance V1 pour transformer un brief en projet, interface ou application dirigé, poli et vérifiable. Utiliser lorsqu’un humain ou un agent doit choisir un chemin proportionné, produire un artefact, observer une preuve ou sérialiser une RUN_CARD ; charger les sources et références progressivement, sans créer de règles concurrentes.
---

# Design Governance V1 — pratique

## Rôle

Utiliser cette skill comme **couche d’activation et d’apprentissage** de Design Governance V1. Elle aide à passer du brief à l’artefact en gardant une direction située, un premier objet, des composants et assets qui servent le produit, un polish réel et une preuve honnête.

Ne pas utiliser cette skill pour modifier les règles canoniques de V1. Les règles, modes, gates, axes, statuts, preuves, structures et propriétaires appartiennent aux fichiers V1 fournis par l’utilisateur ou le projet. En cas de divergence, charger la source canonique et lui donner priorité.

## Carte de lecture et sortie

Lorsque le package le fournit, utilisez `V1/official/READING_MAP.md` comme vue dérivée pour résoudre le premier chemin, les perspectives conditionnelles et le handoff. Si plusieurs capacités doivent être combinées pour obtenir un résultat créatif, produit, technique ou de preuve plus fort, utilisez ensuite `V1/official/ORCHESTRATION_MAP.md` pour choisir le profil, les intensités et les conditions d’ajustement. Ces cartes ne remplacent aucune source normative.

Une sortie de run a deux formes (copie de façade, voir `ACTION/HANDOFF`). Par défaut, la **réponse visible** :

```text
MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER
```

Pour une reprise ou un run persistant, le **handoff** au niveau du mode (forme courte en `LITE`) :

```text
MODE — DECISION — RISK — SCOPE — ARTIFACT
OBSERVATION/METHOD — PROOF/TRACE-LOCATOR — LIMIT/NOT-VERIFIED
DECISION-CHANGE — NEXT-ACTION — OWNER — NEXT-PROOF — EXIT-CONDITION
```

Les champs non applicables sont marqués `N/A-JUSTIFIED`.

### Activation en 30 secondes

Avant de charger une route, établir : `MODE`, `DECISION`, `RISK`, `NEXT-PROOF` et `OWNER`. Produire ensuite l’artefact ou le diff le plus petit qui peut changer la décision. Observer dans le scope disponible, puis choisir : corriger, approfondir la preuve, rouvrir, reclassifier ou fermer. Ne charger une source ou une référence que si son bénéfice décisionnel peut être nommé.

### Constitution minimale à garder active

Même pour une activation courte, garder ces cinq protections :

1. une direction perceptible lorsque la surface est identitaire ;
2. une ancre inspectable ou une limite explicite lorsqu’une référence guide la décision ;
3. les preuves applicables au mode et au risque ;
4. le mode, le scope, la prochaine preuve et la capacité réellement disponible déclarés avant l’action ;
5. le réel et le beau cadrés ensemble, sans laisser une intention créative masquer un risque d’usage, d’accessibilité ou de robustesse.

Cette constitution ne crée ni mode, ni gate, ni statut. Elle rappelle les protections de `DIRECTION` ; charger la formulation canonique si l’une d’elles peut modifier la décision.

## Préparer le contexte

1. Localiser le paquet V1 réellement fourni. Ne pas supposer qu’un chemin, une archive ou une ancienne copie existe. Si les sources restent indisponibles, le signaler et ne pas présenter une proposition comme un run V1 conforme ; une proposition créative peut rester explicitement hypothétique.
2. Lire `README.md` et `QUICKSTART.md` pour l’orientation ; lire `ORCHESTRATION_MAP.md` si plusieurs capacités ou un résultat créatif ambitieux doivent être composés.
3. Classer la demande avec `DIRECTION/START` avant tout build, modification, vérification, action externe ou décision persistante.
4. Charger ensuite seulement le propriétaire utile : `DIRECTION.md` pour le mode et la cible, `ACTION.md` pour la trace et la preuve, `SAVOIR.md` pour le jugement et le craft, `BIBLIOTHEQUE.md` pour la structure.
5. Lire `references/examples.md` lorsque le parcours est ambigu, lorsqu’un débutant demande « comment faire », ou lorsqu’il faut comparer `LITE`, `DIRECTION` et `SYSTÈME`.
6. Lire `references/flow.md` pour une vue rapide du chemin. Lire `references/machine_projection.md` seulement si un script, un agent délégué ou un handoff a besoin d’une représentation structurée. Lire `references/canonical_minimum.md` uniquement si les sources V1 sont momentanément indisponibles ou si une séparation de termes doit être vérifiée rapidement. Lorsque la projection machine est utilisée, renseigner les champs de traçabilité et exécuter le validateur fourni ; ses invariants sémantiques renforcent la trace sans remplacer `ACTION.md`.

Ne pas charger toutes les références par réflexe. Une aide ne doit être ouverte que si elle peut modifier une décision, un artefact, une preuve, une limite ou la prochaine action. Si le parcours est simple, cette activation courte suffit ; si le risque augmente, conserver la protection et charger la source propriétaire nécessaire.

## Routage et handoff

Après le classement, activer seulement la capacité qui peut modifier la prochaine décision :

- `DIRECTION` pour le mode, le risque, la cible et la direction située ;
- `ACTION` pour tout build, vérification, changement d’état, preuve ou clôture ;
- `SAVOIR` pour un jugement de craft, style, source, contexte ou intégrité ; charger `SAVOIR/STYLE` seulement si un profil d’expression peut modifier la prochaine décision ;
- `BIBLIOTHEQUE` pour une décision de support, grille, scène, objet, micro-interface ou composant ;
- `GOVERNANCE` pour une règle partagée, une route durable, une contradiction canonique ou une évolution du package ; cette responsabilité renvoie à `CHANGELOG.md` et au propriétaire normatif concerné, sans créer de sixième source.

Ces noms décrivent des responsabilités, pas une obligation d’installer six skills. Si une skill propriétaire n’est pas disponible, rester sur les sources V1 fournies ou déclarer la limite ; ne pas inventer un handoff, un statut ou une route.

### Routes canoniques à activer conditionnellement

Pour une direction créative ouverte, charger `DIRECTION/FIRST-OBJECT` et `DIRECTION/DOUBLE-LOOP` ; activer `DIRECTION/DIRECTION-ATELIER` uniquement si l’atelier peut modifier la thèse, l’objet de preuve ou la direction. Pour un brief vague, utiliser `DIRECTION/EXTERNAL-START` avant de construire. Pour l’exécution, `ACTION/ROUTING` détermine les prérequis, `ACTION/STRUCTURED-PROOF` organise les contrats avant build, `ACTION/FIRST-RENDER` juge la qualité initiale et `ACTION/CLOSE-PACKAGE` rassemble la clôture. `ACTION/PIPELINE-DIRECTION` reste la référence de la boucle qualité et du one-shot. Ces routes sont des points de lecture vers les sources propriétaires ; elles ne créent pas de nouvelles règles dans la skill.

## Délégation humain-agent

Lorsqu’un agent exécute V1 pour une personne, active le système silencieusement : l’humain fournit l’objectif, le périmètre, l’autonomie et le seuil de confirmation ; l’agent choisit le mode, charge les sources utiles et conserve la trace dans le projet. Ne demande pas à l’humain de choisir `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME` sauf si le périmètre est réellement ambigu.

Par défaut, restitue la réponse visible (`ACTION/HANDOFF`). Si l’humain demande « pourquoi ? », « qu’as-tu vérifié ? » ou « explique V1 », expose successivement le mode, le risque, les sources, les capacités et la trace complète, sans créer un nouveau statut. Demande confirmation avant toute action externe, irréversible, publique, destructive, financière ou persistante hors du périmètre autorisé. Une `EXECUTION-SNAPSHOT` peut transporter le contexte d’un handoff ; elle ne remplace jamais les sources V1 ni la trace parent. Lorsqu’un profil d’expression ou une décision de style est utilisé, la trace peut porter `profile_decision` ; lorsqu’un run `DIRECTION` est clôturé, `creative_close` décrit la revue créative. Ces champs transportent une décision ou une observation ; ils ne sont ni des verdicts ni des statuts supplémentaires.

Ligne de run minimale : `ID — MODE — DECISION — RISK — NEXT-PROOF — STATE`. L'entrée minimale DIRECTION complète couvre `DECISION`, `RISK`, `SCOPE`, `CONSTRAINT`, `NEXT-PROOF` et `OWNER`. Dans un bloc structuré, `RUN: <id>` peut nommer le run ; il ne crée pas un champ concurrent. Ajouter `DECISION-INTENT` au lancement. Ne produire `DECISION-CHANGE` qu’après une observation ayant réellement modifié, confirmé ou abandonné la décision.

## Noyau d’exécution

Suivre le chemin : **classer → diriger → construire → vérifier → corriger → fermer**. Pour les runs `DIRECTION`, le one-shot est une compression de cycles après observation réelle du premier rendu, jamais une absence de jugement ; la boucle qualité (`ACTION/PIPELINE-DIRECTION`) couvre la préparation, la construction, l’observation, la correction et la décision.

## Table de charge obligatoire

Avant de construire, charge seulement les sources indiquées pour le mode. Les modules de la colonne « non chargé par défaut » restent activables si une décision ou un risque déclaré les rend nécessaires ; ils ne sont jamais une interdiction de consulter une source critique.

| Mode | Charger d’abord | Non chargé par défaut |
|---|---|---|
| `LITE` | `DIRECTION/START/TREE`, `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. | Atlas, atelier, `VISUAL_TARGET`, Gate C et routes structurelles de `BIBLIOTHEQUE`. |
| `ITER` | `DIRECTION/START`, `ACTION/RUN-ITER`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. | Atlas, atelier et `VISUAL_TARGET`, sauf si la direction, le système ou le risque change ; Gate C seulement si le craft change. |
| `STANDARD` | `DIRECTION/START`, `ACTION/RUN-STANDARD` et `BIBLIOTHEQUE/SELECT` si la structure est ouverte. | Atelier, `CFT-00` et Gate C, sauf si la qualité créative ou le craft est l’objet de la décision. |
| `DIRECTION` | `DIRECTION/START`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `ACTION/ROUTING`, `ACTION/FIRST-RENDER`, `ACTION/RUN-DIRECTION`, `SAVOIR/CRAFT/CFT-00` et gates A/B/C. | Atlas, `DIRECTION-ATELIER` et `SAVOIR/STYLE`, sauf si une famille, un atelier ou un profil nommé peut modifier la décision. |
| `SYSTÈME` | `DIRECTION/START`, `ACTION/RUN-SYSTEM` et `BIBLIOTHEQUE/COMPONENTS`. | Atelier et `CFT-00`, sauf si l’expression visuelle du système partagé est elle-même une décision. |

La table règle la charge documentaire ; elle ne réduit jamais le mode, le niveau de preuve ou la protection d’un risque. Si un risque critique, une surface identitaire, une contrainte culturelle ou une capacité manquante exige une source supplémentaire, active-la et conserve la justification dans la trace existante. Le Core doit rester exécutable : un run `LITE` ne lit pas tout le corpus pour corriger une petite surface.

### Approfondir seulement si nécessaire

Après l’activation express, appliquer cette règle de charge : `DIRECTION/START` pour classer ; `DIRECTION` si la direction ou la cible change ; `ACTION` dès qu’un artefact, une preuve, un état ou une clôture est concerné ; `SAVOIR` si le jugement, le craft, la source ou le contexte peut changer la décision ; `BIBLIOTHEQUE` si la structure, le composant ou la micro-interface peut changer la décision ; `CHANGELOG` uniquement si une règle, une route ou une responsabilité partagée évolue.

Cette règle ne remplace aucune source propriétaire et ne constitue ni un nouveau mode ni un nouveau gate. Charger `FIRST-OBJECT`, `FIRST-RENDER`, `CFT-00` ou le premier objet habitable seulement lorsque la décision concernée l’exige ; ne pas remplir plusieurs grilles en parallèle lorsqu’une route principale suffit. Si le risque ou la décision change, recalculer la charge.

**Activation positive.** Chaque source doit être chargée pour le gain qu’elle peut produire : `DIRECTION` pour obtenir une position située et un premier objet plus fort ; `SAVOIR` pour transformer une impression en jugement et en choix de craft ; `BIBLIOTHEQUE` pour rendre la structure habitable, compatible et maintenable ; `ACTION` pour transformer la décision en livraison observable, corrigible et prouvable. Si le bénéfice attendu ne peut pas être nommé, ne charge pas la source par réflexe ; si une décision critique peut changer, ne sacrifie pas la profondeur au seul chemin court.

### Classer

Déterminer le mode parmi `LITE`, `ITER`, `STANDARD`, `DIRECTION` et `SYSTÈME`, le risque dominant, la décision à changer et la prochaine preuve la moins coûteuse. Une tâche locale ne devient pas `DIRECTION` parce qu’elle doit être jolie ; une surface identitaire ne doit pas être réduite à un correctif technique.

### Diriger

Pour une surface créative, formuler une thèse située, une silhouette, un premier objet, une relation de contenu, un rôle d’asset ou de matière, une anti-direction et une condition de retrait. Activer `SAVOIR/CRAFT/CFT-00` lorsque la qualité perceptuelle est une décision : examiner présence, point de vue, culture visuelle transformée, spécificité, composition, désirabilité, résolution et retenue. Activer aussi `DIRECTION/FIRST-OBJECT` pour la grille à 8 dimensions et la compilation du brief vers le premier objet. Charger `ACTION/FIRST-RENDER` pour le contrat de qualité initiale du premier rendu. Activer `SAVOIR/STYLE` seulement si une grammaire d’expression peut changer cette décision ; choisir un profil pilote, un dial ou l’absence de profil, jamais un style par défaut. Viser dès le premier rendu le niveau d’`ACTION/FIRST-RENDER`, sans style par défaut.

Avant ce build, activer `DIRECTION/CREATIVE-BOOT` pour une décision visuelle ouverte : promesse, objet de preuve, geste, anti-directions concrètes, tension et signature structurelles (nombre d’axes : `BIBLIOTHEQUE/TENSION`), jusqu’à trois cibles créatives `SAVOIR/CRAFT`, `MODAL`/`PARTI` (d’où viennent les anti-directions), bilan de fabrication (`FABRICATION`), premier objet et défaut dominant. Ce boot est une vue de cadrage, non un nouveau mode, gate, statut, score ou champ machine concurrent. Les cibles CFT orientent la construction ; elles ne diminuent pas les protections d’usage, d’accessibilité, de robustesse ou de risque critique. Omettre ou condenser le boot pour un delta strictement local lorsque ces décisions ne changent pas. Sur brief vague, demander au plus trois intrants, dans cet ordre : contenu réel, marque, asset principal, destination (`DIRECTION/EXTERNAL-START`) ; construire dans tous les cas.

Pour un nouveau domaine, une audience incertaine ou une décision à forte conséquence, activer `DIRECTION/DOMAIN-FRAME` avant les routes expressives. Déclarer domaine, public, JTBD, modèle de confiance, actions critiques, conventions, contexte culturel, tolérance à l’écart, exigences de preuve et déclencheur de profondeur. Lorsque le déclencheur est actif, charger `SAVOIR/SOURCE` pour une recherche orientée décision et conserver observation, retenue, rejet, transformation, décision changée et limite ; ne jamais transformer une collection de références en direction.

Pour juger une proposition premium, examiner la relation entre clarté, cohérence, précision, singularité maîtrisée et confiance. Ce repère est une lentille de critique, jamais un score ou un verdict ; ne confonds pas premium avec minimalisme, espace vide, contraste faible ou effet décoratif.

Pour une décision créative, alterner comprendre le public et le JTBD, ouvrir plusieurs directions réellement distinctes, converger vers une proposition principale, puis prouver par un artefact observé dans son scope. Annoter les références et moodboards par la décision qu’ils peuvent modifier ; retirer toute variante qui ne change ni la compréhension, ni la tâche, ni la direction, ni la preuve. Ne traite jamais l’anti-slop, la retenue ou le premium comme un canon visuel unique : une expression forte, populaire, joyeuse, dense, étrange, vernaculaire ou maximaliste peut être juste si elle sert le contexte, le public et la décision. Lorsque l’enjeu culturel, identitaire ou irréversible le justifie, cherche un contrepoint situé ; ne produis pas de variantes artificielles uniquement pour satisfaire une procédure.

Les composants et assets visibles peuvent être conçus pour le produit lorsque cela augmente la compréhension, la valeur ou la mémoire. Garder les primitives critiques robustes, sémantiques, accessibles et fonctionnelles. Ne pas confondre singularité avec nouveauté forcée.

### Construire

Produire un artefact réel ou modifier l’artefact existant. Autoriser code, SVG, canvas, image, vidéo, texture, illustration, objet 3D, asset curaté ou combinaison hybride lorsque le rôle, la livraison et les limites sont clairs. Ne pas ajouter d’effet, d’asset ou de composant sans conséquence identifiable.

Pour une UI/UX nouvelle, construire avec la réalité du produit : contenu crédible, tâche principale, premier geste, feedback, états critiques, contenu extrême, responsive recomposé, focus, récupération et robustesse selon le risque. Une capture nominale ne suffit pas si les états ou la récupération changent la décision ; utiliser `ACTION/UI-UX-REALITY` et déclarer le scope réellement observé.

### Vérifier

Comparer intention, artefact et observation. Inspecter le rendu réel dans le scope disponible ; vérifier le geste, les états, le responsive, le focus et le reduced motion lorsque le risque le requiert. Lorsque le risque visuel ou identitaire le demande, juger aussi hiérarchie, composition, typographie, matière, spécificité, cohérence, retenue et résolution. Distinguer une direction artistique située, un craft construit, un polish résolu, une créativité pertinente et un goût situé ; aucune de ces qualités ne devient un score ou un verdict automatique. Après la première scène et avant la clôture d’un run `DIRECTION`, produire une revue créative courte (`creative_close` dans la RUN_CARD) : présence effectivement produite, signature spécifique, détail ou état révélant le craft, défaut dominant et prochaine action de polish. Fermer avec `ACTION/CLOSE-PACKAGE` pour le paquet de clôture. Cette revue cite un artefact ou une observation et ne remplace aucune preuve d’usage, d’accessibilité ou de robustesse. Séparer toujours `A/B/C` de `V/U/A/T`, et `STATE`, `ISSUE`, `VERDICT` du statut de direction.

Une rationale, une référence, une présélection de l’atlas, une ancre, un asset ou une belle capture ne constitue pas une preuve indépendante. Seul un résultat observé dans le scope déclaré peut alimenter `DECISION-CHANGE` ou un verdict.

### Corriger et fermer

Corriger le défaut dominant plutôt que produire de nombreuses variantes. Rattacher la preuve à l’artefact, déclarer `NOT-VERIFIED`, `NOT-OBSERVED`, `N/A-JUSTIFIED` ou l’issue appropriée lorsque nécessaire, puis fermer avec les limites restantes. Ne jamais appeler `POLISHED`, `SLOP-FREE` ou une qualité universelle comme un statut. Les signaux de réouverture (`DIRECTION/FIRST-OBJECT`) — thèse absente, foyer perdu, signature générique, objet de preuve manquant, résolution insuffisante, état ou runtime non tenu — déclenchent un retour créatif, pas un gate supplémentaire.

## Anti-slop opératoire

Chercher et retirer les patterns interchangeables, le composant soup, les cartes répétées, la matière décorative, les données fictives non marquées, les rationales non implémentées, les assets sans rôle et les variantes qui ne changent aucune décision. Préférer une proposition principale et une alternative seulement si elle change une décision située.

Le polish est la résolution cohérente de la structure, du contenu, de la typographie, de la matière, de l’action et des états ; ce n’est pas une couche de blur, de gradients, d’ombres ou de gros rayons. Un rendu peut être poli mais générique, créatif mais incompréhensible, ou visuellement convaincant sans preuve d’usage ; restituer la qualité observée avec sa limite plutôt qu’une qualité universelle.

## Sortie attendue

Livrer d’abord l’artefact ou le diff. Donner ensuite le handoff au niveau du mode (forme courte en `LITE`, voir `ACTION/HANDOFF`). Pour un handoff, utiliser la projection machine-readable comme transport, jamais comme source de vérité. Ne pas réciter la skill ou produire un dossier de gouvernance si le run ne le nécessite pas.

Toujours identifier l’owner de la décision finale. Une capacité technique ou un profil d’agent n’est pas une autorisation : lorsque l’agent agit au nom d’un owner, expliciter seulement si cela peut changer la décision, le risque, la persistance ou une action externe la portée d’action autorisée, la base de l’autonomie et la condition de reprise ou d’escalade. Un checkpoint indisponible ne justifie pas une baisse silencieuse du mode et `APPROVED` ne signifie pas que le résultat est accepté. Pour les assets, références, données ou captures sensibles, déclarer la provenance et les restrictions pertinentes ; une provenance ne vaut pas une licence, et une limitation de vérification n’autorise jamais le partage d’un contenu confidentiel. Arrêter le polish lorsque le défaut dominant est corrigé ou explicitement réservé, qu’une itération supplémentaire ne promet plus de changement visible ou utile, et que la prochaine action est définie. Ne remplis jamais un quota de variantes ou de finition pour satisfaire la procédure.

## Références conditionnelles

- **Exemples complets :** lire [references/examples.md](references/examples.md) pour voir des parcours `LITE`, `DIRECTION` et `SYSTÈME`, y compris `FIRST-OBJECT` et un profil de style situé.
- **Direction créative :** charger `DIRECTION/FIRST-OBJECT`, `DIRECTION/DOUBLE-LOOP` et, si nécessaire, `DIRECTION/DIRECTION-ATELIER` ; activer `DIRECTION/EXTERNAL-START` pour un brief vague.
- **Flux de décision :** lire [references/flow.md](references/flow.md) pour la vue Mermaid courte et son équivalent texte.
- **Profil d’expression :** lire `SAVOIR/STYLE` dans la source canonique pour choisir ou refuser une grammaire d’expression ; ne pas traiter un style comme une recette.
- **Projection machine :** lire [references/machine_projection.md](references/machine_projection.md) pour sérialiser une `RUN_CARD` ou une `EXECUTION-SNAPSHOT` existante.
- **Aide-mémoire minimal :** lire [references/canonical_minimum.md](references/canonical_minimum.md) seulement si les sources V1 ne sont pas disponibles ou si les séparations critiques doivent être rappelées sans charger le corpus.

