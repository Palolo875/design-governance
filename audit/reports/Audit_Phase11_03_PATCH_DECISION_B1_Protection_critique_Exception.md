# DG-AUDIT-001 — Phase 11.03 — PATCH-DECISION B1 : protection critique et exception

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ». Cadre fixé en 11.00 : **D-ACT-1 = c.** Seuls les invariants déterministes et à fort risque passent en machine ; le reste est déclaré « forme seule ».

**Grappe B1 (6 fiches, dont 3 Majeur) :**

| Fiche | Gravité | Objet |
|---|---|---|
| **F-DIR-007** | Majeur | Correctif local critique sans classement stable |
| **F-ACT-017** | Majeur | La protection critique ne gouverne pas la clôture |
| **F-ACT-038** | Majeur | FAIL-ASSUMED accepte une preuve absente ou un risque exclu |
| F-ACT-039 | Significatif | Diffusion limitée sans disposition finale |
| F-DIR-016 | Significatif | Traduction humaine de START sans question de risque |
| F-QS-003 | Significatif | QUICKSTART 298 : mêmes conditions pour toute clôture non acceptée |

**Sorties :** cette `PATCH-DECISION` et `B1_harnais_non_regression.py`, écrit avant toute modification. Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan, décisions 11.00–11.02 | Relus ; règle A2 appliquée : un invariant = un cas unitaire avec motif |
| Empreintes | B01 `016e6002…` conforme |
| Protocole | §21, §22, §32 |
| Sources propriétaires relues | `DIRECTION` 127–146 (arbre et **Protection de niveau** 140), 253 et 664 (lignes LITE des tables), 300–312 (traduction humaine), 800 ; `ACTION` 116–153 (STATUS), 265–300 (RUN_CARD, capacités, preuve dégradée), 806–828 (OVERRIDE) ; `QUICKSTART` 298 |
| Machine relue | Schéma `risk`, `closure` ; `validate_run_card.py` 150–275 (`check_semantic_contract`) ; fixtures `valid_closed_return`, `invalid_critical_*`, `invalid_fail_assumed_accepted` ; `machine_projection.md` 90–97 |

## 2. Re-vérification sur B01

**Comportements machine, rejoués aujourd'hui sur l'exemple canonique modifié en mémoire :**

| Carte | B01 |
|---|---|
| `LITE` + risque `critical` + protection `BLOCKED` + verdict accepté avec réserve | **acceptée** |
| `ITER` + risque `critical` | **acceptée** |
| `STANDARD` + `critical` + verdict accepté, sans aucune trace du résultat du contrôle | **acceptée** |
| `STANDARD` + `critical` (`failure_action = BLOCKED`) + issue `FAIL-ASSUMED` | **acceptée** |
| `FAIL-ASSUMED` sans observation d'échec, sans autorisation, sans structure d'exception | **acceptée** |

**Harnais B1 : témoin 1/1, tests B1 0/12.**
- Deux tests échouent **par le défaut lui-même** : B1-03 (protection critique acceptée sans résultat) et B1-07 (FAIL-ASSUMED sans exception, acceptée).
- Les dix autres échouent parce que les champs proposés n'existent pas encore.

**Ce que le harnais montre au passage.** Sans exiger de motif, B1-01, 02, 04, 05, 06, 08 et 09 auraient paru **réussis sur B01** : ils sont rejetés, mais pour « champ inconnu ». C'est exactement le faux positif que la décision A2 interdit. La règle « un négatif = un motif » s'applique donc dès cette grappe.

**Côté texte, une vérification qui change le diagnostic de F-DIR-007.** La règle humaine est **déjà forte et claire** : DIRECTION 140, « Protection de niveau », interdit `LITE` et `ITER` dès qu'un risque critique est touché, et nomme les flux concernés (onboarding, consentement, permission…). Le défaut est donc ailleurs :
- **(a)** les deux tables LITE (253, 664) ne rappellent pas cette condition ;
- **(b)** la machine ne l'applique pas.

**Cohérence avec le corpus.** La fixture positive officielle `valid_closed_return` (`SYSTÈME`, risque `critical`, `failure_action = RETURNED`, issue `RETURNED`, verdict `RETURN`) respecte déjà les invariants proposés ci-dessous. Le système sait donc ce qu'il veut ; seule la machine ne le vérifie pas.

## 3. Les sept questions du §21

