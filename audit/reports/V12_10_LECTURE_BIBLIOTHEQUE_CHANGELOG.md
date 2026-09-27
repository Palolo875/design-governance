# V1.2 — Unité 10 — Lecture intégrale de BIBLIOTHEQUE.md et de CHANGELOG.md (B05)

**Date :** 2026-09-27 · **Lecteur :** même modèle que l'auteur des patchs (auto-comparaison)
**Objet :**
- BIBLIOTHEQUE.md : 818 lignes, 9 195 mots ;
- CHANGELOG.md : 101 lignes, 1 552 mots.

Ce sont les deux dernières sources normatives non lues.

**Question :** mêmes objectifs que `V12_05` à `V12_09`. Question propre à cette unité : **la structure aide-t-elle à composer du beau, et sert-elle tous les contextes visés par l'owner ?**

## 1. Carte de BIBLIOTHEQUE

| Lignes | Bloc | Mots | Nature |
|---|---|---|---|
| 1–67 | Responsabilité, **entrée prioritaire (à lire avant le catalogue)**, orientation, charges de lecture, contrat par périmètre | 1 093 | Méta |
| 70–158 | `READ` : chaîne support → grille → scène → objet → primitive ; lecture expressive ; **`TENSION`** ; **`SIGNATURE`** ; thèse structurelle et premier objet habitable ; préfixes ; types de preuve | 1 332 | **Génératif** + méta |
| 161–258 | `SELECT` : filtre avant catalogue, fast-path, questions de sélection, sélection par mode, one-shot et boucle, **`DERIVE`**, **signaux de convergence structurelle** | 1 502 | **Génératif** + trace |
| 262–290 | `CONTRACTS` : contrat de route (18 champs) | 507 | Gouvernance |
| 294–614 | **Catalogue** : 4 supports, 6 grilles, 6 scènes, 9 objets, 7 micro-interfaces, 3 modificateurs | 2 543 | **Vocabulaire de composition** |
| 618–684 | `COMPONENTS` : couches, contrat de composant, `BRAND_GRAMMAR` (15 champs) | 419 | Système |
| 688–720 | `COMPAT` : matrice de combinaisons | 397 | Aide à la sélection |
| 724–756 | `GATE` structurel (11 tests) | 630 | Contrôle |
| 760–818 | `EVOLUTION`, contrat de gain, test de sortie | 764 | Gouvernance |

**Mesures (certain) :**
- 104 négations défensives ;
- **175 jetons internes distincts**, le plus haut du système : c'est le catalogue de noms de routes ;
- « beau / joli » : 2 occurrences ;
- **64 noms de champs** de trace dans 8 blocs de code ;
- répartition approximative : génératif (`READ`, `SELECT`) ≈ 31 %, catalogue ≈ 28 %, gouvernance et contrats ≈ 41 %.

## 2. Ce qui est solide

1. **L'entrée prioritaire est en tête** (l.22), « à lire avant le catalogue ». C'est le seul fichier source dont l'ordre suit sa propre consigne (contraste avec `V12_05` §3.1).
2. **La phrase d'ouverture** (l.66) : « L'interface ne commence ni avec une landing premium, ni avec une grille de cartes, ni avec une image inspirante. Elle déclare d'abord **où elle vit**, **comment le regard circule**, **quelle preuve devient tangible** et **comment la personne agit**. » C'est la meilleure définition du travail de composition du système.
3. **`TENSION`** (l.88-104). Sept axes observables (densité, foyer, position de la preuve, temporalité, matière du champ, navigation, action). Il faut en choisir un ou deux **avant** la route. Un vrai outil génératif, positif et court (208 mots).
4. **La lecture expressive de la structure** (l.84) : calme ou tension, intimité ou monumentalité, précision ou spontanéité, collection ou instrument. Un vocabulaire positif pour **viser** un caractère, pas seulement pour éviter un défaut.
5. **Les signaux de convergence structurelle** (l.245-256). Six compositions convergentes avec leur **question de reprise** :
   - trois cartes égales sous un titre centré ;
   - hero et double CTA ;
   - split 50/50 sans mécanisme ;
   - plinthe de logos avant la preuve ;
   - capture produit sans état ;
   - grille répétitive sans priorité.

   C'est le **`MODAL` structurel** : ce que le lot 1 demande de nommer, déjà écrit, et formulé en questions positives.
