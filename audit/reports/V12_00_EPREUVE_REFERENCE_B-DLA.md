# V1.2 — Unité 00 — Épreuve de référence B-DLA (clôture)

**Date :** 2026-09-26 · **Owner :** Junior (Kamel) · **Protocole :** `plans/Protocole_Epreuve_Reference_V1.2.md` (v2, §11)
**Statut : clôturée sans J1 par décision de l'owner.** Seul un modèle a jugé : c'est une **orientation déclarée en auto-comparaison**, pas une preuve. La réserve n° 1 (efficacité `NOT-VERIFIED`) reste entière.

## 1. Ce qui a été fait

- 6 rendus, brief B-DLA (boulangerie, Douala) : C1 sans système, C2 brief riche et 5 vraies photos, C4 V1.1.1 ; 2 répétitions chacun. Producteurs : sous-agents neufs, modèle de la session, consignes identiques mot pour mot hors brief et ligne C4.
- Captures 1440 et 390 px pleine page ; aucune erreur JavaScript ni débordement horizontal.
- Jugement : J2a et J2b (Sonnet, sans contexte). J1 (owner) non réalisé.
- Pièces : `plans/epreuve_reference/B-DLA/` (rendus A à F, captures, grille J1 non remplie, archive des traces).

**Clé :**

| Condition | Rép. | ID producteur | Étiquette J1 |
|---|---|---|---|
| C1 | 1 | R57C3 | A |
| C1 | 2 | RBCC1 | E |
| C2 | 1 | R2AD5 | F |
| C2 | 2 | RFE26 | D |
| C4 | 1 | RF099 | C |
| C4 | 2 | RA8F0 | B |

## 2. Résultats

### Mesures mécaniques (certain)

| Mesure | C1 | C2 | C4 |
|---|---|---|---|
| **M4** lignes de règles chargées | 0 | 0 | **805 et 965** (estimation antérieure : environ 1 300) |
| Tokens du producteur | 88 k, 101 k | 102 k, 101 k | **190 k, 188 k** (environ ×2) |
| Durée | 280 s, 396 s | 269 s, 358 s | 512 s, 599 s |
| Questions consignées | 11, 10 | 6, 6 | 10, 10 |
| Mentions « exemple / fictif / à renseigner » dans la page | **0, 0** (tout inventé) | 0, 0 (contenu fourni) | **3, 10** |
| **M2** fond de page | crème, environ `#F5EDE0` | crème | crème |

**M2 — convergence :** les 6 rendus, toutes conditions confondues, ont le même fond crème et un texte brun foncé. Ni V1.1.1 ni le brief riche avec vraies photos n'ont fait sortir de la palette modale. Les polices varient davantage (Jaccard intra-condition de 0,20 à 0,33), mais les deux rendus C1 ont la même police de titre (Young Serif).

### Jugement par paires (J2, auto-comparaison)

| Paire | J2a | J2b |
|---|---|---|
| C1 contre C4, rép. 1 (R57C3 / RF099) | C1 | égal |
| C1 contre C4, rép. 2 (RBCC1 / RA8F0) | C4 (« plus honnête, respecte le ton ») | C1 (« direction artistique plus aboutie ») |
| C1 contre C2 (×2) | *invalide* | C1, C1 |
| C2 contre C4 (×2) | *invalide* | C4, C4 |

- **C1 contre C4 :** C1 gagne 2 fois, C4 1 fois, 1 égalité. Les deux juges se contredisent sur les deux paires : l'accord (M5) est nul.
- **C2 :** perd ses 4 paires en J2b, mais ces paires sont **biaisées** (voir §3, écart 3).
- **Vérité (M3) :** comptes instables entre J2a et J2b (C1 : 2 défauts « b » par rendu en J2a, 0 en J2b). Seul point constant, confirmé mécaniquement : **les rendus C4 signalent leur contenu d'exemple, les rendus C1 non**.

## 3. Écarts déclarés

1. **Pas de J1, aucun juge D3.** Décision de l'owner. Le résultat oriente, il ne prouve rien.
2. **Captures défectueuses, puis corrigées.** Ma première capture ne faisait pas défiler la page : les images à chargement différé des deux rendus C2 restaient vides (2 à 9 % des pixels). Correction : défilement, puis attente des images. J2a est invalide pour les 4 paires impliquant C2.
3. **Besoin du juge incomplet.** J'ai donné au juge un résumé du brief riche au lieu du brief intégral ; il omettait « ouverte en 2019, deux fours, six employés » et « une phrase d'accueil en anglais est la bienvenue ». J2b reproche aux rendus C2 précisément ces deux points. **Les paires C2 sont biaisées contre C2 ; Q2 n'est pas lisible.**
4. **Vérification inégale par les producteurs.** La consigne « ne rien écrire hors du dossier » a empêché 3 producteurs sur 6 de voir leur page dans un navigateur ; les 2 runs C4 et 1 run C2 l'ont fait. Un producteur C1 a écrit un fichier temporaire hors dossier, puis l'a supprimé (déclaré).
5. **Branche.** Travail sur `claude/init-repo-claude-md-gm6njm`, seule branche où la session peut pousser (CLAUDE.md §6 prévoit une branche par unité).
6. **Coordonnée personnelle.** Lors de la collecte des photos, l'adresse e-mail de l'owner a été envoyée une fois à l'API de Wikimedia dans l'identifiant de requête, puis retirée. Déclaré à l'owner.

## 4. Lecture (certain, probable, hypothétique)

- **Certain :** un run V1.1.1 coûte environ deux fois plus de tokens et charge 800 à 950 lignes de règles. Il rend le contenu d'exemple explicite ; sans système, l'agent invente tout sans le dire. Aucune condition ne sort de la palette crème.
- **Probable :** sur la qualité perçue, **V1.1.1 ne se distingue pas de C1** (C4 ≈ C1 : 1 victoire, 2 défaites, 1 égalité ; juges en désaccord). Son gain observable porte sur **l'honnêteté**, pas sur la qualité visuelle.
- **Hypothétique :** l'hypothèse « les intrants sont le levier » (Q2) n'est **pas testée** (biais de l'écart 3). Signal faible et contraire, à vérifier : J2b qualifie les vraies photos Wikimedia de « photos de stock » et préfère les illustrations SVG. Une photo réelle mais générique pourrait ne pas suffire à monter le niveau perçu.

## 5. Conséquences proposées pour V1.2

Selon la table §7 du protocole, la ligne « C4 ≈ C1 » dit : suspendre G3, revoir le diagnostic ou alléger. Compte tenu de la faiblesse de la preuve, je propose plutôt à l'owner :

1. **Ne pas suspendre la rédaction de la PATCH-DECISION A, B, D**, mais exiger qu'elle **allège** : le coût ×2 est mesuré, l'effet sur la qualité ne l'est pas.
2. **Chantier D (anti-slop vivant) : la réponse modale est maintenant observée.** Fond crème et brun, serif de caractère pour les titres, dans 6 rendus sur 6. C'est l'entrée concrète de la réponse `MODAL / PARTI`.
3. **Garder ce qui marche :** le signalement du contenu d'exemple est le seul gain constant de V1.1.1 ; aucun chantier ne doit l'affaiblir.
4. **Pour G4 :** donner aux juges le brief riche intégral, capturer avec défilement, et ne pas interdire aux producteurs l'usage d'un navigateur.

## 6. Non-régression

`package/` et `reference/` non modifiés ; B01 218/218 en début et en fin d'unité.
