# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 9 : STYLE, profils et dials

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **574–689** : introduction/parcours (574–578), sélection et trace (580–599), taxonomie et huit profils (601–626), test (628–632), neuf dials (634–650), traduction multi-médias (652–656), ponctuation située (658–662), anti-slop procédural (664–670), vocabulaire (672–686), séparateur 688. `SAVOIR/SYSTEM` commence à 690.
- Protocole externe v2.0 §12, quatre passages A–D. Continuité : plan maître, rapport SAVOIR bloc 8, checkpoints DIRECTION/ACTION et constats SAVOIR 001–004. Lecture des interfaces `DIRECTION/CREATIVE-BOOT`, `DOMAIN-FRAME`, `REUSE-CHALLENGE`, `VISUAL_TARGET`, `ACTION` (intention, décision, preuve, gates, routage), `SAVOIR/FRAME`, `SOURCE`, `DESIGN-ATLAS`, et projection machine `run_card.schema.json`/fixtures.
- Baseline B01 inchangée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Portée : diagnostic documentaire et test ciblé de la validation machine ; aucun produit, rendu, source culturelle, standard ou public réel n’est évalué. Les jugements d’efficacité de style restent à tester sur artefacts et personnes quand le run le demande.

## Conclusion locale

STYLE refuse utilement le profil automatique, le cliché sectoriel, la mode prise pour une norme et la confusion entre expression et preuve. Son catalogue est borné mais non prioritaire sur une référence réelle ou une direction construite ; les dials sont qualitatifs, situés et peuvent rester inchangés. Le réemploi doit être justifié, et l’absence de profil est une sortie légitime.

Deux tensions vérifiables méritent des IDs provisoires. **F-SAV-005** : la fiche `PROFILE-DECISION` exige une décision « réellement modifiée » dans le choix du profil et se mappe à la fois à l’intention pré-build et au changement post-observation, sans indiquer quand chacun est autorisé ; la projection tolère en outre une `profile_decision.evidence` purement prospective. **F-SAV-006** : le test de style conclut qu’il n’y a « seulement une étiquette » quand on cache l’image, les couleurs et le logo sans garder de différence de type/hiérarchie/densité/matière ; ce verdict peut rejeter à tort un profil dont la différence utile est justement dans l’image ou la couleur. Les conséquences en runs réels restent à éprouver ; aucun patch n’est décidé ici.

## Passage A — architecture visible

| Segment | Forme et statut | Effet sur le parcours |
|---|---|---|
| 574–599 | Section `SAVOIR/STYLE`, parcours, règle de sélection, quatre champs de fiche, réemploi | Profil conditionnel ; FRONTIÈRE `FRAME/STYLE` contre `BIBLIOTHEQUE/SELECT`, `ACTION/RUN_CARD` et preuve |
| 601–626 | Sept dimensions de taxonomie, huit profils internes avec intention/expression/contre-indication | Exemples d’expression, non genres scientifiques ni packs obligatoires |
| 628–650 | Un test de masquage, neuf dials `[À ADAPTER]` et garde-fous | Hypothèses perceptuelles ; test du profil contesté sur les rôles image/couleur/mouvement |
| 652–662 | Médiums et règle de ponctuation | Une intention peut se traduire en son, espace ou haptique ; reflow et locale gouvernent la ponctuation |
| 664–686 | Test anti-slop et sept expressions faibles à préciser | Critiquer symptômes observables plutôt que labels ou adjectifs ; ne pas créer de verdict esthétique |

`read_route.py SAVOIR/STYLE` renvoie « locator inconnu » alors que le titre existe ; `validate_reading_map.py` passe. C’est une occurrence de **F-DIR-028/F-ACT-001**, à conserver comme test du lecteur sans créer un nouvel ID pour cette route. Les identifiants `STYLE/...` du tableau de profils n’accordent pas un nouveau mode, gate ou verdict : le chargement de cette section suit `SAVOIR/ROUTING` et le risque réel.

## Passage B — contrat sémantique, section par section

### Entrée, sélection, temporalité de la fiche (574–599)

