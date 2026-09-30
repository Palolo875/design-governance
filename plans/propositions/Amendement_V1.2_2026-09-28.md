# Design Governance V1.2 — Amendement consolidé du plan de reprise

**Date :** 28 septembre 2026.  
**Statut :** copie de l’amendement préparé dans la discussion, à intégrer au plan existant ; non appliqué au dépôt.  
**Base examinée :** `Palolo875/design-governance`, commit `e71ba7d90c0cc9f70fb594c7bf52ba180bca773c`. Les deux branches de travail pointaient sur ce commit lors de la dernière vérification.  
**Portée :** décisions, précisions de périmètre, dépendances, critères de sortie et points ouverts. Aucun fichier GitHub modifié, aucun test réexécuté et aucune production R10 lancée pour cette consolidation.

Ce document rassemble les conclusions de la revue et la décision de remplacer le catalogue de références par des enseignements transférables. Il sert à mettre à jour le plan de reprise existant, sans créer un second plan actif. Les changements ci-dessous décrivent le travail à réaliser ; ils ne constituent pas un bilan d’implémentation.

## 1. Objectif commun et principes conservés

Le système doit aider à produire dès la première proposition un résultat composé, spécifique, crédible et soigné, avec une expression adaptée au projet. Il doit aussi rendre ses limites compréhensibles, rester utilisable par un novice et maîtriser l’effort de fabrication, de lecture et de maintenance.

La **double boucle existante reste centrale** : créer, observer, améliorer et, lorsque nécessaire, rouvrir la direction. Aucun nouveau circuit de finition ou de validation ne doit lui faire concurrence.

La qualité prime sur une réduction mécanique du nombre de mots. Les suppressions visent les répétitions et les instructions sans effet utile ; les ajouts doivent améliorer une décision, une construction ou une vérification.

Les arbitrages conservés sont : ancre graduée, schéma inchangé, R9 reporté, version cible V1.2.0, lois de SAVOIR inchangées, catalogue de routes élargi après publication, R11 ciblé et R10 par paliers. Le catalogue de **routes structurelles** est distinct de l’atlas de **créations de référence** abandonné ici comme livrable opérationnel.

## 2. Mettre les documents de pilotage en cohérence

Le [plan de reprise](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/plans/Plan_V1.2_Suite_Reprise.md) conserve le séquencement opérationnel. Le plan maître décrit l’architecture et les lots ; le registre explique les décisions et leurs révisions ; `CLAUDE.md` indique l’état et la prochaine action.

La mise à jour doit :

- retirer les mentions périmées de décisions 3, 6, 8, 9 et 10 « en attente » ;
- remplacer l’intégration future des arbitrages par leur état réel ;
- consigner la réorientation de R8b décidée par l’owner, en conservant l’historique de la décision précédente ;
- corriger la référence G1 : le calendrier de l’atlas relevait de la décision **2**, sa forme de la décision **5** ;
- identifier clairement les anciens périmètres comme historiques lorsqu’ils contredisent les décisions actuelles ;
- retirer des consignes actives les anciens plafonds rigides de mots incompatibles avec « qualité avant nombre de mots ».

Le plan consolidé archivé reste un document de provenance. Ses anciennes propositions ne doivent pas réintroduire un périmètre remplacé.

## 3. Séquence conservée

| Ordre | Lot | Résultat attendu |
|---|---|---|
| Préparation | Synchronisation documentaire | Un état de reprise cohérent |
| 1 | R8b | Moyens de fabrication consolidés et enseignements utiles réconciliés avec l’existant |
| 2 | R8c | Gestes de résolution précisés, intégrés à la double boucle |
| 3 | R7 | Règle d’ancre graduée alignée |
| 4 | R11 ciblé | Clarifications, tests manquants pertinents et reliquat explicite |
| 5 | R6b élargi | Entrée humaine simple et cohérente dans les distributions |
| 6 | Restes R5 | Doublons retirés et maintenance mieux séparée |
| 7 | R10 | Évaluation par paliers sur une candidate stable |
| 8 | R11 final | Réserves disposées et preuves de livraison |
| 9 | R12 | Publication V1.2.0 après feu vert final |

## 4. R8b — Moyens et enseignements transférables

Consolider la carte des moyens en distinguant capacité technique, ressources disponibles et limites de qualité. Remplacer les affirmations trop générales, notamment « atteignable en HTML seul », par des conditions utiles à la décision. Corriger la généralisation sur les licences de Fontshare et vérifier les conditions pertinentes des ressources retenues.

Pour chaque couche, expliquer brièvement ce qu’elle permet de construire, comment choisir une ressource adaptée et ce qui limite son usage. Préserver D-20 : contenu d’exemple clairement marqué lorsque le contenu réel manque, avec les éléments à fournir.

**L’intégration des 18 créations de l’atlas cesse d’être un objectif.** Leur recherche exhaustive, leurs images et leurs liens ne conditionnent plus la livraison de R8b.

