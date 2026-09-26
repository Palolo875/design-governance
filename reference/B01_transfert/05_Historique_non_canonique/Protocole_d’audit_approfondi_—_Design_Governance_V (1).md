# Protocole d’audit approfondi — Design Governance V1

**Version :** 1.0  
**Statut :** protocole de référence pour les audits proportionnés, avec un niveau approfondi pour les fichiers à haut risque  
**Périmètre :** fichiers normatifs, façades d’activation, schémas, validateurs, artefacts de distribution et documents de mémoire  
**Principe d’exécution :** un propriétaire de décision à la fois ; plan → baseline → lecture complète proportionnée → audit → décision → correction éventuelle → validation → clôture. Les artefacts dérivés et tests directement nécessaires peuvent être alignés dans le même cycle, sans devenir de nouvelles sources d’autorité.

---

## 1. Finalité

Ce protocole sert à vérifier qu’un fichier du système est suffisamment clair, cohérent, exploitable et robuste pour contribuer à une production de design de haute qualité, y compris dès le premier rendu ou dans une stratégie one-shot, tout en restant compatible avec une boucle d’apprentissage rigoureuse.

L’audit ne cherche pas seulement à réduire le slop. Il vérifie aussi la capacité positive du système à produire une direction perceptible, une composition maîtrisée, une structure habitable, une expérience utilisable, une preuve honnête et une maintenance soutenable.

L’objectif n’est pas de rendre chaque fichier plus long. Une correction est valable seulement si elle améliore une décision, une création, une preuve, une exécution, une coordination, une protection ou une capacité de maintenance sans créer une contradiction supérieure.

> **Règle centrale :** aucun fichier n’est déclaré meilleur parce qu’il contient davantage de règles. Il est meilleur lorsqu’il rend une bonne décision plus probable, une bonne création plus concrète, une preuve plus honnête ou une erreur plus difficile à commettre.

## 2. Profils d’audit et règle de proportionnalité

Le protocole décrit le niveau **DEEP**, réservé aux contrats normatifs, aux changements de gouvernance, aux schémas critiques et aux fichiers dont le défaut pourrait produire un risque important ou un blast radius partagé. Il ne doit pas être appliqué intégralement à chaque fichier par défaut.

Le profil est choisi après une première estimation du risque, du nombre de consommateurs, de l’autorité du fichier et du coût d’une erreur. Le profil peut être augmenté si une résistance révèle un risque supérieur. Il ne peut pas être réduit uniquement pour accélérer un travail alors qu’un risque critique reste non protégé.

| Profil | Quand l’utiliser | Couverture minimale | Sortie attendue |
|---|---|---|---|
| **LITE** | Fichier local, faible risque, changement éditorial ou correction sans changement de contrat | Baseline courte, lecture complète, propriétaire, décision, dépendances, constat, test ciblé et validation concernée | Rapport court, diff éventuel, validation et prochaine preuve si nécessaire |
| **STANDARD** | Fichier opérationnel, façade d’activation, guide partagé ou contrat consommé par plusieurs lecteurs | Baseline, rôles essentiels, contrats d’entrée et de sortie, perspectives applicables, scénarios ciblés, non-régression et alignement des dérivés | Rapport de clôture structuré, diff éventuel, validations et réserves |
| **DEEP** | Source normative, schéma ou validateur critique, changement de gouvernance, risque critique ou blast radius élevé | Toutes les phases du présent protocole, avec les perspectives et scénarios applicables justifiés | Dossier complet d’audit, validation de distribution, réserves gouvernées et prochaine preuve |

Un audit **LITE** ou **STANDARD** ne dispense jamais de déclarer la source canonique, le propriétaire, le risque, la décision, la preuve attendue et les limites. La profondeur varie ; la vérité de la preuve et la protection du risque ne varient pas.

### Deux objectifs à ne pas confondre

Le protocole distingue deux familles de conclusions :

- **Audit de contrat :** le fichier est-il cohérent, lisible, compatible, testable et correctement relié à ses propriétaires ?
- **Audit d’efficacité :** le fichier améliore-t-il effectivement une décision, une création, une preuve, une coordination ou un résultat observé dans un contexte réel ?

