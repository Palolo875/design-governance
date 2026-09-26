# DG-AUDIT-001 — Phase 2 — Checkpoint de consolidation DIRECTION

## Nature du checkpoint

Ce document consolide les dix diagnostics sectionnels produits pendant la lecture complète de `V1/official/DIRECTION.md`. Il sert à empêcher trois pertes avant l’ouverture d’`ACTION.md` :

1. confondre une cause transversale avec chacune de ses occurrences locales ;
2. fusionner trop tôt des constats qui dépendent de propriétaires encore non lus intégralement ;
3. transformer des gravités provisoires de phase 2 en décisions de patch de phase 10 ou 11.

Ce checkpoint n’est donc :

- ni un verdict global sur DIRECTION ;
- ni la classification finale des constats ;
- ni une décision de correction ;
- ni une autorisation de modifier le corpus.

Le protocole exige que la lecture complète du périmètre précède le diagnostic final. DIRECTION est entièrement lu ; le périmètre système ne l’est pas encore.

## Intégrité des entrées

### Baseline

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les deux empreintes correspondent toujours à B01. Aucun patch n’a été appliqué à la source compilée ou à la reconstruction de travail.

### Rapports consolidés

Le checkpoint reprend exactement :

1. `Audit_DIRECTION_Phase2_01_Constitution.md` ;
2. `Audit_DIRECTION_Phase2_02_START.md` ;
3. `Audit_DIRECTION_Phase2_03_Daily_Fast_External.md` ;
4. `Audit_DIRECTION_Phase2_04_First_Object_Grounding_Reuse.md` ;
5. `Audit_DIRECTION_Phase2_05_Visual_Target_Anchors_Assets.md` ;
6. `Audit_DIRECTION_Phase2_06_Atelier_Truth_Double_Loop.md` ;
7. `Audit_DIRECTION_Phase2_07_Role_Five_Absolutes.md` ;
8. `Audit_DIRECTION_Phase2_08_Posture_Mode_ITER_Capacity.md` ;
9. `Audit_DIRECTION_Phase2_09_Divergence_Routing.md` ;
10. `Audit_DIRECTION_Phase2_10_Invariants_Closure_Instrumentation.md`.

Empreinte agrégée ordonnée du manifeste de ces dix rapports :

```text
f114eacafbe571f5f6de80b75ec0e3abcb19dd3357046cc5de9f911ac462f2a9
```

### Couverture de lecture

Les blocs couvrent les lignes utiles 1–817 de DIRECTION :

| Bloc | Lignes |
|---|---:|
| 01 | 1–109 |
| 02 | 113–241 |
| 03 | 245–312 |
| 04 | 314–369 |
| 05 | 373–445 |
| 06 | 449–541 |
| 07 | 543–642 |
| 08 | 646–700 |
| 09 | 701–762 |
| 10 | 766–817 |

Les intervalles non nommés entre ces plages ont été revérifiés. Ils ne contiennent que lignes vides, séparateurs Markdown ou la ligne immédiatement antérieure d’un titre inclus dans le bloc suivant. Aucun contenu normatif n’est omis.

## Méthode de consolidation

Chaque ID est conservé. La consolidation distingue :

- **cause transversale** : défaut qui explique plusieurs occurrences ;
- **occurrence locale** : manifestation concrète avec son propre comportement ou risque ;
- **dépendance** : constat dont la disposition exige la lecture d’un autre propriétaire ;
- **candidat à fusion** : deux constats peut-être réductibles à une seule cause, sans fusion avant confirmation ;
- **observation ouverte** : risque plausible dont l’impact réel reste à éprouver.

Une proximité de vocabulaire ne suffit pas à fusionner deux constats. Deux IDs restent distincts si leur correction, leur propriétaire, leur test de non-régression ou leur comportement observable diffèrent.

## État quantitatif provisoire

| Niveau provisoire après les mises à jour des dix blocs | Nombre | IDs |
|---|---:|---|
| Bloquant | 0 | — |
| Majeur | 2 | F-DIR-007, F-DIR-027 |
| Significatif ou provisoirement significatif | 38 | Tous les IDs hors catégories Majeur et Observation/Mineur ci-dessous |
| Observation / Mineur | 6 | F-DIR-004, F-DIR-005, F-DIR-017, F-DIR-038, F-DIR-040, F-DIR-043 |
| Total | 46 | F-DIR-001 à F-DIR-046, séquence continue |

