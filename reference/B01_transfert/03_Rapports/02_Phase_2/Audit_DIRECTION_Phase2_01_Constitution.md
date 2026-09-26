# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 1

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 1–109 de la reconstruction de travail, du titre aux repères de vocabulaire
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2 — architecture visible, contrat sémantique, usage simulé et résistance
- Statut : diagnostic sectionnel provisoire ; aucune décision finale de patch avant lecture complète du périmètre et vérification des interfaces

La baseline a été revérifiée avant lecture. Les SHA-256 du système et du protocole correspondent à B01.

## Lecture structurée du bloc

| Segment | Fonction réelle | Ce qui fonctionne | Question ou faiblesse à suivre |
|---|---|---|---|
| Lignes 1–3 | Nommer le document, son statut expérimental et son rôle d’entrée | Statut et rôle immédiatement visibles ; la stabilisation publique n’est pas prétendue | La promesse d’efficacité formulée plus loin dépasse ce statut expérimental |
| Lignes 5–17 | Définir l’autorité de DIRECTION et répartir les responsabilités | Bonne séparation entre classification, exécution, jugement, structure et gouvernance | Le mot « exclusive » devra être confronté aux responsabilités effectivement exercées dans chaque source |
| Lignes 19–21 | Protéger la frontière entre vues de cadrage et schéma `RUN_CARD` | La source machine et le propriétaire de clôture sont explicitement renvoyés vers ACTION | Vérifier que toutes les projections ultérieures respectent réellement cette frontière |
| Lignes 23–29 | Orienter la lecture et transmettre à ACTION | La condition d’arrêt est claire et lutte contre le chargement excessif | Le handoff pré-build et la clôture post-observation sont réunis dans une même « sortie » |
| Lignes 31–39 | Séparer `ROUTE`, `TARGET` et `HANDOFF` | Modèle mental utile et compact | Le contenu de HANDOFF inclut des éléments disponibles seulement après observation ; temporalité à clarifier |
| Lignes 41–55 | Montrer les vues internes et leur déclenchement | Bonne logique de chargement conditionnel ; chaque vue possède un résultat attendu | Une autre chaîne interne inverse ensuite `VISUAL_TARGET` et `FIRST-OBJECT` |
| Lignes 57–72 | Fournir un chemin rapide | Les besoins courants sont reliés à des locators concrets | Plusieurs lignes donnent des ordres différents ; la carte peut être prise pour une seconde séquence canonique |
| Lignes 74–90 | Définir périmètre, ambition, priorité, standard créatif et gouvernance | Bonne ambition positive ; priorité critique et limites de preuve explicites | Claim d’efficacité non démontré, périmètre possiblement trop étroit et mapping entre vues encore informel |
| Lignes 92–109 | Séparer les taxonomies et expliquer les tags | Les quatre taxonomies sont distinguées ; les adjectifs faibles sont refusés comme décisions suffisantes | Une partie de la légende n’est pas utilisée dans DIRECTION ; `BASIS` et `CAPABILITY-BASIS` demandent un mapping stable |

## Passage A — architecture visible

Le bloc agit comme une façade interne complète. Il présente successivement : autorité, frontières, sortie, contrats, modules, carte rapide, ambition, priorités, taxonomies et vocabulaire. Cette architecture répond bien à la question « comment démarrer et à qui transmettre ? ».

La difficulté vient du nombre de représentations successives du même chemin : table des responsabilités, orientation, trois contrats, architecture d’activation, carte en trente secondes et chaîne de lecture interne. Ces représentations peuvent être utiles pour des questions différentes, mais elles doivent produire le même ordre lorsque cet ordre est causal.

L’ordre actuellement observable n’est pas stable :

1. lignes 47–53 et 55 : `START → CREATIVE-BOOT → VISUAL_TARGET → DIRECTION-ATELIER → FIRST-OBJECT → DOUBLE-LOOP → HANDOFF/ACTION` ;
2. ligne 72 : `START → FIRST-OBJECT → VISUAL_TARGET → DIRECTION-ATELIER → DOUBLE-LOOP → HANDOFF` ;
3. `READING_MAP` : `START → VISUAL_TARGET`, puis `FIRST-OBJECT`, `SAVOIR/CRAFT`, `ACTION/RUN-DIRECTION` ;
4. `QUICKSTART` : `START → VISUAL_TARGET → FIRST-OBJECT → DOUBLE-LOOP → ACTION/RUN-DIRECTION`, avec `SAVOIR/CRAFT` dans le noyau ;
5. `ACTION/RUN-DIRECTION` exige une ancre et `VISUAL_TARGET` avant le build de la première scène.

Le contrat causal dominant du corpus place donc la cible visuelle avant la construction du premier objet. La ligne 72 est la divergence la plus nette. La position exacte de `CREATIVE-BOOT`, de `SAVOIR/CRAFT` et du lancement d’`ACTION/RUN-DIRECTION` demande encore une vérification inter-fichiers complète.

