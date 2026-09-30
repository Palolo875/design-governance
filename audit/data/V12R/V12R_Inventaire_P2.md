# V1.2 — Inventaire unique des défauts (vue de la porte P2)

**Créé le :** 30-09-2026, à partir de la note de consolidation préparatoire (`plans/propositions/Consolidation_preparatoire_V1.2_2026-09-30.md`, §2 et §3), complétée par la vérification du dépôt au même jour. **Rôle :** liste de sortie de la consolidation ; chaque lot met à jour les lignes qu'il traite (état, preuve). Document de pilotage : il n'est jamais chargé pendant un run de design.

**Règles :**
- un défaut déjà corrigé reste un acquis à vérifier ; il ne redevient pas une correction à faire ;
- « non bloquant P2 » se justifie par la conséquence restante ;
- Q-13 et R-16 à R-32 ont été instruits le 30-09-2026 sur leurs traces (`V12R_22`) ;
- les classements P2 ci-dessous sont des propositions, à confirmer pendant les lots.

**Lecture des états :** « corrigé documenté » désigne un traitement décrit par un rapport avec ses contrôles, sans réexécution dans cette préparation ; « à traiter » désigne un travail restant dans le plan ; « effet non établi » renvoie à une question d’usage pour R10 ; « à instruire » signale une dépendance de preuve. Les conséquences P2 ci-dessous sont des propositions de classement fondées sur les constats et restent à confirmer pendant les lots.

Cette vue couvre les identifiants D-01 à D-23 et les mineurs transmis. Elle n’annonce ni une nouvelle lecture exhaustive du package ni l’extraction des journaux zip. R-16 à R-32 représentent **17 points individuels**, regroupés ici seulement pour afficher leur dépendance commune ; leur tri ne peut pas être fait collectivement.

## 1. Défauts, mineurs et points de pilotage

