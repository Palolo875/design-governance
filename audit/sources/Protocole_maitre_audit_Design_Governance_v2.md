---
title: "Protocole maître d’audit — Design Governance"
version: "2.0 — proposition consolidée"
language: fr
document_type: protocole externe de référence
---

Protocole maître d’audit — Design Governance

Version : 2.0 — proposition consolidée
Statut : protocole externe de référence pour l’audit de Design Governance
Nature : instrument d’audit ; ne fait pas partie du système Design Governance audité
Périmètre : fichiers normatifs, façades d’activation, contrats humains et machine, schémas, validateurs, scripts, fixtures, artefacts de mémoire, migrations, distributions, chaînes inter-fichiers et comportement du système complet
Principe d’exécution : cadrer → établir la baseline → comprendre → éprouver → diagnostiquer → décider → corriger si nécessaire → valider → clôturer
Principe de couverture : toutes les dimensions du protocole sont considérées ; leur profondeur varie selon l’objet, le risque, l’autorité, le blast radius, les consommateurs et les observations faites pendant l’audit.

---

## 1. Finalité

Ce protocole sert à auditer Design Governance avec suffisamment de rigueur pour identifier :

- les contradictions ;
- les responsabilités mal placées ;
- les routes concurrentes ;
- les zones trop complexes ou trop faibles ;
- les preuves insuffisantes ;
- les comportements agentiques contournables ;
- les risques de bureaucratisation ;
- les défauts de production ;
- les défauts de maintenance ;
- les limites d’efficacité réelle ;
- les capacités positives manquantes.

L’audit ne cherche pas seulement à réduire le slop, empêcher les erreurs ou vérifier la conformité interne.

Il cherche également à déterminer si le système augmente réellement la probabilité de produire :

- une décision claire ;
- une direction perceptible ;
- un premier objet suffisamment fort ;
- une structure habitable ;
- une expérience utilisable ;
- une preuve honnête ;
- une correction utile ;
- une coordination compréhensible ;
- une maintenance soutenable.

Le protocole n’a pas pour objectif de rendre chaque fichier plus long, plus réglementé ou plus explicite sur chaque détail.

Une correction est utile uniquement lorsqu’elle améliore au moins l’un des éléments suivants sans créer une dette supérieure :

décision, création, preuve, exécution, compréhension, coordination, sécurité, maintenance, observabilité ou capacité d’apprentissage.

«Règle centrale : un fichier ou un système n’est pas meilleur parce qu’il contient davantage de règles. Il est meilleur lorsqu’il rend une bonne décision plus probable, une bonne création plus concrète, une preuve plus honnête, une erreur plus difficile à commettre ou une correction plus facile à effectuer.»

---

## 2. Position du protocole

Ce protocole est externe à Design Governance.

Il ne crée donc aucun :

- mode Design Governance ;
- gate Design Governance ;
- verdict de run ;
- statut produit ;
- règle normative du système ;
- source d’autorité concurrente.

Ses termes comme "LIGHT", "TARGETED", "FULL", "AUDIT-PASS" ou "AUDIT-RETURN" appartiennent uniquement à l’activité d’audit.

Le protocole peut constater qu’une règle de Design Governance est absente, contradictoire, mal placée ou inefficace.

Il ne doit pas devenir lui-même une seconde gouvernance du design.

---

## 3. Deux familles de conclusions à ne jamais confondre

L’audit distingue systématiquement deux niveaux.

### 3.1 Audit de contrat

Il cherche à déterminer si un fichier, une interface ou le système est :

- cohérent ;
- compréhensible ;
- navigable ;
- correctement possédé ;
- compatible avec ses voisins ;
- testable ;
- maintenable ;
- correctement relié à ses preuves et consommateurs.

Une conclusion de contrat peut être obtenue par inspection documentaire, exécution de validateurs, comparaison de schémas ou analyse de dépendances.

### 3.2 Audit d’efficacité

Il cherche à déterminer si le système améliore effectivement :

- une décision ;
- une création ;
- une preuve ;
- un handoff ;
- une correction ;
- un résultat construit ;
- une compréhension ;
- une coordination réelle.

Une conclusion d’efficacité exige une observation suffisamment directe :

- run instrumenté ;
- artefact produit ;
- comparaison ;
- test ;
- observation utilisateur ;
- comportement agentique ;
- résultat reproductible ;
- autre preuve appropriée au claim.

«Une cohérence documentaire ne devient jamais automatiquement une preuve d’efficacité.»

Un fichier peut donc être :

contractuellement solide mais empiriquement non vérifié.

Cette situation doit rester visible.

---

## 4. Modèle de couverture adaptative

Toutes les phases du protocole sont considérées à chaque audit.

Cela ne signifie pas qu’elles reçoivent toutes la même profondeur.

Pour chaque phase, perspective ou scénario, l’auditeur choisit explicitement l’un des cinq niveaux suivants.

| Niveau | Signification |
|---|---|
| LIGHT | Contrôle rapide suffisant ; aucun signal ne justifie davantage. |
|---|---|
| TARGETED | Analyse ciblée sur le risque, la décision, la frontière ou le changement concerné. |
|---|---|
| FULL | Analyse approfondie nécessaire pour conclure honnêtement. |
|---|---|
| N/A-JUSTIFIED | Dimension réellement non applicable, avec justification courte. |
|---|---|
| ESCALATED | L’analyse révèle un problème qui doit être traité à une autre échelle, dans un autre fichier ou par un propriétaire différent. |
|---|---|

