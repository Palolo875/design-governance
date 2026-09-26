# Audit ACTION — Phase 2, bloc 7 — Pipeline DIRECTION, one-shot et checkpoint

## Périmètre examiné

- Source propriétaire : `V1/official/ACTION.md`
- Lignes : 443–525
- Sections :
  - `ACTION/PIPELINE-DIRECTION` ;
  - boucle de qualité et branche one-shot ;
  - positions ;
  - traduction de l’émotion ;
  - alternative située ;
  - spec visuelle ;
  - sourcing et trace ;
  - sélection contre la facilité ;
  - direction et checkpoint ;
  - vérification du rendu réel ;
  - passe créative et polish.
- Interfaces relues : `DIRECTION/DOUBLE-LOOP`, `DIRECTION/VISUAL_TARGET`, `ACTION/RUN-DIRECTION`, `ACTION/AUTHORITY`, `ACTION/RUN_CARD`, `ACTION/CLOSE-PACKAGE`, `SAVOIR/CRAFT`, READING_MAP, schéma et validateur `RUN_CARD`.
- Limite : lecture de phase 2, sans verdict global et sans patch.

## Baseline et continuité

| Élément | Valeur vérifiée |
|---|---|
| Audit | `DG-AUDIT-001` |
| Baseline | `B01` |
| Hash système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé | ACTION bloc 6, lignes 335–441 |
| Constats ACTION transportés | F-ACT-001 à F-ACT-025 |
| Patches autorisés | Aucun |

Les empreintes correspondent à B01. La phase 2 du protocole, le plan maître, le rapport ACTION bloc 6 et le checkpoint DIRECTION ont été relus. La source et le protocole n’ont pas changé.

## Résumé du bloc

Le pipeline est l’une des sections les plus fortes du corpus sur la fabrication d’une direction réelle. Il sépare correctement décision créative, exécution livrable et gate spécialisé ; rend le one-shot compatible avec une véritable observation ; refuse les quotas de variantes ; transforme les émotions en leviers visibles ; exige une spec avant build ; compare le rendu réel à cette spec ; et réserve le polish aux changements observables.

Les défauts se concentrent dans la trace et l’autorité : le checkpoint obligatoire n’a pas de transport identifiable et peut être confondu avec le regard externe compensable ; les statuts de sources, types d’ancres et routes d’assets doivent être conservés mais ne possèdent pas de mapping structuré commun ; les résultats d’écarts post-build introduisent une taxonomie locale sans registre canonique. Le bloc renforce aussi deux constats existants : preuve visuelle non représentative encore acceptable et creative close humain en quatre questions face à cinq champs machine.

## Passage A — architecture visible

### Relation entre les trois niveaux

La ligne 447 fournit une clarification d’architecture importante :

| Niveau | Responsabilité |
|---|---|
| `DIRECTION/DOUBLE-LOOP` | Décision créative et apprentissage |
| `ACTION/PIPELINE-DIRECTION` | Exécution livrable, preuve, correction et clôture |
| `ACTION/GATE-B/B1b` | Contrôle spécialisé lorsque son scope est actif |

Ces niveaux ne sont pas trois boucles concurrentes. Cette phrase atténue directement F-DIR-030 sur la propriété du jugement de craft et protège le pipeline contre trois revues parallèles.

### Séquence visible

Le pipeline expose :

1. une boucle générale de qualité ;
2. une branche one-shot ;
3. huit étapes numérotées, de la position à la comparaison post-build ;
4. une passe créative finale ;
5. une condition de retour sans nombre fixe d’itérations.

La séquence est cohérente avec l’amont : cible et spec avant build, checkpoint lorsque nécessaire, artefact réel, capture, comparaison, correction ou retour. Elle évite l’inversion ancienne où le premier objet pouvait précéder les décisions de direction.

### Résolution des routes

