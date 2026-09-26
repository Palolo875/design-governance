# Audit ACTION — Phase 2, bloc 10 — Gate B, jugement contextualisé et risques

## Périmètre examiné

- Source propriétaire : `V1/official/ACTION.md`
- Lignes : 690–773
- Sections :
  - `ACTION/GATE-B` ;
  - comparaison relationnelle B1 ;
  - discrimination sur capture B1b et atelier d’édition ;
  - écart narratif accepté ;
  - familles de preuve B2 ;
  - regard externe B3 ;
  - corrections ancrées B4 ;
  - trace d’assets B5 ;
  - format de sortie compact B6.
- Interfaces relues : `ACTION/PIPELINE-DIRECTION`, `ACTION/RUN-DIRECTION`, `ACTION/RUN_CARD`, `ACTION/CLOSE-PACKAGE`, `ACTION/VISUAL_PROOF`, `ACTION/GATE-C`, `DIRECTION/DOUBLE-LOOP`, `DIRECTION/VISUAL_TARGET`, `SAVOIR/CRAFT`, `BIBLIOTHEQUE` sur le one-shot et la paire B1b, READING_MAP, schéma et validateur `RUN_CARD`.
- Limite : lecture de phase 2, sans verdict global et sans patch.

## Baseline et continuité

| Élément | Valeur vérifiée |
|---|---|
| Audit | `DG-AUDIT-001` |
| Baseline | `B01` |
| Hash système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé | ACTION bloc 9, lignes 604–688 |
| Constats ACTION transportés | F-ACT-001 à F-ACT-035 |
| Patches autorisés | Aucun |

Les empreintes correspondent à B01. Le plan maître, le rapport du bloc 9, le checkpoint DIRECTION, les quatre passages de la phase 2 et les propriétaires voisins ont été rouverts. La source et le protocole n’ont pas changé.

La suite officielle a été exécutée deux fois. Le premier lancement a terminé sur :

```text
REPRODUCIBILITY FAILED — les archives diffèrent entre deux builds
```

Sans modification du corpus, le lancement immédiatement suivant a terminé sur :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

L’échec isolé est conservé comme observation de test ; il ne suffit pas à attribuer un défaut à Gate B. Il devra être reproduit et caractérisé lors de l’audit des builds. Le PASS final confirme l’intégrité de la baseline selon les contrôles actuels, pas l’exécution des contrats de Gate B.

## Résumé du bloc

Gate B possède une philosophie forte : comparer des relations et non des styles isolés, adapter la preuve au risque, interdire la moyenne décorative, distinguer auto-comparaison et contrepoint externe, corriger un écart observable et arrêter sans quota d’itérations. B1b est particulièrement concret : une décision principale, une édition réversible, deux captures réelles, une variable perceptible et une décision confirmée, modifiée ou abandonnée. Le maintien de l’original est reconnu comme résultat valide, ce qui protège la comparaison contre l’obligation de préférer artificiellement la variante.

Deux défauts nouveaux sont isolés. Premièrement, le contrôle B1b est déclaré matériellement obligatoire dans son scope, mais aucun champ ne représente son déclencheur, sa paire, sa décision, sa variable, son effet ou son résultat ; une DIRECTION avec risque craft dominant se clôt en `ACCEPTED` sans paire, tandis qu’un objet B1b complet est rejeté. Deuxièmement, B3 demande de documenter une revue « indépendante » sans définir le critère d’indépendance ni conserver relation, conflit d’intérêts, identité ou auteur du rendu ; une auto-revue du même auteur peut donc se déclarer indépendante dans les chaînes libres. La taxonomie d’exposition ajoute une fragilité : code, prompt et mapping peuvent être exposés simultanément, mais la liste est présentée comme un choix unique.

