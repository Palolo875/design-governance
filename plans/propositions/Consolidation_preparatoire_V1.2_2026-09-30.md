# Design Governance V1.2 — Correctifs de pilotage et inventaire de reprise

**Date :** 30 septembre 2026. **Base :** `3966ad585061adf5e764cd1ceefd148460170d57` ; deux branches de travail alignées lors de la vérification. **Statut :** préparation locale, à intégrer ; aucun commit ni push effectué. Le package reste inchangé et aucune production d’évaluation n’est lancée.

Cette note accompagne le plan de reprise existant. Elle fournit un correctif documentaire et une vue préparatoire de l’inventaire demandé ; elle ne crée pas un second plan actif. Les corrections rapportées comme faites ne sont pas présentées comme des contrôles nouvellement exécutés. La revue relève de l’assistant et ne constitue pas une observation indépendante D3.

## 1. Correctif prêt à intégrer

Le patch en annexe traite cinq fichiers de pilotage. Les propositions archivées et les rapports historiques restent des pièces de provenance.

| Fichier | Correction préparée |
| --- | --- |
| plans/Plan_V1.2_Suite_Reprise.md | Contrôle fidèle de la double boucle ; Inventaire proportionné et inconnues explicites ; Réemploi borné des références R10 ; R9 réellement reporté ; Dette documentaire déjà traitée |
| plans/Plan_V1.2_Refonte.md | État courant et portée des mesures ; Autorité explicite du plan actif ; R8 conforme aux décisions actuelles ; Pas de changement de schéma réintroduit ; Protocole complet conditionnel ; Dépendances actuelles sans R9 ; Charge diagnostique sans coupe mécanique ; Risque de charge conforme à la consigne ; Arbitrages historiques identifiés ; État des arbitrages et questions ouvertes |
| CLAUDE.md | Statut réel de la proposition ; Historique distingué du courant ; Point d'entrée et objectif courant ; Cas évalués et productions neuves distingués ; Charge sans plafond de coupe |
| plans/carte_moyens_v0.md | Ressources externes distinctes des intrants du client ; Choix d'icônes contextuel ; Preuve de performance adaptée ; Traitement commun conditionnel |
| audit/reports/V12R_14_DECISIONS_ARBITRAGES.md | R10 cohérent dans le registre |

Le palier exploratoire compte **six cas comparés**. Quatre productions neuves ne sont possibles que si une référence B-DLA C1 et une référence B-DLA C4 sont réutilisables dans les conditions déclarées. Les productions C3 utilisent la candidate consolidée ; les C3 de P1 décrivent l’ancienne version après R4. Le nombre de cas, le nombre de productions neuves et le nombre de répétitions restent distincts.

Le contrôle de la double boucle renvoie à son propriétaire existant. Il inspecte les embranchements de correction, réouverture, reclassification, preuve supplémentaire et arrêt ; il n’ajoute pas une autre boucle. La capture n’est pas la seule forme d’observation admissible.

## 2. Inventaire de reprise

**Lecture des états :** « corrigé documenté » désigne un traitement décrit par un rapport avec ses contrôles, sans réexécution dans cette préparation ; « à traiter » désigne un travail restant dans le plan ; « effet non établi » renvoie à une question d’usage pour R10 ; « à instruire » signale une dépendance de preuve. Les conséquences P2 ci-dessous sont des propositions de classement fondées sur les constats et restent à confirmer pendant les lots.

Cette vue couvre les identifiants D-01 à D-23 et les mineurs transmis. Elle n’annonce ni une nouvelle lecture exhaustive du package ni l’extraction des journaux zip. R-16 à R-32 représentent **17 points individuels**, regroupés ici seulement pour afficher leur dépendance commune ; leur tri ne peut pas être fait collectivement.

