# DG-AUDIT-001 — Phase 11.04 — PATCH-DECISION B2 : invariants d'acceptation et liste close de D-ACT-1

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.04 ». Cadre : **D-ACT-1 = c** (mixte).

**Grappe B2 (8 fiches, dont 6 Majeur) :**

| Fiche | Gravité | Objet |
|---|---|---|
| **F-ACT-010** | Majeur | Compatibilités issue / verdict / statut de direction |
| **F-ACT-012** | Majeur | Axe bloquant absent de la base du verdict |
| **F-ACT-018** | Majeur | Capacité absente compatible avec des claims inobservables |
| **F-ACT-022** | Majeur | Preuve d'une version, livraison d'une autre |
| **F-ACT-023** | Majeur | Réserve sans objet ni cycle de vie |
| **F-ACT-024** | Majeur | Droits inconnus sans effet sur le verdict |
| F-ACT-019 | Significatif | Snapshot incapable de dater sa péremption |
| F-RC-001 | Significatif | Interdit d'ancre qui force à mentir |

**Sorties :**
1. cette `PATCH-DECISION` ;
2. **`DG_AUDIT_001_Liste_close_invariants_RUN_CARD.csv`**, la **liste close de D-ACT-1** : les 46 lignes, existantes, nouvelles et retirées ;
3. `B2_harnais_non_regression.py`.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 (D-ACT-1 = c), 11.01–11.03 (A1, A2, B1 ; règle A2 : un invariant = un cas unitaire avec motif) |
| Empreintes | B01 `016e6002…` conforme |
| Sources propriétaires relues | ACTION 116–153 (STATUS), 164–175 (axes), 265–300 (RUN_CARD, capacités, preuve dégradée), 301–317 (snapshot), 405–435 (fraîcheur, réserves, droits) |
| Machine relue | Schéma : `artifact`, `capability_profile`, `proof`, `anchors`, `closure`, `allOf`. Validateur : les **38 messages de rejet** du contrat sémantique et du profil strict, tous inventoriés dans la liste close |

## 2. Re-vérification sur B01

**Rejoué aujourd'hui, sur l'exemple canonique modifié en mémoire. B01 accepte :**
- `RETURNED + ACCEPTED`, `RECLASSIFIED + ACCEPTED-WITH-RESERVATION` et `ESCALATED + ACCEPTED-WITH-RESERVATION` (F-ACT-010) ;
- `PARTIALLY-HELD + ACCEPTED` (F-ACT-010) ;
- une carte datée V99, acceptée avec une preuve V1 (F-ACT-022) ;
- `observed_at = "hier"` (F-ACT-022).

**B01 rejette** une ancre réellement transformée sous un verdict `RETURN`, alors que le retour est dû à une autre preuve manquante (F-RC-001).

**Harnais B2 : témoin 1/1, tests B2 1/19.**
- Le seul succès est **B2-P2** : la fixture officielle de retour simple (`valid_closed_return`) reste valide **sans aucun champ nouveau**. Elle servira de témoin de proportion après correction.
- Les autres échouent parce que les champs proposés n'existent pas encore, ou, pour B2-P3, à cause de F-RC-001.

**Constat nouveau sur l'exemple canonique.** Sa `basis` est « capacité déclarée dans le périmètre et les limites du run » : c'est une **déclaration non attestée** (ACTION 288). Or cet exemple est accepté avec réserve. **L'exemple officiel enseigne donc précisément le cas que F-ACT-018 décrit.** Il devra être mis à jour. C'est un consommateur direct, et un lien avec la grappe C6 (exemples de référence).

## 3. Les sept questions du §21

