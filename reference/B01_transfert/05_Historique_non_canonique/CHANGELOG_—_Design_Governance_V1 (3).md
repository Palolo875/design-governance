# CHANGELOG — Design Governance V1

## État actuel

**Version active :** `V1.0.1`  
**Statut :** actif et canonique.  
**Owner d’acceptation :** propriétaire du corpus.

Le package actif contient exactement sept fichiers. `README.md` identifie le package ; `QUICKSTART.md` oriente la lecture ; `DIRECTION.md` porte le mode, la cible et les absolus ; `ACTION.md` porte le run, la preuve et la clôture ; `SAVOIR.md` porte le jugement et l’intégrité ; `BIBLIOTHEQUE.md` porte les structures et contrats ; ce fichier enregistre l’état et les modifications appliquées.

Les éléments de support et de provenance sont maintenus hors du package actif. Ils ne constituent pas des règles ni des claims de performance de cette version.

## Politique de changement

Toute évolution identifie sa **source canonique unique**, puis enregistre dans ce changelog : le problème, la décision et le remplacement éventuel, l’owner, la compatibilité, la preuve et sa limite, la condition de revue, ainsi que le rollback. Une entrée de release reste courte : elle ne reproduit pas un benchmark, un audit ou une provenance, mais elle doit permettre à un mainteneur de contester, reprendre ou annuler le changement.

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
