# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 10 : SYSTEM, tokens et composants

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **690–707** : titre (690), obligation token/primitive (692), comportement et reclassification (694), autorités (696), consumers, modes, interopérabilité et trace (698), stack et primitives (700–702), contrat du composant partagé et handoff (704), séparateur 706. `SAVOIR/CONTEXT` commence à 708.
- Protocole externe v2.0 §12, passages A–D ; plan maître, rapport STYLE bloc 9, checkpoints DIRECTION/ACTION et constats F-SAV-001 à F-SAV-006 relus. Interfaces exactes : `DIRECTION/START` 129–144 et DAILY 253–257 ; `SAVOIR/ROUTING` 66–82 et ATLAS 534–541 ; `ACTION/RUN-SYSTEM` 379–387, CLOSE-PACKAGE 391–405 et ROUTING 870–887 ; `BIBLIOTHEQUE/SELECT` 191–199, COMPONENTS 611–655 et EVOLUTION 763–772 ; transport RUN_CARD déjà testé dans ACTION.
- Baseline B01 stable : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Étendue de la preuve : lecture normative et parcours simulés, sans token exécuté ni migration observée dans un vrai produit. Les constats sont provisoires et aucun fichier source du système n’est modifié.

## Résultat local

La section apporte un vrai contenu de jugement spécialisé : distinguer valeurs primitives et rôles sémantiques, examiner plusieurs consumers et thèmes, utiliser la stack existante de façon consciente, séparer primitive accessible et identité, et définir un contrat de composant qui comporte états, responsive, compatibilité et baseline de rendu. Elle attribue correctement la structure détaillée à BIBLIOTHEQUE et la preuve/issue à ACTION. Sa présence **confirme F-SAV-004** : l’ATLAS oublie une route nécessaire alors que `SAVOIR/SYSTEM` est explicitement propriétaire des questions que la cellule « Structure / composant » ne couvre pas.

Une contradiction de portée supplémentaire apparaît en ligne 694, **F-SAV-007 provisoire** : « Reclassifie en SYSTÈME lorsqu’un token, composant, convention, format ou comportement affecte plusieurs consumers, plusieurs surfaces ou une source de vérité partagée » peut substituer SYSTÈME à un run DIRECTION dont le changement partagé n’est qu’une conséquence. `DIRECTION/START` 131 et 138 n’applique SYSTÈME comme mode direct que si la **décision partagée est l’objet du run** ; si elle naît d’une direction, il mène la direction d’abord, puis un run système dépendant, sauf décisions inséparables. SYSTEM 696 reconnaît la primauté de START, ce qui atténue l’écart sans résoudre l’impératif inconditionnel de 694. L’incidence pratique demande un parcours lecteur.

## Passage A — architecture visible

| Ligne(s) | Rôle et forme | Owner / sortie |
|---|---|---|
| 690–692 | Titre stable et tag `[REQUIS PAR LE MODULE — blast radius partagé, token ou primitive]` | Jugement SAVOIR : valeur primitive versus rôle sémantique ; obligation si scope activé, pas mode imposé par le tag |
| 694–696 | Exiger comportement au-delà du nom ; « reclassifie » puis précision d’autorité | START classe ; ACTION exécute ; SAVOIR doit signaler le blast radius sans se substituer à START |
| 698 | Plusieurs consumers, source de vérité, modes, format interopérable, migration/rollback et trace | Distinguer thèmes/états de modes de run ; décider si interopérabilité change la décision avant de l’imposer |
| 700–702 | Stack existante, primitive accessible, pas de kits concurrents gratuits | Capacité/maintenance sans sacrifier accessibilité, identité ou justification de migration |
| 704–707 | Contrat partagé, BIBLIOTHEQUE pour structure, ACTION pour preuve/verdict, fin de section | Anatomy/variants/états/tokens/compatibilité/base de rendu puis observation, migration et clôture pertinentes |

Le titre et l’obligation sont présents dans le source, mais `read_route.py SAVOIR/SYSTEM` refuse la clé ; `validate_reading_map.py` annonce pourtant la carte valide. C’est une occurrence supplémentaire **F-DIR-028/F-ACT-001**, sans nouvel ID de locator. Le lecteur doit suivre le titre dans SAVOIR, puis la route d’ACTION propriétaire.

