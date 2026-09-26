# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 11 : COMPONENTS

## Cadre, reprise et baseline

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 611–660** ; catalogue des couches 613–620, échelle de responsabilité 622–629, contrat `LAYER/BRAND_GRAMMAR` 631–651, graphe et interdits 653–657. `COMPAT` commence à 661 et sera lu dans le bloc suivant.
- Protocole externe v2.0 §12 relu : A architecture, B contrat sémantique, C lecteurs sous contrainte simulés, D résistance. Rapport MODIFIER bloc 10, plan maître et checkpoints DIRECTION/ACTION/SAVOIR repris. Interfaces consultées : BIBLIOTHEQUE entrée 54–63, READ 70–80, SELECT 129–199, CONTRACTS 256–284, OBJECT 519–538, MICRO 542–550, MODIFIER 585–607, EVOLUTION 733–770 et sortie 776–790 ; DIRECTION/START 119–144 ; SAVOIR/SYSTEM 690–704 ; ACTION/AUTHORITY 63–67, RUN-SYSTEM 379–387 et ROUTING 870–885 ; CHANGELOG 23–42. Ces renvois vérifient les propriétaires et ne valent pas audit final des sections restantes.
- Hash B01 vérifiés inchangés : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Contrôle du bloc précédent : MODIFIER est une route **transversale après la structure**, pas une septième couche de composants. `FIELD_SWITCH` et `NAVIGATION_SHELL` ne remplacent pas les gestes accessibles de `LAYER/PRIMITIVES` ; `PRINT_FIELD` ne devient ni couche `BRAND_GRAMMAR` ni règle partagée sans gain transversal. COMPONENTS confirme ces séparations par la table 615–620 et le graphe 655–657. Aucun amendement du rapport MODIFIER n'est nécessaire.
- Périmètre : diagnostic documentaire avec simulations de choix et de preuves. Pas d'interface en production, de test utilisateur, de mesure de gain, de patch normatif ou de verdict global.

## Passage A — architecture des couches et accès

`BIBLIOTHEQUE/COMPONENTS` est un titre canonique. L'outil `read_route.py BIBLIOTHEQUE/COMPONENTS` ouvre **l'intégralité de cette section** ; `validate_reading_map.py` passe. Ce résultat diffère des refus pour OBJECT, MICRO et MODIFIER et confirme qu'un défaut d'accès est **partiel**, pas que toutes les routes de BIBLIOTHEQUE seraient introuvables. Il n'efface ni F-DIR-028 ni F-ACT-001. Les sous-types et préfixes évoqués dans la table ne deviennent pas pour autant des locators autonomes de ce lecteur.

| Couche de 615–620 | Ce qu'elle porte | Limite importante |
|---|---|---|
| `LAYER/TOKENS` | Valeurs et relations durables, notamment rôles de couleur, type, espace, z-index et motion | Un token nommé ne donne pas seul un comportement, un état testé ou un verdict ; SAVOIR/SYSTEM juge la sémantique et les thèmes |
| `LAYER/BRAND_GRAMMAR` | Expression de marque hors logique métier : cadres, signes, trames, signatures type et matière | Couche transversale gouvernée ; n'est ni un dossier de CSS décoratif ni le propriétaire de l'identité à la place de DIRECTION |
| `LAYER/PRIMITIVES` | Geste et sémantique accessibles de Button, Link, Input, Dialog et autres bases | Ne déclarent pas la promesse entière ; une primitive isolée ne valide pas sa scène ou sa tâche |
| `LAYER/OBJECTS` | Formes locales stables de preuve, information, état ou action ; `MICRO/*` y est sous-type dense | Aucun `LAYER/MICRO` parallèle ; les objets ne portent pas une page spécifique ni les primitives réinventées |
| `LAYER/SCENES` | Combinaison de `SUPPORT/*`, `GRID/*` et `SCENE/*` pour la composition et la hiérarchie d'un écran | La scène ne dispense ni des états ni des gestes accessibles des couches inférieures |
| `LAYER/TEMPLATES` | Séquence de scènes pour une intention produit | `TEMPLATE/*` n'est qu'une possibilité **si nommée et contractualisée** ; « Produit », « dashboard », « authentification », « archive », « campagne » sont descriptifs, pas cinq routes publiées |

