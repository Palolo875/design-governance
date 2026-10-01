# V1.2 — AP4a : validateurs (C11, C12, C13, C19, C20) et outil 13.01 (C21)

**Date :** 01-10-2026.
**Origine :** audit progressif externe, `DG_Audit_progressif_10`.
**Décision de l'owner :** « Allons-y pour AP4a ». C'est la première partie de l'unité AP4 coupée en deux : outillage seulement, aucune prose normative.

**Pièces :**
- patch : `audit/tools/V12R_Patch_AP4a.py` (+ `_fichiers/`, sept scripts) ;
- preuves directes : `audit/tools/V12R_Sonde_AP4a.py` ;
- diff : `audit/diffs/V12R_AP4a_validateurs.diff` (package et outil 13.01) ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP4a.json`.

## 1. Diagnostic (reproduit sur copie avant correction)

| Constat | Observation avant (certain) |
|---|---|
| **C11** | `read_route.py` sert en silence trois fautes que `validate_reading_map` refuse : un locator répété dans la table (la dernière ligne gagne), une ligne pointant vers un autre propriétaire (`SAVOIR.md` pour `DIRECTION/START`), et un second titre porteur du locator quand la route passe par la table |
| **C12** | Une clé répétée est écrasée sans erreur : `depth` IMPOSSIBLE puis valide est accepté dans un contrat ; une clé répétée dans le manifeste est acceptée |
| **C13** | Un mot-clé non interprété (`pattern` ajouté à `run_card.id`) est ignoré : la suite RUN_CARD reste verte |
| **C19** | RUN_CARD : `25:61` et le fuseau `+25:00` sont acceptés. Contrats : `2026-02-30` et `2026-13` sont acceptés |
| **C20** | Erreurs brutes au lieu de diagnostics : `closure.issue = []` donne une `TypeError` ; un schéma de contrat `[]` donne une `AttributeError` à la détection de type ; un Markdown non UTF-8 donne une `UnicodeDecodeError` sans nom de fichier, dans cinq commandes (`read_route`, `validate_reading_map`, `validate_structure`, `build_core`, `validate_design_governance`) |
| **C21** | 13.01 « distributions » : le manifeste n'était lu que dans la boucle des interpréteurs. Sans Python 3.10 ni 3.13, D-4 échouait alors que les archives étaient conformes, et l'absence d'interpréteur s'affichait comme un échec |

**Total : sonde rouge, 22 contrôles KO sur 36.**

## 2. Corrections

| Constat | Lieu | Changement |
|---|---|---|
| C11 | `read_route.py` | `parse_routes` refuse un locator répété. Par la table, le lecteur vérifie le propriétaire (`<PRÉFIXE>.md`), le titre de destination et l'unicité du titre porteur. L'absence de titre reste diagnostiquée « titre introuvable » |
| C11 | `validate_reading_map.py` | Deux **témoins du lecteur** (table à locator répété, propriétaire incohérent) : la protection est permanente dans le package |
| C12 | `validate_contracts.py`, `validate_design_governance.py` | Clé répétée refusée (`object_pairs_hook`) dans les contrats et le manifeste ; témoin dans la suite des contrats. RUN_CARD la refusait déjà (E2-17) |
| C13 | `validate_run_card.py` | Le schéma est contrôlé récursivement avant toute validation : seuls les mots-clés interprétés sont admis, plus les annotations (`$schema`, `$id`, `$comment`, `title`, `description`, `default`, `examples`). Témoin dans la suite. Le schéma livré n'utilise aucun mot-clé fautif |
| C19 | `validate_run_card.py` | Heure, minute, seconde et fuseau réels. Formes admises inchangées : date, date-heure, `Z` ou décalage. Cas unitaires C19-1 et C19-2 |
| C19 | `validate_contracts.py` | `source_date` : AAAA, AAAA-MM ou AAAA-MM-JJ avec des composants réels ; `unknown` toujours admis. Cas C19-1 et C19-2 |
| C20 | `validate_run_card.py` | Pré-passe : un champ à enum sans type reçoit le type de ses valeurs (« type attendu null, string »). Cas C20-1. L'ordre des diagnostics métier est inchangé : U-01 garde « HELD est un statut de direction » |
| C20 | `validate_contracts.py` | Schéma non objet à la détection de type : « schéma inopérant » |
| C20 | `read_route.py` (+ quatre commandes) | `non_utf8()` nomme les fichiers Markdown non UTF-8 avant toute lecture, sous la bannière d'échec de chaque commande. `validate_structure` utilise la forme « arrêt » (pas « contrôle complet ») : le suivi ne tient pas ses gardes pour établies |
| C21 | `DG_AUDIT_001_Verifications_13-01.py`, **rectification déclarée** | Manifeste lu dans l'archive GitHub, indépendamment des interpréteurs. Un interpréteur absent devient `INDISP.` (non exécuté), distinct d'un échec ; le code de sortie reste non nul tant qu'une ligne n'est pas exécutée |
| — | CHANGELOG | Entrée « Validateurs (audit progressif, unité 4a) » |

## 3. Preuves

- **Sonde (36 contrôles) :** rouge avant (22 KO), verte après (36/36), sur copie puis sur le package. Elle couvre aussi les cas qui doivent rester admis :
  - cinq routes légitimes, dont un raccourci et un sous-locator ;
  - dates valides (`Z`, décalage, AAAA, AAAA-MM, `unknown`) ;
  - suites des validateurs vertes.
- **Mutations de code : 7/7 rouges.** Locator répété accepté ; propriétaire non contrôlé ; clés écrasées ; `pattern` admis ; heure non contrôlée ; date de contrat non contrôlée ; type d'enum non contrôlé.
- **Suite RUN_CARD :** 87/87 cas unitaires, 10/10 locators admis, témoin C13. **Suite des contrats :** 22/22, témoin C12.

## 4. Contrôles finaux sur le package

- **Suivi :** VERT. 389 cas, 363 maintenus, 26 obsolètes avec gardes établies, aucune migration ; `validate_all` vert ; cliquets inchangés (13 774 mots, doublons 142).
- **13.01, par sous-contrôle :**
  - texte 6/6 ;
  - mutations 6/6 ;
  - non-régression 5/5 ;
  - distributions 9/9 (Linux ; Python 3.10 et 3.13 disponibles ici ; archives construites depuis une copie ; pas de CI hébergée).
- **13.02 :** 38/38. **Sonde AP1 :** verte. **B01 :** 218/218.

## 5. Écarts et limites déclarés

- **Correction en cours d'unité.** Une mutation est restée non rouge sur la première version, et elle a révélé un défaut de mon correctif : avec zéro titre porteur, `_unique([])` levait une `IndexError`. L'unicité n'est désormais contrôlée qu'à partir de deux porteurs ; l'absence de titre reste diagnostiquée. Le motif d'une mutation a été élargi au préfixe « témoin du lecteur : propriétaire incohérent », qui couvre les deux messages possibles.
- **Protections permanentes inégales.** C11, C12 (contrats), C13, C19 et C20 (type d'enum) ont un témoin ou un cas unitaire dans le package. C12 (manifeste) et C20 (Markdown non UTF-8, schéma de contrat non objet) ne sont prouvés que par la sonde.
- **Lecteurs du build non modifiés.** Les deux extraits Python de `build_distributions.sh` lisent encore le manifeste sans contrôle des clés. `validate_design_governance` le refuse en amont dans le même build, avant tout archivage.
- **Encodage.** `non_utf8()` parcourt les fichiers `*.md` du package, hors `.build`, `dist` et sauvegardes. Les JSON gardent leurs propres diagnostics de lecture.
- **Dates.** Les fractions de seconde restent libres en longueur. Les secondes intercalaires (`:60`) sont refusées.

## 6. Suite

**AP4b, façades :**
- C04 : trace légère dans QUICKSTART, GLOSSAIRE et READING_MAP ;
- C17 et AUD-08 : exemple de la skill ;
- C23 : liens vers « Commencer » ;
- C24, C33 et C39 : démarrage, livraison et ancienne entrée ;
- AUD-06 et AUD-13.

Comme en AP3, ce sont des textes : diagnostic et textes exacts soumis avant application.
