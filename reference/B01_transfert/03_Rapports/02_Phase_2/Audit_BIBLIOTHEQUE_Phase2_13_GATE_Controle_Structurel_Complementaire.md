# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 13 : GATE

## Cadre, continuité et baseline

- **Source propriétaire :** `audit_work/package/V1/official/BIBLIOTHEQUE.md`, lignes **697–732** ; titre 697, frontière avec ACTION 699–703, dix tests et trace 705–717, statut et preuve 719–729, séparateur 731. `EVOLUTION` commence à 733.
- **Méthode :** protocole externe v2.0 §12, quatre passages A–D relus. Le rapport COMPAT bloc 12 et le plan maître ont été revérifiés : ses dix hypothèses restent des combinaisons à éprouver, pas des preuves acquises. F-BIB-004, absence du contrat détaillé de composant partagé, n'est pas résolu par GATE ; F-BIB-001/002/003 restent ouverts. Aucune réécriture rétrospective de COMPAT.
- **Baseline B01 stable :** compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Interfaces relues :** BIBLIOTHEQUE/SELECT 161–205, CONTRACTS 256–284, SUPPORT 332–336, SCENE 425–449, COMPAT 661–693, sortie 776–790 ; DIRECTION/FIRST-OBJECT 314–335 et route d'asset 421–437 ; SAVOIR/CRAFT CFT-04a 346–359 et STYLE 620–632 ; ACTION/DECISION-CHANGE 212–236, GATE-A/provenance 623–665, GATE-B 690–720 et GATE-C 775–794.
- **Lecture machine :** `read_route.py BIBLIOTHEQUE/GATE` refuse le locator bien que le titre existe à 697 ; `validate_reading_map.py` passe. Nouvelle occurrence de F-DIR-028/F-ACT-001, non nouveau constat BIBLIOTHEQUE. Lecture réalisée dans la source propriétaire. Cette vérification ne vaut pas test complet des scripts.
- **Nature :** examen documentaire et simulations, sans rendu de produit, test utilisateur ou verdict ACTION exécuté. Aucun patch normatif à cette phase.

## Passage A — architecture, place du contrôle et handoff

Le nom `GATE` et le tableau de tests peuvent faire penser à une quatrième barrière de livraison. Les lignes 699, 701 et 719 lèvent expressément cette lecture : **contrôle de module structurel complémentaire**, sans statut ni verdict autonomes ; les trois gates du run et la clôture restent dans ACTION. Son entrée est une sélection structurelle dans un scope déclaré avec premier objet inspectable, contenu et états pertinents ; sa sortie est une observation de la relation structurelle, de sa limite et, après observation seulement, une trace de décision transmise à ACTION.

L'architecture du bloc suit une progression cohérente : frontière d'autorité, terrain de contrôle, dix questions de qualité plus une question de conséquence, frontière réaffirmée, statut/action probatoire, puis route d'asset. Le contrôle traverse SUPPORT, GRID, SCENE, OBJECT, MICRO et les conditions de médium ; il n'oblige pas à instancier tous ces niveaux pour chaque delta. SELECT 163 et 191–199 permet zéro route en LITE, la seule route touchée en ITER et une sélection située en STANDARD/DIRECTION. La ligne 703 fait revenir les micro-interfaces d'identification, santé, permission et récupération à la classification DIRECTION/START et à la preuve ACTION : une description structurelle ne valide pas une conséquence critique.

Le lecteur CLI refusant ce heading exact tandis que COMPONENTS et EVOLUTION sont disponibles dans sa liste, la navigation machine est partielle. Le passage par la source exacte préserve l'audit ; la route dérivée sera éprouvée dans la phase 2 dédiée aux outils et à l'architecture de l'information.

## Passage B — contrat des dix questions et de la trace

