# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 3 : SELECT et DERIVE

## Cadre et reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 161–255** ; SELECT 161–214, DERIVE et signaux de convergence 215–252, séparateur 254. `BIBLIOTHEQUE/CONTRACTS` commence à 256 et sera examiné au prochain bloc.
- Méthode : protocole externe v2.0 §12, quatre passages A–D ; rapport BIBLIOTHEQUE bloc 2, checkpoints DIRECTION, ACTION et SAVOIR relus. Interfaces ciblées : `DIRECTION/START`, `ACTION/FAST-PATH`, `ACTION/GATE-B/B1b` 702–716, `ACTION/CLOSE-EXIT-CHECK`, `SAVOIR/STYLE` et `SAVOIR/CRAFT`.
- Baseline B01 stable : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Ce rapport qualifie une lecture documentaire et des simulations de lecteurs ; ni résultat d'usage réel, ni patch normatif, ni verdict système global.

## Passage A — architecture et frontières

`BIBLIOTHEQUE/SELECT` est une route accessible par `read_route.py` ; elle regroupe également FAST-PATH, questions, sélection par mode, one-shot, garde-fou, DERIVE et signaux de convergence. Le titre `BIBLIOTHEQUE/DERIVE` à la ligne 215 est une **sous-section**, et `read_route.py BIBLIOTHEQUE/DERIVE` ne la résout pas comme route autonome. `validate_reading_map.py` passe. Cette différence entre titre et adresse est une occurrence des problèmes de résolution déjà suivis par F-DIR-028/F-ACT-001 ; le bloc n'établit ni coût réel de lecture, ni besoin prouvé d'une nouvelle route.

L'ordre d'autorité est net aux lignes 163–167 : `DIRECTION/START` classe le mode ; `SAVOIR/STYLE` intervient lorsque le registre d'expression pourrait changer la structure ; SELECT choisit **zéro à plusieurs responsabilités** seulement si elles changent la prochaine décision. Le filtre exige décision, niveau minimal, premier objet et preuve de sortie **avant** le catalogue. Un nom séduisant ou une sélection de table n'est pas une preuve. BIBLIOTHEQUE garde la responsabilité structurelle ; ACTION garde observation, statuts et clôture (199–205), SAVOIR la qualité située du geste et de la matière (209–213), EVOLUTION/CHANGELOG l'adoption des routes (237).

La trace structurelle de la ligne 199 se loge dans la `RUN_CARD` ou sa trace canonique référencée par `trace_locator`, avec sources ou paquet de preuve pour les routes : pas de statut ni champ machine concurrent. Son énumération réunit des éléments **préparatoires** (`DECISION`, `RISK`, `NEXT-PROOF`) et **postérieurs à l'observation** (`ARTIFACT`, `OBSERVATION/METHOD`, `DECISION-CHANGE`). Les remplir ensemble avant de construire serait une erreur temporelle déjà couverte par F-DIR-003/006 et F-ACT-002/030. Le prochain audit des contrats doit contrôler la projection réelle de ces éléments ; cette phrase seule ne prouve pas qu'ils sont tous stockables.

## Passage B — contrat sémantique dans l'ordre du texte

### Choisir seulement ce qui change la décision (161–167)

SELECT peut laisser la structure héritée, retenir un support ou une grille, une scène, un objet de preuve, un objet de rythme, un micro contrat ou un modificateur **si son comportement est réel** (163). Une route sans effet sur espace, hiérarchie, comportement ou preuve est refusée (165). Le filtre 167 empêche de chercher dans un catalogue pour résoudre un manque de brief : revenir à START, hériter ou demander une clarification ciblée. La preuve de sortie est une cible anticipée ; elle ne transforme pas le premier objet encore absent en observation acquise.

### FAST-PATH et non-applicabilité (169–173)

