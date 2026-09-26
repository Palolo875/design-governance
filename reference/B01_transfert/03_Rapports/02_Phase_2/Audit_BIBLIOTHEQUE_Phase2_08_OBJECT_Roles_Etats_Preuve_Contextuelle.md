# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 8 : OBJECT

## Cadre, reprise et correction rétrospective

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 501–541** : rôle 501–503, neuf objets 505–517, contrat et états 519–534, variantes et intégration 536–538, séparateur 540. `BIBLIOTHEQUE/MICRO` commence à 542 ; il reste pour le bloc suivant.
- Protocole externe v2.0 §12 relu, passages A–D. Rapports BIBLIOTHEQUE blocs 1–7, plan maître, checkpoints DIRECTION/ACTION/SAVOIR relus. Interfaces de contrôle : SELECT 163–205, CONTRACTS 258–284, SCENE 425–497 ; DIRECTION/FIRST-OBJECT 314–335, ACTION/UI-UX-REALITY 93–110 et preuve 605–665, SAVOIR/CRAFT/CFT-04a 346–359, CHANGELOG 31–42. MICRO 542–550 lu uniquement comme frontière ; son audit détaillé suit.
- Baseline B01 stable : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Vérification du bloc précédent :** le rapport SCENE est précisé dans sa section « preuve différée ». DIRECTION 316 dit « l'objet arrive avant les bénéfices », mais SAVOIR 348 accepte parfois promesse ou geste d'abord, en particulier pour des contenus intimes. SCENE/EDITORIAL_FIELD 443–445 accepte une projection éditoriale dont la preuve détaillée suit. Ces formulations ne doivent pas être déclarées harmonisées par l'hypothèse d'un objet forcément affiché dans le hero. L'obligation de relation produit, de vérité du claim et d'action non fictive demeure ; la divergence de **priorité du premier contact** est réservée à la consolidation inter-propriétaires, en lien avec F-DIR-018/F-DIR-024. L'amendement ne change pas les sources normatives, ne tranche pas la divergence et ne crée pas un verdict de run.
- Diagnostic sectionnel documentaire, sans test d'interface ni d'utilisateur réel, patch du système ou verdict global.

## Passage A — niveaux, routes et accès

OBJECT donne une **forme locale** à preuve, sélection, comparaison, mémoire, contrôle ou action ; il possède rôle, slots, contextes et états et **ne compose pas un écran entier** (503). SCENE relie ce type d'unité à la promesse, au contenu et au geste à l'échelle d'une surface (427, 479, 489). Une fenêtre produit utilisée comme unité n'établit pas que la scène a été conçue ; inversement la scène ne valide ni sémantique ni état de l'objet. La table à 509–517 répertorie neuf identifiants canoniques ; un nom de domaine ou variante de maquettage ne devient pas une nouvelle route (536, SELECT 237).

La frontière de cycle de vie est claire : le tableau de 521–534 concerne **chaque objet durable**, pas chaque objet local isolé. Contrat local réduit d'abord, puis contrat complet, consumers, mainteneur, compatibilité et preuve avant adoption (CONTRACTS 258–280, 538, CHANGELOG 37–42). Un objet partagé peut servir plusieurs scènes, mais sa conformité en isolation ne dispense pas d'observer son intégration là où le risque le requiert (538).

`python3 scripts/read_route.py BIBLIOTHEQUE/OBJECT` refuse le titre exact alors que `validate_reading_map.py` passe. La résolution manuelle dans le fichier propriétaire reste possible. Ajouter ce cas aux échecs de locator déjà enregistrés sous **F-DIR-028/F-ACT-001** ; pas de nouvel ID pour chaque route de premier niveau refusée. Les neuf sous-identifiants sont des noms de catalogue, et leur absence du lecteur dédié ne démontre pas, à elle seule, neuf défauts différents.

## Passage B — responsabilités, contrat et portée de preuve

### Les neuf objets (505–517)

