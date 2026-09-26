# DG-AUDIT-001 — Phase 11.17 — PATCH-DECISION D1 : frontière du jugement de craft

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne » (deux fois). **Première grappe du lot D.**

**Grappe D1 : 3 fiches, toutes Significatif.**

| Fiche | Objet |
|---|---|
| F-DIR-030 | Trois propriétaires décrivent une revue du craft. 6.02b : **cinq grilles** mobilisées pour **un seul** objet |
| F-DIR-020 | Deux grilles de huit dimensions (DIRECTION/FIRST-OBJECT, QUICKSTART §6). La seconde se dit « opérationnalisation » de la première, mais n'en partage que **deux** dimensions |
| F-DIR-042 | Trois déclencheurs critiques (DIRECTION 737–743) mènent au mauvais propriétaire |

**Sorties :**
- cette `PATCH-DECISION` ;
- `D1_harnais_non_regression.py` ;
- 3 entrées LCF (la liste passe à 19).

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | D-FAC-1 = c et LCF (C5, C6) ; C2 (`creative_close` dans la projection) ; C4 (sous-locators `X/Y/Z`, qui rendent `SAVOIR/CRAFT/CFT-01` résoluble) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 |
| Sources relues | DIRECTION 320–333 (contrat positif du premier objet), 449–481 (ATELIER), 482–499 (DOUBLE-LOOP, contrôle du premier objet), 730–744 (déclencheurs) ; SAVOIR 211–240 (CFT-00, Creative Quality Review), 242–260 (CFT-01), 302 (CFT-03) ; ACTION 509–521 (passe créative), 775–797 (GATE-C) ; QUICKSTART 158–176 ; BIBLIOTHEQUE 425 (SCENE) |

## 2. Re-vérification

**Harnais D1 sur B01 :**
- témoin **1/1** ;
- LCF **0/3** ;
- gardes **0/4** ;
- mutations au rouge **0/2**.

**Inventaire des grilles et des revues de craft dans B01 :**

| # | Où | Forme | Rôle déclaré |
|---|---|---|---|
| G1 | SAVOIR/CRAFT/CFT-00 | 8 dimensions : Présence, Point de vue, Culture visuelle, Spécificité, Composition, Désirabilité, Résolution, Retenue | « Grille de regard » |
| G2 | SAVOIR, Creative Quality Review | 6 questions (présent, spécifique, transformé, générique, résolution, geste de polish) | Méthode de revue |
| G3 | DIRECTION/FIRST-OBJECT | 8 dimensions : Présence, Foyer, Signature, Intégration, Résolution, Désirabilité située, Vérité de scène, Résilience visible | « Contrat positif du premier objet » |
| G4 | DIRECTION/DOUBLE-LOOP | 5 tests (Promesse et geste, Preuve précoce, Signature, Finition, Vérité) | « Contrôle du premier objet » |
| G5 | QUICKSTART §6 | 8 dimensions, dont **2 seulement** en commun avec G3 | « opérationne FIRST-OBJECT » |
| G6 | ACTION, passe créative | Une **seconde description de la revue**, plus 4 questions de clôture | Exécution |
| G7 | ACTION/GATE-C | 6 critères C1–C6 | Gate |
| G8 | ATELIER, clôture de craft | Critique par verbes | Méthode locale |

**Constat.** Deux fonctions seulement sont réellement distinctes :
- **juger la qualité créative** : une revue ;
- **décider un gate** : Gate C.

Tout le reste est une **vue** de l'une des deux, mais aucune ne se déclare comme telle ni ne renvoie à sa source. Dans le pire cas, un run DIRECTION produit **deux revues** (G2 et G6) et **trois grilles** (G3, G4, G5) qui ne nomment pas les mêmes défauts dominants.

**F-DIR-042 : trois lignes, trois erreurs de propriétaire.**
- « Motif générique » renvoie au « test motivation/construction **d'ACTION** ». SAVOIR 255 dit pourtant : « cette matrice appartient à `SAVOIR/CRAFT/CFT-01` ; `ACTION/ANTI-SLOP` en contrôle la conséquence ».
- « Scène » ne charge aucune route BIBLIOTHEQUE, alors que la scène est une route structurelle (`BIBLIOTHEQUE/SCENE`, 425).
- « Densité » charge STATE et INTEGRITY, mais **pas CRAFT**. La densité relève de `CFT-03 — composition, densité et harmonie`.

## 3. Les sept questions du §21

