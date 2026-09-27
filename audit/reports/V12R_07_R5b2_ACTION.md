# V1.2 refonte — Unité R5b-2 — ACTION restructurée

**Date :** 2026-09-27 · **PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R5b2.py` (18 entrées, `validate_structure.py` remplacé). **Diff :** `audit/diffs/V12R_R5b2_action.diff` (6 fichiers, +46 / −24).

## 1. Décision et consigne de l'owner (27-09-2026)

- **R5b-2 : « Allons-y ».**
- **Plafond du noyau (écart 2 de `V12R_06`) : non adopté comme contrainte de coupe.** Consigne : ne pas réduire le nombre de mots au prix de l'efficacité ou du résultat ; une base solide et belle rend l'itération plus facile, même si elle coûte.
- **Règle appliquée désormais :** on ne retire que les doublons et le texte sans effet sur le rendu ; un ajout qui sert la fabrication est admis et déclaré.

## 2. Ce qui change

| Lieu | Changement | Effet attendu sur le rendu |
|---|---|---|
| `ACTION/GATE-A` (concept `GTA-01`) | **Profils de surface.** Pour une page vitrine, une application, une scène ou un support hors Web : contrôles d'office et contrôles selon le contenu. Un contrôle hors profil s'applique dès que l'élément existe. La trace légère renvoie au profil | Plancher d'accessibilité juste et rapide à appliquer, sans contrôles hors sujet |
| `ACTION/GATE-C` | Colonne **« Geste si absent »** : chaque critère C1 à C6 renvoie au geste de correction du noyau (§4 à §6). **En trace légère**, Gate C sert de contrôle de craft sur la capture, sans verdict écrit | Un défaut de craft débouche sur un geste, pas sur un constat |
| ACTION (responsabilité, parcours minimal, pipeline) | **Une seule description de la boucle** : `DIRECTION/DOUBLE-LOOP` (copiée dans le noyau). Les trois séquences d'ACTION deviennent des renvois ; le « parcours en cinq minutes » renvoie au noyau | Une seule boucle à suivre |
| `ACTION/RUN_CARD`, frontière de validation (`VAL-01`) | **Promesse du validateur tenue en un seul lieu.** Le README et la référence `machine_projection.md` gardent un résumé d'une phrase et un renvoi | Pas de copies qui divergent |

## 3. Résultats

| Mesure | Après R5b-1 | **Après R5b-2** |
|---|---|---|
| Chemin prescrit (LETTRE, trace légère) | 11 740 mots | 12 076 (+336 : gestes de Gate C et profils de Gate A, à dessein) |
| Trace complète (COMPLET) | 16 351 | 16 687 |
| Doublons (occurrences) | 161 | **152** |
| Négations | 812 | 809 |
| Noyau | 3 217 | 3 222 |

| Contrôle | Résultat |
|---|---|
| Rouge avant (nouveau validateur, package non patché, sur copie) | 7 erreurs : `GTA-01` et `VAL-01` absents ; 2 copies de la promesse ; 3 séquences de boucle dans ACTION |
| Vert après | `validate_structure` : 17 concepts, 6 vocabulaires retirés ; `validate_reading_map` : vert, **aucune rectification** |
| Mutations | **8/8 rouges** (7 inverses et 1 mutation de la carte d'ACTION, CHG-09) |
| Suivi | **Vert** : 372 cas maintenus, 17 migrés (inchangé), aucune migration nouvelle ; `validate_all` vert. Instantané : `V12R_Instantane_suivi_R5b2.json` |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 4. Écarts déclarés

1. **Carte de lecture d'ACTION non fusionnée dans `DIRECTION/CHARGE`.**
   - Elle est lue par le harnais C4 (G-01, G-03), par les épreuves 13.02, par `validate_design_governance.py` et par LCF-25.
   - La fusion aurait demandé plus de rectifications que de changements de texte, ce qui est le critère d'arrêt du plan.
   - Elle reste une vue d'ACTION, alignée en R5b-1 et désormais gardée : **CHG-09**, Gate B en `DIRECTION` seulement en trace complète.
   - CHG-09 était déjà vert avant ce patch (garde de consolidation, sans rouge avant) ; sa mutation le rougit.
2. **Garde « boucle unique » avec exemptions provisoires** pour SAVOIR, BIBLIOTHEQUE et README, qui portent encore leur séquence. Elles seront retirées en R5c, R5d et R6.
3. **Gestes de Gate C sans garde de propriété dédiée.** Il s'agit d'un ajout de contenu de fabrication, pas d'une propriété d'honnêteté. Ils sont protégés par le diff et le suivi.
4. **Ajout net sur le chemin (+336 mots)**, conforme à la consigne de l'owner (§1).

## 5. Lecture

- **Certain :**
  - une seule description de la boucle dans ACTION ;
  - une seule promesse du validateur ;
  - Gate A adapté au type de surface ;
  - chaque critère de Gate C mène à un geste ;
  - aucune propriété perdue.
- **Probable :**
  - les défauts de craft se corrigent au lieu d'être seulement constatés ;
  - moins de contrôles hors sujet sur une page vitrine.
- **Hypothétique :** l'effet sur le rendu perçu, à mesurer en R10.
- **Limite :** auto-comparaison.

## 6. Suite

R5a (DIRECTION : trois couches, une seule vue d'entrée, doublons, D-17, D-19), puis R5c, R5d, R6.
