# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 6 : GRID

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 340–424** : six variantes de grille 344–390, contrat et recomposition 392–413, niveaux de preuve 415–421, séparateur 423. `BIBLIOTHEQUE/SCENE` commence à 425 et reste hors de cette unité.
- Protocole externe v2.0 §12 relu, passages A–D ; rapports BIBLIOTHEQUE blocs 1–5, plan maître et constats F-BIB-001/002 repris. Interfaces ciblées : SELECT 163–199, CONTRACTS 258–284, SUPPORT 288–336 ; SAVOIR/CFT-03 302–310, ACTION/VISUAL_PROOF 605–619 et GATE-A 624–653 ; F-DIR-038 sur la portée par médium. COMPAT 661–685 seulement consulté pour vérifier les combinaisons indicatives, sans lui donner un diagnostic propriétaire anticipé.
- Baseline B01 stable : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Diagnostic provisoire de texte et de lecture simulée : aucun résultat d'usage, de préférence ou de performance de surfaces réelles n'a été mesuré ; aucun patch et aucun verdict global.

## Passage A — architecture du niveau GRID

GRID est l'**infrastructure de lecture dans un support** : circulation, axes, rythme, foyer et relations offertes à la scène, jamais un overlay ajouté après les composants (342). SUPPORT règle le champ (290), SCENE la relation promesse/contenu/preuve/action (336, 425–429), SAVOIR/CRAFT juge si la composition est située (304–310) et ACTION exécute les preuves puis garde les statuts. Une grille peut reprendre un support existant : SELECT 163–167 autorise zéro à plusieurs niveaux selon la décision, LITE/ITER évitent de reconstruire une structure suffisante (193–194), STANDARD peut ouvrir une décision GRID (195). Un nom de grille ou une valeur de colonnes ne reclassifie pas le mode.

Le tableau COMPAT donne des couplages possibles pour les supports et certaines scènes, mais se qualifie d'**hypothèses**, non de prescriptions ou d'exclusions des autres combinaisons (663–674). Le bon test est le contexte produit et la preuve, non la présence de la paire dans une cellule. `python3 scripts/read_route.py BIBLIOTHEQUE/GRID` refuse le titre de premier niveau ; `validate_reading_map.py` passe. Cette occurrence prolonge **F-DIR-028/F-ACT-001** (titres annoncés versus locators réellement chargeables) sans créer un ID par route refusée. Le fichier propriétaire et le titre exact restent consultables directement.

## Passage B — sémantique des six variantes

| Variante et lignes | Décision déclenchante | Preuve discriminante et limite |
|---|---|---|
| `GRID/MODULAR` 344–350 | Pièces de poids proche, collection, cartes, tableau, archive ou système où des unités répétables aident à lire | Rythme **et priorité** perceptibles ; un ensemble de boîtes de même importance sans raison n'établit aucune hiérarchie. En supervision, plusieurs priorités liées peuvent néanmoins être légitimes (SAVOIR 310) : ne pas inventer une dominante unique |
| `GRID/COLUMN` 352–358 | Axes verticaux durables pour texte, média, navigation et plusieurs sections, y compris responsive | Éléments critiques retrouvent des axes identifiables ; compter douze colonnes ou aligner des images sans rendre la lecture plus claire ne suffit pas |
| `GRID/RADIAL` 360–366 | Foyer réel autour duquel convergent signal, choix, communauté, produit ou action | Foyer reconnaissable **sans rayons décoratifs visibles** et périphérie qui le renforce ; test perceptuel, sans présumer de la réussite de la tâche |
| `GRID/HIERARCHICAL` 368–374 | Priorités inégales et ruptures contrôlées pour récit, annonce, pièce forte ou relation promesse/artefact/preuve | Sujet, contexte puis détail retrouvables ; chaque rupture modifie la priorité. Ne pas forcer cette séquence sur un écran où plusieurs alertes doivent rester simultanément lisibles |
| `GRID/BASELINE` 376–382 | Rythme typographique, métadonnées et blancs lorsque lecture et précision éditoriale portent l'identité | Cadence partagée par titres, texte et microcopie **sans comprimer le contenu** ; vérifier contenu réel, long et traduit si pertinent |
| `GRID/AXIAL` 384–390 | Progression, déplacement ou tension réellement portée par un axe horizontal, vertical ou diagonal | Chemin vers artefact et action sans atteinte à la lecture et au focus. Énergie géométrique seule ou ordre visuel qui contredit le focus ne suffit pas |

Les six intitulés qualifient des relations, pas des styles exclusifs ou des quotas de nouveauté. Une grille modulaire peut avoir une hiérarchie, une grille à colonnes peut aussi suivre un rythme de baseline : ce sont des propriétés compatibles si la décision et les responsabilités restent lisibles. L'étiquette HIERARCHICAL ne permet pas de revendiquer une réussite utilisateur ; le test doit rester adapté au risque et à la tâche. La contre-indication peut être déduite du résultat qui échoue à la preuve spécifique et des contrats communs, mais la section ne fournit pas un « éviter lorsque » explicite pour chaque variante comme SUPPORT : vérifier en simulation si le contrat commun 266 et le risque local suffisent, sans inventer ici six interdictions stylistiques.

