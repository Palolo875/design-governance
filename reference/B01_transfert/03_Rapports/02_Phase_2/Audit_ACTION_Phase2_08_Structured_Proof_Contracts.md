# Audit ACTION — Phase 2, bloc 8 — Contrats de preuve structurée avant build

## Périmètre examiné

- Source propriétaire : `V1/official/ACTION.md`
- Lignes : 527–602
- Sections :
  - `ACTION/STRUCTURED-PROOF` ;
  - carte de hiérarchie ;
  - preuve U attendue ;
  - partition typographique ;
  - fiche d’asset directeur ;
  - contrat de composant et baseline ;
  - contrat de motion ou scène spatiale.
- Interfaces relues : `ACTION/RUN_CARD`, `ACTION/UI-UX-REALITY`, `ACTION/RUN-DIRECTION`, `ACTION/RUN-SYSTEM`, `ACTION/VISUAL_PROOF`, `ACTION/GATE-A`, `SAVOIR/DECISION`, `SAVOIR/TYPE`, `SAVOIR/STATE`, `SAVOIR/MOTION`, `BIBLIOTHEQUE/COMPONENTS`, READING_MAP, ORCHESTRATION_MAP, schémas et validateurs `RUN_CARD` et `production_contracts`.
- Limite : lecture de phase 2, sans verdict global et sans patch.

## Baseline et continuité

| Élément | Valeur vérifiée |
|---|---|
| Audit | `DG-AUDIT-001` |
| Baseline | `B01` |
| Hash système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé | ACTION bloc 7, lignes 443–525 |
| Constats ACTION transportés | F-ACT-001 à F-ACT-028 |
| Patches autorisés | Aucun |

Les empreintes correspondent à B01. Le plan maître, le rapport du bloc 7, les quatre passages de la phase 2 du protocole et les interfaces propriétaires ont été rouverts. La source et le protocole n’ont pas changé.

La suite officielle a été réexécutée :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

Ce PASS confirme l’intégrité de la baseline. Il ne démontre pas que les contrats de ce bloc sont transportés ni que leurs conséquences sont appliquées.

## Résumé du bloc

Le bloc définit un ensemble de garde-fous pré-build particulièrement utile. Il relie la hiérarchie à une tâche et à un risque de mauvaise lecture ; distingue inspection experte et test d’utilisabilité ; conditionne la partition typographique à une décision réelle ; sépare provenance et droit d’usage ; refuse qu’une différence visuelle soit automatiquement une régression ; et exige qu’une motion possède une fonction, un fallback et une contre-indication.

Son point faible n’est pas l’intention, mais l’opérabilité. Le déclenchement commun « lorsque le mode ou le risque les déclenche » n’est pas résolu artefact par artefact. Le titre « contrats avant build » contient ensuite des champs de plan, d’observation et de résultat sans phase explicite. Enfin, ni la `RUN_CARD` ni `production_contracts` n’acceptent ces objets structurés. Un système automatique peut donc accepter une preuve U sans participant, des droits inconnus avant diffusion, une régression sans baseline identifiée ou une claim de motion sans runtime, alors que la prose l’interdit.

Quatre nouveaux constats sont ouverts : déclenchement non opérationnalisé, confusion temporelle plan/résultat, baseline non identifiable et partition typographique incomplète par rapport à son propriétaire SAVOIR. Les défauts de transport, capacité, droits et routes déjà enregistrés sont renforcés plutôt que dupliqués.

## Passage A — architecture visible

### Un conteneur, six contrats

`ACTION/STRUCTURED-PROOF` regroupe six familles :

| Artefact | Décision protégée | Déclencheur local explicite |
|---|---|---|
| Carte de hiérarchie | Priorité, tâche, contenu, action et mauvaise lecture | Aucun déclencheur propre |
| Plan de preuve U | Validité d’une claim d’utilisabilité | U dominant |
| Partition typographique | Famille, registre, langue, données et hiérarchie | Peut changer la décision |
| Fiche d’asset directeur | Production, droits, intégration et preuve de l’asset | Aucun déclencheur propre |
| Contrat de composant/baseline | Réemploi, composant critique et régression | Nouveau pattern réutilisable ou composant critique |
| Contrat de motion/scène | Usage, accessibilité, fallback et performance | Motion non triviale, animation interactive ou scène 3D |

