# Release notes — Design Governance V1.2.0

**Statut expérimental :** Design Governance V1.2.0 est une expérimentation maintenue.  
**Date de la version :** 2026-10-01 (V1.1.1 : 2026-09-26 ; V1.0.0 : 2026-09-19)  
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Présentation

Design Governance aide un agent à produire un travail de design dirigé, construit et soigné dès la première proposition, puis à l’améliorer avec la personne qui le demande. V1.2.0 réorganise le système autour de la fabrication. L’agent lit un **noyau de fabrication**, compilé depuis les sources normatives. Il charge ensuite ce que la ligne de son mode dans `DIRECTION/CHARGE` demande. Il construit une première proposition composée et tient une **trace proportionnée** : légère par défaut, complète si le run est persistant, partagé, audité ou si une acceptation est demandée.

Les cinq sources normatives restent les autorités. Le schéma `RUN_CARD` est inchangé.

## Changements depuis V1.1.1

- **Noyau de fabrication.** Les gestes de structure, de composition, de typographie, de couleur, de contenu et de boucle d’édition sont compilés dans la skill depuis leurs propriétaires (`scripts/build_core.py`). `DIRECTION/CHARGE` est la seule liste de chargement ; les autres tables en sont des vues.
- **Trace graduée et proposition.** Par défaut, le run s’arrête à une proposition. La première proposition vaut checkpoint, sauf action irréversible ou coûteuse. Valider n’est pas accepter : l’acceptation pour un vrai produit se demande et passe en trace complète.
- **Vérité du contenu.**
  - Une destination réelle sans contenu reçoit des exemples marqués, pas des emplacements vides.
  - L’action principale reste fonctionnelle avec une valeur d’exemple marquée.
  - Les fonctions affirmées d’un produit fictif sont marquées comme exemples.
- **Ancre graduée.** On peut explorer sans ancre, avec une limite déclarée. Une direction identitaire n’est acceptée qu’avec une ancre, observée ou fournie pour un produit réel. `FAIL-ASSUMED` est réservé à un échec connu.
- **Interfaces.** `ACTION/UI-UX-REALITY` est chargé avant la fabrication d’une surface UI/UX nouvelle ou substantiellement modifiée. Toute exigence UI/UX déclarée est couverte : observée, non vérifiée, ou non applicable avec sa raison.
- **Entrée humaine.** La section « Commencer » du README répond à quatre questions, sans mode à choisir. Le QUICKSTART devient le guide de l’opérateur. La carte de lecture porte les combinaisons par résultat.
- **Outillage.**
  - Gardes de propriété (`scripts/validate_structure.py`).
  - Le lecteur de routes refuse les ambiguïtés.
  - Clés JSON répétées refusées.
  - Le schéma `RUN_CARD` est limité aux mots-clés réellement interprétés.
  - Dates et heures réelles.
  - Diagnostics nommés au lieu d’erreurs brutes.
  - Profil strict pour les fichiers locaux.
  - En cas d’échec, le build restaure ensemble `dist` et les archives.
  - En-tête YAML de la skill valide.
- **Charge de lecture.** Le chemin prescrit d’un run `DIRECTION` passe d’environ 23 600 à 13 835 mots. C’est une mesure documentaire, pas une économie observée en usage.

**Compatibilité.**
- Une `RUN_CARD` valide en V1.1.1 le reste, sauf si elle porte une date ou une heure impossible, désormais refusée.
- Un contrat de production dont la couverture UI/UX omettait des exigences déclarées doit être complété : une exigence non vérifiée y figure en `NOT-VERIFIED`.

L’historique détaillé est dans `V1/official/CHANGELOG.md`.

## Ce que contient la baseline

| Élément | Fonction |
|---|---|
| `V1/official/` | Sources normatives, guides d’entrée, glossaire et carte de lecture (`ORCHESTRATION_MAP.md` n’est plus qu’un pointeur vers elle) |
| `skills/design-governance-practice/` | Couche d’activation : noyau de fabrication compilé, références conditionnelles |
| `schemas/` | Projections machine, exemples et fixtures de contrôle |
| `scripts/` | Validateurs, compilation du noyau, runner global et construction des distributions |

## Parcours

**Pour une personne qui fait une demande :** la section « Commencer » du README du package. Elle n’a pas de mode à choisir.

**Pour un agent :**

```text
lire la skill (noyau de fabrication) → classer avec DIRECTION/START
→ charger la ligne de son mode dans DIRECTION/CHARGE → construire la première proposition
→ boucle d’édition → réponse visible et trace légère (trace complète si le run est persistant, partagé, audité ou à accepter)
```

**Pour un opérateur :** le guide `V1/official/QUICKSTART.md`.

## Contrôles inclus

Le package contrôle :
- son inventaire, ses liens et son vocabulaire structuré ;
- ses gardes de propriété et son noyau compilé ;
- ses contrats machine, avec leurs fixtures positives et négatives ;
- sa carte dérivée et son lecteur de routes ;
- la reproductibilité de ses distributions.

Ces contrôles établissent la cohérence documentaire et technique du package. Ils ne remplacent ni une observation de rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

Pour vérifier la baseline :

```bash
python3 scripts/validate_all.py
```

La validation complète a été observée sur un runner GitHub hébergé (Linux, Python 3.10, 3.11 et 3.13) le 2026-10-01, dans le dépôt de travail.

## Ce que le validateur atteste

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close.

Elle n’atteste pas :
- que les observations ont eu lieu ;
- la justesse des jugements ;
- la réalité des droits et des données ;
- la qualité perceptuelle.

La frontière exacte est écrite dans `ACTION/RUN_CARD`.

## Limites déclarées

- **Efficacité : `NOT-VERIFIED`.** Un palier exploratoire a été mené avec six productions, en auto-comparaison et avec des juges modèles d’une seule famille. Il oriente sans prouver. Seule une épreuve à l’aveugle avec des juges extérieurs (G4) pourra établir l’effet de V1.2.0 sur la qualité des rendus.
- **Convergence.** Le palier exploratoire a observé le même objet central et la même police de titre, avec ou sans système. Ce signal est suivi dans le noyau ; le système ne le rompt pas à lui seul.
- **Coût.** Lors du palier exploratoire, un run avec le système a coûté 1,7 à 1,8 fois un run sans système, en tokens. Ce coût n’a pas été remesuré depuis.
- **Intégration continue.** Elle a été observée sous Linux. macOS, Windows et le workflow du package dans un dépôt de distribution autonome n’ont pas été observés.
- **Champs libres.** Les placeholders n’y sont pas filtrés globalement.
- **Historique.** L’historique de construction et d’audit est conservé hors de la distribution publique. Il n’est pas nécessaire pour utiliser la baseline.
