# DG-AUDIT-001 — Phase 11.05 — PATCH-DECISION B3 : paquets de clôture par mode et B1b

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.05 ». Cadre : **D-ACT-1 = c**, et la liste close publiée en 11.04.

**Grappe B3 (5 fiches, dont 2 Majeur) :**

| Fiche | Gravité | Objet |
|---|---|---|
| **F-ACT-021** | Majeur | Les paquets de clôture propres à chaque mode ne gouvernent pas la projection (cause systémique) |
| **F-ACT-015** | Majeur | Le minimum SYSTÈME n'est ni représenté ni contrôlé |
| F-ACT-036 | Significatif | B1b obligatoire, mais invisible et non opposable |
| F-ACT-031 | Significatif | Une non-régression sans baseline identifiée |
| F-BIB-001 | Significatif | L'exception « paire équivalente » de SELECT élargie hors de B1b |

**Sorties :**
- cette `PATCH-DECISION` ;
- `B3_harnais_non_regression.py` ;
- la liste close mise à jour, avec 4 invariants : **47 actifs**.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00–11.04 (D-ACT-1 = c ; règle A2 ; « qui accepte prouve » ; liste close) |
| Empreintes | B01 `016e6002…` conforme |
| Sources propriétaires relues | ACTION 196–202 (minimum par mode), 335–404 (routes RUN-* et CLOSE-PACKAGE), 586–594 (baseline), 700–716 (B1b) ; BIBLIOTHEQUE/FAST-PATH 169–173 |
| Machine relue | Schéma : aucun objet de mode, sauf les blocs DIRECTION. Validateur : invariants DIRECTION existants (INV-E07 à E14) |

## 2. Re-vérification sur B01

**Sur l'exemple canonique, B01 accepte :**
- une carte **SYSTÈME** acceptée avec réserve, sans aucun élément SYSTÈME : ni consumers, ni migration, ni rollback, ni non-régression, ni référence CHANGELOG ;
- une carte **DIRECTION** acceptée avec réserve, où B1b n'est pas représentable du tout ;
- une carte **ITER** acceptée sans trace ni diff. C'est F-ACT-020 (grappe C4) ; je le note ici sans le traiter.

**Harnais B3 : témoin 1/1, tests B3 1/12.**
- Le seul succès est **B3-P3** : la fixture officielle SYSTÈME en retour (`valid_closed_return`) reste valide sans paquet. C'est le témoin de proportion.
- Les autres échouent parce que les champs des contrats B2 et B3 n'existent pas encore. Le harnais suppose B2 en place.

## 3. Ce qui change la décision : F-ACT-021 n'appelle pas cinq paquets machine

La cause systémique de F-ACT-021 : « un verdict vert ne dit pas si le paquet du mode a été conservé ». Deux remèdes s'offraient :

| Remède | Effet | Coût |
|---|---|---|
| Cinq objets de paquet, un par mode, tous contrôlés | La machine « couvre » tout | Le formulaire universel que F-ACT-006 dénonce déjà. LITE et ITER portent la charge de SYSTÈME. Contredit « qui accepte prouve, **à proportion** » |
| **Contrôle machine là où le rayon d'impact est fort, forme seule ailleurs, et une promesse explicite** | La machine couvre **SYSTÈME** (blast radius, consumers) et **DIRECTION** (déjà largement couverte ; il manque B1b). Pour LITE, ITER et STANDARD, le paquet vit dans la trace, et la promesse dit que la machine ne le vérifie pas | 4 invariants ; aucune charge nouvelle pour LITE, ITER, STANDARD (témoin B3-P4) |

**Choix : le second.** C'est l'application directe de D-ACT-1 = c. F-ACT-021 est corrigée par **la fin de l'ambiguïté** : la table CLOSE-PACKAGE dira, mode par mode, ce que la machine contrôle. Elle ne l'est pas par l'extension du contrôle à tout.

**Limite déclarée (9.06 T1).** Une carte DIRECTION qui s'accepte en nommant elle-même un défaut de signature reste acceptable si ses champs sont cohérents. Le sens d'un texte libre n'est pas déterministe. Deux choses réduisent ce risque sans le supprimer :
- **B1b devient obligatoire** pour toute DIRECTION acceptée avec V en `PASS` ou `PASS-WITH-RESERVATION` ;
- **l'axe V** doit être déclaré (B2).

## 4. Les sept questions du §21

| Question | Réponse |
|---|---|
| Change une décision, une preuve ? | **Oui.** F-ACT-015 porte sur les changements partagés, avec le plus fort rayon d'impact ; B1b porte sur la preuve de la décision visuelle en DIRECTION |
| Défaut réel ? | **Oui**, re-vérifié (§2) |
| Gain > charge ? | **Oui**, parce que le périmètre est limité à SYSTÈME et DIRECTION acceptés (§3) |
| Nouvelle autorité ? | **Non.** `system_package` reprend ACTION 200/399 champ pour champ. `b1b` reprend ACTION 704–714, y compris **les deux seuls motifs** de N/A recevables. La baseline reprend ACTION 590 |
| Testable ? | Oui : 8 négatifs avec motif, 4 positifs (dont 2 témoins de proportion) |
| Positif / défensif équilibré ? | Oui. B3-P2 accepte une B1b qui **confirme** l'original (« conserver l'original est un résultat valide », ACTION 712) ; aucun quota de variantes |
| Suppression ou fusion ? | **Pas de nouvel objet de réserve** : les réserves SYSTÈME utilisent l'objet unique de B2. Et **aucun paquet pour les trois modes légers** |

## 5. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **alignement humain/machine** : 4 invariants et 2 objets ;
- **clarification** : table CLOSE-PACKAGE, correspondance des champs, promesse ;
- **correction normative locale** : BIBLIOTHEQUE 173.