La condition commune « seulement lorsque le mode ou le risque les déclenche » est proportionnée en principe. Elle ne précise cependant pas quel mode active quelle famille, comment le risque est résolu vers l’artefact, ni comment une omission est justifiée. Les contrats U, typographie, composant et motion possèdent une règle locale ; la carte de hiérarchie et la fiche d’asset restent suspendues à une inférence.

### Position temporelle

Le titre annonce des contrats **avant build**, puis les sous-sections utilisent trois temporalités :

| Temporalité | Exemples |
|---|---|
| Cible ou intention | signal visuel prévu, preuve U attendue, rôle d’asset, poids cible, fallback prévu |
| Méthode à exécuter | tâche, contexte, success criterion, observation/measure, reflow, zoom, reduced motion |
| Résultat ou artefact observé | satisfaction/retour qualitatif, baseline d’un état réel, capture de référence, preuve V/U/A/T |

La section suivante, `ACTION/VISUAL_PROOF`, commence correctement « dès qu’une première scène significative est disponible ». Aucun passage comparable ne marque ici le moment où une attente devient observation. L’architecture visible peut donc inciter à remplir un résultat avant qu’il existe ou, inversement, à considérer le plan initial comme suffisant après build.

### Résolution des routes

| Locator | Résultat |
|---|---|
| `ACTION/STRUCTURED-PROOF` | Échec — locator inconnu |
| `ACTION/UI-UX-REALITY` | Résolu |
| `ACTION/RUN-DIRECTION` | Résolu |
| `ACTION/RUN-SYSTEM` | Résolu |
| `ACTION/VISUAL_PROOF` | Échec — locator inconnu |
| `ACTION/GATE-A` | Résolu |
| `SAVOIR/TYPE` | Échec — locator inconnu |
| `SAVOIR/CRAFT` | Résolu |
| `BIBLIOTHEQUE/COMPONENTS` | Résolu |

La carte dérivée affirme que les locators non listés restent résolubles par préfixe propriétaire et titre exact. Le lecteur officiel, lui, refuse ces titres. Cette preuve renforce F-ACT-001 et F-DIR-028. Elle devient particulièrement importante ici : `SAVOIR/TYPE` détient des critères absents de la table locale.

## Passage B — contrat sémantique

### Règle de proportion

Le bloc commence par une protection saine : les artefacts rendent les décisions inspectables et ne sont obligatoires que si mode ou risque les déclenche. Cela évite de transformer six structures riches en formulaire universel.

Cette règle reste néanmoins incomplète. Le système ne fournit pas une fonction du type :

```text
trigger(mode, risk, decision, artifact) -> REQUIRED | OPTIONAL | N/A-JUSTIFIED
```

La `RUN_CARD` ne transporte pas davantage une activation par artefact. Deux comportements opposés deviennent plausibles : tout remplir par prudence, ou omettre carte/asset faute de déclencheur littéral. F-ACT-004 est donc renforcé, et F-ACT-029 isole la lacune propre à cette famille.

### Carte de hiérarchie

La carte relie neuf éléments qui comptent réellement : public prioritaire, contexte/tâche, contenu primaire, action critique, contenu secondaire, contenu à la demande, risque de mauvaise lecture, signal visuel prévu et preuve U attendue.

Sa qualité principale est de ne pas réduire la hiérarchie à des tailles ou contrastes. Elle rattache l’expression visuelle à la tâche et à une mauvaise lecture possible. Elle peut donc guider la construction avant de servir de grille de comparaison après rendu.

Deux limites demeurent :

1. elle n’a pas de déclencheur propre ;
2. elle n’a ni objet structuré accepté ni mapping déclaré vers `ui_ux_reality_pack`, `direction`, `proof` ou la trace externe.

Une simple chaîne dans `proof.observed` peut conserver le sens, mais elle ne permet pas de vérifier que contenu primaire, action critique, risque et signal restent reliés.

### Preuve U attendue

