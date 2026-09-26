# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 4 : CONTRACTS

## Cadre et continuité

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 256–287** ; `CONTRACTS` 256–284, séparateur 286 ; `SUPPORT` commence à 288.
- Protocole externe v2.0 §12 relu : passages A architecture, B contrat sémantique, C simulation de lecteurs, D résistance. Reprise du rapport BIBLIOTHEQUE bloc 3 et de F-BIB-001. Interfaces consultées seulement pour tester le contrat : entrée BIBLIOTHEQUE 54–63 ; DERIVE 215–237 ; EVOLUTION 733–770 ; ACTION/PRECONDITION 204–218, STATUS 164–202, RUN_CARD 310–325, GATE-A 624–655 ; CHANGELOG 31–42. L'audit propre d'EVOLUTION et CHANGELOG reste à venir.
- Baseline B01 inchangée : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Rapport sectionnel provisoire. Les essais de lecteur sont des simulations documentaires ; aucun résultat d'usage ou de qualité produit n'est attribué à ces scénarios. Aucun patch du système ni verdict global.

## Passage A — emplacement, accès, propriétaires

`BIBLIOTHEQUE/CONTRACTS` est une section de premier niveau (256), annoncée comme contrat transversal dès l'ouverture de BIBLIOTHEQUE (3). Un lecteur humain peut la retrouver dans le fichier propriétaire par son titre exact. `python3 scripts/read_route.py BIBLIOTHEQUE/CONTRACTS` échoue toutefois avec « locator inconnu » : le lecteur CLI ne connaît que les entrées de la table de `READING_MAP`, alors que cette carte indique aussi que les autres routes doivent être retrouvées par préfixe et titre exact. `validate_reading_map.py` passe. **Occurrence de F-DIR-028/F-ACT-001**, pas nouvel ID pour chaque titre refusé : le futur test de couverture doit inclure CONTRACTS, et la solution doit préciser si l'outil garantit tous les titres exacts ou seulement les locators principaux.

La section sépare trois axes : **portée du contrat** (local réduit, durable complet), **cycle de vie de la route** (`PILOT`, `ADOPTED` via CHANGELOG) et **état/issue/verdict du run** (ACTION). Le contrat structurel ne crée ni état de run, ni gate, ni verdict. `DECISION-CHANGE` relève d'une décision réellement confirmée, modifiée ou abandonnée **après observation** (258, 278 et ACTION 212–218). Le contrôle d'un composant en isolation est insuffisant si son intégration, ses états ou permissions font partie du risque (284).

## Passage B — sémantique des phrases et du tableau

### Local, candidat, PILOT et ADOPTED (258)

Le contrat **initial** d'une route locale annonce responsabilité, contre-indications, preuve attendue et décision initiale. L'entrée 54–61 précise pour la contribution locale décision touchée, responsabilité, preuve attendue et limite ; ces deux minima se complètent : conserver une limite et une contre-indication pertinente, sans en déduire que chaque route locale doit recevoir la totalité du contrat durable. « Commence » laisse la possibilité de compléter la trace quand l'artefact, le risque ou la candidature l'exige.

Un essai local ne devient pas `PILOT` par déclaration : CHANGELOG 37 définit `PILOT` comme route locale ou candidate **testée dans un périmètre déclaré**. La ligne 258 permet le suivi comme candidate et situe `DECISION-CHANGE` ou l'issue ACTION **après** observation. Une proposition non testée conserve son statut documentaire local ou exploratoire, avec preuve attendue ; le lecteur ne fabrique pas une conclusion pour satisfaire le tableau de minimum `PILOT` ligne 59. Cette clarification confirme l'analyse du bloc 1, sans nouveau constat.

Pour `ADOPTED`, contrat complet nécessaire **mais non suffisant** : usages réellement contrastés, gain observé ou mesuré, compatibilité, mainteneur, prochaine revue et décision persistée dans CHANGELOG. Répéter la même belle capture, obtenir un `PASS` technique ou avoir plusieurs usages proches ne prouve pas ces conditions. Un `ADOPTED` n'est pas le `ACCEPTED` du run ; l'inverse non plus.

### Champs du contrat durable (260–280)