| Ligne | Question et décision structurale à observer | Preuve recevable et limite à garder |
|---|---|---|
| 707 — non-généricité | Ablation de l'image, des données et du nom ; détecter une structure simplement interchangeable et envisager support/grille/scène/preuve plutôt qu'un polish final | Diagnostic perceptuel/expert contextualisé ; l'ablation retire aussi parfois le médium qui porte légitimement la relation au produit. **F-BIB-005** ci-dessous. |
| 708 — silhouette | Flouter pour éprouver foyer, masses, support et axes | Capture ou comparaison du rendu réel ; le flou ne prouve ni la lisibilité des libellés ni une tâche réussie. |
| 709 — grille | Identifier les relations entre éléments critiques et l'effet des ruptures sur la priorité | Observation perceptuelle/expert dans le viewport et avec données représentatives ; aucun nombre de colonnes n'est une qualité en soi. |
| 710 — preuve | Examiner contenu, état et action crédibles de l'objet ou de la MICRO au regard de la promesse | Revue experte du claim et, si la réussite d'une tâche est revendiquée, observation utilisateur/tâche adéquate. Un mockup plausible n'établit pas une capacité réelle. |
| 711 — asset | Contrôler route de production, crop, occupation, contraste, provenance, droits et relation à support/scène/preuve | DIRECTION choisit la route, ACTION vérifie selon le risque. Une provenance renseignée ne démontre ni droit effectivement acquis ni impact utile au rendu. |
| 712 — clarté | Relier tâche, référence, conséquence et action | Expert pour un défaut plausible, USER/TASK pour une conclusion d'utilisabilité réelle ; méthode et population déclarées. |
| 713 — états | Loading, empty, error, unavailable, disabled, succès, contenu long, données sensibles : le rôle résiste-t-il ? | Inspection technique et tâche selon risque ; périmètre des états réellement observés explicite, sans PASS global par seul état nominal. |
| 714 — mobile | Recomposer priorité, voisinage, action, état, contenu et performance | Rendu/inspection technique et tâche pertinente sur mobile **lorsqu'il est dans le scope**. F-BIB-003 demeure pour la prescription non bornée du contrat GRID ; GATE ne tranche pas un médium non mobile. |
| 715 — accessibilité | Focus, clavier, contrastes, noms, alternatives, information non chromatique | Contrôles techniques et parcours dans la scène réelle ; une question dans un tableau n'est pas un audit d'accessibilité exécuté ni une preuve exhaustive. |
| 716 — contexte | Vérifier public, JTBD et risque dominant | Jugement expert sur contexte réel, tâche utilisateur si la conclusion l'exige ; une silhouette originale ne suffit pas. |
| 717 — `DECISION-CHANGE` | Après observation, décision changée, confirmée ou abandonnée, ou simple documentation ? | Sortie de trace **ACTION**, avec méthode et scope distincts. Elle ne donne pas un résultat positif au simple fait d'avoir rempli les routes. |

La colonne « type possible » des dix tests ne définit aucune méthode automatique et ne transforme pas `EXPERT` type en `METHOD: EXPERT` (SELECT 155–157). ACTION 659–665 sépare mesure technique, capture, jugement expert et observation d'une tâche. ACTION 653 limite `PASS` au médium et périmètre effectivement examinés ; 655 exige provenance minimale pour une livraison acceptée. La description dans `RUN_CARD` peut documenter une relation simple et non critique (725), mais une relation visuelle critique demande un rendu, une capture annotée ou une comparaison adaptée ; si ce rendu nécessaire est absent, le contrôle reste `NOT-VERIFIED` selon ACTION, et Gate C exige explicitement une capture réelle (779).

Les cinq libellés 723 sont **statuts de contrôle ACTION dans le registre approprié**, pas statuts de route, états ou verdicts globaux. `N/A-JUSTIFIED` sert une non-applicabilité réelle dans le scope ; `NOT-VERIFIED` garde une preuve nécessaire manquante ; `RETURN` demande reprise. Une confirmation observée peut être `DECISION-CHANGE` (ACTION 212–215) : la ligne 727 ne commande donc pas une modification artificielle après un one-shot réussi. Une chaîne documentaire complète, même avec `DECISION-CHANGE`, ne prouve pas par elle-même le rendu, la tâche ou les états : 725, 727 et ACTION 665 imposent l'adéquation de l'observation.

La ligne 729 fait recevoir à la structure une route d'asset décidée par DIRECTION et vérifiée par ACTION lorsqu'elle modifie support, scène, objet ou mobile ; la formulation n'énumère pas GRID. Un asset dont le crop modifie un axe ou un rythme de grille doit néanmoins être examiné via GRID 340–342, question 709 et SELECT 180, et en pratique via sa scène/son objet. **Point de vigilance de couverture**, sans nouvel ID à ce stade : tester dans une vraie intégration si cette omission formelle fait effectivement perdre la relation de grille avant d'attribuer une deuxième défaillance. Aucun sourcing, classement d'outils, galerie ou archivage de goût n'est transféré à BIBLIOTHEQUE.

