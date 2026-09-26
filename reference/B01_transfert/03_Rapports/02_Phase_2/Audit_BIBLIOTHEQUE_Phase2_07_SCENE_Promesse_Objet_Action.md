# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 7 : SCENE

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 425–500** ; responsabilité 427–429, six scènes 431–489, test 491–497, séparateur 499. `BIBLIOTHEQUE/OBJECT` commence à 501 et sera examiné dans l'unité suivante.
- Méthode : protocole externe v2.0 §12, passages A–D relus ; rapport GRID bloc 6, rapports BIBLIOTHEQUE antérieurs, plan et constats F-BIB-001/002/003 repris. Interfaces ciblées : SELECT 163–205, CONTRACTS 258–284, SUPPORT 288–336, GRID 340–421 ; DIRECTION/FIRST-OBJECT 314–339 et absolus 559–601, ACTION/VISUAL_PROOF 605–619 et adéquation des preuves 657–665 ; SAVOIR/CONTEXT, F-SAV-008 sur motion/scène narrative. OBJECT 501–539 et COMPAT 661–687 consultés **uniquement** pour la distinction de niveau, sans conclure sur leurs contrats futurs.
- Baseline B01 stable : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Diagnostic sectionnel provisoire : cas de lecture simulés, sans mesure d'efficacité, de succès de tâche ou de préférence humaine ; aucun patch ni verdict global.

## Passage A — rôle, accès et frontières de propriété

Une scène organise **la relation promesse–contenu–média–preuve–action** ; si elle devient durable, son rôle distinctif doit être documenté, avec les conditions d'adoption de CONTRACTS/EVOLUTION (427). SUPPORT est le champ spatial ; GRID construit les axes de lecture ; SCENE orchestre le scénario ; OBJECT ou MICRO peuvent matérialiser un élément local de preuve et d'action (429, 439, 449, 459, 469, 479, 489). Le mot « preuve » dans une description de scène désigne l'objet, la relation ou la **preuve attendue** : seul ACTION peut dire, après observation et méthode adaptée, ce qui est établi et dans quel périmètre. SELECT permet de conserver une structure déjà suffisante sans nommer une nouvelle scène (163–167), et un nom de route n'est pas un statut de livraison.

Les six identifiants de scène sont présents : `SCENE/INSTRUMENT`, `SCENE/EDITORIAL_FIELD`, `SCENE/FRAMED_PRODUCT`, `SCENE/OPERATING_GRID`, `SCENE/SPLIT_PROOF`, `SCENE/PRODUCT_NARRATIVE`. COMPAT 682–687 les cite dans des combinaisons explicitement **indicatives** (663–674) ; on ne déduit ni permission universelle ni interdiction des combinaisons non listées. `python3 scripts/read_route.py BIBLIOTHEQUE/SCENE` refuse le titre exact alors que `validate_reading_map.py` passe : occurrence additionnelle de **F-DIR-028/F-ACT-001**, à inclure dans la future matrice de couverture des locators ; le texte reste trouvable dans le fichier propriétaire.

## Passage B — six scénarios, phrase par phrase

