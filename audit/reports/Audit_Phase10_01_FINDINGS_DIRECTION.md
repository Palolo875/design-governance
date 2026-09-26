# DG-AUDIT-001 — Phase 10.01 — FINDINGS : DIRECTION (46 fiches)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** phase 10 par propriétaire, en commençant par DIRECTION (message du 25-09).

**Sortie :** le registre `FINDINGS` de DIRECTION, soit 46 fiches avec les 15 champs du §20, dans `DG_AUDIT_001_Phase10_01_FINDINGS_DIRECTION.csv`. Une colonne supplémentaire, `SEVERITY-PROVISOIRE (phase 2)`, garde la traçabilité.

**Ce que ce rapport n'est pas :**
- ce n'est pas une décision de correction : la `PATCH-DECISION` relève de la phase 11 ;
- aucun patch, aucun verdict global.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan | Plan maître, état 9.08 |
| Bloc précédent | 9.08 |
| Checkpoint du propriétaire | `Audit_DIRECTION_Phase2_Checkpoint_Consolidation.md`, relu en entier |
| Empreintes | B01 et protocole conformes |
| Protocole | §20 (gravité, 15 champs), §21 (types de correction), §7.7 et §7.8 (fusion) |
| Sources de niveau 5 (rapports sectionnels) | **Les dix rapports DIRECTION de phase 2.** Les 99 sections `F-DIR-*` (définitions et mises à jour) ont été extraites et relues en entier. |
| Dispositions ultérieures | Recherchées dans les checkpoints ACTION, SAVOIR, BIBLIOTHEQUE, QUICKSTART, « cinq propriétaires » et « final de phase 2 » |
| Preuves d'objet | 6.02b, 9.06, 9.07, 9.08, citées fiche par fiche quand elles changent le jugement |

## 2. Méthode de classement

- **Grille §20 :**
  - **Bloquant** : contradiction, fausse preuve, risque critique ou perte de contrôle ;
  - **Majeur** : peut faire échouer le système ou crée une autorité concurrente ;
  - **Significatif** : défaut régulier de clarté, de frontière ou d'exécution ;
  - **Mineur** : défaut éditorial local, à faible impact structurel ;
  - **Observation** : risque plausible sans preuve suffisante.
- **Règle appliquée.** La gravité suit l'**impact réel**, en tenant compte des facteurs atténuants documentés en phase 2 et des preuves d'objet. « Un constat sans comportement observé ou risque formulable reste une observation » (§20).
- **Décision (dernier champ) :**
  - `RETENU → phase 11` : à arbitrer ;
  - `RETENU (mineur) → lot éditorial` : à regrouper dans un seul cycle de clarification ;
  - `OBSERVATION` : pas d'obligation de patch, un test futur est nommé ;
  - `RATTACHÉ` : cause commune avec une autre fiche ; le test est conservé.

## 3. Résultat

| Gravité | Nombre | IDs |
|---|---:|---|
| Bloquant | 0 | — |
| **Majeur** | **2** | F-DIR-007 (correctif local critique sans classement stable), F-DIR-027 (ancres : contrat humain et machine divergents) |
| **Significatif** | **27** | 001, 002, 003, 006, 008, 009, 010, 011, 013, 016, 018, 019, 020, 021, 023, 024, 028, 029, 030, 032, 034, 035, 036, 039, 041, 042, 046 |
| **Mineur** | **12** | 005, 012, 014, 015, 025, 026, 031, 033, 037, 040, 043, 045 |
| **Observation** | **5** | 004, 017, 022, 038, 044 |

**Décisions :**
- 29 fiches `RETENU → phase 11` ;
- 11 fiches `RETENU (mineur) → lot éditorial` ;
- 1 fiche `RETENU (mineur) → phase 11`, candidate à la suppression (F-DIR-033) ;
- 5 fiches `OBSERVATION` ;
- 1 fiche `RATTACHÉ` (F-DIR-019 → F-DIR-011).

## 4. Écarts avec les gravités provisoires de phase 2 (13 sur 46)

Aucune fiche n'est relevée. Treize sont abaissées, chacune pour une raison nommée :

