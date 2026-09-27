# V1.2 refonte — Unité R8a — Convergence typographique (D-21)

**Date :** 2026-09-27 · **PATCH-DECISION :** `audit/tools/V12R_Patch_R8a.py` (3 entrées). **Diff :** `audit/diffs/V12R_R8a_convergence_typo.diff`.

## 1. Changement

- **Question de convergence** (noyau §5, bloc `COMP-CONVERGENCE` de SAVOIR) : elle porte désormais sur la palette **et la police de titre**.
  - Geste ajouté : comparer au moins deux voix typographiques distinctes (grotesque, serif, mécane, manuscrite ou vernaculaire du lieu) **sur le vrai titre** avant de choisir.
  - Règle inchangée : nommer, justifier ou reconsidérer ; un choix convergent justifié reste valide.
- **Veille** (bloc `COMP-VAGUES`) : ajout du signal P1, déclaré « à confirmer » (3 rendus sur 3, même auteur) : grotesque large ou condensée (Archivo) sur blanc neutre, avec un seul accent vif.

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | Garde FIDELITY « question de convergence » (sans « police de titre ») : 2 lieux, la source et la copie compilée |
| Vert après | `validate_structure` : 3 résumés fidèles ; `validate_reading_map` : vert (LCF-46, marqueurs datés, inchangée) |
| Mutations | 1/1 rouge |
| Suivi | Vert : 372 cas maintenus, aucune migration ; chemin 12 160 mots (+76) |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Écarts et lecture

- **Lot R8 découpé.** R8a traite seulement D-21 ; la carte des moyens consolidée et l'atlas d'ancres restent en R8b.
- **Probable :** plus de variété typographique sur brief vague, pour un coût de fabrication faible (deux essais de titre).
- **Hypothétique :** l'effet mesuré sur la diversité, en R10.
- **Limite :** le signal de veille repose sur N = 3.
