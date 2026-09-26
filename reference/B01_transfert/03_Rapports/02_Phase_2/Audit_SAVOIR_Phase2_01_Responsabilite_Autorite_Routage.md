# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 1

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **1–84** ; ligne 85 vide, `SAVOIR/FRAME` commence à la ligne 86.
- Sections : statut de l’expérimentation et responsabilité, frontières avec les quatre autres propriétaires, orientation interne et handoff vers ACTION, `SAVOIR/READ`, `SAVOIR/FAST-PATH`, niveaux d’autorité, `SAVOIR/ROUTING`.
- Interfaces relues : checkpoints consolidés DIRECTION et ACTION, §12 du protocole, `DIRECTION/START`, `ACTION/HANDOFF`, `ACTION/PRECONDITION`, `ACTION/STATUS`, `ACTION/ROUTING`, `ACTION/GATE-A`, `READING_MAP`, `CHANGELOG`, titres des routes spécialisées de SAVOIR, lecteur et validateur de routes.
- Baseline B01 revérifiée : système `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, SAVOIR extrait et package identiques `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Méthode : quatre passages de la phase 2, inspection des titres et des routes réellement chargeables, simulation de décisions cumulées et confrontation aux constats F-DIR et F-ACT. Ni verdict global ni patch du corpus.

## Résumé du bloc

SAVOIR se place correctement comme propriétaire du **jugement situé** : il aide à décider comment cadrer, composer, vérifier et nommer une limite, puis renvoie à ACTION pour observation, preuve et verdict. Les sept tags évitent de traiter une opinion de design, une méthode, une obligation spécialisée, une veille datée et une source dépréciée comme s’ils avaient la même force. Le fast path conserve risque dominant et conséquence positive/négative sans exiger un dossier complet.

Deux tensions apparaissent à l’entrée. Le lecteur fourni ouvre `SAVOIR/READ`, `/ROUTING` et `/CRAFT`, mais refuse onze autres locators cités ou titrés par cette façade, y compris `/FRAME` et `/FAST-PATH`; leurs sections existent dans le fichier et restent trouvables manuellement. Cette occurrence confirme F-DIR-028 et F-ACT-001. De plus, « charger zéro, une ou deux routes » peut être pris comme plafond alors qu’ACTION cible parfois trois routes SAVOIR ou davantage pour des responsabilités distinctes et applicables. Cette tension reçoit **F-SAV-001**, provisoire et à éprouver sur un run réel ; la formule de SAVOIR peut aussi avoir été voulue comme recommandation de départ, et non comme plafond normatif.

## Passage A — architecture visible

| Lignes | Rôle du segment | Sortie / limite |
|---|---|---|
| 1–3 | Positionne SAVOIR comme bibliothèque de jugement dans une expérimentation maintenue | Limites d’usage explicites ; pas de prétention à une release stabilisée |
| 5–22 | Décrit sa capacité positive et réserve classification, exécution probante, structure et adoption aux propriétaires correspondants | Une méthode ou une ancre ne vaut pas preuve ni PASS |
| 26–32 | `ROUTING` comme carte principale, route principale puis renvoi conditionnel, handoff en sept éléments et arrêt de lecture | « Aucune décision ne change » renvoie à `N/A-JUSTIFIED`, à relire avec confirmation et changement de preuve |
| 34–44 | `READ` et `FAST-PATH` réduisent la charge de lecture et les sorties d’un delta local | « Zéro, une ou deux » risque d’être interprété comme plafond ; preuve critique préservée |
| 48–64 | Sept tags d’autorité et cadre de claims datés | Méthode ≠ résultat ; N/A doit être justifiée dans le scope ; veille non adoptée par défaut |
| 66–83 | Onze routes principales par type de question, renvois ciblés | Tout renvoi ne crée pas une seconde procédure ; pas de maximum explicite dans la table |

L’architecture documentaire est intelligible : DIRECTION classe, SAVOIR aide à juger, BIBLIOTHEQUE propose la structure, ACTION exécute la preuve et ferme, CHANGELOG gouverne l’adoption. `READING_MAP` est explicitement dérivé. Les routes spécialisées portent des titres réels dans SAVOIR ; l’entrée reste lisible à la main même si un agent outillé échoue sur leur locator. Le FAST-PATH de SAVOIR est une vue de jugement, distincte des vues homonymes de DIRECTION et d’ACTION ; son existence ne crée pas un sixième mode de run.

### Résolution des routes annoncées

Test sur B01 avec `scripts/read_route.py`, confronté aux titres exacts du propriétaire :