Ces niveaux ne sont pas la classification finale de phase 10. F-DIR-027 reste explicitement **Majeur provisoire** ; plusieurs constats significatifs portent encore une réserve « à éprouver » ou « ouvert ».

## Neuf familles de causes et d’interfaces

| Famille | IDs | Noyau commun | Ce qu’il ne faut pas confondre |
|---|---|---|---|
| C1 — Architecture de lecture et façades | 001, 020, 028, 043, 044 | Ordre, vues dérivées, résolution des routes et instrumentation de lecture | Ordre causal, divergence de grille, accès outillé et taxonomie de mesure sont quatre effets différents |
| C2 — Classification, mode et routage initial | 007, 014, 016, 017, 031, 041 | Choisir la bonne route avant qu’un artefact ou une preuve soit engagé | Trou de mode, perte d’un mode dans une façade, brief sans risque, autorité pré-build et temporalité ne se corrigent pas par une seule phrase |
| C3 — Trace, projection, statuts et clôture | 003, 006, 008, 010, 013, 015, 019, 023, 034, 035, 036, 039, 045 | Transporter les décisions sans perte entre vue humaine, trace et RUN_CARD | Mapping, multiplicité des formes, sémantique d’un champ, minimum de preuve et chemin JSON restent distincts |
| C4 — Boucle créative, premier objet et ownership de craft | 009, 012, 018, 030, 042 | Construire et juger un premier objet sans quota, sur-contrainte ni propriétaire concurrent | Itération forcée, cardinalité, forme légitime, frontière de jugement et erreur de route nécessitent des tests différents |
| C5 — Preuve, vérité et sémantique des conclusions | 002, 011, 021, 024, 029, 032, 033 | Ne pas transformer hypothèse, objet, label ou méthode en preuve plus forte qu’observée | Claim d’efficacité, absence de changement, divulgation, collision de terme, axes de vérité et méthode humaine ne sont pas des doublons |
| C6 — Grounding, assets et ancres | 022, 025, 026, 027 | Représenter honnêtement présence, absence, source, limite et voie d’ancrage | Refus de grounding, absence d’asset, recherche non bornée et divergence machine ont des owners et sorties différents |
| C7 — Portée, capacité et médium | 004, 037, 038 | Adapter construction et preuve au médium réel sans rétrécissement ni universalisation Web | Portée déclarée, activation de capacité et exemples Web/mobile sont trois contrats différents |
| C8 — Promotion et gouvernance | 046 | Faire évoluer une règle chez son propriétaire sans forcer une route structurelle | Une promotion de structure n’est pas une promotion de méthode, de schéma ou de preuve |
| C9 — Dette éditoriale localisée | 005, 040 | Réduire les ambiguïtés sans leur donner une gravité artificielle | Légende de corpus et terme unique non défini restent deux observations locales |

Les neuf familles couvrent chacun des 46 IDs exactement une fois.

## Décisions de déduplication provisoires

### D1 — F-DIR-011 et F-DIR-019 : seule fusion réellement plausible

F-DIR-011 constate une mauvaise classification de l’absence de changement. F-DIR-019 montre le même mécanisme dans le contrat du premier objet, où `NOT-VERIFIED` ou `NOT-OBSERVED` disparaît au profit de `N/A-JUSTIFIED`.

Décision du checkpoint :

- conserver les deux IDs pendant la lecture d’ACTION ;
- traiter F-DIR-011 comme cause sémantique potentielle ;
- traiter F-DIR-019 comme occurrence spécialisée et test de non-régression ;
- fusionner seulement si ACTION confirme un contrat unique applicable aux deux situations sans perte de test.

### D2 — F-DIR-006 et F-DIR-010 : liés, mais non fusionnables

F-DIR-006 porte l’absence de mapping explicite entre vues, trace et projection. F-DIR-010 porte la multiplication de formes minimales concurrentes. Un système peut avoir plusieurs vues correctement mappées, ou une seule vue mal mappée : les deux défauts sont indépendants.

F-DIR-013, F-DIR-020, F-DIR-023, F-DIR-039 et F-DIR-045 sont des occurrences ou conséquences précises de ce couple, mais conservent leurs propres comportements, propriétaires et tests.