## Passage B — contrat sémantique

### Statut et autorité

Les lignes 3, 7 et 21 établissent une hiérarchie saine : DIRECTION cadre ; ACTION possède les preuves exécutables et la clôture ; SAVOIR porte le jugement ; BIBLIOTHEQUE la structure ; CHANGELOG la gouvernance durable. La distinction entre cadrer un niveau de preuve et exécuter une preuve est intelligible.

Le tableau parle toutefois de « responsabilité exclusive ». Cette force contractuelle exige une vérification stricte : toute procédure de preuve détaillée dans DIRECTION, toute classification recréée dans ACTION ou tout statut créé ailleurs deviendrait une violation. Le point reste ouvert jusqu’à la lecture des propriétaires.

### Sortie vers ACTION

La ligne 27 dit que « la sortie de DIRECTION vers ACTION réutilise intégralement `ACTION/HANDOFF` », y compris `OBSERVATION/METHOD`, `DECISION-CHANGE` et les éléments de clôture. Or ACTION précise qu’une sortie incapable de fournir ces éléments reste une préparation ou une décision non clôturée. Avant le build, une observation et un changement de décision peuvent légitimement ne pas encore exister.

Le défaut n’est pas que ces informations soient demandées à la clôture. Le problème est que le terme unique « sortie de DIRECTION » couvre au moins deux moments :

- handoff de cadrage vers la construction et la preuve ;
- restitution après observation vers la décision et la clôture.

Cette ambiguïté peut pousser un agent à remplir prématurément `DECISION-CHANGE`, à employer `N/A-JUSTIFIED` pour un élément simplement futur, ou à croire qu’un handoff de préparation est déjà complet. ACTION distingue pourtant non-applicabilité, non-observation et préparation incomplète.

### Trois contrats

`ROUTE`, `TARGET` et `HANDOFF` donnent un modèle mental utile. Leur séparation devrait rester. La colonne HANDOFF mentionne toutefois « après observation » dans le même contrat que l’exécution à venir. Il faudra décider si HANDOFF est un contenant évolutif avec états temporels explicites, ou s’il faut distinguer le handoff initial de la restitution vers ACTION sans créer un nouveau contrat concurrent.

### Priorités et qualité

La relation P0–P3 est cohérente avec ACTION et SAVOIR : le risque dominant est vérifié d’abord ; sur une surface identitaire sans risque critique, P0 précède le contrôle du plancher P1 ; un risque critique passe avant le craft. Le texte empêche explicitement d’utiliser cette priorité pour sacrifier usage, accessibilité ou sécurité.

L’exigence d’un premier rendu construit et jugeable est également cohérente avec ACTION et SAVOIR. Le terme « polie par défaut » est plus fort et plus subjectif que « suffisamment résolu pour être jugé », mais la phrase suivante le borne par le mode, le contexte et l’absence de verdict automatique. Ce point reste à examiner avec les modes LITE, ITER et STANDARD avant de conclure à une sur-prescription.

## Passage C — usage simulé

### Agent sous contrainte de temps

L’agent comprend vite qu’il doit classer, déclarer le risque et charger conditionnellement. Il peut toutefois hésiter entre la table d’activation, la carte en trente secondes et la chaîne interne. L’inversion `FIRST-OBJECT` / `VISUAL_TARGET` est opérationnelle : suivre la ligne 72 littéralement peut conduire à construire avant d’avoir rendu la cible pilotable.

L’agent peut aussi traiter les treize éléments d’`ACTION/HANDOFF` comme des champs immédiatement obligatoires. La mention de `N/A-JUSTIFIED` offre alors une échappatoire formelle : marquer « non applicable » ce qui est seulement « pas encore observé ».

### Designer

Le designer reçoit une ambition créative claire et une protection contre le rendu générique. Les descriptions de présence, composition, matière, type et spécificité donnent une direction positive. La multiplication des vues de cadrage peut néanmoins sembler être plusieurs briefings successifs si le mécanisme de réutilisation de l’information n’est pas matérialisé par un exemple ou un mapping.

### Reviewer

Le reviewer sait que conformité technique, direction visuelle et preuve d’usage ne se compensent pas. Le bloc ne lui permet pas encore de déterminer quelle représentation de la séquence est normative en cas de désaccord.

### Mainteneur et système automatique

Le mainteneur dispose de propriétaires et de locators. Le système automatique ne possède pas encore un mapping complet entre les sorties locales (`promesse`, `thèse`, `relation`, `anti-direction`, `exclusion`) et la projection machine. La ligne 88 donne une règle sémantique de déduplication, mais pas un contrat testable.

## Passage D — résistance

### F-DIR-001 — ordre interne contradictoire