| Locators | CLI | Titres propriétaires |
|---|---|---|
| `SAVOIR/READ`, `/ROUTING`, `/CRAFT` | PASS (3) | Présents |
| `SAVOIR/FAST-PATH`, `/FRAME`, `/TYPE`, `/STATE`, `/SOURCE`, `/STYLE`, `/SYSTEM`, `/CONTEXT`, `/TECH`, `/TOOLS`, `/INTEGRITY` | FAIL (11) | Présents |
| `ACTION/GATE-A`, `ACTION/RUN-SYSTEM` (renvois) | PASS | Présents dans ACTION |

Le validateur officiel de `READING_MAP` annonce `READING MAP VALIDATION PASSED` alors que `read_route.py SAVOIR/FRAME` échoue. Il vérifie notamment les locators listés dans la carte, pas la totalité des appels normatifs issus de SAVOIR. Ce point ne crée pas un nouvel ID par route : F-DIR-028 porte la couverture du lecteur, F-ACT-001 l’effet sur le chargement et les minima par mode. Une recherche de titre manuel peut retrouver les 11 sections ; on ne doit donc pas écrire qu’elles sont absentes du corpus.

## Passage B — contrat sémantique, phrase et section par section

### Responsabilité et frontière de vérité (1–22)

« Comment exercer le jugement » donne une fonction positive : de l’impression à un levier, une décision située, une contre-indication et une limite. La phrase « ne remplace ni observation réelle d’ACTION, ni décision de clôture, ni contexte humain » protège la frontière épistémique. La table des quatre autres propriétaires évite que SAVOIR reclasse le mode, délivre une permission de publication, instaure une structure obligatoire ou promeuve une règle seul. La phrase finale interdit explicitement qu’un texte de principe, une ancre ou un profil produise automatiquement un `PASS` d’usage, d’accessibilité ou de qualité.

Le « chemin par problème » cite `FRAME`, `CRAFT`, `TYPE`, `STATE`, `CONTEXT`, `SOURCE`, `STYLE`, `SYSTEM`, `TECH`, `TOOLS` et `INTEGRITY` selon une décision ou une preuve à modifier. Il refuse le chargement réflexe. Sa qualité dépend néanmoins de la possibilité de retrouver chaque source spécialisée et de ne pas confondre « le prochain artefact ne bouge pas » avec « la méthode ou le statut de preuve ne change pas ». F-ACT-004 et F-DIR-037 restent pertinents, mais la première phrase de SAVOIR est plus large que le déclencheur étroit observé dans ACTION.

### Orientation, sortie et arrêt (26–32)

La route principale traite une question ; les renvois interviennent seulement s’ils peuvent changer décision, preuve ou limite. La sortie conserve décision jugée, principe/méthode, conséquence observable, preuve attendue, limite, owner et prochaine preuve. Ce paquet n’est pas un verdict et ne remplace pas `ACTION/HANDOFF`, plus large pour la clôture d’un run. La condition d’arrêt de lecture exige question, levier, contre-indication, limite et prochaine observation, sans imposer tous les chapitres.

« Si aucune décision ne change, retournez `N/A-JUSTIFIED` » est plus étroit si on le lit comme « rien n’a été modifié ». `ACTION/PRECONDITION` compte aussi la confirmation ou l’abandon réellement motivés par l’observation ; une route peut changer seulement le choix de preuve, la limite ou la prochaine vérification. Le risque de classer un résultat utile comme non applicable réactive F-DIR-011/019 et F-ACT-013/014. Il faudra tester cette lecture avec SAVOIR/INTEGRITY et la projection sans créer une taxonomie concurrente.

### READ, FAST-PATH et tags (34–64)

`READ` distingue correctement zéro route SAVOIR (jugement inchangé) du maintien des contrôles ACTION applicables. `FAST-PATH` réduit sa trace à décision touchée, risque dominant, principe utile, preuve la moins coûteuse et conséquence selon deux résultats ; il refuse que le coût documentaire efface une preuve critique. Un contrôle marqué `[REQUIS PAR LE MODULE — scope]` demeure applicable même si l’ensemble de SAVOIR n’est pas chargé. `N/A-JUSTIFIED` doit signifier non-applicabilité justifiée du contrôle dans le scope, et non indisponibilité de preuve ou manque de temps ; la table des tags ne crée pas un PASS par déclaration.

`[DURABLE]` guide sans transformer une préférence située en loi empirique ; `[MÉTHODE]` décrit un raisonnement adaptable ; `[À ADAPTER]` appelle justification ; `[VEILLE]` exige vérification avant usage factuel ; `[OPINION DE SYSTÈME]` reste hypothèse ; `[DÉPRÉCIÉ]` exclut une instruction active pour un nouveau run. `SAVOIR/TOOLS` porte le contrat des claims externes ; ce bloc n’en prouve pas encore la mise en œuvre dans chaque route. Les vérifications précises de sourcing et de temporalité attendent son bloc propriétaire et les contrats machine.

