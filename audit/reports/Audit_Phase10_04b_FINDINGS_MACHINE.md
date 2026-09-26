# DG-AUDIT-001 — Phase 10.04b — FINDINGS : MACHINE (38 fiches)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne » après 10.04a.

**Sortie :** `DG_AUDIT_001_Phase10_04b_FINDINGS_MACHINE.csv`, soit 38 fiches avec les 15 champs du §20. Elles couvrent :
- validateurs : `validate_run_card` (F-VRC 8, F-RC 1, F-FIX 3), `validate_contracts` (F-VCT 3), `validate_design_governance` (F-VDG 4), `validate_reading_map` (F-VRM 3), `validate_all` (F-ALL 2) ;
- contrats de production et de cadrage : F-DF 2, F-RB 2, F-PC 2 ;
- lecteur de routes : F-RRT 1 ;
- manifeste, build et CI : F-MAN 2, F-BLD 4, F-WF 1.

**Ce que ce rapport n'est pas :** ni une décision de correction, ni un patch, ni un verdict global.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan | Plan maître, état 10.04a |
| Empreintes | B01 et protocole inchangés (aucune écriture dans B01 depuis la vérification de 10.03) |
| Checkpoints | Validate_RUN_CARD (passages C–D), Fixtures, RUN_CARD, relus pour les dispositions |
| Sources de niveau 5 | 37 sections de définition, plus F-FIX-003 (définie dans le checkpoint Fixtures), relues en entier |
| Dispositions ultérieures | 3.01, 4.01–4.09, 5.01–5.04, 6.01–6.02, 7.01–7.02, 9.06–9.07 |
| Vérifications ajoutées ici | (1) Aucune ligne des propriétaires B01 ne déclenche F-RRT-001. (2) La forme `state:` minuscule n'apparaît qu'une fois dans les sources, dans un YAML de projection (F-VDG-003). (3) La dépréciation de Node 20 sur les runners GitHub est confirmée (F-WF-001) ; la date exacte du retrait citée en phase 2 n'a pas été revérifiée |

## 2. Règle de gravité pour la machine

La machine (schémas, validateurs, build) n'est pas une source normative. Elle projette et emballe. Sa gravité se mesure donc à la **confiance qu'elle fait porter à tort** :

| Gravité | Règle |
|---|---|
| **Majeur** | Faux PASS du gate **entier** : le feu vert ne dépend plus du contenu |
| **Significatif** | Fausse acceptation ou fausse couverture d'une **règle précise** ; divergence silencieuse entre release et manifeste ; oracle de test qui ne peut pas prouver ce qu'il prétend |
| **Mineur** | Échec **visible** (crash, code non nul, faux rejet), incohérence étroite, ou défaut latent sans occurrence dans B01 |
| **Observation** | Le périmètre même du défaut est incertain |

C'est la même logique que F-DIR-045 et F-ACT-034 : une erreur visible coûte moins qu'une acceptation silencieuse.

## 3. Résultat

| Gravité | Nombre | IDs |
|---|---:|---|
| Bloquant | 0 | — |
| **Majeur** | **2** | **F-VRC-007**, **F-VCT-001** |
| **Significatif** | **15** | VRC-006, VRC-008, RC-001, FIX-002, FIX-003, ALL-001, DF-001, RB-001, PC-001, PC-002, VDG-001, VRM-001, VRM-003, BLD-001, BLD-004 |
| **Mineur** | **20** | VRC-001 à 005, FIX-001, ALL-002, VCT-002, VCT-003, DF-002, RB-002, VDG-002, VDG-004, VRM-002, RRT-001, MAN-001, MAN-002, BLD-002, BLD-003, WF-001 |
| **Observation** | **1** | VDG-003 |

**Décisions :**
- 17 fiches `RETENU → phase 11` ;
- 20 fiches `RETENU (mineur) → lot technique` (un seul cycle d'outillage, l'équivalent du lot éditorial) ;
- 1 fiche `OBSERVATION`.