| Scène / lignes | Responsabilité et déclencheur | Contre-indication et observation exigible |
|---|---|---|
| `INSTRUMENT` 431–439 | Champ expressif plus panneau de mesure **fonctionnel** ; scores, états, signaux ou décisions doivent devenir une lecture concrète | Une image qui habille une carte sans donnée, statut ni geste ne suffit pas (437). L'éventuel `OBJECT/SYSTEM_DATA_MODULE` ou `MICRO/QUERY_HEALTH` garde sa responsabilité locale, ses états et sa preuve propre (439). Afficher un chiffre plausible n'établit ni sa fraîcheur ni sa justesse |
| `EDITORIAL_FIELD` 441–449 | Espace visuel souverain et projection émotionnelle ou culturelle avant preuve produit **détaillée ultérieure**, ou métaphore qui explique/oriente ; l'image doit porter une relation produit (443–445) | Prix, capacités ou données à comparer immédiatement interdisent de reporter cette comparaison par effet d'ambiance (447). Une métaphore décorative sans mécanisme ni repère produit échoue au test 495 ; zone et nature de la preuve suivante restent explicites |
| `FRAMED_PRODUCT` 451–459 | Page objet avec châssis et contenu immersif ; qualité, confiance ou expérience intégrée perceptibles en premier | Si le châssis n'aide ni hiérarchie du contenu ni interaction, il est injustifié (457). `SUPPORT/ARCHITECTED_FRAME` porte le cadre spatial ; cette route porte la relation produit/narration, même si les formes se ressemblent (459) |
| `OPERATING_GRID` 461–469 | Cellules nommées, métriques, texte et module d'analyse rendent lisible une opération ou un système | Éviter d'aplatir un sujet sensible ou singulier sous une grille bureaucratique (467). `SUPPORT/OPERATIONAL_CANVAS` est le champ dense ; la scène fait réellement lire mesure et décision (469). Un tableau qui a l'air sérieux ne prouve pas la bonne action |
| `SPLIT_PROOF` 471–479 | Artefact concret face à promesse et action ; une idée est rendue inspectable par cet artefact | Refuser si la démonstration doit être plus large ou si la division impose artificiellement 50/50 (477). `OBJECT/COMPARISON_SPLIT` est une unité de comparaison locale ; sa présence ne crée ni deux côtés équivalents ni preuve de performance par le seul visuel (479) |
| `PRODUCT_NARRATIVE` 481–489 | Fenêtre applicative ou état produit fait avancer l'histoire ; une **interaction réelle** est un meilleur candidat de preuve pour assistant, analyse, cockpit ou collaboration (483–485) | Fenêtre générique, trop petite ou sans rapport au titre échoue (487). `OBJECT/PROOF_PRODUCT_STAGE` peut fournir une fenêtre réutilisable, sans remplacer le scénario, l'interaction observée, ses états et sa vérité de claim (489) |

Les intitulés `INSTRUMENT`, `OPERATING_GRID` ou `PRODUCT_NARRATIVE` ne reclassifient pas un run en `SYSTÈME` ou `DIRECTION` : START garde ce choix. Une scène narrative peut comporter un objet opérationnel, et une scène d'opération peut rester expressivement composée ; choisir selon la décision réelle et le risque. Pour un même produit, des scènes différentes peuvent prendre en charge surfaces ou phases différentes. Un **premier objet habitable** reste nécessaire lorsqu'une décision de scène est ouverte (BIBLIOTHEQUE 119–127), avec contenu crédible, action et états proportionnés ; nommer la scène sans la construire n'est pas une preuve.

### La preuve différée d'EDITORIAL_FIELD et le premier objet

La phrase 445 autorise explicitement l'émotion ou la culture **avant une preuve produit ultérieure**. Cela ne signifie pas qu'une entrée `DIRECTION` peut afficher une illustration générique et promettre que son lien au produit sera trouvé plus tard. La phrase précédente impose à l'image ou à l'illustration une **relation de produit** (443) et le test final demande métaphore, navigation ou lien précis à la preuve (495). `DIRECTION/FIRST-OBJECT` 316–335 demande un objet de preuve intelligible et dit que l'objet arrive avant les bénéfices ; pourtant `SAVOIR/CRAFT/CFT-04a` 346–359 autorise une promesse ou un geste avant l'objet dans certains contextes, notamment lorsqu'il faut préserver une juste distance envers un contenu intime. **Cette divergence inter-propriétaires reste ouverte** : elle ne peut être résolue en décrétant qu'un composant de preuve doit toujours apparaître dans le hero. Une preuve détaillée peut venir plus loin si l'entrée montre déjà une relation produit située, si les claims non démontrés sont bornés et si le compromis de position est explicite. Un premier écran purement interchangeable, sans lien produit pertinent et avec action fictive, reste un retour ou une hypothèse non vérifiée, sans remplacer cette absence par `N/A-JUSTIFIED`.

