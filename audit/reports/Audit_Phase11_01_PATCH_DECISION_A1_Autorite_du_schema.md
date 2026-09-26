# DG-AUDIT-001 — Phase 11.01 — PATCH-DECISION A1 : autorité du schéma

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée (`016e6002…` vérifié). B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.01 ». Ordre fixé en 11.00 : A1 → A2 → B1–B5…

**Grappe :** F-VRC-007 (Majeur), F-VCT-001 (Majeur), F-VRC-008, F-VRC-006, plus F-VCT-003 (rattachée ici, voir §4).

**Sorties :**
- cette `PATCH-DECISION` ;
- `A1_harnais_non_regression.py`, un **harnais de preuve écrit avant toute modification** (§21 : « définir la preuve avant modification »).

**Ce que ce document n'est pas :** un patch. Aucune ligne de B01 n'a été modifiée, et **aucun prototype de correctif n'a été écrit**. C'est volontaire : l'écart relevé par R01 était justement d'avoir patché avant de décider. La correction elle-même relève de la phase 12.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan et décision précédente | Plan maître ; `Audit_Phase11_00_DECISIONS_Owner_Sortie_Phase10.md` |
| Empreintes | B01 `016e6002…` conforme. Scripts ciblés : `validate_run_card.py` `ba60d5da…`, `validate_contracts.py` `ec6cbb62…` ; schéma `run_card.schema.json` `ea3d0511…` |
| Protocole | §21 (questions et types de correction), §22 (exigences du futur patch), §32 |
| Sources de niveau 5 | Rapports VRC 03–04 et VCT 01 de phase 2 ; 4.04–4.07 ; registre consolidé |
| Code relu | `validate_run_card.py` 51–70 et 327–590 (`validate_card`, `check_fixture`, `check_schema_authority`, `validate_single_path`, `main`) ; `validate_contracts.py` en entier ; `validate_all.py` (consommateur) |

## 2. Question 2 du §21 : le défaut est-il réel ? Oui, re-vérifié aujourd'hui

Plutôt que de m'appuyer sur les rapports, j'ai rejoué chaque défaut sur une **copie temporaire** de B01 avec le harnais. Résultat sur B01 : **témoins positifs 4/4, tests A1 0/11.** Chaque échec documente un défaut :

| Test | Mutation | Attendu après correction | B01 aujourd'hui |
|---|---|---|---|
| A1-01 | schéma RUN_CARD `{}`, suite | Échec gouverné | **code 0, PASSED** |
| A1-02 | schéma `{}`, carte **invalide** ciblée | Échec gouverné | **code 0, PASSED** (la carte n'est même pas lue) |
| A1-03 | schéma absent | Échec gouverné | Traceback |
| A1-04 | schéma `{"type":"object"}` | Échec gouverné | Traceback |
| A1-05 | enum `mode` retiré du schéma | Suite rouge | **code 0, PASSED** |
| A1-06 | enum retiré + carte `BOGUS-MODE` ciblée | Échec gouverné | **code 0, PASSED** |
| A1-07 à 09 | chacun des trois schémas de contrats `{}` | Échec gouverné | **code 0, PASSED** |
| A1-10 | mot-clé non supporté dans une branche non visitée | Échec gouverné | **code 0, PASSED** |
| A1-11 | enum `research_brief.depth` retiré | Suite rouge | **code 0, PASSED** |

**Deux précisions sur la phase 2 :**
- **A1-02 confirme le point le plus grave de F-VRC-007**, déjà noté en phase 2 : avec un schéma vide, `main` ne passe jamais par la validation ciblée, et une carte **invalide** demandée explicitement reçoit « PASSED », avec le message de la suite.
- **A1-05 et A1-06 rendent F-VRC-006 plus plausible.** La phase 2 l'obtenait en modifiant le **code** du validateur. Ici, une simple édition du **schéma** (retirer l'enum `mode`) suffit : la suite reste verte et une carte au mode inventé est acceptée en validation ciblée.