| Lignes | Ce que le champ doit permettre de décider | Frontière à préserver |
|---|---|---|
| 264–267, responsabilité / usage juste / contre-indication / preuve attendue | Quelle décision structurelle la route simplifie, où elle aide, où elle nuit et par quel objet ou test l'examiner | Une preuve **attendue** avant le build n'est pas une preuve obtenue |
| 268–270, `PROOF-TYPE`, `PROOF-SCOPE`, `PROOF-LIMIT` | Nature de la prétention, contexte couvert et conclusion interdite | `PROOF-TYPE` ne remplace ni méthode ACTION ni observation ; le scope attendu peut être corrigé par le scope réellement observé |
| 271, contenu et états | Cas longs, localisation, empty/error/loading, indisponibilité, disabled, focus, permissions, récupération et succès partiel pertinents | Ne pas annoncer leur couverture par la seule existence d'un composant nominal |
| 272, mobile | Relation et priorité recomposées, conservées ou remplacées | Le médium ou device non applicable se justifie ; pas de capture web simulée pour un autre médium |
| 273–274, accessibilité, confidentialité et permissions | Risques concernés, méthode, périmètre, données et voies de récupération | Un résultat en isolation ne vaut pas automatiquement conformité ou permission dans la scène ; contrôles selon risque et médium |
| 275, compatibilité | Consumers, combinaisons, plateformes, fallback, migration, rollback | Contrat durable ou partagé, pas liste universelle imposée à tout ajustement local |
| 276–278, owner / revue / `DECISION-CHANGE` | Décideur du run, destinataire de la suite, mainteneur, observations et révision ; décision réellement modifiée, confirmée ou abandonnée | Ne pas écrire `DECISION-CHANGE` avant observation ; owner du run et mainteneur ne sont pas forcément la même personne |
| 279–280, contribution expressive / banalisation | Ce que la route permet de rendre présent, et comment elle pourrait uniformiser des surfaces | Un style ou une beauté déclarée ne fonde pas une route ni son adoption |

Ces 17 lignes sont des **questions de contrat pour la route durable**, pas 17 résultats à cocher pour chaque run. La preuve à l'issue du run garde artefact, version, méthode, scope et limites chez ACTION ; une mesure de gain pour l'adoption conserve baseline et contextes contrastés (EVOLUTION 735–759). Le tableau ne spécifie pas à lui seul un format machine pour chaque champ, et `RUN_CARD` ne devient pas un second contrat de route partagé.

### Sorties et test en contexte (282–284)

`PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` et `NOT-VERIFIED` décrivent ici **le résultat d'un contrôle applicable**, dans le registre ACTION concerné ; ce ne sont ni `PILOT`/`ADOPTED`, ni les verdicts globaux `ACCEPTED`/`RETURN` simplement homonymes. `N/A-JUSTIFIED` requiert une non-applicabilité réelle ; une preuve nécessaire mais indisponible reste `NOT-VERIFIED` (ACTION 202, 653). Une réserve doit rester bornée par scope, impact, owner et prochaine preuve ; elle n'efface pas un risque bloquant.

Le test d'accessibilité en isolation d'un objet est une donnée utile mais bornée : si le risque touche états, contenu, viewport, permissions, navigation ou interactions dans la scène, vérifier **cette intégration**. Une capture peut établir une hiérarchie perceptuelle ; elle n'établit à elle seule ni succès de tâche, ni performance, ni conformité globale. Cette limitation est écrite explicitement à 284 et complète la typologie du bloc 2.

## Passage C — simulations de lecteurs

| Situation | Choix correct sous contrainte | Lecture erronée recherchée |
|---|---|---|
| Designer, forme locale unique sans réemploi prévu | Décision, responsabilité, contre-indication utile, preuve attendue, limite, owner et prochain contrôle proportionnés ; enregistrement du run selon ACTION | Exiger le tableau complet d'adoption avant le premier objet |
| Designer, forme locale DERIVE sur contenu long et état erreur | Déclarer levier, premier objet et ces risques ; enrichir preuve/scope/états activés, sans promotion automatique | Remplir tous les éléments DERIVE comme preuves déjà exécutées ou ignorer les états activés |
| Mainteneur, nouvelle route candidate encore sans observation | Laisser candidature en préparation ; planifier essai dans un scope ; issue ACTION si bloque | Déclarer `PILOT` et `DECISION-CHANGE` pour une hypothèse |
| Mainteneur, PILOT testé sur une seule scène | Conserver test et limite, chercher usages contrastés, compatibilité, mainteneur et gain avant adoption | Appeler `ADOPTED` à cause d'un run `ACCEPTED` |
| Reviewer, contrôle accessibilité `NOT-VERIFIED` dans une scène critique | Demander vérification applicable, noter scope et owner, refuser N/A de confort | Transformer un composant isolément correct en `PASS` global |
| Équipe produit, route adoptée utile sur web, essai print | Déclarer le médium et ce qui est réellement applicable ; adapter preuve et contrat de support | Exiger métriques web non pertinentes ou simuler leur réussite |
| Agent, cherche `BIBLIOTHEQUE/CONTRACTS` via le lecteur CLI | Constater l'échec ; ouvrir le fichier propriétaire et son titre exact ; garder le défaut d'accès en F-DIR-028/F-ACT-001 | Inventer la teneur du contrat ou conclure que la section n'existe pas |
| Designer, route STRUCTURE partage un motif sur plusieurs écrans | Identifier consumers, permissions, compatibilité, migration/rollback et owner selon blast radius ; passer par décision SYSTÈME/CHANGELOG si promotion | Gérer l'adoption comme une décision locale de style |

