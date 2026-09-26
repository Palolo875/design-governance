# DG-AUDIT-001 — Phase 2 — `validate_contracts.py` : schémas, oracles et CLI

## Cadrage, sources et intégrité

**Cible :** lecture complète **1–218/218** de `scripts/validate_contracts.py`, en passages A–D du protocole externe v2.0 §12. **Échelle :** script et interfaces aux trois schémas/exemples, à `validate_all.py` et aux auteurs des contrats. **Responsabilité pressentie :** valider un sous-ensemble documenté de JSON Schema et quelques liens sémantiques ; le script ne possède ni la vérité des preuves ni la décision créative. **Risque dominant :** annoncer un PASS après perte d'une règle structurelle ou prendre un échec quelconque pour la protection d'une règle précise. Aucun patch ou verdict global n'est autorisé dans cette unité de phase 2.

Baseline B01 revérifiée : compilation `Design_Governance_V1.0.md` SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole SHA-256 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`. Le script est incorporé aux lignes **7388–7605** de la compilation et reconstruit à l'identique sur **218 lignes / 10 975 octets**, SHA-256 `ec6cbb6254381c3aa1bd9115650bf77a572e2107db5457955b9c97ec90a1395e`. Les 60 unités reconstruites avaient déjà été comparées en lignes et octets à l'inventaire B01. Toutes les mutations ci-dessous portent sur des copies temporaires de cette reconstruction ; aucune source reçue n'est modifiée.

Rapports amont repris : `Audit_DOMAIN_FRAME_Phase2_01_Schema_Exemple_Couverture_Preuve.md` (F-DF-001/002), `Audit_RESEARCH_BRIEF_Phase2_01_Schema_Exemple_Sources_Incertitude.md` (F-RB-001/002), `Audit_PRODUCTION_CONTRACTS_Phase2_01_Schema_Exemple_Trois_Objets.md` (F-PC-001/002), le rapport de `validate_all.py`, le checkpoint RUN_CARD et le plan maître actif. La lecture des interfaces ACTION, DIRECTION et SAVOIR reste sous leurs propriétaires ; ce rapport ne les requalifie pas.

## Passage A — architecture visible, 1–218/218

| Lignes | Mécanisme | Ce qui est réellement vérifié |
|---|---|---|
| 1–24 | Trois couples schéma/exemple et liste de mots-clés pris en charge. | Les contraintes listées sont un sous-ensemble ; la déclaration Draft 2020-12 dans les schémas n'en fait pas un moteur complet de ce draft. |
| 27–74 | `validate` : enum, type, chaînes, cardinalités, champs requis, propriétés supplémentaires, objets/éléments. | Parcours déclenché par les valeurs de l'exemple ; les propriétés d'un schéma non présentes dans l'exemple ne sont pas parcourues. Aucun précontrôle global du schéma. |
| 77–81 | Chargement JSON, erreurs de lecture et de syntaxe converties en `ValidationError`. | `UnicodeDecodeError` n'est pas captée ; la forme racine du schéma n'est pas contrôlée ici. |
| 84–134 | Liens sémantiques propres aux trois familles. | DOMAIN_FRAME : intersections textuelles ; RESEARCH_BRIEF : chaînes d'incertitude différentes et conséquences non vides ; production : IDs, sélection, cardinalité et carte de couverture. Leur portée de fond est déjà F-DF/F-RB/F-PC. |
| 137–151 | Quatre mutations négatives intégrées. | `expect_invalid` accepte **toute** `ValidationError`, sans vérifier la règle qui a provoqué le rejet ; les quatre mutants conservent des contrôles sémantiques même si les schémas sont vides. |
| 154–178 | CLI ciblée limitée au chemin résolu d'un exemple canonique, puis validation de ce couple. | Une copie externe octet pour octet identique est refusée avant lecture : accès projet déjà F-ACT-008. Le ciblé ne lance pas les quatre mutants. |
| 181–218 | Sans argument : trois exemples, puis quatre mutations si aucun échec, sortie PASS/FAILED. | Les exceptions non converties sortent de la boucle au lieu du diagnostic contrôlé. |

## Passage B — tests discriminants et garanties positives

Baseline sur copie vérifiée : `validate_contracts.py` sans argument retourne **code 0, `CONTRACT VALIDATION PASSED`**. Les trois exemples canoniques passent individuellement avec code 0. Une copie externe identique du DOMAIN_FRAME est refusée par « chemin non canonique », comportement de CLI déjà documenté sous F-ACT-008. Une valeur `depth=IMPOSSIBLE` sous le schéma intact est rejetée avec `$.depth: valeur non canonique`; un champ requis supprimé est rejeté avec son chemin ; un mot-clé `pattern` ajouté à une propriété effectivement parcourue est rejeté proprement comme non supporté ; un schéma absent donne une erreur de lecture contrôlée. Ces garde-fous réels doivent rester présents.

| Contre-épreuve isolée | Résultat observé | Conséquence |
|---|---|---|
| Remplacer **un seul** des trois schémas par `{}`, puis les **trois** par `{}`. | Dans les quatre variantes, le script retourne code 0, imprime que les trois exemples et quatre mutations négatives passent ; avec les trois schémas vides, `validate_all.py` retourne aussi **code 0, `FULL VALIDATION PASSED`**. | F-VCT-001 : les obligations de structure peuvent disparaître derrière les rejets sémantiques des mutants. Cela ne prouve pas que les trois contrôles sémantiques ont eux aussi disparu. |
| Ajouter à `research_brief.schema.json` une propriété optionnelle nouvelle portant `pattern`, mot-clé non supporté, sans l'utiliser dans l'exemple. | **Code 0, PASS** ; le même mot-clé sur une propriété de l'exemple est rejeté. | Une branche déclarée du schéma peut échapper à l'inventaire des mots-clés. Occurrence de F-VCT-001 : prévalidation globale du schéma, distincte de l'exécution d'un document. |
| Remplacer la racine de `domain_frame.schema.json` par `[]`. | Code 1 et traceback `AttributeError: 'list' object has no attribute 'get'`, sans bannière CONTRACT VALIDATION FAILED. | F-VCT-002 : schéma mal typé non diagnostiqué par l'interface. |
| Mettre un octet UTF-8 invalide dans l'exemple DOMAIN_FRAME. | Code 1 et `UnicodeDecodeError` avec traceback, sans bannière contrôlée. | Autre branche de F-VCT-002 ; distincte d'un JSON syntaxiquement mal formé, correctement capté par `load`. |
| Supprimer **seulement** l'enum de `research_brief.depth`, puis mettre `depth=IMPOSSIBLE` dans l'exemple. | `validate_contracts.py` et `validate_all.py` rendent **code 0 / PASS complet** ; le schéma intact rejette ce même exemple. | F-VCT-003 : l'oracle des quatre mutations ne protège pas cette enum, même quand le schéma n'est pas vide. |

Les sources B01 elles-mêmes contiennent leurs schémas complets et leurs valeurs canoniques. Les faux PASS ci-dessus sont **des contre-épreuves sur copies mutées**, pas une affirmation que la baseline saine accepte déjà `depth=IMPOSSIBLE` ou utilise `{}`.

## Passage C — lecteurs, limites et interfaces

**Intégrateur :** le chemin CLI d'un fichier projet est refusé sans valider son contenu, F-ACT-008. Le message ciblé dit « fichier canonique » et l'usage sans argument valide les exemples distribués ; un PASS n'atteste ni la preuve annoncée dans DOMAIN_FRAME, ni la source de RESEARCH_BRIEF, ni le rendu d'un état UI/UX. Le défaut `schema=[]` ou un octet UTF-8 invalide crée un traceback, alors qu'un schéma absent ou un JSON malformé produit un diagnostic gouverné.

**Mainteneur/CI :** `validate_all.py` lance ce validateur et contrôle seulement son code 0. Si les schémas deviennent `{}`, les quatre mutations échouent encore pour leurs raisons sémantiques et la suite complète reste verte ; pour la perte d'une seule enum, les quatre mutants ne fournissent pas de voisin négatif. Un mode d'oracle par diagnostic attendu ou une épreuve d'autorité du schéma serait une option à décider en phase 11, après vérification de l'owner.

**Designer/reviewer et propriétaires DIRECTION/SAVOIR/ACTION :** les règles `domain_frame` des lignes 85–90 redémontrent F-DF-001, l'incertitude aux lignes 92–99 F-RB-002, et la concaténation des exigences aux lignes 113–130 F-PC-002. Aucune nouvelle fiche n'est créée pour ces limites déjà prouvées ; leur changement éventuel dépend du contrat propriétaire, et le résultat de la CLI ne remplace pas l'inspection de la source, de l'artefact ou du contexte.

## Passage D — constats provisoires et non-fusions

### F-VCT-001 — schéma vide ou branche non visitée admis avec PASS

**Preuve :** lignes 31–74 et 191–205 ; chacun des trois `{}` séparément et les trois ensemble rendent PASS, y compris au niveau `validate_all.py`. Un mot-clé non supporté sur une propriété absente de l'exemple passe également. **Impact :** la promesse « schémas validés » dépasse les contraintes effectivement exercées ; les quatre mutations ne constituent pas une preuve de la structure. **Owner pressenti :** admission et parcours de schéma du validateur de contrats, en interface avec les schémas propriétaires. **Épreuve de résolution :** refuser un schéma vide et parcourir ses branches déclarées avant de traiter les documents, tout en conservant les exemples et les vrais cas négatifs. Risque provisoire prioritaire de faux PASS ; gravité finale en phase 10.

### F-VCT-002 — dépendances invalides : exceptions brutes

**Preuve :** racine `[]` → `AttributeError` dans `validate`, octet UTF-8 invalide → `UnicodeDecodeError` depuis `load`, code 1 et traceback sans bannière contrôlée dans les deux cas. **Owner pressenti :** frontière d'entrée du schéma/document, `load`, forme racine et CLI. **Épreuve de résolution :** schéma mal typé et données non UTF-8 doivent échouer avec code non nul, chemin utile, diagnostic stable sans traceback ; préserver le rejet existant du schéma absent, JSON malformé et champ requis absent. Deux causes, un même contrat observable de diagnostic ; des corrections internes distinctes peuvent être nécessaires. Gravité finale ouverte.

### F-VCT-003 — disparition de l'enum `depth` non détectée par la suite

**Preuve :** enlever `enum` à `research_brief.depth`, modifier l'exemple vers `IMPOSSIBLE` ; la suite des contrats et la suite supérieure passent, alors que l'exemple muté est refusé par le schéma intact. **Owner pressenti :** oracle négatif et autorité de l'enum côté schéma/validateur. **Épreuve de résolution :** conserver un exemple canonique valide, ajouter un voisin invalide pour `depth` et vérifier qu'une mutation ne supprimant que cet enum rend la suite rouge. **Distinct provisoirement** de F-VCT-001 : une prévalidation qui refuserait seulement `{}` laisserait cette perte ciblée invisible. Gravité finale ouverte.

F-ALL-001 concerne le motif non vérifié des échecs dans l'orchestrateur, alors que F-VCT-003 est une règle non exercée par la suite native de contrats ; F-VRC-006 et F-VRC-007 concernent le validateur RUN_CARD. F-DF-001/002, F-RB-001/002 et F-PC-001/002 portent les obligations de contenu des contrats, non l'admission des schémas comme dépendance du script. Les candidats de fusion restent à examiner en phase 10, sans patch maintenant.

**Registre :** 135 fiches provisoires avant ce bloc, **138** après F-VCT-001 à 003. Aucun verdict système, aucune correction ni validation de release à partir de ces seules épreuves. **Prochaine unité :** lecture complète **1–105/105 de `validate_reading_map.py`**, avec `READING_MAP.md`, les propriétaires, le lecteur de routes et la frontière entre table dérivée et route exécutable ; ensuite `read_route.py`, manifeste, build et workflow. Revérifier B01 et relire le protocole §12 et ce rapport avant de continuer.