| Locator | Résultat |
|---|---|
| `ACTION/PIPELINE-DIRECTION` | Échec — locator inconnu |
| `DIRECTION/DOUBLE-LOOP` | Résolu |
| `DIRECTION/VISUAL_TARGET` | Résolu |
| `ACTION/RUN-DIRECTION` | Résolu |
| `ACTION/VISUAL_PROOF` | Échec — locator inconnu |
| `ACTION/GATE-B` | Échec — locator inconnu |
| `ACTION/GATE-C` | Échec — locator inconnu |
| `SAVOIR/CRAFT` | Résolu |
| `ACTION/CLOSE-PACKAGE` | Résolu |
| `ACTION/CLOSE-EXIT-CHECK` | Résolu |

Le pipeline central de la route DIRECTION et trois de ses contrôles aval restent donc introuvables par le lecteur officiel. Cette preuve renforce F-ACT-001 et F-DIR-028 ; elle ne justifie pas un nouvel ID par locator.

## Passage B — contrat sémantique

### Boucle de qualité

La séquence `préparer → construire → observer → isoler → corriger → réobserver → comparer → décider` est presque identique à `DIRECTION/DOUBLE-LOOP`. ACTION ajoute correctement la possibilité de modifier l’artefact **ou la décision**, alors que DIRECTION formule parfois la correction seulement comme modification d’artefact.

La règle la plus importante est la conséquence réelle : une correction change une relation visible, une tâche, une preuve, une contrainte ou une propriété de robustesse. Une nouvelle explication ne compte pas. Cette règle empêche le système de transformer un commentaire plus sophistiqué en itération de design.

### Branche one-shot

Le one-shot n’est ni l’absence de préparation, ni l’absence d’observation. Il permet de clôturer après l’observation initiale seulement si :

- le premier rendu atteint la qualité du mode ;
- la direction est identifiable ;
- les risques applicables sont couverts ;
- aucune amélioration utile n’est probable.

Cette formulation converge avec DIRECTION et atténue F-DIR-009 : une correction artificielle n’est pas exigée lorsque le premier objet tient déjà. Le producteur doit néanmoins conserver la preuve de l’observation et la confirmation de décision. Le schéma ne possède pas de champ `execution_branch`, mais l’absence d’un tag one-shot n’est pas en soi un défaut si le paquet de preuve permet de vérifier les conditions de sortie.

Une ambiguïté mineure demeure avec la « repasse ciblée avant clôture » de la ligne 513. La lecture la plus cohérente est qu’une repasse peut être une réinspection sans modification lorsque le défaut dominant est absent ; sinon elle contredirait le one-shot et l’arrêt du polish. Cette interprétation devra être rendue explicite lors d’une éventuelle correction, sans créer un nouveau rituel.

### Positions et absence de quota

Les positions sont demandées seulement lorsque la décision est ouverte. Les axes possibles — structure, matière, voix, temporalité, densité, rapport texte/image, rythme, émotion — restent des leviers, pas une grille à remplir.

L’absence de quota est protectrice. Une position retenue et une alternative située suffisent lorsque risque et tensions sont clairs. Si aucune alternative plausible ne peut modifier le choix, la raison est notée puis le pipeline passe à la spec. Cette règle empêche le catalogue de variantes et reste cohérente avec la condition d’arrêt de lecture.

### Traduction de l’émotion

Le bloc refuse qu’un adjectif devienne une direction autonome. « Premium », « chaleureux » ou « dynamique » doivent modifier une décision visible : composition, contraste, densité, typographie, motion, contenu, relation texte/image ou matière.

Ce contrat est utile parce qu’il transforme un langage subjectif en hypothèse observable sans prétendre que l’émotion devient mesurable par simple déclaration.

### Alternative située

L’alternative répond à un public, un JTBD, une contrainte ou une opportunité réellement différents. Elle n’est matérialisée qu’au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou rendu.

Le niveau de matérialisation est donc proportionné à l’incertitude. Le système peut comparer une décision sans payer systématiquement le coût de deux builds complets.

