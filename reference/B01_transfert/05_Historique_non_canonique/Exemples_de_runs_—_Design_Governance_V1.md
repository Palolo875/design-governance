# Exemples de runs — Design Governance V1

> **Statut du document : compagnon non canonique.** Ces exemples montrent comment utiliser V1 ; ils n’ajoutent aucune règle, route, gate, statut, score ou autorité. En cas de divergence, les sources canoniques font foi.

> **Reprendre la séquence de raisonnement et de vérification, pas les décisions visuelles, les valeurs, le style ou les composants de ces exemples.**

Les trois cas sont volontairement contrastés. Ils montrent qu’un run peut rester très court, devenir créatif lorsque le produit le justifie, ou exiger une analyse de portée lorsqu’une règle partagée est touchée. Les cas ci-dessous sont `ILLUSTRATIVE` et `SIMULATED` ; ils ne constituent pas des preuves de l’efficacité universelle de V1.

## 1. LITE — Corriger le contraste d’un bouton

### Demande

> « Le bouton secondaire “Annuler” est difficile à lire sur la surface sombre. Corrige uniquement ce problème sans changer le reste de l’interface. »

### Classification et décision

Le périmètre est local, le risque est normal et la demande ne touche ni une règle partagée ni une zone critique. Le mode retenu est `LITE`. La décision est : augmenter le contraste du texte et de la bordure du bouton sans modifier sa sémantique, sa taille, son emplacement ni son comportement.

`DESIGN-ATLAS` reste silencieux : aucune famille ne peut modifier utilement cette décision locale. Il n’y a pas d’ancre externe nécessaire. L’anti-direction locale est de ne pas transformer un correctif de contraste en refonte esthétique.

### Construction

| Élément | Avant | Après |
|---|---|---|
| Texte | Gris clair sur fond graphite | Blanc cassé sur fond graphite |
| Bordure | Gris moyen | Gris clair avec état focus conservé |
| Structure | Inchangée | Inchangée |
| Interaction | Inchangée | Inchangée |

Les valeurs de contraste sont ici des valeurs d’exemple destinées à illustrer la trace ; elles ne doivent pas être lues comme un calcul exécuté dans ce document.

### Mini-snapshot

```text
RUN: LITE-CONTRAST-001
MODE: LITE
DECISION-INTENT: améliorer la lisibilité du bouton secondaire sans élargir le scope
ARTIFACT: capture avant/après du bouton dans son état normal et focus
OBSERVED: modification locale du texte et de la bordure ; structure et interaction inchangées
NOT-VERIFIED: rendu sur tous les thèmes et appareils
DECISION-CHANGE: la couleur du texte et de la bordure a changé ; le reste a été conservé
ISSUE: aucune dans le scope observé
VERDICT: local uniquement, après vérification applicable
STATE: CLOSED
```

### Ce que montre ce cas

Un run `LITE` ne charge ni l’atlas, ni l’atelier, ni une longue analyse de style. Il conserve cependant l’intention, l’artefact, l’observation et la limite. La brièveté est une propriété du périmètre, pas une dispense de vérité.

## 2. DIRECTION — Hero éditoriale pour un service de cartographie sonore

### Demande

> « Conçois la première scène d’un service qui permet de découvrir les sons d’une ville. Je veux une hero mémorable et haut de gamme, mais pas une landing page SaaS générique. »

### Hypothèse de brief

Le produit est fictif et le cas est `ILLUSTRATIVE`. Le service aide une personne à explorer un territoire par ses ambiances sonores. Le JTBD est : *« Quand j’arrive dans une ville, je veux ressentir ses lieux avant de les parcourir, afin de choisir où aller avec une intuition personnelle. »*

Le mode est `DIRECTION`, car la première scène porte l’identité du produit. La décision n’est pas « rendre la page premium » ; elle est de faire sentir une ville comme une matière vivante et navigable, sans réduire l’expérience à une carte standard.

### Direction retenue

| Décision | Choix |
|---|---|
| Thèse | La ville se découvre par couches d’écoute, pas par une carte vue d’en haut. |
| Premier objet | Une topographie sonore interactive qui se déforme lorsqu’un lieu est activé. |
| Composition | Une scène asymétrique : titre court, objet directeur large, légende et geste de découverte. |
| Matière | Trames topographiques générées à partir d’extraits audio illustratifs, avec une texture sobre. |
| Typographie | Une fonte expressive pour le nom du lieu et une fonte instrumentale pour les mesures. |
| Composant authored | Une “sound contour card” qui associe lieu, durée, intensité, extrait et action. |
| Anti-direction | Pas de carte plate avec pins, pas de hero centré avec bouton générique, pas de photographie de ville interchangeable. |
| Condition de retrait | Si la matière sonore ne rend pas la relation lieu–écoute plus compréhensible, elle est retirée. |

### Construction et preuve

L’agent construit une première scène ouvrable avec un objet topographique, une carte authored et un geste local d’exploration. Les données et extraits sont explicitement fictifs. Le label `SIMULATION ILLUSTRATIVE` apparaît à proximité des métriques et des exemples audio.