| Identifiant | Décision concrète possible | Risque et preuve à qualifier |
|---|---|---|
| `EDITORIAL_SELECTION` | Choisir entre catégories, cas, experts, parcours ou articles avec image, titre, explication et action | S'assurer que les options/liaisons correspondent aux catégories et destinations réelles ; une belle galerie ne prouve pas le choix juste |
| `COMPARISON_SPLIT` | Montrer une **comparaison ou coexistence réelle** de thèmes, fonctions, lumières ou données | Une rupture de couleur décorative ne vaut pas comparaison ; distinguer ce petit objet de la scène complète `SCENE/SPLIT_PROOF` (479) |
| `MEDIA_ARCHIVE` | Relier média principal, métadonnées et repère mémorable pour archive ou pièce culturelle | Identité, provenance, droits et confidentialité selon le contexte ; la mémorabilité perçue n'est pas une tâche de recherche réussie |
| `SYSTEM_DATA_MODULE` | Donner forme à lignes/réseaux/nœuds/coordonnées quand ils **encodent une relation du système** | Données fictives, périmées ou purement décoratives n'établissent ni mesure ni fonctionnement ; tester états et légende nécessaires |
| `PROOF_PRODUCT_STAGE` | Relier promesse et large fenêtre du produit concret | « Produit réel » (513) ne permet pas d'appeler réel un mockup, une simulation ou une capture non exécutée ; source, état, version, rôle illustratif et méthode ACTION restent nécessaires |
| `NAV_CONTEXT_CAPSULE` | Loger destinations, utilitaires et action dans un contexte de scène/châssis/image | Vérifier destination disponible, focus, nom accessible, contenu réduit et responsive quand ils portent la navigation |
| `BRAND_GRAMMAR_PLATE` | Faire du logo, contraste, palette, matière, typographie et application une **décision répétable** d'identité | Une planche de style sans application fonctionnelle et limites de transfert ne démontre pas la robustesse d'un système de marque |
| `CONVERSION_CONTEXT_FIELD` | Situer une promesse parmi des artefacts de travail pertinents pour la conversion | Des artefacts inventés ou une intimité exposée sans permission peuvent rendre la scène trompeuse ; distinguer crédibilité située et conversion mesurée |
| `CONTROL_VALUE_TILE` | Lier valeur principale, statut, contexte limité et actions courtes pour solde, quota, score ou capacité | Un chiffre net et une couleur de statut ne prouvent ni fraîcheur, ni exactitude, ni résultat de l'action ; vérifier données, état et récupération dans le scope |

La table nomme **ce que l'objet porte**, pas le résultat obtenu après test. La décision de mode reste à DIRECTION/START et la preuve exécutée à ACTION ; `SYSTEM_DATA_MODULE` n'est pas un permis de reclassifier tout usage en `SYSTÈME`. Un « objet de preuve » de DIRECTION peut prendre d'autres formes que ces neuf routes ; SELECT permet l'héritage ou une forme locale si aucune route ne change la prochaine décision (163–167, 217–237). Le rôle « objet de rythme » du bloc SELECT 187 reste un rôle `OBJECT/*`, non un dixième préfixe.

### Contrat de l'objet durable (519–536)

Les dix champs du tableau 525–534 couvrent **rôle**, **contextes où l'objet aide**, **slots requis/optionnels/interdits**, **variantes sémantiques** (`context`, `density`, `emphasis`), **états**, **contenu**, **risques**, **type de preuve**, **test**, et **limite de preuve**. La matrice d'états distingue explicitement applicable, non applicable justifié et requis (529) ; elle ne prétend pas qu'`error`, `focus`, permissions ou récupération existent pour tout objet. Un cas sans état applicable doit être justifié selon le contrat, et un état nécessaire mais non observé reste non vérifié selon ACTION ; ne pas remplir tous les états avec une capture nominale. Les variantes sémantiques expliquent ce que change le contenu ou l'emphase ; `green-hero-v3` n'est qu'un nom de maquettage, pas un contrat de variant (528, 536).