### D3 — F-DIR-028 absorbe déjà les échecs de locators ultérieurs

F-DIR-028 a été découvert sur `DIRECTION/DIRECTION-ATELIER`, puis étendu à dix routes SAVOIR et au renvoi `DIRECTION/lecture instrumentée`. Ces échecs n’ont pas reçu de nouveaux IDs, car ils confirment la même insuffisance de couverture du lecteur et de son validateur.

Décision du checkpoint : conserver F-DIR-028 comme constat systémique unique et considérer chaque locator rejeté comme fixture future.

### D4 — F-DIR-030 et F-DIR-042 : frontière contre erreur de routage

F-DIR-030 concerne la propriété du jugement de craft. F-DIR-042 concerne des lignes de routage qui attribuent ou omettent concrètement les mauvais propriétaires. Corriger les trois routes fautives ne suffirait pas à clarifier la frontière générale ; réécrire la frontière ne garantit pas que les routes deviennent exactes.

Décision : conserver les deux.

### D5 — F-DIR-034, F-DIR-035 et F-DIR-045 : trois étages de clôture

- F-DIR-034 : minimum de preuve local affaibli ;
- F-DIR-035 : registres de fidélité et de clôture confondus ;
- F-DIR-045 : chemin machine `limitations` erroné.

Ils touchent la même interface mais pas le même contrat. Les fusionner rendrait impossible de savoir si une correction textuelle, sémantique et JSON a réellement couvert les trois risques.

### D6 — F-DIR-002 et F-DIR-044 : dépendance de mesure, pas doublon

F-DIR-002 porte un claim d’efficacité non démontré. F-DIR-044 rend l’instrumentation de lecture ambiguë. Une taxonomie corrigée ne démontrerait pas l’efficacité ; elle permettrait seulement de mieux mesurer une partie de la charge. Les deux IDs restent distincts et liés.

### D7 — F-DIR-004 et F-DIR-038 : tension de portée, pas répétition

F-DIR-004 soupçonne une portée déclarée plus étroite que les usages évoqués. F-DIR-038 soupçonne l’application trop large de contrôles Web/mobile à d’autres médiums. Le premier risque sous-déclare ; le second sur-généralise. Leur résolution commune devra définir la portée puis traduire les contrôles, pas supprimer l’un des constats.

### D8 — F-DIR-021 et F-DIR-029 : transport contre orthogonalité

F-DIR-021 demande à qui le marquage de vérité s’adresse et comment il est transporté. F-DIR-029 montre que les labels mélangent factualité et nature du claim. Une taxonomie orthogonale pourrait encore être affichée au mauvais public ; un transport correct pourrait encore transporter un label ambigu. Les deux restent distincts.

## Registre provisoire des 46 constats

