# V1.2 refonte — Décisions de l'owner sur le plan consolidé (27-09-2026)

**Contexte :** plan consolidé proposé (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`), relu et vérifié dans le dépôt (constats exacts, correctifs appliqués en R11a). Arbitrages posés en questions groupées ; l'owner a retenu toutes les options recommandées.

| # | Objet | Décision de l'owner | Conséquence |
|---|---|---|---|
| 6 | Ancre | **Graduée.** Une première proposition est possible sans ancre (limite déclarée, reste `EXPLORATORY`) ; une ancre observée ou fournie est exigée **avant d'accepter** une direction pour un produit réel | R7 : aligner DIRECTION, ACTION, SAVOIR et les façades depuis un propriétaire canonique ; doublons `ANCHOR-GENERATED` traités ensuite. Validateur inchangé (il refuse déjà une DIRECTION acceptée sans ancre) |
| 3 et R9 | Schéma et version | **Schéma `RUN_CARD` inchangé → V1.2.0.** Ni `trace_level` ni `fabrication` sans consommateur machine ; modal et parti restent projetés dans `direction.anti_direction` | R9 devient un **report explicite**, documenté dans le rapport de publication |
| — | Calendrier de l'atlas | **Intégré en R8b, en référence conditionnelle de la skill** (chargée seulement si la décision visuelle est ouverte), pour être testé par R10 ; retiré si R10 montre une baisse de diversité (critères gardés) | **Révise explicitement** la décision 5 de G1 et le calendrier de `V12_04` (atlas hors package jusqu'après G4). Forme maintenue : liens et descriptions, pas de captures embarquées |
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
