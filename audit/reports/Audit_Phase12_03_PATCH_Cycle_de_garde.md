# DG-AUDIT-001 — Phase 12.03 — PATCH : cycle de garde

**Date :** 25 septembre 2026. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée.

**Format :** rapport allégé, décidé par l'owner le 25 septembre : diff, résultats, écarts déclarés.

**Commit :** `5ebdd3d`, étiquette `12.03-garde`, diff `DG_AUDIT_001_B03_12-03_garde.diff`.

**Décisions appliquées :**
- C4 O-1 et O-2, dans un seul diff (rectification R-2 de 11.23) ;
- E2 O-5 ;
- C5 (table LCF), avec les entrées de C6, D1 et D4 ;
- D4 O-1, placé dans le cycle de garde par la rectification R-4 de 11.23.

## 1. Diff

| Fichier | Lignes | Contenu |
|---|---|---|
| `read_route.py` | +132 / −40 | Le résolveur passe par trois étapes : la table (y compris les sous-locators écrits `titre › titre`), puis le préfixe (titre unique), puis le sous-locator `X/Y/Z`. S'y ajoutent le refus « locator ambigu », les titres ignorés dans les blocs de code (E2 O-5, F-RRT-001) et l'exclusion des sous-blocs qui portent leur propre locator, signalés par une ligne-marqueur. Le résolveur est importable (`resolve`, `extract`, `RouteError`) |
| `validate_reading_map.py` | +264 / −45 | Validateur « carte et façades ». Côté **carte** : locator en double, propriétaire incohérent, destination qui ne correspond pas au locator, titre introuvable, couverture de **tout** locator cité (fichiers officiels et skill), unicité des titres porteurs d'un locator. Le seuil « ≥ 10 lignes » est retiré. Côté **façades** : la **LCF à 21 entrées**, en table déclarative ; chaque échec imprime `LCF-xx`, la façade et la source propriétaire. Le résolveur est importé, sans écrire de bytecode dans le package |
| `validate_design_governance.py` | +1 / −1 | `SEED` est ajouté aux termes requis du cycle de vie |

**Ce qui ne bouge pas :**
- aucun fichier n'est ajouté ; les manifestes restent à 60/56 ;
- bibliothèque standard seulement ;
- **aucun texte n'est modifié.**

Les prédicats de la LCF reprennent à l'identique ceux des harnais C5, C6, D1 et D4. Deux adaptations tiennent aux distributions :
- le README et la skill sont pris dans la distribution validée (GitHub ou Local) ;
- `RELEASE_NOTES.md`, absent de la distribution Local, n'est exigé par LCF-21 que là où il existe.

## 2. Résultats

**État réel de B03.** C'est la fenêtre de garde : des rouges sont voulus.

| Contrôle | Résultat |
|---|---|
| `validate_reading_map.py` | **Rouge, pour exactement 21 motifs attendus :** 20 conditions LCF non tenues (tout sauf LCF-20, qui est une conservation) et « locator ambigu : DIRECTION/START » (DIRECTION 119 et 300 ; levé par C4 T-5) |
| `validate_design_governance.py` | **Rouge, pour 1 motif attendu :** `SEED` absent du CHANGELOG (levé par D4 T-1) |
| `validate_all.py` | Rouge : il s'arrête sur `SEED` |
| Build | Rouge : il lance le validateur de package |
| Suites RUN_CARD et contrats | Vertes |
| Verdicts ciblés (29 documents) | **Identiques à B01** |
| Couverture des locators cités | **56/56 servis** (8 étaient refusés dans B01, F-DIR-028) |

**Contre-épreuve.** Il s'agit d'une copie de B03 où seules les trois gardes de la fenêtre sont neutralisées. Résultats :
- **`validate_all.py` : FULL VALIDATION PASSED**, avec les deux distributions construites deux fois à l'identique et les exports Local validés, résolveur compris ;
- **témoins des 22 harnais : 40/40.**

**Rien d'autre n'est cassé.** Les seuls rouges de B03 sont les rouges voulus.

**Suivi** (`--fenetre --compare` avec 12.02) :
- cas verts bruts : **44/300** ;
- cas verts **significatifs**, c'est-à-dire qui restent verts dans la contre-épreuve : **27/300** (+8 ; ils étaient 19) ;
- **aucune alerte.**

Les huit cas nouveaux :
- C4 R-01 et R-02 : tout locator cité et toute la carte de chargement d'ACTION sont servis ;
- C4 R-06 : `SAVOIR/CRAFT/CFT-01` est servi seul ;
- C4 V-01 à V-04 : les quatre mutations de la carte sont rouges, chacune pour son motif ;
- E2-12 : un titre factice dans un bloc de code est ignoré.

