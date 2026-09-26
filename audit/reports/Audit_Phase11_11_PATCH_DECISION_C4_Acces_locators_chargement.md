# DG-AUDIT-001 — Phase 11.11 — PATCH-DECISION C4 : accès, locators et chargement

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ».

**Grappe C4 : 5 fiches, toutes Significatif.**

| Fiche | Objet |
|---|---|
| F-ACT-001 | La carte de lecture d'ACTION annonce un chargement minimal que le lecteur outillé ne peut pas exécuter. STANDARD, DIRECTION et SYSTÈME n'y chargent ni STATUS ni PRECONDITION |
| F-ACT-020 | `trace_locator` : la prose, le profil normal et le profil strict disent trois choses différentes (LITE refusé en strict, ITER sans trace admis en normal) |
| F-DIR-028 | Des titres existants sont refusés par `read_route.py`, alors que la validation de la carte passe |
| F-RM-003 | Granularité : `DIRECTION/START` sert tout le bloc parent (Boot et Domain Frame compris), alors que la skill demande « l'arbre seulement » |
| F-VRM-001 | `validate_reading_map.py` n'exige qu'« au moins 10 lignes » : un doublon, une mauvaise destination ou des retraits passent |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C4_harnais_non_regression.py`, en quatre parties : RUN_CARD, résolution, validateur de carte, gardes ;
- 2 lignes ajoutées à la liste close.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 à 11.10 ; D-ACT-1 = c ; D-FAC-1 = c ; A2 ; C2 (un résumé concurrent cède la place à un renvoi) ; C3 (forme légère au départ) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218. Contrôles directs sur une copie |
| Sources relues | ACTION 1–21 (Responsabilité, carte de lecture), 252–334 (RUN_CARD, dont 273 TRACE-LOCATOR), 335 (`## ACTION/RUN`) ; DIRECTION 119–244 (START et sous-sections), 300 ; READING_MAP 78–127 ; QUICKSTART 116–124 ; README 100 ; skill 75–82 |
| Machine relue | `read_route.py` (86 lignes) ; `validate_reading_map.py` (105 lignes) ; `validate_run_card.py` 150–236 (exigences par mode), 276–325 (`check_strict_contract`) |

## 2. Re-vérification

**Harnais C4 sur B01 :**
- témoins **3/3** ;
- RUN_CARD **0/6** ;
- résolution **0/7** ;
- validateur de carte **0/4** ;
- gardes **0/7**.

**Mesures déterministes :**

| Mesure | B01 |
|---|---|
| Locators cités (en code) dans les fichiers officiels et la skill | **56 distincts ; 24 servis** par le lecteur (43 %). ACTION 12/24, SAVOIR 3/15, BIBLIOTHEQUE 4/7, DIRECTION 5/10 |
| Carte de lecture d'ACTION | **8/15 servis.** Refusés : `STATUS`, `PRECONDITION`, `PIPELINE-DIRECTION`, `VISUAL_PROOF`, `GATE-B`, `GATE-C`, `RUN_CARD` |
| « Commencez par `ACTION/RUN` » (ACTION 7) | Refusé ; le titre existe pourtant (`## ACTION/RUN — routes d'exécution`) |
| `DIRECTION/START` | 130 lignes : Boot, Domain Frame, sortie et mémoire de lancement. L'arbre utile en fait 19 |
| Route LITE de la skill (START, RUN-LITE, FAST-PATH) | **158 lignes servies**, dont 130 pour START (9.08 : 80 %) |
| Validateur de carte, quatre mutations (destination fausse, doublon, titre renommé, mauvais propriétaire) | **PASS** aux quatre |

**Contrôles directs (cartes de forme B01, sur copie) :**

| Cas | B01 |
|---|---|
| ITER sans `trace_locator`, profil normal | **acceptée** |
| LITE sans `trace_locator`, profil normal | acceptée |
| La même LITE, artefact présent, profil strict | **rejetée** (« trace_locator doit être renseigné »), contre ACTION 273 |
| STANDARD en strict, locator relatif présent **à côté de la carte** | **rejetée** (« artefact local absent ») : le strict résout les chemins depuis la racine du package, pas depuis la carte (`source_path` est reçu mais inutilisé) |