| Question | Réponse |
|---|---|
| Change une décision, une preuve ? | **Oui.** Ce sont six Majeur, où la machine accepte ce qu'ACTION interdit |
| Défaut réel ? | **Oui**, re-vérifié (§2) |
| Gain > charge ? | **Oui, sous une condition de proportion.** Les champs nouveaux ne sont exigés **que des cartes qui acceptent** (et `rights_status` des cartes DIRECTION). Les retours, explorations et blocages ne portent aucun champ de plus (témoin B2-P2). C'est le principe « qui accepte prouve » |
| Nouvelle autorité ? | **Non.** Chaque invariant traduit une phrase existante (colonne `SOURCE HUMAINE` de la liste close). **Une seule exception** : la matrice issue / verdict / statut n'est écrite nulle part. Elle est donc **d'abord ajoutée au texte** d'ACTION/STATUS (T-1), puis appliquée en machine |
| Testable ? | **Oui** : 16 négatifs avec motif, 3 positifs |
| Positif / défensif équilibré ? | Oui : B2-P2 (proportion) et B2-P3 (F-RC-001 : une ancre vraie n'est plus dégradée) sont des gains positifs |
| Suppression ou fusion ? | **Oui, trois fois.** INV-E11 est **retiré** (F-RC-001). INV-E17 (BLOCKED, FAIL-ASSUMED) est **généralisé** par INV-B2-1, et INV-E02 **remplacé** par INV-B2-6 : deux règles disparaissent dans des règles plus générales. **L'objet de réserve est unique** et réutilisé par l'exception de B1 |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **alignement humain/machine** : invariants et champs ;
- **correction normative** : la matrice de compatibilités, seul ajout de règle ;
- **clarification** : snapshot et promesse du validateur ;
- **suppression** : INV-E11.

**Propriétaire :** ACTION (texte, schéma, validateur) ; `machine_projection.md` et l'exemple en consommateurs.

### 4.1 Invariants B2 (détail dans la liste close)

| ID | Invariant | Fiches |
|---|---|---|
| INV-B2-1 | `issue ≠ null` ⇒ aucun verdict accepté (généralise INV-E17) | F-ACT-010 |
| INV-B2-2 | `PARTIALLY-HELD` ⇒ verdict ≠ `ACCEPTED`. `HELD-WITH-ACCEPTED-DIFFERENCE` reste le statut prévu pour une différence acceptée | F-ACT-010 |
| INV-B2-3 | Verdict accepté ⇒ `closure.axes {V,U,A,T}`. Un axe `RETURN` ⇒ aucun verdict accepté. Un axe `NOT-VERIFIED` ou `PASS-WITH-RESERVATION` ⇒ verdict ≠ `ACCEPTED` (la réserve reste possible) | F-ACT-012 |
| INV-B2-4 et 5 | Verdict accepté ⇒ `capability_profile` présent, et `provenance.capability` disponible (ni absente, ni déclarée indisponible) | F-ACT-018 |
| INV-B2-6 | `basis` typée selon les quatre sortes d'ACTION 288 ; la capacité d'une provenance acceptée ne repose pas sur une déclaration non attestée | F-ACT-018 |
| INV-B2-7 et 8 | Verdict accepté ⇒ `artifact.version` = `provenance.artifact_version` ; `observed_at` est une date ISO | F-ACT-022 |
| INV-B2-9 | `ACCEPTED-WITH-RESERVATION` ⇒ `closure.reservations` non vide ; chaque réserve porte les 7 attributs d'ACTION 413–422, sans placeholder, avec une `review_date` ISO | F-ACT-023 |
| INV-B2-10 | DIRECTION ⇒ `artifact.rights_status` ; `unknown` ⇒ verdict ≠ `ACCEPTED` | F-ACT-024 |
| (retrait) | INV-E11 : `transformed` redevient compatible avec un retour ; `ACCEPTED` exige toujours `transformed` (INV-E12) | F-RC-001 |

**L'objet de réserve commun.** Ses champs sont `owner`, `scope`, `date_version`, `impact`, `next_proof`, `review_date` et `exit_condition` : c'est la structure d'ACTION 413–422, mot pour mot. Il est utilisé tel quel par `closure.reservations[]`, et **étendu** par l'exception FAIL-ASSUMED de B1 (`gate_axis`, `failure_evidence`, `requested_by`, `disposition`).

### 4.2 La liste close (livrable de D-ACT-1)

| Statut | Nombre |
|---|---:|
| Existant conservé (dont 5 du profil strict) | 26 |
| Existant remplacé ou généralisé | 2 (INV-E02, INV-E17) |
| Existant retiré | 1 (INV-E11) |
| Nouveau B1 | 7 |
| Nouveau B2 | 10 |
| **Invariants actifs après correction** | **43** |

**Règle de clôture de la liste.** Tout invariant machine futur doit :
1. entrer dans cette liste avec sa source humaine ;
2. passer par une `PATCH-DECISION` ;
3. arriver avec son cas unitaire et son motif (règle A2).

Hors de la liste, la machine ne décide rien.

### 4.3 Promesse du validateur (texte à insérer)

Emplacements : README 128–129, ACTION près de 323, `machine_projection.md`.

> **Ce qu'atteste une RUN_CARD validée :** la forme de la projection et les invariants de la liste close (états, issues, verdicts, axes, protection critique, exception, capacité de la provenance, version de la preuve, réserves, droits déclarés).
> **Ce qu'elle n'atteste pas (forme seule) :** que les observations ont réellement eu lieu ; la justesse des jugements V/U/A/T ; l'étendue réelle d'un claim (tâche utilisateur, technologie d'assistance, périmètre de diffusion) ; l'identité de la personne qui autorise ; la réalité des droits, licences et données ; la qualité perceptuelle. Ces points restent à la trace, à la revue et à l'owner.

### 4.4 Retouches de texte

| # | Où | Quoi |
|---|---|---|
| T-1 | ACTION/STATUS, après la table des issues | **Matrice de compatibilités** : une issue non nulle ⇒ verdict non accepté ; `LOST-IN-BUILD` ⇒ non accepté ; `PARTIALLY-HELD` ⇒ pas `ACCEPTED` ; `transformed` compatible avec tout verdict, requis pour l'acceptation (F-ACT-010, F-RC-001) |
| T-2 | ACTION 277 | Les axes V/U/A/T d'une carte qui accepte sont sérialisés dans `closure.axes`, jamais dans `verdict` (F-ACT-012) |
| T-3 | ACTION 283–289 | Basis typée et `provenance.capability` (F-ACT-018) |
| T-4 | ACTION 407–411 | `artifact.version` et l'égalité avec la version de preuve ; le cas du déplacement garde la même version (F-ACT-022) |
| T-5 | ACTION 413–427 | Correspondance vers `closure.reservations[]` (F-ACT-023) |
| T-6 | ACTION 429–435 | `rights_status` ; « en cas de doute, pas d'ACCEPTED » (F-ACT-024) |
| T-7 | ACTION 305–315 (snapshot) | Trois lignes : ID du run, version de la source et de l'artefact, instant de génération. La snapshot devient datable ; aucune machine (F-ACT-019) |
| T-8 | README, ACTION, `machine_projection.md` | Promesse du validateur (§4.3) |

## 5. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | Après A1 et A2 ; chaque invariant nouveau arrive avec son cas unitaire et son motif |
| C2 | **Une seule migration de schéma** pour B1 et B2 (et le champ de risque transféré de C2, s'il est retenu) |
| C3 | **Proportion** : aucun champ nouveau n'est exigé d'une carte non acceptante, sauf `rights_status` en DIRECTION (témoin B2-P2) |
| C4 | **Consommateurs à mettre à jour** : l'exemple canonique (dont la `basis` déclarative), `valid_direction_with_profile_decision` (acceptée avec réserve), les fixtures acceptantes utilisées comme bases de cas unitaires, `machine_projection.md` (YAML et règles). Aucun fichier ajouté |
| C5 | Aucune nouvelle valeur de mode, d'état, d'issue ou de verdict ; les statuts d'axe restent les cinq d'ACTION |
| C6 | Relecture complète d'ACTION 116–180, 265–320 et 405–435 après patch (fort rayon d'impact, §22) |

## 6. Condition de sortie (phase 13)

1. `B2_harnais_non_regression.py` : **1/1 et 19/19** (16 négatifs rejetés pour leur motif, 3 positifs acceptés, dont la fixture de retour simple sans champ nouveau).
2. Harnais A1, A2 et B1 inchangés et verts.
3. `validate_all` : `FULL VALIDATION PASSED`.
4. **Rejeux :**
   - 4.04 : RETURNED + ACCEPTED ;
   - 7.02 B4 : RECLASSIFIED + ACCEPTED ;
   - 9.02 20-N : ESCALATED + ACCEPTED ;
   - 4.08 et 9.02 17-N1 : version périmée ;
   - 4.07 : capture statique présentée comme test de tâche. Ce dernier reste « forme seule » **si** la capacité est disponible et attestée. C'est la limite déclarée, non un échec.

   Tous les autres sont refusés en machine.
5. La liste close publiée compte 43 invariants actifs, chacun relié à sa source humaine.

## 7. Sortie

- **PATCH-DECISION B2 : CORRIGER.** 10 invariants nouveaux, 1 retrait, 2 règles absorbées par des règles plus générales ; un objet de réserve unique ; une matrice écrite d'abord dans le texte.
- **D-ACT-1 = c est désormais concrète** : une liste close de 43 invariants actifs et une promesse du validateur qui dit ce qu'il n'atteste pas.
- Les 9 Majeur du lot B1 + B2 ont chacun un invariant testable.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- le principe « qui accepte prouve » **limite la charge** aux cartes qui acceptent, et la fixture de retour simple le démontre ;
- un seul ajout de règle (la matrice), écrit dans le texte avant la machine ;
- trois simplifications (un retrait, deux absorptions) ;
- l'exemple officiel est révélé comme enseignant le défaut qu'il devait prévenir ;
- la liste close rend fermée ce qui, jusqu'ici, était une accumulation de contrôles.

**Prochaine unité : 11.05 PATCH-DECISION B3** (paquets de clôture par mode et B1b : F-ACT-021, F-ACT-015, F-ACT-036, F-ACT-031, F-BIB-001). Chaque invariant de mode devra justifier son entrée dans la liste close, ou être déclaré « forme seule ».
