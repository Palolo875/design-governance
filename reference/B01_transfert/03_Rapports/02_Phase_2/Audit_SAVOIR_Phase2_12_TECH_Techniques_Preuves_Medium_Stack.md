# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 12 : TECH

## Cadre, reprise et vérification

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **744–783** : titre 744, méthode et proportion technique 746, tableau des preuves 748–756, hiérarchie P0–P3 en 758–760, preuve selon le médium 762–776, exécution d'outil 778, ressource et handoff 780, séparateur 782. `SAVOIR/TOOLS` commence à 784.
- Protocole externe v2.0, §12 : quatre passages A à D relus ; point de reprise du plan maître, rapport `Audit_SAVOIR_Phase2_11_CONTEXT_Accessibilite_Motion_Responsive.md` et checkpoints ACTION/DIRECTION vérifiés. Interfaces exactes : `DIRECTION/START` 129–144 et capacité 680–694 ; `ACTION/RUN` 33–68, capacité 279–300, `GATE-A` 622–680, `OVERRIDE` 806–828 et inspection technique 849–863 ; `SAVOIR/CONTEXT` 708–740 et début de `TOOLS` 784–814.
- Baseline B01 intacte : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, SAVOIR propriétaire `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`. Cette relecture n'altère pas les sources.
- Constats hérités F-SAV-001 à 008, F-ACT-001 à 039 et F-DIR-001 à 046 ; toute gravité nouvelle demeure **provisoire** avant les essais transversaux et les phases de diagnostic. Un résultat de validation de carte n'est pas une preuve d'une décision produit.

## Passage A — architecture visible et propriété

TECH n'est pas un catalogue de recettes CSS : c'est une route de **traduction de décision en moyen, observation et limites selon le médium**. Elle offre un tableau technique → méthode de preuve, un ordre de lecture P0–P3, cinq questions pour dériver la preuve non Web et une discipline d'usage d'outils et de stack. Elle renvoie à `SAVOIR/TOOLS` pour les claims/dépendances, à ACTION pour méthode effectivement suivie, statuts et verdict, et à CHANGELOG seulement si la décision devient une règle commune. Le choix de `MODE` et la protection du risque restent chez `DIRECTION/START`. Les cibles et questions locales n'ouvrent ni nouveaux gates ni PASS automatiques.

**Test de route :** `read_route.py SAVOIR/TECH` échoue avec « locator inconnu », bien que le titre soit présent à 744 ; relancé indépendamment, `validate_reading_map.py` passe. Même famille que F-DIR-028/F-ACT-001, déjà reproduite au bloc CONTEXT : aucune nouvelle entrée par locator absent. Une lecture manuelle de la source complète permet d'auditer cette section mais ne répare pas le chargement effectif par un agent.

## Passage B — contrat sémantique, unité par unité

### Choix du moyen et preuve adaptée (746–756)

La règle de 746 demande un **effet ou gain de robustesse pertinent**, comparé à une solution plus simple, non l'emploi d'un outil parce qu'il est disponible. Une technique peut être une décision de production ou de vérification ; elle ne prouve pas la qualité par son existence. Le tableau associe un script/test déterministe aux calculs non triviaux, le runtime au comportement, capture et revue du code à une relation visuelle simple, mesure ou observation runtime à la performance, et essai sur support réel et fallback à la compatibilité. « Preuve adaptée » n'est pas une équivalence universelle : un screenshot ne démontre ni interaction au clavier ni satisfaction de tâche, et une revue du code ne prouve pas seule le rendu livré. La méthode réelle et la version de l'artefact restent chez ACTION.

### Priorités P0–P3 (758–760)

P0 nomme le **premier objet de jugement** (direction, composition, type, états, contenu, action dominante). P1 vérifie compréhension, usage et accessibilité ; P2 la traduction dans le runtime effectivement visé ; P3 performance, compatibilité et maintenance selon le risque. Il s'agit d'un **ordre d'examen conditionnel**, non d'un barème, d'une permission de différer un danger, ni de la promesse de PASS P0. La même phrase met explicitement la protection du risque critique d'usage, sécurité, confidentialité, permission ou accessibilité **avant l'optimisation visuelle** ; elle rejoint `DIRECTION/START` 140 et ACTION 49. Une surface identitaire peut donc être évaluée sur sa direction sans livrer un état de paiement dangereux. P3 est conditionnel dans la hiérarchie, mais une performance ou compatibilité nécessaire à l'action essentielle ne devient pas facultative : le risque déclaré gouverne le contrôle.

