# Design Governance V1.1.1

Design Governance V1 est un cadre de **direction, de création, de jugement et de vérification du design**. Il aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

> **Statut expérimental :** Design Governance V1.1.1 est une expérimentation maintenue. La baseline est contrôlée et destinée à un usage supervisé ; elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage, ni conformité sans preuve adaptée.

<!-- entree:début -->
## Commencer

Design Governance aide un agent à produire un design dirigé, construit et soigné dès la première proposition, puis à l’améliorer avec vous. Vous n’avez besoin de connaître ni les modes, ni le vocabulaire interne : l’agent s’en charge.

**1. Que demander ?** Décrivez en quelques phrases ce que vous voulez obtenir (une page, un écran, une identité, une correction), pour qui, et où cela servira : démonstration, maquette ou vrai produit. S’il s’agit d’un vrai commerce ou d’un vrai service, dites-le.

**2. Que fournir ?** Ce que vous avez déjà : textes, prix, horaires, logo, couleurs, photos (même prises au téléphone, à la lumière du jour), exemples que vous aimez, lien vers l’existant. Vos textes, votre marque et vos photos aident à produire une proposition plus spécifique et crédible. S’il en manque, l’agent vous pose au plus trois questions, en un seul message, seulement celles qui améliorent vraiment le résultat : contenu réel, marque, image principale ou source d’images autorisée, destination si elle est incertaine. Il construit la proposition dans tous les cas.

**3. Que recevoir ?** Une première proposition réellement construite, pas un gabarit vide. La réponse dit simplement ce qui a été fait et pourquoi, ce qui est un exemple à remplacer, ce qui manque pour la vraie version, et la suite proposée. C’est une proposition à discuter, pas une validation : pour retenir cette direction pour un vrai produit, l’agent doit s’appuyer sur des éléments réels, observés ou fournis, et effectuer les vérifications nécessaires.

**4. Comment poursuivre ?** Validez, réorientez ou arrêtez. Dites en une phrase ce qui ne va pas (« le titre écrase la photo », « trop froid pour une boulangerie ») : l’agent corrige le défaut principal, regarde de nouveau le résultat et vous dit ce qui a changé. Avant toute action irréversible ou coûteuse (publier, envoyer, payer, remplacer l’existant), il vous demande votre accord.

Pour aller plus loin : le [guide opérateur](V1/official/QUICKSTART.md), la [skill](skills/design-governance-practice/SKILL.md) pour les agents, le [glossaire](V1/official/GLOSSAIRE.md) et les [sources normatives](V1/official/README.md).
<!-- entree:fin -->

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

## Mission

> Aider à créer des projets dirigés, construits et spécifiques, puis rendre visibles les décisions, les preuves et les limites qui permettent de les juger honnêtement.

Le corpus s’adresse à un designer, une équipe produit ou un agent qui doit produire un travail visuellement dirigé, spécifique, construit et poli, tout en rendant ses décisions, ses preuves et ses limites lisibles.

V1 vise une première proposition composée, spécifique et soignée, sans imposer un registre esthétique par défaut. La méthode protège l’ambition de création — présence, point de vue, culture visuelle, spécificité, craft et polish — sans confondre une référence, une rationale, un asset ou une capture avec une preuve d’usage. Lorsqu’une décision exige une trace structurée, la `RUN_CARD` rassemble le mode, le risque, la décision, l’artefact, la preuve, la limite et la clôture. Pour les runs multi-domaines ou de profondeur élevée, les contrats `DOMAIN_FRAME`, `RESEARCH_BRIEF`, `CREATIVE_DIRECTION_SET`, `UI_UX_REALITY_PACK` et `EVALUATION_CASE` rendent exécutables le cadrage, la recherche, la divergence, la réalité UI/UX et l’apprentissage.

## Pour les agents et les opérateurs

