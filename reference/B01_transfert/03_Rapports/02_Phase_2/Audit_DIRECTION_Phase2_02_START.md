# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 2

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 113–241 de la reconstruction de travail
- Sections : `SERVICE-BOUNDARY`, `START`, arbre de classification, entrée minimale, `CREATIVE-BOOT`, `DOMAIN-FRAME`, sortie immédiate et mémoire de lancement
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, comparaison avec ACTION, QUICKSTART, BIBLIOTHEQUE, les schémas et un test ciblé du validateur
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée. Les deux empreintes correspondent à B01. Les constats F-DIR-001 à F-DIR-006 du bloc précédent ont été repris lorsque ce bloc les touche.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 113–117 | Autoriser une proposition de cadrage avant l’ouverture d’un run | Frontière claire entre hypothèse discutable et effet réellement produit ; protection des permissions externes | La notion de proposition « complète » devra rester bornée pour ne pas devenir une production informelle hors trace |
| 119–125 | Déclarer START comme classificateur unique | Autorité et ordre minimal explicites ; modules conditionnels | Le classificateur humain n’est pas entièrement aligné avec le contrat machine sur les risques critiques locaux |
| 127–144 | Classer les cinq modes et gérer les conflits | Ordre clair ; distinction utile entre décision système directe et conséquence d’une direction ; micro-deltas protégés contre l’atlas | Aucun mode ne correspond proprement à certains correctifs locaux critiques après l’interdiction de LITE/ITER |
| 146–159 | Définir l’entrée courte | Décision, risque, scope, contrainte, preuve et owner forment une bonne base | La règle d’omission peut retirer des champs nécessaires ; le mode manque dans ce gabarit alors qu’il vient d’être classé |
| 161–186 | Préparer une décision visuelle ouverte | Relie promesse, preuve, geste, structure, craft, ancre et défaut dominant avant construction | De facto douze champs ; quota fixe ; conflit avec one-shot ; responsabilités empruntées à plusieurs propriétaires |
| 188–215 | Adapter le cadrage au domaine | Propriétés exactement alignées avec le schéma ; anti-stéréotypes ; profondeur conditionnelle | Les seize propriétés sont toutes requises par le schéma ; le coût réel devra être observé sur des runs nouveaux mais simples |
| 217–241 | Créer la mémoire du run et transmettre à ACTION | Sépare intention et changement observé ; persistance proportionnée aux modes | Trois formes différentes de la ligne de run, emploi trop large de N/A, état ACTION introduit dans DIRECTION |

## Passage A — architecture visible

Ce bloc constitue le vrai noyau opérationnel de DIRECTION. Il trace une frontière avant le run, classe, cadre une décision visuelle ou de domaine, puis produit une mémoire et un handoff. L’enchaînement général est intelligible.

La section porte toutefois quatre représentations concurrentes du démarrage :

1. l’entrée minimale à six champs : `DECISION`, `RISK`, `SCOPE`, `CONSTRAINT`, `NEXT-PROOF`, `OWNER` ;
2. le Creative Boot à douze champs ;
3. la ligne de run affichée à sept positions : `ID`, `MODE`, décision, risque, preuve suivante, état ;
4. la mémoire de lancement décrite ensuite à dix champs : `ID`, `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT`, `OWNER`, `NEXT-PROOF`, `LIMIT`, `EXIT-CONDITION`.

Ces vues peuvent servir des moments différents, mais les lignes 221 et 237 donnent deux définitions directes de « la ligne de run ». Le premier format contient `STATE` et omet notamment `SCOPE`, `OWNER`, `LIMIT` et `EXIT-CONDITION`; le second exige ces derniers et omet `STATE`. Le lecteur ne sait pas si le premier est un résumé affiché, une forme minimale ou le contenu réel de la mémoire.

## Passage B — contrat sémantique

### SERVICE-BOUNDARY