### ROUTING (66–83)

Le tableau donne onze questions dont chacune possède une route principale et des renvois. Les routes ne sont pas onze obligations universelles : un composant existant local sans nouvelle décision de structure peut demander `STATE` et aucune sélection BIBLIOTHEQUE ; une source datée qui modifie une claim ajoute `TOOLS`. L’usage de préfixes abrégés dans les renvois (`SOURCE`, `STYLE`, `TECH`) s’interprète grâce à la colonne propriétaire, mais n’est pas une clé littérale de la CLI. Le risque de clé absente relève déjà de F-DIR-028.

Le groupement « accessibilité, responsive, performance, motion, risque critique » conduit à `SAVOIR/CONTEXT`, puis mentionne `ACTION/GATE-A` et « l’axe T ». Or `ACTION/STATUS` place les contrôles d’accessibilité dans **A** et performance/responsive dans **T** ; un même cas peut toucher les deux axes. La mention de T peut être additive et n’ordonne pas explicitement d’omettre A. On conserve cette **ambiguïté locale à vérifier** lors de `SAVOIR/CONTEXT`, `ACTION/GATE-A` et des parcours A/T en phase 9, sans prétendre que la route a déjà déplacé tous les contrôles d’accessibilité vers T.

## Passage C — lecteurs sous contrainte de temps

1. Un designer corrige une microcopie locale, avec le même risque et sans changement de décision de jugement : zéro route spécialisée peut être raisonnable, mais la preuve et la trace proportionnée d’ACTION restent applicables.
2. Un designer prépare une nouvelle surface identitaire multilingue avec une image externe et des contraintes de clavier/focus : CRAFT, TYPE, SOURCE et CONTEXT ont quatre questions distinctes. Une lecture littérale « au plus deux routes » risque d’en laisser deux de côté ; une lecture proportionnée les charge si chacune change un levier, une preuve ou une limite.
3. Un agent reçoit `SAVOIR/FRAME` comme prochaine route. Le titre existe ligne 86, mais la CLI refuse le locator ; il ne doit ni halluciner une règle ni conclure que le chapitre est supprimé. Il ouvre le propriétaire et recherche son titre.
4. Un reviewer voit un tag `[VEILLE]` devant un outil actuel : il vérifie source, date, portée et limite avant d’utiliser une claim ; il n’en déduit ni PASS d’ACTION ni permission d’exécuter l’outil.
5. Un intégrateur termine un rendu déjà suffisant après examen : « décision confirmée » est un résultat possible ; une prochaine preuve différente est transportée. `N/A-JUSTIFIED` ne doit être utilisé que pour une vraie non-applicabilité, pas pour masquer l’observation.
6. Un mainteneur trouve une exigence `[REQUIS PAR LE MODULE]` dans une route non chargée au premier passage : il identifie le scope déclencheur et fait exécuter le contrôle ou documente sa non-applicabilité, sans charger tout SAVOIR ni inventer un PASS.

## Passage D — résistance et registre

### F-SAV-001 — « zéro, une ou deux routes » peut devenir un plafond alors que plusieurs questions indépendantes sont applicables

- Gravité : **Significatif provisoire**.
- État : **contradiction documentaire confirmée, impact réel à tester**. La formulation peut être une recommandation de charge typique ; aucun validateur n’impose ce plafond. Elle n’est pas décrite comme quota formel, mais elle ne précise pas non plus ce qu’il faut faire à trois routes ou davantage.
- Preuve : `SAVOIR/READ` ligne 38 limite la liste de chargement à zéro, une ou deux routes ; `SAVOIR/ROUTING` lignes 68–82 répartit onze questions, `SAVOIR/READ` ligne 40 exige d’exécuter/tracer les obligations spécialisées applicables ; `ACTION/ROUTING` ligne 876 appelle CRAFT, TYPE, SOURCE et parfois STYLE pour une spec DIRECTION, et CONTEXT dès qu’un risque pertinent apparaît.
- Contre-exemple : une surface DIRECTION multilingue avec asset externe et accessibilité active sollicite, pour des décisions distinctes, CRAFT, TYPE, SOURCE et CONTEXT. Si « deux » est un maximum, deux sujets peuvent être traités sans ouvrir leurs critères propriétaires ni transporter leur limite.
- Risque : typographie sans glyphes/fallback/licence, asset sans provenance/droit/limite ou accessibilité sans méthode adaptée ; sortie propre en apparence mais incomplète. Le risque augmente si l’agent applique la phrase comme quota au lieu de charger selon le risque.
- Atténuation : la section exige une route supplémentaire lorsqu’elle change question, preuve ou limite ; le tableau n’écrit pas « maximum deux » ; les tags `[REQUIS]` et les gates ACTION demeurent des protections même sans lecture intégrale de SAVOIR.
- Relations : F-ACT-004 (déclencheur trop étroit sur le prochain artefact), F-ACT-001/F-DIR-028 (chargement outillé), F-ACT-029 (conditions d’activation de contrats), F-DIR-012 (autre cardinalité du Creative Boot, cause distincte), F-DIR-042 (propriétaires spécialisés omis).
- Propriétaire pressenti : SAVOIR/READ et /ROUTING pour l’intention du nombre et l’exception quand des questions distinctes sont actives ; ACTION/ROUTING pour la sélection transversale, sans imposer un chargement universel.
- Test futur : zéro, une, deux, trois et quatre questions indépendantes, chacune avec décision/preuve/limite changeante ou non ; cas critique et cas local ; vérifier que toute obligation applicable est exécutée ou réellement N/A, tout en arrêtant le chargement inutile.

