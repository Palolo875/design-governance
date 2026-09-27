# V1.2 — Unité 07 — Lecture intégrale de la skill et de READING_MAP (B05)

**Date :** 2026-09-27 · **Lecteur :** même modèle que l'auteur des patchs (auto-comparaison) · **Objet :** `skills/design-governance-practice/` (SKILL.md, 165 lignes, 3 191 mots ; quatre références, 277 lignes, 2 377 mots) et `V1/official/READING_MAP.md` (130 lignes, 1 412 mots).
**Question :** mêmes objectifs que `V12_05` et `V12_06`. Question propre à cette unité : **le chemin d'entrée conduit-il l'agent vers la fabrication ou vers la procédure ?**

## 1. Carte

### SKILL.md

| Lignes | Bloc | Fonction |
|---|---|---|
| 1–4 | Frontmatter (`description`) | Déclenchement de la skill |
| 8–12 | Rôle | « couche d'activation », non-autorité |
| 14–32 | Carte de lecture et sortie | Deux formats de sortie (réponse visible, handoff) |
| 34–48 | Activation en 30 s, constitution minimale | Résumé des cinq absolus |
| 50–59 | Préparer le contexte | Ordre de lecture (README, QUICKSTART, ORCHESTRATION_MAP, START…) |
| 61–75 | Routage et handoff, routes conditionnelles | Qui charger |
| 77–83 | Délégation humain-agent | Activation silencieuse, réponse visible |
| 85–109 | Noyau d'exécution, **table de charge obligatoire**, approfondir, activation positive | Charge documentaire |
| 111–143 | Classer, **Diriger**, Construire, Vérifier, Corriger et fermer | **Seul bloc de fabrication** |
| 145–149 | Anti-slop opératoire, polish | Critères de craft (négatifs puis une définition du polish) |
| 151–165 | Sortie attendue, références conditionnelles | Clôture, renvois |

### Références

| Fichier | Mots | Fonction | Charge réelle |
|---|---|---|---|
| `examples.md` | 933 | Trois runs illustratifs (LITE, DIRECTION, STYLE, SYSTÈME) | Si parcours ambigu |
| `flow.md` | 230 | Flux Mermaid en sept étapes | Vue rapide |
| `machine_projection.md` | 956 | YAML de `RUN_CARD` | Si sérialisation |
| `canonical_minimum.md` | 258 | Séparations de statuts si les sources manquent | Secours |

### READING_MAP.md

Utilisation, chemin canonique en six étapes, **constitution minimale** (encore), routage par décision (7 lignes), activation multi-perspective (11 perspectives × 5 colonnes), **handoff minimal** (encore), résolution des routes, 25 locators, condition d'arrêt.

**Mesures (certain) :**
- SKILL : 46 négations défensives, 7 formules « ne crée ni / ne constitue ni / ne remplace », **82 jetons internes distincts** ;
- READING_MAP : 12 négations, 4 formules défensives, 66 jetons internes ;
- `examples.md` : les exemples sont des **traces de preuve** (`AXES`, `VERDICT`, `STATE`, `RESERVATION`) ; aucun ne montre un rendu, une composition ou un geste de craft.

## 2. Ce qui est solide

1. **La délégation humain-agent** (SKILL l.79-81) : l'agent active le système **silencieusement**, l'humain donne l'objectif et l'autonomie, et le détail n'est exposé que si l'humain demande « pourquoi ? ». C'est exactement la posture voulue pour un non-spécialiste.
2. **La table de charge par mode** (l.93-99) : un vrai outil de proportionnalité, lisible d'un coup d'œil.
3. **Le bloc « Diriger »** (l.115-127), notamment : premier objet, objet de preuve codé, lentille premium (clarté, cohérence, précision, singularité maîtrisée, confiance), « ne confonds pas premium avec minimalisme ».
4. **La définition du polish** (l.149) : « résolution cohérente de la structure, du contenu, de la typographie… ; ce n'est pas une couche de blur, de gradients, d'ombres ». La meilleure phrase de craft de la skill.
5. **READING_MAP, condition d'arrêt** (l.129) : arrêter de lire quand la décision est assez explicite. Bon principe d'économie.
6. **`flow.md`** : court, clair, avec l'équivalent texte.