La structure `USER/PROFILE`, `TASK`, `CONTEXT`, `SUCCESS-CRITERION`, `OBSERVATION/MEASURE`, `SATISFACTION-OR-QUALITATIVE-RETURN`, `LIMIT`, `NEXT-PROOF` est substantielle. Elle oblige à définir tâche, réussite, limite et suite au lieu de produire une impression globale.

La phrase suivante pose une frontière épistémique essentielle : une capture ou inspection experte peut formuler un risque U, mais ne doit pas être appelée test d’utilisabilité sans tâche représentative exécutée avec une personne concernée. `SAVOIR` renforce cette lecture en demandant personne, tâche, contexte, échantillon et résultat observé lorsque l’utilisabilité réelle domine.

Le terme « profil concerné » pourrait être mal lu comme persona synthétique. La lecture inter-propriétaire lève l’ambiguïté : le profil décrit la personne ou population concernée ; il ne remplace pas une exécution avec un participant réel lorsque la claim est un test d’utilisabilité.

La projection ne sait pas faire respecter cette frontière. Elle accepte simultanément :

- participant et tâche représentative déclarés indisponibles ;
- méthode limitée à une inspection experte de capture ;
- observation « test d’utilisabilité réussi » ;
- verdict `ACCEPTED`.

Le contrat humain est donc bon, mais non opposable. Cela renforce F-ACT-018 plutôt que de créer un doublon.

### Partition typographique

Le déclencheur local est bien formulé : produire la partition complète seulement si famille, registre, langue, données ou hiérarchie peuvent changer la décision ; sinon conserver le système existant avec une raison. Cette règle protège contre la refonte typographique rituelle.

La table couvre cinq rôles utiles — fonctionnel, éditorial, microcopie, donnée, signature — et demande fonction, famille/registre, mesure/interligne, poids/axe, contextes, fallback et justification. La phrase finale ajoute reflow, zoom et ajustement d’espacement utilisateur.

Le propriétaire `SAVOIR/TYPE` exige cependant aussi langues, chiffres, ponctuation, graisses, lisibilité, licence, performance, chargement, fallback, ton, axes disponibles et caractères absents. Sa preuve distingue forme des caractères, lisibilité du texte, hiérarchie, personnalité et effet sur la tâche. La partition dite « complète » d’ACTION n’offre pas de champs explicites pour :

- couverture de langue, glyphes, chiffres et ponctuation ;
- licence et source de la police ;
- stratégie de chargement et performance ;
- résultat de lisibilité/résilience et limite de preuve.

Ces données peuvent être rangées en texte libre dans `Contextes` ou `Justification`, ou externalisées. Ce n’est toutefois ni explicite ni stable, et le renvoi inverse vers `SAVOIR/TYPE` manque dans le bloc. Comme ce locator échoue dans le lecteur, le risque ne peut pas être traité comme simple détail de navigation.

### Fiche d’asset directeur

La fiche est riche et correctement multidimensionnelle. Elle sépare :

- rôle dans la promesse ;
- route et statut de production ;
- médium ou absence intentionnelle ;
- raison et alternative refusée ;
- source, disponibilité et droits ;
- provenance et transformations ;
- usage, intégration et alternative textuelle ;
- comportement desktop/mobile ;
- format, poids, fallback, motion et reduced motion ;
- preuve V/U/A/T et contre-indication.

Elle corrige partiellement F-DIR-025 : l’absence intentionnelle existe bien comme choix de médium. Elle ne fait toutefois pas partie de l’enum de route ; une implémentation peut donc hésiter entre aucune route, `CODE-NATIVE`, `HYBRIDE` ou une valeur inventée. Le constat DIRECTION reste ouvert jusqu’au mapping des deux dimensions.

La distinction provenance/autorisation est excellente. Une origine connue ne vaut pas permission de réemploi. Un droit inconnu ou non autorisé doit provoquer `RETURNED`, `ESCALATED` ou le statut contextuel avant diffusion.

Cette dernière formulation réutilise cependant le mot « statut » pour des conséquences qui croisent état, issue, verdict et autorité. Le validateur accepte des droits inconnus avec `ACCEPTED`; la conséquence humaine n’est donc pas reliée aux registres canoniques. F-ACT-003, F-ACT-010 et surtout F-ACT-024 sont renforcés.

