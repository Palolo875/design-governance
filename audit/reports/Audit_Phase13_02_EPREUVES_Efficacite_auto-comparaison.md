# DG-AUDIT-001 — Phase 13.02 — ÉPREUVES d'efficacité (auto-comparaison différée)

**Date :** 26 septembre 2026.
**Objet :** Design Governance **V1.1.0**, distribution GitHub (`Design_Governance_V1.1.0_GITHUB.zip`).
**Référence :** B01, en lecture seule.
**Format :** rapport allégé.

**Fichiers produits :**
- `DG_AUDIT_001_Epreuves_13-02.py` : épreuves déterministes, rejouables ;
- `DG_AUDIT_001_Epreuves_13-02_traces.zip` : réponses des lecteurs, revue bornée, run DIRECTION (HTML, 12 captures, trace, RUN_CARD), imitation, palettes, clé du classement en aveugle ;
- `DG_AUDIT_001_13-02_run_DIRECTION_v2_desktop.png` : capture du rendu final du run.

## 1. Observateur (critères D3 T-5)

**Décision de l'owner (26 septembre) :** pas d'observateur. Les épreuves sont donc conduites en **auto-comparaison différée**. **Aucune n'est clôturée FULL.**

```text
REVIEWER-ROLE — sous-agents du même modèle : 4 lecteurs, 1 relecteur de release, 1 producteur (run DIRECTION), 1 imitateur, 2 producteurs de palettes, 1 classeur
REVIEWER-RELATION — SAME-AUTHOR : même modèle que l'auteur des corrections, lancé et instruit par lui
RENDER-AUTHOR — sous-agent producteur (run DIRECTION) ; auteur des corrections pour le corpus
CONFLICT — DECLARED : l'auditeur est l'auteur des corrections qu'il éprouve
ARTEFACTS-REVIEWED — distribution V1.1.0 ; diff textuel de la phase 12 ; rendus et palettes produits
REVIEW-EXPOSURE — PROMPT-EXPOSED ; aveugles aux rapports d'audit par consigne, sans contrôle technique ; classeur des palettes aveugle à la condition
MAPPING-TIMING — clé des palettes révélée APRÈS le classement
LIMIT — un même modèle lit, produit et juge : les biais communs ne sont pas neutralisés
```

**Ce qui n'est pas concerné par cette limite :** les épreuves déterministes du §2.1. Leur verdict est mécanique : aucun jugement n'intervient.

## 2. Résultats

### 2.1 Épreuves déterministes : 38/38 (`DG_AUDIT_001_Epreuves_13-02.py`)

