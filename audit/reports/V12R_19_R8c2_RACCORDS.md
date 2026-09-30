# V1.2 refonte — Unité R8c-2 — Raccords de R8c après vérification de l'owner

**Date :** 30-09-2026 · **Déclencheur :** vérification de l'owner (trois points et un raccord documentaire, tous reproduits dans le dépôt). **PATCH-DECISION :** `audit/tools/V12R_Patch_R8c2.py` (3 entrées, `validate_structure.py` remplacé ; textes remplacés extraits dans `V12R_Patch_R8c2_textes.py`). **Diff :** `audit/diffs/V12R_R8c2_raccords.diff`.

## 1. Constats et corrections

| Constat | Reproduction | Correction |
|---|---|---|
| UNI-01 accepte « Applique **toujours** un traitement unique, puis utilise la comparaison… » et rejette un choix situé (« pour cette série de portraits, un seul traitement a été retenu… ») ainsi qu'une interdiction (« N'impose jamais une seule famille à tous les projets ») | **Les trois reproduits** (accepté, rejeté, rejeté) | UNI-01 devient une **garde bornée, déclarée comme telle**. Elle détecte seulement (a) le retour des formulations universelles retirées en R8b et (b) les impératifs universels explicites (« toujours », « à tous les », « dans tous les cas »…) portant sur un traitement ou une famille unique, sauf négation. Elle ne juge pas le sens d'une phrase quelconque ; la revue juge le reste |
| Le geste du titre rend ses corrections systématiques | Confirmé par lecture | Corrections rattachées à **ce que la capture montre** (coupe qui casse le sens, mot isolé non voulu, lignes trop inégales, approche trop lâche, hiérarchie aplatie) ; hiérarchie rétablie par l'échelle, **le poids, la position ou l'espace** ; « un mot isolé, un déséquilibre ou un faible écart peut être le choix de composition : on le garde si la capture montre qu'il fonctionne » |
| La récupération prescrit trop généralement le déplacement du focus | Confirmé par lecture | **Focus selon le moment** : après une soumission bloquée, il peut aller à l'erreur ou au résumé ; pendant la saisie, l'erreur est annoncée de façon accessible (région live) sans déplacer le focus. Reprise « jusqu'au succès, ou jusqu'à une issue claire lorsque la réussite est impossible (alternative ou sortie expliquée) » |
| Le plan de reprise affiche 19 concepts et 3 renvois | Confirmé | Mis à jour : 23 concepts, 4 renvois, 7 résumés fidèles |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | Fidélité du titre (2 lieux) et de la récupération |
| Garde bornée sur le package d'avant R8b | 7 erreurs UNI-01 : les mêmes formulations restent détectées |
| Mutations (rouges attendues) | 2 inverses ; contre-exemple 1 de l'owner ; 2 formulations retirées ; les 4 mutations UNI-01 de R8b (K2 à K5) : **toutes rouges** |
| Acceptations (vertes attendues) | Contre-exemples 2 et 3 de l'owner ; choix conditionné ; choix justifié ; les deux acceptations de R8b-2 : **toutes vertes** |
| Suivi | Vert : 372 cas maintenus, aucune migration ; doublons 148 ; 24/25 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |
| Mesures | Chemin 12 629 → 12 682 mots ; noyau 3 695 → 3 748 |

## 3. Écarts et portée

1. **Rectification de la promesse de R8b-2.** « Obligation universelle refusée, choix justifié accepté » était trop large pour une garde lexicale. La portée réelle d'UNI-01 est celle du §1 : une garde de régression et d'impératif explicite, pas une compréhension du sens. `V12R_16` et `CLAUDE.md` sont corrigés en conséquence.
2. **Ce que les contrôles établissent.** Les formulations testées sont refusées ou acceptées comme attendu. Une formulation universelle écrite autrement (sans marqueur explicite) peut passer : c'est une limite déclarée, couverte par la relecture de parcours et la revue.
3. **Effet sur les rendus :** à observer en R10. Pour la récupération, l'observation demande une interaction.