**Cas verts non significatifs : 17.** Ils se répartissent ainsi : C5 (6), C6 (4), D1 (2), D4 (2), E2 (3). Ce sont des mutations LCF, vertes seulement parce que le validateur est déjà rouge sur le texte non corrigé, et trois cas de build, verts parce que le build s'arrête plus tôt. Ils ne sont **pas comptés**.

**B01 :** 218/218, aucun fichier généré.

## 3. Écarts et rectifications déclarés

**R-7 : témoins rouges dans la fenêtre (rectification de 11.23 §6).**
- **Ce qu'écrivait 11.23 :** « les témoins restent verts » pendant la fenêtre.
- **Pourquoi c'était faux :** huit témoins lancent eux-mêmes le validateur de carte, `validate_all` ou le build : A2, C4, C5, C6, C8, D1, D4 et E2. Ils sont donc rouges par construction.
- **Ce que j'ai changé :** l'outil de suivi a reçu une option `--fenetre`. Un témoin rouge n'y est admis que si la **contre-épreuve** le rend vert. Le critère « rouges décroissants » porte alors sur les cas **significatifs**.
- **Les harnais ne sont pas modifiés.** C'est l'outil de suivi qui change, et le changement est déclaré ici.
- **Fin de la fenêtre :** elle se ferme à la fin de 12.05. Ensuite, `--fenetre` n'est plus utilisé, et tout témoin rouge redevient une alerte.

**Conséquence pratique pour 12.04 (certaine).** Pendant la fenêtre, le build et `validate_all` ne se lancent pas. La migration sera donc contrôlée autrement :
- par les suites RUN_CARD et contrats, lancées directement ;
- par la contre-épreuve, qui construit les deux distributions.

**Message « locator inconnu ».** L'ancien message énumérait « disponibles : … », c'est-à-dire la table. La table n'est plus un inventaire : la plupart des locators sont servis par préfixe. La liste aurait donc induit en erreur, et je l'ai retirée. Le motif `locator inconnu : <locator>`, attendu par l'orchestrateur, est conservé.

**À surveiller : le budget de C4 R-04 (probable).**
- **Mesure :** `DIRECTION/START` est servi en **76 lignes**, pour un budget de 75 (130 dans B01). CREATIVE-BOOT et DOMAIN-FRAME en sont exclus, et signalés par une ligne-marqueur.
- **Pourquoi ce n'est pas tranché :** les corrections de texte de la zone 119–310 (C5 T-4, passe DIRECTION) changeront ce nombre.
- **Si le dépassement persiste à la fin de 12.05,** il sera déclaré : ou bien le budget de 11.11 était trop serré d'une ligne, ou bien une ligne-marqueur est de trop. Le harnais ne sera pas modifié en silence.

## 4. Fiches

**Levées côté outil (certain) :**
- **F-DIR-028** : couverture 56/56 ;
- **F-VRM-001** : V-01 à V-04 ;
- **F-RRT-001** : E2-12.

**Garde en place, texte à venir :**
- F-VRM-003 : la LCF est posée ;
- F-RM-003 : le sous-locator est prêt ; il reste la ligne de table `DIRECTION/START/TREE` (C4 T-4) ;
- F-CHG-001 : `SEED` exigé ; il reste le CHANGELOG (D4 T-1) ;
- toutes les fiches couvertes par la LCF.

**Journal des notes de version (B03), ligne ajoutée :**

> 12.03 — Le lecteur de routes résout par table, préfixe et sous-locator, refuse l'ambiguïté et ignore les titres des blocs de code ; le validateur de carte vérifie la couverture de tout locator cité et une liste close de conditions de façade.

## 5. Suite

**Prochaine unité : 12.04, migration unique**, en unité plus grosse, comme convenu. Elle porte sur :
- **les quatre schémas**, avec les invariants nouveaux de la liste close et leurs cas unitaires ;
- **les données** : exemple canonique, fixtures, exemples de contrats, YAML de `machine_projection.md` ;
- **INV-C4-1 et C4-2, et E2 O-12.**

**R-6 s'applique dans cette migration** (racine de `production_contracts`), sauf objection de votre part.

**Une décision reste ouverte : les cas unitaires pour les ~14 invariants existants sans négatif** (12.02, §2.2). Sans réponse de votre part, **je ne les ajoute pas.** La migration ne couvrira alors que les invariants nouveaux, comme décidé en 11.02.
