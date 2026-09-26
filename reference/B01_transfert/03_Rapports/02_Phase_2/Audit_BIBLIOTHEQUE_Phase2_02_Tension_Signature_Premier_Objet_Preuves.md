# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 2 : TENSION, SIGNATURE et types de preuve

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/BIBLIOTHEQUE.md`, **lignes 88–160** : TENSION 88–104, SIGNATURE 106–117, thèse et premier objet 119–127, préfixes 129–142, types de preuve 144–157, séparateur 159. `BIBLIOTHEQUE/SELECT` commence à **161** et sera lu au prochain bloc.
- Méthode : protocole externe v2.0 §12, passages A à D relus ; continuité contrôlée avec `Audit_BIBLIOTHEQUE_Phase2_01_Responsabilite_Entree_READ.md`, le plan maître et les checkpoints DIRECTION, ACTION, SAVOIR. Interfaces ciblées : DIRECTION/CREATIVE-BOOT 168–184 et START 129–144 ; ACTION/FIRST-RENDER 79–91, PRECONDITION 205–236, VISUAL_PROOF 610–619, GATE-A 627–653 et GATE-B 694–700 ; SAVOIR/FRAME 95–112 et CRAFT 308–320. Les lignes SELECT 161–214 ne sont consultées qu'en interface pour vérifier proportion et one-shot ; leur diagnostic propriétaire est reporté.
- Baseline B01 inchangée : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- Aucun patch du système ni verdict global. Les scénarios de lecteurs sont des simulations documentaires et ne mesurent pas la fréquence d'un défaut en production.

## Passage A — architecture, rôles et accès

TENSION et SIGNATURE sont des **sous-sections de `BIBLIOTHEQUE/READ`**, respectivement aux lignes 88 et 106. Leurs noms ressemblent à des routes distinctes, mais `read_route.py` ne résout ni `BIBLIOTHEQUE/TENSION`, ni `BIBLIOTHEQUE/SIGNATURE` ; il résout `BIBLIOTHEQUE/READ` et extrait les lignes 70–160, incluant ces deux sous-sections, la thèse, les préfixes et les types de preuve. `validate_reading_map.py` passe malgré les deux locators refusés. Ce problème d'accès appartient déjà à F-DIR-028/F-ACT-001. **Extraire du texte ne déclenche pas automatiquement l'obligation conditionnelle qu'il contient** : TENSION s'active quand une décision structurelle ou créative est ouverte (90) ; SIGNATURE quand la sélection `DIRECTION` est ouverte ou qu'une dérivation vise un écart perceptible (108). Le surcoût ou les erreurs réelles dus à cette extraction large restent à mesurer en phase d'instrumentation ; pas de nouvel ID sur cette seule base.

Le chemin logique est : question de structure → tension utile → relation/route choisie → conséquence attendue et premier objet → observation selon ACTION. La ligne 102 refuse qu'un nom de route fasse office de direction créative ; les lignes 121–125 séparent thèse, signature, conséquence attendue et artefact. Les lignes 144–157 qualifient les **types de prétentions prouvées** ; ACTION garde méthodes, observations, gates, axes et verdict. BIBLIOTHEQUE ne peut convertir un type de preuve annoncé en résultat de test.

## Passage B — contrat sémantique, phrase par phrase

### TENSION : axe, pôle et conséquence (88–104)

La ligne 90 conseille de déclarer **un ou deux axes** de tension seulement lorsque la décision est ouverte. Densité, foyer, position de preuve, temporalité, matière, navigation et action (92–100) sont des dimensions de **relation** ; les pôles ne sont ni styles préinstallés, ni scores, ni taxonomie de verdict. `PROOF-POSITION` possède trois pôles, et 104 demande de nommer le pôle retenu et son effet au lieu de forcer une fausse opposition binaire. Une tension est utile si un pôle change espace, hiérarchie, comportement, preuve ou mémoire, et si le premier objet permet de voir cette différence (102). Si aucun axe ne change la prochaine décision, préserver l'héritage ; `N/A-JUSTIFIED` ne concerne qu'une responsabilité réellement non applicable, pas une conséquence attendue sans preuve (104, ACTION 218/236).

`DIRECTION/CREATIVE-BOOT` 173 demande **un seul** `STRUCTURAL-TENSION` alors que le propriétaire structurel en admet un **ou deux**. Ce désaccord textuel est déjà F-DIR-012 ; ce bloc confirme la différence sans démontrer qu'un run réellement utile à deux tensions a été tronqué. Le test discriminant doit confronter zéro tension applicable, une tension dominante et deux tensions **indépendantes** qui modifient chacune une décision ; ne ni supprimer le second axe utile par quota de façade, ni inventer un deuxième axe pour remplir un tableau. La trace `TENSION-AXES / SELECTED-POLE / DECISION-IMPACT / OWNER / SCOPE / NEXT-OBSERVATION / EXIT-CONDITION` (104) décrit **l'intention et la prochaine observation** avant build ; l'impact effectivement constaté attend l'observation ACTION.

### SIGNATURE et thèse structurelle (106–127)

La signature est requise pour une **sélection ouverte `DIRECTION`** ou une dérivation cherchant un écart perceptible (108), pas pour toute correction locale ni toute route simplement citée. Elle porte relation rendue possible, limite de l'héritage/précédent, manifestation attendue dans le premier objet et condition d'abandon ou recomposition (110–115). Elle n'impose pas la nouveauté visuelle : foyer, voisinage, retenue, temporalité, preuve ou geste peuvent être spécifiques sans composant inédit (117). Si aucune différence structurelle utile ne peut être nommée, choisir l'héritage ou la trace documentaire sans revendiquer une nouvelle direction structurelle. Cela n'annule pas une direction de contenu, voix ou style dont la structure est délibérément héritée ; DIRECTION reste propriétaire du mode et de la thèse générale.

Le libellé `PREVIOUS-LIMIT` présuppose une structure héritée ou antérieure. Pour une surface réellement nouvelle sans précédent inspectable, **ne pas inventer un ancien écran** : enregistrer l'absence de base structurelle comme limite de comparaison et borner la signature par la relation attendue et la prochaine observation. Le corpus ne spécifie pas ici une valeur canonique pour cette absence. L'ambiguïté peut être éprouvée avec un premier produit sans héritage et avec un redesign possédant une baseline réelle ; elle ne prouve pas à elle seule une obligation de fabriquer un historique ni un nouvel ID.

La thèse 121 décrit **pourquoi** la combinaison de support, grille, scène ou objet sert le produit et le regard ; SIGNATURE décrit **l'écart** et la limite antérieure ; `OBSERVABLE-CONSEQUENCE` est la **prédiction contrôlable** commune ; `FIRST-OBJECT` est l'artefact construit ; `EXIT-CONDITION` prévient maintien/retour/abandon (123). Avant le rendu, « observable » exprime une cible, non un résultat acquis. Après, la capture et les tests adaptés donnent un résultat dans un scope daté/versionné, à comparer à la prédiction, puis ACTION qualifie `DECISION-CHANGE`, les axes et le verdict. Une double déclaration textuelle de thèse et signature ne remplace pas cette chaîne.

Le premier objet « habitable » (125–127) a contenu crédible, hiérarchie, geste, états pertinents et résolution proportionnée au mode. Tester contenu réel/long, état significatif, viewport et route d'image permet de découvrir une structure qui ne fonctionne qu'avec un exemple idéal. Une première version suffisamment forte peut être **confirmée sans itération artificielle** : la ligne 127 demande correction si une relation dominante **peut être améliorée** ; DIRECTION 502, ACTION 453 et BIBLIOTHEQUE/SELECT 201–205 permettent un one-shot observé lorsque risques et qualité tiennent. F-DIR-009/F-ACT-025 conservent les autres tensions de clôture, sans nouvel ID local.

### Préfixes et statut de route (129–142)

`SUPPORT`, `GRID`, `SCENE`, `OBJECT`, `MICRO`, `MODIFIER` et `LAYER` codent des **responsabilités structurelles**. `LAYER/PRIMITIVES` est la couche canonique des primitives accessibles ; les primitives nommées sont sélectionnées par contrat d'objet ou de couche (139), ce qui évite d'inventer un `PRIMITIVE/<NAME>` comme préfixe actif absent de la table. « Objet de rythme » peut être un rôle de `OBJECT/*`, mais sa qualification détaillée appartient au bloc SELECT, non à ce tableau. Un nom de campagne, de domaine ou de variante locale ne devient pas une route canonique du seul fait d'un préfixe ressemblant (142) : statut et éventuelle promotion passent par EVOLUTION/CHANGELOG. Ce tableau n'oblige pas à charger tous les niveaux ; la condition de décision de READ 72–80 et SELECT 163 reste prioritaire.

### Types de preuve, méthodes et limites (144–157)

`PERCEPTUAL` porte foyer/masses/silhouette/contraste visibles ; `EXPERT` une interprétation située de cohérence par une personne compétente ; `TECHNICAL` une propriété mesurée ou inspectée ; `USER/TASK` un résultat pour une tâche et un contexte déclarés. Chaque ligne indique aussi ce qu'elle ne prouve **pas seule** (150–153). Plusieurs types peuvent être nécessaires (155) : une capture du premier écran et un avis expert ne démontrent pas, sans tâche observée, la réussite d'un parcours utilisateur. Réciproquement, un test de tâche circonscrit ne démontre ni performance globale ni conformité technique complète.

La ligne 157 affirme la différence entre **ce qui est établi** (`PROOF-TYPE`) et **comment** (méthodes ACTION `AUTOMATED`, `MANUAL`, `EXPERT`, `USER` ou combinaison). Le même mot `EXPERT` sert toutefois aux deux axes : l'un désigne une conclusion interprétative contextualisée, l'autre une inspection menée par expertise (ACTION/GATE-A 636 et 650). Ce recouvrement rend leur mapping **non mécanique**, comme l'avoue la ligne 157 : une revue experte de masses visibles peut être `PERCEPTUAL` et `EXPERT` selon le contenu revendiqué, mais sa méthode doit rester attribuée à l'examen réellement effectué. Déclarer `PROOF-TYPE=EXPERT` sans artefact, méthode, scope et limites ne valide aucune propriété. Ce risque de transport revient à F-DIR-032/033 et F-ACT-002/029 ; la valeur sémantique et son éventuelle ambiguïté machine seront vérifiées lors des contrats, sans ouvrir d'ID BIB sur le seul homonyme.

## Passage C — simulations de lecteurs sous contrainte

| Cas | Décision attendue et preuve proportionnée | Erreur que la simulation cherche |
|---|---|---|
| Designer, surface `DIRECTION` avec deux tensions indépendantes | Garder les deux si elles changent foyer **et** position de la preuve, choisir les pôles, nommer objets et prochaine observation | Le Boot à un champ élimine une décision utile (F-DIR-012) |
| Intégrateur, grille locale suffisante | Zéro tension nouvelle utile, héritage explicite, contrôle ACTION du delta réel | Fabriquer une tension ou faire de N/A une confirmation sans observation |
| Designer, première surface sans structure antérieure | Thèse et relation attendue, absence de baseline antérieure signalée, premier objet habitable ; comparaison à cible actuelle | Inventer `PREVIOUS-LIMIT` historique ou feindre un écart observé |
| Reviewer, structure nommée mais état erreur absent | Reprendre le premier objet avec état/viewport applicables ; qualifier le résultat manquant dans ACTION | Prendre le nom de route, deux champs textuels ou la capture nominale pour preuve du run |
| Analyste, expert juge le rythme d'une capture | Consigner artefact, scope, méthode expert, résultat interprétatif et limites ; ajouter tâche réelle si conclusion U visée | Confondre type et méthode `EXPERT`, puis déclarer usage prouvé |
| Mainteneur, nouvelle variante appelée `GRID/BRAND_X` | Vérifier statut local/candidate et responsabilité réelle avant prétention canonique, conserver owner et preuve | Transformer un nom plausible en route adoptée |
| Agent, objet initial suffisant sans défaut dominant | Comparer au contrat et au risque, confirmer la décision avec preuve, puis arrêter le polish inutile | Lire « la correction vient ensuite » comme obligation de modifier (F-DIR-009) |

Ces sept parcours sont des **tests de lecture simulés**. Aucun ne démontre un résultat produit, une baisse de charge ou un défaut fréquent d'usage. Le niveau de preuve est celui du contrat documentaire et des contrôles d'accès cités, pas d'une expérimentation sur des personnes.

## Passage D — résistance, déduplication et statut

**Aucun nouvel ID autonome pour ce bloc.** Les ambiguïtés observées sont soit les occurrences précises de constats existants, soit des hypothèses à départager lorsque SELECT, les contrats machine et des runs réels seront examinés. Les protections positives restent fortes : tensions situées, zéro nouveauté forcée, premier objet complet, rôles de preuve bornés et méthode distincte du verdict.

| Observation | Rattachement / prochain test |
|---|---|
| Un ou deux axes TENSION, Creative Boot n'en transporte qu'un | F-DIR-012 ; tester zéro, un, deux axes utiles et absence de quota artificiel |
| READ inclut TENSION/SIGNATURE ; locators dédiés rejetés | F-DIR-028/F-ACT-001 ; mesure du coût/erreur de chargement à venir, aucun effet réel présumé |
| SIGNATURE demande limite antérieure sur premier objet sans antécédent | Observation à éprouver avec greenfield/redesign ; documenter absence honnête sans créer un précédent fictif |
| `OBSERVABLE-CONSEQUENCE` ou `DECISION-IMPACT` rempli comme résultat avant premier objet | F-DIR-003 et F-ACT-013/030 ; ACTION réserve `DECISION-CHANGE` à l'après observation |
| Premier objet jugé sur état/viewport idéal seulement | F-ACT-005/012/021 et ACTION/VISUAL_PROOF ; vérifier scope livré/observé |
| Preuve de type `EXPERT` prise pour méthode ou réussite utilisateur | F-DIR-032/033 et F-ACT-002/029 ; confronter typologie, méthode, claim et résultats réellement inspectés |
| Signature/noeud de route pris pour obligation de créer une variante ou une correction | F-DIR-009/012, F-ACT-025 ; le one-shot et l'héritage restent valides selon preuve |
| Préfixe ressemblant à une route canonique | Gouvernance EVOLUTION/CHANGELOG et vérification ultérieure des identifiants ; pas de promotion par nom |

## Couverture, limites et reprise

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | TENSION et SIGNATURE dans READ ; routes, préfixes, accès outillé |
| B — sémantique | FULL | 88–157, axes/pôles, temporalité de thèse/signature, premier objet, types et méthodes |
| C — usage | TARGETED | Sept cas contrastés ; aucun test humain ou produit revendiqué |
| D — résistance | TARGETED | Cardinalité F-DIR-012, temporalité, PREVIOUS-LIMIT, accessibilité, déduplication |
| Machine | TARGETED | READ résolu, TENSION/SIGNATURE locators refusés, carte de lecture validée ; projection des types non testée ici |
| Externe | N/A-JUSTIFIED | Aucun claim externe requis pour qualifier ce contrat interne |

Le bloc 2 couvre jusqu'au séparateur 159 et à la ligne vide 160. Aucun patch ni verdict global. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **161–255**, SELECT et DERIVE ; reprendre le protocole §12, ce rapport, la baseline B01, F-DIR-012/018/041 et F-ACT-001/029. Vérifier alors si les préfixes, axes et rôles de preuve orientent une sélection sans menu forcé et si la dérivation reste locale jusqu'à preuve d'un gain réel.