### Spec visuelle avant build

La spec synthétique est obligatoire avant le premier code ou rendu d’une surface DIRECTION. ACTION laisse à `DIRECTION/VISUAL_TARGET` la définition des voies d’ancrage et conserve la trace opératoire.

Le minimum annoncé par ACTION comprend type et identifiant d’ancre, cible ou hypothèse, attributs observés, retenus et rejetés, contre-indications, limites de transfert et preuve attendue. La projection `anchors[]` ne possède pourtant ni type d’ancre, ni identifiant, ni contre-indication dédiée, ni preuve attendue. Cette divergence, déjà enregistrée sous F-DIR-027, est confirmée depuis le propriétaire de la trace.

La protection `ANCHOR-GENERATED` est conceptuellement saine : à enjeu identitaire élevé, une hypothèse générée seule exige calibration réelle ou réserve explicite. La projection ne sait pas reconnaître la voie générée et ne peut donc pas appliquer cette condition.

### Sourcer et tracer

Le bloc distingue trois dimensions différentes :

| Dimension | Valeurs ou contenu |
|---|---|
| État épistémique de recherche | `VERIFIED-THIS-RUN`, `MODEL-KNOWLEDGE-NOT-RECHECKED`, `USER-SOURCED-NOT-RECHECKED` |
| Type d’ancre | `ANCHOR-GENERATED`, `ANCHOR-OBSERVED`, `ANCHOR-PROVIDED` |
| Route d’asset | `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ`, `HYBRIDE` |

Cette séparation est bonne : état de vérification, origine de l’ancre et moyen de production ne sont pas la même chose. Les claims mesurés, datés, réglementaires ou dépendants d’un outil reçoivent source, date, portée et limite. Un prompt ou une requête ne devient pas une preuve d’adéquation de l’asset.

Le transport reste cependant implicite. `run_card.sources` n’accepte que des chaînes ; `anchors[]` n’accepte ni type, ni ID, ni route d’asset, ni statut de droits ; aucun objet d’asset n’existe. Le manifeste externe peut légitimement porter ces informations, mais aucun mapping ne dit quelles données restent dans la carte, lesquelles sont externalisées et comment les résoudre depuis `trace_locator`.

### Sélection contre la facilité

Le bloc ne condamne pas la solution simple. Il exige seulement que sa simplicité soit défendue par JTBD, risque, droits, performance, maintenance ou contrainte réelle. Cette règle distingue simplicité appropriée et choix opportuniste dicté uniquement par l’implémentation immédiate.

### Checkpoint pré-build et autonomie

La règle est claire dans son premier paragraphe : en session interactive, une validation précède le build lorsque l’autonomie ne couvre pas explicitement le périmètre DIRECTION. Nouvelle marque, nouveau public, nouvelle surface identitaire ou nouvelle hypothèse déclenchent un nouveau checkpoint.

Le bloc précédent `ACTION/AUTHORITY` exigeait portée, base de l’autonomie, condition de reprise/escalade et rôle qui reprend la décision. Aucun de ces éléments n’a de champ structuré dans la `RUN_CARD`; un objet `authority` est rejeté. Une nouvelle identité sans checkpoint ni trace d’autorité est validée.

La phrase suivante crée une ambiguïté supplémentaire : l’absence de « regard externe » peut être compensée par capture, comparaison, réserve et prochaine preuve. Elle ne précise pas que ce regard est une revue indépendante distincte du checkpoint d’autorité. Un lecteur pressé peut donc croire qu’un owner indisponible peut être remplacé par une auto-comparaison, alors que `ACTION/AUTHORITY` impose retour, exploration ou escalade lorsque l’autonomie manque.

### Vérification du rendu réel

L’observation post-build est riche : capture, comparaison à la spec, observation, cause probable, effet sur la tâche/direction et issue. La priorité donnée à structure, hiérarchie, typographie, composition, spécificité, assets, composants, états et finition protège contre un polish décoratif masquant un défaut structurel.

