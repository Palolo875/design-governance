# Protocole — Épreuve de référence avant V1.2 (phase 0, en parallèle)

**Date :** 2026-09-26 · **Owner :** Junior (Kamel) · **Statut :** brouillon, à valider par l'owner avant toute production de rendu
**Base :** V1.1.1 (`package/`, étiquette `v1.1.1-import`), plan `plans/Plan_V1.2_Qualite_senior_gouvernance.md` §9 et §11.

---

## 0. Décision et écarts déclarés

- **Décision de l'owner (26-09-2026) :** option « en parallèle ». La PATCH-DECISION A, B, D se rédige normalement ; l'**application sur B05 (porte G3) attend la lecture de cette épreuve**.
- **Écart 1 — séquencement.** Le plan §11 place toute l'épreuve en phase 4. Ici, les conditions C1, C2 et C4 sont produites et jugées avant G3. C3 reste en phase 4.
- **Écart 2 — branche.** CLAUDE.md §6 prévoit une branche par unité (`v1.2/...`). La session n'autorise que `claude/init-repo-claude-md-gm6njm` ; le travail y est fait et le sera déclaré dans le rapport de l'unité.
- **Inchangé :** aucun fichier de `package/` ni de `reference/` n'est modifié. V1.1.1 est utilisée depuis une copie.

## 1. Questions tranchées

| # | Question | Comparaison | Ce que la réponse change |
|---|---|---|---|
| Q1 | V1.1.1 améliore-t-elle un rendu à brief vague ? | C4 contre C1 | Si non : ajouter du texte au même cadre est douteux ; revoir le diagnostic ou alléger d'abord |
| Q2 | Les intrants sont-ils le levier principal (diagnostic §2, « probable ») ? | C2 contre C1 et C4 | Si C2 domine nettement : A et B en tête, confirmés |
| Q3 | Les juges et la grille sont-ils fiables ? | Accord entre juges | Si non : corriger le protocole avant G4 |
| Q4 | Combien de lignes de règles un run V1.1.1 charge-t-il réellement ? | Mesure sur C4 | Donne le « avant » du budget de lecture (CLAUDE.md §6) |

## 2. Conditions

| Condition | Brief donné | Système | Assets |
|---|---|---|---|
| **C1** | Vague | Aucun | Aucun |
| **C2** | Riche | Aucun | Fournis par l'owner |
| **C4** | Vague | V1.1.1 (skill `design-governance-practice` + `V1/official/`, copie) | Aucun |

**Règles communes (identiques pour toutes les conditions) :**
- même modèle, noté avec la date ; session ou sous-agent neuf par rendu, sans contexte partagé ; aucun accès aux rapports d'audit ni au plan V1.2 ;
- livrable : **une page HTML unique et autonome** ; polices web autorisées ; **aucune image téléchargée** depuis le réseau (les seules images sont les assets fournis en C2 ou ce que l'agent dessine en CSS/SVG) ;
- **one-shot** : aucune réponse humaine. Toute question posée par l'agent est consignée, sans réponse, et l'agent poursuit sur hypothèses ;
- consigne, hors brief et hors ligne système de C4, **mot pour mot identique** (§4).

## 3. Briefs

Deux des quatre briefs du plan §9, pour que les rendus C1, C2 et C4 soient **réutilisables tels quels en G4** (voir §8).

| Code | Brief vague (C1, C4) | Brief riche (C2) : contenu attendu |
|---|---|---|
| **B-DLA** — commerce local, Douala | « Fais le site d'une boulangerie-pâtisserie à Douala. » | Nom réel ou plausible, quartier, offre et prix, horaires, public, ton, contraintes (mobile d'abord, réseau lent, WhatsApp comme canal de commande), 4 à 8 photos réelles |
| **B-SAAS** — produit SaaS | « Fais la page d'accueil d'un logiciel de facturation pour PME. » | Produit, cible, 3 fonctions réelles, preuve disponible (ou « aucune »), tarif, ton, captures d'écran du produit, logo |

**À fournir par l'owner :** les briefs riches définitifs et leurs assets (droits d'usage vérifiés). Le brief riche sert aussi de **référence de besoin** pour les juges (§5) et, en G4, de **feuille de réponses** pour l'intake simulé de C3.

## 4. Production

- **Volume :** 2 briefs × 3 conditions × 3 répétitions = **18 rendus**. Repli déclaré si le coût est trop haut : 2 répétitions (12 rendus), la mesure de diversité devient alors indicative.
- **Consigne commune** : « Voici un brief. Produis le rendu final, une page HTML unique et autonome, dans le fichier `index.html`. [BRIEF] » ; en C4, ajout d'une seule ligne en tête : « Applique Design Governance V1.1.1 (skill et sources fournies dans `dg/`). »
- **Captures** (Playwright, Chromium préinstallé) : 1440 × pleine page et 390 × pleine page, par rendu.
- **Anonymisation :** chaque rendu reçoit un identifiant aléatoire. La clé (identifiant → brief, condition, répétition) est **remise à l'owner et n'entre pas dans le dépôt** avant la fin du jugement.
- **Trace par rendu :** modèle, date, condition, questions posées, fichiers de règles lus et leur nombre de lignes (C4), durée.

