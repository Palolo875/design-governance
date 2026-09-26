# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 10 : MODIFIER

## Cadre et reprise vérifiée

- **Source propriétaire :** `audit_work/package/V1/official/BIBLIOTHEQUE.md`, lignes **585–610**. Le rôle est défini à 585–587 ; `FIELD_SWITCH` 589–593, `NAVIGATION_SHELL` 595–599 et `PRINT_FIELD` 601–607 ; séparateur 609. `COMPONENTS` commence à 611 et fera l'objet de la lecture suivante.
- **Méthode :** protocole externe v2.0 §12 relu, passages A architecture, B contrat, C simulations d'usage, D résistance. Interfaces vérifiées : BIBLIOTHEQUE/READ 70–80, SELECT 161–205, DERIVE 207–237, CONTRACTS 256–284, OBJECT 501–538, MICRO 542–584, COMPONENTS 613–629, COMPAT 661–687 et GATE 697–719 ; SAVOIR/STYLE 575–632, CONTEXT 708–740, TECH 744–776 ; ACTION/GATE-A 623–685, B1/B1b 694–720 et GATE-C 775–794. Ces sections servent à tester la frontière de MODIFIER et ne sont pas rouvertes entièrement ici.
- **Baseline B01 stable :** SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, source BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Contrôle du précédent :** MICRO est une unité dense et non un modificateur. La sélection, l'état et la conséquence des sept micro-routes restent à tester dans leur tâche (MICRO 542–560). Leur avant/après ne déclenche B1b que dans son scope (579, ACTION 702–716). La liste « au minimum » de MICRO 550 garde son occurrence sous F-BIB-002 ; MODIFIER n'apporte pas de règle qui tranche la temporalité de cette liste. Aucun amendement rétrospectif du rapport MICRO nécessaire.
- Diagnostic textuel avec scénarios **simulés** ; aucun run produit, test avec personne, benchmark, mesure de performance ou verdict de conformité n'a été réalisé. Les sources normatives ne sont pas modifiées.

## Passage A — architecture, activation et route de lecture

La route `MODIFIER/*` ajoute un **comportement transversal après la structure** lorsque lisibilité, navigation ou matérialité change réellement (587). Elle ne remplace ni le support, ni la grille, ni une scène de preuve, ni l'objet ou la micro-interface où s'effectue la tâche ; elle n'est pas un `STYLE/*` qui réglerait une expression générale. READ 78, SELECT 163–185 et le préfixe 138 répètent cette frontière. « Après » désigne la dépendance de décision : une proposition de matière ou de navigation peut être anticipée, mais son contrat ne se juge qu'avec une structure et une conséquence observables. Aucun modificateur n'est requis si la structure actuelle ou une primitive répond déjà au besoin.

Le catalogue comporte **trois** routes explicites. Leur nom n'est ni un composant prêt à déployer ni un niveau de `LAYER` supplémentaire ; `MODIFIER/FIELD_SWITCH` peut s'appliquer à une unité interactive, `MODIFIER/NAVIGATION_SHELL` à une navigation intégrée à une scène et `MODIFIER/PRINT_FIELD` à une matérialité dessinée ou produite par code. L'appellation historique « PRINT » n'interdit ni CSS ni SVG : DERIVE 213 et MODIFIER 605 disent explicitement que le médium n'est pas réduit à l'impression.

`python3 audit_work/package/scripts/read_route.py BIBLIOTHEQUE/MODIFIER` refuse le locator, tandis que le titre exact et les trois routes existent dans le propriétaire et que `validate_reading_map.py` passe. C'est la même famille d'accès F-DIR-028/F-ACT-001 rencontrée dans OBJECT et MICRO. La source est consultable directement ; l'échec du raccourci ne démontre ni absence des routes ni défaut autonome pour chacune d'elles.

## Passage B — responsabilités, preuves et frontières

