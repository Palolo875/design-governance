# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 3

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 245–312 de la reconstruction de travail
- Sections : `DIRECTION/DAILY`, `DIRECTION/FAST-PATH`, `DIRECTION/EXTERNAL-START` et traduction humaine minimale de `START`
- Interfaces vérifiées : `ACTION/HANDOFF`, `ACTION/FAST-PATH`, `ACTION/RUN_CARD`, `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`, `ACTION/PIPELINE-DIRECTION`, `DIRECTION/FIRST-OBJECT`, `DIRECTION/VISUAL_TARGET`, carte interne et README
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, matrice de clôture par mode, simulation de lecture rapide et reprise des constats antérieurs
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les deux empreintes correspondent à B01. Les constats F-DIR-001 à F-DIR-012 ont été repris lorsqu’une façade de ce bloc les confirme, les corrige ou les aggrave.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 245–261 | Réduire le chargement quotidien selon le mode et le risque | `START` demeure l’entrée ; chargement conditionnel ; atlas non automatique ; responsabilités rappelées | La clôture résumée perd des champs canoniques ; LITE ne peut pas évoluer vers ITER ; le risque critique reproduit le trou de classification |
| 263–274 | Exécuter un delta court sans rituel | Quatre questions décisionnelles nettes ; condition d’arrêt utile ; sémantique N/A correcte | Owner rendu conditionnel ; abandon d’une décision absent de `DECISION-CHANGE` |
| 278–298 | Activer V1 sur brief vague dans un contexte externe | Vérité en premier ; refus du faux réalisme ; modules conditionnels ; proposition principale plutôt qu’un catalogue | `FIRST-OBJECT` précède encore la direction ; checkpoint humain non rendu visible ; ordre « avant navigation/cartes » trop absolu |
| 300–312 | Traduire l’entrée pour une personne non spécialiste | Questions compréhensibles ; anti-direction, preuve, condition d’arrêt et owner conservés | Le risque dominant et le périmètre ne sont pas explicitement traduits alors qu’ils déterminent mode et preuve |

## Passage A — architecture visible

Le bloc contient quatre façades destinées à simplifier l’entrée : une table quotidienne par mode, un chemin court, une activation pour brief vague et une traduction humaine. Chacune affirme ne pas créer de nouveau contrat. C’est une bonne architecture d’intention : l’utilisateur ne devrait pas relire tout le corpus pour chaque run.

Le problème n’est donc pas l’existence de ces vues, mais leur dérive par rapport aux propriétaires qu’elles résument. Trois types de dérive sont visibles :

1. **réduction de contenu** : la colonne « clôture minimale » de `DAILY` omet des éléments requis par `ACTION/CLOSE-PACKAGE` ;
2. **réduction de routage** : le passage de LITE à un mode plus riche omet ITER ;
3. **réduction sémantique** : `FAST-PATH` rend l’owner conditionnel et ne cite que les décisions modifiées ou confirmées, alors qu’ACTION inclut aussi une décision abandonnée.

`EXTERNAL-START` réintroduit aussi l’ordre causal déjà contesté : `FIRST-OBJECT` apparaît en position 2, puis `DIRECTION` en position 3. Le titre `RUN-PRIORITY` peut être lu comme une priorité et non comme une séquence stricte, mais le bloc est numéroté et placé « avant le premier code ou le premier rendu ». Pour un agent externe utilisant précisément cette façade portable, l’ordre apparent est opératoire.

## Passage B — contrat sémantique

### DIRECTION/DAILY

Les lignes 247, 249 et 261 établissent trois garde-fous solides : commencer par `START`, ne charger que ce qui peut changer la décision, et laisser `ACTION` posséder preuve, gates, statuts, verdicts et clôture. Ces garde-fous réduisent la gravité des omissions locales, mais ne les annulent pas : une table intitulée « clôture minimale » reste une instruction exécutable.

#### Matrice de dérive de clôture

| Mode | Élément exigé par `ACTION/CLOSE-PACKAGE` mais absent de `DAILY` | Autre dérive |
|---|---|---|
| LITE | verdict ; `DECISION-CHANGE` ou `N/A-JUSTIFIED` | aucune précision que l’alternative « réserve ou prochaine action » reste la même que dans ACTION |
| ITER | risque restant ; prochaine action ; décision | `DAILY` ajoute une réserve mais ne remplace pas les champs omis |
| STANDARD | verdict ; prochaine action | aucune |
| DIRECTION | artefact explicite ; revue créative ; `creative close` ; verdict ; prochaine preuve | « statut » ne distingue pas `state`, `issue`, `direction_status` et `verdict` |
| SYSTÈME | décision ; verdict ; entrée CHANGELOG | aucune |