Les valeurs locales `CORRECTED`, `ACCEPTED-DIFFERENCE` et `REMAINING-RISK` ne sont cependant placées dans aucun registre canonique. Elles ne sont ni des valeurs de `closure.issue`, ni des verdicts globaux, ni des statuts de direction, ni des types structurés de `decision_change`. Le mot « issue » utilisé dans la phrase augmente le risque de les confondre avec `ISSUE`.

Un objet structuré `render_comparison` est rejeté. Les résultats peuvent vivre dans la trace externe ou une chaîne libre, mais aucune règle ne relie :

- `CORRECTED` à la correction et sa réinspection ;
- `ACCEPTED-DIFFERENCE` à `HELD-WITH-ACCEPTED-DIFFERENCE` ou à une réserve ;
- `REMAINING-RISK` au cycle de vie des réserves de F-ACT-023.

### Passe créative et polish

La revue reste courte et ne produit ni score, ni statut. Elle inspecte présence, point de vue, spécificité, transformation réelle de la référence, généricité, résolution et geste de polish dominant. La repasse corrige d’abord la relation la plus importante et refuse les effets sans conséquence observable.

La clôture humaine doit répondre à quatre questions : présence, signature, détail de craft et défaut prioritaire. Le schéma exige cinq champs, avec `next_polish_action`. Un producteur suivant littéralement les quatre questions échoue donc à la validation machine.

Cette divergence renforce F-ACT-025 : lorsque le one-shot est valide ou que le polish doit s’arrêter, la cinquième valeur devrait pouvoir exprimer explicitement un arrêt justifié plutôt qu’une action artificielle.

### Représentativité de la preuve

Le bloc protège correctement la différence entre capture idéale et artefact réel. Une preuve visuelle ne doit pas masquer état, viewport, contenu ou comportement non inspecté. Les niveaux `Correction`, `Précision` et `Intention` restent une lentille locale issue de SAVOIR, pas un score ni un verdict.

La projection ne relie toutefois pas le scope de l’artefact à la couverture observée. Une carte dont `artifact.scope` couvre desktop, mobile et états, mais dont la preuve observe seulement un hero desktop idéal et déclare le reste non vérifié, peut encore produire `ACCEPTED`. Cela renforce F-ACT-005, F-ACT-012 et F-ACT-021 sans créer un nouveau registre de couverture.

### Retour sans quota

Le pipeline retourne à la direction, à l’ancre, à la spec ou au build selon la localisation du défaut. Il n’impose aucun nombre fixe d’itérations. Lorsque la correction locale ne modifie plus le résultat, il revient au niveau de décision approprié au lieu d’ajouter des effets.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

Exécutée depuis la racine canonique du package :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

Ce PASS confirme l’intégrité de B01. Il ne couvre pas les divergences de trace, d’autorité et de registre caractérisées par les mutations suivantes.

### Contrôle 1 — routes

```text
ACTION/PIPELINE-DIRECTION  FAIL
DIRECTION/DOUBLE-LOOP      PASS
DIRECTION/VISUAL_TARGET    PASS
ACTION/RUN-DIRECTION       PASS
ACTION/VISUAL_PROOF        FAIL
ACTION/GATE-B              FAIL
ACTION/GATE-C              FAIL
SAVOIR/CRAFT               PASS
ACTION/CLOSE-PACKAGE       PASS
ACTION/CLOSE-EXIT-CHECK    PASS
```

### Contrôle 2 — checkpoint et autorité

```text
Nouvelle marque + nouvelle surface identitaire
Aucun checkpoint ou objet d’autorité
Résultat : ACCEPTED

Ajout d’un objet authority {scope, basis, resume_condition, takeover_role}
Résultat : REJECTED — propriété inconnue
```

### Contrôle 3 — regard externe indisponible

