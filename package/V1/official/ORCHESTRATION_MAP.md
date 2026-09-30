# ORCHESTRATION_MAP — combinaisons dérivées par résultat

**Statut :** vue dérivée, non normative. `DIRECTION/START`, les cinq sources normatives, `READING_MAP.md`, le schéma `RUN_CARD` et les validateurs font foi en cas de divergence.

## Rôle

Cette fiche aide à combiner plusieurs capacités lorsque chacune peut **modifier la même décision** ou **protéger un risque déclaré**. Elle ne crée ni mode, ni route, ni gate, ni statut, ni verdict, ni champ machine. Le mode est d’abord classé par `DIRECTION/START` ; la combinaison est ensuite choisie selon le résultat recherché et le scope réel.

> **Principe :** ne pas charger le maximum de routes ; composer le maximum de contribution pertinente. Toute capacité activée doit avoir une contribution nommable et être retirée si elle ne change ni la décision, ni l’artefact, ni la preuve, ni la limite, ni la prochaine action.

La combinaison choisie reste dans la trace existante du run, seulement si elle peut modifier la décision. Ne crée pas une trace par capacité et ne transforme pas une table d’orientation en preuve.

## Combinaisons par résultat recherché

| Résultat recherché | Noyau possible | Renforcement seulement si nécessaire | Preuve à privilégier |
|---|---|---|---|
| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) | `DIRECTION/CREATIVE-BOOT`, `DIRECTION/DOMAIN-FRAME`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE`, `SAVOIR/STYLE`, `BIBLIOTHEQUE/SELECT` | Premier objet réel, revue créative, observation du défaut dominant et correction réellement observée. |
| **Beauté, goût et craft situés** | `DIRECTION/FIRST-OBJECT` + `SAVOIR/CRAFT` + `ACTION/FIRST-RENDER` | `SAVOIR/STYLE`, contenu crédible, matière, typographie ou ancre lorsque chacun peut modifier le jugement | Rendu réel dans le scope ; jugement créatif séparé des preuves d’usage, d’accessibilité et de robustesse. |
| **Créativité variée mais utile** | `DIRECTION/CREATIVE-BOOT` + `DIRECTION/VISUAL_TARGET` + une alternative située | `DIRECTION/DOMAIN-FRAME`, `SAVOIR/SOURCE` ou atelier seulement si l’axe de divergence change une décision | Comparaison dans le même scope par public, JTBD, promesse, geste, structure ou expression. |
| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + `ACTION/GATE-A` (contrôles applicables) + contenu et états réels | Responsive, focus, récupération, runtime ou `SAVOIR/CONTEXT` selon le risque | Tâche, états, viewports, contenu extrême, clavier ou méthode adaptée au claim. |
| **Preuve et décision fiables** | `ACTION/STRUCTURED-PROOF` + artefact réel + gate correspondant au risque + `ACTION/CLOSE-EXIT-CHECK` | Preuve croisée ou `RUN_CARD` stricte si la persistance l’exige | Claim, méthode, scope, date, artefact, limite et `TRACE-LOCATOR` retrouvables. |
| **Vitesse sans appauvrissement** | `DIRECTION/START` + `ACTION/FAST-PATH` + `LITE` ou `ITER` correctement classé | Ajouter une seule capacité si elle peut changer la décision ; reclassifier si le risque ou le périmètre augmente | Artefact réel, observation ciblée, preuve minimale applicable et prochaine action. |
| **Système maintenable** | `ACTION/RUN-SYSTEM` + `BIBLIOTHEQUE/COMPONENTS` si un composant change + migration, rollback et `CHANGELOG` (paquet SYSTÈME) | `BIBLIOTHEQUE/EVOLUTION` ou `SAVOIR/SYSTEM` selon la décision partagée | Consumers, compatibilité, non-régression, owner, migration et condition de reprise. |
| **Domaine sensible ou incertain** | `DIRECTION/DOMAIN-FRAME` + `SAVOIR/SOURCE` + `ACTION/STRUCTURED-PROOF` | Contexte culturel, conventions, confiance ou recherche seulement si un déclencheur peut changer la décision | Source ou observation reliée à la décision, transformation, rejet et limite. |
| **Agent contrôlé** | `DIRECTION/START` + `ACTION/AUTHORITY` + `SKILL.md` + owner | `READING_MAP`, `RUN_CARD` et cette fiche seulement si plusieurs capacités sont réellement nécessaires | Artefact livré, autonomie exercée, décision, preuve, limite, escalade et prochaine action. |

Ces combinaisons ne sont pas des parcours obligatoires. Elles indiquent des capacités compatibles ; `READING_MAP.md` résout le premier chemin et les sources propriétaires définissent le contenu exact des routes.

## Variation créative

Pour produire du beau varié sans bruit : `SAVOIR/CRAFT/CFT-02` (un axe situé à la fois).

Une alternative est utile si elle peut modifier le choix. Une référence, une ancre, une rationale ou une variante ne constitue pas une preuve indépendante.

## Garde-fous

- Classer d’abord avec `DIRECTION/START` ; cette fiche ne reclassifie pas.
- `ITER` signifie une itération sur une direction ou un système existant retrouvable, dans son périmètre ; il ne signifie pas simplement « quelque chose existe déjà ».
- Un chemin court ne réduit jamais la protection d’un risque critique.
- Une capacité indisponible limite le claim correspondant ; elle ne justifie pas une baisse silencieuse du mode.
- Ne pas remplir toutes les routes d’une combinaison si une route principale suffit.
- Ne pas ajouter de trace, de variante ou de preuve qui ne peut changer la décision, l’artefact, la limite ou l’action suivante.

## Arrêt

Arrêter l’orchestration lorsque la décision, le risque, le scope, l’owner, l’artefact, la preuve, la limite et la prochaine action sont suffisamment explicites. La richesse de lecture n’est pas un résultat ; **l’effet positif observable dans le périmètre déclaré** est le résultat recherché.