## Passage C — simulations d'usage sous contrainte

| Lecteur et cas | Action attendue | Faux positif ou faux retour à éviter |
|---|---|---|
| Designer, scène éditoriale portée par une photographie autorisée, structure sobre | Vérifier lien réel de l'image à la promesse, crop, fallback, tâche et scène entière ; utiliser le retrait pour montrer la dépendance | Forcer une nouvelle grille simplement parce que, photographie retirée, le squelette pourrait servir à de nombreux produits (F-BIB-005). |
| Reviewer, hero avec logo interchangeable et stock photo sans fonction | Retirer nom/image, détecter structure générique ; vérifier les questions 710, 716 et Gate C C1/C3/C6 avant `RETURN` approprié | Déclarer une signature produit parce que la photo est séduisante. |
| Agent, premier rendu ayant déjà confirmé la décision initiale | Tracer confirmation observée, artefact/version/méthode/instant, scope et limites chez ACTION | Produire une seconde itération factice pour « obtenir un changement » (727). |
| Intégrateur, capture desktop nette mais mobile et loading non ouverts | Limiter le constat à la capture et noter les états/médiums à vérifier selon scope/risque | Faire passer les dix questions comme preuve de tous les états et de l'accessibilité. |
| Équipe produit, identification avec permission refusée | Reclasser à START, observer tâche, erreur, permission et récupération dans ACTION | Conclure au PASS depuis l'anatomie d'une MICRO isolée. |
| Reviewer, mot « GATE » sur un correctif de texte LITE | Contrôler seulement la relation effectivement touchée, consigner la non-applicabilité du craft si elle est réelle | Exiger une revue structurelle complète et un quatrième verdict. |
| Mainteneur, asset dont l'occupation change l'axe GRID sur une page campagne | Vérifier axes, scène et crop réellement rendus, trace DIRECTION/ACTION ; conserver une réserve sur l'ellipse « grille » de 729 | Laisser le changement hors revue structurelle parce que seul le nom GRID manque dans 729. |
| Système automatique, registre `RUN_CARD` rempli et aucune capture d'une relation visuelle critique | Conserver `NOT-VERIFIED` et prochaine preuve ; empêcher clôture non soutenue | Déduire `PASS` ou `ACCEPTED` du nombre de champs et d'une description. |

Ces parcours sont des **contre-exemples documentaires**. Ils ne prétendent pas avoir observé un produit, un droit d'asset, un utilisateur ou une performance.

## Passage D — résistance et constat

### F-BIB-005 — ablation de contenu appliquée comme obligation de différenciation de la structure