| Lecteur | Entrée | Ce qu’il y trouve |
|---|---|---|
| Agent | [`SKILL.md`](skills/design-governance-practice/SKILL.md) | Noyau de fabrication et liste de chargement unique (`DIRECTION/CHARGE`). |
| Opérateur ou designer qui pilote un run | [Guide opérateur](V1/official/QUICKSTART.md) | Parcours commun, classement, chargement, handoff et exemple complet. |
| Reviewer ou lead | [`READING_MAP.md`](V1/official/READING_MAP.md), puis `ACTION.md` | Preuve dans le scope, limites et décision de clôture. |
| Mainteneur du package | Ce README, `CHANGELOG.md` et les validateurs | Contrat cohérent, testable et reproductible. |

Le mode d’un run est choisi par l’agent avec `DIRECTION/START`, seule classification ; il n’est jamais demandé à la personne qui fait la demande. Le parcours complet d’un run est : classer, diriger, construire, observer, corriger, fermer ; chaque mode n’en garde que les étapes de sa route.

Le README oriente la navigation. Il ne crée aucune règle concurrente. Les sources normatives font foi dans leur périmètre.

<!-- constitution:début -->
## Constitution minimale

Les cinq absolus transversaux de `DIRECTION` forment le noyau de protection de V1 : une surface identitaire doit avoir une direction perceptible ; une direction identitaire n’est acceptée qu’avec une ancre, observée ou fournie pour un produit réel (l’exploration peut commencer sans ancre, avec sa limite déclarée) ; aucune livraison ne contourne les preuves applicables ; le mode, la preuve et le budget sont déclarés avant l’exécution ; le réel et le beau sont cadrés ensemble.

Ces absolus ne remplacent pas les procédures propriétaires d’`ACTION`, de `SAVOIR` ou de `BIBLIOTHEQUE`. Ils rappellent la priorité de gouvernance et renvoient à [DIRECTION.md](V1/official/DIRECTION.md#les-cinq-règles-absolues), qui reste la source normative. Le piège de conformité est explicite : une conformité de surface ne vaut ni direction perceptible, ni preuve d’usage, ni qualité réelle.
<!-- constitution:fin -->

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

> **La boucle d’édition** (`DIRECTION/DOUBLE-LOOP`, reprise dans le noyau de la skill) : observer, nommer le défaut dominant, modifier l’artefact, comparer, décider.

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

Ces contrôles vérifient la forme du package, de ses projections et de ses distributions, ainsi que la liste close des conditions de façade ; une divergence hors de cette liste n’est pas détectée. Ils ne remplacent ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption. Une projection `RUN_CARD` valide reste une trace structurée ; elle ne transforme pas une cible de conformité, une capture ou une validation CLI en preuve de résultat.

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close ; elle n’atteste ni la réalité des observations, ni la justesse des jugements, ni la qualité perceptuelle. La liste exacte vit en un seul lieu : la frontière de validation d’`ACTION/RUN_CARD`.

## Limites et discipline d’usage

Une capture prouve un rendu dans son scope ; elle ne prouve pas à elle seule une tâche utilisateur, un lecteur d’écran, une sécurité, une performance ou une intégration réelle. Une trace complète sans conséquence est du slop procédural : si une étape, une variante, une référence ou un tag ne change aucune décision, observation, preuve, limite ou prochaine action, retirez-le ou justifiez `N/A-JUSTIFIED`.

La qualité créative reste située. Une proposition peut être visuellement convaincante sans avoir prouvé l’usage, l’accessibilité ou la robustesse ; elle peut aussi être conforme et robuste tout en restant générique ou insuffisamment résolue. V1 demande de rendre cet écart visible et de corriger le défaut dominant plutôt que de le compenser par une autre preuve.

V1 rend certaines affirmations plus difficiles à simuler ; elle ne remplace pas le jugement créatif, les tests utilisateurs, l’inspection technique ou la responsabilité du projet. Toute conclusion doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
