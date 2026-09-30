# V1.2 refonte — Unité R8c — Gestes de résolution précisés

**Date :** 30-09-2026 · **Diagnostic :** `V12R_17_R8c_DIAGNOSTIC.md` ; textes validés par l'owner (« Allons-y »). **PATCH-DECISION :** `audit/tools/V12R_Patch_R8c.py` (6 entrées ; `validate_structure.py` et `build_core.py` remplacés). **Diff :** `audit/diffs/V12R_R8c_gestes.diff` (7 files changed, 27 insertions(+), 3 deletions(-)).

## 1. Changements

| Geste | Lieu propriétaire | Dans le noyau |
|---|---|---|
| **Équilibre d'un titre** (`TIT-01`), avec l'écart d'échelle titre/texte | `SAVOIR/TYPE` | Oui, §5 |
| **Texte sur image** (`TXI-01`) : zone calme, recadrage ou voile, contraste au point le plus défavorable, à chaque largeur | `SAVOIR/CRAFT` CFT-03 | Oui, §5 |
| **Relecture de l'ensemble** : question 5 étendue à la hiérarchie et à l'harmonie de l'ensemble (réobserver la page entière) | `DIRECTION/DOUBLE-LOOP` (bloc `BOUCLE-QUESTIONS`) | Oui, §7 (déjà compilé) |
| **Récupération après erreur** (`RCV-01`) : message, saisie conservée, focus, reprise ; observée par interaction | `SAVOIR/STATE` | Non ; appelée depuis Gate C C6 |

Chaque geste nomme son déclencheur, les corrections possibles et l'observation de l'effet. Aucun n'impose de retouche si la relation fonctionne. Non ajoutés, car couverts : le poids optique des icônes (carte des moyens R8b, compensation optique) et le contraste d'échelle comme geste séparé (Gate C C2, masse visuelle), intégré au geste du titre.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 7 erreurs : 3 concepts absents ; renvoi Gate C → RCV-01 absent ; fidélité de la question 5 (2 lieux) ; bloc de noyau absent |
| Vert après | `validate_structure` : 23 concepts, 4 renvois, 5 résumés fidèles, UNI-01 vert ; `validate_reading_map` : vert |
| Mutations | **5/5 rouges** |
| Suivi | Vert : 372 cas maintenus, aucune migration ; doublons 148 (inchangés) ; atteignabilité 24/25 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |
| Mesures | Chemin 12 430 → **12 629 mots (+199)** ; noyau 3 505 → **3 695 (+190)** |

## 3. Écarts et lecture

- **+199 mots sur le chemin**, conformément à « qualité avant nombre de mots ». Les deux gestes de fabrication sont lus au moment de construire, la récupération seulement quand une erreur est en jeu.
- **Certain :** les quatre manques du diagnostic sont couverts, avec un propriétaire et une garde chacun.
- **Probable :**
  - des titres mieux composés ;
  - du texte sur image lisible ;
  - moins de régressions d'ensemble après une correction locale.
- **Hypothétique :** l'effet sur les rendus, à observer en R10. La récupération demande une observation par interaction.
- **Limite :** auto-comparaison.