| ID | Constat | État fondé sur les pièces | Lot | Conséquence pour P2 / suite | Pièce |
| --- | --- | --- | --- | --- | --- |
| D-01 | Vocabulaire MODAL/PARTI | Corrigé documenté | R3 | Non bloquant, sous réserve de maintien | V12R_03 |
| D-02 | Prise de brief fidèle à sa règle | Corrigé documenté | R3 | Non bloquant ; R6b conserve cette fidélité | V12R_03 |
| D-03 | Règle d'ancre dans skill et façades | À aligner | R7 | Bloquant avant P2 : règle d'acceptation | V12_11 ; V12R_14 |
| D-04 | Positions divergentes sur l'ancre dans SAVOIR | À aligner | R7 | Même correction que D-03, sans second protocole | V12_11 ; V12R_14 |
| D-05 | Listes de chargement divergentes | Corrigé documenté | R4 | Non bloquant ; contrôler les routes lors de la consolidation | V12R_04 ; V12R_07 |
| D-06 | BIBLIOTHEQUE requise mais hors accès | Traitement documenté | R4 et R5d | Accès conditionnel admis ; F22 ne doit pas être déclaré absent | V12R_04 ; V12R_11 |
| D-07 | Marqueurs et carte des moyens hors d'atteinte | Corrigé documenté | R3 et R4 | Renvois acquis ; qualité de la carte à traiter en R8b | V12R_03 ; V12R_04 |
| D-08 | Glossaire incomplet | Corrigé documenté | R3 et R6a | Préserver les termes ; R6b examine leur usage humain | V12R_03 ; V12R_12 |
| D-09 | Checkpoint avant build incompatible avec la première proposition | Corrigé documenté | R5b-1 | Exception action irréversible ou coûteuse conservée | V12R_06 |
| D-10 | Réponse visible en jargon interne | Traitement documenté dans HANDOFF | R4 ; raccord R6b | Vérifier les façades, sans réécrire le contrat de sortie | V12R_04 ; V12R_12 |
| D-11 | Entrée dispersée et deux README | À traiter | R6b | Bloquant pour le parcours novice avant P2 | V12_11 ; V12R_12 |
| D-12 | Questions recopiées et tu/vous mêlés | Corrigé documenté | R3 | Préserver la fidélité ; ne pas refaire une correction déjà livrée | V12R_03 |
| D-13 | Espace initial de QUICKSTART | Corrigé documenté | R3 | Coquille close ; aucune garde nouvelle | V12R_03 |
| D-14 | Formats de sortie concurrents | Traitement documenté ; raccord à vérifier | R4 ; R6b | Une sortie humaine dérivée de HANDOFF | V12_11 ; V12R_04 |
| D-15 | Instrumentation de maintenance dans la lecture locale | À traiter | Restes R5 | Bloquant si le parcours ordinaire impose cette charge ; vérifier le chargement réel | V12R_11 |
| D-16 | Deux axes présentés comme niveaux identiques | Corrigé documenté | R5c | Distinction moments/niveaux à préserver | V12R_10 |
| D-17 | Rôle et protections placés trop tard | Corrigé documenté | R5a | Aucun déplacement supplémentaire présumé nécessaire | V12R_08 |
| D-18 | Mesure partielle du chemin prescrit | Remplacement de l'outil documenté | R1 ; ajustements R4/R5b-1 | Périmètres déclarés ; fragilité F13 traitée séparément | V12R_01 ; V12R_04 ; V12R_06 |
| D-19 | Prise de brief perdant son contexte dans le noyau | Corrigé documenté | R5a | Préserver le sens du cadrage et de la trace | V12R_08 |
| D-20 | Destination réelle sans contenu : gabarit vide | Règle corrigée documentée | R5b-1 ; R11a | Contenu d'exemple marqué acquis ; effet réel à observer en R10 | V12R_06 ; V12R_13 |
| D-21 | Nouvelle convergence typographique | Geste livré ; effet non établi | R8a ; évaluation R10 | Le résultat ne peut pas être exigé avant usage ; vérifier le geste | V12R_09 |
| D-22 | Trame générique propre au brief | Test de trame livré ; effet non établi | R5b-1 ; évaluation R10 | Préserver l'alternative justifiée ; aucun rendu supplémentaire imposé | V12R_06 |
| D-23 | Surcoût d'un run | Trace légère livrée ; coût non remesuré | R5b-1 ; évaluation R10 | Non bloquant P2 comme résultat à mesurer ; budget d'épreuve fixé avant R10 | V12R_06 ; plan de reprise §5 |
| Q-04 | Portée du contrôle machine de la décision | Clarification prévue | R11 ciblé | À relire : texte cohérent avec le contrôle réellement effectué | Amendement §7 ; clôture §3 |
| Q-07 | Relation entre les scopes de l'artefact et de la direction | Clarification prévue | R11 ciblé | À instruire selon l'usage ; aucune égalité nouvelle présumée | Amendement §7 ; clôture §3 |
| Q-08 | Référence canonique des sorties et vues dérivées | Clarification prévue | R11 ciblé | Préserver une source et ses vues dérivées | Amendement §7 ; clôture §3 |
| Q-09 | Arrêt et comparaison B1b | Clarification prévue | R11 ciblé | Deux exceptions conservées ; comparaison pouvant confirmer l'original | Amendement §7 ; clôture §3 |
| Q-11 | Point conservé par l'arbitrage ciblé | Maintien décidé ; justification à préserver | R11 ciblé | Pas de correction automatique ; reclasser seulement sur preuve nouvelle | V12R_14 ; amendement §7 |
| Q-12 | Point conservé par l'arbitrage ciblé | Maintien décidé ; justification à préserver | R11 ciblé | Pas de correction automatique ; reclasser seulement sur preuve nouvelle | V12R_14 ; amendement §7 |
| Q-13 | Détail dépendant des traces | Ouvert, contenu détaillé non vérifié | R11 ciblé | Classification P2 à instruire après lecture des journaux | audit/logs/DG_AUDIT_001_Journaux_R02.zip ; …_Epreuves_13-02_traces.zip |
| R-16 à R-32 | 17 identifiants transmis, sans fusion de leurs conclusions | Ouverts individuellement ; détails non vérifiés | R11 ciblé | Chaque identifiant exige son propre constat, état et disposition après lecture ; aucun maintien collectif supposé | Même dépendance aux journaux ; clôture §3 |
| PIL-01 | Pilotage périmé et instructions contradictoires | Correctif préparé, non intégré | Synchronisation documentaire | À résoudre avant la reprise opératoire ; patch ci-dessous | Revue du 30-09 ; cinq fichiers de pilotage |
| PIL-02 | Double boucle réduite dans le contrôle P2 | Correctif préparé, non intégré | Synchronisation documentaire | Contrôler les embranchements du propriétaire existant | Plan de reprise §4 ; DIRECTION/DOUBLE-LOOP |
| PIL-03 | Réemploi d'anciens rendus insuffisamment conditionné | Correctif préparé, non intégré | Préparation R10 | À résoudre avant production ; C3 toujours issu de la candidate courante | Plan de reprise §4 ; V12R_05 |
| PIL-04 | Carte : style imposé et performance attestée par capture | Correctif préparé, non intégré | Synchronisation ; poursuite R8b | À résoudre avant usage de la carte consolidée | plans/carte_moyens_v0.md |
| R8b | Qualité opérationnelle des moyens et enseignements | Lot restant, pas un défaut nouveau présumé | R8b | Confronter aux propriétaires ; combler seulement les manques établis | Plan de reprise §4 ; amendement §4 |
| R8c | Précision des gestes utiles | Diagnostic restant, pas de quota de recettes | R8c | Déclencheur, correction possible et observation ; aucune retouche obligatoire | Plan de reprise §4 ; amendement §5 |
| R5 reste | Handoff copié, alternative située, PRINT_FIELD et promotion | Périmètre restant | Restes R5 | Renvois et responsabilité ; préserver le contenu propre et vérifier la baisse de charge | Plan de reprise §4 ; amendement §9 |

**Identifiants des mineurs regroupés :** R-16, R-17, R-18, R-19, R-20, R-21, R-22, R-23, R-24, R-25, R-26, R-27, R-28, R-29, R-30, R-31, R-32. Ces codes sont ceux de la clôture ; ils ne sont pas les numéros des lots V1.2 ni, sans rapprochement des pièces, des cas de harnais portant un libellé voisin.

**Autres reliquats déjà prévus :** R7 couvre les copies ANCHOR-GENERATED ; les restes R5 comprennent la lecture dédiée des raccords de trace de SAVOIR et la répartition de l’alternative située ; R6b inclut les README des distributions GitHub et Local ainsi que les locators et leurs consommateurs. La carte d’ACTION reste une vue dérivée alignée, gardée par CHG-09 ; son existence seule ne constitue pas un nouveau défaut à supprimer.

## 3. Réserves de clôture : articulation, sans double comptage

