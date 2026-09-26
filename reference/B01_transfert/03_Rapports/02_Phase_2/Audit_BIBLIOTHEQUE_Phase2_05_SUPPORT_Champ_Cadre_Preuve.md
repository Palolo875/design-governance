# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 5 : SUPPORT

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 288–339** : rôle du support 288–290 ; quatre variantes 292–330 ; test et frontière avec SCENE 332–336 ; séparateur 338. `BIBLIOTHEQUE/GRID` commence à 340 et appartient au bloc suivant.
- Méthode : protocole externe v2.0 §12, quatre passages A–D relus ; rapport bloc 4 CONTRACTS, rapports blocs 1–3 et plan maître consultés. Interfaces ciblées : SELECT 163–199, CONTRACTS 258–284, préfixes 129–142 ; SCENE 441–469 et COMPAT 661–685 consultés **uniquement pour la frontière et la cohérence**, sans anticiper leur audit propriétaire ; ACTION 161–175, 624–655 ; SAVOIR/STYLE 576 et son constat antérieur F-SAV-006.
- Baseline B01 inchangée : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Diagnostic sectionnel, sans patch ni verdict global. Les scénarios ci-dessous simulent des lectures documentaires ; aucune expérience d'usage ou mesure de gain n'est prétendue.

## Passage A — architecture et portée du niveau SUPPORT

SUPPORT est le **champ spatial** dans lequel entrent navigation, données, médias et surface produit (290, 133). GRID organise axes et regard **dans** ce champ ; SCENE décrit le scénario liant contenu, preuve et action (134–135, 336). Ce découpage est illustré plus loin par `SCENE/EDITORIAL_FIELD` par rapport à `SUPPORT/FREE_FIELD` (449), `SCENE/FRAMED_PRODUCT` par rapport à `SUPPORT/ARCHITECTED_FRAME` (459), et `SCENE/OPERATING_GRID` par rapport à `SUPPORT/OPERATIONAL_CANVAS` (469). Un support n'est ni une direction de style SAVOIR, ni une preuve par son nom, ni un ordre obligatoire de charger GRID/SCENE.

Quatre identifiants de variantes sont présents et distincts : `SUPPORT/FREE_FIELD`, `SUPPORT/ARCHITECTED_FRAME`, `SUPPORT/OPERATIONAL_CANVAS`, `SUPPORT/COLLECTION_PLINTH`. La matrice COMPAT 678–681 mentionne les quatre et la qualifie d'hypothèses, sans combinaisons imposées (663–674). `BIBLIOTHEQUE/SELECT` 163–167 permet **zéro route** si le champ hérité suffit ; la table 195 réserve un nouveau SUPPORT en STANDARD au champ ouvert, et 196 dit d'évaluer puis retenir uniquement ce qui change la décision en DIRECTION. Un produit opérationnel peut donc avoir des repères stables sans charger cette route sur chaque correction locale.

`python3 scripts/read_route.py BIBLIOTHEQUE/SUPPORT` refuse cet identifiant, alors que la section et son titre existent ; `validate_reading_map.py` passe. Le lecteur CLI utilise les locators explicitement listés dans la carte, qui recommande par ailleurs le repérage des autres titres exacts par préfixe et fichier propriétaire. C'est une nouvelle **occurrence de F-DIR-028/F-ACT-001**, comme CONTRACTS au bloc 4, à ajouter à la matrice future des titres promis versus locators outillés ; aucun ID supplémentaire pour un deuxième échec de la même cause.

## Passage B — lecture du contrat dans l'ordre

