# Plan V1.2 — Refonte : fabrication, structure, trace et preuve

**Date :** 2026-09-27 · **Owner :** Junior (Kamel) · **Statut :** proposition ; **rien n'est appliqué** avant validation des décisions du §8.
**Base :** B05, candidate V1.2 (lots 1 et 2 appliqués).
**Sources du plan :**
- lectures `V12_05` à `V12_10` et synthèse `V12_11` (registre D-01 à D-18) ;
- plan V1.2 et addendum (chantiers C, E, F non terminés) ;
- dossier de clôture DG-AUDIT-001, §3 (réserves 1 à 9) ;
- mineurs transmis (Q-04, Q-07, Q-08, Q-09, Q-11, Q-12, Q-13 ; R-16 à R-32).

Ce plan **remplace le séquencement** du plan V1.2 et de l'addendum à partir de maintenant. Leurs chantiers y sont repris (§4). Les décisions G1 déjà prises restent valables, sauf si le §8 les rouvre explicitement.

---

## 1. Objectif

Faire de Design Governance **une machine à produire un travail de design de niveau senior dès le premier rendu** :
- beau, vrai, situé ;
- utilisable avec un brief flou, par une personne non spécialiste comme par un connaisseur ;
- **moins coûteux** que V1.1.1 ;
- avec une gouvernance conservée : honnêteté de preuve, plafond déclaré, pas de faux asset.

Le levier (probable, `V12_11` §2) : **placer le savoir-faire existant sur le chemin du run** et **alléger ce qui l'en éloigne**. Presque tout le contenu nécessaire existe ; la refonte déplace, condense et relie davantage qu'elle n'écrit.

## 2. État initial et cibles

| Indicateur | Initial (B05) | Cible V1.2.0 | Nature de la cible |
|---|---|---|---|
| Chemin prescrit d'un run `DIRECTION` (lu à la lettre) | ≈ 23 600 mots, ≈ 1 650 lignes | **≤ 14 000 mots** (−40 %) ; objectif haut ≤ 12 000 | Hypothèse, mesurée à chaque lot |
| Outils de fabrication sur le chemin (`V12_11` §3) | 7 / 25 | **25 / 25 atteignables**, dont ≥ 15 dans le noyau | Mesurable |
| Listes de chargement `DIRECTION` | 6, divergentes | **1**, les autres générées ou remplacées par un renvoi | Mesurable |
| Descriptions de la boucle | 9 | 1 (+ renvois) | Mesurable |
| Copies du handoff, de la constitution | 7 ; 6 | 1 chacune (+ renvois) | Mesurable |
| Défauts signalés ouverts (D-01 à D-18) | 18 | 0 ouvert sans décision | Mesurable |
| Réserves d'audit ouvertes | 9 | Chacune fermée ou maintenue par décision écrite | Mesurable |
| Qualité perçue (épreuve B-DLA) | V1.1.1 ≈ sans système | **V1.2 > sans système et > V1.1.1**, à l'aveugle, diversité tenue | À éprouver (F) |
| Coût en tokens d'un run | ≈ 2 × sans système | **≤ 1,3 ×** sans système | À éprouver |
| Honnêteté (seul effet mesuré de V1.1.1) | Données d'exemple marquées | **Conservée**, sans régression | Garde + épreuve |

**Aucune cible d'efficacité n'est un verdict** (règle 7). Elles servent de critères de décision, pas de preuve générale.

## 3. Architecture cible

### 3.1 Principes

1. **Une chose, un lieu.** Chaque contenu (définition, liste, boucle, règle) a **un seul lieu normatif**. Ailleurs, il y a un renvoi ou une copie **générée** par script, jamais recopiée à la main.
2. **Fabriquer d'abord, prouver ensuite.** Sur le chemin du run, les gestes de fabrication précèdent les contrôles. La preuve lourde devient conditionnelle (run persistant, partagé ou audité).
3. **Positif d'abord.** On dit quoi faire avant quoi éviter. Les frontières de responsabilité sont regroupées dans **une table par fichier**, au lieu de centaines de négations dispersées (≈ 590 relevées en `V12_05` à `V12_10`, méthodes de comptage non homogènes ; R1 fournit un compteur unique).
4. **Gardes de propriété.** Les contrôles vérifient des propriétés (unicité, atteignabilité, égalité des listes, fidélité des copies générées), pas des phrases ni des nombres de lignes.
5. **Proportion réelle.** Ce que la skill fait lire doit être ce que la table de charge dit de lire, et ce que l'outil de budget mesure.