- Gravité provisoire : **Significatif**
- Preuve : lignes 47–55 contre ligne 72 ; confirmation par ACTION, READING_MAP et QUICKSTART
- Risque : construire un premier objet avant la cible, ou produire des lectures différentes selon la façade choisie
- Propriétaire pressenti : DIRECTION, avec alignement des guides dérivés
- Test futur : une seule séquence causale résolue dans DIRECTION, ACTION, QUICKSTART et READING_MAP
- Décision actuelle : défaut confirmé, patch différé jusqu’à la lecture complète

### F-DIR-002 — claim d’efficacité non démontré

- Gravité provisoire : **Significatif**
- Preuve : ligne 74 affirme que le système « augmente la probabilité d’un travail de niveau expert » ; le README classe l’efficacité sur des runs réels `NOT-VERIFIED` et les release notes déclarent l’efficacité et la supériorité non démontrées
- Risque : présenter une hypothèse de valeur comme un résultat établi
- Propriétaire pressenti : DIRECTION pour le claim local, avec cohérence README/release
- Correction probable à éprouver : exprimer l’objectif ou l’hypothèse, puis réserver l’affirmation causale aux pilotes
- Décision actuelle : contradiction épistémique confirmée ; formulation finale après audit du corpus

### F-DIR-003 — handoff sans temporalité explicite

- Gravité provisoire : **Significatif**
- Preuve : lignes 27 et 37 réunissent données de cadrage, observation et clôture ; ACTION distingue préparation, sortie de run et clôture
- Risque : `DECISION-CHANGE` prématuré, faux `N/A-JUSTIFIED`, impression de preuve complète
- Propriétaire pressenti : ACTION possède le contrat HANDOFF ; DIRECTION doit le projeter sans en changer le sens
- Prochaine vérification : lire `ACTION/HANDOFF`, `ACTION/RUN_CARD`, les exemples et le schéma sur le cycle de vie des champs
- Décision actuelle : risque fortement étayé, défaut final à confirmer à l’interface DIRECTION → ACTION

### F-DIR-004 — portée déclarée possiblement plus étroite que la portée appliquée

- Gravité provisoire : **Observation**
- Preuve : ligne 74 limite la cible exprimée aux interfaces et frontends web/natifs ; d’autres parties du corpus traitent print, signalétique, spatial, vidéo, jeu et embarqué
- Risque : mauvaise attente sur les médiums réellement couverts et sur la transférabilité des preuves
- Prochaine vérification : lire les sections de médium et les contrats non web avant classement
- Décision actuelle : ouverte

### F-DIR-005 — légende partiellement inactive

- Gravité provisoire : **Mineur / Observation**
- Preuve : dans DIRECTION, `[RECOMMANDÉ]` et `[À ADAPTER]` n’apparaissent que dans la légende ; `[ABSOLU]` est expliqué alors que les titres emploient `[ABSOLU 1 — …]`
- Risque : charge cognitive faible mais inutile, doute sur la portée locale ou transversale de la légende
- Prochaine vérification : déterminer si la légende est volontairement inter-document et si les tags sont validés par script
- Décision actuelle : ouverte

### F-DIR-006 — mapping informel entre vues et projection

- Gravité provisoire : **Observation**
- Preuve : ligne 88 demande de conserver l’information dans la vue qui la rend décisionnelle et de renvoyer les autres vues ; aucun mapping machine complet n’est donné ici
- Risque : duplications différentes selon l’agent, perte de provenance ou divergence entre trace humaine et `RUN_CARD`
- Prochaine vérification : schéma, exemple, `ACTION/RUN_CARD` et contrats de production
- Décision actuelle : ouverte

## Ce que le bloc réussit déjà et qu’une correction doit préserver

1. Le statut expérimental est visible dès l’entrée.
2. Les propriétaires de classification, preuve, jugement, structure et gouvernance sont séparés.
3. La condition d’arrêt combat directement la lecture et la documentation sans conséquence.
4. Les modules sont conditionnels à une décision modifiable.
5. La qualité créative est formulée positivement, au-delà de la conformité et de l’anti-slop.
6. Le risque critique prévaut explicitement sur l’optimisation visuelle.
7. Aucune taxonomie n’est censée compenser une autre.
8. Les adjectifs comme « premium » ou « beau » doivent devenir des relations observables.
9. Une source ou observation locale ne devient pas une règle partagée sans promotion.

## Couverture du bloc

| Passage de phase 2 | Profondeur | État |
|---|---|---|
| A — Architecture visible | FULL | Effectué sur les lignes 1–109 et comparé aux principales façades |
| B — Contrat sémantique | FULL | Effectué ; plusieurs interfaces restent à confirmer |
| C — Usage réel | TARGETED | Agent, designer, reviewer, mainteneur et système automatique simulés |
| D — Résistance | FULL | Six constats ou observations enregistrés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc commence par `DIRECTION/SERVICE-BOUNDARY`, puis `DIRECTION/START`, en vérifiant d’abord les constats F-DIR-001 à F-DIR-006 lorsque les nouvelles sections les touchent.
