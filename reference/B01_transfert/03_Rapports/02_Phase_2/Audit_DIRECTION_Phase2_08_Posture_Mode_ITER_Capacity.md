# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 8

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 646–700 de la reconstruction de travail
- Sections : `Posture — à lire avant toute action`, `0. Classification du mode, preuve et capacité`, `ITER se souvient`, `Cadrage de médium et de capacité`
- Interfaces vérifiées : constitution et carte de lecture de DIRECTION, `DIRECTION/START`, mémoire de lancement, `ACTION/PRECONDITION`, `ACTION/RUN_CARD`, `ACTION/RUN-*`, `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`, `ACTION/GATE-A`, `ACTION/GATE-C`, `SAVOIR/DESIGN-ATLAS`, `SAVOIR/TECH`, QUICKSTART, READING_MAP, ORCHESTRATION_MAP, schéma et validateur de `RUN_CARD`
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison ligne à ligne avec les propriétaires, cinq scénarios d’usage et quatre contrôles machine ciblés
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et le rapport du bloc 7 ont été relus. Les constats repris directement sont F-DIR-006, F-DIR-007, F-DIR-008, F-DIR-010, F-DIR-027, F-DIR-030 et F-DIR-031.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 646–652 | Installer une posture anti-convergence et anti-gaming | Première idée traitée comme hypothèse ; convention et nouveauté restent situées ; limites du jugement reconnues | Le renvoi aux absolus ne suffit pas seul à définir la conséquence opérationnelle d’un gate « passé » sans conception réelle |
| 656–670 | Résumer portée, preuve minimale et arrêt par mode | START reste l’unique classificateur ; capacité absente ne baisse pas le mode ; axes et gates sont distingués | La table se dit contractuelle mais affaiblit plusieurs minima d’ACTION et décrit mal la clôture DIRECTION |
| 672–674 | Protéger la mémoire nécessaire à ITER | Six éléments de continuité exigés ; reclassification si identité ou règle partagée change | Précondition plus riche que le contrat machine ; aucune exigence ITER spécifique dans le schéma ou le validateur normal |
| 678–686 | Choisir le médium et la capacité après le mode | Sépare construction et vérification ; impose l’équivalent réel hors Web ; rend stack et contraintes explicites | Le critère d’activation omet précisément la construction et la robustesse qu’il vient de définir |
| 688–695 | Illustrer les capacités possibles | Lie besoin, moyen et contrat ; accepte explicitement l’absence de capacité additionnelle | Plusieurs contrôles Web/mobile sont formulés comme contrat générique d’un médium plus large |
| 697 | Empêcher qu’une technique devienne la direction | Principe net et cohérent avec SAVOIR | Aucun défaut autonome |

## Passage A — architecture visible

Ce bloc vient immédiatement après les cinq absolus. Il joue donc le rôle d’un pont entre constitution et exécution : posture de jugement, résumé des modes, mémoire d’ITER, puis sélection du médium et des capacités. L’ordre général est solide : **classer la tâche avant de choisir l’outil**, puis adapter la preuve aux capacités réellement disponibles.

La hiérarchie d’autorité est explicitement rappelée :

- `START` classe ;
- DIRECTION cadre le médium et la capacité ;
- ACTION possède les preuves minimales, gates, statuts, verdicts et sorties ;
- SAVOIR possède le jugement et la traduction par médium.

La section 0 franchit toutefois cette frontière en présentant une table nommée « vue contractuelle » de la **preuve minimale** et de la **condition d’arrêt**. Elle n’est donc pas une simple carte de navigation. Dès lors, toute omission par rapport à `ACTION/PRECONDITION` ou `ACTION/CLOSE-EXIT-CHECK` devient matériellement dangereuse : un lecteur pressé peut prendre cette table pour le contrat suffisant.

Le bloc crée par ailleurs trois niveaux de mémoire : la session, la `RUN_CARD` et le manifeste local. Cette souplesse est utile pour les petits ITER. Elle ne précise pas comment prouver qu’une session contient réellement la direction, le dernier artefact et une preuve encore fraîche lorsqu’un run est repris, délégué ou transporté.

## Passage B — contrat sémantique

### Posture

La première idée est correctement traitée comme une hypothèse, non comme une faute. Le texte demande de nommer sa part conventionnelle ou interchangeable, puis autorise trois résultats : conserver, infléchir ou remplacer. Il évite ainsi les deux extrêmes : reproduire automatiquement un genre ou fabriquer de la nouveauté pour elle-même.

