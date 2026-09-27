# Design Governance V1.1.1

Design Governance V1 est un cadre de **direction, de création, de jugement et de vérification du design**. Il aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

Le corpus s’adresse à un designer, une équipe produit ou un agent qui doit produire un travail visuellement dirigé, spécifique, construit et poli, tout en rendant ses décisions, ses preuves et ses limites lisibles.

> **Statut expérimental :** Design Governance V1.1.1 est une expérimentation maintenue. La baseline est contrôlée et destinée à un usage supervisé ; elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage, ni conformité sans preuve adaptée.

## Fiche de version

| Élément | État |
|---|---|
| Contrat documentaire et machine | Validé avec réserves explicites |
| Build et distributions | Validés et reproductibles |
| Architecture de lecture | Durcie ; carte dérivée disponible |
| Efficacité sur des runs réels | `NOT-VERIFIED` |
| Usage recommandé | Pilote contrôlé, revue humaine et preuve adaptée |

La carte [`V1/official/READING_MAP.md`](V1/official/READING_MAP.md) résout le premier chemin, l’activation multi-perspective, les handoffs et les locators principaux. Elle est dérivée et non normative. Les cinq sources officielles, le schéma `RUN_CARD` et leurs validateurs restent les autorités.

Pour exploiter plusieurs capacités sans les charger mécaniquement, utilisez la [`ORCHESTRATION_MAP.md`](V1/official/ORCHESTRATION_MAP.md). Cette vue dérivée compose les résultats recherchés, les capacités, les intensités, les patterns créatifs et la preuve ; elle ne crée aucun mode ni aucune règle concurrente.

## Par où commencer

Pour utiliser le système, commencez par [`V1/official/QUICKSTART.md`](V1/official/QUICKSTART.md). Le parcours minimal est :

> **Classer → diriger → construire → observer → corriger → fermer.**

### Démarrage express — 90 secondes

Avant de lire une route détaillée, écrivez seulement :

```text
MODE — DECISION — RISK — NEXT-PROOF — OWNER
```

Puis produisez ou retrouvez l’artefact, observez-le dans son scope et choisissez une seule suite : corriger, approfondir la preuve, rouvrir la direction, reclassifier ou fermer. Le [Quickstart](V1/official/QUICKSTART.md) explique ensuite le parcours complet ; le [Glossaire](V1/official/GLOSSAIRE.md) donne les définitions utiles sans créer de nouvelles règles.

Si le vocabulaire est nouveau, consultez ensuite [`V1/official/GLOSSAIRE.md`](V1/official/GLOSSAIRE.md). Avant d’ouvrir les routes détaillées, établissez seulement cinq éléments : **mode**, **risque dominant**, **décision à changer**, **prochaine preuve** et **owner**. Chargez ensuite uniquement la source capable de modifier la prochaine décision : `DIRECTION` pour le cadrage, `ACTION` pour la preuve et la clôture, `SAVOIR` pour le jugement, ou `BIBLIOTHEQUE` pour la structure. Activez les modules conditionnels seulement lorsqu’un risque, une décision ou une capacité manquante le justifie ; ne chargez pas tout le corpus par réflexe. `DIRECTION/START` reste l’unique classification.

### Choisir le chemin court

| Situation | Chemin de départ | Point d’attention |
|---|---|---|
| Correction locale à faible risque | `LITE` | Preuve minimale et scope étroit. |
| Retouche d’une surface dont la direction existe et est retrouvable | `ITER` | La correction doit modifier l’artefact ou la décision. |
| Construction produit standard | `STANDARD` | Structure, contenu réel, états et usage proportionnés. |
| Identité, premier contact ou direction visuelle autonome | `DIRECTION` | Premier objet, cible visuelle, craft et preuve réelle. |
| Système partagé ou bibliothèque | `SYSTÈME` | Cohérence inter-surfaces, robustesse et promotion. |

Classement : voir `DIRECTION/START`.