Le profil décrit une **manière d’exprimer** une décision, pas la tâche, le support ou la scène. La nécessité de FRAME et d’une structure approfondie dépend du problème : `BIBLIOTHEQUE/SELECT` n’est chargé que si la structure est ouverte, et le profil peut rester absent. STYLE 582 demande qu’un profil puisse modifier une décision du run ; cela se lit d’abord comme une hypothèse d’intention. Pourtant le bloc de trace 584–593 demande `PROFILE-DECISION — décision réellement modifiée`, `EVIDENCE — preuve montrant son effet`, puis mappe le premier champ à **la fois** vers `DECISION-INTENT` et `DECISION-CHANGE`. ACTION 206–218 et 232–236 sépare formellement l’intention avant build et la confirmation/modification/abandon seulement après observation dans le scope. Le texte STYLE ne fournit pas cette séparation temporelle ; F-SAV-005 en découle.

Le schéma machine possède, en plus de `decision_intent`, de `decision_change`, de `proof` et du `trace_locator`, un objet facultatif `profile_decision` qui exige quatre chaînes, notamment `decision` et `evidence`. STYLE 593 parle de mapping vers les champs ACTION, mais n’explique pas si cet objet représente l’hypothèse, le résultat, ou les deux ; le validateur ne lit pas une phrase d’« evidence » comme une observation datée. Il n’est pas nécessaire d’exiger tous les détails dans le JSON ; il est nécessaire de ne pas promouvoir une hypothèse de profil en constat simplement parce que quatre chaînes sont remplies. Cette perte de phase renforce F-ACT-002/013/028, sans leur confondre la formulation propriétaire locale.

Les règles de refus du profil genre/premium/composants (595), de non-réemploi de confort (597) et de référence réelle transformée plutôt que copiée (599) sont solides. Le catalogue est borné et non exclusif ; le profil découvert/construit reste permis. `WHY-NOW` et `REUSE-CHALLENGE` comparent décision, public, contexte et relation du run antérieur au présent ; une source réelle doit garder provenance/limite et une source générée n’acquiert pas le rang de calibration externe de SOURCE (F-SAV-003).

### Taxonomie, profils et épreuve du retrait (601–632)

Les sept dimensions aident à séparer composition, matière, représentation, culture, énergie, interaction et voix. Les huit profils listent chaque fois une intention et une contre-indication : ni `RAW_BRUTALISM` ni `QUIET_SYSTEM` n’est une esthétique par défaut ; `MAXIMAL_EXPRESSION` peut être valable si le contenu et les points de repos soutiennent l’usage. `PICTORIAL_UTILITY` fait expressément de l’image ou de l’illustration un repère explicatif (621) ; `MAXIMAL_EXPRESSION` autorise couleur et matière coordonnée (623), et la traduction multi-médias peut reposer sur son, motion ou haptique (654).

Le test 632 masque **image, couleurs de marque et logo**, puis, si les autres dimensions ne diffèrent plus substantiellement, conclut sans réserve qu’il n’y avait pas de profil. Un masquage peut être une bonne **contre-épreuve conditionnelle** contre un simple logo posé sur une grille générique ; il ne prouve pas l’absence d’une décision située lorsque l’élément masqué est précisément le support de la relation. Cas discriminant : même grille et même type, mais une illustration authentique et autorisée remplace un texte ambigu par un repère concret qui change la compréhension ou l’orientation ; retirer l’image fait disparaître le profil `PICTORIAL_UTILITY` alors que l’effet sur l’objet intégral est justement ce qu’il faut inspecter. Autre cas : couleur dont les rôles sont hiérarchie/états, sans compter sur elle seule pour l’accessibilité. La formulation universelle de 632 reçoit F-SAV-006 ; le test utile de retrait reste à préserver lorsqu’il évalue la dépendance/fallback plutôt que d’exiger la survie du profil après suppression de son médium.

### Dials, médiums et mise en preuve (634–656)

Neuf dials varient variance, motion, densité, contraste, matérialité, voix typographique, formalité, intensité émotionnelle et originalité. Ils ne sont ni une échelle chiffrée ni un formulaire de neuf réponses. Position basse/haute a une contre-indication ; un dial inchangé est permis. La phrase 650 les place « après `DOMAIN-FRAME` et `CREATIVE-BOOT` » ; ces deux vues sont conditionnelles chez DIRECTION (boot pour décision visuelle ouverte ; domaine pour demande nouvelle, multiple ou ambiguë). Ce raccourci ne doit pas devenir l’obligation de fabriquer ces deux artefacts à chaque révision de style locale ; le risque de chargement réflexe est transporté sous F-SAV-001 et la protection one-shot F-DIR-009, sans nouvel ID tant que les déclencheurs supérieurs permettent une lecture conditionnelle.