Aucune phase ne doit disparaître silencieusement.

"N/A-JUSTIFIED" est une conclusion de couverture, pas un moyen d’éviter une analyse inconfortable.

Une profondeur initialement "LIGHT" peut devenir "TARGETED" ou "FULL" à tout moment si un signal nouveau apparaît.

Une profondeur "FULL" n’oblige pas à prolonger l’analyse lorsqu’aucune nouvelle observation n’est produite.

«Règle de progression : approfondir lorsqu’une observation peut encore modifier le diagnostic ou la décision ; arrêter lorsque la profondeur supplémentaire ne promet plus de gain réel.»

---

## 5. Profils d’audit

Les profils ne déterminent pas quelles phases existent.

Ils fournissent uniquement une profondeur initiale.

LITE

À utiliser pour :

- changement éditorial local ;
- petite façade ;
- correction clairement bornée ;
- artefact à faible autorité ;
- problème dont le blast radius est faible.

Toutes les phases restent considérées.

La majorité peut rester "LIGHT".

Le risque dominant, le propriétaire, la source canonique, le changement et la non-régression deviennent au minimum "TARGETED".

STANDARD

À utiliser pour :

- fichier opérationnel ;
- façade partagée ;
- guide consommé par plusieurs acteurs ;
- changement pouvant modifier plusieurs décisions ;
- interaction entre plusieurs contrats.

Toutes les phases sont considérées.

Les contrats, frontières, architecture, consommateurs, risques et validations applicables sont au minimum "TARGETED".

Les zones dominantes deviennent "FULL".

DEEP

À utiliser pour :

- source normative ;
- changement de gouvernance ;
- schéma critique ;
- validateur critique ;
- migration sensible ;
- blast radius élevé ;
- risque critique ;
- contradiction systémique ;
- campagne de stabilisation d’un fichier propriétaire.

Toutes les phases sont considérées.

Les responsabilités, sources, contrats, interfaces, architecture, scénarios de résistance et validations deviennent généralement "FULL" lorsqu’ils sont applicables.

Les dimensions sans impact restent néanmoins "LIGHT" ou "N/A-JUSTIFIED".

«"DEEP" signifie profondeur élevée là où elle produit de l’information utile. Il ne signifie jamais « produire le maximum de documentation possible ».»

---

## 6. Échelles d’audit

Le protocole s’utilise à plusieurs échelles.

Une campagne complète peut en combiner plusieurs.

### 6.1 Audit intra-fichier

Objet :

un fichier propriétaire ou opérationnel.

Questions principales :

- que possède-t-il ?
- que permet-il ?
- comment est-il lu ?
- quelles décisions produit-il ?
- quelles preuves demande-t-il ?
- quelles responsabilités ne doit-il pas absorber ?
- contient-il des répétitions utiles ou accidentelles ?
- ses chemins courts fonctionnent-ils ?

### 6.2 Audit d’interface

Objet :

la relation entre plusieurs propriétaires ou consommateurs.

Exemples :

"DIRECTION → ACTION"

"SAVOIR → ACTION"

"DIRECTION → BIBLIOTHEQUE"

document humain → schéma machine

schéma → validateur

source → distribution

Questions :

- l’entrée du second correspond-elle réellement à la sortie du premier ?
- une décision change-t-elle de sens pendant le handoff ?
- plusieurs propriétaires pensent-ils posséder le même contrat ?
- une information essentielle se perd-elle ?
- une obligation apparaît-elle sans propriétaire ?

### 6.3 Audit de chaîne

Objet :

un parcours complet.

Exemple :

brief → classification → direction → construction → observation → verdict → persistance.

Il cherche les défauts qui ne sont visibles dans aucun fichier isolé.

### 6.4 Audit système

Objet :

Design Governance comme totalité.

Il examine notamment :

- architecture globale ;
- charge cognitive ;
- nombre réel de taxonomies ;
- concurrence de routes ;
- cohérence humain/machine ;
- adoption ;
- comportement agentique ;
- proportionnalité ;
- capacité à produire ;
- capacité à corriger ;
- maintenabilité ;
- efficacité réelle.

### 6.5 Audit de release ou distribution

Objet :

une version livrable.

Il vérifie :

- cohérence des sources ;
- schémas ;
- validateurs ;
- fixtures ;
- distributions ;
- archives ;
- versions ;
- migrations ;
- reproductibilité ;
- réserves connues.

---

## 7. Principes non négociables

### 7.1 Un propriétaire de décision à la fois

Lorsqu’un défaut normatif est corrigé, un propriétaire principal doit porter la décision.

Les consommateurs et artefacts dérivés peuvent être modifiés dans le même cycle uniquement pour rester alignés.

Ils ne deviennent pas de nouvelles sources d’autorité.

### 7.2 Aucun patch avant diagnostic

Avant toute modification substantielle, établir :

- le comportement observé ;
- le risque ;
- la gravité ;
- le propriétaire ;
- l’impact ;
- le test permettant de vérifier la correction.

Une formulation « meilleure » ou plus élégante ne suffit pas.

### 7.3 La source canonique prime

Une copie distribuée, une archive, un export, une baseline historique ou un extrait ne doit jamais être corrigé à la place de la source propriétaire.

### 7.4 Positif et défensif restent liés

Chaque audit examine :

- ce que le système empêche ;
- ce qu’il permet ;
- ce qu’il rend observable ;
- ce qu’il permet de décider ;
- ce qu’il rend maintenable ;
- ce qu’il risque d’homogénéiser ;
- ce qu’il risque de bureaucratiser.

