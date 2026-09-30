# Exemples de runs

> Ces exemples sont des aides non canoniques. Reprendre la séquence, pas le style, les valeurs, les composants ou les décisions visuelles. Les cas sont `ILLUSTRATIVE` et `SIMULATED` sauf mention contraire. Les champs affichés varient volontairement selon le mode : une omission dans une condensation n’est pas une suppression de la règle correspondante et ces blocs ne constituent pas un formulaire universel de `RUN_CARD`. Les champs affichés respectent les contrats d’ACTION ; un champ omis reste dû dans la `RUN_CARD`.
>
> **Trace, pas sérialisation.** Ces blocs sont des traces : leurs noms (`OBSERVED`, `AXES`, `RISK` en phrase…) ne sont pas des clés JSON. Pour produire une `RUN_CARD`, partir de `schemas/run_card.example.json`, suivre [machine_projection.md](machine_projection.md) et la table de correspondance d’`ACTION/RUN_CARD`, puis contrôler avec `scripts/validate_run_card.py`.
>
> **Niveau de trace.** Les exemples qui se terminent par `CLOSED` montrent une trace complète (clôture demandée ou run persistant) ; « fabrication depuis un brief flou » montre la sortie par défaut : une proposition et sa réponse visible, sans clôture.

## LITE — correctif local

**Demande :** améliorer le contraste du bouton secondaire sans modifier la structure.

**Chemin :** classer `LITE` → déclarer `DECISION-INTENT` → modifier → vérifier le ratio et l’état focus → clôturer avec la limite.

```text
MODE: LITE
DECISION-INTENT: améliorer la lisibilité sans élargir le scope
RISK: libellé secondaire illisible en contraste faible
ARTIFACT: diff et snapshot avant/après
OBSERVED: ratio 3,1:1 → 5,2:1 ; focus visible ; structure et interaction conservées
LIMIT: autres thèmes hors scope
AXES: V PASS · A PASS (contraste, focus) · U N/A-JUSTIFIED · T N/A-JUSTIFIED
DECISION-CHANGE: CONFIRMED — garder la hiérarchie du bouton secondaire et ne corriger que sa couleur (observation : snapshot avant/après, ratio mesuré)
VERDICT: ACCEPTED
STATE: CLOSED
```

Ne pas charger l’atlas ou une analyse de style si aucune responsabilité de design ne change.

## DIRECTION — fabrication depuis un brief flou

**Demande :** « Il me faut un site pour ma boulangerie. » Rien d’autre.

**Prise de brief, en un seul échange :** l’agent demande les contenus réels (produits, prix, horaires, adresse), le logo ou les couleurs s’ils existent, et deux ou trois photos du comptoir ; la destination est une vraie mise en ligne. Faute de réponse, il construit avec des hypothèses nommées.

```text
THÈSE: le pain du jour se choisit d’un coup d’œil, avant d’entrer
OBJET DE PREUVE: la vitrine du jour, composant codé (produit, prix, heure de sortie du four)
MODAL: photo pleine largeur, titre centré, trois cartes « nos valeurs »
PARTI: s’écarter pour la première scène, où la vitrine du jour remplace la photo ; garder la navigation attendue
FABRICATION: typographie et couleur au plafond (polices libres, palette tirée des photos) ; photos du client moyennes, traitement commun choisi pour unifier la série ; aucune illustration dessinée
DÉFAUT DOMINANT: après capture, les prix se lisent mal sur mobile ; taille et contraste corrigés, seconde capture comparée
```

**Réponse visible :** « J’ai construit une page d’accueil organisée autour de la vitrine du jour. Pourquoi : on choisit son pain avant d’entrer, la page le permet en un coup d’œil. Ce qui manque pour la vraie version : vos prix, vos horaires et une photo du comptoir en lumière du jour ; les produits affichés sont des exemples marqués comme tels. La suite : envoyez ces éléments, je les intègre et je vérifie le mobile. »

## DIRECTION — première scène identitaire

**Demande :** créer une hero mémorable pour un service de cartographie sonore, sans page SaaS générique.

**Décisions :** thèse située, premier objet sonore, composition asymétrique, matière utile, composant authored, modal et parti. L’artefact doit être ouvrable et les données fictives marquées.

