# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 4 : fin de CRAFT

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **281–376** : `CFT-02` alternative située (281–300), `CFT-03` composition (302–320), `CFT-04` émotion et `CFT-04a` premier contact (322–359), `CFT-05` couleur/contraste (361–373), séparateur 375. `SAVOIR/TYPE` commence à 377.
- Protocole externe : §12, quatre passages A–D. Rapports SAVOIR blocs 1–3, checkpoints DIRECTION/ACTION et plan maître relus pour la continuité. Interfaces vérifiées : `SAVOIR/FRAME`, `SAVOIR/TOOLS`, `SAVOIR/CONTEXT`, `DIRECTION/START`, `ACTION/PIPELINE-DIRECTION`, `ACTION/GATE-A`, `ACTION/POLICIES`, `ACTION/ANTI-SLOP` et `ACTION/RUN_CARD`.
- Baseline B01 revérifiée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`. Aucun patch du corpus.
- Le présent bloc examine le **contrat interne** du document. Il ne certifie pas une valeur externe de contraste, une version de standard, une causalité psychologique ni l’effet d’une palette sur un produit réel ; ces claims devront être vérifiés dans leurs phases et scopes applicables.

## Résumé du bloc

La fin de CRAFT donne des méthodes utiles pour explorer une alternative seulement si elle change une décision, composer selon le contenu, adapter l’émotion au public et choisir entre un objet concret et une promesse au premier contact. Elle protège nettement la frontière entre impression perceptuelle et preuve d’utilisabilité ou de conformité. La palette est pensée par rôles, le contraste exige un calcul selon ACTION, et les claims évolutifs passent par SAVOIR/TOOLS.

Un point local mérite un constat provisoire **F-SAV-002** : dans la section `[REQUIS PAR LE MODULE]` sur la couleur, la phrase « Les neutres portent l’essentiel de la structure ; l’accent signale… » (363) se lit comme un choix de palette prescrit pour toute surface concernée, alors que FRAME et CRAFT admettent des directions intensément colorées et aucune esthétique universelle. La règle peut avoir été voulue comme heuristique par défaut, mais elle ne le dit pas. Une lecture littérale pourrait neutraliser une identité où plusieurs couleurs construisent réellement l’espace et la hiérarchie. L’effet pratique reste à tester ; la correction éventuelle doit préserver les rôles sémantiques, le contraste et l’information non chromatique.

## Passage A — architecture visible

| Segment | Autorité / travail demandé | Frontière et sortie |
|---|---|---|
| `CFT-02`, 281–300 | `[MÉTHODE]` : six axes de direction ; alternative relative à public, contrainte, JTBD ou opportunité | Aucune variante matérialisée sans décision modifiable ; étiquettes culturelles à dater dans TOOLS |
| `CFT-03`, 302–320 | `[REQUIS PAR LE MODULE — surface identitaire, hiérarchie complexe ou revue perceptuelle]` : grille, densité, priorités, capture | Peut avoir plusieurs priorités liées ; perception ≠ utilisabilité prouvée |
| `CFT-04`, 322–344 | `[MÉTHODE]` : émotion viscérale, comportementale, réflexive ; leviers et contre-indications | Hypothèses culturelles/contextuelles, aucun effet émotionnel garanti |
| `CFT-04a`, 346–359 | `[À ADAPTER]` : premier contact par objet ou par geste/promesse, compromis selon rapport de personne | « Objet de preuve » est un objet de produit ; ACTION détient la preuve exécutée |
| `CFT-05`, 361–373 | `[REQUIS PAR LE MODULE — couleur, thème, statut ou surface identitaire]` : palette par rôles et contraste calculé | Palette documentée conditionnellement ; standard et résultat relèvent d’ACTION, claims datés de TOOLS |

Le lecteur `read_route.py SAVOIR/CRAFT` réussit et restitue les sous-sections `CFT-02` à `CFT-05` ; `validate_reading_map.py` passe également. L’existence de cette route ne signifie pas que chaque méthode de CRAFT devient obligatoire pour tout run. Les tags spécialisés `CFT-03` et `CFT-05` demandent, eux, d’examiner leur déclencheur même si l’agent n’ouvre pas tout le chapitre ; ils ne créent ni nouvelle route ACTION ni verdict séparé.

## Passage B — contrat sémantique, section par section

### CFT-02 : axes et alternative située (281–300)

Les six axes structure, matière, voix, temporalité, densité et rapport texte/image (285–292) sont des pôles de discussion, sans valeurs ou styles gagnants. La ligne 294 refuse le catalogue et la marginalité obligatoire. Une alternative n’est justifiée que par différence de contrainte, public, JTBD ou opportunité (296), et peut rester une phrase ou un schéma si cela suffit pour comparer (298). La ligne 300 reconnaît que des **étiquettes culturelles et exemples** vieillissent : `SAVOIR/TOOLS` les vérifie lorsqu’ils soutiennent un claim. `ACTION/PIPELINE-DIRECTION` (457–471) donne le même arrêt sans quota ; F-DIR-012 concerne une cardinalité imposée ailleurs, non une obligation dans CFT-02. Cette méthode est compatible avec un one-shot après observation, sous réserve des gates effectivement déclenchés, notamment la tension B1b déjà classée F-DIR-009.

### CFT-03 : composition, densité et harmonie (302–320)

Le déclencheur `[REQUIS]` de la ligne 304 est explicite. Grille, taille, espace et breakpoint sont des **diagnostics**, jamais des chiffres universels (306). Le responsive recompose selon tâche et contenu (308) ; une supervision peut avoir plusieurs décisions simultanément visibles (310) sans forcer une priorité unique. Cohérence de règles et harmonie des relations sont deux observations différentes (312–316) ; une tension ou une asymétrie peut être tenue plutôt que rejetée comme non conforme. Une matière issue du code doit justifier sa contribution avant d’être préférée à un asset externe (318), sans interdire ni l’un ni l’autre. L’observation sur capture d’harmonie et de clarté reste perceptuelle : lorsque U domine, une claim d’utilisabilité demande tâche, contexte et preuve d’usage (320). L’ordre « action et contenu lisibles avant la couleur » oriente la composition ; il n’autorise pas le report d’un contrôle de contraste déclenché par ACTION.

### CFT-04 : émotion située (322–344)

Le triptyque viscéral/comportemental/réflexif (328–330) distingue premiers signaux, expérience pendant l’usage et interprétation après interaction. Les associations calme, énergie, confiance, luxe et sérieux sont présentées comme **hypothèses de travail**, chacune avec contre-indication (332–342). Une impression de confiance ne valide ni sécurité du produit ni véracité d’une donnée : ce cas est signalé ligne 338. La méthode exige de nommer public, tâche ou relation visée, contre-indication et preuve attendue ; aucune couleur, police ou animation ne produit universellement une émotion (344). La suite STYLE/TOOLS devra être lue au bon moment pour les claims culturels ou datés ; une case de ce tableau n’est pas une recommandation universelle.

### CFT-04a : geste/promesse ou objet concret (346–359)

La première scène peut présenter tôt un mécanisme représentatif et actionnable, ou garder d’abord une distance éditoriale plus juste si le produit touche une personne ou un contenu intime (348). Aucune géométrie de hero, y compris trois cards ou split hero, ne gagne par défaut (350). La table de 354–357 compare compréhension, nature de l’objet, registre et mobile. La phrase « objet de preuve » est potentiellement trompeuse pour qui confond **objet présenté par le produit** avec preuve d’usage ou de vérité exécutée ; la ligne 359 réserve explicitement la preuve à ACTION, ce qui atténue F-DIR-024 sans effacer sa tension de vocabulaire. Le refus du faux dashboard ou de la donnée sensible utilisée comme vitrine (350) rejoint les protections de vérité, droits et confidentialité : F-ACT-024 reste ouvert pour la conséquence de gate et la clôture. Le compromis demandé (359) rend explicites bénéfice, coût et signal de révision ; une revue perceptuelle ne valide ni tâche utilisateur ni vérité émotionnelle générale.

### CFT-05 : palette, contraste et claim (361–373)

Le déclencheur `[REQUIS]` est large : couleur, thème, statut ou surface identitaire. Le **design par rôles** (surface, texte, action, état, frontières) est utile et cohérent avec les tokens sémantiques ; il ne suffit toutefois pas à établir que le **neutre** doit porter l’essentiel de toute composition (363). La ligne 365 borne la documentation : lorsque le système existant est conservé et qu’aucun choix de couleur ne change la décision, noter cette conservation et sa raison ; elle évite de transformer chaque correction locale de contraste en nouveau projet de palette (`DIRECTION/START` 142 et `SAVOIR/DESIGN-ATLAS` 570). La palette conditionnelle ne supprime pas le contrôle de contraste applicable.

OKLCH « peut servir » (367) ; HEX/HSL restent des formats de sortie possibles ; aucun espace n’est universellement requis. La recomposition du dark mode, la non-dépendance à un gamut élargi et l’information critique non chromatique (367–371) fixent des protections de conception. « Aucun `PASS` à l’œil » (369) renvoie à `ACTION/POLICIES` (844–848) pour le calcul selon référentiel applicable, et à `ACTION/GATE-A` (629–653) pour médium, scope, méthode, cible de conformité, échantillon et limite. La vérification colorimétrique d’une paire de textes ne suffit pas à prouver l’accessibilité globale (F-ACT-035). Toute claim sur chroma, statut perçu ou tendance doit porter source, date, portée et limite dans la trace locale (373), complétées par `SAVOIR/TOOLS` lorsqu’elle influence une décision. Cette section ne déclare aucun seuil chiffré à valider ici.

## Passage C — lecteurs sous contrainte de temps

1. **Designer, direction ouverte.** Il situe deux positions selon la tâche et note pourquoi une alternative peut changer le choix ; une phrase suffit pour la comparer tant qu’une seconde scène n’apporte rien. Les gates déclenchés par le risque restent séparés de ce tri créatif.
2. **Designer, console dense.** Il garde plusieurs priorités simultanées, transforme la grille sur mobile et inspecte la capture ; il ne conclut pas que la vitesse de décision des utilisateurs est prouvée par sa propre inspection.
3. **Équipe produit, service à contenu intime.** Elle peut choisir une promesse et un geste avant l’exemple ; elle n’expose pas une histoire réelle ou une donnée personnelle sous prétexte de « preuve » visuelle.
4. **Reviewer, identité énergique ou très colorée.** Il demande quelle tâche, culture, présence et contre-indication la couleur sert. Une application littérale « neutres d’abord, un accent » peut effacer la construction visuelle voulue : scénario de F-SAV-002.
5. **Intégrateur, correction de contraste sur composant existant.** Il conserve la palette, documente pourquoi elle n’est pas redéfinie et calcule le contraste pertinent. Le résultat reste borné aux rôles/états réellement testés, sans PASS de conformité du produit entier.
6. **Agent, claim sur couleur ou émotion.** Il distingue une hypothèse contextuelle de perception de l’effet observé avec personnes ou tâche ; une tendance datée sans source ne devient pas règle de livraison.
7. **Mainteneur, matériau code-native.** Il conserve sa relation produit, ses états et son comportement dans le scope de test ; il ne substitue pas « plus simple techniquement » à une preuve d’adéquation, ni un asset externe à une préférence universelle.

## Passage D — résistance et registre

### F-SAV-002 — prescription des neutres dans une exigence de couleur autrement située

- **Gravité provisoire : Significatif à éprouver.** Contradiction de portée textuelle confirmée ; impact sur runs réels non observé. Aucun validateur n’impose un ratio de neutres.
- **Preuve propriétaire :** `CFT-05` ligne 363, sous `[REQUIS PAR LE MODULE]`, dit sans qualification que les neutres portent l’essentiel de la structure et que l’accent signale action/focus/état/information. `SAVOIR/FRAME` lignes 106 et 143 et `CFT-00` ligne 234 admettent plusieurs registres, y compris coloré et intense, selon produit et public ; `CFT-02` lignes 294–298 exclut un menu imposé ; `CFT-04` ligne 344 refuse une association couleur/émotion universelle.
- **Contre-exemple :** un outil pédagogique ou une identité culturelle où plusieurs grandes zones colorées portent de façon cohérente la progression, l’appartenance et la hiérarchie ; texte, état et action restent identifiables sans couleur seule, contrastes applicables calculés, version sans couleur ou autre indice maintenu selon le besoin. Une transposition obligatoire vers des neutres et un unique accent retire ici une relation produit validable au lieu de réduire un risque.
- **Effet possible :** homogénéisation, perte de présence ou de reconnaissance, arbitrage stylistique prétendument obligatoire dans un contrôle qui devrait protéger rôles, états et contraste. Effet nul si les lecteurs interprètent la phrase comme **exemple fréquent** de palette et non comme exigence de style.
- **Atténuations :** la même section rend la documentation conditionnelle (365) et préserve l’information non chromatique et le contraste (369–371) ; les principes de pluralité en amont offrent une lecture située. La règle peut aussi viser un fond neutre suffisamment flexible, sans interdire de multiples accents ; cette intention n’est simplement pas explicitée.
- **Propriétaire pressenti :** `SAVOIR/CRAFT/CFT-05` pour qualifier le statut « neutres/accent » et conserver l’exigence fonctionnelle des rôles ; ACTION garde le calcul et le verdict, sans palette universelle déduite d’un gate.
- **Relations sans fusion :** F-DIR-018 protège d’autres formes surcontraintes du premier objet ; F-SAV-001 concerne le nombre de routes ; F-ACT-035 concerne la portée du PASS de contraste. F-SAV-002 est une restriction **locale de palette** sous tag `[REQUIS]`, dont le mécanisme et le test diffèrent.
- **Test futur :** direction neutre à un accent, identité à plusieurs couleurs structurelles, interface de supervision codée par zones, correction locale de contraste ; lecteurs novices et experts ; comparer ce qu’ils déclarent obligatoire, ce qu’ils conservent, calculent et retirent, en contrôlant la lisibilité et le rôle des couleurs.

### Occurrences reliées sans nouvel ID

| Observation | Constat / test ultérieur |
|---|---|
| « Objet de preuve » au hero peut être pris pour preuve exécutée | F-DIR-024 ; la ligne 359 réserve bien la preuve à ACTION, vérifier le libellé lors des contrats |
| Exemple ou histoire intime utilisée comme démonstration fonctionnelle | F-ACT-024 et protections de vérité ; vérifier droits, permission, scope et conséquence à la clôture |
| Impression d’harmonie ou d’émotion traitée comme preuve de réussite de tâche | F-ACT-005/018 ; U demande méthode et résultat, pas seulement capture ou auto-critique |
| PASS de contraste limité prétendu conformité totale | F-ACT-035 ; `ACTION/GATE-A` exige medium, échantillon, méthode et couverture |
| Alternative CFT-02 située mais B1b imposée si risque V/craft | F-DIR-009/F-ACT-036 ; tension déjà instruite au bloc SAVOIR 3, sans nouveau test identique |
| CFT-03 et CFT-05 peuvent s’ajouter à FRAME, TYPE, CONTEXT selon une tâche donnée | F-SAV-001 ; ne pas lire « deux routes » comme plafond d’obligations distinctes |
| « Lisible avant la couleur » peut être lu comme report du contraste | ACTION/POLICIES et GATE-A tranchent l’exigence de calcul ; tester si un lecteur retarde un risque critique |

### Protections positives à préserver

1. Pas de quota de directions : l’alternative est construite à la profondeur nécessaire pour comparer une décision.
2. Densité, hiérarchie et responsive suivent le contenu réel ; plusieurs priorités liées peuvent coexister.
3. L’émotion est hypothèse située, avec public et contre-indication, sans promesse universelle.
4. L’intimité, les droits et la distance juste sont pris en compte dès le premier contact.
5. Palette par rôle, états non dépendants de la couleur seule, dark mode recomposé et contraste mesuré selon scope sont des exigences distinctes d’une préférence de style.
6. Une observation perceptuelle n’est pas confondue avec la réussite d’une tâche ni avec une conformité générale.
7. Les claims culturels, techniques ou de tendance restent datés, bornés et soumis à la vérification pertinente.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Quatre sous-sections, cinq tags/scopes, route parente et renvois |
| B — sémantique | FULL | CFT-02 à CFT-05, y compris 04a, signaux, limites et autorités |
| C — usage réel | TARGETED | Sept scénarios designer, produit, reviewer, intégrateur, agent et mainteneur |
| D — résistance | TARGETED | F-SAV-002 provisoire ; six interfaces aux constats existants sans duplication |
| Machine | TARGETED | `read_route.py SAVOIR/CRAFT` et `validate_reading_map.py` passent ; aucun test colorimétrique de produit revendiqué |
| Externe | N/A-JUSTIFIED pour ce bloc | Standards, seuils et effets culturels extérieurs nécessitent leur source et leur scope avant tout claim de livraison ; contrôle dédié ultérieur |

Le bloc 4 termine **SAVOIR/CRAFT** et ajoute un seul constat provisoire F-SAV-002, sans patch ni verdict global. La prochaine unité est **SAVOIR.md, lignes 377–414** : `SAVOIR/TYPE`, choix typographiques et séparation de six dimensions de preuve. `SAVOIR/STATE` commence à 415. Reprendre avec §12, baseline, présent rapport et contrats ACTION concernés.