Le delta local se formule par relation, risque, preuve la moins coûteuse et décision différente après résultat positif ou négatif (171). Si aucune décision structurelle ne change, hériter ou traiter le cas documentaire ; un contrôle applicable du run reste à satisfaire selon ACTION. La ligne 171 réserve `N/A-JUSTIFIED` à la non-applicabilité réelle. La ligne 173 ajoute la branche d'une « paire équivalente » encore valide après le dernier changement substantiel, avec artefact, owner et `NEXT-PROOF` « selon ACTION ». Cette branche reprend manifestement `ACTION/GATE-B/B1b` 714, où une paire déjà faite peut dispenser **de refaire ce contrôle** uniquement si elle couvre **exactement la même décision** ; B1b lui-même n'est requis que dans le scope `DIRECTION` et sous son déclencheur V/craft (704, 716). Une décision locale différente ne peut être exemptée par une paire visuelle valide pour une autre décision. La formulation BIBLIOTHEQUE ne répète ni l'identité exacte, ni le scope B1b : constater l'omission n'autorise pas à changer la règle propriétaire ACTION.

### Questions, modes et objet de rythme (175–199)

Les questions 179–185 relient chaque niveau à une décision visible : champ, circulation du regard, relation promesse/preuve/action, objet qui rend une promesse tangible, rythme, micro-état, comportement transversal. L'« objet de rythme » est un **rôle** porté par `OBJECT/*` (187), sans nouveau préfixe. Si aucun objet de ce rôle ne convient, il peut être omis avec justification ; cette non-sélection n'efface pas un objet de preuve nécessaire ni un gate du run. L'exemple `OBJECT/COMPARISON_SPLIT` ne rend pas automatiquement toute comparaison pertinente.

La table 193–197 module le **volume de sélection**, sans reclassifier le mode : `LITE` préserve la structure sauf vrai delta ; `ITER` ne reprend que la route touchée ; `STANDARD` cherche une décision structurante, support seulement si champ ouvert ; `DIRECTION` évalue support/grille/scène/objet de preuve, puis garde seulement les niveaux utiles ; `SYSTÈME` cible une couche partagée et son contrat avec rayon d'impact réel. Le verbe « évaluer » pour DIRECTION n'oblige pas à créer quatre routes. À confronter à F-DIR-041, où un raccourci de l'atlas peut présélectionner STANDARD à tort pour un nouvel écran. `SYSTÈME` ne se déclenche pas du seul emploi d'un token ou d'une scène : le rayon d'impact et l'objet du run restent à qualifier (F-SAV-007).

### Premier objet, observation et boucle (201–205)

Le one-shot est possible **après** composition d'un premier objet complet et observation dans le scope : thèse, spécificité, états et risques applicables doivent tenir ; ACTION conserve gates, statuts et contrôle de sortie (203). Si une relation dominante échoue, la boucle impose une modification qui touche effectivement foyer, rythme, hiérarchie, preuve, comportement ou robustesse et une nouvelle observation (205). La simple variante nominale ou la seconde version décorative n'est pas un progrès. La tension avec l'édition requise par B1b quand son déclencheur s'active reste F-DIR-009/F-ACT-025 ; elle n'est ni résolue, ni aggravée par la seule permission du one-shot ici.

### Forme dérivée, responsabilité et preuve (207–237)

Inventer une forme locale ne promeut pas une route : charger CRAFT, partir de tâche, donnée, état, conséquence, densité et preuve (209) ; garder matière/métaphore seulement si elle change la relation et passe états, accessibilité, performance et test de retrait (211). `PRINT_FIELD` est un nom historique pour matière imprimée ou générée par code CSS/SVG/masque/trame ; il ne limite pas le médium (213).

Quand les routes existantes sont insuffisantes, DERIVE commence par une responsabilité ou un héritage de départ (217–220), une contrainte produit réelle, **un levier principal**, la responsabilité préservée et une nouvelle contre-indication (221–224, 237). FIRST-OBJECT, SIGNATURE, PREVIOUS-LIMIT, conséquence observable et condition de sortie encadrent l'essai (225–229). Le scope, contenu/états, A11Y/performance **lorsque le risque les active**, type/limite de preuve, owner et prochaine preuve bornent les claims (230–234). La conséquence est **prédite avant** le premier objet, puis vérifiée ; `PROOF-TYPE` ne peut devenir un résultat positif par déclaration. Sur un premier produit sans structure antérieure, signaler l'absence de base inspectable au lieu de fabriquer une limite historique : observation déjà ouverte au bloc 2, à éprouver dans les contrats.

