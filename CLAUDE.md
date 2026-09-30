# CLAUDE.md — Design Governance (dépôt de travail)

Ce fichier est lu automatiquement par Claude Code. Il donne le contexte, les règles de méthode, l'état actuel et la prochaine étape. Lis-le en entier avant toute action.

## 0. Première session : initialisation (à faire une seule fois)

Le dépôt peut arriver sous forme de deux fichiers : ce `CLAUDE.md` et une archive `DG_kit_ClaudeCode.zip`. Si l'arborescence décrite au §3 n'existe pas encore :

1. Décompresser l'archive **à la racine du dépôt** : son contenu doit se retrouver directement sous la racine (`package/`, `audit/`, …), sans dossier intermédiaire. Le `CLAUDE.md` inclus est identique à celui-ci.
2. Vérifier l'intégrité du kit : `sha256sum -c KIT_SHA256SUMS.txt` (tous `OK`).
3. Vérifier la référence B01 : `cd reference/B01_transfert && sha256sum -c SHA256SUMS.txt` → **218/218**.
4. Vérifier le système : `cd package && python3 -B scripts/validate_all.py` → `FULL VALIDATION PASSED`.
5. Supprimer l'archive du dépôt, commiter (« Import du kit Design Governance V1.1.1 »), étiqueter `v1.1.1-import`, pousser.
6. Rendre compte à l'owner en quelques lignes : résultats des étapes 2 à 4, et rien d'autre.

Ne rien modifier dans `package/` pendant l'initialisation.

## 1. Le projet

**Design Governance** est un système de gouvernance de design pour agents IA. Il fait produire à un agent un travail de design dirigé, prouvé et tracé, au lieu d'un rendu générique. Il est écrit en français.
- Cinq sources normatives : `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md`, `CHANGELOG.md` (dans `package/V1/official/`).
- Des façades dérivées : QUICKSTART, README, GLOSSAIRE, READING_MAP, ORCHESTRATION_MAP, la skill `skills/design-governance-practice/`.
- Une projection machine : `schemas/run_card.schema.json`, validée par `scripts/validate_run_card.py`, et des validateurs de package et de façades.

**Owner :** Junior (Kamel), designer et développeur, basé à Douala. Il décide de chaque arbitrage.

## 2. État actuel (26-09-2026)

- **Version courante : V1.1.1**, dans `package/`. Non publiée.
- **Audit DG-AUDIT-001 : clos**, statut final décidé par l'owner : **`AUDIT-PASS-WITH-RESERVATION`**. Dossier : `audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md`.
- **Contrôles de V1.1.1 :** 22 harnais 300/300, témoins 40/40 ; harnais R 31/31 ; harnais R03 18/18 ; vérifications 13.01 26/26 ; épreuves déterministes 13.02 38/38.
- **Réserves ouvertes** (détail dans le dossier de clôture, §3) :
  - efficacité sur des runs réels `NOT-VERIFIED` ;
  - run CI hébergé non observé ;
  - environ 14 invariants sans cas négatif ;
  - 16 limites déclarées ;
  - promesse du validateur ;
  - coût de lecture (environ 1 300 lignes pour un run `DIRECTION`) ;
  - placeholders dans les champs libres ;
  - mineurs transmis ;
  - publication.