```text
MODE: DIRECTION
DECISION-INTENT: choisir une direction située pour le premier geste de découverte
THESIS: la ville se découvre par couches d’écoute
FIRST-OBJECT: topographie sonore interactive
MODAL: carte plate à pins, titre centré, cartes de fonctionnalités
PARTI: s’écarter de la carte à pins ; l’écoute par couches porte la scène
ARTIFACT: hero construite avec objet, contenu et geste
OBSERVED: hiérarchie, matière et premier geste dans le viewport inspecté
NOT-VERIFIED: préférence, utilisabilité générale, accessibilité exécutée
AXES: V PASS · U NOT-VERIFIED · A NOT-VERIFIED · T PASS
DECISION-CHANGE: CHANGED — la topographie sonore remplace la carte à pins comme premier objet (observation : paire v1/v1b, le premier geste est lu en premier dans le viewport inspecté)
CREATIVE-REVIEW: présence portée par la topographie sonore ; signature spécifique dans la relation entre ville, couche et écoute ; résolution à renforcer dans les états secondaires ; prochaine action : polir la transition entre découverte et premier geste
VERDICT: ACCEPTED-WITH-RESERVATION
RESERVATION: accessibilité exécutée non vérifiée — owner : lead design ; scope : hero ; impact : parcours clavier de la topographie inconnu ; prochaine preuve : parcours clavier et lecteur d’écran ; revue : 2026-10-09 ; condition de sortie : parcours clavier observé sans blocage
DIRECTION-STATUS: HELD
STATE: CLOSED
```

Une belle capture ne prouve pas l’usage. Une rationale ne prouve pas l’implémentation.

Lecture visuelle illustrative — annotation narrative, non-champ `RUN_CARD` : la direction artistique est visible dans la matière et le premier objet ; le craft est observé dans la hiérarchie et la composition du viewport ; la revue créative rend explicites la présence, la signature et le défaut dominant ; le polish des états secondaires et l’usage général restent non vérifiés. `CREATIVE-REVIEW` est ici un libellé narratif illustratif ; dans la projection machine, cette observation est transportée par `creative_close`. Ce contenu ne constitue pas un nouveau statut ni un verdict esthétique.

## DIRECTION + STYLE — profil d’expression situé

**Demande :** donner une présence culturelle à une archive numérique sans transformer l’interface en nostalgie décorative.

**Choix :** tester `STYLE/DIGITAL_MEMORY` comme hypothèse d’expression. Le profil modifie la matière, le rythme et le traitement des fragments ; il ne choisit ni la structure de l’archive ni le verdict.

```text
MODE: DIRECTION
PROFILE: STYLE/DIGITAL_MEMORY
PROFILE-DECISION: transformer la mémoire d’écran en repère de collection
PROFILE-PHASE: observed
DIALS: densité haute dans l’archive, motion basse dans la navigation, variance modérée dans les pièces
COUNTERINDICATION: lecture critique, contraste faible, nostalgie sans relation au contenu
ARTIFACT: scène d’archive avec fragments, métadonnées et états réels
EVIDENCE: paire de captures avec et sans traitement pixel/raster : les pièces se distinguent des contrôles et les métadonnées restent lisibles (claim visuel seulement)
PROOF-LIMIT: mémorisation et tâche NOT-VERIFIED (elles exigeraient un protocole utilisateur : participants, tâche, mesure) ; droits des fragments externes non validés
DECISION-CHANGE: CHANGED — le traitement numérique est limité aux pièces et retiré des contrôles critiques (observation : paire de captures)
```

Le profil peut être refusé si la paire ne change aucune décision ou si la matière nuit à la lisibilité. `PROFILE-DECISION` ne devient ni un score, ni un verdict esthétique, ni une autorisation d’imiter une référence.

## SYSTÈME — composant partagé

**Demande :** ajouter au Select un libellé long, une aide et un état d’erreur sans casser les écrans existants.

**Chemin :** classer `SYSTÈME` → inventorier les dépendances → modifier la primitive et ses états → inspecter des consommateurs représentatifs → corriger ou restaurer.

```text
MODE: SYSTÈME
DECISION-INTENT: étendre le Select sans rompre clavier, focus ou compatibilité
RISK: blast radius partagé
ARTIFACT: composant, états, captures et consommateurs représentatifs
OBSERVED: libellé long, erreur, focus et clavier dans trois consommateurs ; troncature observée sur mobile dans le consommateur 2
NOT-VERIFIED: autres écrans, plateformes et thèmes
DECISION-CHANGE: ABANDONED — l’extension du Select en l’état est abandonnée : la troncature mobile casse ce consommateur ; une version corrigée reprend dans le même mode (observation : consommateur 2)
ISSUE: RETURNED
VERDICT: RETURN
STATE: CLOSED
```

Le blast radius appartient au scope du run ; il ne devient pas un score global.