| Route et lignes | Condition de choix et changement attendu | Test du propriétaire, limite de preuve |
|---|---|---|
| `FIELD_SWITCH` 589–593 | Une **sélection** recompose champ visuel, microcopie ou action et rend la conséquence utile. Si elle ne fait que changer une couleur active, la primitive de sélection peut suffire sans route ajoutée. | Vérifier nom, rôle, valeur, focus, actif/inactif, conséquence et changement utile à l'œil, au clavier et au lecteur d'écran dans le scope. Inspecter la transition réelle, la valeur exposée et l'action suivante ; une capture des deux états seule ne prouve ni utilisation clavier, ni annonce correcte, ni persistance. |
| `NAVIGATION_SHELL` 595–599 | La navigation agit comme couche de contrôle sur scène, cadre ou image ; elle conserve sorties et actions malgré les fonds et crops. Si la navigation est seulement une capsule locale, `OBJECT/NAV_CONTEXT_CAPSULE` 514 décrit l'objet ; sélectionner en plus un modificateur exige un **comportement de couche** qui change. | Tester focus et contraste ainsi que sorties et actions dans une **matrice finie déclarée** de fonds, crops, thèmes, viewports et états, avec fallback. Une photo favorable, un seul état ou des liens apparents ne couvrent pas les autres combinaisons ni l'activation réelle. |
| `PRINT_FIELD` 601–607 | Grain, trame, aplat, bordure ou hachure ont un rôle de matière perceptuelle **ou** de repère sémantique sur une structure déjà choisie. Si le seul but est un registre esthétique, SAVOIR/STYLE peut porter la décision sans nouvelle route. | Vérifier rôle, test de retrait, contraste, performance, alternative si la matière informe ; garder la sémantique indépendante de texture/couleur seules. Observer si la matière soutient identité ou preuve sans perte de lisibilité, accessibilité ou robustesse. Une technique disponible ou une capture séduisante ne prouvent ni performance ni gain transversal. |

**Frontière objet/modificateur.** `OBJECT/NAV_CONTEXT_CAPSULE` fournit l'anatomie locale des destinations, utilitaires et action (514) ; `NAVIGATION_SHELL` vérifie leur comportement quand l'ensemble se déploie **sur** une scène ou une image avec fonds, crops et états changeants (597–599). Les deux peuvent coexister si leurs décisions sont distinctes ; choisir deux routes pour nommer deux fois la même navigation est refusé par SELECT 165–167. `FIELD_SWITCH` peut modifier une micro-interface dense, mais ne remplace pas le contrat de lecture, d'état et de tâche de MICRO. `PRINT_FIELD` peut modifier un objet ou une scène sans devenir à lui seul scène, preuve produit ou identité globale.