### 7.5 Une justification n’est pas une preuve

Toujours distinguer :

intention → construction → observation → interprétation → preuve → décision.

Une rationale, un nom de route, une capture isolée ou une règle documentaire ne prouve pas automatiquement un résultat.

### 7.6 Les exceptions restent visibles

Toute réduction de portée, absence de preuve, non-applicabilité, impossibilité, héritage, réserve ou escalade doit rester explicite.

### 7.7 La duplication doit avoir une fonction

Une répétition est acceptable lorsqu’elle :

- protège une frontière ;
- raccourcit un chemin ;
- traduit un concept pour un autre lecteur ;
- évite une erreur probable.

Une répétition qui ne produit aucun de ces effets doit être fusionnée ou retirée.

### 7.8 Les phases ne doivent pas devenir des rituels

Si deux étapes successives produisent la même décision sans nouvelle observation, elles peuvent être fusionnées dans l’exécution.

La couverture reste visible, mais la procédure ne doit pas produire de cérémonial inutile.

---

## 8. Démarrage rapide

Avant tout audit, produire cette fiche minimale :

**AUDIT-ID:**
**TARGET:**
**SCALE:**
**PROFILE:**
**CANONICAL-SOURCE:**
**OWNER:**
**DECISION-AT-RISK:**
**DOMINANT-RISK:**
**CONSUMERS:**
**SCOPE:**
**EXPECTED-EVIDENCE:**
**EXIT-CONDITION:**

Puis :

1. établir la baseline ;
2. lire entièrement le périmètre ;
3. cartographier rôle, contrats et consommateurs ;
4. tester architecture et capacité positive ;
5. appliquer les perspectives et résistances utiles ;
6. classifier les constats ;
7. décider si un patch est réellement justifié ;
8. corriger ;
9. valider ;
10. clôturer.

Cette façade est une interface d’activation.

Elle ne remplace aucune phase détaillée.

---

## 9. Unité d’audit

Chaque cycle possède :

- une cible principale ;
- un propriétaire principal ;
- une décision principale ;
- un risque dominant ;
- une condition de sortie.

Des surfaces secondaires peuvent être examinées lorsque nécessaire :

- fichiers consommateurs ;
- schémas ;
- validateurs ;
- fixtures ;
- exports ;
- historiques ;
- distributions.

Elles restent des surfaces d’alignement sauf lorsqu’un nouvel audit leur attribue explicitement le rôle de cible principale.

Un audit peut produire un seul dossier consolidé.

Les artefacts séparés ne sont requis que si leur séparation apporte une valeur réelle :

- automatisation ;
- revue parallèle ;
- preuve indépendante ;
- archivage ;
- handoff ;
- reproductibilité.

---

## 10. Phase 0 — Préparer le cycle

Objectif

Définir ce qui est audité, pourquoi, par rapport à quelle autorité et jusqu’où.

Établir

| Champ | Question |
|---|---|
"TARGET"| Quel fichier, interface, parcours ou système est audité ?
"SCALE"| Intra-fichier, interface, chaîne, système ou release ?
"CANONICAL-SOURCE"| Quelle source possède réellement le contrat ?
"DOCUMENT-ROLE"| Quel rôle joue la cible ?
"OWNER"| Qui possède la décision active ?
"CONSUMERS"| Qui consomme cette cible ?
"DEPENDENCIES"| De quelles autorités dépend-elle ?
"NON-GOALS"| Que ne doit-elle pas posséder ?
"SCOPE"| Qu’est-ce qui est inclus et exclu ?
"DOMINANT-RISK"| Quel dommage une erreur pourrait-elle produire ?
"EXPECTED-EVIDENCE"| Qu’est-ce qui permettra réellement de conclure ?
"EXIT-CONDITION"| Quand l’audit pourra-t-il s’arrêter ?

Contrôle

Si le propriétaire, la décision ou la condition de sortie ne peuvent pas être formulés clairement, ne commencer aucun patch.

Sortie

"AUDIT-FRAME".

---

## 11. Phase 1 — Établir la baseline

Objectif

Capturer l’état réel avant toute correction.

Baseline minimale

Lorsque pertinent :

- chemin ;
- version ;
- date ou identifiant d’audit ;
- hash ;
- taille ;
- lignes ;
- encodage ;
- hiérarchie des titres ;
- tableaux ;
- blocs machine ;
- identifiants ;
- routes ;
- statuts ;
- liens ;
- références croisées ;
- dépendances ;
- source distribuée ;
- schémas ;
- fixtures ;
- historique comparable.

Les métriques purement mécaniques doivent être automatisées autant que possible.

L’auditeur interprète les écarts ; il ne doit pas perdre du temps à produire manuellement des informations calculables.

Classer toute divergence

- source ;
- distribution ;
- baseline ;
- schéma ;
- documentation ;
- historique ;
- changement attendu ;
- anomalie non expliquée.

Une différence n’est pas automatiquement une erreur.

Sortie

"BASELINE + DIVERGENCES".

---

## 12. Phase 2 — Lire entièrement le périmètre

La lecture complète précède le diagnostic final.

Elle utilise quatre passages complémentaires.

Passage A — Architecture visible

Observer :

- hiérarchie ;
- titres ;
- façades ;
- routes ;
- chemins courts ;
- tableaux ;
- tags d’autorité ;
- blocs machine ;
- tests de sortie ;
- renvois.

