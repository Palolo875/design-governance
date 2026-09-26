# CHANGELOG — Design Governance V1

## État actuel

**Version active :** `V1.0.4`  
**Statut :** actif et canonique pour usage réel ; revue ciblée maintenue sur les cas externes et les briefs vagues.  
**Owner d’acceptation :** propriétaire du corpus.

Le package actif contient exactement sept fichiers. `README.md` identifie le package ; `QUICKSTART.md` oriente la lecture ; `DIRECTION.md` porte le mode, la cible et les absolus ; `ACTION.md` porte le run, la preuve et la clôture ; `SAVOIR.md` porte le jugement et l’intégrité ; `BIBLIOTHEQUE.md` porte les structures et contrats ; ce fichier enregistre l’état et les modifications appliquées.

Les éléments de support et de provenance sont maintenus hors du package actif. Ils ne constituent pas des règles ni des claims de performance de cette version.

## Politique de changement

Toute évolution identifie sa **source canonique unique**, puis enregistre dans ce changelog : le problème, la décision et le remplacement éventuel, l’owner, la compatibilité, la preuve et sa limite, la condition de revue, ainsi que le rollback. Une entrée de release reste courte : elle ne reproduit pas un benchmark, un audit ou une provenance, mais elle doit permettre à un mainteneur de contester, reprendre ou annuler le changement.

## V1.0.4 — activation externe des garde-fous situés

**Date :** 2026-08-23.  
**Problème.** Des essais externes rapportés par le propriétaire du corpus ont montré qu’un agent pouvait avoir V1 et les fichiers accessibles dans la conversation, tout en livrant une famille visuelle récurrente, des claims simulés comme réels, des démonstrations ambiguës ou des CTA sans action. Les principes existaient dans les sources et les pilotes, mais leur déclenchement était trop distribué pour une exécution one-shot externe.

**Décision et remplacement.** `DIRECTION/EXTERNAL-START` devient une vue officielle de démarrage portable. Elle promeut le noyau déjà conçu dans les pilotes : priorité vérité → premier objet → direction située → finition utile ; `RUN-PRIORITY` compact ; `DIRECTION-FIRST-OBJECT` référant les contrats existants ; grounding contestable ; `REUSE-CHALLENGE` conditionnel ; CTA réel, local ou limité. `QUICKSTART.md` et `README.md` rendent la vue trouvable. Cette promotion ne fait pas entrer `FEEDBACK-REPAIR`, les boucles de comparaison, les profils, les mesures de nouveauté ou les préférences mémorisées dans le noyau actif. Lorsque la vue est activée, `ACTION` conserve après le premier artefact les sorties minimales `DECISION-CHANGE`, `OMISSION-AVOIDED` ou `NOT-OBSERVED`, et `REMAINING-LIMIT`, sans créer de gate ou de statut supplémentaire.

**Owner et compatibilité.** Propriétaire du corpus V1. `DIRECTION.md` et le contrat de trace post-build d’`ACTION.md` sont les seules sources canoniques dont le contenu normatif est modifié ; `README.md` et `QUICKSTART.md` restent des guides non canoniques. Les en-têtes des sources actives affichent désormais la version de package pour éviter une confusion de distribution, sans modifier leurs responsabilités ni leurs règles locales. Les modes, les absolus, les gates, les statuts, `RUN_CARD`, `CAPABILITY-PROFILE`, B1b, les axes V/U/A/T et les responsabilités de `ACTION`, `SAVOIR` et `BIBLIOTHEQUE` restent inchangés. La vue ne crée ni second formulaire, ni score, ni gate, ni profil esthétique.

**Preuve, limite et revue.** La décision s’appuie sur les sorties externes fournies et inspectées — Lumen, Surge, Vespera, Pli et Trace — ainsi que sur les essais réels rapportés par le propriétaire ayant chargé V1 comme skill. Elle démontre un défaut de découvrabilité et d’activation, non que tout modèle a lu ou ignoré les fichiers, ni une efficacité causale universelle du nouveau démarrage. Revoir seulement si un usage externe réel signale un défaut précis que cette vue ne couvre pas ou si elle dégrade matériellement la vitesse, la direction ou la vérité.

**Rollback.** Retirer `DIRECTION/EXTERNAL-START`, la trace post-build associée et les lignes correspondantes de `README.md`/`QUICKSTART.md`, puis restaurer l’état actif antérieur. Aucune migration de trace n’est requise.

## V1.0.3 — contrôle officiel du premier objet

**Date :** 2026-08-22.  
**Problème.** La promotion de `DIRECTION-ATELIER` rendait officielle la source du goût et de la direction, mais ne rendait pas assez explicite le contrôle de qualité intrinsèque du premier rendu. Le risque restant était un premier objet cohérent avec le contrat, mais trop générique, décoratif, tardif dans sa preuve ou insuffisamment fini.