| ID | Constat | État fondé sur les pièces | Lot | Conséquence pour P2 / suite | Pièce |
| --- | --- | --- | --- | --- | --- |
| D-01 | Vocabulaire MODAL/PARTI | Corrigé documenté | R3 | Non bloquant, sous réserve de maintien | V12R_03 |
| D-02 | Prise de brief fidèle à sa règle | Corrigé documenté | R3 | Non bloquant ; R6b conserve cette fidélité | V12R_03 |
| D-03 | Règle d'ancre dans skill et façades | **Corrigé (R7, `V12R_21`)** | R7 | ~~Bloquant P2~~ fermé ; limite déclarée : la destination relève de la revue d'acceptation | V12_11 ; V12R_14 |
| D-04 | Positions divergentes sur l'ancre dans SAVOIR | **Corrigé (R7, `V12R_21`) ; raccord R7-2 (`V12R_24`) : sans ancre, `EXPLORATORY` ; `FAIL-ASSUMED` réservé à un échec connu** | R7 | ~~Bloquant P2~~ fermé ; limite déclarée : la destination relève de la revue d'acceptation | V12_11 ; V12R_14 |
| D-05 | Listes de chargement divergentes | Corrigé documenté | R4 | Non bloquant ; contrôler les routes lors de la consolidation | V12R_04 ; V12R_07 |
| D-06 | BIBLIOTHEQUE requise mais hors accès | Traitement documenté | R4 et R5d | Accès conditionnel admis ; F22 ne doit pas être déclaré absent | V12R_04 ; V12R_11 |
| D-07 | Marqueurs et carte des moyens hors d'atteinte | Corrigé documenté | R3 et R4 | Renvois acquis ; qualité de la carte à traiter en R8b | V12R_03 ; V12R_04 |
| D-08 | Glossaire incomplet | Corrigé documenté | R3 et R6a | Préserver les termes ; R6b examine leur usage humain | V12R_03 ; V12R_12 |
| D-09 | Checkpoint avant build incompatible avec la première proposition | Corrigé documenté | R5b-1 | Exception action irréversible ou coûteuse conservée | V12R_06 |
| D-10 | Réponse visible en jargon interne | Traitement documenté dans HANDOFF | R4 ; raccord R6b | Vérifier les façades, sans réécrire le contrat de sortie | V12R_04 ; V12R_12 |
| D-11 | Entrée dispersée et deux README | **Fermé (R6b-1, `V12R_27`)** : une entrée humaine en quatre questions (README du package, reprise par le README Local généré) ; guide opérateur à un parcours ; README officiel en pointeur ; garde ENT-01 | R6b-1 | ~~Bloquant P2~~ fermé ; facilité réelle à observer (novices, R10) | `V12R_25` ; `V12R_27` |
| D-24 | README du dépôt : constitution minimale avec l'ancien absolu 2 ; profil agent orienté vers QUICKSTART | **Fermé (R6b-1, `V12R_27`)** : une seule constitution exacte (garde CST-01) ; agent → skill | R6b-1 | ~~Bloquant P2~~ fermé | `V12R_25` ; `V12R_27` |
| D-12 | Questions recopiées et tu/vous mêlés | Corrigé documenté | R3 | Préserver la fidélité ; ne pas refaire une correction déjà livrée | V12R_03 |
| D-13 | Espace initial de QUICKSTART | Corrigé documenté | R3 | Coquille close ; aucune garde nouvelle | V12R_03 |
| D-14 | Formats de sortie concurrents | Traitement documenté ; raccord à vérifier | R4 ; R6b | Une sortie humaine dérivée de HANDOFF | V12_11 ; V12R_04 |
| D-15 | Instrumentation de maintenance dans la lecture locale | **Fermé (restes R5, `V12R_30`)** : catégories de lecture et contrat de promotion hors du préambule (`BIBLIOTHEQUE/EVOLUTION`) ; déclaration de lecture limitée aux runs instrumentés ou audités ; garde MNT-01 ; préambule −25 % | Restes R5 | ~~Bloquant P2~~ fermé | V12R_11 ; `V12R_29` ; `V12R_30` |
| D-16 | Deux axes présentés comme niveaux identiques | Corrigé documenté | R5c | Distinction moments/niveaux à préserver | V12R_10 |
| D-17 | Rôle et protections placés trop tard | Corrigé documenté | R5a | Aucun déplacement supplémentaire présumé nécessaire | V12R_08 |
| D-18 | Mesure partielle du chemin prescrit | Remplacement de l'outil documenté | R1 ; ajustements R4/R5b-1 | Périmètres déclarés ; fragilité F13 traitée séparément | V12R_01 ; V12R_04 ; V12R_06 |
| D-19 | Prise de brief perdant son contexte dans le noyau | Corrigé documenté | R5a | Préserver le sens du cadrage et de la trace | V12R_08 |
| D-20 | Destination réelle sans contenu : gabarit vide | Règle corrigée documentée | R5b-1 ; R11a | Contenu d'exemple marqué acquis ; effet réel à observer en R10 | V12R_06 ; V12R_13 |
| D-21 | Nouvelle convergence typographique | Geste livré ; effet non établi | R8a ; évaluation R10 | Le résultat ne peut pas être exigé avant usage ; vérifier le geste | V12R_09 |
| D-22 | Trame générique propre au brief | Test de trame livré ; effet non établi | R5b-1 ; évaluation R10 | Préserver l'alternative justifiée ; aucun rendu supplémentaire imposé | V12R_06 |
| D-23 | Surcoût d'un run | Trace légère livrée ; coût non remesuré | R5b-1 ; évaluation R10 | Non bloquant P2 comme résultat à mesurer ; budget d'épreuve fixé avant R10 | V12R_06 ; plan de reprise §5 |
| Q-04 | Portée du contrôle machine de la décision | **Fermé (R11 ciblé, `V12R_23`)** : contrôle machine nommé par mode ; VAL-01 exacte ; garde de vocabulaire et de fidélité | R11 ciblé | ~~Bloquant P2~~ fermé | `V12R_22` ; `V12R_23` |
| Q-07 | Relation entre les scopes de l'artefact et de la direction | **Fermé (`V12R_23`)** : `direction.scope` distingué d'`artifact.scope` ; contrainte = `CONSTRAINT` de START | R11 ciblé | Non bloquant ; garde au niveau de la table (limite déclarée) | `V12R_23` |
| Q-08 | Référence canonique des sorties et vues dérivées | **Fermé (`V12R_23`)** : CLOSE-PACKAGE source, RUN-DIRECTION et RUN-SYSTEM précisions | R11 ciblé | Non bloquant | `V12R_23` |
| Q-09 | Arrêt et comparaison B1b | **Fermé (`V12R_23`)** : one-shot propriétaire relié à B1b (deux motifs conservés, confirmation possible, sans effet en trace légère) ; deux renvois | R11 ciblé | ~~Bloquant P2~~ fermé | `V12R_23` |
| Q-11 | Point conservé par l'arbitrage ciblé | **Maintenu (`V12R_22` §4)** : réserve structurée ≠ simple mention ; aucune preuve nouvelle | R11 ciblé | Non bloquant | `V12R_22` ; V12R_14 |
| Q-12 | Point conservé par l'arbitrage ciblé | **Maintenu (`V12R_22` §4)** : légende limitée à trois tags partagés | R11 ciblé | Non bloquant | `V12R_22` ; V12R_14 |
| Q-13 | Affirmations de cohérence non bornées (README, RELEASE_NOTES) | **README : corrigé (R6b-1, `V12R_27`)** ; RELEASE_NOTES : à réécrire en R12 (texte cible dans `V12R_22` §3) | R12 (RELEASE_NOTES) | Non bloquant : hors du chemin d'un run | `V12R_22` ; `V12R_27` |
| R-16 à R-32 | 17 identifiants, instruits un par un | **Traités (`V12R_23`)** : R-16 et R-21 fermés ; R-17 à R-20, R-23, R-24, R-26 à R-31 corrigés ; R-22, R-25a et R-32 corrigés auparavant ; **R-25b corrigé en R6b-1 (`V12R_27`)** | R11 ciblé ; R6b | ~~Bloquants P2 R-16 et R-21~~ fermés ; tous traités | `V12R_22` ; `V12R_23` |
| PIL-01 | Pilotage périmé et instructions contradictoires | **Intégré le 30-09-2026** (commit `8e430cc`) ; **confirmé par la relecture de parcours et l'examen P2 (`V12R_31`, `V12R_33`)** | Synchronisation documentaire | À résoudre avant la reprise opératoire ; patch ci-dessous | Revue du 30-09 ; cinq fichiers de pilotage |
| PIL-02 | Double boucle réduite dans le contrôle P2 | **Intégré le 30-09-2026** (commit `8e430cc`) ; **confirmé par la relecture de parcours et l'examen P2 (`V12R_31`, `V12R_33`)** | Synchronisation documentaire | Contrôler les embranchements du propriétaire existant | Plan de reprise §4 ; DIRECTION/DOUBLE-LOOP |
| PIL-03 | Réemploi d'anciens rendus insuffisamment conditionné | **Intégré le 30-09-2026** (commit `8e430cc`) ; **confirmé par la relecture de parcours et l'examen P2 (`V12R_31`, `V12R_33`)** | Préparation R10 | À résoudre avant production ; C3 toujours issu de la candidate courante | Plan de reprise §4 ; V12R_05 |
| PIL-04 | Carte : style imposé et performance attestée par capture | **Intégré le 30-09-2026** (commit `8e430cc`) ; **confirmé par la relecture de parcours et l'examen P2 (`V12R_31`, `V12R_33`)** | Synchronisation ; poursuite R8b | À résoudre avant usage de la carte consolidée | plans/carte_moyens_v0.md |
| R8b | Qualité opérationnelle des moyens et enseignements | **Fait (`V12R_15`)** : carte consolidée, A08 ajouté (`EXD-01`), contraste d'échelle et relation texte/image renvoyés à R8c | R8b | Confronter aux propriétaires ; combler seulement les manques établis | Plan de reprise §4 ; amendement §4 |
| R8c | Précision des gestes utiles | **Fait (`V12R_18`)** : titre (`TIT-01`), texte sur image (`TXI-01`), relecture de l'ensemble (question 5), récupération (`RCV-01`) ; icônes et contraste d'échelle couverts | R8c | Non bloquant ; effet à observer en R10 (récupération : par interaction) | `V12R_17` ; `V12R_18` |
| R5 reste | Handoff copié, alternative située, PRINT_FIELD et promotion | **Fait (`V12R_30`)** : renvois au handoff ; alternative répartie (ALT-01) ; signal PRINT_FIELD dans le noyau ; doublons 145 → 134 | Restes R5 | Non bloquants ; fermés | `V12R_29` ; `V12R_30` |
| PKG-01 | Formulations universelles « un seul traitement » et « une seule famille » **dans le package**, alors que l'amendement du 28-09 les veut contextuelles : `SAVOIR` l.587 (bloc noyau `MOY-ASSETS`, compilé dans la skill), `SAVOIR` l.867 (carte des moyens, « Icônes : une seule famille »), `ACTION/GATE-C` C1 (geste ajouté en R5b-2), `DIRECTION` l.483, `references/examples.md` l.39 | **Corrigé (R8b, `V12R_15`)** ; garde UNI-01 au niveau de la phrase (R8b-2, `V12R_16`) : obligation universelle refusée, choix justifié accepté | R8b | ~~Bloquant P2~~ fermé : consigne active lue à chaque run, en contradiction avec une décision ; risque d'uniformisation | Vérification du 30-09 ; amendement §5 |
| R6b-2 | Deux cartes dérivées qui se renvoient (E7 de `V12R_25`) | **Fait (`V12R_28`)** : READING_MAP porte les combinaisons ; ORCHESTRATION_MAP en pointeur ; garde MAP-01 | R6b-2 | Non bloquant P2 ; fermé | `V12R_25` ; `V12R_28` |
| PAR-G1 | « Valider » au checkpoint sans sens défini ; passage exploratoire → acceptation non dit | **Fermé (R11b, `V12R_32`)** : valider oriente la suite ; l'acceptation se demande et passe en trace complète | R11b parcours | ~~Bloquant P2~~ fermé | `V12R_31` ; `V12R_32` |
| PAR-G2 | Moment des demandes de brief ambigu | **Fermé (R11b, `V12R_32`, décision (a))** : humain présent, demandes avant le build, en un seul message | R11b parcours | ~~Bloquant P2~~ fermé ; effet à observer en R10 | `V12R_31` ; `V12R_32` |
| PAR-G4 | Sortie en trace légère non dite hors DIRECTION ; reprise ITER depuis une trace légère | **Fermé (R11b, `V12R_32`)** : « Trace légère : la proposition » dans chaque route ; ligne de thèse retrouvable pour ITER | R11b parcours | ~~Bloquant P2~~ fermé | `V12R_31` ; `V12R_32` |
| PAR-G4b | Rubriques « Clôture » de RUN-LITE, RUN-ITER, RUN-STANDARD et RUN-SYSTEM : `DECIDED` puis `CLOSED` sans condition de trace, contre `TRA-01` (ni verdict ni clôture en trace légère) ; seule RUN-DIRECTION dit « En trace complète ». Relevé par la revue du 30-09 sur `9cbdcc2`, manqué par l'examen P2 | **Ouvert ; raccord R11c préparé** (`audit/tools/V12R_Patch_R11c.py`, vert sur copie), application en attente de l'owner | R11c | **Bloquant P2** : instruction locale contraire au noyau sur le chemin d'un run | Revue du 30-09 ; `V12R_33` §5 |
| PAR-F1 à F3 | Trace de l'alternative, alternative écartée, ordre de chargement | **Fermés (R11b, `V12R_32`)** | R11b parcours | Non bloquants ; fermés | `V12R_31` ; `V12R_32` |