| Question | F-DIR-030 | F-DIR-020 | F-DIR-042 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : revues concurrentes, défauts dominants divergents | **Oui** : couverture différente selon la façade | **Oui** : méthode cherchée au mauvais endroit, structure non chargée |
| Défaut réel ? | Oui (6.02b) | Oui (2 dimensions sur 8 en commun) | Oui (relecture ; SAVOIR 255) |
| Gain > charge ? | **Oui, avec réduction** : une grille et une revue en moins | Oui : une table recopiée à l'identique | Oui : trois cellules |
| Nouvelle autorité ? | **Non** : chaque propriétaire garde son rôle (SAVOIR : méthode ; DIRECTION : seuil du premier objet ; ACTION : exécution, trace, gate) | Non | Non |
| Testable ? | Gardes et épreuve (« un run, une revue ») | LCF-15 | LCF-17 |
| Positif / défensif équilibré ? | Oui : la revue garde sa capacité positive (geste de polish le plus rentable) | Oui | Oui |
| Suppression ou fusion ? | **Fusion** (G4 dans G3, G6 dans G2) et **simplification** | **Façade** | **Routing** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Principe : **une revue, une grille de dimensions, un gate. Toute autre forme est une vue qui se déclare.**

| Rôle | Forme unique | Propriétaire |
|---|---|---|
| Vocabulaire des dimensions de qualité créative | **CFT-00** (G1) | SAVOIR (méthode) |
| La revue créative | **Creative Quality Review** (G2) | SAVOIR (méthode) ; **ACTION l'exécute et la trace** (`creative_close`) |
| Seuil du premier objet | **Contrat positif** (G3), vue de CFT-00 avec une colonne de correspondance | DIRECTION (cadrage) |
| Gate | **Gate C** (G7), critères de décision | ACTION |

### 4.1 Corrections (F-DIR-030)

| # | Où | Correction |
|---|---|---|
| T-1 | **DIRECTION 324–333** (contrat positif) | Nouvelle colonne **« Dimension CFT-00 »** : Présence → Présence ; Foyer → Composition ; Signature → Point de vue, Spécificité ; Intégration → Spécificité, Retenue ; Résolution → Résolution ; Désirabilité située → Désirabilité ; Vérité de scène → DIRECTION (TRUTH, ATELIER) ; Résilience visible → Résolution. **Perte déclarée** : « Culture visuelle » n'a pas de seuil au premier objet ; elle est jugée par la revue (« ce qui est culturellement transformé »), `N/A-JUSTIFIED` sans référence. La ligne Intégration absorbe la question « Preuve précoce » de G4 (« …et rend le mécanisme plus clair que le texte seul ») |
| T-2 | **DIRECTION 486–499** (DOUBLE-LOOP) | **La table G4 est supprimée.** Elle est remplacée par : « Avant de présenter, applique le contrat positif de `DIRECTION/FIRST-OBJECT` à la capture réelle ; un défaut appelle la réponse de la colonne « Retour si… ». » Le paragraphe « une correction substantielle… sans quota » reste |
| T-3 | **ACTION 513** (passe créative) | « …effectue après la première scène **la revue créative définie par `SAVOIR/CRAFT/CFT-00` (Creative Quality Review)**, puis une repasse ciblée avant la clôture. » La liste concurrente de ce qu'elle « identifie » est supprimée. ACTION garde le **quand**, la **trace** (les quatre questions de clôture, projetées dans `creative_close`) et le « ni score, ni statut » |
| T-4 | **ACTION/GATE-C** (après 781) | « Gate C décide sur le rendu à partir des observations de la revue créative et, si elle est déclenchée, de la paire B1b ; il **ne refait pas** une seconde revue. » Les critères C1–C6 ne changent pas |
| T-5 | **ATELIER 478** | « La critique de craft, **consignée dans la revue créative unique**, emploie des verbes et leurs effets… » |

**Effet :** un run DIRECTION produit **une** revue (méthode SAVOIR, trace ACTION) et consulte **une** grille (CFT-00), dont le contrat du premier objet est une vue déclarée. Gate C juge ; il ne revoit pas.

### 4.2 Projection exacte (F-DIR-020)

| # | Où | Correction |
|---|---|---|
| T-6 | **QUICKSTART 164–173** | La table reprend **les huit dimensions de G3, dans le même ordre et sous les mêmes noms**. La colonne « ce que le premier rendu doit rendre visible » garde la formulation actuelle de QUICKSTART là où la notion correspond (Silhouette → Foyer, Spécificité → Signature, Premier objet et Relation produit → Intégration, Contenu → Vérité de scène et Résolution, Retenue → Intégration). Mention : « **voir `DIRECTION/FIRST-OBJECT`** » |

La recommandation offrait « projection exacte ou mapping ». La projection exacte est retenue : un mapping dans une façade de démarrage serait une troisième table à maintenir.

### 4.3 Routage (F-DIR-042)

| # | Ligne (DIRECTION 730–744) | Correction |
|---|---|---|
| T-7 | Motif possiblement générique ou réflexe | « Test motivation/construction `SAVOIR/CRAFT/CFT-01` ; conséquence de gate `ACTION/ANTI-SLOP`. » |
| T-8 | Asset, motion, scène ou type spécifique | « Contrat correspondant d'ACTION, route SAVOIR nécessaire ; **pour une scène, `BIBLIOTHEQUE/SELECT` puis la route `BIBLIOTHEQUE/SCENE` retenue.** » |
| T-9 | Détail final (caractère, état, hiérarchie, densité, robustesse) | Ajouter `SAVOIR/CRAFT/CFT-03` (composition, densité et harmonie) à `SAVOIR/STATE`, `SAVOIR/INTEGRITY` et la capture rendue |