**Décision et remplacement.** `DIRECTION/DIRECTION-ATELIER` ajoute un contrôle de premier objet avant présentation : promesse et geste, preuve précoce, signature située, finition qui sert et vérité de scène. Le contrôle autorise une réparation interne substantielle lorsqu’elle change réellement le rendu ; il remplace la boucle de polish implicite par une limite ou une escalade lorsque la réparation utile est impossible.

**Owner et compatibilité.** Propriétaire du corpus V1. Les cinq sources canoniques, les modes, `RUN_CARD`, `CAPABILITY-PROFILE`, gates, B1b, verdicts et statuts restent inchangés. Le contrôle vit dans le module officiel `DIRECTION-ATELIER` ; il ne crée aucun score, statut concurrent, quota d’itérations ni workflow utilisateur.

**Preuve, limite et revue.** La promotion retient le seuil du pilote de qualité de sortie et les trois runs construits, capturés et testés localement. Elle réduit le risque de premier rendu techniquement complet mais creux ; elle ne démontre pas le goût universel, une préférence humaine, une qualité « premium », une tâche utilisateur réussie ou une robustesse multi-agent. Revoir après une comparaison de briefs identiques avec/sans contrôle, captures anonymisées et regard humain concerné.

**Rollback.** Retirer la sous-section « Contrôle du premier objet » et les lignes de guide associées ; `DIRECTION-ATELIER` V1.0.2 reste utilisable sans migration des traces.

## V1.0.2 — module officiel de direction située

**Date :** 2026-08-22.  
**Problème.** Le studio de direction artistique restait un pilote de provenance malgré une revue comparative et trois runs contrastés. Le conserver indéfiniment en expérimentation aurait empêché son usage quotidien ; le promouvoir comme gate ou preuve de qualité universelle aurait dépassé les preuves obtenues.

**Décision et remplacement.** Le noyau de craft précédemment documenté en pilote devient `DIRECTION/DIRECTION-ATELIER`, module officiel et activable uniquement en mode `DIRECTION`. Cette promotion ne remplace ni la provenance du pilote, ni ses comparaisons ni leurs limites ; elle rend seulement sa route de craft utilisable pour les surfaces identitaires, publiques ou culturellement sensibles. Son noyau relie moment humain, tension, geste produit, position/exclusion, contre-choix situé lorsque nécessaire, vérité locale et critique par verbes aux preuves déjà propriétaires d’ACTION. Les pilotes complets, A/B, baselines et revues humaines restent hors du run ordinaire.

**Owner et compatibilité.** Propriétaire du corpus V1. Les cinq sources canoniques, les modes, `RUN_CARD`, `CAPABILITY-PROFILE`, gates, B1b, verdicts et statuts restent inchangés. `README.md` et `QUICKSTART.md` rendent la route trouvable ; aucune migration de trace n’est requise.

**Preuve, limite et revue.** La promotion s’appuie sur une revue antérieure de trois paires baseline/pilote, puis trois runs opérationnels distincts — Reprise, Raccord et Sillage — avec captures et premier geste local confirmé par l’utilisateur. Elle démontre une faisabilité de craft et de premier objet, non une préférence humaine universelle, un gain causal contre baseline, une absence de coût, une robustesse multi-agent ou une validation de public cible. Revoir le module après une comparaison opérationnelle avec baseline chronométré, revue humaine anonyme et au moins un profil de capacité différent.

**Rollback.** Retirer `DIRECTION/DIRECTION-ATELIER` et les lignes d’orientation de README/QUICKSTART ; restaurer le statut de pilote de provenance. Les sources ACTION, SAVOIR et BIBLIOTHEQUE restent valides sans migration.

### Maintenance d’audit V1.0.3 — 2026-08-22

**Problème.** Les labels locaux `OBSERVED`/`ILLUSTRATIVE`/`MECHANISM` pouvaient être confondus avec `ANCHOR-OBSERVED` ou des statuts ACTION ; l’expression « statut de vérité » et la formulation de remplacement du pilote pouvaient surinterpréter la promotion.

**Décision.** Les marques deviennent `TRUTH/OBSERVED`, `TRUTH/ILLUSTRATIVE` et `TRUTH/MECHANISM`, explicitement non canoniques pour ACTION et les ancres. `DIRECTION` parle de marquage local, et l’entrée V1.0.2 borne la promotion au noyau de craft sans effacer la provenance, les comparaisons ou leurs limites.

**Owner et compatibilité.** Propriétaire du corpus V1 ; aucun mode, gate, statut, ancre, `RUN_CARD` ou route ACTION n’est modifié. Les anciens labels restent lisibles seulement dans les traces de provenance antérieures.