## 3. Problèmes observés

### 3.1 Le chemin d'entrée prescrit coûte environ deux fois le budget mesuré (certain)

La skill demande, pour un run `DIRECTION` :
- l.53 : lire `README.md` et `QUICKSTART.md`, puis `ORCHESTRATION_MAP.md` pour un résultat créatif ambitieux ;
- l.98 (table de charge) : `START`, `VISUAL_TARGET`, `FIRST-OBJECT`, `ACTION/ROUTING`, `FIRST-RENDER`, `RUN-DIRECTION`, `CFT-00` **et gates A/B/C** ;
- l.75 : `DOUBLE-LOOP` pour une direction ouverte.

| Poste | Mots |
|---|---|
| Budget mesuré par `V12_Budget_lecture.py` (SKILL, READING_MAP, 7 routes) | 9 591 |
| README (package) + QUICKSTART | 5 639 |
| ORCHESTRATION_MAP | 823 |
| `ACTION/ROUTING` + `CFT-00` | 963 |
| Gates A + B + C | 2 716 |
| `DOUBLE-LOOP` | 959 |
| **Total prescrit, lu à la lettre** | **≈ 20 700** |

**Conséquence :**
- l'outil de budget ne mesure qu'environ la moitié de ce que la skill prescrit (écart de périmètre, pas d'erreur de calcul). La baisse de 17 mots obtenue par les lots 1 et 2 est donc négligeable face à la charge réelle ;
- sur ces ≈ 20 700 mots, la fabrication (Diriger/Construire de la skill, `VISUAL_TARGET`, `FIRST-OBJECT`, `FIRST-RENDER`, `CFT-00`, Gate C) en représente **environ un quart à un tiers** (probable, estimation par blocs : 5 400 à 6 400 mots selon que la boucle est comptée ou non).

**Correction (`V12_11` §1) :** en suivant aussi le renvoi impératif de `RUN-DIRECTION` vers `PIPELINE-DIRECTION`, `VISUAL_PROOF`, `CLOSE-PACKAGE` et `HANDOFF`, le chemin prescrit atteint ≈ 23 600 mots (≈ 1 650 lignes).

**Déclaré :** l'outil `V12_Budget_lecture.py` n'est pas modifié. Un second périmètre « chemin prescrit » est proposé en piste (§6).

### 3.2 La consigne de chargement est dite quatre fois (certain)

- « Préparer le contexte » (l.50-59) ;
- « Routage et handoff » (l.61-75) ;
- « Table de charge obligatoire » (l.89-101) ;
- « Approfondir seulement si nécessaire » et « Activation positive » (l.103-109).

READING_MAP la redit une cinquième fois (chemin canonique, routage minimal, perspectives). Les versions ne disent pas exactement la même chose : l.53 fait lire README et QUICKSTART, alors que la table de charge ne les mentionne pas. **L'agent doit arbitrer entre ses propres instructions de chargement.**

### 3.3 La constitution et le handoff sont recopiés (certain)

- Les cinq absolus : DIRECTION, **SKILL l.40-46**, **READING_MAP l.24**, QUICKSTART (à vérifier à l'unité suivante).
- Le handoff : ACTION/HANDOFF, **SKILL l.26-30**, **READING_MAP l.62-76**.

Chaque copie porte sa mention « copie de façade », « ne crée ni mode, ni gate » : la duplication fabrique elle-même une partie du langage défensif. La cohérence est tenue par les gardes LCF, donc par vérification et non par construction (déjà noté en `V12_05` §4).

### 3.4 La sortie visible parle le langage du système, pas celui du client (certain pour le texte, probable pour l'effet)

La réponse visible par défaut est `MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER` (l.21).
- Pour un commerçant ou un client lambda, `MODE: DIRECTION` et `OWNER` ne veulent rien dire.
- La délégation (l.79) dit pourtant d'activer le système « silencieusement ».
- Observé sur B-DLA (V12_00) : les réponses C4 exposaient ce vocabulaire. C'est une contradiction interne de la skill.
- Un designer senior rend : **ce que j'ai fait, pourquoi, ce qui manque (assets, contenu), ce que je te propose ensuite**. Les champs internes vont dans la trace.

### 3.5 Le frontmatter oriente vers la procédure (probable)

La `description` (celle qui déclenche la skill et cadre l'agent) dit : « dirigé, poli et **vérifiable** … observer une **preuve** ou **sérialiser une RUN_CARD** ». Le mot « beau » n'apparaît pas, ni « designer », ni « niveau senior ». La première impression de l'agent est administrative.

### 3.6 Le craft est abstrait et formulé en négatif (certain pour le texte)

- « Diriger » énumère des **objets à déclarer** (thèse, silhouette, premier objet, relation de contenu, rôle d'asset, anti-direction, condition de retrait) et des **dimensions à examiner** (présence, point de vue, culture visuelle transformée…). Il ne donne aucun geste.
- « Anti-slop opératoire » est une liste de choses à **retirer**. Une liste négative pousse vers le moyen inoffensif, ce qui correspond au paradoxe anti-slop mesuré (6/6 rendus crème et brun sur B-DLA, probable).
- `examples.md` n'illustre que des traces : un débutant qui demande « comment faire » (l.56) reçoit des `VERDICT: ACCEPTED-WITH-RESERVATION`, pas un exemple de composition.
- **Ce qui manque**, déjà nommé en `V12_05` §3.5 : contraste d'échelle, un seul accent, lumière dirigée, texte dans la zone calme, deux familles au plus, cohérence de série, traitement unifié ; l'atelier d'édition (retrait, réduction, transformation) de `V12_06` §3.4.

### 3.7 READING_MAP : une carte de lecture qui se lit elle-même lourdement (probable)

- La table des perspectives (11 × 5) est utile pour un audit, mais pour un run elle demande 11 évaluations de déclencheur.
- La table des locators (25 lignes) sert surtout `read_route.py` : c'est une donnée machine placée dans une façade de lecture.
- La carte renvoie à `ORCHESTRATION_MAP`, qui est une deuxième carte : deux cartes pour un seul chemin.

### 3.8 Incohérences mineures (certain ; signalées, non corrigées)

1. **Vocabulaire** : SKILL l.117 « une anti-direction et une condition de retrait » ; l.119 « anti-directions concrètes » puis « `MODAL`/`PARTI` (d'où viennent les anti-directions) » ; `examples.md` l.32 « anti-direction » alors que le bloc montre `MODAL`/`PARTI`. Le lien est dit à l.119, mais le boot porte les deux vocabulaires.
2. **« Au plus trois intrants »** suivi de **quatre** éléments (contenu réel, marque, asset principal, destination), l.119. C'est la décision B (au plus trois demandes, choisies dans cet ordre de priorité parmi quatre), mais la phrase se lit comme une erreur de compte.
3. **Deux README** : la skill dit `README.md` sans chemin ; le package en porte un à la racine (1 856 mots) et un dans `V1/official/` (695 mots).
4. **« Ligne de run minimale »** (l.83) : troisième format de sortie, en plus de la réponse visible et du handoff.

## 4. Relations

- La skill est la **porte d'entrée réelle** de l'agent : c'est le seul fichier chargé à coup sûr. Tout ce qui n'y est pas dépend de la discipline de chargement, et §3.2 montre que cette discipline est ambiguë.
- Elle **résume** DIRECTION (constitution, classer, diriger) et ACTION (vérifier, fermer, handoff) sans en porter les meilleurs outils de fabrication (atelier d'édition, Gate C, passe créative, premier objet à huit dimensions : présents par renvoi seulement).
- READING_MAP, QUICKSTART, ORCHESTRATION_MAP et la skill forment **quatre façades d'entrée** au-dessus des dix vues d'entrée de DIRECTION (`V12_05` §3.2).
- Les gardes LCF 43 à 50 lisent des phrases de la skill (P-B, P-D, L2-G2) : toute réécriture de la skill passe par des rectifications de gardes (`V12_05` §3.9).

## 5. Écart aux objectifs

| Objectif | État dans la skill et READING_MAP | Écart |
|---|---|---|
| Machine à faire du beau | Exigence présente (Diriger, polish) | Aucun geste de craft ; anti-slop en négatif ; exemples en traces |
| Brief flou, non-spécialiste | Délégation silencieuse, prise de brief B | Sortie visible en jargon (§3.4) |
| Connaisseur | Table de charge, locators | Bon |
| Économe | Proportionnalité, condition d'arrêt | Chemin prescrit ≈ 20 700 mots ; chargement dit quatre fois (§3.1-3.2) |
| Senior | Lentille premium, polish | Posture d'auditeur dans le frontmatter et la sortie |

## 6. Pistes (à décider, rien n'est appliqué)

1. **Faire de la skill le noyau de fabrication.** C'est le seul fichier chargé à coup sûr, donc le bon lieu pour le noyau proposé en `V12_05` §6.1 et `V12_06` §6.1. Contenu visé, sur une à deux pages :
   - rôle de designer senior ;
   - classement en une ligne ;
   - prise de brief ;
   - **carte de gestes de craft** (positifs) ;
   - **boucle d'édition** (retrait, réduction, transformation ; comparer deux captures) ;
   - vérité (données, assets, plafond) ;
   - sortie.
2. **Une seule consigne de chargement** : la table de charge, avec README, QUICKSTART et ORCHESTRATION_MAP retirés du chemin d'un run (lecture humaine d'orientation, pas lecture d'agent).
3. **Sortie visible en langage produit** : « ce que j'ai fait · pourquoi · ce qui manque pour la vraie version · la suite proposée ». Les champs `MODE`, `OWNER`, etc. vont dans la trace, exposés seulement sur demande, comme la skill le prévoit déjà l.81.
4. **Frontmatter orienté résultat** : « produire un rendu de niveau designer senior, vrai et situé, avec une trace proportionnée ».
5. **Remplacer la copie de la constitution et du handoff** par un renvoi d'une ligne (skill et READING_MAP).
6. **Ajouter un exemple de fabrication** dans `examples.md` : un brief flou → décisions de craft → rendu décrit → ce qui manque. Les traces actuelles restent comme exemples de preuve.
7. **Mesurer deux budgets** : le périmètre actuel et le **chemin prescrit** par la skill, pour que le chantier « structure et budget » vise la charge réelle.
8. **READING_MAP** : garder chemin canonique, routage minimal et condition d'arrêt ; envoyer les locators et les perspectives vers une annexe machine ou vers `read_route.py`.

## 7. Lecture

- **Certain :** les mesures ; le chemin prescrit ≈ 20 700 mots contre 9 591 mesurés ; la consigne de chargement répétée quatre fois avec des écarts ; les copies de la constitution et du handoff ; la sortie visible en jargon qui contredit la délégation silencieuse ; les incohérences du §3.8.
- **Probable :** que le frontmatter, la sortie et les exemples orientent l'agent vers la posture d'auditeur ; que l'anti-slop formulé en négatif pousse vers le moyen inoffensif ; que la skill soit le meilleur levier du système, parce qu'elle est le seul fichier chargé à coup sûr.
- **Hypothétique :** qu'une skill-noyau d'une à deux pages avec gestes positifs change le rendu ; à vérifier par épreuve (mini-épreuve, puis G4).
- **Limite :** lecture en auto-comparaison ; aucun regard extérieur.

## 8. Suite

Lecture des façades restantes : QUICKSTART (3 783 mots, la plus lourde), README, GLOSSAIRE, ORCHESTRATION_MAP. SAVOIR et BIBLIOTHEQUE plus tard, puis la mini-épreuve.