Le contrat est utile et bien borné. Une proposition de cadrage peut rendre une hypothèse discutable sans prétendre avoir construit ou vérifié quoi que ce soit. Dès qu’un build, une modification, une vérification, une action externe ou une décision persistante est engagé, le run doit s’ouvrir. La frontière sur les permissions est saine : V1 prépare l’intention et la preuve attendue, tandis que le système autorisé retourne l’effet observé.

Cette section réduit la bureaucratie du premier échange sans créer de preuve fictive. Aucun défaut confirmé dans ce périmètre.

### Arbre de classification

L’ordre `SYSTÈME → DIRECTION → ITER → LITE → STANDARD` est clair. La phrase sur les changements partagés issus d’une direction corrige utilement le risque de classer trop tôt en SYSTÈME. La règle de conflit donne aussi un bon critère pour découper deux risques : indépendance des preuves, owners, artefacts et conditions de sortie.

La « protection de niveau » crée cependant un trou de classification. Elle interdit LITE et ITER lorsqu’un risque critique touche une action, un état, une sémantique, une donnée, une récupération ou une preuve. Les modes de remplacement ne couvrent pas forcément le cas :

- STANDARD est défini pour un écran ou flow nouveau ;
- DIRECTION pour une identité ou position autonome ;
- SYSTÈME pour un blast radius partagé.

Exemple : corriger localement le nom accessible d’un bouton critique dans un écran existant, sans composant partagé et sans changement de direction. Le changement est local et relève naturellement de LITE ou ITER, mais la règle l’interdit. Aucun des trois modes proposés ne décrit honnêtement le travail.

Le contrat machine confirme l’écart. Un test dérivé de l’exemple officiel, avec `mode: LITE`, `risk.level: critical` et une `critical_protection` complète, est accepté par le schéma et par `check_semantic_contract`. Le schéma traite donc mode et protection critique comme deux dimensions combinables, alors que le texte interdit cette combinaison.

La cause probable est une fusion entre deux questions :

- quelle est la nature et la portée du changement ?
- quelle intensité de protection et de preuve exige son risque ?

Le système possède déjà `risk.level` et `critical_protection`. Forcer un autre mode peut décrire moins bien le travail sans ajouter une protection que le contrat de risque ne pourrait porter.

### Entrée minimale

Les six informations choisies sont pertinentes. La règle finale est trop générale : « si l’une de ces lignes ne peut pas changer le mode, la cible, l’artefact ou la preuve, elle est omise ou N/A ».

`OWNER` peut ne modifier aucun de ces quatre objets et rester indispensable à la responsabilité, à l’escalade et à la reprise. Le schéma `RUN_CARD` le requiert pour tous les modes. `SCOPE` peut aussi stabiliser une conclusion sans changer l’artefact. L’utilité d’un champ ne se limite donc pas à sa capacité à changer directement le mode ou la production.

Le texte confond ici :

- champ décisionnel conditionnel, que l’on peut omettre ;
- invariant de traçabilité ou de responsabilité, qui doit rester résoluble ;
- propriété réellement non applicable, seule admissible à `N/A-JUSTIFIED`.

### Creative Boot

Le but est bon : déplacer le jugement créatif avant le build. Les responsabilités sont explicitement attribuées à DIRECTION, BIBLIOTHEQUE, SAVOIR et ACTION.

Trois problèmes apparaissent.

Premièrement, le bloc affirme ne pas créer de champs concurrents, puis introduit douze labels en majuscules, reproduits dans QUICKSTART. Ces labels contiennent des décisions possédées par quatre documents. Sans mapping testable, le Boot devient un formulaire composite de fait. Cela renforce F-DIR-006.

Deuxièmement, `ANTI-DIRECTIONS` exige deux patterns précis et `STRUCTURAL-TENSION` un seul axe. BIBLIOTHEQUE, propriétaire de cette tension, autorise un ou deux axes. DIRECTION réduit donc silencieusement la cardinalité du propriétaire. Le quota de deux anti-directions n’est relié à aucun risque ou test dans ce bloc.

