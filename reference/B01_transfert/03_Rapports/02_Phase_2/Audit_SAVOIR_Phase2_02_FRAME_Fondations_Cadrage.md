# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 2 : FRAME

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **86–192** : `FND-01` (88–149), `FND-02` (151–162) et `FND-03` (164–191). La ligne 193 sépare le bloc ; `SAVOIR/CRAFT` commence à 195. La section explicite « Qualité du premier rendu, one-shot et preuve » commence à **199** et sera analysée au prochain bloc.
- Protocole : §12, quatre passages A–D ; continuité vérifiée avec le rapport SAVOIR bloc 1, le plan maître et les checkpoints DIRECTION/ACTION. Interfaces vérifiées : `ACTION/HANDOFF`, `RUN_CARD`, `PIPELINE-DIRECTION`, `GATE-B`, `DIRECTION/ABSOLU 5`, schéma et validateur de `RUN_CARD`.
- Baseline B01 inchangée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Nature du résultat : diagnostic sectionnel provisoire, sans patch et sans verdict global sur le système. Les tests de carte décrivent la portée du validateur, pas la qualité d’un run observé sur le terrain.

## Résumé du bloc

FRAME apporte un jugement de conception situé : ordre des décisions, singularité compatible avec les conventions, pluralité esthétique, compromis explicite et cadrage du public, de la tâche et des hypothèses. Son obligation de cadrage s’applique à toute tâche de surface ; une ligne compacte est permise en LITE **uniquement** pour une modification réellement locale. Cette portée apporte un exemple supplémentaire à F-SAV-001 : une route FRAME peut devenir applicable en même temps que plusieurs autres routes spécialisées, sans démontrer pour autant qu’il faudrait charger tout SAVOIR.

Deux frontières demandent une lecture prudente. L’« ouverture par plusieurs directions » est une méthode de réflexion et ne doit pas se muer en nombre imposé d’artefacts, au regard du pipeline ACTION qui permet de passer sans variante artificielle. Les champs humains du cadrage ne se projettent pas tous dans `RUN_CARD` : la carte n’accepte pas `user_input_required`, une carte avec seule revue experte peut être validée structurellement, et la liste courte de FRAME omet `DECISION` ainsi que `DECISION-INTENT` pourtant exigés par ACTION. Les constats de mapping et de clôture déjà ouverts portent ces écarts ; aucun nouvel ID n’est justifié à ce stade.

## Passage A — architecture visible

| Segment | Autorité et fonction | Interface décisive |
|---|---|---|
| FND-01, 88–100 | `[DURABLE]` : intention, retenue, cohérence et qualité justifiée par la tâche | Principe de jugement, explicitement pas une loi empirique (92) |
| 102–112 | `[OPINION DE SYSTÈME]` sur le premium ; `[MÉTHODE]` comprendre/ouvrir/converger/prouver | Aucune mesure ni preuve automatique ; renvoi à l’artefact et à l’observation ACTION |
| 114–149 | Convention légitime, grammaire positive de composition, `[À ADAPTER]` pour le goût situé | `ACTION/ANTI-SLOP`, états, contexte culturel, contrepoint pertinent |
| FND-02, 151–162 | `[DURABLE]` : décision, dette, réversibilité, owner et prochaine preuve | V/U/A/T d’ACTION, sans nouveau score |
| FND-03, 164–191 | `[REQUIS PAR LE MODULE — toute tâche de surface]` : cadrage puis hypothèse tracée | Handoff, `RUN_CARD`, choix `USER/TASK`, axe de risque et preuve applicable |

La façade SAVOIR pointait déjà vers `SAVOIR/FRAME`, dont le titre existe ; le lecteur de route le refuse sur B01 (F-DIR-028/F-ACT-001, vérifiés dans le bloc 1). Ici, la recherche manuelle du titre a permis de lire la section. L’obligation FND-03 dépend du **scope** de la tâche, pas du succès de cette CLI ; ne pas charger la route par l’outil ne justifie pas d’ignorer son contrôle applicable.