Le discriminant restant est un run `DIRECTION` où l'image matérialise la catégorie et oriente vers un cas réel situé sous la ligne de flottaison, comparé à un run où l'image pourrait servir à n'importe quelle marque et le CTA mène à une démonstration fictive. La bonne première scène ne transforme pas la capture en test de tâche ou de véracité du produit ; ACTION garde le résultat des claims et l'issue. Le texte propriétaire offre **déjà** les garde-fous 443 et 495 : aucune contradiction autonome n'est établie sans voir le comportement d'un lecteur sur ces deux cas.

### Test final : refuser le template sans bannir une forme utile (491–497)

La formule `titre + sous-texte + CTA + image décorative` échoue **lorsque** la responsabilité choisie exige instrument, fenêtre, grille ou preuve (493), et non parce qu'un titre ou CTA serait interdit par principe. Un visuel souverain doit réellement porter une métaphore produit, un repère de navigation ou une relation concrète à la preuve (495). Les scènes déclarent leur **type** de prétention et sa **limite** (497), comme le contrat commun 268–270 ; un perceptuel réussi n'est pas une tâche accomplie. Cela protège aussi une scène familière et sobre qui montre effectivement un outil, un état ou un geste plutôt que d'imposer une variante stylistique de façade.

Les états, responsive, accessibilité, confidentialité/permissions, performance et vérité de données restent activés par mode, risque, médium et claim (CONTRACTS 269–284 ; ACTION 95, 625–655). Si une scène spatiale ou animée est utilisée pour l'expression narrative, ACTION/MOTION 596–602 impose rôle, déclencheurs, interruption, alternative, performance et preuve ; la tension du filtre SAVOIR/CONTEXT qui pourrait rejeter le rôle narratif reste **F-SAV-008**, sans nouvel ID SCENE. Une simple capture peut montrer composition et présence, pas test utilisateur, interaction effective ou conformité globale (ACTION 619, 659–665).

## Passage C — simulations de lecteurs

| Cas | Suite correcte sous contrainte | Erreur recherchée |
|---|---|---|
| Designer `LITE`, correction d'un CTA sur une scène existante | Garder structure héritée si elle tient ; prouver le lien ou l'action réellement touchée selon ACTION | Sélectionner une scène nouvelle pour un delta local |
| Direction culturelle, entrée éditoriale liée à une archive située | `EDITORIAL_FIELD` avec relation concrète, chemin vers l'archive, vérité des claims et preuve détaillée située ensuite | Rejeter toute preuve différée comme illégale, ou déclarer un PASS parce que la capture est belle |
| Direction de marque, image spectaculaire interchangeable et CTA factice | Revenir à la décision, au produit et au geste ; marquer illustration et indisponibilité de l'action | Faire de la métaphore vague une preuve produit future garantie |
| Produit B2B, image de chiffres factices dans un cadre « sérieux » | `INSTRUMENT` ou `OPERATING_GRID` seulement avec donnée, statut et action réellement pertinents ; vérifier source, état et tâche | Confondre panneau décoratif avec module de mesure |
| Démo d'outil, artefact concret unique et promesse connexe | `SPLIT_PROOF` si l'artefact démontre vraiment le mécanisme dans le scope, sans équilibre 50/50 automatique ; limiter le claim | Nommer `COMPARISON_SPLIT` comme si deux variantes avaient été testées |
| Interaction d'assistant, fenêtre produit très réduite | Produire état et comportement suffisamment observables ou revenir ; tester la tâche si réussite revendiquée | Prendre un screenshot minuscule pour preuve de l'interaction |
| Designer, scène narrative animée justifiée par l'identité | Confronter F-SAV-008, contrat motion ACTION, alternative/réduction/états, scope et preuve ; ne pas conclure sur la seule animation | Exempter la scène narrative des contrôles ou supprimer le récit par une règle de style supposée |
| Agent, `BIBLIOTHEQUE/SCENE` refusé par CLI | Ouvrir le titre exact du propriétaire, consigner F-DIR-028/F-ACT-001 | Inventer un locator résolu ou abandonner la lecture de la section |