La liste DERIVE comporte de nombreuses étiquettes, alors que CONTRACTS 258 annonce un « contrat réduit » pour la route locale : possible charge disproportionnée, **laissée ouverte au prochain bloc** pour vérifier si cette liste est un canevas de preuve proportionné ou une obligation simultanée. Plusieurs usages **contrastés** et un gain réel sont nécessaires avant une route candidate ; son statut, sa promotion, sa maintenance et sa mémoire suivent EVOLUTION puis CHANGELOG (237). Les noms de tendance (`SCENE/BENTO`, `SCENE/GLASS_HERO`, `SCENE/EDITORIAL_PREMIUM`) sans responsabilité distinctive ne sont pas des routes durables.

### Signaux de convergence (239–252)

Les six exemples — cartes égales, hero à double CTA générique, split 50/50, logos avant la preuve, screenshot décoratif, grille répétitive — servent de **questions de reprise**, jamais d'interdictions. Une structure familière peut rester si contenu, mécanisme de preuve, geste et tâche en établissent la pertinence ; changer seulement la peau ou ajouter une scène ne démontre rien. Risque inverse à éprouver : un lecteur pressé pourrait éliminer une convention utile pour « faire original ». Le texte 241 et 252 protège explicitement contre cette lecture.

## Passage C — simulations de lecteurs

| Cas | Suite correcte | Erreur à détecter |
|---|---|---|
| Agent `LITE`, correction de libellé sans delta structurel | Hériter sans route BIB, vérifier le libellé et la preuve applicable via ACTION | Faire du `N/A` de structure un verdict général |
| Designer `DIRECTION`, première surface de marque | START puis style si actif ; évaluer les niveaux, retenir les seuls utiles ; objet complet et observation | Remplir quatre routes parce que la table les énumère |
| Reviewer, capture B1b valide pour décision V « contraste du hero », nouveau delta local sur récupération d'erreur | Appliquer la preuve adaptée à la récupération ; ne pas invoquer la paire V pour ce contrôle | Utiliser l'exception de la ligne 173 malgré l'absence d'identité de décision |
| Reviewer, paire B1b valide après dernier changement, **même** décision V et déclencheur actif | Réutiliser cette paire avec son artefact, propriétaire, scope et prochaine preuve selon ACTION | Refaire une variante inutile ou déclarer un PASS sans conclusion de la paire |
| Designer, premier objet DIRECTION solide et observé | Vérifier les gates et risques activés, puis clôturer selon ACTION si tout tient | Ajouter une itération cosmétique ; oublier B1b s'il est déclenché |
| Designer, micro-interface dense aux états erreur et focus | Charger MICRO pour décision d'état/action, observer les états et leurs limites | Employer un « objet de rythme » imaginaire pour couvrir la micro-interaction |
| Mainteneur, `SCENE/BENTO` réemployé sur trois campagnes semblables | Garder local ; chercher usages contrastés et gain démontré avant EVOLUTION/CHANGELOG | Traiter la répétition ou le nom de mode comme promotion automatique |
| Designer, split 50/50 utile à une vraie comparaison | Conserver si la relation artefact/action est démontrée dans son contexte | Interdire par réflexe un motif signalé dans la table |

Ces huit cas sont des tests de lecture **simulés**, non des expériences sur produit, agent ou utilisateurs. Les deux cas de paire B1b sont le test discriminant de portée : décision différente versus même décision et même scope.

## Passage D — résistance, constat provisoire et déduplication

### F-BIB-001 — l'exception de paire équivalente dans SELECT perd l'identité de décision et le scope B1b