## Passage B — contrat sémantique, phrase par phrase

### Tag spécialisé et distinction des tokens (690–692)

Le tag rend la séparation primitive/sémantique applicable lorsque la responsabilité token ou primitive est en jeu : une valeur comme une couleur ou un espacement n’est pas à elle seule le rôle `danger`, `texte` ou `action`. Un token purement local peut nécessiter ce jugement sans devenir automatiquement un run SYSTÈME : le tag porte le **scope de la méthode**, START demeure l’autorité de mode. Le changement d’un token global utilisé par plusieurs produits ou surfaces appelle, en revanche, consumers, thèmes, états, migration et non-régression selon son blast radius. Ce cas justifie la route principale de `SAVOIR/ROUTING` 78 et montre pourquoi son absence de la cellule ATLAS 541 reste **F-SAV-004**.

### Comportement et condition de reclassification (694–696)

Exiger le comportement du token/composant est positif : un contrat qui ne contient que noms et couleurs échoue face aux états, contrastes, thèmes et consumers. La formule de reclassification énumère **l’extension de l’impact** (« affecte plusieurs surfaces »), tandis que START 131/138 examine **l’objet de la décision** et l’ordre des runs. Les deux questions ne sont pas équivalentes. Une nouvelle direction de marque peut déboucher sur un token `brand-action` partagé : elle réclame bien une décision système sur le token, mais ne remplace pas automatiquement le mode du travail créatif initial. Si le token partagé était l’objet direct depuis le départ, START conduit directement à SYSTÈME ; si les deux décisions sont inséparables, START prévoit un arbitrage explicite. SYSTEM 696 dit que START classe, ce qui permet à un lecteur averti de respecter l’ordre, mais 694 n’expose pas la distinction. C’est F-SAV-007, limité à cette instruction locale.

### Consumers, interopérabilité et trace (698)

Le format interopérable est **à évaluer**, pas obligatoire pour un dépôt local sans consumer supplémentaire. « Modes » désigne ici les variations du système de design (p. ex. thèmes) ; il ne crée pas des valeurs de `MODE` dans ACTION. Une décision système documente impact, rôle sémantique, thème, owner, consumers, migration, rollback, fallback, maintenance et méthode/scope/résultat/limite de non-régression. Ces champs ne sont pas tous des propriétés JSON autonomes de RUN_CARD : la carte peut pointer vers une trace ou un manifeste résoluble. Le validateur ne contrôle pas actuellement consumers/migration/rollback/non-régression en mode SYSTÈME : **F-ACT-015/021** et F-ACT-002 restent ouverts. Reprendre l’épreuve machine déjà exécutée dans ACTION plutôt que multiplier des mutations identiques.

La baseline de rendu, la version du token, les supports testés et la preuve après migration doivent être alignés : une capture antérieure ne prouve pas le thème, l’état ou le consumer livré après changement. Les limites déjà identifiées **F-ACT-022/031** persistent ; la simple énumération d’un « scope de non-régression » n’est pas une observation exécutée.

### Stack, primitives et contrat du composant (700–704)

« La stack existante prime » se lit avec les exceptions exprimées : accessibilité, capacité à adapter tokens/états et migration justifiée. Il ne faut pas ajouter un kit par mode ni changer de fondation par goût ; une primitive accessible assure des gestes et une sémantique de base sans dicter toute la direction. Aucun conflit autonome n’est établi avec BIBLIOTHEQUE/COMPONENTS : cette dernière définit couches, anatomie et graphe de dépendance, tandis que SYSTEM juge rôles sémantiques, thèmes, source de vérité et conséquences de conception. ACTION exécute le run, observe le résultat et clôt ; CHANGELOG porte la décision de cycle de vie de la route, pas un PASS technique.

La ligne 704 exige pour un composant partagé intention, anatomie, variants utiles, états, responsive, tokens, frontières de composition, baseline de rendu, source de vérité, owner, compatibilité et prochaine revue. « Variants utiles » n’est pas un quota et une baseline déclarée n’est pas une capture fraîche. La structure du contrat est propriétaire BIBLIOTHEQUE ; preuve de gain, usage contrasté ou promotion de route sont examinés selon EVOLUTION/CHANGELOG, et la qualité de l’objet ne se déduit pas du nombre de consumers.

## Passage C — parcours réels simulés