Cette dérive est systématique : les cinq lignes omettent au moins un élément du paquet canonique. La ligne 249 dit que `DAILY` n’est pas une seconde source de vérité, mais l’utilisateur pressé est précisément celui qui risque d’appliquer la colonne sans rouvrir `CLOSE-PACKAGE`.

La route LITE présente un second problème. Lorsque le changement dépasse le micro-delta, elle autorise seulement une reclassification vers `STANDARD`, `DIRECTION` ou `SYSTÈME`. Or `START` définit `ITER` comme la retouche d’une surface existante dont la direction est retrouvable. Un correctif local qui s’étend sans devenir un nouvel écran, une nouvelle identité ou une règle partagée doit pouvoir devenir ITER. Son omission produit un saut inutile ou une classification fausse.

Le traitement du risque critique reproduit F-DIR-007. La phrase « si un risque critique apparaît, reclassifie » ne donne toujours aucun mode honnête pour une correction locale critique non partagée. La liste selon laquelle contraste, focus ou état « restent locaux » peut en outre être lue comme absolue, alors que ces propriétés peuvent toucher un parcours critique ou un composant partagé. Le contrat devrait séparer portée du changement et niveau de protection, ou définir explicitement le mode cible.

### DIRECTION/FAST-PATH

Les quatre questions correspondent bien à `ACTION/FAST-PATH`. La quatrième fournit une vraie condition d’arrêt et évite une procédure sans conséquence. La ligne 274 reprend aussi la bonne sémantique : `N/A-JUSTIFIED` n’est disponible que lorsqu’aucun contrôle ou aucune décision applicable ne peut changer. Cela constitue une formulation correcte à réutiliser pour corriger F-DIR-011 ailleurs dans DIRECTION.

Deux écarts subsistent.

Premièrement, la réponse attendue sur le risque demande un owner « si nécessaire ». ACTION exige qu’une sortie de run rende l’owner résoluble, la `RUN_CARD` le requiert, et chaque run conserve un owner de décision finale. L’owner peut être hérité ou déjà connu, mais il ne devient pas facultatif pour autant.

Deuxièmement, la ligne 274 rend `DECISION-CHANGE` obligatoire seulement lorsqu’une décision de production a été « modifiée ou confirmée ». ACTION définit ce champ pour une décision changée, confirmée **ou abandonnée**. L’abandon est une conséquence réelle du run ; l’omettre affaiblit la mémoire et peut faire passer une décision rejetée pour une absence de conséquence.

### DIRECTION/EXTERNAL-START

La section possède plusieurs protections fortes à préserver : elle n’ajoute ni mode ni trace ; les modules ne s’activent que s’ils peuvent modifier une décision distincte ; les claims non observés sont retirés, sourcés ou marqués ; le faux réalisme et le dashboard décoratif sont des `NO-GO` ; l’utilisateur reçoit une proposition principale au lieu d’un catalogue de variantes.

L’ordre numéroté reste toutefois incohérent avec la majorité des contrats déjà lus. Il place `FIRST-OBJECT` avant `DIRECTION`, tandis que la table d’activation, QUICKSTART, READING_MAP et `ACTION/PIPELINE-DIRECTION` demandent une cible ou une spec avant le build. `DIRECTION/FIRST-OBJECT` déclare lui-même référencer `VISUAL_TARGET`. Ce bloc renforce donc F-DIR-001 et révèle une dépendance presque circulaire : la cible définit l’objet de preuve, mais la façade demande de matérialiser cet objet avant de retenir la direction.

La phrase « avant les bénéfices, la navigation, les cartes ou le polish » est trop générale. Écarter des cartes ou une navigation génériques avant le mécanisme est sain. Interdire littéralement navigation ou cartes avant l’objet de preuve ne l’est pas lorsque le mécanisme principal est précisément une navigation, une carte de contenu, un explorateur, une liste de résultats ou un tableau. Le défaut est pour l’instant classé comme sur-contrainte à tester : la règle peut être sauvée en visant les éléments génériques ou décoratifs plutôt que les formes elles-mêmes.

Enfin, « la personne reçoit directement une proposition principale » ne mentionne pas le checkpoint interactif requis avant build lorsque l’autonomie DIRECTION n’est pas explicite. La section n’ordonne pas formellement de contourner ce checkpoint et rappelle qu’elle n’est qu’une vue ; la contradiction n’est donc pas encore confirmée. Mais une façade destinée à un agent externe peut raisonnablement être suivie seule. L’absence du checkpoint crée un risque d’exécution avant décision humaine, à vérifier lors de l’audit du pipeline et des modes d’autonomie.

### Traduction humaine minimale