### 5.1 Invariants B3 (ajoutés à la liste close)

| ID | Invariant | Fiches |
|---|---|---|
| **INV-B3-1** | SYSTÈME ∧ verdict accepté ⇒ `closure.system_package` complet : impact, consumers (≥ 1), owner, migration, rollback, non_regression, changelog_ref ; sans vide ni placeholder | F-ACT-015, F-ACT-021 |
| **INV-B3-2** | `non_regression.baseline` = {locator, version, état} | F-ACT-031 |
| **INV-B3-3** | DIRECTION ∧ verdict accepté ∧ V ∈ {PASS, PASS-WITH-RESERVATION} ⇒ `closure.b1b`. Statut `DONE` ⇒ une paire avec deux captures **distinctes**, la décision éprouvée et son issue (confirmée, modifiée ou abandonnée) | F-ACT-036, F-ACT-021 |
| **INV-B3-4** | `b1b` en `N/A-JUSTIFIED` ⇒ motif ∈ {aucune décision éditable, paire équivalente valide}, décision couverte, owner, prochaine preuve ; paire équivalente ⇒ référence de la paire | F-ACT-036, F-BIB-001 |

**Liste close : 50 lignes, 47 invariants actifs.**

**Forme seule (ajout à la promesse du validateur) :**
- pour LITE, ITER et STANDARD, le paquet de clôture vit dans la trace ; la machine ne le vérifie pas ;
- pour tous les modes, la machine ne vérifie pas que les consumers listés sont tous les consumers réels, que la baseline montre ce qu'elle prétend, ni que la décision « couverte » par une paire équivalente est bien la même.

### 5.2 Retouches de texte

| # | Où | Quoi |
|---|---|---|
| T-1 | ACTION/CLOSE-PACKAGE 391–404 | Une colonne **« Contrôle machine »** : SYSTÈME → `system_package` ; DIRECTION → invariants DIRECTION et B1b ; LITE, ITER, STANDARD → **forme seule, dans la trace**. Une phrase : « Un verdict vert ne certifie que ce que la liste close contrôle » (F-ACT-021) |
| T-2 | ACTION 200 et RUN-SYSTEM 379–387 | Correspondance vers `system_package` (F-ACT-015) |
| T-3 | ACTION 586–594 | Correspondance de la baseline (F-ACT-031) |
| T-4 | ACTION 704–716 | Correspondance vers `closure.b1b` ; les deux motifs de N/A deviennent les deux valeurs admises (F-ACT-036) |
| T-5 | BIBLIOTHEQUE 173 | « Paire équivalente : seulement lorsque **B1b est déclenché** et que la paire couvre **exactement la même décision** — voir ACTION/B1b » (F-BIB-001 ; marquage D-FAC-1 = c) |
| T-6 | Promesse du validateur (README, ACTION, `machine_projection.md`) | Ajout de la ligne « par mode » (§5.1) |

## 6. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | Après A1 et A2, **dans la même migration de schéma que B1 et B2** |
| C2 | **Proportion** : aucune exigence nouvelle pour LITE, ITER et STANDARD, ni pour une carte SYSTÈME ou DIRECTION non acceptante (témoins B3-P3, B3-P4) |
| C3 | **Consommateurs** : l'exemple canonique (DIRECTION acceptée) reçoit une B1b réalisée, ce qui en fait un **exemple d'apprentissage** du geste ; `valid_direction_with_profile_decision` aussi ; `valid_closed_return` inchangée pour B3 ; `machine_projection.md` mise à jour. Aucun fichier ajouté |
| C4 | Aucun quota : une B1b qui confirme l'original est un succès |
| C5 | Relecture complète d'ACTION 335–404 et 700–716, et de BIBLIOTHEQUE 161–203, après patch |

## 7. Condition de sortie (phase 13)

1. `B3_harnais_non_regression.py` : **1/1 et 12/12**.
2. Harnais A1, A2, B1 et B2 verts.
3. `validate_all` : `FULL VALIDATION PASSED`.
4. **Rejeux :**
   - 4.04 et 4.02 N1 (carte SYSTÈME acceptée sans consumers, migration ni rollback) → **refusés** ;
   - 9.03 (composant partagé) → le paquet est exigé à l'acceptation ;
   - 9.06 T1 → **limite déclarée**, pas un succès revendiqué (§3).
5. La table CLOSE-PACKAGE et la promesse disent, pour chaque mode, ce qui est contrôlé et ce qui ne l'est pas.

## 8. Sortie

- **PATCH-DECISION B3 : CORRIGER** : 4 invariants (liste close : 47 actifs), 2 objets, 6 retouches de texte.
- **F-ACT-021 résolue par délimitation plutôt que par extension** : la machine contrôle les deux modes à fort enjeu ; les trois autres sont déclarés « forme seule ».
- **Grappes B1 à B3 décidées** : les 11 Majeur « machine » d'ACTION et de DIRECTION ont chacun un invariant ou une délimitation explicite. Il reste B4 (ancres, dont F-DIR-027 Majeur) et B5.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- un Majeur systémique traité par une frontière nommée plutôt que par cinq formulaires ;
- les deux seuls motifs légitimes de N/A B1b deviennent les deux seules valeurs admises, ce qui corrige aussi F-BIB-001 côté machine ;
- l'exemple canonique va enseigner la B1b au lieu de l'omettre ;
- une limite (9.06 T1) est déclarée plutôt que prétendue couverte.

**Prochaine unité : 11.06 PATCH-DECISION B4** (ancres : **F-DIR-027** Majeur, contrat humain et machine divergents ; F-SAV-003 revue indépendante prise pour calibration).