**Mécanisme commun :**
- `validate_run_card.main` saute tous les contrôles lorsque `schema` est vide (`if schema:`) ou non initialisé.
- `validate_contracts` ne visite que les branches présentes dans l'exemple, et ses mutations négatives réussissent sur **n'importe quelle** erreur. Le contrôle sémantique masque donc un schéma inopérant.

## 3. Les sept questions du §21

| Question | Réponse | Conséquence |
|---|---|---|
| Le défaut change-t-il une décision, une preuve, une exécution ou la maintenance ? | **Oui.** Le feu vert des deux validateurs est la preuve machine de toutes les RUN_CARD et contrats, et ce seront les outils des phases 12–13 | Corriger |
| Le fichier ciblé possède-t-il ce défaut ? | **Oui**, re-vérifié (§2) | — |
| Le gain dépasse-t-il la charge ? | **Oui.** Gain : un PASS de nouveau significatif pour tout le reste de l'audit. Charge estimée : 40 à 60 lignes par script, **aucun nouveau fichier**, aucune obligation nouvelle pour l'auteur d'une carte | Corriger |
| Le patch crée-t-il une nouvelle autorité ? | **Non, sous condition** : la prévalidation ne vérifie que ce que le code **utilise déjà** (racine objet, `properties.run_card.properties.mode.enum`, `required` à la racine des contrats, mots-clés supportés). Elle ne recopie pas le schéma | Condition C1 (§5) |
| Le patch est-il testable ? | **Oui** : harnais écrit **avant** (11 tests + 4 témoins) | Condition de sortie |
| Positif et défensif restent-ils équilibrés ? | **Oui.** Aucun effet sur les cartes valides ; les 25 fixtures gardent leurs résultats | Témoins T-POS |
| Une suppression ou une fusion résout-elle mieux ? | **Non.** Remplacer par la bibliothèque `jsonschema` ajoute une dépendance (SAVOIR/TECH 778, package « sans dépendance »). Un module commun aux deux scripts ajoute un fichier aux manifestes 60/56 et aux deux distributions. Ne rien faire laisse un faux PASS dans l'outil même de la phase 13 | Correction locale dans chaque script |

## 4. PATCH-DECISION

**Décision : CORRIGER.** Types §21 : **validateur** et **test**. Aucune correction normative : aucun texte propriétaire n'est touché.

**Propriétaire du correctif :** le mainteneur du package, sur les deux scripts. ACTION reste propriétaire du sens de la RUN_CARD. Les schémas ne changent pas.

### 4.1 `validate_run_card.py`

1. **Chargement gouverné du schéma**, avant toute branche (suite ou ciblée). Trois cas donnent `RUN_CARD VALIDATION FAILED` avec code 1 et sans traceback :
   - schéma absent ;
   - racine non objet ou vide : « schéma inopérant » ;
   - chemin `properties.run_card.properties.mode.enum` absent ou vide : « schéma incomplet ».
2. **Témoin négatif avant tout PASS**, en suite **et** en validation ciblée : l'exemple canonique, avec un mode sentinelle invalide, doit être rejeté par `validate_node` **seul** (niveau schéma, pas contrôle sémantique). S'il est accepté, l'échec est gouverné : « le schéma n'impose pas l'enum de mode ». Le test positif existant de `check_schema_authority` est conservé.
3. **Flot de `main`** : une demande ciblée ne retombe jamais sur la suite, et les deux messages de succès restent distincts.

### 4.2 `validate_contracts.py`

1. **Chargement gouverné de chaque schéma.** Sont refusés :
   - une racine vide ;
   - une racine sans `type: object` ;
   - une racine sans `required` non vide ;
   - tout mot-clé non supporté **n'importe où** dans le schéma (parcours statique, pas seulement les branches visitées par l'exemple).
2. **Témoin négatif au niveau schéma, par contrat** : l'exemple privé de sa première clé requise doit être rejeté par `validate` **seul**.
3. **F-VCT-003 rattachée** : un voisin `depth = "IMPOSSIBLE"` doit être rejeté par `validate` seul. C'est le même mécanisme de témoin. La fiche passe du lot technique E2 à A1 (registre mis à jour) : un deuxième cycle pour trois lignes ne se justifie pas (§32).

