# DG-AUDIT-001 — Phase 12.05c — PATCH : DIRECTION, SAVOIR, cartes, glossaire et façades ; fermeture de la fenêtre de garde

**Date :** 26 septembre 2026. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée. **Format :** rapport allégé.

**Commit :** `6de1f9b`, étiquette `12.05c-textes-facades`.

**Fichiers produits :**
- `DG_AUDIT_001_B03_12-05c.diff` ;
- `DG_AUDIT_001_B03_package_12-05c.zip` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-05c.json` ;
- harnais rectifiés : `C5_harnais_non_regression.py` et `E1_harnais_non_regression.py` (R-12 à R-14, §3).

**Ordre suivi :** 11.23 §7, c'est-à-dire DIRECTION → SAVOIR → cartes et glossaire → façades. C'est la dernière passe de texte.

## 1. Inventaire de la passe

L'inventaire reprend toutes les lignes de correction des 22 rapports de la phase 11 dont la cible n'est ni CHANGELOG, ni BIBLIOTHEQUE, ni ACTION. Une seconde lecture a été faite par colonne « Où ».

**Résultat : 15 fichiers modifiés, +198 / −175. Toutes les corrections sont appliquées.**

| Propriétaire | Décisions et corrections | Contenu appliqué (résumé) |
|---|---|---|
| **DIRECTION** (≈ 60 corrections) | B1 T-1, T-2 ; B4 T-4 ; C1 T-2, T-7 à T-11 ; C2 T-4 à T-8, T-11 ; C4 T-5, T-6 ; C5 T-1, T-2, T-4, T-5 ; D1 T-1, T-2, T-5, T-7 à T-9 ; D2 T-1 à T-3 ; D4 T-4 à T-6 ; E1 F-DIR-005, 012, 014, 015, 025, 026, 031, 037, 040, 043, 045 | Voir le détail ci-dessous |
| **SAVOIR** (11) | B4 T-1, T-2 ; B5 T-3, T-4 ; C1 T-6 ; C7 T-1, T-2, T-4 ; D3 T-6 ; E1 F-SAV-001, 004, 010 | Voir le détail ci-dessous |
| **Cartes et glossaire** | READING_MAP : C4 T-3, T-4 ; C5 T-8, T-9, T-11. ORCHESTRATION_MAP : C5 T-3, T-10. GLOSSAIRE : C6 T-5, T-6 ; E1 F-GLO-001 | Voir le détail ci-dessous |
| **Façades** | QUICKSTART : B1 T-4 ; C3 T-7 ; C4 T-6 ; C5 T-6 ; C9 T-1 ; D1 T-6 ; E1 F-QS-001, T-QS. README des deux distributions : C5 T-7 ; C9 T-1. Promesse du validateur : B2 T-8, B3 T-6, B4 T-5. Skill : C3 T-5, T-6 ; C4 T-6 ; C5 T-3. `examples.md` : C6 T-1 à T-4, T-7. `flow.md` : F-FLOW-001. `machine_projection.md` : prose de B1 (§107) et promesse | Voir le détail ci-dessous |

**Détail DIRECTION :**
- Sortie vers ACTION par la colonne Phase de la table de correspondance ; contrat `HANDOFF` rangé en « avant build » et « après observation » (D2 T-1, T-2).
- Chaîne de lecture dans l'ordre START → CREATIVE-BOOT → VISUAL_TARGET → ATELIER → FIRST-OBJECT → DOUBLE-LOOP ; RUN-PRIORITY avec DIRECTION avant FIRST-OBJECT et l'exception « sauf si la navigation, la recherche ou les cartes sont l'objet de preuve » (C5 T-1, T-2).
- Efficacité : « vise à augmenter… ; cette efficacité reste `NOT-VERIFIED` » (D4 T-4, T-5).
- `OWNER` et `SCOPE` ne sont jamais omis (C5 T-4).
- La colonne « Clôture minimale » de DAILY est remplacée par un renvoi à `ACTION/CLOSE-PACKAGE`. La section 0 est réduite à trois renvois (C2 T-4, T-5).
- `VISUAL_TARGET` a une seule table canonique : « Objet de preuve », « Résolution initiale ». `SPECCED` est défini par renvoi à la table (C2 T-7, T-8 ; C1 T-9).
- Contrat du premier objet :
  - il reçoit une colonne « Dimension CFT-00 », avec la perte « Culture visuelle » déclarée ;
  - la grille propre de DOUBLE-LOOP et la section « contrôle compact » sont supprimées (D1 T-1, T-2, addendum 11.19).
- TRUTH :
  - deux axes : factualité × nature, la fiction l'emporte ;
  - règle d'audience (langage produit) ;
  - la critique d'ATELIER se fait dans la revue créative unique (C1 T-7, T-8 ; D1 T-5).
- Triade de la conséquence décisionnelle dans la Sortie immédiate, le premier objet et ATELIER (C1 T-2).
- ABSOLU 5 : DIRECTION signale le risque et la méthode relève d'`ACTION/GATE-B` et de `SAVOIR/CONTEXT`. La table « trois niveaux de preuve » est supprimée (C1 T-10, T-11).
- Titre `DIRECTION/START` en double : il est renommé « Traduction humaine minimale de DIRECTION/START », et la question de risque y est ajoutée (C4 T-5, B1 T-2).
- Déclencheurs critiques :
  - motif → `SAVOIR/CRAFT/CFT-01` et `ACTION/ANTI-SLOP` ;
  - scène → `BIBLIOTHEQUE/SELECT` puis `BIBLIOTHEQUE/SCENE` ;
  - détail final → `SAVOIR/CRAFT/CFT-03` (D1 T-7 à T-9).
- Autres corrections :
  - paquet d'alternative transporté par la trace (C2 T-6) ;
  - ordre de promotion conditionné au caractère structurel (D4 T-6) ;
  - correspondance `direction.calibration` (B4 T-4) ;
  - lot éditorial E1 (légende commune, cardinalités du Boot, `ITER` dans DAILY, triade de FAST-PATH, `SANS-ASSET`, `GÉNÉRÉ-DIRIGÉ` borné, ABSOLU 4, capacité, « direction retenue », récapitulatif de protection, `closure.limitations`).

**Détail SAVOIR :**
- Chargement « typiquement zéro à deux routes ; une route par question active ».
- CFT-05 : répartition neutres/couleurs laissée à la direction, plus la question de convergence.
- Test de style : dépendance au médium masqué.
- `PROFILE-DECISION` se lit en deux temps.
- Ancre requise pour une surface identitaire ; une revue indépendante n'est pas une calibration.
- SYSTEM :
  - l'effet partagé est signalé à `DIRECTION/START` ;
  - le contrat de composant est renvoyé à `BIBLIOTHEQUE/COMPONENTS`.
- TECH : l'approbation vise la **nouvelle dépendance**, avec renvoi à `ACTION/POLICIES`.
- ATLAS : `SAVOIR/SYSTEM` ; règle d'or 6.

**Détail cartes et glossaire :**
- READING_MAP :
  - la colonne « Sortie minimale » est remplacée par un renvoi à `ACTION/HANDOFF` et à `ACTION/CLOSE-PACKAGE` ;
  - « Direction identitaire » suit START → VISUAL_TARGET → FIRST-OBJECT → `ACTION/RUN-DIRECTION` ;
  - l'accessibilité reste due au-delà de Gate A ;
  - la résolution en trois étapes et le refus d'ambiguïté sont décrits ;
  - la ligne `DIRECTION/START/TREE` est ajoutée.
- ORCHESTRATION_MAP : Gate A, le gate du risque et le paquet SYSTÈME passent au noyau.
- GLOSSAIRE : RUN_CARD persistante ; exemples `DECISION-CHANGE` et `CLOSED` réécrits.

**Détail façades :**
- QUICKSTART :
  - deux sorties (réponse visible et handoff) ;
  - classement renvoyé à `DIRECTION/START` ;
  - §6 projette les huit dimensions de FIRST-OBJECT, dans le même ordre et sous les mêmes noms ;
  - conditions de fermeture par issue ;
  - commande `--type` ;
  - chemins des références de la skill.
- README des deux distributions : lignes ITER et DIRECTION, « Classement : voir `DIRECTION/START` ». Le README racine reçoit aussi la commande `--type` et la promesse du validateur.
- Skill :
  - deux sorties, copiées mot pour mot du canon ;
  - `DIRECTION/START/TREE` ;
  - `SAVOIR/CRAFT/CFT-00` ;
  - VISUAL_TARGET avant FIRST-OBJECT.
- Exemples : le triplet de conséquence avec son observation, une réserve complète, la preuve visuelle bornée et le `NOT-VERIFIED` du SYSTÈME.
- Flux : deux arêtes de retour.

## 2. Résultats

**La fenêtre de garde est fermée.** `validate_all.py` sort **FULL VALIDATION PASSED sans aucune neutralisation**, avec les deux distributions construites deux fois à l'identique et l'export Local validé, résolveur et conditions de façade compris. `--fenetre` n'est plus utilisé à partir de cette unité.

| Contrôle | Résultat |
|---|---|
| `validate_reading_map.py` | **Vert** : les 21 conditions LCF sont tenues ; plus de locator ambigu ; tous les locators cités sont servis, dont `DIRECTION/START/TREE`, `BIBLIOTHEQUE/TENSION`, `BIBLIOTHEQUE/SCENE`, `SAVOIR/CRAFT/CFT-03` |
| Package, RUN_CARD, contrats | Verts ; 25/25 fixtures, 76/76 et 20/20 cas unitaires |
| **Témoins des 22 harnais** | **40/40, sans contre-épreuve** |
| Suivi (`--rectifies C5,E1 --compare` 12.05b) | **Cas verts : 190 → 282/300**, aucune alerte, aucune régression |
| Gardes textuelles | Toutes vertes (B5, C1 à C7, D1 à D4, E1-01 à E1-27). Mutations LCF : toutes au rouge (C5 6/6, C6 4/4, D1 2/2, D4 2/2) |
| B01 | 218/218, aucun fichier généré ; les harnais rectifiés restent rouges sur une copie de B01 |

**Les 18 rouges restants :**

| Rouges | Nature | Unité |
|---|---|---|
| E2 (13), C8 R-1 à R-3 (3), E1-28 (1) | Outils : manifeste, UTF-8, clés répétées, build atomique, chemins Local, workflow | **12.06**, cycle d'outils final |
| C4 R-04 (1) | Budget de `DIRECTION/START` (R-4) | **Décision de l'owner**, voir §3 |

**Relecture de fin de passe (§22).** J'ai relu toutes les lignes modifiées de chaque fichier.
- **Corrigé :** une faute d'accord dans ATELIER (« emploie… puis nomme »).
- **Relevé, non corrigé** (aucune décision de phase 11 ne les vise ; je les note sans les corriger) :
  - QUICKSTART 45 et la skill 103 résument encore le Creative Boot avec « deux anti-directions concrètes, une tension ». DIRECTION a retiré ces nombres (F-DIR-012) : la copie contredit désormais le propriétaire ;
  - la table d'architecture de DIRECTION (ligne VISUAL_TARGET) dit encore « preuve », alors que la table cible dit « objet de preuve » ;
  - la redondance `PILOT` de BIBLIOTHEQUE, déjà relevée en 12.05a.

## 3. Écarts et rectifications déclarés

**Rectifications de harnais et d'outil**

| # | Écart | Traitement |
|---|---|---|
| **R-12** | Pour LCF-07 et LCF-09, le validateur (copié du harnais C5 en 12.03) et le harnais C5 cherchaient le bloc RUN-PRIORITY à partir de la **première occurrence** du mot, qui est la première ligne du bloc. Le bloc lu était donc celui d'après : ces deux conditions ne pouvaient jamais être vertes | Le marqueur devient l'ouverture du bloc (`` ```text\nRUN-PRIORITY ``). Correction identique dans `validate_reading_map.py` (B03) et dans le harnais C5. B01 reste rouge, et les mutations LCF-07/09 passent au rouge |
| **R-13** | Deux gardes E1 attendaient une formulation différente du **texte décidé** : E1-12 cherchait « observé**es** » (le texte décidé est au singulier) ; E1-23 cherchait « par mode / selon le mode » (le texte décidé dit « chaque mode n'en garde que… ») | Les expressions régulières acceptent le texte décidé. B01 reste à 0/28 |
| **R-14** | La mutation M-6 de C5 cherchait `` `EXIT-CONDITION` `` entre accents graves. La copie décidée (C3 T-5) recopie le canon en bloc de code, sans accents : la mutation ne modifiait donc rien | La mutation vise le jeton, avec ou sans accents. Sur B01, elle touche la même occurrence qu'avant. Elle est de nouveau au rouge |

**Rattrapage de 12.05b.** B4 T-5 (le point « forme seule » sur la fraîcheur de l'ancre dans la promesse du validateur) n'avait pas été appliqué dans ACTION en 12.05b. Sa colonne « Où » disait « Promesse du validateur », sans nommer ACTION, et mon filtre ne l'a pas retenu. Il est appliqué ici dans ACTION, et dans les copies du README et de `machine_projection.md`. **L'inventaire de 12.05b comptait donc 45 lignes, et non 44.**

**Écarts de rédaction**
- **B1 T-1** :
  - la mention « sans risque critique touché » est posée aussi sur la ligne ITER de DAILY : la décision le laissait « à confirmer en phase 12 », et c'est confirmé, puisque la protection de niveau exclut LITE comme ITER ;
  - la ligne 664 a disparu avec la table de la section 0 (C2 T-5).
- **Numéros de ligne remplacés par des locators :** « BIBLIOTHEQUE 90 » → `BIBLIOTHEQUE/TENSION` ; « START 131, 138 » → `DIRECTION/START/TREE` ; « ACTION 483 » → `ACTION/PIPELINE-DIRECTION`. L'identifiant d'audit « INV-B4-6 » est retiré de la règle d'or 6 : aucun texte du package ne cite d'identifiant d'invariant.
- **D1 T-1** : la cellule CFT-00 de « Vérité de scène » vaut « DIRECTION » seul, pour que LCF-16 la lise. Le renvoi (TRUTH, ATELIER) est placé dans une phrase sous la table. Dans DOUBLE-LOOP, « Lorsqu'un test échoue » devient « Lorsqu'une dimension échoue », puisque la grille des tests est supprimée.
- **Alignement imposé par C1 T-7** : dans FIRST-OBJECT, une démonstration hypothétique porte `TRUTH/ILLUSTRATIVE`, cumulé avec `TRUTH/MECHANISM`, et non plus « l'un ou l'autre ». Sans cet alignement, le texte aurait contredit la règle décidée.
- **C6 T-1** : la ligne `NOT-VERIFIED` de l'exemple LITE devient la ligne `LIMIT` décidée.
- **E1 T-QS** : les chemins des références sont écrits en chemins de code, et non en liens Markdown. Un lien vers `skills/…` serait cassé dans l'export Local et ferait échouer le build jusqu'à la réécriture O-1, prévue en 12.06.
- **LCF-21 dans les deux distributions** :
  - `RELEASE_NOTES` 56 et le README Local reçoivent le jeton `NOT-VERIFIED` ; les deux textes disaient déjà « non démontré » et « à vérifier » ;
  - le README Local (dans `build_distributions.sh`) sépare LITE et ITER ; sa section « Trois cas simples » devient « Cas simples » (C5 T-7 : « les deux distributions »).
- **E1 F-DIR-031** : la phrase « l'intake nécessaire au classement reste possible » est reprise de l'annotation de la décision.

**R-4 : budget de `DIRECTION/START`. Décision de l'owner requise.**
- **Mesure :** le bloc est servi en **76 lignes, pour un budget de 75**. Les corrections de la zone START sont toutes écrites dans des lignes existantes : aucune ligne n'a été ajoutée.
- **D'où vient la ligne en trop :** le bloc servi se termine par la règle horizontale `---` qui sépare START de DAILY, suivie d'une ligne vide. Ce ne sont pas des lignes de contenu.
- **Option (a) :** porter le budget à 76. C'est une rectification du seuil fixé en 11.11, trop serré d'une ligne.
- **Option (b) :** faire retirer au lecteur les séparateurs de fin de bloc, en 12.06. C'est un changement d'outil qui n'a pas été décidé en phase 11.
- **Sans réponse de votre part, je ne fais ni l'un ni l'autre :** R-04 reste rouge et déclaré.

**Journal des notes de version (B03), ligne ajoutée :**

> 12.05c — DIRECTION : sortie par phase, chaîne cible → premier objet, efficacité bornée (NOT-VERIFIED), une seule table de cible, contrat du premier objet relié à CFT-00, marquage TRUTH à deux axes, triade de conséquence, section 0 et DAILY renvoyées à ACTION, titre START dédoublé. SAVOIR : palette sans répartition imposée, test de style par dépendance, contrat de composant renvoyé à BIBLIOTHEQUE, approbation limitée aux nouvelles dépendances. Cartes, glossaire et façades alignés sur leurs propriétaires et contrôlés par les 21 conditions LCF, dans les deux distributions.

## 4. Suite

**12.06 : cycle d'outils final.** Il comprend :
- C8 O-1 à O-4 (build atomique, liens symboliques, fichiers inattendus, archives périmées) ;
- E2 O-1, O-3, O-4, O-6 à O-11 et O-13 (manifeste, UTF-8, clés répétées, types, lancement externe) ;
- E1 O-1 (chemins propres à l'export Local, E1-28) ;
- F-WF-001 (actions du workflow épinglées ; **la preuve demande un run GitHub hébergé que vous seul pouvez lancer**).

Il se termine par les notes de version de B03. **Je vous demanderai le numéro de version de B03** : B02 a déjà pris V1.0.1.

**Décisions de l'owner encore ouvertes :**
1. R-4, option (a) ou (b) ci-dessus ;
2. les cas unitaires des quelque 14 invariants existants sans négatif (12.02 §2.2) ;
3. les trois incohérences relevées non corrigées (§2).