1. **Mainteneur, token `danger` partagé Web et mobile.** La décision directe est le rôle et la valeur du token ; START classe SYSTÈME, SAVOIR/SYSTEM traite primitive/sémantique et thèmes, BIBLIOTHEQUE la couche réellement affectée, ACTION les consumers, migration et preuves de non-régression. Aucun formulaire STYLE n’est requis sans décision d’expression nouvelle.
2. **Designer, première scène de marque et token partagé induit.** La décision initiale porte sur la direction de l’identité. SAVOIR/SYSTEM 694 peut sembler exiger de remplacer ce run par SYSTÈME dès qu’un token devient partagé ; START 138 dit direction d’abord puis run système dépendant, sauf inséparabilité. La séparation protège à la fois la créativité et la migration (F-SAV-007).
3. **Intégrateur, variable locale d’une seule vue.** Il distingue token primitif et rôle sémantique si pertinent, mais un nom `--space-local` sans dépendance partagée n’ouvre pas automatiquement migration, CHANGELOG et rollback multi-consumers. La classification reste celle de START, sauf risque critique ou changement de scope.
4. **Équipe produit, primitive de consentement critique.** Même si l’implémentation paraît locale, START 140 reclassifie hors LITE/ITER si le changement affecte action/état/sémantique/permission ; le mode exact dépend du blast radius. Ni « token » seul ni « un composant » seul ne décide de la protection de ce risque.
5. **Reviewer, carte SYSTÈME clôturée.** La prose demande thème, source de vérité, consumers et non-régression ; la validation JSON peut passer sans ces détails structurés. Il suit la trace et les preuves exécutées, ne confond pas l’acceptation de la projection et la migration sûre (F-ACT-015/021/031).
6. **Agent arrivant par ATLAS.** La cellule « Structure / composant » le mène à BIBLIOTHEQUE et ACTION pour un composant partagé, mais omet SYSTEM ; la présente section démontre que sémantique, modes de thème et interopérabilité ne sont pas entièrement couverts par ces deux routes (F-SAV-004).

## Passage D — résistance et registre

### F-SAV-007 — reclassification SYSTÈME fondée sur l’impact sans distinguer l’objet direct du run

- **Gravité provisoire : Significatif à éprouver.** Divergence de critère textuelle confirmée, conséquence réelle non observée.
- **Preuve :** SAVOIR/SYSTEM 694 ordonne « Reclassifie en SYSTÈME » dès qu’un token/composant/format affecte plusieurs consumers, surfaces ou une source de vérité partagée ; `DIRECTION/START` 131 requiert que la décision partagée soit **l’objet direct** et 138 prévoit explicitement une direction en premier puis un SYSTÈME dépendant lorsque le changement partagé en découle. SYSTEM 696 reconnaît l’autorité de START sans qualifier le « Reclassifie » de 694.
- **Scénario discriminant :** un run conçoit une identité nouvelle et aboutit à un token réutilisable sur plusieurs surfaces. Lecture de 694 seule : reclasser le run entier SYSTÈME. Lecture de START 138 : conserver la décision DIRECTION et ouvrir la migration SYSTÈME dépendante, sauf si décisions réellement inséparables. Contrôle opposé : si le brief initial est de modifier le token partagé pour plusieurs consumers, START classe directement SYSTÈME.
- **Risque :** perdre la thèse et la preuve de direction en remplaçant le run créatif, ou fusionner migration et direction sans owner/condition de sortie distincts ; inversement, conserver un seul run DIRECTION sans la preuve SYSTÈME serait aussi incorrect.
- **Atténuation :** SYSTEM 696 rappelle expressément la primauté de START et DIRECTION/DAILY 257 dirige vers SYSTEM ; un lecteur qui consulte les deux sources peut conserver deux décisions liées.
- **Propriétaire pressenti :** SAVOIR/SYSTEM 694 pour limiter son impératif à la remontée du signal vers START ; DIRECTION/START reste la source de classification et ACTION celle des runs, liens et clôtures. Aucune nouvelle valeur MODE.
- **Relations sans fusion :** F-DIR-007 concerne le fix local critique sous-classé ; F-ACT-011 manque origine/destination d’un `RECLASSIFIED` ; F-ACT-015/021 perd les minima machine de SYSTÈME. F-SAV-007 porte la **substitution d’un run DIRECTION par un SYSTÈME en raison d’une conséquence partagée** et demeure même si les champs machine transportent correctement la transition. F-SAV-004 concerne l’accès à la route SYSTEM par l’ATLAS, autre mécanisme.
- **Test futur :** comparer trois briefs identiques sauf objet direct (identité avec token induit ; token partagé direct ; identité et migration inséparables), plus delta local et composant critique. Faire classer depuis START puis lire SYSTEM 694 ; noter mode, ordre des runs, owner, preuve, consumers et issue. Vérifier que le troisième cas arbitre sans inventer un mode hybride.

