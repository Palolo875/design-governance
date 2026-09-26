# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 1 : responsabilité, entrée et READ

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 1–87**. Introduction et responsabilité 1–20, entrée prioritaire 22–33, orientation et handoff 35–41, charges de lecture 43–52, contrat minimal et statuts 54–66, `BIBLIOTHEQUE/READ` 70–86. `BIBLIOTHEQUE/TENSION` commence **ligne 88** et reçoit le bloc suivant avec SIGNATURE et les autres sous-sections de READ.
- Méthode : protocole externe v2.0 §12 relu, passages A à D ; reprise du plan maître et des checkpoints SAVOIR, DIRECTION et ACTION. Interfaces exactes consultées : DIRECTION/START 119–144 et lecture instrumentée 806–817 ; ACTION 69–77, 205–236, 272–278, 875–885 ; `BIBLIOTHEQUE/CONTRACTS` 256–258 et `EVOLUTION` 733–762 seulement pour la temporalité de PILOT et promotion ; `CHANGELOG` 35–42 pour les statuts. Les conclusions sur ces sections aval restent réservées à leur lecture propriétaire.
- Baseline B01 inchangée : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; BIBLIOTHEQUE propriétaire `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Lecture documentaire sectionnelle ; aucun patch de la cible, verdict produit ni conclusion globale de l'audit. Les constats des autres propriétaires restent provisoires.

## Passage A — architecture visible, routes et propriété

BIBLIOTHEQUE possède le **choix, l'adaptation et l'évolution de structures** d'interface (7–11) : support, grille, scène, objet, micro-interface, modificateur, primitive et couche. La capacité positive formulée en 9 est une cible : rendre une direction ou décision de produit **habitable**, compatible et maintenable dans un premier objet ; elle ne prouve pas à elle seule un gain réel. Le démarrage DIRECTION classe mode, risque et portée ; SAVOIR juge méthode/craft ; ACTION exécute, vérifie et clôt ; CHANGELOG gouverne l'adoption des routes. La table 15–20 et les disclaimers 33/37/39 évitent que l'entrée rapide de BIBLIOTHEQUE soit prise pour un second classificateur ou gate.

L'entrée prioritaire 22–33 sert de **résumé de protection** avant le catalogue, avec six règles numérotées. `BIBLIOTHEQUE/READ` 70–86 décrit les responsabilités des cinq niveaux de la chaîne, explicitement **sans ordre de chargement rigide**. Les sous-routes `TENSION` à 88 et `SIGNATURE` à 106 seront jugées ensuite, sans déduire leur statut exact de la seule entrée qui les mentionne.

**Accès contrôlé :** `read_route.py BIBLIOTHEQUE/READ` répond correctement mais extrait 95 lignes d'affichage, dont la source 70–160 et les sous-sections `TENSION`, `SIGNATURE`, thèse, préfixes et types de preuve. Les appels dédiés `BIBLIOTHEQUE/TENSION` et `BIBLIOTHEQUE/SIGNATURE` renvoient « locator inconnu », tandis que `validate_reading_map.py` réussit. L'extraction large peut imposer plus de lecture que la question locale ; la non-résolution des deux locators relève déjà de F-DIR-028/F-ACT-001. L'effet pratique de la largeur de READ reste à éprouver avec les conditions des sous-sections dans le bloc 2, **sans ouvrir ici un nouvel ID**.

## Passage B — contrat sémantique, phrase par phrase

### Responsabilité, priorité et zéro route (1–33)

Les phrases 7–11 demandent de partir d'une **décision à modifier**, puis de juger la relation perceptuelle/produit, la preuve attendue, la compatibilité et le coût de maintenance. Conserver la structure existante ou n'ouvrir aucune route structurelle est permis. Cette voie ne suspend pas un contrôle ACTION applicable si un texte, un état ou une action change. L'héritage peut être un **choix confirmé** après observation : on n'écrit `N/A-JUSTIFIED` que pour la route ou le contrôle réellement non applicable ; on n'efface pas une décision observée simplement parce qu'aucune nouvelle structure n'est ajoutée (ACTION 212–218/234–236, F-DIR-011/019, F-ACT-013/014). Avant observation, décrire l'intention et la preuve attendue plutôt qu'un succès.

Les protections 26–31 demandent une structure habitable au premier objet lorsque la sélection est ouverte, mais distinguent quatre types de contribution : ce que l'on perçoit, l'interprétation experte, la mesure technique et la tâche accomplie par une personne. La chaîne de routes ne peut valoir preuve d'usage. Partir d'un seul niveau structurel utile puis ajouter un niveau activé évite la sélection décorative ; en revanche, « minimal » ne peut réduire une protection critique de DIRECTION/START ni un contrat de structure partagé réellement applicable.

La chaîne de promotion 31 et DIRECTION 817 concerne une **route structurelle partagée** ou candidate à la durée. Elle relie classification, run système si la décision partagée est l'objet direct, contrat d'évolution et gouvernance, sans offrir une promotion par simple parcours des titres. Si une direction produit seulement plus tard une migration structurelle, garder la décision DIRECTION puis ouvrir la décision SYSTÈME dépendante selon START 138 (F-SAV-007). Si le changement partagé est non structurel, l'appel systématique à BIBLIOTHEQUE reste une question de F-DIR-046, non une autorité nouvelle tirée de ce résumé. Un composant strictement local n'est pas automatiquement `PILOT` ou `ADOPTED`.

### Orientation et handoff (35–41)

La ligne 37 appelle `READ` une fois BIBLIOTHEQUE activée et `SELECT` **si** une décision structurelle est ouverte. `SAVOIR/STYLE` n'est consulté auparavant que lorsque l'expression peut changer cette structure. Une micro-interface peut être le point de départ (78), donc la chaîne support → grille → scène → objet → primitive est une **carte des rôles**, et non cinq chargements ou cinq étapes de build imposés. La condition d'arrêt 41 favorise un jugement ciblé et sa transmission.

La ligne 39 nomme à la fois une sortie structurelle locale (`DECISION`, niveau ou héritage, signature si applicable, contre-indication, premier objet attendu, preuve, limite, owner, condition de sortie) et des champs du handoff canonique ACTION (`MODE`, `RISK`, `SCOPE`, `ARTIFACT`, `OBSERVATION/METHOD`, `DECISION-CHANGE`, `NEXT-ACTION`, `NEXT-PROOF`, etc.). **Deux temps doivent rester séparés :** avant build, intention, artefact attendu, méthode et preuve attendue ; après observation, artefact réel, résultat et éventuel `DECISION-CHANGE`. ACTION 209–218 interdit de déclarer le changement avant observation ; la section propriétaire `BIBLIOTHEQUE/CONTRACTS` 258 le dit expressément aussi. Exiger toutes les valeurs de 39 à une présélection produirait du remplissage fictif. La coexistence de la liste longue 39 et du minimum « Local » 58 ravive F-DIR-006/010 et F-ACT-002/030 sur mapping et temporalité ; aucune obligation nouvelle de formulaire parallèle n'est établie ici.

### Catégories de lecture et promesse de gain (43–52)

`STARTUP-NOMINAL` décrit une recommandation avant sélection ; `CONDITIONAL-READ` un motif lié au brief ; `AUDIT-READ` un motif de contrôle du corpus ; `ACTUAL-READ` la lecture effectuée dans le run. Une route recommandée puis lue est à la fois nominale et effective ; une route conditionnelle lue a également deux attributs. La formulation « nature de chaque lecture effectivement lue » (45) accentue le mélange d'un **fait** et de **motifs**. F-DIR-044 possède déjà cette taxonomie, même avec BIBLIOTHEQUE comme occurrence explicitement anticipée dans son rapport ; créer F-BIB par reprise serait redondant. Ne pas compter AUDIT-READ parmi les lectures nécessaires à un run produit. La phrase 52 empêche un claim de gain en temps, charge ou qualité sans méthode, portée, observation et limite ; elle ne démontre aucune baisse par sa présence.

### Minimum local, PILOT, partagé, durable (54–66)

Le tableau est une **échelle de contribution et de statut de route**, pas une nouvelle échelle de verdict ACTION. Local = décision, responsabilité, preuve attendue, limite, sans contrat complet de promotion ; partagé = consumers, owner, compatibilité, états, mobile/accessibilité, migration/rollback **selon le risque** ; durable = usages contrastés, baseline, gain observé ou mesuré, maintenance et revue. Une seule jolie capture ne prouve pas la réutilisabilité ou l'adoption. Les statuts `PILOT`, `ADOPTED`, `DEPRECATED`, `ABANDONED` appartiennent à CHANGELOG, distincts des états de run (63, CHANGELOG 35–40).

La ligne 59 inscrit `DECISION-CHANGE` au minimum d'une route `PILOT`. Elle peut être lue trop tôt si la route est seulement **candidate** ; `CONTRACTS` 258 rétablit la séquence : contrat local de départ, candidature `PILOT` possible, puis `DECISION-CHANGE` ou issue ACTION appropriée **après observation**. `CHANGELOG` appelle PILOT une route locale ou candidate **testée dans un périmètre déclaré** (37) ; la simple déclaration d'intention n'atteint donc pas ce statut démontré. Toute lacune de preuve demeure visible dans ACTION et la gouvernance : ne pas inventer un résultat pour cocher la cellule 59. Owner de la décision, destinataire de la prochaine action et mainteneur d'une route partagée sont trois rôles possibles distincts (63) ; aucune identité commune n'est présumée.

### Responsabilités de READ et expression (70–86)

Support = champ où vit la surface ; grille = regard et hiérarchie ; scène = rapport promesse/contenu/média/action ; objet = preuve/état/action local tangible ; primitive = geste et sémantique accessible. Les sous-familles micro, modificateur et couche complètent cette carte selon la décision, sans quotas. L'objet « preuve » ici est une **pièce visible du produit** ; l'observation exécutée d'efficacité appartient à ACTION (F-DIR-024). Un composant authored peut composer silhouette, contenu, hiérarchie, matière et comportement, tout en conservant les comportements accessibles des primitives critiques (80).

La lecture expressive 82–86 est productive lorsque présence, voix ou expérience du regard **font réellement partie du brief** : calme/tension ou intimité/monumentalité sont des oppositions à traduire en masse, rythme, matière, contenu et comportement, pas des profils de style à sélectionner d'office. Une relation perceptuelle justifiée peut rendre une structure préférable sans prétendre que la seule beauté démontre la tâche ; la contre-indication et la condition de sortie doivent rester observables. C'est une protection contre un choix systématique de dashboards/cards et contre la réduction de toute valeur à la stricte réussite d'une tâche, sous réserve des protections d'accessibilité et d'usage.

## Passage C — parcours de lecteurs sous contrainte de temps

| Lecteur / situation | Décision et trace attendues | Risque de lecture littérale |
|---|---|---|
| Agent, correction d'un libellé dans un composant stable | DIRECTION classe le delta ; aucune nouvelle structure ni catalogue ; contrôle ACTION du libellé/état touché | « Commencez par READ » pris comme obligation universelle d'ouvrir le catalogue |
| Designer, nouvelle scène expressive | Nommer relation, premier objet et structure utile ; STYLE seulement si expression change la structure ; SELECT ensuite si choix ouvert | Ajouter support, grille, scène, objet et primitive par quota, ou déduire l'usage d'une seule composition |
| Intégrateur, héritage de grille après première capture | Inspecter la grille, confirmer son adéquation et noter la conséquence observée ; N/A seulement pour la route non applicable | Classer toute confirmation comme « aucune décision » puis N/A |
| Mainteneur, route locale candidate PILOT | Garder contrat réduit, scope et test ; séparer proposition, preuve post-observation et décision de statut | Remplir `DECISION-CHANGE` à la sélection ou appeler PILOT une hypothèse non testée |
| Équipe, token partagé né d'une identité | DIRECTION d'abord, puis run SYSTÈME dépendant si migrable, BIBLIOTHEQUE/EVOLUTION si la structure est concernée ; CHANGELOG décide cycle de vie | Remplacer la décision initiale ou promouvoir implicitement un composant local |
| Responsable de pilote, mesure de charge de lecture | Distinguer pourquoi on a ouvert un fichier et s'il a été lu, exclure AUDIT-READ d'un run ; mesurer temps/qualité sur périmètre | Additionner catégories recouvrantes et annoncer une économie non mesurée |

Ce sont des simulations documentaires, non des tests utilisateurs, ni des gains observés. Le statut réel d'une route, la preuve du rendu et l'effet du lecteur de locators seront éprouvés dans les sections suivantes et dans les phases système.

## Passage D — résistance et déduplication

**Aucun nouvel ID autonome dans ce bloc.** Les tensions repérées ont un propriétaire ou une fiche antérieure, ou sont nuancées par une section propriétaire de BIBLIOTHEQUE déjà consultée en interface. Cette retenue n'équivaut pas à un verdict positif sur tout le fichier.

| Observation | Relation et épreuve restante |
|---|---|
| READ extrait jusqu'à 160, TENSION/SIGNATURE sans locator dédié, carte validée | F-DIR-028/F-ACT-001 pour l'accès ; lors du bloc 2, tester si le préchargement de sous-routes conditionnelles a un coût ou effet distinct et vérifiable |
| Zéro route conseillé alors que l'héritage est réellement confirmé après observation | F-DIR-011/019, F-ACT-013/014 ; distinguer non-applicabilité du choix confirmé et absence de preuve |
| Handoff 39 paraît exiger artefact/observation/décision effective à la présélection | F-DIR-003/006/010, F-ACT-002/030 ; `CONTRACTS` 258 et ACTION 209–218 imposent la séparation temporelle |
| PILOT 59 exige `DECISION-CHANGE` dans le minimum | `CONTRACTS` 258, CHANGELOG 37 réservent l'effet à l'après observation ; tester une candidate non testée, un pilote testé et un abandon |
| Quatre charges de lecture mélangent recommandation, motif et fait | F-DIR-044 contient déjà la même occurrence BIB ; contrôler instrumentation sans double comptage |
| Chaîne promotion lue comme obligation BIB pour changement partagé non structurel | F-DIR-046 ; route structurelle seulement, propriétaire CHANGELOG pour gouvernance |
| Chaîne support/grille/scène/objet/primitive utilisée comme ordre de chargement ou preuve d'usage | F-DIR-024 et F-ACT-001/029 ; READ 72–80 dit expressément « responsabilités » |

**Acquis à préserver :** capacité de composer des premiers objets spécifiques et habitables ; zéro sélection décorative ; niveau structurel chargé si utile ; preuve perceptuelle distincte de méthode/usage ; expression située sans gabarit ; compatibilité et maintenance proportionnelles ; cycle de vie indépendant du verdict de run ; sortie vers ACTION et arrêt de lecture lorsque décision, limite et owner sont clairs. Ne pas remplacer ces propriétés par un formulaire universel.

## Couverture, limites et reprise

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | Propriétés, résumé, READ, sous-routes, extraction CLI et interface d'ownership |
| B — sémantique | FULL | Lignes 1–86, non-sélection, handoff, quatre charges, Local/PILOT/partagé/durable, cinq niveaux READ |
| C — usage | TARGETED | Six lecteurs ; hypothèses explicites, aucun run terrain |
| D — résistance | TARGETED | Aucun ID nouveau, accès et temporalité rattachés, effets du bloc 2 réservés |
| Machine | TARGETED | READ résolu mais extraction 70–160 ; TENSION/SIGNATURE refusés ; carte dérivée validée |
| Externe | N/A-JUSTIFIED | Aucun claim externe décisif dans ce contrat documentaire ; performance et gains non mesurés |

**Prochaine unité :** `BIBLIOTHEQUE.md` **lignes 88–160**, TENSION, SIGNATURE, thèse du premier objet, préfixes canoniques et types de preuve ; `BIBLIOTHEQUE/SELECT` commence à 161. Reprendre le protocole §12, ce rapport et la baseline, relire les obligations dans leur ordre exact, puis décider si la largeur de READ révèle un défaut autonome ou seulement l'occurrence d'accès déjà consignée. Aucun patch et aucun verdict global.
