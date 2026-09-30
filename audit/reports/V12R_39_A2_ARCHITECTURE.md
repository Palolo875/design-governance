# V1.2 refonte — A2 : une seule liste de chargement (AUD-01), plancher SAVOIR dans le noyau (AUD-02), lieu de la trace légère (AUD-05)

**Date :** 30-09-2026 · **Décision de l'owner :** « Allons-y » sur les options recommandées (a) de `V12R_38` §5.
**Patch :** `audit/tools/V12R_Patch_A2.py` (+ `_fichiers/`, dont `build_core.py`). **Diff :** `audit/diffs/V12R_A2_architecture.diff`. **Instantané :** `audit/snapshots/V12R_Instantane_suivi_A2.json`.

## 1. Forme retenue pour AUD-01 (écart déclaré)

L'option (a) prévoyait de transformer les trois tables concurrentes en renvois. Or la « Carte de lecture par mode » d'ACTION et les « Déclencheurs critiques » de DIRECTION sont lus par des contrats existants :
- conditions de façade LCF-17 et LCF-25 ;
- garde CHG-09 ;
- harnais C4 (G-01 à G-03) et D1 ;
- épreuves 13.02 (O-C4, déclencheurs).

Les supprimer aurait imposé des migrations de harnais. **Forme appliquée :**
- les tables restent, mais sont déclarées **vues de `DIRECTION/CHARGE`** : chacune porte une phrase de renvoi, et leurs chargements forcés deviennent conditionnels ;
- `CHARGE` absorbe les déclencheurs de DIRECTION §2 dans sa colonne « Ajouter seulement si » ;
- **cette colonne entre dans le noyau.** Auparavant, seules les deux premières colonnes étaient compilées : la liste « ajouter si » n'était jamais vue par l'agent. C'est un constat nouveau, relevé pendant l'unité, et la raison de ce choix.

## 2. Diff

| Constat | Lieu | Changement |
|---|---|---|
| AUD-01 | ACTION, Responsabilité | « Dans un run, le chargement suit `DIRECTION/CHARGE`, seule liste de chargement. Pour lire ACTION hors run, commencez par… » |
| AUD-01 | ACTION, carte de lecture | Déclarée vue de `CHARGE`. Socle `STATUS` et `PRECONDITION` « dès que le run écrit un statut, un gate ou un verdict (trace complète) ». En-tête : « Sections d'ACTION appelées par la route » |
| AUD-01 | DIRECTION §2, déclencheurs critiques | Phrase de renvoi. « Détail final » passe de `[FORCÉ]` à « Conditionnel : colonne « Ajouter seulement si » de `DIRECTION/CHARGE` » |
| AUD-01 | `ACTION/ROUTING` | Renvoi à `CHARGE`. « Spec DIRECTION » : `CRAFT`, `TYPE` ou `SOURCE` si la composition, la typographie ou l'ancrage restent ouverts |
| AUD-01 | `DIRECTION/CHARGE`, ligne DIRECTION (colonne 3) | Ajout : `CFT-03`, `STATE` ou `INTEGRITY` si un détail final peut changer le caractère ou la robustesse ; `INTEGRITY` avant un verdict (trace complète). Reformulation « si la tension, le geste produit ou un anti-choix peuvent… » (voir §4) |
| AUD-01 | `build_core.py` | `CHARGE-TABLE` compilée avec toutes ses colonnes |
| AUD-02 | SAVOIR/TYPE, SAVOIR CFT-05 | Blocs noyau `COMP-TYPO` (typographie : langues, chiffres, licence, fallback…) et `COMP-COULEUR` (palette par rôles, contraste calculé, indice non chromatique), compilés dans la section « Composition » |
| AUD-02 | SAVOIR/READ, chemin minimal | « Sur le chemin d'un run, le plancher de ces obligations est compilé dans le noyau… ; leur détail s'applique lorsque la route est chargée » |
| AUD-05 | `TRA-01` (noyau) | « Elle s'écrit à côté de l'artefact quand l'agent écrit des fichiers (fichier de trace ou en-tête du fichier livré) ; sinon, après la réponse visible, sous « Trace » » |
| — | CHANGELOG | Entrée « Architecture du chargement (refonte, A2) » |

**Gardes :**
- 6 résumés fidèles (AUD-01 ×4, AUD-02, AUD-05) ;
- `LOAD_HEADERS` élargi aux tables « \| Mode \| Chargement… » ;
- nouvelle garde **CORE-01** : la section compilée doit porter la colonne « Ajouter seulement si », le plancher couleur et le plancher typographique.

## 3. Résultats

- **Gardes :** 11 erreurs avant, 0 après.
- **Mutations :** 10/10 rouges, dont l'en-tête concurrent rétabli, la colonne retirée du noyau, le bloc couleur retiré du registre et le plancher typographique retiré de la skill.
- **Suivi complet** (copie, puis package) : vert (§5).
- **Mesures :**
  - chemin prescrit 13 238 → **13 614 mots** ;
  - trace complète 18 347 mots ;
  - noyau **4 068 → 4 444 mots** (+376) : colonne « Ajouter seulement si », plancher couleur et typographique, lieu de la trace ;
  - doublons 142 (inchangé) ; outils 24/25.
- Consigne « qualité avant nombre de mots » : chaque ajout porte une règle déjà décidée, désormais lue par l'agent.

## 4. Écarts déclarés

- **Premier essai sur copie : suivi rouge.**
  - Symptôme : LCF-24 et R-03 échouaient, `validate_all` était rouge et les témoins T-1 tombaient.
  - Cause (certain) : une fois la colonne 3 compilée, la ligne DIRECTION de la skill contenait « si une tension, un geste produit… ». La condition LCF-24 interdit un compte de tensions dans les lignes « Creative Boot » de la skill.
  - Correction : reformulation « si la tension, le geste produit ou un anti-choix peuvent modifier… », sans changement de sens. Suivi vert ensuite.
  - Aucun harnais modifié ; défaut vu sur copie, avant application.
- **Tables conservées** au lieu d'être supprimées (§1).
- **Mesure du noyau :** comptage de la section « Noyau de fabrication » sans les balises, même convention avant et après.

## 5. Contrôles finaux

Sur le package appliqué :
- suivi **VERT** : 389 cas, 363 maintenus, 26 migrés, aucune migration nouvelle ; `validate_all` vert ;
- 13.01 : texte 6/6, non-régression 5/5 ;
- 13.02 : 38/38 ;
- B01 : 218/218.

## 6. Ce qui reste de l'audit

- **Lot façades :** AUD-06 (QUICKSTART, READING_MAP, `flow.md`, exemples), AUD-08 (exemple hors du domaine boulangerie), AUD-13 (forme courte LITE et trace légère).
- **AUD-07 :** convergence de concept.
- **AUD-16 :** limite de méthode.
- **Effet de A2 sur les rendus :** non observé (aucun run).