6. **Des tests perceptifs concrets :**
   - test de support : masquer texte et images, le cadre doit encore indiquer un parti ;
   - silhouette au flou ;
   - non-généricité : « pourrait-elle appartenir à cinquante produits ? » ;
   - test de scène : échoue si elle reste `titre + sous-texte + CTA + image décorative`.
7. **Le catalogue** : chaque route a « choisir lorsque / éviter lorsque / preuve ». C'est un vocabulaire de composition partagé, concret, avec contre-indications (`FREE_FIELD`, `COLLECTION_PLINTH`, `EDITORIAL_FIELD`, `SPLIT_PROOF`…).
8. **`DERIVE`** : inventer une forme locale en changeant **un seul levier principal** (l.243), sans créer de route. Cohérent avec « un axe à la fois » (ORCHESTRATION_MAP).
9. **Le refus des routes « peau »** (l.243) : pas de `SCENE/BENTO`, `SCENE/GLASS_HERO`, `SCENE/EDITORIAL_PREMIUM`. Le système refuse de canoniser une tendance.

## 3. Problèmes observés

### 3.1 BIBLIOTHEQUE est hors du chemin `DIRECTION`, alors qu'elle s'y dit requise (certain)

- **BIBLIOTHEQUE/SELECT, « sélection par mode »** (l.196) : en `DIRECTION`, « évaluer `SUPPORT`, `GRID`, `SCENE` et objet de preuve, puis ne retenir que les niveaux qui changent la décision ».
- **Le Creative Boot** exige `STRUCTURAL-TENSION` (`BIBLIOTHEQUE/TENSION`) et `STRUCTURAL-SIGNATURE`.
- **Or aucune des six listes de chargement `DIRECTION`** (`V12_08` §3.3) ne charge BIBLIOTHEQUE. Seul le boot nomme le locator `TENSION` ; `SIGNATURE`, `SELECT`, les signaux de convergence et le catalogue ne sont chargés nulle part par défaut.

**Conséquence (probable) :** l'agent remplit `STRUCTURAL-TENSION` et `STRUCTURAL-SIGNATURE` sans les axes ni le catalogue. Il ne voit pas non plus les six signaux de convergence, alors que c'est la meilleure liste de `MODAL` structurel du système. C'est le même mécanisme que `V12_09` §3.1 : **le savoir-faire existe, le chemin ne le charge pas**.

### 3.2 Un catalogue centré sur le produit numérique, pas sur les contextes visés (certain pour le contenu ; probable pour l'effet)

- Sur **16 unités locales** (9 objets, 7 micro-interfaces), **au moins 11 relèvent du produit numérique ou du B2B** :
  - `SYSTEM_DATA_MODULE`, `PROOF_PRODUCT_STAGE`, `CONTROL_VALUE_TILE`, `CONVERSION_CONTEXT_FIELD`, `NAV_CONTEXT_CAPSULE` ;
  - `QUERY_HEALTH`, `ENTITY_STATUS_RAIL`, `USAGE_LEDGER`, `SETTINGS_GROUP`, `IDENTIFICATION_GATE`, `ITINERARY_SEGMENTS`.
- Trois scènes sur six sont applicatives (`INSTRUMENT`, `OPERATING_GRID`, `PRODUCT_NARRATIVE`).
- **Rien n'est prévu pour le commerce de proximité, la restauration, l'artisanat, la culture locale ou le service** : carte et prix, horaires et lieu, commande par message, galerie de produits réels, avis, contact. Aucun de ces mots n'apparaît dans le fichier.
- Pour B-DLA (boulangerie à Douala), les seules routes utilisables étaient `FREE_FIELD`, `COLLECTION_PLINTH`, `EDITORIAL_FIELD`, `EDITORIAL_SELECTION` et `MEDIA_ARCHIVE`, **toutes du registre éditorial**.

**Hypothèse :** pour une petite entreprise, le catalogue oriente vers l'éditorial, donc vers la vague 2 (même mécanisme que `V12_09` §3.4). Les routes sont toutes `SEED`, « sans gain mesuré » (CHANGELOG l.74) : ce sont des propositions d'auteur, pas des structures éprouvées.

### 3.3 La texture du catalogue recouvre les marqueurs de vague (certain pour le texte ; hypothèse pour l'effet)

