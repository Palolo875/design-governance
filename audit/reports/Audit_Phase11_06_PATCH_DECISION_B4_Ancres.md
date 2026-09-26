# DG-AUDIT-001 — Phase 11.06 — PATCH-DECISION B4 : ancres

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ». Cadre : **D-ACT-1 = c**, **D-FAC-1 = c**, liste close.

**Grappe B4 :**

| Fiche | Gravité | Objet |
|---|---|---|
| **F-DIR-027** | Majeur | Le contrat machine des ancres diverge du contrat humain |
| F-SAV-003 | Significatif | Une comparaison indépendante prise pour la calibration d'une ancre générée seule |

**Sorties :**
- cette `PATCH-DECISION` ;
- `B4_harnais_non_regression.py` ;
- la liste close mise à jour (6 invariants, 1 modifié) : **53 actifs**.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00–11.05 |
| Empreintes | B01 `016e6002…` conforme |
| Sources propriétaires relues | DIRECTION 176–177 (ANCHOR-BASIS), 381, 439–441 (réserve generated-only), 577–590 (**ABSOLU 2**) ; SAVOIR/SOURCE 475–477 ; ACTION 475–487 (pipeline, trace, conséquence d'une ancre manquante) |
| Machine relue | Schéma `anchors[]` (9 champs, **sans type**) ; validateur INV-E10 (au moins un ancrage, structuré) et INV-E12 (accepté ⇒ `transformed`) ; tests 9.06 T2–T5 |

## 2. Re-vérification sur B01

| Carte (sur l'exemple canonique) | B01 |
|---|---|
| Une seule ancre, générée par IA et non revérifiée, direction `HELD`, verdict accepté avec réserve, **aucune réserve de calibration** | **acceptée** : la règle DIRECTION 441 n'est pas appliquée |
| Ancre datée 2001, puis ancre datée « récemment » | **acceptées** toutes deux |
| Ancre avec un champ `type` | **rejetée** : champ inconnu. Le type exigé par DIRECTION 381 est **impossible à déclarer** |
| **DIRECTION sans ancre, déclarée honnêtement** : issue `EXPLORATORY`, verdict `EXPLORATORY`, `PARTIALLY-HELD` | **rejetée** : « DIRECTION exige au moins un ancrage structuré » |

**Le dernier cas est le plus grave.** ACTION 483 prescrit exactement cette sortie quand l'ancre manque : axes `NOT-VERIFIED` et issue appropriée. La machine l'interdit. Un producteur qui veut persister son run n'a alors que deux choix :
- ne rien persister ;
- **inventer une ancre**.

C'est le risque « faux ancrage pour satisfaire le validateur » que la fiche nommait. C'est aussi la situation réelle du pilote A en 9.06, construit sans ancre.

**Harnais B4 : témoin 1/1, tests B4 0/12.** Tous les tests échouent pour la même raison : les champs proposés n'existent pas, ou l'ancrage reste exigé sans condition.

## 3. Trancher la « branche N/A »

Deux textes divergent :
- **DIRECTION, ABSOLU 2 (577)** : « Avant le premier code ou le premier rendu d'une surface DIRECTION, établis une ancre fraîche et inspectable. » C'est un absolu, et DIRECTION est le **propriétaire** de l'ancrage (SAVOIR 475 et ACTION 475 le disent eux-mêmes).
- **SAVOIR/SOURCE 475** : « si aucune ancre n'est applicable, justifie la non-applicabilité ».

**Décision : pas de N/A pour une surface DIRECTION.** L'absolu du propriétaire prévaut. La phrase de SAVOIR reste valable pour les surfaces non identitaires, où une ancre n'est utile « que si elle peut modifier la décision » (SAVOIR 475, ACTION 481).

**Et quand l'ancre manque quand même ?** On ne la déclare pas « non applicable » : on applique ACTION 483. Les axes concernés passent `NOT-VERIFIED`, l'issue suit, et **aucune acceptation** n'est possible. La machine doit permettre de **sérialiser cet échec honnêtement** au lieu d'exiger une ancre (INV-B4-6).

**Et la comparaison indépendante (F-SAV-003) ?**
- **DIRECTION 441 et 587**, propriétaires, admettent trois calibrations d'une ancre générée seule à fort enjeu : une référence observée, une ancre fournie ou une contrainte réelle. À défaut, une réserve explicite.
- **SAVOIR 477** ajoute « une comparaison indépendante ». C'est la seule source qui l'ajoute, et elle n'est pas propriétaire.

**Décision :** une revue indépendante reste un **contrepoint** (ACTION B3), **pas une calibration**. SAVOIR 477 est aligné sur DIRECTION, et la machine n'admet pas « revue indépendante » comme base de calibration.

## 4. Les sept questions du §21

| Question | Réponse |
|---|---|
| Change une décision, une preuve ? | **Oui.** Protection identitaire non contrôlée d'un côté ; de l'autre, la machine pousse à falsifier (§2) |
| Défaut réel ? | **Oui**, re-vérifié. Les deux divergences de texte sont localisées (SAVOIR 475 et 477) |
| Gain > charge ? | **Oui.** Pour une carte DIRECTION : un type par ancre, une date ISO, un champ d'enjeu, et une calibration **seulement** dans le cas « fort enjeu + ancres toutes générées + direction tenue ». Rien pour les autres modes |
| Nouvelle autorité ? | **Non.** Types, réserve et calibrations reprennent DIRECTION 381, 441 et 583–587 mot pour mot. `identity_stake` rend **explicite** la condition « enjeu identitaire élevé » qu'utilise déjà DIRECTION 441 ; sans ce champ, la règle ne peut pas s'appliquer sans deviner |
| Testable ? | Oui : 8 négatifs avec motif, 4 positifs |
| Positif / défensif équilibré ? | **Oui, et c'est un gain positif net.** L'échec honnête devient sérialisable (B4-P3). Un enjeu normal n'exige aucune calibration (B4-P4). Une ancre générée avec réserve peut être tenue (B4-P2) : DIRECTION 441 dit que la réserve « ne déclare ni l'image fausse, ni la direction invalide » |
| Suppression ou fusion ? | **Suppression** : l'exigence inconditionnelle « au moins un ancrage » est retirée d'INV-E10 et remplacée par une règle conditionnelle. **Suppression** : « comparaison indépendante » disparaît de SAVOIR 477 |

## 5. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **alignement humain/machine** : 6 invariants, 1 invariant modifié, 3 champs ;
- **correction normative** : SAVOIR 475 et 477 alignés sur le propriétaire ;
- **clarification** : correspondance dans ACTION.

**Propriétaires :**
- DIRECTION pour les voies d'ancrage et la réserve (aucune modification de fond ; il porte déjà la bonne règle) ;
- SAVOIR/SOURCE pour ses deux phrases ;
- ACTION pour la trace et la projection.

### 5.1 Invariants B4 (liste close)

| ID | Invariant | Fiches |
|---|---|---|
| **INV-B4-1** | `anchors[].type ∈ {generated, observed, provided}` requis | F-DIR-027 |
| **INV-B4-2** | `anchors[].date` est une date ISO. Le **caractère frais** reste un jugement : forme seule, pas de seuil numérique inventé | F-DIR-027 |
| **INV-B4-3** | DIRECTION ⇒ `direction.identity_stake ∈ {high, normal}` | F-DIR-027 |
| **INV-B4-4** | Enjeu `high` ∧ ancres toutes `generated` ∧ direction tenue ⇒ `direction.calibration`, dont la base est une contrainte réelle ou la réserve generated-only, avec son détail. Les bases admises ne comprennent **pas** la revue indépendante | F-DIR-027, F-SAV-003 |
| **INV-B4-5** | Calibration « générée seule, réservée » ⇒ verdict ≠ `ACCEPTED` (la réserve reste possible, via l'objet de B2) | F-DIR-027 |
| **INV-B4-6** | DIRECTION sans ancrage ⇒ aucun verdict accepté **et** une issue non nulle | F-DIR-027 |
| (modifié) | INV-E10 garde la structure des ancrages ; son exigence « au moins un » est remplacée par INV-B4-6. INV-E12 (accepté ⇒ `transformed`) est conservé | — |

**Liste close : 56 lignes, 53 invariants actifs.**

**Forme seule (ajout à la promesse du validateur) :**
- qu'une ancre `observed` a réellement été ouverte ;
- qu'elle est fraîche ;
- que la transformation déclarée a eu lieu (la limite montrée par 9.06 T3 demeure) ;
- que l'enjeu déclaré `normal` n'est pas en réalité élevé.

**Ce que la machine gagne quand même :** elle sait maintenant quand une ancre est **générée**, et elle applique la seule règle identitaire vérifiable, DIRECTION 441.

### 5.2 Retouches de texte

| # | Où | Quoi |
|---|---|---|
| T-1 | SAVOIR/SOURCE 475 | « Pour une surface identitaire, l'ancre est requise (DIRECTION, ABSOLU 2) ; si elle manque, les axes restent NOT-VERIFIED et le run suit ACTION 483. Hors surface identitaire, justifie la non-applicabilité. » (marquage D-FAC-1 = c, « voir DIRECTION ») |
| T-2 | SAVOIR/SOURCE 477 | Retirer « d'une comparaison indépendante » ; ajouter : « une revue indépendante est un contrepoint (ACTION B3), pas une calibration » (F-SAV-003) |
| T-3 | ACTION 475–487 | Correspondance : type, date, `identity_stake`, `calibration` ; une ancre manquante se sérialise par l'issue, jamais par une ancre inventée |
| T-4 | DIRECTION 441 | Une phrase de correspondance vers `direction.calibration` (le fond est inchangé) |
| T-5 | Promesse du validateur | Ajout des points « forme seule » ci-dessus |

## 6. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | Dans la même migration de schéma que B1 à B3 ; chaque invariant avec son cas unitaire et son motif (règle A2) |
| C2 | Proportion : aucune exigence nouvelle hors DIRECTION ; la calibration n'est exigée que dans le cas étroit d'INV-B4-4 |
| C3 | **Consommateurs** : l'exemple canonique (type, date ISO, `identity_stake`), les fixtures DIRECTION, `machine_projection.md`. Aucun fichier ajouté |
| C4 | **Compatibilité F-RC-001 (B2)** : une ancre `transformed` reste valide sous un retour |
| C5 | Relecture complète de DIRECTION 373–445 et 577–590, de SAVOIR 471–529 et d'ACTION 470–490 après patch |

## 7. Condition de sortie (phase 13)

1. `B4_harnais_non_regression.py` : **1/1 et 12/12**.
2. Harnais A1, A2, B1, B2 et B3 verts.
3. `validate_all` : `FULL VALIDATION PASSED`.
4. **Rejeux 9.06 :**
   - T2 (DIRECTION acceptée sans ancre) : toujours refusé, désormais pour le motif d'INV-B4-6 ;
   - pilote A (sans ancre) : sérialisable en `EXPLORATORY`, sans ancre inventée ;
   - T3 (`transformed` déclaratif) : limite déclarée.
5. SAVOIR 475 et 477 ne contredisent plus DIRECTION (relecture croisée).

## 8. Sortie

- **PATCH-DECISION B4 : CORRIGER** : 6 invariants, 1 modifié ; deux phrases de SAVOIR alignées sur le propriétaire ; 3 champs.
- **F-DIR-027** : la divergence est tranchée (pas de N/A en DIRECTION ; l'échec se sérialise honnêtement), et la réserve identitaire devient vérifiable.
- **F-SAV-003** : la revue indépendante est remise à sa place de contrepoint.
- **Grappes B1 à B4 décidées** : les **12 Majeur** normatifs sur lesquels la machine a prise (DIRECTION et ACTION) sont couverts. Il reste B5 (composant partagé, sans Majeur).
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- la correction **retire** une exigence (ancre inconditionnelle) qui poussait à falsifier ;
- une divergence de propriétaire est tranchée en faveur du propriétaire, par suppression de mots dans le texte dérivé ;
- aucun seuil de fraîcheur inventé ;
- la seule règle identitaire vérifiable (DIRECTION 441) devient enfin applicable, grâce à un champ qui rend explicite une condition déjà écrite.

**Prochaine unité : 11.07 PATCH-DECISION B5** (composant partagé / SYSTÈME : F-BIB-004 contrat de composant absent de COMPONENTS, F-SAV-007 « Reclassifie » dans SAVOIR/SYSTEM 694).