`PROOF-TYPE` dit **quelle prétention** est établie ; « Test » 533 peut être une observation, capture, **scénario ou résultat attendu**. Ce dernier est prospectif, et ne suffit jamais à constater une réussite déjà obtenue. Lorsque la méthode, le scope, l'owner, le locator et la date/version soutiennent un claim exécuté, leur fraîcheur doit être contrôlée selon ACTION, même si 533 dit « lorsque pertinents » ; un verdict global accepté requiert sa provenance minimale (ACTION 655). `PROOF-LIMIT` empêche qu'un screenshot perceptuel soit vendu comme accessibilité, performance, confidentialité ou tâche réussie (534, ACTION 619/659–665). Le statut et la clôture restent aux registres ACTION, jamais à un objet de catalogue.

La confidentialité, les permissions, la localisation, les contenus extrêmes et la récupération sont explicitement présents dans les champs 529–531. Ils doivent être activés et inspectés selon l'objet, le risque et le médium ; un objet de solde ou de données personnelles n'a pas la même preuve qu'une pièce média publique. Le test de scène de 538 est **supplémentaire** : un contrôle isolé de clavier ou de focus peut être vrai dans le composant et faux après insertion dans une image, un overlay ou un viewport compact. Pour le partagé/durable, `OWNER-SCOPE`, `CONSUMERS`, `MOBILE`, `A11Y`, `COMPATIBILITY`, `MIGRATION`, `ROLLBACK`, `ADOPTION-STATUS`, `NEXT-REVIEW` s'ajoutent selon le risque (538), sans rendre un local de campagne automatiquement PILOT ou ADOPTED. Le débat de proportion de DERIVE, F-BIB-002, demeure pertinent mais n'est pas aggravé par le seul tableau **explicitement durable** de cette section.

## Passage C — simulations de lecteurs

| Situation | Décision/preuve attendue | Erreur à déceler |
|---|---|---|
| Designer, composant de sélection éditoriale dans une scène déjà stable | Choisir `EDITORIAL_SELECTION` si cette sélection change une décision, vérifier destinations et contenu réel ; ne pas rouvrir toute la scène | Créer une route SCENE nouvelle ou compter les cartes comme preuve de choix |
| Direction visuelle, fenêtre de produit stylisée mais fonction non construite | Marquer honnêtement l'objet illustratif et les claims non prouvés ; construire/observer pour pouvoir conclure sur comportement | Faire de `PROOF_PRODUCT_STAGE` un résultat d'intégration réel par son seul nom |
| Équipe produit, valeur de quota avec permissions refusées et état indisponible | `CONTROL_VALUE_TILE` avec état, statut, issue de récupération et données réellement accessibles ; tester la décision dans la scène | Conclure sur valeur nominale seulement et masquer le refus d'accès |
| Reviewer, navigation capsule correcte isolément mais cachée par le hero mobile | Refaire test focus, destinations et actions dans la scène/viewport concernés | Généraliser un PASS d'objet isolé à tout le flow |
| Mainteneur, planche de marque réemployée dans trois écrans similaires | Garder la responsabilité, examiner consumers et usages contrastés ; promotion décidée en CHANGELOG seulement après gain réel | Appeler une planche jolie `ADOPTED` automatiquement |
| Designer, histoire intime dont la première scène pose une promesse sans image de personne | Mettre la distance juste et le compromis dans la trace ; vérifier relation produit/claims ; ne pas forcer `MEDIA_ARCHIVE` ou objet personnel au hero pour remplir un slogan | Ignorer SAVOIR/CFT-04a ou reporter toute relation produit à une page future |
| Intégrateur, comparateur réel rendu en rupture thématique | Séparer `COMPARISON_SPLIT` comme unité de la scène globale ; observer donnée, états et résultat si la tâche est revendiquée | Prendre une différence de couleur pour une comparaison faite |
| Agent, le lecteur refuse `BIBLIOTHEQUE/OBJECT` | Chercher le titre exact dans le fichier propriétaire, consigner F-DIR-028/F-ACT-001 | Déduire que les neuf objets sont absents ou inventer leurs contrats |