```text
capability_profile.unavailable = ["regard externe indépendant"]
preuve = auto-comparaison du même producteur
not_verified = regard externe non réalisé
verdict = ACCEPTED
réserve spécifique = absente
Résultat : ACCEPTED
```

Le test confirme le défaut de raccord avec la réserve et la prochaine preuve exigées par la prose. Il ne suppose pas que toute revue externe soit obligatoire pour tout run.

### Contrôle 4 — qualification des sources et ancres

```text
sources[0] = {locator, status, date, scope, limitation}
Résultat : REJECTED — type attendu string

anchors[0] enrichi avec anchor_type, anchor_id, counterindication,
expected_proof, asset_route et rights_status
Résultat : REJECTED — champs inconnus
```

### Contrôle 5 — comparaison du rendu

```text
render_comparison = [{observation, probable_cause, effect, outcome: REMAINING-RISK}]
Résultat : REJECTED — propriété inconnue
```

### Contrôle 6 — creative close

```text
presence + signature + craft_detail + dominant_defect
next_polish_action absent
Résultat : REJECTED — creative_close exige next_polish_action
```

### Contrôle 7 — one-shot

```text
Décision confirmée après observation initiale
Aucun défaut dominant restant
next_polish_action = STOP justifié
verdict = ACCEPTED
Résultat : ACCEPTED

Ajout execution_branch = ONE-SHOT
Résultat : REJECTED — propriété inconnue
```

La branche n’a pas besoin d’être un statut. Le test montre seulement que sa vérification dépend de la trace et de la preuve, pas d’un champ machine dédié.

### Contrôle 8 — preuve non représentative

```text
artifact.scope = desktop + mobile + états
observed = capture idéale desktop
not_verified = mobile + états + contenu long + comportement
verdict = ACCEPTED
Résultat : ACCEPTED
```

## Passage C — usages simulés

### Premier rendu excellent

La spec est claire, le rendu est complet, la capture tient la direction et aucun gain utile n’est probable. Le one-shot permet correctement de confirmer la décision et de clôturer sans fabriquer une seconde version.

### Premier rendu générique

La rationale est forte mais l’artefact est interchangeable. La branche one-shot est indisponible ; le pipeline retourne à la position, à l’ancre ou à la spec, puis exige une correction visible. Le texte protège correctement contre l’acceptation narrative.

### Alternative sans effet

Une deuxième direction ne modifierait ni public, ni JTBD, ni contrainte, ni risque. Le designer note la raison et passe à la spec. Aucun quota de variantes n’est imposé.

### Nouvelle marque sans owner disponible

La première phrase du checkpoint interdit le build sans autonomie couvrant la nouvelle marque. La phrase sur l’absence de regard externe peut cependant être lue comme voie de compensation. Le comportement correct, selon AUTHORITY, est de retourner, explorer ou escalader — pas de convertir l’auto-comparaison en autorisation.

### Recherche substantielle depuis la mémoire du modèle

Le statut `MODEL-KNOWLEDGE-NOT-RECHECKED` limite honnêtement le claim. Si le claim est daté ou réglementaire, une source ouverte, datée et bornée reste nécessaire. La règle humaine est saine ; le statut n’est simplement pas contrôlable dans `sources[]` autrement que comme texte.

### Asset généré à enjeu identitaire élevé

L’ancre générée seule devrait recevoir calibration externe, contrainte réelle ou réserve. Comme le type d’ancre et la route d’asset ne sont pas représentés, une carte HELD peut passer sans cette protection. F-DIR-027 est confirmé depuis ACTION.

### Écart post-build accepté

Le reviewer inscrit `ACCEPTED-DIFFERENCE`, mais ne sait pas si cela doit devenir statut de direction, décision-change, réserve ou simple ligne de comparaison. Deux équipes peuvent persister le même événement dans des registres différents.

### Hero desktop idéal, mobile non inspecté