Le paragraphe sur la limite structurelle est particulièrement sain. Le système reconnaît qu’il ne produit ni juge impartial, ni transfert automatique du goût. Il sépare nettement :

- craft et direction ;
- gate et vision ;
- contrepoint humain et absence de biais.

Le « piège de conformité » nomme enfin une vulnérabilité réaliste du système : satisfaire sa forme sans honorer son intention. Le retour aux ABSOLUS 1 et 5 protège la direction perceptible, la tâche, le contenu réel et les contraintes d’usage. Il manque seulement une conséquence explicite dans cette phrase — retourner la direction, corriger l’artefact ou déclarer l’absence de preuve — mais ACTION fournit ensuite ces sorties. Aucun nouveau constat autonome n’est nécessaire ici.

### Section 0 — autorité et séquence

La séquence `classe d’abord → vérifie ensuite les capacités` est correcte. Elle empêche un agent de choisir `LITE` parce qu’il ne possède ni navigateur, ni participant, ni runtime. Elle s’aligne sur `ACTION/PRECONDITION` : la tâche et le blast radius déterminent le mode ; les capacités déterminent la voie de preuve et le niveau de conclusion atteignable.

Cette formulation aide aussi à interpréter F-DIR-031 : l’intention raisonnable n’est pas d’interdire l’intake ou la clarification, mais d’obtenir la classification avant la construction, la vérification ou l’action qui engage le run. Le texte ne remplace toutefois pas encore explicitement « avant d’agir » par cette frontière.

### Section 0 — preuve minimale

La comparaison avec le propriétaire ACTION révèle les écarts suivants :

| Mode | Section 0 de DIRECTION | Contrat minimal d’ACTION | Écart matériel |
|---|---|---|---|
| `LITE` | Gate A applicable ou N/A, preuve du risque dominant, axes touchés, diff/artefact | Gates A applicables, **Gate B du risque dominant**, axes concernés, réserve ou prochaine action | Gate B et la conséquence de sortie deviennent implicites |
| `ITER` | Direction rappelée, non-régression, axes touchés, gates si le craft change | Direction retrouvable, diff, non-régression, **Gate A applicable, Gate B du risque touché**, Gate C si le craft change | Gates A et B disparaissent ; seule la relation craft/C reste visible |
| `STANDARD` | JTBD, arbitrage, hiérarchie, typographie, états, axes | Même noyau, plus **Gates A et B ciblés** | Les gates ciblés disparaissent de la « preuve minimale » locale |
| `DIRECTION` | Divergence, ancre, cible, build, capture, gates applicables ; « B1b et C seulement lorsqu’ils sont déclenchés par ACTION » | Alternative si nécessaire, ancre, cible, build, capture, comparaison, **gates A/B/C**, trace d’assets, statut et axes | C est obligatoire pour DIRECTION dans ACTION ; le groupement avec B1b le rend apparemment conditionnel |
| `SYSTÈME` | Impact, consumers, owner, migration, rollback, non-régression | Même noyau, plus décision et **entrée CHANGELOG** | La décision et la promotion durable ne figurent pas dans le minimum local |

Une vue courte peut condenser le propriétaire, mais pas retirer silencieusement les protections qu’elle appelle « preuve minimale ». La ligne 670 rappelle que les gates sont canoniques dans ACTION, ce qui atténue le risque sans le supprimer : sous contrainte de temps, le lecteur a précisément tendance à s’arrêter à la table locale.

### Section 0 — condition d’arrêt

Les sorties LITE, ITER, STANDARD et SYSTÈME sont des résumés raisonnables mais incomplets. Elles ne remplacent pas le test canonique d’ACTION, qui exige notamment artefact et décision retrouvables, preuve ou absence déclarée, scope, axes touchés, risque restant, verdict, owner et prochaine action.

La ligne DIRECTION pose un problème plus net. Elle indique que `direction_status` est « tenu, tenu avec écart assumé ou perdu », puis renvoie « sinon » à l’issue et au verdict ACTION.

Or :

1. `PARTIALLY-HELD`, quatrième valeur canonique, est omis ;
2. `LOST-IN-BUILD` est un statut de fidélité, jamais une clôture suffisante ;
3. `HELD` n’équivaut explicitement pas à `ACCEPTED` ;
4. issue, verdict, limites, owner et prochaine preuve doivent être renseignés selon leur applicabilité pour **toutes** les branches, pas seulement « sinon ».

