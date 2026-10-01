# V1.2 refonte — R10, palier exploratoire (6 cas) : lecture

**Date :** 30-09-2026.
**Protocole :** `plans/Protocole_R10_Palier_exploratoire.md`, critères écrits avant la production.
**Décisions de l'owner :**
- consigne « pas de run » levée pour ce palier ;
- 6 productions neuves ;
- juges modèles seulement ;
- brief B-SAAS validé.

**Pièces :** `plans/epreuve_reference/R10-EXP/` : rendus, captures, clé, traces, mesures mécaniques, consignes et résultats des juges, scripts.

**Statut : orientation en auto-comparaison.** Les juges sont des modèles de la même famille que le producteur, sans juge humain. Ce n'est pas une preuve : la réserve `NOT-VERIFIED` reste entière (décision 9).

## 1. Ce qui a été fait

**Production :**

| | C1 | C3 | C4 |
|---|---|---|---|
| Système | aucun | candidate V1.2 (`package/` à `64265da`) | V1.1.1 (`v1.1.1-import`) |

- 2 briefs vagues × ces 3 conditions = 6 cas.
- Producteurs : un sous-agent neuf par cas, sur le modèle de la session.
- Consigne de B-DLA mot pour mot. La seule différence est la ligne de système : celle de P1 pour C3, celle de B-DLA pour C4.

**Captures :** pipeline de P1 (défilement, attente des images, 1440 et 390 px pleine page), puis planches uniformes.

**Jugement :**
- par brief, deux juges modèles neufs, à l'aveugle ;
- étiquettes et ordre tirés au hasard pour chaque juge ;
- brief riche intégral ;
- chaque paire vue deux fois, côtés inversés.

## 2. Écarts déclarés

1. **Premier essai de production interrompu.**
   - À 18 h 41 UTC, la limite d'usage de la session (429) a coupé les 6 producteurs lancés en parallèle.
   - Les rendus partiels sont écartés, non jugés et conservés hors du dépôt.
   - Les 6 cas ont été refaits à neuf après la réinitialisation, avec les mêmes identifiants et consignes, par lots de deux à quatre.