La capture est belle et la direction identifiable, mais le scope livré inclut mobile et états. La prose interdit de masquer ces absences ; le validateur autorise néanmoins l’acceptation pleine.

### Clôture sans défaut restant

Les quatre questions humaines sont satisfaites et aucun polish supplémentaire n’est utile. Le schéma exige encore une cinquième chaîne. La sortie la plus honnête est un arrêt justifié, mais cette convention n’est pas écrite.

## Passage D — constats

### F-ACT-026 — le checkpoint d’autorité peut être confondu avec un regard externe compensable

- Gravité provisoire : **Majeur provisoire**
- État : **ambiguïté opérationnelle et lacune de transport confirmées**
- Preuve : lignes 499–505 exigent validation avant build sans autonomie, puis autorisent la compensation de l’absence de « regard externe » sans distinguer reviewer et autorité ; une nouvelle identité sans checkpoint valide, tandis qu’un objet d’autorité structuré est rejeté
- Comportement observable : un agent peut remplacer une autorisation manquante par auto-comparaison, capture, réserve et prochaine preuve, puis poursuivre le build
- Risque : action au-delà du scope autorisé, nouvelle identité construite sans décision du rôle responsable, confusion entre qualité de preuve et droit d’agir
- Facteur atténuant : `ACTION/AUTHORITY` interdit explicitement la baisse silencieuse et ordonne retour, exploration ou escalade lorsque le checkpoint manque ; la trace externe peut conserver l’autonomie
- Relations : F-DIR-017, F-ACT-002, F-ACT-010, F-ACT-018 et F-ACT-024
- Propriétaires pressentis : ACTION/AUTHORITY pour la décision ; PIPELINE-DIRECTION pour distinguer checkpoint et revue indépendante ; RUN_CARD/trace pour le transport
- Test futur : autonomie explicite/implicite/absente, owner disponible/indisponible, revue indépendante disponible/absente, nouveau public, nouvelle marque et extension de scope

### F-ACT-027 — les résultats d’écart post-build créent une taxonomie locale sans registre canonique

- Gravité provisoire : **Significatif**
- État : **ambiguïté de registre confirmée**
- Preuve : ligne 509 appelle « issue » les valeurs `CORRECTED`, `ACCEPTED-DIFFERENCE` et `REMAINING-RISK`; aucune n’appartient aux enums `ISSUE`, verdict ou statut de direction, et aucun objet de comparaison n’est accepté
- Comportement observable : le même écart peut être persisté comme texte de preuve, décision-change, limitation, réserve ou statut de direction selon l’équipe
- Risque : perte de cause/effet, réserves non suivies, différence acceptée sans `HELD-WITH-ACCEPTED-DIFFERENCE`, confusion avec l’ISSUE canonique
- Facteur atténuant : ces valeurs peuvent être comprises comme résultats locaux de comparaison, non comme nouveaux statuts ; `trace_locator` peut préserver le détail
- Relations : F-ACT-003, F-ACT-010, F-ACT-013, F-ACT-023 et F-DIR-030
- Propriétaires pressentis : ACTION/STATUS pour nommer le registre ; PIPELINE-DIRECTION pour le mapping ; trace ou RUN_CARD pour la persistance choisie
- Test futur : correction réinspectée, différence acceptée avec et sans effet sur la direction, remaining risk avec owner/review/exit, plusieurs écarts et verdict final

### F-ACT-028 — la trace de sources, ancres et assets n’a pas de mapping structuré commun

