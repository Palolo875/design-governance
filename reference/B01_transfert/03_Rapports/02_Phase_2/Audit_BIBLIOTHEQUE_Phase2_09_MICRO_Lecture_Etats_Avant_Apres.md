# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 9 : MICRO

## Cadre et contrôle du bloc précédent

- **Source propriétaire :** `audit_work/package/V1/official/BIBLIOTHEQUE.md`, lignes **542–584** : règle de lecture et contrat 542–550, sept routes 552–560, avant/après 562–579, promotion 581. `MODIFIER` commence à 585 ; son audit détaillé reste à faire.
- **Méthode :** protocole externe v2.0, §12, relu pour les passages A à D. Reprise du rapport OBJECT (501–541), des constats BIBLIOTHEQUE 001–003 et des checkpoints DIRECTION/ACTION/SAVOIR. Interfaces ciblées : BIBLIOTHEQUE/READ 70–80, préfixes 129–157, SELECT 161–205, DERIVE 215–237, CONTRACTS 256–284, OBJECT 519–538, COMPONENTS 618, GATE 697–713 et EVOLUTION 733–770 ; ACTION/GATE-A 623–665, GATE-B/B1b 702–720 et CLOSE 407–411. Ces renvois contrôlent le sens de MICRO ; ils n'ouvrent pas leur audit à nouveau.
- **Baseline B01 contrôlée :** SHA-256 système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE propriétaire `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Vérification OBJECT :** ses neuf types d'unités (509–517) et son contrat explicitement **durable** (521) ne sont ni des modèles d'écran ni une validation de tâche. MICRO est un sous-type d'objet dense (`LAYER/OBJECTS`, 618) qui porte lecture, état, conséquence et action ; un objet isolé correct ne prouve toujours pas l'intégration dans la scène (OBJECT 538). La nuance SCENE/SAVOIR sur le premier contact demeure en réserve inter-propriétaires ; les lignes MICRO n'y apportent pas de solution. Aucun changement du rapport OBJECT nécessaire.
- La présente sortie est un diagnostic documentaire et des simulations de lecture. Aucun produit, utilisateur, capture, tâche ou temps de décision réel n'est attesté ; pas de patch normatif ni de verdict global.

## Passage A — architecture, accès et limites de niveau

MICRO se lit après le filtrage de SELECT : charger une micro-route **si une tâche opérationnelle exige** un contrat d'état, de conséquence et d'action (184–196), puis sélectionner uniquement ce qui change la décision. La chaîne de READ 72–78 n'en fait pas une étape obligatoire ; une micro-interface peut même être le point de départ d'une surface dense. Elle ne transforme pas pour autant un composant en scène ni en template. Les sept noms de 554–560 relèvent du préfixe `MICRO/<NAME>` (137), sous `LAYER/OBJECTS` (618), avec responsabilité et vérification principales distinctes.

La lecture 546 va de **l'identité** à **l'état**, puis à **la mesure ou au choix**, **la conséquence** et **l'action**. C'est un contrat de lisibilité, non une obligation de placer cinq libellés dans cet ordre à l'écran. Quand la mesure est sans objet, un choix peut porter la décision ; quand l'action n'est pas immédiatement autorisée, la conséquence et la voie de récupération doivent rester honnêtes. Graphique, couleur, texture ou icône soutiennent cette lecture mais ne suffisent jamais à coder seuls l'état (548).

L'accès CLI échoue pour `python3 audit_work/package/scripts/read_route.py BIBLIOTHEQUE/MICRO` : le locator n'est pas dans sa liste, alors que le titre et les sept routes sont présents dans le propriétaire ; `python3 audit_work/package/scripts/validate_reading_map.py` passe. C'est une nouvelle **occurrence** de F-DIR-028/F-ACT-001, non sept routes absentes et non un nouvel ID de constat pour MICRO. La lecture directe du propriétaire reste possible.

## Passage B — contrat, responsabilités et preuve

### Sept routes, sept décisions situées

| Route | Décision ou action rendue possible | État, conséquence et épreuve discriminante |
|---|---|---|
| `MICRO/IDENTIFICATION_GATE` (554) | Entrer, s'identifier ou reprendre une première étape de service | Expliquer tâche, raison et suite ; tester attente, erreur et accès/récupération alternative dans le médium et le viewport. Une capture du formulaire nominal ne prouve pas l'authentification accessible ni une permission accordée. |
| `MICRO/SETTINGS_GROUP` (555) | Comprendre puis modifier un réglage ou ouvrir sa destination | Regrouper selon le modèle mental et distinguer valeur actuelle, valeur modifiée, sauvegarde effective et indisponibilité ; un intitulé clair seul ne prouve pas que le changement a persisté. |
| `MICRO/PROFILE_EVIDENCE` (556) | Se fier à une personne, un compte ou un agent et agir | Montrer sujet et base de crédibilité avant attributs décoratifs ; distinguer preuve de source, avis situé et vérification du compte. Une photo, un badge ou un prénom ne créent pas une identité attestée. |
| `MICRO/QUERY_HEALTH` (557) | Diagnostiquer une requête, ressource ou tâche et décider quoi faire | Nom, période, métrique, référence, source, fraîcheur, état, diagnostic et action répondent aux cinq questions explicites. Une valeur isolée, une couleur verte ou une donnée sans horodatage ne justifient pas « sain ». |
| `MICRO/ENTITY_STATUS_RAIL` (558) | Prioriser une flotte, un site ou des ressources à surveiller | Garder total de référence, actifs, fraîcheur, exception, capacité et action lisibles. Un compteur « 4 actifs » sans dénominateur, période ou exception peut masquer une panne. |
| `MICRO/ITINERARY_SEGMENTS` (559) | Comparer ou modifier un trajet, une livraison ou une séquence | Expliciter connexions, fuseaux, transfert, annulation, coût/délai et effet de la modification ; traiter données incomplètes. Une visualisation de segments ne démontre pas la faisabilité du transfert. |
| `MICRO/USAGE_LEDGER` (560) | Décider face à un budget, quota, crédit ou consommation | Associer valeur, unité, plafond, période, prévision et conséquence du dépassement ; distinguer mesure actuelle et projection. Un pourcentage seul ne dit ni quand le plafond sera atteint ni l'action possible. |

L'unité dense est sélectionnée pour une tâche, pas pour imposer une esthétique de dashboard. Les routes `QUERY_HEALTH` et `ENTITY_STATUS_RAIL` peuvent entrer dans `SCENE/INSTRUMENT` ou une scène opérationnelle (439, COMPAT 682–685) ; la vérification doit encore couvrir la lisibilité **dans** cette scène. `USAGE_LEDGER` et `OBJECT/CONTROL_VALUE_TILE` partagent des contenus possibles mais pas exactement la responsabilité : un objet local peut montrer valeur et statut, la micro-interface doit aider une décision de quota dans sa période, sa prévision et sa conséquence. Ne pas charger les deux par défaut.

### Le contrat minimum et sa frontière locale (550)

La phrase « une micro-interface déclare au minimum » associe rôle, contextes, slots, variantes, états applicables, contenu/localisation/confidentialité, risques, type et limite de preuve, test, scope, owner et prochaine preuve. Les champs sont nécessaires à un **contrat de micro-interface utilisable**, mais le texte ne dit pas nettement à quel moment chaque champ doit être rempli par un run **local**. L'entrée 54–61 et CONTRACTS 258 commencent ce run avec décision, responsabilité, preuve attendue et limite ; la route partagée ou durable ajoute consumers, compatibilité, maintenance et cycle de vie, ce que la seconde phrase de 550 confirme. OBJECT 521 borne au durable son propre tableau détaillé ; la différence de formulation dans MICRO est donc réelle.

Lecture proportionnée possible : conserver une trace courte initiale, puis enrichir états, confidentialité, test et récupération **quand le risque ou la tâche les active**, sans inventer des résultats avant construction. Cependant la première phrase de 550 ne marque pas « contrat cible à compléter » ni ce déclenchement par risque. Elle peut être lue comme dossier intégral exigé avant une micro-expérimentation locale. **Rattachement à F-BIB-002**, qui suit déjà le défaut de frontière entre contrat réduit et listes déclaratives locales dans DERIVE 217–235 ; cette occurrence élargit le test discriminant à MICRO. Ce rattachement ne nie pas les obligations réelles de sécurité, accessibilité, permission ou preuve d'une tâche activées par le risque.

Un `PROOF-TYPE` décrit le **claim** établi, tandis que `METHOD` décrit l'observation (BIBLIOTHEQUE 144–157, ACTION 644–665). `TEST` et `NEXT-PROOF` de 550 peuvent être planifiés ; ils ne sont pas un résultat positif. En particulier un état error, denied, unavailable ou une donnée périmée non observés restent hors preuve. Si un verdict `ACCEPTED` est envisagé, ACTION exige provenance d'artefact, version, méthode et date/heure observée (655) ; la liste de MICRO ne remplace ni cette provenance ni le statut de run.

### Avant/après : deux hypothèses et des conditions non interchangeables

Le gabarit 564–575 demande tâche, regroupement, priorité, référence, conséquence, état, test et limite. Le contrôle 577 accepte l'après **si** une ambiguïté diminue, les états critiques sont préservés et une décision devient plus directe **sans demander davantage d'attention**. Ces critères ne sont pas prouvés par le seul alignement de deux captures ou par l'étiquette « moderne ». Quand compréhension ou usage domine, une tâche utilisateur est requise dans le scope déclaré : un test expert peut préparer la décision mais ne peut annoncer la réussite d'usage (ACTION 659–665).

La ligne 579 rattache **conditionnellement** cet avant/après à `ACTION/GATE-B/B1b` lorsque son scope le requiert. B1b (ACTION 702–716) est déclenché pour une surface DIRECTION par risque V/craft ou variante manquante ; il exige une paire de captures réelles autour de l'édition réversible d'une seule décision principale. Un avant/après produit/usage de MICRO en STANDARD n'active pas B1b par son seul nom. Inversement, une paire B1b sur le hero n'atteste ni la réussite d'une tâche d'identification ni le gain de compréhension de QUERY_HEALTH. Si la paire couvre déjà **exactement la même décision** et reste fraîche, ACTION 714 gouverne sa réutilisation : ne pas étendre l'exception imprécise de SELECT 173 (F-BIB-001). S'il manque observation ou méthode adéquate, le résultat reste non vérifié selon ACTION ; le gabarit n'autorise aucun `PASS` implicite.

La promotion de 581 demande usages contrastés, contrat réutilisable, owner de maintenance, baseline et gain limité, compatibilité, prochaine revue et statut. Elle passe par EVOLUTION puis CHANGELOG ; une micro-route locale n'est pas canonisée par l'emploi du tableau, une belle comparaison ou une fréquence apparente. La procédure décrit des conditions de promotion, sans produire à elle seule les usages et gains requis.

## Passage C — simulations de lecteurs sous contrainte

| Situation | Décision et preuve raisonnables | Mauvaise lecture à détecter |
|---|---|---|
| Designer, formulaire d'identification sur mobile et refus de permission | Charger `IDENTIFICATION_GATE`, nommer voie alternative et suite, inspecter attente/erreur/refus et contrôle accessible dans ce viewport | Appeler « accessible » la seule capture du succès ou offrir une récupération fictive |
| Intégrateur, réglage sauvegardé uniquement en apparence | `SETTINGS_GROUP` : comparer valeur avant/après retour ou rechargement, vérifier indisponibilité et feedback dans le médium | Confondre changement visuel de toggle avec persistance de la décision |
| Reviewer, profil d'agent avec badge non vérifié | `PROFILE_EVIDENCE` : borner la source de crédibilité et tester ce que l'action promet réellement | Traiter l'ornement comme vérification d'identité |
| Équipe produit, job affiché « OK » sans période ni source | `QUERY_HEALTH` : récupérer métrique, référence, fraîcheur, erreur et prochaine action, ou laisser la santé non vérifiée | Déduire santé opérationnelle d'un point vert |
| Opérateur, 4 ressources actives sur une flotte mais dénominateur absent | `ENTITY_STATUS_RAIL` : afficher total, exceptions, capacité et période puis tester la priorisation | Conclure « tout va bien » depuis le seul nombre d'actifs |
| Designer, segment de livraison modifié avec transfert et fuseau incertains | `ITINERARY_SEGMENTS` : rendre coût, délai, connexion et information manquante explicites avant validation | Montrer une nouvelle route séduisante comme faisabilité prouvée |
| Produit, quota à 80 % avant fin de période | `USAGE_LEDGER` : associer unité, plafond, période, prévision, dépassement et action réaliste | Transformer une estimation en consommation observée |
| Agent, dérivation micro locale à risque bas | Garder un contrat initial court selon l'entrée/CONTRACTS ; préciser la prochaine preuve et les champs activés par le risque, tout en réservant la lecture litigieuse de 550 à F-BIB-002 | Remplir le dossier complet de données fictives ou omettre un état critique actif |
| Reviewer, avant/après d'une tâche de santé en STANDARD | Exiger observation adaptée de la tâche si compréhension dominante ; appliquer B1b seulement si son déclencheur DIRECTION est établi | Produire `PASS` depuis une paire jolie ou exiger B1b universellement |
| Mainteneur, micro composant réutilisé deux fois | Garder statut local jusqu'aux usages contrastés, gain avec baseline, owner et décision CHANGELOG | Déclarer `ADOPTED` par répétition nominale |

Ces dix situations sont des **simulations d'interprétation**, pas des tests utilisateurs, des données de production ou des preuves de gain.

## Passage D — résistance et déduplication

| Point de rupture essayé | Résultat et propriétaire de suite |
|---|---|
| Contrat « au minimum » de 550 appliqué dès le premier essai local malgré entrée 58/CONTRACTS 258 | **F-BIB-002, occurrence supplémentaire** : clarifier ultérieurement les champs initiaux, ceux conditionnés au risque, puis ceux exigés pour promotion. Aucun nouvel ID tant que la cause est la même. |
| Avant/après de 579 interprété comme B1b universel ou comme preuve de tâche | ACTION 702–720 possède le déclencheur B1b ; ACTION 659–665 possède la portée de preuve de tâche ; F-BIB-001 porte toujours le risque d'exception trop large en SELECT 173. |
| Nom de route `PROFILE_EVIDENCE` ou `QUERY_HEALTH` tenu pour vérité sur personne ou donnée | BIBLIOTHEQUE définit la structure de lecture ; ACTION conserve méthode, fraîcheur, trace et verdict. Claim sans source ou état non observé : pas de conclusion positive. |
| Couleur et icône seules codent une alerte, un niveau de quota ou une permission | Interdiction déjà explicite à 548 et 558 ; éprouver nom, valeur, statut textuel, focus, contraste et annonce utile selon risque/médium. |
| Micro correcte isolément mais action inaccessible dans la scène | OBJECT 538, CONTRACTS 284 et GATE 703 exigent une inspection contextualisée ; un test unitaire seul ne couvre pas intégration. |
| `BIBLIOTHEQUE/MICRO` refuse l'accès direct alors que la carte valide | Occurrence F-DIR-028/F-ACT-001 ; corriger l'index propriétaire/consommateur lors des phases d'architecture et de validation machine, sans déduire que le catalogue manque. |
| Réutilisation d'une micro-route confondue avec promotion durable | 550 seconde phrase, 581 et EVOLUTION 735–770 gardent usages, gain, maintenance et décision de cycle de vie. |

**Pas de nouveau F-BIB autonome.** La lecture de MICRO ajoute une occurrence argumentée à F-BIB-002, des exemples à F-DIR-028/F-ACT-001, et conserve F-BIB-001 comme risque de déport de la portée B1b. F-BIB-003, lié au déclencheur mobile de GRID, n'est ni réparé ni aggravé par le seul libellé « dans le viewport » de MICRO. Le texte donne de bons garde-fous concrets pour chaque tâche ; leur efficacité réelle reste à mesurer dans des runs contrôlés.

## Couverture, limite et reprise

| Passage | Profondeur | Fait établi et limite |
|---|---|---|
| A — architecture | FULL | 542–584, sept routes, frontière OBJECT/MICRO/MODIFIER, lecteur direct refusé |
| B — sémantique | FULL | Lecture à cinq composantes, contrat, sept responsabilités, preuve adaptée, B1b conditionnel, promotion |
| C — usage | TARGETED | Dix simulations ; aucune tâche utilisateur ni gain mesuré |
| D — résistance | TARGETED | Occurrence F-BIB-002 ; accès F-DIR-028/F-ACT-001 ; pas de nouvel ID |
| Machine | TARGETED | Échec du locator `MICRO`, carte dérivée validée ; aucun schéma de run ou fixture d'interface rejoué ici |
| Externe | N/A-JUSTIFIED | Aucun standard externe invoqué pour trancher le contrat interne dans ce bloc |

Le séparateur est à 583 et la ligne 584 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **585–610**, `MODIFIER` ; relire le présent rapport et le protocole §12, puis vérifier les comportements transversaux, leurs tests et leur frontière avec style, scène et objet.
