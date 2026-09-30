# V1.2 refonte — Porte P2 « prêt pour l'évaluation » — Examen

**Date :** 30-09-2026.
**Candidate :** `cb669a6` (après R11b).
**Référentiel :** plan de reprise, « Porte P2 » (cinq axes, seuil).
**Méthode :** examen sur preuves (inventaire, suivi, mesures, gardes, relecture de parcours, résolution des routes), sans production. Auto-examen déclaré : ce n'est pas un observateur D3, et aucun verdict d'efficacité n'est posé.

## 1. Seuil

| Condition du seuil | État | Preuve |
|---|---|---|
| Aucun « bloquant P2 » ouvert dans l'inventaire | **Tenu (certain)** | Inventaire (54 lignes) : aucune ligne classée bloquante sans être fermée. Les derniers bloquants fermés sont D-15 (`V12R_30`), puis G1, G2 et G4 (`V12R_32`) |
| Parcours essentiels vérifiés | **Tenu (certain)** | Relecture de parcours `V12R_31` (agent sur brief vague, agent sur brief riche avec photos, novice, expert qui reprend) ; ses constats sont corrigés |
| Limites restantes écrites et non bloquantes pour l'épreuve | **Tenu** | §3 ci-dessous |

## 2. Les cinq axes

| Axe | Critère | Preuve | État |
|---|---|---|---|
| **Hiérarchie et autorité** | Chaque règle a un lieu propriétaire ; obligatoire et conditionnel distingués ; résolution des conflits écrite | `validate_structure` : 25 concepts à leur lieu propriétaire, 28 vocabulaires retirés, 25 résumés fidèles, noyau compilé, chargement unique ; UNI-01, LOC-01, ENT-01, CST-01, MAP-01, MNT-01, ALT-01 | Tenu (certain) |
| **Organisation et accès** | Une entrée agent, une entrée humaine ; chaque ressource atteignable au moment où elle sert | Skill (noyau lu à chaque run) ; section « Commencer » du README du package, reprise par le README Local généré ; `DIRECTION/CHARGE` seule liste ; **66/66 routes citées résolues** ; 24/25 outils sur le chemin (F22 atteignable depuis Gate C, sous condition) | Tenu (certain) |
| **Cohérence opérationnelle** | Double boucle reliée : fabrication, réobservation, comparaison, maintien ou réouverture, arrêt justifié ; observation adaptée au risque | Boucle d'édition du noyau (six diagnostics et leurs suites ; question 5 sur la page entière) ; B1b relié à l'arrêt one-shot (Q-09) ; observation par interaction via Gate C (`RCV-01`, `PRC-01`) ; passage de la proposition à l'acceptation dit (G1) ; demandes de brief avant le build quand la personne est présente (G2) ; trace légère dans chaque route et reprise ITER (G4) | Tenu (certain, sur texte) |
| **Clarté et charge** | Pas de doublon contradictoire ; aucune nuance utile perdue ; jargon expliqué | Doublons **134 occurrences** (190 en référence), sans contradiction dans les amas examinés ; glossaire (16 termes gardés) ; entrée humaine sans mode ni jargon (ENT-01) ; chemin prescrit **13 105 mots** (≈ 23 600 à l'ouverture de la refonte) ; préambule de BIBLIOTHEQUE −25 % | Tenu (probable : revue des doublons par amas, non exhaustive) |
| **Fiabilité** | Renvois valides ; exemples conformes ; distributions fidèles aux sources | Suivi complet vert à `cb669a6` (389 cas, 363 maintenus, 26 migrés avec gardes de remplacement) ; `validate_all` vert (build GitHub et Local, reproductibilité) ; 13.01 6/6 et 5/5 ; 13.02 38/38 ; B01 218/218 ; 82 cas unitaires | Tenu (certain) |

**Pilotage (PIL-01 à PIL-04)**, à confirmer par la relecture : **confirmé**.
- Plan de reprise cohérent avec l'état.
- Embranchements de la double boucle vérifiés.
- Condition de réemploi des références C1 et C4 écrite (C3 produit sur la candidate consolidée).
- Carte des moyens avec conditions (capture, performance mesurée, choix selon la thèse).

## 3. Limites restantes (écrites, non bloquantes pour l'épreuve)

| Limite | Nature | Traitement |
|---|---|---|
| Efficacité sur des runs réels | `NOT-VERIFIED` | R10 progressif, juges à l'aveugle (décision 9) |
| Facilité pour un novice | Non observée | Observation novice distincte (2 ou 3 personnes) |
| Coût d'un run (D-23), effets de D-21 (police de titre) et D-22 (trame) | Non mesurés | R10 |
| CI hébergée | Non observée | R11 final |
| Premier échec de reproductibilité observé par la revue | Cause inconnue ; relance isolée réussie | R11 final (`V12R_28` §6) |
| Promesse du validateur | Limite de conception : destination « produit réel » hors schéma (décision 3) | Déclarée (`VAL-01`, absolu 2) |
| Doublons restants (134), dont trois copies identiques de la phrase `ANCHOR-GENERATED` | Non contradictoires | À réduire après publication, si utile |
| Défauts signalés non corrigés | Contrôle des chemins Local (faux positif avec un lien vers une ancre) ; garde REGISTER sensible à la casse ; locators numériques dans les libellés des conditions de façade | Hors du chemin d'un run ; à décider (R11 final ou après) |
| Noyau à 4 012 mots | Au-dessus de l'ancien repère de 3 000 | Écart déclaré ; consigne « qualité avant nombre de mots » |

## 4. Conclusion et décision

- **Recommandation (certain, sur les critères écrits) :** P2 est **franchissable**. La candidate est prête pour l'évaluation au sens du plan : aucun bloquant ouvert, parcours vérifiés, limites écrites.
- **Ce que P2 ne dit pas :** rien sur la qualité réelle des rendus, la facilité d'usage ou le coût. Seuls R10 et l'observation peuvent l'établir.

**Décisions de l'owner :**
1. Déclarer la porte P2 franchie : **décidé (30-09-2026, « Allons-y »)**.
2. Lever ou non la consigne « pas de run ni d'épreuve », condition de R10 : **non levée à ce jour** ; demandée avec le protocole du palier exploratoire.

**Protocole écrit :** `plans/Protocole_R10_Palier_exploratoire.md` (30-09-2026).

**Prochaine étape possible sans run (faite) :** écrire le protocole du palier exploratoire de R10 **avant toute production** :
- critère du « problème évident » ;
- seuil pour passer à 18 productions ;
- compromis de coût acceptable ;
- traitement des désaccords entre juges ;
- vérification du réemploi des références C1 et C4 ;
- tableau des mesures par rendu.

## 5. Revue postérieure (30-09-2026) : un bloquant manqué

Une revue externe de `9cbdcc2`, transmise par l'owner, a relancé indépendamment la validation complète, les mutations de R11b, les routes et les mesures (résultats conformes). Elle relève deux points, **vérifiés (certain)** :

1. **PAR-G4b — clôture sans condition de trace.**
   - Les rubriques « Clôture » de `RUN-LITE`, `RUN-ITER`, `RUN-STANDARD` et `RUN-SYSTEM` prescrivent `DECIDED` puis `CLOSED` sans condition. `ACTION/STATUS` exige alors un verdict.
   - Or `TRA-01` dit qu'une trace légère livre une proposition sans verdict ni clôture. Seule `RUN-DIRECTION` dit « En trace complète ».
   - Le noyau porte la bonne règle, mais l'instruction locale la contredit sur le chemin d'un run.
   - **Écart de cet examen :** l'axe « cohérence opérationnelle » a été déclaré tenu. R11b avait traité les rubriques « Sortie » ; les rubriques « Clôture » n'ont pas été relues.
2. **Documentaire :** la note de l'inventaire disait encore PIL-01 à PIL-04 « à confirmer », contre leurs lignes et ce dossier. Corrigée.

**Raccord R11c préparé** (`audit/tools/V12R_Patch_R11c.py`) :
- « En trace complète, » en tête des quatre phrases de clôture, comme `RUN-DIRECTION` ;
- règles de retour et de reclassification conservées ;
- garde de fidélité « clôture des routes en trace complète », rouge avant (4 routes), verte après ;
- 5/5 mutations rouges, dont le retrait de la condition de `RUN-DIRECTION` ;
- testé sur copie, **non appliqué**.
- **suivi complet sur la copie : VERT** (389 cas, 363 maintenus, 26 migrés, aucune migration nouvelle ; `validate_all` vert) ; chemin prescrit inchangé (13 105 mots) ;
- **écart déclaré :** doublons 134 → 139. C'est un amas formel nouveau : les cinq phrases « Clôture. En trace complète, … » ont désormais la même tournure, chacune à sa route, sans copie de contenu ni contradiction. Le cliquet reste vert (référence 190).

**Statut de P2 :** la décision de l'owner (P2 franchie) a précédé cette revue. R11c a été appliqué sur décision de l'owner (`V12R_34`) ; **P2 est conclue**. Le passage de P2 et l'autorisation de produire restent deux décisions distinctes.