La table 624–629 établit une échelle : primitive = geste, objet = preuve/état/action locale, scène = composition d'écran, template = orchestration de plusieurs scènes. Elle ne dit pas de fabriquer systématiquement six couches pour une correction locale. SELECT 163–197 permet de n'ouvrir que la responsabilité qui change la prochaine décision, avec héritage des autres. `TEMPLATE/*` n'est pas un préfixe énuméré dans la liste canonique 129–140 : tant qu'aucune route nommée ne figure dans la source, un lecteur ne peut pas en inférer une route ADOPTED. S'il crée une forme locale candidate, il doit la marquer local ou PILOT et suivre CONTRACTS/EVOLUTION/CHANGELOG, conformément à la sortie 786 ; une séquence de scènes spécifique à un projet peut rester locale.

Le graphe 655 descend de **templates → scenes → objects → primitives → tokens** et dispose `brand_grammar → tokens` avec application limitée aux surfaces déclarées. Il représente la direction des dépendances, pas une obligation d'emboîtement de tous les niveaux dans chaque rendu. Les interdits 657 bloquent des inversions usuelles : une scène qui refait la primitive accessible, un objet qui importe une page, une primitive qui décide la direction, ou une grammaire de marque qui décide à la place de DIRECTION. `MICRO/*` n'ajoute aucune branche indépendante du graphe, et `MODIFIER/*` ne change pas son sens.

## Passage B — contrat, rôles et temporalité des décisions

### Couche versus décision de mode

Une couche décrit **où réside la responsabilité et de quoi elle dépend** ; le mode du run reste classé par DIRECTION/START 131–144. Un composant de marque utilisé localement dans une nouvelle direction peut requérir une décision créative DIRECTION, tandis que sa promotion comme règle partagée avec consumers distincts réclame une décision SYSTÈME dépendante (START 138), sauf inséparabilité explicitement arbitrée. La présence de `LAYER/TOKENS` ou `LAYER/BRAND_GRAMMAR` dans une maquette ne reclassifie pas tout le run. Cette distinction protège la réserve F-SAV-007 sur l'impératif « reclassifie » de SAVOIR/SYSTEM 694 ; COMPONENTS ne reproduit pas cet impératif.

SAVOIR/SYSTEM 692–704 distingue token primitif et token sémantique, juge thèmes, source de vérité, stack et contrat de composant ; BIBLIOTHEQUE/COMPONENTS est désigné pour la structure détaillée ; ACTION/RUN-SYSTEM 381–387 détient impact, consumers, migration, rollback, non-régression, preuve et issue. ACTION/ROUTING 885 mentionne explicitement les trois quand le composant ou le blast radius est concerné ; l'omission de SAVOIR/SYSTEM dans la cellule d'ATLAS reste **F-SAV-004**. Pour un changement partagé, la carte machine et la trace doivent rendre les minima inspectables ; F-ACT-015/F-ACT-021 sur le transport et le contrôle du paquet SYSTÈME demeurent ouverts. **Cependant, le renvoi de SAVOIR 704 vers COMPONENTS n'est pas intégralement servi par le contrat de cette section ; voir F-BIB-004 ci-dessous.**

### `LAYER/BRAND_GRAMMAR` : quinze champs, plusieurs autorités (631–651)

| Famille de champs | Champs de 634–648 | Fonction et borne |
|---|---|---|
| Responsabilité et périmètre | `OWNER`, `SCOPE`, `DECISION-OWNER`, `BLAST-RADIUS` | Séparer maintenance/usage de la personne qui prend la décision finale ; cartographier les surfaces et consumers touchés avant propagation. L'owner de run n'est pas automatiquement propriétaire de la marque entière. |
| Expression autorisée | `TOKENS-CONSUMED`, `AUTHORIZED-SIGNATURES`, `ADMISSIBLE-SURFACES`, `COUNTERINDICATIONS`, `REMOVAL-TEST` | Définir application et refus situés ; un motif peut être retiré du cas où il nuit sans supprimer toute expression de marque. N'infère pas « autorisé » depuis la présence d'un token. |
| Gouvernance et suivi | `APPROVAL-ROUTE`, `LIFECYCLE-STATUS`, `NEXT-REVIEW` | Relier à l'autorité effectivement compétente et à la décision CHANGELOG ; le champ ne crée pas un approbateur ni un statut de run. Si l'autorité nécessaire manque, ACTION/AUTHORITY 65–67 prévoit reprise/escalade, pas auto-approbation. |
| Preuve et retrouvabilité | `PROOF`, `PROOF-LIMIT`, `TRACE-LOCATOR` | Documenter l'observation et sa limite, rendre le run et les usages retrouvables ; un champ rempli ne prouve ni efficacité de marque, ni accessibilité, ni gain chez plusieurs consumers. |