Un audit documentaire peut établir une conclusion de contrat sans établir une conclusion d’efficacité. Une conclusion d’efficacité exige une observation de run, un artefact ou une comparaison dans le scope déclaré. Aucun statut d’audit ne doit transformer une cohérence documentaire en preuve de résultat.

---

## 3. Principes non négociables

### 3.1 Un propriétaire de décision à la fois

Un seul fichier propriétaire porte la décision normative active pendant un cycle. Les autres fichiers peuvent être consultés pour vérifier les frontières, les consommateurs, les dépendances et les contradictions. Les artefacts dérivés, fixtures, validateurs et distributions peuvent être alignés dans le même cycle lorsqu’ils sont directement nécessaires à la compatibilité ou à la non-régression. Ils restent des surfaces d’alignement et ne deviennent pas des sources d’autorité.

Cette règle évite de corriger simultanément plusieurs contrats sans savoir lequel est responsable d’un changement, tout en permettant de livrer une modification cohérente lorsque le contrat propriétaire et ses consommateurs doivent rester synchronisés.

### 3.2 Aucun patch avant le diagnostic

La formulation d’un défaut, sa gravité, son propriétaire, son impact et son test de non-régression doivent être établis avant toute modification. Une amélioration stylistique plausible ne suffit pas à justifier un patch.

### 3.3 La source canonique prime

L’audit commence par identifier la source de vérité du fichier. Les copies distribuées, baselines, exports, archives et extraits historiques servent à détecter les divergences, mais aucune copie dérivée ne doit être corrigée à la place de la source propriétaire.

### 3.4 Le positif et le défensif sont indissociables

Chaque audit examine à la fois :

- ce que le système empêche ;
- ce qu’il permet de créer ;
- ce qu’il rend observable ;
- ce qu’il permet de décider ;
- ce qu’il rend maintenable ;
- ce qu’il risque d’homogénéiser ou de bureaucratiser.

La qualité visuelle, la spécificité, la présence, la hiérarchie, la matière, la typographie, les états, la preuve et le polish sont considérés comme des capacités de production, pas comme des effets secondaires du contrôle.

### 3.5 Une justification n’est pas une preuve

Une rationale, une intention, un nom de route, une capacité disponible, une capture isolée ou une conformité textuelle ne suffit pas à établir un résultat. L’audit doit distinguer intention, construction, observation, interprétation, preuve et verdict.

### 3.6 Les exceptions restent explicites

Une réduction de portée, une absence de preuve, un héritage, une route non sélectionnée, un `N/A-JUSTIFIED`, un `NOT-VERIFIED`, un `RETURN`, un `FAIL-ASSUMED` ou une réservation ne doivent jamais être implicites.

---

## 4. Unité d’audit

Chaque cycle porte sur un **fichier propriétaire cible** et, lorsque nécessaire, sur une surface d’alignement dérivée. Il produit au minimum :

1. une baseline vérifiable ;
2. un plan spécifique au fichier ;
3. un audit sectionnel ;
4. un diagnostic de rôles, lecteurs et contrats ;
5. une liste de constats classés ;
6. une décision de correction ou de non-correction ;
7. un diff ou une justification de conservation ;
8. une validation complète ;
9. un rapport de clôture ;
10. une prochaine étape clairement bornée.

Une section interne peut être traitée comme sous-unité, mais elle reste rattachée au contrat global du fichier. Un artefact dérivé peut être modifié dans le même cycle uniquement pour refléter la décision du propriétaire, satisfaire un test ou régénérer une distribution ; la décision et sa justification restent dans le fichier propriétaire.

---

## 5. Phase 0 — Préparer le cycle

Avant de lire ou modifier le fichier, établir une fiche de cadrage :

| Champ | Question à établir |
|---|---|
| `TARGET` | Quel fichier exact est audité ? |
| `CANONICAL-PATH` | Où se trouve la source propriétaire ? |
| `DOCUMENT-ROLE` | Quel contrat ce fichier possède-t-il ? |
| `CONSUMERS` | Quels fichiers, outils, agents ou équipes le consomment ? |
| `DEPENDENCIES` | De quelles autorités dépend-il ? |
| `NON-GOALS` | Que ne doit pas posséder ce fichier ? |
| `SCOPE` | Quelles sections et surfaces sont couvertes ? |
| `RISK` | Quel dommage une mauvaise interprétation pourrait-elle produire ? |
| `EXIT-CONDITION` | Qu’est-ce qui permettra de déclarer l’audit terminé ? |