| ID | Libellé consolidé | Gravité p. | Relation de consolidation | Lecture propriétaire requise avant disposition |
|---|---|---|---|---|
| F-DIR-001 | Ordre cible / premier objet divergent selon les façades | Significatif | Cause de façade C1 | ACTION, QUICKSTART, READING_MAP |
| F-DIR-002 | Claim d’efficacité non démontré | Significatif | Distinct ; lié à F-044 | CHANGELOG, pilotes et instrumentation |
| F-DIR-003 | Temporalité du handoff insuffisamment explicite | Significatif | Cause temporelle C3 | ACTION/HANDOFF, RUN_CARD, états |
| F-DIR-004 | Portée déclarée possiblement plus étroite que les médiums appliqués | Observation | Ouvert C7 | SAVOIR/TECH, ACTION par médium |
| F-DIR-005 | Légende locale partiellement inactive | Mineur / Observation | Dette éditoriale C9 | Usage des tags dans tout le corpus |
| F-DIR-006 | Mapping humain / trace / projection informel | Significatif p. | Cause systémique C3 | ACTION, schéma, exemples, trace externe |
| F-DIR-007 | Correctif critique local sans classification stable | Majeur | Cause de mode C2 | ACTION, schéma et validateur |
| F-DIR-008 | Omission de champs incompatible avec owner et scope | Significatif | Occurrences multiples C3 | ACTION/HANDOFF et schéma |
| F-DIR-009 | Creative Boot impose une modification au one-shot valide | Significatif | Défaut local C4 | ACTION, QUICKSTART, SAVOIR |
| F-DIR-010 | Formes minimales concurrentes | Significatif | Cause systémique C3 | ACTION comme forme canonique |
| F-DIR-011 | Absence de changement mal classée | Significatif | Parent possible de F-019 | ACTION : N/A / NOT-OBSERVED / NOT-VERIFIED |
| F-DIR-012 | Cardinalités du Boot non alignées | Significatif à éprouver | Distinct C4 | BIBLIOTHEQUE/TENSION et anti-quota |
| F-DIR-013 | Clôture DAILY incomplète | Significatif | Occurrence F-010 / interface ACTION | CLOSE-PACKAGE et HANDOFF |
| F-DIR-014 | Reclassification LITE sans ITER | Significatif | Défaut local C2 | START et RUN-ITER |
| F-DIR-015 | FAST-PATH perd l’abandon de DECISION-CHANGE | Significatif | Perte sémantique C3 | ACTION/RUN_CARD |
| F-DIR-016 | Traduction humaine sans risque dominant explicite | Significatif à éprouver | Défaut de couverture C2 | START, domaines à risque |
| F-DIR-017 | EXTERNAL-START masque le checkpoint pré-build | Observation à risque | Ouvert C2 | ACTION/AUTHORITY, pipeline, skill |
| F-DIR-018 | Priorité du premier objet sur-contraint des formes légitimes | Significatif localisé | Défaut local C4 | FIRST-OBJECT, BIBLIOTHEQUE/SELECT |
| F-DIR-019 | Premier objet réduit les sorties à observation ou N/A | Significatif | Candidat enfant de F-011 | ACTION statuts et preuves |
| F-DIR-020 | Deux grilles de huit dimensions non alignées | Significatif | Occurrence de projection C1 | DIRECTION et QUICKSTART |
| F-DIR-021 | Marquage de vérité : audience et transport non définis | Significatif à éprouver | Distinct de F-029 | ACTION preuve/scope, artefact visible |
| F-DIR-022 | Refus de grounding insuffisamment gardé | Significatif ouvert | Dépendance C6 | SAVOIR/SOURCE/TOOLS et ACTION |
| F-DIR-023 | VISUAL_TARGET possède plusieurs paquets non équivalents | Significatif | Occurrence F-006/F-010 | DIRECTION puis mapping ACTION |
| F-DIR-024 | « Preuve » confond objet produit et preuve exécutée | Significatif | Frontière sémantique C5 | ACTION propriétaire de PROOF |
| F-DIR-025 | Absence intentionnelle d’asset sans route | Significatif | Lacune taxonomique C6 | DIRECTION + fiche ACTION |
| F-DIR-026 | GÉNÉRÉ-DIRIGÉ dépend d’une recherche non bornée | Significatif | Défaut logique C6 | SAVOIR/SOURCE et contraintes réelles |
| F-DIR-027 | Contrat humain/machine des ancres divergent | Majeur provisoire | Cause systémique C6 | ACTION, SAVOIR, schéma, validateur |
| F-DIR-028 | Lecteur de routes incomplet face aux routes actives | Significatif | Constat systémique C1 | READING_MAP, script, fixtures |
| F-DIR-029 | Labels de vérité non orthogonaux | Significatif | Taxonomie distincte C5 | ACTION pour base/scope/preuve |
| F-DIR-030 | Propriété du jugement de craft brouillée | Significatif | Cause d’ownership C4 | SAVOIR/CRAFT et ACTION review |
| F-DIR-031 | « Avant d’agir » interdit implicitement l’intake nécessaire | Significatif | Temporalité C2 | ACTION/STATUS et START |
| F-DIR-032 | Méthode de preuve humaine redéfinie hors propriétaire | Significatif | Frontière de preuve C5 | SAVOIR méthode, ACTION preuve |
| F-DIR-033 | Contexte / Décision / Rendu non raccordé aux registres | Significatif | Taxonomie parallèle C5 | ACTION axes, gates et méthodes |
| F-DIR-034 | Minimum local de preuve affaibli | Significatif | Occurrence F-010, distincte | ACTION/PRECONDITION, gates, close |
| F-DIR-035 | Fidélité de direction et clôture confondues | Significatif | Registres distincts C3 | ACTION états/issues/verdicts |
| F-DIR-036 | Mémoire ITER non protégée par la projection | Significatif | Divergence machine C3 | ACTION, schéma, validation stricte |
| F-DIR-037 | Activation de capacité omet la construction/robustesse | Significatif | Cause C7 | ACTION, SAVOIR, ORCHESTRATION_MAP |
| F-DIR-038 | Contrôles Web/mobile apparemment universels | Observation à risque | Ouvert C7 | SAVOIR/TECH, ACTION/GATE-A |
| F-DIR-039 | Paquet d’alternative non mappé dans RUN_CARD | Significatif | Occurrence F-006/F-023 | ACTION projection ou trace |
| F-DIR-040 | « Direction modale » unique et non définie | Observation | Dette éditoriale C9 | DIRECTION ; vérifier absence de sens spécialisé |
| F-DIR-041 | Nouvelle structure présélectionnée STANDARD | Significatif | Conflit de route C2 | START et BIBLIOTHEQUE/SELECT |
| F-DIR-042 | Déclencheurs critiques routés vers les mauvais owners | Significatif | Manifestation F-030 | SAVOIR, BIBLIOTHEQUE, ACTION |
| F-DIR-043 | Entrée prioritaire placée et routée comme une fin | Observation à risque | Lié à F-028, non doublon | DIRECTION + politique de locators |
| F-DIR-044 | Catégories de lecture non exclusives | Significatif | Instrumentation C1 | BIBLIOTHEQUE et pilotes |
| F-DIR-045 | `limitations` référencé au mauvais niveau JSON | Significatif | Occurrence exacte F-006/F-035 | ACTION et schéma |
| F-DIR-046 | BIBLIOTHEQUE forcée sur les promotions non structurelles | Significatif | Ownership C8 | Sources normatives + CHANGELOG |

