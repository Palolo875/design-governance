# DG-AUDIT-001 — Phase 2 — Validateur RUN_CARD, plage 3/4 : assemblage, oracles et fichier ciblé

## Périmètre, reprise et baseline

Lecture intégrale A–D des **lignes 327–381/590** de `audit_work/package/scripts/validate_run_card.py` : ordre `validate_card`, oracle `check_fixture`, auto-contrôle `check_schema_authority` et `validate_single_path`. Les plages **1–149** et **150–326** ont été relues dans leurs rapports respectifs ; le checkpoint des 25 fixtures, le plan maître et le protocole externe v2.0 §12 fixent la continuité. Les appels concrets de la suite et le routage CLI, lignes 382–590, ne sont consultés ici qu'en tant qu'interfaces : lecture intégrale à la prochaine unité.

Baseline B01 stable : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucune écriture dans le package.

## Passage A — architecture de la décision automatique

| Lignes | Fonction et branche | Effet et limite explicite |
|---|---|---|
| 327–334 | `validate_card` enchaîne `check_held_message` → `check_semantic_contract` → `check_strict_contract` si demandé → `validate_node`. | Un diagnostic métier lisible prend le pas sur le schéma, mais un type inattendu ou une URL mal formée peut lever une exception brute avant ce dernier : F-VRC-003. |
| 337–355 | `check_fixture` lit puis valide une carte ; pour un positif, tout `ValidationError` ajoute une erreur ; pour un négatif, il exige un rejet et contrôle sa sous-chaîne `expected_message` **si elle est fournie**. | L'oracle positif est réel ; un négatif sans message attendu réussit sur n'importe quelle `ValidationError` : F-FIX-003. La fonction ne découvre pas d'elle-même les fichiers du répertoire : F-FIX-001. |
| 358–368 | `check_schema_authority` copie le schéma, remplace l'enum de `mode` par `SCHEMA-DRIVEN-TEST`, met le même mode dans l'exemple et échoue si la carte est rejetée. | Prouve l'acceptation d'une valeur ajoutée dans cette configuration ; ne prouve pas que la suppression du contrôle de l'enum serait détectée. |
| 370–379 | `validate_single_path` lit le fichier choisi, transmet `source_path` et `strict`, renvoie 0/1 avec un en-tête PASS/FAILED pour `ValidationError` et `OSError`. | Assure une interface ciblée, mais ne capture ni `UnicodeDecodeError` (F-VRC-002), ni `TypeError`/`ValueError` issus de certaines entrées invalides (F-VRC-003). |

La relation avec ACTION est claire : les contrôles de structure et les oracles ne concluent pas qu'un risque a été couvert, qu'une provenance est vraie ou qu'un artefact a été inspecté. Le contrôle métier s'exécute en premier pour nommer un défaut utile ; le schéma ferme ensuite la carte pour les cas bien typés. `source_path` est transporté au mode strict, mais la plage précédente a montré qu'il n'est pas utilisé pour ancrer les chemins locaux (F-VRC-005).

## Passage B — épreuves et limite des tests actuels

Toutes les mutations et substitutions de fonction suivantes sont **en mémoire**. Les deux fichiers illisibles ont été créés dans un dossier temporaire extérieur au package, puis supprimés. Le code, les fixtures et les sources propriétaires restent inchangés.

| Épreuve | Résultat | Ce qui est établi |
|---|---|---|
| `valid_closed_return.json` sous `check_fixture(..., should_pass=True)` ; `invalid_accepted_without_provenance.json` sous `should_pass=False` avec son message attendu | Aucune erreur ajoutée dans les deux cas | Les deux classes d'oracle fonctionnent sur des cas connus et doivent rester protégées. |
| `invalid_missing_proof.json` en mémoire avec preuve et provenance ajoutées, mais `mode=BOGUS` | Sans `expected_message`, **aucune erreur de suite** ; avec sous-chaîne de preuve attendue, « diagnostic inattendu » | Confirme F-FIX-003 : le premier rejet peut être complètement étranger à la faute nommée. |
| `validate_single_path` sur fichier absent, puis fichier JSON mal formé | Code 1 et en-tête `RUN_CARD VALIDATION FAILED` dans les deux cas | L'échec ciblé est contrôlé pour `OSError`/`JSONDecodeError` enveloppés par `load_json`. |
| Variante mal encodée UTF-8, objet dans `proof.observed`, liste comme `issue`, URL mal formée sous `--strict` | Code 1 avec traceback et **sans** en-tête `RUN_CARD VALIDATION FAILED` | F-VRC-002/003 traversent les `except` actuels ; il s'agit d'erreurs de diagnostic, pas d'acceptations invalides. |
| Exemple valide avec `mode=BOGUS-MODE`, code intact | REJECT `run_card.mode : valeur non canonique` | L'enum fonctionne **actuellement** ; le constat nouveau porte sur sa protection contre régression. |