Le bloc réactive aussi une contradiction déjà connue : la branche one-shot autorise la clôture après la première observation lorsqu’aucun gain utile n’est probable, tandis que B1b impose une édition et une seconde capture dès que son déclencheur est actif et refuse précisément l’argument « cela ne changerait rien ». La non-applicabilité ne couvre pas le cas d’une décision éditable déjà satisfaisante. F-DIR-009 n’est donc plus localisé au seul Creative Boot.

Les autres écarts confirment des constats existants : statut d’écart narratif sans paquet transportable, revue absente sans conséquence contrôlée, paire périmée encore acceptable, droits d’asset sans effet sur le verdict, axes V/U/A/T et familles de preuve dans une trace libre, et promesse B6 de conserver paires/logs/preuves/diffs dans une `RUN_CARD` qui refuse leurs objets structurés.

## Passage A — architecture visible

### Séquence de Gate B

Le bloc suit une chaîne de décision cohérente :

1. comparer build et ancre sur les axes réellement concernés ;
2. déclencher B1b lorsque le risque craft ou la base du verdict V le demande ;
3. éditer une décision principale et comparer deux captures ;
4. mapper la différence vers correction, écart assumé ou non-transfert ;
5. choisir la famille de preuve selon V, U, A/T ou gouvernance ;
6. ajouter un contrepoint externe selon le risque ;
7. corriger ou retourner au bon niveau ;
8. conserver la trace d’asset et le statut de direction ;
9. livrer artefact puis verdict compact.

Cette architecture relie jugement créatif, risque produit et gouvernance sans les réduire à une note. Elle est plus utile qu’une grille esthétique générique.

### Répartition des sous-contrats

| Sous-contrat | Décision portée | Sortie attendue |
|---|---|---|
| B1 | Build ou ancre résout mieux la relation concernée | Correction, écart assumé ou non-transfert |
| B1b | Une décision perceptuelle résiste-t-elle à une variante réelle ? | Paire, changement, effet et décision confirmée/modifiée/abandonnée |
| Écart narratif | La divergence entre thèse et récit peut-elle être assumée ? | Statut de direction, réserve et condition de sortie |
| B2 | Quelle famille de preuve répond au risque ? | Observation factuelle par axe |
| B3 | Quel contrepoint réduit l’auto-préférence ? | Revue située avec exposition et limite |
| B4 | Où retourner lorsque l’écart persiste ? | Divergence, ancre, spec, build ou reclassification |
| B5 | L’asset directeur tient-il dans le rendu réel ? | Route, droits, traitement, observation et écart |
| B6 | Comment rendre la sortie lisible sans duplication ? | Artefact d’abord, verdict proportionné au mode |

La répartition est lisible, mais l’autorité persistante est ambiguë. B6 dit que paires, logs, preuves et diffs vivent dans un artefact associé **ou la `RUN_CARD`**. Or cette dernière ne possède aucun objet B1b, revue, écart narratif, résultat d’axe ou asset directeur. La trace associée est donc la seule destination réellement capable de conserver le contrat complet, sauf condensation en chaînes libres.

### Résolution des routes

| Locator | Résultat |
|---|---|
| `ACTION/GATE-B` | Échec — locator inconnu |
| `ACTION/GATE-C` | Échec — locator inconnu |
| `ACTION/RUN-DIRECTION` | Résolu |
| `DIRECTION/DOUBLE-LOOP` | Résolu |
| `DIRECTION/VISUAL_TARGET` | Résolu |
| `SAVOIR/CRAFT` | Résolu |

La route d’exécution DIRECTION et les propriétaires de direction/craft sont accessibles, mais les deux gates nommés par cette route ne le sont pas directement. Cela renforce F-ACT-001 et F-DIR-028.

## Passage B — contrat sémantique

### B1 compare des relations, pas une proximité décorative

La comparaison est correctement conditionnelle : obligatoire face à l’ancre utile en DIRECTION, seulement justifiée en STANDARD. Les questions portent action critique, rythme, intention et singularité. Une différence dominante reçoit une conséquence ; aucune quantité fixe de comparaisons ne constitue un PASS.

