# V1.2 — Unité 08 — Lecture intégrale des façades (B05)

**Date :** 2026-09-27 · **Lecteur :** même modèle que l'auteur des patchs (auto-comparaison) · **Objet :** les cinq façades humaines de `package/` :

| Fichier | Lignes | Mots |
|---|---|---|
| `V1/official/QUICKSTART.md` | 320 | 3 783 |
| `README.md` (racine du package) | 161 | 1 856 |
| `V1/official/README.md` | 52 | 695 |
| `V1/official/GLOSSAIRE.md` | 71 | 1 379 |
| `V1/official/ORCHESTRATION_MAP.md` | 53 | 823 |

Avec la skill et READING_MAP (`V12_07`), les façades totalisent **≈ 13 100 mots**, presque autant que DIRECTION (13 478).
**Question :** mêmes objectifs que `V12_05` à `V12_07`. Question propre à cette unité : **les façades convergent-elles vers un seul chemin, ou chacune en propose-t-elle un ?**
**Méthode :** lecture intégrale des cinq fichiers ; comparaison ligne à ligne avec DIRECTION (absolus, `START/TREE`, `EXTERNAL-START`), la skill et READING_MAP ; diff depuis l'import (`ea3bb92`) pour distinguer l'hérité de ce que les lots 1 et 2 ont touché.

## 1. Carte

