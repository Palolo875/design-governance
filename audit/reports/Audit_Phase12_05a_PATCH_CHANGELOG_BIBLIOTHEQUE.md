# DG-AUDIT-001 — Phase 12.05a — PATCH : passes CHANGELOG et BIBLIOTHEQUE

**Date :** 26 septembre 2026. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée. **Format :** rapport allégé.

**Commit :** `d537083`, étiquette `12.05a-changelog-bibliotheque`.

**Fichiers produits :**
- `DG_AUDIT_001_B03_12-05a.diff` ;
- `DG_AUDIT_001_B03_package_12-05a.zip` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-05a.json`.

**Ordre suivi :** 11.23 §7. CHANGELOG vient avant BIBLIOTHEQUE, parce que BIBLIOTHEQUE recopie les statuts du CHANGELOG (condition LCF-20).

## 1. Inventaire de la passe

L'inventaire a été extrait des 22 rapports de la phase 11 : ce sont toutes les lignes de correction qui visent l'un des deux propriétaires. **Neuf corrections, toutes appliquées :**

| Propriétaire | Correction | Décision | Texte appliqué |
|---|---|---|---|
| CHANGELOG, table des statuts | T-1 | D4 | Ligne `SEED` (« canonique par construction, sans gain mesuré », vers `ADOPTED` ou `DEPRECATED`). `PILOT` peut aller vers `DEPRECATED` lorsque la route a des consumers. `DEPRECATED` : « aucun nouvel usage ; migration par `ACTION/RUN-SYSTEM` » |
| CHANGELOG 42 | T-2 | D4 | Le seed a le statut `SEED` ; `ADOPTED` exige le contrat de gain réel ; une dépréciation est possible depuis tout état publié ou utilisé et ne revendique aucun gain. L'expression « routes présentes dans le seed » est conservée, car le validateur la cherche |
| BIBLIOTHEQUE 58 (ligne `Local`) | T-2 | C3 | Renvoi au contrat réduit de `BIBLIOTHEQUE/CONTRACTS` |
| BIBLIOTHEQUE 63 et 789 (ancienne ligne 762) | T-3 | D4 | Les deux listes de statuts reçoivent `SEED` |
| BIBLIOTHEQUE 173 | T-5 | B3 | Paire équivalente : seulement lorsque B1b est déclenché et que la paire couvre exactement la même décision (renvoi à `ACTION/GATE-B/B1b`) |
| `BIBLIOTHEQUE/DERIVE` | T-3 | C3 | Les quinze lignes sont conservées et rangées par phase : avant build (contrat réduit, 8 lignes), si le risque l'active, après observation, promotion |
| `BIBLIOTHEQUE/CONTRACTS` 258 | T-1 | C3 | Contrat réduit = décision initiale, responsabilité, contre-indication, preuve attendue, limite. C'est la seule définition ; la ligne `Local` et `DERIVE` y renvoient |
| Contrat de grille | F-BIB-003 | E1 | Les familles `MOBILE-*` ne s'appliquent que lorsque le mobile est dans le scope ou qu'un risque responsive est réel ; sinon `N/A-JUSTIFIED` |
| `BIBLIOTHEQUE/COMPONENTS` | T-1 | B5 | Nouveau bloc « Contrat de composant partagé » (13 lignes au format `text`). Il réunit la liste d'ACTION 588 et celle de SAVOIR 704. Il s'active pour un pattern réutilisable, un composant critique ou un composant partagé ; un delta local n'a aucune obligation. Les parts d'ACTION (baseline, migration, verdict) et de SAVOIR (jugement) y sont nommées |
| BIBLIOTHEQUE 707 (non-généricité) | T-3 | C7 | L'ablation révèle une dépendance. Une dépendance porteuse (relation déclarée, fallback) est conservée ; une dépendance décorative mène à changer la relation. Dans les deux cas, on décide sur le rendu entier, la tâche et `ACTION/GATE-C` |

**Diff :**
- BIBLIOTHEQUE : +50 / −23 ;
- CHANGELOG : +4 / −3.

Aucun contenu nouveau au-delà des cibles décidées (B5 C2, C3 C4). Les lignes `PILOT`, `Partagé` et `Durable` du contrat minimal sont inchangées (C3 T-2).

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| **`SEED`** | `validate_design_governance.py` **vert**. La garde de D4 O-1, posée rouge en 12.03, est levée par le texte, comme prévu (R-4) |
| LCF-20 | Toujours verte : BIBLIOTHEQUE et CHANGELOG ont les mêmes cinq statuts |
| Gardes de la passe | D4 G-01 à G-04 et G-06 ; C3 G-01 à G-03 ; C7 G-01 ; B5-01 et B5-02 ; E1-06 : **toutes vertes** |
| Validateur de carte | Rouge seulement pour les motifs de la fenêtre : 20 LCF et le titre en double `DIRECTION/START`. Les nouveaux renvois (`ACTION/GATE-B/B1b`, `ACTION/GATE-C`, `DIRECTION/VISUAL_TARGET`, `BIBLIOTHEQUE/EVOLUTION`, `ACTION/RUN-SYSTEM`) sont tous servis |
| Suivi (`--fenetre --compare` 12.04) | **Cas significatifs : 149 → 160/300**, aucune alerte |
| B01 | 218/218 |

**Relecture de fin de passe (§22).** Zones relues : BIBLIOTHEQUE 50–63, 161–203, 205–275, 611–680, 700–712, 760–795, et le CHANGELOG en entier.

Aucune incohérence introduite. Un point relevé, laissé en l'état :
- la ligne `PILOT` du contrat minimal énumère encore « contre-indication » en plus du « contrat réduit » qui la contient déjà ;
- cette redondance vient de B01, et C3 T-2 a décidé de ne pas toucher cette ligne ;
- je la note sans la corriger : une correction non décidée n'entre pas en phase 12.

## 3. Écarts déclarés

- **Format du bloc DERIVE.** Les phases sont marquées par des lignes entre crochets à l'intérieur du bloc `text`, par exemple `[Avant build — contrat réduit]`. J'ai écarté des titres Markdown : les titres placés dans un bloc de code sont désormais ignorés par le lecteur de routes.
- **Aucun autre écart** avec les cibles décidées.

**Journal des notes de version (B03), ligne ajoutée :**

> 12.05a — Cycle de vie : statut `SEED` pour les routes du seed, dépréciation possible depuis tout état utilisé, sans revendication de gain. BIBLIOTHEQUE : contrat réduit unique, dérivation rangée par phase, contrat de composant partagé, familles mobiles conditionnées au scope, test de non-généricité fondé sur la dépendance.

## 4. Suite

**12.05b : passe ACTION.** C'est la plus dense. Elle regroupe B1 à B5, C1 à C4, D1 à D3 et E1 : table de correspondance de la RUN_CARD, promesse du validateur, formes (HANDOFF et CLOSE-PACKAGE), carte de lecture, profil strict, frontières du jugement, etc.

Elle rend verts les gardes ACTION, et en partie C5 (LCF-C1 et LCF-C2, dont le canon est dans ACTION/HANDOFF).