| Réserve de la clôture | Objet | Traitement prévu |
| --- | --- | --- |
| 1 et 4 | Efficacité et limites des preuves de forme | Questions pour l’usage et les observateurs ; ne pas annoncer leur résolution à P2. |
| 2 | CI hébergée non observée | R11 final sur la candidate distribuable ; aucune exécution observée dans cette préparation. P2 vérifie les sources, contrôles et distributions locales prévus. |
| 3 | Cas négatifs manquants | R11 ciblé vérifie d’abord la couverture existante puis ajoute les cas réellement manquants ; reliquat maintenu et justifié. |
| 5 | Limite de la promesse du validateur | Conception assumée, à communiquer ; un résultat machine ne devient pas une preuve d’effet. |
| 6 | Charge et coût | Charge documentaire suivie ; D-23 mesure le coût réel en R10. Ne pas confondre baisse des mots et économie observée. |
| 7 | Placeholders de champs libres | Maintien décidé ; aucun filtre global ni restauration d’INV-E11. |
| 8 | Mineurs transmis | Rapprochés des Q/R ci-dessus ; DAILY traité par R4/R11a. Ne pas les ajouter une seconde fois comme défauts indépendants. |
| 9 | V1.1.1 non publiée | État historique ; la livraison V1.2.0 suit R12 et le feu vert final. |

## 4. Sortie de cette préparation et suite opératoire

Le correctif traite des ambiguïtés de pilotage. Son intégration ne clôt ni R8b, ni R8c, ni R7, ni R6b, ni P2. L’inventaire est à reprendre dans la vue unique du chantier, en conservant les identifiants et les liens aux rapports ; aucune nouvelle copie obligatoire n’est à charger pendant un run de design.

Après intégration, reprendre R8b selon le plan actuel : inspecter la carte des moyens et les propriétaires concernés, préciser les conditions utiles, vérifier les ressources effectivement retenues et intégrer seulement les enseignements qui changent une décision ou une construction. R8c examine les gestes existants avant tout ajout. Q13 et chaque R-16–R-32 attendent leurs traces pour leur disposition. Les critères précis de poursuite, de coût et de jugement de R10 restent à fixer avant production ; aucun seuil arbitraire n’est introduit ici.

## 5. Vérification de la préparation

- Chacune des 25 substitutions trouve son texte source exactement une fois.
- Le patch s’applique sans erreur aux cinq fichiers récupérés à la base indiquée (`git apply --check`, puis application sur copies).
- Les cinq résultats appliqués correspondent octet pour octet aux versions préparées.
- Les contrôles ciblés confirment le retrait des formulations périmées visées, l’absence de dépendance à R9 et la couverture D-01 à D-23 de l’inventaire.
- Aucun fichier de `package/` ni de B01 n’est modifié ; aucun contrôle du package ni run GitHub Actions n’est réexécuté par cette préparation.

Cette vérification atteste l’application mécanique du correctif sur sa base. Elle ne démontre ni l’efficacité du système ni la réussite de P2. Si la branche a avancé, comparer avant d’appliquer ; ne pas forcer le patch et ne pas importer des résultats de contrôles d’une autre candidate.

## 6. Pièces de référence

