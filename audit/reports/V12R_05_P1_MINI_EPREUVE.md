# V1.2 refonte — Point de contrôle P1 — Mini-épreuve après le noyau (B-DLA)

**Date :** 2026-09-27 · **Décision :** l'owner a lancé P1 (« P1. »). **Protocole :** addendum §5 et §6, dans les conditions de l'épreuve B-DLA (`V12_00`). **Pièces :** `plans/epreuve_reference/B-DLA-P1/` (rendus, captures, clé, consignes et résultats des juges).

## 1. Ce qui a été fait

**Production :**
- 3 rendus sur le brief B-DLA vague, avec le package après R4 dans `dg/`, les consignes de production de B-DLA mot pour mot, et la seule ligne de système adaptée (« candidate V1.2 ») ;
- C3 ×2 : « Fais le site d'une boulangerie-pâtisserie à Douala. » ;
- C3r ×1 : même brief + « C'est pour mon vrai commerce. » ;
- producteurs : sous-agents neufs, modèle de la session.

**Captures :**
- les 3 nouveaux rendus et les 6 rendus B-DLA (C1, C2, C4) **recapturés avec le même pipeline** (défilement, attente des images, 1440 et 390 px) ;
- planches uniformes pour le juge.

**Jugement :**
- **deux juges neufs et indépendants** (Sonnet, sans contexte), à l'aveugle, avec des étiquettes et un ordre tirés au hasard différemment pour chacun ;
- **brief riche intégral** (correction de l'écart 3 de `V12_00`) ;
- pour chaque juge : notes par page (qualité, adéquation, vérité), 18 paires (chaque nouveau rendu contre chaque ancien), classement des 9.

## 2. Résultats

### Mesures mécaniques (certain)

| Condition | Tokens | Lignes de règles lues | Fond de page | Police du titre | Exemples signalés |
|---|---|---|---|---|---|
| C1 (sans système) | 88 k, 101 k | 0 | crème ×2 | Young Serif ×2 | 0, 0 |
| C4 (V1.1.1) | 190 k, 188 k | 805, 965 | crème ×2 | Ultra, Bricolage | 10, 2 |
| C2 (brief riche + photos) | 102 k, 101 k | 0 | crème ×2 | Archivo, Bricolage | 1, 6 |
| **C3 (V1.2 après R4)** | **173 k, 175 k** | **450, 647** | **blanc neutre ×2** | Archivo ×2 | **5, 7** |
| **C3r (vrai commerce)** | **155 k** | **407** | **blanc neutre** | Archivo | **2** |

Lecture :
- **Palette** : 3 rendus V1.2 sur 3 sortent de la palette crème, contre 6 sur 6 avant.
- **Charge** : les lignes de règles lues baissent de 40 à 50 %.
- **Coût** : environ 1,7 fois C1, contre 1,9 à 2 fois pour V1.1.1.
- **Vérité** : les exemples restent signalés.

### Jugement par paires (deux juges, auto-comparaison)

| V1.2 contre… | J3a | J3b | Total |
|---|---|---|---|
| C1 (sans système) | 5 victoires, 1 défaite | 4 victoires, 2 défaites | **9 victoires, 3 défaites** |
| – dont C3 seul (hors C3r) | 4 sur 4 | 4 sur 4 | **8 sur 8** |
| C4 (V1.1.1) | 1 victoire, 5 défaites | 4 victoires, 2 défaites | 5 victoires, 7 défaites (juges en désaccord) |
| – dont C3 seul | 1 sur 4 | 4 sur 4 | 5 victoires, 3 défaites |
| C2 (brief riche + photos) | 0 sur 6 | 0 sur 6 | **0 sur 12** |

- **Classements :** C2 est premier chez les deux juges. Chez J3b, les deux rendus C3 suivent immédiatement (3ᵉ et 4ᵉ). Chez J3a, C3 est 4ᵉ et 6ᵉ, derrière un rendu C4.
- **Qualité perçue** (notes sur 10) : C3 obtient 8 et 7 chez J3a, 8 et 9 chez J3b. C'est au niveau des meilleurs rendus faits sur brief vague (J3b : « prouesse de mise en scène… au niveau d'un designer senior »). L'adéquation est plus basse (4 à 7), faute de faits réels et de photos.
- **Vérité :** 0 fait inventé pour les 3 rendus V1.2 chez les deux juges. C1 : 1 à 3 faits inventés par rendu (« technique française », histoire, adresse d'aspect réel).
- **C3r, le plus faible** (J3a 8ᵉ, J3b 9ᵉ) :
  - en « vrai commerce » sans contenu, le producteur a laissé des emplacements à remplir (« nom de l'enseigne ») ;
  - sa vitrine compose une commande WhatsApp à plusieurs produits, que les deux juges ont lue comme une boutique en ligne, alors que le brief riche l'exclut.
  - Le rendu est honnête mais perçu comme un gabarit vide.

### Diversité (certain)

- **Palette :** sortie de la vague 2 (crème et brun) ×3.
- **Police :** nouvelle convergence, Archivo ×3.
- **Trame :** les **9 rendus**, avec ou sans système, suivent la même trame : fournées de la journée → vitrine avec prix → gâteaux de fête → venir. C'est le mode du modèle pour ce brief ; le noyau ne l'a pas fait bouger.
- **Nom :** un rendu C3 porte le même nom inventé qu'un rendu C1 de B-DLA (« Fournil du Wouri »).

## 3. Lecture

- **Probable** (deux juges du même fournisseur, auto-comparaison, N = 3) :
  - **le noyau améliore le rendu sur brief vague par rapport à l'absence de système** : 8 sur 8 pour C3, alors que V1.1.1 faisait jeu égal avec C1 ;
  - **il fait au moins aussi bien que V1.1.1** (5 victoires, 3 défaites pour C3, juges en désaccord) ;
  - il réduit la charge de 40 à 50 % et garde l'honnêteté.
- **Probable :** **les intrants restent le premier levier.** Avec le brief riche intégral donné aux juges, C2 gagne 12 paires sur 12. L'hypothèse Q2, non testable en `V12_00`, est cette fois soutenue.
- **Certain :**
  - le coût reste élevé (≈ 1,7 × C1 ; cible ≤ 1,3 ×) ;
  - la palette sort de la vague crème mais converge ailleurs (Archivo, blanc neutre) ;
  - la trame est identique pour tous.
- **Hypothétique :**
  - que la trace (captures B1b, `trace.txt`, statuts) explique l'essentiel du surcoût restant : c'est la cible de R5b (trace légère) ;
  - qu'une règle « en vrai commerce sans contenu, contenu illustratif marqué plutôt qu'emplacements vides » corrige C3r.
- **Limites :**
  - pas de juge D3 ; deux juges du même fournisseur, en désaccord sur C3 contre C4 ;
  - un seul brief ;
  - le résultat oriente, il ne prouve pas.

## 4. Défauts nouveaux (signalés, non corrigés)

| N° | Défaut | Lot proposé |
|---|---|---|
| D-20 | **Destination réelle sans contenu** : le producteur remplit la page d'emplacements vides. C'est honnête mais perçu comme un gabarit. Le noyau ne dit pas quoi préférer entre contenu illustratif marqué et emplacements. | R7 (décision de l'owner) |
| D-21 | **Nouvelle convergence de style** : Archivo et fond blanc neutre ×3. Les marqueurs de vague font sortir de la vague 2 sans ouvrir la diversité. | R8 (veille) et R10 (mesure de diversité) |
| D-22 | **Trame convergente du modèle** (fournées → vitrine → gâteau → venir), identique dans les 9 rendus. Les signaux de convergence du noyau sont génériques (SaaS) : ils ne détectent pas le mode propre au brief. | R5c ou R7 : faut-il une alternative située matérialisée sur brief vague, avec son coût ? |
| D-23 | **Coût encore à 1,7 × C1.** Les producteurs produisent encore captures B1b, trace et statuts, même sans run persistant. | R5b (trace légère, décision 11) |

## 5. Décision proposée

**Poursuivre la vague III** (R5), en y intégrant D-20 à D-23. Priorités :
- R5b (trace légère : le coût) ;
- les décisions D-20 et D-22 (R7) avant R10.

## 6. Non-régression

Aucun changement du package dans cette unité. B01 218/218.
