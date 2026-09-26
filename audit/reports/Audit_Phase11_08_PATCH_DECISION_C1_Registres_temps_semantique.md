# DG-AUDIT-001 — Phase 11.08 — PATCH-DECISION C1 : registres, temps et sémantique de preuve

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.08 ». Première grappe C, et la plus grosse restante.

**Grappe C1 : 14 fiches, 0 Majeur.**
- **ACTION** : F-ACT-009, 011, 013, 014, 025, 027.
- **DIRECTION** : F-DIR-011 (+ F-DIR-019 rattachée), 021, 024, 029, 032, 033.
- **SAVOIR** : F-SAV-005.

**Sorties :**
- cette `PATCH-DECISION` : une décision de grappe, avec des sous-décisions quand une fiche diverge ;
- `C1_harnais_non_regression.py` : partie machine et gardes textuelles ;
- la liste close mise à jour : **58 invariants actifs**.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00–11.07 (D-ACT-1 = c, D-FAC-1 = c, règle A2, « qui accepte prouve », liste close) |
| Empreintes | B01 `016e6002…` conforme |
| Sources relues | ACTION 116–153 (STATUS), 204–240 (contrat de décision, trace post-build, sortie ATLAS), 405 et 437–439 (polish), 505–512 (écarts post-build) ; DIRECTION 231–235, 314–324, 385–389, 468–482 (vérité de la scène), 493 (DOUBLE-LOOP), 626–642 (ABSOLU 5) ; SAVOIR 582–600 (STYLE) |
| Machine relue | Schéma : `decision_change` (deux chaînes libres), `profile_decision`, `creative_close`, `closure.verdict` (non nullable) |

## 2. Re-vérification sur B01

**Machine, sur l'exemple canonique :**

| Carte | B01 |
|---|---|
| STANDARD clôturée et acceptée **sans conséquence décisionnelle** | **acceptée** (F-ACT-013) |
| `decision_change.value = "NOT-OBSERVED"` avec verdict `ACCEPTED` | **acceptée** : la conséquence attendue est absente, et pourtant tout est accepté (F-ACT-014) |
| Carte `INTAKE` avec verdict `null`, **honnête** | **rejetée** : le verdict est obligatoire dès l'entrée, ce qui force un verdict prématuré (F-ACT-009) |
| `RECLASSIFIED` sans mode de destination | rejetée, mais pour un autre motif (F-RC-001) ; la transition n'est de toute façon pas représentable (F-ACT-011) |
| `next_polish_action = "STOP — le gain suivant serait du polish"` | **acceptée** : une phrase d'arrêt est **déjà valide** (voir §3.3) |

**Texte :**
- `NOT-OBSERVED` apparaît **zéro fois dans DIRECTION** et **zéro fois dans ACTION/STATUS**. Il n'est défini qu'à ACTION 226–236.
- La table « Distingue trois niveaux de preuve » est présente (F-DIR-033).
- VISUAL_TARGET nomme « Preuve » un objet produit (F-DIR-024).

**Harnais C1 :** témoin 1/1, machine 0/13, gardes textuelles 0/10.

## 3. Ce que la re-lecture change

### 3.1 La triade existe déjà : il faut la rendre visible, pas l'inventer

ACTION 230–236 définit exactement la distinction que F-DIR-011 réclame. Après observation :
- `DECISION-CHANGE` si une décision a changé, a été confirmée ou abandonnée ;
- `N/A-JUSTIFIED` si **aucune conséquence n'était applicable** ;
- `NOT-OBSERVED` si **une conséquence attendue n'a pas été observée**.

`NOT-VERIFIED`, lui, vit dans les axes : une preuve manque.

Le défaut a deux faces :
- ACTION/STATUS ne liste pas cette « conséquence décisionnelle » parmi ses plans (F-ACT-014) ;
- DIRECTION n'en reprend que la moitié (F-DIR-011 et F-DIR-019).

