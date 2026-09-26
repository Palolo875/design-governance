# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 6 : STATE, craft et états

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **415–470** : déclencheur STATE (415–417), jugement visuel situé (419–448), vocabulaire perceptuel (450–461), états pertinents (463–467) et séparateur 469. `SAVOIR/SOURCE` commence à 471.
- Protocole externe : §12, quatre passages A–D. Point de reprise relu : rapport SAVOIR bloc 5, plan maître, checkpoints ACTION et DIRECTION. Interfaces inspectées : `ACTION/VISUAL_PROOF` (611–619), `ACTION/GATE-A` (623–686), `ACTION/GATE-C` (775–794), `ACTION/RUN_CARD`, `DIRECTION/START` et le début de `SAVOIR/SOURCE` pour fixer la frontière sans analyser sa route.
- Baseline B01 inchangée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Diagnostic de lecture, sans run produit ni patch. Les scénarios illustrent les conséquences de lecture ; ils ne constituent pas un PASS d’un artefact réel. Les défauts machine déjà testés par ACTION ne sont pas répétés sans question distincte.

## Résumé du bloc

STATE décrit le craft comme travail sur les états, la donnée réelle, la récupération et les détails de comportement. Ses six lentilles servent le **jugement situé** et n’ajoutent ni score ni statut. Ses trois niveaux Correction/Précision/Intention aident à nommer une résolution effectivement observée, sans rendre les trois niveaux cumulatifs ou quantifiés. Aucun composant ne doit avoir « tous les états » ; chaque état nécessaire à sa tâche et à son risque doit être explicite.

La dernière phrase répartit correctement les contrôles : **Gate A** vérifie les propriétés applicables, **Gate C** examine la résolution perceptuelle du rendu et une **observation de tâche** est parfois nécessaire pour la compréhension ou la récupération. Deux formulations requièrent néanmoins la même prudence déjà identifiée ailleurs : « Correction : comportement et accessibilité de base fonctionnent » (438) pourrait être prononcée après une simple revue visuelle, et « HTML sémantique » (467) pourrait être généralisé hors du Web. Les lignes 434 et 467 ainsi que les propriétaires ACTION limitent ces lectures. Ces risques prolongent F-ACT-005, F-ACT-035 et F-DIR-038 ; aucun nouvel ID SAVOIR n’est établi.

## Passage A — architecture visible

| Lignes | Fonction et autorité | Condition de sortie / frontière |
|---|---|---|
| 415–417 | `[REQUIS PAR LE MODULE — composant, état, surface DIRECTION ou Gate C]` ; craft des états et contenus réels | Obligation déclenchée par scope, pas preuve ou verdict automatique |
| 419–434 | Six lentilles de jugement : direction, craft, polish, créativité, goût, spécificité | Observation d’un objet réellement construit avec conséquence, scope, limite ; aucun statut nouveau |
| 436–448 | Correction, Précision, Intention et question de décision délibérée | Niveaux descriptifs de résolution ; le temps investi n’est pas preuve |
| 450–461 | Six termes perceptuels associés à une question et à un diff possible | Chercher une modification concrète, non appliquer une recette uniforme |
| 463–467 | États nécessaires, HTML sémantique, focus, erreur et récupération | Applicabilité par composant/médium ; Gate A, Gate C et tâche utilisateur restent distincts |

La CLI `read_route.py` refuse `SAVOIR/STATE` et `ACTION/GATE-C`, mais accepte `ACTION/GATE-A` ; tous les titres sont présents dans les propriétaires. `validate_reading_map.py` passe. C’est une nouvelle occurrence de **F-DIR-028/F-ACT-001** : le succès de la carte dérivée ne démontre pas la couverture des locators spécialisés. La recherche manuelle retrouve STATE et Gate C ; aucune de leurs règles n’est absente de la source.

## Passage B — contrat sémantique, section par section

### Propriété et six lentilles (415–434)

Le déclencheur large de la ligne 417 s’applique aux composants, états, surfaces `DIRECTION` et cas Gate C. Il vise le craft comme précision des états, contenus, microcopie, données extrêmes et récupération, et non un embellissement final. Les six questions 425–430 sont un vocabulaire de **jugement**, pas des valeurs que `closure.direction_status` ou `closure.verdict` pourraient prendre (432). La direction donne un point de vue, le craft le matérialise, le polish résout ses détails ; créativité, goût et spécificité restent appréciés par rapport au produit, au public et au contexte. Cette distinction aide à lire F-DIR-030 sur la frontière DIRECTION/SAVOIR/ACTION : SAVOIR possède les critères, ACTION le contrôle sur le rendu, les preuves et la clôture.