**Mutation discriminante de l'autorité du schéma.** Une substitution en mémoire de `validate_node` omet **seulement** la vérification de l'enum principal `run_card.mode` et de l'enum temporaire créé par `check_schema_authority` ; les deux conditions `if` du schéma, les autres enums, les autres propriétés et les contrôles métier restent actifs. Dans cet état, l'exemple muté avec `mode=BOGUS-MODE` passe. `check_schema_authority(schema, errors)` renvoie néanmoins **`errors=[]`**. En exécutant ensuite la **suite intégrée entière** sous cette substitution, `main([])` retourne **0** et imprime `RUN_CARD VALIDATION PASSED`. La suite actuelle ne contient pas de fixture `mode` invalide qui ferait échouer cette mutation. Les tests n'ont pas été modifiés sur disque ; ceci montre la limite de l'oracle, tout en préservant le fait que la baseline non mutée rejette le mode inconnu.

## Passage C — lecteurs et conséquences de l'ordre actuel

Le mainteneur qui exécute uniquement la suite obtient un vert utile sur 24 fixtures appelées et l'exemple ; il ne peut pas inférer que l'enum principal resterait actif après une modification du validateur. L'intégrateur qui soumet un fichier précis obtient un verdict explicite pour un fichier absent ou mal formé, mais certaines valeurs de mauvais type passent par une trace Python avant le schéma. Un agent qui répare une fixture composite a besoin du premier diagnostic **et** d'un voisin valide après réparation ; le message seul ne prouve pas l'isolation des 17/22 négatifs composites. Le reviewer maintient la différence entre une carte bien formée et une décision vraie sur l'artefact.

Le cas positif `CLOSED + RETURNED + RETURN`, l'exploration avec ancre non transformée et le profil complet restent des repères de non-régression. Rien dans cette plage n'impose de modifier leur sens ou la règle d'ACTION qui sépare état, issue, statut de direction et verdict.

## Passage D — constat nouveau et déduplication

### F-VRC-006 — auto-contrôle de l'enum des modes ne détecte pas sa disparition

- **Preuve :** `check_schema_authority` ne pose que le test positif « valeur ajoutée au schéma puis acceptée ». Sous une substitution **ciblée** qui désactive l'application de l'enum principal `mode`, ce test ne signale aucune erreur, un mode `BOGUS-MODE` est accepté, et la suite intégrée reste verte. Le schéma et la baseline non modifiés rejettent aujourd'hui ce mode ; l'écart concerne la **non-régression** d'un contrôle déclaré comme dépendant du schéma.
- **Effet :** un changement futur qui fait perdre la contrainte de mode peut passer la suite sans signal alors que le mode gouverne les obligations conditionnelles, notamment trace et paquets DIRECTION. La mutation ne démontre pas que toutes les contraintes du schéma pourraient disparaître sans être remarquées ; elle isole cet enum et ses cas de suite.
- **Owner pressenti :** `check_schema_authority`, choix de fixtures et oracle de `validate_run_card.py`. **Gravité provisoire significative** pour la couverture d'une décision structurante. Épreuve future : garder le test positif d'extension, ajouter un test négatif de mode inconnu et une mutation qui désactive uniquement le contrôle du mode ; exiger que la suite devienne rouge. Préserver la validation des cinq modes canoniques.

F-VRC-006 est distinct de F-FIX-001 (fichier présent non appelé), F-FIX-002 (plusieurs invalidités) et F-FIX-003 (fixture appelée sans diagnostic attendu). Son point de défaillance est le **test d'autorité du schéma** et l'absence d'un voisin négatif pour le mode. F-VRC-002/003 sont confirmés par le filtrage des exceptions ; F-VRC-004/005 restent des limites du mode strict dont `source_path` est transmis mais non exploité. F-RC-001 et les constats ACTION sur la sémantique du run restent propriétaires de leurs mécanismes. Toute fusion, sévérité finale ou patch attend les phases prévues.

Le registre passe de **126 à 127 constats provisoires** : 101 propriétaires + 16 façades/contrats antérieurs + F-RC-001 + trois F-FIX + **six F-VRC**. Aucun fichier de la cible modifié, aucun verdict global.

**Prochaine unité : lignes 382–590/590** du même script. Relire le protocole §12, ce rapport, les trois précédents et B01 ; examiner parsing des arguments, absence de schéma, chemins relatifs/absolus, choix strict versus suite, les 25 appels, les messages attendus, codes de sortie et le contrôle d'autorité. Recompter les fichiers de fixtures couverts et les scénarios manquants ; puis produire le checkpoint complet des 590 lignes avant d'ouvrir un autre script.