**Frontière style/matière.** SAVOIR/STYLE 576–630 règle la manière d'exprimer une décision et peut accueillir de la matière. `PRINT_FIELD` 605 requiert une fonction **située** de cette matière et un test de retrait ; ce test examine sa contribution, il n'impose pas qu'une matière expressive disparaisse dès qu'elle n'encode pas une donnée. Le texte accepte explicitement un rôle **perceptuel**. Si la texture porte une information, un texte, symbole, structure ou autre alternative la maintient compréhensible quand texture/couleur échouent. Si elle porte une identité, vérifier la relation au produit, à la composition et au risque, sans exiger un faux statut opérationnel pour la conserver. Cette lecture évite d'amplifier F-SAV-006 (masquage abusif de l'image/couleur dans un test de style) ; aucun conflit nouveau démontré dans 605.

**Portée des tests.** `FIELD_SWITCH` énumère clavier, lecteur d'écran et œil pour son comportement interactif déclaré. Hors Web ou sans lecteur d'écran natif identique, ACTION 629–653 et SAVOIR/TECH 764–776 demandent de déclarer médium et idiomes pertinents, puis de tester l'équivalent réellement disponible et de réserver ce qui manque. Le texte de MODIFIER n'autorise pas un `PASS` d'accessibilité globale sur la seule présence de focus. `NAVIGATION_SHELL` demande une matrice **finie**, non toutes les combinaisons imaginables ; l'équipe doit déclarer celles pertinentes, tester le fallback, préciser les cas non couverts et ne pas appeler robuste une seule capture. Pour `PRINT_FIELD`, la comparaison avant/après retrait sert d'observation perceptuelle située ; mesure technique si la performance est revendiquée ; tâche utilisateur si un gain d'usage est revendiqué. ACTION conserve méthode, scope, provenance, statuts et verdict, GATE-C le jugement craft sur rendu réel (775–794) et B1b une paire réversible uniquement quand son propre déclencheur DIRECTION s'applique (702–716).

**Route locale et partage.** Une application locale commence avec responsabilité, contre-indication, preuve attendue et décision initiale selon CONTRACTS 258, puis active les contrôles de risque réels. La dernière phrase de 605 refuse qu'une recette de matière devienne réutilisable sans gain transversal : faire `PRINT_FIELD` une fois ne déclenche ni adoption, ni mode SYSTÈME. Pour un modificateur réemployé à plusieurs endroits avec blast radius, les obligations de consumers, compatibilité, maintenance, migration et preuve sont examinées chez CONTRACTS/EVOLUTION et ACTION/RUN-SYSTEM ; le statut de cycle de vie demeure chez CHANGELOG. Ce n'est pas une nouvelle occurrence fautive de F-BIB-002 : MODIFIER ne présente pas de liste de dossier « au minimum » à remplir pour toute tentative locale.

## Passage C — simulations de lecture sous contrainte

| Cas simulé | Décision/prochaine vérification | Mauvaise lecture recherchée |
|---|---|---|
| Designer, toggle de thème existant : seule la couleur du contrôle change | Garder la primitive si état et action fonctionnent ; documenter le delta sans charger `FIELD_SWITCH` sans changement de champ | Inventer une route pour un état natif |
| Intégrateur, choix qui change libellé, action et panneau actif | Choisir `FIELD_SWITCH`, vérifier valeur, état exposé, focus, contenu et conséquence au clavier et à la technologie d'assistance dans le scope | Tester deux captures statiques puis annoncer un comportement accessible |
| Équipe produit, sélection rendant impossible une action antérieure | Garder une voie compréhensible, annoncer indisponibilité et prochaine action ; observer la transition et la récupération | Cacher le contrôle par style et perdre l'état/action |
| Designer, navigation capsule sur image fixe | `OBJECT/NAV_CONTEXT_CAPSULE` peut suffire si aucune couche variable n'est introduite ; vérifier liens et focus adaptés | Charger `NAVIGATION_SHELL` en doublon par ressemblance de nom |
| Reviewer, navigation blanche sur fonds clairs, foncés et crops mobiles | Pour `NAVIGATION_SHELL`, définir matrice réellement visée, vérifier focus, sorties, contraste et fallback dans chaque classe critique | Généraliser le résultat d'une seule image favorable |
| Intégrateur, support tactile natif sans parcours au clavier dans le scope | Déclarer médium/idiome, substitut et limite selon ACTION/SAVOIR ; inspecter interaction et annonce pertinentes au support | Forcer une preuve Web fictive ou déclarer `PASS` sans observation |
| Direction visuelle, trame donnant caractère à une archive sans coder le statut | Tester `PRINT_FIELD` perceptuel avec/sans trame sur l'objet complet, contraste et coût ; accepter un rôle identitaire réel si maintenu | Supprimer systématiquement la matière faute de valeur chiffrée |
| Opérateur, hachure seule distingue danger et normal | Exiger texte/symbole/structure et alternative, vérifier contraste et lecture réelle ; état essentiel non démontré tant que la distinction dépend de texture | Déduire sécurité ou accessibilité du seul motif |
| Mainteneur, même `PRINT_FIELD` dans trois produits | Évaluer gain contrasté, consumers, performance, propriétaire et migration avant toute recette partagée | Déclarer `ADOPTED` par fréquence ou disponibilité CSS |

Ces neuf cas discriminent l'échelle de route, le médium et la portée de preuve ; ils ne rapportent aucun essai exécuté sur les produits fictifs.

## Passage D — résistance, constats et déduplication

| Test de résistance | Traitement |
|---|---|
| Une sélection de `FIELD_SWITCH` change le décor mais ni valeur, ni microcopie, ni action | Le critère 591/593 et SELECT 165–167 refusent le modificateur sans comportement réel. Si le changement visuel est une décision de style, SAVOIR peut la porter. |
| La navigation paraît correcte sur une image et échoue sur un crop ou un focus | 599 prescrit matrice déclarée et fallback ; OBJECT 538/CONTRACTS 284 demandent l'intégration ; ACTION 625–665 garde la preuve. Aucun `PASS` de navigation sur une capture unique. |
| Un lecteur confond capsule locale et couche transverse | Analyser les deux décisions 514 versus 597 ; composer les routes seulement si les deux responsabilités existent. La différence d'échelle est explicable sans nouvel ID. |
| Un lecteur écarte une matière expressive après le test de retrait parce qu'elle n'encode pas un statut | 605 autorise un rôle perceptuel. Test de retrait = jugement d'effet et de coût dans le contexte ; garder la nuance F-SAV-006 sans lui attribuer une prescription nouvelle de MODIFIER. |
| Matière informative reposant uniquement sur texture ou couleur | 605 l'interdit et demande une alternative ; suivre ACTION/GATE-A et les tests du médium. La règle textuelle existe ; efficacité à observer. |
| Recette de `PRINT_FIELD` réutilisée, gain et maintenance inconnus | 605 et EVOLUTION 735–770 bloquent l'adoption tacite ; F-BIB-002 concerne la charge d'un dérivé local, pas un droit de promotion. |
| `BIBLIOTHEQUE/MODIFIER` refusé par le lecteur CLI et validateur de carte vert | Occurrence supplémentaire F-DIR-028/F-ACT-001 ; conserver repérage direct du titre et auditer l'index/les consommateurs lors des phases 5 et 13. |

**Aucun nouvel ID F-BIB.** La section fournit déjà une condition d'activation, trois tests distincts, un fallback pour la navigation, une alternative aux signaux uniquement matériels et une garde contre la recette partagée sans gain. Les zones à éprouver sont la décision de sélectionner **zéro/une/deux** routes dans un cas réel, la matrice finie des fonds et états, l'effet de la matière et les idiomes d'interaction selon le médium. Aucun de ces points ne doit devenir un score ou une obligation universelle hors du risque déclaré. F-BIB-001/002/003 restent provisoires sans nouvelle occurrence normative ici.

## Couverture et reprise

| Passage | Profondeur | Couverture et limite |
|---|---|---|
| A — architecture | FULL | 585–610, trois routes sous le préfixe MODIFIER, frontière style/objet/micro/scène, CLI refusé |
| B — sémantique | FULL | Conditions et tests 589–607 ; portée de preuve, test de retrait, matrice, médium et partage |
| C — usage | TARGETED | Neuf situations fictives ; aucun résultat de runtime ou utilisateur |
| D — résistance | TARGETED | Déduplication F-DIR-028/F-ACT-001 et F-SAV-006 ; aucun nouvel ID BIB |
| Machine | TARGETED | Locator MODIFIER refusé, carte dérivée valide ; aucun fixture de composant rejoué |
| Externe | N/A-JUSTIFIED | Aucun claim externe nécessaire pour lire les trois contrats internes ; les normes applicables restent à déterminer par médium lors d'un run réel |

Le séparateur est à 609 et la ligne 610 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md` lignes **611–660**, `COMPONENTS` ; reprendre §12, le présent rapport et les responsabilités de couches, puis vérifier dépendances, promotion et frontières avec SAVOIR/SYSTEM et ACTION/RUN-SYSTEM.