## Passage B — contrat sémantique, section par section

### FND-01 : jugement et capacité positive (88–149)

Les « trois lois » (94–100) sont un ordre de critique : tout effet expressif doit servir le JTBD, la compréhension ou la direction ; la qualification « principe et non loi empirique » (92) limite la force d’un argument d’autorité. Le premium à cinq facettes (102–106) est expressément une opinion de système, sans score scientifique ou verdict ; une palette sombre ou un minimalisme ne suffisent pas. Une direction peut être intense, tactile ou ludique si elle sert le contexte.

Le cycle comprendre/ouvrir/converger/prouver (108–112) produit une décision et une preuve attendue, **pas** une route supplémentaire ni une preuve issue d’une référence. « Plusieurs directions réellement distinctes » (110) peut être compris comme des hypothèses explorées, ou à tort comme des variantes livrables obligatoires. Le même alinéa conditionne l’alternative à son utilité ; `ACTION/PIPELINE-DIRECTION` (459, 467–471) interdit le quota et permet de noter qu’aucune alternative située ne change la décision. La rédaction reste ambiguë pour un lecteur pressé ; on ne l’interprète pas comme l’obligation démontrée de construire deux scènes. F-DIR-009 concerne, lui, une **modification et une réobservation** exigées ailleurs malgré un one-shot suffisant ; F-DIR-012 porte une cardinalité distincte du Creative Boot.

Le test « sans logo ni nom » (116) recherche ce qui reste propre à la tâche, à la donnée, à la voix et aux états. Les conventions qui servent un genre restent légitimes (118) ; la ressemblance n’est pas une faute automatique, et `ACTION/ANTI-SLOP` possède le flag (120). L’ordre JTBD → structure → hiérarchie → lisibilité → accessibilité → système visuel → polish (122) et la survie au contenu long et au responsive (124) empêchent de maquiller une architecture faible par des effets.

La grammaire de composition (126–139) est un outil productif, expressément ni recette de style ni checklist obligatoire. La pluralité (141–149) rejette le canon esthétique implicite, demande de nommer le public et le contexte, et recommande un contrepoint situé si disponible pour une décision identitaire, culturelle ou irréversible. Ce contrepoint ne garantit ni neutralité ni validité ; la méthode de preuve et la limite restent à déclarer. La dernière question distingue préférence, inadéquation réelle et risque critique sans imposer de variantes fictives. Le propriétaire ACTION de la revue indépendante et la preuve avec personnes concernées restent applicables selon leurs propres déclencheurs.

### FND-02 : compromis (151–162)

Le format rend visibles la préférence de X sur Y, la raison Z, le risque résiduel, le signal de réversibilité, l’owner et la prochaine preuve. Il alimente V/U/A/T sans score concurrent. La dette d’usage, d’accessibilité, de performance ou de confiance doit être explicitée ; le fait de la nommer ne transforme pas un risque critique interdit en compromis acceptable. Les protections et issues d’ACTION conservent leur autorité.

### FND-03 : cadrage, hypothèses, transmission (164–191)

Le déclencheur de la ligne 166 est large et clair : **toute tâche de surface** ; seul le format est compactable pour un LITE réellement local. Les cinq questions (170–174) lient personne, JTBD, décision dominante, preuve et contraintes. Une inconnue doit devenir une hypothèse avec impact ; les lignes 176–183 demandent nature/confiance, source/coût d’erreur, owner/prochaine preuve et `User input requis` (`YES`, `NO` ou `NOT-REQUIRED`). `N/A-JUSTIFIED` reste un motif de non-applicabilité séparé, pas un verdict.