Troisièmement, la ligne 184 exige après observation « la modification réelle apportée » et une réobservation attendue. ACTION et QUICKSTART permettent pourtant un one-shot clôturé après l’observation initiale si la qualité attendue est atteinte, si le défaut dominant est absent et si aucune correction ne promet de gain. Un Boot valide doit donc pouvoir conclure qu’aucune modification est justifiée, en conservant l’observation et la raison.

### DOMAIN-FRAME

Le contrôle mécanique est positif : les seize propriétés listées dans DIRECTION correspondent exactement aux seize propriétés du schéma. Il n’y a ni clé manquante ni clé supplémentaire. Le schéma les rend toutes obligatoires et interdit les propriétés supplémentaires.

Le rôle est également clair : déterminer ce qui mérite recherche ou adaptation sans transformer un domaine en style. La profondeur augmente avec une incertitude ou un coût d’erreur réel.

La charge reste une hypothèse à tester. Le déclencheur inclut toute demande « nouvelle », tandis que la projection machine exige les seize champs. Sur un nouveau domaine simple et bien compris, cela peut produire un formulaire lourd malgré la consigne de ne garder que les variables capables de changer la décision. Cette tension relève de l’efficacité et devra être observée en micro-run.

### Sortie et mémoire

La séparation entre `DECISION-INTENT` et `DECISION-CHANGE` est saine. Le changement ne peut être déclaré qu’après observation.

La ligne 233 transforme cependant toute absence de changement en `N/A-JUSTIFIED`. ACTION donne une règle plus précise :

- `N/A-JUSTIFIED` si aucune conséquence n’était applicable ;
- `NOT-OBSERVED` si une conséquence attendue n’a pas été observée.

Une décision attendue mais non modifiée ne devient donc pas automatiquement non applicable. DIRECTION affaiblit ici la sémantique propriétaire d’ACTION.

Le champ `[état]` dans la ligne 221 pose aussi une frontière : ACTION possède les états de run, mais DIRECTION ne précise pas si cette valeur doit reprendre l’enum ACTION, une simple description ou un autre état. La mémoire détaillée de la ligne 237 ne mentionne ensuite plus l’état.

## Passage C — usage simulé

### Agent sous contrainte de temps

L’arbre de classification est rapide à suivre pour les cas ordinaires. Sur un correctif critique local, l’agent est forcé de mentir sur la nature du travail, de désobéir au texte, ou de chercher une exception non donnée. Le validateur ne l’aidera pas : il acceptera LITE.

L’agent reçoit ensuite plusieurs formats de démarrage. Il peut prendre la ligne courte de 221 comme suffisante et perdre scope, owner ou limite ; il peut aussi remplir les douze champs du Boot par réflexe malgré la règle de proportionnalité.

### Designer

Le Boot prépare utilement promesse, preuve, geste et défaut dominant. Les champs structurels et de craft évitent un rendu commenté seulement après coup. Le quota fixe peut toutefois fabriquer deux anti-directions faibles ou limiter une tension réellement bidimensionnelle.

### Reviewer

Le reviewer peut distinguer intention et changement observé. La règle N/A trop large peut masquer un échec : une conséquence attendue mais absente risque d’être enregistrée comme non applicable.

### Mainteneur et système automatique

Le DOMAIN-FRAME est correctement aligné avec son schéma. À l’inverse, le validateur RUN_CARD ne reflète pas l’interdiction textuelle de LITE/ITER critique. Les différentes formes de la ligne de run ne possèdent pas de mapping machine unique.

## Passage D — constats

### F-DIR-007 — trou de classification pour un correctif critique local

- Gravité provisoire : **Majeur**
- État : **confirmé**
- Preuve : lignes 140 et définitions des modes ; test ciblé accepté par schéma et validateur avec `LITE + critical_protection`
- Risque : mauvaise classification, surcharge, contournement du texte ou divergence humain/machine sur des corrections sensibles
- Propriétaire pressenti : DIRECTION pour la classification ; ACTION et schéma comme consommateurs à aligner selon la décision retenue
- Test futur : cas local critique non partagé, cas partagé critique, nouveau flow critique et correction identitaire critique

