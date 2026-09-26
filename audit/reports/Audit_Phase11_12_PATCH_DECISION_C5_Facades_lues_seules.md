# DG-AUDIT-001 — Phase 11.12 — PATCH-DECISION C5 : façades lues seules (D-FAC-1 = c)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.12 ».

**Cadre fixé en 11.00 :** D-FAC-1 = c, « façades bornées et testées ». La grappe se réduit donc à deux choses :
- des **marquages courts** dans les façades ;
- **un test de cohérence** façade ↔ propriétaire, porté par F-VRM-003.

**Grappe C5 : 10 fiches, toutes Significatif.** Même mécanisme : une cellule de façade, lue seule, **perd la condition** que le propriétaire attache à la règle.

| Fiche | Façade | Condition perdue |
|---|---|---|
| F-RM-001 | READING_MAP 33 | `ACTION/RUN-DIRECTION`, forcée par DIRECTION 734–735, rangée en « ajouter seulement si nécessaire » |
| F-RM-002 | READING_MAP 40, 49 | « Risque hors scope et `N/A-JUSTIFIED` » : une exclusion déclarée devient un N/A des contrôles Gate A |
| F-OM-001 | ORCHESTRATION_MAP 20, 21, 23 | Gate A, gate du risque, migration / rollback / CHANGELOG placés en « renforcement » |
| F-QS-002 | QUICKSTART 141 ; README racine 48 | « ou enjeu de craft dominant » suffit à classer DIRECTION |
| F-RDR-001 | README racine 46 | ITER sans la condition « direction retrouvable » |
| F-DIR-041 | DIRECTION 749 (index) | « Nouvelle structure d'écran » présélectionne STANDARD |
| F-DIR-001 | DIRECTION 72, RUN-PRIORITY (285) | Le premier objet passe avant la cible qu'il consomme |
| F-DIR-008 | DIRECTION 159, FAST-PATH 270 | La règle d'omission s'applique aussi à l'owner et au scope |
| F-DIR-018 | RUN-PRIORITY | « Objet avant navigation, cartes » sans le cas où la navigation **est** l'objet |
| F-VRM-003 | `validate_reading_map.py` | Frontière d'autorité vérifiée par sous-chaînes : les contradictions réelles de B01 passent |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C5_harnais_non_regression.py` ;
- **`DG_AUDIT_001_Liste_close_conditions_facade.csv`**, liste close des conditions de façade (LCF) : **12 entrées**.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 (D-FAC-1 = c) ; C2 (un résumé de clôture concurrent cède la place à un renvoi) ; C3 (copies de façade du handoff et de la réponse visible, test attendu ici) ; C4 (résolveur unique importé par `validate_reading_map.py`) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; contrôles sur copie |
| Sources relues | DIRECTION 45–75, 119–160, 263–296, 728–752 ; READING_MAP 14–76 ; ORCHESTRATION_MAP 1–27 ; QUICKSTART 136–146, 150–160 ; README racine 38–54 ; skill 55–92 ; ACTION 202 |
| Machine relue | `validate_reading_map.py` (REQUIRED, frontière 96–98) ; `validate_design_governance.py` (`check_reading_contract`, `check_experimental_position`) ; `validate_all.py` |
| Antécédent | 10.04a §6 : huit fiches ramenées à une décision d'architecture ; 5.01 et 5.04 : « une cellule isolée peut s'interpréter comme permission concurrente » |

## 2. Re-vérification

**Harnais C5 sur B01 :**
- témoins **2/2** ;
- conditions LCF **0/12** ;
- mutations virées au rouge **0/6**.

On réinjecte dans la copie chacune des six cellules fautives (les cinq cellules de B01 et une copie de handoff amputée). **Le validateur reste vert les six fois.** C'est l'objet même de F-VRM-003.