Cette règle protège contre deux erreurs : copier une référence sur des axes sans rapport et accumuler des variantes sans apprendre. Elle doit être préservée.

### Déclencheur et preuve B1b

B1b s’active lorsque :

- le risque V/craft est dominant ; ou
- le verdict V dépend d’une intention, composition, matière ou traitement non confronté à une variante.

Le déclencheur repose sur le risque et la décision déclarés. Une affirmation d’inutilité ne le désactive pas. Une fois activé, le minimum est matériel : capture initiale, édition réversible d’une décision principale, seconde capture et variable observable.

Le schéma ne possède cependant ni axe dominant, ni risque V/craft, ni état « confronté à une variante », ni objet de paire. Le validateur ne peut donc déterminer si B1b s’applique. Une carte dont la décision dit explicitement « risque V/craft dominant », dont la preuve reconnaît l’absence de variante et dont la limitation reconnaît B1b non exécuté obtient malgré tout `ACCEPTED`.

Inversement, l’ajout d’un objet structuré avec déclencheur, décision, variable, captures versionnées, type d’édition, effet, résultat, owner et prochaine preuve est rejeté comme champ inconnu. Ce double comportement fonde F-ACT-036.

### Atelier d’édition

L’atelier possède de bonnes contraintes : lecture sans rationale, décision principale nommée, retrait/réduction/transformation, absence d’ajout compensatoire et comparaison de l’effet. Une seule décision peut coordonner plusieurs diffs ; le nombre de fichiers modifiés n’est pas assimilé au nombre de décisions.

Le résultat est symétrique : garder l’original n’est ni un échec ni une itération perdue. Cette symétrie rend l’exercice réellement discriminant.

### Non-applicabilité, exploration et one-shot

`N/A-JUSTIFIED` est limité à deux cas : aucune décision principale éditable, ou paire équivalente encore valide après le dernier changement substantiel et couvrant la même décision. Thèse incertaine, élément producteur absent ou paire inconclusive maintiennent `EXPLORATORY`.

Cette protection est stricte, mais elle entre en collision avec trois règles propriétaires :

- `ACTION/PIPELINE-DIRECTION` permet la clôture après l’observation initiale si aucun gain utile n’est probable ;
- `DIRECTION/DOUBLE-LOOP` autorise le même arrêt ;
- `BIBLIOTHEQUE` demande de ne pas produire une seconde version décorative lorsque l’observation ne promet aucun gain.

Si une décision reste techniquement éditable, B1b n’autorise pas `N/A-JUSTIFIED`, même lorsque le premier rendu tient et qu’une variante serait rituelle. Le producteur doit donc soit violer B1b, soit violer l’anti-rituel. F-DIR-009 doit être élargi à cette occurrence ACTION ; une correction future devra distinguer preuve comparative nécessaire et itération décorative sans affaiblir le contrôle craft.

### Écart narratif accepté

Le mapping principal est bon : ne pas créer une nouvelle `ISSUE`, employer `HELD-WITH-ACCEPTED-DIFFERENCE`, et seulement si la clôture le permet `ACCEPTED-WITH-RESERVATION`. La trace doit rendre la différence explicite, assumée, compatible avec U/A/T et révisable.

Deux détails restent problématiques :

1. la phrase suivante appelle « cette issue » ce qui vient précisément d’être exclu du registre `ISSUE` ;
2. le statut et le verdict sont contrôlables, mais `REASON`, `PRODUCT-OR-PUBLIC-CONSTRAINT`, `OWNER` et `EXIT-CONDITION` ne le sont pas.

Une carte portant le bon statut, le bon verdict, une limitation « écart narratif accepté » et une prochaine preuve générique passe sans raison, contrainte ni condition de sortie. L’objet complet est rejeté. Cela renforce F-ACT-003, F-ACT-023 et F-ACT-027.

### B2 adapte la preuve au risque

La matrice sépare correctement :

