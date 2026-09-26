# DG-AUDIT-001 — Phase 10.05 — CONSOLIDATION : registre unique, écarts, grappes et décisions de l'owner

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne » après 10.04b.

**Sorties :**
- `DG_AUDIT_001_Phase10_05_REGISTRE_CONSOLIDE_158.csv` : les 158 fiches, avec leurs 15 champs du §20, la gravité provisoire de phase 2 et deux colonnes nouvelles, `ÉCART / PHASE 2` et `GRAPPE PHASE 11`. Le fichier est trié par grappe, puis par gravité.
- Ce rapport.
- Une archive de transfert pour reprendre le travail ailleurs.

**Ce que ce rapport n'est pas :** ni une décision de correction (phase 11), ni un patch, ni un verdict global.

---

## 1. Contrôle de cohérence des cinq registres

Le contrôle a été exécuté par script sur les cinq CSV (10.01 à 10.04b) :

| Contrôle | Résultat |
|---|---|
| En-têtes identiques (16 colonnes) | Oui |
| Nombre de fiches | 158 (157 du pré-tri + F-RM-003) |
| Doublons d'ID | Aucun |
| Fiche du pré-tri absente | Aucune |
| Champ vide | Aucun |
| Référence à un ID inexistant (dans tous les champs) | Aucune |
| Décision incohérente avec la gravité | Une seule, **légitime** : F-DIR-019, Significatif, `RATTACHÉ à F-DIR-011` (cause commune, test conservé) |
| Chaque fiche dans une seule grappe | Oui (contrôle par assertion) |
| Aucune fiche Majeur ou Significatif dans un lot mineur ou en observation | Oui |

## 2. Résultat global

| Gravité | Nombre |
|---|---:|
| Bloquant | 0 |
| **Majeur** | **14** |
| Significatif | 87 |
| Mineur | 48 |
| Observation | 9 |
| **Total** | **158** |

**Les 14 Majeur :**
- DIRECTION (2) : F-DIR-007 (correctif local critique), F-DIR-027 (ancres) ;
- ACTION (10) : F-ACT-010, 012, 015, 017, 018, 021, 022, 023, 024, 038 ;
- machine (2) : F-VRC-007, F-VCT-001 (schéma vide → PASS).

**Constat principal.** Douze des quatorze ont la **même forme** : la prose protège, mais la projection machine accepte ce que la prose interdit, ou ne valide rien du tout. C'est pourquoi deux décisions d'architecture (D-ACT-1 et D-FAC-1) précèdent tout correctif, et pourquoi l'instrument de validation passe en premier.

## 3. Écarts avec la phase 2 : chiffres corrigés

**Rectification.** Les rapports 10.01 à 10.04b annonçaient un cumul de « 35 abaissements, 1 relèvement ». Le recalcul par script, fiche par fiche, donne **33 abaissements et 3 relèvements**.

L'erreur vient de 10.01 : F-DIR-040 et F-DIR-043 sont passées d'Observation à Mineur. C'est un **relèvement**, que j'avais compté comme un ajustement parmi les « 13 abaissées », tout en écrivant « aucune fiche n'est relevée ». Les rapports antérieurs ne sont pas réécrits ; ce registre fait foi.

| Écart | Nombre |
|---|---:|
| Maintenue | 94 |
| **Abaissée** | **33** |
| **Relevée** | **3** (F-DIR-040, F-DIR-043, F-QS-001 : Observation → Mineur) |
| Premier classement (pas de gravité en phase 2) | 27 |
| Nouvelle fiche | 1 (F-RM-003) |

### Ce que les 33 abaissements changent réellement

Un abaissement vers Mineur **ne retire pas la correction** : la fiche reste retenue, elle passe seulement dans un lot groupé (éditorial ou technique). Les 33 abaissements ont donc trois portées très différentes :

