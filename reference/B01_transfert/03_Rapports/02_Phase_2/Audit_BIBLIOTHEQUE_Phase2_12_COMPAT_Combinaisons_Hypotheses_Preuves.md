# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 12 : COMPAT

## Cadre, précédent vérifié et baseline

- **Source propriétaire :** `audit_work/package/V1/official/BIBLIOTHEQUE.md`, lignes **661–696**. Introduction et champs de lecture 661–674 ; dix lignes de matrice 676–687 ; contrat de compatibilité durable et handoff 689–693 ; séparateur 695. `BIBLIOTHEQUE/GATE` commence à 697 et sera audité au bloc suivant.
- **Méthode :** protocole externe v2.0 §12 relu : A architecture, B contrat sémantique, C usages simulés, D résistance. Rapport COMPONENTS bloc 11, rapport SCENE corrigé et plan de reprise relus. Interfaces ciblées : SELECT 161–205, CONTRACTS 256–284, SUPPORT 288–336, GRID 340–421, SCENE 425–497, OBJECT 501–538, MICRO 542–581, COMPONENTS 611–657, GATE 697–719 et sortie 776–790 ; DIRECTION/FIRST-OBJECT 314–318, SAVOIR/CRAFT CFT-04a 346–359 et ACTION/GATE-A 623–665/B1b 702–716. Ces interfaces vérifient les limites de la table, sans prétendre achever leur diagnostic de phase 2 à la place de leurs propres blocs.
- **Baseline B01 contrôlée, inchangée :** système compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Contrôle du bloc précédent :** la matrice 676 nomme objets et MICRO comme **unités locales**, cohérentes avec `LAYER/OBJECTS` et l'échelle de COMPONENTS 615–629 ; elle ne fournit ni anatomie, ni variants, ni tokens, ni source de vérité d'un composant partagé ordinaire. F-BIB-004 reste donc ouvert. Une ligne favorable ne valide pas davantage `LAYER/BRAND_GRAMMAR` ou un template complet ; aucun amendement nécessaire du rapport COMPONENTS.
- Diagnostic documentaire seulement : les scénarios décrivent des décisions de lecture, pas une interface livrée, des mesures utilisateur, une vérification d'accessibilité exécutée ou un verdict global. Aucune source normative n'est modifiée.

## Passage A — place de la matrice, locators et frontières

COMPAT vient **après** la sélection et les contrats des niveaux ; il donne des **hypothèses** d'assemblage plutôt qu'un catalogue de recettes ou une autorité de classement de mode. Les dix entrées se partagent en quatre supports (678–681) et six scènes (682–687), chacune avec grilles favorables, objets ou micro-interfaces possibles et condition principale. Le tableau ne prescrit pas dix assemblages complets ni un produit à dix surfaces. SUPPORT est le champ spatial et SCENE le scénario de preuve : une ligne de support et une ligne de scène peuvent s'éclairer mutuellement dans un cas donné, sans imposer leur association ni leurs trois grilles à toute la page (SUPPORT 336, SCENE 427–429).

La phrase 663 protège deux lectures distinctes : **présence** dans le tableau = combinaison à éprouver, jamais présomption d'efficacité ; **absence** = rien n'est indiqué ici, jamais contre-indication, permission particulière ou moindre risque. Par exemple `MICRO/USAGE_LEDGER`, `MICRO/IDENTIFICATION_GATE`, `MICRO/ITINERARY_SEGMENTS` et les modificateurs ne figurent pas dans les dix lignes : leurs décisions et états existent toujours dans MICRO/MODIFIER. Une route inventée ou non canonique doit rester déclarée locale ou `PILOT` selon SELECT 142 et la sortie BIBLIOTHEQUE 786 ; l'absence du tableau ne la transforme pas en identifiant publié.

`python3 audit_work/package/scripts/read_route.py BIBLIOTHEQUE/COMPAT` refuse ce titre exact, tandis que le titre existe dans le propriétaire et que `validate_reading_map.py` passe. C'est une occurrence ciblée de **F-DIR-028/F-ACT-001**. L'accès à COMPONENTS au bloc précédent réussissait : l'index du lecteur est partiel, pas entièrement défaillant. La matrice se lit directement dans le propriétaire en attendant l'épreuve d'architecture de l'information et de la machine.

## Passage B — contrat de chaque rangée et statut des preuves