## Carte des dépendances par propriétaire

Cette carte n’attribue pas encore les corrections. Elle indique ce que la lecture suivante doit confirmer ou infirmer.

| Propriétaire / surface | Constats à transporter en priorité | Question à trancher |
|---|---|---|
| `ACTION.md` | 003, 007–011, 013, 015, 017, 019, 021–024, 027, 030–037, 039, 042, 045–046 | Quelle forme est canonique pour handoff, preuve, statuts, autorité, capacité et clôture ? |
| Schéma et validateurs RUN_CARD | 003, 006–008, 010–011, 015, 019, 021, 027, 032–033, 035–036, 039, 045 | Quelles obligations humaines sont projetées, volontairement externes ou réellement non contrôlées ? |
| `SAVOIR.md` | 004, 021–022, 024, 026–027, 029–030, 032, 037–038, 042 | Où vivent jugement, méthode, sourcing, médium et limite ? |
| `BIBLIOTHEQUE.md` | 001, 012, 018, 020, 023, 025, 030, 037, 041–042, 044, 046 | Quelles décisions sont réellement structurelles, avec quelles cardinalités et quelle promotion ? |
| `CHANGELOG.md` | 002, 028, 046 | Qu’est-ce qui est expérimental, mesuré, promu, migré ou seulement documenté ? |
| QUICKSTART / READING_MAP / ORCHESTRATION_MAP | 001, 005–006, 010, 013–014, 017–020, 028, 034, 037, 041, 043–044 | Les façades dérivées conservent-elles exactement ordre, champs, routes et limites ? |
| Skill, scripts et distributions | 017, 028, 043 | Les instructions réellement exécutées pointent-elles vers des locators résolubles et une autorité explicite ? |

Un même ID peut apparaître sous plusieurs dépendances : cela décrit des interfaces à vérifier, pas plusieurs propriétaires de décision.

## Ordre de reprise dans ACTION

La lecture d’ACTION ne doit pas devenir une simple recherche de confirmation. Elle suivra son ordre réel, mais quatre paquets de réserves seront rejoués lorsqu’une section propriétaire apparaît.

### Paquet A — handoff, trace et temporalité

Constats : F-DIR-003, 008, 010, 011, 013, 015, 019, 031.

À vérifier :

- séparation intake / pré-build / observation / décision / clôture ;
- champs requis dans une sortie courte ;
- sémantique de `DECISION-CHANGE`, `N/A-JUSTIFIED`, `NOT-OBSERVED` et `NOT-VERIFIED` ;
- owner, scope, limite, prochaine preuve et condition de sortie.