Ces huit tests sont documentaires et contrastés ; ils n'établissent ni taux d'erreur des lecteurs ni qualité d'un produit réel. La réussite d'une scène doit être observée dans son artefact et son scope avec ACTION.

## Passage D — résistance et déduplication

**Aucun nouvel ID autonome pour SCENE à ce stade.** L'ouverture émotionnelle est conditionnée à une relation produit ; la distinction support/scène/objet est répétée aux six endroits utiles ; les six contre-indications sont explicites ; le test de template refuse seulement une image **décorative** lorsque la responsabilité exige une preuve ; type et limite sont rappelés. Les difficultés se rattachent à des constats antérieurs ou nécessitent une simulation réelle pour changer de statut.

| Point de tension ou résistance | Relation et prochain test |
|---|---|
| `EDITORIAL_FIELD` permet une preuve détaillée plus loin ; DIRECTION 316 donne priorité à l'objet, SAVOIR/CFT-04a 348 accepte parfois la promesse/le geste d'abord | Comparer relation produit réelle immédiatement visible et distance juste contre ambiance générique avec preuve seulement promise ; arbitrer la divergence DIRECTION/SAVOIR sans forcer l'objet dans le hero |
| Narration/motion située contre filtre SAVOIR/CONTEXT | F-SAV-008 ; comparer trois briefs narratif/explicatif/décoratif avec contrôles ACTION et fallback effectif |
| Scène ou objet pris pour preuve de résultat de tâche | F-ACT-005/021/029 et BIBLIOTHEQUE 497 ; méthode, états, périmètre et résultat réellement observés |
| Titre SCENE refusé par le lecteur de routes, carte validée | F-DIR-028/F-ACT-001 ; test de résolution future de tous les titres annoncés |
| Image illustrative, démonstration fictive ou CTA vide présentés comme réels | DIRECTION/FIRST-OBJECT 316–318 et ACTION/ASSET/claims ; ne pas ouvrir un doublon pour le nom de scène |
| Scène devenue route durable par simple réemploi ou « skin » | F-BIB-002 et CONTRACTS/EVOLUTION ; usages contrastés, gain, owner et décision CHANGELOG restent nécessaires |

F-BIB-001 (paire B1b réutilisée hors décision/scope) et F-BIB-003 (champs MOBILE de GRID) ne reçoivent pas de nouvelle occurrence fautive de SCENE. Leurs contrôles s'appliquent seulement si leur question est active pour le run. La préférence pour une scène « originale » ne doit ni dégrader la tâche, ni supprimer une convention qui porte déjà la preuve.

## Couverture et suite

| Passage | Profondeur | Couverture et limite |
|---|---|---|
| A — architecture | FULL | Six scènes, rôles SUPPORT/GRID/OBJECT, accès au titre exact |
| B — sémantique | FULL | 425–497, six conditions/contre-indications, preuve différée, vérité et limites |
| C — usage | TARGETED | Huit simulations ; aucune observation de surface ou utilisateur réel |
| D — résistance | TARGETED | Preuve différée, récit, scène décorative et claims ; déduplication sans nouvel ID |
| Machine | TARGETED | `read_route.py` refuse SCENE ; `validate_reading_map.py` passe ; aucun contrôle de schéma probant rejoué ici |
| Externe | N/A-JUSTIFIED | Aucun fait externe requis pour qualifier ces règles documentaires internes |

Le séparateur est à 499 et la ligne 500 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **501–541**, `OBJECT` ; relire protocole §12, le présent rapport et les frontières scènes/objets avant d'analyser routes d'objet, slots, états et preuve en contexte.