La traduction réussit à convertir plusieurs termes internes en questions simples : intention, premier objet, spécificité, refus et preuve. Elle conserve aussi owner et condition d’arrêt dans la dernière ligne.

Elle affirme cependant reformuler « les mêmes décisions » que `START`, sans question explicite sur le risque dominant ni sur le périmètre touché. Or le risque détermine la preuve et peut modifier la protection ; le scope distingue notamment LITE, ITER et SYSTÈME. Ces informations peuvent être inférées par l’agent, mais la traduction ne dit pas à la personne qu’elles doivent être clarifiées. Le défaut de couverture est textuellement confirmé ; son impact sera à éprouver sur un brief non spécialiste contenant un risque caché ou un blast radius partagé.

## Passage C — usage simulé

### Agent sous forte contrainte de temps

L’agent ouvre `DAILY`, choisit LITE et suit la colonne de clôture. Il peut livrer artefact, risque, axes et prochaine action sans verdict ni `DECISION-CHANGE`. La vue lui dit pourtant qu’il s’agit de la clôture minimale. Le garde-fou « ACTION reste propriétaire » ne garantit pas qu’il rouvrira `CLOSE-PACKAGE`, surtout puisque `DAILY` est conçu pour éviter les lectures réflexes.

Si le correctif LITE s’étend sur plusieurs parties d’une surface existante, l’agent ne voit pas ITER dans les destinations autorisées. Il choisira STANDARD, restera abusivement LITE ou retournera à START sans indication de route.

### Agent externe sur brief vague

L’agent protège d’abord la vérité, ce qui est positif. Il peut ensuite prendre la numérotation au pied de la lettre et construire un premier objet avant d’avoir fixé la cible ou obtenu le checkpoint. Si le produit est un explorateur ou un hub de contenu, il peut aussi éviter artificiellement navigation et cartes alors qu’elles constituent le mécanisme.

### Personne non spécialiste

Les cinq questions sont plus compréhensibles que les labels internes. Une demande telle que « corriger ce bouton de consentement » peut toutefois être traduite sans question explicite sur la criticité, les données touchées ou la portée partagée. Le système dépend alors entièrement de l’inférence de l’agent pour choisir la protection.

### Reviewer et mainteneur

Le reviewer peut voir un paquet quotidien apparemment complet qui ne comporte pas le verdict ou la décision. Le mainteneur doit arbitrer entre le libellé local « statut » et les quatre champs séparés d’ACTION. Les façades simples deviennent donc une source de divergence documentaire malgré leur clause de non-autorité.

## Passage D — constats

### F-DIR-013 — la clôture de DAILY est incomplète face au paquet canonique

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : lignes 251–257 contre `ACTION/CLOSE-PACKAGE` lignes 391–405 et `ACTION/HANDOFF` lignes 23–33
- Risque : clôture présentée comme minimale sans verdict, décision, prochaine action/preuve, creative close ou CHANGELOG selon le mode
- Facteur atténuant : lignes 249 et 261 déclarent ACTION propriétaire et `DAILY` non normative
- Propriétaire pressenti : ACTION pour le paquet ; DIRECTION pour l’alignement exact de la vue
- Test futur : matrice automatique ou éditoriale vérifiant qu’aucune façade ne retire un champ canonique requis

### F-DIR-014 — la reclassification depuis LITE omet ITER

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : ligne 253 autorise seulement STANDARD, DIRECTION ou SYSTÈME ; `START` et la section 0 définissent ITER pour une retouche de surface existante à direction retrouvable
- Risque : surcharge en STANDARD, maintien abusif en LITE ou mauvaise description d’une retouche élargie mais non identitaire et non partagée
- Propriétaire pressenti : DIRECTION/START et façade DAILY
- Test futur : micro-delta qui devient retouche multi-zone sans changement de direction

### F-DIR-015 — FAST-PATH exclut l’abandon de la sémantique de DECISION-CHANGE

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau textuel**
- Preuve : ligne 274 cite seulement « modifié ou confirmé » ; ACTION définit « changée, confirmée ou abandonnée »
- Risque : décision rejetée non persistée, confusion avec une absence de conséquence ou un N/A
- Propriétaire pressenti : ACTION pour la sémantique ; DIRECTION pour la reproduction fidèle
- Correction probable à éprouver : reprendre la triade canonique sans la reformuler

### F-DIR-016 — la traduction humaine ne rend pas le risque dominant explicite

- Gravité provisoire : **Significatif / à éprouver**
- État : **défaut de couverture confirmé, impact à mesurer**
- Preuve : lignes 302–310 contre l’entrée minimale de START et le rôle du risque dans la classification et la preuve
- Risque : sous-classification d’un brief non spécialiste, surtout pour données, permission, accessibilité, santé, sécurité ou portée partagée
- Propriétaire pressenti : DIRECTION/START
- Test futur : briefs courts non spécialistes avec risque critique latent et blast radius latent