| Lignes et variante | Décision de champ, condition et contre-indication | Ce que la preuve devrait établir et ce qu'elle n'établit pas seule |
|---|---|---|
| 292–300, `FREE_FIELD` | Champ sans châssis pour une promesse, une illustration ou un geste de marque avant preuve détaillée ; éviter si comparaison dense, tâche opérationnelle ou contexte critique exigent des repères continus | Foyer, circulation et **zone de preuve encore lisibles** malgré l'absence de cadre ; `PERCEPTUAL` en premier, ajouter `USER/TASK` si le champ porte une action. L'expressivité ne dispense pas de preuve produit ni de tâche si celle-ci est revendiquée |
| 302–310, `ARCHITECTED_FRAME` | Encadrement, axes ou seuils qui rendent construction/soin/institution perceptibles ; éviter quand intimité, spontanéité ou récit organique seraient refroidis | Le cadre doit organiser une relation d'usage ou de preuve ; une bordure qui signale seulement du prestige ne satisfait pas le contrat. Jugement sur le rendu réel, puis preuve de tâche si une efficacité d'usage est revendiquée |
| 312–320, `OPERATIONAL_CANVAS` | Surface instrumentée : contrôles, contexte et données en première lecture pour observer, comparer, administrer ou décider ; éviter quand une pièce média ou un manifeste est la tâche dominante | Contrôles et données retrouvables sans décor concurrent ; `USER/TASK` si une décision est portée. Une capture bien ordonnée ne prouve pas la récupération d'une donnée, la justesse d'une décision ni les états critiques |
| 322–330, `COLLECTION_PLINTH` | Pièces séparées, archive/portfolio/cas/média avec vide généreux et proportions d'objet ; éviter lorsque comparaison rapide ou manipulation dense dominent | Chaque pièce garde identité, métadonnées et lien à l'action. Une impression de collection n'établit pas à elle seule que les métadonnées sont retrouvées, comparables et utiles dans le scope réel |

« Choisir lorsque » et « éviter lorsque » sont des **conditions de décision**, pas un algorithme de mode ou une liste d'interdits. Un brief peut mêler introduction expressive et tableau dense : sélectionner des supports selon surfaces et tâches distinctes, déclarer l'héritage si applicable, et vérifier la transition ; le texte ne demande pas de choisir une seule variante pour tout le produit. La proposition et la prochaine preuve sont préparatoires ; après construction, ACTION conserve artefact, méthode, portée, axes et issue. La métaphore du cadre ou la préférence de style n'autorise pas une route sans conséquence observable (SELECT 165–167).

### Test de masquage et frontière de preuve (332–336)

La phrase 334 demande qu'après masquage du **texte, des données et des images**, cadre, vide, axes et foyer indiquent encore un parti de composition. Elle qualifie elle-même cette opération de contrôle `PERCEPTUAL` ou `EXPERT` qui **ne prouve pas l'utilisabilité**. Elle ne transforme donc ni la silhouette restante en PASS U, ni l'image masquée en preuve que la tâche est absente. Pour `FREE_FIELD`, l'épreuve peut révéler une hiérarchie purement portée par l'illustration ; pour `OPERATIONAL_CANVAS` et `COLLECTION_PLINTH`, les libellés, chiffres, métadonnées et images constituent parfois précisément la relation à juger. Il faut faire **deux inspections distinctes** : test abstrait de composition et rendu réel avec contenu, état, viewport et action. Si la première paraît faible mais que la seconde démontre une décision juste et proportionnée, ne conclure ni rejet automatique ni PASS global sur un seul test.

Cette limite ressemble à F-SAV-006 (le masquage image/couleur pouvait faire rejeter un style légitimement porté par le médium retiré), mais elle n'est pas encore la même contradiction : SUPPORT exige seulement un **parti de composition**, sans annoncer que la route ou le profil est invalide si le test isolé échoue ; le texte borne expressément sa conclusion à 334. Test discriminant réservé : surface à forte valeur sémantique dont la composition s'appuie sur données réelles, comparée à une surface dont les masses et les repères disparaissent parce qu'elle n'a aucune hiérarchie. Le résultat en contexte tranchera l'éventuelle tension ; pas d'ID BIB autonome sur cette hypothèse.

Les contrats de modes, mobile, accessibilité, confidentialité, permissions et performance continuent de s'appliquer **si leur risque ou leur médium les active** (CONTRACTS 269–284, ACTION 625–655). Rien dans ce bloc n'affirme que `FREE_FIELD` est exempt de focus visible, que `OPERATIONAL_CANVAS` valide une décision opérationnelle par seul agencement ou que le test masqué remplace une observation sur device. `SCENE` conserve le scénario de preuve (336) : les ressemblances de noms ne fusionnent pas les deux responsabilités.

## Passage C — simulations de lecteurs