**Décision : la triade n'est pas un nouveau registre.** Ce sont les **valeurs du champ `DECISION-CHANGE`**, déjà canoniques. ACTION/STATUS l'écrit une fois ; DIRECTION y renvoie.

**L'ordre imposé par 10.01 est respecté** : F-ACT-014 (le canon ACTION) passe avant F-DIR-011 (les trois occurrences DIRECTION).

### 3.2 La machine peut porter la triade à peu de frais

Aujourd'hui, `decision_change` est fait de deux chaînes libres. Un champ `outcome` typé rend la triade vérifiable. Il permet aussi deux règles simples, toutes deux tirées d'ACTION 236 : une conséquence attendue mais non observée interdit l'acceptation pleine, et une carte qui accepte doit dire ce qui a changé.

### 3.3 Deux fiches se résolvent sans machine

- **F-ACT-025 (STOP du polish).** B01 accepte déjà « STOP — raison ». Le défaut est que le texte ne dit pas que c'est permis, et que la phrase « prochaine action de polish » invite à en inventer une. **Correction de texte seulement** : une phrase dans ACTION 405 et 437–439. **Pas de changement de schéma** : §21, préférer le moins.
- **F-ACT-027 (CORRECTED, ACCEPTED-DIFFERENCE, REMAINING-RISK).** Ces valeurs d'ACTION 509 ne sont pas des statuts. Ce sont des **résultats locaux de comparaison**, qui se traduisent dans des objets existants :
  - `CORRECTED` → `decision_change` CHANGED, avec la nouvelle preuve ;
  - `ACCEPTED-DIFFERENCE` → `HELD-WITH-ACCEPTED-DIFFERENCE` et une réserve (objet de B2) ;
  - `REMAINING-RISK` → une réserve.

  Texte seulement.

### 3.4 Preuve d'objet (9.08)

Le run avec DG a affiché « TRUTH/MECHANISM » **dans l'interface produit**, et a dû compléter en prose (« taux illustratifs »). Cette observation fonde F-DIR-021 (à qui s'adresse le marquage) et F-DIR-029 (deux axes mêlés dans une seule liste).

## 4. Les sept questions du §21 (grappe)

| Question | Réponse |
|---|---|
| Change une décision, une preuve ? | **Oui.** Une conséquence absente peut être acceptée ; un verdict est forcé trop tôt ; la vérité d'un contenu fictif est mal dite aux utilisateurs (9.08) |
| Défaut réel ? | **Oui**, re-vérifié (§2) |
| Gain > charge ? | **Oui.** 6 invariants, dont un assouplissement. Un seul champ nouveau obligatoire (`outcome`), et seulement quand `decision_change` est présent ou exigé. Le reste est du texte |
| Nouvelle autorité ? | **Non.** Chaque valeur existe déjà (ACTION 206–236, STATUS 121–139, SAVOIR 582–593). Aucun statut n'est ajouté ; les résultats locaux d'ACTION 509 sont **ramenés** à des objets existants |
| Testable ? | Oui : 9 négatifs avec motif, 4 positifs, 10 gardes textuelles |
| Positif / défensif équilibré ? | **Oui, avec trois gains positifs** : une carte `INTAKE` honnête devient valide ; « STOP » est reconnu ; LITE n'a toujours pas de `decision_change` obligatoire |
| Suppression ou fusion ? | **Oui.** Suppression de la table « trois niveaux de preuve » (F-DIR-033 : jamais mobilisée, §32). INV-E24 (DIRECTION seule) est absorbé dans une règle générale. Aucun changement de schéma pour le STOP |

## 5. PATCH-DECISION C1 : CORRIGER

### 5.1 Invariants machine (liste close)