La traduction en son, espace, haptique, image ou interface (654) rend le profil indépendant d’une recette technique. Elle renforce aussi F-SAV-006 : la preuve du style doit être adaptée au **médium porteur**, sans inférer une compréhension utilisateur du seul jugement expert. Le dial Motion ne neutralise jamais reduced motion, performance ou accessibilité ; la preuve exécutée et sa limite appartiennent à ACTION/CONTEXT.

### Ponctuation, procédure et vocabulaire (658–686)

Le cadratin n’est ni interdit ni signature automatique ; la décision dépend de la langue, du rôle du texte, du reflow, de la lecture assistée et de la relation logique. Une répétition déclenche une relecture, sans « faute » basée sur un nombre de signes. Le test anti-slop (664–670) exige conséquence, observation, limite et prochaine action plutôt qu’un dossier qui ne change rien ; l’étiquette « slop » doit être rattachée à un symptôme. La phrase 668 « si rien ne change ... utilise `N/A-JUSTIFIED` » est recevable pour une procédure réellement inapplicable, mais un effet attendu non observé ou une preuve manquante relève de `NOT-OBSERVED` ou `NOT-VERIFIED` selon ACTION 236 : occurrence des constats F-DIR-011/019 et F-ACT-014, sans nouvel ID.

Les sept adjectifs ou expressions faibles (678–684) ne sont pas interdits dans une marque, une citation ou une hypothèse ; ils deviennent insuffisants **comme justification** sans conséquence située et contre-indication. « Intuitif » ne vaut pas observation de tâche ; « premium » ne vaut pas qualité universelle. L’écriture concrète enrichit le jugement sans produire un score esthétique ni exclure un langage culturel légitime.

## Passage C — lecteurs et scénarios sous contrainte de temps

1. **Designer, STYLE avant build.** Il peut choisir provisoirement un profil pour préciser une hiérarchie à essayer. STYLE 587 lui demande déjà une décision « réellement modifiée » et une preuve d’effet ; ACTION n’autorise encore que l’intention. Si la trace mélange les deux, une hypothèse peut devenir résultat (F-SAV-005).
2. **Mainteneur, carte validée.** Il met `profile_decision.evidence = « capture prévue après build ; aucun rendu du profil observé »` dans une fixture DIRECTION déjà clôturée, sans autre changement. Le validateur de carte renvoie succès : la chaîne est non vide, la validité structurelle ne garantit pas la réalité de la preuve du profil. Ce test n’affirme pas que le run fictif est valablement conclu sur le fond.
3. **Designer, illustration explicative.** La grille et le type restent stables, l’image apporte le repère concret à la tâche. La masquer fait disparaître la différence ; le test 632 classe pourtant le profil comme étiquette. Il faut examiner la relation **avec** l’image et son fallback, non rejeter le profil par ablation universelle (F-SAV-006).
4. **Reviewer, site coloré/énergique.** Il constate des rôles colorés lisibles et une hiérarchie cohérente. Retirer toutes les couleurs de marque pour conclure que le profil est illégitime ajoute à la possible prescription de neutres de F-SAV-002 ; contraste/état/fallback restent à tester séparément.
5. **Équipe produit, profil hérité.** Elle documente `WHY-NOW`, ce qui a changé de public et le contre-exemple qui ferait abandonner le profil ; elle peut renoncer au style ancien sans créer un profil par brief.
6. **Intégrateur, profil `DIGITAL_MEMORY` en motion.** Il conserve le médium, le comportement reduced motion, le fallback, le runtime et la capture observée dans leur scope ; une image statique ou une étiquette de style ne prouve pas une animation exécutée.
7. **Éditeur, texte localisé.** Il change un cadratin répété si le sens ou le reflow souffre, mais ne remplace pas mécaniquement tous les cadratins ; il qualifie l’effet réel de la ponctuation.

## Passage D — résistance et registre

### F-SAV-005 — le champ PROFILE-DECISION confond intention de profil et décision constatée

