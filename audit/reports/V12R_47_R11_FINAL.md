# V1.2 — R11 final : CI hébergée observée et dispositions finales des réserves de clôture

**Date :** 01-10-2026.
**Décision de l'owner :** « Allons-y pour R11 final ». Elle couvre l'ajout d'un workflow racine et l'observation d'un run GitHub Actions.
**Package :** inchangé.
**Pièce :** `.github/workflows/validate.yml`, à la racine du dépôt de travail.

## 1. CI hébergée (réserve 2, C38)

- **Constat (certain).** Le workflow du package vit dans `package/.github/workflows/`. GitHub ne l'exécute pas depuis ce dépôt de travail : aucun run n'avait jamais été observé.
- **Ce qui a été ajouté.** Un workflow racine, avec le même épinglage d'actions que celui du package (F-WF-001). Pour chaque version de Python (3.10, 3.11, 3.13) :
  - il contrôle la baseline B01 (218/218) ;
  - il lance `validate_all` depuis `package/` : package, RUN_CARD, contrats, carte, structure, build des deux distributions et reproductibilité.
- **Runs observés :** voir §1 bis.

### 1 bis. Résultat

| Run | Branche | Commit | Résultat |
|---|---|---|---|
| 1, 2 | branche de session | `55bce63` | Échec : fichier de workflow invalide (§3) |
| 3 (`36876916540`) | `claude/init-repo-claude-md-gm6njm` | `3ed8059` | **Succès** : 3 jobs (Python 3.10, 3.11, 3.13), ≈ 25 s |
| 4 (`36876917185`) | `v1.2/patch-decision-abd` | `3ed8059` | **Succès** : 3 jobs |

Journal du job Python 3.10.21 (run 3), lu :
- B01 218/218 ;
- `LOCAL VALIDATION PASSED` ;
- `ARCHIVE MEMBERS PASSED` (GitHub et Local) ;
- deux builds (reproductibilité) ;
- échecs attendus des fixtures et de la CLI, tous rencontrés ;
- `FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité`.

**Certain :** la candidate passe sa validation complète sur un runner GitHub hébergé (`ubuntu-latest`), sous trois versions de Python.

**Non couvert :**
- le suivi de refonte et les harnais d'audit (`audit/tools/`), qui ne sont pas dans ce workflow ;
- macOS et Windows ;
- un dépôt de distribution autonome.

## 2. Dispositions finales des réserves de clôture DG-AUDIT-001 (§3)

| Réserve | État au 01-10-2026 | Disposition finale avant R12 |
|---|---|---|
| **1** Efficacité `NOT-VERIFIED` | Palier exploratoire R10 en auto-comparaison, avec des juges modèles d'une seule famille (`V12R_35`, errata `V12R_41`). R10 arrêté par l'owner | **Maintenue.** Seule une épreuve à juges extérieurs (G4) peut la lever. V1.2.0 la déclare explicitement |
| **2** CI hébergée non observée | Workflow racine ajouté ; runs observés (§1 bis) | **Levée dans le périmètre observé** : Linux, Python 3.10, 3.11 et 3.13, dépôt de travail. Restent non observés : le workflow du package dans un dépôt de distribution autonome, ainsi que macOS et Windows |
| **3** Cas négatifs manquants | Six cas ajoutés en R11 ciblé (N1 à N5). Puis l'audit progressif en a ajouté d'autres : C02-1 et C02-2, C19-1 et C19-2 (RUN_CARD et contrats), C20-1, C15-1, ainsi que les témoins C12, C13 et du lecteur de routes (C11) | **Réduite ; reliquat déclaré.** Les invariants hors de ces domaines n'ont pas été réexaminés un par un |
| **4** Seize limites : une garde prouve une forme, pas un effet | Inchangé par nature | **Maintenue**, comme la réserve 1 |
| **5** Promesse du validateur | Tenue en un seul lieu (`VAL-01`, `ACTION/RUN_CARD`) ; profil strict corrigé (C02) | **Assumée et à communiquer** dans les notes de V1.2.0 (R12) |
| **6** Coût de lecture | Chemin prescrit d'un run `DIRECTION` : ≈ 23 600 mots (`V12_11`) → **13 835 mots**, soit −41 %. Noyau 4 602 mots. Coût du palier R10 : 1,7 à 1,8 × C1 en tokens, ≤ C4. Coût après A2 et AP non mesuré | **Réduite, limite déclarée.** La baisse des mots n'est pas une économie observée (D-23) |
| **7** Placeholders dans les champs libres | Maintien décidé par l'owner | **Maintenue**, sans filtre global |
| **8** Mineurs transmis | Q-04 à Q-13 et R-16 à R-32 disposés (R11 ciblé, `V12R_23`) ; 39 constats de l'audit progressif disposés (`V12R_40` à `V12R_46`) | **Close**, chaque point avec sa disposition dans l'inventaire |
| **9** Publication | V1.2.0 non publiée | **R12**, après feu vert de l'owner |

## 3. Écarts déclarés

- **Premier push : YAML invalide.** La ligne `run:` de l'étape B01 contenait « `': '` » sans être citée : c'est le même défaut que C01, dans un fichier neuf. Les runs 1 et 2 ont donc échoué sur une erreur de fichier de workflow. Correction en scalaire de bloc, validée localement par un parseur YAML avant le second push. La validation locale du YAML aurait dû précéder le premier push.
- **Périmètre.** Ce workflow observe la candidate dans le dépôt de travail, pas une distribution publiée. Le workflow propre au package sera observé dans le dépôt de publication, en R12.