La liste « il déclare » s'adresse à **la couche transversale gouvernée** ; elle n'ordonne pas de remplir quinze champs pour chaque trame de campagne locale. L'entrée BIBLIOTHEQUE 54–61, CONTRACTS 258 et EVOLUTION 768 distinguent local, partagé et durable. Une expression de marque propre à une scène peut rester sous la direction, le style, un objet ou un modificateur local ; lorsqu'elle devient une grammaire applicable à plusieurs surfaces, le contrat fort et les droits de décision deviennent pertinents. Le point discriminant à observer plus tard : un composant local à faible risque et une grammaire réellement publiée à plusieurs consumers ne demandent pas la même preuve ni le même circuit d'approbation. Cette lecture ne crée pas de nouvelle occurrence F-BIB-002 sans texte imposant le tableau à tout run local.

`LIFECYCLE-STATUS` conserve la décision de cycle de vie gouvernée chez CHANGELOG 31–42. Sa présence dans le contrat est une **référence à synchroniser**, pas une capacité pour BIBLIOTHEQUE de prononcer `ADOPTED` ; `APPROVAL-ROUTE` indique par où une approbation existante est demandée, jamais qu'un champ vide peut être auto-rempli « APPROVED ». ACTION/AUTHORITY 67 distingue l'autorisation de décider d'un résultat validé. `PROOF` doit renvoyer à méthode, artefact, version/scope et observation pertinents selon ACTION ; `PROOF-LIMIT` prévient la généralisation d'une capture de marque à tous les thèmes, langues ou scènes. `REMOVAL-TEST` est une épreuve locale de contribution, pas une preuve d'adoption ou un critère qui supprimerait une signature portant réellement identité et produit.

Une baseline V1 cohérente et des identifiants de couches ne prouvent pas les bénéfices d'un composant partagé. CONTRACTS 260–284 et EVOLUTION 735–770 réservent la promotion à usages contrastés, gain avec baseline/observation ou mesure, non-homogénéisation, maintenance et décision persistée. La source CHANGELOG 21 signale d'ailleurs explicitement que l'efficacité des runs, adoption et qualité produite restent non vérifiées. Les labels de couche servent au diagnostic, pas de preuves de transfert sur Web/mobile/print par leur simple présence.

## Passage C — simulations de lecteurs et décisions de frontière

| Situation simulée | Lecture/action attendue | Erreur recherchée |
|---|---|---|
| Agent, correction de focus dans un Button existant | Hériter de la primitive, contrôler le focus et l'intégration dans la scène selon le risque ; ne pas relancer toute la grammaire de marque | Créer une route de template ou un run SYSTÈME pour un delta strictement local |
| Designer, état « danger » fondé sur un rouge brut | Distinguer valeur de palette et rôle sémantique avec SAVOIR/SYSTEM, vérifier texte/contraste/états dans l'objet | Appeler le nom du token une preuve de compréhension ou mettre la couleur seule dans la primitive |
| Intégrateur, `MICRO/QUERY_HEALTH` au sein d'une scène de supervision | Conserver MICRO sous `LAYER/OBJECTS`, primitive pour action, scène pour hiérarchie ; tester les états dans le rendu réel | Inventer une couche `LAYER/MICRO` ou proclamer la scène valide parce que l'objet isolé passe |
| Designer, parcours de trois scènes propre à un produit | Garder l'orchestration locale si aucune route TEMPLATE nommée ; contrat/prochaine preuve si candidat au partage | Employer `TEMPLATE/DASHBOARD` ou `TEMPLATE/AUTHENTIFICATION` comme routes canoniques inexistantes |
| Mainteneur, `LAYER/PRIMITIVES` avec Dialog partagé entre Web et mobile | Chercher anatomie, variants, frontières de composition, tokens et baseline dans le contrat de composant indiqué par SAVOIR 704 ; constater que COMPONENTS ne donne pas ces champs pour les primitives, consigner F-BIB-004 et ne pas inventer leur vérification | Prendre la simple liste « Dialog » ou le contrat de marque pour contrat détaillé du composant |
| Direction visuelle, nouvelle signature de marque avec token partagé induit | Traiter la direction, puis dépendance SYSTÈME sur token/consumers selon START 138 ; assigner owner et preuve pour chaque décision | Substituer immédiatement un run SYSTÈME au travail identitaire initial (F-SAV-007) |
| Mainteneur, `BRAND_GRAMMAR` distribuée à design, Web et mobile | Déclarer surfaces, signatures, contre-indications, approval route réelle, owner(s), migration et rollback ; tester application et non-régression sur consumers | Écrire `ADOPTED` dans le composant et supposer la décision CHANGELOG ou la preuve réalisées |
| Équipe, trame spécifique à une seule campagne | Tracer intention et limites dans le run local ; évaluer `MODIFIER/PRINT_FIELD` si elle change vraiment la matière ; ne pas imposer le contrat gouverné complet | Remplir quinze champs fictifs de `BRAND_GRAMMAR` pour un motif unique |
| Reviewer, primitive accessible seule mais navigation dans un overlay illisible | Test d'intégration dans scène, viewport, focus et fond, puis issue ACTION ; ne pas faire remonter l'accessibilité entière à la scène | Déclarer « accessible » sur test unitaire, ou réimplémenter le focus dans la scène |
| Mainteneur, bibliothèque de marque sans owner/approbateur défini | Identifier le décideur et le canal réel ou escalader la décision partagée ; laisser le résultat non accepté sans autorité | Auto-accorder `APPROVED` depuis l'existence du champ `APPROVAL-ROUTE` |