Question :

comment le document se présente-t-il comme système d’action ?

Passage B — Contrat sémantique

Pour chaque section, identifier :

- ce qu’elle possède ;
- ce qu’elle définit ;
- ce qu’elle conseille ;
- ce qu’elle interdit ;
- ce qu’elle mesure ;
- ce qu’elle rend optionnel ;
- ce qu’elle transmet ;
- ce qu’elle laisse ouvert.

Question :

que produit réellement cette section ?

Passage C — Usage réel

Simuler les lecteurs applicables :

- agent ;
- designer ;
- reviewer ;
- équipe produit ;
- intégrateur ;
- mainteneur ;
- système automatique ;
- autre consommateur réel.

Question :

que ferait ce lecteur sous contrainte de temps ?

Passage D — Résistance

Chercher activement :

- ambiguïtés ;
- contradictions ;
- obligations contournables ;
- propriétaires concurrents ;
- routes concurrentes ;
- champs sans effet ;
- répétitions ;
- exceptions silencieuses ;
- formulations rassurantes mais non opérationnelles ;
- sorties sans conséquence.

Aucune conclusion globale ne doit être fondée uniquement sur une façade ou un extrait.

Sortie

"READING-MAP + SECTIONAL-DIAGNOSTIC".

---

## 13. Phase 3 — Cartographier les rôles

Chaque cible est examinée selon neuf rôles.

| Rôle | Question |
|---|---|
| Propriété | Qui peut définir ou modifier le contrat ? |
|---|---|
| Décision | Quelle décision devient possible ? |
|---|---|
| Exécution | Qui transforme la décision en action ou artefact ? |
|---|---|
| Preuve | Qu’est-ce qui peut être affirmé et sur quelle base ? |
|---|---|
| Jugement | Qui interprète qualité, pertinence ou risque ? |
|---|---|
| Coordination | Qui orchestre les passages et escalades ? |
|---|---|
| Lecture | Qui lit quoi, quand et pourquoi ? |
|---|---|
| Mémoire | Où restent décisions, versions et limites ? |
|---|---|
| Garde-fou | Quelle erreur ou réduction silencieuse est empêchée ? |
|---|---|

Ajouter lorsque pertinent :

INPUT
OUTPUT
OWNER
ESCALATION
NON-GOAL
NEXT-PROOF
EXIT-CONDITION

Une section est suspecte lorsque son propriétaire, sa décision ou sa sortie ne peuvent pas être formulés concrètement.

Sortie

"ROLE-MAP".

---

## 14. Phase 4 — Auditer les contrats

Examiner sept contrats.

Responsabilité

Que possède la cible ?

Que ne possède-t-elle pas ?

Entrée

Quelles informations sont nécessaires ?

Que se passe-t-il lorsqu’elles manquent ?

Transformation

Comment passe-t-on de l’entrée à :

- décision ;
- artefact ;
- observation ;
- trace ;
- sélection ?

Sortie

La sortie est-elle :

- concrète ;
- retrouvable ;
- interprétable ;
- exploitable par le consommateur suivant ?

Preuve

La preuve est-elle appropriée au :

- claim ;
- risque ;
- support ;
- scope ;
- moment ;
- contexte ;
- niveau d’incertitude ?

Escalade

Que se passe-t-il si :

- le risque augmente ;
- l’information manque ;
- le rendu échoue ;
- une autorité différente doit décider ;
- une capacité n’est pas disponible ?

Mémoire

Les décisions, migrations, réserves et apprentissages restent-ils au bon endroit sans devenir des règles concurrentes ?

Sortie

"CONTRACT-DIAGNOSTIC".

---

## 15. Phase 5 — Auditer l’architecture de l’information

Façade

Un nouveau lecteur comprend-il rapidement :

- le rôle ;
- la capacité positive ;
- le risque dominant ;
- le premier chemin ;
- la prochaine preuve ou le propriétaire suivant ?

Hiérarchie

Les éléments nécessaires à l’action arrivent-ils avant :

- variantes spécialisées ;
- exceptions rares ;
- détails historiques ;
- annexes ;
- instrumentation ?

Chargement conditionnel

Le noyau commun est-il distinct des branches conditionnelles ?

Navigation

Les renvois sont-ils :

- précis ;
- actuels ;
- non circulaires inutilement ;
- suffisamment bidirectionnels ?

Charge cognitive

Examiner notamment :

- nombre de taxonomies ;
- termes à retenir ;
- décisions simultanées ;
- répétitions ;
- tables réellement utiles ;
- profondeur de navigation ;
- nombre de concepts nécessaires avant la première action.

Façade contre source

Une façade :

- simplifie-t-elle ;
- traduit-elle ;
- ou crée-t-elle une seconde autorité ?

Sortie

"INFORMATION-ARCHITECTURE-DIAGNOSTIC".

---

## 16. Phase 6 — Auditer la capacité positive

L’audit ne demande pas seulement :

«« Que bloque ce système ? »»

Il demande :

«« Qu’est-ce qu’il permet de produire de meilleur ? »»

Examiner les dimensions applicables :