### Contrat de composant et baseline

Pour un pattern réutilisable ou composant critique, le bloc exige intention, non-usage, sémantique, clavier, focus, anatomie, slots, tokens, modes, variants, états, responsive, stories ou captures de baseline. Cette liste est cohérente avec `BIBLIOTHEQUE/COMPONENTS` et les responsabilités de `ACTION/RUN-SYSTEM`.

La définition de la baseline est solide : image versionnée d’un état réel, elle signale un écart mais ne produit pas automatiquement un PASS. La qualification de régression dépend de l’intention, du comportement attendu ou du contrat de compatibilité. Une différence intentionnelle doit être reliée à une décision et une preuve.

L’identité du comparateur n’est pourtant pas transportée. La `RUN_CARD` possède une provenance de l’artefact observé, mais aucun champ ou mapping pour le locator, la version, l’état et le contrat de compatibilité de la **baseline comparée**. Un claim « aucune régression visuelle » passe sans baseline identifiée ; un objet `baseline` structuré est rejeté.

Le problème ne signifie pas qu’une baseline doive être embarquée dans la carte. Un locator externe est suffisant si son mapping, sa version et son lien au résultat sont obligatoires. Ce lien n’est pas défini dans B01.

### Contrat de motion ou scène spatiale

La motion non triviale reçoit un contrat complet : fonction utilisateur/narrative, état initial, déclencheurs, transitions, interruptions, clavier/tactile, reduced motion, fallback statique, performance, contenu alternatif, capture de référence et contre-indication.

La règle de retrait est particulièrement utile : sans feedback, information, relation spatiale ou décision de direction, l’effet devient candidat à la suppression. Elle évite de traiter la motion comme polish autonome.

La `RUN_CARD` n’accepte pas d’objet de motion et ne relie pas une claim aux capacités runtime. Une carte déclarant runtime, performance et reduced motion indisponibles peut encore observer « motion fluide, performante et compatible reduced motion » à partir d’une capture statique, puis clôturer en `ACCEPTED`. Cela renforce F-ACT-018 et F-ACT-021.

### Transport humain et machine

| Contrat humain | Transport possible aujourd’hui | Limite observée |
|---|---|---|
| Carte de hiérarchie | Trace libre, `ui_ux_reality_pack` partiel | Relations non structurées, pack non autonome |
| Preuve U | `proof`, `evaluation_case`, trace | Participant/méthode/claim non contraints ensemble |
| Partition typographique | Trace libre | Objet rejeté, champs propriétaires incomplets |
| Fiche d’asset | `anchors`, `sources`, trace | Route, droits, absence, transformation et usage non mappés |
| Composant/baseline | `artifact`, `system_close`, trace | Baseline comparée non identifiée ni versionnée dans la projection |
| Motion/scène | `proof`, trace | Fonction, fallback, reduced motion et runtime non liés au claim |

L’externalisation vers `trace_locator` est compatible avec une projection partielle. Le défaut est l’absence de contrat de résolution : quels invariants restent dans la carte, quels objets vivent dehors, et quelles conséquences le validateur doit contrôler.

Le schéma `production_contracts` ne sert pas de solution générale. Il exige à la racine `creative_direction_set`, `ui_ux_reality_pack` et `evaluation_case` ensemble. Un pack UI/UX seul est rejeté, ce qui confirme F-ACT-006 sur l’agglomération de contrats conditionnels.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

### Contrôle 1 — routes

```text
ACTION/STRUCTURED-PROOF  FAIL
ACTION/UI-UX-REALITY     PASS
ACTION/RUN-DIRECTION     PASS
ACTION/RUN-SYSTEM        PASS
ACTION/VISUAL_PROOF      FAIL
ACTION/GATE-A            PASS
SAVOIR/TYPE              FAIL
SAVOIR/CRAFT             PASS
BIBLIOTHEQUE/COMPONENTS  PASS
```

### Contrôle 2 — transport des six objets

```text
Ajout dans RUN_CARD : hierarchy_map, user_proof_plan,
typography_partition, director_asset, component_contract, motion_contract
Résultat : REJECTED — six champs inconnus

Ajout de structured_proof à production_contracts
Résultat : REJECTED — champ inconnu
```