Ces huit cas sont des simulations d'interprétation et de portée ; ils ne prouvent ni efficacité du catalogue, ni comportement de personnes ou produit en production.

## Passage D — résistance, déduplication et statut

**Aucun nouvel ID autonome dans OBJECT.** La section garde une frontière d'échelle claire, sépare état et variante, rend l'applicabilité des états explicite, réserve le contrat détaillé aux objets durables et demande une seconde vérification d'intégration dans la scène. Les risques identifiés restent traités par les propriétaires existants ou par des tests ultérieurs.

| Résistance ciblée | Constat/reprise |
|---|---|
| « Preuve » dans le nom d'objet prise pour observation ou vérité de claim | F-DIR-024, F-ACT-005/021/029 ; ACTION garde méthode, artefact, scope, date/version et verdict |
| `Test` peut être un scénario attendu et le lecteur annonce PASS avant observation | F-DIR-003, F-ACT-005/030 ; séparer cible, exécution et résultat, aucun nouvel ID pour 533 seul |
| États applicables omis ou variantes cosmétique codées comme sémantiques | Contrat 528–530 explicite ; éprouver objet avec error/permission/localisation vs objet sans état interactif |
| Objet correct en isolation, scène défaillante | 538 et CONTRACTS 284 protègent déjà l'intégration ; confronter focus superposé, contenu long et viewport réel |
| `BIBLIOTHEQUE/OBJECT` refusé, carte de lecture validée | F-DIR-028/F-ACT-001, occurrence du même déficit d'accès |
| Local devenu durable par fréquence ou nom séduisant | F-BIB-002 pour la proportion de la dérivation ; CONTRACTS/EVOLUTION/CHANGELOG pour le statut de route, aucune promotion tacite |
| Premier contact geste/promesse versus objet systématiquement avant bénéfices | Rectification du bloc SCENE ; SAVOIR/CFT-04a 348–359, DIRECTION/FIRST-OBJECT 316 et SCENE 445 à trancher au niveau inter-propriétaires, dans le voisinage de F-DIR-018/F-DIR-024 ; ne pas forcer une vitrine de contenu intime |

F-BIB-001 (réemploi de paire B1b hors même décision) et F-BIB-003 (déclencheur mobile dans GRID) restent ouverts mais cette section n'en fournit pas de nouvelle prescription fautive. L'expression « neuf objets » décrit la liste, pas neuf obligations à charger pour chaque surface. La réussite de tâche, l'accessibilité et la robustesse demeurent `NOT-VERIFIED` tant qu'une preuve applicable n'a pas été exécutée dans son périmètre.

## Couverture et suite

| Passage | Profondeur | Couverture et limite |
|---|---|---|
| A — architecture | FULL | 501–541, frontière SCENE/OBJECT/MICRO, neuf routes, CLI refusé |
| B — sémantique | FULL | Neuf responsabilités ; dix champs durables ; variantes, états, preuve et intégration |
| C — usage | TARGETED | Huit cas simulés ; aucun usage terrain mesuré |
| D — résistance | TARGETED | Claim, temporalité, états, promotion et nuance précédente ; aucun nouvel ID |
| Machine | TARGETED | `read_route.py` refuse OBJECT ; carte validée ; schémas/fixtures d'objet non rejoués ici |
| Externe | N/A-JUSTIFIED | Aucune affirmation externe nécessaire à la lecture du contrat interne |

Le séparateur est à 540 et la ligne 541 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **542–584**, `MICRO` ; reprendre protocole §12 et le présent rapport, puis tester les micro-interfaces, leurs états, actions et preuves distinctes du contrat des objets durables.