Toutes les fiches sont **confirmées par relecture**. Deux précisions :
- **F-DIR-001 est plus large que la fiche.** L'ordre « premier objet avant cible » apparaît aussi dans ORCHESTRATION_MAP 17 (« Direction forte ») et dans la ligne DIRECTION de la skill (82). READING_MAP 33 et QUICKSTART 153 ont le bon ordre.
- **READING_MAP porte un septième résumé de sortie** : la colonne « Sortie minimale » de son routage (28–36). Elle diverge de CLOSE-PACKAGE (sa ligne « Correction locale » n'a ni verdict ni décision) : c'est la famille de F-DIR-010, déjà décidée en C2. Je l'applique ici **par cohérence, sans nouvelle fiche**, et je le déclare.

## 3. Les sept questions du §21

| Question | Neuf fiches de façade | F-VRM-003 |
|---|---|---|
| Change une décision, une exécution ? | **Oui** : route forcée sautée, contrôle a11y déclaré N/A, mode mal classé, reprise sans owner | **Oui** : aucune correction de façade n'est protégée contre la régression |
| Défaut réel ? | Oui (relecture ; 9.07 : les contrôles a11y ont trouvé des défauts réels sur le pilote B, donc F-RM-002 n'est pas théorique) | Oui (6 mutations en PASS) |
| Gain > charge ? | Oui : une cellule réécrite par fiche, aucune ligne ajoutée hors marquage | **Oui** : 12 conditions ciblées, pas une analyse sémantique |
| Nouvelle autorité ? | **Non** : chaque cellule reprend la condition **existante** du propriétaire (START 132–133, DIRECTION 55, 734–735, ACTION 202) | **Non** : le test vérifie ; il ne définit rien |
| Testable ? | Oui (LCF) | Oui (mutations M-1 à M-6) |
| Positif / défensif équilibré ? | Oui : les façades restent courtes (option c, pas a) | Oui : liste close, pas de « tout contrôler » |
| Suppression ou fusion ? | **Correction de façade** et **routing** ; une colonne supprimée (READING_MAP) | **Validateur** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 : **façade**, **routing**, **clarification** et **validateur**.

### 4.1 Le test de cohérence (F-VRM-003) : une liste close de conditions

**Principe.** Un test qui « comprend » les façades serait indéterministe. Un test par sous-chaînes positives laisse passer les contradictions : c'est la situation de B01. La décision prend une troisième voie, **symétrique de D-ACT-1** : une **liste close de conditions de façade (LCF)**.
- Chaque entrée nomme une façade précise (fichier, ligne de tableau, colonne), la condition du propriétaire qu'elle doit conserver et sa source.
- La liste vit dans `validate_reading_map.py`, sous forme de table déclarative (comme `REQUIRED`). **Aucun nouveau fichier** dans le package ni dans le manifest.
- Le script devient le validateur **« carte et façades »**. Il importe déjà le résolveur décidé en C4.
- `DG_AUDIT_001_Liste_close_conditions_facade.csv` en est le miroir d'audit.
- **Règle d'entrée :** une nouvelle condition n'entre que par une PATCH-DECISION, avec sa source propriétaire et sa mutation rouge (règle A2). C'est la même discipline que la liste close RUN_CARD.

**Trois familles de conditions :**

| Famille | Entrées | Contrôle |
|---|---|---|
| **Condition conservée** (une cellule garde la condition du propriétaire) | LCF-01 à LCF-09 | Présence ou absence d'un jeton dans une **colonne donnée** d'une **ligne donnée**, ou ordre de deux jetons |
| **Marquage** D-FAC-1 | LCF-10 | Les deux tables de mode (QUICKSTART, README) portent « Classement : voir `DIRECTION/START` » |
| **Copie déclarée** (C3) | LCF-C1, LCF-C2 | Les copies du handoff et de la réponse visible ont les mêmes jetons que `ACTION/HANDOFF`, et dans le même ordre pour READING_MAP |

**Motif (A2) :** chaque échec imprime l'identifiant `LCF-xx` et la façade en cause.

**Deux distributions.** Le README racine diffère entre GitHub et Local (`check_local_autonomy`). LCF-04, LCF-05 et LCF-10 s'appliquent aux deux. Le test prend le README de la racine de la distribution qu'il valide.

**Revue bornée, forme seule.** Une contradiction **nouvelle**, dans une cellule que la liste ne couvre pas, n'est pas détectée. Pour compléter, avant chaque release, le diff des façades (README, QUICKSTART, READING_MAP, ORCHESTRATION_MAP, vues DIRECTION, skill) est relu contre les propriétaires. Chaque contradiction trouvée entre dans la liste par PATCH-DECISION. **Cette limite est déclarée ; elle n'est pas masquée par le test.**

### 4.2 Corrections de façade

| # | Où | Quoi | Fiche |
|---|---|---|---|
| T-1 | **DIRECTION 72** | La chaîne interne suit l'ordre de 55 : `START` classe → `CREATIVE-BOOT` ouvre → `VISUAL_TARGET` spécifie → `DIRECTION-ATELIER` si nécessaire → `FIRST-OBJECT` matérialise → `DOUBLE-LOOP` apprend | F-DIR-001 |
| T-2 | **RUN-PRIORITY (285–295)** | Les items 2 et 3 sont échangés. « 2. DIRECTION — retenir… » (la cible). « 3. FIRST-OBJECT — matérialiser la cible : promesse → objet de preuve → geste, avant les éléments génériques ou décoratifs (bénéfices, navigation, cartes, polish), **sauf si la navigation, la recherche ou les cartes sont elles-mêmes l'objet de preuve** » | F-DIR-001, F-DIR-018 |
| T-3 | **ORCHESTRATION_MAP 17 ; skill 82** | Ordre des routes : `VISUAL_TARGET` avant `FIRST-OBJECT`. Contenu inchangé | F-DIR-001 |
| T-4 | **DIRECTION 159 ; FAST-PATH 270** | 159 : « `OWNER` et `SCOPE` ne sont jamais omis : ils rendent la reprise et la portée vérifiables. Les autres lignes sont omises ou `N/A-JUSTIFIED` si elles ne peuvent rien changer. » 270 : « Un risque principal et son owner. » | F-DIR-008 |
| T-5 | **DIRECTION 749** | « Après la classification par `DIRECTION/START` (une nouvelle structure peut relever de `STANDARD`, `DIRECTION` ou `SYSTÈME`), `BIBLIOTHEQUE/SELECT`, puis la route ACTION du mode. » | F-DIR-041 |
| T-6 | **QUICKSTART 141 et 139** | 141 : « Identité, premier contact ou direction visuelle autonome » (START 132) ; le craft est retiré. 139 (STANDARD) ajoute : « craft exigeant : Gate C ciblé, pas un critère de mode ». Sous la table : « **Classement : voir `DIRECTION/START`** » | F-QS-002, D-FAC-1 |
| T-7 | **README racine 46, 48** | 46 (ITER) : « Retouche d'une surface dont la direction existe et est retrouvable ». 48 (DIRECTION) : « Identité, premier contact ou direction visuelle autonome ». Sous la table : « Classement : voir `DIRECTION/START` ». **Les deux distributions** | F-RDR-001, F-QS-002 |
| T-8 | **READING_MAP 33** | « Direction identitaire » : première lecture `DIRECTION/START` → `DIRECTION/VISUAL_TARGET` → `DIRECTION/FIRST-OBJECT` → `ACTION/RUN-DIRECTION` (dès qu'il y a un build). Optionnel : `SAVOIR/CRAFT`, `DIRECTION/DIRECTION-ATELIER` | F-RM-001 |
| T-9 | **READING_MAP 40, 49** | 49, non-chargement : « Aucun risque d'accessibilité au-delà des contrôles `ACTION/GATE-A` applicables, qui restent dus ». 40 ajoute : « Ne pas charger une lecture ne rend jamais `N/A` un contrôle applicable du propriétaire. » | F-RM-002 |
| T-10 | **ORCHESTRATION_MAP 20, 21, 23** | UI/UX : `ACTION/GATE-A` (contrôles applicables) passe au noyau. Preuve : « gate correspondant au risque » passe au noyau. Système : migration, rollback et `CHANGELOG` passent au noyau (paquet SYSTÈME de B3). Le renforcement garde le reste | F-OM-001 |
| T-11 | **READING_MAP 28–36** | La colonne « Sortie minimale » est supprimée et remplacée par un renvoi : « Sortie : réponse visible et handoff (`ACTION/HANDOFF`) ; clôture : `ACTION/CLOSE-PACKAGE`. » La colonne « Sortie » des perspectives reste, car elle décrit l'apport d'une perspective et non une clôture | C2 (F-DIR-010), appliqué par cohérence |

**Aucune cellule ne devient autosuffisante** (option a). Chacune reprend la condition du propriétaire en une expression courte, ou renvoie.

**Sur le lot E1.** QS-001, GLO-001 et FLOW-001 relèvent du même mécanisme (10.04a §6). Si E1 corrige une cellule de façade, sa condition entre dans la LCF selon la règle d'entrée.

## 5. Inventaire à date : ajouts C5

| Objet | Changement | Nature |
|---|---|---|
| `validate_reading_map.py` | Table LCF (12 entrées) et contrôle de cohérence ; motif `LCF-xx` ; README selon la distribution. S'ajoute au résolveur importé (C4) | outil |
| Suite A2 | Mutations M-1 à M-6 ajoutées aux oracles | tests |
| Schémas, validateurs RUN_CARD et contrats | **Aucun** | — |

Candidats de migration de schéma encore ouverts : C9, D2.

## 6. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Ordre** : outil C4 (O-2) → **table LCF** → textes. La table est d'abord écrite **rouge** sur B01 (12 échecs), puis les textes la rendent verte. Jamais l'inverse : un texte corrigé sans test est un texte sans garde |
| C2 | **Canon avant façade** : LCF-C1 et LCF-C2 supposent C3 T-4 déjà appliqué dans ACTION/HANDOFF |
| C3 | **Passes par propriétaire** : DIRECTION (T-1, T-2, T-4, T-5) dans la passe DIRECTION déjà fixée (C1, C2, C4 T-5) ; READING_MAP (T-8, T-9, T-11) avec C4 T-3 et T-4 ; QUICKSTART et README avec C3 T-7 et C4 T-7 |
| C4 | **Façades courtes** : aucune cellule ne dépasse la longueur de la cellule B01 de plus d'une proposition |
| C5 | **Relecture complète** de READING_MAP, ORCHESTRATION_MAP, QUICKSTART 130–165, README racine (deux distributions), DIRECTION 45–75, 119–160, 263–296, 728–752, skill 55–92 |

## 7. Condition de sortie (phase 13)

1. `C5_harnais_non_regression.py` : témoins **2/2**, conditions LCF **12/12**, mutations au rouge **6/6**. Harnais A1 à C4 verts.
2. **Épreuve de lecture « cellule seule, puis texte complet »** (tests des fiches), par un lecteur qui ne connaît pas ce rapport :
   - cadrage de direction **sans build** contre livraison identitaire **avec capture** (F-RM-001) ;
   - UI web « a11y hors scope », artefact imprimé, petit delta frais : CONTEXT lu ? contrôles applicables ? statut ? (F-RM-002) ;
   - deux écrans d'égale exigence de craft, l'un opérationnel, l'autre première scène (F-QS-002) ;
   - même observation sur surface avec direction, direction perdue, écran neuf, règle partagée (F-RDR-001) ;
   - hub, explorateur, recherche, dashboard opérationnel (F-DIR-018).

   Critère : la cellule seule et le texte complet donnent **le même mode, les mêmes routes forcées et le même statut**.
3. **Revue bornée** de release faite une fois sur le diff de phase 12 : les contradictions trouvées sont listées ou déclarées absentes.

**Limite déclarée.** La LCF protège douze conditions connues. Elle ne prouve pas qu'aucune autre cellule ne contredit un propriétaire : c'est le rôle de la revue bornée, qui reste humaine.

## 8. Sortie

- **PATCH-DECISION C5 : CORRIGER.**
  - 1 test de cohérence : la liste close des conditions de façade, 12 entrées ;
  - 11 corrections de façade ;
  - 1 application déclarée du principe C2 (colonne « Sortie minimale » de READING_MAP) ;
  - F-DIR-001 élargi à ORCHESTRATION_MAP et à la skill.
- La liste close RUN_CARD et contrats est inchangée : **70 lignes, 66 actifs**. Nouvelle liste : **LCF, 12 entrées**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- D-FAC-1 = c devient concret. Pas d'analyse de sens, pas de façades dupliquées : **douze conditions précises, chacune avec sa mutation rouge**, et une revue bornée pour le reste.
- Le même geste que D-ACT-1 : **la machine contrôle peu, mais ce qu'elle contrôle, elle le contrôle vraiment.**

**Prochaine unité : 11.13 PATCH-DECISION C6** (exemples de référence : 3 fiches, F-EX-001, F-EX-002, F-GLO-002 ; les exemples qui enseignent les Majeur d’ACTION).