| Dimension | Question |
|---|---|
| Présence | Le premier objet peut-il produire une perception forte et juste ? |
|---|---|
| Point de vue | Une position réelle est-elle possible ? |
|---|---|
| Spécificité | Le résultat peut-il appartenir au produit et au contexte ? |
|---|---|
| Composition | Les masses, vides, axes, échelles et rythmes sont-ils gouvernables ? |
|---|---|
| Matière et type | Les assets, la typographie, la donnée ou le code peuvent-ils porter du sens ? |
|---|---|
| Désirabilité située | Le résultat peut-il donner envie sans manipulation ni canon universel ? |
|---|---|
| Résolution | Les détails, états et transformations peuvent-ils tenir l’idée ? |
|---|---|
| Retenue | Le système sait-il ne pas ajouter ? |
|---|---|
| Habitabilité | Le premier objet est-il suffisamment complet pour être jugé ? |
|---|---|
| Transfert | La décision survit-elle au runtime, mobile, contenu et états critiques ? |
|---|---|

Une gouvernance composée uniquement de défenses est incomplète.

Sortie

"POSITIVE-CAPABILITY-DIAGNOSTIC".

---

## 17. Phase 7 — Auditer les boucles de création et de gouvernance

Boucle créative

Le système doit pouvoir soutenir :

comprendre → ouvrir → choisir → composer → produire → observer → améliorer ou confirmer.

Vérifier :

- qualité initiale ;
- divergence utile ;
- observation réelle ;
- correction substantielle ;
- condition d’arrêt.

Boucle de gouvernance

Le système doit pouvoir soutenir :

classer → définir le risque → choisir la route → déclarer la preuve → exécuter → vérifier → décider → persister ou escalader.

One-shot

Un one-shot valide est :

fortement préparé + réellement observé.

Il n’est jamais :

généré une fois = accepté.

Répondre :

1. qu’est-ce qui devait tenir immédiatement ?
2. qu’est-ce qui a réellement été observé ?
3. qu’est-ce qu’une nouvelle itération pourrait encore améliorer ?

Double boucle

Une itération ne compte que si elle modifie au moins :

- artefact ;
- décision ;
- preuve ;
- portée ;
- propriété de robustesse.

Une rationale supplémentaire n’est pas une amélioration.

Sortie

"LOOP-DIAGNOSTIC".

---

## 18. Phase 8 — Audit multi-perspectives

Toutes les perspectives sont considérées.

Chacune reçoit :

"LIGHT", "TARGETED", "FULL", "N/A-JUSTIFIED" ou "ESCALATED".

Perspectives

1. Création visuelle — direction, présence, composition, type, matière, assets, polish, diversité.
2. Produit et usage — JTBD, action, hiérarchie, récupération, confiance.
3. Accessibilité et inclusion — clavier, focus, sémantique, alternatives, reflow, motion, capacité.
4. Contenu et communication — vérité, longueur, localisation, ambiguïté, ton, états.
5. Technique et runtime — compatibilité, performance, fallback, erreur, observabilité.
6. Preuve et épistémologie — claim, méthode, scope, date, limite, extrapolation.
7. Agentique — activation, sélection de route, contournement, coût cognitif, handoff.
8. Équipe — compréhension, collaboration, revue, adoption.
9. Gouvernance — propriété, statuts, exceptions, autorité, conflits.
10. Production et opérations — versionnement, rollback, permissions, confidentialité, maintenance.
11. Expérimentation — hypothèse, baseline, mesure, apprentissage, promotion.
12. Migration — compatibilité avec anciennes routes, aliases, formats, distributions.

Des perspectives supplémentaires peuvent être ajoutées lorsqu’un domaine le justifie.

Elles doivent être nommées et motivées.

Sortie

"PERSPECTIVE-COVERAGE-MATRIX".

---

## 19. Phase 9 — Tests de résistance

Les scénarios constituent une bibliothèque de résistance.

Ils ne sont pas exécutés mécaniquement.

Chaque scénario reçoit également un niveau de couverture.

| Scénario | Question |
|---|---|
| Brief vague | Le système avance-t-il sans inventer le contexte ? |
|---|---|
| One-shot | Peut-il produire un premier objet fort et observable ? |
|---|---|
| Correction locale | Évite-t-il une reconstruction inutile ? |
|---|---|
| Direction identitaire | Traite-t-il réellement singularité, ancrage et composition ? |
|---|---|
| Surface opérationnelle | Usage, action et états restent-ils prioritaires ? |
|---|---|
| Composant partagé | Blast radius, consumers et migration sont-ils visibles ? |
|---|---|
| Contenu long | Le système recompose-t-il plutôt que casser ? |
|---|---|
| Mobile | Priorité, action et rythme survivent-ils ? |
|---|---|
| État critique | La structure s’adapte-t-elle à l’erreur ou la récupération ? |
|---|---|
| Asset absent | La proposition tient-elle sans artifice principal ? |
|---|---|
| Référence séduisante | La relation est-elle transformée plutôt que copiée ? |
|---|---|
| Style recyclé | Le réemploi par confort est-il contesté ? |
|---|---|
| Accessibilité tardive | Peut-elle encore modifier la décision ? |
|---|---|
| Runtime différent | La preuve correspond-elle au runtime réel ? |
|---|---|
| Preuve absente | "NOT-VERIFIED" reste-t-il possible ? |
|---|---|
| Action externe | Permissions, confidentialité et confirmation sont-elles protégées ? |
|---|---|
| Changement post-verdict | La fraîcheur et la réouverture sont-elles claires ? |
|---|---|
| Migration | Les anciennes routes restent-elles dépréciées ? |
|---|---|
| Surcharge procédurale | Une étape sans conséquence peut-elle être supprimée ? |
|---|---|
| Divergence texte/schéma | Les contrats humain et machine restent-ils alignés ? |
|---|---|

