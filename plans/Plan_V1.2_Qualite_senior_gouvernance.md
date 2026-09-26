# Plan V1.2 — Qualité senior dès le premier rendu, gouvernance conservée

**Date :** 2026-09-26 · **Owner :** Junior (Kamel)
**Base :** Design Governance V1.1.1 (B04, commit `f157dca`), statut d'audit `AUDIT-PASS-WITH-RESERVATION`.

---

## 1. Objectif et périmètre

V1.2 vise un premier rendu de niveau designer senior dès le one-shot, sans affaiblir la gouvernance ni alourdir la lecture. Le levier n'est pas un nouveau style : c'est un meilleur usage des intrants et des décisions.

**Objectif principal.** Que l'agent sache, avant de construire, ce qu'il peut fabriquer avec les moyens disponibles. Qu'il déclare son plafond, demande l'intrant qui le fait monter, et ne simule jamais un asset bas de gamme pour un produit réel.

**Inclus :** bilan de fabrication, prise de brief minimale, matériaux de qualité, anti-slop vivant, atlas d'ancres, épreuve de preuve.

**Exclus :** tout nouveau mode, gate ou statut ; tout style maison ; tout outil payant imposé ; la refonte du schéma machine au-delà d'un champ facultatif (décision de l'owner).

### Critères de réussite

| Critère | Seuil | Comment on le mesure |
| --- | --- | --- |
| Qualité perçue | Rendu V1.2 au niveau du rendu « brief riche + assets », au-dessus du « brief vague » | Classement à l'aveugle par des humains extérieurs (chantier F) |
| Diversité | Pas inférieure à la condition sans système | Similarité entre rendus d'un même brief (chantier F) |
| Honnêteté des assets | 0 asset fabriqué bas de gamme en destination réelle | Revue des runs d'épreuve |
| Plafond déclaré | Présent dans chaque run `DIRECTION` | Garde de texte et cas machine |
| Coût de lecture | Pas d'augmentation nette pour un run `DIRECTION` (environ 1 300 lignes aujourd'hui) | Mesure des lignes chargées |
| Non-régression | 300/300, harnais R 31/31, R03 18/18 | Harnais existants |

### Critères d'arrêt

- V1.2 ne dépasse pas V1.1.1 à l'épreuve à l'aveugle : on ne publie pas les chantiers A à D, on revoit.
- La diversité baisse nettement : c'est un style maison ; on retire les matériaux proposés par défaut.
- Le coût de lecture monte de plus de 10 % sans gain mesuré : on simplifie avant toute publication.

---

## 2. Diagnostic de départ

V1.1.1 sait juger et tracer les décisions, mais ne sait pas évaluer ce qu'il peut fabriquer avant de construire. C'est le manque principal.

| Élément | État dans V1.1.1 | Certitude |
| --- | --- | --- |
| Routes de production (`CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ`, `HYBRIDE`, `SANS-ASSET`) | Présentes dans `DIRECTION/VISUAL_TARGET`. La génération n'est ni le défaut ni un rattrapage décoratif | Certain |
| Profil de capacités | Porte sur l'**observation** (ce que je peux vérifier), pas sur la **fabrication** | Certain |
| Résolution initiale | Le premier rendu ne doit pas être un wireframe creux « lorsque les capacités sont disponibles ». Rien ne dit quoi faire quand elles ne le sont pas | Certain |
| Destination (démo, prototype, produit réel) | Absente comme variable explicite ; seul l'enjeu identitaire existe | Certain |
| Anti-directions et exemples | L'exemple « hero SaaS avec gradient » date de la vague 1 ; l'exemple du QUICKSTART §9 penche vers la vague 2 | Certain (textes) ; probable (effet) |
| Auto-jugement | L'agent juge ses propres captures ; biais d'auto-préférence documenté | Certain |
| Efficacité sur des runs réels | `NOT-VERIFIED` ; mesure M non concluante ; imitation 0/2 | Certain |

**Ce que la discussion a établi (probable) :** avec un brief vague, du HTML seul et aucun asset, le plafond réaliste est le « slop poli ». C'est un défaut d'intrants, pas de talent. Les assets figuratifs (photos, illustrations, 3D) sont la couche où l'IA seule produit du bas de gamme.

---

## 3. Principes directeurs

