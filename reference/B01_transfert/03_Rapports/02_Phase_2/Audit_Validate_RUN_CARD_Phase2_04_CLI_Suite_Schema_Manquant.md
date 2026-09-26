# DG-AUDIT-001 — Phase 2 — Validateur RUN_CARD, plage 4/4 : CLI, suite et schéma indispensable

## Périmètre et reprise

Lecture intégrale A–D des **lignes 382–590/590** de `audit_work/package/scripts/validate_run_card.py`. Les trois plages antérieures sont **1–149**, **150–326**, **327–381** : ensemble, elles couvrent le script sans trou ni recouvrement. Le protocole externe v2.0 §12, `Audit_Validate_RUN_CARD_Phase2_03_Assemblage_Oracles_Cible.md`, les deux rapports précédents, le checkpoint des 25 fixtures et le plan maître ont été repris. L'interface du README du package (lignes 100 et 128–136) distingue la suite sans argument, la validation d'un fichier ciblé et `--strict` ciblé. Cette lecture achève le parcours sectionnel ; le **checkpoint cumulatif du validateur** reste la prochaine unité.

Baseline B01 inchangée : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucune modification des fichiers audités.

## Passage A — carte des branches de `main`

| Lignes | Branche | Garantie actuelle et limite |
|---|---|---|
| 382–398 | `path` optionnel, `--strict` booléen, liste `errors` | Le mode sans chemin signifie suite intégrée ; un chemin signifie validation ciblée. |
| 399–408 | Présence puis chargement de `SCHEMA`, exigence d'un objet racine | JSON mal formé ou racine non objet ajoutent un diagnostic ; absence de fichier laisse `schema` **non initialisé**, objet `{}` ne déclenche **aucune** erreur. |
| 410–418 | Refus de `--strict` sans chemin ; résolution du fichier ciblé depuis le répertoire courant, appel à `validate_single_path` | Mode strict réservé au ciblé ; la suite seule ne passe pas les fixtures sous `--strict`. Chemin ciblé explicite transmis au contrôle (F-VRC-005 rappelle qu'il est ignoré pour l'ancrage d'un artefact relatif). |
| 420–575 | Exemple officiel et 24 fixtures codées en dur | Trois positives, 21 négatives ; 20 négatives possèdent un `expected_message`. La 21e (`invalid_missing_proof.json`) n'en a pas ; une fixture sur disque n'est pas appelée. |
| 576–585 | `check_schema_authority`, liste d'erreurs et résumé PASS/FAILED | Un contrôle positif d'extension d'enum existe (F-VRC-006) ; les erreurs captées conduisent au code 1. Si `schema={}`, ni suite ni contrôle d'autorité ne s'exécutent et le code 0 est imprimé. |
| 588–590 | `sys.exit(main())` | Transporte normalement le code 0/1 ; une exception hors handlers produit un traceback. |

Le schéma et le validateur sont des moyens de contrôler une projection locale, non une preuve qu'un rendu ou une décision humaine satisfait ACTION/DIRECTION/SAVOIR. Les branches du script s'exécutent sur l'exemple et les fixtures du package en mode ordinaire ; le fichier utilisateur ciblé suit une autre route. Confondre les deux résultats masquerait la différence entre une suite verte et une carte effectivement soumise.

## Passage B — résultats contrôlés et inventaire exact

Analyse syntaxique des appels `check_fixture` et comparaison par noms avec `schemas/fixtures` : **25 appels au total**, dont **un exemple hors dossier** et **24 fichiers du dossier sur 25** ; le dossier contient **22 `invalid_*` et trois `valid_*`**. Les 24 appels du dossier sont 21 négatifs et trois positifs. **20/21** négatifs appelés contrôlent une sous-chaîne `expected_message`. L'unique négatif appelé sans message est `invalid_missing_proof.json` (ligne 430) : F-FIX-003. L'unique fichier jamais appelé est `invalid_capability_profile_missing_basis.json` : F-FIX-001. Les **17/22** négatifs composites consolidés par les trois rapports de fixtures restent F-FIX-002. Aucun nouveau calcul ne transforme ces ratios en couverture d'exécution réelle d'artefact.

| Invocation sur la baseline | Code et résultat | Protection ou frontière |
|---|---|---|
| `python3 scripts/validate_run_card.py` | 0, `RUN_CARD VALIDATION PASSED` | Suite intégrée et contrôle d'autorité positif passés sur la baseline. |
| Même commande avec `--strict` seul | 1, `RUN_CARD VALIDATION FAILED` | Chemin JSON ciblé exigé ; la suite ne teste pas automatiquement le profil strict. |
| Ciblée sur `valid_closed_return.json` | 0, `RUN_CARD VALIDATION PASSED — fichier ciblé` | Positif `CLOSED + RETURNED + RETURN` préservé. |
| Ciblée sur `invalid_missing_proof.json`, puis copie temporaire à mode inconnu | 1 dans les deux cas, diagnostic contrôlé | Rejet actuel réel ; la protection de la raison du premier rejet reste F-FIX-003. |
| Schéma temporaire contenant JSON mal formé ou racine `null` | 1, échec contrôlé | Deux branches de prévalidation fonctionnent. |

**Contre-épreuve schéma, sans modifier `SCHEMA` sur disque :** substituer au chemin du schéma du module un emplacement temporaire, puis appeler `main` en mémoire. Si le fichier est **absent**, `errors.append(...)` a lieu, mais `schema` n'est pas assigné ; la suite, le ciblé et le ciblé strict lèvent `UnboundLocalError` avant d'afficher l'échec collecté. Si le fichier existe avec le contenu **`{}`**, la racine satisfait `isinstance(schema, dict)` mais est fausse au test `if schema` : la suite, un fichier ciblé **invalide** et même un fichier ciblé avec `--strict` rendent tous **code 0** et la phrase générale `RUN_CARD VALIDATION PASSED — projection validée contre le schéma et fixtures contrôlés`, alors qu'aucun fichier de carte ni aucune fixture n'a été lu. Une racine objet non vide mais incomplète telle que `{"type":"object"}` lève `KeyError: 'properties'` dans `check_schema_authority` au lieu d'un diagnostic contrôlé. Ces deux familles de défaillances sont séparées ci-dessous.

Le README annonce qu'un fichier ciblé absent, mal formé ou sémantiquement invalide échoue. Cette promesse est tenue avec le schéma officiel présent ; elle ne l'est pas quand le fichier de schéma est vide, puisque le ciblé est sauté. Les substitutions ci-dessus portent sur le **chargement de dépendance**, pas sur une nouvelle carte qui contournerait un schéma sain.

## Passage C — lecteurs sous contrainte

Un mainteneur voit que l'exemple et les fixtures déclarées passent en mode ordinaire ; il doit tout de même comparer le dossier à la liste codée et vérifier le chargement effectif du schéma. Dans un pipeline, un code 0 annoncé pour un document jamais lu risque d'être interprété comme une validation concluante ; le test du schéma `{}` est donc plus grave qu'un simple mauvais message. Un intégrateur qui soumet sa carte avec `--strict` ne bénéficie pas d'un jeu de fixtures strictes dans la suite sans argument ; les écarts sur hôtes de démonstration et chemins relatifs restent F-VRC-004/005. L'agent et le reviewer gardent la frontière entre une chaîne de preuve présente et une observation exécutée sur le rendu livré.

Les positifs `valid_closed_return`, `valid_direction_exploratory_untransformed` et `valid_direction_with_profile_decision` restent des exemples valides nécessaires. Le contrôle actuel refuse effectivement un mode inconnu ; F-VRC-006 démontre seulement que la suite pourrait perdre cette protection sans virer au rouge.

## Passage D — constats, déduplication et suite

### F-VRC-007 — schéma vide : succès sans validation ni lecture du fichier ciblé

- **Preuve :** un schéma existant réduit à `{}` ne déclenche pas l'erreur de racine ; ses deux tests de vérité sautent `validate_single_path`, toutes les fixtures et `check_schema_authority`. `main([])`, `main([chemin-invalide])` et `main(["--strict", chemin-invalide])` rendent **0** avec le message de succès de la suite. Aucun objet de carte n'est lu dans ces trois appels.
- **Effet :** un schéma accidentellement vidé rend le feu vert indépendant du contenu de la carte. Ce n'est pas une hypothèse sur une correction future : le flot de contrôle de la baseline produit déjà ce résultat lorsque sa dépendance est vide. **Gravité provisoire majeure** pour la fiabilité du gate, à reclasser après analyse des build/distributions et des consommateurs.
- **Owner pressenti :** initialisation/prévalidation du schéma dans `main`. Épreuve de résolution future : schéma vide ou incomplet → échec contrôlé avant toute annonce de validation, code non nul, et fichier ciblé effectivement lu seulement après reconnaissance des invariants du schéma attendu. Distinct de F-VRC-006, qui concerne le test de régression d'un enum sur un schéma sain.

### F-VRC-008 — schéma absent ou objet incomplet : exception brute au lieu du diagnostic prévu

- **Preuve :** `SCHEMA.is_file() == False` ajoute bien « schéma absent » à `errors`, puis l'utilisation de `schema` non initialisé lève `UnboundLocalError`, avant la sortie FAILED. Un objet schéma non vide mais incomplet `{"type":"object"}` passe le test de racine, puis l'accès direct à `properties.run_card.mode.enum` dans `check_schema_authority` lève `KeyError` pendant la suite.
- **Effet :** ces entrées ne sont pas validées et le processus échoue, mais avec un traceback non maîtrisé au lieu d'un diagnostic sur la dépendance. **Gravité provisoire mineure à significative** selon la manière dont les consommateurs affichent les échecs. Owner pressenti : même prévalidation de dépendance, plus contrôle de forme avant le test d'autorité. La suppression du schéma ne doit jamais mener au code 0 ; traiter l'absence et l'incomplétude explicitement et préserver les cas d'erreur JSON déjà contrôlés.

F-VRC-007 (**faux succès**) et F-VRC-008 (**échec non contrôlé**) sont distincts par leur impact et l'épreuve de non-régression, même si leur correction peut partager une prévalidation unique. F-FIX-001/002/003, F-VRC-001 à 006, F-RC-001 et les owners ACTION/DIRECTION/SAVOIR conservent leurs preuves et limites ; la phase 10 pourra fusionner ou reclasser avec un raisonnement explicite. Pas de nouvel ID pour le fait attendu que `--strict` exige un chemin ou que la suite ordinaire n'ouvre pas l'artefact réel.

Le registre passe de **127 à 129 fiches provisoires** : 101 propriétaires + 16 façades/contrats antérieurs + F-RC-001 + trois F-FIX + **huit F-VRC**. Les **590/590 lignes** du validateur ont désormais un rapport de lecture, sans décision finale sur le script, les distributions ou le système. Aucun patch du package.

**Prochaine unité : checkpoint cumulatif du validateur.** Reprendre les quatre rapports, le checkpoint des fixtures, le protocole §12 et B01 ; contrôler les plages adjacentes, les huit F-VRC avec preuves et owners, les trois F-FIX, F-RC-001, les protections positives, les lacunes de suite et le risque de faux succès du schéma `{}`. Fixer l'ordre des autres scripts (`validate_contracts.py`, lecteur de routes, build/manifeste/workflow selon inventaire) seulement après inventaire exact de leurs appels et dépendances. Phase 2 encore ouverte ; ni patch normatif ni verdict global.
