# DG-AUDIT-001 — Phase 10.02 — FINDINGS : ACTION (39 fiches)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** enchaîner sur ACTION après DIRECTION (« Oui, enchaîne »).

**Sortie :** le registre `FINDINGS` d'ACTION, soit 39 fiches avec les 15 champs du §20, dans `DG_AUDIT_001_Phase10_02_FINDINGS_ACTION.csv`. La colonne `SEVERITY-PROVISOIRE (phase 2)` garde la traçabilité, comme en 10.01.

**Ce que ce rapport n'est pas :**
- ce n'est pas une décision de correction : la `PATCH-DECISION` relève de la phase 11 ;
- aucun patch, aucun verdict global.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan | Plan maître, état 10.01 |
| Bloc précédent | 10.01 DIRECTION |
| Checkpoint du propriétaire | `Audit_ACTION_Phase2_Checkpoint_Consolidation.md`, relu en entier : familles A–H, notes de déduplication 1–10, 14 protections |
| Empreintes | B01 `016e6002…` et protocole `990fc86f…` conformes |
| Protocole | §20 (gravité, 15 champs), §21 (types de correction), §32 |
| Sources de niveau 5 | **Les douze rapports ACTION de phase 2.** Les 106 sections `F-ACT-*` (définitions et mises à jour) ont été extraites et relues en entier. Les champs « Comportement », « Risque » et « Test futur » du CSV sont **repris mot pour mot** des fiches d'origine. |
| Dispositions ultérieures | Recherchées dans les 91 fichiers de rapport (copies incluses) qui citent un F-ACT hors rapports ACTION : checkpoints RUN_CARD, Validate_RUN_CARD, Fixtures, SAVOIR, QUICKSTART, BIBLIOTHEQUE, « cinq propriétaires », et unités 4.01–9.05 |
| Preuves d'objet | 6.02b, 9.06, 9.07, 9.08, citées fiche par fiche quand elles changent le jugement |

## 2. Méthode de classement

Même grille qu'en 10.01 : la gravité suit l'**impact réel**, en tenant compte des facteurs atténuants et des preuves d'objet.

**Règle de discrimination ajoutée pour ACTION.** La plupart des fiches ACTION ont la même forme : la prose protège, la projection machine (`RUN_CARD` et son validateur) ne le fait pas. Pour ne pas tout classer « Majeur », j'ai retenu **Majeur** seulement si les trois conditions suivantes sont réunies :
1. la machine **admet une acceptation** que le contrat humain interdit explicitement ;
2. le risque touche la **sécurité, la vérité de la preuve ou le droit** (pas seulement la qualité) ;
3. le contournement est **reproduit** par mutation ou par un cas d'essai.

Une cause systémique qui couvre tous les modes (F-ACT-021) est traitée comme un cas à part (voir §5).

**Pourquoi aucun Bloquant.** F-ACT-017 et F-ACT-038 laissent passer un risque critique en machine, ce qui touche le critère « risque critique ». Je les maintiens en Majeur pour trois raisons :
- le contrat humain les exclut sans ambiguïté ;
- ACTION déclare que la validation d'une carte ne prouve pas le monde ;
- aucun run observé n'a diffusé un défaut critique.

C'est le même raisonnement que pour F-DIR-007 en 10.01.

## 3. Résultat

| Gravité | Nombre | IDs |
|---|---:|---|
| Bloquant | 0 | — |
| **Majeur** | **10** | 010, 012, 015, 017, 018, 021, 022, 023, 024, 038 |
| **Significatif** | **23** | 001, 002, 005, 006, 007, 008, 009, 011, 013, 014, 019, 020, 025, 026, 027, 028, 029, 030, 031, 033, 036, 037, 039 |
| **Mineur** | **5** | 003, 004, 016, 032, 034 |
| **Observation** | **1** | 035 |

**Décisions :**
- 33 fiches `RETENU → phase 11` ;
- 5 fiches `RETENU (mineur) → lot éditorial` ;
- 1 fiche `OBSERVATION` ;
- aucun `RATTACHÉ` : les liens de cause sont notés dans `DEPENDENCIES`, sans retirer de test.

## 4. Écarts avec les gravités provisoires de phase 2 (10 sur 39)

Six « Majeur provisoire » sont **confirmés** en Majeur : 012, 015, 018, 021, 024, 038. Seul le suffixe tombe, le niveau ne change pas.

Dix fiches sont **abaissées**, aucune n'est relevée :