**Identifiants des mineurs regroupés :** R-16, R-17, R-18, R-19, R-20, R-21, R-22, R-23, R-24, R-25, R-26, R-27, R-28, R-29, R-30, R-31, R-32. Ces codes sont ceux de la clôture ; ils ne sont pas les numéros des lots V1.2 ni, sans rapprochement des pièces, des cas de harnais portant un libellé voisin.

**Autres reliquats déjà prévus :** R7 couvre les copies ANCHOR-GENERATED ; les restes R5 comprennent la lecture dédiée des raccords de trace de SAVOIR et la répartition de l’alternative située ; R6b inclut les README des distributions GitHub et Local ainsi que les locators et leurs consommateurs. La carte d’ACTION reste une vue dérivée alignée, gardée par CHG-09 ; son existence seule ne constitue pas un nouveau défaut à supprimer.

**Deux séries « R » distinctes (vérifié le 30-09).** Les mineurs R-16 à R-32 viennent de la revue bornée 13.02 (`Audit_Phase13_02_EPREUVES_Efficacite_auto-comparaison.md`, « transmis tels quels ») et du retour (`Audit_PhaseR_01_PATCH_DECISION_Retour.md` §6 et §7 : « non vérifiés un par un »). Le harnais R (`R_harnais_non_regression.py`, cas R-01 à R-30) utilise des numéros voisins pour d'autres objets (conditions, LCF, conservations machine) : les deux séries ne se rapprochent pas par le numéro.