### Déclaration et proportion de la grille (392–411)

La liste énumère `GRID`, `UNIT`, `MARGIN + GUTTER`, `ANCHORS`, `RHYTHM`, puis `FOCUS` seulement si radialité, axialité ou hiérarchie le requièrent (394–401). Elle ajoute **sept familles MOBILE** : `MOBILE-PRIORITY`, `MOBILE-NEIGHBORHOOD`, `MOBILE-ACTION`, `MOBILE-STATE`, `MOBILE-CONTENT`, `MOBILE-PERFORMANCE`, `MOBILE-COVERAGE-LIMIT` (402–408), ainsi que fallback et condition de sortie si la relation ne survit pas au contexte (409). « 12 colonnes » et « baseline 8 » ne sont que des départs adaptables (411), cohérents avec SAVOIR/CFT-03 304–308.

La ligne 411 conditionne **trois** familles (`MOBILE-STATE`, `MOBILE-CONTENT`, `MOBILE-PERFORMANCE`) au risque et à la responsabilité directe de la grille ; sinon scène, objet ou SAVOIR/CONTEXT conservent le sujet avec scope et prochaine preuve. Elle ne borne pas aussi explicitement les quatre autres familles MOBILE au **médium** et au **scope du run**. Lire « une déclaration de grille précise » à la lettre peut donc exiger priorité, voisinage, action et limite mobile même pour une grille uniquement destinée au print, à une installation fixe ou à un correctif local dont la version mobile n'est pas dans le scope. Il serait aussi erroné de s'affranchir du mobile réellement couvert : un nouveau layout web mobile requiert recomposition et preuve dans son périmètre. Voir F-BIB-003 ci-dessous.

La recomposition 413 protège les relations plutôt que le nombre de colonnes : radialité en séquence, mosaïque en rail, mesure en étiquette, dominante hiérarchique maintenue sans tout rendre uniforme. Ces transformations sont des **hypothèses à observer** dans un premier objet avec contenu, état et device pertinents ; elles ne constituent pas une preuve de robustesse par simple description. Si le support réel n'a pas d'équivalent mobile, choisir une adaptation pertinente au médium et déclarer la limite de preuve selon ACTION, sans fabriquer une capture mobile.

### Types, méthodes et statuts (415–421)

