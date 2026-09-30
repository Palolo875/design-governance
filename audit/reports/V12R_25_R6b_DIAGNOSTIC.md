# V1.2 refonte — R6b élargi — Diagnostic de l'entrée humaine (avant correction)

**Date :** 30-09-2026. **Sources du périmètre :**
- plan de reprise §4 (ordre 5) et « Définition du 27-09 » ;
- amendement du 28-09, §8 ;
- plan consolidé, §6 (provenance) ;
- inventaire : D-11 (bloquant P2), Q-13 (README), R-25b.

**Méthode :**
- lecture ciblée des six fichiers d'entrée (≈ 9 800 mots) : README du dépôt, README officiel, QUICKSTART, READING_MAP, ORCHESTRATION_MAP, README Local généré par `build_distributions.sh` ;
- carte des dépendances (harnais, conditions LCF, validateurs) ;
- **maquette sur copie** : démarrages concurrents retirés, entrée en quatre questions, README officiel réduit à un pointeur ; suivi complet exécuté sur cette copie pour mesurer le coût réel.

Auto-lecture déclarée. Aucun fichier du package n'est modifié.

## 1. Constats (certain)

| # | Constat | Lieu |
|---|---|---|
| E1 | **Neuf démarrages concurrents** : « Démarrage express — 90 secondes » et « Par où commencer » (README) ; « Démarrage en 90 secondes », « Façade d'activation en cinq éléments », « Le chemin en trente secondes », « Le parcours complet en cinq minutes », table « Si vous avez 30 secondes / 5 minutes » (QUICKSTART) ; « Commencer ici » (README officiel) ; « Commencer en deux minutes » (README Local) | 4 fichiers |
| E2 | **Le novice doit choisir un mode.** Tous ces démarrages demandent d'écrire `MODE — DECISION — RISK — NEXT-PROOF — OWNER`. Le README et le README Local donnent une table « situation → `LITE` / `ITER` / `DIRECTION`… ». L'amendement §8 dit l'inverse : « le novice ne doit pas choisir lui-même un mode interne » | README, Local, QUICKSTART |
| E3 | **Aucune page ne répond aux quatre questions** (que demander, que fournir, que recevoir, comment poursuivre). La prise de brief amicale n'existe que côté agent (`DIRECTION/EXTERNAL-START`). Nulle part le novice n'apprend que le vrai contenu et les photos changent le résultat (P1 : la condition avec intrants gagne 12/12). Ce qu'il reçoit (proposition exploratoire, exemples marqués, ce qui manque) et la façon de poursuivre (valider, réorienter, arrêter : `CHK-01`) ne lui sont pas expliqués | — |
| E4 | **Trois présentations** du package : README du dépôt (1 732 mots), README officiel (705), README Local codé en dur dans le build (≈ 500). La **constitution minimale est recopiée cinq fois** : README, README officiel, QUICKSTART, READING_MAP, README Local | 5 lieux |
| E5 | **Résidus périmés** dans le README du dépôt : | README |
| | – la constitution minimale garde l'ancien absolu 2 (« une surface identitaire ne doit pas être dessinée uniquement de mémoire ») : **résidu de D-03, non vu par R7**, car la garde visait l'impératif « Ne dessine jamais… » | |
| | – « parcours **minimal** » (R-25b) | |
| | – « Ces contrôles établissent la cohérence… » (Q-13) | |
| | – profil « Agent : `QUICKSTART.md`, puis `SKILL.md` » (l'entrée agent est la skill) | |
| E6 | **README Local codé en dur** (heredoc de `build_distributions.sh`). Chaque réécriture du README doit être refaite à la main dans le build, et R7 l'avait oubliée une fois (R7-F4) | build |
| E7 | **Deux cartes dérivées** (READING_MAP, ORCHESTRATION_MAP) qui se renvoient l'une à l'autre. READING_MAP garde une copie de la constitution. L'orientation « par résultat » d'ORCHESTRATION_MAP recoupe le « routage minimal par décision » de READING_MAP | cartes |

## 2. Architecture cible proposée

| Rôle | Lieu | Contenu |
|---|---|---|
| **Entrée humaine** (une seule) | Section « Commencer » en tête du **README du dépôt**, que GitHub affiche en premier | Quatre questions, au vouvoiement, sans jargon ; renvois vers la profondeur |
| Entrée humaine, export Local | README Local **généré à partir de la même section** (réécriture des chemins par le build), plus de heredoc divergent | Même texte |
| **Entrée agent** | La skill (inchangée) | — |
| Présentation experte | Suite du README du dépôt : sources, structure, validation, limites (fusion avec le README officiel) | Une seule constitution minimale, exacte |
| README officiel (`V1/official/README.md`) | Pointeur court : sources normatives et introduction de la `RUN_CARD`, que `validate_design_governance` exige, plus un renvoi | Plus de démarrage |
| **QUICKSTART** | Guide opérateur raccourci : **un seul parcours commun**, puis approfondissements (mode, chargement, premier rendu, handoff, exemple, clôture) | Démarrages 90 s / 30 s / 5 min fusionnés |
| **Cartes** | READING_MAP garde chemin et locators, et absorbe l'orientation utile d'ORCHESTRATION_MAP. `DIRECTION/CHARGE` reste la seule liste de chargement | Sous-lot séparé (voir §4) |

**Texte proposé pour l'entrée humaine** (≈ 330 mots ; vouvoiement ; règles citées par renvoi, aucune redéfinie) :

> ## Commencer
>
> Design Governance aide un agent à produire un design dirigé, construit et soigné dès la première proposition, puis à l'améliorer avec vous. Vous n'avez besoin de connaître ni les modes, ni le vocabulaire interne : l'agent s'en charge.
>
> **1. Que demander ?** Décrivez en quelques phrases ce que vous voulez obtenir (une page, un écran, une identité, une correction), pour qui, et où cela servira : démonstration, maquette ou vrai produit. S'il s'agit d'un vrai commerce ou d'un vrai service, dites-le.
>
> **2. Que fournir ?** Ce que vous avez déjà : textes, prix, horaires, logo, couleurs, photos (même prises au téléphone, à la lumière du jour), exemples que vous aimez, lien vers l'existant. Ces éléments changent davantage le résultat que tout le reste. S'il en manque, l'agent vous pose au plus trois questions, en un seul message, seulement celles qui améliorent vraiment le résultat : contenu réel, marque, image principale ou source d'images autorisée, destination si elle est incertaine. Il construit la proposition dans tous les cas.
>
> **3. Que recevoir ?** Une première proposition réellement construite, pas un gabarit vide. La réponse dit simplement ce qui a été fait et pourquoi, ce qui est un exemple à remplacer, ce qui manque pour la vraie version, et la suite proposée. C'est une proposition à discuter, pas une validation : accepter une direction pour un vrai produit demande vos éléments réels et les vérifications prévues.
>
> **4. Comment poursuivre ?** Validez, réorientez ou arrêtez. Dites en une phrase ce qui ne va pas (« le titre écrase la photo », « trop froid pour une boulangerie ») : l'agent corrige le défaut principal, regarde de nouveau le résultat et vous dit ce qui a changé. Avant toute action irréversible ou coûteuse (publier, envoyer, payer, remplacer l'existant), il vous demande votre accord.
>
> Pour aller plus loin : le [guide opérateur](V1/official/QUICKSTART.md), la [skill](skills/design-governance-practice/SKILL.md) pour les agents, le [glossaire](V1/official/GLOSSAIRE.md) et les sources normatives.

