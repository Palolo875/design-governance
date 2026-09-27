# V1.2 refonte — Unité R3 — Alignements (D-01, D-02, D-07, D-08, D-12, D-13)

**Date :** 2026-09-27
**Plan :** `plans/Plan_V1.2_Refonte.md`, lot R3 ; registre `V12_11` §4 ; méthode M1 à M4 (`V12R_02_PROPOSITION_R2`).
**PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R3.py` (33 entrées ; validateur de structure remplacé par sa version R3). **Diff :** `audit/diffs/V12R_R3_alignements.diff`.

## 1. Corrections et gardes

Chaque correction entre avec sa garde (M4).

| Défaut | Correction | Garde de propriété (`validate_structure.py`) |
|---|---|---|
| **D-01** deux vocabulaires | « anti-direction » remplacé par `MODAL` / `PARTI` dans DIRECTION (contrat `TARGET`, vues, `RUN-PRIORITY`, traduction humaine, table `VISUAL_TARGET` : champ « Modal / parti »), ACTION (table de correspondance, projection `direction.anti_direction` inchangée), SAVOIR, skill, exemples, QUICKSTART | **Vocabulaire retiré** : le terme n'apparaît plus hors du CHANGELOG (historique) |
| **D-02** prise de brief compressée | Résumés de la skill, de QUICKSTART et du CHANGELOG fidèles au canon : « contenu réel, marque, asset principal ou route autorisée, destination si elle est incertaine » | **Fidélité des résumés** : tout paragraphe qui dit « au plus trois » porte la condition canonique |
| **D-07** marqueurs et carte hors d'atteinte | Le boot (`MODAL`) renvoie aux marqueurs datés de `SAVOIR/TOOLS` ; la route de production cite `SAVOIR/TOOLS` (renvoi résolvable) ; balises `ANT-01` et `MOY-01` | **Renvois** : `CREATIVE-BOOT` → `ANT-01` et `VISUAL_TARGET` → `MOY-01`, atteignables en un saut |
| **D-08** glossaire en retard | Onze termes ajoutés : thèse, ancre, Creative Boot, `MODAL`, `PARTI`, `FABRICATION`, plafond, objet de preuve, défaut dominant, vérité de scène, slop | **Glossaire** : chaque terme a sa ligne |
| **D-12** QUICKSTART | Une seule table des cinq questions (la version la plus complète, au démarrage) ; §2 y renvoie ; vouvoiement (7 formes) | **Lignes de table uniques** (tous fichiers) ; **registre** (QUICKSTART) |
| **D-13** coquille | Espace initiale supprimée | — (typographie ; pas de garde, déclaré) |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| **Rouge avant** (B05 + R2, avec le validateur R3) | 36 erreurs : exactement les défauts ciblés (2 concepts, 2 renvois, 11 occurrences de vocabulaire, 3 résumés, 11 termes, 1 doublon, 4 tutoiements) |
| **Vert après** | `STRUCTURE VALIDATION PASSED` : 10 concepts, 2 renvois, vocabulaire, résumés, glossaire, lignes uniques, registre |
| **Mutations** | 10/10 rouges (inverse d'une entrée par type de garde) + 2/2 mutations de migration (LCF-24, LCF-28) |
| `validate_reading_map` | Vert (50 conditions) |
| Suivi : harnais | **387 maintenus verts ; 2 migrés** (R-17, R-21), garde de remplacement verte et justifiée |
| Suivi : cliquets | Chemin prescrit **23 849** (réf. 23 891, −42) ; négations **862** (−1) ; doublons **186** (−4) ; listes distinctes 5 |
| `validate_all` | Vert |
| 13.01 ; 13.02 | 6/6 et 5/5 ; 38/38 |
| B01 | 218/218 |

## 3. Écarts déclarés

1. **D-16 retiré de R3.** Les deux modèles à trois niveaux de SAVOIR (intrinsèque / construite / prouvée ; correction / précision / intention) ne sont pas des doublons : ce sont deux axes différents. Les aligner changerait le sens. Le point passe en R5c (restructuration de SAVOIR).
2. **Condition canonique reformulée.**
   - « destination si elle n'est pas évidente » devient « destination si elle est incertaine », dans `EXTERNAL-START` comme dans ses résumés.
   - Raisons : même sens ; charte « positif d'abord » ; la formule négative recopiée trois fois faisait monter le cliquet des négations (+3).
   - Le mot « destination » et l'ordre, vérifiés par LCF-44, sont inchangés.
3. **Nom de champ « Modal / parti ».** La première version (« Modal et parti ») faisait rougir LCF-28, qui découpe les noms de champs sur « et ». La garde protège une propriété légitime ; c'est le libellé qui a été ajusté, pas la garde.
4. **Migrations M1.**
   - R-17 et R-21 (harnais R) inversaient des textes de R.01 (P-06, P-15) que R3 a réécrits.
   - Leur propriété est toujours portée par LCF-24 et LCF-28, vertes.
   - Leur sensibilité est démontrée par deux mutations de migration (rouges).
   - La table de correspondance les marque `OBSOLETE`, avec garde et justification.
5. **Budget par périmètre.** Le chemin prescrit (LETTRE) baisse de 42 mots. Les périmètres ACTUEL et TABLE montent de 41 mots : le renvoi du boot vers les marqueurs, la ligne « Modal / parti » plus explicite, la prise de brief complète dans la skill. Le cliquet porte sur LETTRE, conformément à M3.
6. **Atteignabilité inchangée en texte chargé** (7/25 en TABLE). Les marqueurs et la carte sont désormais **garantis à un saut** par une garde, mais pas encore dans le texte chargé : c'est l'objet de R4 (noyau).

## 4. Lecture

- **Certain :**
  - les six défauts ciblés sont corrigés et protégés par des gardes de propriété (rouge avant, vert après, mutation rouge) ;
  - deux cas de harnais sont migrés sans perte de propriété ;
  - les cliquets baissent.
- **Probable :** les gardes « vocabulaire retiré », « fidélité » et « lignes uniques » empêcheront le retour des dérives observées (D-01, D-02, D-12) lors des réécritures de R4 et R5.
- **Limite :** la garde de registre repose sur une liste de formes de tutoiement. Elle ne couvre que QUICKSTART et que ces formes.

## 5. Suite

**R4 — noyau de fabrication.** C'est le lot qui doit changer le rendu :
- balisage des blocs normatifs ;
- `build_core.py` ;
- skill réécrite (noyau compilé, liste de chargement unique, sortie en langage produit, marqueurs dans le noyau, décision 7) ;
- exemple de fabrication.

Puis le point de contrôle **P1** (mini-épreuve).