**PIL-01 à PIL-04 :** intégrés le 30-09-2026 (patch de la note préparatoire, appliqué sur `3966ad5`, empreintes conformes) ; confirmés par la relecture de parcours et l'examen P2 (`V12R_31`, `V12R_33`).

## 2. Réserves de clôture : articulation, sans double comptage

| Réserve de la clôture | Objet | Traitement prévu |
| --- | --- | --- |
| 1 et 4 | Efficacité et limites des preuves de forme | Questions pour l’usage et les observateurs ; ne pas annoncer leur résolution à P2. |
| 2 | CI hébergée non observée | R11 final sur la candidate distribuable ; aucune exécution observée dans cette préparation. P2 vérifie les sources, contrôles et distributions locales prévus. |
| 3 | Cas négatifs manquants | Couverture vérifiée (`V12R_22` §5) ; **six cas ajoutés en R11 ciblé** (N1 à N5 : locator de provenance, `observed` / `not_verified`, `failure_action`, champs de la protection critique, champs de provenance ; `V12R_23`), chacun rouge quand sa règle est retirée. Reliquat : les invariants hors de ces trois domaines ne sont pas réexaminés dans cette phase. |
| 5 | Limite de la promesse du validateur | Conception assumée, à communiquer ; un résultat machine ne devient pas une preuve d’effet. |
| 6 | Charge et coût | Charge documentaire suivie ; D-23 mesure le coût réel en R10. Ne pas confondre baisse des mots et économie observée. |
| 7 | Placeholders de champs libres | Maintien décidé ; aucun filtre global ni restauration d’INV-E11. |
| 8 | Mineurs transmis | Rapprochés des Q/R ci-dessus ; DAILY traité par R4/R11a. Ne pas les ajouter une seconde fois comme défauts indépendants. |
| 9 | V1.1.1 non publiée | État historique ; la livraison V1.2.0 suit R12 et le feu vert final. |
