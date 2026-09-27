# Plan V1.2 — Addendum : viser le niveau senior dès le premier rendu

**Date :** 2026-09-27 · **Owner :** Junior (Kamel) · **Statut :** proposition, décisions attendues (§7)
**Complète :** `plans/Plan_V1.2_Qualite_senior_gouvernance.md`. Base : B05 (A, B, D appliqués, `audit/reports/V12_03_G3_APPLICATION_B05.md`).
**Sources de l'addendum :** épreuve B-DLA (`V12_00`), revue de 4 lots de références de designers (discussion du 26 au 27-09-2026), recherche sur le slop (§1).

---

## 1. Constat

**Le slop en design a deux sens.** Le sens du dictionnaire : contenu de faible qualité produit en masse. Le sens design, plus insidieux : **compétent mais interchangeable**. Les rendus B-DLA sont propres un par un et identiques ensemble (6 sur 6 en crème et brun).

| Constat | Certitude | Source |
|---|---|---|
| Interdire les défauts de vague 1 (Inter, violet, trois cartes) pousse l'IA vers le défaut suivant : crème, terre cuite, serif | Probable, corroboré par des praticiens et par B-DLA | [avoid-ai-design](https://github.com/funboy322/avoid-ai-design), [Developers Digest](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it), `V12_00` |
| L'homogénéisation résiste aux modifications de prompt et de paramètres ; qualité individuelle bonne, diversité collective en baisse | Probable (études évaluées par des pairs et prépublications) | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S294988212500091X), [arXiv 2608.11426](https://arxiv.org/pdf/2608.11426) |
| Les outils anti-slop fonctionnent par listes d'interdits et thèmes, donc créent la prochaine médiane | Probable | [Hallmark](https://dev.to/rams901/hallmark-stop-ai-generated-ui-slop-in-one-command-in-2026-3p9n) |
| Les designers humains produisent les mêmes marqueurs (palette modale, faux chiffres, faux logos) : c'est la culture des « shots » dont les modèles ont appris | Probable | Revue des 4 lots |
| Les pièces qui dépassent réunissent un texte précis, un objet de preuve qui montre le produit et un motif tiré du domaine (Fold, Fabric, termes solaires, bannière Bay Area) | Probable | Revue des 4 lots |

**Conséquence :** un texte de règles seul ne vaincra pas l'homogénéisation. Les leviers sont les **intrants** (A, B), la **fabrication là où l'agent est fort** et l'**itération observée**.

## 2. Ce qu'un agent peut atteindre, couche par couche

| Couche | Niveau senior en HTML seul | Condition |
|---|---|---|
| Structure, grille, hiérarchie | Atteignable | — |
| Typographie | Atteignable | Polices de qualité disponibles |
| Couleur | Atteignable | Nommer le modal (`MODAL`/`PARTI`) |
| Composants, UI produit | Atteignable | Design system fourni ou bibliothèque de qualité |
| Données, objets de preuve interactifs | Atteignable | Contenu ou données plausibles et marqués |
| Texture et traitement (grain, trame, duotone, étalonnage) | Atteignable | Justifié par la thèse |
| Mouvement | Atteignable | Utile, pas décoratif |
| **Assets figuratifs** (illustration, photo, 3D, personnages, paysages) | **Non atteignable** | Fourni, curaté, généré dirigé, ou absent |
| **Contenu réel** (textes, prix, preuves) | **Non atteignable** sans le client | Sinon emplacements marqués |

**Observation clé :** une grande part des meilleures pièces revues est entièrement codable : widgets de données, cartes produit, bloc de code, file d'attente, matrice de points. L'agent atteint le niveau senior quand l'objet de preuve est dans son terrain.

## 3. Nouveaux chantiers

### G — Objet de preuve codé, de préférence