- **Localisation :** `BIBLIOTHEQUE/SELECT` 171–173, surtout la seconde branche de 173 ; source propriétaire de l'exception : `ACTION/GATE-B/B1b` 704–716, surtout 714.
- **Constat :** la phrase BIBLIOTHEQUE autorise littéralement `N/A-JUSTIFIED` dès qu'une paire équivalente demeure valide après le dernier changement substantiel, mais ne demande pas qu'elle couvre **exactement la même décision** et ne borne pas cette alternative au contrôle B1b dans son scope DIRECTION. Le renvoi « selon ACTION » peut permettre une lecture correcte ; il n'empêche pas une lecture rapide de SELECT seul d'étendre cette exemption à une décision locale applicable et distincte.
- **Effet possible :** contrôle applicable contourné, preuve d'une autre décision citée comme justification N/A, puis clôture indûment favorable si ACTION n'est pas relu. **Gravité provisoire : significatif à éprouver**, sans fréquence ni incident de run attestés.
- **Test discriminant :** (a) paire initiale/après édition toujours valide pour la composition du hero DIRECTION ; nouveau delta de récupération d'erreur qui ne figure pas dans la paire : N/A sur cette base doit être refusé ; (b) paire toujours valide et couvrant exactement la même décision V sous B1b déclenché : réutilisation permise avec provenance et prochaine preuve. Tester aussi hors scope B1b. Aucun résultat machine ou humain revendiqué à ce stade.
- **Réparation candidate, à arbitrer après la lecture des propriétaires :** préciser que l'alternative de la paire vaut seulement pour **B1b déclenché et la même décision**, avec les conditions de fraîcheur et de traçabilité ACTION ; conserver la première branche pour les contrôles réellement non applicables et les contrôles applicables sans preuve à `NOT-VERIFIED`/retour selon ACTION.
- **Déduplication :** F-DIR-011/019 portent sur l'absence d'effet classée à tort N/A ; F-ACT-036 porte sur l'absence de représentation/opposabilité machine de B1b. Ici, la cause est l'**élargissement sémantique** de l'exception lors du transport vers un FAST-PATH local. Corriger ces constats ne rétablit pas nécessairement la portée de la phrase 173. L'ID reste provisoire jusqu'aux contrats et aux tests de lecture.

Les protections textuelles sont importantes : la ligne 171 exige une non-applicabilité réelle, 173 dit aussi « selon ACTION », 199 n'invente pas un statut, 203 conserve tous les gates et 237 interdit la promotion implicite. F-BIB-001 n'est **pas** la conclusion que le système prescrirait formellement d'ignorer ACTION ; il isole une interprétation dangereuse permise par un raccourci.

| Observation liée | Traitement |
|---|---|
| `DERIVE` figure dans un sous-titre de route mais le lecteur CLI ne le résout pas seul | F-DIR-028/F-ACT-001 ; tester coût d'accès et documentation des locators |
| Table par mode de SELECT contre raccourci « nouvel écran = STANDARD » | F-DIR-041 ; conserver START propriétaire du classement |
| Objet complet / one-shot contre B1b éditable | F-DIR-009/F-ACT-025 ; test de même déclencheur et état observé |
| Trace 199 mélange champs prospectifs et observation | F-DIR-003/006, F-ACT-002/030 ; examiner schéma et temporalité plus tard |
| PREVIOUS-LIMIT sans précédent ; DERIVE long versus contrat local réduit | Observations ouvertes aux contrats 256–287, sans nouvel ID |
| Objet de rythme ou signal de convergence pris pour préfixe, quota ou interdiction | Texte 187, 241, 252 apporte déjà les garde-fous ; aucun défaut autonome prouvé |

## Couverture et prochaine unité

| Passage | Profondeur | Évidence et limite |
|---|---|---|
| A — architecture | FULL | Route SELECT résolue, DERIVE inclus, interfaces et autorité situées |
| B — contrat | FULL | Lignes 161–252 lues dans l'ordre, conditions et sorties rapprochées d'ACTION/SAVOIR |
| C — usage | TARGETED | Huit scénarios contrastés ; pas de test humain ni d'effet produit mesuré |
| D — résistance | TARGETED | F-BIB-001 provisoire et test discriminant ; plusieurs points rattachés à des IDs existants |
| Machine | TARGETED | `read_route.py` et `validate_reading_map.py` ; ni projection de la trace ni validateur des preuves rejoués ici |
| Externe | N/A-JUSTIFIED | Aucune donnée externe nécessaire à l'interprétation de ce corpus interne |

Les lignes 254–255 ferment SELECT. Aucun patch ni verdict global. **Prochaine unité :** `BIBLIOTHEQUE.md` **256–287**, `CONTRACTS` ; relire protocole §12, présent rapport, F-BIB-001, les conditions de statut de route et les contrats ACTION avant d'évaluer le contrat réduit, le contrat durable, les contrôles et la preuve en contexte.
