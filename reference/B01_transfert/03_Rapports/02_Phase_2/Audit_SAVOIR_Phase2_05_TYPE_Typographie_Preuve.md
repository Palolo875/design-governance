# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 5 : TYPE et preuve typographique

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **377–414** ; `SAVOIR/TYPE` lignes 377–411, séparateur 413. `SAVOIR/STATE` commence ligne 415 et attend le prochain bloc.
- Protocole externe : §12, passages A architecture, B contrat sémantique, C usage réel simulé, D résistance. Reprise vérifiée avec le rapport SAVOIR bloc 4, le plan maître et les constats des checkpoints ACTION/DIRECTION. Interfaces : `ACTION/STRUCTURED-PROOF` (527–570), `ACTION/RUN_CARD`, `ACTION/GATE-A` et adéquation des preuves, `DIRECTION/START`, `SAVOIR/CRAFT` et le futur `SAVOIR/STATE` sans préjuger son diagnostic.
- Baseline B01 stable : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Diagnostic documentaire ciblé, sans police livrée à inspecter : ni verdict sur un produit, ni test de licence d’une famille donnée, ni patch du système. Les tests antérieurs de `RUN_CARD` sont repris lorsqu’ils suffisent ; le présent bloc vérifie localement les routes et la structure des champs.

## Résumé du bloc

TYPE est court et substantiel. Il relie le choix d’une famille à la langue, aux chiffres, à la ponctuation, à la lecture, au coût, à la licence, au fallback et au comportement sous zoom/reflow ; il traite les familles variables sans supposer la présence de leurs axes. Sa grille de preuve distingue **reconnaissance des caractères**, **lecture en contexte**, **hiérarchie**, **tonalité perçue** et **effet sur la tâche**, avec `LIMIT`. Une impression de marque ne suffit jamais à conclure qu’une police est « supérieure ».

Le raccord à ACTION reste incomplet : la « partition typographique complète » d’`ACTION/STRUCTURED-PROOF` ne prévoit explicitement ni tous les critères de choix ni cette séparation des preuves. Son titre « contrats avant build » pourrait en outre recevoir des résultats post-build prématurément. Ces mécanismes sont déjà suivis comme **F-ACT-032** et **F-ACT-030** ; la route `SAVOIR/TYPE` et la route `ACTION/STRUCTURED-PROOF` sont refusées par le lecteur officiel malgré des sections présentes, occurrence de **F-DIR-028/F-ACT-001**. Aucun nouvel ID SAVOIR n’est nécessaire sur ces 38 lignes.

## Passage A — architecture visible

| Lignes | Autorité / décision | Handoff et limite |
|---|---|---|
| 377–379 | `[REQUIS PAR LE MODULE — lecture, ton, données, hiérarchie ou surface identitaire]` ; choisir selon langue, chiffres, ponctuation, graisses, lisibilité, licence, performance, fallback et ton | Déclencheur par responsabilité typographique, pas obligation de changer la famille à chaque run |
| 381–385 | Interroger la famille fréquente et le système existant ; « une ou deux voix » `[À ADAPTER]` ; rôle, ligne, interligne, figures tabulaires, chargement | Heuristique explicite, sans quota de polices ou interdiction d’une famille répandue |
| 387–389 | Variable font : employer uniquement les axes livrés ; vérifier signature sous zoom, reflow, locale et ajustement d’espacement | Choix technique et perceptuel avant claim de robustesse ; le rendu doit être réellement inspecté |
| 391–402 | « Preuve typographique » déclenchée si la typographie peut changer la décision ; cinq dimensions et `LIMIT` | ACTION possède méthode, observation, trace et verdict ; un plan ne devient pas preuve par remplissage |
| 404–411 | Quatre familles d’échantillons et contre-indication ; U dominant → effet sur tâche prouvé par ACTION | Une capture de spécimen peut informer V/forme, pas démontrer à elle seule U |

Dans B01, `read_route.py SAVOIR/TYPE` et `read_route.py ACTION/STRUCTURED-PROOF` répondent chacun « locator inconnu » alors que les deux titres existent aux lignes indiquées. `validate_reading_map.py` passe. Cela confirme la couverture partielle déjà constatée ; une recherche manuelle dans les sources permet de retrouver les contrats, mais l’échec CLI peut faire manquer les critères de TYPE à un agent qui se fie aux routes outillées. Ce passage n’ajoute pas un ID par locator.

## Passage B — contrat sémantique, phrase par phrase

### Choix, convention et proportion (377–385)

Le tag de la ligne 379 porte sur des décisions de typographie qui affectent lecture, ton, données, hiérarchie ou identité ; il exige un **choix informé**, pas une refonte automatique. La ligne 381 admet une famille courante lorsque le système hérité ou le contexte la justifie : le défaut visé est la sélection réflexe sans comparaison, examen de l’existant **ou** raison formulée. Cette disjonction évite de forcer une police concurrente pour justifier une correction locale.