### F-DIR-017 — EXTERNAL-START ne rend pas visible le checkpoint pré-build

- Gravité provisoire : **Observation à risque**
- État : **ouvert**
- Preuve : lignes 282–298 contre le checkpoint interactif des lignes 722 et `ACTION/PIPELINE-DIRECTION` lignes 499–505
- Risque : un agent externe livre directement un build ou une proposition matérialisée sans autonomie explicite ni décision humaine
- Facteur atténuant : la vue se déclare dérivée et ne supprime pas formellement le checkpoint
- Prochaine vérification : scénarios agent externe avec et sans autonomie explicite ; lecture des instructions d’activation de la skill

### F-DIR-018 — priorité du premier objet formulée comme interdiction de formes légitimes

- Gravité provisoire : **Observation / à tester**
- État : **ouvert**
- Preuve : lignes 288–289 placent l’objet de preuve avant navigation et cartes sans qualifier ces éléments de génériques ou décoratifs
- Risque : mécanisme principal dénaturé lorsque la preuve est justement une navigation, une collection, une carte de données ou un explorateur
- Propriétaire pressenti : DIRECTION/FIRST-OBJECT
- Test futur : hub éditorial, explorateur de fichiers, carte interactive, moteur de recherche et dashboard opérationnel non décoratif

### Mise à jour de F-DIR-001 — ordre FIRST-OBJECT / VISUAL_TARGET

Le constat est renforcé. `RUN-PRIORITY` place `FIRST-OBJECT` avant `DIRECTION`, tandis que `FIRST-OBJECT` référence `VISUAL_TARGET` et que les autres guides dominants demandent cible/spec avant build. Gravité provisoire maintenue à **Significatif**, état **confirmé**.

### Mise à jour de F-DIR-007 — correctif critique local

Le constat est renforcé. `DAILY` demande encore une reclassification en présence d’un risque critique sans destination couvrant le cas local critique, tandis que contraste, focus et état sont décrits comme corrections restant locales. Gravité **Majeur** maintenue.

### Mise à jour de F-DIR-008 — invariants de responsabilité

Le constat est renforcé par `FAST-PATH`, qui demande un owner seulement « si nécessaire ». ACTION exige pourtant un owner résoluble pour chaque sortie de run. Gravité **Significatif** maintenue.

### Mise à jour de F-DIR-010 — formes dérivées divergentes

La table `DAILY` ajoute cinq résumés de clôture qui ne reproduisent pas exactement le paquet canonique. Le problème n’est plus seulement la ligne de run de START : les vues dérivées dérivent de façon répétée. F-DIR-013 isole le défaut de clôture ; F-DIR-010 reste le constat transversal de fragmentation des formes.

### Mise à jour de F-DIR-011 — sémantique N/A

`FAST-PATH` et `EXTERNAL-START` emploient ici la bonne règle : N/A seulement pour une non-applicabilité réelle. Cela confirme que le défaut de la ligne 233 est local et corrigeable par alignement interne. F-DIR-011 reste confirmé pour le passage fautif, mais ce bloc fournit la formulation de référence.

## Éléments conformes à préserver

1. `START` reste explicitement l’unique classificateur.
2. `DAILY` interdit le chargement automatique des cinq documents.
3. L’atlas n’est ouvert que s’il peut changer une décision.
4. Les responsabilités de DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG sont rappelées.
5. `FAST-PATH` possède une condition d’arrêt fondée sur la conséquence réelle de la preuve.
6. La sémantique de `N/A-JUSTIFIED` est correcte dans FAST-PATH et EXTERNAL-START.
7. EXTERNAL-START traite la vérité avant le réalisme visuel.
8. Le faux réalisme, le dashboard décoratif et le réemploi automatique sont explicitement refusés.
9. Les modules externes restent indépendants et conditionnels à une décision distincte.
10. La traduction humaine conserve la preuve, la condition d’arrêt et l’owner.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Effectué sur les lignes 245–312 et les façades propriétaires |
| B — Contrats | FULL | Matrice exacte DAILY/ACTION ; routage, owner, décision et checkpoint comparés |
| C — Usage | TARGETED | Agent pressé, agent externe, personne non spécialiste, reviewer et mainteneur simulés |
| D — Résistance | FULL | Six nouveaux constats/observations et cinq mises à jour enregistrés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc commence par `DIRECTION/FIRST-OBJECT`, puis ses contrats de suffisance, grounding et réutilisation. Il devra notamment déterminer si l’ordre contradictoire est seulement documentaire ou s’il forme une dépendance circulaire dans l’exécution réelle.