| Portée | Nombre | Fiches | Effet réel |
|---|---:|---|---|
| **Majeur → Significatif** | **4** | F-ACT-009, F-ACT-026, F-ACT-033, F-ACT-036 | Sortent du niveau le plus élevé ; restent traitées en phase 11 (grappes B3, C1, D3) |
| **→ Observation** | **4** | F-DIR-022, F-DIR-044, F-ACT-035, F-SAV-008 | **Plus d'obligation de patch** ; un test futur est nommé |
| Significatif → Mineur | 25 | Les autres | Restent corrigées, dans un lot groupé plutôt qu'une grappe |

**Pour l'owner, 8 abaissements méritent un vrai arbitrage** (les deux premières lignes). Les 25 autres changent l'emballage de la correction, pas son existence.

**Pourquoi l'asymétrie (33 contre 3) :**
- **mécanique** : la phase 2 a inscrit presque tout « Significatif à éprouver » par défaut ;
- **preuves limitées** : un relèvement exige une preuve de dommage, et la campagne n'a que peu de preuves d'objet (N = 1, web seulement, un observateur) ;
- **biais possible** : l'auditeur seul peut pencher vers l'indulgence.

Les trois relèvements s'appuient tous sur une confirmation textuelle ou mesurée. Un quatrième candidat est nommé avec sa condition : F-SAV-002 passerait Majeur si la convergence « neutres + accent » était confirmée N ≥ 3 fois par un observateur indépendant.

## 4. Rectifications cumulées de la phase 10

1. **F-DIR-044** : attribution erronée de la mesure « START = 80 % de la route LITE » (corrigée en 10.01 ; la mesure est devenue F-RM-003 en 10.04a).
2. **9.07 O8 → F-BIB-003** : rattachement trop large (corrigé en 10.03).
3. **Cumul des écarts** : 35/1 annoncé, 33/3 réel (corrigé ici).

Les trois erreurs ont un point commun : un **résumé** a été pris pour la source (9.08 pour F-DIR-044, 9.07 pour F-BIB-003, mes propres tableaux pour les écarts). C'est exactement le risque que l'architecture anti-perte de contexte veut prévenir, et le recalcul par script sur le CSV l'a corrigé. **Règle ajoutée pour la suite : tout total cité dans un rapport est calculé sur le registre, jamais recopié d'un rapport précédent.**

## 5. Grappes pour la phase 11 (ordre proposé, non décidé)

Le registre regroupe les 158 fiches en 20 grappes et 2 lots, plus les observations :