- `MODIFIER/PRINT_FIELD` (« grain, trame, aplat, bordure ou hachure ») recouvre des marqueurs des vagues 2 et 3 (tramage, hachures de plan).
- `SUPPORT/ARCHITECTED_FRAME` (« bordures, axes, lignes ou seuils ») et `GRID/BASELINE` (« précision éditoriale ») décrivent aussi l'esthétique « éditoriale construite » des références de designers en 2025-2026.

Ce n'est pas une contradiction : les marqueurs servent à **nommer**, jamais à interdire. Mais aucun renvoi ne relie `PRINT_FIELD` aux marqueurs. Un agent qui choisit `PRINT_FIELD` ne sait pas qu'il choisit un marqueur de vague, et donc ne le déclare pas dans `PARTI`.

### 3.4 Instrumentation d'audit dans le chemin d'un run (certain)

- **« Charges de lecture à ne pas confondre »** (l.43-52) : « **Déclare dans la trace** la nature de chaque lecture structurelle effectivement lue » (`STARTUP-NOMINAL`, `CONDITIONAL-READ`, `AUDIT-READ`, `ACTUAL-READ`). C'est un outil de mesure de l'audit (`DIRECTION`, lecture instrumentée) imposé au run.
- **64 champs de trace** dans BIBLIOTHEQUE :
  - tension (7) ;
  - signature (4) ;
  - dérivation (17 lignes) ;
  - contrat de route (18) ;
  - grille (6 + 7 `MOBILE-*`) ;
  - objet (10) ;
  - avant/après (8) ;
  - composant (13) ;
  - `BRAND_GRAMMAR` (15) ;
  - compatibilité (6) ;
  - gain (7).

  La plupart ne servent qu'à la promotion d'une route, un cas rarissime en run. Ils sont pourtant dans les mêmes sections que les outils génératifs.
- **Cinq statuts de cycle de vie** (`SEED`, `PILOT`, `ADOPTED`, `DEPRECATED`, `ABANDONED`) s'ajoutent aux 37 valeurs relevées en `V12_06`.

### 3.5 Doublons (certain)

| Contenu | Lieux |
|---|---|
| Handoff à 12 champs | l.39 et l.199 : **6ᵉ et 7ᵉ copies** (ACTION, READING_MAP, SKILL, SAVOIR FND-03) |
| One-shot « stratégie de préparation, pas une absence de jugement » | l.203 ≈ SAVOIR l.205 |
| Boucle structurelle | l.205 : **9ᵉ description** de la boucle |
| « Zéro route est valide » / « `N/A-JUSTIFIED` n'est pas une sortie de confort » | l.27, l.102, l.104, l.171, l.173 |
| « Ne crée ni gate, ni statut, ni verdict » | l.33, l.199, l.288, l.720, l.726-728, l.746, l.750 |
| « Une chaîne de routes n'est pas une preuve » | l.29, l.754, l.817 |

### 3.6 Un quatrième gate qui dit ne pas en être un (certain)

`BIBLIOTHEQUE/GATE` compte 11 tests et renvoie aux statuts d'ACTION. Il se déclare trois fois non concurrent : « pas un quatrième gate global » (l.726), puis « ni statut ni verdict propres » (l.728 et l.750). Son test de non-généricité délègue explicitement à `ACTION/GATE-C`. En pratique, c'est un gate de plus à parcourir, et ses tests recoupent Gate A (accessibilité, états) et Gate C (non-généricité, silhouette).

### 3.7 Mineurs (certain ; signalés, non corrigés)

1. **Autre énoncé du chemin** : `SELECT` (l.163) et l.37 disent « après `DIRECTION/START` et, si un registre doit être choisi, après `SAVOIR/STYLE` » : un 7ᵉ ordre de lecture (`V12_08` §3.4, `V12_09` §4).
2. **`SCENE/INSTRUMENT` « champ expressif et panneau de mesure »** : la description est si courte qu'elle ne permet pas de choisir sans exemple. Même remarque pour plusieurs objets (`CONVERSION_CONTEXT_FIELD`).
3. **Les noms de routes** (`COLLECTION_PLINTH`, `ARCHITECTED_FRAME`…) sont des jetons anglais dans un corpus français. Les noms ne sont pas le problème (convention) ; les descriptions sont françaises, c'est cohérent.

## 4. CHANGELOG

