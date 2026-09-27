# V1.2 — Unité 11 — Synthèse des lectures intégrales (`V12_05` à `V12_10`)

**Date :** 2026-09-27 · **Lecteur :** même modèle que l'auteur des patchs (auto-comparaison) · **Objet :** bilan des six lectures, registre consolidé des défauts signalés, proposition de chantier « structure et budget ». **Rien n'est appliqué.**

## 1. Périmètre couvert

| Ensemble | Fichiers | Mots | Rapport |
|---|---|---|---|
| Sources normatives | DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE, CHANGELOG | 52 703 | `V12_05`, `V12_06`, `V12_09`, `V12_10` |
| Skill et références | SKILL.md, `examples`, `flow`, `canonical_minimum`, `machine_projection` | 5 568 | `V12_07` |
| Façades | READING_MAP, QUICKSTART, deux README, GLOSSAIRE, ORCHESTRATION_MAP | 9 948 | `V12_07`, `V12_08` |
| **Total lu intégralement** | 16 fichiers | **≈ 68 200** | |

**Non lus dans cette série (déclaré) :**
- schémas JSON et fixtures ;
- scripts de validation (hors la liste des conditions LCF, consultée) ;
- distributions `dist/` (copies dérivées) ;
- `schemas/examples/`.

Ce sont des outils, pas des textes que l'agent lit pendant un run.

**Correction d'un chiffre de `V12_07` §3.1.** Le chemin prescrit y est estimé à ≈ 20 700 mots. `ACTION/RUN-DIRECTION` ordonne en plus d'« exécuter le pipeline `ACTION/PIPELINE-DIRECTION` » (1 482 mots), avec `VISUAL_PROOF` (242), le paquet `CLOSE-PACKAGE` (840) et le handoff (320). **Chemin prescrit réel, lu à la lettre : ≈ 23 600 mots, ≈ 1 650 lignes.** Pour comparaison :
- le plan V1.2 retient ≈ 1 300 lignes ;
- l'outil de budget mesure 614 lignes ;
- les runs B-DLA ont lu 805 à 965 lignes (M4).

Les agents lisent donc déjà **moins que ce qui leur est prescrit**.

## 2. Diagnostic en un paragraphe

Le système possède :
- **les bonnes exigences** (DIRECTION : rôle senior, premier objet, absolus 1 et 5) ;
- **une honnêteté rare** (ACTION : frontière de validation, agent seul, vérité de scène, seul effet mesuré) ;
- **un vrai savoir-faire** (SAVOIR : grammaire positive, forme située, vocabulaire perceptuel ; BIBLIOTHEQUE : tension, signaux de convergence, tests perceptifs).

Mais **le chemin d'un run charge les exigences et la preuve, pas le savoir-faire.** L'agent reçoit « sois senior, prouve-le » sans les gestes. Il retombe donc sur ses réflexes, les mêmes que sans système : c'est l'explication probable de `C4 ≈ C1`, pour deux fois le coût.

**Quatre causes structurelles (probable) :**
1. **Accrétion par audit.** Chaque audit ajoute une protection, une copie ou un renvoi, presque jamais une suppression. Les conditions de façade sont passées de 21 à 42 puis 50, et aucune n'a été retirée.
2. **Architecture pensée à partir de la preuve.** La fabrication est exigée et contrôlée, jamais outillée sur le chemin court. Le meilleur craft d'ACTION (atelier B1b, Gate C, passe créative) est écrit comme un contrôle a posteriori.
3. **Gardes sur des phrases.** Elles figent le texte, rendent toute simplification coûteuse et laissent passer les divergences de structure. Cette limite est **déclarée depuis V1.1.0** (CHANGELOG l.38).
4. **Placement.** Le savoir-faire vit dans les sections que les listes de chargement n'ouvrent pas. C'est aussi le cas des textes des lots 1 et 2 (marqueurs de vague, carte des moyens).

## 3. Où est le beau : inventaire des outils de fabrication