| ID | Phase 2 → 10.01 | Raison |
|---|---|---|
| F-DIR-012 | Significatif à éprouver → **Mineur** | Écart de cardinalité purement textuel ; aucun effet observé ; correction d'une phrase |
| F-DIR-014 | Significatif → **Mineur** | L'omission d'ITER mène à un sur-classement (plus de protection, pas moins) : coût, pas risque |
| F-DIR-015 | Significatif → **Mineur** | Un mot manquant (« abandonnée ») ; ACTION reste la définition canonique |
| F-DIR-022 | Significatif ouvert → **Observation** | Aucun contournement observé ; les règles globales anti-contournement existent |
| F-DIR-025 | Significatif → **Mineur** | ACTION et SAVOIR reconnaissent déjà l'absence d'asset ; seule une valeur manque dans une table |
| F-DIR-026 | Significatif → **Mineur** | Condition logique locale, qui ne joue que sur la route « générée » |
| F-DIR-031 | Significatif → **Mineur** | START (question 6) et la posture résolvent l'ambiguïté ; dans le run 9.08, la clarification avant classement n'a créé aucun conflit |
| F-DIR-033 | Significatif → **Mineur** | Taxonomie jamais mobilisée dans six unités de runs (§32 : champ sans effet) ; candidate à la suppression |
| F-DIR-037 | Significatif → **Mineur** | La table adjacente (688–695) réintroduit les capacités de construction |
| F-DIR-040 | Observation → **Mineur** | Défaut éditorial confirmé, correction triviale |
| F-DIR-043 | Observation à risque → **Mineur** | Contradiction architecturale confirmée, mais locale et atténuée |
| F-DIR-044 | Significatif → **Observation** | La taxonomie de lecture ne sert qu'aux pilotes, inexistants à ce jour ; à reprendre quand ils seront conçus |
| F-DIR-045 | Significatif → **Mineur** | Le mauvais chemin JSON est **rejeté par le validateur** (`additionalProperties: false`) : erreur visible, pas silencieuse |

**Limite.** Ces abaissements reflètent le jugement d'un seul auditeur. Si l'owner préfère la prudence de phase 2, les 13 fiches repasseraient en « Significatif », sans changer l'ordre des priorités (§6).

## 5. Déduplication

- **F-DIR-019 → F-DIR-011 (rattachement, pas suppression).** Les trois occurrences (START 233, FIRST-OBJECT 322, ATELIER 480) relèvent d'une **seule correction** : reprendre la triade ACTION `N/A-JUSTIFIED` / `NOT-VERIFIED` / `NOT-OBSERVED`. Le test propre à F-DIR-019 reste dans la matrice de F-DIR-011. La réserve des checkpoints ACTION et « cinq propriétaires » (`NOT-OBSERVED` sans place dans la projection) porte sur **F-ACT-014** ; elle sera traitée en 10.02, pas ici.
- **Occurrences conservées avec leur propre ID, rattachées à une cause systémique :**
  - 013, 034 → cause 010 ;
  - 023, 039, 045 → cause 006 ;
  - 042 → cause 030.

  Chacune garde un comportement et un test distincts (décisions D2, D4 et D5 du checkpoint DIRECTION, confirmées).
- **Aucune autre fusion.** D6, D7 et D8 (002/044, 004/038, 021/029) restent distincts : correctifs et tests différents.

## 6. Ce que les preuves d'objet ont changé

Les phases 6.02b et 9.06–9.08 apportent pour la première fois des comportements **observés** :