### 4.4 Entrées LCF (règle d'entrée C5 : source et mutation rouge)

| ID | Condition | Source | Mutation |
|---|---|---|---|
| **LCF-15** | Les dimensions de QUICKSTART §6 sont **exactement** celles du contrat positif de FIRST-OBJECT (noms et ordre) | DIRECTION 324–333 | M-11 |
| **LCF-16** | La colonne « Dimension CFT-00 » du contrat ne cite que des dimensions de CFT-00, ou « DIRECTION » | SAVOIR/CRAFT/CFT-00 | — |
| **LCF-17** | Déclencheurs critiques : motif → `SAVOIR/CRAFT/CFT-01` et `ACTION/ANTI-SLOP` ; scène → `BIBLIOTHEQUE/…` ; densité → `SAVOIR/CRAFT` | SAVOIR 255 ; BIBLIOTHEQUE 425 ; CFT-03 | M-12 |

**La LCF passe à 19 entrées.**

## 5. Inventaire et conditions

**Inventaire à date : ajouts D1.**
- `validate_reading_map.py` : LCF-15 à 17.
- **Aucun** changement de schéma, de validateur RUN_CARD ou de contrats.

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Passe DIRECTION** (T-1, T-2, T-5, T-7 à T-9) avec les passes déjà fixées (C1, C2, C4 T-5, C5) ; **passe ACTION** (T-3, T-4) avec C1, C2, C3, C4, B5 ; QUICKSTART (T-6) avec C3, C4, C5 |
| C2 | **Canon avant façade** : T-1 avant T-6 ; LCF-15 écrite rouge avant T-6 |
| C3 | **Aucune dimension nouvelle** : T-1 ajoute une colonne de correspondance, pas une ligne |
| C4 | Les **quatre questions de clôture** d'ACTION et `creative_close` (C2) restent inchangées : c'est la trace de la revue unique |

**Sortie (phase 13) :**
1. `D1_harnais_non_regression.py` : témoin **1/1**, LCF **3/3**, gardes **4/4**, mutations au rouge **2/2**. Harnais A1 à C9 verts.
2. **Épreuve « un run, une revue »** (test de F-DIR-030) : un run DIRECTION conduit avec les textes corrigés. Il produit **une seule** revue créative, un seul défaut dominant, et les critères de Gate C citent les observations de cette revue.
3. **Épreuve « un exemple, deux façades »** (test de F-DIR-020) : un rendu évalué par QUICKSTART §6 puis par FIRST-OBJECT fait apparaître **les mêmes lacunes**.
4. **Épreuve de routage** (test de F-DIR-042) : chaque déclencheur corrigé, résolu par le lecteur de routes (C4), mène au propriétaire exact.

**Limite déclarée.** Unifier les grilles ne garantit pas que la revue **juge juste**. Cela garantit seulement qu'un run n'a plus plusieurs revues concurrentes. La qualité du jugement relève de l'observation indépendante (limite F-ACT-037).

## 6. Sortie

- **PATCH-DECISION D1 : CORRIGER.**
  - 9 corrections de texte ;
  - 2 fusions : la grille G4 dans G3, la revue G6 dans G2 ;
  - 1 projection exacte ;
  - 3 routages ;
  - 3 entrées LCF (**19 au total**).
- Liste close RUN_CARD et contrats **inchangée** : 88 lignes, 79 actifs.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Huit formes de jugement de craft deviennent **une grille, une revue, un gate** et deux vues déclarées.
- La correction retire une table (G4) et une description de revue (G6). Elle n'ajoute qu'une colonne de correspondance.

**Prochaine unité : 11.18 PATCH-DECISION D2** (boucle et one-shot : F-DIR-003, F-DIR-009, F-DIR-036). **Dernier candidat de migration de schéma** (F-DIR-036). Réutilise le vocabulaire de phase de C2 (F-DIR-003).

---

## Addendum (11.19) : rectification sur G4

La relecture faite pour D3 a trouvé **DIRECTION 337–339**, « Relation avec le contrôle compact de `DOUBLE-LOOP` ». Cette section déclarait **déjà** G4 comme une vue compacte de G3, avec sa propre correspondance.

**Ce qui est inexact dans ce rapport.** Au §2, j'ai écrit qu'aucune vue « ne se déclare comme telle ». C'est faux pour G4.

**Ce qui ne change pas.** La décision de fusionner G4 dans G3 (T-2) est maintenue. La vue compacte obligeait à maintenir une deuxième grille et une deuxième table de correspondance. Le besoin de « décider rapidement d'un retour » est couvert par la colonne « Retour si… » de G3.

**Ce qui est ajouté.** T-2 supprime aussi la section 337–339, devenue sans objet. La garde G-01 du harnais D1 vérifie désormais son absence.
