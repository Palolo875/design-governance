# Protocole R10 — Palier exploratoire (6 cas)

**Date :** 30-09-2026 · **Owner :** Junior (Kamel) · **Statut : écrit avant toute production.** Aucune production tant que l'owner n'a pas levé la consigne « pas de run ni d'épreuve » (plan de reprise §1).
**Hérite de :** `plans/Protocole_Epreuve_Reference_V1.2.md` (v2, §11) et de P1 (`audit/reports/V12R_05_P1_MINI_EPREUVE.md`). Seuls les écarts et les compléments sont écrits ici.
**Cadre :** plan de reprise, « R10 progressif » ; porte P2 franchie (`V12R_33`) ; décision 9 (`V12R_14`).

## 1. But et limites

- **But :** voir, sur deux briefs contrastés, ce qu'une lecture ne peut pas établir : la qualité de la première proposition, le coût, l'honnêteté et la variabilité de la candidate V1.2, face à C1 (sans système) et C4 (V1.1.1).
- **Ce que le palier ne dit pas (certain) :** avec un rendu par case, aucun résultat n'est une preuve d'efficacité. Le palier oriente vers la suite : corriger, passer à 18, ou s'arrêter. Il ne lève pas la réserve `NOT-VERIFIED`, et un juge modèle ne reçoit jamais le label D3.

## 2. Les 6 cas

| Brief | C1 (sans système) | C3 (candidate V1.2) | C4 (V1.1.1) |
|---|---|---|---|
| B-DLA « Fais le site d'une boulangerie-pâtisserie à Douala. » | 1 rendu | 1 rendu | 1 rendu |
| B-SAAS « Fais la page d'accueil d'un logiciel de facturation pour PME. » | 1 rendu | 1 rendu | 1 rendu |

- **Brief reçu par les producteurs :** le brief vague seul, dans les trois conditions. C2 n'entre pas dans ce palier : P1 a déjà montré l'effet des intrants (12/12).
- **Candidate C3 :** le `package/` du dépôt au commit de production. Son contenu doit être celui de la candidate après le raccord R11c (`cb669a6` + R11c) ; l'empreinte de l'arbre est consignée dans la clé.
- **C4 :** le `package/` de l'étiquette `v1.1.1-import`.
- **Où le système est posé :** dans les deux cas, copié dans `dg/` à côté du dossier de production, comme en B-DLA et en P1.

### Réemploi des références B-DLA C1 et C4 : vérification

Le plan autorise 4 productions au lieu de 6 si les références B-DLA C1 et C4 (`V12_00`, 26-09) restent comparables. Vérification sur les pièces (`plans/epreuve_reference/B-DLA/traces_et_cle_B-DLA.tar.gz`) :

| Élément | Constat | État |
|---|---|---|
| Consigne et brief | Consigne de production conservée mot pour mot (`prompts.json`) | Réutilisable (certain) |
| Modèle et version | Consigné « modèle de la session », sans identifiant (`traces.json`, et de même `cle_P1.json`) | **Non vérifiable (certain)** |
| Outils et capacités | Sous-agents neufs, dossier fermé. Les 2 rendus C1 n'ont pas été vus dans un navigateur, les 2 rendus C4 l'ont été (`vu_navigateur`) | Écart de condition connu, qui fait partie de C1 |
| Intrants | Brief vague seul, pas d'asset | Réutilisable (certain) |
| Limites de production | Une seule passe, personne ne répond aux questions | Réutilisable (certain) |
| Captures et mesures | Recapturées avec le pipeline de P1 (défilement, attente des images, 1440 et 390 px). Tokens, durée, questions et lignes lues consignés | Réutilisable (certain) |

**Conclusion (certain) :** on ne peut pas établir que le modèle est le même. Or, en C1, le modèle est la seule variable : un changement de modèle déplace toute la comparaison.

**Recommandation : 6 productions neuves.** Le surcoût est d'environ 290 k tokens, pour 2 productions de plus. Les références du 26-09 restent des pièces historiques, sans servir de comparateur.

**Option déclarée :** réemployer les références, avec un écart « modèle non vérifié » écrit dans chaque lecture.

## 3. Production