| Ordre | Grappe | Fiches | dont Majeur |
|---|---|---:|---:|
| **0** | **Décisions préalables** : D-ACT-1, D-FAC-1, confirmation de F-RM-003 | — | — |
| **1** | A1 Instrument : autorité du schéma | 4 | 2 |
| **1** | A2 Instrument : oracles de test | 3 | 0 |
| **2** | B1 Protection critique et exception | 6 | 3 |
| **2** | B2 Invariants d'acceptation (dépend de D-ACT-1) | 8 | 6 |
| **2** | B3 Paquets de clôture par mode et B1b | 5 | 2 |
| **2** | B4 Ancres | 2 | 1 |
| **2** | B5 Composant partagé / SYSTÈME | 2 | 0 |
| 3 | C1 Registres, temps et sémantique de preuve | 14 | 0 |
| 3 | C2 Formes et projections | 14 | 0 |
| 3 | C3 Proportion | 3 | 0 |
| 3 | C4 Accès, locators et chargement (F-VRM-001 d'abord) | 5 | 0 |
| 3 | C5 Façades lues seules (dépend de D-FAC-1) | 10 | 0 |
| 3 | C6 Exemples de référence | 3 | 0 |
| 3 | C7 Homogénéisation et ablation | 3 | 0 |
| 3 | C8 Intégrité de release | 3 | 0 |
| 3 | C9 Contrats de production et de cadrage | 4 | 0 |
| 4 | D1 Frontière du jugement de craft | 3 | 0 |
| 4 | D2 Boucle et one-shot | 3 | 0 |
| 4 | D3 Autorité, droits et gates spécialisés | 4 | 0 |
| 4 | D4 Cycle de vie et claims d'efficacité | 3 | 0 |
| 5 | E1 Lot éditorial | 27 | — |
| 5 | E2 Lot technique | 20 | — |
| — | F Observations (test futur) | 9 | — |

**Pourquoi l'instrument passe avant les Majeur normatifs.** Les phases 12 et 13 valideront les correctifs avec ces validateurs et ces fixtures. Tant qu'un schéma vide donne PASS et que les négatifs composites ne permettent pas d'isoler un effet, **aucun correctif ne peut être prouvé**. A1 et A2 ne demandent aucune décision d'architecture : elles peuvent ouvrir la phase 11 pendant que D-ACT-1 et D-FAC-1 sont tranchées.

**Ordres internes à respecter :**
- F-ACT-014 avant F-DIR-011 (C1) ;
- F-VRM-001 avant F-RM-003, F-DIR-028 et F-ACT-001 (C4) ;
- F-RC-001 dans le chantier de matrice de F-ACT-010 (B2).

## 6. Anti-bureaucratisation (§32) : le volume de la phase 11

La phase 11 porte sur 102 fiches réparties en 20 grappes, plus 47 fiches mineures en deux lots. Une `PATCH-DECISION` fiche par fiche produirait plus de cent arbitrages : c'est exactement la dérive que le §32 veut éviter. Proposition :
- **une `PATCH-DECISION` par grappe** (20), et une par lot (2) ;
- chaque décision cite ses fiches, son type de correction (§21), sa condition de sortie et son test de non-régression ;
- une fiche ne reçoit une décision propre que si elle diverge de sa grappe.

**Effet attendu de D-ACT-1 et D-FAC-1 sur ce volume :**
- l'option b de D-ACT-1 (« la validation atteste la forme ») transformerait une partie de B2, B3, C2 et C9 en clarifications de promesse plutôt qu'en invariants machine ;
- l'option c de D-FAC-1 concentrerait C5 sur un test unique (dans F-VRM-003) plus des marquages courts.

## 7. Décisions attendues de l'owner

| # | Décision | Options | Recommandation de l'auditeur |
|---|---|---|---|
| 1 | Confirmer F-RM-003 (granularité des locators) | Confirmer / refuser (elle redeviendrait une observation sans ID) | Confirmer : la mesure est déterministe et c'est le coût principal mesuré sur les routes courtes |
| 2 | Arbitrer les 8 abaissements à portée réelle | Accepter / rétablir les 4 Majeur / rétablir les 8 | Accepter, avec une réserve sur F-ACT-033 (reduced motion) si l'owner juge l'accessibilité non négociable |
| 3 | **D-ACT-1** : autorité d'une RUN_CARD validée | a. relever la machine / b. réduire la claim à la forme / c. mixte (invariants déterministes et à fort risque seulement) | **c**, car elle couvre les 6 Majeur de B2 avec une liste close, sans formulaire universel |
| 4 | **D-FAC-1** : statut d'une façade lue seule | a. autosuffisante / b. simples renvois / c. résumés courts marqués + test de cohérence au build | **c**, parce qu'elle garde la vitesse d'entrée et que le test a déjà sa place (F-VRM-003) |

**Ce sont des recommandations, pas des décisions.** Aucune n'est appliquée avant votre réponse.

## 8. Sortie de la phase 10

- **158/158 fiches classées**, un registre consolidé, cohérence contrôlée par script.
- **Condition de sortie de la phase 10 : satisfaite sous réserve des décisions 1 et 2.** La décision 1 fixe le total (157 ou 158) ; la décision 2 fixe les gravités.
- Aucun patch, aucun verdict global. B01 reste canonique, B02 reste gelée.

**Prochaine unité : 11.00.** Enregistrer les décisions 1 à 4, puis ouvrir la phase 11 par les grappes A1 et A2 (`PATCH-DECISION` par grappe), avant les grappes B.