Ajouter un scénario spécifique si le risque dominant n’est couvert par aucun scénario existant.

Sortie

"RESISTANCE-RESULTS".

---

## 20. Phase 10 — Classer les constats

Classer les constats selon leur impact réel.

| Gravité | Définition |
|---|---|
| Bloquant | Contradiction, fausse preuve, risque critique, perte de contrôle ou comportement dangereux. |
|---|---|
| Majeur | Défaut pouvant faire échouer le système, créer une autorité concurrente ou produire régulièrement une mauvaise sortie. |
|---|---|
| Significatif | Défaut régulier de clarté, charge, frontière, exécution, accessibilité, adoption ou maintenance. |
|---|---|
| Mineur | Défaut éditorial ou ergonomique local à faible impact structurel. |
|---|---|
| Observation | Risque plausible ou opportunité sans preuve suffisante pour justifier une correction. |
|---|---|

Chaque constat comprend :

**ID:**
**TARGET:**
SECTION / INTERFACE:
**SCALE:**
**ROLE-CONCERNED:**
**PERSPECTIVE:**
**OBSERVED-BEHAVIOR:**
**EVIDENCE:**
**RISK-OF-NON-CORRECTION:**
**SEVERITY:**
**OWNER:**
**RECOMMENDATION:**
**DEPENDENCIES:**
**NON-REGRESSION-TEST:**
**DECISION:**

Un constat sans comportement observé ou risque formulable reste une observation, pas une obligation de patch.

---

## 21. Phase 11 — Décider s’il faut corriger

Avant toute correction, répondre :

| Question | Conséquence |
|---|---|
| Le défaut change-t-il une décision, création, preuve, exécution ou maintenance ? | Sinon, ne pas patcher. |
|---|---|
| Le fichier ciblé possède-t-il réellement ce défaut ? | Sinon, escalader. |
|---|---|
| Le gain dépasse-t-il la charge ajoutée ? | Sinon, simplifier ou conserver. |
|---|---|
| Le patch crée-t-il une nouvelle autorité ? | Vérifier la gouvernance. |
|---|---|
| Le patch est-il observable ou testable ? | Sinon, définir la preuve avant modification. |
|---|---|
| Le positif et le défensif restent-ils équilibrés ? | Sinon, reconcevoir. |
|---|---|
| Une suppression ou fusion résout-elle mieux le problème qu’un ajout ? | La préférer lorsqu’elle suffit. |
|---|---|

Corrections possibles :

- correction normative ;
- clarification ;
- fusion ;
- suppression ;
- déplacement ;
- simplification ;
- amélioration de façade ;
- capacité positive ;
- routing ;
- alignement humain/machine ;
- migration ;
- test ;
- validateur ;
- instrumentation.

Corrections interdites sans nécessité démontrée :

- règle supplémentaire par préférence ;
- gate concurrent ;
- score arbitraire ;
- quota universel ;
- exception destinée à éviter une décision ;
- catalogue remplaçant le jugement ;
- répétition sans fonction ;
- déplacement d’une preuve vers le mauvais propriétaire.

Sortie

"PATCH-DECISION".

---

## 22. Phase 12 — Appliquer la correction

Tout patch doit être :

- attribuable ;
- localisable ;
- lisible en diff ;
- cohérent ;
- réversible ;
- testable ;
- compatible avec les consommateurs ;
- proportionné ;
- documenté.

Le patch peut modifier plusieurs fichiers dans un même cycle uniquement lorsque :

1. un propriétaire principal porte la décision ;
2. les autres fichiers sont des consommateurs ou dérivés directement concernés ;
3. la modification commune est nécessaire à la cohérence ou à la non-régression.

Après patch :

relire au minimum la zone corrigée, ses interfaces amont et aval, puis réévaluer les constats touchés.

Pour une source normative à fort blast radius, relire le fichier complet.

Sortie

"PATCH + DIFF-REASONING".

---

## 23. Phase 13 — Valider

La validation possède cinq couches.

### 13.1 Validation textuelle

Vérifier :

- hiérarchie ;
- titres ;
- liens ;
- routes ;
- termes ;
- statuts ;
- tableaux ;
- blocs machine ;
- alias ;
- contradictions.

### 13.2 Validation contractuelle

Vérifier :

- obligations ;
- preuves ;
- sorties ;
- escalades ;
- responsabilités ;
- non-goals ;
- interfaces.

### 13.3 Validation machine

Lorsque disponible :

- schémas ;
- fixtures ;
- validateurs ;
- scripts ;
- build ;
- compilation ;
- identifiants ;
- export.

### 13.4 Validation de distribution

Vérifier :

- source ;
- exports ;
- packages ;
- hashes ;
- versions ;
- archives ;
- reproductibilité.

### 13.5 Validation de non-régression

Rejouer les contrôles qui couvrent :

- le défaut corrigé ;
- la frontière modifiée ;
- les consumers touchés ;
- les scénarios de résistance concernés.

«Une validation verte qui ne teste pas le risque corrigé n’est pas une preuve suffisante.»

Sortie

"VALIDATION-RESULT".

---

## 24. Phase 14 — Clôturer

L’audit peut être clôturé lorsqu’il est possible de retrouver :

- cible ;
- source ;
- propriétaire ;
- baseline ;
- couverture des phases ;
- couverture des perspectives ;
- tests de résistance ;
- constats ;
- décisions de patch ;
- validations ;
- réserves ;
- prochaine preuve ;
- condition de sortie.