La ligne 185 appelle ces éléments « projection lisible » et énumère un minimum de handoff mais laisse de côté `DECISION` de `ACTION/HANDOFF` (28) et `DECISION-INTENT` de `ACTION/RUN_CARD` (268–270). Sa formule « `RUN_CARD` ou trace équivalente » doit être réconciliée avec ACTION : un run persistant requiert la projection `RUN_CARD` et son validateur (ACTION 33), alors qu’une trace non persistante peut être proportionnée à son mode. La ligne 185 n’abolit donc pas la projection persistante. En l’état, l’aller-retour entre la table des hypothèses, le handoff textuel et la carte validée n’est pas explicité champ par champ (F-ACT-002, F-DIR-008).

La ligne 189 demande `USER/TASK` lorsque l’utilisabilité réelle domine, avec personne, tâche, contexte, échantillon et résultat ; lorsqu’une population ou l’accessibilité domine, elle laisse choisir `USER`, `EXPERT` ou personne concernée en justifiant la méthode. `DIRECTION/ABSOLU 5` (632) ajoute une protection plus stricte dans certains cas : personnes représentatives observées, **ou** impossibilité explicitée avec owner et prochaine preuve ; expertise et conformité seules ne remplacent pas automatiquement l’observation. Ces phrases peuvent se lire ensemble si le choix `EXPERT` ne dispense pas silencieusement du justificatif et de la limite quand le déclencheur supérieur est actif. ACTION doit porter axes, statut et limites de preuve ; le validateur seul ne vérifie pas cette obligation. La ligne 191 prolonge le cadrage vers l’architecture d’information et les cas limites (erreur, permission, succès partiel, localisation).

## Passage C — lecteurs sous contrainte de temps

1. **Designer, correction de microcopie locale LITE.** Il formule en une ligne qui lit, l’action touchée, la contrainte et la preuve ; il ne transforme pas « ligne compacte » en dispense si la formulation change une hypothèse de public ou une action critique.
2. **Équipe produit, direction identitaire encore ouverte.** Elle compare mentalement plusieurs possibilités réelles, matérialise la proposition principale et seulement une alternative qui change une décision ; référence et moodboard restent des ancres, l’artefact observé sert la preuve. L’absence de seconde variante n’est pas automatiquement un défaut.
3. **Reviewer, direction expressive atypique.** Il demande quelle présence ou mémoire cette expression sert, ce qui tient sous contenu réel, et une observation distinguant goût et inadéquation ; il ne prononce pas « slop » sur une simple ressemblance.
4. **Intégrateur, tâche critique accessible.** Il peut remplir le champ `EXPERT` en texte, puis clôturer une carte sans observation de personne représentative ; la fermeture structurelle est possible, mais le niveau de preuve de la claim reste à juger par ACTION et la justification de l’impossibilité doit demeurer visible.
5. **Agent de transfert vers ACTION.** Il copie la liste courte de FRAME comme si elle était exhaustive, oublie `DECISION`/`DECISION-INTENT` et se heurte au validateur ; il reprend alors les minima de la source propriétaire au lieu d’inventer `user_input_required` dans le JSON.
6. **Mainteneur, route FRAME non résolue.** Il recherche le titre dans SAVOIR pour examiner le déclencheur `[REQUIS]`, conserve le problème du lecteur sous les constats existants et ne marque pas l’obligation N/A parce que la CLI échoue.

## Passage D — résistance, preuves ciblées et registre

### Épreuve machine sur copie de `schemas/run_card.example.json`

Le test met la carte en `STANDARD`, renseigne décision et intention, déclare un risque important, une revue experte de captures, l’absence de personne observée et la limite « test utilisateur à planifier » ; les champs propres à DIRECTION sont retirés pour ce mode. `validate_card` renvoie `None` (acceptation structurelle), alors que la méthode est « Expert seulement » et que l’absence d’observation humaine est explicitement inscrite dans `proof.not_verified`. Trois mutations indépendantes :