**Preuve, limite et revue.** Contrôle textuel, recherche de collisions, scénarios agent/personne/mainteneur et rollback documentaire ; aucune attestation humaine de compréhension du nouveau préfixe n’est créée. Revoir après le premier run V1 utilisant explicitement `TRUTH/…`.

**Rollback.** Restaurer les formulations précédentes de DIRECTION et de l’entrée V1.0.2 ; les sources ACTION, SAVOIR et BIBLIOTHEQUE restent indépendantes.

## V1.0.1 — exécution dérivée et frontière de service

**Date :** 2026-08-21.  
**Portée :** orientation de lecture et exécution de run ; aucun changement de mode, de gate, d’axe `V/U/A/T` ou de propriétaire de preuve.

Cette version ajoute `QUICKSTART.md` comme orientation non canonique. Elle ajoute dans `ACTION.md` le `CAPABILITY-PROFILE` et l’`EXECUTION-SNAPSHOT` comme vues dérivées et éphémères de champs déjà canoniques. Elle clarifie dans `DIRECTION.md` qu’une proposition exploratoire peut précéder l’ouverture d’un run, à condition de rester explicitement hypothétique et de ne pas être présentée comme un artefact construit, une preuve obtenue ou une action réalisée.

**Compatibilité.** Les cinq racines, les modes, les statuts, les gates, B1b et les routes existantes restent inchangés. Aucun alias ni migration n’est requis.

**Rollback.** Retirer les blocs ajoutés dans `DIRECTION.md`, `ACTION.md` et `QUICKSTART.md` ; les routes et statuts antérieurs restent valides.

### Maintenance d’audit — 2026-08-21

**Problème.** L’entrée pouvait confondre fichiers actifs et sources canoniques, orienter `STANDARD` vers une route trop large, raccourcir excessivement la trace minimale et laisser la politique de changement trop faible.  
**Décision.** `README.md` distingue guides et sources canoniques ; `QUICKSTART.md` pointe vers `ACTION/RUN-STANDARD` et sépare ligne de run minimale de `RUN_CARD` persistante ; ce changelog restaure les éléments de décision requis.  
**Owner et compatibilité.** Propriétaire du corpus V1 ; aucun mode, gate, statut ou route canonique existante n’est modifié.  
**Preuve, limite et revue.** Le contrôle porte sur les textes, identifiants et liens actifs ; il ne démontre pas encore la compréhension d’un utilisateur ou le comportement d’un runtime. Revoir après trois changements de système.  
**Rollback.** Retirer ces clarifications des trois fichiers concernés.

### Remédiation des frontières et claims — 2026-08-21

**Problème.** `V1` désignait à la fois la release et une voie d’ancrage ; proposition pré-run et issue `EXPLORATORY` se recouvraient ; l’alternative, la capacité et B1b solo pouvaient être surinterprétées.  
**Décision.** Les voies d’ancrage deviennent `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` et `ANCHOR-PROVIDED` ; la proposition pré-run devient « proposition de cadrage » ; les traces DIRECTION ouvertes, les bases de capacité et l’auto-comparaison B1b sont explicitement bornées.  
**Owner et compatibilité.** Propriétaire du corpus V1 ; les anciennes voies `V1/V2/V3` restent lisibles en archive uniquement et les modes, gates, verdicts et routes de run ne changent pas.  
**Preuve, limite et revue.** Contrôle des termes et scénarios E1–E5 ; aucune attestation runtime ou revue humaine n’est créée par le texte. Revoir après trois runs DIRECTION et trois reprises.  
**Rollback.** Restaurer les anciens labels et formulations dans les sources propriétaires ; les traces antérieures restent interprétables.

### Praticité quotidienne — 2026-08-21

**Problème.** Le chargement complet de V1 peut ralentir les tâches ordinaires, exposer le jargon d’atelier à la personne et omettre la base de capacité d’une snapshot.  
**Décision.** QUICKSTART distingue réponse/diff local, proposition de cadrage et conséquence externe sans créer de mode ; `CAPABILITY-BASIS` devient un champ additif de la snapshot.  
**Owner et compatibilité.** Propriétaire du corpus V1 ; modes, gates, statuts, routes et RUN_CARD existants restent compatibles.  
**Preuve, limite et revue.** Simulation de six parcours et mesure de taille documentaire ; aucune latence runtime ou compréhension utilisateur n’est prouvée. Revoir après six runs instrumentés.  
**Rollback.** Retirer la section opérationnelle de QUICKSTART et le champ additif de snapshot.

## V1.0.0 — noyau initial

**Date :** 2026-08-20.  
**Portée :** création des cinq sources canoniques : `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md` et `CHANGELOG.md`.

V1.0.0 établit la séparation des responsabilités : direction, exécution et preuve, jugement, structures, puis état du package. Toute évolution ultérieure doit modifier une source canonique unique, déclarer sa compatibilité et son rollback, puis être enregistrée ici.