Les enseignements sont confrontés aux sources existantes. Ceux déjà présents deviennent des renvois ou des améliorations ciblées ; les autres ne sont ajoutés que s’ils apportent une décision utile. Ils restent conditionnels : portée, observation attendue et contre-indication.

Aucun jugement global sur la valeur d’une création ou de son auteur n’est nécessaire. Une affirmation non étayée dans le matériau disponible ne devient pas une accusation de fabrication. Une contribution précise et identifiable conserve son attribution.

**Sortie :** une carte utilisable et des améliorations localisées, sans nouvelle bibliothèque obligatoire ni style général déduit d’un petit échantillon.

## 5. R8c — Résoudre plus précisément

Remplacer le projet d’une douzaine de recettes systématiques par une sélection fondée sur les manques constatés.

Conserver les gestes déjà présents dans TYPE, CRAFT, STATE et Gate C. Compléter seulement les passages insuffisamment opérables : équilibre d’un titre, relation texte/image, poids optique des icônes, récupération après erreur ou réinspection de l’ensemble après un réglage local.

Chaque geste précise son déclencheur, les corrections possibles et la manière d’en observer l’effet. La vérification peut nécessiter une capture, une interaction, une séquence ou une mesure.

**Une modification n’est pas obligatoire si la relation fonctionne déjà.** Les gestes peuvent guider le premier rendu ; ils ne sont pas réservés à une étape terminale.

Les notions d’accent unique, de traitement unique ou de famille unique restent des solutions contextuelles. Elles ne deviennent pas des exigences universelles de finition.

Les contenus restent chez leurs propriétaires ; le noyau reprend les éléments utiles par compilation. La création d’un bloc `FINITION` n’est pas une fin en soi.

**Sortie :** des gestes plus précis, sans deuxième checklist, sans quota de retouches et sans appauvrissement esthétique.

## 6. R7 — Ancre graduée

Aligner toutes les formulations sur la décision enregistrée :

Une première proposition peut commencer sans ancre, avec une limite déclarée et un statut exploratoire. L’acceptation d’une direction destinée à un produit réel exige une ancre observée ou fournie, pertinente et inspectée, ainsi que les autres preuves applicables.

Une ancre peut provenir du projet lui-même : identité existante, produit, photographie ou interface actuelle. Elle doit réellement contribuer à une décision. Une hypothèse générée reste utile à l’exploration.

DIRECTION conserve la règle canonique ; SAVOIR explique son exploitation ; ACTION porte les observations, la trace et les conséquences sur l’acceptation. Les façades et le noyau suivent cette règle.

**Limite à déclarer :** le validateur interdit notamment l’acceptation sans ancre, mais ne garantit pas entièrement l’exigence « observée ou fournie pour un produit réel ». Puisqu’il reste inchangé, ce point relève de la revue d’acceptation.

**Sortie :** aucune obligation préalable incompatible avec l’exploration autorisée, et aucune présentation du résultat machine comme preuve complète de la nouvelle règle.

## 7. R11 ciblé — Corriger sans élargir l’audit

Traiter Q04, Q07, Q08 et Q09 : portée réelle du contrôle machine, relation entre les scopes, référence canonique des sorties et articulation entre arrêt du polish et B1b.

Préserver les deux exceptions existantes de B1b. Une comparaison peut confirmer l’original ; elle n’impose pas de conserver une retouche.

Maintenir Q11 et Q12 avec leur justification, sauf nouvel élément probant. Enregistrer `DAILY` comme déjà corrigé par R11a.

Pour les cas négatifs, vérifier d’abord les autres harnais. Ajouter seulement les cas manquants retenus concernant la provenance de preuve, la séparation `observed`/`not_verified` et la protection critique. Chaque cas part d’une base valide et isole la faute attendue.

Q13 et R16–R32 restent ouverts jusqu’à lecture de leurs traces détaillées. Les limites des champs libres sont conservées ; aucun filtre général supplémentaire ni restauration d’INV-E11.

**Sortie :** chaque point traité possède une preuve ou une justification ; les inconnues restent visibles.

## 8. R6b élargi — Une entrée humaine cohérente

Unifier l’accueil autour de quatre questions : que demander, que fournir, que recevoir et comment poursuivre.

Le novice ne doit pas choisir lui-même un mode interne. La prise de brief reste proportionnée : au plus trois demandes utiles en un échange, aucune si les informations suffisent. Le contenu provisoire et les limites restent compréhensibles.

Fusionner les README du package, raccourcir QUICKSTART et réunir l’orientation utile des cartes de lecture sans perdre leurs liens et locators. Conserver l’accès aux détails pour les opérateurs expérimentés.

**Inclure impérativement le README Local généré dans `build_distributions.sh`.** Sinon, l’export recréerait l’ancienne entrée après la refonte.