**Correspondances vérifiées :**

| Question | Source |
|---|---|
| 1 | Prise de brief (`DIRECTION/EXTERNAL-START`) ; `CONSTRAINT` de START (destination) |
| 2 | Prise de brief, condition canonique incluse (garde de fidélité existante) ; `CNT-01` |
| 3 | Réponse visible (`ACTION/HANDOFF`, `SOR-01`) ; `TRA-01` (proposition `EXPLORATORY`) ; `ANC-01` |
| 4 | `CHK-01` ; boucle d'édition (`DIRECTION/DOUBLE-LOOP`) ; confirmation avant action irréversible ou coûteuse (`CHK-01`, `ACTION/AUTHORITY`) |

« Vous dit ce qui a changé » remplace « avant/après », qui promettrait B1b hors de son scope.

## 3. Coût mesuré (maquette, certain)

Sur la copie, le suivi donne **15 cas rouges**, pour **trois causes réelles** :
- **LCF-04, LCF-05 et LCF-10** supposent une table des modes dans le README (ligne `DIRECTION`, ligne `ITER`, « Classement : voir `DIRECTION/START` ») ;
- les **12 autres cas en découlent** : témoins T-1 et T-POS, E2-01, C8 R-1, E1-28, tous rouges parce que `validate_all` est rouge.