Six principes cadrent tous les chantiers. Chacun vient d'un constat de la discussion ou des recherches.

1. **Juger des décisions, jamais prescrire un style.** Toute prescription fixe, répétée à grande échelle, devient la nouvelle moyenne. C'est le paradoxe anti-slop : la consigne « polices distinctives, atmosphère » a précédé le look beige et serif de 2026 (probable).
2. **Un senior ne produit pas à partir de rien.** Le one-shot de qualité vient après une bonne prise de brief. L'agent doit se comporter comme un senior : peu de questions, les bonnes.
3. **Ne jamais simuler ce qu'on fabrique mal.** En destination réelle, un trou d'asset se comble par une route assumée ou un emplacement honnête, jamais par un faux asset.
4. **Livrer quand même.** Le plafond déclaré ne bloque pas : le premier rendu sort avec la meilleure route disponible et la liste de ce qui le ferait monter.
5. **La vérité avant l'esthétique.** Les marqueurs de slop les plus fiables sont de vérité et de texte : métriques sans référence, faux logos, prestige inventé, copie recyclée. Ils ne dépendent pas de la mode.
6. **Ne rien ajouter sans retirer.** Chaque chantier doit tenir dans le budget de lecture actuel, en remplaçant ou en fusionnant du texte existant.

---

## 4. Chantier A — Bilan de fabrication

Avant le build, l'agent croise la destination, les moyens et le plafond atteignable, puis décide. C'est une extension de `DIRECTION/START` et du Creative Boot, dans la trace existante : ni mode, ni gate, ni statut.

```text
DESTINATION : démo | prototype | produit réel (+ enjeu identitaire)
MOYENS      : assets fournis · marque · polices · composants/design system ·
              génération d'image · sources autorisées · contenu réel
PLAFOND     : structure / typo / couleur / assets / contenu
              → atteignable | limité | non atteignable sans X
DÉCISION    : construire | construire avec plafond déclaré | demander X | changer de route
```

### Règles

| Situation | Comportement attendu |
| --- | --- |
| Plafond suffisant pour la destination | Construire ; le bilan tient en une ligne |
| Asset manquant, destination réelle | Route `CODE-NATIVE` ou `SANS-ASSET` assumée, ou emplacement réservé marqué ; demander l'asset. Jamais de faux asset |
| Asset manquant, démo ou template | Approximation permise, marquée `ILLUSTRATIVE` |
| Contenu absent | Emplacements marqués comme illustratifs ; aucun chiffre, logo, témoignage ou prix inventé présenté comme réel |
| Couche « non atteignable » décisive pour la promesse | Le déclarer avant le build et proposer l'intrant qui lève la limite |

### Emplacement proposé

- `DIRECTION/START` : ajouter la destination à l'entrée minimale.
- Creative Boot : remplacer `ANCHOR-BASIS` et `ANCHOR-LIMIT` par un bloc `FABRICATION` qui les absorbe, pour ne rien ajouter au budget.
- `ACTION` : distinguer, dans le profil de capacités, observation et fabrication.

### Projection machine (décision de l'owner)

- **Option 1 :** trace seule.
- **Option 2 :** champ facultatif `fabrication` dans la `RUN_CARD`, exigé pour une `DIRECTION` en destination réelle.

**Gardes visées :** une condition de façade (LCF) par copie du bilan ; si l'option 2 est retenue, des cas unitaires rouges sur V1.1.1.

---

## 5. Chantier B — Prise de brief minimale

L'agent pose au plus trois questions, classées par gain de plafond, puis construit quoi qu'il arrive. Le brief vague n'est pas une excuse pour produire la moyenne, ni une raison de bloquer.

**Ordre des demandes (par gain de plafond, probable) :**

1. **Le vrai contenu** : textes, chiffres, preuves, noms. C'est le levier le plus fort : Fold et Orchid se distinguaient d'abord par leurs mots.
2. **La marque** : logo, couleurs, polices, ton, sites de référence.
3. **L'asset principal** : photo, illustration, produit réel, ou l'autorisation d'une route (génération dirigée, source autorisée).
4. **La destination**, si elle n'est pas évidente : démo ou produit réel.

### Comportement selon la présence de l'humain