Ces huit cas testent les branches, y compris un local vraiment simple, un dérivé à risques activés et un candidat observé ; ils ne donnent ni taux d'erreur de lecteurs, ni temps de production, ni verdict sur un produit réel.

## Passage D — résistance et déduplication

### F-BIB-002 — frontière insuffisamment explicite entre dérivation locale et contrat réduit

- **Localisation :** entrée BIBLIOTHEQUE 54–61 ; `SELECT/DERIVE` 217–235 ; `CONTRACTS` 258, 260–280 ; protection ultérieure `EVOLUTION` 768.
- **Fait textuel :** CONTRACTS dit qu'une route locale **commence** par quatre éléments et réserve le contrat complet à l'adoption. DERIVE dit qu'une **forme locale** « déclare » d'emblée quinze lignes de champs, dont certains semblent rétrospectifs (`CONTENT / STATES` « effectivement couverts », `PROOF-TYPE / PROOF-LIMIT`) et plusieurs portent sur la preuve ou l'intégration après premier objet. Seule A11Y/PERFORMANCE indique expressément « lorsque le risque les active ». Aucun passage ne précise si les autres champs de DERIVE sont un dossier à compléter par étapes, des questions conditionnelles ou un minimum bloquant avant tout essai local.
- **Effet possible :** un lecteur pressé applique la liste entière à une expérimentation locale, remplit les inconnues de fiction ou renonce au chemin réduit ; un autre ne garde que quatre champs et omet un état ou une limite indispensable au risque réel. **Gravité provisoire : significatif à éprouver** ; ni fréquence ni coût mesuré.
- **Atténuations réelles :** le verbe « commence » (258) autorise un enrichissement progressif ; l'entrée 58 et EVOLUTION 768 protègent le run local court ; les risques actifs justifient des éléments supplémentaires et les obligations ACTION restent applicables indépendamment de la route. Il est donc possible de lire le corpus sans violation logique. L'ambiguïté porte sur la **condition de passage**, pas sur l'interdiction de dériver.
- **Test discriminant :** confronter (a) un local unique à faible risque sans variante, (b) une dérivation locale avec état erreur et contenu long, (c) un candidat testé `PILOT`, (d) une route durable sur consumers contrastés. À chaque état : quels éléments sont requis *maintenant*, lesquels sont attendus après objet/observation, lesquels attendent promotion, quelle issue si la preuve manque ? Un lecteur peut-il le décider en suivant uniquement les textes affichés ?
- **Réparation candidate après consolidation :** rendre explicite la temporalité de la liste DERIVE et les conditions qui activent chaque famille de champs, en préservant l'obligation de risque sans recopier dix-sept champs sur chaque run local.
- **Déduplication :** F-ACT-006 concerne un paquet structuré d'ACTION rendu universel et agrégé ; ici, la collision est **interne aux deux niveaux de contrat BIBLIOTHEQUE pour une forme dérivée**. F-ACT-002 traite de transport vers `RUN_CARD`, question distincte. Les retours F-DIR-003/F-ACT-005 sur temporalité de preuve aident à tester, mais ne fixent pas la frontière local/durable.

F-BIB-001 reste ouvert pour l'exception de paire B1b de SELECT 173 ; CONTRACTS 282 répète la vraie séparation entre contrôle et statut, sans autoriser la paire d'une autre décision. L'accès CLI refusé pour CONTRACTS appartient à F-DIR-028/F-ACT-001. Les libellés exacts des contrôles, des états, des issues et des verdicts de run doivent rester disjoints (F-ACT-003/014) : l'homonyme `RETURN` n'implique pas fusion des registres.

## Couverture, limites et reprise

| Passage | Profondeur | Couverture et réserve |
|---|---|---|
| A — architecture | FULL | 256–287, place de CONTRACTS, accès CLI refusé, trois propriétaires séparés |
| B — sémantique | FULL | Phrase 258, dix-sept champs 264–280, contrôles 282, preuve en contexte 284 |
| C — usage | TARGETED | Huit simulations ; aucun lecteur réel ni coût mesuré |
| D — résistance | TARGETED | F-BIB-002 provisoire, test discriminant ; accès rattaché à F-DIR-028/F-ACT-001 |
| Machine | TARGETED | `read_route.py` refuse CONTRACTS ; `validate_reading_map.py` passe ; ni schéma de route partagé ni projection complète testés dans ce bloc |
| Externe | N/A-JUSTIFIED | Aucun fait externe nécessaire pour ces règles internes ; usages contrastés et gain produit restent à établir |

La ligne 286 ferme la section. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **288–339**, `SUPPORT` ; relire le protocole §12, ce rapport et les blocs antérieurs, confronter les supports à SELECT/CONTRACTS et à l'adaptation par médium. Aucun patch ni verdict global.