- **Consigne :** celle de B-DLA, mot pour mot (`prompts.json`, entrée C1), le brief remplacé selon le cas.
  - C3 ajoute une seule ligne en tête, celle de P1 (« candidate V1.2 »).
  - C4 ajoute la ligne de B-DLA (V1.1.1).
  - Toute autre différence de consigne rend le cas à refaire (arrêt du protocole §9).
- **Ce que la consigne teste (déclaré) :** « Personne ne répondra à tes questions » place les trois conditions dans le cas « humain absent » de la prise de brief. Le cas « humain présent » (demandes avant le build, décision G2 (a)) n'est pas testé par le palier : il relève de l'observation novice (§7).
- **Producteurs :**
  - un sous-agent neuf par rendu, sur le modèle de la session, le même pour les 6 cas ;
  - les 6 sont produits le même jour, dans un ordre tiré au hasard ;
  - l'identifiant du modèle est vérifié avant la production et consigné dans la clé, hors dépôt : aucun identifiant de modèle n'entre dans le dépôt.
- **Première proposition seulement.** Le palier juge le rendu d'une passe, qui est la première proposition au sens de `CHK-01`. Le résultat après corrections n'est pas produit : les reprises nécessaires sont mesurées par les juges (§4, R).
- **Captures :**
  - le pipeline de P1 (défilement, attente des images, 1440 et 390 px pleine page) ;
  - des planches uniformes (`B-DLA-P1/jugement/planches.py`) ;
  - un contrôle mécanique : erreurs JavaScript, débordement horizontal à 390 px, poids de la page.
- **Anonymisation :**
  - identifiant aléatoire par rendu ;
  - la clé reste hors du dépôt jusqu'à la remise de tous les jugements, puis entre dans le dépôt, comme en P1 ;
  - pièces dans `plans/epreuve_reference/R10-EXP/`.

## 4. Mesures par rendu

| Code | Mesure | Méthode | Nature |
|---|---|---|---|
| **Q** | Qualité de la première proposition | Paires par brief (C1–C3, C1–C4, C3–C4), soit 6 paires. Question du protocole : « Lequel est le plus proche d'un travail de designer senior pour ce besoin ? » (gauche, droite ou égal). Notes par page de 1 à 5 (qualité, adéquation, vérité) et classement par brief, comme en P1 | Jugement |
| **R** | Reprises nécessaires | Pour chaque page, le juge liste ce qu'il faudrait corriger avant de la montrer au client, classé bloquant, notable ou finition. On compte par classe | Jugement borné |
| **E** | Effort | Tokens, appels d'outils, durée, lignes de règles lues (M4). Ratios C3/C1 et C3/C4 par brief | Mécanique |
| **H** | Honnêteté | M3 (faits inventés et non signalés : prix, avis, chiffres, clients, prestige) compté à l'aveugle. Contenu d'exemple signalé : compte mécanique. Langage du système visible sur la page (`EXPLORATORY`, `MODAL`, « trace »…) | Jugement borné et mécanique |
| **D** | Diversité et convergence | Fond de page, police de titre, 5 couleurs dominantes, trame de l'écran d'accueil : entre les deux briefs d'une même condition, et comparés aux 3 rendus C3 de P1 (Archivo ×3, trame identique : D-21, D-22) | Mécanique |
| **T** | Tenue technique | Page unique autonome ; erreurs JavaScript ; débordement à 390 px ; poids (B-DLA : cible < 1 Mo, contrainte du brief riche) ; `questions.txt` | Mécanique |

**Brief riche des juges :**
- B-DLA : le brief riche de `briefs.md` ;
- B-SAAS : un brief riche fictif, proposé en annexe, à valider par l'owner. Il sert seulement de référence de besoin aux juges, car aucun producteur ne le reçoit dans ce palier.

## 5. Juges

- **Composition (décision 9) :**
  - des humains extérieurs (D3), si l'owner en recrute ;
  - J1 = l'owner, à l'aveugle sur la condition, avec la grille. Il connaît le style du système : exposition déclarée ;
  - J2a et J2b = deux juges modèles neufs, sans contexte, aux étiquettes et à l'ordre tirés au hasard séparément.