`validate_design_governance` et `validate_structure` restent verts.

**Traitement prévu :**
- les trois conditions sont **rectifiées de manière déclarée** : leur propriété (une table des modes fidèle à START) s'applique à la table qui subsiste, celle du QUICKSTART opérateur, et ne force plus une table dans l'entrée novice ;
- les trois cas C5 correspondants sont migrés (M1) ;
- les témoins redeviennent verts d'eux-mêmes.

**Coût : faible au regard du changement de texte. L'arrêt du plan ne s'applique pas.**

**Non mesuré par la maquette :**
- génération du README Local depuis la section « Commencer » : attentes de `validate_design_governance` sur le Local ;
- fusion des cartes : LCF-03 et les pointeurs de LCF lisent ORCHESTRATION_MAP, et C5 et le manifeste la listent.

## 4. Découpage proposé

- **R6b-1 — Entrée humaine et présentations.** Ferme D-11, E1 à E6, Q-13 (README) et R-25b.
  - Section « Commencer » en tête du README du dépôt.
  - README du dépôt et README officiel fusionnés ; le README officiel devient un pointeur.
  - README Local généré depuis la même section.
  - QUICKSTART réduit à un seul parcours.
  - Une seule constitution minimale, exacte ; les autres lieux y renvoient.
  - Profils de lecture corrigés (agent → skill).
- **R6b-2 — Cartes réunies.** E7 : READING_MAP absorbe l'orientation d'ORCHESTRATION_MAP ; ORCHESTRATION_MAP devient un pointeur de compatibilité ou disparaît, selon le coût mesuré par une seconde maquette. **Non bloquant P2** : il concerne des lecteurs experts ; il améliore clarté et charge.

## 5. Gardes prévues (R6b-1)

- **Une seule entrée humaine** : vocabulaire retiré pour « Démarrage en 90 secondes », « Démarrage express », « Le chemin en trente secondes », « en cinq minutes », « Commencer en deux minutes ».
- **Entrée balisée** (concept `ENT-01`, README) :
  - la section contient les quatre questions ;
  - elle ne contient aucune table ni ligne de mode (`LITE`, `ITER`, `STANDARD`, `DIRECTION` comme mode à choisir) ;
  - le README Local construit contient le même texte, vérifié dans la distribution par `validate_all`.
- **Registre** : vouvoiement étendu du QUICKSTART au README (garde REGISTER).
- **Fidélité existante** : prise de brief (« destination si elle est incertaine »).
- **Constitution minimale** : vocabulaire retiré pour « dessinée uniquement de mémoire » (résidu de D-03) ; une seule copie exacte.
- **Mutations** : rouges sous leur inverse. Suivi, 13.01, 13.02, B01.

## 6. Décisions de l'owner

1. **Lieu de l'entrée humaine** : section « Commencer » en tête du README du dépôt, et même texte dans le README Local (recommandé). Autre option : un fichier `COMMENCER.md` séparé, qui ajoute une entrée à suivre dans le manifeste et les liens.
2. **Texte des quatre questions** (§2) : à valider ou à amender. C'est la page que lira un novice.
3. **README officiel** : pointeur court (recommandé) ou maintien comme présentation experte (il resterait alors deux présentations).
4. **R6b-2 (cartes)** : maintenant, après R6b-1 (recommandé), ou reporté après P2 comme non bloquant.

## 7. Arrêt

- Si la génération du README Local fait rougir des contrôles au-delà des trois LCF mesurées sans que la cause se traite par rectification déclarée, le README Local reste un texte du build, aligné à la main, et l'écart est déclaré.
- Si R6b-2 coûte plus de migrations que de texte changé, ORCHESTRATION_MAP reste un fichier séparé, simplement lié depuis READING_MAP.
