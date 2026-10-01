# V1.2 — AP5b : raccords de chargement et de précision (C15 option a, C25 à C31)

**Date :** 01-10-2026.
**Décision de l'owner :** « (a), allons-y pour AP5b ». Textes soumis dans `V12R_45` §3 et appliqués tels quels.

**Pièces :**
- patch : `audit/tools/V12R_Patch_AP5b.py` (+ `_fichiers/` : `validate_contracts.py`, `validate_structure.py`) ;
- diff : `audit/diffs/V12R_AP5b_raccords.diff` (package et harnais C9) ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP5b.json`.

## 1. Diff

| Constat | Lieu | Changement |
|---|---|---|
| C15 (a) | `validate_contracts.py` | Toute exigence déclarée (états, responsive, accessibilité, robustesse) doit figurer dans `coverage_map`. Message : « exigence déclarée non couverte ». Cas unitaire C15-1. ACTION/UI-UX-REALITY est inchangé : il disait déjà « la couverture de chaque exigence » |
| C15 (a) | `production_contracts.example.json` | 8 entrées ajoutées : 2 `OBSERVED` (desktop 1440 et clavier, dans `observed_scope`), 6 `NOT-VERIFIED`. Aucun `PASS` artificiel |
| C25 | `CHARGE`, lignes STANDARD et DIRECTION, compilées dans le noyau | « `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l'expression ou la preuve » |
| C26 | Déclencheurs critiques ; `ACTION/ROUTING` ; `SAVOIR/STYLE` | Mêmes conditions que `CHARGE` : `STATE` **ou** `INTEGRITY` selon la question ouverte ; `COMPONENTS` si un composant change ; `FRAME` si le cadrage est à éclaircir |
| C27 | `BIBLIOTHEQUE`, contrat de composant partagé | Le delta local est qualifié : il ne doit porter aucune responsabilité critique, réutilisable ou partagée ; sinon, il relève du contrat, avec reclassement par `DIRECTION/START` |
| C28 | `BIBLIOTHEQUE/MICRO`, avant/après | Validité de la comparaison distincte de la version retenue ; l'original peut être retenu (`ACTION/B1b`) |
| C29 | `BIBLIOTHEQUE/SUPPORT`, test de masquage | La dépendance porteuse avec repli est recevable (`BIBLIOTHEQUE/GATE`) ; le masquage sert à diagnostiquer |
| C30 | Question de convergence (noyau) | « …si rien ne les justifie, reconsidère-les » |
| C31 | `SAVOIR/TECH`, preuve par médium | « cinq responsabilités de preuve, regroupables dans un même artefact » |
| — | CHANGELOG | Entrée « Raccords de chargement et de précision (audit progressif, unité 5b) » |

**Gardes ajoutées :**
- 4 résumés fidèles (C26, C27, C28, C29) ;
- 3 vocabulaires retirés (C28, C30, C31) ;
- 4 lignes FAC-01 (C25 ×2, C26 ×2) ;
- CORE-01 étendue (C25) ;
- cas unitaire C15-1 dans les contrats.

## 2. Rectification déclarée du harnais C9 (règle 5)

- **Cas concerné :** P-P1, « liaison exacte, tous les états couverts → accepté ». Sa base ne couvrait que 2 des 12 exigences hors états.
- **Pourquoi il tombait (certain) :** il encodait l'ancienne règle (« états seuls ») que la décision C15 (a) remplace. Ce n'est pas une régression du patch.
- **Rectification :** la base `pc_base` couvre chaque ligne des trois autres matrices (`NOT-VERIFIED`, sauf « focus visible » en `OBSERVED`), et le libellé devient « toutes les exigences déclarées couvertes → accepté ».
- **Ce qui est conservé :** l'intention de P-P1 (une liaison exacte est acceptée) et le cas négatif P-02 (état omis → refusé). C9 passe à 11/11 sur l'ancien package comme sur le nouveau.
- **Aucune migration** dans la table de correspondance.

## 3. Résultats

- **Gardes :** rouges avant (12 erreurs de structure ; l'exemple de contrat refusé par la règle C15), vertes après.
- **Mutations :** 11/11 rouges, dont « couverture limitée aux états » qui fait rougir C15-1.
- **Suivi :** VERT. 389 cas, 363 maintenus, 26 obsolètes avec gardes établies ; `validate_all` vert. Cliquets : 13 835 mots, négations 820, doublons 142, une liste.
- **13.01 :** texte 6/6 ; mutations 6/6 ; non-régression 5/5 ; distributions 9/9 (Linux, Python 3.10 et 3.13, archives construites depuis une copie, pas de CI hébergée).
- **13.02 :** 38/38. **Sondes AP1 et AP4a :** vertes. **B01 :** 218/218.
- **Mesures :** chemin prescrit 13 785 → 13 835 mots (+50) ; noyau 4 552 → 4 602 mots (+50, déclencheur `DOMAIN-FRAME` sur deux lignes de `CHARGE`).

## 4. Écarts et limites

- **Rectification du harnais C9 :** §2.
- **Effet sur les rendus et l'usage :** non observé.
- **Audit progressif externe :** les 39 constats ont tous une disposition (correction appliquée, limite ou réserve maintenue), sans certification d'effet.