- **Gravité provisoire : Significatif à éprouver.** Contradiction de temporalité textuelle confirmée ; occurrence machine positive sur une chaîne prospective ; incidence réelle à tester.
- **Preuve :** STYLE 582, 584–593, 599 demandent sélection et « décision réellement modifiée » puis mappent le même libellé à `DECISION-INTENT` **et** `DECISION-CHANGE`. ACTION 206–218 et 232–236 exige une observation avant le second. Le schéma a `profile_decision.decision/evidence` facultatifs au niveau carte mais `evidence` obligatoire si cet objet existe ; le validateur n’exige qu’une chaîne non vide.
- **Contre-exemple :** une fiche préparatoire dit « cette voix typographique devrait clarifier le premier geste », joint seulement « capture prévue » et choisit le profil avant construction. Il y a une hypothèse réelle, pas encore une décision modifiée prouvée. Une fiche post-build avec capture et méthode peut, elle, relier l’effet observé au changement ou à la confirmation.
- **Épreuve ciblée :** copie temporaire de `schemas/fixtures/valid_direction_with_profile_decision.json`, remplacer `profile_decision.decision` par une hypothèse future et `profile_decision.evidence` par « Capture prévue après build ; aucun rendu du profil observé » ; `python3 scripts/validate_run_card.py <copie>` renvoie code 0 et `RUN_CARD VALIDATION PASSED`. Les autres champs de la fixture sont restés ceux d’une DIRECTION clôturée avec une autre décision déjà observée. Cela prouve la limite de ce contrôle ciblé, pas l’existence d’une décision de style fausse sur un produit réel.
- **Effet possible :** fiche profil anticipée lue comme preuve de résultat, puis clôture ou réemploi de style avec autorité excessive. Un lecteur qui suit le protocole ACTION et consulte la capture/trace peut éviter ce glissement.
- **Propriétaire pressenti :** SAVOIR/STYLE pour nommer intention/profil sélectionné versus conséquence constatée ; ACTION et schéma pour le transport et la condition de preuve sans forcer un formulaire universel.
- **Relations sans fusion :** F-ACT-013 couvre `decision_change` optionnel/non typé, F-ACT-002/028 le mapping et la trace ; F-DIR-003 la temporalité du handoff. F-SAV-005 porte le **même libellé local de sélection style projeté avant et après observation** ; corriger le schéma seul ne clarifierait pas 587/593.
- **Test futur :** pré-build sans profil observé, post-build profil retenu, profil abandonné après observation, profil sans effet attendu, profil ancien réutilisé. Comparer fiche locale, carte, méthode, `DECISION-INTENT`, `DECISION-CHANGE` et statut des preuves.

### F-SAV-006 — le test de masquage peut rejeter une expression portée par le médium masqué

- **Gravité provisoire : Significatif à éprouver.** Contradiction de portée avec les profils de représentation/couleur/médium ; aucune mesure utilisateur fournie.
- **Preuve :** STYLE 632 conclut « il n’y avait pas de profil choisi » si masquage image/couleurs/logo supprime la différence de hiérarchie/type/densité/matière. STYLE 609 et 621 donnent explicitement un profil image explicatif ; STYLE 623 et 654 acceptent couleur et médias différents. `DIRECTION/VISUAL_TARGET` 385 et 405 autorise asset/matière lorsque la relation produit tient dans l’artefact ; ACTION/GATE-C 785–794 observe rendu et élément concrets.
- **Contre-exemples discriminants :** (a) illustration autorisée porte seule une orientation nouvelle tandis que grille et typographie demeurent stables ; (b) motif ou couleur de marque donne un signal distinct, avec information non chromatique et contraste validés. Un profil temporel ou sonore montre séparément qu’un test purement statique ne suffit pas à juger tous les médiums. L’ablation sert à tester dépendance/fallback, pas à prononcer automatiquement l’absence de profil dans les deux premiers cas.
- **Risque :** appauvrissement d’une expression fonctionnelle, imposition implicite de différences typographiques/structurelles pour « prouver » un profil, ou suppression d’un asset utile ; inversement, un logo décoratif sur un template doit bien être contesté.
- **Propriétaire pressenti :** SAVOIR/STYLE pour qualifier la portée du test ; SOURCE et ACTION restent responsables de l’intégration, des droits, du fallback et de la preuve adaptée.
- **Relations sans fusion :** F-SAV-002 est une prescription possible de palette neutre sous un tag requis ; F-SAV-006 est **un test de validité du profil fondé sur retrait de ses éléments porteurs**. F-DIR-018 concerne l’interdiction de formes du premier objet, autre mécanisme.
- **Test futur :** comparer deux objets complets à typographie/grille identiques, dont un seul intègre l’image explicative ; faire varier également couleur porteuse, logo décoratif isolé et média motion. Juger rôle, tâche, droits, accessibilité, fallback et possibilité d’observer la relation. Un masquage ne vaut conclusion que pour la question qu’il teste.

