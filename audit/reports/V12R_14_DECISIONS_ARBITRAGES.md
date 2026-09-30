# V1.2 refonte — Décisions de l'owner sur le plan consolidé (27-09-2026)

**Contexte :** plan consolidé proposé (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`), relu et vérifié dans le dépôt (constats exacts, correctifs appliqués en R11a). Arbitrages posés en questions groupées ; l'owner a retenu toutes les options recommandées.

| # | Objet | Décision de l'owner | Conséquence |
|---|---|---|---|
| 6 | Ancre | **Graduée.** Une première proposition est possible sans ancre (limite déclarée, reste `EXPLORATORY`) ; une ancre observée ou fournie est exigée **avant d'accepter** une direction pour un produit réel | R7 : aligner DIRECTION, ACTION, SAVOIR et les façades depuis un propriétaire canonique ; doublons `ANCHOR-GENERATED` traités ensuite. Validateur inchangé (il refuse déjà une DIRECTION acceptée sans ancre) |
| 3 et R9 | Schéma et version | **Schéma `RUN_CARD` inchangé → V1.2.0.** Ni `trace_level` ni `fabrication` sans consommateur machine ; modal et parti restent projetés dans `direction.anti_direction` | R9 devient un **report explicite**, documenté dans le rapport de publication |
| — | Calendrier de l'atlas | **Intégré en R8b, en référence conditionnelle de la skill** (chargée seulement si la décision visuelle est ouverte), pour être testé par R10 ; retiré si R10 montre une baisse de diversité (critères gardés) | **Révise explicitement** la décision **2** de G1 (calendrier : C et E intégrés après G4 ; la décision 5 ne fixait que la forme) et le calendrier de `V12_04`. *Rectification du 30-09-2026 : la première version citait à tort la décision 5.* **Révisé à son tour le 30-09-2026 (addendum 2) : l'atlas n'est plus un livrable.** Forme maintenue : liens et descriptions, pas de captures embarquées |
| 9 | Juges de R10 | **Humains extérieurs (D3) et modèles d'autres familles**, déclarés non indépendants. Sans juge D3 : résultat d'orientation ; publication seulement avec réserve et feu vert final | Aucun label « indépendant » pour un modèle ou une seconde session |
| 8 | Lois de SAVOIR | **Inchangées** ; l'hypothèse d'un biais vers la retenue est examinée en R10 | Aucun ajout de règle de pluralité (déjà présente) |
| 10 | Catalogue élargi | **Après publication**, depuis des runs réels (routes `PILOT`) ; la dérivation locale reste permise | — |
| — | Volume de R10 | **Par paliers.** Palier 1 : B-DLA et SaaS × C1, C3, C4 × 3 = 18 productions ; arrêt diagnostique si C3 ne se détache pas ; sinon protocole complet (60). Toute réduction est déclarée avec sa perte de portée | Budget à confirmer avant lancement ; la consigne « pas de run dans cette phase » reste en vigueur jusqu'au passage explicite à R10 |
| — | Portée de R11 | **Ciblée.** Cas négatifs prioritaires (cohérence locator preuve/artefact ; `observed` / `not_verified` ; protection critique complète avec action d'échec valide) ; reliquat maintenu par écrit ; réserve « placeholders des champs libres » maintenue ; extraction des journaux zip pour trier Q13 et R16 à R32 | Aucun filtre global ajouté ; INV-E11 non restauré |
| — | Ordre des lots | **Le rendu d'abord :** R8b → R7 → R11 ciblé → R6b → restes R5 → R10 par paliers → R11 final → R12 (R9 reporté) | Remplace l'ordre de la section 4 du plan de reprise |

**Décisions antérieures conservées :** 1, 2, 4, 5, 7, 11 ; D-20 ; D-22 ; consigne « qualité avant nombre de mots ».

**Proposition non tranchée :** un cliquet d'atteignabilité dans `V12R_Suivi.py` (écart 1 de `V12R_13`), à inclure dans la prochaine unité si l'owner l'accepte.

## Addendum (27-09-2026) — deux lots ajoutés

Discussion sur l'ambition du système (« le meilleur des deux mondes » : gouvernance **et** production du beau, haut de gamme, pour l'agent comme pour un novice, sans multiplier le travail). Proposition acceptée par l'owner (« Vas-y ») :

- **R8c — passe de finition**, après R8b : gestes de polish concrets par couche (type, espace, couleur, image, interaction et états, détail), observables sur capture, dans le noyau à côté de la boucle d'édition.
- **R6b élargi** : une page d'entrée humaine d'une page, une demande d'intrants amicale en un message, une voix produit engageante pour la réponse visible.

**Ordre mis à jour :** R8b → **R8c** → R7 → R11 ciblé → **R6b élargi** → restes R5 → R10 par paliers → R11 final → R12.

## Addendum 2 (30-09-2026) — amendement du 28-09, R10 progressif, consolidation avant les runs

Trois messages de l'owner, discutés et approuvés dans la conversation (sources : `plans/propositions/Amendement_V1.2_2026-09-28.md` et échanges du 30-09-2026).

| Objet | Décision | Remplace |
|---|---|---|
| **R8b réorienté** | L'intégration des 18 créations de l'atlas **cesse d'être un objectif** ; leurs images, liens et recherche exhaustive ne conditionnent plus R8b. R8b = carte des moyens consolidée (capacité, ressources, limites ; conditions au lieu de « atteignable en HTML seul » ; licences vérifiées par ressource) + **enseignements transférables** confrontés à l'existant (renvoi ou ajout ciblé, conditionnel, avec observation attendue et contre-indication). Attribution conservée pour une contribution précise ; aucun jugement global sur une création ou son auteur | L'intégration de l'atlas en R8b (addendum 1, 27-09) ; l'atlas v0 reste un matériau historique |
| **R8c recadré** | Pas de douzaine de recettes systématiques ni de bloc `FINITION` comme fin en soi. Compléter seulement les gestes insuffisamment opérables (équilibre d'un titre, relation texte/image, poids optique des icônes, récupération après erreur, réinspection de l'ensemble après un réglage local), avec déclencheur, corrections possibles et observation de l'effet. **Aucune modification obligatoire si la relation fonctionne.** « Accent unique », « traitement unique », « famille unique » restent des solutions contextuelles, jamais des exigences universelles | La liste de l'addendum 1 |
| **R10 progressif** | Évaluer après consolidation. Palier exploratoire : 2 briefs × C1, C3, C4 = **6 cas comparés**, avec 4 à 6 productions neuves selon la réutilisation vérifiée d'une référence B-DLA C1 et d'une référence B-DLA C4. Même modèle ne suffit pas : consignes, intrants, outils, capacités, limites, captures et mesures restent comparables et les écarts sont consignés. **C3 utilise la candidate après P2 ; les C3 de P1 ne la représentent pas.** Problème évident → diagnostic et correction ; extension à 18 puis davantage seulement si justifiée, critères écrits avant production | Le palier initial de 18 ; précision des conditions de réemploi, sans nouveau lancement autorisé |
| **Observation novice** | Distincte des productions d'agents : 2 ou 3 personnes lisent l'entrée R6b et lancent une demande ; on note les blocages. Aucun volume de runs ne la remplace | — |
| **Consolider avant d'évaluer** | Aucun run avant la **porte P2 « prêt pour l'évaluation »**. Corriger et améliorer = mettre l'existant à sa place (hiérarchie, organisation, accès, cohérence, clarté, fiabilité), pas ajouter ni retirer au hasard ; chaque modification répond à un défaut identifié, préserve ce qui marche et a une vérification proportionnée. Les moyens de produire du beau interviennent **pendant** la conception. Outils : **inventaire unique des défauts** (bloquant P2 ou non) et **relecture de parcours** (4 profils) | Le palier exploratoire ne contourne pas la consolidation |

*Précision du 30-09-2026 (note de consolidation préparatoire, intégrée le même jour) : la ligne « R10 progressif » ci-dessus a été reformulée. Formulation initiale : « 2 briefs contrastés × 3 conditions (≈ 6 productions ; ≈ 4 si les rendus B-DLA existants restent comparables, même modèle producteur) ». Apports : 6 **cas comparés** distincts du nombre de productions neuves ; conditions de réemploi au-delà du seul modèle ; C3 toujours produit sur la candidate après P2.*

**Seuil de P2 :** les défauts connus qui compromettent l'usage ou faussent l'évaluation sont corrigés ; les parcours essentiels sont vérifiés ; les limites restantes sont explicites et ne bloquent pas l'épreuve. P2 ne prétend pas résoudre ce que seul l'usage montre (qualité réelle, variabilité, facilité pour un novice).

**Conservé :** ancre graduée, schéma inchangé, R9 reporté, V1.2.0, lois inchangées, catalogue de routes après publication, R11 ciblé ; « qualité avant nombre de mots » (les anciens plafonds de mots deviennent des repères de diagnostic historiques).

**Proposition encore ouverte :** contrôle d'atteignabilité dans le suivi, distinguant disparition réelle, accès conditionnel et fragilité de l'ancre textuelle (cas F13).