### Constats rééprouvés sans nouvel ID

| Observation | Constat et suite |
|---|---|
| Route SYSTEM absente du tableau ATLAS mais possédant le jugement tokens/composants | **F-SAV-004 confirmé dans son objet** ; test réel de lecture encore à faire |
| Tag token/primitive et routes multiples vs plafond implicite zéro/une/deux routes | F-SAV-001 ; charger selon chaque décision/risk utile, sans ouvrir toute la bibliothèque |
| Statut `RECLASSIFIED` sans origine/destination machine, même si mode est bien choisi | F-ACT-011 ; ne pas confondre avec F-SAV-007 |
| Contrat SYSTÈME exige impact, consumers, migration, rollback et preuve, carte générique acceptée | F-ACT-002/015/021 ; test ACTION antérieur conservé |
| Baseline de rendu, fraîcheur, portée et non-régression après migration | F-ACT-022/031 ; vérifier version source vs artefact réellement livré |
| Token d’action critique local : protection de niveau et contrôle applicable | F-DIR-007/F-ACT-017 ; risque prioritaire sur étiquette « local » |
| Route présente mais locator CLI refusé malgré carte verte | F-DIR-028/F-ACT-001 ; ajouter fixture au contrôle futur |
| Token, couleur ou composant ne démontre pas à lui seul style observé | F-SAV-005/006 ; ne pas faire de SYSTEM une source de verdict esthétique |

## Vérifications, protections et reprise

Les hashes B01 restent identiques. `read_route.py SAVOIR/SYSTEM` refuse la route, `validate_reading_map.py` passe ; le titre source est consultable directement. Aucune mutation RUN_CARD répétée : ACTION a déjà validé une carte SYSTÈME sans consumers/migration/rollback/non-régression, et la présente lecture n’ajoute pas un comportement machine distinct. La confrontation de 694 à START 131/138 est une preuve de divergence textuelle ; il reste à mesurer si elle induit effectivement un classement erroné en run.

1. Le tag spécialisé rend le jugement de tokens applicable sans décider seul du mode.
2. Un token primitif et son rôle sémantique sont distincts ; états et thèmes se jugent chez les consumers.
3. SOURCE, SYSTEM, BIBLIOTHEQUE et ACTION possèdent des décisions différentes et ne se remplacent pas par une liste de fichiers chargés.
4. La stack existante est un point de départ avec accessibilité, compatibilité et migration comme critères réels.
5. Les primitives accessibles protègent les gestes sans homogénéiser toute identité ou tout type de surface.
6. Versions, baseline, fallback, owner et prochaine revue rendent le contrat partagé réexaminable ; la preuve exécutée dépend du scope et de la version livrée.

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | Tag, sept paragraphes normatifs, owners, route refusée |
| B — sémantique | FULL | Token local/partagé, critère de mode, trace, stack, composant |
| C — usage réel | TARGETED | Six rôles/scénarios, dont objet direct contre conséquence partagée |
| D — résistance | TARGETED | F-SAV-007 provisoire, F-SAV-004 confirmé dans sa portée, huit occurrences reliées |
| Machine | TARGETED | Locator refusé et carte dérivée verte ; test de carte SYSTÈME déjà disponible dans ACTION |
| Externe | N/A-JUSTIFIED ici | Aucun claim empirique de stack ou standard externe nécessaire pour cette lecture |

Bloc 10 terminé sans patch ni verdict global. **Prochaine unité : `SAVOIR/CONTEXT`, lignes 708–743**, accessibilité, contextes critiques, responsive, motion et preuve; `SAVOIR/TECH` commence à 744. Repartir du §12, de B01 et des réserves medium/accessibilité, en gardant F-SAV-007 pour les interfaces de classement.