| ID | Invariant | Fiches |
|---|---|---|
| **INV-C1-1** | `decision_change.outcome` ∈ {CHANGED, CONFIRMED, ABANDONED, N/A-JUSTIFIED, NOT-OBSERVED} ; N/A-JUSTIFIED ⇒ une raison | F-ACT-013, F-ACT-014, F-DIR-011 |
| **INV-C1-2** | `NOT-OBSERVED` ⇒ verdict ≠ `ACCEPTED` (la réserve reste possible) | F-ACT-014 |
| **INV-C1-3** | Clôturée ∧ acceptée ∧ mode ≠ LITE ⇒ `decision_change`. **Absorbe INV-E24** | F-ACT-013 |
| **INV-C1-4** | Verdict **nullable**. Avant `CHECKING`, le verdict est `null` ; à `DECIDED` et `CLOSED`, il est présent | F-ACT-009 |
| **INV-C1-5** | `RECLASSIFIED` ⇒ `closure.reclassification` {mode cible ≠ mode, référence du run successeur} | F-ACT-011 |
| **INV-C1-6** | `profile_decision.phase` ∈ {intended, observed} ; carte acceptée ⇒ `observed` | F-SAV-005 |

**Liste close : 62 lignes, 58 invariants actifs.**

**Forme seule :**
- que la conséquence déclarée « confirmée » l'ait réellement été ;
- que le run successeur existe ;
- qu'un profil « observed » ait vraiment été observé.

### 5.2 Corrections de texte