**Relecture : quatre constats qui orientent la décision.**

1. **La règle de résolution est déjà promise et jamais implémentée.** READING_MAP 95 : « Les routes non listées restent résolues par leur préfixe propriétaire et leur titre exact ». `read_route.py` ne sert que la table. Une règle « préfixe + titre exact » servirait **53 des 56** locators cités sans aucune ligne de table.
2. **Un locator est porté par deux titres.** `DIRECTION/START` est à la fois le titre 119 (« classer avant d'agir ») et le titre 300 (« traduction humaine minimale »). C'est un défaut d'identité de la famille de F-VRM-001, découvert pendant la re-vérification.
3. **Le surcoût de START n'est pas le seul fait de l'arbre.** Le bloc embarque deux sous-blocs qui ont **leur propre locator** : `DIRECTION/CREATIVE-BOOT` et `DIRECTION/DOMAIN-FRAME`. Même phénomène pour SELECT, qui embarque `BIBLIOTHEQUE/FAST-PATH` et `BIBLIOTHEQUE/DERIVE`.
4. **Deux analyseurs de la même table.** `validate_reading_map.py` réécrit son propre analyseur au lieu d'utiliser celui du lecteur. C'est ainsi que la validation passe là où le lecteur refuse.

## 3. Les sept questions du §21

| Question | F-ACT-001 | F-ACT-020 | F-DIR-028 | F-RM-003 | F-VRM-001 |
|---|---|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : préconditions non chargées en mode lourd | **Oui** : le résultat dépend de la commande choisie | Oui : module ignoré ou lecture intégrale | Oui : coût de contexte ×5 sur la route courte | Oui : toute correction de locator passerait sans contrôle |
| Défaut réel ? | Oui (8/15) | Oui (contrôles directs) | Oui (24/56) | Oui (130 lignes contre 19) | Oui (4 mutations en PASS) |
| Gain > charge ? | Oui : une ligne de socle | Oui : une règle, deux profils alignés | **Oui, sans table à maintenir** : une règle dans l'outil | Oui : une règle générique et **une** ligne de table | Oui |
| Nouvelle autorité ? | **Non** : STATUS et PRECONDITION sont déjà généraux | **Non** : ACTION 273 est la règle ; l'outil s'aligne | **Non** : READING_MAP 95 promet déjà la règle | **Non** : sous-titres existants, aucun nouveau propriétaire | Non |
| Testable ? | Machine (R-02) et gardes | Machine (C4-01 à C4-P4) | Machine (R-01) | Mesure (R-03 à R-06) | Mutations (V-01 à V-04) |
| Positif / défensif équilibré ? | Oui | **Oui, gain positif** : LITE honnête valide en strict | Oui | **Oui** : route LITE ≤ 60 lignes | Oui |
| Suppression ou fusion ? | **Suppression** d'une colonne (« Sortie à conserver ») | **Alignement** | **Routing** et **test** | **Simplification** | **Validateur** et **fusion** des deux analyseurs |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Principe : **un seul résolveur, défini par une règle, servi par un seul outil, vérifié par ce même outil.**

### 4.1 Résolution (F-DIR-028, F-ACT-001 volet outil, F-VRM-001)

**O-1. `read_route.py` : résolveur en trois étapes**, exposé comme fonction importable :

| Étape | Règle |
|---|---|
| 1. Table | Entrée exacte de la table « Locators principaux » (raccourcis et sous-locators) |
| 2. Préfixe | Titre **unique** du fichier propriétaire qui **commence par le locator** (nu ou entre accents graves), suivi d'une espace, d'un tiret long ou de la fin de ligne |
| 3. Sous-locator `X/Y/Z` | Sous-titre commençant par `Z` **à l'intérieur du bloc** de `X/Y`, résolu récursivement. Exemples : `SAVOIR/CRAFT/CFT-01`, `ACTION/GATE-B/B3` |
| Refus | Plusieurs titres → « **locator ambigu** », avec les candidats. Aucun titre → « locator inconnu » (actuel) |
| Extraction | Un bloc servi **exclut les sous-blocs qui portent leur propre locator**. Une ligne-marqueur les signale (« `DIRECTION/CREATIVE-BOOT` : servi séparément »). Les sous-sections sans locator restent dans le bloc |
| Blocs de code | Les titres placés dans un bloc de code sont ignorés : c'est **F-RRT-001 (E2)**, appliqué dans le **même cycle d'outil** |

**Choix de méthode, déclaré.** L'hypothèse gelée B02 (lot 1) indexait **70 locators dans une table**. **Je ne la suis pas.** La règle de l'étape 2 est déjà promise par READING_MAP 95. Elle sert 53 des 56 locators cités sans rien maintenir, alors qu'une table exhaustive doit être tenue à jour à chaque titre. **B02 reste gelée ;** ce choix ne l'adopte ni ne la rejette.

**O-2. `validate_reading_map.py` : il importe le résolveur d'O-1**, au lieu d'avoir un second analyseur.

| Contrôle | Motif (A2) | Mutation qui doit virer au rouge |
|---|---|---|
| Unicité des locators de la table | « locator en double » | V-02 |
| La destination d'une ligne commence par son locator, ou par la chaîne parente pour un sous-locator | « ne correspond pas au locator » | V-01 (RUN-LITE ouvre RUN-ITER) |
| Propriétaire = fichier du préfixe | « propriétaire incohérent » | V-04 |
| **Couverture** : tout locator cité dans les fichiers officiels et la skill est résolu | « locator cité non résolu » | V-03 (titre ACTION/STATUS renommé) |
| Unicité des titres porteurs d'un locator, dans tous les propriétaires | « locator ambigu » | R-07 |
| La contrainte « ≥ 10 lignes » | **Retirée** : elle n'est plus la seule | — |

### 4.2 Granularité (F-RM-003)

| # | Où | Quoi |
|---|---|---|
| T-4 | **READING_MAP, table** | **Une seule ligne ajoutée** : `DIRECTION/START/TREE` → `DIRECTION.md` — `## DIRECTION/START — classer avant d'agir` › `### Arbre de classification`. Les autres sous-blocs utiles sont servis par la règle (étape 3) ou par l'exclusion des sous-blocs à locator |
| T-6 | **Skill, DIRECTION 86, QUICKSTART** | Skill 79 : « `DIRECTION/START` (arbre seulement) » devient `DIRECTION/START/TREE`. Les six occurrences de « `SAVOIR/CRAFT — CFT-00` » (DIRECTION 86, QUICKSTART ×3, skill ×2) deviennent `SAVOIR/CRAFT/CFT-00` |

**Effet mesurable, et critère de sortie :**

| Ce qui est servi | B01 | Après |
|---|---|---|
| `DIRECTION/START/TREE` | refusé | ≤ 25 lignes (arbre : 19) |
| `DIRECTION/START` (sortie immédiate et mémoire gardées, Boot et Domain Frame exclus) | 130 lignes | ≤ 75 |
| Route LITE complète | 158 lignes | ≤ 60 |

### 4.3 Carte de lecture d'ACTION (F-ACT-001, volet normatif)

| # | Où | Quoi |
|---|---|---|
| T-1 | **ACTION 7** | « commencez par `ACTION/RUN` » devient : « commencez par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode `ACTION/RUN-<MODE>` » |
| T-2 | **ACTION 13–21** | **Socle pour tous les modes** : `ACTION/STATUS`, `ACTION/PRECONDITION`. Les lignes gardent le chargement propre au mode, écrit en **locators complets** (« gates A/B/C » devient `ACTION/GATE-A`, `ACTION/GATE-B`, `ACTION/GATE-C`). La colonne « **Sortie à conserver** » est **supprimée** et remplacée par un renvoi à `ACTION/CLOSE-PACKAGE`. C'est le principe de C2 : c'était un sixième résumé de clôture, divergent (sa ligne LITE omet le verdict) |
| T-5 | **DIRECTION 300** | Le titre « `### DIRECTION/START — traduction humaine minimale` » devient « `### Traduction humaine minimale de DIRECTION/START` ». Il ne porte plus le locator. Le contenu est inchangé |
| T-3 | **READING_MAP 93–95** | Décrit les trois étapes d'O-1, le refus d'ambiguïté et l'exclusion des sous-blocs à locator. La table est déclarée « **raccourcis et sous-locators** », pas un inventaire |

### 4.4 `trace_locator` et profil strict (F-ACT-020)

Une règle par mode, **la même dans les deux profils** :

| Mode | `trace_locator` |
|---|---|
| STANDARD, DIRECTION, SYSTÈME | Requis (existant) |
| **ITER** | **Requis dans toute RUN_CARD sérialisée** (**INV-C4-1**). Une RUN_CARD JSON est une trace persistante (HANDOFF 33 : « un run persistant utilise la projection RUN_CARD »). Un ITER éphémère vit dans la mémoire locale **sans** RUN_CARD (DIRECTION 241) |
| LITE | Facultatif : l'artefact localement évident sert de locator (ACTION 273) |

**INV-C4-2, profil strict.**
- Le strict applique **les mêmes exigences par mode** que le normal.
- Il ajoute seulement trois contrôles :
  - le rejet des placeholders ;
  - le rejet des hôtes de démonstration ;
  - l'**existence des locators locaux, résolus depuis le dossier de la carte** (`source_path`), et non plus depuis la racine du package.
- Une LITE sans `trace_locator` dont l'artefact existe est donc valide en strict.

**Sous-décision : résolution relative.** Elle n'est pas dans le texte de la fiche. Je la rattache à F-ACT-020, parce que la fiche demande un « profil strict **documenté** ». Documenter le comportement actuel (« chemins relatifs à la racine du package qui valide ») reviendrait à documenter un défaut. **F-VRC-004** (hôtes de démonstration acceptés pour `artifact.locator`) **reste en E2**, appliquée dans le même cycle d'outil.

| # | Où | Quoi |
|---|---|---|
| T-7 | **ACTION/RUN_CARD** (« Frontière de validation ») | Deux phrases : « Le **profil strict** applique les mêmes exigences par mode que la validation normale. Il ajoute le rejet des placeholders et des hôtes de démonstration, et l'existence des locators locaux, résolus depuis le dossier de la carte. » QUICKSTART 118–124 et README 100 y renvoient |
| T-8 | **ACTION 273** (ligne TRACE-LOCATOR) | « ITER persistant » devient « ITER (toute RUN_CARD sérialisée ; un ITER éphémère reste en mémoire locale, sans RUN_CARD) » |

**Coordination :**
- **F-DIR-036 (D2)** demande « trace_locator **ou** référence de direction » pour ITER. La partie `trace_locator` est décidée ici. D2 ne décidera que la **référence de direction** rappelée ; la fiche reste en D2.
- **F-GLO-001 (E1)**, sur la définition de la RUN_CARD par la persistance, appliquera la même définition que T-8.

### 4.5 Ce qui n'entre pas dans la liste close

La liste close D-ACT-1 porte les invariants sur les **artefacts produits par un run** (RUN_CARD, contrats). Les contrôles d'O-2 portent sur l'**outillage documentaire** : ils vont dans l'inventaire des outils (§6), pas dans la liste. Je le déclare pour qu'aucune frontière ne change en silence.

## 5. Liste close

| ID | Invariant | Fiche |
|---|---|---|
| **INV-C4-1** | Mode ITER ⇒ `trace_locator` non vide (profil normal comme strict) | F-ACT-020 (et F-DIR-036, partie trace) |
| **INV-C4-2** | Profil strict = exigences par mode du profil normal, plus placeholders, hôtes de démonstration et existence des locators locaux résolus depuis le dossier de la carte. LITE sans `trace_locator` valide si l'artefact résout | F-ACT-020 |

**Liste close : 70 lignes, 66 actifs.**

## 6. Inventaire à date : ajouts C4

| Objet | Changement | Nature |
|---|---|---|
| `run_card.schema.json` | **Aucun** | — |
| `validate_run_card.py` | INV-C4-1 dans le contrôle sémantique ; `check_strict_contract` aligné (INV-C4-2), avec `source_path` utilisé | validateur |
| `read_route.py` | Résolveur en trois étapes, refus d'ambiguïté, exclusion des sous-blocs à locator, blocs de code ignorés (avec F-RRT-001) | outil |
| `validate_reading_map.py` | Import du résolveur ; unicité, correspondance, propriétaire, couverture, unicité des titres ; retrait du seuil « ≥ 10 » | outil |
| Suite A2 | Cas V-01 à V-04 et R-01 à R-07 ajoutés aux oracles | tests |

**F-ACT-020 est réglé sans changement de schéma.** Candidats encore ouverts pour la migration unique : C9 et D2.

## 7. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **O-2 avant toute modification de locator** (F-VRM-001 est le prérequis déclaré par le registre). Ensuite O-1, puis T-3 à T-6 |
| C2 | **Un cycle d'outil** : O-1, O-2, F-RRT-001 et F-VRC-004 (E2) ensemble ; le validateur RUN_CARD dans la migration unique (INV-C4-1 et C4-2) |
| C3 | **Passe ACTION unique** : T-1, T-2, T-7 et T-8 rejoignent la passe déjà fixée (C1, C2, C3, B5) |
| C4 | **Aucun titre renommé** sauf DIRECTION 300. Aucun locator existant ne doit cesser de résoudre : la couverture d'O-2 le vérifie |
| C5 | **Relecture complète** de READING_MAP ; ACTION 1–21, 252–334 ; DIRECTION 119–310 ; QUICKSTART 110–126 ; README 95–105 ; skill 70–90 |

## 8. Condition de sortie (phase 13)

1. `C4_harnais_non_regression.py` : témoins **3/3**, RUN_CARD **6/6**, résolution **7/7**, validateur de carte **4/4**, gardes **7/7**. Harnais A1 à C3 verts.
2. **Épreuve outillée** (test de la fiche F-ACT-001) : un scénario par mode, exécuté **uniquement** avec READING_MAP et `read_route.py`. Les sections chargées sont comparées au socle et à la ligne du mode de la carte d'ACTION.
3. **Mesure** : la route LITE de 9.08 est rejouée, **≤ 60 lignes servies** (contre 158). La mesure est déterministe ; elle ne prouve pas que le lecteur **comprend** mieux, seulement qu'il lit moins.
4. **Profils** : 5 modes × normal / strict × trace présente / absente × artefact local présent / absent. Un même résultat par mode dans les deux profils, hors contrôles propres au strict.

**Limite déclarée.** L'exclusion des sous-blocs peut retirer un contenu qu'un lecteur attendait sous START. La ligne-marqueur le rend visible, et l'épreuve outillée (point 2) le vérifie.

## 9. Sortie

- **PATCH-DECISION C4 : CORRIGER.**
  - 2 invariants RUN_CARD ;
  - 2 corrections d'outil (résolveur unique, validateur de carte) ;
  - 8 corrections de texte ;
  - 2 sous-décisions : résolution relative au dossier de la carte ; B02 non suivie pour la table exhaustive ;
  - 1 constat nouveau, rattaché à F-VRM-001 : le titre en double DIRECTION 300.
- **Liste close : 70 lignes, 66 actifs.** Aucun changement de schéma.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Le refus des locators n'était pas un problème de table trop courte, mais une **promesse de résolution jamais implémentée**. Une règle remplace une table de 70 lignes à maintenir.
- Le surcoût de START venait moins de l'arbre que des **sous-blocs qui ont déjà leur locator**.
- Deux analyseurs deviennent un : la validation vérifie désormais ce que le lecteur sert réellement.

**Prochaine unité : 11.12 PATCH-DECISION C5** (façades lues seules, D-FAC-1 : 10 fiches, dont F-VRM-003, le test de cohérence de façade dont dépendent C3 et d'autres grappes).