- **Épreuve de référence B-DLA (unité V1.2-00) : close sans juge humain**, orientation déclarée : `audit/reports/V12_00_EPREUVE_REFERENCE_B-DLA.md`.
- **Porte G1 franchie** (26-09-2026) : `audit/reports/V12_01_DECISIONS_G1.md`.
- **PATCH-DECISION A, B, D appliquée sur B05 (G3)** : `audit/reports/V12_03_G3_APPLICATION_B05.md`. Sur la branche `v1.2/patch-decision-abd` (et la branche de session), `package/` est la **candidate V1.2** (version affichée V1.1.1, CHANGELOG « Non publié ») ; `main` reste V1.1.1. Contrôles B05 : 300/300, témoins 40/40, R 30/30, R03 18/18, 13.02 38/38, 46 conditions de façade. Instantané de référence : `audit/snapshots/V12_Instantane_harnais_B05_G3.json`.
- **Lot 2 (G, H, I, D') appliqué sur B05** : `audit/reports/V12_04_LOT2_G_H_I_D.md` ; 50 conditions de façade ; instantané `V12_Instantane_harnais_B05_Lot2.json` ; budget 9 591 mots.
- **Lectures structurelles (auto-comparaison), complètes** : DIRECTION, ACTION, skill + READING_MAP, façades, SAVOIR, BIBLIOTHEQUE + CHANGELOG : `audit/reports/V12_05` à `V12_10` ; **synthèse, registre des défauts D-01 à D-18 et proposition de chantier « structure et budget » (phases 0 à 4) : `V12_11_SYNTHESE_LECTURES.md`**. Diagnostic : accrétion par audit, architecture pensée à partir de la preuve, gardes sur des phrases ; levier probable : skill-noyau de fabrication, liste de chargement unique, gardes de propriété. Défauts signalés non corrigés : vocabulaire anti-direction / `MODAL`-`PARTI`, prise de brief compressée (corrigée en R3), dérive de l'absolu 2 dans la skill, glossaire non mis à jour, six listes de chargement `DIRECTION` divergentes. Chemin prescrit réel d'un run `DIRECTION` : ≈ 23 600 mots (≈ 1 650 lignes) ; 7 outils de fabrication sur 25 sont sur ce chemin.
- **Plan de refonte proposé** (27-09-2026) : `plans/Plan_V1.2_Refonte.md` — architecture cible (noyau de run compilé, une chose un lieu, gardes de propriété), lots R1 à R12 en cinq vagues, point de contrôle P1 (mini-épreuve après le noyau), 11 décisions de l'owner (§8). Il remplace le séquencement du plan V1.2 et de l'addendum, dont il reprend les chantiers.
- **Refonte, décisions 1, 2, 4 et 7 prises** (27-09-2026, `audit/reports/V12R_00_DECISIONS_REFONTE.md`) : noyau compilé depuis les sources, gardes de propriété + table de correspondance, sortie en langage produit, marqueurs de vague dans le noyau.
- **R1 fait** (`V12R_01_OUTILS_MESURE.md`) : `audit/tools/V12R_Mesures.py` (budget ACTUEL/TABLE/LETTRE : 9 591 / 16 339 / 23 891 mots ; atteignabilité 3 / 7 / 10 outils sur 25 ; 863 négations ; 79 amas de doublons ; 5 listes de chargement distinctes sur 6) et `V12R_Carto_harnais.py` (389 cas : 233 structurels, 156 sensibles à la prose dont 58 via les LCF).
- **R2 appliqué** (`V12R_02_R2_GARDES_PROPRIETE.md`, méthode M1–M4 validée) : `scripts/validate_structure.py` (8 concepts d'honnêteté balisés `<!-- concept:HON-0x -->`, uniques, à leur lieu propriétaire ; `read_route` retire les balises) ; table `audit/data/V12R/V12R_Correspondance_harnais.csv` (389 cas) ; **suivi de refonte `audit/tools/V12R_Suivi.py`** : 389/389, cliquets = référence B05, validate_all vert, 13.01 6/6 et 5/5, 13.02 38/38.
- **R3 appliqué** (`V12R_03_R3_ALIGNEMENTS.md`) : D-01 (vocabulaire `MODAL`/`PARTI` unique), D-02 (prise de brief fidèle, condition canonique reformulée « destination si elle est incertaine »), D-07 (renvois vers marqueurs et carte, `SAVOIR/TOOLS`), D-08 (11 termes au glossaire), D-12, D-13 ; gardes de propriété associées ; R-17 et R-21 migrés (LCF-24, LCF-28) ; suivi vert, chemin prescrit 23 849 mots. D-16 reporté en R5c.
- **R4 appliqué** (`V12R_04_R4_NOYAU.md`) : noyau de fabrication (2 843 mots, 29 blocs balisés dans les sources, compilé dans la skill par `scripts/build_core.py`) ; `DIRECTION/DAILY` → `DIRECTION/CHARGE`, seule liste de chargement ; réponse visible en langage produit (`ACTION/HANDOFF`) ; chemin prescrit **13 537 mots (−43 %)**, **24/25 outils de fabrication sur le chemin**, 1 liste de chargement ; 7 LCF rectifiées, 15 cas migrés ; suivi vert.
- **P1 fait** (`V12R_05_P1_MINI_EPREUVE.md`, pièces `plans/epreuve_reference/B-DLA-P1/`) : 3 rendus V1.2 (C3 ×2, C3r ×1), 2 juges neufs à l'aveugle avec brief riche intégral. C3 bat C1 8/8 ; C3 contre C4 5-3 (juges en désaccord) ; C2 gagne 12/12 (les intrants restent le premier levier) ; 0 fait inventé ; sortie de la palette crème 3/3 mais convergence Archivo 3/3 et trame identique 9/9 ; coût ≈ 1,7 × C1 ; C3r faible (emplacements vides). Défauts D-20 à D-23 signalés.
- **R5b-1 appliqué** (`V12R_06_R5b1_TRACE_CHECKPOINT.md`) : décisions 5 (a) et 11 (a), D-20 (exemple marqué) et D-22 (test de trame) ; trace légère par défaut (`ACTION/HANDOFF`, `TRA-01`), première proposition = checkpoint (`CHK-01`), `CNT-01`, `TRM-01` ; Gate B, `RUN_CARD` et `CLOSE-PACKAGE` en trace complète seulement ; chemin prescrit **11 740 mots** (trace complète 16 351) ; noyau 3 217 mots (au-dessus de 3 000, écart déclaré) ; 9/9 mutations rouges ; suivi vert sans migration.
- **R5b-2 appliqué** (`V12R_07_R5b2_ACTION.md`) : Gate A par profil de surface (`GTA-01`), Gate C avec « geste si absent » et contrôle de craft sans verdict en trace légère, boucle unique (`DIRECTION/DOUBLE-LOOP`), promesse du validateur en un seul lieu (`VAL-01`), CHG-09 ; chemin 12 076 mots ; 8/8 mutations rouges ; suivi vert sans migration. **Consigne de l'owner : la qualité du résultat prime sur le nombre de mots** (pas de plafond de coupe du noyau ; on ne retire que doublons et texte sans effet sur le rendu).
- **R5a appliqué** (`V12R_08_R5a_DIRECTION.md`) : rôle (`ROL-01`), posture et récapitulatif de protection en tête de DIRECTION (ORD-01) ; entrée unique ; doublons retirés ; D-17 et D-19 fermés ; 5/5 mutations rouges ; suivi vert sans migration.
- **R8a appliqué** (`V12R_09_R8a_CONVERGENCE_TYPO.md`) : question de convergence étendue à la police de titre (deux voix comparées sur le vrai titre) ; signal de veille P1 (Archivo sur blanc neutre, à confirmer) ; suivi vert.
- **R5c appliqué, hors ancre** (`V12R_10_R5c_SAVOIR.md`) : un seul modèle de niveaux (D-16), boucle et one-shot de SAVOIR en renvoi ; doublons 145 ; suivi vert.
- **R5d appliqué** (`V12R_11_R5d_BIBLIOTHEQUE.md`) : boucle et one-shot de BIBLIOTHEQUE en renvoi (exemptions retirées) ; F22 : tests perceptifs `PRC-01` appelés depuis Gate C ; suivi vert.
- **R6a appliqué** (`V12R_12_R6a_FACADES.md`) : boucle du README en renvoi (la garde « boucle unique » n'a plus d'exemption provisoire), 5 termes au glossaire ; suivi vert ; doublons 144.
- **R11a appliqué** (`V12R_13_R11a_CORRECTIFS.md`) : résidu `DAILY` retiré de `DIRECTION/START` ; ancre de mesure F13 rectifiée (24/25, F22 atteignable sous condition depuis Gate C) ; carte des moyens v0 alignée sur D-20. Mesures : chemin 12 187 mots, noyau 3 302. **Plan consolidé archivé** (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`) : provenance historique ; arbitrages intégrés au plan de reprise, avec les révisions de `V12R_14` addendum 2.
- **Arbitrages initiaux décidés** (`V12R_14_DECISIONS_ARBITRAGES.md`, 27-09-2026 ; calendrier de l'atlas et volume de R10 révisés par l'addendum 2 du 30-09) : toutes les options recommandées. Décision 6 : ancre graduée ; décision 3 : schéma inchangé → V1.2.0, R9 reporté ; atlas intégré en R8b (révision de G1) ; décision 9 : juges humains + modèles ; décision 8 : lois inchangées ; décision 10 : catalogue après publication ; R10 par paliers (18 productions) ; R11 ciblé ; ordre « le rendu d'abord ».
- **Pilotage synchronisé** (30-09-2026, `V12R_14` addendum 2) : amendement du 28-09 intégré (R8b sans atlas, avec enseignements transférables ; R8c recadré sur les gestes insuffisants ; R7, R11 et R6b précisés ; README Local du build inclus en R6b) ; **consolider avant d'évaluer** : porte **P2 « prêt pour l'évaluation »**, inventaire unique des défauts, relecture de parcours ; **R10 progressif** (6 cas exploratoires, dont 4 à 6 productions neuves selon le réemploi vérifié de références C1/C4 ; C3 produit sur la candidate consolidée ; puis 18 si justifié) ; observation novice distincte ; anciens plafonds de mots historiques ; référence G1 rectifiée (décision 2).
- **Pilotage corrigé et inventaire créé** (30-09-2026) : note de consolidation préparatoire intégrée (patch appliqué sur `3966ad5`, empreintes conformes ; archivée dans `plans/propositions/`) ; **inventaire unique** : `audit/data/V12R/V12R_Inventaire_P2.md` (D-01 à D-23, Q, R-16 à R-32, PIL-01 à PIL-04, **PKG-01** : « un seul traitement / une seule famille » encore universels dans le package, bloquant P2, à traiter en R8b et R8c).
- **R8b appliqué** (`V12R_15_R8b_MOYENS.md`) : carte des moyens consolidée (vérification par ressource, Fontshare corrigé, performance mesurée) ; **PKG-01 fermé** (traitement et famille d'icônes choisis selon la thèse) ; enseignement A08 ajouté (`EXD-01`, données d'exemple cohérentes) ; 6/6 mutations rouges ; suivi vert ; 24/25 ; chemin 12 430 mots.
- **R8b-2 appliqué** (`V12R_16_R8b2_RACCORDS.md`) : garde PKG-01 remplacée par **UNI-01** (portée rectifiée en R8c-2 : garde bornée) ; Fontshare FFL ou OFL ; erratum de R8b (contraste d'échelle : geste existant en Gate C, C2) ; inventaire à jour ; mesures après R8b-2 : chemin 12 430, noyau 3 505.
- **R8c appliqué** (`V12R_17` diagnostic, `V12R_18`) : équilibre d'un titre (`TIT-01`) et texte sur image (`TXI-01`) dans le noyau ; question 5 de la boucle étendue à l'ensemble ; récupération après erreur (`RCV-01`, `SAVOIR/STATE`, appelée depuis Gate C) ; icônes et contraste d'échelle déjà couverts ; 5/5 mutations rouges ; suivi vert ; chemin 12 629, noyau 3 695.
- **R8c-2 appliqué** (`V12R_19_R8c2_RACCORDS.md`) : **UNI-01 bornée et déclarée** (formulations retirées et impératifs universels explicites ; contre-exemples de l'owner testés) ; titre : corrections sur défaut observé, composition voulue conservée ; récupération : focus selon le moment, issue claire si la réussite est impossible ; plan de reprise à jour ; chemin 12 682, noyau 3 748.
- **R7 appliqué** (`V12R_20` diagnostic rectifié, `V12R_21`) : **ancre graduée** dans l'absolu 2 (`ANC-01`, compilée dans le noyau) — explorer sans ancre avec limite déclarée ; accepter avec une ancre, observée ou fournie pour un produit réel (le projet peut la fournir) ; sans ancre, la direction reste `EXPLORATORY` ; `FAIL-ASSUMED` réservé à un échec connu, jamais à une ancre absente (raccord R7-2, `V12R_24`) ; limite déclarée du validateur (destination hors schéma) ; D-03 et D-04 fermés (SAVOIR, déclencheur, récapitulatif, façades et README Local du build) ; 6/6 mutations rouges ; suivi vert ; chemin 12 795, noyau 3 861.
- **R11 ciblé appliqué** (`V12R_22` diagnostic, `V12R_23`) : Q-04 à Q-13 et R-16 à R-32 instruits sur leurs traces ; bloquants P2 fermés : contrôle machine nommé par mode (Q-04, VAL-01), arrêt one-shot relié à B1b (Q-09), exclusion LITE/ITER conditionnelle comme dans START (R-16, décision de l'owner : `risk.level` = risque touché), ancre `transformed` exigée en DIRECTION (R-21) ; 13 mineurs alignés ; triade définie ; locators nommés dans le validateur (garde LOC-01) ; **six cas négatifs** (N1 à N5, 82 cas unitaires) ; trois cas de harnais migrés (M1 : R-15, R3-10, R3-17) ; 41/41 mutations rouges ; Q-13 et R-25b affectés à R6b ; chemin 12 839, noyau 3 861.
- **R7-2 appliqué** (`V12R_24`, erratum de R7 après revue) : `ANC-01` et le paragraphe final de l'absolu 2 disent qu'une ancre absente laisse la direction `EXPLORATORY` ; `FAIL-ASSUMED` exige un échec connu (`ACTION/OVERRIDE`) ; CHANGELOG aligné ; 4/4 mutations rouges ; chemin 12 867, noyau 3 889 (+28 ; mesure rectifiée).
- **R7-3 appliqué** (`V12R_26`) : garde « ancre absente → `FAIL-ASSUMED` » bornée à son contexte (refuse les trois anciens raccourcis, accepte une diffusion limitée d'un échec connu) ; mesure du noyau de R7-2 rectifiée (3 861 → 3 889).
- **R6b-1 appliqué** (`V12R_25` diagnostic, `V12R_27`) : **entrée humaine unique** en quatre questions (section « Commencer » de `package/README.md`, vouvoiement, aucun mode à choisir), reprise par le README Local **généré par le build** depuis la même source ; QUICKSTART = guide opérateur à un parcours commun ; README officiel = pointeur ; une seule constitution minimale exacte (D-24) ; gardes ENT-01, CST-01 ; LCF-04, -05, -10 rectifiées vers le QUICKSTART ; 4 cas migrés (C5) ; 16/16 mutations rouges ; D-11 fermé ; racine du dépôt : lien « Commencer ».
- **R6b-2 appliqué** (`V12R_28`) : READING_MAP porte les combinaisons par résultat (reprises d'ORCHESTRATION_MAP, devenu pointeur de compatibilité) ; LCF-03, LCF-07 et CHG-06 lisent READING_MAP (rectification déclarée) ; garde MAP-01 ; 2 cas migrés ; 5/5 mutations rouges ; chemin 12 865, noyau 3 888, doublons 145.
- **Restes R5 appliqués** (`V12R_29` diagnostic avec maquette, `V12R_30`) : copies du handoff en renvoi ; **D-15 fermé** (catégories de lecture et contrat de promotion hors du préambule de BIBLIOTHEQUE, déclaration de lecture limitée aux runs instrumentés ou audités, garde MNT-01) ; alternative située répartie (ALT-01 : DIRECTION déclenche, SAVOIR leviers, ACTION matérialise, trace graduée, compare) ; signal PRINT_FIELD dans le noyau ; 13/13 mutations rouges ; aucune migration ; préambule −25 %, doublons 134, chemin 12 937, noyau 3 923.
- **Relecture de parcours faite** (`V12R_31`, quatre profils, sans production) : 3 bloquants P2 relevés — G1 « valider » au checkpoint sans sens défini (passage à l'acceptation), G2 moment des demandes de brief (décision de l'owner), G4 sortie en trace légère non dite pour LITE, ITER, STANDARD et SYSTÈME et reprise ITER ; 3 mineurs (F1 à F3) ; lot « R11b parcours » proposé.
- **R11b parcours appliqué** (`V12R_32`, décision (a)) : valider n'est pas accepter (l'acceptation pour un produit réel se demande et passe en trace complète) ; humain présent, les demandes de brief précèdent le build ; « Trace légère : la proposition » dans chaque route `RUN-*` ; ITER reprend depuis la ligne de thèse ; réponse visible avec l'alternative écartée ; EXTERNAL-START avant CREATIVE-BOOT ; 12/12 mutations rouges ; aucune migration ; ancre de mesure rectifiée ; chemin 13 105, noyau 4 012, doublons 134.
- **Porte P2 examinée** (`V12R_33`) : seuil tenu (aucun bloquant ouvert, parcours vérifiés, limites écrites) ; cinq axes tenus (66/66 routes résolues, suivi vert, doublons 134, chemin 13 105) ; **franchie** par décision de l'owner (30-09-2026) ; **revue postérieure** (`V12R_33` §5) : un bloquant manqué (PAR-G4b, clôture des routes `RUN-*` sans condition de trace) ; **R11c appliqué** (`V12R_34`) : « En trace complète, » dans les clôtures de RUN-LITE, ITER, STANDARD et SYSTEM ; garde G4b ; 5/5 mutations rouges ; suivi vert ; doublons 139 (amas formel déclaré) ; **P2 conclue**.
- **Protocole du palier exploratoire de R10 écrit** (`plans/Protocole_R10_Palier_exploratoire.md`, aucune production) : 6 cas (B-DLA et B-SAAS × C1, C3, C4) ; réemploi des références B-DLA C1/C4 non recommandé (modèle non consigné) ; critères écrits avant de produire (problèmes évidents P-1 à P-6, passage à 18, coût C3 ≤ C4 et visé ≤ 2 × C1, désaccords entre juges) ; brief riche B-SAAS fictif proposé pour les juges. **Consigne « pas de run » non levée** : décisions de l'owner attendues (§9 du protocole).
- **Chantier en cours : consolidation V1.2**, pilotée par `plans/Plan_V1.2_Suite_Reprise.md` ; architecture dans `plans/Plan_V1.2_Refonte.md`, décisions dans `V12R_14`. Objectif : un premier rendu composé, spécifique et soigné, avec une entrée humaine claire et un effort maîtrisé ; efficacité encore à évaluer. R8b mobilise les moyens et les enseignements transférables ; R8c précise les gestes utiles ; aucun atlas de créations obligatoire.

## 3. Arborescence

| Chemin | Contenu | Statut |
|---|---|---|
| `package/` | Système V1.1.1 (sources, schémas, scripts, skill) | Version courante ; ne se modifie que par PATCH-DECISION |
| `reference/B01_transfert/` | Baseline B01 = V1.0.0, avec `SHA256SUMS.txt` (218 fichiers) | **Lecture seule, toujours** |
| `reference/B02/` | Candidate V1.0.1 gelée, jamais utilisée | Gelée |
| `history/` | Bundles git : `B03_V1.1.0.bundle`, `B04_V1.1.1.bundle` (toutes les étiquettes : `12.00`… `12.06-outils-v1.1.0`, `R.02-*`, `R.03-patch`, `R.03b-seconde-passe`) | Archive ; `git clone history/B04_V1.1.1.bundle /tmp/b04` pour consulter |
| `audit/tools/` | 22 harnais `*_harnais_non_regression.py`, harnais R et R03, suivi, patchs R.01 et R.03, vérifications 13.01, épreuves 13.02 | Outils ; ne changent que par rectification déclarée |
| `audit/snapshots/` | Instantanés des harnais (B01, B03 12-00 à 12-06, B04 R.02 et R.03) | Référence de comparaison |
| `audit/reports/` | Tous les rapports d'audit, le plan maître, le dossier de clôture | Historique |
| `audit/data/`, `audit/diffs/`, `audit/logs/`, `audit/sources/` | Registres CSV, diffs, journaux et captures, protocole maître d'audit v2.0 | Historique |
| `releases/` | Zips GitHub/Local et fichier compilé de V1.1.0 et V1.1.1 | Livrables figés |
| `plans/` | Plan V1.2 | Travail en cours |

## 4. Règles de méthode (non négociables)

1. **B01 en lecture seule.** Vérifier `SHA256SUMS.txt` (218/218) à chaque unité de travail. Ne jamais écrire dans `reference/`.
2. **Toute modification de `package/` passe par une PATCH-DECISION** :
   - une décision écrite, validée par l'owner ;
   - les textes exacts sous forme exécutable (modèle : `audit/tools/DG_AUDIT_001_Patch_R01.py`) ;
   - des gardes **rouges avant, vertes après** : conditions de façade LCF dans `scripts/validate_reading_map.py` avec mutation rouge, ou cas unitaires.
3. **Aucune correction non décidée n'entre dans un patch.** Un défaut découvert en cours de route est signalé, pas corrigé en silence.
4. **Aucun changement de méthode silencieux.** Tout écart est déclaré dans le rapport de l'unité.
5. **Les harnais ne changent que par rectification déclarée**, nommée et justifiée dans le rapport.
6. **Tous les tests s'exécutent sur des copies.** Les outils le font déjà ; ne pas lancer de build destructif dans `package/` sans raison.
7. **Aucun verdict global d'efficacité.** Pas de clôture FULL d'efficacité sans observateur indépendant (critères D3 : relation externe ou collaborateur non impliqué, conflit déclaré). Une revue par sous-agent du même auteur est une auto-comparaison, déclarée comme telle.
8. **Non-régression à chaque unité** : 300/300, témoins 40/40, harnais R et R03 verts, `validate_all` vert.
9. **Distinguer certain, probable, hypothétique** dans chaque rapport.
10. **Garder le plan maître et les rapports à jour** (`audit/reports/`), pour que le travail puisse reprendre ailleurs.

## 5. Commandes

Depuis `audit/tools/` :

```bash
# Suivi des 22 harnais (environ 5 à 10 minutes), comparé au dernier instantané
python3 DG_AUDIT_001_Suivi_harnais.py ../../package --compare ../snapshots/DG_AUDIT_001_Instantane_harnais_B04_R03.json  # sur B05 : V12_Instantane_harnais_B05_Lot2.json [--out ../snapshots/<nouvel_instantane>.json]

# Suivi de refonte (englobe les 22 harnais, R et R03 ; table de correspondance ; cliquets ; validate_all sur copie)
python3 V12R_Suivi.py ../../package [--out ../snapshots/<instantane>.json]   # attendu : SUIVI VERT
python3 V12R_Mesures.py ../../package      # budget, atteignabilité, indicateurs, doublons, listes de chargement

# Harnais du retour
python3 R_harnais_non_regression.py ../../package      # attendu : Témoin 1/1 ; cas R 30/30
python3 R03_harnais_non_regression.py ../../package    # attendu : Cas R03 18/18

# Vérifications 13.01 et épreuves 13.02
python3 DG_AUDIT_001_Verifications_13-01.py texte ../../package
python3 DG_AUDIT_001_Verifications_13-01.py non-regression ../../reference/B01_transfert/02_Sources_B01/package ../../package
python3 DG_AUDIT_001_Epreuves_13-02.py ../../package
```

Depuis `package/` :

```bash
python3 -B scripts/validate_all.py        # validation complète, build des deux distributions
python3 -B scripts/validate_reading_map.py  # 42 conditions (V1.1.1) ; 50 sur B05
python3 -B scripts/validate_structure.py   # gardes de propriété : concepts, renvois, vocabulaire, noyau compilé, chargement unique
python3 -B scripts/build_core.py [--check]  # compile le noyau de fabrication dans la skill (ne jamais éditer la section compilée à la main)
python3 scripts/read_route.py ACTION/RUN_CARD  # lire une route
```

**Limite connue :** `DG_AUDIT_001_Verifications_13-01.py distributions` cherche `python3.10` et `python3.13`. S'ils sont absents de l'environnement, ces lignes échouent « indisponible » : ce n'est pas une régression.

## 6. Prochaine étape

1. ~~Porte G1 du plan V1.2~~ : franchie le 26-09-2026 (`audit/reports/V12_01_DECISIONS_G1.md`).
2. ~~B05, lot 1 (A, B, D), addendum, lot 2 (G, H, I, D')~~ : faits (`V12_02` à `V12_04`). Lectures `V12_05` à `V12_11` faites. Mini-épreuve **reportée par l'owner** (27-09-2026). **Refonte (`plans/Plan_V1.2_Refonte.md`) : décisions 1, 2, 4, 7 prises ; R1, R2, R3 et R4 faits. P1 fait (orientation positive). R5b-1, R5b-2, R5a, R8a, R5c (hors ancre), R5d, R6a et R11a faits. Arbitrages décidés (`V12R_14`). Inventaire créé ; R8b, R8c, R7 (et raccords R7-2, R7-3), R11 ciblé, R6b élargi (R6b-1, R6b-2), restes R5, relecture de parcours et raccords R11b faits ; porte P2 franchie et conclue après R11c ; protocole du palier exploratoire écrit. Prochaine : décisions de l'owner sur le protocole (levée de « pas de run ») → R10 progressif → R11 final → R12 — voir `plans/Plan_V1.2_Suite_Reprise.md`**, puis G4.
**Plan de reprise (à lire en premier pour continuer) : `plans/Plan_V1.2_Suite_Reprise.md`** — consignes en vigueur (pas de run ni d'épreuve dans cette phase ; qualité avant nombre de mots), recette d'une unité, lots restants avec périmètre, gardes, réussite et arrêt, porte P2 et R10 progressif.
3. Suivre le séquencement du plan : G2 (gardes rouges puis vertes) → G3 (non-régression, charge mesurée et justifiée) → G4 (épreuve à l'aveugle avec juges extérieurs) → publication V1.2.0.

Travail par branche : une branche par unité (`v1.2/patch-decision-abd`, …) ; étiquettes aux points de contrôle ; rapport de l'unité dans `audit/reports/`.

## 7. Style de travail attendu par l'owner

- Répondre **en français**, clair et structuré, sans remplissage. Profondeur utile, minimum de bruit.
- Montrer le pourquoi et le comment ; hiérarchiser ; distinguer certain, probable, hypothétique, à vérifier.
- Progresser étape par étape, en continuité avec les décisions déjà validées.
- Donner à chaque unité un périmètre, une priorité, des critères de réussite et des critères d'arrêt.
- Rapports « allégés » : diff, résultats, écarts déclarés.
- Adapter l'effort : une tâche simple reste rapide ; signaler une tâche surdimensionnée.
- Économiser les limites d'usage : éviter les relectures intégrales inutiles et les agents superflus.