La ligne 434 empêche le formulaire universel : n’examiner les dimensions que si elles peuvent modifier une décision ; nommer l’objet visible, la conséquence, le scope et la limite. Une capture prouve ce qu’elle montre dans son périmètre, non le build complet, la réussite de l’action, l’accessibilité exécutée ni la robustesse. `ACTION/VISUAL_PROOF` (611–619) précise quelles vues et quels états seraient nécessaires selon la décision ; `ACTION/GATE-C` exige une capture pour son propre jugement (777–783). Sans rendu capturé, la qualité perceptuelle est `NOT-VERIFIED`, pas acquise par une rationale.

### Trois niveaux et temps investi (436–448)

`Correction` (438) nomme une base de comportement et d’accessibilité qui fonctionne ; `Précision` (439) nomme le soin des mesures, transitions et états ; `Intention` (440) demande une décision située qui change visiblement une relation ou un usage. La ligne 442 prévient qu’un rendu précis peut rester générique et qu’une vue polie peut laisser ses états secondaires non vérifiés. Ces mots n’ont donc pas la force d’un PASS de tous les axes V/U/A/T ; ils décrivent l’objet **dans la partie réellement jugée**.

La combinaison « niveau de lecture visuelle » (442) et « accessibilité de base fonctionne » (438) comporte un risque de glissement : un reviewer pourrait cocher Correction sur une capture sans avoir exercé clavier, nom accessible ou récupération. Mais la ligne 434 refuse explicitement cette inférence et ACTION garde Gate A. Ce risque relève de F-ACT-005/035 et du contrôle de scope en phase 9, sans preuve d’un défaut autonome dans STATE. La question de niveau 3 (444–446) demande quelle contrainte une décision sert ; un choix silencieux et rapide peut être intentionnel. La ligne 448 refuse de compter le temps passé ou l’effort comme preuve de qualité.

### Vocabulaire perceptuel et action (450–461)

Rayons, masses, vide, silhouette, surface et états sont reliés à une **question** et à un diff possible (454–459). « Possible » est essentiel : aucune liste n’impose un changement de rayon, un effet de profondeur ou une modification après un one-shot suffisant. La silhouette d’une transaction peut simplement renforcer la lecture prioritaire (461) ; elle n’exige pas spectacle ni identité nouvelle. Un diff de masse ou de contenu doit être inspecté après exécution pour dire quel effet il a produit. La trace de changement et la non-régression relèvent d’ACTION ; une ligne de vocabulaire n’est pas une preuve de correction.

### États pertinents, médium et propriétaires des gates (463–467)

La ligne 465 donne des exemples conditionnels : focus clavier, liste vide, erreur de formulaire, overflow, chargement, permission refusée, image absente, valeur extrême et texte long **lorsque pertinents**. Elle refuse à la fois la liste exhaustive des états imaginables et l’omission d’un état nécessaire. Le risque dépend de la fonction : un bouton de consentement, un tableau dense et une carte purement éditoriale n’ont pas la même matrice. Un état attendu mais non inspecté doit rester dans la limite ou le `NOT-VERIFIED` pertinent ; `ACTION/VISUAL_PROOF` (616) nomme explicitement les axes U/A/T pour un état significatif absent.

La ligne 467 dit que sémantique HTML, nom accessible, focus visible, erreur associée et récupération compréhensible servent le craft aussi bien que la conformité. `ACTION/GATE-A` (671–684) vérifie les contrôles **applicables** par méthode et médium ; `ACTION/GATE-C` (785–794) juge la résolution perceptuelle sans produire un PASS d’accessibilité ; `ACTION/GATE-A` (659–665) rappelle que la réussite d’une tâche demande une preuve d’usage appropriée quand U domine. HTML sémantique n’est littéralement applicable qu’à une surface Web : sur une app native, un document imprimé ou un autre médium, on traduit l’objectif vers les primitives et contrôles du support déclaré. F-DIR-038 porte déjà cette question transversale de portée ; le texte de STATE doit être lu avec le contrat de médium de Gate A (629–653).

## Passage C — lecteurs sous contrainte de temps

1. **Designer, composant transactionnel.** Il représente attente, erreur, permission refusée et récupération si ces cas existent, puis inspecte leur relation à l’action ; la belle capture nominale ne couvre pas le paiement échoué.
2. **Reviewer, direction visuelle forte.** Il nomme l’objet réellement inspecté, sa spécificité et le détail faible. Il ne donne ni statut `HELD` ni PASS U/A au seul mot « Intention ».
3. **Intégrateur, liste administrative.** Il juge silhouette comme hiérarchie calme et met à l’épreuve empty, erreur, contenu long et clavier. Il ne fabrique pas de profondeur spectaculaire parce qu’une ligne « Surface » existe dans la table.
4. **Équipe produit, récupération critique.** Elle sépare présence de l’erreur, compréhension de la prochaine action et capacité d’une personne représentative à reprendre la tâche ; une capture suffit à la première question, pas nécessairement aux deux autres.
5. **Agent sans runtime.** Il prépare critères, états et méthode, puis marque le rendu et les comportements non vérifiés ; une rationale ou une image générée n’est pas capture du build.
6. **Reviewer en contexte non Web.** Il conserve l’exigence de sémantique/nom/focus ou leur équivalent adapté au support, sans exiger HTML littéral là où il n’existe pas.
7. **Mainteneur, run clôturé avec seul état nominal.** Il retrouve la trace et cherche états requis, versions, méthodes et limites ; une `RUN_CARD` formellement valide ne prouve pas que chacun a été exécuté.