La clôture de direction située plus loin dans le même document fournit la formulation correcte : `ACTION/CLOSE-EXIT-CHECK` est l’unique test de sortie et conserve séparément état, issue, statut de direction, verdict, limites et creative close.

### ITER se souvient

Le principe est excellent. ITER ne signifie pas seulement « un artefact existe » ; il exige une continuité de décision. Les six éléments demandés sont pertinents :

- direction précédente ;
- périmètre ;
- dernier artefact ;
- décision ;
- preuve ;
- risque restant.

La reclassification est également bien conçue : direction remise en cause → `DIRECTION`; règle partagée → `SYSTÈME`; contexte absent → reconstituer puis reclasser selon la décision réellement retrouvée.

Le contrat de transport ne protège pas cette exigence. Le schéma `RUN_CARD` n’ajoute aucune condition pour `mode: ITER`. L’objet `direction` reste optionnel, `trace_locator` n’est exigé en validation normale que pour STANDARD, DIRECTION et SYSTÈME, et aucun lien ne rattache une preuve antérieure à l’artefact courant. Un manifeste ou une session peut naturellement porter ces informations, mais la projection structurée ne permet pas de distinguer mémoire réelle et simple déclaration générique.

### Cadrage de médium et de capacité

Plusieurs distinctions sont solides :

- capacité de construction ≠ capacité de vérification ;
- runtime de preuve ≠ médium principal de conception ;
- technique ≠ direction ;
- plateforme réelle → preuve adaptée au runtime réel ;
- capacité absente → limite ou `NOT-VERIFIED`, jamais simulation ;
- aucun gain utile → aucune capacité additionnelle.

Le parcours non Web est particulièrement utile : **médium réel → capacité → preuve propre au médium → fallback**. Il s’aligne avec `SAVOIR/TECH`, qui demande rendu observable, idiomes d’interaction, référentiel, unité de budget et preuve indisponible, puis avec `ACTION/GATE-A`, qui exige un médium explicite hors Web lorsque conformité ou accessibilité sont dans le scope.

La définition de la capacité contient cependant une contradiction interne. La première phrase inclut une possibilité qui change **le résultat, la preuve ou la robustesse**. La suivante n’active la capacité que si son absence empêche de **décider ou d’observer** correctement. La construction et la robustesse disparaissent du test d’activation, alors que la phrase suivante demande justement de distinguer construction et vérification.

Cette restriction est plus étroite que l’ORCHESTRATION_MAP, qui garde une capacité si elle change décision, artefact, preuve, limite ou prochaine action. Elle échoue par exemple pour :

- un CMS nécessaire à une publication répétable mais non nécessaire pour choisir une direction ;
- un fichier de design et ses tokens nécessaires à un handoff maintenable ;
- une primitive accessible nécessaire à la robustesse du composant ;
- une typographie variable nécessaire au résultat construit sans être indispensable à l’observation initiale.

La table finale doit aussi rester explicitement située. Les lignes « comportement critique » et « 3D/spatiale » présentent clavier, focus, responsive et mobile comme éléments du contrat. Ils sont appropriés dans de nombreux cas, mais pas universels : une installation spatiale, un casque, une épreuve print ou un système embarqué peuvent exiger d’autres idiomes. Le paragraphe précédent ordonne de chercher l’équivalent réel ; la table devrait donc marquer ces contrôles comme exemples conditionnels ou renvoyer au contrat par médium de SAVOIR/ACTION.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

Commande :

```text
python3 scripts/validate_run_card.py
```

Résultat :

```text
RUN_CARD VALIDATION PASSED — projection validée contre le schéma et fixtures contrôlés
```

La baseline machine est saine avant les mutations de test.

### Test 1 — ITER accepté sans mémoire de direction transportée

Mutation de l’exemple officiel :

- `mode: ITER` ;
- suppression de `direction`, `anchors`, `trace_locator`, `capability_profile`, `creative_close` et `direction_status` ;
- preuve observée limitée à une auto-comparaison du diff courant ;
- verdict `ACCEPTED-WITH-RESERVATION` conservé.

Résultat :

```text
RUN_CARD VALIDATION PASSED
```

Le test ne prouve pas qu’aucune mémoire externe n’existe. Il prouve que la projection et le validateur ne peuvent pas établir la précondition « ITER se souvient » ni exiger le locator qui permettrait de l’inspecter.

### Test 2 — `PARTIALLY-HELD` accepté avec réserve

