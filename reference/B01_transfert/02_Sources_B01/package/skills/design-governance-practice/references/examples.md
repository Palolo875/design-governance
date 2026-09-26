# Exemples de runs

> Ces exemples sont des aides non canoniques. Reprendre la séquence, pas le style, les valeurs, les composants ou les décisions visuelles. Les cas sont `ILLUSTRATIVE` et `SIMULATED` sauf mention contraire. Les champs affichés varient volontairement selon le mode : une omission dans une condensation n’est pas une suppression de la règle correspondante et ces blocs ne constituent pas un formulaire universel de `RUN_CARD`.

## LITE — correctif local

**Demande :** améliorer le contraste du bouton secondaire sans modifier la structure.

**Chemin :** classer `LITE` → déclarer `DECISION-INTENT` → modifier → vérifier le ratio et l’état focus → clôturer avec la limite.

```text
MODE: LITE
DECISION-INTENT: améliorer la lisibilité sans élargir le scope
ARTIFACT: diff et snapshot avant/après
OBSERVED: texte et bordure modifiés ; structure et interaction conservées
NOT-VERIFIED: autres thèmes et appareils
DECISION-CHANGE: couleur du texte et de la bordure
STATE: CLOSED
```

Ne pas charger l’atlas ou une analyse de style si aucune responsabilité de design ne change.

## DIRECTION — première scène identitaire

**Demande :** créer une hero mémorable pour un service de cartographie sonore, sans page SaaS générique.

**Décisions :** thèse située, premier objet sonore, composition asymétrique, matière utile, composant authored et anti-direction. L’artefact doit être ouvrable et les données fictives marquées.

```text
MODE: DIRECTION
DECISION-INTENT: choisir une direction située pour le premier geste de découverte
THESIS: la ville se découvre par couches d’écoute
FIRST-OBJECT: topographie sonore interactive
ANTI-DIRECTION: carte plate à pins et hero centré interchangeable
ARTIFACT: hero construite avec objet, contenu et geste
OBSERVED: hiérarchie, matière et premier geste dans le viewport inspecté
NOT-VERIFIED: préférence, utilisabilité générale, accessibilité exécutée
DECISION-CHANGE: la matière sonore a changé la scène
CREATIVE-REVIEW: présence portée par la topographie sonore ; signature spécifique dans la relation entre ville, couche et écoute ; résolution à renforcer dans les états secondaires ; prochaine action : polir la transition entre découverte et premier geste
VERDICT: ACCEPTED-WITH-RESERVATION
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
DIALS: densité haute dans l’archive, motion basse dans la navigation, variance modérée dans les pièces
COUNTERINDICATION: lecture critique, contraste faible, nostalgie sans relation au contenu
ARTIFACT: scène d’archive avec fragments, métadonnées et états réels
EVIDENCE: paire de captures avec et sans traitement pixel/raster ; la sélection des pièces reste plus mémorable sans perdre la tâche
PROOF-LIMIT: aucune preuve utilisateur générale ni validation de droit des fragments externes
DECISION-CHANGE: le traitement numérique est conservé uniquement dans les pièces, pas dans les contrôles critiques
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
OBSERVED: libellé long, erreur, focus, clavier et trois consommateurs
NOT-OBSERVED: tous les écrans, plateformes et thèmes
ISSUE: RETURNED
VERDICT: RETURN
STATE: CLOSED
```

Annotation narrative — non-champ `RUN_CARD` : régression observée à corriger avant clôture ; restaurer le composant précédent si nécessaire.

Le blast radius appartient au scope du run ; il ne devient pas un score global.