### Occurrences préexistantes, sans nouvel ID

| Lecture locale | Constat transporté |
|---|---|
| FRAME/CREATIVE-BOOT présentés comme antécédents systématiques du dial | F-SAV-001 ; F-DIR-009 si boot entraîne une repasse artificielle |
| Couleur « neutres/accent » susceptible d’affaiblir MAXIMAL_EXPRESSION | F-SAV-002, en lien mais non fusionné avec F-SAV-006 |
| Référence générée ou externe pour profil : observation, licence, réserve | F-SAV-003, F-ACT-024/028 |
| Fiche profil, preuve et trace ne sont pas magiquement garanties par une carte valide | F-ACT-002/013/028 ; F-SAV-005 couvre le défaut temporel local |
| `N/A-JUSTIFIED` de 668 alors qu’un effet attendu n’est pas observé | F-DIR-011/019, F-ACT-014 ; lire avec ACTION 236 |
| Le test du STYLE ne remplace ni jugement CRAFT ni Gate C | F-DIR-030, F-DIR-024 ; effet perceptuel ≠ preuve d’usage |
| Locator STYLE refusé alors que le titre est réel | F-DIR-028/F-ACT-001 |

## Contrôles et qualités à protéger

Hashes B01 vérifiés. Lecteur `SAVOIR/STYLE` refusé, carte de lecture valide. Épreuve machine unique de `profile_decision` sur copie : succès structurel malgré preuve prospective explicite ; l’épreuve isole le défaut de qualification de cette chaîne, elle ne valide aucun vrai run. Le test de masquage est évalué par contre-exemples logiques ; une étude perceptuelle ou d’usage demanderait des objets réels et un public/scope déclarés.

1. Zéro profil est valide ; un profil interne ne prime pas sur une expression située construite ou réellement observée.
2. Les sept dimensions et huit profils servent à poser des questions, jamais à imposer une collection de motifs, un secteur ou un style « premium ».
3. La contre-indication et le réemploi situé empêchent l’application automatique d’un profil déjà disponible.
4. Les dials restent qualitatifs et soumis aux obligations d’accessibilité, de preuve, de public et de médium.
5. Le test de retrait garde sa valeur pour détecter le décor de marque ou un asset fragile, avec portée bornée à l’objet de l’épreuve.
6. Ponctuation et vocabulaire sont relus pour leur effet, sans blacklist de signes ou d’adjectifs.
7. ACTION demeure la source de statut, méthode, résultat et verdict ; un jugement esthétique ne prouve pas une tâche ni une conformité globale.

## Couverture et suite

| Passage | Profondeur | Résultat |
|---|---|---|
| A — architecture | FULL | Règle, sept dimensions, huit profils, neuf dials, test et interfaces |
| B — sémantique | FULL | Sélection, temporalité, réemploi, médiums, ponctuation, slop et vocabulaire |
| C — usage réel | TARGETED | Sept scénarios designer, mainteneur, reviewer, intégrateur et éditeur |
| D — résistance | TARGETED | F-SAV-005/006 provisoires ; sept occurrences rattachées aux constats existants |
| Machine | TARGETED | Locator refusé, lecture dérivée validée, une mutation de fixture acceptée ; pas de réexécution globale |
| Externe | N/A-JUSTIFIED ici | Aucun standard culturel ou claim empirique externe employé comme prémisse |

Bloc 9 terminé sans patch ni verdict global. **Prochaine unité : SAVOIR.md 690–707, `SAVOIR/SYSTEM`**, tokens et composants partagés ; `SAVOIR/CONTEXT` commence à 708. Vérifier particulièrement F-SAV-004 et le partage des responsabilités avec BIBLIOTHEQUE et ACTION.