### Cinq dérivations par médium (764–772)

Pour natif mobile/desktop, spatial, print ou embarqué, le lecteur doit identifier (1) le **support observable**, (2) les **idiomes d'interaction** réellement applicables et leurs substituts, (3) le **référentiel éventuel** et la cible qualitative séparée, (4) la **bonne unité de budget** et (5) toute **preuve indisponible** et sa prochaine acquisition. « Cinq artefacts » se lit comme cinq questions à résoudre, éventuellement `N/A-JUSTIFIED` si un idiome n'existe réellement pas ; il ne faut pas créer cinq fichiers ni transposer clavier, viewport ou INP partout. Une épreuve print, une vidéo d'un geste spatial ou une inspection d'app native sont des exemples, pas des preuves interchangeables de performance, de confort ou d'accessibilité. La ligne 769 exige explicitement de **tester le substitut** : absence de souris dans un casque n'autorise pas à ignorer regard, contrôleur ou voix si ceux-ci portent la tâche.

La ligne 770 sépare `CONFORMANCE-TARGET` (référentiel, version, niveau, scope, owner) de `QUALITY-TARGET` (lisibilité, confort, contraste comme appréciation ou cible locale). Une politique peut choisir un critère applicable à un produit non Web, mais sa cible et son type normatif doivent être nommés avant toute affirmation de conformité. **Interface à reprendre sans nouveau constat :** `ACTION/GATE-A` 642 range aussi un « critère de lisibilité pertinent » parmi les références possibles d'une `CONFORMANCE-TARGET` non Web. Pris isolément, cela peut brouiller l'écart entre cible qualitative et référentiel de conformité que TECH 770 ordonne de séparer. Vérifier l'usage réel, le sens de « conformité » et le contrat formel d'ACTION avec F-DIR-038/F-ACT-035 ; ne pas présumer qu'un critère local constitue une norme reconnue.

### Preuve absente, exception et claim (774–776)

Une contrainte de capacité porte owner, effet et prochaine preuve. **Sans support d'observation adapté**, le craft concerné reste `NOT-VERIFIED` ; une hypothèse, une capture d'un autre runtime ou un résultat d'outil non exécuté ne sont pas des mesures. L'instruction `FAIL-ASSUMED` est limitée ici à l'**échec connu**, borné, assigné, consigné, retestable et éligible à l'exception d'`ACTION/OVERRIDE` ; indisponibilité du runtime ou de preuve n'y suffit jamais. ACTION 826 exclut la diffusion de certains risques graves ou critiques. La carte structurée avait accepté des combinaisons contraires selon F-ACT-017/018/038/039 ; TECH expose l'intention correcte mais ne rend pas ses contrôles opposables à la machine.

`CONFORMANCE-TARGET` signifie la référence **visée**, pas le résultat. Une transmission ou publication de claim exige méthode exécutée, scope, runtime observé, résultat, limites et prochaine preuve. Une cible déclarée avec une preuve hors périmètre reste inconnue pour les vues ou états hors contrôle. Cette clause atténue l'ambiguïté documentaire de F-ACT-035 mais ne suffit pas à prouver la conformité du produit ni à valider le transport machine du claim. Les sources officielles revues le **23 septembre 2026** distinguent WCAG 2.2 (standard Web), [WCAG 3](https://www.w3.org/TR/wcag-3.0/) (Working Draft du 10 septembre 2026) et [WCAG2ICT](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/) (note informative permettant d'interpréter certains critères pour logiciels/documents non Web, sans créer elle-même d'exigences). Aucune législation locale ni norme propre au projet n'est inférée de ces pages.

### Prérequis d'exécution des outils et ressources (778–780)