Le test ne conclut pas que tous ces objets doivent devenir des champs de `RUN_CARD`. Il prouve qu’aucun mapping structuré direct n’existe dans les adaptateurs actuels.

### Contrôle 3 — proportion machine

```text
Document contenant seulement ui_ux_reality_pack
Résultat : REJECTED — creative_direction_set obligatoire
```

Le contrat machine force un bundle étranger même si seul l’usage est activé.

### Contrôle 4 — plan pré-build marqué observé

```text
proof_scope = "Plan avant build : mobile et clavier à observer plus tard"
coverage_map.proof_status = observed
artifact_locator = /artefact-encore-inexistant@375px
Résultat : ACCEPTED
```

Ni l’existence de l’artefact, ni la concordance entre temporalité du scope et statut observé ne sont contrôlées.

### Contrôle 5 — test d’utilisabilité sans participant

```text
available = capture + inspection experte
unavailable = participant + tâche représentative
observed = "Test d’utilisabilité réussi"
method = inspection experte d’une capture
verdict = ACCEPTED
Résultat RUN_CARD : ACCEPTED

evaluation_case.available_capabilities = inspection experte + capture
task_results = test utilisateur réussi sans participant documenté
Résultat production_contracts : ACCEPTED
```

### Contrôle 6 — droits inconnus

```text
anchor.limit = droit inconnu et autorisation requise avant diffusion
verdict = ACCEPTED
Résultat : ACCEPTED
```

### Contrôle 7 — baseline absente

```text
mode = SYSTÈME
observed = aucune régression visuelle par rapport à la baseline
baseline locator/version/état = absents
verdict = ACCEPTED
Résultat : ACCEPTED

Ajout baseline {locator, version, state, compatibility_contract}
Résultat : REJECTED — champ inconnu
```

### Contrôle 8 — motion sans runtime

```text
available = capture statique
unavailable = runtime motion + mesure performance + reduced motion
observed = motion fluide, performante et compatible reduced motion
method = inspection d’une capture statique
verdict = ACCEPTED
Résultat : ACCEPTED
```

## Passage C — usages simulés

### Micro-delta typographique local

Une correction de wrapping conserve la famille existante et explique pourquoi. Le bloc permet correctement de ne pas produire une partition complète. La proportion est saine si le déclencheur est réellement examiné.

### Nouvelle surface multilingue

La langue peut changer la décision, donc la partition s’active. Un agent qui ne parvient pas à ouvrir `SAVOIR/TYPE` peut remplir famille, mesure, poids et fallback tout en omettant glyphes, chiffres, licence et chargement. Il croit avoir produit la partition « complète » alors que le propriétaire exige davantage.

### Inspection experte sans recrutement

L’équipe possède une capture mais aucun participant. La prose autorise une hypothèse ou un risque U, jamais un test d’utilisabilité. Les adaptateurs acceptent pourtant une claim de réussite utilisateur et un verdict plein.

### Asset curaté aux droits inconnus

La fiche conserve provenance et incertitude, puis exige retour, escalade ou statut contextuel avant diffusion. La projection permet cependant `ACCEPTED`; si l’équipe traite ce verdict comme autorisation de publier, la barrière juridique disparaît.

### Absence intentionnelle d’image

La décision est valide : aucun asset ne sert mieux la promesse. La fiche sait noter « absence intentionnelle », mais la route de production ne sait pas exprimer cette absence. Deux équipes peuvent sérialiser ce choix différemment ou inventer une sixième route.

### Composant partagé avec différence volontaire

Une modification visuelle correspond à une nouvelle intention documentée et ne constitue pas une régression. La règle humaine évite de restaurer aveuglément l’ancien rendu. Sans identité de baseline et contrat de compatibilité, l’automatisation ne peut toutefois pas déterminer quel état et quelle version étaient comparés.

### Animation évaluée sur capture statique

L’image montre l’état final, mais ne prouve ni interruption, ni clavier/tactile, ni reduced motion, ni performance. Le contrat humain exige ces axes ; le validateur accepte malgré tout une claim complète de motion.

### Effet décoratif sans fonction