## Passage D — résistance et registre

### Occurrences rattachées aux constats antérieurs

| Cas de résistance | Constats et test de suite |
|---|---|
| `Correction` prononcé depuis une capture alors que clavier et récupération n’ont pas été exercés | F-ACT-005/035 ; distinguer impression V et preuve A/U, conserver scope et `NOT-VERIFIED`. Le texte STATE 434 fournit déjà la limite. |
| Capture unique pour une surface à états critiques | F-ACT-005/021 ; `ACTION/VISUAL_PROOF` exige l’état significatif dans son périmètre, et le paquet de clôture doit conserver ce qui reste non vérifié. |
| État réduit motion annoncé mais non exercé | F-ACT-033 ; ce mécanisme spécialisé n’est pas résolu par une alternative dessinée dans la table de STATE. |
| HTML sémantique présenté comme critère d’une app native ou d’un imprimé | F-DIR-038 ; déclarer le médium et contrôler son équivalent dans ACTION. Aucun nouveau défaut de normativité établi pour STATE seul. |
| Une lentille de jugement SAVOIR produit directement un verdict ou une revue ACTION parallèle | F-DIR-030/F-ACT-002 ; séparer critère, artefact, méthode, résultat, axe et verdict. |
| Un tableau `Diff possible` incite à modifier malgré un premier rendu tenu | F-DIR-009 ; « possible » ne déclenche aucune variante, et la branche one-shot de CRAFT s’arrête après observation si les risques tiennent. |
| Plusieurs routes spécialisées quand composant, type, contexte et source comptent | F-SAV-001 ; les scopes ne s’annulent pas au deuxième chargement, et aucune route unique n’est universellement requise. |

### Contrôle outillé ciblé et limites

Sur B01, `SAVOIR/STATE` et `ACTION/GATE-C` échouent dans le lecteur, `ACTION/GATE-A` réussit et la carte dérivée est validée. C’est un test de **résolution de locators**, pas un test de comportement d’un composant. Les rapports ACTION précédents ont déjà éprouvé des cartes acceptées avec seulement l’état nominal et des états critiques explicitement non vérifiés ; ce bloc ne répète pas ces mutations identiques. En phase 9, il faudra un scénario d’état réel avec observation et résultat distincts de la déclaration de scope, pour vérifier que le risque U/A/T gouverne le verdict.

### Protections positives à préserver

1. SAVOIR nomme des lentilles de critique sans créer une taxonomie concurrente de statuts et de scores.
2. Le jugement visuel s’applique au rendu construit, à un objet et à une conséquence observable dans un scope déclaré.
3. La précision ne compense ni la généricité de la direction ni un état ou une tâche non vérifiés.
4. Un petit changement rapide peut être intentionnel ; le temps et le nombre de variantes ne sont pas des preuves.
5. Chaque état nécessaire est explicite, mais aucun composant ne reçoit par défaut tous les états concevables.
6. Gate A, Gate C et observation de personne/tâche répondent à des questions différentes ; chacun garde sa méthode et sa limite.
7. Les critères techniques sont traduits au médium réel et la couverture observée ne s’étend pas par formule générale.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Déclencheur, six lentilles, trois niveaux, six termes perceptuels, gates et routes |
| B — sémantique | FULL | Portée, jugement, lexique, effet, états nécessaires et séparation des preuves |
| C — usage réel | TARGETED | Sept scénarios designer, reviewer, intégrateur, produit, agent et mainteneur |
| D — résistance | TARGETED | Sept interfaces liées à constats ouverts, sans nouveau constat |
| Machine | TARGETED | Deux locators refusés, Gate A accessible, carte dérivée verte ; tests de clôture antérieurs repris |
| Externe | N/A-JUSTIFIED | Aucun standard, seuil ou claim technique externe nouveau n’est tranché ici |

Bloc 6 terminé **sans nouvel ID**, sans patch ni verdict global. Prochaine unité : **SAVOIR.md, lignes 471–529**, `SAVOIR/SOURCE` : utilité de l’ancre, recherche orientée décision, origine, droits, création et intégration. `SAVOIR/DESIGN-ATLAS` commence à 530. Reprendre avec le §12, la baseline, le présent rapport et les constats d’ancres/provenance déjà ouverts.