- **Règle proposée :** dans `DIRECTION/FIRST-OBJECT`, la première scène est portée **de préférence** par un objet de preuve codé : composant, donnée, état ou interaction du produit (bon de commande, horloge des fournées, file d'attente). Une illustration ne porte la scène que si elle est fournie, curatée ou générée dirigée.
- **Pourquoi :** c'est la couche où l'agent atteint le niveau senior ; c'est aussi la meilleure preuve du produit.
- **Garde visée :** une condition de façade vérifiant la règle dans `FIRST-OBJECT` et sa copie dans la skill.

### H — Carte des moyens par couche (`[VEILLE]`)

- **Contenu :** pour chaque couche du §2, les **sources** où trouver de la qualité, pas des styles. Exemples à valider :
  - polices : Google Fonts, Fontshare ;
  - icônes : une seule famille (Lucide, Phosphor) ;
  - composants : design system fourni, sinon shadcn ou Radix ;
  - photos : client, banques sous licence (Wikimedia Commons, Unsplash) ;
  - génération dirigée : outil d'image avec références ;
  - fichiers de design : Figma par connecteur ;
  - 3D : Spline.
- **Emplacement :** `SAVOIR`, bloc `[VEILLE AAAA-MM]` daté, révisable ; une ligne de renvoi depuis `FABRICATION`.
- **Articulation avec la décision 4 (critères seuls) :** une source n'est pas un style ; aucune famille n'est recommandée par défaut. À trancher explicitement (§7).

### I — Traitement des assets moyens

- **Règle proposée :** quand les assets disponibles sont moyens (photos de téléphone, banque d'images), appliquer **un traitement unique et cohérent** (recadrage, étalonnage, duotone, grain ou trame) justifié par la thèse, plutôt que de les poser bruts ou de les remplacer par un dessin.
- **Garde-fou :** la trame et le dithering sont des marqueurs de la vague 3 ; le traitement se justifie par la relation au produit, pas par la mode.
- **Emplacement :** `SAVOIR/CRAFT`, technique ; renvoi depuis la route de production (`VISUAL_TARGET`).

### E' — Atlas d'ancres annotées, à double colonne (précise le chantier E)

- Chaque entrée porte une **leçon visuelle** (échelle, palette, lumière, texture, typographie) et une **leçon de fond** (relation, mots, vérité, destination).
- Liens et descriptions seulement (décision 5).
- Première version tirée de la revue des 4 lots : `plans/atlas_references_v0.md`.

### D' — Vague 3 datée (complète le chantier D)

- Marqueurs : tramage et dithering, logos pixel, ASCII, hachures de plan, gravures, bleu Klein, libellés mono en capitales, repères de recadrage, paysage peint ou tramé comme nouvelle image de banque.
- Fiche : `plans/veille_vague3.md`, à intégrer au bloc `[VEILLE]` de SAVOIR par PATCH-DECISION.

### Non retenu : équipe d'agents simulée

Répartir direction artistique, rédaction et contrôle entre plusieurs agents du même modèle n'ajoute pas de regard indépendant (mêmes biais). La valeur d'une équipe tient à la critique et à l'itération : elle passe par la boucle existante (`DIRECTION/DOUBLE-LOOP`, captures, défaut dominant). À revoir seulement si la mini-épreuve montre que la boucle n'est pas suivie.

## 4. Exemple de référence : bilan `FABRICATION` attendu

Brief vague, HTML seul, vrai commerce :

```text
DESTINATION : produit réel (vrai commerce), enjeu identitaire moyen
MOYENS      : HTML/CSS/JS ; polices web ; aucune photo ; aucun logo ; contenu partiel
PLAFOND     : structure, typo, couleur, composants      → atteignable
              bon de commande, horaires (objet codé)     → atteignable
              photos des produits                        → non atteignable sans intrant
              logo                                       → limité (mot-symbole typographique)
              contenu (prix, horaires, adresse)          → non atteignable sans le commerçant
DÉCISION    : construire avec plafond déclaré ; aucune illustration figurative en SVG ;
              emplacements photo marqués « à fournir », cadrage indiqué
DEMANDES    : 1) 4 à 6 photos (téléphone, lumière du jour)  2) prix et horaires réels
              3) logo s'il existe — ou autorisation : banque sous licence, génération dirigée
```

En démo ou gabarit : approximation permise, marquée illustrative.

## 5. Séquencement

| Étape | Contenu | Touche `package/` ? | Porte |
|---|---|---|---|
| 1 | Atlas v0 (E'), fiche vague 3 (D'), brouillon de la carte des moyens (H) dans `plans/` | Non | — |
| 2 | **Mini-épreuve V1.2** sur B-DLA : vérifie si A (bilan, plafond) et D (`MODAL`/`PARTI`) sont suivis | Non (utilise B05) | Lecture |
| 3 | PATCH-DECISION « V1.2 lot 2 » : G, H, I, D', informée par l'étape 2 | Oui, sur B05 | G2 puis G3 |
| 4 | Épreuve G4 (4 briefs, juges extérieurs si disponibles) | Non | G4 |

**Mini-épreuve (étape 2), conditions proposées :**
- **C3** : brief vague + B05, 2 rendus ;
- **C3r** : même brief + « c'est pour mon vrai commerce », 1 rendu. Teste la déclaration de plafond en destination réelle ;
- comparaison avec les 6 rendus B-DLA existants (même modèle) ;
- juge neuf, **brief riche intégral**, captures avec défilement.

Coût estimé (probable) : 3 runs d'environ 190 000 tokens et un juge d'environ 160 000.

## 6. Critères

**Réussite de l'étape 2 :**
- bilan `FABRICATION` présent et **différent** entre C3 et C3r (sinon : rituel) ;
- en C3r : aucune illustration figurative dessinée en SVG ; emplacements marqués et demandes listées ;
- objet de preuve codé dans la première scène ;
- `PARTI` explicite ; palette hors du modal, ou modal gardé par décision écrite ;
- paires C3 contre C1 et C4 : au moins égalité.

**Arrêt :**
- bilan absent ou identique d'un run à l'autre : revoir A avant tout lot 2 ;
- agents qui ignorent la destination réelle et dessinent quand même : la règle ne suffit pas, chercher un mécanisme (par exemple une vérification sur capture) ;
- **budget :** tout ajout du lot 2 est payé par des coupes ou placé dans `SAVOIR` (chargé à la demande) ; aucune hausse nette du budget d'un run `DIRECTION` (`V12_Budget_lecture.py`).

## 7. Décisions attendues de l'owner

| # | Décision | Recommandation |
|---|---|---|
| 1 | G : objet de preuve codé, règle ou recommandation ? | **Recommandation** (« de préférence »), pas une obligation : certains produits ont un asset réel plus fort |
| 2 | H : nommer des sources et outils, malgré la décision 4 ? | **Oui**, sources seulement (pas de styles), `[VEILLE]` daté, dans SAVOIR |
| 3 | I : traitement des assets moyens ? | **Oui**, technique dans `SAVOIR/CRAFT`, justifiée par la thèse |
| 4 | Équipe d'agents simulée ? | **Non** pour V1.2 (§3) |
| 5 | Mini-épreuve : C3 (×2) + C3r (×1) ? | **Oui**, avant le lot 2 |
| 6 | Étape 1 (atlas, vague 3, carte des moyens) maintenant, dans `plans/` ? | **Oui**, coût faible, aucun effet sur le package |

## 8. Lecture

- **Certain :** avec un brief vague et du HTML seul, les assets figuratifs et le contenu réel ne peuvent pas atteindre le niveau senior ; les autres couches le peuvent.
- **Probable :** orienter la première scène vers un objet codé, déclarer le plafond et traiter les assets moyens rapproche le premier rendu du niveau des meilleures pièces revues.
- **Hypothétique :** que les agents respectent réellement le bilan et s'arrêtent pour demander. C'est l'objet de l'étape 2.