Lire ensuite les instructions applicables, notamment le protocole d’audit, la taxonomie des rôles, les règles de rédaction et les compétences spécifiques au type d’artefact.

---

## 6. Phase 1 — Établir la baseline

La baseline doit être produite à partir de la source canonique actuelle, avant toute correction.

### 6.1 Mesures minimales

Capturer :

- chemin absolu ;
- date ou identifiant de l’audit ;
- hash SHA-256 ;
- nombre de lignes et d’octets ;
- encodage et fin de ligne si pertinent ;
- structure des titres ;
- tableaux, blocs de code, tags et identifiants ;
- liens internes et externes ;
- références croisées ;
- statuts, modes, routes, champs et valeurs machine ;
- copie distribuée correspondante ;
- baseline historique et extrait original lorsqu’ils existent.

### 6.2 Questions de baseline

1. La source canonique est-elle identifiable sans ambiguïté ?
2. Les copies distribuées correspondent-elles à la source ?
3. La baseline historique est-elle réellement comparable ou déjà obsolète ?
4. Le fichier est-il modifié localement avant l’audit ?
5. Existe-t-il des fichiers générés qui doivent être régénérés plutôt que patchés ?
6. Une divergence est-elle normative, documentaire, générée ou historique ?

### 6.3 Règle de divergence

Une divergence entre baseline et source actuelle n’est pas automatiquement un défaut du fichier. Elle doit être classée comme :

- divergence de source ;
- divergence de distribution ;
- divergence de baseline ;
- divergence de schéma ;
- divergence de documentation ;
- changement attendu lié à une refonte antérieure.

---

## 7. Phase 2 — Lire le fichier entièrement

La lecture est complète avant le diagnostic final. Elle se fait en quatre passages complémentaires.

### Passage A — Architecture visible

Relever les titres, la hiérarchie, les façades, les chemins courts, les tables de routing, les tags d’autorité, les blocs de code, les tests de sortie et les renvois.

### Passage B — Contrat sémantique

Pour chaque section, identifier ce qu’elle définit, ce qu’elle conseille, ce qu’elle interdit, ce qu’elle mesure, ce qu’elle laisse ouvert et vers qui elle renvoie.

### Passage C — Usage réel

Simuler la lecture par les utilisateurs principaux : agent, designer, reviewer, équipe produit, intégrateur, mainteneur et système automatique. Vérifier le premier chemin que chacun suivrait sous contrainte de temps.

### Passage D — Résistance

Chercher les ambiguïtés, contradictions, routes concurrentes, formulations contournables, obligations sans preuve, champs sans effet, doublons, exceptions silencieuses et sorties qui rassurent sans changer une décision.

Aucune conclusion ne doit être tirée à partir de la seule façade ou d’un extrait.

---

## 8. Phase 3 — Cartographier les rôles

Chaque fichier et chaque section sont analysés avec les neuf rôles suivants.

| Rôle | Question obligatoire |
|---|---|
| **Propriété** | Qui a l’autorité de définir et modifier ce contrat ? |
| **Décision** | Quelle décision ce fichier aide-t-il à prendre ? |
| **Exécution** | Qui transforme cette décision en artefact, sélection, observation ou trace ? |
| **Preuve** | Que peut-on affirmer, avec quelle observation, portée, date et limite ? |
| **Jugement** | Qui interprète qualité, pertinence, composition, structure ou risque ? |
| **Coordination** | Qui orchestre chargement, handoff, séquence et escalade ? |
| **Lecture** | Quels lecteurs utilisent quelle partie, dans quel ordre ? |
| **Mémoire** | Quelles décisions, versions, migrations et limites sont conservées ? |
| **Garde-fou** | Quelle réduction silencieuse du mode, risque, preuve ou autorité est empêchée ? |