Ces dix cas sont des épreuves de **lecture documentaire**, sans preuve d'utilisation ni test de conformité exécuté.

## Passage D — résistance, déduplication et limites

| Résistance tentée | Diagnostic et suite |
|---|---|
| Une scène redéfinit un Button ou un objet importe la page complète | 624–629 et 657 l'interdisent ; inspecter dépendances réelles en phase de contrat/technique, sans conclure sur un projet inexistant. |
| Le tableau des couches transforme MICRO ou MODIFIER en couches de même rang | MICRO est explicitement sous `LAYER/OBJECTS` 618 ; MODIFIER 587 est comportement ajouté après structure ; aucun nouveau préfixe de couche. |
| Des exemples de TEMPLATE sont repris comme routes prêtes à adopter | 620 est conditionnel, SELECT 142 et sortie 786 exigent route canonique existante ou statut local/PILOT déclaré ; pas de route inventée. |
| Une grammaire « approuvée » s'autorise elle-même ou déclare un PASS | 631–651 contient champs, mais ACTION/AUTHORITY et RUN-SYSTEM gardent le décideur et l'issue ; CHANGELOG possède statut. `APPROVAL-ROUTE` n'est pas une permission. |
| Une couche partagée est testée seulement en isolation | CONTRACTS 284/OBJECT 538 et GATE 703 exigent intégration contextualisée ; ACTION garde scope, preuve et verdict. F-ACT-015/021 protègent le transport machine du run SYSTÈME. |
| Un style local induisant un token partagé remplace le run DIRECTION | Rattacher à F-SAV-007 et START 138 ; retenir dépendance SYSTÈME distincte si nécessaire, pas de nouveau F-BIB. |
| L'ATLAS appelle COMPONENTS et ACTION sans SAVOIR/SYSTEM | F-SAV-004 reste localisé à ce renvoi de l'ATLAS ; ACTION/ROUTING 885 offre le trajet complet. Ajouter la route au contrat de couches lui-même ne corrigerait pas nécessairement l'ATLAS. |
| SAVOIR 704 délègue l'anatomie et les frontières de composition d'un composant partagé à COMPONENTS | La table 613–629 borne les couches, 631–649 contractualise seulement la grammaire de marque. CONTRACTS 260–280 ajoute un contrat **de route** durable mais ne reprend ni anatomie/variants génériques, ni tokens, ni baseline de rendu, ni source de vérité du composant. **F-BIB-004** : destination structurelle insuffisante pour un composant partagé ordinaire. |
| Le locator CLI de COMPONENTS est supposé défaillant par analogie avec MODIFIER | Test direct **réussi** ; la famille F-DIR-028/F-ACT-001 doit rester circonscrite aux titres refusés. |

### F-BIB-004 — renvoi au contrat structurel d'un composant partagé non matérialisé