| Question | Réponse |
|---|---|
| Change une décision, une preuve, une exécution ? | **Oui.** Ce sont les trois Majeur où un danger critique peut être accepté ou diffusé |
| Défaut réel ? | **Oui**, re-vérifié (§2). Pour F-DIR-007, le défaut est dans les tables et la machine, pas dans START 140 |
| Gain > charge ? | **Oui.** 7 invariants, 2 champs, 4 fixtures à ajuster, 4 retouches de texte courtes. Pas de nouveau mode, pas de nouveau statut, pas de nouvelle valeur de verdict |
| Nouvelle autorité ? | **Non**, à trois conditions : les invariants traduisent des phrases **existantes** (DIRECTION 140, ACTION 283–299, 808–828) ; le vocabulaire (`RETURNED`/`BLOCKED`/`ESCALATED`, `PASS`/`FAIL`/`NOT-VERIFIED`) est déjà canonique ; la structure d'exception est celle qu'ACTION 427 applique déjà à FAIL-ASSUMED |
| Testable ? | **Oui** : 9 négatifs avec motif, 3 positifs |
| Positif / défensif équilibré ? | Oui. Les cartes non critiques sans exception ne changent pas. Un correctif local **non** critique reste en LITE (START 140, dernière phrase) |
| Suppression ou fusion ? | **Fusion** : l'exception FAIL-ASSUMED reprend l'objet de réserve de B2 (F-ACT-023) au lieu d'un second objet. **Pas d'ajout de valeur de verdict** pour la diffusion limitée : un champ de disposition suffit |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **alignement humain/machine** : invariants et deux champs ;
- **clarification** : quatre retouches de texte ;
- **amélioration de façade** : QUICKSTART et traduction humaine.

**Propriétaires :**
- DIRECTION pour la classification (tables) ;
- ACTION pour la protection, l'exception et la projection (texte, schéma, validateur) ;
- QUICKSTART en façade dérivée.

### 4.1 Invariants machine (contribution de B1 à la liste close de D-ACT-1)