« Une ou deux voix expressives » (383) est une heuristique `[À ADAPTER]`, pas un plafond universel, et une famille dédiée aux données n’est pas nécessairement une nouvelle voix expressive. C’est plus précis que de compter les fichiers chargés comme autant de partis pris créatifs ; les rôles fonctionnels, éditoriaux, microcopie, données et signature se retrouvent dans la table d’ACTION (562–568). La ligne 385 ajoute mesure et interligne, figures tabulaires, hiérarchie, fallback et chargement ; une signature forte qui perd les chiffres corrects ou la lecture longue n’est pas une décision tenue.

### Variable font et robustesse (387–389)

Poids, largeur, taille optique et grade sont des **possibilités conditionnelles** d’un fichier livré. « Lorsqu’il existe » borne le grade ; « n’utilise que les axes présents » empêche d’imaginer un réglage inexistant. La préférence pour les propriétés de haut niveau et la méfiance envers les styles synthétiques non déclarés ne prétendent pas que toute police variable est meilleure. Le critère de sortie est la signature réelle sous locale, zoom, reflow et ajustement d’espacement, pas la seule capture nominale. Sans runtime ou famille concrète, le présent bloc ne vérifie aucun axe, glyph, fallback, chargement ni droit effectif : les claims d’implémentation restent à vérifier dans un run.

### Preuve, limites et transfert à ACTION (391–411)

Le déclencheur « lorsque la typographie peut changer la décision » (393) permet de conserver un système existant avec sa raison si aucune nouvelle décision typographique n’existe ; `ACTION/STRUCTURED-PROOF` ligne 560 le confirme. La liste (396–401) sépare explicitement : reconnaissance de lettres/chiffres ou glyphes (`FORM-LEGIBILITY`), lecture d’un vrai texte (`TEXT-READABILITY`), différence entre rôles (`HIERARCHY`), tonalité située (`PERSONALITY`), et changement de compréhension ou d’action mesurable/observable lorsqu’il est pertinent (`TASK-EFFECT`). `LIMIT` empêche de transformer un spécimen réussi en preuve globale. Tous ces axes ne sont pas obligatoires pour chaque micro-delta ; les activer selon la décision et le risque.

Les quatre types de preuve (406–409) imposent contenu réel selon rôle, situations adverses (longueur, locale, chiffres, zoom, caractères absents), rendu du couple taille/interligne/mesure et décision améliorée ou contre-indication. Il manque une application exécutée à ces phrases : la table d’ACTION prépare rôles et paramètres avant le build, mais n’indique pas directement les cinq résultats de preuve, la licence ou le coût de chargement. F-ACT-032 porte déjà ce déficit. La `RUN_CARD` structurée n’offre pas de champs nommés `typography_partition`, `form_legibility`, `text_readability` ou `task_effect` : elle accepte la preuve textuelle, une provenance et un locator vers une trace détaillée, sans garantir à elle seule cette partition. F-ACT-002/021 décrivent la nécessité d’un mapping du contrat humain vers cette trace et le verdict ; la réponse n’est pas automatiquement d’ajouter quatre colonnes au JSON.

« Preuve documentée dans `ACTION/STRUCTURED-PROOF` » (393) renvoie à un bloc **avant build** (ACTION 527). Une partie de TYPE est nécessairement postérieure au build ou à une tâche observée : rendu réel, fallback effectivement affiché, zoom/reflow testé et résultat U. La lecture sûre sépare cible/méthode avant build et observation/résultat après, avec version et limite ; la source ACTION ne donne pas encore cette séparation en un contrat univoque. F-ACT-030 et F-ACT-005 portent ce risque de remplir « observed » sur une intention. La ligne 411 réaffirme que personnalité/« impression de marque » ne mesure pas l’effet sur la tâche ; si U domine, `ACTION/GATE-A` (659–665) privilégie utilisateur représentatif, tâche et résultat et conserve les limites de méthode.

## Passage C — lecteurs sous contrainte de temps

1. **Designer, microcopie LITE sans changement de système.** Il vérifie que la police existante rend la nouvelle chaîne dans la langue et la mesure touchées, note la conservation et sa raison. Il ne fabrique ni alternative décorative ni partition complète sans déclencheur.
2. **Designer, nouvelle surface multilingue.** Il contrôle caractères, chiffres, ponctuation, petits corps, police de fallback, texte long et licence ; un specimen latin parfait ne valide pas une locale différente ou des glyphes absents.
3. **Intégrateur, famille variable choisie.** Il confirme les axes **effectivement livrés**, désactive les styles synthétiques non déclarés, observe poids/largeur/grade et teste zoom, espace utilisateur et reflow. La promesse « variable » seule ne prouve pas la résilience.
4. **Reviewer, titre singulier jugé beau.** Il peut qualifier `PERSONALITY` et hiérarchie sur un rendu inspecté, mais laisse lecture longue, chiffres, fallback et `TASK-EFFECT` non vérifiés s’ils ne l’ont pas été ; « signature premium » ne remplace pas une méthode.
5. **Équipe produit, tâche U dominante.** Une variante semble plus claire en capture ; la claim de réussite exige tâche et contexte, observation de personnes pertinentes ou limite explicite, et résultat selon ACTION. Le jugement V du reviewer ne couvre pas U.
6. **Agent, route indisponible.** Il ouvre manuellement le titre de SAVOIR/TYPE et d’ACTION/STRUCTURED-PROOF, confronte les deux tables et évite de prendre une partition déclarée « complète » pour couverture de licence, glyphes, chargement et cinq preuves.
7. **Mainteneur, validation de `RUN_CARD`.** Il peut trouver la provenance et le locator des tests mais ne lit pas cinq champs typographiques dédiés dans le schéma ; il suit la trace effective avant de conclure à une preuve suffisante.