Mutation : `closure.direction_status: PARTIALLY-HELD`, `issue: null`, `verdict: ACCEPTED-WITH-RESERVATION`.

Résultat :

```text
RUN_CARD VALIDATION PASSED
```

Ce résultat n’est pas classé comme défaut du validateur. Il confirme que `PARTIALLY-HELD` est une combinaison machine réellement supportée et que son omission dans la condition d’arrêt DIRECTION n’est pas purement théorique.

### Test 3 — preuve dépendante d’un moyen sans profil de capacité

Mutation : suppression complète de `capability_profile` de l’exemple DIRECTION accepté, alors que la preuve déclare une inspection du rendu dans des viewports.

Résultat :

```text
RUN_CARD VALIDATION PASSED
```

Le profil est conditionnel dans ACTION, mais aucun raccord machine ne détermine qu’une méthode déclarée dépend d’un navigateur, d’une capture ou d’un runtime. L’obligation reste donc humaine.

### Test 4 — transport du médium

Ajout direct de `run_card.medium: print` :

```text
RUN_CARD VALIDATION FAILED
- run_card : champs inconnus : medium
```

Inscription du médium dans `artifact.scope` et adaptation de `proof.provenance.method` :

```text
RUN_CARD VALIDATION PASSED
```

Le médium peut donc être transporté textuellement dans un champ existant, mais aucun mapping canonique ne dit si sa place est `artifact.scope`, `proof.provenance.method`, `trace_locator` ou une trace externe. Ce contrôle renforce F-DIR-006 sans démontrer qu’un nouveau champ JSON est nécessaire.

## Passage C — usage simulé

### Designer face à une première idée conventionnelle

La posture produit le bon comportement : nommer ce qui converge, comparer au risque, puis conserver ou modifier selon la décision. Elle n’impose ni excentricité, ni catalogue de variantes. C’est un garde-fou créatif efficace.

### Agent sous contrainte de temps

L’agent peut prendre la table de la section 0 comme contrat suffisant. En ITER, il vérifie alors direction et non-régression sans Gate A applicable ni Gate B du risque touché. En STANDARD, il construit hiérarchie et états sans exécuter les Gates A/B ciblés. Le renvoi général à ACTION ne compense pas entièrement un tableau explicitement intitulé « preuve minimale ».

### Reprise ITER après perte de session

Le texte humain force correctement la reconstitution et la reclassification. Une projection JSON peut néanmoins valider un ITER accepté sans direction structurée, sans locator de trace et sans preuve antérieure identifiable. Un reviewer ou un système automatique ne peut pas savoir si la non-régression repose sur une baseline réelle.

### Publication éditoriale à forte cadence

Le besoin peut justifier un CMS, des templates, une recette et des fallbacks pour rendre l’exploitation robuste. L’absence de CMS n’empêche pas nécessairement de décider ou d’observer une maquette ; le critère strict de la ligne 682 pourrait donc interdire la capacité même que la table recommande.

### Installation spatiale non mobile

Le parcours général demande correctement une preuve propre au médium. La ligne 3D/spatial ajoute toutefois « mobile » au contrat. Un lecteur littéral peut produire un fallback mobile sans utilité, alors que le vrai risque porte sur casque, contrôleur, lisibilité à distance, confort motion, performance ou sécurité spatiale.

### Runtime indisponible

Le comportement attendu est robuste : conserver le mode, déclarer la capacité indisponible, réduire seulement la force du claim et utiliser `NOT-VERIFIED`, réserve, retour ou escalade. Le système évite ici le faux `PASS` et la rétrogradation opportuniste.

## Passage D — constats

### F-DIR-034 — la table locale de preuve minimale affaiblit les contrats ACTION

- Gravité provisoire : **Significatif**
- État : **contradiction documentaire confirmée**
- Preuve : lignes 662–668 contre `ACTION/PRECONDITION` lignes 194–200 et `ACTION/GATE-C` ligne 777
- Écarts principaux : Gate B implicite en LITE ; Gates A/B absents en ITER et STANDARD ; Gate C apparemment conditionnel en DIRECTION alors qu’il est obligatoire ; décision et entrée CHANGELOG absentes en SYSTÈME
- Risque : arrêt prématuré, gates non exécutés, preuve minimale différente selon la façade lue
- Facteur atténuant : la section déclare ACTION canonique et la ligne 670 renvoie aux gates propriétaires
- Propriétaire pressenti : ACTION pour le minimum ; DIRECTION doit seulement projeter sans perte
- Test futur : exécuter un cas par mode depuis la seule section 0 et comparer les sorties au CLOSE-EXIT-CHECK