| Ligne et point de départ | Compatibilité proposée et condition à maintenir | Contre-épreuve située, sans présumer de `PASS` |
|---|---|---|
| 678 — `SUPPORT/FREE_FIELD` | `HIERARCHICAL`/`RADIAL`/`BASELINE` avec archive, sélection ou capsule de navigation ; préserver foyer ou cadence | Une collection d'éléments égaux dans un grand champ peut aplatir le choix ; vérifier priorité, entrée et zone de preuve sur contenu/viewport réels. Un contexte opérationnel critique peut refuser le champ malgré la ligne favorable. |
| 679 — `SUPPORT/ARCHITECTED_FRAME` | `COLUMN`/`MODULAR`/`BASELINE` avec fenêtre produit ou capsule ; le cadre sert usage ou preuve | Un châssis prestigieux sans hiérarchie, focus ni lien à l'action ne devient pas preuve de maturité ou de confiance. |
| 680 — `SUPPORT/OPERATIONAL_CANVAS` | `COLUMN`/`MODULAR`/`BASELINE` avec module de données, comparaison ou santé de requête ; ne pas masquer les lectures de même importance | Un panneau expressif peut cacher période, référence, source ou erreur d'une mesure ; tester la lecture et l'action réelles, pas la seule silhouette du dashboard. |
| 681 — `SUPPORT/COLLECTION_PLINTH` | `MODULAR`/`HIERARCHICAL`/`BASELINE` avec archives ou sélections ; foyer ponctuel et comparaison toujours possible | Métadonnées et liens doivent rester retrouvables ; une exposition espacée peut coûter trop d'effort si comparaison rapide ou manipulation dense domine. |
| 682 — `SCENE/INSTRUMENT` | `COLUMN`/`BASELINE`/`MODULAR` avec données, santé de requête ou état d'entités ; décision et mesure avant récit d'écosystème | `MICRO/QUERY_HEALTH` exige période, source, fraîcheur, diagnostic et prochaine action ; la scène ne remplace ni la donnée ni sa preuve. |
| 683 — `SCENE/EDITORIAL_FIELD` | `HIERARCHICAL`/`RADIAL`/`BASELINE` avec sélection, archive ou fenêtre produit ; image/paysage porte une relation, preuve produit explicite | `SCENE` 443–445 autorise une projection initiale avec preuve détaillée ultérieure ; « explicite » requiert lien et vérité de la relation, **pas** un objet sensible forcé au premier viewport. DIRECTION 316 versus SAVOIR 348 reste divergence de priorité du premier contact, à consolider, sans faux produit ou action fictive. |
| 684 — `SCENE/FRAMED_PRODUCT` | `COLUMN`/`MODULAR`/`BASELINE` avec fenêtre produit/capsule ; châssis soutient usage et confiance | Observer l'état produit et la relation au titre ; mockup sans fonction ou navigation masquée par cadre/overlay n'établit ni produit effectif ni accessibilité. |
| 685 — `SCENE/OPERATING_GRID` | `MODULAR`/`COLUMN`/`BASELINE` avec données, requête ou état d'entités ; ruptures pour action/alerte prioritaire | Une exception urgente ne peut disparaître dans cellules identiques ; préserver donnée, dénominateur, état et conséquence avec vérification dans la tâche. |
| 686 — `SCENE/SPLIT_PROOF` | `AXIAL`/`HIERARCHICAL`/`COLUMN` avec données ou fenêtre produit ; artefact au centre, sans split décoratif | Une moitié 50/50 et un screenshot générique sans mécanisme ne constituent pas preuve ; distinguer la scène `SPLIT_PROOF` d'un `OBJECT/COMPARISON_SPLIT` local (SCENE 479). |
| 687 — `SCENE/PRODUCT_NARRATIVE` | `HIERARCHICAL`/`COLUMN`/`MODULAR` avec fenêtre produit ou profil ; la fenêtre répond directement à la promesse | Vérifier une interaction/état représentatif et le statut de vérité du produit ; un profil crédible ou une capture seule ne démontre pas la capacité, le comportement ou l'usage revendiqués. |

La matrice qualifie **la relation possible** entre niveaux ; elle ne rend pas l'unité « locale » automatiquement indépendante de son contrat durable lorsqu'elle est publiée pour plusieurs consumers. Une ligne n'exige pas de sélectionner toutes les grilles et tous les objets cités. Une combinaison support/scène pertinente peut partager certains éléments, mais si leurs conditions tirent en sens opposés dans un même viewport, le lecteur doit préciser surface, séquence, priorité et responsabilité dominante, puis observer le résultat ; COMPAT n'est pas un algorithme pour fusionner des grilles incompatibles.

