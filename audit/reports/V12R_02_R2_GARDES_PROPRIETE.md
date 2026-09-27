# V1.2 refonte — Unité R2 — Gardes de propriété (application)

**Date :** 2026-09-27
**Décisions :**
- décision 2 (`V12R_00`) ;
- méthode M1 à M4 (`V12R_02_PROPOSITION_R2`), validée par l'owner le 2026-09-27 : migration au fil de l'eau, balise invisible, cliquets dans l'audit, garde entrant avec sa correction.

**PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R2.py` (18 entrées, 1 fichier créé, manifeste). **Diff :** `audit/diffs/V12R_R2_gardes_propriete.diff`.

## 1. Changements

**Dans le package :**

| Élément | Changement |
|---|---|
| `scripts/validate_structure.py` (nouveau) | Moteur de concepts : chaque concept du registre existe **une seule fois**, dans **son fichier propriétaire**, suivi d'un bloc **non vide** (≥ 12 mots) ; balise hors registre refusée |
| 8 balises `<!-- concept:HON-0x -->` | Vérité de scène et faux asset (DIRECTION, SAVOIR) ; plafond `FABRICATION` (DIRECTION) ; frontière de validation, agent seul, `NOT-VERIFIED` plutôt que `PASS`, capture ≠ tâche, droit inconnu (ACTION) |
| `scripts/read_route.py` | Retire les balises à la lecture : routes servies **à l'identique** (vérifié sur quatre routes qui contiennent des balises) |
| `validate_all.py`, `build_distributions.sh`, manifeste | Le nouveau validateur est compilé, exécuté (source, GitHub, Local) et distribué |
| CHANGELOG « Non publié » | Entrée R2 |

**Hors package :**

| Élément | Rôle |
|---|---|
| `audit/data/V12R/V12R_Correspondance_harnais.csv` | Table des 389 cas : 233 `MAINTENU`, 156 `MAINTENU-JUSQU-A-REECRITURE` ; colonnes garde de remplacement, lot, justification |
| `audit/tools/V12R_Suivi.py` | Suivi de refonte (voir ci-dessous) |

**Ce que vérifie `V12R_Suivi.py` :**
- les cas maintenus sont verts ;
- un cas obsolète n'est admis qu'avec une garde de remplacement verte et une justification ;
- aucun cas n'est hors table ;
- les cliquets ne dépassent pas la référence B05 (chemin prescrit, négations, doublons, listes distinctes) ;
- `validate_all` passe (sur copie).

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| **Rouge avant** (copie B05 + validateur seul) | 8/8 concepts absents, code 1 |
| **Vert après** | `STRUCTURE VALIDATION PASSED` : 8 concepts |
| **Mutations** | 5/5 rouges : absence, copie dans une façade, déplacement, bloc vidé, balise hors registre |
| `read_route` | Sortie identique avant et après pour `ACTION/RUN_CARD`, `ACTION/PRECONDITION`, `DIRECTION/CREATIVE-BOOT`, `SAVOIR/INTEGRITY` |
| `validate_all` | FULL VALIDATION PASSED (build et reproductibilité) |
| Suivi : harnais | **389/389 verts** (22 harnais, témoins, R, R03), aucun obsolète |
| Suivi : cliquets | Chemin prescrit 23 891 mots ; négations 863 ; doublons 190 ; listes distinctes 5 ; tous égaux à la référence |
| 13.01 texte ; non-régression B01 | 6/6 ; 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |

## 3. Écarts déclarés

1. **Nouvel outil de non-régression.** `V12R_Suivi.py` devient le contrôle de référence de la refonte. Il **englobe** les 22 harnais, R et R03, et y ajoute la table de correspondance et les cliquets. Les commandes de `CLAUDE.md` §5 restent valables.
2. **Premier test « rouge avant » invalide** : le validateur avait été lancé hors de `scripts/`, donc sans fichiers à lire. Il a été refait sur une copie correcte (16 fichiers lus, 8 absents). Déclaré parce que le premier rouge n'était pas probant.
3. **Registre dans le script** : les huit concepts sont listés dans `validate_structure.py` et non dans un fichier de données. C'est un fichier de moins à distribuer ; le registre s'étendra lot après lot (M4).
4. **Budget** : +8 lignes de balises dans les sources, **0 mot** sur le chemin prescrit (retirées par `read_route` ; aucune balise dans les fichiers lus en entier).

## 4. Lecture

- **Certain :** les résultats du §2 ; l'honnêteté (seul effet mesuré de V1.1.1) est désormais protégée par des gardes qui **survivent à une reformulation** et rougissent à une suppression, un déplacement ou une copie.
- **Probable :** que ce mécanisme suffise pour migrer les 156 cas sensibles au fil des lots, sans coût de harnais disproportionné (arrêt commun de R5 si ce n'est pas le cas).
- **Limite :** une balise protège la présence et l'unicité d'un concept, pas la justesse de sa formulation. La justesse reste affaire de relecture.

## 5. Suite

**R3 — alignements** : D-01, D-02, D-07 (renvois), D-08, D-12, D-13, D-16, entrée CHANGELOG. Chaque correction arrive avec sa garde de propriété (M4). Les cas de harnais touchés sont migrés dans la table (M1).
