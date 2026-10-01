# V1.2 — AP2 : errata R10 (C34 à C36, réserve D-26) ; rectification du suivi (C14) et de l'export de mesure (C22)

**Date :** 01-10-2026.
**Origine :** audit progressif externe, étape 10 (`DG_Audit_progressif_10`).
**Décision de l'owner :** « Allons-y » sur l'unité 2 du plan validé (`V12R_40` §6).
**Package :** inchangé ; aucune PATCH-DECISION nécessaire.
**Pièces :**
- outils rectifiés : `audit/tools/V12R_Suivi.py`, `audit/tools/V12R_Mesures.py` ;
- preuves directes : `audit/tools/V12R_Sonde_AP2.py` ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP2.json`.

## 1. Rectifications déclarées des outils (règle 5)

| Constat | Outil | Avant | Après |
|---|---|---|---|
| **C14** (présence des cas) | `V12R_Suivi.py` | Un cas `OBSOLETE` absent du run passait sans erreur, alors que la docstring promettait l'inverse | Tout cas de la table absent du run est une erreur, quel que soit son statut |
| **C14** (garde établie) | `V12R_Suivi.py` | Une garde de remplacement était « verte » dès que son identifiant n'apparaissait pas dans la sortie. C'était le cas aussi quand le validateur s'arrêtait tôt ou plantait, ou quand l'identifiant n'existait pas | Une garde est verte seulement si elle est **établie** : validateur connu, identifiant présent dans son source, et validateur allé au bout (bannière PASSED, ou bannière FAILED de contrôle complet suivie de sa liste) sans citer la garde |
| **C14** (forme) | `V12R_Suivi.py` | Logique dans `main` | Logique extraite dans `evaluate()`, testable. Sortie, instantané et décision inchangés en situation normale |
| **C22** | `V12R_Mesures.py` | La boucle d'affichage du §5 réutilisait `r`, d'où un JSON `atteignabilite` contenant une route | Variable distincte. L'export égale `reach(budget)` (dictionnaire, 25 outils). Affichage console inchangé |

**Justification.** Le suivi est le filet de sécurité de l'unité AP3, la plus exposée aux contrats de harnais. Il devait refuser un cas disparu et une garde non exécutée avant cette unité.

## 2. Preuves directes (`V12R_Sonde_AP2.py`)

La décision du suivi est rejouée sur l'ancienne version (lue dans git à `472ff24`) et sur la nouvelle. Les scénarios dérivent des **résultats réels** de l'instantané AP1 (389 cas). Seuls varient un cas retiré, une sortie de validateur simulée ou une garde renommée ; `validate_all` est simulé vert.

| Scénario | Attendu | Ancienne | Nouvelle |
|---|---|---|---|
| Résultats réels | VERT | VERT | VERT |
| Cas OBSOLETE retiré (C2 G-06), scénario de l'audit | ROUGE | **VERT** | ROUGE |
| Cas MAINTENU retiré (C1 G-06) | ROUGE | ROUGE | ROUGE |
| `validate_reading_map` interrompu tôt | ROUGE | **VERT** | ROUGE |
| `validate_structure` en trace Python | ROUGE | **VERT** | ROUGE |
| Garde inconnue (`structure:XXX-99`) | ROUGE | **VERT** | ROUGE |
| Autre garde rouge, contrôle complet | VERT | VERT | VERT (pas de refus excessif) |
| Garde de remplacement citée | ROUGE | ROUGE | ROUGE |

- **C22 :** l'ancienne version exporte `"DIRECTION/VISUAL_TARGET"` (défaut reproduit) ; la nouvelle exporte un dictionnaire égal à `reach(budget)`.
- **Total :** sonde verte, 10/10. L'ancienne version échoue sur 4 scénarios et sur l'export.

## 3. Errata (rapports historiques annotés, texte d'origine conservé)

Chaque erratum est une section datée en fin de rapport ; la ligne fautive porte un renvoi. Les corrections disent ce que les preuves permettent d'affirmer. Elles ne démontrent pas l'usage effectif des blocs compilés et n'annulent pas le signal de convergence.

| Constat | Rapport | Correction |
|---|---|---|
| **C34** | `V12R_37` | « SAVOIR et BIBLIOTHEQUE ne le sont presque pas » confondait route non ouverte et contenu non disponible. Le noyau lu par les agents C3 (à `64265da`) compilait 39 blocs, dont **16 de SAVOIR et 4 de BIBLIOTHEQUE**. Les agents n'ont pas ouvert ces routes séparément (traces déclarées) ; l'application des gestes n'est pas attestée. La justification d'A2 était surestimée pour le reste de SAVOIR ; les planchers couleur et typographique d'A2 ne figuraient pas parmi ces blocs |
| **C35** | `V12R_35` | « Polices comprises » est faux : 33 736 à 49 217 octets de **HTML seul**, avec deux références de polices externes par rendu, non mesurées. Le poids chargé est inconnu ; aucun dépassement n'est établi |
| **C36** | `V12R_35` | « Tous blanc cassé » est faux. Le fond de `body` est blanc cassé dans 4 rendus et **blanc pur dans 2**, tous deux B-SAAS : C4 déclare `#ffffff`, C1 ne déclare rien (blanc du navigateur). Masses et premiers écrans non mesurés. La convergence d'objet reste établie, la convergence de fond était surestimée |
| **D-26** (C16) | `V12R_37`, `V12R_35`, CLAUDE.md | « 0 fait inventé » s'entend au sens de P-2. Des fonctions affirmées d'un produit fictif restent hors marquage (C3 et C4 B-SAAS). La réserve est rétablie dans chaque résumé |