| Cas | Suite attendue | Erreur recherchée |
|---|---|---|
| Designer, correctif de texte d'une page structurée | Hériter du champ, traiter contenu et preuve selon le risque ; zéro SUPPORT nouveau | Sélectionner une route pour reproduire l'existant |
| Designer, première entrée de marque suivie d'un comparateur | Considérer `FREE_FIELD` pour la promesse et un champ à repères pour la comparaison ; vérifier transition et zone de preuve | Imposer `FREE_FIELD` à la tâche dense au nom du premier écran |
| Agent, dashboard de surveillance avec alerte et récupération | Évaluer `OPERATIONAL_CANVAS`, données/contrôles dans état réel, tâche observée et risque d'erreur | Déclarer la décision réussie sur seule capture nominale |
| Designer, portfolio de cas qu'il faut retrouver puis comparer | `COLLECTION_PLINTH` si identité et métadonnées restent retrouvables ; revenir si vitesse de comparaison domine | Sacrifier métadonnées et action pour le vide artistique |
| Reviewer, châssis « premium » sans effet sur usage ou preuve | Refuser `ARCHITECTED_FRAME` décoratif et questionner la responsabilité réelle | Faire de la bordure un argument d'autorité |
| Intégrateur, collection où les images sont volontairement structurantes | Faire le test masqué comme lecture des masses, puis contrôler pièces/métadonnées en rendu complet et états applicables | Prononcer un échec global parce que l'image masquée portait le sens, ou un PASS parce que les cases vides s'alignent |
| Designer, surface non web avec contraintes spatiales propres | Traduire le champ dans le support réellement observé, annoncer médium, méthode et limites | Répliquer un viewport web ou une capture non représentative |
| Agent, CLI refuse `BIBLIOTHEQUE/SUPPORT` | Signaler l'échec, ouvrir le titre dans le fichier propriétaire, rattacher F-DIR-028/F-ACT-001 | Inventer la route ou ignorer un contrat existant |

Ces huit parcours visent les variantes et la non-sélection. Ils ne mesurent ni proportion d'erreurs, ni qualité finale, ni temps de décision ; les verdicts de run restent chez ACTION.

## Passage D — résistance et déduplication

**Aucun nouvel ID autonome dans ce bloc.** La section formule quatre décisions et leurs contre-indications, donne un rôle de preuve prioritaire sans le confondre avec une méthode ou une réussite, borne le test de masquage et sépare explicitement support et scène. Les risques relevés se distribuent comme suit :

| Point éprouvé | Suite et relation |
|---|---|
| SUPPORT de premier niveau refusé par `read_route.py`, carte verte | F-DIR-028/F-ACT-001 ; ajouter la route au futur test de couverture des titres exacts et documenter la portée effective du CLI |
| Test masqué pris pour preuve de réussite ou d'échec fonctionnel | Texte 334 interdit le PASS U implicite ; observation en rendu réel selon ACTION. Comparer avec F-SAV-006 seulement pour la technique d'ablation, sans fusion prématurée |
| DIRECTION ou STANDARD chargé de tous les supports ou support de style imposé | SELECT 163, 195–196 ; START classe le mode ; F-DIR-041 reste la tension de présélection STANDARD |
| Support qui fonctionne uniquement avec contenu idéal ou état nominal | READ 125–127, CONTRACTS 269–284 et F-ACT-005/021 ; borner le scope réellement observé et la prochaine preuve |
| Association favorable COMPAT traitée comme recette | COMPAT 663–674 déclare une hypothèse, à réexaminer lors de son bloc propriétaire |
| Forme locale de support à inventer pour un seul cas | F-BIB-002 : garder contrat initial proportionné, responsabilité et preuve selon le risque ; aucune promotion par nom ou fréquence |

F-BIB-001 demeure ouvert sur l'exception de paire B1b de SELECT 173 ; aucune phrase de SUPPORT ne l'élargit. Les quatre variantes décrivent des possibilités de composition et de robustesse ; l'effectivité sur des surfaces réelles reste `NOT-VERIFIED` jusqu'aux essais adéquats.

## Couverture, limites et suite

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | 288–339, quatre variantes, niveau SUPPORT, accès CLI, frontière avec GRID/SCENE |
| B — contrat | FULL | Rôle, conditions, refus et preuves 290–336 ; masque, type de preuve et limites |
| C — usage | TARGETED | Huit cas simulés ; sans observation de produit ni mesure |
| D — résistance | TARGETED | Masquage, preuve de tâche, proportion et cas mixtes ; rattachements sans nouvel ID |
| Machine | TARGETED | CLI SUPPORT refusé ; `validate_reading_map.py` passe ; pas de schéma ou fixture exécutés pour ce bloc |
| Externe | N/A-JUSTIFIED | Aucune assertion externe nécessaire pour juger ce contrat documentaire |

Le séparateur est à 338, la ligne 339 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **340–424**, `GRID` ; relire le protocole, le présent rapport, SELECT/CONTRACTS et les constats existants avant d'évaluer chaque famille de grille et leurs tests.