La motion ne produit aucun feedback, information, relation spatiale ou choix de direction. Le bloc donne une condition de retrait claire et évite une discussion purement esthétique.

## Passage D — constats

### F-ACT-029 — l’activation des contrats structurés n’est pas résolue artefact par artefact

- Gravité provisoire : **Significatif**
- État : **règle proportionnée mais non opérationnalisée**
- Preuve : ligne 529 rend les artefacts obligatoires lorsque mode ou risque les déclenche ; la carte de hiérarchie et la fiche d’asset n’ont pas de déclencheur local, aucune matrice d’activation ni sortie `N/A-JUSTIFIED` par artefact n’est définie
- Comportement observable : une équipe remplit les six structures à chaque run ; une autre omet carte ou asset en l’absence de trigger littéral ; les deux peuvent considérer le protocole respecté
- Risque : surcharge procédurale, omission de preuve déterminante, faux sentiment de complétude et divergence entre équipes
- Facteur atténuant : quatre familles possèdent un déclencheur local pertinent ; START et READING_MAP contiennent déjà une logique générale de risque et de contribution utile
- Relations : F-ACT-004, F-ACT-006, F-ACT-007 et F-DIR-038
- Propriétaires pressentis : ACTION/STRUCTURED-PROOF pour la condition par artefact ; DIRECTION/START et READING_MAP seulement pour l’activation générale ; projection pour le transport choisi
- Test futur : cinq modes, risques U/A/T/V, asset absent/présent, composant neuf/existant, motion triviale/non triviale, et justification d’omission

### F-ACT-030 — le bloc « avant build » mélange attente, méthode exécutée et résultat observé

- Gravité provisoire : **Significatif**
- État : **ambiguïté temporelle confirmée et contournement machine reproduit**
- Preuve : le titre annonce des contrats avant build, tandis que `OBSERVATION/MEASURE`, retour qualitatif, vérification de reflow, baseline d’un état réel, preuve V/U/A/T et capture de référence supposent une exécution ou un artefact ; un plan portant `proof_status=observed` sur un artefact inexistant est accepté
- Comportement observable : un producteur préremplit une observation attendue comme résultat, ou conserve après build une cible non remplacée par l’observation réelle
- Risque : preuve circulaire, statut `observed` prématuré, décision clôturée sur une intention et confusion entre cible, méthode, résultat et prochaine preuve
- Facteur atténuant : `ACTION/VISUAL_PROOF` et `ACTION/GATE-A` séparent mieux portée préalable et observation ; la trace externe peut versionner plan et exécution
- Relations : F-ACT-005, F-ACT-007, F-ACT-013, F-ACT-018, F-ACT-022 et F-DIR-003
- Propriétaires pressentis : ACTION/STRUCTURED-PROOF pour les phases du contrat ; ACTION/VISUAL_PROOF et gates pour l’exécution ; schéma/validateur pour l’invariant choisi
- Test futur : PRE-BUILD/POST-BUILD, artefact absent/présent, statut planned/observed/not-verified, re-observation après changement et version de preuve

### F-ACT-031 — une claim de non-régression n’identifie pas nécessairement sa baseline

- Gravité provisoire : **Significatif**
- État : **lacune de comparateur et de fraîcheur confirmée**
- Preuve : lignes 590–594 exigent image versionnée, intention, comportement attendu et compatibilité ; une `RUN_CARD SYSTÈME` affirme aucune régression sans locator/version/état de baseline et obtient `ACCEPTED`, tandis qu’un objet baseline structuré est rejeté
- Comportement observable : une comparaison textuelle ne permet pas de retrouver quelle image, quel état, quel viewport, quelle version ou quel contrat a servi de référence
- Risque : faux négatif de régression, restauration d’un comportement obsolète, différence volontaire supprimée ou différence accidentelle acceptée
- Facteur atténuant : la provenance de l’artefact courant existe ; stories, captures et trace externe peuvent héberger la baseline si leur mapping devient explicite
- Relations : F-ACT-015, F-ACT-021, F-ACT-022, F-ACT-027 et F-DIR-034
- Propriétaires pressentis : BIBLIOTHEQUE/COMPONENTS pour la baseline de structure ; ACTION/RUN-SYSTEM pour la comparaison et conséquence ; trace/RUN_CARD pour locator et version
- Test futur : baseline courante/obsolète/manquante, état et viewport, diff intentionnel, compatibilité rompue, artefact modifié après verdict

