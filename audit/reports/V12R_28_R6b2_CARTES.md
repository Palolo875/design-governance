# V1.2 refonte — Unité R6b-2 — Cartes réunies

**Date :** 30-09-2026.
**Diagnostic :** `V12R_25_R6b_DIAGNOSTIC.md` §4 (non bloquant P2).
**Décision de l'owner :** « Allons-y » (R6b-2 après R6b-1, avec sa propre maquette et la vérification des liens et des locators).
**PATCH-DECISION :** `audit/tools/V12R_Patch_R6b2.py` (13 entrées ; READING_MAP et ORCHESTRATION_MAP remplacés).
**Diff :** `audit/diffs/V12R_R6b2_cartes.diff` (10 fichiers, 65 insertions, 57 suppressions).

## 1. Maquette (coût mesuré avant application)

Sur une copie, les combinaisons ont été déplacées dans READING_MAP et ORCHESTRATION_MAP réduit à un pointeur, sans toucher aux validateurs.
- **2 causes réelles** : LCF-03 et LCF-07 lisent ORCHESTRATION_MAP.
- Les autres rouges en découlent : témoins et `validate_all`.
- Coût faible : **l'arrêt ne s'applique pas**.

## 2. Changements

- **READING_MAP** porte la section « Combinaisons par résultat recherché », reprise d'ORCHESTRATION_MAP : rôle et principe, table des neuf résultats, variation créative, garde-fous, condition d'arrêt.
  - Le garde-fou « Classer d'abord avec `DIRECTION/START` ; cette fiche ne reclassifie pas » est retiré : il doublait « Cette carte ne reclassifie pas ».
  - La ligne « Agent contrôlé » ne renvoie plus à « cette fiche ».
  - Le paragraphe « Utilisation » renvoie à la section.
- **ORCHESTRATION_MAP** devient un **pointeur de compatibilité**. Le fichier est gardé pour le manifeste et les liens externes.
- **Renvois alignés** :
  - README du package ;
  - README officiel (« une carte, un pointeur ») ;
  - skill (flux, lecture humaine) ;
  - `DIRECTION/CHARGE`, dans le noyau : « README, QUICKSTART et READING_MAP ».
- **Rectifications déclarées** :
  - LCF-03 et LCF-07 lisent les mêmes lignes dans READING_MAP ;
  - CHG-06 (pointeur de chargement « Direction forte et spécifique ») lit READING_MAP ;
  - libellés mis à jour.
- **Nouvelle garde MAP-01** : READING_MAP porte une seule section « Combinaisons » ; ORCHESTRATION_MAP ne reprend aucun contenu propre (pas de table, pas de section, 80 mots au plus).

## 3. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | LCF-03 et LCF-07 rouges sur les cartes déplacées avec les validateurs non rectifiés |
| Après | structure, carte de lecture, `validate_design_governance` (liens) et noyau verts ; routes résolues |
| Mutations | **5/5 rouges** : contenu réintroduit dans ORCHESTRATION_MAP ; section dédoublée ; liste de chargement redéfinie (CHG-06) ; LCF-03 ; LCF-07 |
| Suivi complet | vert : 389 cas, 363 maintenus, **26 migrés (2 en R6b-2)** ; instantané `V12R_Instantane_suivi_R6b2.json` |
| 13.01 | 6/6 et 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |
| Mesures | chemin prescrit 12 867 → 12 865 ; noyau 3 889 → 3 888 (section avec titre) ; 24/25 ; doublons 147 → 145 |

## 4. Écarts déclarés

1. **Deux cas de harnais migrés (M1)** : C5 LCF-03 et M-3, qui lisaient ORCHESTRATION_MAP. Garde de remplacement `lcf:LCF-03`, avec une mutation rouge dans le patch. Harnais non modifiés.
2. **Renvois sans garde propre** : README, README officiel, skill et CHARGE. Leur inverse ne casse aucune garde ; l'exactitude des liens est contrôlée par `validate_design_governance`.
3. **Locators** : aucun locator n'est renommé. ORCHESTRATION_MAP n'avait pas de locator de route ; « Locators principaux » de READING_MAP est inchangé.

## 5. Lecture

- **Certain** : une seule carte dérivée à lire, un pointeur de compatibilité, aucune règle nouvelle ; `DIRECTION/CHARGE` reste la seule liste de chargement.
- **Probable** : moins de renvois croisés pour un lecteur expert.
- **Limite** : auto-comparaison.