Statuts d’audit

Ces statuts appartiennent uniquement au protocole d’audit.

| Statut | Signification |
|---|---|
| AUDIT-PASS | Aucun défaut significatif restant dans le scope examiné. |
|---|---|
| AUDIT-PASS-WITH-RESERVATION | La cible peut être conservée mais certaines limites restent explicitement ouvertes. |
|---|---|
| AUDIT-RETURN | Une correction requise reste incomplète ou non validée. |
|---|---|
| AUDIT-NOT-VERIFIED | Une preuve essentielle manque pour conclure. |
|---|---|
| AUDIT-EXPLORATORY | L’analyse reste volontairement exploratoire. |
|---|---|

Ils ne remplacent jamais les statuts ou verdicts internes de Design Governance.

---

## 25. Matrice de couverture obligatoire

Chaque audit conserve une matrice compacte.

PHASE 0  PREPARE            — LIGHT / TARGETED / FULL / N/A / ESCALATED
PHASE 1  BASELINE           — ...
PHASE 2  READING            — ...
PHASE 3  ROLES              — ...
PHASE 4  CONTRACTS          — ...
PHASE 5  INFORMATION-ARCH   — ...
PHASE 6  POSITIVE-CAPACITY  — ...
PHASE 7  LOOPS              — ...
PHASE 8  PERSPECTIVES       — ...
PHASE 9  RESISTANCE         — ...
PHASE 10 FINDINGS           — ...
PHASE 11 PATCH-DECISION     — ...
PHASE 12 PATCH              — ...
PHASE 13 VALIDATION         — ...
PHASE 14 CLOSURE            — ...

Pour les phases "N/A-JUSTIFIED", conserver une justification courte.

Pour les phases "ESCALATED", conserver :

- nouvelle cible ;
- owner ;
- raison ;
- prochaine preuve.

Cette matrice permet de vérifier que rien n’a été simplement oublié.

---

## 26. Audit intra-fichier, inter-fichiers et système

Une campagne complète ne s’arrête pas après les audits de fichiers.

Elle comporte idéalement trois niveaux.

Niveau A — Contrats locaux

Auditer les propriétaires principaux.

Exemples :

- "DIRECTION";
- "ACTION";
- "SAVOIR";
- "BIBLIOTHEQUE";
- "CHANGELOG".

Niveau B — Interfaces

Auditer les relations critiques.

Exemples :

- DIRECTION → ACTION ;
- DIRECTION → SAVOIR ;
- DIRECTION → BIBLIOTHEQUE ;
- ACTION → RUN_CARD ;
- documents → schémas ;
- schémas → validateurs ;
- sources → distributions.

Niveau C — Système

Tester des parcours complets.

Exemples :

- brief vague → premier objet ;
- correctif local ;
- nouvelle surface produit ;
- direction identitaire ;
- modification de composant partagé ;
- run avec preuve absente ;
- migration ;
- one-shot ;
- double boucle ;
- handoff agentique.

Une architecture peut être correcte localement mais échouer globalement.

L’audit système est donc obligatoire avant de conclure sur l’efficacité du corpus entier.

---

## 27. Ordre recommandé d’une campagne de stabilisation initiale

Cet ordre est recommandé pour une campagne de stabilisation, mais n’est pas le seul parcours autorisé par le protocole.

1. sources normatives propriétaires ;
2. interfaces entre ces propriétaires ;
3. schémas et validateurs ;
4. façades d’activation ;
5. documents de lecture ;
6. mémoire, migration et release ;
7. distributions ;
8. audit système ;
9. micro-runs instrumentés ;
10. pilotes réels ;
11. audit d’efficacité.

Un problème découvert à une étape peut rouvrir une étape précédente.

Un fichier suivant ne doit jamais masquer une réserve non résolue d’un propriétaire précédent.

---

## 28. Micro-runs et pilotes

Les audits documentaires ne suffisent pas à établir :

- adoption ;
- charge cognitive réelle ;
- temps de décision ;
- efficacité créative ;
- comportement réel des agents ;
- compréhension humaine ;
- qualité du premier rendu ;
- performance en situation.

Après stabilisation suffisante, utiliser deux niveaux.

Micro-runs contrôlés

Objectif :

tester très tôt les hypothèses importantes sans prétendre à une validation générale.

Exemples :

- temps jusqu’au premier objet jugeable ;
- nombre de modules réellement chargés ;
- erreurs de classification ;
- décisions inutiles ;
- répétitions ;
- confusion de taxonomies ;
- qualité du premier rendu ;
- correction réellement apportée.

Pilotes réels

Objectif :

tester le système sur plusieurs contextes suffisamment représentatifs.

Le pilote doit enregistrer :

- contexte ;
- version ;
- tâche ;
- mode ;
- artefacts ;
- observations ;
- difficultés ;
- changements ;
- limites.

Une réussite isolée ne devient jamais une preuve générale.

---

## 29. Signaux à mesurer pendant les runs

Selon la question étudiée :

- temps jusqu’à la première décision exploitable ;
- temps jusqu’au premier artefact jugeable ;
- nombre de fichiers réellement chargés ;
- nombre de routes réellement utilisées ;
- fréquence de reclassification ;
- fréquence de "N/A-JUSTIFIED";
- fréquence de "NOT-VERIFIED";
- premier défaut dominant ;
- type de correction effectuée ;
- correction modifiant réellement l’artefact ;
- régression introduite ;
- preuve manquante ;
- confusion terminologique ;
- modules rarement utiles ;
- modules systématiquement contournés ;
- qualité perçue par plusieurs reviewers ;
- adoption ;
- coût cognitif ;
- différence avec une baseline sans le protocole.