## Passage D — résistance et registre

### Interfaces éprouvées sans nouvel ID

| Cas de résistance | Comportement contrôlé / réserve |
|---|---|
| Locale avec glyphes absents, chiffres tabulaires et fallback différent | TYPE (379, 385, 407) nomme les facteurs ; ACTION « partition complète » (558–570) ne leur donne pas tous un contrôle explicite : **F-ACT-032**. Un rôle ou une justification libre pourrait néanmoins les documenter ; impact réel à tester. |
| Exemple pré-build déclaré déjà observé | TYPE (393, 408–411) exige rendu et tâche lorsque pertinent, ACTION/STRUCTURED-PROOF se dit avant build : **F-ACT-030/005** ; statut `planned` ≠ résultat `observed`. |
| Specimen beau mais tâche U inconnue | TYPE (411) et ACTION (659–665) interdisent l’inférence ; capacité d’observer la tâche et scope doivent être vérifiés : **F-ACT-018/021**, pas un nouveau défaut TYPE. |
| Licence ou temps de chargement inconnus | TYPE les demande (379, 385) ; l’autorisation de livrer et le coût réellement constaté ne suivent pas d’une case remplie : **F-ACT-024** pour les droits d’asset dans le scope pertinent, **F-ACT-032** pour l’omission locale, autres contrats à vérifier. |
| `SAVOIR/TYPE` et `ACTION/STRUCTURED-PROOF` non ouverts par la CLI | Titres propriétaires présents, clés absentes, carte dérivée validée : **F-DIR-028/F-ACT-001**. Recherche manuelle possible ; pas de conclusion « section supprimée ». |
| TYPE actif avec FRAME, CRAFT, SOURCE, CONTEXT sur un projet réel | **F-SAV-001** pour le risque de plafonner à deux routes ; charger selon décisions et preuves distinctes. F-SAV-002 ne s’étend pas automatiquement à TYPE : « une ou deux voix » est explicitement adaptable. |

### Contrôle outillé ciblé et portée

Sur B01, les deux appels de lecture de route échouent (« locator inconnu »), et le validateur de carte de lecture annonce néanmoins `READING MAP VALIDATION PASSED`. Le schéma JSON de `RUN_CARD` contient `proof.observed`, `proof.not_verified` et `proof.provenance` ; il ne contient pas de champs typographiques spécialisés portant les noms de la partition ni les cinq catégories TYPE. Ce contrôle **caractérise la projection**, pas l’absence de toute trace externe. Les essais négatifs de transport de contrats structurés et d’observation précoce sont déjà consignés dans `Audit_ACTION_Phase2_08_Structured_Proof_Contracts.md` ; ils ne sont pas répétés pour simplement produire un nouvel échec identique.

### Protections positives à préserver

1. La sélection typographique sert langues, données, hiérarchie, licence, performance et contenu réel ; une famille courante peut être la bonne.
2. Les voix expressives sont une heuristique adaptable, non un nombre autorisé de polices.
3. Le variable font n’autorise que les axes réellement présents ; zoom, locale, fallback et espacement utilisateur sont des conditions de qualité.
4. Forme des signes, lecture contextuelle, hiérarchie, personnalité et réussite de la tâche ne deviennent pas la même preuve par le seul mot « lisible ».
5. Un test perceptuel ou de marque reste une appréciation située ; U dominant demande une observation adaptée de la tâche.
6. L’existant peut être conservé avec raison, sans charge de comparaison artificielle, tandis qu’un changement de langue ou de données peut réactiver la preuve.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Obligation TYPE, heuristique locale, cinq preuves, quatre familles de test et renvois |
| B — sémantique | FULL | Lignes 379–411, déclencheur, choix, axes variables, preuve, limite, frontière ACTION |
| C — usage réel | TARGETED | Sept scénarios designer, intégrateur, reviewer, produit, agent, mainteneur |
| D — résistance | TARGETED | Six interfaces rattachées aux constats existants ; aucun nouveau constat |
| Machine | TARGETED | Deux routes refusées, carte dérivée verte, absence de champs dédiés constatée ; tests de transport antérieurs réutilisés |
| Externe | N/A-JUSTIFIED | Aucun nom de police, licence particulière, support de navigateur ou seuil chiffré n’est tranché dans ce bloc |

Bloc 5 terminé **sans nouvel ID**, sans patch ni verdict global. La prochaine unité est **SAVOIR.md, lignes 415–470** : `SAVOIR/STATE`, jugement visuel situé, états pertinents et frontière entre Gate A, Gate C et tâche utilisateur. `SAVOIR/SOURCE` commence à 471. Repartir du §12, de la baseline, du présent rapport et des constats transportés.