- caractère/perception vers V ;
- compréhension/produit vers U ;
- système/robustesse vers A/T ;
- gouvernance vers réserve ou prochaine action.

Le rappel qu’une direction visuellement tenue peut répondre au mauvais problème est essentiel. Il empêche V de compenser U. La note sur cinq reste tolérée comme locator de risque, jamais comme moyenne ou substitut à une observation factuelle.

Le transport reste incomplet : `RUN_CARD` ne possède pas de résultats V/U/A/T structurés, de source d’hypothèse, de confiance ou de coût d’erreur. Ces éléments peuvent vivre dans `proof`, `risk`, `limitations` ou la trace, mais aucun mapping canonique ne relie la famille, l’axe, l’observation et la conséquence. F-ACT-002, F-ACT-005 et F-ACT-012 restent ouverts.

### B3 distingue contrepoint et indépendance

B3 formule plusieurs protections justes : un regard externe est situé, non parfaitement neutre ; l’auto-comparaison du même auteur n’est ni externe, ni indépendante, ni aveugle ; plusieurs évaluateurs ou méthodes peuvent être nécessaires ; l’absence doit devenir réserve ou prochaine preuve.

La qualification d’« indépendance » n’est toutefois pas définie. La trace exigée contient rôle, artefacts, exposition, timing du mapping et limite, mais pas :

- identité ou identifiant du reviewer ;
- relation avec l’auteur, l’équipe ou la décision ;
- conflit d’intérêts ou intérêt dans le résultat ;
- auteur du rendu ;
- date et résultat initial distinct de l’interprétation après divulgation.

Le texte commence en outre par mettre sur le même plan « un regard humain, une seconde session ou un autre évaluateur ». Une seconde session du même auteur peut réduire un biais de récence, mais ne crée pas une indépendance. Un producteur peut pourtant déclarer `available = revue indépendante`, `basis = même auteur, seconde session`, observer une revue favorable et obtenir `ACCEPTED`.

Enfin, `REVIEW-EXPOSURE` est présenté comme une valeur parmi `BLIND`, `CODE-EXPOSED`, `PROMPT-EXPOSED`, `MAPPING-EXPOSED` et `NOT-BLIND`. Code, prompt et mapping peuvent être exposés ensemble ; `NOT-BLIND` est un résumé, pas une exposition exclusive. Un objet structuré acceptant plusieurs expositions est rejeté. F-ACT-037 porte cette faiblesse sans supposer qu’une revue indépendante parfaite soit possible.

### B4 corrige au bon niveau

La correction répond à un écart observable et remonte à divergence, ancre, spec ou build selon la cause. Une correction locale qui dénature le produit force un retour plus haut. Le stop ne dépend d’aucun quota : direction tenue, écart assumé, preuve impossible mais statuée ou reclassification.

Ce contrat est cohérent avec la double boucle. La formule « preuve impossible et statuée » ne signifie pas acceptation automatique ; le statut approprié peut rester non accepté, exploratoire ou réservé selon le risque.

### B5 juge l’asset dans son intégration réelle

La trace DIRECTION conserve capacités, références, attributs, direction, écarts, réserves et statut. Pour un asset directeur, elle ajoute route, raison, droit ou incertitude, traitement et observation du rendu réel.

La distinction entre disponibilité technique et réussite de direction est excellente : un crop faible, un asset hors récit ou seulement joli reste un écart. En revanche, le droit incertain n’a toujours aucune conséquence obligatoire sur le verdict. Un objet `director_asset` structuré est rejeté ; une mention libre de droit inconnu peut accompagner `ACCEPTED`. Cela renforce F-ACT-024 et F-ACT-028.

### B6 compacte sans dupliquer

L’ordre artefact puis verdict est adapté à un système de production. Le volume varie correctement avec LITE, ITER/STANDARD et DIRECTION. La règle de non-duplication est saine si la structure ou l’artefact reste réellement accessible.