### 3.2 Couches

| Couche | Contenu | Lecture | Lieu |
|---|---|---|---|
| **1. Noyau de run** | Rôle senior ; classement en une ligne ; prise de brief ; **fabrication** (structure, composition, matériaux et moyens, vérité) ; **boucle d'édition** ; sortie en langage produit ; liste de chargement unique ; trace légère | **Toujours**, sans outil (dans la skill) | Blocs normatifs balisés dans les sources, **compilés** dans la skill |
| **2. Routes à la demande** | Classement fin, cible visuelle, premier objet, preuve structurée, gates, catalogue, styles, contexte, technique | Selon la liste de chargement | Les cinq sources, réordonnées : noyau de fichier, référence, table des frontières |
| **3. Maintenance et audit** | Promotion de routes, contrats de route et de `BRAND_GRAMMAR`, instrumentation de lecture, migrations, cycle de vie | **Jamais** pendant un run | Annexes marquées dans les sources, ou fichiers dédiés |
| **4. Façades humaines** | Un README, un QUICKSTART humain, un GLOSSAIRE complet, un index de locators | Humains ; `read_route.py` | `V1/official/` |

### 3.3 Noyau compilé

- Les blocs du noyau restent **normatifs dans leur fichier propriétaire** :
  - rôle et boot dans DIRECTION ;
  - gestes dans SAVOIR ;
  - structure dans BIBLIOTHEQUE ;
  - trace légère dans ACTION.
- Ils sont balisés (`<!-- noyau:début id -->` … `<!-- noyau:fin -->`).
- Un script (`scripts/build_core.py`) assemble la section « Noyau » de la skill. `validate_all.py` échoue si la skill diverge de sa compilation.
- La cohérence est ainsi **obtenue par construction**, et non par vérification de phrases (`V12_05` §4).
- La skill reste une façade non normative : son noyau est une **copie générée**, déclarée comme telle.

### 3.4 Contenu du noyau (une à deux pages, cible ≤ 2 500 mots)

