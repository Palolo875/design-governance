# V1.2 refonte — Unité R4 — Noyau de fabrication (application)

**Date :** 2026-09-27
**Décisions :**
- 1 (noyau compilé), 4 (langage produit), 7 (marqueurs dans le noyau) ;
- R4 validé par l'owner (`V12R_04_PROPOSITION_R4`) : sélection de paragraphes canoniques, liste canonique `DIRECTION/CHARGE`, allègement du chargement par défaut.

**PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R4.py` (40 entrées, 29 blocs balisés, skill et validateur remplacés, `build_core.py` créé). **Diff :** `audit/diffs/V12R_R4_noyau.diff` (17 fichiers, +540 / −173).

## 1. Ce qui change pour l'agent

**Un noyau de fabrication** de 2 843 mots, lu à chaque run dans la skill et compilé depuis 29 blocs balisés dans DIRECTION, ACTION, SAVOIR et BIBLIOTHEQUE :

| § | Contenu |
|---|---|
| 1 | Rôle de directeur·rice artistique senior ; la première idée comme hypothèse contre la convergence |
| 2 | Classer, puis charger : **la** table de chargement (copie de `DIRECTION/CHARGE`) |
| 3 | Prise de brief ; chaîne promesse → objet de preuve → geste ; objet **codé** de préférence ; marquage de vérité |
| 4 | Structure : où elle vit, comment le regard circule ; lecture expressive ; axes de tension ; **six signaux de convergence** |
| 5 | Composition : **grammaire positive** ; test de singularité ; forme située ; contrôles (compensation optique, recomposition) ; **vocabulaire perceptuel avec « diff possible »** ; question de convergence ; **marqueurs de vague datés** |
| 6 | Moyens et vérité : plafond `FABRICATION` ; carte des moyens ; assets moyens ; calibrations croisées ; faux asset interdit ; vérité de scène et audience |
| 7 | Boucle d'édition : boucle ; **table de diagnostic** ; atelier retrait / réduction / transformation ; revue créative ; six questions ; repasse ; un axe à la fois |
| 8 | Sortie en **langage produit** (ce que j'ai fait, pourquoi, ce qui manque pour la vraie version, la suite) ; trace sur demande |

**Dans les sources :**
- `DIRECTION/DAILY` devient **`DIRECTION/CHARGE`**, seule liste de chargement : Gates A et B en `LITE` et `ITER` ; `CREATIVE-BOOT`, `EXTERNAL-START`, `FIRST-RENDER` en `DIRECTION`.
- La table de diagnostic et les six questions passent de QUICKSTART à `DIRECTION/DOUBLE-LOOP`.
- « Un axe à la fois » passe d'ORCHESTRATION_MAP à `SAVOIR/CRAFT/CFT-02`.
- `ACTION/HANDOFF` définit la réponse visible en langage produit (concept `SOR-01`).
- Les façades renvoient à `DIRECTION/CHARGE` et à `ACTION/HANDOFF`.
- `examples.md` s'ouvre sur un exemple de **fabrication depuis un brief flou**.

## 2. Résultats

| Mesure (outil R1) | B05 | Après R3 | **Après R4** |
|---|---|---|---|
| Chemin prescrit d'un run `DIRECTION` (LETTRE) | 23 891 | 23 849 | **13 537 mots (−43 %)** |
| Lignes lues (LETTRE) | 1 662 | 1 654 | **870** |
| Outils de fabrication sur le chemin (TABLE) | 7/25 | 7/25 | **24/25** |
| Listes de chargement distinctes | 5 | 5 | **1** |
| Négations défensives (hors copie compilée) | 863 | 862 | **813** |
| Doublons (occurrences) | 190 | 186 | **161** |
| Skill | 3 191 mots | 3 191 | 3 096 (dont noyau 2 843) |

| Contrôle | Résultat |
|---|---|
| `validate_structure` | Vert : 11 concepts, noyau compilé et conforme, chargement unique, gardes CHG-01 à CHG-07 |
| `validate_reading_map` | Vert (50 conditions, dont 7 rectifiées) |
| Mutations | **20/20 rouges** : 13 gardes de structure, 7 conditions de façade rectifiées |
| Suivi | **372 maintenus verts, 17 migrés** (15 en R4), cliquets en baisse, `validate_all` vert |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

La cible de fin de R5 (≤ 14 000 mots) est atteinte dès R4.

## 3. Écarts déclarés

1. **DAILY transformée en CHARGE**, au lieu d'une section nouvelle.
   - `DIRECTION/DAILY` était déjà une table de chargement par mode : une septième liste, non repérée par la mesure R1.
   - Ajouter `CHARGE` à côté en aurait créé une huitième.
   - DAILY est donc devenue `DIRECTION/CHARGE`. La colonne « ajouter seulement si » et la règle d'atlas sont conservées ; les renvois ont été mis à jour.
   - Cela ferme au passage le mineur transmis « `DIRECTION/DAILY` sans gates en LITE/ITER » (réserve 8).
2. **Noyau à 2 843 mots**, au-dessus de la cible de 2 500, sous le seuil d'arrêt de 3 000.
   - Le premier assemblage faisait 3 204 mots (au-dessus du seuil).
   - Coupes faites : troisième paragraphe du rôle, deux paragraphes de posture, statut de la liste, table `TRUTH`, table de tests de la forme située.
   - Choix assumé : couvrir 24 outils sur 25 plutôt que tenir 2 500 en coupant des gestes de fabrication. Le chemin total baisse de 43 %.
3. **Sept conditions de façade rectifiées** (même propriété, nouveau lieu) :
   - LCF-01, LCF-07, LCF-25, LCF-39 : vérifiées dans `DIRECTION/CHARGE` ;
   - LCF-47 : objet codé, forme en gras admise ;
   - LCF-C1 : copies fidèles là où elles existent ;
   - LCF-C2 : rubriques du langage produit, ancien format refusé.

   Chacune est rougie par une mutation propre. Le nombre de conditions reste 50.
4. **LCF-46 non rectifiée.** Les marqueurs recopiés dans le noyau restent des lignes `[VEILLE 20…]` datées, que la condition admet déjà. La décision 7 est satisfaite sans toucher à la garde (le plan prévoyait une rectification).
5. **Quinze cas de harnais migrés (M1)** : C2 G-06, C3 G-05, G-06, G-08, C5 M-6, LCF-01, LCF-07, LCF-C1, LCF-C2, E1-09, E1-23, R03 R3-04, R3-11, R R-04, R-18.
   - Chacun a une garde de remplacement verte et une mutation démontrant sa sensibilité : CHG-01 à CHG-03, NOY-02, ou LCF rectifiée.
   - Voir `V12R_Correspondance_harnais.csv`.
6. **Outillage d'audit adapté** (versions B05 archivées sous `_B05.json`) :
   - périmètres redéfinis sur la table canonique ;
   - la copie compilée est exclue des indicateurs et des doublons, mais comptée dans le budget ;
   - une liste réduite à un renvoi vers `CHARGE` n'est pas une liste distincte.
7. **D-19 signalé, non corrigé.** Dans le paragraphe canonique de prise de brief (`EXTERNAL-START`), la phrase « cette vue reste interne » perd son contexte une fois compilée. Traitement : R5a.
8. **F22 hors chemin** (tests perceptifs de `BIBLIOTHEQUE/GATE`). Le test de singularité et Gate C couvrent l'essentiel ; R5d (fusion de `BIBLIOTHEQUE/GATE` dans les gates A et C) le traitera.

## 4. Lecture

- **Certain :**
  - le savoir-faire de fabrication est désormais **sur le chemin** : 24 outils sur 25 au lieu de 7 ;
  - le chemin prescrit baisse de 43 % ;
  - une seule liste de chargement ;
  - une sortie en langage produit ;
  - toutes les propriétés protégées restent gardées, avec rouge sous mutation.
- **Probable :**
  - l'agent produira des premiers rendus plus construits (gestes positifs, `MODAL` nommé avec les marqueurs, objet codé, boucle d'édition) ;
  - le coût d'un run baissera nettement.
- **Hypothétique :** la qualité perçue. **C'est l'objet du point de contrôle P1.**
- **Limite :** auto-comparaison ; le noyau reprend des textes existants et n'a pas été relu par un regard extérieur.

## 5. Suite : P1, mini-épreuve

Protocole de l'addendum §5 et §6 :
- brief B-DLA vague ;
- C3 (V1.2 après R4) ×2 ;
- C3r (même brief + « c'est pour mon vrai commerce ») ×1 ;
- même modèle ;
- captures avec défilement ;
- juge neuf avec le brief riche intégral ;
- comparaison avec les 6 rendus B-DLA ;
- mesure des tokens.

Selon le résultat, soit la vague III (R5), soit un diagnostic.