### F-DIR-035 — la condition d’arrêt DIRECTION confond fidélité et clôture

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau documentaire**
- Preuve : ligne 667 omet `PARTIALLY-HELD`, traite `LOST-IN-BUILD` comme valeur d’arrêt et ne rend issue/verdict explicites que dans la branche « sinon », contre ACTION et la clôture DIRECTION des lignes 786–792
- Contrôle machine : `PARTIALLY-HELD + ACCEPTED-WITH-RESERVATION + issue null` est une combinaison validée
- Risque : prendre un statut de fidélité pour un verdict, perdre une branche supportée ou fermer sans le paquet canonique
- Propriétaire pressenti : ACTION pour la clôture ; DIRECTION pour la projection courte
- Correction probable à éprouver : remplacer la cellule par un renvoi au CLOSE-EXIT-CHECK et énumérer seulement les informations que DIRECTION doit rendre prêtes

### F-DIR-036 — la précondition de mémoire ITER n’est pas protégée par la projection structurée

- Gravité provisoire : **Significatif**
- État : **divergence humain/machine confirmée**
- Preuve : lignes 672–674 contre le schéma, qui n’ajoute aucune exigence conditionnelle pour `mode: ITER`, et le validateur, qui n’exige pas `trace_locator` en validation normale
- Contrôle machine : une RUN_CARD ITER acceptée sans direction, trace locator, profil de capacité ni lien à une preuve antérieure passe
- Risque : ITER utilisé comme raccourci sans baseline retrouvable ; non-régression non inspectable ; reprise et délégation fragiles
- Facteur atténuant : la session ou le manifeste local peuvent porter la mémoire hors JSON
- Propriétaires pressentis : DIRECTION pour la précondition ; ACTION et la projection pour son transport vérifiable
- Test futur : ITER éphémère dans une session, ITER persistant, reprise par un autre agent, artefact déplacé et preuve devenue périmée

### F-DIR-037 — le test d’activation d’une capacité exclut une partie des capacités de construction

- Gravité provisoire : **Significatif**
- État : **contradiction interne et inter-document confirmée**
- Preuve : ligne 682 définit une capacité par résultat/preuve/robustesse puis l’active seulement si son absence empêche de décider ou observer ; ligne 684 sépare pourtant construction et vérification ; ORCHESTRATION_MAP garde aussi ce qui modifie artefact, limite ou prochaine action
- Risque : CMS, tokens, primitive robuste, handoff ou moyen de construction écartés parce que l’observation reste possible sans eux
- Facteur atténuant : les exemples de la ligne 680 et la table 688–695 réintroduisent plusieurs capacités de construction
- Propriétaire pressenti : DIRECTION pour le test d’activation ; SAVOIR/ACTION pour preuve et robustesse
- Correction probable à éprouver : activer si l’absence empêche de construire, décider, observer ou tenir une contrainte déclarée de robustesse/maintenance

### F-DIR-038 — la table de capacité rend des contrôles Web/mobile apparemment universels

- Gravité provisoire : **Observation à risque**
- État : **ambiguïté textuelle confirmée ; impact à éprouver**
- Preuve : lignes 692–694 imposent clavier, focus, responsive et mobile dans des contrats génériques, immédiatement après l’interdiction de transposer un critère Web sans équivalent réel
- Risque : faux N/A, contrôle inutile ou oubli des vrais idiomes d’un casque, d’une installation, du print, de l’embarqué ou d’un autre support
- Facteur atténuant : la colonne parle de « capacité possible » et le paragraphe 680 impose l’adaptation au médium réel
- Propriétaire pressenti : SAVOIR/TECH et ACTION/GATE-A pour la preuve par médium ; DIRECTION pour l’exemple de sélection
- Test futur : mobile natif, print, borne tactile, casque spatial, installation sans mobile et interface embarquée

### Mise à jour de F-DIR-006 — mapping humain / trace / projection

Le médium n’a pas de champ direct mais peut être transporté dans `artifact.scope`; la distinction construction/vérification reste une qualification textuelle ; la mémoire ITER ne possède aucun lien structuré avec la version ou la preuve précédente. Le profil de capacité peut aussi être omis malgré une méthode dépendante d’un runtime. F-DIR-006 est renforcé, sans conclure que chaque concept doit devenir un nouveau champ JSON.

### Mise à jour de F-DIR-007 — correctif critique local