### F-ACT-032 — la partition typographique dite complète ne porte pas tous les critères de son propriétaire

- Gravité provisoire : **Significatif provisoire**
- État : **contrat local incomplet et dépendance difficile à charger**
- Preuve : lignes 558–570 couvrent rôles, mesure, poids, contextes, fallback, justification, reflow et zoom ; `SAVOIR/TYPE` exige aussi langues/glyphes, chiffres, ponctuation, licence, performance/chargement, axes réels, lisibilité et limites de preuve ; aucun renvoi local ne les mappe et `SAVOIR/TYPE` échoue dans le lecteur de routes
- Comportement observable : une famille est approuvée avec une partition apparemment complète sans contrôle explicite de licence, caractères nécessaires ou coût de chargement
- Risque : texte manquant ou synthétique, fallback divergent, non-conformité de licence, régression de performance et claim de lisibilité sans preuve
- Facteur atténuant : certains éléments peuvent être consignés dans `Contextes` ou `Justification`; SAVOIR contient le contrat substantiel et les routes de démarrage peuvent le charger conditionnellement
- Relations : F-ACT-001, F-ACT-002, F-ACT-028, F-DIR-006 et F-DIR-028
- Propriétaires pressentis : SAVOIR/TYPE pour les critères ; ACTION/STRUCTURED-PROOF pour leur support de preuve ou mapping ; READING_MAP/lecteur pour la résolution
- Test futur : latin/CJK/RTL, chiffres tabulaires, glyphes absents, licence inconnue, webfont lente, variable font, zoom/reflow et fallback réel

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — routes

`ACTION/STRUCTURED-PROOF`, `ACTION/VISUAL_PROOF` et `SAVOIR/TYPE` sont présents mais refusés par le lecteur officiel. Les routes RUN-DIRECTION, RUN-SYSTEM, UI-UX-REALITY, GATE-A, SAVOIR/CRAFT et BIBLIOTHEQUE/COMPONENTS passent. Le défaut reste une carte fermée incomplète, désormais avec impact direct sur la preuve typographique et la frontière plan/exécution.

### F-ACT-002 et F-ACT-028 — mapping de trace

Les six objets structurés sont rejetés par la `RUN_CARD` et par `production_contracts`. L’externalisation reste possible, mais aucune convention ne relie leurs champs essentiels au locator, à la version, au claim et à la conséquence canonique.

### F-ACT-003 et F-ACT-010 — registres

La fiche d’asset demande `RETURNED`, `ESCALATED` ou « le statut prévu par le contexte ». Cette phrase protège la diffusion, mais brouille encore issue, état, verdict et escalade. Le mapping devra empêcher qu’un `ACCEPTED` global soit pris pour une autorisation de publier.

### F-ACT-004 — déclencheur CONTEXT/TECH

Le bloc fournit de meilleurs déclencheurs locaux pour U, type, composant et motion. Il montre néanmoins que la même faiblesse s’étend aux artefacts : carte et fiche d’asset n’ont pas de résolution propre. F-ACT-029 spécialise ce défaut sans remplacer le constat transversal.

### F-ACT-005 et F-ACT-007 — scope et statut de preuve

Un plan pré-build est accepté comme couverture observée d’un artefact inexistant. `proof_scope` et `coverage_map.proof_status` ne distinguent donc pas attente, disponibilité, exécution et résultat.

### F-ACT-006 — universalisation des contrats conditionnels

`production_contracts` rejette un `ui_ux_reality_pack` autonome et exige le trio direction/UI-évaluation. Le test confirme que l’adaptateur agglomère encore des contrats que la prose active proportionnellement.

### F-ACT-008 — validateur des contrats

Les tests en mémoire exposent des lacunes sémantiques supplémentaires, mais le script officiel reste centré sur les exemples canoniques et mutations prédéfinies. Le PASS global ne couvre donc pas les scénarios de ce bloc.