- Gravité provisoire : **Significatif**
- État : **divergence de transport confirmée**
- Preuve : lignes 475–491 demandent type/ID d’ancre, statut épistémique, route d’asset, droits et preuve attendue ; `sources[]` n’accepte que des chaînes et `anchors[]` rejette ces propriétés
- Comportement observable : statuts, types et routes sont concaténés dans des chaînes libres, déplacés dans un manifeste sans convention de résolution ou omis tout en conservant une carte valide
- Risque : impossibilité d’appliquer la réserve generated-only, confusion source/ancre/asset, droits perdus, claim daté présenté sans statut de vérification
- Facteur atténuant : le texte autorise explicitement un manifeste externe ; `trace_locator` peut le rendre retrouvable ; la projection JSON est déclarée partielle
- Relations : F-DIR-006, F-DIR-027, F-DIR-029, F-ACT-002, F-ACT-024 et F-ACT-026
- Propriétaires pressentis : ACTION pour le mapping de trace ; DIRECTION pour les types d’ancre et routes d’asset ; schéma seulement pour les éléments choisis comme invariants machine
- Test futur : source vérifiée/non revue, trois types d’ancre, cinq routes d’asset, droits connus/inconnus, manifeste externe, locator cassé et réserve generated-only

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — routes

Le pipeline appelé par RUN-DIRECTION reste non résoluble, de même que VISUAL_PROOF et les gates B/C. DOUBLE-LOOP, VISUAL_TARGET, RUN-DIRECTION, SAVOIR/CRAFT et les deux routes de clôture passent. Le défaut reste celui d’une carte fermée incomplète, pas d’une absence documentaire.

### F-ACT-002 et F-DIR-006 — mapping

Autorité, source qualifiée, type/ID d’ancre, route d’asset, comparaison d’écarts et branche d’exécution restent hors projection. L’externalisation est acceptable si le mapping et la résolution sont explicites ; ils ne le sont pas encore.

### F-ACT-005, F-ACT-012 et F-ACT-021 — couverture de preuve

La phrase sur la capture idéale fournit une règle propriétaire très claire : scope livré et scope observé ne doivent pas être confondus. Le test desktop/mobile montre pourtant qu’une acceptation pleine reste possible lorsque des parties déclarées du scope sont non vérifiées. Les trois constats sont renforcés.

### F-ACT-013 — conséquence décisionnelle

Le one-shot montre un usage légitime de `decision_change` comme confirmation, sans correction artificielle. La projection ne distingue toujours pas confirmation, modification ou abandon, mais la sémantique humaine est cohérente.

### F-ACT-018 — capacité et regard externe

Une auto-comparaison avec regard externe indisponible produit encore `ACCEPTED`. Le pipeline exige pourtant réserve et prochaine preuve. La divergence capacité/claim est renforcée.

### F-ACT-023 — réserve

`REMAINING-RISK` est explicitement produit par la comparaison post-build. Aucun raccord ne lui attribue owner, review date et exit condition. Le cycle de vie non transportable affecte donc directement le pipeline DIRECTION.

### F-ACT-024 — droits et confidentialité

La route d’asset exige droits ou incertitudes et alternative refusée, ce qui renforce la qualité humaine du contrat. L’absence de champ structuré et de conséquence automatique reste ouverte jusqu’à la fiche d’asset et aux gates aval.

### F-ACT-025 — arrêt du polish

Le pipeline confirme le one-shot et l’absence de nombre fixe d’itérations, mais sa clôture humaine énumère quatre réponses alors que le schéma exige `next_polish_action` en cinquième. La convention d’arrêt justifié devient nécessaire pour éviter une action fictive.

### F-DIR-009 — one-shot

ACTION confirme que la correction n’est pas obligatoire après un premier rendu suffisant. Le défaut reste strictement local au Creative Boot qui exige encore une modification réelle.

### F-DIR-017 — checkpoint pré-build

Le propriétaire ACTION confirme enfin le checkpoint pour nouvelle marque, nouveau public, nouvelle surface ou nouvelle hypothèse. La façade EXTERNAL-START reste incomplète et F-ACT-026 ajoute le risque de confusion entre autorité et regard externe.

### F-DIR-027 — contrat des ancres

ACTION annonce explicitement type et identifiant d’ancre, mais la projection les rejette. La divergence humain/machine et la protection generated-only non exécutable sont confirmées.