- **Écart déclaré :** la décision 9 prévoit des modèles « d'autres familles ». Cet environnement n'en offre pas : J2a et J2b sont de la même famille que le producteur et sont déclarés non indépendants, sauf si l'owner fournit un autre accès.
- **Contrôle du biais de position :** chaque juge modèle voit chaque paire deux fois, côtés inversés. Deux réponses contradictoires comptent comme « égal ». Coût : 12 jugements par juge modèle.
- **Ce que voit un juge :** le brief riche, les planches anonymes et la grille ; jamais la condition, le système, le plan ni le producteur. Un bloc d'exposition par juge (protocole §5).
- **Sans juge D3 :** le résultat est une orientation (décision 9) ; publier n'est alors possible qu'avec réserve et feu vert final.

## 6. Critères écrits avant de produire

### 6.1 Problème évident : on corrige d'abord

Le problème évident est un défaut de la candidate qu'on voit sans comparer finement. On le corrige par une PATCH-DECISION avant toute suite. Après correction, seul C3 est refait : C1 et C4 ne dépendent pas de la candidate.

| # | Problème évident | Mesure |
|---|---|---|
| P-1 | Un rendu C3 inutilisable : erreur JavaScript bloquante, débordement horizontal à 390 px, contenu principal absent ou image vide | T |
| P-2 | Un rendu C3 présente comme réel un fait inventé (prix, avis, chiffre, client) : un défaut M3 non signalé, vérifié contre le brief riche (§6.4) | H |
| P-3 | Un rendu C3 livre un compte rendu de cadrage au lieu d'une page, ou montre le langage du système au client final | H, T |
| P-4 | Les deux rendus C3 partagent à la fois la police de titre, le fond et la trame de l'écran d'accueil sur deux briefs de genres opposés (style maison) | D |
| P-5 | C3 coûte plus de 2,5 fois C1 ou plus que C4, sur au moins un brief | E |
| P-6 | Sur un brief, C3 perd toutes ses paires contre C1 chez tous les juges (aucune victoire, au plus une égalité) | Q |

Un seul problème évident suffit pour corriger d'abord. Pour P-4 et P-6, le diagnostic précède la correction : on examine consignes et ressources sans présumer la cause (plan, « si la diversité baisse »).

### 6.2 Ce qui justifie de passer à 18

- **Passer à 18** si trois conditions sont réunies :
  - aucun problème évident n'est ouvert ;
  - le coût est dans le compromis (§6.3) ;
  - les résultats sont encourageants mais incertains : C3 gagne ou fait jeu égal contre C1 et contre C4 sur la majorité des jugements, mais l'accord des juges est faible, ou l'écart net est d'au plus une paire par brief.
- **Ne pas passer à 18, diagnostiquer** si C3 perd nettement contre C1 ou contre C4 sur les deux briefs, avec des juges d'accord.
- **Résultat net et favorable :** avec un rendu par case, il reste incertain. On passe à 18, sauf si l'owner juge le palier suffisant pour une publication avec réserve (décision 9).
- **Composition des 18 :**
  - 2 briefs × 3 conditions × 3 répétitions (protocole §4) ;
  - les 6 cas du palier comptent comme répétition 1 si la candidate, la consigne et le modèle sont inchangés ; sinon, ils restent un palier à part.

### 6.3 Compromis de coût acceptable

- **Repères mesurés :**
  - P1 : C3 (après R4) coûtait environ 1,7 fois C1 ;
  - B-DLA : C4 coûtait 1,9 à 2 fois C1.
  - La trace légère (R5b-1) n'a pas encore été mesurée (D-23).
- **Acceptable :** sur chaque brief, les tokens de C3 ne dépassent pas ceux de C4.
- **Visé :** C3 ≤ 2 × C1.
- **Entre 2 et 2,5 × C1 :** acceptable seulement si C3 bat C1 en qualité avec l'accord des juges. C'est la consigne de l'owner : qualité avant nombre de mots.
- **Au-delà de 2,5 × C1 :** problème évident (P-5).
- **Durée :** relevée et lue avec les tokens ; elle ne décide pas seule.

### 6.4 Désaccords entre juges

- **Paire tranchée :** une paire est tranchée quand une majorité nette des juges choisit le même côté. Une paire sans majorité (partage ou égalités) est « indécise ». Aucun juge n'a de poids spécial.
- **Accord (M5) :** part des paires tranchées.
  - Moins de la moitié : le résultat de qualité n'est « pas lisible » (protocole §7). On ne conclut pas sur Q, et l'on revoit la grille ou le brief des juges avant de passer à 18.
  - Les mesures mécaniques (E, H mécanique, D, T) restent lisibles.