### Champs de lecture et contrat durable (663–674, 689–693)

Les **six lignes de lecture regroupent huit libellés** : `DECISION`, `PROOF-TYPE`, `PROOF-SCOPE`, `PROOF-LIMIT`, `RISK`, `RESPONSIVE-RELATION`, `CRITICAL-STATES` et `EXIT-CONDITION` (la triade PROOF partage une ligne). Ce sont des **questions à poser à la combinaison** ; ce ne sont ni routes, ni statuts, ni champs JSON créés par COMPAT. Ils obligent à nommer ce qui changera dans la décision, quel risque sera protégé, quelles relations survivent au mobile ou à un autre médium, quels états sont critiques et quelle preuve pourra effectivement faire sortir la combinaison. Le type de preuve décrit le claim, la méthode ACTION l'observation : un type `USER/TASK` écrit à l'avance n'est pas un test utilisateur exécuté (BIBLIOTHEQUE 144–157, ACTION 659–665).

Le contrat de **compatibilité durable** 691 ajoute relation de preuve, décision dominante, contre-indication, recomposition responsive, états critiques, scope, méthode, owner, limite et condition de sortie. Il complète CONTRACTS 258–284 et les obligations des routes **partagées/durables** ; il ne transforme pas un croquis local sans risque dominant en dossier universel. Si une combinaison ne peut pas encore répondre à ces champs, 693 la laisse exploratoire ou locale ; cela n'accorde pas de passer outre un état critique activé ou le contrôle ACTION applicable. Pour un run livrable, METHOD/SCOPE, provenance et issue reviennent à ACTION ; pour une candidature durable, usages contrastés, gain, maintenance et décision CHANGELOG restent à EVOLUTION 733–770. Ce partage préserve la réserve F-BIB-002 sur le contrat local, sans ajouter ici une prescription fautive équivalente.

La sortie 693 transmet les contrôles **structurels** à BIBLIOTHEQUE/GATE puis les statuts et verdicts à ACTION. `GATE` n'est pas un quatrième gate global (697–701) et COMPAT n'a ni statut ni PASS propre. Même la plus pertinente des dix lignes ne dispense de regarder la recomposition, les états, la confidentialité, les permissions, la disponibilité de l'action ou le coût de performance selon le risque. Une observation perceptuelle n'établit pas à elle seule la réussite de tâche ; l'intégration concrète de l'objet et de la scène est requise là où le risque l'exige (CONTRACTS 284, OBJECT 538).

## Passage C — simulations de lecture sous contrainte

| Situation | Décision et prochaine preuve | Mauvaise lecture à détecter |
|---|---|---|
| Designer, premier contact intime sur champ libre | Évaluer `FREE_FIELD` et `EDITORIAL_FIELD` sans vitrine intrusive ; formuler relation produit, limite, moment de preuve et conflit DIRECTION/SAVOIR à reprendre | Forcer `PROOF_PRODUCT_STAGE` au hero parce que la table le suggère à 683 |
| Designer, archive à pièces distinctes et recherche fréquente | Comparer `COLLECTION_PLINTH` à besoin réel de comparaison ; vérifier métadonnées/retrouvabilité dans le viewport | Prendre une plinthe élégante pour un parcours de recherche réussi |
| Équipe produit, tableau d'exploitation où erreur réseau et alerte coexistent | Combiner support opérationnel et scène de grille seulement si décisions distinctes ; tester santé de requête et rail d'entités, erreur, fraîcheur et action | Se satisfaire des deux lignes 680/685 comme si leur répétition faisait preuve |
| Reviewer, `USAGE_LEDGER` nécessaire mais absent de la matrice | Lire sa route MICRO 560 et le contrat applicable, l'intégrer dans la scène qui répond à la tâche | Déclarer incompatibilité ou sécurité moindre par absence du tableau |
| Intégrateur, split décoratif montrant une simulation de produit | Exiger artefact et marquage de vérité adaptés ; si la comparaison n'est pas réelle, changer scène/objet ou rester exploratoire | Appeler preuve une symétrie visuelle et un mockup |
| Designer, support libre et scène instrument dense dans deux sections successives | Scoper chaque section et sa transition ; choisir grilles selon la décision dans chacune, observer priorité et action sur mobile | Exiger un seul triplet de routes pour l'ensemble de la page |
| Mainteneur, combinaison non listée avec micro-interface d'identification critique | Déclarer route canonique ou locale, task/états/récupération, méthode et test requis selon le risque | Se croire exempt de sécurité ou d'accessibilité parce que non listé |
| Agent, résultat d'inspection d'une seule capture desktop | Limiter `PERCEPTUAL` à sa surface/version ; observer états et mobile si dans scope, réserver tâche et performance | Annoncer PASS U/A/T global depuis la correspondance avec une ligne |
| Équipe système, combinaison répétée dans plusieurs produits | Examiner usages contrastés, compatibilité, owner, migration et gain avant toute promotion ; décision CHANGELOG | Transformer la table indicative en template ADOPTED par fréquence |