Ces chemins sont des points d’entrée vers les contrats propriétaires, non de nouvelles règles du README. Pour une surface créative, le premier rendu doit déjà être composé, spécifique, crédible et suffisamment résolu selon le risque. Le `one-shot` peut compresser les cycles seulement après observation réelle ; il ne supprime ni le jugement ni la preuve applicable.

Le README oriente la navigation. Il ne crée aucune règle concurrente. Les sources normatives font foi dans leur périmètre.

## Constitution minimale

Les cinq absolus transversaux de `DIRECTION` forment le noyau de protection de V1 : une surface identitaire doit avoir une direction perceptible ; une surface identitaire ne doit pas être dessinée uniquement de mémoire ; aucune livraison ne contourne les preuves applicables ; le mode, la preuve et le budget doivent être déclarés avant l’exécution ; le réel et le beau doivent être cadrés ensemble.

Ces absolus ne remplacent pas les procédures propriétaires d’`ACTION`, de `SAVOIR` ou de `BIBLIOTHEQUE`. Ils rappellent la priorité de gouvernance et renvoient à [`DIRECTION.md`](V1/official/DIRECTION.md#les-cinq-règles-absolues), qui reste la source normative. Le piège de conformité est explicite : une conformité de surface ne vaut ni direction perceptible, ni preuve d’usage, ni qualité réelle.

## Le modèle à double boucle

V1 sépare deux boucles qui se répondent :

| Boucle de création | Boucle de gouvernance et d’amélioration |
|---|---|
| Cadrer le produit et le public. | Classer le risque et le mode. |
| Cultiver des références et un territoire lorsque cela peut changer la décision. | Définir le scope et la preuve nécessaire. |
| Ouvrir puis sélectionner une direction située. | Protéger les contraintes critiques. |
| Composer et construire une scène complète, avec les assets et composants utiles. | Observer le rendu réel et ses limites. |
| Polir la proposition sans confondre finition et décoration. | Isoler le défaut dominant, corriger l’artefact, observer à nouveau et décider. |

La seconde boucle ne se résume pas à une critique textuelle. Lorsque la décision créative ou perceptuelle est en jeu, son chemin est :

> **Observer → isoler le défaut dominant → modifier l’artefact → observer à nouveau → comparer → décider.**

La trace doit dire ce qui a changé, ce qui n’a pas été vérifié et ce qui doit se passer ensuite. Une preuve technique ne devient pas automatiquement un jugement esthétique ; une intention créative ne masque pas une preuve d’usage ou d’accessibilité manquante.

## Structure du dépôt

| Couche | Chemin | Responsabilité |
|---|---|---|
| **Sources et guides** | `V1/official/` | Corpus normatif et guides d’entrée de la V1. |
| **Activation pratique** | `skills/design-governance-practice/` | Couche d’activation et références conditionnelles ; elle ne crée pas de règles concurrentes. |
| **Projection machine** | `schemas/` | Schéma, exemple et fixtures de la projection `RUN_CARD`. |
| **Contrôles et distributions** | `scripts/` | Validation du package, validation des RUN_CARD et génération des exports. |

Les cinq sources normatives sont les suivantes :

| Source | Décision principalement couverte |
|---|---|
| `DIRECTION.md` | Mode, risque, absolus, direction, cible et capacité. |
| `ACTION.md` | Procédures, preuve, gates, états, verdicts et clôture. |
| `SAVOIR.md` | Jugement, craft, contenu, contexte, styles, sources et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, évolution, cycle de vie et décisions de gouvernance. |

`README.md`, `QUICKSTART.md` et `GLOSSAIRE.md` facilitent l’orientation et la compréhension ; ils ne créent pas de route, de gate, de statut ou d’autorité supplémentaire.

Pour charger uniquement un bloc documenté, utilisez `python3 scripts/read_route.py DIRECTION/START`. Pour une carte concrète, `python3 scripts/validate_run_card.py --strict chemin/vers/run_card.json` complète la validation structurelle en rejetant les placeholders et en contrôlant les locators d’artefacts locaux.

## Source de vérité et distributions

Le dépôt GitHub est la **source de vérité**. La distribution Local est un export dérivé et ne doit pas être modifiée à la main. Pour produire les deux archives, exécutez :

```bash
./scripts/build_distributions.sh
```

Le build régénère les distributions de travail dans `dist/` et écrit les archives déterministes suivantes à la racine du dépôt :

```text
Design_Governance_V1_GITHUB.zip
Design_Governance_V1_LOCAL.zip
```

Les modifications doivent être apportées aux sources du dépôt, puis vérifiées par les contrôles et le build. Les archives et exports ne sont pas des sources normatives indépendantes.

## Validation

Les scripts sont autonomes et ne nécessitent aucune dépendance Python tierce. Utilisez Python **3.10 ou plus récent**.

La projection machine comprend aussi les contrats de production : `DOMAIN_FRAME`, `RESEARCH_BRIEF` et les contrats de direction créative, de réalité UI/UX et d’évaluation. Ils sont illustrés dans `schemas/examples/` et contrôlés par `scripts/validate_contracts.py`.

| Commande | Fonction |
|---|---|
| `python3 scripts/validate_design_governance.py` | Contrôle l’inventaire, les liens Markdown relatifs, le vocabulaire structuré et les conventions du package. |
| `python3 scripts/validate_run_card.py` | Exécute la suite intégrée de validation des projections et des fixtures `RUN_CARD`. |
| `python3 scripts/validate_run_card.py chemin/run.json` | Valide un fichier JSON ciblé et échoue s’il est absent, malformé ou sémantiquement invalide. |
| `python3 scripts/validate_contracts.py --type production_contracts chemin/contrat.json` | Valide un contrat ciblé, y compris hors du package ; sans `--type`, la famille est détectée par les clés racines. |
| `python3 scripts/validate_reading_map.py` | Vérifie la carte de lecture, ses propriétaires, ses locators et sa frontière non normative. |
| `python3 scripts/validate_all.py` | Exécute les contrôles documentaires, machine, CLI, fixtures négatives, compilation et reproductibilité des distributions. |

```bash
python3 scripts/validate_design_governance.py
python3 scripts/validate_run_card.py
python3 scripts/validate_run_card.py chemin/run.json
python3 scripts/validate_all.py
```

Ces contrôles établissent la cohérence du package, de ses projections et de ses distributions. Ils ne remplacent ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption. Une projection `RUN_CARD` valide reste une trace structurée ; elle ne transforme pas une cible de conformité, une capture ou une validation CLI en preuve de résultat.

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close ; elle n’atteste ni la réalité des observations, ni la justesse des jugements, ni la qualité perceptuelle. La liste exacte vit en un seul lieu : la frontière de validation d’`ACTION/RUN_CARD`.

## Limites et discipline d’usage

Une capture prouve un rendu dans son scope ; elle ne prouve pas à elle seule une tâche utilisateur, un lecteur d’écran, une sécurité, une performance ou une intégration réelle. Une trace complète sans conséquence est du slop procédural : si une étape, une variante, une référence ou un tag ne change aucune décision, observation, preuve, limite ou prochaine action, retirez-le ou justifiez `N/A-JUSTIFIED`.

La qualité créative reste située. Une proposition peut être visuellement convaincante sans avoir prouvé l’usage, l’accessibilité ou la robustesse ; elle peut aussi être conforme et robuste tout en restant générique ou insuffisamment résolue. V1 demande de rendre cet écart visible et de corriger le défaut dominant plutôt que de le compenser par une autre preuve.

## Profils de lecture

| Lecteur | Commencer par | Sortie attendue |
|---|---|---|
| Designer ou équipe produit | `QUICKSTART.md` | Décision, artefact, observation et prochaine action. |
| Reviewer ou lead | `READING_MAP.md`, puis `ACTION.md` | Preuve dans le scope, limites et décision de clôture. |
| Agent | `QUICKSTART.md`, puis `SKILL.md` | Artefact livré, trace proportionnée et escalade explicite. |
| Mainteneur du package | `README.md`, `CHANGELOG.md`, validateurs | Contrat cohérent, testable et reproductible. |