La section 0 répète les cinq modes sans résoudre le trou de classification. Sa ligne LITE décrit un delta local sans qualifier le niveau de risque, tandis que l’entrée prioritaire plus loin précise « sans risque critique » et que la projection machine autorise toujours LITE + protection critique. F-DIR-007 reste **Majeur confirmé**.

### Mise à jour de F-DIR-008 — owner et invariants de responsabilité

La condition d’arrêt DIRECTION et le minimum SYSTÈME citent l’owner, mais les trois autres cellules d’arrêt ne le font pas. Comme la table se présente comme contractuelle, le motif d’omission par vue courte persiste. F-DIR-008 reste **Significatif confirmé**.

### Mise à jour de F-DIR-010 — formes minimales concurrentes

La section 0 ajoute une nouvelle matrice de portée, preuve et sortie, distincte de START, ACTION/PRECONDITION, RUN-*, CLOSE-PACKAGE et CLOSE-EXIT-CHECK. F-DIR-034 isole la perte de protections ; F-DIR-010 reste le problème transversal de multiplication des projections sans règle de perte autorisée.

### Mise à jour de F-DIR-027 — ancrage humain et machine

La ligne DIRECTION exige encore une « ancre utile » sans représenter la branche N/A décrite ailleurs. Elle ne précise pas non plus la réserve generated-only. Le bloc renforce donc le contrat humain obligatoire sans corriger sa divergence machine. F-DIR-027 reste **Majeur provisoire**.

### Mise à jour de F-DIR-030 — frontière du jugement de craft

La posture formule ici une frontière saine : le craft n’est pas la direction, le gate n’est pas une vision et un regard externe n’est pas impartial par nature. Cette formulation est à préserver et fournit une base de correction aux zones où DIRECTION absorbe du jugement spécialisé.

### Mise à jour de F-DIR-031 — classification avant action

« Classe d’abord la tâche ; vérifie ensuite les capacités » est plus opérable que « avant d’agir ». La section confirme l’intention d’un classement avant production ou vérification, pas avant la clarification nécessaire au classement. L’exception d’intake reste toutefois implicite ; F-DIR-031 demeure **Significatif**.

## Éléments conformes à préserver

1. La première idée est une hypothèse à tester, non une faute à effacer.
2. Le système ne remplace pas le conformisme par une obligation de nouveauté.
3. Le texte reconnaît l’absence de juge impartial et les limites d’un regard externe.
4. Le craft n’est pas confondu avec la direction ; un gate reste un plancher.
5. Le piège de conformité procédurale est nommé explicitement.
6. START demeure l’unique source de classification.
7. Le mode dépend de la tâche et du blast radius, jamais de l’outil disponible.
8. Une capacité absente réduit la force du claim, jamais silencieusement le niveau de protection.
9. V/U/A/T restent des axes et A/B/C des gates ; aucune note locale ne devient verdict global.
10. ITER exige une direction et une preuve antérieures retrouvables.
11. Une remise en cause identitaire reclassifie vers DIRECTION ; une règle partagée vers SYSTÈME.
12. Construction et vérification sont distinguées.
13. Le runtime de preuve n’est pas automatiquement le médium de conception.
14. Un médium non Web exige son équivalent réel au lieu d’une copie mécanique des critères Web.
15. Stack, version, contrainte déterminante, owner, conséquence et prochaine preuve doivent rester déclarables.
16. Une adaptation de plateforme ne justifie ni dégradation silencieuse ni rendu simulé.
17. L’absence de capacité additionnelle est une sortie valide.
18. Une technique ne devient jamais une direction par défaut.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Position du bloc, autorités, table contractuelle et niveaux de mémoire examinés |
| B — Contrats | FULL | Posture, cinq modes, arrêt, ITER, médium et capacité comparés à leurs propriétaires |
| C — Usage | TARGETED | Première idée, agent pressé, reprise ITER, CMS, spatial et runtime absent simulés |
| D — Résistance | FULL | Cinq nouveaux constats et sept mises à jour enregistrés |
| Contrôles machine | TARGETED | Suite officielle, mémoire ITER, statut partiel, profil de capacité et transport du médium testés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `1. Direction divergente — déclenchement DIRECTION` et le début de `2. Routage — quoi charger et quand` — lignes 701–762. Il devra vérifier la divergence réellement décisionnelle, les axes proposés, la matière obligatoire mais non texturée, le checkpoint humain, les déclencheurs forcés, la résolution des routes et le risque de duplication avec START/ACTION.