## 5. Juges et exposition

- **Cible :** 3 à 5 personnes extérieures, dont au moins un designer ; critères D3 : relation externe ou collaborateur non impliqué, conflit déclaré.
- **Minimum viable :** avec 1 ou 2 juges extérieurs, l'épreuve se fait quand même ; le résultat oriente, il reste une réserve.
- **Ce que voit un juge :** le brief riche (le besoin réel) et des paires de captures anonymes. Jamais la condition, le système ni la clé.
- **Bloc d'exposition** (format du rapport 13.02), rempli pour chaque juge :

```text
REVIEWER-ROLE — juge de paires, épreuve de référence V1.2
REVIEWER-RELATION — <externe | collaborateur non impliqué | lié à l'owner>
CONFLICT — <aucun | déclaré : ...>
ARTEFACTS-REVIEWED — 18 paires de captures, briefs riches B-DLA et B-SAAS
REVIEW-EXPOSURE — aveugle à la condition ; aucun accès au système ni au plan
MAPPING-TIMING — clé révélée APRÈS la remise des jugements
LIMIT — <...>
```

## 6. Mesures

| Code | Mesure | Méthode | Nature |
|---|---|---|---|
| **M1** | Qualité perçue | Par brief : paires C1-C2, C1-C4, C2-C4, appariées par répétition → 9 paires par brief, **18 par juge** (environ 15 minutes). Question unique : « Lequel est le plus proche d'un travail de designer senior pour ce besoin ? », réponse « gauche / droite / égal ». Côté et ordre tirés au hasard | Jugement humain |
| **M2** | Diversité | Pour les 3 rendus d'un même brief et d'une même condition : polices, 5 couleurs dominantes, structure de l'écran d'accueil. Script déterministe à écrire (outil nouveau, déclaré) | Mécanique |
| **M3** | Défauts de vérité | Compte par rendu : métriques sans référence, faux logos ou clients, prestige inventé, copie recyclée (plan §3, principe 5). Compté à l'aveugle par l'owner ou un juge | Jugement borné |
| **M4** | Budget de lecture réel | Lignes de règles chargées par chaque run C4, lues dans la trace | Mécanique |
| **M5** | Accord entre juges | Part des paires où la majorité est nette | Mécanique |

Pas de test de significativité : l'échantillon ne le permet pas. On lit des taux de victoire et des écarts nets.

## 7. Lecture des résultats

| Résultat | Décision proposée à l'owner |
|---|---|
| C2 domine C1 et C4 nettement | Diagnostic des intrants confirmé : G3 ouverte, A et B prioritaires |
| C4 > C1, C4 < C2 | Scénario attendu : G3 ouverte, plan inchangé, référence mesurée |
| C4 ≈ C1 | V1.1.1 sans effet mesurable sur la qualité : G3 suspendue, revoir le diagnostic ou alléger avant d'ajouter |
| C4 < C1, ou M3 plus élevé en C4 | Alerte : le système nuit ; G3 suspendue, analyse |
| M5 faible (juges en désaccord) | Résultat non lisible : corriger la grille ou les briefs avant G4 |
| M2 : C4 moins divers que C1 | Signe de style maison dès V1.1.1 : à traiter avant les chantiers C et E |

## 8. Réutilisation en G4 et limites

- **Réutilisation (probable) :** si le modèle ne change pas avant G4, les 18 rendus C1, C2 et C4 servent tels quels ; seuls les rendus C3 restent à produire, et deux briefs à ajouter. Si le modèle change, C1, C2 et C4 sont régénérés : la comparaison n'est valable qu'à modèle égal.
- **Limites (certain) :** N petit ; deux genres seulement ; un seul modèle ; le producteur est un agent instruit par l'auteur du plan. Le résultat **oriente** la porte G3, il ne prouve pas une efficacité générale et ne lève pas la réserve n° 1 à lui seul.

## 9. Critères de l'unité

- **Réussite :** 18 rendus (ou 12, repli déclaré) produits selon §2 à §4 ; au moins un juge extérieur ; M1 à M5 calculées ; décision G3 proposée selon §7 ; rapport dans `audit/reports/`.
- **Arrêt :** assets de C2 non disponibles (C2 sans vrais assets ne teste pas Q2) ; aucune personne extérieure disponible (on déclare une auto-comparaison et on ne l'utilise pas pour G3) ; une consigne diffère entre conditions après production (rendus à refaire).
- **Non-régression :** aucune modification de `package/` ; B01 218/218 vérifiée en début et fin d'unité.

## 10. Entrées attendues de l'owner

1. Valider ce protocole, ou l'amender.
2. Briefs riches B-DLA et B-SAAS, et leurs assets.
3. Noms et relation des juges (le recrutement peut commencer tout de suite).
4. Modèle producteur retenu, et 3 ou 2 répétitions.