### F-DIR-008 — règle d’omission incompatible avec les invariants de responsabilité

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau textuel**
- Preuve : ligne 159 contre l’exigence d’owner dans la mémoire, ACTION et le schéma
- Risque : owner ou scope omis parce qu’ils ne changent pas directement l’artefact
- Propriétaire pressenti : DIRECTION, avec vérification ACTION/HANDOFF

### F-DIR-009 — Creative Boot incompatible avec le one-shot valide

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : ligne 184 exige modification et réobservation ; ACTION et QUICKSTART autorisent la clôture après observation initiale sans correction utile
- Risque : itération artificielle pour satisfaire le Boot, contraire à la règle anti-rituel
- Propriétaire pressenti : DIRECTION ; ACTION conserve la règle de clôture

### F-DIR-010 — ligne de run définie sous des formes incompatibles

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : lignes 221 et 237 ; comparaison avec entrée minimale, QUICKSTART et ACTION/HANDOFF
- Risque : perte de scope, owner, limite ou condition de sortie ; création d’un état local non aligné
- Propriétaire pressenti : ACTION pour la trace ; DIRECTION pour la façade de lancement

### F-DIR-011 — absence de changement mal classée

- Gravité provisoire : **Significatif**
- État : **confirmé**
- Preuve : ligne 233 contre ACTION, qui distingue `N/A-JUSTIFIED` et `NOT-OBSERVED`
- Risque : masquer une conséquence attendue mais absente comme non-applicable
- Propriétaire pressenti : ACTION pour la sémantique ; DIRECTION doit reprendre la distinction

### F-DIR-012 — cardinalités du Boot non alignées avec le propriétaire structurel

- Gravité provisoire : **Significatif / à éprouver**
- État : **écart textuel confirmé, impact à mesurer**
- Preuve : un axe à la ligne 173 contre un ou deux axes dans BIBLIOTHEQUE ; deux anti-directions sans justification de risque
- Risque : réduction arbitraire ou remplissage de quota
- Propriétaire pressenti : BIBLIOTHEQUE pour la tension ; DIRECTION pour l’activation

### Mise à jour de F-DIR-003 — handoff sans temporalité

Le constat est renforcé. Les lignes 219–239 distinguent mieux intention et observation, mais multiplient les formes de lancement et réintroduisent les champs de clôture. Gravité provisoire maintenue à **Significatif**.

### Mise à jour de F-DIR-006 — mapping informel

Le Creative Boot confirme le risque : ses labels empruntent des responsabilités à quatre propriétaires sans mapping canonique. Le constat passe d’**Observation** à **Significatif provisoire** ; la lecture des contrats machine décidera s’il faut un mapping, une réduction ou une simple clarification de transport.

## Éléments conformes à préserver

1. SERVICE-BOUNDARY distingue correctement hypothèse, production, preuve et permission.
2. START est explicitement l’unique classificateur.
3. La classification par décision directe évite de transformer toute conséquence partagée en run système immédiat.
4. La règle de conflit définit l’indépendance par preuve, owner, artefact et sortie.
5. Les micro-deltas ne chargent pas automatiquement l’atlas.
6. Le Creative Boot place le jugement avant la construction.
7. Le DOMAIN-FRAME est textuellement aligné avec son schéma.
8. Les stéréotypes de domaine sont explicitement refusés.
9. `DECISION-CHANGE` reste subordonné à une observation réelle.
10. La persistance est proportionnée au mode.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Effectué sur les lignes 113–241 |
| B — Contrats | FULL | Effectué ; interfaces ACTION et schémas vérifiées de façon ciblée |
| C — Usage | TARGETED | Agent, designer, reviewer, mainteneur et système automatique simulés |
| D — Résistance | FULL | Six nouveaux constats et deux mises à jour enregistrés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `DIRECTION/DAILY`, `FAST-PATH` et `EXTERNAL-START`. Il devra vérifier si les façades dérivées reproduisent les défauts de START, résolvent les formats de lancement ou créent des routes concurrentes.