Le choix « artefact associé ou `RUN_CARD` » doit cependant être rendu déterministe par famille. Sans mapping, une équipe peut omettre la paire du rapport parce qu’elle la croit dans la carte, tandis que la carte ne peut pas la contenir. Le format compact devient alors perte de preuve plutôt que compression.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

```text
Exécution 1 : REPRODUCIBILITY FAILED — les archives diffèrent entre deux builds
Exécution 2 : FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

### Contrôle 1 — routes

```text
ACTION/GATE-B          FAIL
ACTION/GATE-C          FAIL
ACTION/RUN-DIRECTION   PASS
DIRECTION/DOUBLE-LOOP  PASS
DIRECTION/VISUAL_TARGET PASS
SAVOIR/CRAFT           PASS
```

### Contrôle 2 — B1b déclenché mais absent

```text
decision = risque V/craft dominant
observed = première capture jugée satisfaisante
not_verified = aucune variante ni seconde capture
decision_change = N/A-JUSTIFIED car aucun gain attendu,
                  bien que la décision soit éditable
verdict = ACCEPTED
Résultat : ACCEPTED
```

### Contrôle 3 — paquet B1b structuré

```text
Ajout b1b {trigger, decision, variable,
initial_capture, edited_capture, edit, effect,
outcome, owner, next_proof}
Résultat : REJECTED — champ inconnu
```

### Contrôle 4 — décision identitaire sans revue indépendante

```text
decision = décision identitaire exigeant un contrepoint externe
available = auteur + seconde session
unavailable = regard externe indépendant
proof = auto-comparaison par l’auteur
verdict = ACCEPTED
Résultat : ACCEPTED
```

### Contrôle 5 — qualification de la revue

```text
Ajout external_review {reviewer_role, relationship,
conflict_of_interest, artifacts_reviewed,
review_exposure=[CODE-EXPOSED, PROMPT-EXPOSED],
mapping_timing, limit, result}
Résultat : REJECTED — champ inconnu

available = revue indépendante
basis = même auteur, seconde session
observed = revue indépendante favorable
Résultat : ACCEPTED
```

### Contrôle 6 — écart narratif

```text
direction_status = HELD-WITH-ACCEPTED-DIFFERENCE
verdict = ACCEPTED-WITH-RESERVATION
limitation = écart narratif accepté
raison, contrainte et condition de sortie absentes
Résultat : ACCEPTED