| # | Fiche | Où | Quoi | Type §21 |
|---|---|---|---|---|
| T-1 | F-ACT-014 | ACTION/STATUS | Une ligne « **Conséquence décisionnelle** (`DECISION-CHANGE`) : changée · confirmée · abandonnée · `N/A-JUSTIFIED` (aucune conséquence applicable) · `NOT-OBSERVED` (conséquence attendue absente). À ne pas confondre avec `NOT-VERIFIED` (preuve manquante, axes) » | Clarification |
| T-2 | F-DIR-011, 019 | DIRECTION 233, FIRST-OBJECT 322, ATELIER ~480 | Remplacer « N/A-JUSTIFIED » seul par la triade, avec « voir ACTION/STATUS » (D-FAC-1 = c) — **après T-1** | Clarification |
| T-3 | F-ACT-009, 011, 013 | ACTION 206–218 et STATUS | Correspondance vers `outcome` ; verdict nul avant décision ; champs de reclassement | Clarification |
| T-4 | F-ACT-025 | ACTION 405 et 437–439 | « `STOP — [raison]` est une valeur valide de `next_polish_action` : aucune action de polish n'est requise » | Clarification |
| T-5 | F-ACT-027 | ACTION 509 | « Ces valeurs sont des **résultats locaux de comparaison**, pas des statuts », avec leur correspondance (§3.3) | Clarification |
| T-6 | F-SAV-005 | SAVOIR 584–593 | `PROFILE-DECISION` se lit en deux temps : le **profil retenu** (intention, vers `DECISION-INTENT`) et **l'effet constaté après capture** (vers `DECISION-CHANGE`) | Clarification |
| T-7 | F-DIR-029 | DIRECTION 468–476 | Deux axes : **factualité**, `OBSERVED` ou `ILLUSTRATIVE`, obligatoire et exclusive ; **nature**, `MECHANISM`, qui se **cumule** avec la factualité. **La fiction l'emporte** : un élément illustratif rend le tout `ILLUSTRATIVE` | Correction normative |
| T-8 | F-DIR-021 | Même section | **Audience** : les labels `TRUTH/*` sont internes (spec, trace, annotations). Ils n'apparaissent **jamais** dans l'interface produit. Quand le public doit savoir, la divulgation se fait **en langage produit** (« données d'exemple », « taux illustratifs ») | Correction normative |
| T-9 | F-DIR-024 | VISUAL_TARGET 387 et DOUBLE-LOOP 493 | « Preuve » devient « **Objet de preuve** », et « preuve précoce » devient « objet de preuve précoce ». Le mot « preuve » reste réservé à ACTION. FIRST-OBJECT emploie déjà « objet de preuve » | Clarification |
| T-10 | F-DIR-032 | ABSOLU 5, 632 | DIRECTION **signale le risque** (population, accessibilité réelle, tâche critique). Le **choix de méthode** (utilisateur représentatif, expert, technique) relève d'ACTION/GATE-B et SAVOIR/CONTEXT. Une méthode non utilisateur ne soutient pas un claim d'usage (642 conservée) | Déplacement |
| T-11 | F-DIR-033 | ABSOLU 5, 634–640 | **Supprimer** la table « trois niveaux de preuve » : troisième taxonomie, jamais mobilisée en six unités de runs. La phrase 642 (capture ≠ preuve d'utilisabilité) est conservée | Suppression |

### 5.3 Sous-décisions (fiches qui s'écartent de la grappe)

- **F-DIR-019 : RATTACHÉE** à F-DIR-011 (10.01). Son test est conservé dans la garde G-02 et dans l'épreuve de lecture.
- **F-DIR-033 : SUPPRESSION**, et non une correspondance en une phrase. Une phrase de correspondance garderait une troisième grille sans usage ; la supprimer ne retire aucune obligation.
- **F-ACT-025 : texte seulement.** Le changement de schéma envisagé (objet `{CONTINUE|STOP}`) est **écarté** : B01 accepte déjà la chaîne STOP.

## 6. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | Ordre : **T-1 avant T-2** (canon ACTION avant les renvois DIRECTION) ; machine dans la migration de schéma unique (B1 à C1) |
| C2 | **Proportion** : aucun `decision_change` obligatoire pour LITE ; une carte `INTAKE` n'exige rien de plus qu'aujourd'hui, et même moins (verdict nul) |
| C3 | **Consommateurs** : l'exemple et les fixtures qui portent `decision_change` reçoivent `outcome`. `invalid_accepted_before_decision` (CHECKING) garde son motif, puisqu'INV-C1-4 autorise un verdict pendant CHECKING. `machine_projection.md` suit |
| C4 | **Aucun label `TRUTH/*` dans une interface produit** : la règle s'applique aussi aux exemples de la skill |
| C5 | Relecture complète d'ACTION 116–240 et 400–512, de DIRECTION 226–240, 314–345, 373–395, 466–500 et 620–645, et de SAVOIR 574–600 |

## 7. Condition de sortie (phase 13)

1. `C1_harnais_non_regression.py` : **1/1 ; machine 13/13 ; gardes 10/10**.
2. Harnais A1 à B5 verts ; `validate_all` : `FULL VALIDATION PASSED`.
3. **Épreuve de lecture**, par un lecteur neuf :
   - trois clôtures (conséquence obtenue, conséquence non applicable, conséquence attendue absente) → `CONFIRMED` ou `CHANGED`, `N/A-JUSTIFIED`, `NOT-OBSERVED`, sans confusion avec `NOT-VERIFIED` ;
   - **rejeu du micro-run 9.08** : le lecteur produit une interface sans label `TRUTH/*` visible, avec une divulgation en langage produit.

## 8. Sortie

- **PATCH-DECISION C1 : CORRIGER.**
  - 6 invariants (dont 1 assouplissement), 1 invariant absorbé : liste close à 58 actifs ;
  - 11 corrections de texte, dont une suppression et un déplacement ;
  - 3 sous-décisions.
- **L'ordre F-ACT-014 → F-DIR-011, fixé en 10.01, est tenu.**
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- la triade existait déjà : on la **rend visible** au lieu de créer un registre ;
- une taxonomie morte est supprimée ;
- un changement de schéma est écarté parce que la machine acceptait déjà la bonne réponse ;
- trois valeurs orphelines sont ramenées à des objets existants ;
- l'observation 9.08 (jargon dans l'interface) devient une règle d'audience testable.

**Prochaine unité : 11.09 PATCH-DECISION C2** (formes et projections : 14 fiches, dont F-ACT-002, le mapping HANDOFF → RUN_CARD, et le champ de risque transféré depuis B1). Elle bouclera la migration de schéma unique.