La vérification porte sur la présence de la thèse dans la composition, la lisibilité du premier geste, le rôle réel de la matière, la cohérence du composant, le responsive de la scène initiale et l’existence d’un fallback sans animation. Le rendu peut fournir une observation visuelle dans le viewport inspecté ; il ne fournit pas une preuve de préférence, d’utilisabilité générale, d’accessibilité exécutée ou de qualité de la cartographie sonore.

### Trace abrégée

```text
RUN: DIRECTION-SOUND-CONTOUR-001
MODE: DIRECTION
DECISION-INTENT: faire comprendre une ville par des couches d’écoute et non par une carte conventionnelle
THESIS: la ville se découvre par couches d’écoute
FIRST-OBJECT: topographie sonore interactive
ANTI-DIRECTION: carte à pins, hero centré générique, photographie interchangeable
ARTIFACT: hero HTML ouvrable avec objet topographique et sound contour card
OBSERVED: hiérarchie de la scène, rôle de la matière, premier geste et fallback dans le scope inspecté
NOT-OBSERVED: préférence humaine, utilisabilité générale, accessibilité exécutée, données audio réelles
DECISION-CHANGE: la matière topographique a remplacé une carte plate dans la composition
ISSUE: métriques et extraits uniquement illustratifs
VERDICT: direction tenue dans le scope observé ; autres propriétés non vérifiées
STATE: HELD ou CLOSED selon le contrat de confirmation du run
```

### Ce que montre ce cas

`DIRECTION` ne signifie pas qu’il faut ajouter des effets ou utiliser un style naturel. Il signifie qu’une décision identitaire doit modifier la scène, les objets, la matière et le geste. Le composant authored existe parce qu’il porte la relation produit–lieu–écoute ; il ne s’agit pas d’une carte décorée.

## 3. SYSTÈME — Modifier un composant Select partagé

### Demande

> « Le Select du système doit accepter un libellé long, un état d’erreur et une aide contextuelle sans casser les écrans existants. »

### Classification et décision

La demande touche une primitive partagée et peut affecter plusieurs surfaces. Le mode retenu est `SYSTÈME`. La décision est d’ajouter une anatomie documentée et des états compatibles, puis de vérifier les dépendances avant toute extension visuelle.

L’objectif n’est pas de rendre le Select original à tout prix. La priorité est la stabilité sémantique, le clavier, le focus, le responsive, la compatibilité et la réduction du blast radius. Une singularité de surface n’est acceptable que si elle reste cohérente avec le système et ne détériore pas les usages existants.

### Périmètre et blast radius

| Zone | À examiner |
|---|---|
| Anatomie | Label, trigger, valeur, icône, aide, erreur, liste et option sélectionnée. |
| États | Default, hover, focus, ouvert, désactivé, erreur, vide, chargement et valeur longue. |
| Entrées | Clavier, pointeur, fermeture, sélection, échappement et navigation dans la liste. |
| Surfaces dépendantes | Formulaires, filtres, onboarding, paramètres et écrans mobiles. |
| Compatibilité | Tokens, thèmes, densité, textes longs, zoom et fallback. |
| Risque | Régression de focus, clipping du libellé, superposition de liste ou perte d’information d’erreur. |

### Construction et observation

L’agent crée une variante minimale du composant, documente ses frontières de composition et produit des captures des états pertinents. Il teste quelques surfaces représentatives plutôt que de prétendre avoir vérifié toute l’application.

Si une régression est observée dans un écran dépendant, l’issue est conservée et la décision est réouverte. Si aucune régression n’est observée dans le scope déclaré, cela n’autorise pas un claim sur les surfaces non inspectées. Une capture de baseline de composant signale un écart ; elle ne produit pas automatiquement un `PASS`.

### Trace abrégée

```text
RUN: SYSTEM-SELECT-001
MODE: SYSTÈME
DECISION-INTENT: étendre le Select sans rompre clavier, focus, états ou écrans dépendants
RISK: blast radius partagé ; protection de compatibilité active
ARTIFACT: composant Select, contrat d’états, captures et surfaces représentatives
OBSERVED: libellé long, erreur, focus, clavier et trois consommateurs inspectés
NOT-OBSERVED: tous les consommateurs, toutes les plateformes et toutes les combinaisons de thèmes
DECISION-CHANGE: anatomie et états d’erreur ajoutés ; tokens partagés non modifiés
ISSUE: une surface mobile présente un clipping à corriger, si observé
VERDICT: ne pas fermer tant que l’issue dans le scope reste ouverte
STATE: DECIDED puis CLOSED après correction et revalidation
ROLLBACK: restaurer le composant précédent si la correction augmente le blast radius
```

### Ce que montre ce cas

Un run `SYSTÈME` n’est pas une version plus longue de `LITE`. Il protège un autre type de décision : la compatibilité d’un élément partagé. Le blast radius est une propriété du périmètre et non un score global. Il faut pouvoir arrêter, corriger ou restaurer sans déclarer une réussite artificielle.

## Résumé commun

Les trois cas suivent le même noyau : **classer → diriger → construire ou modifier → vérifier → corriger → fermer**. Ils ne chargent pas les mêmes modules et ne produisent pas les mêmes preuves. La direction, le polish et la singularité peuvent être importants dans `DIRECTION`; ils ne remplacent jamais la vérification adaptée au risque et au scope.