### Paquet B — modes, runs et protection critique

Constats : F-DIR-007, 014, 016, 017, 034, 035, 036, 041.

À vérifier :

- correctif local critique ;
- reclassification vers ITER ;
- autorité et checkpoint pré-build ;
- préconditions et preuves minimales de chaque run ;
- mémoire suffisante pour ITER ;
- séparation state / issue / direction status / verdict.

### Paquet C — preuve, méthode et capacité

Constats : F-DIR-002, 021, 024, 027, 029, 032, 033, 037, 038, 039.

À vérifier :

- claim, méthode, scope, résultat, limite et prochaine preuve ;
- place de la preuve humaine, experte, manuelle et automatique ;
- adaptation au médium ;
- capacité de construction contre capacité d’observation ;
- transport des ancres, vérités et alternatives.

### Paquet D — craft, structure et gouvernance

Constats : F-DIR-009, 012, 018, 020, 023, 030, 042, 046.

À vérifier :

- one-shot sans itération rituelle ;
- rôle exact de la revue créative ACTION ;
- passage vers SAVOIR et BIBLIOTHEQUE ;
- cas où BIBLIOTHEQUE/EVOLUTION est nécessaire ou hors périmètre.

## Protections positives à préserver pendant tout audit ultérieur

La consolidation ne doit pas transformer DIRECTION en simple liste de défauts. Les corrections futures devront préserver au minimum :

1. START reste la source unique de classification.
2. Le risque critique prévaut sur l’optimisation visuelle.
3. Une structure conventionnelle peut être juste ; la nouveauté n’est pas un quota.
4. Le premier objet doit être spécifique, habitable et jugeable, sans wireframe creux par défaut.
5. Aucun nombre obligatoire de variantes, références, retraits ou itérations n’est imposé.
6. Une alternative n’est produite que si elle peut changer la décision.
7. Une première observation positive peut permettre un one-shot lorsqu’aucune correction utile n’est nécessaire.
8. Une capture, une rationale, une validation de package ou un PASS technique ne prouvent pas automatiquement usage, accessibilité, performance ou qualité visuelle.
9. Une capacité absente réduit la force du claim ; elle ne transforme pas l’inconnu en PASS.
10. `N/A-JUSTIFIED`, `NOT-VERIFIED`, issue, verdict et statut de direction restent des registres différents.
11. DIRECTION cadre ; ACTION exécute et ferme ; SAVOIR juge ; BIBLIOTHEQUE structure ; CHANGELOG gouverne le cycle de vie.
12. Une route, une liste ou une chaîne complète ne remplace jamais le jugement ou la preuve réelle.
13. Les modules sont activés seulement lorsqu’ils peuvent modifier une décision.
14. Le réel et le beau restent coordonnés sans faux réalisme.
15. Les claims de gain restent limités tant que les pilotes ne les démontrent pas.

## Condition de sortie du checkpoint

Le checkpoint est satisfait si :

- les dix rapports sont identifiés et intègres ;
- les lignes utiles 1–817 sont couvertes ;
- les IDs F-DIR-001 à F-DIR-046 sont continus ;
- chaque ID apparaît dans une famille unique ;
- les liens cause/occurrence ne suppriment aucune preuve ;
- chaque réserve possède au moins un propriétaire ou une interface future à lire ;
- aucun patch ni verdict global n’est émis.

Ces conditions sont remplies.

## Prochaine étape protocolaire

La phase 2 continue avec `ACTION.md`, deuxième source normative principale et propriétaire déclaré des procédures, preuves exécutables, gates, statuts, verdicts et clôtures.

Le premier bloc ACTION devra être délimité après lecture de sa table des matières réelle. Avant son diagnostic, il faudra :

1. revérifier les empreintes B01 ;
2. relire la phase 2 du protocole ;
3. relire ce checkpoint plutôt qu’un seul rapport local ;
4. identifier les réserves DIRECTION activées par le bloc ACTION ;
5. effectuer les quatre passages A–D ;
6. ne reclasser aucun constat DIRECTION sans preuve propriétaire nouvelle.

Aucun patch ne sera entrepris avant la lecture complète du périmètre système et les phases de diagnostic prévues par le protocole.