Réutiliser la réponse visible d’`ACTION/HANDOFF`, sans nouveau protocole concurrent. La page courte est une porte d’entrée, pas une compression de toute la méthode.

**Sortie :** un parcours cohérent dans GitHub et Local. La facilité réelle pour un novice reste à observer en R10.

## 9. Restes R5 — Réduire les répétitions

Remplacer les copies du handoff dans SAVOIR et BIBLIOTHEQUE par des renvois, tout en conservant leurs contributions propres.

Regrouper les détails de maintenance et de promotion hors du parcours local lorsqu’ils ne sont pas applicables. Vérifier que leur déplacement réduit effectivement le chargement inutile.

Conserver `PRINT_FIELD` et le relier aux signaux de convergence comme question de jugement, jamais comme interdiction stylistique.

Répartir les responsabilités de l’alternative située : DIRECTION définit son déclenchement, SAVOIR ses leviers créatifs, ACTION sa comparaison.

**Sortie :** moins de prescriptions répétées, aucune capacité utile perdue et des propriétaires retrouvables.

## 10. R10 — Évaluer la candidate complète

Conserver le premier palier décidé : **B-DLA et SaaS × C1, C3, C4 × trois répétitions = 18 productions**. Si le diagnostic justifie la poursuite, compléter le protocole prévu de 60 ; réutiliser les premières productions seulement si leurs conditions restent comparables.

Avant lancement, fixer candidate, modèle, capacités, briefs, réponses d’intake, captures et mesures. Définir également ce que signifie « C3 se détache », le traitement des résultats discordants et le compromis de coût acceptable.

Observer séparément qualité, diversité pertinente, honnêteté et effort. Conserver si possible la première proposition présentable et le résultat après corrections, sans imposer un brouillon artificiellement faible.

Tracer les informations supplémentaires obtenues par l’intake et l’effort humain correspondant. Les gains de la candidate complète ne seront pas attribués automatiquement à un seul lot.

Jugements anonymisés, sans argumentaire du producteur ; désaccords conservés. Aucun modèle ou session neuve ne reçoit automatiquement le label indépendant D3. Prévoir une observation distincte du parcours novice.

La clause historique de retrait des exemples de l’atlas doit être adaptée à son nouveau périmètre : si la diversité baisse, examiner les consignes et ressources susceptibles de favoriser cette convergence, sans prétendre en connaître la cause à l’avance.

**Sortie :** résultats bornés et décision de poursuite, diagnostic ou publication avec les réserves requises. Aucun lancement n’est autorisé par cette consolidation.

## 11. R11 final et R12 — Livrer ce qui a été vérifié

Disposer chaque réserve, vérifier la candidate distribuable et obtenir la CI hébergée attendue. Conserver le lien du run, le commit, les versions effectives et les résultats.

Une modification après R10 demande une analyse d’impact avant réutilisation des conclusions. Finaliser version, CHANGELOG, notes, manifestes, distributions reproductibles et SHA-256.

La publication vise V1.2.0 avec R9 reporté. Elle exige le feu vert final de l’owner et ne promet pas davantage que les preuves obtenues.

## 12. Méthode et points encore ouverts

L’implémentation reprend la méthode existante : patchs explicites, gardes pertinentes, mutations, compilation, suivi, tests sur copies et protection de B01. Les contrôles déjà englobés ne sont pas relancés inutilement. Une adaptation de harnais reste déclarée et justifiée.

Le contrôle supplémentaire d’atteignabilité reste une proposition non tranchée. Il devra distinguer disparition réelle, accès conditionnel et fragilité de reconnaissance textuelle ; le cas F13 ne justifie pas à lui seul de transformer le nombre 24/25 en preuve suffisante.

Restent aussi à résoudre au moment approprié : les traces Q13/R16–R32, les critères précis de poursuite et de coût de R10, la disponibilité des juges et participants, puis le feu vert de publication.

**Ce texte constitue le contenu d’intégration au plan de reprise existant.** Les décisions de cette discussion sont distinguées de leur application : le dépôt demeure inchangé, et les bénéfices attendus restent à démontrer.

---

### Sources de reprise

Les liens suivants sont figés au commit examiné. Ils documentent la base de l’amendement, et non son application :

- [Plan de reprise](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/plans/Plan_V1.2_Suite_Reprise.md)
- [Plan maître de refonte](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/plans/Plan_V1.2_Refonte.md)
- [Registre des arbitrages](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/audit/reports/V12R_14_DECISIONS_ARBITRAGES.md)
- [Sources normatives](https://github.com/Palolo875/design-governance/tree/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/package/V1/official)
- [Validateur RUN_CARD](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/package/scripts/validate_run_card.py)
- [Génération des distributions et du README Local](https://github.com/Palolo875/design-governance/blob/e71ba7d90c0cc9f70fb594c7bf52ba180bca773c/package/scripts/build_distributions.sh)

Avant toute application ultérieure, comparer la branche courante à cette base et tenir compte des travaux réalisés entre-temps.
