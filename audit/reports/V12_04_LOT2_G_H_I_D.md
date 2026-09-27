# V1.2 — Unité 04 — Lot 2 : chantiers G, H, I, D' (étape 1, G2 et G3)

**Date :** 2026-09-27 · **Owner :** Junior (Kamel)
**Décision de l'owner (27-09-2026) :** « implémenter ce plan avant » la mini-épreuve, qui passe en dernier. Les recommandations de l'addendum (§7) sont prises comme validées : G en recommandation, H avec sources nommées, I retenu, pas d'équipe simulée.
**Base :** B05 après le lot 1 (`V12_03`). **Branche :** `v1.2/patch-decision-abd`, synchronisée avec la branche de session.

## 1. Étape 1 — documents de travail (`plans/`, hors package)

| Fichier | Contenu |
|---|---|
| `plans/atlas_references_v0.md` | 10 références fortes, 8 contre-exemples, 7 principes visuels ; double colonne visuel / fond (chantier E') |
| `plans/veille_vague3.md` | Marqueurs des vagues 1, 2, 3, sources, mécanisme de glissement (D') |
| `plans/carte_moyens_v0.md` | Plafond et sources de qualité par couche, route de production, traitement des assets moyens (H, I) |

## 2. Lot 2 — PATCH-DECISION exécutable (`audit/tools/V12_Patch_Lot2.py`, 14 entrées)

| Entrées | Chantier | Où | Effet |
|---|---|---|---|
| L2-G1, L2-G2 | G | `FIRST-OBJECT`, skill | L'objet de preuve est **de préférence codé** (composant, donnée, état, interaction) ; une illustration ne porte la scène que fournie, curatée ou générée dirigée |
| L2-H1 | H | `SAVOIR`, `[VEILLE 2026-09]` | Carte des moyens par couche : sources, jamais styles ; en HTML seul, figuratif et contenu réel hors plafond |
| L2-V1 | H, I | Route de production (`VISUAL_TARGET`) | Renvoi à la carte ; un asset moyen reçoit un traitement justifié, jamais un dessin de remplacement |
| L2-I1 | I | `SAVOIR`, section `DESIGN-ATLAS` | Traitement des assets moyens : un seul traitement cohérent, justifié par la thèse ; ne masque ni droit inconnu ni image hors sujet |
| L2-D1 | D' | `SAVOIR`, `[VEILLE 2026-09]` | Vague 3 datée, source nommée |
| L2-C1 à L2-C4 | C- | `FIRST-OBJECT`, skill | Coupes de doublons (méta-phrase, renvoi de colonne, qualités déjà définies dans `VISUAL_TARGET`, quota de variantes déjà interdit) |
| L2-CH1 | — | CHANGELOG « Non publié » | Lot 2 ; 42 → 50 conditions |
| L2-R1, L2-L1, L2-L2 | Gardes | `validate_reading_map.py` | LCF-46 étendue à la vague 3 ; LCF-47 à LCF-50 |

## 3. Résultats

| Contrôle | Résultat |
|---|---|
| `--verifier` sur B05 | 14/14 |
| Gardes du lot 2 sur B05 (gardes seules) | **4/4 rouges** (LCF-47 à 50) |
| Après patch | `validate_reading_map` vert, **50 conditions** |
| Mutations | Lot 2 : **5/5 rouges** (dont LCF-46 sous injection d'un marqueur de vague 3) ; lot 1 : 4/4 toujours rouges |
| `validate_all` | FULL VALIDATION PASSED |
| 22 harnais (comparés à `V12_Instantane_harnais_B05_G3.json`) | **300/300**, témoins 40/40, 0 rouge ; instantané `V12_Instantane_harnais_B05_Lot2.json` |
| Harnais R ; R03 | 30/30 ; 18/18 |
| 13.01 texte ; non-régression B01 | 6/6 ; 5/5 |
| 13.02 | 38/38 |
| Budget de lecture (`V12_Budget_lecture.py`) | 9 604 → **9 591 mots** (−13), 614 lignes ; depuis V1.1.1 : 9 608 → 9 591 (−17) |
| B01 | 218/218 |

## 4. Écarts déclarés

1. **Séquencement inversé** par l'owner : le lot 2 précède la mini-épreuve, qui ne peut donc plus l'informer ; elle évaluera A, B, D, G, H, I ensemble.
2. **Décision 2 de G1 dépassée** : H relève du chantier C, que G1 renvoyait après G4. L'owner l'a fait entrer maintenant. L'atlas (E') reste hors package, conformément à G1.
3. **Emplacement de I** : l'addendum visait `SAVOIR/CRAFT` ; le paragraphe sur les effets et les rôles d'asset se trouve en réalité dans la section `DESIGN-ATLAS` de SAVOIR. I y est placé, et la garde LCF-49 y pointe. Détecté par la garde elle-même (rouge après le premier essai).
4. **Garde existante étendue** : LCF-46 couvre désormais aussi la vague 3 (entrée L2-R1), avec une mutation propre.
5. **Sources nommées dans H** (Google Fonts, Lucide, shadcn, Unsplash…) : ce sont des sources, pas des styles, datées `[VEILLE]` ; décision de l'owner via l'addendum.
6. **Même auteur** pour les textes, les gardes et les contrôles : aucune revue extérieure.

## 5. Lecture

- **Certain :** B05 porte A, B, D, G, H, I et D' ; tous les contrôles existants sont verts ; le budget de lecture est légèrement en baisse.
- **Hypothétique :** que l'agent suive ces textes, déclare son plafond, choisisse un objet codé et traite ses assets au lieu de dessiner. C'est l'objet de la mini-épreuve, désormais dernière étape avant G4.

## 6. Suite

**Mini-épreuve V1.2** (addendum §5 et §6) : C3 (brief vague + B05) ×2, C3r (même brief + « c'est pour mon vrai commerce ») ×1 ; juge neuf avec le brief riche intégral, captures avec défilement ; comparaison avec les 6 rendus B-DLA.