| ID | Phase 2 → 10.02 | Raison |
|---|---|---|
| F-ACT-009 | Majeur → **Significatif** | Un verdict accepté avant `DECIDED` est déjà refusé. La valeur que la machine force est donc non acceptante : sous-déclaration, pas fausse acceptation (4.01 N1) |
| F-ACT-026 | Majeur p. → **Significatif** | L'ambiguïté des lignes 499–505 est levée dans le même propriétaire : ACTION/AUTHORITY interdit la baisse silencieuse, et B3 dit qu'un contrepoint est une preuve, pas une autorisation. Reste le transport |
| F-ACT-033 | Majeur p. → **Significatif** | Contradiction interne à Gate A (677 contre 653/665), déjà corrigée par SAVOIR/MOTION ; aucun cas observé. Correction d'un mot, à faire tôt car peu coûteuse |
| F-ACT-036 | Majeur p. → **Significatif** | Le risque porte sur la qualité, pas sur la sécurité ; au texte, B1b a fonctionné (A2, 9.06). Occurrence de la cause F-ACT-021 |
| F-ACT-003 | Significatif p. → **Mineur** | 5.02 : les deux ensembles sont une progression et une catégorisation ; aucun remplissage confus observé. Question de nom |
| F-ACT-004 | Significatif → **Mineur** | Le critère de SAVOIR/ROUTING (« prochaine décision / preuve / limite ») couvre le cas ; une capacité manquante donne `NOT-VERIFIED`. Alignement d'une phrase |
| F-ACT-016 | Significatif → **Mineur** | Portée limitée à LITE et petits ITER. 9.08 mesure le problème **inverse** (surcharge de clôture LITE) : le remède est un noyau LITE court |
| F-ACT-032 | Significatif p. → **Mineur** | SAVOIR/TYPE porte le contrat complet ; le défaut est le mot « complète » et l'absence de renvoi. La licence reste couverte par F-ACT-024 |
| F-ACT-034 | Significatif → **Mineur** | Le validateur applique la lecture protectrice, avec une fixture négative officielle : l'écart produit un rejet **visible** (même logique que F-DIR-045) |
| F-ACT-035 | Significatif p. → **Observation** | Trois passages bornent déjà la claim (CONFORMANCE-TARGET, 653, SAVOIR/TECH) ; les pilotes ne revendiquent rien (9.07) |

**Signal de biais à connaître.** Dans deux unités de suite (10.01 et 10.02), je n'ai fait qu'abaisser : 23 abaissements, 0 relèvement. Deux explications sont possibles :
- la phase 2 était volontairement prudente (« à éprouver ») ;
- mon jugement d'auditeur seul penche vers l'indulgence.

Je ne peux pas trancher seul entre les deux. Chaque abaissement a une raison écrite et contestable. Si l'owner préfère la prudence de phase 2, les dix fiches reprennent leur niveau d'origine sans changer l'ordre des grappes de la phase 11.

## 5. Déduplication et causes

Aucune fusion. Les notes 1–10 du checkpoint sont confirmées ; chaque ID garde sa mutation négative. Les liens qui orienteront la phase 11 :

- **F-ACT-021, cause systémique des paquets par mode.** Les fiches F-ACT-015 (SYSTÈME), F-ACT-036 (B1b) et F-ACT-031 (baseline) en sont des occurrences qui gardent leur propre ID.
  - F-ACT-015 reste **Majeur** pour son rayon d'impact : consumers, migration, rollback.
  - F-ACT-036 et F-ACT-031 sont Significatif.
- **F-ACT-014 est un prérequis de F-DIR-011 (+019).** Ceci règle la réserve laissée en 10.01 : la triade `N/A-JUSTIFIED` / `NOT-VERIFIED` / `NOT-OBSERVED` ne peut être reprise par DIRECTION que si ACTION donne d'abord une place canonique à `NOT-OBSERVED`. Il n'y a pas de fusion (propriétaires et tests différents), mais un **ordre de correction** : ACTION, puis DIRECTION.
- **F-ACT-017 et F-DIR-007 : même scénario, deux étages.** DIRECTION classe, ACTION fait gouverner la clôture par `failure_action`. Les deux restent Majeur, dans la même grappe de priorité 1.
- **F-ACT-019 → cause F-ACT-022** (fraîcheur).
- **Distinctions confirmées :**
  - 026/037 : l'autorité et l'indépendance du regard ;
  - 033/035 : l'alternative prévue et le PASS ciblé ;
  - 038/039 : la légitimité de l'exception et sa disposition ;
  - 009/013 : deux erreurs temporelles inverses ;
  - 024/028 : le droit et la trace.
- **Transmis à 10.04 (façades et machine) :**
  - F-ACT-010 face à F-RC-001 (même règle ou non) ;
  - F-ACT-002 face à F-SK-001 (mesure 9/13 N/A de 9.08) ;
  - F-ACT-008 face aux F-FIX.

## 6. Ce que les preuves d'objet ont changé

| Fiche | Observation d'objet |
|---|---|
| **F-ACT-021** | 9.06 T1 : une carte DIRECTION `ACCEPTED/HELD` est admise alors que ses propres champs nomment « signature non située ». La protection repose entièrement sur le jugement de l'agent. **Majeur confirmé.** |
| **F-ACT-022** | 9.07 : **au texte**, la règle de fraîcheur a fait refaire contraste, mobile et couleurs forcées sur B′ (protection positive). **En machine**, la preuve V1 reste acceptée pour V2 (4.08, 9.02). **Majeur maintenu** : humain et machine divergent. |
| **F-ACT-017** | 9.08 : START reclasse bien un changement de consentement, au texte seulement ; la machine accepte LITE avec protection critique (4.01, 7.02) |
| **F-ACT-002** | 9.08 : 9 champs HANDOFF sur 13 deviennent N/A pour une correction LITE. C'est la première mesure de coût sur un run réel |
| **F-ACT-036** | 9.06 : B1b et DOUBLE-LOOP ont produit A2, meilleure que A. Le défaut est bien la non-opposabilité machine, pas la règle |
| **F-ACT-037** | Toute la campagne 6.02b–9.08 repose sur un observateur unique, déclaré comme tel : la limite est réelle et récurrente |
| **F-ACT-016** | 9.08 montre la surcharge, pas l'arrêt prématuré : abaissement |