| Mutation | Résultat du validateur | Portée |
|---|---|---|
| Ajout de `run_card.user_input_required = YES` | Rejet : champ inconnu | La table humaine FND-03 n’a pas de slot structuré portant ce nom |
| Suppression de `run_card.decision` | Rejet : champ obligatoire absent | La liste de FRAME ligne 185 n’est pas exhaustive |
| Suppression de `run_card.decision_intent` | Rejet : champ obligatoire absent | ACTION garde cette exigence même quand FRAME ne la mentionne pas |

Ce test n’établit ni que la revue experte est toujours insuffisante, ni que tout run réel a été accepté illégitimement : le risque, la population et le statut exact de la claim déterminent le niveau de preuve ; une trace textuelle peut documenter l’exigence. Il établit que **cette validation de structure** ne déduit pas de ces mots l’obligation d’une preuve `USER/TASK` ou d’une justification d’impossibilité.

### Occurrences et suites, sans nouvel ID

| Observation du bloc | Constat / vérification à reprendre |
|---|---|
| FND-03 applicable à toute tâche de surface, cumul possible avec TYPE, SOURCE, CONTEXT, etc. | F-SAV-001 : éprouver trois routes et plus sans imposer le chargement intégral ; la multiplicité n’est pas un quota |
| « Ouvrir plusieurs directions » pourrait être pris pour plusieurs artefacts obligatoires | Ambiguïté mitigée par ACTION 459, 467–471 ; rapprocher de F-DIR-009/012, sans confondre leurs mécanismes ; rejouer avec le one-shot en phases 7 et 9 |
| Handoff FRAME omet `DECISION`/`DECISION-INTENT`; table d’hypothèses sans mapping explicite | F-ACT-002 et F-DIR-008 ; établir mapping et autorité de la trace persistante en phase 4 |
| `User input requis` non projeté, acceptation structurelle d’une revue experte seule | F-ACT-002/017/021 : tester si U/A dominant, population réelle, impossibilité et réserve gouvernent effectivement le verdict ; phase 9 |
| Opposition possible `EXPERT` ligne 189 / personnes représentatives DIRECTION 632 | Lire de façon cumulative ; tester un cas critique où `EXPERT` est choisi avec et sans justification de l’impossibilité ; pas de contradiction formellement confirmée |
| Compromis conscient contre protection critique | F-ACT-017/038 ; tester le cas réel et les décisions de gate sans affaiblir l’exigence de dette visible |

### Protections positives à préserver

1. Un principe de goût ou une opinion premium ne sont jamais présentés comme score empirique ou verdict.
2. Une convention utile, une forme expressive située et un premier objet spécifique peuvent tous être légitimes ; le contexte, la tâche et les états tranchent.
3. La pluralité appelle un regard situé sans prétendre qu’un reviewer externe est neutre ni forcer des variantes.
4. La preuve est associée à un artefact et à une observation réelle ; la référence reste une aide à décider.
5. Un compromis expose sa dette, sa réversibilité, son owner et sa prochaine preuve, sans remplacer les axes d’ACTION.
6. Le cadrage compact ne retire ni hypothèse à risque, ni personne concernée, ni limite de preuve.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Trois fondations, quatre tags et frontières de route |
| B — sémantique | FULL | Principe, méthode, opinion, adaptation, obligation, transmission, contre-indications |
| C — usage | TARGETED | Six lectures designer, produit, reviewer, intégrateur, agent et mainteneur |
| D — résistance | TARGETED | Scénarios, interfaces et constats reliés sans doublon |
| Machine | TARGETED | Une carte expert seul acceptée structurellement ; trois mutations rejetées comme attendu |
| Externe | N/A-JUSTIFIED | Aucun standard externe n’est mobilisé pour décider ce bloc documentaire |

Bloc 2 terminé **sans nouveau constat** et sans modification du système. La prochaine unité est `SAVOIR.md` lignes **195–280** : introduction `SAVOIR/CRAFT`, qualité du premier rendu et one-shot, `CFT-00` et `CFT-01`. `CFT-02` commence à 281. Relire le §12, ce rapport, la baseline et les réserves liées avant de commencer ce nouveau bloc.