| Cas | Comportement |
| --- | --- |
| Humain présent | Questions groupées en un seul échange, avant le build |
| Humain absent (run autonome) | Hypothèses nommées dans la trace ; build avec plafond déclaré ; demandes listées à la livraison |
| Brief déjà riche | Aucune question ; le bilan de fabrication tient en une ligne |

**Ce que ce chantier remplace :** les questions implicites dispersées dans `START` et le Creative Boot. Il les regroupe au lieu de les multiplier.

**Garde visée :** une condition de façade vérifiant que QUICKSTART, la skill et `START` citent le même ordre de demandes.

---

## 6. Chantier C — Matériaux de qualité, pas un style

Le système indique où trouver des matériaux de bonne facture ; il ne dit jamais lesquels utiliser par défaut. Le choix découle de la thèse du run.

| Couche | Ce que le système fournit | Garde-fou contre le style maison |
| --- | --- | --- |
| Typographie | Critères de choix (usage, langues, graisses, licence) et quelques familles ouvertes de qualité par registre | Aucune famille par défaut ; la famille choisie doit être justifiée par la thèse |
| Icônes | Exigence d'une seule famille cohérente par run, et bibliothèques ouvertes connues | Pas d'icône dessinée à la main par l'agent en destination réelle |
| Matière code-native | Techniques : typographie comme image, dataviz, SVG géométrique, trames, grilles, mouvement utile | Une technique n'est retenue que si elle porte la relation au produit |
| Assets figuratifs | Routes existantes (`FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ`) + droits | Jamais d'illustration figurative dessinée en SVG par l'agent pour un produit réel |
| Composants | Renvoi à `BIBLIOTHEQUE/COMPONENTS` et aux design systems fournis | Pas de kit de composants « maison » imposé |

**Point à vérifier avant rédaction :** les listes de ressources (polices, icônes) vieillissent. Elles seront marquées `[VEILLE]`, datées, et rangées dans SAVOIR, pas dans les textes normatifs.

**Critère d'arrêt propre à ce chantier :** si l'épreuve montre une baisse de diversité, on retire les exemples de familles et on ne garde que les critères.

---

## 7. Chantier D — Anti-slop vivant

L'anti-direction ne doit plus être une liste figée : l'agent nomme d'abord sa propre réponse modale, puis décide s'il s'en écarte. Les marqueurs de mode sont datés ; les critères de vérité restent permanents.

### 1. Réponse modale nommée

Dans le Creative Boot, un champ remplace l'anti-direction figée :

```text
MODAL : ce que n'importe quelle IA produirait ici (structure, palette, typo, assets)
PARTI : garder | s'écarter — où, et pourquoi, au regard de la thèse
```

Cela reprend l'esprit de *Verbalized Sampling* et de la « friction productive » : on explicite le centre au lieu d'y tomber. Garder le mode reste une sortie valide, si elle est décidée.

### 2. Deux niveaux de critères

| Niveau | Contenu | Durée de vie | Où |
| --- | --- | --- | --- |
| Permanent | Vérité de scène, test de substitution, précision du texte, intégration | Durable | Textes normatifs (existants) |
| Daté | Marqueurs de vague (vague 1 : violet, Inter, halos ; vague 2 : beige, serif italique, orange rouille, bandeaux défilants, illustration peinte, tramage) | Quelques mois | SAVOIR, tag `[VEILLE]`, avec date et source |

### 3. Exemples à corriger (certain)

- Anti-direction d'exemple « hero SaaS interchangeable avec gradient décoratif et cartes répétées » : datée vague 1.
- Exemple du QUICKSTART §9, « entrée éditoriale dense, objet visuel propriétaire » : proche de la vague 2.
- Remplacement : des exemples formulés en décisions (« la preuve du produit porte la première scène »), sans style nommé.

**Gardes visées :** une condition de façade qui refuse un marqueur de mode hors d'un bloc `[VEILLE]` daté ; une qui vérifie la présence du couple `MODAL` / `PARTI` dans le boot et ses copies.

---

## 8. Chantier E — Atlas d'ancres annotées

Un petit corpus de références réellement observées, chacune jugée sur ses décisions et datée. Le goût se transmet par des exemples regardés, pas par des paragraphes de principes.

### Format d'une entrée