### 4.3 Hors périmètre (volontairement)

| Fiche | Pourquoi pas ici | Où |
|---|---|---|
| F-ACT-008 (fichier utilisateur refusé par le CLI des contrats) | Change l'interface d'usage, pas l'autorité du schéma | C9 |
| Oracles à message attendu (F-FIX-003, F-ALL-001) | Ils portent sur la raison d'échec des négatifs, pas sur l'autorité du schéma | A2 |
| Exceptions brutes hors schéma (F-VRC-002/003, F-VCT-002) | Robustesse des diagnostics | E2 |

Garder A1 étroit respecte le §22 : un propriétaire, deux fichiers, un seul mécanisme.

## 5. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Pas de nouvelle autorité** : la prévalidation ne vérifie que des chemins que le code déréférence déjà ; aucune copie de contrainte métier du schéma |
| C2 | **Aucun nouveau fichier** : les auto-tests vivent dans les suites existantes, en mémoire (comme `check_schema_authority`). Les manifestes 60/56 restent inchangés |
| C3 | **Compatibilité avec `validate_all.py`** : il ne lit que les codes de retour et l'absence de traceback. Les bannières `PASSED` / `FAILED` sont conservées |
| C4 | **Sans dépendance** : bibliothèque standard seulement |
| C5 | **Diff lisible** : deux scripts, environ 40 à 60 lignes ajoutées chacun ; pas de refactorisation hors périmètre |
| C6 | **Documentation** : une ligne dans les notes de version du prochain lot publié. Pas d'entrée CHANGELOG, qui gouverne le cycle de vie des routes, pas les outils |

## 6. Condition de sortie et non-régression

**Le correctif A1 sera accepté en phase 13 si et seulement si :**
1. `A1_harnais_non_regression.py` donne **4/4 témoins positifs et 11/11 tests A1** sur la copie corrigée ;
2. `validate_all.py` rend `FULL VALIDATION PASSED`, avec des archives reproductibles ;
3. les 25 fixtures gardent leur résultat (valide ou rejetée) ;
4. le diff se limite aux deux scripts (C5).

**Garde-fou.** Le harnais est un artefact d'audit, hors package. Il travaille toujours sur une copie temporaire. Rejoué sur B01, il redonne 0/11 : il sert aussi de **preuve du défaut**.

## 7. Effets sur le reste du registre

- **A2 (oracles)** pourra s'appuyer sur un schéma dont l'autorité est garantie : ses tests à message attendu gagnent leur sens.
- **B2 (invariants d'acceptation, D-ACT-1 = c)** : les invariants ajoutés au validateur ne vaudront que si A1 empêche qu'un schéma vidé les désactive tous.
- **B02 (gelée)** : son PASS avait été obtenu sur des validateurs exposés à A1-01/02 ; cela s'ajoute aux limites déjà notées.

## 8. Sortie

- **PATCH-DECISION A1 : CORRIGER**, sous les conditions C1 à C6 et la condition de sortie du §6.
- Grappe A1 : 5 fiches (4 + F-VCT-003 rattachée). Registre mis à jour ; les totaux par gravité ne changent pas.
- Aucun patch, aucun prototype, aucun verdict global.

**§32 — ce que l'unité a changé :**
- chaque défaut re-vérifié par exécution plutôt que cité ;
- un effet déjà connu rendu plus plausible (F-VRC-006, par simple édition du schéma) ;
- la preuve écrite avant la modification ;
- une fiche mineure rattachée pour éviter un cycle de plus ;
- trois alternatives écartées avec leur raison.

**Prochaine unité : 11.02 PATCH-DECISION A2** (oracles de test : F-FIX-002, F-FIX-003, F-ALL-001, et F-FIX-001 à examiner pour rattachement), avec la même méthode : re-vérification par harnais, puis décision.