1. **Rôle et posture** : designer senior ; la première proposition est complète et présentable ; l'honnêteté sur ce qui manque fait partie de la qualité.
2. **Classer** (une ligne) et **prendre le brief** : au plus trois demandes en un seul échange (contenu réel, marque, asset principal ou route autorisée, destination si elle n'est pas évidente) ; puis construire.
3. **Structure** (BIBLIOTHEQUE) :
   - où la surface vit, comment le regard circule, quelle preuve devient tangible, comment la personne agit ;
   - un ou deux axes de tension ;
   - les six signaux de convergence structurelle, comme `MODAL` structurel.
4. **Composition** (SAVOIR) :
   - grammaire positive (intention → tension → foyer → masse → rythme → matière et type → contenu réel → états → résolution → retenue) ;
   - vocabulaire perceptuel avec « diff possible » ;
   - test de singularité ;
   - question de convergence (palette, typographie, assets) ;
   - marqueurs de vague datés `[VEILLE]` (décision 7).
5. **Matériaux, moyens et vérité** :
   - `FABRICATION` et plafond par couche ;
   - carte des moyens ;
   - traitement des assets moyens ;
   - jamais de faux asset en destination réelle ;
   - données d'exemple marquées ;
   - demander ou connecter un outil quand la couche le requiert.
6. **Boucle d'édition** :
   - capture ;
   - table de diagnostic (défaut → geste) ;
   - une seule décision éditée par **retrait, réduction ou transformation** ;
   - seconde capture ;
   - six questions de revue ;
   - repasse « ce qui est resté par défaut ».
7. **Sortie** :
   - en langage produit (ce que j'ai fait, pourquoi, ce qui manque pour la vraie version, la suite) ;
   - trace légère ;
   - trace complète seulement si le run est persistant, partagé ou audité, ou sur demande.
8. **Charger ensuite** : **la** liste de chargement par mode (générée depuis `DIRECTION/START`).

## 4. Inventaire de ce qui est corrigé ou amélioré (traçabilité)

Chaque élément est rattaché à un lot (§5). Rien n'est laissé sans lot ni décision.

| Élément | Source | Lot |
|---|---|---|
| D-01 vocabulaire anti-direction / `MODAL`-`PARTI` | V12_11 | R3 |
| D-02 prise de brief compressée (skill, QUICKSTART, CHANGELOG) | V12_11 | R3 |
| D-03, D-04 absolu 2 : dérives et trois positions sur l'ancre | V12_11 | R7 (décision 6), puis R3 pour les textes |
| D-05 six listes de chargement ; `FIRST-RENDER` absent | V12_11 | R4 (liste unique générée) |
| D-06 BIBLIOTHEQUE exigée mais non chargée | V12_11 | R4 (structure dans le noyau) |
| D-07 marqueurs de vague et carte des moyens hors d'atteinte | V12_11 | R3 (renvois) puis R4 (noyau) |
| D-08 glossaire non mis à jour | V12_11 | R3 puis R6 |
| D-09 checkpoint avant build contre « construire dans tous les cas » | V12_11 | R5b (décision 5) |
| D-10, D-14 sortie visible en jargon ; trois formats de sortie | V12_11 | R4 (décision 4) |
| D-11 circuit d'entrée ; deux README | V12_11 | R6 |
| D-12, D-13 QUICKSTART : table en double, registre, coquille | V12_11 | R3 |
| D-15 instrumentation de lecture dans le run | V12_11 | R5d |
| D-16 deux modèles à trois niveaux (SAVOIR) | V12_11 | R5c |
| D-17 ordre de DIRECTION (posture l.634, récapitulatif l.776) | V12_11 | R5a |
| D-18 outil de budget partiel | V12_11 | R1 |
| DIRECTION : trois couches, dix vues d'entrée, défensif, doublons | V12_05 | R5a |
| ACTION : trace à deux niveaux, craft en gestes, Gate A par profil, 37 statuts | V12_06 | R5b, R9 |
| Skill : frontmatter, chargement dit quatre fois, exemples de fabrication | V12_07 | R4, R6 |
| SAVOIR : outils hors chemin, champs de trace, biais vers la retenue | V12_09 | R4, R5c, R7 (décision 8) |
| BIBLIOTHEQUE : hors chemin, catalogue produit numérique, `PRINT_FIELD`, `GATE` | V12_10 | R4, R5d, R7 (décision 10) |
| Gardes sur des phrases ; harnais qui figent la prose | V12_05 §3.9 | R2 (décision 2) |
| Chantier C : matériaux (critères, familles `[VEILLE]`) | Plan V1.2 | R4 (carte des moyens) et R8 |
| Chantier E / E' : atlas d'ancres annotées | Plan V1.2, addendum | R8 |
| Chantier F : épreuve à l'aveugle, 4 briefs, juges | Plan V1.2 | R10 |
| Réserve 1 et 4 : efficacité `NOT-VERIFIED`, observateur D3 | Clôture | R10 (décision 9) |
| Réserve 2 : run CI hébergé non observé | Clôture | R11 |
| Réserve 3 : ≈ 14 invariants sans cas négatif | Clôture | R11 |
| Réserve 5 : promesse du validateur | Clôture | Maintenue (conception) ; texte unique en R5b |
| Réserve 6 : coût d'un run `DIRECTION` | Clôture | R1 à R5 (mesure), R10 (tokens) |
| Réserve 7 : placeholders dans les champs libres | Clôture | R11 (décision) |
| Réserve 8 : mineurs Q-04 à Q-13, R-16 à R-32, `DIRECTION/DAILY` | Clôture | R11 (tri un par un) |
| Réserve 9 : publication | Clôture | R12 |

## 5. Lots

Chaque lot suit la méthode du §6. **Taille :** S ≈ une unité courte, M ≈ une unité, L ≈ plusieurs unités (à découper).

### Vague I — Mesurer et sécuriser (sans toucher au sens)

**R1 — Outils de mesure** (hors package, S)
- **Périmètre :**
  - budget sur deux périmètres (actuel ; **chemin prescrit**, en suivant les renvois impératifs) ;
  - détecteur de doublons (paragraphes quasi identiques entre fichiers) ;
  - vérificateur d'**atteignabilité** (depuis la liste de chargement, chaque texte dont dépend le boot est-il lu ?) ;
  - compteur d'indicateurs homogène (négations, jetons, champs de trace, « beau ») ;
  - **cartographie des harnais** : pour chacun des 300 cas, la propriété protégée et le texte ancré.
- **Réussite :** mesures B05 reproductibles ; les défauts connus (D-05, D-07, doublons du §2) détectés par les outils eux-mêmes.
- **Arrêt :** si un outil ne retrouve pas un défaut déjà établi à la main, il est corrigé avant usage.

**R2 — Migration des gardes** (package et harnais, M ; **décision 2**)
- **Périmètre :**
  - gardes de propriété dans le validateur : unicité des définitions balisées, égalité des listes de chargement, atteignabilité, vocabulaire unique `MODAL`/`PARTI`, fidélité des résumés (prise de brief, absolus), compilation du noyau ;
  - **table de correspondance** des 300 cas de harnais : propriété conservée (portée par une garde de propriété), rendue obsolète par une décision (déclarée) ou maintenue telle quelle ;
  - protection explicite des **propriétés d'honnêteté** (vérité de scène, frontière de validation, pas de faux asset, plafond).
- **Réussite :** sur B05, les nouvelles gardes sont **rouges** exactement sur les défauts connus ; mutations rouges ; aucun cas de harnais sans ligne dans la table.
- **Arrêt :** une propriété d'honnêteté non couverte par une garde bloque la vague II.

**R3 — Alignements** (package, S)
- **Périmètre :** D-01, D-02, D-07 (renvois), D-08 (glossaire : termes manquants), D-12, D-13, D-16 ; entrée CHANGELOG « Non publié ».
- **Réussite :** gardes R2 correspondantes vertes ; budget non augmenté ; 300/300 (ou table de correspondance à jour).
- **Arrêt :** toute correction qui dépasse l'alignement (changement de sens) sort du lot et va en décision.

### Vague II — Construire le noyau

**R4 — Noyau de fabrication** (package, M ; **décisions 1, 4, 7**)
- **Périmètre :**
  - balisage des blocs normatifs (§3.4) dans leurs fichiers ;
  - `build_core.py` ;
  - réécriture de la skill : frontmatter orienté résultat, noyau compilé, **liste de chargement unique** générée depuis `DIRECTION/START`, sortie en langage produit ;
  - `examples.md` : ajout d'un exemple de fabrication (brief flou → décisions → rendu décrit → ce qui manque).
- **Réussite :** noyau ≤ 2 500 mots ; ≥ 15 outils de fabrication dans le noyau et 25/25 atteignables ; chemin prescrit en baisse d'au moins 25 % dès ce lot ; gardes vertes.
- **Arrêt :** si le noyau dépasse 3 000 mots ou si le chemin prescrit ne baisse pas, retour à l'owner avant R5.

**Point de contrôle P1 — mini-épreuve.** Après R4, une épreuve courte sur le brief B-DLA : C3 (brief vague + B06) ×2, C3r ×1, comparée aux 6 rendus B-DLA, avec le même modèle, les captures avec défilement et un juge neuf. Elle dit si le noyau change le rendu **avant** d'engager les lots lourds.
- Si oui : vague III.
- Si non : diagnostic avant de continuer.

### Vague III — Restructurer les sources (après P1)

**R5 — Restructuration**, un lot par fichier :
- **R5a DIRECTION (M) :**
  - trois couches (noyau de fichier, référence, frontières) ;
  - rôle et posture en tête ;
  - une seule vue d'entrée (`START`), les autres remplacées par des renvois ;
  - doublons supprimés ;
  - récapitulatif intégré au noyau (D-17).
- **R5b ACTION (L, à découper ; décisions 5, 11) :**
  - **trace à deux niveaux** : légère par défaut, `RUN_CARD` complète si le run est persistant, partagé ou audité ;
  - « la première proposition vaut checkpoint », sauf action irréversible ou coûteuse (D-09) ;
  - craft d'ACTION (B1b, Gate C, passe créative) réécrit en gestes et relié au noyau ;
  - Gate A par profil de surface ;
  - une seule description de la boucle ;
  - promesse du validateur en un seul texte.
  - Le schéma `RUN_CARD` reste compatible (voir R9).
- **R5c SAVOIR (M) :**
  - champs de trace sortis vers ACTION ;
  - doublons ;
  - un seul modèle à trois niveaux ;
  - les trois positions sur l'ancre alignées (après décision 6) ;
  - lois : **inchangées tant que R10 n'a pas tranché** (décision 8).
- **R5d BIBLIOTHEQUE (M) :**
  - instrumentation de lecture et contrats de promotion en annexe de maintenance ;
  - `BIBLIOTHEQUE/GATE` fondu dans les gates A et C, ou réduit à une liste de tests perceptifs ;
  - `PRINT_FIELD` relié aux marqueurs de vague.
- **Réussite commune :** chemin prescrit ≤ 14 000 mots à la fin de R5 ; gardes de propriété vertes ; table de correspondance des harnais à jour ; B01 218/218.
- **Arrêt commun :** un lot qui augmente le chemin prescrit, ou qui exige plus de rectifications de harnais que de changements de texte, s'arrête et revient à l'owner.

**R6 — Façades** (S à M)
- **Périmètre :**
  - un seul README (fusion des deux) ;
  - QUICKSTART **humain** (vouvoiement, une activation, un chemin, la table de diagnostic et les six questions par renvoi au noyau) ;
  - GLOSSAIRE complet (vocabulaire de fabrication, statuts regroupés sous « Preuve ») ;
  - READING_MAP réduit au chemin et à l'index des locators ;
  - ORCHESTRATION_MAP fondu dans READING_MAP (« un axe à la fois » passe dans le noyau).
- **Réussite :** aucune façade ne redéfinit un contenu normatif ; une entrée par public (agent : skill ; humain : README).

### Vague IV — Orientation, matériaux, trace machine

**R7 — Décisions d'orientation** (S pour le texte, après décision)
- Ancre graduée par destination (décision 6) :
  - démo ou modèle : ancre générée ou absence déclarée ;
  - produit réel : ancre observée ou fournie.
- Lois de SAVOIR (décision 8) : testées en R10.
- Catalogue élargi aux contextes de l'owner (décision 10) : **après publication**, à partir de runs réels, en `PILOT`.

**R8 — Matériaux et atlas** (M ; chantiers C et E')
- **Périmètre :** carte des moyens consolidée (critères + sources datées `[VEILLE]`) ; atlas d'ancres annotées v1 (liens et descriptions, double colonne visuel / fond, références hors canon occidental), placé en **référence de la skill**, chargée seulement si la décision visuelle est ouverte.
- **Arrêt :** si R10 montre une baisse de diversité, on retire les exemples et on ne garde que les critères (règle déjà décidée dans le plan V1.2).

**R9 — Trace machine** (L ; décision 3)
- **Périmètre :** niveau de trace dans la `RUN_CARD` (léger / complet) ; champ facultatif `fabrication` ; vocabulaire `direction.anti_direction` → `modal`/`parti`, avec alias de compatibilité.
- **Version :** si le schéma reste **rétrocompatible**, V1.2.0 ; sinon V1.3.0.

### Vague V — Preuve, réserves, publication

**R10 — Épreuve à l'aveugle** (L ; chantier F ; décision 9)
- **Briefs :** B-DLA (commerce, Douala), B-LOG (reporté), un produit SaaS, un service public, un portfolio.
- **Conditions :**
  - C1 : brief vague, sans système ;
  - C2 : brief riche et assets, sans système ;
  - C3 : brief vague + V1.2 ;
  - C3r : C3 avec destination réelle ;
  - C4 : V1.1.1.
- **Protocole :** 3 rendus par condition et par brief ; captures avec défilement ; ordre aléatoire ; clé gardée par l'owner.
- **Mesures :**
  - préférence par paires ;
  - diversité (famille de palette, typographie, structure) ;
  - défauts de vérité ;
  - tokens et lignes lues ;
  - plafond déclaré ou non.
- **Décision :**
  - C3 > C1 et C3 > C4, diversité tenue, honnêteté conservée : publication possible ;
  - C3 ≈ C4 : diagnostic, pas de publication.

**R11 — Réserves et mineurs** (M)
- **Périmètre :**
  - tri **un par un** de Q-04, Q-07, Q-08, Q-09, Q-11, Q-12, Q-13, R-16 à R-32 et `DIRECTION/DAILY` : corrigé, rendu obsolète par la refonte (déclaré) ou maintenu (déclaré) ;
  - cas négatifs pour les ≈ 14 invariants ;
  - décision sur les placeholders ;
  - run CI hébergé (dépôt de la distribution GitHub, workflow épinglé, versions et SHA consignés).
- **Réussite :** chaque réserve a une décision écrite.

**R12 — Publication V1.2.0** (S)
- Version relevée ; CHANGELOG ; distributions reproductibles ; archives et SHA-256 ; dossier de clôture V1.2 ; réserves restantes déclarées.

### Dépendances

```
R1 → R2 → R3 → R4 → P1 ─┬→ R5a → R5b → R5c → R5d → R6 → R9
                        └→ R7 (texte) , R8
R6 + R8 + R9 → R10 → R11 → R12
```

R11 (tri des mineurs) peut commencer en parallèle dès R2, pour les mineurs que la refonte ne rend pas obsolètes.

**Signalement de taille (style de l'owner) :** le programme compte **douze lots**, dont trois grands (R5b, R9, R10). Il est surdimensionné pour être mené d'un bloc. Le point de contrôle P1 permet de s'arrêter après la vague II si le noyau ne change pas le rendu.

## 6. Méthode

1. **PATCH-DECISION par lot** :
   - décision écrite validée par l'owner ;
   - textes exacts dans un script exécutable (`audit/tools/V12R_<lot>.py`, modèle `V12_Patch_ABD.py`) ;
   - gardes **rouges avant, vertes après**, avec mutation rouge.
2. **Non-régression à chaque lot** :
   - `validate_all` ;
   - gardes de propriété ;
   - table de correspondance des harnais (300 cas : conservé / obsolète déclaré) ;
   - R, R03, 13.01, 13.02 ;
   - B01 218/218.
3. **Budget mesuré à chaque lot** sur le chemin prescrit (R1). Aucun lot n'augmente le chemin sans décision.
4. **Aucune correction non décidée** (règle 3). Un défaut découvert va au registre D-xx avec son lot.
5. **Rapport allégé par lot** : diff, résultats, écarts déclarés, certain / probable / hypothétique.
6. **Charte de rédaction** appliquée à tout texte réécrit :
   - **positif d'abord** : l'action, puis au plus une limite ;
   - **un concept, un lieu** : ailleurs, un renvoi d'une ligne ;
   - **registres** : « tu » dans les sources (adressées à l'agent), « vous » dans les façades humaines ;
   - **vocabulaire unique** : `MODAL`/`PARTI`, trace légère / complète, noms de routes inchangés ;
   - **ponctuation** : pas de tiret cadratin comme séparateur de champs dans les formats de sortie ;
   - **test anti-slop procédural** sur nos propres lignes : « qu'est-ce qui change si cette ligne est absente ? » ; si rien, elle sort.
7. **Honnêteté protégée** : aucun lot ne réduit la vérité de scène, la frontière de validation, le plafond ni l'interdiction du faux asset. Des gardes dédiées le vérifient (R2).
8. **Branches** : le travail continue sur la branche de session et `v1.2/patch-decision-abd`. Une branche par lot demande ton accord explicite (règle Git de la session). L'envoi d'étiquettes est refusé par le dépôt distant : les points de contrôle sont des commits nommés dans les rapports.
9. **Auto-comparaison déclarée** : toute revue faite par le même modèle est déclarée comme telle. R10 cherche au moins un regard extérieur.

## 7. Risques et parades

| Risque | Signal | Parade |
|---|---|---|
| Coût des harnais (prose figée) | Plus de rectifications que de changements de texte | R2 avant tout ; table de correspondance ; arrêt commun de R5 |
| Perte de l'honnêteté mesurée | Données d'exemple non marquées en P1 ou R10 | Gardes d'honnêteté (R2) ; critère bloquant en R10 |
| Style maison créé par le noyau (mêmes gestes → mêmes rendus) | Diversité en baisse en P1 ou R10 | Mesure de diversité ; gestes formulés en décisions, pas en styles ; retrait des exemples (R8) |
| Noyau qui gonfle | > 3 000 mots | Arrêt de R4 ; tout ajout financé par une coupe |
| Biais d'auto-comparaison | Mêmes conclusions que l'auteur | Juge neuf en P1 ; regard extérieur en R10 ; déclaration |
| Surdimensionnement | Lots qui débordent | Découpage de R5b et R9 ; P1 comme porte de sortie |
| Temps et usage de l'owner | Décisions en attente | Décisions groupées (§8) ; défauts par recommandation écrite |

## 8. Décisions attendues de l'owner

| # | Décision | Options | Recommandation |
|---|---|---|---|
| 1 | Forme du noyau | (a) blocs normatifs balisés dans les sources, **compilés** dans la skill ; (b) noyau écrit à la main dans la skill ; (c) nouvelle section normative `DIRECTION/NOYAU` recopiée dans la skill | **(a)** : cohérence par construction, aucune copie manuelle |
| 2 | Migration des gardes | (a) gardes de propriété + table de correspondance des 300 cas ; (b) rectification cas par cas | **(a)** : sinon la refonte coûte plus en harnais qu'en texte |
| 3 | Version et schéma | (a) V1.2.0 si `RUN_CARD` rétrocompatible, sinon V1.3.0 ; (b) tout en V2.0.0 | **(a)** |
| 4 | Sortie visible | (a) langage produit par défaut, trace sur demande ; (b) statu quo | **(a)** |
| 5 | Checkpoint | (a) la première proposition vaut checkpoint, sauf action irréversible ou coûteuse ; (b) checkpoint avant build en session interactive | **(a)** |
| 6 | Ancre | (a) graduée par destination ; (b) absolu 2 bloquant pour toute surface identitaire | **(a)** |
| 7 | Marqueurs de vague | (a) dans le noyau sous `[VEILLE]` daté, avec LCF-46 rectifiée ; (b) renvoi seulement | **(a)** : c'est au moment de nommer le modal qu'ils servent |
| 8 | Lois de SAVOIR (retenue) | (a) tester en R10 avant de changer ; (b) changer maintenant | **(a)** |
| 9 | Juges de R10 | (a) personnes extérieures (critères D3) ; (b) toi et des juges modèles d'autres familles, déclarés non indépendants ; (c) les deux | **(c)** : publication avec réserve si aucun juge D3 |
| 10 | Catalogue élargi | (a) après publication, depuis des runs réels ; (b) dès maintenant | **(a)** : pas de route inventée sans usage |
| 11 | Trace par défaut | (a) légère sauf run persistant, partagé ou audité ; (b) `RUN_CARD` complète en `DIRECTION` | **(a)** |

Les décisions 1, 2, 4 et 7 conditionnent R2 à R4. Les autres peuvent attendre leur lot.

## 9. Lecture

- **Certain :** l'inventaire du §4 couvre le registre D-01 à D-18, les pistes des six lectures, les chantiers C, E, F et les neuf réserves d'audit ; les états initiaux du §2 sont ceux mesurés en `V12_05` à `V12_11`.
- **Probable :** l'ordre des vagues ; l'effet d'économie du noyau et de la trace légère.
- **Hypothétique :** les cibles chiffrées (−40 %, ≤ 1,3 × les tokens) et l'effet sur la qualité. P1 et R10 les éprouvent.
- **Limite :** plan conçu par le même modèle que l'auteur des lectures et des patchs ; aucune revue extérieure.