Ces neuf scénarios sont des **simulations documentaires**. Aucun délai, taux de réussite, comportement utilisateur ou changement de statut en production n'est mesuré.

## Passage D — résistances et constats rattachés

| Épreuve | Observation ou propriétaire de la suite |
|---|---|
| Une route absente du tableau est prise pour incompatibilité, interdiction ou exemption | 663–674 l'excluent explicitement ; lire la route propriétaire et son contrat, puis juger risque et preuve. Aucun nouvel ID. |
| Une ligne favorable est appliquée comme recette par défaut | 663, 674 et SELECT 163–167 demandent décision changée, condition, contre-indication et preuve située ; une combinaison de noms ne conclut rien. |
| Des grilles de deux lignes support/scène sont imposées ensemble sur tout le produit | Champ et scénario diffèrent (SUPPORT 336, SCENE 429) ; scope et responsabilité dominante doivent guider, sans matrice cartésienne universelle. |
| `EDITORIAL_FIELD` lu comme obligation de preuve détaillée dans le premier hero | Ligne 683 dit « preuve produit explicite », SCENE 445 permet une preuve détaillée ultérieure et SAVOIR 348 un geste initial ; maintenir divergence DIRECTION 316/SAVOIR CFT-04a sous F-DIR-018/024, sans inventer de synthèse globale. |
| COMPAT confondu avec une preuve de compatibilité exécutée ou un gate autonome | 691–693 borne contrat et handoff ; ACTION 653–665 garde méthodes/résultats, GATE 697–701 structure. Aucun PASS implicite. |
| La matrice supposée remplir le contrat de composant partagé | F-BIB-004 garde son objet : aucune anatomie/variant/source de vérité de primitive partagée n'est fournie en 663–693 ; `PROOF-SCOPE` de combinaison ne remplace pas ce contrat. |
| Le lecteur CLI ne localise pas COMPAT tandis que COMPONENTS fonctionnait | Nouvelle occurrence de F-DIR-028/F-ACT-001 seulement, à évaluer avec les titres réellement déclarés et la carte dérivée. |

**Pas de nouvel ID F-BIB autonome.** Le texte possède ses exceptions : hypothèse et non prescription (663), combinaison non listée admise (674), contrat fort réservé à la compatibilité durable (691) et handoff sans verdict (693). F-BIB-001 sur l'exception B1b de SELECT et F-BIB-003 sur GRID/MOBILE ne sont pas corrigés par COMPAT ; la règle de risque/action reste chez leurs propriétaires. La divergence du premier contact reste ouverte et F-BIB-004 sur le contrat de composant partagé n'est pas absorbé par la table. L'efficacité de ces associations demeure non vérifiée tant qu'un rendu situé et des tâches pertinentes ne sont pas observés.

## Couverture et prochaine unité

| Passage | Profondeur | Couverture et limite |
|---|---|---|
| A — architecture | FULL | 661–696, dix lignes de matrice, absence permise, CLI refusé |
| B — sémantique | FULL | Dix conditions principales, champs de lecture, contrat durable et handoff |
| C — usage | TARGETED | Neuf cas simulés ; aucune combinaison testée sur produit réel |
| D — résistance | TARGETED | Hypothèses, absent, priorité de preuve, F-BIB-004 préservé ; pas de nouvel ID |
| Machine | TARGETED | `read_route.py` COMPAT refusé, carte valide ; pas de validation de fixtures d'assemblage dans ce bloc |
| Externe | N/A-JUSTIFIED | Aucun fait externe requis pour lire ces hypothèses internes ; leurs résultats empiriques restent à produire |

Le séparateur est à 695 et la ligne 696 est vide. **Prochaine unité :** `BIBLIOTHEQUE.md`, lignes **697–732**, `GATE` ; relire §12 et le présent rapport, vérifier le contrôle structurel, ses dix questions, l'absence de quatrième gate global et la preuve ACTION avant tout verdict.