| Champ | Contenu |
| --- | --- |
| Identifiant et date | Ex. `AT-2026-09-07`, date d'observation |
| Source | Lien et auteur, droit d'usage de la capture |
| Vague | Aucune, vague 1, vague 2… |
| Décision portée | Ce qui lie la forme au produit (ex. Fold : les conteneurs comme motif) |
| Retenu | Ce qui est transférable comme principe |
| Rejeté | Ce qui est tendance, faux ou décoratif |
| Vérité | Défauts de vérité relevés (métriques, logos, prestige) |
| Limite de transfert | Ce qu'on ne doit pas copier |

**Point de départ :** les 17 images des deux lots déjà analysés, complétées par des références hors web (édition, affiche, signalétique) et hors canon occidental, pour réduire le biais culturel.

### Règles

- Les entrées servent de **calibration**, jamais de modèle à reproduire (règle déjà présente pour les ancres).
- L'atlas vit hors des textes normatifs : référence de la skill, chargée seulement si une décision visuelle est ouverte.
- Révision au moins à chaque version ; une entrée de vague périmée est archivée, pas supprimée.

**À vérifier :** le droit de reproduire des captures de tiers dans un package publié. Option sûre : des descriptions et des liens, sans image embarquée.

---

## 9. Chantier F — Preuve

V1.2 n'est publiée que si une épreuve à l'aveugle, jugée par des humains extérieurs, montre un gain de qualité sans perte de diversité. C'est aussi la réserve n° 1 de l'audit.

### Protocole

| Élément | Choix |
| --- | --- |
| Briefs | 4 briefs variés (produit SaaS, commerce local, service public, portfolio), dont au moins un ancré à Douala |
| Conditions | C1 : brief vague, sans système ni asset. C2 : brief riche + assets fournis, sans système. C3 : brief vague + V1.2 (bilan, intake simulé ou réel). C4 : V1.1.1 |
| Répétitions | 3 rendus par brief et par condition, pour mesurer la diversité |
| Juges | 3 à 5 personnes extérieures, dont au moins un designer ; relation déclarée (critères D3) |
| Mesures | Classement de qualité par paires ; similarité entre rendus d'un même brief ; défauts de vérité comptés ; lignes de règles lues |
| Aveugle | Rendus anonymisés, ordre aléatoire, clé gardée par l'owner |

### Lecture des résultats

| Résultat | Décision |
| --- | --- |
| C3 ≈ C2 et C3 > C1, diversité tenue | Publier V1.2 |
| C3 > C1 mais diversité en baisse | Style maison : retirer les matériaux par défaut, rejouer |
| C3 ≤ C4 | Arrêter : les chantiers n'apportent rien, revoir le diagnostic |

**Limite (certain) :** même bien menée, cette épreuve reste petite. Elle tranche une décision de publication, elle ne prouve pas une efficacité générale.

---

## 10. Gouvernance du changement

V1.2 suit exactement la méthode qui a produit V1.1.1 : décision écrite, textes exacts, gardes rouges avant et vertes après, aucune régression. Seul le contenu change.

| Règle | Application à V1.2 |
| --- | --- |
| Base | B05 = copie de V1.1.1 (B04, `f157dca`) ; B01 à B04 intactes |
| Décision | Une PATCH-DECISION par chantier retenu, textes exacts sous forme exécutable |
| Gardes | Conditions de façade LCF-43 et suivantes, chacune rouge sous mutation ; cas unitaires si la machine change |
| Non-régression | 22 harnais (300/300), harnais R et R03, vérifications 13.01, épreuves déterministes 13.02 |
| Revue | Revue bornée du diff ; au moins une relecture par une personne extérieure avant publication |
| Budget de lecture | Mesure des lignes chargées par mode avant et après ; aucune hausse nette en `DIRECTION` |
| Version | V1.2.0 : changement de fond du comportement, compatibilité des cartes V1.1.1 conservée si l'option 1 (trace seule) est retenue |

**Ce qui ne change pas :** l'honnêteté des statuts, l'interdiction de `POLISHED` et `SLOP-FREE`, la séparation trace / machine, la règle « une entrée LCF n'entre que par une PATCH-DECISION ».

---

## 11. Séquencement, risques et arrêts

Le travail avance en cinq phases séparées par quatre portes ; on ne franchit une porte que si son critère est tenu. L'épreuve à l'aveugle (phase 4) décide seule de la publication.

