# V1.2 — Unité 06 — Lecture intégrale d'ACTION.md (B05)

**Date :** 2026-09-27 · **Lecteur :** même modèle que l'auteur des patchs (auto-comparaison) · **Objet :** ACTION.md sur B05, 1 031 lignes, 14 274 mots.
**Question :** mêmes objectifs que `V12_05` (machine à faire du beau, brief flou, tout public, économe, niveau senior).

## 1. Carte du fichier

| Lignes | Bloc | Mots | Fonction |
|---|---|---|---|
| 1–94 | Responsabilité, carte par mode, `HANDOFF`, quatre registres, `AUTHORITY`, parcours en cinq minutes | ~1 900 | Méta, sorties, entrée |
| 95–131 | `FIRST-RENDER`, `UI-UX-REALITY` | ~600 | **Production** (qualité initiale, interface et tâche) |
| 135–212 | `STATUS` : états, issues, verdicts, statut de direction | ~1 000 | Vocabulaire de statuts |
| 215–275 | `PRECONDITION`, contrat de décision, traces post-build, `FAST-PATH` | ~800 | Contrats de trace |
| 277–398 | `RUN_CARD` : champs, correspondance JSON, capacités, agent seul, snapshot, projection, frontière de validation | ~2 500 | **Trace machine** |
| 400–452 | `RUN-*` (cinq modes) | ~640 | Routes d'exécution |
| 456–507 | `CLOSE-PACKAGE`, fraîcheur, réserves, droits, arrêt du polish | ~850 | Clôture |
| 510–593 | `PIPELINE-DIRECTION` (8 étapes, passe créative) | ~1 700 | **Production** (direction) |
| 596–685 | `STRUCTURED-PROOF` (hiérarchie, typographie, asset, composant, motion) | ~1 000 | Contrats de décision |
| 687–703 | `VISUAL_PROOF` | ~240 | Preuve visuelle |
| 706–770 | `GATE-A` | ~960 | Plancher (accessibilité, honnêteté) |
| 773–862 | `GATE-B` (B1, B1b, atelier d'édition, B2 à B6) | ~1 500 | Jugement, comparaison, regard externe |
| 865–893 | `GATE-C`, `ANTI-SLOP` | ~450 | **Craft sur rendu réel** |
| 896–1031 | Override, politiques, routage, maintenance, test de sortie, mesure | ~1 600 | Exceptions, maintenance, sortie |

**Mesures (certain) :** 81 négations défensives ; `N/A-JUSTIFIED` 30 fois, `NOT-VERIFIED` 28 fois ; 104 jetons internes distincts ; **37 valeurs de statut** énumérées (états, issues, verdicts d'axe, verdicts globaux, statuts de direction, conséquences décisionnelles, résultats de comparaison, labels de vérité) ; `RUN_CARD` citée 41 fois ; 79 termes de craft.

## 2. Ce qui est solide

1. **L'honnêteté de preuve** : « Frontière de validation » (l.388-396), « Mode agent seul et preuve dégradée » (l.346-357), fraîcheur de la preuve. C'est ce qui a produit le seul effet mesuré de V1.1.1.
2. **De vrais outils de craft, cachés dans la preuve :**
   - **l'atelier d'édition de B1b** (l.791-795) : éditer une seule décision par **retrait, réduction ou transformation**, sans rien ajouter, et comparer deux captures. C'est une technique de designer senior ;
   - **Gate C** (C1 à C6) : les critères les plus concrets du système sur le beau (stratégie de surface, typographie choisie, composition, densité optique, profondeur, résolution située) ;
   - **la passe créative** (l.580-592) : masses, vides, échelles, rythme, lumière ; « ne corrige pas un défaut structurel par un effet décoratif terminal » ;
   - **`UI-UX-REALITY`** : penser en états (loading, empty, error…) et en modèle de contenu ; exactement le « états plutôt qu'écrans » de ta vision du design ;
   - **la partition typographique** : rôles (fonctionnel, éditorial, microcopie, donnée, signature).
3. **Le test de sortie** (l.1011-1026), en particulier les questions 8 à 10 : « Quelle décision a changé grâce à la procédure ? », « La dernière modification a-t-elle changé une relation perceptible… ou seulement la justification ? ». Excellent garde-fou contre le rituel.
4. **La maintenance** : « chaque mécanisme est testé contre sa manière la plus facile d'être satisfait sans intention » (l.1000).

## 3. Problèmes observés

### 3.1 La preuve pèse plus que la production (certain pour les volumes)

Environ 3 800 mots produisent (premier rendu, UI-UX, pipeline, gate C) contre plus de 8 000 pour la trace, les statuts, la `RUN_CARD`, les gates A et B, les exceptions et la maintenance. Pour un run `DIRECTION`, la `RUN_CARD` (environ 230 lignes) est obligatoire, avec paire B1b, ancres datées, `creative_close`, réserves à sept attributs : c'est la cause principale du coût double mesuré sur B-DLA (probable).

### 3.2 Trente-sept valeurs de statut (certain)

Sept états, six issues, cinq statuts d'axe, six verdicts globaux, quatre statuts de direction, cinq conséquences décisionnelles, trois résultats de comparaison, labels de vérité. Chacune se justifie dans un audit ; ensemble, elles occupent l'attention de l'agent pendant le run. Un designer senior raisonne avec trois questions : est-ce bon, est-ce vrai, qu'est-ce qui reste à prouver ?

### 3.3 Contradiction avec le one-shot et la prise de brief (certain)

- `PIPELINE-DIRECTION` étape 7 (l.572-574) : en session interactive, **demander une validation avant le build** si l'autonomie n'est pas explicite ; sinon, **ne pas engager le build**.
- `DIRECTION/EXTERNAL-START` (lot 1, B) : « Le rendu est construit dans tous les cas. »
- Pour un non-spécialiste, valider une phrase de direction abstraite est difficile ; voir un rendu est facile. Pratique senior (probable) : la première proposition **est** le point de validation.

### 3.4 Le craft est déguisé en contrôle (probable)

B1b, Gate C et la passe créative sont les meilleures techniques de fabrication du système, mais ils sont écrits comme des preuves à produire après coup (captures, statuts, sérialisation), pas comme des gestes de création à faire pendant le build. L'agent les vit comme de l'administratif.

### 3.5 Doublons avec DIRECTION (certain)

- La **boucle** construire → observer → isoler → corriger est décrite au moins six fois entre les deux fichiers (`DIRECTION/DOUBLE-LOOP`, one-shot ; `ACTION` capacité positive, parcours en cinq minutes, principe positif, boucle de qualité).
- L'**alternative située** : troisième description (étape 3).
- La **réserve sur l'ancre générée** : troisième description (étape 4).
- Le **checkpoint avant build** : deux fois.
- La **table des propriétaires** : une fois de plus (l.68-75).

### 3.6 Gate A : liste générique pour tous les produits (probable)

Quatorze contrôles, dont certains ne concernent que des parcours applicatifs (authentification, saisie redondante, aide cohérente). Le texte dit « applicables », mais la liste est chargée entière à chaque run `DIRECTION`.

### 3.7 Le vocabulaire `anti-direction` persiste côté machine (certain, mineur)

`direction.anti_direction` (l.322) reste le champ de projection ; c'est cohérent avec la décision « trace seule » du lot 1 (`MODAL`/`PARTI` s'y projettent), mais la table ne le dit pas. **Signalé, non corrigé.**

## 4. Relations

- ACTION est le **propriétaire de la preuve** ; DIRECTION lui renvoie 69 fois. Le couple DIRECTION + ACTION, c'est 27 750 mots, dont un run `DIRECTION` charge une partie (805 à 965 lignes mesurées) **plus** la production de la `RUN_CARD`.
- Le schéma `run_card.schema.json` et le validateur rendent la trace vérifiable **en forme** ; la frontière de validation dit bien qu'ils n'attestent pas la qualité.

## 5. Écart aux objectifs

| Objectif | État dans ACTION | Écart |
|---|---|---|
| Machine à faire du beau | Bons outils (B1b, Gate C, passe créative, UI-UX, typographie) | Présentés comme contrôles après coup, pas comme gestes de fabrication |
| Brief flou, non-spécialiste | Parcours en cinq minutes | Checkpoint avant build sur une direction abstraite (§3.3) |
| Économe | Fast-path pour LITE/ITER | `RUN_CARD` lourde obligatoire en `DIRECTION` ; 37 statuts |
| Vrai | Frontière de validation, agent seul, droits, fraîcheur | Solide ; c'est le point fort |
| Senior | Test de sortie, maintenance anti-théâtre | Bon ; noyé dans la trace |

## 6. Pistes (à décider)

1. **Retourner le craft en gestes** : faire de l'atelier d'édition (retrait, réduction, transformation, comparaison de captures), des critères C1 à C6 et de la passe créative une **boucle de fabrication** pendant le build, placée dans le noyau ; la trace en garde seulement le résultat.
2. **Deux niveaux de trace** : un **mode léger par défaut** (trois questions : bon, vrai, reste à prouver + artefact + limite) et la `RUN_CARD` complète seulement si le run est persistant, partagé ou audité.
3. **La première proposition vaut checkpoint** : construire d'abord, puis faire valider sur rendu ; garder le checkpoint préalable pour les décisions coûteuses ou irréversibles.
4. **Gate A par profil** : un sous-ensemble par type de surface (vitrine, application, formulaire critique), chargé selon la surface.
5. **Une seule description de la boucle** dans le noyau, les autres remplacées par un renvoi.

## 7. Lecture

- **Certain :** les mesures, les doublons, la contradiction checkpoint / « construire dans tous les cas ».
- **Probable :** que le poids de la trace et des statuts explique l'essentiel du coût double, et que présenter le craft comme contrôle l'affaiblisse comme fabrication.
- **Hypothétique :** qu'un mode de trace léger préserve le gain d'honnêteté ; à vérifier par épreuve.
- **Limite :** lecture en auto-comparaison.
