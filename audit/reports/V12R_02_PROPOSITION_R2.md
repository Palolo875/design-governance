# V1.2 refonte — Unité R2 — Proposition de PATCH-DECISION (gardes de propriété)

**Date :** 2026-09-27 · **Statut :** **proposition**, soumise à l'owner ; rien n'est appliqué.
**Entrées :** décision 2 (`V12R_00`), cartographie R1 (`V12R_01` §3).

## 1. Problème

- 156 cas de harnais sur 389 dépendent de la formulation exacte ; 58 d'entre eux via les 50 conditions LCF.
- Toute réécriture les fait passer au rouge, sans que la propriété protégée soit perdue.
- La décision 2 demande des gardes de propriété et une table de correspondance, sans abandon silencieux.

## 2. Quatre choix de méthode (règle 4 : aucun changement de méthode silencieux)

| # | Choix | Proposition | Alternative écartée | Raison |
|---|---|---|---|---|
| M1 | Migration des 156 cas sensibles | **Au fil de l'eau.** La table initiale marque les 233 cas structurels « maintenu » et les 156 cas sensibles « maintenu jusqu'à réécriture ». Chaque lot qui réécrit un texte ancré déclare l'obsolescence des cas touchés **et** fournit la garde de remplacement, verte. | Tout migrer en R2 (≈ 150 concepts balisés d'un coup) | On ne paie que les cas réellement touchés ; même rigueur (aucun rouge inexpliqué) |
| M2 | Ancrage d'une garde de propriété | **Balise invisible** `<!-- concept:ID -->` au lieu propriétaire. La garde vérifie : une seule définition, dans le bon fichier, non vide. `read_route.py` retire les balises à la lecture. | Citation de phrase dans un registre | Une reformulation ne casse pas la garde ; une suppression ou une copie la casse |
| M3 | Cliquets de refonte (chemin prescrit, négations, doublons, listes de chargement) | **Dans l'outillage d'audit** (`V12R_Suivi.py`) : valeurs de référence B05 qui ne peuvent que baisser | Dans le package | Ce sont des garde-fous du chantier, pas des invariants du produit |
| M4 | Entrée des gardes dans le package | **Chaque garde entre dans le lot qui la rend verte** (rouge avant, verte après, mutation rouge) | Gardes « rouges attendues » dès R2 | Respecte la règle 2 à la lettre ; `validate_all` reste vert à chaque lot |

## 3. Contenu de R2 si M1 à M4 sont retenus

**Hors package (audit) :**
1. `audit/data/V12R/V12R_Correspondance_harnais.csv` : 389 lignes (cas, catégorie R1, statut, garde de remplacement, lot, justification).
2. `audit/tools/V12R_Suivi.py` :
   - lance les harnais ;
   - vérifie qu'un cas est vert, ou déclaré obsolète avec une garde de remplacement verte ;
   - applique les cliquets M3 ;
   - produit un instantané.

**Dans le package (PATCH-DECISION exécutable `audit/tools/V12R_Patch_R2.py`) :**
1. `scripts/validate_structure.py` : moteur de concepts (registre `schemas/concepts.json` : ID, fichier propriétaire, rôle), appelé par `validate_all.py`.
2. `read_route.py` : les balises `<!-- concept:… -->` sont retirées de la sortie.
3. **Huit concepts d'honnêteté** balisés à leur lieu propriétaire. Ce sont les propriétés que la refonte ne doit jamais perdre (plan §6.7) :

| ID | Propriété | Lieu propriétaire |
|---|---|---|
| HON-01 | Vérité de scène : exemples marqués `ILLUSTRATIVE`, divulgation en langage produit | DIRECTION, vérité de scène |
| HON-02 | Pas de faux asset (abstraction, image générée ou placeholder présentés comme authentiques) | SAVOIR/INTEGRITY |
| HON-03 | Plafond déclaré quand une capacité manque (`FABRICATION`) | DIRECTION/CREATIVE-BOOT |
| HON-04 | Frontière de validation : ce que la machine atteste et n'atteste pas | ACTION/RUN_CARD |
| HON-05 | Agent seul, preuve dégradée | ACTION/RUN_CARD |
| HON-06 | `NOT-VERIFIED` plutôt qu'un `PASS` sans preuve | ACTION/STATUS |
| HON-07 | Une capture prouve un rendu, pas une tâche | ACTION (preuve) |
| HON-08 | Droits inconnus : `ACCEPTED` interdit | ACTION |

- **Rouge avant :** balises absentes, donc 8 concepts manquants.
- **Vert après :** 8 concepts présents, uniques et non vides.
- **Mutations rouges :** balise supprimée, balise dupliquée, balise déplacée dans une façade, bloc vidé.
- **Non-régression :** 389/389 (aucun texte réécrit) ; B01 218/218.

**Budget :** + 8 lignes de balises, invisibles à la lecture de route. Le chemin prescrit ne change pas en mots, car `read_route` les retire.

## 4. Critères

- **Réussite :** 8/8 concepts verts ; 4 mutations rouges ; table de 389 lignes sans cas orphelin ; `validate_all` vert ; suivi vert.
- **Arrêt :** si retirer les balises casse un cas de harnais, ou si une balise gêne l'export Local, retour à l'owner.