| Outil | Lieu | Sur le chemin `DIRECTION` ? |
|---|---|---|
| Premier objet, 8 dimensions et « Retour si… » | `DIRECTION/FIRST-OBJECT` | **Oui** |
| Qualité initiale attendue | `ACTION/FIRST-RENDER` | Oui dans la skill seulement (absent de QUICKSTART et de READING_MAP) |
| Grille de regard CFT-00 et revue créative | `SAVOIR/CRAFT/CFT-00` | **Oui** (le plus abstrait) |
| Atelier d'édition B1b (retrait, réduction, transformation ; deux captures) | `ACTION/GATE-B` | Oui, **comme preuve** |
| Critères Gate C (C1 à C6) | `ACTION/GATE-C` | Oui, **comme contrôle** |
| Passe créative (masses, vides, échelles, rythme, lumière) | `ACTION/PIPELINE-DIRECTION` | Oui, par renvoi de `RUN-DIRECTION` |
| Traitement des assets moyens (I) | Résumé dans `VISUAL_TARGET` | **Oui** |
| Axes de tension | `BIBLIOTHEQUE/TENSION` | Nommé par le boot, non chargé par les listes |
| **Grammaire positive** (intention → tension → foyer → masse → rythme → matière → contenu → états → résolution → retenue) | `SAVOIR/FRAME` | **Non** |
| Test de singularité, trois lois | `SAVOIR/FRAME` | Non |
| Forme située et test de retrait | `SAVOIR/CRAFT/CFT-01` | Non |
| Composition : compensation optique, recomposition responsive, cohérence ≠ harmonie | `SAVOIR/CRAFT/CFT-03` | Non |
| Question de convergence de la palette | `SAVOIR/CRAFT/CFT-05` | Non |
| **Vocabulaire perceptuel avec « diff possible »** | `SAVOIR/STATE` | Non |
| Calibrations croisées (cinéma, édition, affichage…) | `SAVOIR/SOURCE` | Non |
| Repasse : « ce qui est resté par défaut » | Fin de SAVOIR | Non |
| **Marqueurs de vague** (D, D') | `SAVOIR/TOOLS` | **Non** : le boot n'y renvoie pas |
| Carte des moyens (H) | `SAVOIR/TOOLS` | Non : renvoi non résolvable |
| « Où elle vit, comment le regard circule, quelle preuve, comment on agit » | BIBLIOTHEQUE l.66 | Non |
| **Signaux de convergence structurelle** (6 compositions et questions) | `BIBLIOTHEQUE/SELECT` | Non |
| Lecture expressive (calme ou tension, intimité ou monumentalité…) | `BIBLIOTHEQUE/READ` | Non |
| Tests perceptifs (masquage, silhouette, cinquante produits, scène) | BIBLIOTHEQUE | Non |
| Table de diagnostic (défaut → geste) | QUICKSTART §3 | Ambigu : prescrit par la skill (l.53), absent de la table de charge |
| Six questions de revue créative | QUICKSTART §10 | Ambigu (idem) |
| « Un axe à la fois » | ORCHESTRATION_MAP | Conditionnel |

**Constat (certain) :** sur 25 outils de fabrication, **7 sont sur le chemin** (dont `FIRST-RENDER`, présent dans une seule des six listes). Trois d'entre eux (B1b, Gate C, CFT-00) le sont sous forme de contrôle ou de grille de regard. Tous les outils de **composition positive** sont hors du chemin.

## 4. Registre consolidé des défauts signalés, non corrigés (règle 3)

| N° | Défaut | Lieux | Origine | Rapport | Nature |
|---|---|---|---|---|---|
| D-01 | Deux vocabulaires : « anti-direction » et `MODAL`/`PARTI` | DIRECTION l.36, 88, 292, 315 ; SKILL l.117, 119 ; `examples.md` l.32 ; SAVOIR l.685 ; note de la table `RUN_CARD` d'ACTION | Lot 1 (remplacement partiel) | 05, 06, 07, 09 | Alignement |
| D-02 | Prise de brief compressée : « destination si elle n'est pas évidente » perdue | SKILL l.119 ; QUICKSTART l.45 ; CHANGELOG l.11 | **Lot 1 (nos textes)** | 07, 08, 10 | Alignement |
| D-03 | Absolu 2 : dérive de la skill (conditionnel, sans « fraîche ») ; « fraîche » absent de READING_MAP et du README `V1/official` | SKILL l.43 ; READING_MAP l.24 ; README `V1/official` l.39 | Hérité | 08 | **Décision** (voir D-04) |
| D-04 | Trois positions sur l'ancre dans SAVOIR (requise, recommandée, « utile ou absence déclarée ») contre l'absolu 2 bloquant | SAVOIR l.477, 826, 923 ; DIRECTION absolu 2 | Hérité | 09 | **Décision** |
| D-05 | Six listes de chargement `DIRECTION` divergentes ; `FIRST-RENDER` absent de QUICKSTART et du routage de READING_MAP | SKILL, QUICKSTART §1/§4/§5, READING_MAP, ORCHESTRATION_MAP | Hérité | 08 | Alignement (après choix de la liste) |
| D-06 | BIBLIOTHEQUE exigée en `DIRECTION` (`SELECT`, boot) mais absente des listes | BIBLIOTHEQUE l.196 ; boot | Hérité | 10 | Décision |
| D-07 | Marqueurs de vague et carte des moyens non atteignables depuis le boot ; renvoi « carte des moyens (`SAVOIR`, `[VEILLE]`) » non résolvable | `CREATIVE-BOOT` ; `VISUAL_TARGET` l.64 | **Lots 1 et 2** | 09 | Alignement (renvoi) ou décision (placement, LCF-46) |
| D-08 | GLOSSAIRE non mis à jour : ancre, thèse, `MODAL`, `PARTI`, `FABRICATION`, objet de preuve, défaut dominant, plafond, slop… | GLOSSAIRE | **Lots 1 et 2** (oubli) | 08 | Alignement |
| D-09 | Checkpoint avant build (`PIPELINE` étape 7 ; `START` étape 6 « ne devine pas ») contre « le rendu est construit dans tous les cas » | ACTION l.572-574 ; `START/TREE` ; `EXTERNAL-START` | Hérité + lot 1 | 06, 08 | **Décision** |
| D-10 | Réponse visible en jargon (`MODE — … — OWNER`) contre la délégation silencieuse ; cadratins en série contre `SAVOIR/STYLE` | SKILL l.21 ; QUICKSTART l.213 ; ACTION/HANDOFF | Hérité | 07, 09 | **Décision** |
| D-11 | Circuit d'entrée sans point de départ ; deux README | README ×2, QUICKSTART, READING_MAP, SKILL | Hérité | 08 | Décision (piste « une entrée par public ») |
| D-12 | QUICKSTART : table des cinq questions recopiée ; « tu » et « vous » mêlés | QUICKSTART l.19-25 et 65-71 | Hérité | 08 | Alignement |
| D-13 | Espace en tête de ligne | QUICKSTART l.267 | Hérité | 08 | Coquille |
| D-14 | Troisième format de sortie (« ligne de run minimale ») | SKILL l.83 ; QUICKSTART l.76 | Hérité | 07, 08 | Avec D-10 |
| D-15 | Instrumentation de lecture d'audit dans le chemin d'un run | BIBLIOTHEQUE l.43-52 | Hérité | 10 | Décision |
| D-16 | Deux modèles à trois niveaux | SAVOIR l.203 et l.440 | Hérité | 09 | Alignement |
| D-17 | Ordre de DIRECTION : « à lire avant toute action » l.634, récapitulatif l.776 | DIRECTION | Hérité | 05 | Restructuration |
| D-18 | L'outil de budget ne mesure qu'environ 40 % du chemin prescrit | `audit/tools/V12_Budget_lecture.py` | Nos outils | 07, 11 | Outil (hors package) |

**Défauts introduits par nos lots (certain) :**
- D-02 ;
- D-07 ;
- D-08 ;
- la part lot 1 de D-01.

Ils sont passés **malgré 50 conditions vertes et 300/300** : ces contrôles ne testaient ni la fidélité d'un résumé, ni l'atteignabilité, ni le glossaire.

## 5. Proposition : chantier « structure et budget » (à décider)

### Principes

- **Placer avant d'écrire.** Presque tout le contenu nécessaire existe déjà. Le chantier déplace et condense ; il n'écrit que des renvois et un noyau.
- **Retirer au moins autant qu'on ajoute**, mesuré sur le **chemin prescrit** (D-18), pas sur le périmètre actuel.
- **Gardes de propriété d'abord**, sinon chaque déplacement coûte une série de rectifications (`V12_05` §3.9).

### Phases

| Phase | Contenu | Taille estimée | Méthode |
|---|---|---|---|
| **0. Outils** | Budget sur deux périmètres (actuel et prescrit) ; **gardes de propriété** rouges d'abord : égalité des listes de chargement, atteignabilité des textes dont dépend le boot, vocabulaire unique `MODAL`/`PARTI`, fidélité des résumés de la prise de brief et des absolus | Petite | Outils hors package, puis LCF dans une PATCH-DECISION |
| **1. Alignements** | D-01, D-02, D-05 (une liste, avec `FIRST-RENDER`), D-07 (renvois), D-08, D-12, D-13, D-16, entrée CHANGELOG | Petite | PATCH-DECISION sans changement de méthode |
| **2. Noyau de fabrication** (la skill) | Voir ci-dessous | Moyenne | PATCH-DECISION ; rectifications de harnais déclarées (C4, R-17…) |
| **3. Trace à deux niveaux** (ACTION) | Trace légère par défaut, `RUN_CARD` complète si le run est persistant ou audité ; la première proposition vaut checkpoint (D-09) ; Gate A par profil de surface ; `BIBLIOTHEQUE/GATE` fondu dans A et C ; instrumentation de lecture hors run (D-15) | **Grande** (schéma, validateurs, harnais) | PATCH-DECISION en plusieurs unités |
| **4. Décisions d'orientation** | Ancre graduée par destination (D-03, D-04) ; lois de SAVOIR rééquilibrées pour les surfaces identitaires ; catalogue élargi aux contextes de l'owner (runs réels, `PILOT`) | Variable | Décision de l'owner, puis épreuve |

**Contenu du noyau de fabrication (phase 2), une à deux pages dans la skill :**
1. **Rôle** : designer senior, en une phrase. Classement en une ligne.
2. **Prise de brief** : une seule fois, puis construire.
3. **Structure** : où elle vit, comment le regard circule, quelle preuve, comment on agit ; un ou deux axes de tension ; les six signaux de convergence comme `MODAL` structurel.
4. **Composition** : la grammaire positive ; le vocabulaire perceptuel avec « diff possible » ; le test de singularité ; la question de convergence (palette, typo, assets) ; les marqueurs de vague datés (placement à décider, LCF-46).
5. **Boucle d'édition** : table de diagnostic (défaut → geste), atelier retrait / réduction / transformation, deux captures, six questions de revue, repasse « ce qui est resté par défaut ».
6. **Vérité** : plafond par couche, jamais de faux asset, traitement des assets moyens, données marquées.
7. **Sortie en langage produit** : ce que j'ai fait, pourquoi, ce qui manque pour la vraie version, la suite. La trace n'est détaillée que sur demande.

**Financement :** une seule activation, une seule liste de chargement ; les copies de la constitution, du handoff et du polish remplacées par des renvois ; README et QUICKSTART retirés du chemin de run de l'agent. **Objectif (hypothèse) : −30 % au moins sur le chemin prescrit.**

**Critères de réussite :**
- chemin prescrit en baisse d'au moins 30 % ;
- gardes de propriété vertes ;
- 300/300 avec rectifications déclarées ;
- harnais R et R03, 13.01 et 13.02 verts ;
- B01 218/218.

**Critères d'arrêt :** une phase qui augmente le chemin prescrit, ou qui exige plus de rectifications de harnais que de changements de texte, s'arrête et revient à l'owner.

**Taille (à signaler, règle de style) :** la phase 3 est **surdimensionnée** pour une seule unité. Elle touche le schéma `RUN_CARD`, les validateurs, les fixtures et plusieurs harnais. Elle doit être découpée, ou reportée après une épreuve qui confirme l'intérêt des phases 1 et 2.

### Ordre recommandé (probable)

0 → 1 → 2, puis **une épreuve** (la mini-épreuve reportée, sur B06), puis 3 et 4 selon le résultat. Raison : les phases 0 à 2 sont peu risquées et testent l'hypothèse principale (« placer le savoir-faire sur le chemin améliore le rendu »). La phase 3 est coûteuse et ne se justifie que si cette hypothèse tient.

## 6. Lecture

- **Certain :**
  - le périmètre lu ;
  - les chiffres corrigés du chemin prescrit (≈ 23 600 mots, ≈ 1 650 lignes) ;
  - l'inventaire du §3 (7 outils de fabrication sur 25 sur le chemin) ;
  - le registre du §4, dont quatre défauts viennent de nos lots et ont franchi tous les contrôles.
- **Probable :**
  - le diagnostic (le savoir-faire existe mais n'est pas sur le chemin) et ses quatre causes ;
  - l'ordre recommandé.
- **Hypothétique :**
  - l'objectif de −30 % ;
  - l'effet sur la qualité d'un noyau de fabrication ;
  - le biais vers la retenue (`V12_09` §3.4) ;
  - l'effet du catalogue sur les petites entreprises (`V12_10` §3.2).

  Tout cela est à éprouver.
- **Limite :** six lectures par le même modèle que l'auteur des patchs. Il n'y a eu aucun regard extérieur ; un relecteur indépendant (critère D3) pourrait contester l'inventaire du §3 et les priorités du §5.