| Épreuve (décision) | Résultat |
|---|---|
| B1 : rejeu 9.08 (consentement classé LITE avec risque critique) | **Refusé en machine**, motif Protection de niveau |
| B2 : rejeux 4.04, 7.02, 9.02 (issue non nulle et ACCEPTED) ; 4.08 (version périmée) | 4/4 refusés, chacun pour son motif |
| B2 : rejeu 4.07 (capture statique présentée comme test de tâche) | **Accepté**, comme prévu : c'est la limite déclarée « forme seule » |
| B3 : SYSTÈME accepté sans paquet ; composant partagé sans consumer | 2/2 refusés |
| B3 : 9.06 T1 (paire équivalente) | Accepté : limite déclarée (la machine ne vérifie pas l'équivalence) |
| B4 : DIRECTION acceptée sans ancre ; pilote A sans ancre en EXPLORATORY ; `transformed` déclaratif | Refusé (INV-B4-6) ; accepté sans ancre inventée ; accepté (limite déclarée) |
| D2 : photo de la carte aux états INTAKE à BUILDING ; ITER sans puis avec rappel de direction | 8/8 : chaque champ « après observation » rempli trop tôt est refusé. L'ITER sans rappel est refusé, celui avec rappel accepté |
| C4 : un scénario par mode avec READING_MAP et `read_route` seuls ; profils normal et strict (20 combinaisons) | 5/5 scénarios servis. Profils : même résultat dans les deux, hors contrôles propres au strict |
| C4 : mesure de la route LITE de 9.08 | **51 lignes** (158 sur B01 ; budget 60) |
| D1 : routage des trois déclencheurs corrigés ; D4 : épreuve de propriétaire | 3/3 et 4/4 : chaque locator est servi par son propriétaire exact |
| C9 : intégrateur hors du package, avec la seule commande du README | 3 contrats valides acceptés ; 3 contrats cassés refusés proprement |
| F-DIR-044 : taille des blocs servis (préalable des pilotes) | Les plus gros blocs : SAVOIR/CRAFT 188 lignes, DIRECTION/START 76, VISUAL_TARGET 75, COMPONENTS 74 |

J'ai corrigé deux erreurs de construction dans mes propres cas avant de consigner les résultats :
- les photos D2 partaient d'une fixture à risque critique ;
- le cas « contrat cassé » de C9 utilisait un placeholder que le validateur n'est pas censé refuser dans ce champ (constat 6, §3).

### 2.2 Épreuves de lecture : lecteurs neufs, en auto-comparaison

| Épreuve | Critère de la décision | Résultat | État |
|---|---|---|---|
| **B5** (4.02 A et B, 4.03 C) | SYSTÈME d'abord si partagé ; DIRECTION puis SYSTÈME dépendant ; contrat trouvé en une ouverture | 3/3 | **Tenue** |
| **C1** (triade, TRUTH) | CHANGED, N/A-JUSTIFIED et NOT-OBSERVED, sans confusion avec NOT-VERIFIED ; labels internes jamais dans l'UI | Distingués correctement ; divulgation en langage produit | **Tenue** |
| **D4** (cycle de vie, propriétaires) | Statuts, interdiction d'usage, migration, aucun gain revendiqué | Correct | **Tenue** |
| **C7** (palette, non-généricité, test de style) | Lecture conforme aux cas | Conforme ; deux ambiguïtés relevées (CFT-05 « requis » et « conditionnel » ; le test de style et le test de non-généricité ne masquent pas les mêmes éléments) | **Tenue, avec réserves** |
| **C5** (cellule seule, puis texte complet) | Même mode, mêmes routes forcées, même statut | 2 scénarios sur 5 identiques. A1 : la façade conditionne `RUN-DIRECTION` au build, alors que START le route toujours. A4 : le README n'a pas de ligne « direction perdue ». A5 : le récapitulatif (point 4) ne garde que l'exception « navigation » | **Partielle** |
| **C2** (projection) | Aucune perte non déclarée | Destinations non déclarées : NEXT-ACTION hors polish, METHOD sans provenance, `decision_change.value` et `evidence` absents de la table | **Partielle** |
| **C3** (proportion, sorties) | Réponse visible ou handoff selon le cas ; pas de variante fabriquée | Tenu ; OWNER passe `N/A` par défaut dans la forme courte LITE | **Tenue, avec réserve** |
| **C6** (exemples, glossaire) | Choix et observation lisibles ; ligne CLOSED applicable | Exemples lisibles. **Contradiction :** GLOSSAIRE rend un risque critique non vérifié inéligible à ACCEPTED-WITH-RESERVATION, alors qu'ACTION et le validateur l'admettent (« la réserve reste possible ») | **Partielle** |
| **D3** (autorité, motion, indépendance, outillage) | Lecture conforme | Conforme ; deux contradictions (issue sans autorisation : DIRECTION ≠ ACTION ; champs d'une nouvelle dépendance : ACTION ≠ SAVOIR) | **Partielle** |
| **E1** (26 passages) | Compris comme le propriétaire l'entend | Sens compris dans la majorité des cas ; 12 contradictions signalées, 14 ambiguïtés. **Vérifié :** la « légende commune » est fausse, car SAVOIR n'emploie aucun `[RECOMMANDÉ]`. **Erreur du lecteur :** le n° 6 affirme à tort que les validateurs sont absents | **Partielle** |

### 2.3 Épreuves de production

| Épreuve | Résultat | État |
|---|---|---|
| **D1 « un run, une revue »** : run DIRECTION réel (coopérative vélo, HTML, 12 captures) | **Une seule** revue créative, **un** défaut dominant (la fiche masque l'objet du geste). B1b déclenchée et réalisée (`modified`). Gate C cite les observations R1 à R8 de la revue. Correction v2 ré-observée ; arrêt motivé avant une v3. RUN_CARD **valide du premier coup**, y compris en strict. Aucun label interne dans l'UI | **Tenue** |
| **C1, rejeu du micro-run 9.08** | Contenu d'exemple divulgué en langage produit (« données d'exemple ») | **Tenue** |
| **D1 « un exemple, deux façades »** | Sur le même rendu, QUICKSTART §6 trouve **1** lacune, FIRST-OBJECT en trouve **5 de plus**. Cause : §6 reprend les huit dimensions mais pas la colonne « Retour si » (décision D1 T-6) | **Non tenue** |
| **D2, boucle** | Branche « run faible → retour exigé » observée. La branche « one-shot suffisant, aucune modification » n'a pas été produite | **Partielle** |
| **C6, imitation** : un agent qui n'a que `examples.md` produit une carte LITE et une carte DIRECTION | **0/2 passent le validateur** (`risk` en chaîne ; `creative_close` à `null`). Tous les noms de clés ont dû être devinés, sauf `creative_close`. Les exemples enseignent la trace, pas la sérialisation | **Non tenue** |
| **C7, mesure M** : 3 briefs, avec et sans DG, classement en aveugle | **Sans DG :** 3/3 dans des classes convergentes (2 « neutres + un accent », 1 « sombre + doré »). **Avec DG :** 2/3 « neutres + un accent », avec convergence justifiée, et 1 « multicolore » (festival ; le classeur est en confiance basse sur ce cas). **Recul faible**, porté par un seul cas incertain, N = 3 | **Non concluante** |

**Ce que la mesure M implique.** Le critère de la décision C7 est : « si la convergence persiste avec DG corrigé, F-SAV-002 passe Majeur ». Elle ne persiste pas entièrement, et elle ne recule pas nettement non plus. **F-SAV-002 reste Significatif.** Le relèvement de gravité n'est ni accordé ni rejeté.

### 2.4 Revue bornée du diff de la phase 12 (C5, point 3)

Le relecteur a lu le diff V1.0.0 → V1.1.0 et le package. Il relève **32 contradictions : 2 bloquantes, 13 significatives, 17 mineures**. Il confirme aussi des zones sans contradiction : versions, SEED, protection critique, réserves et exception, LCF, colonne CFT-00, locators, build.

**Mon tri (certain pour les points marqués « vérifié ») :**

| # | Contradiction | Vérifié | Origine |
|---|---|---|---|
| R-01 (B) | La table RUN_CARD d'ACTION (l. 295) et le GLOSSAIRE (l. 38) donnent `N/A-JUSTIFIED` quand une conséquence est « attendue » mais non obtenue ; la triade (ACTION/STATUS) impose `NOT-OBSERVED` | oui | Texte de B01 laissé en place : C1 T-3 ne visait pas cette ligne |
| R-02 (B) | B1b : « hors de son scope, il ne s'applique pas », mais la machine exige `closure.b1b` pour **toute** DIRECTION acceptée avec V en PASS, sans motif « hors scope » | oui | Décision B3 (INV-B3-3), plus large que le scope textuel |
| R-03 | QUICKSTART 45 et skill : « deux anti-directions, une tension » | oui | Déjà relevé en 12.05c, non décidé |
| R-07 | Skill : « gates B/C non chargés par défaut » en LITE et ITER, alors que la carte d'ACTION charge Gate B | oui | Texte de B01 laissé en place |
| R-08 | La table de correspondance attribue à VISUAL_TARGET « premier objet, périmètre, contrainte », qui ne sont pas dans sa table | oui | **Texte même de la décision C2 T-1** |
| R-10 | `machine_projection` : `NOT-OBSERVED` listé pour les axes ; « quatre champs » de `profile_decision` (le schéma en a cinq depuis 12.04) | oui | B01, plus un consommateur non mis à jour en 12.04 |
| R-12 | Droits `unknown` : pas d'ACCEPTED, mais ACCEPTED-WITH-RESERVATION passe ; ACTION 666 dit RETURNED ou ESCALATED | oui | Décision B2 (INV-B2-10) face à un texte de B01 |
| R-13 | Ressource technique : sept champs (ACTION) contre une autre liste (SAVOIR 782) | oui | D3 T-6 n'a modifié que la phrase précédente |
| R-14 | « Sortie définie une seule fois par CLOSE-PACKAGE », alors que les blocs RUN-* gardent leur propre « Sortie » | oui | Phrase de C4 T-2 ; RUN-* non traités |
| R-04, R-05, R-06, R-09, R-11, R-15 | Ligne de run sans OWNER ni SCOPE ; OWNER `N/A` en LITE ; défaut de la skill ; phase de NEXT-PROOF ; NOT-OBSERVED pour une dimension ; revue « unique » | partiellement | Tensions issues de textes **décidés** (C2 T-11, C2 T-3, C3 T-6, C1 T-2). Une partie relève de l'interprétation |
| R-16 à R-32 | Mineurs | non, un par un | Probables selon le relecteur ; transmis tels quels |

**Constat sur le CHANGELOG V1.1.0.** La phrase « Façades … alignées sur leurs propriétaires » est **trop forte**. Les LCF sont tenues, mais R-03, R-07 et R-10 montrent des façades encore divergentes hors de la liste close.

## 3. Constats de la phase 13

1. **Certain : ce que la machine promet, elle le tient.** Les 38 épreuves déterministes passent. Les rejeux des antécédents de la campagne (9.08, 4.04, 7.02, 9.02, 9.03, 9.06) sont refusés pour leur motif. Les limites déclarées (forme seule) se comportent comme déclaré.
2. **Certain : les deux épreuves de production « de forme » échouent.**
   - Les exemples n'enseignent pas la sérialisation (imitation : 0/2).
   - QUICKSTART §6 est une projection avec perte : il surestime un rendu que FIRST-OBJECT juge plus sévèrement.

   Dans les deux cas, la cause vient d'un choix de décision : exemples en format trace (C6), §6 sans colonne « Retour si » (D1 T-6). Aucune n'a été appliquée à tort.
3. **Probable (auto-comparaison) : le jugement fonctionne sur un run réel.** Le run DIRECTION a produit un rendu crédible avec une seule revue, un défaut dominant réel, une B1b utile et une carte valide.

   Le coût est élevé : environ 1 300 lignes de règles lues pour une scène, et une RUN_CARD d'environ 230 lignes. Le producteur relève aussi des recouvrements (thèse, objet et anti-direction formulés trois fois) et une carte de chargement ACTION sans locator.
4. **Certain : la liste close des conditions de façade ne suffit pas à garantir la cohérence.** La revue bornée trouve 2 contradictions bloquantes et 13 significatives, dont 9 vérifiées. Elles ne violent aucune LCF : elles sont hors de la liste close.

   Leur origine est mixte :
   - textes de B01 laissés en place (R-01, R-07, R-10) ;
   - décisions de phase 11 elles-mêmes (R-02, R-08, R-12) ;
   - application partielle (R-13, R-14).
5. **Non concluant : l'effet sur l'homogénéisation** (mesure M, N = 3, auto-comparaison).
6. **Observation nouvelle.** Dans les contrats, un placeholder (« à compléter ») est accepté dans les champs de texte libre que E2 n'a pas visés (`domain`, `research_question`). Conforme aux décisions ; noté comme limite.

**Aucune correction n'est faite dans cette unité.** La phase 13 éprouve, elle ne corrige pas. Les constats 2 et 4 relèvent d'un cycle de PATCH-DECISION ultérieur, que l'owner peut ouvrir ou non.

## 4. Suite : phase 14, clôture

Le dossier final rassemble :
- cible, sources, baseline, couverture, résistances, constats, décisions, validations et réserves ;
- la **proposition de statut d'audit**, parmi `AUDIT-PASS`, `AUDIT-PASS-WITH-RESERVATION`, `AUDIT-RETURN`, `AUDIT-NOT-VERIFIED` et `AUDIT-EXPLORATORY` ;
- ce qui décide entre ces statuts : les deux contradictions bloquantes (R-01, R-02) et l'échec de l'imitation, face à une conformité de forme complète.

**La décision de statut revient à l'owner.** Je présenterai les options avec leurs conséquences, sans prononcer de verdict global.
