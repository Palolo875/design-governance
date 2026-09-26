# DG-AUDIT-001 — Phase 11.15 — PATCH-DECISION C8 : intégrité de release

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ».

**Grappe C8 : 3 fiches, toutes Significatif.** Elles ont une conséquence commune : **l'archive livrée peut différer du package validé**, alors que toute la chaîne affiche `FULL VALIDATION PASSED`.

| Fiche | Mécanisme | Conséquence |
|---|---|---|
| F-BLD-001 | `zip` **met à jour** une archive existante au lieu de la recréer (build 147–154) | Un fichier retiré des sources reste dans le ZIP ; deux builds verts et reproductibles |
| F-BLD-004 | `cp -a` conserve les liens symboliques, puis `find -type f` les ignore à l'archivage (17–19, 33–35, 147–154) | Une release **amputée d'un fichier normatif**, code 0 |
| F-VDG-001 | L'inventaire exclut **tout** dossier nommé `.build` ou `dist`, où qu'il soit (validateur 56–70) | Un fichier non déclaré entre dans l'archive sous un PASS complet (jusqu'à une fuite) |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C8_harnais_non_regression.py`, qui exécute **le vrai build** sur des copies.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 à 11.14 ; A2 (motif exigé) ; C4 et C5 (outillage : un seul résolveur, validateur « carte et façades ») |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; tous les builds sur copie |
| Sources relues | `build_distributions.sh` (166 lignes, en entier) ; `validate_design_governance.py` 50–75 (`check_expected_files`) ; `validate_all.py` 78–97 (build et reproductibilité) ; `package_manifest.json` (github 60, local 56) |
| Antécédent | 4.09 : `ACTION.md` injecté en lien, les deux ZIP omettent le fichier normatif, build code 0 ; non-fusion de F-VDG-001 et F-BLD-001 confirmée |

## 2. Re-vérification : les trois défauts reproduits sur le vrai build

**Harnais C8 sur B01 : conservation 1/1, release 0/3.** Quatre builds complets, environ 5 secondes.

| Scénario (sur copie) | Code du build | Résultat observé |
|---|---|---|
| T-1 build propre | 0 | Membres = manifeste (60 / 56). **Le build est sain sur des sources saines** |
| R-1 ZIP ancien contenant `V1/official/ANCIEN_FICHIER_RETIRE.md`, sources propres | **0** | Le membre périmé **reste** dans l'archive GitHub |
| R-2 `GLOSSAIRE.md` remplacé par un lien vers un fichier hors package | **0** | `GLOSSAIRE.md` **absent des deux archives**. Le validateur l'avait accepté (`is_file()` suit le lien) |
| R-3 `V1/official/.build/non_declare.md` ajouté | **0** | Inventaire vert (le dossier est exclu), **fichier présent dans l'archive** |

**Constat qui décide de la forme de la correction.** Les trois défauts sont indépendants dans leur cause, mais **un seul contrôle les aurait tous arrêtés** : comparer, **après l'archivage**, les membres de chaque ZIP à la liste du manifeste. Aujourd'hui, le manifeste est comparé aux **sources**, jamais au **produit livré**. La reproductibilité (deux builds, mêmes empreintes) ne l'attrape pas : une archive périmée se reproduit à l'identique.

## 3. Les sept questions du §21

| Question | F-BLD-001 | F-BLD-004 | F-VDG-001 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : on publie autre chose que ce qu'on a validé | **Oui** : release sans fichier normatif | **Oui** : publication d'un contenu non déclaré |
| Défaut réel ? | Oui (R-1) | Oui (R-2 ; 4.09) | Oui (R-3) |
| Gain > charge ? | Oui : une ligne (`rm -f`) et le contrôle commun | Oui : une règle de refus | Oui : exclusion ramenée à la racine |
| Nouvelle autorité ? | Non : le manifeste existe déjà et devient la référence **du produit** | Non | Non |
| Testable ? | Oui (R-1) | Oui (R-2) | Oui (R-3) |
| Positif / défensif équilibré ? | Oui : aucun coût sur un build sain (T-1 reste vert) | Oui | Oui |
| Suppression ou fusion ? | **Correction d'outil** | **Correction d'outil** et **validateur** | **Correction d'outil** |

## 4. PATCH-DECISION

**Décision : CORRIGER.** Types §21 : **correction d'outil** et **validateur**.

Principe : **ce qui est livré est comparé à ce qui est déclaré.**

| # | Où | Correction | Fiche | Motif (A2) |
|---|---|---|---|---|
| O-1 | `build_distributions.sh` 147–154 | Les archives sont **créées dans le répertoire de travail** (`.build`), à partir d'un fichier absent, puis **déplacées** à la racine à l'étape de publication (156–161). Un build échoué ne laisse ni archive partielle ni archive ancienne modifiée | F-BLD-001 | — |
| O-2 | `build_distributions.sh`, après l'archivage | **Contrôle des membres** : pour chaque archive, l'ensemble des fichiers = la liste `github` ou `local` du manifeste, à l'identique, sans répertoire caché, sans membre en plus ni en moins. Le contrôle s'exécute avant la publication | F-BLD-001, F-BLD-004, F-VDG-001 | « membres de l'archive ≠ manifeste » |
| O-3 | `validate_design_governance.py` (`check_expected_files`) | **Politique de liens : refus.** Tout lien symbolique dans l'arbre du package est une erreur. **L'empaquetage explicite n'est pas retenu** : un lien peut pointer hors du package, ce qui ferait publier un contenu non inventorié | F-BLD-004 | « lien symbolique » |
| O-4 | `validate_design_governance.py` 56–70 | L'exclusion `dist` / `.build` ne vaut **qu'à la racine** du package. `__pycache__` reste exclu partout : le build le purge avant l'archivage (144), donc l'exclusion reste cohérente avec le produit | F-VDG-001 | « fichier inattendu » (message existant) |

**Pourquoi O-2 est dans le build et non dans `validate_all.py`.** `validate_all.py` appelle le build deux fois. Placer le contrôle **dans** le build garantit qu'aucune archive n'est publiée sans lui, même si le build est lancé seul (README 100, QUICKSTART).

**Pourquoi O-1 et O-4 malgré O-2.** O-2 **détecte** ; O-1 et O-4 **suppriment la cause**. Sans O-1, un ZIP ancien ferait échouer chaque build jusqu'à sa suppression manuelle. Sans O-4, l'inventaire resterait aveugle à un fichier que l'archive, elle, publierait.

**Hors liste close.** Ce sont des contrôles d'outillage de release, pas des invariants de run (frontière déclarée en C4, §4.5). Ils vont à l'inventaire des outils.

## 5. Inventaire à date : ajouts C8

| Objet | Changement | Nature |
|---|---|---|
| `build_distributions.sh` | Archives créées dans `.build` puis publiées (O-1) ; contrôle des membres contre le manifeste (O-2) | outil |
| `validate_design_governance.py` | Refus des liens symboliques (O-3) ; exclusion `dist` / `.build` limitée à la racine (O-4) | validateur |
| Suite A2 | Scénarios R-1 à R-3, chacun avec son motif | tests |
| Schémas, validateurs RUN_CARD et contrats | **Aucun** | — |

Candidats de migration de schéma encore ouverts : **C9, D2.**

## 6. Conditions du patch et de sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Dernier cycle d'outil** : O-1 à O-4 **après** toutes les corrections de texte et de schéma. Le manifeste est donc à jour au moment où O-2 devient bloquant. Toute grappe qui ajoute ou retire un fichier (aucune à ce jour : C4 et C5 n'en ajoutent pas) le déclare dans le manifeste |
| C2 | **Deux distributions** : O-2 contrôle GitHub **et** Local, y compris le `README.md` Local généré par le build (44–105) |
| C3 | **Reproductibilité conservée** : `validate_all.py` garde sa double construction. O-1 ne doit pas changer les empreintes d'un build sain (le témoin T-1 et la double construction le vérifient) |
| C4 | **Relecture complète** de `build_distributions.sh`, de `check_expected_files` et de `.github/workflows/validate.yml` (le workflow lance `validate_all.py`, donc le même build) |

**Sortie (phase 13) :**
1. `C8_harnais_non_regression.py` : conservation **1/1**, release **3/3**.
2. `validate_all.py` : `FULL VALIDATION PASSED`, reproductibilité incluse.
3. Harnais A1 à C7 verts.

**Limite déclarée.** Le contrôle des membres garantit que l'archive contient exactement les fichiers déclarés. Il ne garantit pas que le **contenu** de chaque fichier est celui qui a été relu ; ce point relève des empreintes de release (`SHA256SUMS`), déjà produites par la chaîne d'audit mais pas par le build. L'étendre au build serait une nouvelle capacité : **proposée, non décidée**. Je la verse à l'**observation** (lot F), sans patch.

## 7. Sortie

- **PATCH-DECISION C8 : CORRIGER.**
  - 4 corrections d'outil, dont **un contrôle commun** (membres = manifeste) qui ferme les trois fiches ;
  - 1 politique de liens : refus ;
  - 1 observation versée au lot F (empreintes dans le build).
- Listes closes inchangées : RUN_CARD et contrats **70 lignes, 66 actifs** ; LCF **16 entrées**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Trois défauts de causes différentes, **une seule absence** : le produit livré n'était jamais comparé à ce qui était déclaré.
- La correction ajoute ce seul contrôle et supprime les trois causes.
- Pour la première fois dans la phase 11, le harnais exécute **le vrai build**. Les trois défauts y sont reproduits avec un code 0.

**Prochaine unité : 11.16 PATCH-DECISION C9** (contrats de production et de cadrage : 4 fiches, F-ACT-008, F-DF-001, F-PC-002, F-RB-001 ; dernière grappe C, candidate à la migration de schéma, et inventaire des contrôles existants des contrats promis en C3).