| Fichier | Contenu | Public déclaré |
|---|---|---|
| QUICKSTART | Démarrage 90 s ; carte rapide ; §1 profondeur (façade d'activation, bénéfice, Creative Boot, constitution, table « si vous avez… ») ; §2 chemin 30 s ; §3 parcours 5 min (deux boucles, table de diagnostic) ; §4 choix du mode ; §5 table de charge ; §6 qualité du premier rendu (copie des 8 dimensions) ; §7 one-shot ; §8 handoff agentique ; §9 exemple complet ; §10 observer ; §11 fermer ; §12 sources | Humain (« vous ») et agent (« tu ») |
| README racine | Fiche de version ; par où commencer (90 s, chemin court) ; constitution ; double boucle ; structure du dépôt ; distributions ; validation (et ce qu'atteste une `RUN_CARD`) ; limites ; profils de lecture | Designer, reviewer, agent, mainteneur |
| README `V1/official` | Mission ; commencer ici ; cartes ; sources normatives ; constitution ; chemin actif ; limites | Lecteur du corpus |
| GLOSSAIRE | 40 termes ; 6 exemples express ; « commencer sans vocabulaire » | Débutant |
| ORCHESTRATION_MAP | Principe ; 9 combinaisons par résultat ; variation créative ; garde-fous ; arrêt | Agent ou lead qui compose |

**Mesures (certain)**

| Fichier | Négations défensives | Formules d'auto-limitation¹ | Jetons internes distincts | « beau / beauté » |
|---|---|---|---|---|
| QUICKSTART | 37 | 12 | 58 | 2 |
| README racine | 23 | 13 | 29 | 1 |
| README `V1/official` | 11 | 7 | 22 | 1 |
| GLOSSAIRE | 24 | 6 | 40 | 0 |
| ORCHESTRATION_MAP | 13 | 6 | 30 | 1 |
| *Rappel : SKILL, READING_MAP* | *46, 12* | *9, 7* | *82, 66* | *2, 1* |

¹ « ne crée ni… », « non normatif », « font foi », « ne remplace pas », « aucune règle »…

**Sur l'ensemble des façades :** 166 négations et 60 formules par lesquelles une façade rappelle qu'elle n'est pas la source.

**Touché par les lots 1 et 2 (diff depuis l'import) :** QUICKSTART seulement :
- l.45 (Creative Boot, prise de brief) ;
- l.58 (table) ;
- §9, où l'exemple passe de l'anti-direction à `MODAL`/`PARTI`.

Tout le reste est hérité de V1.1.1.

## 2. Ce qui est solide

1. **La table de diagnostic de QUICKSTART §3** (l.98-105) : défaut local → corriger ; défaut de craft → résoudre la relation ; direction faible → rouvrir avant de polir ; risque changé → reclassifier ; preuve insuffisante → déclarer ; décision établie → arrêter le polish. **C'est un vrai geste de senior** : diagnostiquer le type de défaut avant de choisir le geste. Il est absent de la skill.
2. **Les six questions de revue créative** (QUICKSTART §10, l.284-289) : direction visible, détail qui porte la spécificité, défaut dominant, ce qui a changé, ce que la correction a affaibli, corriger, rouvrir ou maintenir. Concrètes et courtes.
3. **L'exemple complet de QUICKSTART §9** : c'est le seul exemple du système qui montre une **décision de design** et pas seulement une trace :
   - une thèse ;
   - un `MODAL` et un `PARTI` concrets ;
   - un défaut mobile observé ;
   - une correction formulée en gestes : « rapprocher l'objet et le titre, réduire la saillance du CTA secondaire, réviser le crop ».
4. **ORCHESTRATION_MAP** :
   - le principe (l.9) : « ne pas charger le maximum de routes ; composer le maximum de contribution pertinente » ;
   - la variation créative : **« faire varier un axe situé à la fois »** (l.31) ;
   - la seule table du système où « Beauté, goût et craft situés » est **un résultat de premier rang** (l.18) ;
   - la conclusion (l.52) : « la richesse de lecture n'est pas un résultat ».
5. **L'honnêteté du README racine** :
   - fiche de version avec l'efficacité `NOT-VERIFIED` ;
   - paragraphe « ce qu'atteste / n'atteste pas une `RUN_CARD` validée » (l.145) : exemplaire.
6. **Les définitions de design du GLOSSAIRE** (craft, polish, créativité située, goût situé, spécificité, premier objet) : simples, positives, bien écrites.
7. **« Une trace complète sans conséquence est du slop procédural »** (QUICKSTART l.307, README l.149) : le système nomme lui-même son risque de rituel.

## 3. Problèmes observés

### 3.1 Aucune entrée unique : les façades se renvoient les unes aux autres (certain)

| Façade | Dit de commencer par… |
|---|---|
| README racine | QUICKSTART, puis GLOSSAIRE ; profil « Agent » : QUICKSTART **puis** SKILL (l.159) |
| README `V1/official` | QUICKSTART, puis GLOSSAIRE, READING_MAP, ORCHESTRATION_MAP |
| QUICKSTART | READING_MAP si la demande est identifiable, sinon `DIRECTION/START` (l.31) |
| READING_MAP | « Lire QUICKSTART **ou** cette carte » (l.14) |
| SKILL | README **et** QUICKSTART, puis ORCHESTRATION_MAP (l.53) |
| ORCHESTRATION_MAP | « `READING_MAP.md` résout le premier chemin » (l.27) |

**Conséquences :**
- chaque façade se déclare dérivée et renvoie à une autre : le circuit n'a pas de point de départ ;
- pour un agent, le point de départ réel est la skill, qui l'envoie lire 5 639 mots de README et de QUICKSTART **avant** `DIRECTION/START` ;
- **deux README** coexistent (racine, 1 856 mots ; `V1/official`, 695 mots) et se recouvrent : constitution, table des sources, chemin, limites.

### 3.2 La même activation est dite huit fois, sous cinq minutages (certain)

Les « cinq éléments » (mode, risque, décision, prochaine preuve, owner) apparaissent dans :
- SKILL « Activation en 30 secondes » ;
- README racine « Démarrage express — 90 secondes » **et** l.39 ;
- README `V1/official` l.17 ;
- QUICKSTART « Démarrage en 90 secondes », « Façade d'activation en cinq éléments », table « 30 secondes », **§2 « Le chemin en trente secondes »** ;
- GLOSSAIRE l.63.

Dans QUICKSTART, **la table des cinq questions est recopiée presque mot pour mot** à 46 lignes d'écart (l.19-25 et l.65-71). Les minutages se contredisent : 30 s, 90 s, 30 s, 5 min.

### 3.3 Six listes de chargement `DIRECTION`, aucune identique (certain)

| Source | Routes listées pour un run `DIRECTION` |
|---|---|
| SKILL, table de charge | `START`, `VISUAL_TARGET`, `FIRST-OBJECT`, `ACTION/ROUTING`, **`FIRST-RENDER`**, `RUN-DIRECTION`, `CFT-00`, gates A/B/C |
| QUICKSTART §5 | `START`, `VISUAL_TARGET`, `FIRST-OBJECT`, **`DOUBLE-LOOP`**, `RUN-DIRECTION`, `CFT-00`, « gates applicables » |
| QUICKSTART §4 | `START`, `VISUAL_TARGET`, `CFT-00`, `RUN-DIRECTION` (sans `FIRST-OBJECT`) |
| QUICKSTART §1, table | `CREATIVE-BOOT`, `VISUAL_TARGET`, `FIRST-OBJECT`, `DOUBLE-LOOP`, `CFT-00`, `RUN-DIRECTION` |
| READING_MAP | `START` → `VISUAL_TARGET` → `FIRST-OBJECT` → `RUN-DIRECTION` |
| ORCHESTRATION_MAP, « Direction forte » | `START`, `RUN-DIRECTION`, `VISUAL_TARGET`, `FIRST-OBJECT` |

**Conséquences :**
- **`ACTION/FIRST-RENDER`**, la route « qualité initiale attendue », la plus proche de l'objectif de l'owner, **n'apparaît que dans la skill et dans la ligne « Beauté » d'ORCHESTRATION_MAP**. Elle est absente de QUICKSTART et ne figure dans READING_MAP que comme locator, pas dans le routage `DIRECTION` ;
- « le chemin d'un run `DIRECTION` » n'a pas de définition unique. Le budget de lecture dépend de la façade suivie. C'est pourquoi le plan V1.2 (« environ 1 300 lignes »), l'outil de budget (614 lignes) et le chemin prescrit par la skill (≈ 1 460 lignes, ≈ 20 700 mots, `V12_07` §3.1) ne mesurent pas la même chose ;
- les 50 conditions de `validate_reading_map.py` sont vertes alors que ces six listes divergent. **Les gardes synchronisent des phrases, pas la structure.**

### 3.4 Cinq formulations du chemin et deux modèles de boucle (certain)

**Formulations du chemin :**
- README racine : « Classer → diriger → construire → observer → corriger → fermer » ;
- QUICKSTART : « … → corriger, résoudre, rouvrir ou décider → persister » ;
- SKILL : « … → vérifier → corriger → fermer » ;
- README `V1/official` et `flow.md` : « Classer et protéger → cultiver et diriger → composer et construire → polir et observer → vérifier et corriger → décider et fermer » ;
- GLOSSAIRE : en quatre étapes.

**Deux modèles de boucle incompatibles :**
- **création / gouvernance** (README `V1/official`, `flow.md`) : les deux boucles « restent distinctes », la gouvernance classe le risque ;
- **création / amélioration** (QUICKSTART §3) : la boucle 1 **inclut** « classer le risque » ;
- README racine combine les deux : « Boucle de gouvernance **et** d'amélioration ».

Un lecteur ne sait pas si la seconde boucle sert à **améliorer le rendu** ou à **gouverner le risque**. Pour la machine à faire du beau, la différence est centrale.

### 3.5 Les absolus dérivent d'une façade à l'autre (certain pour le texte)

| Lieu | Absolu 2 (ancrage) | Absolu 4 (déclaration) |
|---|---|---|
| DIRECTION (canonique) | Ancre **fraîche et inspectable** avant le premier rendu d'une surface `DIRECTION` ; sans elle, axes `NOT-VERIFIED` et livraison validée bloquée | Mode, décision, risque, preuve minimale, condition d'arrêt ; budget en jalons |
| QUICKSTART | « ancre fraîche et inspectable » | « mode, prochaine preuve et budget » |
| README racine | « pas dessinée uniquement de mémoire » | « mode, preuve et budget » |
| READING_MAP, README `V1/official` | « ancre inspectable » (sans « fraîche ») | « mode et prochaine preuve » |
| SKILL | « ancre inspectable **ou une limite explicite lorsqu'une référence guide la décision** » | « mode, scope, prochaine preuve, capacité réellement disponible » |

**Constat :** la skill, seul fichier chargé à coup sûr, porte une version **conditionnelle et assouplie** de l'absolu 2. En pratique, c'est la « version légère de l'ancrage » que `V12_05` piste 3 propose de décider, mais elle est entrée par dérive silencieuse et non par décision. **Signalé, non corrigé.**

### 3.6 La prise de brief perd une condition en passant dans les façades (certain)

- **Canonique** (`EXTERNAL-START` l.27) : « au plus trois demandes … contenu réel, marque, asset principal ou route autorisée, **destination si elle n'est pas évidente** ».
- **Façades** (QUICKSTART l.45, SKILL l.119) : « au plus trois intrants, dans cet ordre : contenu réel, marque, asset principal, destination ». La condition disparaît, et la phrase se lit comme **quatre** demandes pour un plafond de trois. C'est l'origine du défaut noté en `V12_07` §3.8. Il vient de nos propres textes du lot 1 (P-B), qui ont compressé la phrase canonique.

**Tension de source (probable) :**
- `START/TREE` étape 6 : « Si aucune réponse n'est nette, pose une clarification ciblée. Ne devine pas. » ;
- `EXTERNAL-START` : « le rendu est construit dans tous les cas » ;
- QUICKSTART §4 (l.141) juxtapose les deux : « Clarification ou `EXTERNAL-START` avant le mode ».

Rien ne dit laquelle prévaut sur un brief vague avec humain présent. La clarification porte sur le mode, la prise de brief sur les intrants : les deux sont compatibles, mais aucun texte ne le dit.

### 3.7 GLOSSAIRE : un lexique de la preuve, en retard sur V1.2 (certain)

- Sur 40 termes, **environ 30 relèvent de la gouvernance et de la preuve** (statuts, verdicts, états, locators, owner, scope…) et **10 du design** (direction, DA, craft, polish, créativité et goût situés, spécificité, premier objet, boucle, JTBD).
- **Termes absents**, alors qu'ils sont sur le chemin d'un run :
  - **ancre**, alors que l'absolu 2 repose dessus ;
  - thèse ;
  - Creative Boot ;
  - `MODAL`, `PARTI`, `FABRICATION` (lot 1) ;
  - objet de preuve ;
  - défaut dominant ;
  - vérité de scène et `ILLUSTRATIVE` ;
  - plafond (lot 2) ;
  - atlas ;
  - slop.
- **Les lots 1 et 2 n'ont pas mis le glossaire à jour** : c'est un oubli de nos patchs. **Signalé, non corrigé.**
- Les « exemples express » ne le sont pas toujours : l'exemple `CLOSED` (l.59) fait environ 80 mots de règles de verdict.

### 3.8 Deux registres, trois publics, aucun client (certain pour le texte ; probable pour l'effet)

- QUICKSTART vouvoie (23 impératifs) et tutoie (15), dans le même paragraphe par endroits (l.41-47). C'est hérité de V1.1.1 : la trace de textes écrits pour des lecteurs différents puis fusionnés.
- Les façades s'adressent au designer, au reviewer, au mainteneur et à l'agent. **Aucune n'est écrite pour le client lambda.** C'est normal si l'agent traduit pour lui, mais :
  - le seul format d'entrée humain proposé est le handoff agentique (QUICKSTART §8 : `OBJECTIVE`, `SCOPE`, `AUTONOMY`, `CONFIRMATION`, `CONSTRAINTS`, `OUTPUT`), un format d'expert ;
  - le chemin du non-spécialiste n'existe que dans la délégation de la skill et dans `EXTERNAL-START`.

### 3.9 Le contenu positif est dupliqué plutôt que placé (certain)

| Contenu | Nombre de lieux |
|---|---|
| Table des 8 dimensions du premier rendu | 2 (`FIRST-OBJECT`, QUICKSTART §6, copie déclarée) |
| Définition du polish | 4 (SKILL, QUICKSTART, GLOSSAIRE, README racine) |
| Table des sources normatives | 3 (deux README, QUICKSTART §12) |
| Constitution minimale | 6 (DIRECTION, SKILL, READING_MAP, QUICKSTART, deux README) |
| « Une capture prouve un rendu dans son scope… » | 2 (QUICKSTART, README racine) |
| « slop procédural » | 2 |

Les meilleurs outils de fabrication des façades (table de diagnostic, six questions de revue, « un axe à la fois ») ne sont, eux, **dans aucun fichier chargé à coup sûr**.

### 3.10 Mineurs (certain ; signalés, non corrigés)

1. QUICKSTART l.267 commence par une espace (« ` Pour une RUN_CARD…` »).
2. QUICKSTART §7 : le one-shot ne supprime pas « la persistance des preuves, limites et décisions ». C'est cohérent avec ACTION, mais cela rend le one-shot aussi lourd en trace qu'un run itératif (`V12_06` §6.2).
3. Titres « V1.1.1 » sur B05 : connu, la version n'est pas encore relevée.

## 4. Relations

- Les façades **dérivent** des sources et sont tenues cohérentes par les gardes LCF (50 conditions) et les harnais. §3.3 et §3.5 montrent que cette cohérence porte sur des phrases : des divergences de structure (listes de chargement, absolus, prise de brief) passent au vert.
- **Poids :** ≈ 13 100 mots de façades pour ≈ 27 750 mots de DIRECTION et ACTION. Une partie des façades est lue à chaque run (skill, READING_MAP, et QUICKSTART et README si la skill est suivie à la lettre).
- **Diagnostic commun aux quatre lectures (`V12_05` à `V12_08`), probable :**
  1. **accrétion par audit** : chaque audit ajoute une protection, une copie ou un renvoi, rarement une suppression ;
  2. **architecture pensée à partir de la preuve** : la fabrication est décrite, exigée et contrôlée, mais jamais outillée sur le chemin court ;
  3. **gardes sur des phrases** : elles figent le texte et laissent passer la divergence de structure.

## 5. Écart aux objectifs

| Objectif | État dans les façades | Écart |
|---|---|---|
| Machine à faire du beau | Table de diagnostic, revue créative, exemple §9, « un axe à la fois », ligne « Beauté » | Outils présents mais hors du chemin chargé ; `FIRST-RENDER` absent de deux listes |
| Brief flou, non-spécialiste | `EXTERNAL-START` résumé | Condition perdue (§3.6) ; entrée humaine en format expert (§3.8) |
| Connaisseur | Profils de lecture, orchestration | Bon, mais six listes et cinq chemins à réconcilier |
| Économe | Condition d'arrêt, « richesse de lecture n'est pas un résultat » | Huit activations, deux README, six constitutions ; 13 100 mots de façades |
| Vrai | README, fiche de version, frontière de la `RUN_CARD` | Solide |

## 6. Pistes (à décider, rien n'est appliqué)

1. **Une entrée par public.**
   - **Agent** : la skill seule, noyau de fabrication (`V12_07` piste 1). Elle ne renvoie plus à README ni à QUICKSTART pendant un run.
   - **Humain** : un seul README (fusion des deux), qui renvoie à QUICKSTART comme guide.
2. **Une seule liste de chargement par mode**, écrite une fois (table de charge de la skill ou fichier de données). Les autres façades y renvoient. Une garde **de propriété** vérifie l'égalité au lieu de lire des phrases (piste 5 de `V12_05`). `FIRST-RENDER` y figure.
3. **Un seul chemin et un seul modèle de boucle**, énoncés une fois. Recommandation (probable) : **création / amélioration**, la gouvernance devenant la condition de sortie et non une boucle.
4. **Absolus :** un résumé canonique unique, repris par renvoi. **Décider explicitement** la version légère de l'ancrage pour le brief vague, au lieu de la dérive actuelle de la skill (§3.5).
5. **Prise de brief :**
   - rétablir la condition canonique (« destination si elle n'est pas évidente ») dans la skill et QUICKSTART ;
   - dire que la clarification de mode (`START`) et la demande d'intrants (`EXTERNAL-START`) se font dans le même et unique échange, puis que l'agent construit.
6. **GLOSSAIRE :** ajouter le vocabulaire de fabrication (ancre, thèse, `MODAL`, `PARTI`, `FABRICATION`, objet de preuve, défaut dominant, vérité de scène, plafond, slop) ; regrouper les statuts dans une sous-partie « preuve ».
7. **Remonter dans le noyau** les trois outils de fabrication des façades : la table de diagnostic (QUICKSTART §3), les six questions de revue (§10), « un axe à la fois » (ORCHESTRATION_MAP). Les copies (constitution, polish, sources, handoff) sont remplacées par des renvois d'une ligne.
8. **QUICKSTART** : garder une seule activation, retirer la seconde table des cinq questions, choisir un registre (vouvoiement pour l'humain).

Les pistes 2, 5 et 6 corrigent en partie des incohérences : elles relèvent d'une PATCH-DECISION, comme le reste (règle 3).

## 7. Lecture

- **Certain :**
  - les mesures ;
  - le circuit d'entrée sans point de départ ;
  - les huit activations ;
  - les six listes de chargement divergentes et l'absence de `FIRST-RENDER` dans deux d'entre elles ;
  - les cinq chemins et les deux modèles de boucle ;
  - la dérive de l'absolu 2 dans la skill ;
  - la condition perdue de la prise de brief (introduite par le lot 1) ;
  - le glossaire non mis à jour par les lots 1 et 2.
- **Probable :**
  - que ces divergences coûtent de l'attention à l'agent et rendent le budget non mesurable ;
  - que le diagnostic commun (accrétion, preuve d'abord, gardes sur des phrases) explique l'essentiel des quatre lectures.
- **Hypothétique :**
  - qu'une entrée unique avec une liste de chargement unique réduise la charge d'environ un tiers ou plus sans perte ;
  - que les outils de fabrication remontés dans le noyau améliorent le rendu. À vérifier par épreuve.
- **Limite :** lecture en auto-comparaison ; aucun regard extérieur.

## 8. Suite

La lecture du chemin d'entrée est complète (DIRECTION, ACTION, skill, READING_MAP, façades). Il reste :
- **SAVOIR et BIBLIOTHEQUE**, quand l'owner le décide ;
- puis la **mini-épreuve V1.2** ;
- puis le chantier « structure et budget », qui peut désormais s'appuyer sur les pistes de `V12_05` à `V12_08`.