| Fiche | Observation d'objet |
|---|---|
| **F-DIR-021** | Le run avec DG (9.08) a affiché le jargon interne « TRUTH/MECHANISM » **dans l'interface produit** : c'est exactement le risque « audience du marquage non définie » |
| **F-DIR-029** | Le même label a dû être complété en prose (« taux illustratifs ») pour dire que les données sont fictives |
| **F-DIR-023** | Mon propre run a gardé 6 champs de VISUAL_TARGET sur 10 : omission variable observée |
| **F-DIR-030 / F-DIR-020** | Cinq grilles de jugement mobilisées pour un seul objet (6.02b) |
| **F-DIR-027** | T2 refuse l'absence d'ancre ; T3 et T5 (corrigé) acceptent n'importe quelle ancre déclarée (9.06). Le pilote A, surface identitaire, n'en avait aucune. **Majeur maintenu** : texte et machine forment deux autorités divergentes. |
| **F-DIR-007** | START 140 reclasse bien un changement de consentement (9.08), mais **au texte seulement** ; la machine accepte LITE avec protection critique (4.01, 7.02). **Majeur maintenu.** |
| **F-DIR-002** | Le premier comparatif avec et sans DG (9.08, N = 1) ne montre pas de gain en présence ni en désirabilité : le claim causal reste non démontré |
| **F-DIR-009** | DOUBLE-LOOP a permis l'arrêt pour B et l'a refusé pour A (9.06). La règle générale fonctionne ; seule la ligne 184 du Creative Boot est en cause. |

## 7. Rectification : une attribution erronée de ma part

Dans 10.00, 11–13 et 9.08, j'ai associé à **F-DIR-044** le fait que le bloc START servi par la CLI soit trop large (130 lignes, 80 % de la route LITE). **C'est faux.**
- F-DIR-044 porte sur la **taxonomie des catégories de lecture** (rapport DIRECTION 10).
- Le bloc trop large est une **observation transversale sans ID**, relevée en 5.02 (« le bloc large d'un locator valide est une observation transversale distincte »).

**Conséquences :**
- la mesure de 9.08 (130/163 lignes) **ne renforce pas** F-DIR-044 ;
- elle reste valable comme observation de charge ;
- elle est transmise à **10.04** (façades et machine) comme **candidate à une nouvelle fiche** sur la granularité des locators. Propriétaire pressenti : READING_MAP et `read_route.py`.

Le plan maître note cette rectification. Les rapports antérieurs ne sont pas réécrits : ils restent l'historique.

## 8. Entrée pour la phase 11 (ordre proposé, non décidé)

| Priorité | Grappe | Fiches | Type de correction (§21) | Propriétaire |
|---|---|---|---|---|
| 1 | Protection critique | **007** (+ 016) | Correction normative + alignement humain/machine | DIRECTION/START ; schéma |
| 1 | Ancres | **027** | Alignement humain/machine | DIRECTION ; ACTION ; schéma |
| 2 | Formes et projections | 006, 010, 013, 034, 035, 039, 023, 045 | Simplification : une forme canonique et des projections déclarées | ACTION (canon) ; DIRECTION (vues) |
| 2 | Sémantique de preuve et de vérité | 011 (+019), 021, 024, 029, 032, 033 | Clarification ; déplacement de méthode | DIRECTION ; ACTION ; SAVOIR |
| 3 | Frontière du jugement de craft | 030, 042, 020 | Simplification (une revue) ; routing | SAVOIR ; DIRECTION |
| 3 | Routage et façades | 001, 008, 018, 041, 046, 028 | Façade, routing, normatif | DIRECTION ; READING_MAP |
| 3 | Boucle | 009, 003, 036 | Clarification ; alignement machine | DIRECTION ; ACTION |
| 4 | Lot éditorial (un seul cycle) | 005, 012, 014, 015, 025, 026, 031, 037, 040, 043, 045 | Clarification | DIRECTION |
| — | Observations | 004, 017, 022, 038, 044 | Aucune, test futur nommé | — |

## 9. Sortie

- **DIRECTION : 46/46 fiches classées** avec leurs 15 champs.
- **Registre global : 46/157 classées.** Restent 111 fiches provisoires.
- Aucun nouvel ID ; une candidate transmise à 10.04.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- 13 gravités ajustées, avec raison écrite ;
- une cause commune formalisée (011/019) ;
- première utilisation des preuves d'objet pour classer ;
- une erreur d'attribution de ma part corrigée.

**Prochaine unité : 10.02 ACTION** (39 fiches). Sources : les 12 rapports ACTION de phase 2 et leur checkpoint ; même méthode.
