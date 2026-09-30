# V1.2 refonte — Unité R8b-2 — Raccords de R8b après vérification de l'owner

**Date :** 30-09-2026 · **Déclencheur :** vérification de R8b par l'owner (quatre constats, tous confirmés dans le dépôt). **PATCH-DECISION :** `audit/tools/V12R_Patch_R8b2.py` (2 entrées, `validate_structure.py` remplacé). **Diff :** `audit/diffs/V12R_R8b2_raccords.diff`.

## 1. Constats et corrections

| Constat de l'owner | Vérification | Correction |
|---|---|---|
| La garde PKG-01 rejette aussi un choix justifié (« applique un traitement unique si la comparaison confirme… ») | **Vrai.** Le vocabulaire retiré ne regardait pas le contexte | Nouvelle garde **UNI-01**, au niveau de la phrase : « traitement unique », « un seul traitement » ou « une seule famille » exigent un marqueur de choix dans la même phrase (si, lorsque, peut, dépend, suffit, comparaison). **Deux situations testées :** 2 obligations universelles → rouges ; 2 choix conditionnés ou justifiés → verts |
| Le contraste d'échelle n'est pas absent : Gate C, C2 contient « une échelle contrastée » | **Vrai.** Mon rapport R8b cherchait l'expression exacte « contraste d'échelle » | Erratum dans `V12R_15` §2 ; R8c traite un **geste existant à approfondir** (titre, masses, composition) |
| L'inventaire marque PIL-01 à PIL-04 « non intégré » | **Vrai** | Lignes mises à jour : intégrés le 30-09 (commit `8e430cc`) |
| Fontshare : licence FFL ou OFL selon la police | Conforme à ce que la vérification par ressource devait établir | Carte des moyens (bloc noyau) et carte v0 précisées |

**Mesures courantes, distinctes de celles de R11a :**

| Mesure | Après R11a | **Après R8b-2** |
|---|---|---|
| Chemin prescrit, trace légère | 12 187 mots | **12 430** |
| Noyau | 3 302 mots | **3 505** |
| Atteignabilité | 24/25 | 24/25 |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Nouvelle garde sur le package d'avant R8b | **7 erreurs UNI-01**, soit les mêmes formulations que l'ancienne garde ; le package actuel est vert |
| Mutations et acceptations | 3 rouges attendues (2 obligations universelles, la carte sans vérification par ressource) ; **2 vertes attendues** (choix conditionné, choix justifié) |
| Suivi | Vert : 372 cas maintenus, aucune migration ; `validate_all` vert |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Écarts déclarés

1. **Première liste de marqueurs de condition trop large, corrigée avant validation.** « justifié », « thèse » et « choisi » figuraient déjà dans les anciennes formulations universelles (« traitement unique et cohérent… justifié par la thèse »), qui auraient donc été acceptées. La liste a été restreinte aux marqueurs de choix réel, puis testée contre le package d'avant R8b.
2. **Rectification déclarée de `V12R_Patch_R8b.py`.** Les motifs de mutation de K2 à K5 passent à « [UNI-01] ». L'inverse de K1 ne s'applique plus, puisque R8b2-F1 a modifié ce texte ; il est remplacé par une mutation équivalente dans R8b-2 (la carte sans « chaque ressource retenue » rougit).
3. **Doublons 146 → 148 : artefact.** L'entrée du CHANGELOG cite la phrase sur Fontshare.
4. **Portée des contrôles.** Les mutations montrent que les gardes détectent les retours arrière testés. Les acceptations montrent qu'elles laissent passer les formulations légitimes testées. Ni les unes ni les autres ne disent rien de l'effet sur les rendus, qui reste à observer en R10.