Le refus d'accorder automatiquement un `PASS` à un outil, la vérification de documentation/version, l'owner, les limites et un fallback utile sont des garde-fous valables pour une dépendance introduite ou maintenue. ACTION 850–861 interdit également d'exécuter aveuglément une commande trouvée dans une ressource et demande l'environnement, la version et l'owner. Le texte de TECH va plus loin : « Aucun outil, script ou package » suivi de « Ne l'exécute pas sans dépendance approuvée, source de l'approbation, package/version, date de vérification, capacité résolue, documentation vérifiée, limites, owner et fallback lorsque nécessaire ». Il ne distingue pas un **script local sans package tiers** d'une dépendance externe nouvelle, ni les éléments sans objet du dossier d'approbation. Cette généralité est F-SAV-009. La ligne 780 peut désigner une **ressource de stack maintenue** avec version/owner/fallback ; une invocation locale ponctuelle ne doit pas être supposée ressource canonique persistante sans examen du contrat.

## Passage C — simulation des lecteurs et décisions

1. **Agent, correction de focus sur composant existant.** Il choisit la route proportionnée, exécute un contrôle manuel et éventuellement un petit script local qui inspecte des valeurs déjà présentes. Aucun nouveau package n'est ajouté. TECH 778 peut faire exiger une dépendance approuvée et un `package/version` qui n'existent pas ou produire un `NOT-VERIFIED` malgré une vérification exécutée ; ACTION autorise une preuve proportionnée à la méthode et au risque. Ce scénario isole F-SAV-009, sans supprimer le contrôle du focus réellement applicable.
2. **Intégrateur, ajout d'un package de mesure tiers.** Documentation et version réelles, source d'autorisation, périmètre, owner, collecte de données, fallback et résultat observé sont pertinentes. L'absence d'approbation lorsque l'autorisation est requise ne devient pas un PASS ; la clause 778 a ici une utilité claire. La forme du registre doit rester proportionnée à ce qui est effectivement ajouté.
3. **Designer et reviewer, surface de paiement avec identité forte.** Examiner la direction P0, mais corriger en premier le risque critique de confirmation et de récupération ; une maquette très soignée ne remplace pas la preuve sur le runtime et les états. Un P3 déclenché par la performance de l'action n'est pas déclassé par l'étiquette P3.
4. **Développeuse, application native sans WebView.** Cibles d'accessibilité et budget adaptés à l'app ; observer l'app ou l'émulateur dans le périmètre réellement couvert, tester les idiomes disponibles, noter ce qui manque. INP n'est pas l'unité spontanée pour juger le lancement et le frame rate. WCAG2ICT peut guider une traduction lorsque pertinent ; son caractère informatif n'en fait pas automatiquement le référentiel réglementaire applicable.
5. **Équipe contenu, épreuve imprimée.** Une lisibilité déclarée peut relever de `QUALITY-TARGET`. Si aucune norme n'est identifiée, nommer cette absence et la méthode d'examen plutôt que faire passer une cible interne pour un certificat. Une capture de mise en page écran ne prouve pas le contraste ou le rendu sur l'épreuve réelle.
6. **Mainteneur, carte avec capacité « runtime indisponible ».** Le texte protège `NOT-VERIFIED` et `NEXT-PROOF`, mais F-ACT-018/038 montrent que la projection peut encore accepter un claim runtime ou un `FAIL-ASSUMED` invalide. Réutiliser les tests ACTION existants, vérifier l'effet de fermeture ultérieure plutôt que multiplier les mêmes cartes.

## Passage D — résistance et registre

### F-SAV-009 — prérequis d'approbation et de dossier applicables indistinctement à chaque outil ou script