### F-DIR-030 — propriété du craft

La ligne 447 sépare clairement décision créative, exécution et gate ; la ligne 521 garde les niveaux de craft comme lentille locale sans score. Le constat est fortement atténué dans ACTION, même si les façades DIRECTION et SAVOIR devront rester alignées.

## Éléments conformes à préserver

1. DOUBLE-LOOP, pipeline livrable et gate spécialisé ne sont pas des boucles concurrentes.
2. Une correction change l’artefact, la décision, la tâche, la preuve, la contrainte ou la robustesse.
3. Une nouvelle rationale n’est jamais une correction.
4. Le one-shot conserve préparation, rendu complet, observation, risque et condition de sortie.
5. Un rendu faible ou générique ne peut pas se cacher derrière le one-shot.
6. Aucun quota de directions ou d’itérations n’est imposé.
7. Une alternative n’est matérialisée qu’au niveau nécessaire pour changer le choix.
8. Un adjectif émotionnel doit produire une décision visible.
9. La spec précède le premier code ou rendu DIRECTION.
10. Une ancre générée reste une hypothèse, pas une calibration externe suffisante.
11. Une ancre utile apporte décision, contre-indication et attributs retenus/rejetés/non transférables.
12. Sans ancre utile et spec exploitable, les axes concernés restent non vérifiés.
13. BIBLIOTHEQUE n’est ni source d’asset, ni ancre, ni preuve de comparaison.
14. Les claims datés ou réglementaires exigent source, date, portée et limite.
15. Un prompt ou une requête ne prouve pas l’adéquation d’un asset.
16. La solution simple reste légitime lorsqu’une contrainte réelle la justifie.
17. Le checkpoint dépend du scope d’autonomie, pas de la seule capacité de build.
18. L’absence de revue externe ne devient jamais validation implicite.
19. Le rendu est comparé à la spec après build, pas à la rationale seule.
20. Un défaut structurel n’est pas corrigé par un effet terminal.
21. La revue créative ne crée ni score, ni statut, ni verdict concurrent.
22. Le polish corrige d’abord le défaut dominant.
23. Une capture idéale ne masque pas les états et viewports non inspectés.
24. Les niveaux de craft restent distincts du verdict global.
25. Une qualité visuelle observée ne prouve ni usage, ni accessibilité, ni robustesse.
26. Le retour cible direction, ancre, spec ou build selon la cause du défaut.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Niveaux, séquence, routes, amont et aval examinés |
| B — Contrats | FULL | Boucle, one-shot, huit étapes, creative close et retour analysés phrase par phrase |
| C — Usage | TARGETED | Neuf scénarios de direction, autorité, source, asset, preuve et clôture simulés |
| D — Résistance | FULL | Trois nouveaux constats et douze familles antérieures consolidés |
| Contrôles machine | FULL ciblé | Routes, autorité, regard externe, sources, ancres, écarts, one-shot, creative close et couverture testés |

## Point de passage

Le bloc 7 d’ACTION est entièrement lu. Son cœur créatif doit être largement préservé : il construit un premier objet complet, refuse les variantes et itérations rituelles, exige une conséquence visible et maintient la distinction entre qualité visuelle et preuve d’usage. Les faiblesses portent sur le raccord à l’autorité et à la trace, pas sur la logique créative principale.

La prochaine unité est `ACTION.md`, lignes 527–602 : `ACTION/STRUCTURED-PROOF`, carte de hiérarchie, preuve U attendue, partition typographique, fiche d’asset directeur, contrat de composant/baseline et contrat de motion/scène spatiale. Elle devra vérifier la proportionnalité réelle des artefacts pré-build, la frontière entre contrat attendu et preuve exécutée, la couverture accessibilité/états, les droits d’asset, la version de baseline et l’absence intentionnelle. Aucun patch n’est autorisé à ce stade.
