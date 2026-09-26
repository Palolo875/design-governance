# DG-AUDIT-001 — Phase 2 — Validateur RUN_CARD, plage 1/4 : chargement, schéma et HELD

## Périmètre et continuité

Lecture intégrale A–D des **lignes 1–149/590** de `audit_work/package/scripts/validate_run_card.py` : imports et chemins (1–23), `ValidationError` et fonctions de type (25–49), `validate_node` (51–125), `load_json` (127–136), `check_held_message` (138–147). La fonction `check_semantic_contract` commence ligne 150 et constitue la prochaine plage. Le protocole externe v2.0 §12, le plan maître et `Audit_RUN_CARD_Fixtures_Phase2_Checkpoint_Consolidation.md` ont été relus. Interfaces examinées : schéma `run_card.schema.json`, exemple, ACTION/STATUS 116–186 et ACTION/RUN_CARD 252–286 ; les appels de la CLI et les oracles de fixture ne sont ici que des interfaces, à lire exhaustivement plus tard.

Baseline B01 inchangée, contrôlée sur les fichiers : système compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; schéma `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889` ; exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194` ; validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucun fichier du package n'a été modifié.

## Passage A — architecture et responsabilités visibles

| Plage | Fonction | Propriété effective et borne |
|---|---|---|
| 1–23 | Imports, ROOT, SCHEMA, EXAMPLE, FIXTURES | Les trois chemins pointent dans le package à partir du script ; ce bloc ne choisit pas à lui seul un fichier utilisateur. |
| 25–49 | `ValidationError`, `format_path`, `type_matches` | Erreurs avec chemin lisible et reconnaissance de `object`, `array`, `string`, `null`, `boolean`, `number`, `integer`. `bool` est explicitement exclu des types numériques. |
| 51–125 | `validate_node` | Évalue les branches `allOf` conditionnelles et `anyOf`, puis `const`, `enum`, `type`, `minLength`, `minItems`, `items`, `required`, `additionalProperties=false` et les propriétés enfants. Premier échec levé comme diagnostic. |
| 127–136 | `load_json` | Lit en UTF-8 et transforme une erreur d'OS ou de syntaxe JSON en `ValidationError` ; perte des clés dupliquées et erreur d'encodage décrites en passage D. |
| 138–147 | `check_held_message` | Si `closure.state=HELD`, produit un message métier explicite avant que l'enum de schéma ne rejette la valeur. ACTION possède la distinction entre état et statut de direction. |

Le schéma livré contient **deux conditions `if`/`then` sous un `allOf`** : modes STANDARD/SYSTÈME et DIRECTION ; **un `anyOf`** pour les deux listes de preuve ; **un `const`**, dix `enum`, 74 `type` et 14 objets `additionalProperties=false` selon le comptage récursif du fichier. Les autres clés structurelles utilisées par ce schéma appartiennent à l'ensemble traité par `validate_node`. Les métadonnées `$schema`, `$id`, titre et description ne sont pas des règles de validation d'une carte. Le code possède aussi des branches `number`/`integer` que le schéma actuel n'exerce pas ; leur présence ne prouve aucune capacité générale sur d'autres schémas.

## Passage B — contrat réellement exercé

Les tests suivants ont chargé le code et le schéma **sans écrire dans le package** ; les variations de carte ont été réalisées en mémoire, avec fichiers temporaires seulement pour l'interface de lecture. `validate_node` a été invoqué directement quand il fallait isoler une règle de structure du contrôle métier exécuté avant elle par `validate_card`.

| Règle et entrée de contrôle | Observation | Portée |
|---|---|---|
| Exemple officiel inchangé | PASS | Bon voisin structurel, pas preuve d'un artefact exécuté. |
| Retrait de `trace_locator` avec modes STANDARD, SYSTÈME, DIRECTION, puis LITE sur copie de l'exemple | REJECT pour les trois premiers, PASS structurel en LITE | Les deux `if` actifs déclenchent l'obligation selon le mode ; ne tranche pas la persistance d'un run ITER. |
| `proof.observed=[]`, `not_verified=[]` ; puis une des listes non vide | REJECT pour les deux vides ; PASS pour chacune des alternatives | Le `anyOf` fonctionne en conjonction avec le `required` du même objet. |
| `mode=INVALID`, champ racine inconnu, `owner="  "` | Trois rejets ciblés avec chemin et diagnostic appropriés | Enum, fermeture de l'objet et texte non blanc fonctionnent. `strip()` rend le test de longueur volontairement exigeant pour des chaînes d'espaces. |
| `closure.state=HELD` | REJECT avec « HELD est un statut de direction, pas une valeur de state » | Le diagnostic propriétaire précède l'enum générique ; cohérent avec ACTION/STATUS. |
| `type_matches(True, "number")`, `type_matches(True, "integer")`, `type_matches(None, "null")` | False, False, True | Cohérence des branches primitives ; les types numériques ne sont pas présents dans le schéma RUN_CARD actuel. |

Le contrôle des conditions examine la présence de `mode` puis son enum ou const ; si la condition ne correspond pas, il ne réclame pas la trace de cette branche. La fermeture `additionalProperties=false` opère à chaque objet qui l'énonce. Le validateur applique le `minLength` sur une chaîne *dépouillée de ses espaces*, ce qui évite qu'une valeur de remplissage composée d'espaces passe comme renseignée. `load_json` enveloppe bien les erreurs `OSError` et `JSONDecodeError`; sa frontière d'encodage reste incomplète, testée ci-dessous.

## Passage C — usage réel sous contrainte

Un auteur de carte peut choisir LITE et ne pas fournir `trace_locator` selon cette règle structurelle ; les propriétaires ACTION/DIRECTION décideront ultérieurement si le choix du mode et l'artefact sont légitimes. Un mainteneur peut relier le diagnostic `HELD` à la séparation état du run / statut de direction ; il n'a pas besoin de deviner quel enum est incorrect. Un intégrateur recevant un fichier provenant d'un éditeur ou d'une autre application s'appuie sur le résultat ciblé ; il doit pouvoir comprendre les fichiers rejetés et savoir précisément quelles valeurs ont été validées. Une équipe qui archive le JSON puis le relit doit s'assurer que le contenu validé est le même que celui présenté à ses lecteurs.

Les deux frontières de chargement suivantes concernent cette dernière attente. Les effets sont limités à des entrées JSON ambiguës ou mal encodées ; ni le schéma ni la suite des 25 fixtures n'ont ici démontré un contournement des contraintes pour une carte JSON ordinaire à clés uniques et en UTF-8 valide.

## Passage D — résistance, constats et déduplication

### F-VRC-001 — clés JSON répétées acceptées silencieusement

- **Épreuve :** ajouter à l'exemple valide `"mode":"NOT-CANONICAL","mode":"DIRECTION"` dans **le même objet**. `load_json` conserve le second `mode`, supprime silencieusement le premier et `validate_card` passe la carte résultante. Le fichier lu contient pourtant deux déclarations concurrentes d'un champ qui décide des obligations conditionnelles du schéma.
- **Effet :** la validation confirme l'objet *après* écrasement, sans signaler que le fichier source a perdu une valeur. Un lecteur ou un traitement qui lit l'entrée brute peut voir une ambiguïté absente du résultat. Aucun désaccord concret avec un autre parseur du package n'est encore démontré ; vérifier les consommateurs en phase 2 et lors des épreuves de résistance.
- **Owner pressenti :** lecture JSON du validateur et convention d'échange du package ; **gravité provisoire significative** pour l'intégrité et l'interopérabilité de l'entrée. Épreuve de réparation future : rejeter explicitement un champ répété à toute profondeur, tout en conservant les trois positifs des fixtures et les schémas valides.

### F-VRC-002 — UTF-8 invalide : exception non convertie en diagnostic du validateur

- **Épreuve :** charger un petit fichier temporaire contenant l'octet non UTF-8 `0xFF`. `Path.read_text(encoding="utf-8")` lève `UnicodeDecodeError`, qui n'est pas capturée par `load_json`. L'invocation ciblée de la CLI se termine au code 1 avec une trace d'exception en sortie d'erreur, **sans** `RUN_CARD VALIDATION FAILED` ni chemin métier ; une syntaxe JSON mal formée, elle, est convertie en `ValidationError` par cette fonction.
- **Effet :** automatisation et mainteneur voient un échec du processus, mais pas le diagnostic cohérent prévu pour un fichier soumis. Cela n'accepte pas un fichier invalide et n'est pas une faille de schéma. **Gravité provisoire mineure** ; owner pressenti : `load_json`/sortie de CLI. Épreuve future : une entrée invalide en UTF-8 doit donner une erreur contrôlée avec un message de lecture utile et conserver un code non nul.

Ces deux mécanismes sont distincts de F-FIX-001 (fixture jamais appelée), F-FIX-002 (scénarios multi-invalides) et F-FIX-003 (raison de rejet non gardée), tous maintenus. Les limites de chronologie, de combinaison issue/verdict, de provenance et de mode restent rattachées à ACTION, DIRECTION et F-RC-001 ; aucune nouvelle fiche n'est créée pour les contraintes structurelles qui ont passé les contre-épreuves. La lecture des lignes 150–326 peut modifier le classement provisoire et ajouter des interactions, sans fusion anticipée.

Le registre passe de **121 à 123 constats provisoires** : 101 propriétaires + 16 façades/contrats antérieurs + F-RC-001 + trois F-FIX + **deux F-VRC**. Aucun verdict global, aucune sévérité finale, aucun patch du système.

**Prochaine unité : lignes 150–326/590**, fonction métier `check_semantic_contract` et contrôles stricts `check_strict_contract`. Relire §12, ce rapport, le checkpoint fixtures, B01 et les clauses ACTION/DIRECTION pertinentes ; confronter chaque branche aux statuts, risques, ancres, preuves, provenance et aux positifs existants. Puis seulement 327–381 et 382–590 pour assemblage, oracles et CLI, en revenant sur F-VRC-001/002 avec l'analyse des consommateurs.