```text
 Phase 1          Phase 2            Phase 3           Phase 4           Phase 5
 Décisions   ──▶  PATCH-DECISION ──▶ Application  ──▶  Épreuve     ──▶   Publication
 owner (§12)      A, B, D + gardes   B05, contrôles    F, avec C et E    V1.2.0
            ◆ G1              ◆ G2               ◆ G3              ◆ G4
      options choisies   gardes rouges     300/300 et budget   C3 ≈ C2,
                         puis vertes       de lecture tenu     diversité tenue
```

Les chantiers C (matériaux) et E (atlas) se préparent en parallèle des phases 2 et 3, mais n'entrent dans le package qu'après la porte G4.

### Risques principaux

| Risque | Signal | Réponse |
| --- | --- | --- |
| Le bilan de fabrication devient un rituel rempli sans effet (slop procédural) | Bilans identiques d'un run à l'autre | Exiger une décision différente selon la destination ; sinon retirer le champ |
| Style maison issu des matériaux ou de l'atlas | Baisse de diversité en épreuve | Retirer les exemples, garder les critères |
| Hausse du coût de lecture | Lignes chargées en hausse en `DIRECTION` | Fusionner avec l'existant avant d'ajouter |
| Questions excessives à l'humain | Plus de trois demandes, ou demandes sans gain de plafond | Plafonner à trois, classées par gain |
| Juges non indépendants | Juges liés à l'owner ou à l'auteur | Déclarer la relation ; l'épreuve reste une réserve, pas une preuve FULL |

---

## 12. Décisions attendues de l'owner

Sept choix ouvrent la porte G1. Pour chacun, je donne une recommandation ; aucun n'est tranché tant que tu ne l'as pas validé.

| # | Décision | Options | Recommandation |
| --- | --- | --- | --- |
| 1 | Projection machine du bilan de fabrication | Trace seule, ou champ facultatif `fabrication` dans la `RUN_CARD` | Trace seule en V1.2 : les cartes V1.1.1 restent valides ; le champ viendra si l'épreuve le justifie |
| 2 | Périmètre du cœur de V1.2 | A + B + D d'abord, ou les six chantiers ensemble | A + B + D ; C et E préparés en parallèle, intégrés après G4 |
| 3 | Réponse modale (`MODAL` / `PARTI`) | Remplace l'anti-direction figée, ou s'y ajoute | Remplace : même fonction, et le budget de lecture reste stable |
| 4 | Ressources de matériaux | Critères seuls, ou critères + quelques familles nommées `[VEILLE]` | Critères + exemples datés, retirables si la diversité baisse |
| 5 | Forme de l'atlas | Captures embarquées, ou liens et descriptions | Liens et descriptions, pour éviter les questions de droits |
| 6 | Juges de l'épreuve | 3 à 5 personnes extérieures, dont au moins un designer | À recruter par toi ; c'est la seule porte qui ne dépend pas de moi |
| 7 | Briefs de l'épreuve | 4 briefs variés | Au moins un produit ancré à Douala, pour tester le biais culturel des références |

**Prochaine étape après tes choix :** la PATCH-DECISION des chantiers A, B et D, avec textes exacts et gardes, sur une copie B05 de V1.1.1.

---

## Sources principales

- Doshi & Hauser, *Generative AI enhances individual creativity but reduces the collective diversity of novel content*, Science Advances, 2024 — https://www.science.org/doi/10.1126/sciadv.adn5290
- *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity* (biais de typicité), 2025 — https://arxiv.org/abs/2510.01171
- Shin et al., *Interrogating Design Homogenization in Web Vibe Coding* (friction productive), mars 2026 — https://arxiv.org/abs/2603.13036
- Kommers et al., *Why Slop Matters*, ACM AI Letters — https://arxiv.org/abs/2601.06060
- Anthropic, *Improving frontend design through Skills* (convergence distributionnelle) — https://claude.com/blog/improving-frontend-design-through-skills
- Kyle Chayka, *The generic style of AI web design*, juin 2026 — https://kylechayka.substack.com/p/the-generic-style-of-ai-web-design
- *LLM Evaluators Recognize and Favor Their Own Generations*, NeurIPS 2024 — https://arxiv.org/html/2404.13076v1
- Paul Adams, *The dribbblisation of design*, Intercom, 2013 — https://www.intercom.com/blog/the-dribbblisation-of-design/