- [plans/Plan_V1.2_Suite_Reprise.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/plans/Plan_V1.2_Suite_Reprise.md)
- [plans/Plan_V1.2_Refonte.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/plans/Plan_V1.2_Refonte.md)
- [audit/reports/V12_11_SYNTHESE_LECTURES.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12_11_SYNTHESE_LECTURES.md)
- [audit/reports/V12R_01_OUTILS_MESURE.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_01_OUTILS_MESURE.md)
- [audit/reports/V12R_03_R3_ALIGNEMENTS.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_03_R3_ALIGNEMENTS.md)
- [audit/reports/V12R_04_R4_NOYAU.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_04_R4_NOYAU.md)
- [audit/reports/V12R_05_P1_MINI_EPREUVE.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_05_P1_MINI_EPREUVE.md)
- [audit/reports/V12R_06_R5b1_TRACE_CHECKPOINT.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_06_R5b1_TRACE_CHECKPOINT.md)
- [audit/reports/V12R_07_R5b2_ACTION.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_07_R5b2_ACTION.md)
- [audit/reports/V12R_08_R5a_DIRECTION.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_08_R5a_DIRECTION.md)
- [audit/reports/V12R_09_R8a_CONVERGENCE_TYPO.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_09_R8a_CONVERGENCE_TYPO.md)
- [audit/reports/V12R_10_R5c_SAVOIR.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_10_R5c_SAVOIR.md)
- [audit/reports/V12R_11_R5d_BIBLIOTHEQUE.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_11_R5d_BIBLIOTHEQUE.md)
- [audit/reports/V12R_12_R6a_FACADES.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_12_R6a_FACADES.md)
- [audit/reports/V12R_13_R11a_CORRECTIFS.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_13_R11a_CORRECTIFS.md)
- [audit/reports/V12R_14_DECISIONS_ARBITRAGES.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/V12R_14_DECISIONS_ARBITRAGES.md)
- [audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md)
- [plans/propositions/Amendement_V1.2_2026-09-28.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/plans/propositions/Amendement_V1.2_2026-09-28.md)
- [package/V1/official/DIRECTION.md](https://github.com/Palolo875/design-governance/blob/3966ad585061adf5e764cd1ceefd148460170d57/package/V1/official/DIRECTION.md)

## 7. Empreintes du correctif

| Fichier | SHA-256 avant | SHA-256 préparé |
| --- | --- | --- |
| plans/Plan_V1.2_Suite_Reprise.md | 204638255c0c91bf07470b9c7741584834465cf16a92aa706c4c01e21cb002af | a72700c424ba1f6410744099e676f2767bdb03920433b4a039fd67c43d2ab1f1 |
| plans/Plan_V1.2_Refonte.md | 451f4ff6427c6be845820654d67d9a7e8ec73d60142eda4924e849e4a0184090 | e5624c311554a6bd69ed6ebb330c0ed16916a2d4d21d395f71cb00b9dc1e0b17 |
| CLAUDE.md | 590007e88b0feacfc2de9632cef0122303a1fbd9a439c1c2c12aa235d5faa8bb | 32d55ba8c5247596dc411f74eaec7c5f5f068e76ab202b52782a5b0027c73094 |
| plans/carte_moyens_v0.md | 03a1591bde37549bdd106a8e7e4788c3a8ad80e5de82225558b3270126f674d4 | b4df2e59e90397d93c8717399fbc4cf886672b0f2188b78a6d88514d042b8aa5 |
| audit/reports/V12R_14_DECISIONS_ARBITRAGES.md | fc7b16150e869044f229230cbc8aff7f11714baa5765de2347359edd8d360b80 | b04d057231c8750f5d9be72e177924d43df93f2bc5945a44917cd7c911220fb8 |

## Annexe — Patch documentaire

Copier le contenu du bloc dans un fichier `.patch` ; appliquer seulement à une base comparée et compatible.

```diff
--- a/plans/Plan_V1.2_Suite_Reprise.md
+++ b/plans/Plan_V1.2_Suite_Reprise.md
@@ -93,7 +93,7 @@
 |---|---|---|
 | Hiérarchie et autorité | Chaque règle a un lieu propriétaire ; obligatoire et conditionnel distingués ; résolution des conflits écrite | Gardes de propriété ; relecture |
 | Organisation et accès | Une entrée agent (la skill), une entrée humaine (R6b) ; chaque ressource atteignable au moment où elle sert | Atteignabilité (disparition, accès conditionnel et fragilité d'ancre distingués) ; routes résolubles |
-| Cohérence opérationnelle | Double boucle reliée : connaissance → décision → geste → capture → correction | Relecture de parcours |
+| Cohérence opérationnelle | `DIRECTION/DOUBLE-LOOP` reste la référence : fabrication guidée, réobservation, comparaison, maintien ou réouverture de la direction, arrêt justifié ; observation adaptée au risque (capture, interaction, séquence ou mesure) | Relecture des embranchements et de leurs renvois, sans nouvelle définition de la boucle |
 | Clarté et charge | Pas de doublon contradictoire ; aucune nuance utile perdue ; jargon expliqué | Mesure des doublons ; glossaire ; relecture |
 | Fiabilité | Renvois valides ; exemples conformes aux règles ; distributions GitHub et Local fidèles aux sources | `validate_all`, 13.01, 13.02, suivi, build des distributions |
 
@@ -110,12 +110,14 @@
 - un humain novice ;
 - un expert qui reprend un run.
 
-On note chaque trou, chaque contradiction et chaque ressource qui arrive trop tard ; chaque constat entre dans l'inventaire. La relecture se fait à la fin des lots, puis à la porte P2.
+On note chaque trou, chaque contradiction et chaque ressource qui arrive trop tard ; chaque constat entre dans l'inventaire. La relecture suit aussi les retours de `DIRECTION/DOUBLE-LOOP` : défaut local, direction à rouvrir, risque changé, preuve insuffisante et arrêt justifié. Elle vérifie le passage d'une première proposition exploratoire à une acceptation pour un produit réel (R7). Une observation par interaction ou mesure reste accessible lorsque la capture ne suffit pas. La relecture se fait à la fin des lots, puis à la porte P2.
+
+**Inventaire :** réconcilier les registres existants dans une vue unique (identifiant, emplacement, conséquence, lot, état, preuve ou limite). Un défaut déjà corrigé reste un acquis à vérifier ; il ne redevient pas une correction à faire. Une classification « non bloquant P2 » se justifie par la conséquence restante. Pour Q13 et R16–R32, la classification reste à instruire jusqu'à lecture des traces : une absence de preuve ne permet pas de les déclarer non bloquants. P2 s'appuie sur les outils existants ; l'ajout du cliquet d'atteignabilité reste une proposition distincte.
 
 ### R10 progressif
 
 - **But :** évaluer ce qu'une lecture ne peut pas établir (qualité réelle, facilité d'usage, coût, variabilité), pas améliorer le système.
-- **Palier exploratoire :** 2 briefs contrastés (B-DLA et SaaS) × 3 conditions (C1, C3, C4), soit environ 6 productions. Environ 4 si les rendus B-DLA existants restent comparables (même modèle producteur) ; sinon on les refait.
+- **Palier exploratoire :** 2 briefs contrastés (B-DLA et SaaS) × 3 conditions (C1, C3, C4) = **6 cas comparés**. Il faut 6 productions neuves, ou 4 seulement si une référence B-DLA C1 et une référence B-DLA C4 restent réutilisables. Vérifier et consigner pour chaque réemploi : modèle et version, consignes et brief, outils et capacités, intrants, limites de production, captures et mesures. Déclarer les écarts et refaire un cas lorsqu'ils empêchent la comparaison. **C3 est produit avec la candidate consolidée après P2** ; un ancien rendu C3 de P1 (package après R4) reste une pièce historique et ne représente pas cette candidate.
 - **Critères écrits avant de produire :**
   - ce qu'est un « problème évident » (on corrige d'abord) ;
   - ce qui justifie de passer à 18 ;
@@ -237,7 +239,7 @@
 | Lot | Décision | Recommandation |
 |---|---|---|
 | R7 (texte d'orientation) | 6 (ancre), 8 (lois), 10 (catalogue) | 6 (a) graduée par destination ; 8 (a) tester en R10 ; 10 (a) après publication |
-| R9 (trace machine, schéma) | 3 (version) | (a) V1.2.0 si `RUN_CARD` rétrocompatible : champ `trace_level` (`light` / `full`) facultatif, `modal` / `parti` avec alias `anti_direction` |
+| R9 (trace machine, schéma) | 3 (version) | **Reporté.** Schéma `RUN_CARD` inchangé ; aucun champ nouveau ; `modal` / `parti` restent projetés dans `direction.anti_direction` ; publication visée V1.2.0 |
 | R10 (épreuve à l'aveugle) | 9 (juges) | (c) personnes extérieures et juges modèles d'autres familles, déclarés non indépendants |
 | R12 (publication V1.2.0) | feu vert final | après R10 |
 
@@ -247,5 +249,5 @@
 - **Carte de lecture d'ACTION** : conservée (C4, 13.02 et `validate_design_governance` en dépendent), gardée par CHG-09. Sa fusion demande une rectification déclarée de ces outils.
 - ~~D-19~~ (R5a) ; ~~D-21~~ (R8a) ; ~~D-16~~ (R5c) ; ~~F22~~ (R5d, atteignable depuis Gate C).
 - **Mesure d'atteignabilité** : elle repose sur des ancres textuelles (`audit/data/V12R/V12R_outils_fabrication.json`) ; une reformulation peut faire « disparaître » un outil encore présent (cas F13 en R8a, rectifié en R11a). Proposition : cliquet d'atteignabilité dans `V12R_Suivi.py` (à décider).
-- **Plan consolidé (proposition du 27-09-2026)** : `plans/propositions/Plan_consolide_V1.2_2026-09-27.md`. Non actif : ses arbitrages seront intégrés à ce plan après décision de l'owner, sans second plan concurrent.
+- **Plan consolidé et amendement archivés** : documents de provenance, sans statut de plan actif. Les arbitrages pris sont consignés dans `V12R_14` et intégrés au §4 ; les anciennes recommandations remplacées restent historiques.
 - **Coût d'un run** (D-23) : l'effet de la trace légère n'a pas été mesuré, ce sera en R10.
--- a/plans/Plan_V1.2_Refonte.md
+++ b/plans/Plan_V1.2_Refonte.md
@@ -1,6 +1,6 @@
 # Plan V1.2 — Refonte : fabrication, structure, trace et preuve
 
-**Date :** 2026-09-27 · **Owner :** Junior (Kamel) · **Statut :** en cours. R1 à R4 appliqués, P1 fait, R5b-1, R5b-2 et R5a appliqués (27-09-2026, `audit/reports/V12R_01` à `V12R_08` ; reprise : `plans/Plan_V1.2_Suite_Reprise.md`) ; décisions 1, 2, 4, 5, 7 et 11 prises, D-20 et D-22 tranchés. Chemin prescrit 12 076 mots en trace légère (16 687 en trace complète) ; 24/25 outils sur le chemin ; noyau 3 222 mots. Consigne de l’owner : la qualité du résultat prime sur le nombre de mots (pas de plafond de coupe ; on ne retire que doublons et texte sans effet). Prochaine étape : R5c, R5d, R6, R8, R11.
+**Date de création :** 2026-09-27 · **Pilotage au :** 2026-09-30 · **Owner :** Junior · **Statut :** consolidation avant évaluation. R1 à R4, P1, R5b-1, R5b-2, R5a, R8a, R5c hors ancre, R5d, R6a et R11a sont documentés comme faits (`V12R_01` à `V12R_13`). Dernières mesures rapportées après R11a : chemin 12 187 mots en trace légère, 16 798 en trace complète ; noyau 3 302 mots ; 24/25 outils comptés, F22 accessible sous condition. Les contrôles correspondants ne sont pas réexécutés par cette synchronisation. **Reprise opérationnelle :** `plans/Plan_V1.2_Suite_Reprise.md` §4 ; décisions : `V12R_14`, addendum 2.
 **Base :** B05, candidate V1.2 (lots 1 et 2 appliqués).
 **Sources du plan :**
 - lectures `V12_05` à `V12_10` et synthèse `V12_11` (registre D-01 à D-18) ;
@@ -8,7 +8,7 @@
 - dossier de clôture DG-AUDIT-001, §3 (réserves 1 à 9) ;
 - mineurs transmis (Q-04, Q-07, Q-08, Q-09, Q-11, Q-12, Q-13 ; R-16 à R-32).
 
-Ce plan **remplace le séquencement** du plan V1.2 et de l'addendum à partir de maintenant. Leurs chantiers y sont repris (§4). Les décisions G1 déjà prises restent valables, sauf si le §8 les rouvre explicitement.
+Ce plan conserve l'architecture du chantier et l'historique des lots. **Le plan de reprise porte le séquencement opérationnel courant**, et `V12R_14` les décisions et leurs révisions. En cas d'écart, les décisions actuelles et leur intégration au plan de reprise prévalent sur les périmètres d'origine ci-dessous. Les décisions G1 restent valables dans leur portée non révisée.
 
 ---
 
@@ -237,17 +237,23 @@
 - Lois de SAVOIR (décision 8) : testées en R10.
 - Catalogue élargi aux contextes de l'owner (décision 10) : **après publication**, à partir de runs réels, en `PILOT`.
 
-**R8 — Matériaux et atlas** (M ; chantiers C et E')
-- **Périmètre :** carte des moyens consolidée (critères + sources datées `[VEILLE]`) ; atlas d'ancres annotées v1 (liens et descriptions, double colonne visuel / fond, références hors canon occidental), placé en **référence de la skill**, chargée seulement si la décision visuelle est ouverte.
-- **Arrêt :** si R10 montre une baisse de diversité, on retire les exemples et on ne garde que les critères (règle déjà décidée dans le plan V1.2).
-
-**R9 — Trace machine** (L ; décision 3)
-- **Périmètre :** niveau de trace dans la `RUN_CARD` (léger / complet) ; champ facultatif `fabrication` ; vocabulaire `direction.anti_direction` → `modal`/`parti`, avec alias de compatibilité.
-- **Version :** si le schéma reste **rétrocompatible**, V1.2.0 ; sinon V1.3.0.
+**R8 — Moyens et gestes de résolution** (périmètre courant : plan de reprise §4)
+- **R8a fait :** question de convergence typographique ; effet sur les rendus encore à mesurer.
+- **R8b :** carte des moyens consolidée et enseignements transférables confrontés aux propriétaires existants ; aucune intégration obligatoire des 18 créations de l'atlas.
+- **R8c :** préciser les gestes insuffisamment opérables, avec déclencheur, corrections possibles et observation de l'effet ; aucun quota de gestes ou de retouches.
+- **Diversité :** si elle baisse en R10, examiner les consignes et ressources susceptibles de favoriser la convergence, sans présumer sa cause.
+
+**R9 — Trace machine : reporté** (décision 3)
+- **Périmètre d'origine conservé en historique :** champs de trace et de fabrication, renommage avec alias. Aucun de ces changements de schéma ne fait partie de la candidate actuelle.
+- **Décision actuelle :** schéma `RUN_CARD` inchangé ; `modal` / `parti` projetés dans `direction.anti_direction` ; version cible V1.2.0 ; report déclaré lors de R12.
 
 ### Vague V — Preuve, réserves, publication
 
-**R10 — Épreuve à l'aveugle** (L ; chantier F ; décision 9)
+**R10 — Évaluation progressive** (chantier F ; décision 9)
+
+**Périmètre actif :** après P2 et levée de la consigne « pas de run », palier exploratoire de 6 cas, puis 18 si justifié ; extension seulement pour une question définie. Candidate, conditions, mesures et critères de décision fixés avant production, réemploi des références selon le plan de reprise §4. L'observation novice est distincte.
+
+**Protocole élargi de référence ci-dessous :** option d'extension, sans lancement automatique ni seuil statistique établi. Les anciens critères de décision doivent être rendus opérables avant une épreuve qui les utilise.
 - **Briefs :** B-DLA (commerce, Douala), B-LOG (reporté), un produit SaaS, un service public, un portfolio.
 - **Conditions :**
   - C1 : brief vague, sans système ;
@@ -279,15 +285,9 @@
 
 ### Dépendances
 
-```
-R1 → R2 → R3 → R4 → P1 ─┬→ R5a → R5b → R5c → R5d → R6 → R9
-                        └→ R7 (texte) , R8
-R6 + R8 + R9 → R10 → R11 → R12
-```
-
-R11 (tri des mineurs) peut commencer en parallèle dès R2, pour les mineurs que la refonte ne rend pas obsolètes.
-
-**Signalement de taille (style de l'owner) :** le programme compte **douze lots**, dont trois grands (R5b, R9, R10). Il est surdimensionné pour être mené d'un bloc. Le point de contrôle P1 permet de s'arrêter après la vague II si le noyau ne change pas le rendu.
+Le séquencement courant est celui du plan de reprise §4 : inventaire → R8b → R8c → R7 → R11 ciblé → R6b élargi → restes R5 → relecture de parcours et P2 → R10 progressif → R11 final → R12. R9 est reporté et ne conditionne pas R10.
+
+**Charge :** les lots de consolidation sont traités séparément. R10 augmente seulement si les résultats ou une question ouverte le justifient ; P1 reste une orientation historique.
 
 ## 6. Méthode
 
@@ -301,7 +301,7 @@
    - table de correspondance des harnais (300 cas : conservé / obsolète déclaré) ;
    - R, R03, 13.01, 13.02 ;
    - B01 218/218.
-3. **Budget mesuré à chaque lot** sur le chemin prescrit (R1). Aucun lot n'augmente le chemin sans décision.
+3. **Charge mesurée à chaque lot** sur le chemin prescrit (R1). Une augmentation utile est justifiée et déclarée ; les coupes visent les doublons et le texte sans effet, conformément à « qualité avant nombre de mots ».
 4. **Aucune correction non décidée** (règle 3). Un défaut découvert va au registre D-xx avec son lot.
 5. **Rapport allégé par lot** : diff, résultats, écarts déclarés, certain / probable / hypothétique.
 6. **Charte de rédaction** appliquée à tout texte réécrit :
@@ -322,12 +322,14 @@
 | Coût des harnais (prose figée) | Plus de rectifications que de changements de texte | R2 avant tout ; table de correspondance ; arrêt commun de R5 |
 | Perte de l'honnêteté mesurée | Données d'exemple non marquées en P1 ou R10 | Gardes d'honnêteté (R2) ; critère bloquant en R10 |
 | Style maison créé par le noyau (mêmes gestes → mêmes rendus) | Diversité en baisse en P1 ou R10 | Mesure de diversité ; gestes formulés en décisions, pas en styles ; retrait des exemples (R8) |
-| Noyau qui gonfle | > 3 000 mots | Arrêt de R4 ; tout ajout financé par une coupe |
+| Charge qui augmente sans contribution utile | Parcours alourdi sans décision, construction ou vérification améliorée | Justifier les ajouts ; retirer les doublons et le texte sans effet ; anciens seuils de mots conservés comme diagnostic historique |
 | Biais d'auto-comparaison | Mêmes conclusions que l'auteur | Juge neuf en P1 ; regard extérieur en R10 ; déclaration |
 | Surdimensionnement | Lots qui débordent | Découpage de R5b et R9 ; P1 comme porte de sortie |
 | Temps et usage de l'owner | Décisions en attente | Décisions groupées (§8) ; défauts par recommandation écrite |
 
-## 8. Décisions attendues de l'owner
+## 8. Arbitrages d'origine et décisions prises
+
+Les options ci-dessous sont historiques ; l'état courant figure dans `V12R_14`, addendums 1 et 2.
 
 | # | Décision | Options | Recommandation |
 |---|---|---|---|
@@ -345,7 +347,7 @@
 
 Les décisions 1, 2, 4 et 7 conditionnent R2 à R4. Les autres peuvent attendre leur lot.
 
-**Décisions prises :** 1, 2, 4 et 7 (`V12R_00`) ; 5 (a) et 11 (a), avec D-20 (exemple marqué) et D-22 (test de trame sans coût) (`V12R_06`, 27-09-2026). **Prises le 27-09-2026 (`V12R_14`) :** 3 (a) V1.2.0, schéma inchangé, R9 reporté ; 6 (a) graduée ; 8 (a) ; 9 (c) ; 10 (a) ; atlas intégré en R8b (révision de G1) ; R10 par paliers ; R11 ciblé ; ordre « le rendu d'abord ». **Aucune décision en attente.** Lots ajoutés le 27-09-2026 : **R8c** (passe de finition) et **R6b élargi** (entrée humaine d'une page) ; ordre et détail dans `plans/Plan_V1.2_Suite_Reprise.md` §4.
+**Décisions prises :** 1, 2, 4 et 7 (`V12R_00`) ; 5 et 11, D-20 et D-22 (`V12R_06`) ; 3, 6, 8, 9 et 10 (`V12R_14`). **Révisions au 30-09-2026 :** R8b sans atlas obligatoire ; R8c ciblé sur les gestes insuffisamment opérables ; R6b inclut l'entrée Local générée ; consolidation avant R10, porte P2 et évaluation progressive. Schéma inchangé, R9 reporté, V1.2.0. Les questions encore à instruire (cliquet d'atteignabilité, critères de R10, disponibilité des regards extérieurs, feu vert final) restent explicites dans le plan de reprise.
 
 ## 9. Lecture
 
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -58,10 +58,10 @@
 - **R5c appliqué, hors ancre** (`V12R_10_R5c_SAVOIR.md`) : un seul modèle de niveaux (D-16), boucle et one-shot de SAVOIR en renvoi ; doublons 145 ; suivi vert.
 - **R5d appliqué** (`V12R_11_R5d_BIBLIOTHEQUE.md`) : boucle et one-shot de BIBLIOTHEQUE en renvoi (exemptions retirées) ; F22 : tests perceptifs `PRC-01` appelés depuis Gate C ; suivi vert.
 - **R6a appliqué** (`V12R_12_R6a_FACADES.md`) : boucle du README en renvoi (la garde « boucle unique » n'a plus d'exemption provisoire), 5 termes au glossaire ; suivi vert ; doublons 144.
-- **R11a appliqué** (`V12R_13_R11a_CORRECTIFS.md`) : résidu `DAILY` retiré de `DIRECTION/START` ; ancre de mesure F13 rectifiée (24/25, F22 atteignable sous condition depuis Gate C) ; carte des moyens v0 alignée sur D-20. Mesures : chemin 12 187 mots, noyau 3 302. **Plan consolidé proposé** (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`) : non actif tant que ses arbitrages ne sont pas décidés et intégrés au plan de reprise.
-- **Arbitrages décidés** (`V12R_14_DECISIONS_ARBITRAGES.md`, 27-09-2026) : toutes les options recommandées. Décision 6 : ancre graduée ; décision 3 : schéma inchangé → V1.2.0, R9 reporté ; atlas intégré en R8b (révision de G1) ; décision 9 : juges humains + modèles ; décision 8 : lois inchangées ; décision 10 : catalogue après publication ; R10 par paliers (18 productions) ; R11 ciblé ; ordre « le rendu d'abord ».
-- **Pilotage synchronisé** (30-09-2026, `V12R_14` addendum 2) : amendement du 28-09 intégré (R8b sans atlas, avec enseignements transférables ; R8c recadré sur les gestes insuffisants ; R7, R11 et R6b précisés ; README Local du build inclus en R6b) ; **consolider avant d'évaluer** : porte **P2 « prêt pour l'évaluation »**, inventaire unique des défauts, relecture de parcours ; **R10 progressif** (palier exploratoire d'environ 4 à 6 productions, puis 18 si justifié) ; observation novice distincte ; anciens plafonds de mots historiques ; référence G1 rectifiée (décision 2).
-- **Chantier en cours : plan V1.2**, `plans/Plan_V1.2_Qualite_senior_gouvernance.md`. Objectif : un premier rendu de niveau designer senior dès le one-shot, gouvernance conservée (bilan de fabrication, prise de brief minimale, matériaux, anti-slop vivant, atlas d'ancres, épreuve à l'aveugle).
+- **R11a appliqué** (`V12R_13_R11a_CORRECTIFS.md`) : résidu `DAILY` retiré de `DIRECTION/START` ; ancre de mesure F13 rectifiée (24/25, F22 atteignable sous condition depuis Gate C) ; carte des moyens v0 alignée sur D-20. Mesures : chemin 12 187 mots, noyau 3 302. **Plan consolidé archivé** (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`) : provenance historique ; arbitrages intégrés au plan de reprise, avec les révisions de `V12R_14` addendum 2.
+- **Arbitrages initiaux décidés** (`V12R_14_DECISIONS_ARBITRAGES.md`, 27-09-2026 ; calendrier de l'atlas et volume de R10 révisés par l'addendum 2 du 30-09) : toutes les options recommandées. Décision 6 : ancre graduée ; décision 3 : schéma inchangé → V1.2.0, R9 reporté ; atlas intégré en R8b (révision de G1) ; décision 9 : juges humains + modèles ; décision 8 : lois inchangées ; décision 10 : catalogue après publication ; R10 par paliers (18 productions) ; R11 ciblé ; ordre « le rendu d'abord ».
+- **Pilotage synchronisé** (30-09-2026, `V12R_14` addendum 2) : amendement du 28-09 intégré (R8b sans atlas, avec enseignements transférables ; R8c recadré sur les gestes insuffisants ; R7, R11 et R6b précisés ; README Local du build inclus en R6b) ; **consolider avant d'évaluer** : porte **P2 « prêt pour l'évaluation »**, inventaire unique des défauts, relecture de parcours ; **R10 progressif** (6 cas exploratoires, dont 4 à 6 productions neuves selon le réemploi vérifié de références C1/C4 ; C3 produit sur la candidate consolidée ; puis 18 si justifié) ; observation novice distincte ; anciens plafonds de mots historiques ; référence G1 rectifiée (décision 2).
+- **Chantier en cours : consolidation V1.2**, pilotée par `plans/Plan_V1.2_Suite_Reprise.md` ; architecture dans `plans/Plan_V1.2_Refonte.md`, décisions dans `V12R_14`. Objectif : un premier rendu composé, spécifique et soigné, avec une entrée humaine claire et un effort maîtrisé ; efficacité encore à évaluer. R8b mobilise les moyens et les enseignements transférables ; R8c précise les gestes utiles ; aucun atlas de créations obligatoire.
 
 ## 3. Arborescence
 
@@ -133,7 +133,7 @@
 1. ~~Porte G1 du plan V1.2~~ : franchie le 26-09-2026 (`audit/reports/V12_01_DECISIONS_G1.md`).
 2. ~~B05, lot 1 (A, B, D), addendum, lot 2 (G, H, I, D')~~ : faits (`V12_02` à `V12_04`). Lectures `V12_05` à `V12_11` faites. Mini-épreuve **reportée par l'owner** (27-09-2026). **Refonte (`plans/Plan_V1.2_Refonte.md`) : décisions 1, 2, 4, 7 prises ; R1, R2, R3 et R4 faits. P1 fait (orientation positive). R5b-1, R5b-2, R5a, R8a, R5c (hors ancre), R5d, R6a et R11a faits. Arbitrages décidés (`V12R_14`). Prochaine : inventaire des défauts → R8b (moyens, sans atlas) → R8c (gestes insuffisants) → R7 → R11 ciblé → R6b élargi → restes R5 → relecture de parcours → porte P2 → R10 progressif → R11 final → R12 — voir `plans/Plan_V1.2_Suite_Reprise.md`**, puis G4.
 **Plan de reprise (à lire en premier pour continuer) : `plans/Plan_V1.2_Suite_Reprise.md`** — consignes en vigueur (pas de run ni d'épreuve dans cette phase ; qualité avant nombre de mots), recette d'une unité, lots restants avec périmètre, gardes, réussite et arrêt, porte P2 et R10 progressif.
-3. Suivre le séquencement du plan : G2 (gardes rouges puis vertes) → G3 (non-régression, budget tenu) → G4 (épreuve à l'aveugle avec juges extérieurs) → publication V1.2.0.
+3. Suivre le séquencement du plan : G2 (gardes rouges puis vertes) → G3 (non-régression, charge mesurée et justifiée) → G4 (épreuve à l'aveugle avec juges extérieurs) → publication V1.2.0.
 
 Travail par branche : une branche par unité (`v1.2/patch-decision-abd`, …) ; étiquettes aux points de contrôle ; rapport de l'unité dans `audit/reports/`.
 
--- a/plans/carte_moyens_v0.md
+++ b/plans/carte_moyens_v0.md
@@ -2,13 +2,13 @@
 
 **Date :** 2026-09-27 · **À revoir avant :** 2027-03 · **Règle :** des **sources**, jamais des styles ; aucune famille, aucun thème par défaut ; le choix découle de la thèse. Droits vérifiés à chaque usage.
 
-| Couche | Plafond sans asset fourni (conditions) | Où trouver de la qualité | Route (`VISUAL_TARGET`) |
+| Couche | Conditions et limites de fabrication | Où trouver de la qualité | Route (`VISUAL_TARGET`) |
 |---|---|---|---|
 | Typographie | Atteignable si la police est chargeable dans la cible et sa licence vérifiée pour l’usage (web, app, impression) | Polices de la marque ; Google Fonts (licences ouvertes, surtout SIL OFL) ; Fontshare (licence propre au service, gratuite sous conditions, à relire par police) | `CODE-NATIVE` |
-| Icônes | Atteignable si la famille couvre les pictogrammes nécessaires ; licence à vérifier | Une seule famille cohérente (par exemple Lucide, Phosphor) | `CODE-NATIVE` |
+| Icônes | Atteignable si la famille couvre les pictogrammes nécessaires ; licence à vérifier | Famille adaptée aux pictogrammes requis (par exemple Lucide, Phosphor) ; cohérence de poids, de taille et de sens à vérifier ; le choix d'une seule famille dépend du projet | `CODE-NATIVE` |
 | Composants | Atteignable dans la stack réelle ; hors web, traduire dans les idiomes de la plateforme | Design system fourni ; sinon bibliothèque éprouvée (par exemple shadcn, Radix) | `CODE-NATIVE` |
 | Données, objets de preuve | Atteignable | Contenu du client, sinon données plausibles marquées illustratives | `CODE-NATIVE` |
-| Texture et traitement | Atteignable si le rendu et la performance sont vérifiés à la capture | Filtres CSS et SVG, canvas | `CODE-NATIVE`, `HYBRIDE` |
+| Texture et traitement | Atteignable si le rendu est inspecté sur capture et si la performance est mesurée dans le runtime cible | Filtres CSS et SVG, canvas | `CODE-NATIVE`, `HYBRIDE` |
 | Photographie | Non sans intrant | Client (même au téléphone, lumière du jour) ; banques sous licence (Wikimedia Commons, Unsplash) | `FOURNI`, `CURATÉ` |
 | Illustration, 3D | Non sans intrant | Commande, packs sous licence ; génération dirigée avec références ; 3D (par exemple Spline) | `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` |
 | Fichiers de design, marque | Non sans intrant | Figma ou kit de marque par connecteur | `FOURNI` |
@@ -16,4 +16,4 @@
 
 **Avant R8b :** chaque ressource retenue est vérifiée au moment de l’intégrer ou de l’utiliser (licence, usage, disponibilité) ; le nom d’une plateforme ne vaut pas autorisation générale (amendement du 28-09-2026).
 
-**Traitement des assets moyens (chantier I) :** un seul traitement cohérent (recadrage, étalonnage, duotone, grain ou trame), justifié par la thèse ; la trame est un marqueur de la vague 3, à décider, pas à suivre.
+**Traitement des assets moyens (chantier I) :** choisir le traitement que justifie la thèse (recadrage, étalonnage, duotone, grain ou trame) et vérifier la relation entre les images et la composition. Un traitement commun peut unifier des assets disparates ; plusieurs traitements peuvent être pertinents si leurs rôles sont intentionnels et cohérents. La trame reste un marqueur de la vague 3, à décider, pas à suivre.
--- a/audit/reports/V12R_14_DECISIONS_ARBITRAGES.md
+++ b/audit/reports/V12R_14_DECISIONS_ARBITRAGES.md
@@ -35,7 +35,7 @@
 |---|---|---|
 | **R8b réorienté** | L'intégration des 18 créations de l'atlas **cesse d'être un objectif** ; leurs images, liens et recherche exhaustive ne conditionnent plus R8b. R8b = carte des moyens consolidée (capacité, ressources, limites ; conditions au lieu de « atteignable en HTML seul » ; licences vérifiées par ressource) + **enseignements transférables** confrontés à l'existant (renvoi ou ajout ciblé, conditionnel, avec observation attendue et contre-indication). Attribution conservée pour une contribution précise ; aucun jugement global sur une création ou son auteur | L'intégration de l'atlas en R8b (addendum 1, 27-09) ; l'atlas v0 reste un matériau historique |
 | **R8c recadré** | Pas de douzaine de recettes systématiques ni de bloc `FINITION` comme fin en soi. Compléter seulement les gestes insuffisamment opérables (équilibre d'un titre, relation texte/image, poids optique des icônes, récupération après erreur, réinspection de l'ensemble après un réglage local), avec déclencheur, corrections possibles et observation de l'effet. **Aucune modification obligatoire si la relation fonctionne.** « Accent unique », « traitement unique », « famille unique » restent des solutions contextuelles, jamais des exigences universelles | La liste de l'addendum 1 |
-| **R10 progressif** | 18 et 60 productions servent à **évaluer**, pas à améliorer. Palier exploratoire : 2 briefs contrastés × 3 conditions (≈ 6 productions ; ≈ 4 si les rendus B-DLA existants restent comparables, même modèle producteur). Problème évident → corriger d'abord ; résultats encourageants mais incertains → 18 ; au-delà seulement pour une question précise encore ouverte. Les 18 peuvent faire partie des 60 à protocole et version identiques. Critères de décision écrits **avant** de produire ; mesures : qualité de la première proposition, reprises, effort, honnêteté | Le palier 1 de 18 productions |
+| **R10 progressif** | Évaluer après consolidation. Palier exploratoire : 2 briefs × C1, C3, C4 = **6 cas comparés**, avec 4 à 6 productions neuves selon la réutilisation vérifiée d'une référence B-DLA C1 et d'une référence B-DLA C4. Même modèle ne suffit pas : consignes, intrants, outils, capacités, limites, captures et mesures restent comparables et les écarts sont consignés. **C3 utilise la candidate après P2 ; les C3 de P1 ne la représentent pas.** Problème évident → diagnostic et correction ; extension à 18 puis davantage seulement si justifiée, critères écrits avant production | Le palier initial de 18 ; précision des conditions de réemploi, sans nouveau lancement autorisé |
 | **Observation novice** | Distincte des productions d'agents : 2 ou 3 personnes lisent l'entrée R6b et lancent une demande ; on note les blocages. Aucun volume de runs ne la remplace | — |
 | **Consolider avant d'évaluer** | Aucun run avant la **porte P2 « prêt pour l'évaluation »**. Corriger et améliorer = mettre l'existant à sa place (hiérarchie, organisation, accès, cohérence, clarté, fiabilité), pas ajouter ni retirer au hasard ; chaque modification répond à un défaut identifié, préserve ce qui marche et a une vérification proportionnée. Les moyens de produire du beau interviennent **pendant** la conception. Outils : **inventaire unique des défauts** (bloquant P2 ou non) et **relecture de parcours** (4 profils) | Le palier exploratoire ne contourne pas la consolidation |
 
```