- **Statut :** provisoire ; risque de sur-contrainte du jugement structurel, importance à calibrer avec les scénarios des phases 6 et 9.
- **Fait exact :** BIBLIOTHEQUE/GATE 707 demande si la structure, **sans image, données et nom**, pourrait appartenir à cinquante produits et ordonne, si oui, de changer support/grille/scène/preuve plutôt que d'ajouter du polish. Ce « si oui, changer » est plus fort qu'une simple question ou qu'une invitation à inspecter une dépendance.
- **Cas discriminant A :** une scène `EDITORIAL_FIELD` (443–445) a une mise en page volontairement sobre ; l'illustration spécifique, autorisée et cadrée explique une relation au produit, conserve un fallback adapté, et la surface entière montre la promesse et l'action pertinentes. Après retrait de l'illustration, des données et du nom, le squelette paraît interchangeable, mais une autre structure pourrait affaiblir le sens et la clarté sans améliorer la tâche. La consigne littérale de 707 impose quand même de le changer.
- **Cas discriminant B :** même squelette, image de stock sans relation et CTA vague ; le retrait révèle une absence réelle de spécificité. Ici 707 aide à demander une correction située, à vérifier par scène, tâche et Gate C. Ces deux cas ont le **même résultat d'ablation** et une qualité opposée dans le rendu complet : l'ablation seule ne départage pas les décisions.
- **Effet possible :** refonte inutile, nouveauté structurelle ajoutée pour satisfaire le test, coût/complexité, ou rejet d'une scène fondée légitimement sur média ou contenu. La question de contexte 716 et l'adéquation de preuve 710 atténuent ce risque, mais n'annulent pas l'impératif sans exception de 707. SUPPORT 334 présente le masquage comme test perceptuel/expert de composition, sans instruction équivalente de refonte automatique ; SAVOIR/STYLE 632 a une erreur voisine.
- **Propriétaire et déduplication :** F-SAV-006 porte sur la **validité d'un profil de style** quand image/couleur/logo sont masqués ; **F-BIB-005** porte sur une **obligation de modifier la relation structurelle** après ablation, même si celle-ci est adaptée au produit entier. DIRECTION 328–335 et Gate C C1/C3/C6 demandent une signature et un lien situés, sans rendre la structure originale dans l'abstrait. Consolider les règles d'ablation lors du diagnostic inter-propriétaires, sans compter deux incidents empiriques par défaut.
- **Épreuve ultérieure et piste non normative :** comparer sur rendus réels (i) un système sobre avec média/data porteurs et fallback honnête, (ii) un système maquillé par média interchangeable, (iii) une proposition sans média dont la relation structurelle porte toute la preuve. Si le cas (i) est invalidé par 707 malgré preuve située, distinguer dans la correction le diagnostic de dépendance et la conclusion de refonte ; garder le cas (ii) bloqué. Aucune correction du texte n'est appliquée maintenant.

| Résistance complémentaire | Résultat |
|---|---|
| Titre GATE lu comme quatrième gate ou verdict autonome | 699/701/719/723 l'excluent ; laisser ACTION posséder registre, issue et livraison. |
| Description `RUN_CARD` prise comme preuve de rendu critique | 725/779 la refusent ; preuve observée adaptée ou `NOT-VERIFIED`. |
| `DECISION-CHANGE` interprété comme obligation de changer le design à chaque boucle | ACTION 212–215 autorise une confirmation **après observation** ; conserver la preuve réelle, refuser la seconde version rituelle. |
| `N/A-JUSTIFIED` utilisé pour éviter accessibilité, états, micro critique ou mobile dans le scope | 703/713–715 et ACTION 653 imposent applicabilité et preuve ; absence de preuve requise = `NOT-VERIFIED` ou issue adéquate. |
| Liste asset 729 omet « grille » | Couverture compensée par GRID 340–342, SELECT 180 et test 709 ; hypothèse de perte de route à tester en intégration, pas encore nouvel ID. |
| Locator exact GATE refusé par CLI | Occurrence de F-DIR-028/F-ACT-001 ; source lisible directement et carte dérivée validée. |
| Contrat de composant partagé supposé couvert par tests GATE | F-BIB-004 demeure ; vérifier anatomie/variants/tokens/source de vérité au propriétaire, puis preuve ACTION dans le run. |

## Couverture, réserves et prochaine unité

| Passage | Profondeur | Résultat |
|---|---|---|
| A — architecture | FULL | Frontière avec gates ACTION, contrôle complémentaire, route CLI et renvoi MICRO ; 697–703, 719, 731–732 |
| B — contrat sémantique | FULL | Dix questions 707–716, `DECISION-CHANGE` 717, statuts 723, preuve 725–727, route asset 729 |
| C — usage réel simulé | TARGETED | Huit lecteurs/cas ; aucune preuve de produit réellement exécutée |
| D — résistance | TARGETED | F-BIB-005 provisoire, cinq constats BIB désormais ; autres points dédupliqués ou réservés à un test d'intégration |
| Machine | TARGETED | CLI refusé, carte dérivée valide ; scripts et schémas à auditer dans leurs blocs |
| Externe | N/A-JUSTIFIED | Aucune actualité ni norme externe nouvelle nécessaire au constat textuel ; validité empirique et conformité réelles non conclues |

**Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **733–775**, `EVOLUTION` ; relire le protocole §12, ce rapport et les quatre constats antérieurs avant d'examiner promotion, dépréciation, maintenance et raccord CHANGELOG. Les lignes 776–791 et `CHANGELOG.md` restent ensuite à lire. La phase 2, puis les phases 3–14, ne sont pas terminées ; aucun patch n'est autorisé au stade actuel.