2. **Second juge modèle.**
   - Le modèle prévu pour J2b (choisi par l'owner) a échoué : crédits épuisés, erreur 429.
   - Il a été remplacé par un second juge neuf du même modèle que J2a, avec d'autres étiquettes et un autre ordre. C'était l'alternative présentée à l'owner avant le lancement.
   - Conséquence : les deux juges partagent le même modèle, donc leurs accords peuvent venir d'un biais commun (probable).
3. **Notes sur 10 et non sur 5.** L'échelle de P1 est conservée pour la continuité ; le protocole §4 disait « de 1 à 5 ».
4. **Heure de capture.** Trois rendus B-DLA affichent un état qui dépend de l'heure de Douala (« prochaine fournée »). Les captures valent pour l'heure où elles ont été prises (environ 19 h 30 UTC).
5. **Décompte des faits inventés.**
   - Les juges ont parfois écrit dans la liste « verite » des phrases qui ne sont pas des défauts (« Aucun fait inventé… »).
   - Le compte brut n'est donc pas utilisé. Le §3.4 donne un compte **vérifié**, item par item, contre le brief et la page (§6.4 du protocole).

## 3. Résultats

### 3.1 Tenue technique (T) et problèmes évidents

Tenue technique, pour les 6 rendus (certain) :
- aucune erreur JavaScript ;
- aucun débordement à 390 px ;
- aucune image vide ;
- page de 34 à 49 ko, polices comprises dans la cible < 1 Mo ; *(erratum AP2, C35 : ce sont les octets du HTML seul ; voir §Erratum)*
- aucun langage du système visible sur la page.

| Critère | État |
|---|---|
| P-1 inutilisable | Non (certain) |
| P-2 fait inventé non signalé en C3 | Non (vérifié, §3.4) |
| P-3 compte rendu ou langage du système | Non (certain) |
| P-4 style maison | Non : polices de titre différentes (serif à empattements carrés contre grotesque) |
| P-5 coût | Non (§3.3) |
| P-6 C3 perd toutes ses paires contre C1 | Non |

**Aucun problème évident.**

### 3.2 Qualité (Q), accord des juges

Paires retenues : pour chaque juge, les deux sens de chaque paire concordent (24/24) : aucun biais de position observé.

| Brief | Paire | Juge JS | Juge JF | Tranchée ? |
|---|---|---|---|---|
| B-DLA | C1–C3 | C1 | C3 | indécise |
| B-DLA | C1–C4 | C1 | C4 | indécise |
| B-DLA | C3–C4 | C3 | C3 | **C3** |
| B-SAAS | C1–C3 | C3 | C3 | **C3** |
| B-SAAS | C1–C4 | C4 | C4 | **C4** |
| B-SAAS | C3–C4 | C3 | C4 | indécise |

- **Accord (M5) : 3 paires tranchées sur 6, soit 50 %.** C'est le seuil du protocole : résultat lisible mais faible.
- **C3 ne perd aucune paire tranchée.** Contre C1 : 1 victoire (B-SAAS) et 1 indécise. Contre C4 : 1 victoire (B-DLA) et 1 indécise. Sur les verdicts individuels, C3 l'emporte 3 fois sur 4 contre C1, et 3 fois sur 4 contre C4.

**Notes moyennes (4 notes par condition) :**

| Condition | Qualité | Adéquation | Premier au classement | Dernier au classement |
|---|---|---|---|---|
| C1 | 8,0 | 4,75 | 1 fois | 3 fois |
| C3 | 7,75 | 7,0 | 2 fois | 0 fois |
| C4 | 7,0 | 7,0 | 1 fois | 1 fois |

**Lecture (probable) :**
- **C1 plaît à l'œil, mais répond moins bien au besoin et invente** (§3.4).
- **C3 égale C4 en adéquation et le dépasse légèrement en qualité perçue.**
- Sur la boulangerie, les juges se contredisent sur C1 face aux deux systèmes.

### 3.3 Effort (E)

| Brief | Condition | Tokens | Durée | Outils | Lignes de règles lues (M4) | Vu dans un navigateur |
|---|---|---|---|---|---|---|
| B-DLA | C1 | 94 k | 4 min 18 | 6 | 0 | non |
| B-DLA | C3 | 159 k | 7 min 37 | 31 | 665 | oui |
| B-DLA | C4 | 173 k | 9 min 41 | 43 | 625 | oui |
| B-SAAS | C1 | 92 k | 3 min 58 | 6 | 0 | non |
| B-SAAS | C3 | 168 k | 8 min 36 | 31 | 466 | oui |
| B-SAAS | C4 | 232 k | 14 min | 52 | 900 | oui |

| Ratio | B-DLA | B-SAAS |
|---|---|---|
| C3/C1 | 1,69 | 1,82 |
| C3/C4 | 0,92 | 0,72 |

- **Compromis du protocole (§6.3) tenu (certain) :**
  - C3 ≤ C4 sur les deux briefs ;
  - C3 ≤ 2 × C1.
  - Coût de P1 : environ 1,7 × C1. La trace légère n'a pas baissé le coût de façon visible sur B-DLA (D-23, probable).
- **Le système fait voir la page (certain) :**
  - C3 et C4 ont tous vérifié leur page dans un navigateur ;
  - aucun C1 ne l'a fait.
  - C'est une partie du surcoût.

### 3.4 Honnêteté (H), compte vérifié

| Rendu | Faits inventés présentés comme vrais (vérifiés) | Exemples signalés (compte mécanique) |
|---|---|---|
| C1 B-DLA | environ 6 : adresse précise, numéro réel au lieu du format fictif, zones de livraison, provenances et distances, promesses de service, prix et horaires | 0 |
| C1 B-SAAS | environ 5 : grille de trois tarifs, badge « Le plus choisi », conformité Factur-X « couverte », fonctions affirmées, « Facturez en deux minutes » | 1 |
| C3 B-DLA | 0 : bandeau « Maquette », prix et nom « d'exemple » | 9 |
| C3 B-SAAS | 0 au sens de P-2 : prix signalé fictif par le bandeau et le pied de page. Limites ci-dessous | 8 |
| C4 B-DLA | 0 | 11 |
| C4 B-SAAS | 0 au sens de P-2 : tarif « indicatif, à confirmer ». Limites ci-dessous | 11 |

**Limites relevées par un juge sur deux (certain) :**
- **Fonctions inventées non marquées, en C3 comme en C4 B-SAAS :** rapprochement bancaire, Factur-X, export pour le comptable. Le bandeau déclare fictifs le nom, le tarif et les montants, mais pas les fonctions.
- **Prix mis en avant :** le tarif fictif figure dans un bouton du hero (C3) ou en tête de page (C4). Il est signalé, mais il ressemble à un fait établi.
- **Date réglementaire :** le rendu C3 B-SAAS affiche une date de la réforme de la facture électronique, datée « au 30/09/2026 ». Elle **n'a pas été vérifiée** dans cette unité.

**Lecture (certain) :** le marquage des exemples tient dans les deux systèmes. Sans système, l'agent invente et ne le dit pas, comme en B-DLA et en P1.

### 3.5 Reprises (R)

Reprises bloquantes, cumulées sur les deux juges :

| Condition | Reprises bloquantes |
|---|---|
| C1 | 11 |
| C3 | 5 |
| C4 | 6 |

**Défaut commun à C3 et C4 sur B-DLA (certain, relevé par les 4 verdicts) :**
- La page n'a ni numéro ni bouton WhatsApp : la commande s'arrête à « Copier le message ». L'adresse reste en blancs visibles (« Face à ..., carrefour ... »).
- Le brief riche demandait un numéro fictif affiché tel quel. Les producteurs ne le connaissaient pas.
- Mais l'action principale (commander par WhatsApp) est **absente**, et non marquée comme exemple.
- **Cause probable :** la règle du contenu d'exemple marqué (D-20) est appliquée en retirant l'élément inconnu, au lieu de le garder fonctionnel avec une valeur d'exemple signalée.
- C'est un défaut de fabrication, et le levier est identifiable : **D-25, signalé, non corrigé**.

### 3.6 Diversité et convergence (D)

**Convergence entre conditions (certain) :**
- **B-DLA :** les trois rendus, avec ou sans système, s'organisent autour des fournées et de l'heure de Douala (« prochaine fournée », « sorties du four »).
- **B-SAAS :** les trois rendus mettent une facture au centre, avec un tampon « Payée ».
  - Même police de titre dans les trois : une grotesque identique.
  - C3 et C4 portent le même nom provisoire (« Soldé »).
- **Fonds :** tous blanc cassé. Fin de la convergence Archivo de P1 (probable). *(erratum AP2, C36 : inexact pour deux rendus ; voir §Erratum)*

**Lecture :**
- **Probable :** la convergence vient du modèle producteur, pas du système : elle est la même sans système. **Le système ne la rompt pas.**
- La question de convergence (R8a) n'a pas produit de direction distincte de celle de C1. **D-21 et D-22 restent ouverts** sur leur effet.
- **Hypothétique :** la question de convergence ne compare qu'aux habitudes connues, et non à la première idée du modèle lui-même.

## 4. Lecture selon le protocole (§6)

- **Problème évident :** aucun.
- **Coût :** dans le compromis.
- **Qualité :** encourageante mais incertaine. Accord de 50 % ; écart d'au plus une paire tranchée par brief ; juges d'un seul modèle.
- **Selon §6.2 (certain, sur les critères écrits) :** les conditions sont réunies pour **passer à 18 productions**.

**Recommandation à l'owner :** d'abord traiter D-25, puis passer à 18. Deux raisons :
- D-25 est un défaut observé, reproduit sur les deux systèmes, qui touche l'action principale d'une page. Il pèserait sur chaque rendu des 18.
- Le protocole traite un problème évident avant la suite. D-25 n'en est pas un au sens des critères P-1 à P-6, mais sa correction est ciblée : garder l'élément fonctionnel avec une valeur d'exemple marquée. Elle peut précéder les 18 sans en changer la méthode.

**Alternative :** passer à 18 tout de suite, et corriger D-25 après.

**Ce que le palier ne dit pas :**
- rien sur l'efficacité réelle ;
- rien sur un public humain, puisque les juges sont des modèles de la même famille ;
- aucune variabilité intra-condition, avec un rendu par case.

## 5. Défauts signalés (inventaire)

| ID | Constat | Nature |
|---|---|---|
| **D-25** | Une valeur inconnue est retirée au lieu d'être marquée. Sur B-DLA, C3 et C4 perdent le bouton WhatsApp et l'adresse, qui est l'action principale | Probable ; correction ciblée à décider (lieu : bloc CONTENU du noyau, contenu d'exemple marqué de D-20 et `CNT-01` dans DIRECTION) |
| **D-26** | Des fonctions inventées pour un produit fictif ne sont pas couvertes par le marquage (C3 et C4 B-SAAS) | Probable ; limite du marquage |
| Convergence | Même concept, même police de titre et même nom dans toutes les conditions. Signal D-21 et D-22 non levé | Probable ; question de convergence à réexaminer, sans présumer la cause |