**Solide :**
- l'efficacité est `NOT-VERIFIED` à chaque version, et le lot V1.2 dit même « V1.1.1 ≈ sans système » ;
- le cycle de vie des routes est clair ;
- l'erratum V1.1.0 est assumé (l.27).

**À relever :**
1. **L'entrée « Non publié » (l.11), écrite par nous au lot 1**, reprend la prise de brief compressée : « au plus trois demandes, dans l'ordre contenu réel, marque, asset principal, destination ». La condition « destination si elle n'est pas évidente » est perdue ici aussi (`V12_08` §3.6). **Signalé, non corrigé.**
2. **Le CHANGELOG déclare déjà la limite des gardes** (l.38) : « une divergence hors de cette liste n'est pas détectée ». Le constat de `V12_08` §3.3 (six listes de chargement divergentes, gardes vertes) est donc une **limite connue et déclarée depuis V1.1.0**, pas une découverte. La nouveauté est son ampleur sur le chemin `DIRECTION`.
3. **« Version publique : V1.1.1 »** en tête d'un fichier qui porte une section « Non publié » : correct pour B05, à relever au passage en V1.2.0.
4. **Historique des conditions de façade** : 21 → 42 → 50. Chaque version ajoute des gardes de phrases et n'en retire aucune. C'est le mécanisme d'accrétion (`V12_08` §4) écrit noir sur blanc.

## 5. Écart aux objectifs

| Objectif | État dans BIBLIOTHEQUE | Écart |
|---|---|---|
| Machine à faire du beau | Tension, signature, lecture expressive, signaux de convergence, tests perceptifs, catalogue | Hors du chemin `DIRECTION` (§3.1) |
| Tous contextes, personnes lambda | Catalogue riche en produit numérique | Commerce local, culture, service absents (§3.2) |
| Anti-slop vivant | Signaux de convergence, refus des routes « peau » | `PRINT_FIELD` sans lien aux marqueurs (§3.3) |
| Économe | Entrée prioritaire, filtre avant catalogue, « zéro route valide » | 64 champs, instrumentation d'audit, doublons (§3.4-3.5) |

## 6. Pistes (à décider, rien n'est appliqué)

1. **Mettre dans le noyau** (skill) les trois outils structurels :
   - la phrase d'ouverture (où elle vit, comment le regard circule, quelle preuve, comment on agit) ;
   - les sept axes de tension ;
   - les six signaux de convergence avec leur question de reprise, qui sont le `MODAL` structurel.

   Le catalogue reste une référence à la demande.
2. **Élargir le catalogue** aux contextes de l'owner (commerce de proximité, restauration, artisanat, culture, service local), **à partir de runs réels**, en statut `PILOT`, selon `EVOLUTION`. Pas par invention d'auteur.
3. **Relier `PRINT_FIELD` aux marqueurs** : un renvoi d'une ligne (« recouvre des marqueurs de vague datés ; à nommer dans `PARTI` »).
4. **Sortir du chemin de run** l'instrumentation de lecture (`STARTUP-NOMINAL`…) et les contrats de promotion (route, `BRAND_GRAMMAR`, gain) : ils vont dans une annexe « maintenance du catalogue ».
5. **Fusionner `BIBLIOTHEQUE/GATE` dans Gate C** (structure) et Gate A (accessibilité, états), ou le présenter comme une simple liste de tests perceptifs.
6. **Corriger l'entrée CHANGELOG « Non publié »** en même temps que la prise de brief (piste 5 de `V12_08`).

## 7. Lecture

- **Certain :**
  - les mesures ;
  - l'absence de BIBLIOTHEQUE dans les six listes de chargement `DIRECTION` alors que `SELECT` et le boot l'exigent ;
  - la composition du catalogue (11 unités sur 16 orientées produit numérique, aucune pour le commerce local) ;
  - l'instrumentation d'audit dans le chemin ;
  - les doublons ;
  - la prise de brief compressée dans le CHANGELOG ;
  - la limite des gardes déjà déclarée depuis V1.1.0.
- **Probable :** que l'agent remplisse tension et signature sans l'outillage ; que le catalogue oriente les petites entreprises vers l'éditorial.
- **Hypothétique :** l'effet de `PRINT_FIELD` et des supports « construits » sur la convergence vers les vagues 2 et 3 ; l'effet d'une remontée des outils structurels dans le noyau.
- **Limite :** lecture en auto-comparaison ; aucun regard extérieur.
