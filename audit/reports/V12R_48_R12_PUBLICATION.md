# V1.2 — R12 : publication de V1.2.0

**Date :** 01-10-2026.
**Décision de l'owner :** option (a). V1.2.0 est publiée comme expérimentation maintenue, avec l'efficacité `NOT-VERIFIED` déclarée ; G4 (juges extérieurs) viendra après la publication.

**Pièces :**
- patch : `audit/tools/V12R_Patch_R12.py` (+ `_fichiers/` : notes de version, `validate_structure.py`) ;
- compilation : `audit/tools/V12R_Compile_release.py` ;
- diff : `audit/diffs/V12R_R12_publication.diff` ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_R12.json` ;
- livrables : `releases/V1.2.0/`.

## 1. Diff

| Lieu | Changement |
|---|---|
| Manifeste, CHANGELOG, README du package, README officiel, QUICKSTART, README Local (build) | Version 1.2.0 ; date du 2026-10-01 |
| CHANGELOG | Section « Non publié — candidate V1.2 » devenue « V1.2.0 — Refonte : noyau de fabrication, trace graduée et consolidation (2026-10-01) ». Ligne d'efficacité : le palier R10 oriente sans prouver ; G4 reste à faire |
| README, fiche de version | CI hébergée observée ; noyau compilé et liste de chargement unique |
| `RELEASE_NOTES.md` | Réécrites pour V1.2.0 : présentation, changements, compatibilité, contenu, parcours courant, contrôles et CI, frontière du validateur (réserve 5), limites (efficacité, convergence, coût, CI, champs libres) |
| `validate_structure.py`, FAC-01 | Les notes de version doivent déclarer l'efficacité `NOT-VERIFIED`, G4 et ce que le validateur atteste |

Le schéma `RUN_CARD` est inchangé (décision 3). Aucune règle normative ne change.

## 2. Résultats

- **Gardes :** rouges avant (FAC-01 ×3 sur les anciennes notes ; manifeste en 1.2.0 contre CHANGELOG en 1.1.1), vertes après.
- **Mutations :** 3/3 rouges (CHANGELOG revenu à V1.1.1 ; titre du QUICKSTART resté en V1.1.1 ; notes sans efficacité déclarée).
- **Suivi :** VERT (389 cas, aucune migration). **13.01 :** texte 6/6, mutations 6/6, non-régression 5/5, distributions 9/9. **13.02 :** 38/38. **Sondes AP1 et AP4a :** vertes. **B01 :** 218/218.

## 3. Livrables (`releases/V1.2.0/`)

| Fichier | Contenu | SHA-256 |
|---|---|---|
| `Design_Governance_V1.2.0_GITHUB.zip` | Distribution GitHub, 62 fichiers | `5025c8ec…3d4d` |
| `Design_Governance_V1.2.0_LOCAL.zip` | Export Local, 58 fichiers | `49bfa461…41a5` |
| `Design_Governance_V1.2.0.md` | Contenu complet compilé depuis l'archive GitHub | `a6be17e7…d87f` |
| `SHA256SUMS.txt` | Empreintes complètes | — |

- **Reproductibilité (certain) :** un second build indépendant, depuis une copie fraîche du package, donne des empreintes identiques pour les deux archives.
- **Étiquette :** `v1.2.0`, posée sur le commit de publication.

## 4. Écarts et limites

- **Changement de format du fichier compilé.** Celui de V1.1.1 avait été produit sans outil conservé. Désormais, `V12R_Compile_release.py` le régénère, en entourant chaque fichier d'un bloc délimité par des tildes plus longs que toute suite de tildes du contenu, pour que le Markdown reste lisible.
- **`main` reste en V1.1.1.** Fusionner la candidate dans `main` et créer une « Release » GitHub sont des actions visibles hors de ce dépôt de travail. Elles attendent une décision explicite de l'owner.
- **Réserves maintenues :** 1 et 4 (efficacité, G4), 7 (champs libres). La CI n'a pas été observée sous macOS ni sous Windows.