## 7. Constat transversal : une décision préalable pour la phase 11

**26 des 39 fiches** (dont les 10 Majeur) sont des écarts entre le contrat humain et la projection `RUN_CARD` : 002, 005, 006, 007, 009, 010, 011, 012, 013, 014, 015, 017, 018, 020, 021, 022, 023, 024, 027, 028, 030, 031, 036, 037, 038, 039.

Les corriger une par une produirait 26 patches de schéma et de validateur : c'est le risque de bureaucratisation du §32. Une seule question, posée **avant** les correctifs, en fixe la forme.

**D-ACT-1 — Quelle autorité donne-t-on à une `RUN_CARD` validée ?** (à décider par l'owner en phase 11, pas ici)

| Option | Effet | Coût |
|---|---|---|
| **a. Relever la machine** | Le validateur impose les invariants d'acceptation : risque ↔ protection, capacité ↔ claim, version ↔ preuve, réserve, exception | Beaucoup de schéma ; risque de formulaire universel (F-ACT-006) |
| **b. Réduire la claim** | La validation n'atteste que la forme ; `ACCEPTED` exige une trace lue et une revue nommée ; le PASS ne vaut plus acceptation | Peu de schéma ; le contrôle repose sur le jugement, comme T1 l'a montré |
| **c. Mixte** | Seuls les invariants déterministes et à fort risque deviennent machine (017, 022, 038, 010, 024) ; le reste est déclaré « forme seule » | Intermédiaire ; demande une liste close |

Cette décision remplace une partie des recommandations de fiche. Les colonnes `RECOMMENDATION` renvoient à « D-ACT-1 » quand c'est le cas.

## 8. Entrée pour la phase 11 (ordre proposé, non décidé)

| Priorité | Grappe | Fiches | Type (§21) | Propriétaire |
|---|---|---|---|---|
| 0 | **Décision D-ACT-1** | — | Décision d'architecture | Owner |
| 1 | Protection critique et exception | **017**, **038**, 039 (+ F-DIR-007) | Alignement humain/machine | ACTION/OVERRIDE, RUN_CARD ; DIRECTION/START |
| 1 | Invariants d'acceptation | **010**, **012**, **018**, **022** (+019), **023**, **024** | Alignement selon D-ACT-1 | ACTION/STATUS ; validateur |
| 1 | Paquets de clôture par mode | **021**, **015**, 036, 031 | Alignement selon D-ACT-1 | ACTION/CLOSE-PACKAGE, RUN-SYSTEM |
| 2 | Registres et temps | 014 (**avant** F-DIR-011), 009, 013, 011, 027, 025 | Clarification ; alignement | ACTION/STATUS |
| 2 | Formes et projections (rejoint la grappe DIRECTION) | 002, 005, 006, 007, 028, 029, 030 | Simplification | ACTION ; schéma des contrats |
| 3 | Autorité, droits et gates spécialisés | 026, 033, 037 | Clarification | ACTION/AUTHORITY, GATE-A, GATE-B |
| 3 | Accès et chargement | 001 (+ F-DIR-028), 020 | Routing ; alignement outil | ACTION ; READING_MAP ; CLI |
| 3 | Outillage | 008 | Correction d'outil | CLI |
| 4 | Lot éditorial ACTION | 003, 004, 016, 032, 034 | Clarification | ACTION |
| — | Observation | 035 | Aucune, test futur nommé | — |

**Protections à préserver pendant toute correction :** les 14 du checkpoint ACTION. En particulier :
- `CLOSED` n'est pas une acceptation ;
- LITE n'hérite pas des formalités SYSTÈME ;
- pas de quota de variantes ;
- `FAIL-ASSUMED` reste une exception bornée.

## 9. Sortie

- **ACTION : 39/39 fiches classées** avec leurs 15 champs.
- **Registre global : 85/157 classées.** Restent 72 fiches provisoires : SAVOIR, BIBLIOTHEQUE, CHANGELOG (16) et façades/machine (56).
- Aucun nouvel ID. Une décision d'architecture (D-ACT-1) est formulée pour l'owner.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- 10 gravités ajustées, avec raison écrite ;
- une règle de discrimination Majeur rendue explicite et contestable ;
- l'ordre de correction 014 → F-DIR-011 est fixé ;
- 26 fiches ramenées à une seule décision préalable, au lieu de 26 patches.

**Prochaine unité : 10.03 SAVOIR / BIBLIOTHEQUE / CHANGELOG** (16 fiches). Sources : les rapports sectionnels de ces trois propriétaires et leurs checkpoints ; même méthode.