Ajout narrative_difference {reason, constraint, owner,
next_proof, exit_condition}
Résultat : REJECTED — champ inconnu
```

### Contrôle 7 — paire B1b périmée

```text
run = V3 après changement substantiel
preuve = paire B1b V1
provenance.artifact_version = V1
verdict = ACCEPTED
Résultat : ACCEPTED
```

Le validateur ne relie pas la version de preuve à la version livrée. F-ACT-022 est confirmé.

### Contrôle 8 — trace d’asset directeur

```text
Ajout director_asset {route, reason, rights,
treatment, actual_render_observation, direction_gap}
Résultat : REJECTED — champ inconnu
```

## Passage C — usages simulés

### Direction forte dès le premier rendu

Le risque craft est dominant, mais le premier rendu tient et aucune correction utile n’est probable. Le one-shot ordonne l’arrêt ; B1b impose une variante tant qu’une décision reste éditable. Le run n’a pas de sortie cohérente sans interprétation locale.

### Variante qui confirme l’original

Une réduction de masse affaiblit le foyer. La seconde capture permet de conserver l’original avec justification. B1b fonctionne ici exactement comme prévu : la procédure change la confiance dans la décision sans exiger de changer le livrable.

### Paire existante après modification substantielle

Une paire V1 concernait la même intention, puis le crop, le contenu et la densité ont changé en V3. La prose invalide la paire ; la machine accepte encore sa mention. La reprise peut donc s’appuyer sur une comparaison obsolète.

### Écart narratif assumé

La thèse promet une forte étrangeté, mais le public prioritaire nécessite une lecture plus familière. Le statut et le verdict sont adaptés si la raison, la contrainte, l’owner, la prochaine preuve et la sortie restent retrouvables. La projection valide toutefois une simple limitation générique.

### Seconde session du même auteur

La pause réduit l’effet de récence et peut améliorer l’auto-comparaison. Elle ne crée ni indépendance organisationnelle ni regard externe. Le vocabulaire actuel permet pourtant de faire glisser l’une vers l’autre.

### Revue exposée à plusieurs sources

Le reviewer voit le code, le prompt et le mapping avant son avis. La revue reste utile mais non aveugle. La valeur unique `REVIEW-EXPOSURE` ne décrit pas fidèlement ce cumul ; `NOT-BLIND` perd la nature des expositions.

### Asset disponible mais mal intégré

Le fichier est techniquement présent et ses droits sont incertains ; son crop coupe le geste directeur. B5 conclut correctement à un écart de direction, mais la projection peut encore accepter pleinement la carte en conservant ces faits dans des chaînes libres.

### Sortie compacte avec trace externe absente

Le producteur livre le lien et trois lignes de verdict, pensant que la paire vit dans `RUN_CARD`. La carte refuse l’objet B1b et le rapport compact ne le répète pas. La preuve obligatoire disparaît malgré le respect apparent de B6.

## Passage D — constats

### F-ACT-036 — B1b est matériellement obligatoire mais invisible et non opposable dans la projection

- Gravité provisoire : **Majeur provisoire**
- État : **divergence humain/machine confirmée**
- Preuve : lignes 704–716 définissent un déclencheur déterministe et une paire matérielle non omissible ; `RUN_CARD` ne représente ni risque V/craft dominant, ni confrontation à une variante, ni paire ; une carte qui reconnaît l’absence de B1b obtient `ACCEPTED`, tandis qu’un paquet B1b complet est rejeté
- Comportement observable : deux producteurs peuvent fermer la même DIRECTION, l’un avec paire traçable et l’autre avec une seule capture, tout en obtenant la même validation
- Risque : contrôle craft contourné, preuve comparative perdue, automatisation incapable de détecter l’omission, reprise impossible et confiance excessive dans `ACCEPTED`
- Facteur atténuant : `decision_change`, `proof`, `trace_locator` et l’artefact associé peuvent porter une partie de l’information ; Gate C réutilise explicitement la paire lorsqu’elle existe
- Relations : F-ACT-002, F-ACT-018, F-ACT-021, F-ACT-022, F-ACT-028 et F-DIR-039
- Propriétaires pressentis : ACTION/GATE-B pour le contrat ; ACTION/RUN_CARD pour le mapping vers carte ou trace ; validateur seulement pour les invariants choisis comme contrôlables
- Test futur : déclencheur actif/inactif × paire complète/absente/obsolète/inconclusive × décision éditable/non éditable × artefact associé présent/absent × verdict

### F-ACT-037 — l’indépendance d’une revue peut être auto-déclarée sans qualification suffisante

- Gravité provisoire : **Significatif provisoire**
- État : **ambiguïté sémantique et contournement machine confirmés**
- Preuve : lignes 737–753 distinguent auto-comparaison et regard indépendant, mais la trace requise n’établit ni relation avec l’auteur, ni conflit d’intérêts, ni auteur du rendu ; une seconde session du même auteur déclarée comme base d’une « revue indépendante » accompagne `ACCEPTED`
- Comportement observable : une auto-revue différée, un collègue directement impliqué ou un auteur exposé au mapping peut recevoir le label indépendant sans critère commun ; les expositions multiples sont condensées en une valeur unique
- Risque : surpondération d’un avis non indépendant, validation identitaire circulaire, disparition des biais connus et triangulation omise
- Facteur atténuant : le texte dit qu’aucun regard n’est parfaitement indépendant, exige de déclarer exposition et limite, et recommande une triangulation proportionnée au risque
- Relations : F-ACT-018, F-ACT-026, F-ACT-028 et F-DIR-017
- Propriétaires pressentis : ACTION/GATE-B/B3 pour la qualification ; trace de revue pour identité, relation, exposition, résultat et limite ; schéma seulement si la claim d’indépendance doit devenir contrôlable
- Test futur : même auteur/autre auteur/collaborateur/décideur externe × relation et conflit déclarés/absents × exposition simple/multiple × avis initial/interprétation post-mapping × claim externe/indépendante/aveugle

## Mises à jour des constats antérieurs

### F-DIR-009 — modification artificielle dans un one-shot valide

Le constat n’est plus strictement localisé au Creative Boot. B1b impose une édition et une seconde capture lorsque son déclencheur est actif, même si l’observation initiale montre qu’aucun gain utile n’est probable. Sa non-applicabilité ne couvre pas une décision éditable déjà satisfaisante. ACTION, DIRECTION et BIBLIOTHEQUE donnent donc deux ordres incompatibles.

### F-ACT-001 et F-DIR-028 — routes

`ACTION/GATE-B` et `ACTION/GATE-C` sont rejetés par le lecteur alors que `ACTION/RUN-DIRECTION` les appelle. Les routes DIRECTION et SAVOIR voisines se résolvent. La lacune est dans la couverture des locators ACTION, pas dans l’absence des sections.

### F-ACT-002, F-ACT-021, F-ACT-028 et F-DIR-039 — transport des paquets

B1b, regard externe, familles de preuve, écart narratif et asset directeur décrivent des paquets détaillés. Le schéma fermé les refuse ; B6 affirme pourtant qu’ils peuvent vivre dans `RUN_CARD`. La trace externe reste une destination légitime, mais son mapping et sa résolution doivent être explicites avant de compacter la prose.

### F-ACT-003, F-ACT-010 et F-ACT-027 — registres

L’écart narratif est correctement mappé vers `direction_status` et verdict réservé, mais la phrase « cette issue » brouille l’interdiction de créer une nouvelle `ISSUE`. Les sorties locales correction, non-transfert, réserve et prochaine action nécessitent encore un mapping de registre.

### F-ACT-005 et F-ACT-012 — axes et blocage

B2 confirme qu’une réussite V ne compense pas un problème U, A ou T et qu’aucune moyenne n’est permise. La projection ne transporte pas les axes ni leur caractère bloquant ; une observation V peut donc soutenir un verdict accepté pendant que le mauvais problème produit reste seulement décrit dans une chaîne libre.

### F-ACT-018 — capacité et claim

Une décision identitaire exigeant explicitement un contrepoint externe obtient `ACCEPTED` alors que `capability_profile.unavailable` déclare ce regard indisponible. Une auto-revue du même auteur peut aussi se présenter comme indépendante. La contradiction capacité/claim est renforcée.

### F-ACT-022 — fraîcheur

B1b exige qu’une paire équivalente reste valide après le dernier changement substantiel. Une preuve V1 peut néanmoins fermer un run V3 après changement déclaré, car la version de provenance n’est pas comparée à la version du run ou de l’artefact.

### F-ACT-023 — réserves

L’écart narratif et l’absence de regard externe exigent owner, prochaine preuve et condition de sortie. `closure.limitations` reste une liste de chaînes sans cycle de vie. Une limitation générique suffit à la validation.

### F-ACT-024 — droits

B5 rend le droit ou son incertitude visible et juge correctement l’intégration réelle. Il ne fixe pas la conséquence d’un droit inconnu sur diffusion et verdict ; la projection ne le contrôle toujours pas.

### F-ACT-026 — autorité et contrepoint

B3 confirme qu’un contrepoint externe est une preuve située et non une autorisation. Ce point atténue la confusion, mais la relation reviewer/décideur/owner n’est pas transportée. Une revue ne doit toujours pas compenser un checkpoint d’autorité absent.

## Éléments conformes à préserver

1. Gate B compare, observe et explique au lieu de produire une moyenne.
2. L’ancre n’est utilisée que sur des axes réellement concernés.
3. Action critique, rythme, intention et singularité orientent la comparaison.
4. Une différence dominante reçoit une conséquence explicite.
5. Aucun nombre fixe de comparaisons ou d’itérations ne constitue une qualité.
6. B1b s’appuie sur des captures réelles et une décision principale.
7. La variable de comparaison doit être observable.
8. L’édition reste réversible et procède par retrait, réduction ou transformation.
9. Une décision peut coordonner plusieurs diffs sans devenir un quota de changements.
10. Aucun ajout compensatoire ne masque l’effet de l’édition.
11. La trace nomme changement, direction, effet et résultat décisionnel.
12. Conserver l’original est un résultat valide lorsque la variante l’a réellement mis à l’épreuve.
13. Une paire inconclusive ne produit pas un PASS indirect.
14. B1b n’est ni un score esthétique ni un absolu universel.
15. Un écart narratif accepté reste explicite, assumé, compatible avec U/A/T et révisable.
16. Une preuve manquante n’est pas convertie en acceptation par une différence assumée.
17. Une auto-comparaison ne devient pas une revue indépendante.
18. La preuve de contexte complète la preuve visuelle lorsque le risque produit domine.
19. Une direction visuellement tenue peut encore répondre au mauvais problème.
20. Les familles de preuve restent alignées sur V, U, A/T et gouvernance.
21. Toute note locale exige une observation et ne remplace pas les axes.
22. Le regard externe reste situé et non exhaustif.
23. L’absence de regard externe est déclarée, jamais transformée en validation implicite.
24. Une revue non aveugle reste utile si son exposition et sa limite sont déclarées.
25. Une divulgation après l’avis ne réécrit pas le jugement initial.
26. La correction retourne au niveau réel de la cause.
27. Une correction locale qui dénature le produit force un retour plus haut.
28. L’arrêt peut suivre une direction tenue, un écart assumé, une preuve statuée ou une reclassification.
29. Un asset est jugé dans son crop, son récit et son intégration réels.
30. La disponibilité technique d’un asset ne prouve pas sa réussite de direction.
31. L’artefact précède le verdict dans la livraison.
32. Le volume de sortie reste proportionné au mode.
33. Les valeurs structurées ne sont pas répétées inutilement en prose.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Séquence, sept sous-contrats, destinations de trace et routes examinés |
| B — Contrats | FULL | Déclencheur, paire, édition, N/A, one-shot, axes, revue, correction, asset et sortie analysés phrase par phrase |
| C — Usage | TARGETED | Huit scénarios de one-shot, variante, fraîcheur, écart, revue, exposition, asset et compression simulés |
| D — Résistance | FULL | Deux nouveaux constats et treize familles antérieures consolidés |
| Contrôles machine | FULL ciblé | Routes, B1b, revue, indépendance, écart narratif, fraîcheur, asset et suite officielle testés |
| Vérification externe | N/A-JUSTIFIED | Aucun fait externe nécessaire pour ce bloc interne |

## Point de passage

Le bloc 10 d’ACTION est entièrement lu. Gate B est conceptuellement l’un des blocs les plus solides du système : il privilégie relations, risque, preuve située, comparaison réelle et arrêt sans quota. Ses principales faiblesses sont de raccord : le contrôle matériel B1b n’est ni représentable ni opposable, l’indépendance d’une revue reste auto-qualifiable, et la branche one-shot reçoit deux ordres incompatibles. Aucun patch n’est autorisé à ce stade.

La prochaine unité est `ACTION.md`, lignes 775–868 : `ACTION/GATE-C`, `ACTION/ANTI-SLOP`, `ACTION/OVERRIDE` et `ACTION/POLICIES`. Elle devra vérifier le scope du jugement craft, la réutilisation de B1b, les critères C1–C6, le mapping motivation/construction, `FAIL-ASSUMED`, péremption, contraste, ressources techniques, baseline d’états et conséquences de gate.