Ajouter systématiquement : `INPUT`, `OUTPUT`, `ESCALATION`, `NON-GOAL`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`.

Une section est suspecte lorsque son propriétaire, sa décision ou sa sortie ne peuvent pas être formulés en une phrase concrète.

---

## 9. Phase 4 — Auditer les contrats

Pour chaque fichier, vérifier les contrats suivants.

### 9.1 Contrat de responsabilité

Le fichier dit-il clairement ce qu’il possède et ce qu’il ne possède pas ? Ses frontières avec les autres propriétaires sont-elles explicites ?

### 9.2 Contrat d’entrée

Le fichier précise-t-il les informations nécessaires, les hypothèses acceptables, les risques et les données manquantes ?

### 9.3 Contrat de transformation

Le lecteur sait-il comment passer de l’entrée à une décision, un artefact, une observation ou une trace ?

### 9.4 Contrat de sortie

La sortie est-elle concrète, persistante, lisible et exploitable par le prochain propriétaire ?

### 9.5 Contrat de preuve

La preuve attendue est-elle adaptée au claim, au support, au scope, au risque, au moment et aux limites ?

### 9.6 Contrat d’escalade

Que se passe-t-il si l’information manque, si le risque augmente, si le rendu échoue, si l’action sort du périmètre ou si une autre autorité doit décider ?

### 9.7 Contrat de mémoire

Les décisions, changements, migrations, réserves, dates de revue et apprentissages sont-ils conservés au bon endroit sans devenir une règle active concurrente ?

---

## 10. Phase 5 — Audit de l’architecture de l’information

Vérifier l’ordre de l’information dans le fichier lui-même.

### 10.1 Façade

Le lecteur comprend-il rapidement :

1. le rôle du fichier ;
2. la capacité positive qu’il libère ;
3. le risque ou la décision dominante ;
4. le premier chemin à suivre ;
5. le propriétaire suivant ou la prochaine preuve ?

### 10.2 Hiérarchie

Les éléments nécessaires à l’action précèdent-ils les détails spécialisés ? Les absolus, contrats, routes, exemples et annexes sont-ils placés au bon niveau ?

### 10.3 Chargement conditionnel

Le fichier distingue-t-il le noyau commun des modules activés seulement selon le mode, le risque, le médium, la décision ou le blast radius ?

### 10.4 Navigation

Les renvois sont-ils bidirectionnels lorsque nécessaire, précis, non ambigus et exempts de routes obsolètes ?

### 10.5 Charge cognitive

Le fichier peut-il être utilisé sans charger tout le corpus ? Les tableaux réduisent-ils réellement l’effort de lecture ? Les répétitions ajoutent-elles une protection ou seulement du volume ?

### 10.6 Façade contre source

Les façades résument-elles correctement la source sans créer une obligation ou un verdict concurrent ?

---

## 11. Phase 6 — Audit de la capacité positive

La question n’est pas seulement « que bloque le fichier ? », mais aussi « que permet-il de produire de meilleur ? ».

Selon le type de fichier, vérifier les dimensions suivantes :

| Dimension positive | Question |
|---|---|
| **Présence** | Le système favorise-t-il une première perception forte et juste ? |
| **Point de vue** | Les choix expriment-ils une position plutôt qu’une application mécanique ? |
| **Spécificité** | Le résultat appartient-il réellement au produit, au public et au contexte ? |
| **Composition** | Les masses, vides, axes, échelles, foyers et rythmes sont-ils gouvernables ? |
| **Matière et type** | Les assets, la typographie, la texture, la lumière ou le code servent-ils une relation réelle ? |
| **Désirabilité** | Le résultat donne-t-il envie de comprendre, d’entrer ou de poursuivre sans manipulation ? |
| **Résolution** | Les détails, états, microcopies, responsive et transitions tiennent-ils l’idée ? |
| **Retenue** | Le système sait-il retirer ce qui n’ajoute rien ? |
| **Habitabilité** | Le premier objet est-il suffisamment complet pour être regardé et jugé ? |
| **Transfert** | La décision survit-elle au runtime, au mobile, au contenu réel et aux états critiques ? |

Un système qui ne contient que des défenses anti-slop est incomplet, même s’il est rigoureux sur les gates.

---

## 12. Phase 7 — Audit de la double boucle et du one-shot

Vérifier que le fichier s’insère dans une boucle cohérente sans inventer une boucle concurrente.

### Boucle créative

La boucle créative doit pouvoir suivre :

> **comprendre → ouvrir → choisir → composer → produire → observer → améliorer ou confirmer**

Elle doit préserver la divergence utile, la qualité du premier rendu et la capacité à arrêter lorsqu’aucun gain réel n’est attendu.

### Boucle de gouvernance

La boucle de gouvernance doit pouvoir suivre :

> **classer → définir le risque → choisir la route → déclarer la preuve → exécuter → vérifier → décider → persister ou escalader**

### One-shot

Le one-shot est une stratégie de préparation forte suivie d’une observation réelle. Il n’est pas une exemption de jugement, de preuve ou de contrôle.

Le fichier doit permettre de répondre à trois questions :

1. Qu’est-ce qui devait tenir dès le premier rendu ?
2. Qu’a-t-on réellement observé ?
3. Pourquoi une correction supplémentaire promet-elle ou non un gain réel ?

### Double boucle

Toute itération valide doit modifier l’artefact, la décision, la preuve ou la portée. Une nouvelle rationale, une nouvelle étiquette, une variante nominale ou une route supplémentaire ne constitue pas une amélioration en soi.

---

## 13. Phase 8 — Audit multi-perspectives applicable

Le profil **DEEP** et, lorsque le risque le justifie, le profil **STANDARD** évaluent le fichier depuis les perspectives applicables à son rôle, à ses consommateurs et à son risque. Une perspective non retenue doit être marquée `N/A-JUSTIFIED` avec une justification brève ; elle ne doit pas être examinée mécaniquement.

1. **Création visuelle :** direction, présence, composition, matière, typographie, assets, polish et diversité.
2. **Produit et usage :** JTBD, décision dominante, action, contenu réel, confiance et récupération.
3. **Accessibilité et inclusion :** clavier, focus, contraste, sémantique, alternatives, reflow, motion, capacité et contexte.
4. **Contenu et communication :** vérité, longueur, localisation, ton, états, ambiguïtés et conséquences.
5. **Technique et runtime :** code, compatibilité, performance, fallback, erreurs, observabilité et maintien.
6. **Preuve et épistémologie :** claim, méthode, artefact, scope, date, fraîcheur, limite et extrapolation.
7. **Agentique :** activation, choix de route, coût cognitif, contournement, exécution et transmission.
8. **Équipe :** compréhension, handoff, rôles, collaboration, revue et adoption.
9. **Gouvernance :** ownership, statuts, exceptions, migrations, conflits et autorité.
10. **Production et opérations :** versionnement, rollback, confidentialité, permissions, changement substantiel, maintenance et péremption.
11. **Expérimentation :** hypothèse, baseline, mesure, contexte, limite, apprentissage et promotion.
12. **Migration :** compatibilité avec les anciens aliases, anciennes routes, artefacts et versions distribuées.

---

## 14. Phase 9 — Tests de résistance

Le profil **DEEP** confronte le fichier aux scénarios applicables ci-dessous. Le profil **STANDARD** en sélectionne au moins ceux qui couvrent le risque dominant, les consommateurs et les frontières touchées. Le profil **LITE** rejoue au minimum le scénario directement lié au défaut corrigé.

| Scénario | Question de résistance |
|---|---|
| Brief vague | Le système formule-t-il une hypothèse et une prochaine preuve sans inventer le contexte ? |
| One-shot | Le premier rendu peut-il être suffisamment fort, complet et observable ? |
| Correction locale | Le système évite-t-il de reconstruire inutilement toute la surface ? |
| Direction identitaire | La singularité, l’ancrage et la composition sont-ils réellement traités ? |
| Surface opérationnelle | La hiérarchie, l’action, les états et la récupération restent-ils prioritaires ? |
| Composant partagé | Le blast radius, les consumers et la migration sont-ils déclarés ? |
| Contenu long | Le design recompose-t-il au lieu de casser ou tronquer silencieusement ? |
| Mobile | La priorité, le voisinage, le rythme, l’action et l’état survivent-ils ? |
| État critique | L’erreur, la permission, l’indisponibilité ou le succès modifient-ils la structure si nécessaire ? |
| Asset absent | Le résultat tient-il avec contenu, type, donnée, espace et forme ? |
| Référence séduisante | La relation est-elle transformée plutôt que copiée ? |
| Style recyclé | Le système challenge-t-il le réemploi par confort ? |
| Accessibilité tardive | L’accessibilité peut-elle modifier la décision assez tôt ? |
| Runtime différent | Le prototype est-il vérifié dans le runtime déclaré ? |
| Preuve absente | Le système déclare-t-il `NOT-VERIFIED` au lieu d’inventer un PASS ? |
| Action externe | Les droits, permissions, confidentialité et confirmation requise sont-ils respectés ? |
| Changement post-verdict | La fraîcheur, la réouverture et la responsabilité sont-elles claires ? |
| Migration | Les anciens identifiants sont-ils dépréciés sans redevenir actifs ? |
| Surcharge procédurale | Une étape qui ne change rien peut-elle être retirée ou justifiée ? |
| Divergence texte/schéma | Les contrats humains et machine restent-ils alignés ? |

---

## 15. Phase 10 — Classer les constats

Chaque constat est classé selon son impact, et non selon sa visibilité éditoriale.

| Niveau | Définition | Traitement |
|---|---|---|
| **Bloquant** | Contradiction, fausse preuve, risque critique non protégé, perte de contrôle ou comportement dangereux en production. | Correction obligatoire avant clôture. |
| **Majeur** | Défaut susceptible de faire échouer le système, produire une sortie générique, créer une autorité concurrente ou rendre une décision non gouvernable. | Correction obligatoire ou justification exceptionnelle documentée. |
| **Significatif** | Défaut régulier de clarté, charge, frontière, exécution, accessibilité ou adoption. | Correction recommandée dans le cycle actif. |
| **Mineur** | Défaut éditorial, navigationnel ou ergonomique sans conséquence structurelle importante. | Corriger si le coût est faible et le gain clair. |
| **Observation** | Risque plausible ou opportunité sans preuve suffisante pour justifier un patch. | Documenter et surveiller. |

Chaque constat doit contenir :

```text
ID
FICHIER
SECTION
ROLE-CONCERNE
PERSPECTIVE
COMPORTEMENT OBSERVE
RISQUE DE NON-CORRECTION
GRAVITE
PROPRIETAIRE
RECOMMANDATION
DEPENDANCES
TEST DE NON-REGRESSION
DECISION
```

---

## 16. Phase 11 — Décider s’il faut corriger

Avant un patch, appliquer la matrice de décision :

| Question | Si oui | Si non |
|---|---|---|
| Le défaut change-t-il une décision, une création, une preuve, une exécution ou une maintenance ? | Continuer l’analyse. | Ne pas patcher ; supprimer, fusionner ou observer. |
| Le fichier est-il le propriétaire du défaut ? | Préparer le patch local. | Escalader vers le propriétaire approprié. |
| Le gain est-il supérieur à la charge introduite ? | Continuer. | Préférer une façade, un outil ou une note de migration. |
| Le patch crée-t-il une nouvelle autorité, route, gate ou obligation ? | Vérifier la gouvernance globale. | Continuer. |
| Le patch est-il testable ? | Définir le test avant modification. | Ne pas appliquer sans critère observable. |
| Le patch conserve-t-il le positif et le défensif ? | Appliquer avec diff minimal. | Reconcevoir la correction. |

### Types de correction admis

- correction normative du contrat ;
- clarification de propriété ou de frontière ;
- réduction d’ambiguïté ;
- ajout d’une capacité positive manquante ;
- amélioration du chemin court ;
- correction de navigation ou de routing ;
- correction de cohérence machine/document ;
- mise à jour d’un artefact dérivé ;
- ajout d’un test ou d’un validateur ciblé ;
- correction de migration ou de dépréciation.

### Corrections interdites sans nécessité démontrée

- ajouter des règles parce qu’une formulation est esthétique ;
- créer un score de beauté ou de maturité non propriétaire ;
- ajouter un gate concurrent ;
- transformer une heuristique en obligation universelle ;
- créer des quotas de variantes, d’itérations ou de feedback ;
- déplacer une preuve ou un verdict vers le mauvais fichier ;
- ajouter un catalogue qui remplace le jugement ;
- multiplier les exceptions pour éviter une décision réelle.

---

## 17. Phase 12 — Appliquer le patch

Un patch doit être :

1. limité au fichier cible ou à l’artefact explicitement dérivé ;
2. lisible en diff ;
3. cohérent avec la hiérarchie existante ;
4. accompagné d’une intention claire ;
5. compatible avec les routes, statuts, schémas et renvois existants ;
6. réversible ;
7. testable ;
8. documenté dans le rapport d’audit.

Après le patch, relire le fichier entier ou, pour une modification très localisée, la section modifiée ainsi que ses interfaces amont et aval. Ne jamais supposer qu’un remplacement local conserve automatiquement la hiérarchie globale.

---

## 18. Phase 13 — Validation

La validation se fait en plusieurs niveaux.

### 18.1 Validation textuelle

- lecture complète post-patch ;
- titres et hiérarchie ;
- liens internes ;
- vocabulaire et statuts ;
- routes canoniques ;
- aliases dépréciés ;
- tableaux et blocs de code ;
- encodage et caractères suspects ;
- absence de contradiction avec les propriétaires voisins.

### 18.2 Validation de contrat

Vérifier que chaque sortie annoncée existe, que chaque obligation possède une preuve ou une justification, que chaque exception a une route, que chaque escalade possède un propriétaire et que chaque champ machine possède une signification stable.

### 18.3 Validation machine

Lorsque le dépôt le prévoit :

- validation JSON Schema ;
- validation des fixtures valides et invalides ;
- compilation des scripts ;
- validateurs documentaires ;
- vérification des routes et identifiants ;
- contrôle des exports ;
- build et reproductibilité.

### 18.4 Validation de distribution

Comparer les hashes de la source et des distributions attendues. Régénérer les exports lorsqu’ils sont dérivés. Vérifier les archives, le nombre de fichiers, les liens et l’intégrité des paquets.

### 18.5 Validation de non-régression

Rejouer au minimum les tests qui couvrent le défaut corrigé, les frontières touchées et les scénarios de résistance concernés. Une validation verte qui ne couvre pas le risque corrigé est insuffisante.

---

## 19. Phase 14 — Clôturer le fichier

Un fichier peut être clôturé seulement si les exigences de son profil sont satisfaites :

- sa source canonique est identifiée ;
- sa baseline est enregistrée ;
- il a été lu intégralement ;
- ses rôles, lecteurs, contrats et frontières sont documentés ;
- les perspectives obligatoires ont été couvertes ;
- les scénarios applicables ont été testés ;
- les constats sont classés ;
- chaque correction est justifiée ou explicitement refusée ;
- le fichier canonique et ses distributions sont alignés ;
- la validation complète est passée ;
- les réserves restantes ont un owner et une prochaine preuve ;
- la prochaine étape ne modifie pas rétroactivement le fichier clôturé.

### Statuts de clôture

| Statut | Signification |
|---|---|
| **`CLOSED / PASS`** | Aucun défaut résiduel significatif ou majeur identifié dans le périmètre. |
| **`CLOSED / PASS-WITH-RESERVATION`** | Le fichier est stable, mais des réserves documentées restent hors du patch actif. |
| **`RETURN`** | Une correction nécessaire n’a pas encore été appliquée ou validée. |
| **`NOT-VERIFIED`** | Une preuve essentielle manque pour conclure. |
| **`EXPLORATORY`** | Le fichier ou le contrat reste expérimental et ne doit pas être présenté comme stabilisé. |

Le statut d’audit ne doit pas être confondu avec un verdict de run, un statut de route, un statut de release ou un statut utilisateur.

---

## 20. Artefacts obligatoires par fichier

Le cycle complet doit produire, selon le besoin :

| Artefact | Fonction |
|---|---|
| `<FILE>_DEEP_AUDIT_PLAN.md` | Plan spécifique avant lecture et correction. |
| `<FILE>_BASELINE_CURRENT.md` | Hash, taille, structure et invariants de la source actuelle. |
| `<FILE>_SECTION_CONTENT_AUDIT.md` | Lecture et diagnostic section par section. |
| `<FILE>_ROLE_READER_CONTRACT_DIAGNOSTIC.md` | Rôles, lecteurs, contrats, frontières et réserves. |
| `<FILE>_DIFF.md` | Diff raisonné lorsque le fichier est modifié. |
| `<FILE>_FINAL_VALIDATION.txt` | Résultat des validations exécutées. |
| `<FILE>_CLOSURE.md` | Décision finale, réserves, owner, prochaine preuve et statut. |

Les fichiers créés doivent être complets, vérifiés, non tronqués et attachés avec leur chemin absolu lorsqu’ils sont livrés à l’utilisateur.

---

## 21. Format minimal du rapport de clôture

```text
TARGET:
OWNER:
ROLE:
SCOPE:
BASELINE:
READING-COMPLETE:
PERSPECTIVES-COVERED:
RESISTANCE-TESTS:
FINDINGS:
PATCH-DECISION:
FILES-CHANGED:
VALIDATION:
DISTRIBUTION-ALIGNMENT:
STATUS:
RESERVATIONS:
NEXT-PROOF:
NEXT-FILE:
EXIT-CONDITION:
```

Le rapport peut être rédigé en prose et tableaux, mais doit permettre de retrouver ces éléments sans interprétation supplémentaire.

---

## 22. Choisir le profil avant de choisir la profondeur

Le profil est une décision d’audit, pas un nouveau mode de Design Governance V1. Pour le choisir, considérer dans cet ordre :

1. le risque d’une mauvaise interprétation ou d’une fausse preuve ;
2. l’autorité du fichier et le nombre de consommateurs ;
3. le blast radius d’un changement ;
4. la présence d’un schéma, d’un validateur, d’une migration ou d’une distribution ;
5. le coût d’une erreur comparé au coût de l’audit.

Si l’un de ces signaux indique un risque critique, utiliser **DEEP** ou obtenir une décision explicite de ne pas conclure. Si aucun signal ne le justifie, utiliser le profil le plus léger qui couvre réellement le défaut et sa non-régression. La réduction de profondeur doit être visible dans le rapport et ne doit jamais transformer une preuve absente en preuve acquise.

## 23. Règle de progression globale

L’ordre global recommandé est :

1. fichiers normatifs propriétaires, en profil **DEEP** ;
2. schémas et validateurs qui matérialisent leurs contrats, en profil **DEEP** ou **STANDARD** selon le blast radius ;
3. façades d’activation et documents de lecture ;
4. artefacts de mémoire, migration et release ;
5. distributions et paquets finaux ;
6. runs réels seulement après stabilisation de l’architecture.

Un fichier suivant ne doit pas être utilisé pour masquer une réserve du fichier précédent. Une réserve peut être reportée, mais elle doit rester enregistrée avec son propriétaire et sa prochaine preuve.

Les runs réels sont une phase distincte. Ils servent à tester le système stabilisé dans des contextes réels ; ils ne doivent pas être utilisés pour découvrir tardivement les responsabilités fondamentales qui auraient dû être clarifiées pendant l’audit documentaire.

---

## 24. Critère final de qualité du protocole

Le protocole est lui-même réussi s’il permet à une équipe ou à un agent de répondre, pour chaque fichier, à ces questions :

1. **Qui possède ce contrat ?**
2. **Quelle décision ce fichier aide-t-il à prendre ?**
3. **Quelle capacité positive rend-il plus probable ?**
4. **Quelle preuve permet de l’affirmer ?**
5. **Quelle limite doit rester visible ?**
6. **Quel lecteur doit agir ensuite ?**
7. **Que se passe-t-il si le premier rendu échoue ?**
8. **Comment la double boucle modifie-t-elle réellement l’artefact ?**
9. **Quand le one-shot peut-il être accepté honnêtement ?**
10. **Quel propriétaire reçoit l’escalade ?**
11. **Quelle validation prouve que la correction n’a rien cassé ?**
12. **Quelle prochaine preuve permet de réduire les réserves ?**

> **Conclusion :** auditer profondément ne signifie pas tout ajouter. Cela signifie rendre chaque responsabilité, chaque décision, chaque preuve, chaque limite et chaque possibilité de création suffisamment explicites pour être utilisées, contestées, améliorées et maintenues.