### F-ACT-012, F-ACT-018 et F-ACT-021 — claim, capacité et clôture

Trois claims incompatibles avec les capacités déclarées passent : test d’utilisabilité sans participant, motion/performance/reduced-motion depuis une capture statique et non-régression sans baseline. La limite textuelle n’empêche pas `ACCEPTED`.

### F-ACT-022 — fraîcheur

La baseline versionnée introduit un second objet temporel en plus de l’artefact courant. La provenance existante ne lie pas la preuve à cette référence ; un changement de baseline ou de compatibilité après observation reste invisible.

### F-ACT-024 — droits et confidentialité

Le propriétaire humain exige enfin une conséquence avant diffusion lorsque le droit est inconnu ou absent. Le test `ACCEPTED` confirme que cette conséquence n’est pas transportée. Le constat est renforcé et devra distinguer acceptation de qualité, autorité et permission de diffuser.

### F-DIR-025 et F-DIR-026 — routes d’asset

L’absence intentionnelle est reconnue comme médium, ce qui atténue F-DIR-025, mais elle reste extérieure aux cinq routes de production. La fiche ne résout pas non plus la borne de transformation de `GÉNÉRÉ-DIRIGÉ`; F-DIR-026 reste ouvert.

## Éléments conformes à préserver

1. Les artefacts structurés sont conditionnels au mode, au risque et à la décision.
2. La hiérarchie relie public, tâche, contenu, action, risque de mauvaise lecture, signal et preuve.
3. Une inspection experte peut identifier un risque U sans devenir un test d’utilisabilité.
4. Une preuve U nomme tâche, contexte, critère de réussite, mesure, limite et prochaine preuve.
5. Une partition complète n’est pas exigée si le système existant suffit avec une raison.
6. Les rôles typographiques séparent lecture, éditorial, microcopie, données et signature limitée.
7. Reflow, zoom et espacement utilisateur font partie de la décision typographique.
8. La fiche d’asset sépare rôle, route, médium, raison, source, provenance, droits, usage et preuve.
9. L’absence intentionnelle d’asset est une décision légitime.
10. La provenance ne vaut jamais autorisation de réemploi.
11. Desktop et mobile peuvent employer crop, suppression ou alternative différents.
12. Un asset informatif reçoit une alternative adaptée ; un décoratif reçoit une justification.
13. Un composant critique documente sémantique, clavier, focus, états et responsive.
14. Une baseline est un comparateur versionné, pas un PASS.
15. Toute différence visuelle n’est pas automatiquement une régression.
16. Une différence intentionnelle reste reliée à une décision et une preuve.
17. Une motion non triviale possède fonction, interruption, accès alternatif, fallback et performance.
18. Reduced motion fait partie du contrat, pas d’un correctif terminal.
19. Une capture statique ne doit pas être confondue avec la preuve du comportement.
20. Un effet sans feedback, information, relation spatiale ou décision de direction peut être retiré.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Six familles, activation, temporalité, routes et voisinage examinés |
| B — Contrats | FULL | Chaque sous-section comparée à son owner, aux schémas et à la trace |
| C — Usage | TARGETED | Huit scénarios de proportion, utilisateur, type, asset, baseline et motion simulés |
| D — Résistance | FULL | Quatre nouveaux constats et dix-sept familles antérieures consolidés |
| Contrôles machine | FULL ciblé | Routes, transport, proportion, temporalité, U, droits, baseline et motion testés |

## Point de passage

Le bloc 8 d’ACTION est entièrement lu. Son contenu humain doit être largement préservé : il fournit des contrats utiles et des frontières épistémiques fortes. La faiblesse principale est la rupture entre ces exigences et leur activation, leur phase de vie et leur transport machine. Aucun patch n’est autorisé à ce stade.

La prochaine unité est `ACTION.md`, lignes 604–688 : `ACTION/VISUAL_PROOF` et `ACTION/GATE-A`. Elle devra vérifier la portée déclarée avant preuve, la représentativité des captures, l’adéquation méthode/claim, le mapping `COVERAGE-LIMIT`, la provenance minimale, les contrôles applicables et les conditions de `PASS`, `NOT-VERIFIED` et `N/A-JUSTIFIED`.