## Erratum (01-10-2026, unité AP2 de l'audit progressif externe)

Corrections de ce que les preuves permettent d'affirmer. Elles ne démontrent pas l'usage effectif des blocs compilés et n'annulent pas le signal de convergence.

- **C35, poids de page.**
  - Mesuré : les octets du fichier HTML, de 33 736 à 49 217.
  - Non mesuré : les polices. Chaque rendu en charge depuis l'extérieur (deux références par rendu).
  - « Polices comprises » est donc faux. Le poids réel de la page chargée est inconnu, et aucun dépassement de la cible n'est établi.
- **C36, fonds.**
  - Fond de `body` :
    - blanc cassé dans quatre rendus : C1 B-DLA `#FFFEFA`, C3 B-DLA `#F4F2EC`, C4 B-DLA `#FBF3E6`, C3 B-SAAS `#F3F4F1` ;
    - **blanc pur dans deux rendus** : C4 B-SAAS (`#ffffff` déclaré) et C1 B-SAAS (aucun fond déclaré, donc blanc par défaut du navigateur).
  - Les masses colorées, les champs et les premiers écrans n'ont pas été mesurés.
  - La convergence d'objet reste établie (fournées et heure de Douala ; facture et tampon « Payée »), ainsi que la police de titre commune sur B-SAAS.
  - La convergence de fond était surestimée.
  - Le modèle producteur reste une cause possible, sans exclusion des autres.
- **D-26, honnêteté.** « 0 fait inventé » s'entend **au sens de P-2** (prix, nom et montants marqués). Des fonctions affirmées d'un produit fictif restent hors du marquage, en C3 comme en C4 B-SAAS (§3.4, limites). Tout résumé de ce palier porte cette réserve.