### Occurrences sans nouvel ID

| Observation | Relation existante ou vérification différée |
|---|---|
| Onze titres SAVOIR existants mais non chargeables par la CLI ; validation de READING_MAP verte | F-DIR-028 et F-ACT-001, sans nouvel ID par locator |
| Route utile lorsque seul le statut de preuve ou la limite change | F-ACT-004, F-DIR-037 ; SAVOIR donne une formulation plus large |
| `N/A-JUSTIFIED` conseillé si « aucune décision ne change » alors qu’une confirmation ou un changement de preuve peut être utile | F-DIR-011/019 et F-ACT-013/014 ; préciser la lecture avec ACTION |
| CONTEXT mentionne T et GATE-A sans nommer A dans le même renvoi | Observation A/T ouverte ; ACTION définit A et T, ne pas inférer leur fusion |
| INTEGRITY a plus loin un déclencheur obligatoire avant verdict DIRECTION, absent du tableau courant « récitation/limite/délégation » | Réserver l’examen définitif au bloc propriétaire INTEGRITY (ligne 851) et au routage inter-fichiers |

## Protections positives à préserver

1. SAVOIR augmente la précision du jugement et la qualité du premier objet, sans se déclarer preuve ou verdict.
2. La frontière DIRECTION/ACTION/SAVOIR/BIBLIOTHEQUE/CHANGELOG est explicite.
3. La question active et le risque décident du chargement, avec une route principale et des renvois utiles.
4. Une obligation spécialisée demeure applicable dans son scope même si la bibliothèque entière n’est pas chargée.
5. Le FAST-PATH réduit le dossier mais pas le contrôle critique ni la qualité de la décision.
6. Les sept tags séparent principe, méthode, obligation, adaptation, veille, opinion et dépréciation ; ils ne transforment pas un texte en observation empirique.
7. La trace SAVOIR transmet décision, méthode, conséquence, preuve attendue, limite, owner et prochaine preuve à ACTION.
8. Les axes A/T suivent l’objet réellement touché et le périmètre de preuve ; aucune route ne remplace la taxonomie canonique ACTION.
9. Aucun quota de références, d’itérations, de formes ou de routes ne doit évincer une responsabilité réellement applicable.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture visible | FULL | Entrée et hiérarchie des sections, sept tags, onze routes et quatorze locators SAVOIR comparés |
| B — sémantique | FULL | Propriété, déclencheurs, transmission, non-applicabilité, preuve, autorité et contre-indications |
| C — usage réel | TARGETED | Six scénarios designer, agent, reviewer, intégrateur et mainteneur |
| D — résistance | TARGETED | Un nouveau constat provisoire ; cinq occurrences/ambiguïtés suivies sans duplication |
| Machine | TARGETED | 3 routes chargées / 11 rejetées, titres présents ; `validate_reading_map.py` vert |
| Externe | N/A-JUSTIFIED | Aucun claim extérieur nouveau n’est décidé dans ce bloc |

Le bloc 1 est lu sans verdict global ni patch. La prochaine unité est **SAVOIR.md, lignes 86–192**, `SAVOIR/FRAME` : principe FND-01, compromis FND-02, cadrage FND-03, qualité du premier rendu et one-shot. La ligne 193 est séparatrice, la ligne 194 vide et `SAVOIR/CRAFT` commence à la ligne 195. Elle devra rejouer F-SAV-001 seulement si FRAME active réellement une question supplémentaire ; F-DIR-011/019, F-ACT-004 et F-ACT-013/014 restent des réserves indépendantes.