- **Localisation :** SAVOIR/SYSTEM 704 désigne explicitement `BIBLIOTHEQUE/COMPONENTS` comme propriétaire de la structure détaillée d'un composant partagé ; COMPONENTS 613–657 décrit les couches et fournit un contrat détaillé uniquement à `LAYER/BRAND_GRAMMAR`. CONTRACTS 260–280 couvre la route durable en général, OBJECT 521–534 les objets durables, sans remplir la même liste pour une primitive partagée ordinaire.
- **Fait textuel :** intention/anatomie/variants/états/responsive/tokens/frontières de composition/baseline de rendu/source de vérité/owner/compatibilité/revue sont annoncés chez SAVOIR 704. Les états, responsive, owner, compatibilité et revue ont un équivalent générique dans CONTRACTS ; **anatomie, variants génériques, tokens consommés, frontières de composition, baseline de rendu et source de vérité** ne sont pas définis dans COMPONENTS pour `LAYER/PRIMITIVES` ou un composant partagé non lié à la marque. BRAND_GRAMMAR déclare certains de ces aspects pour son propre cas mais ne généralise pas aux autres couches.
- **Effet possible :** un lecteur dirigé vers le bon titre sait quel niveau possède un Dialog, mais pas où fixer sa structure et ses variantes vérifiables ; deux consumers peuvent diverger silencieusement, ou l'équipe peut croire le contrat satisfait avec un nom de couche et une liste d'états. **Gravité provisoire : significatif à éprouver**, sans fréquence ni déploiement réel attestés.
- **Atténuations :** la liste de SAVOIR 704 existe et peut être recopiée dans une trace locale ; CONTRACTS fournit une part du contrat, ACTION 885 renvoie aux trois routes et une équipe peut disposer d'une documentation de composants hors du corpus. Le trou concerne la **destination normative promise** et sa forme opérationnelle, pas l'impossibilité absolue de décrire le composant.
- **Test discriminant :** comparer un `Dialog` partagé Web/mobile, un `OBJECT/CONTROL_VALUE_TILE` durable et une grammaire de marque transversale. Pour chacun, demander où l'on lit anatomie, variant sémantique, tokens consommés, frontière d'assemblage, baseline de rendu et source de vérité ; modifier un état sur un consumer puis vérifier ce que le contrat et ACTION obligent à retester. La documentation extérieure du projet ne sera pas prise pour un champ normatif existant dans V1.
- **Réparation candidate après consolidation :** expliciter dans COMPONENTS le contrat de structure du composant partagé, avec rattachement au contrat commun et aux couches qui l'activent, et renvoyer SAVOIR/SYSTEM au jugement des tokens et ACTION/RUN-SYSTEM à la preuve et à la migration. Définir les éléments exigibles selon risque et type de composant, sans quinze nouveaux champs obligatoires pour un delta local.
- **Déduplication :** F-SAV-004 concerne la **route omise dans l'ATLAS**, F-SAV-007 la reclassification du mode, F-ACT-015/021 la **projection et l'opposabilité** des obligations SYSTÈME. F-BIB-004 porte sur le **contrat de structure absent à l'endroit propriétaire nommé**, même si tous les lecteurs chargent les bons fichiers et si la carte machine transmet parfaitement ce qu'on lui donne. F-BIB-002 concerne le dosage d'un contrat local, pas le contenu manquant d'un composant partagé.

Les autres frontières restent explicites : couches inférieures, grammaire gouvernée, classement chez DIRECTION, jugement chez SAVOIR, preuve/issue chez ACTION et statut de route chez CHANGELOG. La liste BRAND_GRAMMAR exige un arbitrage réel pour son déploiement partagé ; aucun champ ne fournit à lui seul permission, efficacité ou gain. F-BIB-001/002/003 restent provisoires et distincts de F-BIB-004.

## Couverture et reprise

| Passage | Profondeur | Couverture/limite |
|---|---|---|
| A — architecture | FULL | 611–660, six couches, graphe, frontières, CLI COMPONENTS réussi |
| B — sémantique | FULL | Responsabilités, quinze champs BRAND_GRAMMAR, rôles de DIRECTION/SAVOIR/ACTION/CHANGELOG et cycle de vie |
| C — usage | TARGETED | Dix cas de lecture simulés ; aucun consumer déployé observé |
| D — résistance | TARGETED | F-BIB-004 provisoire sur contrat partagé manquant ; autres IDs dédupliqués |
| Machine | TARGETED | `read_route.py` réussi et carte validée ; absence de re-test des fixtures `RUN_CARD` déjà documentée sous F-ACT-015/021 |
| Externe | N/A-JUSTIFIED | Aucune assertion externe requise pour ce contrat interne ; droits réels et normes par médium restent à vérifier si un run les engage |

Le séparateur est à 659 et la ligne 660 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md` lignes **661–696**, `COMPAT`. Reprendre §12 et le présent diagnostic, puis vérifier hypothèses de combinaison, absent de matrice, preuve/scope/risque et absence de recettes obligatoires.