**Les deux Majeur.** `validate_run_card` et `validate_contracts` rendent **PASS sans rien valider** dès que leur schéma est vide (`{}`) :
- 4.04 : RUN_CARD « PASSED deux fois sans lire la cible » ;
- 4.05 à 4.07 : reproduit sur les trois contrats, jusqu'au niveau `validate_all`.

Cela n'arrive pas dans B01 intact. Mais c'est le flot de contrôle de B01 qui le produit, et il suffit d'une édition ratée du schéma. Ce n'est pas Bloquant, parce que la précondition (un schéma vidé) est visible dans un diff et absente de la baseline.

## 4. Écarts avec la phase 2

18 fiches n'avaient pas de gravité en phase 2 (« gravité finale ouverte »). Leur classement ici est un premier classement.

**Six fiches sont abaissées :**

| ID | Phase 2 → 10.04b | Raison |
|---|---|---|
| F-VRC-001 | Significatif → **Mineur** | Aucun consommateur du package ne lit le JSON autrement : le désaccord de parseur, qui ferait le risque, n'est pas démontré |
| F-VRC-003 | Significatif → **Mineur** | Rejets incontrôlés, jamais des acceptations : l'échec est visible |
| F-VRC-004 | Significatif → **Mineur** | Le mode strict ne prouve pas l'identité d'un artefact de toute façon (4.04, 4.08) : l'incohérence entre hôtes de démo est étroite |
| F-VRC-005 | Significatif → **Mineur** | Faux rejet visible ; le contournement par chemin absolu fonctionne |
| F-DF-002 | Significatif → **Mineur** | Cadrage amont sans verdict d'acceptation : la preuve reste chez ACTION |
| F-RB-002 | Significatif → **Mineur** | Atténuation forte déjà notée en phase 2 : le brief peut être omis et le N/A justifié dans ACTION |

**Aucune n'est relevée.** F-VRC-008 est fixée au haut de sa fourchette de phase 2 (« mineure à significative ») : 4.04 a montré qu'avec un schéma incomplet, la carte invalide est **acceptée** en validation ciblée.

**Signal cumulé** (10.01 à 10.04b) : 35 abaissements, 1 relèvement.

## 5. Arbitrages annoncés

**F-ACT-010 face à F-RC-001 : non fusionnés, même chantier.** Ce sont deux erreurs **opposées** sur la même matrice issue / verdict / statut :
- F-ACT-010 est trop permissive : RETURNED + ACCEPTED passe ;
- F-RC-001 est trop stricte : pour clore un retour dû à une autre preuve manquante, il faut dégrader le statut vrai de l'ancre.

Une seule correction, la matrice de compatibilité de F-ACT-010, doit retirer l'interdiction de F-RC-001 et la remplacer. Les deux tests restent distincts. 9.06 montre aussi l'autre face : T3 accepte `transformed` sur simple déclaration.

**F-ACT-008 face aux F-FIX : pas de lien direct.** F-ACT-008 porte sur `validate_contracts` (fichier utilisateur refusé hors des exemples canoniques). Les F-FIX portent sur les fixtures de `validate_run_card`. F-ACT-008 rejoint donc le **même cycle de correction que F-VCT-001 à 003** (même script).

**Test de cohérence de D-FAC-1 (option c) : F-VRM-003, pas F-VDG.** Le contrôle de frontière d'autorité vit dans `validate_reading_map`, et il est aujourd'hui lexical. **Preuve d'objet** : les contradictions réelles de B01 relevées en 10.04a (F-RM-001, F-RM-002, F-OM-001) passent ce validateur. Si l'owner retient l'option c, F-VRM-003 est le lieu du correctif.

## 6. Constat transversal : réparer l'instrument avant de mesurer

Les phases 12 et 13 (application des correctifs, puis validation de non-régression) s'appuieront sur ces validateurs et ces fixtures. Or la phase 10 montre qu'ils ne peuvent pas encore prouver ce qu'ils annoncent :