## 4. Contrôles de l'unité

- **Suivi rectifié :** VERT sur le package réel. 389 cas, 363 maintenus, 26 obsolètes. **Les 26 gardes de remplacement sont désormais établies**, et non plus seulement non citées. `validate_all` vert ; cliquets inchangés.
- **13.01 :** texte 6/6, mutations 6/6, non-régression 5/5. « Distributions » n'a pas été rejoué, puisque le package n'a pas changé ; il était à 9/9 en AP1.
- **13.02 :** 38/38. **B01 :** 218/218.
- **`V12R_Mesures` :** affichage identique (24/25 outils sur le chemin LETTRE).

## 5. Écarts et limites déclarés

- **Données historiques non régénérées.** Le champ `atteignabilite` de `V12R_Mesures_B05.json` et `V12R_Mesures_R4.json` contient une route, conséquence de C22. Le suivi n'utilise pas ce champ (ses cliquets lisent budget, indicateurs, doublons et listes). Les nombres d'atteignabilité des rapports viennent de la sortie console et restent justes.
- **Validateurs simulés dans la sonde.** Une garde « établie » repose sur la forme des sorties actuelles des validateurs. Si leur bannière change, le suivi passera au rouge : c'est voulu, et la rectification sera alors à déclarer.
- **Couverture de la sonde.** La sonde C14 simule les sorties de validateurs et réutilise des résultats de harnais enregistrés. Le suivi complet, lui, a tourné réellement.

## 6. Décision attendue : D-26

| Option | Effet |
|---|---|
| **(a)** Une clause dans `CNT-01` (DIRECTION, compilée dans le noyau), traitée en AP3 : les fonctions affirmées d'un produit fictif sont des contenus d'exemple, marqués comme tels | Une phrase dans le noyau, avec garde et mutation. Effet non observable sans run (R10 arrêté) |
| **(b)** Limite déclarée, sans changement normatif | Rien à compiler. Le défaut observé reste possible |

**Recommandation : (a).** C'est le même principe que D-20 et D-25 (marquer, ne pas inventer) étendu à une catégorie manquante. La clause est courte et entre dans AP3 sans unité supplémentaire.

## 7. Suite

**AP3 :** C08, C05, C06, C07, C09 et C10, plus D-26 si l'option (a) est retenue.
