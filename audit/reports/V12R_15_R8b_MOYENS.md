# V1.2 refonte — Unité R8b — Moyens de fabrication et enseignements transférables

**Date :** 30-09-2026 · **Décision :** owner, « Allons-y », sur le périmètre de R8b réorienté (`V12R_14`, addendum 2) et l'inventaire `V12R_Inventaire_P2.md`. **PATCH-DECISION :** `audit/tools/V12R_Patch_R8b.py` (7 entrées). **Diff :** `audit/diffs/V12R_R8b_moyens.diff` (7 files changed, 37 insertions(+), 7 deletions(-)).

## 1. Changements

| Objet | Changement |
|---|---|
| **Carte des moyens** (bloc noyau `MOY-CARTE`, concept `MOY-01`) | Consolidée par couche : où chercher, comment choisir, ce qui limite. Licence et conditions d'usage vérifiées **pour chaque ressource retenue**, au moment de l'intégrer ; le nom d'une plateforme ne vaut pas autorisation. Fontshare décrit correctement (licence propre, gratuite sous conditions) ; typographie vérifiée dans la cible (chargement, graisses, glyphes) ; icônes : une famille qui couvre les besoins, mélange justifié ; hors Web, idiomes de la plateforme ; texture : rendu sur capture, **performance mesurée** |
| **PKG-01** (bloquant P2) | « Traitement unique » et « une seule famille » deviennent des **choix justifiés par la thèse**, aux 6 endroits concernés : SAVOIR (`MOY-ASSETS` et carte), Gate C C1 (formulation que j'avais ajoutée en R5b-2), DIRECTION (route de production), exemple de la skill, et la copie compilée dans le noyau. Un traitement commun reste possible pour unifier une série ; plusieurs traitements se justifient si leurs rôles sont lisibles |
| **Enseignement A08** (atlas v0) | Nouveau paragraphe dans `DIRECTION/FIRST-OBJECT` (bloc noyau, concept `EXD-01`) : les données d'exemple restent cohérentes entre elles (totaux, pourcentages, unités, dates, prix) ; un chiffre sans référence se situe ou se retire |

## 2. Confrontation des enseignements de l'atlas v0 à l'existant

| Entrée | Enseignement | Disposition |
|---|---|---|
| A01, A06, A10 | Le système naît du sujet ; chaque élément se justifie ; autorat | Déjà couvert : forme située, test de singularité, posture |
| A02, A07, A08 (nombres géants) | Contraste d'échelle | **Existant, à approfondir** : Gate C, C2 (« une échelle contrastée »). R8c précise son application au titre, aux masses et à la composition. *Erratum du 30-09 (`V12R_16`) : la première version disait « absent du package ».* |
| A03, A04, A05 | Texte concret, les mots portent ; le code montre le produit | Couvert : objet de preuve codé (G), langage produit |
| **A08** | Données cohérentes (56,2 % + 43,8 % = 100 %) ; « +32 % » sans référence | **Ajouté** (`EXD-01`) : c'était une lacune |
| A09 | Affordance juste | Couvert : geste produit |
| C01, C08 | Hero et paysage interchangeables | Couvert : signaux de convergence, marqueurs de vague 3 |
| C02, C03, C04, C06 | Faux asset, clients ou impact inventés | Couvert : vérité de scène, faux asset interdit, plinthe de logos |
| C05 | Métaphore arbitraire | Couvert : forme située (métaphore jamais ajoutée pour paraître créatif) |
| C07 | La deuxième passe ajoute de la preuve, pas du style | Couvert : boucle d'édition (pas d'effet décoratif terminal) |
| Principes 2, 6, 7 | Un seul accent, deux familles au plus, cohérence de série | **Non retenus comme règles** : observations situées sur un petit échantillon (amendement §5) ; la cohérence de série est dans `MOY-ASSETS` |
| Principe 5 | Texte posé dans la zone calme de l'image | Relève de R8c (relation texte/image) |

Aucune pièce de l'atlas n'est citée dans le package. L'atlas v0 reste un matériau historique ; aucun jugement n'est porté sur les créations ni sur leurs auteurs.

## 3. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 10 erreurs : `EXD-01` absent ; 7 fois le vocabulaire retiré de PKG-01 ; 2 fois la fidélité de la carte |
| Vert après | `validate_structure` : 20 concepts, 13 vocabulaires retirés, 4 résumés fidèles ; `validate_reading_map` : vert (LCF-48 et LCF-49 préservées) |
| Mutations | **6/6 rouges** |
| Suivi | Vert : 372 cas maintenus, aucune migration ; atteignabilité **24/25** vérifiée |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |
| Mesures | Chemin 12 187 → **12 430 mots (+243)** ; doublons 144 → 146 |

## 4. Écarts déclarés

1. **+243 mots sur le chemin.** C'est la carte consolidée et le traitement des assets, conformément à « qualité avant nombre de mots » ; les deux sont lus au moment où la décision se prend.
2. **Doublons +2 : artefact de mesure.** La phrase « À revoir avant 2027-03. », date de veille propre à chacun, apparaît dans deux blocs distincts (carte et marqueurs de vague). Le reste est un réordonnancement, pas un doublon nouveau.
3. **Deux enseignements renvoyés à R8c** : le contraste d'échelle (geste existant à approfondir, erratum `V12R_16`) et la relation texte/image.

## 5. Lecture

- **Certain :**
  - PKG-01 est fermé ;
  - la carte des moyens est consolidée et exige une vérification par ressource ;
  - la lacune A08 est comblée.
- **Probable :**
  - des choix de traitement et d'icônes plus variés et mieux justifiés ;
  - des données d'exemple plus crédibles.
- **Hypothétique :** l'effet sur les rendus (R10).
- **Limite :** auto-comparaison.