| # | Invariant | Source humaine | Motif de rejet (sous-chaîne stable) | Fiches |
|---|---|---|---|---|
| **I-B1-1** | `risk.level = critical` ⇒ `mode ∉ {LITE, ITER}` | DIRECTION 140 | « risque critical interdit le mode LITE ou ITER » | F-DIR-007 |
| **I-B1-2** | `critical_protection.result ∈ {PASS, FAIL, NOT-VERIFIED}` est **requis** | ACTION 283–299 (une vérification absente n'est pas rédigée comme accomplie) | « critical_protection exige result » | F-ACT-017 |
| **I-B1-3a** | `result = NOT-VERIFIED` ⇒ `verdict ≠ ACCEPTED` (la réserve reste possible, comme le permet ACTION 299) | ACTION 299 | « verdict ACCEPTED interdit » | F-ACT-017 |
| **I-B1-3b** | `result = FAIL` ⇒ aucun verdict accepté **et** `issue = failure_action` | Sens même de `failure_action` | « protection critique en échec » / « issue doit suivre critical_protection.failure_action » | F-ACT-017, F-ACT-038 |
| **I-B1-4** | `issue = FAIL-ASSUMED` ⇒ `closure.exception` requise, avec : la structure de réserve commune (owner, scope, impact, review_date, next_proof, exit_condition), plus `gate_axis`, `failure_evidence` et `requested_by` | ACTION 808–824, 427 | « FAIL-ASSUMED exige closure.exception » | F-ACT-038 |
| **I-B1-5** | `exception.failure_evidence` ∈ `proof.observed` : un échec **connu**, pas un `NOT-VERIFIED` requalifié | ACTION 810 (« échec connu ») | « failure_evidence doit figurer dans proof.observed » | F-ACT-038 |
| **I-B1-6** | `exception.disposition ∈ {NON-DIFFUSÉ, DIFFUSÉ-LIMITÉ, RETIRÉ, ESCALADÉ}` est requise | ACTION 142, 810 | « exception exige disposition » | F-ACT-039 |

**Ce qui est déclaré « forme seule » (D-ACT-1 = c).** La machine ne vérifie ni que `requested_by` est bien l'utilisateur, ni que le périmètre est réellement limité, ni que le risque échappe aux catégories exclues par ACTION 826 (sécurité, dommage grave, conformité critique, action essentielle dangereuse). Ces jugements restent humains et la promesse du validateur le dira. **Une seule exception est couverte en machine :** quand la protection critique du run a échoué, I-B1-3b impose l'issue déclarée, ce qui ferme la voie FAIL-ASSUMED sur ce risque.

**Noms de champs :** indicatifs ; ils seront fixés en phase 12 avec l'objet de réserve de B2.

### 4.2 Retouches de texte (courtes, dans les propriétaires)

| # | Où | Quoi |
|---|---|---|
| T-1 | DIRECTION 253 et 664, lignes LITE (et les lignes ITER correspondantes, à confirmer en phase 12) | Ajouter « sans risque critique touché — voir Protection de niveau (START) ». Aligne les tables sur 140 et 800 (F-DIR-007) |
| T-2 | DIRECTION 302–310 | Une ligne : « Qu'est-ce qui coûterait cher si c'était faux ? » → `RISK`, Protection de niveau (F-DIR-016) |
| T-3 | ACTION, description de `critical_protection` et OVERRIDE 808–828 | Documenter `result`, la règle « l'issue suit `failure_action` en cas d'échec », et l'objet d'exception qui reprend la structure 413–427. Une phrase : « Si la protection critique du run a échoué, FAIL-ASSUMED n'est pas disponible sur ce risque » |
| T-4 | QUICKSTART 298 (façade, D-FAC-1 = c) | Conditions **par issue** : archive simple (BLOCKED, RETURNED, EXPLORATORY : owner, limite, prochaine preuve) / réserve (structure de réserve) / exception (FAIL-ASSUMED : « voir ACTION/OVERRIDE »). Plus d'approbation exigée pour archiver un blocage (F-QS-003) |

La référence `machine_projection.md` (ligne 94) documentera les deux champs : c'est un consommateur dérivé.

### 4.3 Transféré, pas abandonné

**F-ACT-017, première partie.** La carte ne dit pas **quel** est le risque principal (ACTION 271 : « risque principal et impact potentiel ») : le schéma n'a que le niveau. Ajouter un champ texte requis toucherait les 25 fixtures et l'exemple. Cette décision revient à **C2** (mapping HANDOFF → RUN_CARD, F-ACT-002), qui décidera de tous les champs projetés en une fois. La phase 12 regroupera ensuite toutes les modifications de schéma en **une seule migration**.

## 5. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Après A1 et A2** : chaque invariant arrive avec son cas unitaire à faute unique et son motif (règle A2) |
| C2 | **Une migration de schéma** pour tout le lot B, avec l'objet de réserve de B2 défini une seule fois et réutilisé par l'exception |
| C3 | **Fixtures à ajuster** : `valid_closed_return` (ajouter `result` ; elle reste valide) ; `invalid_critical_without_protection` et `invalid_critical_placeholder_protection` (ajouter `result`, garder leur faute) ; `invalid_fail_assumed_accepted` (ajouter une exception complète pour isoler sa faute). Aucun fichier ajouté |
| C4 | **Aucune nouvelle valeur** de mode, d'issue, d'état ou de verdict |
| C5 | La promesse du validateur (liste close de B2) nomme les sept invariants B1 et ce qui reste « forme seule » |
| C6 | Relecture complète de la zone ACTION 265–300 et 806–828 après patch : fort rayon d'impact (§22) |

## 6. Condition de sortie (phase 13)

1. `B1_harnais_non_regression.py` : **1/1 témoin et 12/12 tests** (9 négatifs rejetés **pour leur motif**, 3 positifs acceptés).
2. Harnais A1 (4/4, 11/11) et A2 (2/2, 5/5) inchangés.
3. `validate_all` : `FULL VALIDATION PASSED`, archives reproductibles.
4. **Rejeu de l'antécédent 9.08** : un changement de consentement classé LITE avec risque critique est désormais **refusé en machine**, et plus seulement au texte.
5. Relecture : les tables DIRECTION ne contiennent plus de ligne LITE qui omet la protection de niveau.

## 7. Sortie

- **PATCH-DECISION B1 : CORRIGER** : 7 invariants (I-B1-1 à I-B1-6, dont 3a et 3b ; liste close D-ACT-1), 2 champs, 4 retouches de texte, 1 transfert vers C2.
- Les 3 Majeur de B1 ont chacun un invariant testable, un motif, et un positif qui prouve que le cas légitime passe.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- F-DIR-007 est re-diagnostiquée : la règle existe, ce sont les tables et la machine qui l'ignorent ;
- une fixture officielle montre que les invariants traduisent l'intention du corpus ;
- une fusion (l'exception reprend l'objet de réserve de B2) évite un second objet ;
- aucune valeur nouvelle de statut ;
- le faux positif « rejet pour champ inconnu » est rendu visible et neutralisé par la règle A2.

**Prochaine unité : 11.04 PATCH-DECISION B2** (invariants d'acceptation : F-ACT-010, 012, 018, 019, 022, 023, 024, F-RC-001). Premier livrable : **la liste close complète de D-ACT-1**, qui intègre les sept invariants B1, et l'objet de réserve commun.
