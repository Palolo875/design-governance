# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 11 : CONTEXT

## Cadre et sources

- Baseline `B01`, profil `DEEP` à profondeur adaptée ; source propriétaire `V1/official/SAVOIR.md`, lignes **708–743** : titre 708, partage de responsabilité 710, principes 712, enjeux critiques 714–726, responsive 728–732, motion et espace 734–740, séparateur 742. `SAVOIR/TECH` commence à **744** et se termine à **782** ; `SAVOIR/TOOLS` commence à 784.
- Méthode : protocole externe v2.0 §12, passages A à D ; plan maître, rapport SAVOIR bloc 10 et checkpoints ACTION/DIRECTION relus. Interfaces ciblées : `DIRECTION/START` 129–144 et capacités 680–694 ; `SAVOIR/CRAFT` 93–100 et 325–339, `DESIGN-ATLAS` 534–560, `STYLE` 645–657, `TECH` 744–780 ; `ACTION/GATE-A` 622–680 et contrat motion/scène 597–602 ; `BIBLIOTHEQUE/SELECT` et `SCENE/EDITORIAL_FIELD` 443–447.
- Empreintes revérifiées, inchangées : compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR propriétaire `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Statut : lecture sectionnelle, sans modification de V1, verdict global ou claim de conformité. Les constats antérieurs F-SAV-001 à 007, F-ACT-001 à 039 et F-DIR-001 à 046 sont transportés, sans nouvelle conclusion sur leurs suites.

## Passage A — architecture visible

`SAVOIR/CONTEXT` réunit trois sous-contrats : protection adaptée aux enjeux, adaptation de la présentation et de l'interaction aux supports, jugement de la motion et de l'espace. Le préambule attribue correctement la **décision contextualisée** à SAVOIR et le **contrôle exécuté**, sa méthode, sa portée et son verdict à ACTION. Il ne fournit ni référentiel de conformité universel ni procédure technique de test ; ces objets passent à `ACTION/GATE-A` et `SAVOIR/TECH`. La liste de contextes à fort enjeu est indicative, ce qui évite de faire d'une taxonomie une condition d'accès au contrôle.

Le routage de `SAVOIR/ROUTING` 79 et de `DIRECTION` 757 vise cette section lorsque contexte critique, responsive, performance ou motion peuvent changer la décision. La section suivante `TECH` explicite la preuve selon le médium. **Test machine de navigation :** `python3 audit_work/package/scripts/read_route.py SAVOIR/CONTEXT` retourne `ROUTE READ FAILED — locator inconnu`, alors que `validate_reading_map.py` retourne `READING MAP VALIDATION PASSED`. Le titre et la ligne sont accessibles en lecture directe. C'est la manifestation déjà ouverte de **F-DIR-028/F-ACT-001**, sans nouvel ID.

## Passage B — contrat sémantique, phrase par phrase

### Accessibilité et responsabilité (710–712)

Le contraste « calculé », la sémantique, le nom accessible, le clavier, le focus visible, l'information non chromatique, les cibles, la motion réduite, le contenu long et la récupération sont des **questions de conception et de contrôle selon leur applicabilité**. Leur énumération ne prouve pas qu'un composant les satisfait. `ACTION/GATE-A` exige un médium, un scope, un référentiel/niveau visé lorsqu'applicable, un échantillon, une méthode, des limites et une prochaine preuve. Un contrôle applicable non exécuté reste `NOT-VERIFIED` ; un input inexistant dans un médium peut recevoir `N/A-JUSTIFIED` avec raison, son substitut devant être testé. Pour un projet Web visé par WCAG 2.2 AA, l'absence d'un test de motion pertinent n'est ni une conformité implicite ni automatiquement la violation de tous les critères WCAG. Le critère WCAG 2.2 « Animation from Interactions » est au niveau AAA et admet une exception pour l'animation essentielle ; le devoir de fournir une adaptation dans ce système peut être plus exigeant que la cible de conformité déclarée. Sources primaires : [WCAG 2.2, critère 2.3.3](https://www.w3.org/TR/WCAG22/#animation-from-interactions) et [W3C, compréhension du critère 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). Distinguer obligation de V1, standard applicable, cible du projet, observation et claim externe.

### Contextes à fort enjeu (714–726)

Les trois catégories sont des exemples, pas des modes ni une liste fermée. En santé/paiement/commande critique, examiner confirmation, prévention et récupération ; en décision intensive, précision et densité utile ; en jeu ou temps réel, feedback et latence. Si une expression entre réellement en tension avec une protection critique déclarée dans `DIRECTION/START`, cette protection prime. Cela ne décrète pas toutes les surfaces d'un même secteur identiques ni automatiquement critiques : le risque est attaché à la tâche, à l'état et au changement observés. La sémantique de la phrase « non par un effet spectaculaire » dépend du conflit annoncé : elle ne bannit pas toute expression hors de cette tension. Aucune nouvelle contradiction indépendante de F-DIR-007 ou de la protection `START` n'est établie ici.

### Responsive et performance (728–732)

« Recomposer plutôt que comprimer » est une règle de jugement sur hiérarchie, séquence et tâche ; elle n'autorise pas à faire disparaître une action, un statut, le contenu essentiel ou l'erreur sur un support plus étroit. L'espace média, le feedback rapide, l'attente signalée et la récupération ont des effets observables, mais « immédiat » ne crée pas à lui seul de seuil temporel. CSS, viewport, formats, budgets et compatibilité sont traités comme ressources techniques dont la valeur est à justifier par le runtime. Un export print, une interface native ou une scène spatiale requiert la preuve propre au support et aux idiomes d'interaction réellement présents ; `SAVOIR/TECH` 764–780 poursuit cette dérivation. La réserve **F-DIR-038** subsiste pour les formulations Web/mobile plus générales des autres propriétaires ; CONTEXT ne la résout pas à lui seul.

### Motion et espace (734–740)

La motion a une fonction explicative, de confirmation, d'orientation ou de relation matérielle ; elle ne doit pas ralentir une tâche. Pour l'animation interactive, états initial, déclencheur, transition, interruption et résultat donnent un objet vérifiable. La scène spatiale est rattachée à produit/profondeur/navigation/information ; la réduction de mouvement, l'alternative, l'interruption, les différents inputs, les supports et la performance sont examinés selon le risque et le médium. La capture prouve seulement le rendu dans son périmètre, jamais l'accès au clavier, la performance ou l'issue d'une tâche. Une **alternative de motion seulement prévue** ne vaut pas une alternative observée sur l'artefact livré (**F-ACT-033**). Un `PASS` borné ne constitue pas une attestation WCAG globale (**F-ACT-035**).

La formulation **« doit expliquer, confirmer, orienter ou rendre une relation matérielle compréhensible »** (736), le **« seulement »** limitant la scène spatiale (738) et la préférence pour la suppression ou la 2D si ni feedback, ni information, ni relation spatiale (740) présentent toutefois un filtre de justification plus étroit que les autres contrats expressifs. Cette divergence motive F-SAV-008 ci-dessous ; elle ne dispense en aucun cas des protections d'accessibilité ou de la tâche.

## Passage C — lecteurs et parcours sous contrainte

1. **Designer, transition d'état d'un formulaire de paiement.** Une motion rend la confirmation compréhensible et ne retarde pas l'opération ; le risque critique requiert confirmation, récupération, état interrompu et alternative adaptée. Un GIF ou une capture seuls ne prouvent ni clavier ni reduced motion ; ACTION contrôle l'artefact et garde `NOT-VERIFIED` pour ce qui reste non exécuté.
2. **Designer, prologue narratif d'une expérience culturelle.** La chorégraphie exprime une mémoire et une émotion choisie, sans expliquer un état, orienter un geste ou représenter une profondeur. `SAVOIR/CRAFT` 96/100 et `DESIGN-ATLAS` 539/552–560 admettent une conséquence narrative/perceptive ; `ACTION` 597–602 admet un « rôle utilisateur ou narratif » et une « décision de direction ». Lecture littérale de CONTEXT 736/740 : préférence pour son retrait ou une 2D, même si l'expérience a une direction observable. C'est le cas discriminant F-SAV-008 ; la réduction du mouvement, le contenu accessible et l'absence de retard restent des conditions indépendantes.
3. **Équipe produit, parcours de découverte en 3D sans fonction métrique.** Une installation spatiale sert une projection culturelle et une présence sensible ; STYLE 654 reconnaît l'espace comme registre. La formule « justifiée seulement » de CONTEXT 738 peut l'exclure si elle ne rend pas *plus compréhensible* un produit, la navigation, la profondeur ou l'information. Une scène purement gratuite reste candidate au retrait selon ACTION 600 ; le critère de distinction est la décision située et observée, pas la présence de 3D.
4. **Intégratrice, reflow d'une supervision dense sur mobile.** Réorganiser données, statut et actions sans les perdre ; tester le support et les états concernés, inscrire l'absence de support si aucun runtime mobile n'est disponible. Ne pas importer automatiquement un budget Web sur un écran natif ou spatial. F-DIR-038/F-ACT-004/005/017/018/038 restent à éprouver sur leur propriétaire.
5. **Reviewer, scène spatiale et capture séduisante.** Demander les entrées appropriées, la vidéo ou la preuve runtime selon la décision, le fallback et les états ; distinguer capture, avis perceptuel, tâche observée et performance mesurée. Maintenir `NOT-VERIFIED` sur une exigence applicable non vérifiée au lieu de produire un `PASS` par extrapolation.

## Passage D — résistance et registre

### F-SAV-008 — critère de justification de la motion et de la scène spatiale trop étroit

- **Gravité provisoire : Significatif à éprouver.** Divergence textuelle entre propriétaires constatée ; fréquence et dommage en situation réelle non mesurés.
- **Preuve :** CONTEXT 736 énumère explication, confirmation, orientation, relation matérielle ; 738 n'admet une scène 3D ou spatiale « seulement » si elle rend plus compréhensibles produit, profondeur, navigation ou information spatiale ; 740 conseille suppression ou 2D hors feedback/information/relation spatiale. En regard, `SAVOIR/CRAFT` 96/100 admet l'émotion choisie et la direction ; `DESIGN-ATLAS` 539/552–560 nomme les effets narratif, perceptif et identitaire ; `STYLE` 654 traite mouvement et espace comme moyens de profil ; `ACTION` 597–602 reconnaît expressément le rôle narratif et la décision de direction ; `BIBLIOTHEQUE/SCENE/EDITORIAL_FIELD` 443–445 accepte la projection émotionnelle/culturelle précédant une preuve.
- **Conséquence plausible :** retrait ou aplatissement d'une expérience narrative/identitaire située alors même que sa direction est justifiée, observable et protégée par un fallback ; inversement, permettre un « rôle narratif » sans lien réel avec le produit ouvrirait la porte à des effets gratuits. Les deux risques doivent être évités.
- **Atténuations :** « relation matérielle » peut parfois inclure une relation narrative ; une scène porteuse de produit peut être couverte par 738 ; l'ATLAS exige déjà une relation observable et ACTION écarte les effets sans décision de direction. Ces lectures sauvent certains cas, mais n'annulent pas le caractère fermé de « doit », « seulement » et du dernier test 740 pour le contre-exemple ci-dessus.
- **Propriétaire pressenti :** SAVOIR/CONTEXT 736–740 pour aligner la justification des effets avec le rôle narratif ou la direction retenue, sous protection de START et preuve ACTION ; ni nouveau quota de motion, ni dérogation générale à accessibilité/performance/récupération.
- **Relations :** distinct de F-SAV-006 (test de masquage du style image/couleur), de F-ACT-033 (alternative prévue non observée), de F-DIR-038 (médiums) et de F-DIR-018 (premier objet). `ACTION` 600 explicite déjà la direction, donc ce constat porte sur le filtre local de CONTEXT et l'effet sur le choix créatif.
- **Test à la phase de simulation :** trois briefs contrastés : transition de confirmation purement fonctionnelle ; introduction narrative clairement reliée à la promesse produit mais sans explication d'état ; scène spatiale décorative sans relation située. Faire suivre chaque lecteur par CONTEXT, puis par CRAFT/STYLE et le contrat ACTION ; comparer décision de garder/adapter/retirer, fallback, preuve et tâche, avec et sans préférence de réduction de mouvement. Ne qualifier de défaut prouvé que la divergence qui produit effectivement une mauvaise décision.

### Constats transportés sans doublon

| Interface observée | Statut et suite |
|---|---|
| Route CONTEXT nommée mais locator refusé et carte verte | F-DIR-028/F-ACT-001, reproduction locale ; inspecter le registre des routes à la phase machine |
| `GATE-A` demande alternative motion mais carte peut porter un `PASS` sur prévision seule | F-ACT-033, confirmé sur test ACTION antérieur ; aucune mutation répétée ici |
| PASS de portée bornée et claim de conformité général | F-ACT-035 ; nommer référence, version, niveau, scope, méthode exécutée et limites |
| Contrôles Web/mobile appliqués sans dérivation du médium | F-DIR-038, F-ACT-004/005/017/018/038 ; `SAVOIR/TECH` est l'interface suivante |
| Choix de mode/risk si découverte d'un changement critique ou partagé | F-SAV-007 et DIRECTION/START ; aucune reclassification nouvelle sur les cas de cette section |

## Couverture, limites et reprise

| Passage | Profondeur | Évidence |
|---|---|---|
| A — architecture | FULL | Titre, préambule, sous-sections, route, handoff et locator |
| B — sémantique | FULL | Lignes 710–740 par groupes de phrases ; preuve, périmètre, médium et exception |
| C — usage réel | TARGETED | Cinq lecteurs/scénarios, dont deux cas discriminants expressifs |
| D — résistance | TARGETED | F-SAV-008 provisoire ; protection des constats antérieurs contre duplication |
| Machine | TARGETED | Locator CONTEXT refusé, reading map valide ; tests ACTION antérieurs référencés |
| Externe | TARGETED | W3C officiel consulté pour la distinction entre exigence V1, niveau WCAG et preuve de conformité ; aucun test de produit réel réalisé |

Les protections positives comprennent : division claire du jugement et du verdict, priorité des risques critiques, liste non exhaustive des contextes, recomposition selon le support, animation décrite par états, interruption et fallback, et refus d'inférer la réussite d'une tâche ou l'accessibilité à partir d'une capture. Les autres constats restent provisoires jusqu'aux parcours et contrôles transversaux. Aucun patch normatif, aucun verdict global.

**Prochaine unité :** `SAVOIR/TECH`, lignes **744–783**, avec attention aux preuves par médium, au statut `CONFORMANCE-TARGET`, à l'absence de runtime et à l'ordre de priorité P0–P3 ; `SAVOIR/TOOLS` commence à 784.