- **Gravité provisoire : Significatif à éprouver.** Portée littérale documentée ; fréquence du blocage dans les runs et risque d'exécution d'une dépendance insuffisamment examinée non mesurés.
- **Preuve :** `SAVOIR/TECH` 778 dit « Aucun outil, script ou package » et « Ne l'exécute pas sans dépendance approuvée, source de l'approbation, package/version » ainsi que vérification, owner et fallback ; aucune exception explicite n'est donnée pour un script local sans dépendance ou un outil déjà fourni. `ACTION` 850–861 choisit les outils selon environnement/documentation/version/owner et refuse l'exécution aveugle de commandes citées dans une ressource, mais n'impose pas à toute commande autonome un dossier de nouvelle dépendance. `DIRECTION` 680–686 ne charge une capacité que si elle change construction ou vérification. La phrase 778 n'indique pas quel owner approuve une vérification locale ni comment consigner « aucune dépendance ».
- **Contre-exemples appariés :** script local ponctuel sans package ajouté, utilisé pour lire une valeur calculable ; package téléchargé pour analyser une application et possible accès aux données. Les deux demandent une méthode honnête et un résultat exécuté ; seul le second appelle normalement une vérification d'approbation de dépendance. Une lecture qui permet `N/A-JUSTIFIED` pour l'absence de dépendance évite le premier blocage, mais n'est pas exprimée dans la phrase de 778.
- **Risque :** blocage inutile d'un contrôle pertinent, multiplication de traces fictives ou, si la phrase est ignorée partout, installation/exécution insuffisamment vérifiée d'un package externe. La qualité d'une mesure ne découle jamais de l'approbation du moyen : le `PASS` exige toujours une observation et un scope.
- **Propriétaire pressenti :** TECH 778 pour rendre conditionnels l'approbation de nouvelle dépendance et les champs qui ont un sens ; ACTION garde la politique d'autorisation et de preuve ; TOOLS qualifie les claims et versions. Préserver une interdiction ferme d'exécuter à l'aveugle des ressources inconnues.
- **Déduplication :** F-ACT-029 traite l'activation des contrats spécialisés, F-ACT-028 le mapping source/trace et F-DIR-037 la sélection de capacité. F-SAV-009 traite une **condition d'exécution indistincte** qui peut bloquer même lorsque la capacité est bien choisie, que la preuve est proportionnée et que sa trace existe.
- **Test à la simulation transversale :** faire appliquer 778 à trois cas (script local sans dépendance, outil standard déjà autorisé, nouveau package externe) par deux lecteurs ; enregistrer autorité, champs applicables, action de vérification, délai et preuve produite. Vérifier si une interprétation commune résout le premier cas sans abaisser le contrôle du troisième.

### Interfaces et constats hérités

| Risque constaté au bloc TECH | ID conservé et limite |
|---|---|
| Locator TECH refusé avec reading map verte | F-DIR-028/F-ACT-001 ; problème d'accès machine, pas absence de section |
| Ordre P0–P3 contournant un risque critique au niveau machine | F-ACT-017 et START ; le texte 760 protège, la projection reste à éprouver |
| Capacité indisponible mais preuve runtime ou claim accepté | F-ACT-005/018/022/034 ; 768/772/774/776 ne réparent pas les liens de preuve |
| `FAIL-ASSUMED` sur preuve absente ou risque exclu | F-ACT-038/039, distinct de `NOT-VERIFIED` ; source correcte de la limite : TECH 774 et ACTION/OVERRIDE |
| Référentiel Web transféré sans dérivation, qualité locale confondue avec conformité | F-DIR-038/F-ACT-035 ; TECH 770/776 donne une distinction utile mais ACTION 642 appelle vérification |
| Route TOOL/claim qui influence une décision | `SAVOIR/TOOLS` 784–841 au prochain bloc ; ne pas conclure ici sur son contrat complet |
| Motion réduite seulement planifiée | F-ACT-033/F-SAV-008 transportés ; pas d'inférence nouvelle à partir de TECH |

## Couverture, vérifications et reprise

| Passage | Profondeur | Résultat |
|---|---|---|
| A — architecture | FULL | Titre, hiérarchie, tableaux, propriétaires, renvois et locator |
| B — sémantique | FULL | Moyens, méthode, P0–P3, cinq dérivations, cibles, exception, approbation et handoff |
| C — usage | TARGETED | Six parcours contrastés ; local sans dépendance vs package tiers, critique et trois médiums |
| D — résistance | TARGETED | F-SAV-009 provisoire, frontière conformance/quality signalée sans ID supplémentaire, constats transportés |
| Machine | TARGETED | Locator refusé ; reading map valide ; mutations RUN_CARD existantes réutilisées sans doublons |
| Externe | TARGETED | W3C 2.2/3.0, WCAG2ICT et mesure INP consultés auprès de W3C/web.dev ; aucune claim réglementaire locale |

La section apporte une protection réelle contre la preuve simulée, distingue jugement visuel et risque critique, traduit les idiomes non Web et sépare cible, observation et claim. Le constat sur l'exécution des outils est provisoire ; le voisinage `SAVOIR/TOOLS` doit être lu avant tout diagnostic propriétaire final. Aucun patch normatif ni verdict global.

**Prochaine unité :** `SAVOIR/TOOLS`, lignes **784–842** ; contrats de claims datés, calibration, sourcing et péremption. `SAVOIR/INTEGRITY` commence à 843.