- **Si l'owner (J1) contredit les deux juges modèles sur une paire :** la paire reste indécise. Le désaccord est rapporté à part, avec les motifs, car c'est un signal sur ce que voient ou non les juges modèles.
- **Désaccord sur un fait inventé (M3) :** le fait est vérifié contre le brief riche. Le compte retenu est le compte vérifié, pas un vote.

## 7. Observation novice (à part)

- **Qui :** 2 ou 3 personnes qui ne connaissent pas le système, recrutées par l'owner.
- **Déroulé :**
  - elles lisent la section « Commencer » du README du package ;
  - puis elles adressent une vraie demande à un agent muni du package, humain présent.
- **Ce qu'on note :**
  - le temps pour savoir quoi dire et quoi fournir (cible : moins d'une minute) ;
  - les blocages et les questions posées ;
  - si l'agent pose ses questions avant de construire (G2 (a)) ;
  - si « valider » est compris comme une suite et non comme une acceptation (G1).
- **Sans jugement de qualité du rendu.** Cette observation ne se mélange pas aux 6 cas.

## 8. Déroulé et arrêt

1. Décisions de l'owner (§9). Raccord R11c appliqué (`V12R_34`, fait). Contrôles : B01 218/218, et `package/` identique à la candidate après R11c.
2. Production des 6 cas (ordre aléatoire), puis contrôles T.
3. Captures, planches et mesures mécaniques (E, D, T, H mécanique).
4. Jugement (J2a et J2b, J1, et D3 s'il y en a), puis révélation de la clé.
5. Lecture selon le §6, rapport de l'unité avec les distinctions certain, probable et hypothétique, puis proposition à l'owner : corriger, passer à 18, ou s'arrêter.

**Estimation du coût (probable) :** environ 0,9 M tokens de production (repères B-DLA et P1), plus environ 0,1 M pour les juges modèles.

**Arrêt :**
- une consigne diffère entre conditions après production : cas à refaire ;
- le modèle change pendant la production : cas concernés à refaire ;
- `package/` modifié entre la production et le jugement : C3 à refaire ;
- aucune personne extérieure : on déclare une orientation en auto-comparaison.

**Non-régression :** aucune modification de `package/` dans cette unité ; B01 vérifiée en début et en fin d'unité.

## 9. Décisions de l'owner

1. **Lever la consigne « pas de run ni d'épreuve »** pour ce palier. C'est la condition de toute production.
2. **Réemploi :** 6 productions neuves (recommandé, §2), ou 4 avec l'écart « modèle non vérifié ».
3. **Brief riche B-SAAS des juges :** valider l'annexe, ou l'amender.
4. **Juges :** J1 (l'owner) oui ou non ; humains extérieurs disponibles ; accès éventuel à des modèles d'autres familles.

## Annexe — Brief riche B-SAAS (proposé, fictif, pour les juges)

Faits **fictifs mais plausibles**, comme B-DLA. Il remplace, pour ce palier, B-LOG (logiciel réel), reporté faute de captures crédibles (`briefs.md`). Il ne sert qu'aux juges ; aucun producteur ne le reçoit.

- **Produit :** « Carnet », logiciel de facturation en ligne pour PME et indépendants. Lancé en 2023, petite équipe.
- **Cible :** gérants de TPE et PME (1 à 20 salariés), sans comptable à plein temps ; usage sur ordinateur au bureau, consultation sur mobile.
- **Trois fonctions :**
  - créer un devis et le transformer en facture en un clic ;
  - relancer automatiquement les factures impayées ;
  - voir en un tableau ce qui est encaissé et ce qui reste à encaisser.
- **Objectif de la page :** faire démarrer un essai gratuit de 30 jours, sans carte bancaire.
- **Tarif :** un abonnement mensuel après l'essai, **montant non communiqué**.
- **Preuve disponible :** aucune. Pas de clients nommés, pas de logos, pas de chiffres d'usage, pas de témoignages. **N'en invente pas.**
- **Ton :** sobre, rassurant, concret ; pas de jargon comptable inutile ; pas de promesse chiffrée.
- **Langue :** français.
- **Assets :** aucun. Ni logo ni capture fournis.