La table sépare `PERCEPTUAL` (masses, foyer, axes, rythme visibles), `EXPERT` (cohérence interprétée avec la tâche) et `USER/TASK` (compréhension ou réalisation d'une tâche **avec résultat attendu**). Ce sont des **types de prétention**, distincts de `METHOD: EXPERT` ou `USER` et distincts de `PASS`, comme le disent 415 et BIBLIOTHEQUE/READ 144–157. Une grille peut être lisible sur capture sans que la personne trouve une alerte, achève une comparaison ou puisse suivre le focus. ACTION/VISUAL_PROOF 612–619 borne les captures au rendu dans un viewport et un état ; un utilisateur observé sur une tâche avec méthode, périmètre et limites est nécessaire lorsqu'une conclusion de tâche est revendiquée. Aucune ligne de cette table ne crée un verdict de route concurrent.

## Passage C — simulations de lecteurs

| Cas | Décision/prochaine preuve correcte | Erreur que le cas cherche |
|---|---|---|
| Designer `ITER`, ajustement de gouttière desktop sans structure mobile changée | Garder la grille héritée, comparer le delta et sa non-régression dans le scope ; mentionner preuve mobile antérieure seulement si elle couvre encore la relation | Recopier sept champs MOBILE comme si chaque détail avait changé, ou attribuer un PASS au mobile non revu |
| Designer, affiche imprimée à grille de colonnes | Déclarer médium print, axes et contraintes physiques, preuve d'épreuve print ; justifier l'absence de version mobile | Créer `MOBILE-ACTION` fictif pour satisfaire la liste |
| Intégrateur, écran natif compact avec foyer radial | Proposer une séquence qui conserve priorité, action et focus, inspecter le rendu et les interactions | Réduire mécaniquement la radialité desktop ou masquer l'action |
| Équipe de supervision, tableau de signaux égaux et plusieurs urgences | Garder plusieurs priorités liées avec MODULAR si elles servent la tâche, mesurer localisation/lecture des alertes | Rejeter comme « boîtes équivalentes » malgré l'équivalence produit démontrée, ou forcer une dominante arbitraire |
| Designer, annonce éditoriale à rupture de rythme | HIERARCHICAL si sujet, contexte et preuve sont parcourus, tester contenu long et recomposition pertinente | Appeler chaque asymétrie « hiérarchie » sans conséquence |
| Reviewer, texte dense et libellés traduits sur BASELINE | Comparer cadence et absence de compression avec contenu réel, localisation et état applicable | Conclure sur la grille à partir d'un lorem ipsum court |
| Testeur, axe diagonal qui guide visuellement mais fait sauter le focus | Contrôle perceptuel positif borné ; rendre ordre et focus cohérents, garder A/U non vérifiés ou retourner | Convertir le foyer graphique en PASS accessibilité |
| Agent, route `BIBLIOTHEQUE/GRID` refusée par CLI | Localiser le titre exact dans le propriétaire, signaler F-DIR-028/F-ACT-001 | Déduire que la grille n'existe pas ou inventer un contrat |

Ces huit parcours sont **simulés**, non des runs de design observés. Ils départagent portée, priorité et preuve ; l'effet réel et les coûts restent à mesurer plus tard.

## Passage D — résistance et constat provisoire

### F-BIB-003 — la déclaration GRID présume des champs MOBILE hors de leur périmètre

- **Localisation :** `BIBLIOTHEQUE/GRID` 392–411, surtout l'énumération 402–408 et la restriction partielle 411.
- **Constat :** la prescription « une déclaration de grille précise » énumère sept familles MOBILE ; seules STATE, CONTENT et PERFORMANCE sont explicitement conditionnées au risque à 411. PRIORITY, NEIGHBORHOOD, ACTION et COVERAGE-LIMIT restent littéralement sans branche « mobile absent du médium/scope ». Le même contrat est lu pour GRID quel que soit le mode. Les textes généraux d'ACTION 625/632–653 et SAVOIR/TECH demandent pourtant une preuve adaptée au médium réel ; SELECT 193–195 préserve le delta local.
- **Conséquence plausible :** traces mobiles inventées pour print/borne/installation, `N/A-JUSTIFIED` de confort appliqué à une responsabilité pourtant pertinente dans un autre médium, ou surcharge d'un delta local avec sept lignes non touchées. **Gravité provisoire : significatif à éprouver**, sans incident ni fréquence établis.
- **Atténuations :** un humain peut inférer que « MOBILE » ne s'applique qu'à un produit mobile ; 411 donne déjà trois activations conditionnelles ; 413 permet une recomposition intelligente. Le texte ne force pas formellement un faux PASS : l'ambiguïté concerne la **sortie de la déclaration** et sa transportabilité selon médium/mode.
- **Test discriminant :** trois grilles de même structure dans (a) print sans mobile, (b) web desktop + mobile livré et modifié, (c) correction locale desktop avec mobile hérité et preuve antérieure de fraîcheur vérifiée. Faire remplir 396–409 sans règle ajoutée ; noter ce qui est réellement applicable, ce qui hérite, ce qui reste non vérifié et si la version mobile est dans le scope. Comparer deux lecteurs indépendants et l'issue ACTION.
- **Réparation candidate pour la consolidation :** rattacher les familles MOBILE à la présence du médium mobile dans le scope ou à un risque responsive réel ; préciser l'héritage de preuve valide et la traduction vers d'autres médiums ; conserver priorité, voisinage, action et limite comme obligations lorsqu'elles changent effectivement la décision.
- **Déduplication :** F-DIR-038 constate une universalisation analogue dans une table de capacités de DIRECTION, avec propriétaire et formulation différents ; ce bloc établit une **prescription spécifique au contrat structurel GRID** et son activation partielle à 411. F-BIB-002 porte sur le conflit DERIVE local/CONTRACTS réduit, non sur les champs MOBILE d'une grille existante. F-ACT-006 concerne l'agrégation par schéma machine, non l'obligation textuelle de GRID. La consolidation pourra regrouper leurs corrections, sans compter un incident par champ.

Autres résistances sans ID nouveau : le refus CLI est F-DIR-028/F-ACT-001 ; une valeur « 12 colonnes » prise comme validation contredit 411/SAVOIR 304 ; un `PERCEPTUAL` pris pour tâche réussie contredit 415–421 et ACTION 619 ; l'éventuelle injustice du masque SUPPORT 334 pour un contenu porteur demeure hypothèse ouverte au bloc 5. Aucun verdict global ni exigence de deux grilles ou d'itérations stylistiques ne découle de ce texte.

## Couverture et suite

| Passage | Profondeur | Couverture et limite |
|---|---|---|
| A — architecture | FULL | 340–424, rôle de GRID, six routes et échec du locator outillé |
| B — contrat | FULL | Conditions et preuves de chaque grille, 14 lignes du contrat, conditions partielles, trois types de preuve |
| C — usage | TARGETED | Huit cas contrastés ; aucun test humain réel ni métrique de produit |
| D — résistance | TARGETED | F-BIB-003 provisoire, cas nonmobile/mobile/local ; constats connexes dédupliqués |
| Machine | TARGETED | `read_route.py` refuse GRID, `validate_reading_map.py` passe ; pas de projection complète de contrat de grille testée |
| Externe | N/A-JUSTIFIED | Aucun claim externe nécessaire pour qualifier ces règles internes |

La section finit au séparateur 423 et à la ligne vide 424. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **425–500**, `SCENE` ; relire protocole §12, ce rapport et SUPPORT/CONTRACTS, puis vérifier les scénarios promesse–preuve–action sans confondre scène, support et grille.