| Faiblesse | Fiches | Conséquence pour les phases 12–13 |
|---|---|---|
| Schéma vide ou incomplet → PASS | VRC-007, VCT-001, VRC-008 | Un correctif qui casse le schéma passerait vert |
| Oracles sans motif | FIX-003, ALL-001, FIX-001 | Un négatif peut rester vert pour une raison étrangère |
| Négatifs composites | FIX-002 | Impossible de montrer qu'un correctif isolé agit |
| Autorité d'un enum non testée | VRC-006, VCT-003 | Une régression du mode passerait inaperçue |
| Carte sans contrôle d'identité | VRM-001 | Toute correction de locators (F-RM-003, F-DIR-028, B02 lot 1) serait validée sans être protégée |

**Recommandation d'ordre (non décidée) :** traiter les grappes « Autorité du schéma » et « Oracles » **en premier** dans la phase 11, avant tout correctif normatif, quelle que soit l'option retenue pour D-ACT-1. Même l'option b (« la validation n'atteste que la forme ») exige que la forme soit réellement vérifiée.

**Conséquence pour B02.** Le PASS de B02 lot 1 (hypothèse gelée) a été obtenu avec ces mêmes validateurs. Il hérite de leurs limites, en particulier F-VRM-001 pour les 70 locators ajoutés. B02 reste gelée ; cette limite s'ajoute à celles que R01 avait notées.

## 7. Grappes pour la phase 11

| Priorité | Grappe | Fiches | Type (§21) |
|---|---|---|---|
| **1** | Autorité du schéma | **VRC-007**, **VCT-001**, VRC-008, VRC-006 ; VCT-003 (m) | Correction d'outil : une prévalidation commune + voisins négatifs |
| **1** | Oracles de test | FIX-002, FIX-003, ALL-001 ; FIX-001 (m) | Correction de test : prérequis des phases 12–13 |
| 1 (lié) | Matrice issue / verdict / ancre | RC-001 | Dans le chantier F-ACT-010 |
| 2 | Carte et routes | VRM-001 (**prérequis** de F-RM-003), VRM-003 (D-FAC-1 c) ; VRM-002 (m), RRT-001 (m) | Correction d'outil |
| 2 | Intégrité de release | VDG-001, BLD-001, BLD-004 ; BLD-002, BLD-003, MAN-001, MAN-002, WF-001 (m) | Correction d'outil : comparaison ZIP ↔ manifeste comme garde unique |
| 2 | Contrats de production et de cadrage | DF-001, RB-001, PC-001, PC-002 ; DF-002, RB-002 (m) ; + F-ACT-008 | Alignement selon D-ACT-1 et F-ACT-029 (activation) |
| 3 | Lot technique de robustesse | VRC-001 à 005, VCT-002, VDG-002, VDG-004, ALL-002 | Diagnostics contrôlés, un seul cycle |
| — | Observation | VDG-003 | — |

**F-PC-001 (quota de deux directions)** mérite une mention à part. C'est la seule fiche machine qui touche la **création** : elle contredit la protection « pas de quota de variantes », et sa friction a traversé toute la campagne (4.07, 6.01, 6.02b, 7.01, 7.02, 9.06). Elle rejoint la grappe Proportion.

## 8. Sortie

- **38/38 fiches classées.**
- **Registre complet : 158/158 classées** (157 + F-RM-003, sous réserve de confirmation).
- Aucun nouvel ID ; trois arbitrages rendus ; un ordre de correction recommandé (instrument avant correctifs).
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- une règle de gravité propre à la machine ;
- deux Majeur isolés sur une seule cause (la prévalidation du schéma) ;
- l'ordre « réparer l'instrument avant de mesurer » rendu explicite pour les phases 12–13 ;
- F-RC-001 rattachée au chantier F-ACT-010 sans fusion ;
- le lieu du test de D-FAC-1 identifié ;
- deux vérifications factuelles qui ont réduit des incertitudes (RRT-001 latent, VDG-003 hors contrat).

**Prochaine unité : 10.05 consolidation.**
- Registre unique des 158 fiches.
- Table unique des 35 abaissements et du relèvement, à arbitrer en bloc par l'owner.
- Confirmation de F-RM-003.
- Liste des décisions préalables (D-ACT-1, D-FAC-1) et ordre des grappes pour la phase 11.
- Un contrôle de cohérence entre les cinq CSV (IDs, champs, décisions).