Ces données servent à améliorer le système.

Elles ne deviennent pas automatiquement des scores de qualité.

---

## 30. Artéfacts d’audit

Le protocole ne doit pas produire artificiellement un fichier par étape.

Dossier consolidé par défaut

Un seul document peut contenir :

1. cadrage ;
2. baseline ;
3. lecture sectionnelle ;
4. rôles ;
5. contrats ;
6. architecture ;
7. capacité positive ;
8. perspectives ;
9. résistance ;
10. constats ;
11. patch ;
12. validation ;
13. clôture.

Séparer uniquement lorsque nécessaire

Créer des artefacts indépendants lorsque :

- un script les consomme ;
- une équipe différente en est propriétaire ;
- un reviewer doit les signer séparément ;
- une preuve doit être archivée ;
- un diff doit être isolé ;
- une distribution doit être comparée ;
- un volume important rend le dossier consolidé impraticable.

Exemples possibles :

<FILE>_AUDIT.md
<FILE>_BASELINE.json
<FILE>_DIFF.md
<FILE>_VALIDATION.txt
<SYSTEM>_INTERFACE_AUDIT.md
<SYSTEM>_PILOT_RESULTS.md

Le nombre de fichiers produits n’est jamais une mesure de profondeur.

---

## 31. Rapport minimal de clôture

**AUDIT-ID:**
**TARGET:**
**SCALE:**
**PROFILE:**
**OWNER:**
ROLE:
**CANONICAL-SOURCE:**
**SCOPE:**
**BASELINE:**
**PHASE-COVERAGE:**
**PERSPECTIVES-COVERED:**
**RESISTANCE-TESTS:**
**FINDINGS:**
**PATCH-DECISION:**
**FILES-CHANGED:**
**VALIDATION:**
**DISTRIBUTION-ALIGNMENT:**
**STATUS:**
**RESERVATIONS:**
**NEXT-PROOF:**
**NEXT-TARGET:**
**EXIT-CONDITION:**

Le rapport peut être rédigé en prose.

Ces éléments doivent simplement rester retrouvables.

---

## 32. Protection contre la bureaucratisation

À la fin de chaque audit, poser également ces questions.

1. Quelle étape a réellement changé une décision ?
2. Quelle étape n’a produit aucune information nouvelle ?
3. Quel champ n’a jamais influencé le diagnostic ?
4. Quelle perspective a été systématiquement "N/A" ?
5. Quel contrôle pourrait être automatisé ?
6. Quel artefact pourrait être fusionné ?
7. Quelle règle du protocole a été difficile à appliquer ?
8. Quelle ambiguïté du protocole lui-même a été révélée ?
9. L’audit a-t-il amélioré la cible davantage qu’il n’a augmenté sa complexité ?
10. Referions-nous cette étape lors d’un prochain audit similaire ?

Le protocole lui-même doit pouvoir être simplifié sur la base de ses usages réels.

---

## 33. Critère final de qualité d’un audit

Un audit est réussi lorsqu’il permet de répondre clairement aux questions suivantes :

1. Quelle cible a réellement été auditée ?
2. Quelle source possède le contrat ?
3. Quelle décision cette cible doit-elle permettre ?
4. Qui la consomme ?
5. Quel risque une mauvaise interprétation crée-t-elle ?
6. Quelle capacité positive rend-elle possible ?
7. Quelle preuve soutient les conclusions ?
8. Quelles limites restent non vérifiées ?
9. Où se trouvent les principales frontières ?
10. Le chemin de lecture réel est-il compréhensible ?
11. Le premier objet ou résultat attendu peut-il réellement être produit ?
12. Que se passe-t-il lorsqu’il échoue ?
13. La double boucle modifie-t-elle réellement quelque chose ?
14. Le one-shot peut-il être accepté honnêtement ?
15. Le système résiste-t-il aux scénarios critiques applicables ?
16. Quels constats sont prouvés ?
17. Lesquels restent des observations ?
18. Quelle correction apporte plus de valeur que de charge ?
19. Quelle validation couvre réellement le risque corrigé ?
20. Quel propriétaire reçoit les réserves ?
21. Quelle prochaine preuve réduira l’incertitude ?
22. L’audit a-t-il lui-même introduit une complexité inutile ?

---

## 34. Critère final de qualité du protocole

Le protocole est réussi s’il permet :

- d’être rigoureux sans devenir mécanique ;
- de considérer toutes les dimensions sans approfondir artificiellement chacune ;
- de détecter des défauts locaux et systémiques ;
- de distinguer contrat et efficacité ;
- de protéger les responsabilités ;
- d’améliorer les capacités positives ;
- de tester les limites ;
- de corriger seulement ce qui mérite réellement une correction ;
- de prouver la non-régression ;
- d’apprendre de ses propres audits.

«Conclusion : auditer complètement ne signifie ni tout approfondir, ni tout documenter, ni tout corriger. Cela signifie ne laisser aucune dimension importante disparaître silencieusement, augmenter la profondeur lorsqu’un risque le justifie, réduire la profondeur lorsqu’elle n’apporte plus d’information, et relier chaque conclusion à une observation, une décision, un propriétaire, une limite et une prochaine preuve.»
