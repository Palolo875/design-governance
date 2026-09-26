# DG-AUDIT-001 — Phase 11.20 — PATCH-DECISION D4 : cycle de vie et claims d'efficacité

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ». **Dernière grappe du lot D.**

**Grappe D4 : 3 fiches, toutes Significatif.** Toutes portent sur un **statut accordé sans preuve** : le statut d'une route, le statut de l'efficacité du système, le propriétaire d'une promotion.

| Fiche | Objet |
|---|---|
| F-CHG-001 | CHANGELOG : les routes du seed sont « canoniques » sans statut individuel. `DEPRECATED` n'est atteignable que depuis `ADOPTED`, qui suppose un gain mesuré. `PILOT` ne mène qu'à `ADOPTED` ou `ABANDONED` |
| F-DIR-002 | DIRECTION 74 : le système « augmente la probabilité d'un travail de niveau expert », alors que README, RELEASE_NOTES et CHANGELOG 21 classent l'efficacité `NOT-VERIFIED` |
| F-DIR-046 | DIRECTION 817 : toute route partagée ou candidate est envoyée vers `BIBLIOTHEQUE/EVOLUTION`, même si elle n'est pas structurelle |

**Sorties :**
- cette `PATCH-DECISION` ;
- `D4_harnais_non_regression.py` ;
- 2 entrées LCF (la liste passe à 21).

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | B3 (paquet SYSTÈME : migration, rollback, consumers) ; C3 (contrat réduit et `PILOT`) ; C5 (LCF) ; D3 (critères d'observateur, clôtures `FULL` interdites sans observation directe) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 |
| Sources relues | CHANGELOG 1–63 (en entier) ; DIRECTION 72–78, 815–819 ; BIBLIOTHEQUE 22–35 (entrée prioritaire), 56–63, 733–770 (EVOLUTION, contrat de gain réel) ; README racine 16 ; RELEASE_NOTES 56 ; `validate_design_governance.py` 148–160 (`check_lifecycle_contract`) |

## 2. Re-vérification

**Harnais D4 sur B01 :**
- témoin **1/1** ;
- gardes **0/6** ;
- LCF **1/2** ;
- mutations au rouge **0/2**.

LCF-20 est déjà vérifiée sur B01 : BIBLIOTHEQUE 63 et 762 recopient aujourd'hui les quatre statuts du CHANGELOG. C'est une **condition de conservation** : elle empêchera la divergence quand `SEED` sera ajouté.

**Constats :**
1. **Le trou de F-CHG-001 est certain et sera rencontré dès la première dépréciation.** Toutes les routes actuelles sont des routes du seed (9.05). Elles n'ont aucun des statuts du tableau : elles sont « canoniques » (CHANGELOG 42). Pour en déprécier une, il faut soit la déclarer `ADOPTED`, ce qui revient à revendiquer un gain jamais mesuré (le contrat de gain réel de BIBLIOTHEQUE 739–749 l'exige), soit la retirer hors cycle. Même trou pour un `PILOT` qui a déjà des consumers : il n'a pas de voie de dépréciation avec migration.
2. **Deux formulations causales non bornées dans DIRECTION** : 74 (« il augmente la probabilité ») et 78 (« elle augmente la qualité du cadrage… »). Toutes les autres sources déclarent l'efficacité `NOT-VERIFIED`. 9.08 (N = 1, observateur unique) n'a observé aucun gain de présence ni de désirabilité. La recherche des autres formulations (« garantit », « améliore », « réduit ») ne trouve que des occurrences **bornées** : conditions, négations ou limites déclarées.
3. **F-DIR-046 est isolée.** La même chaîne dans BIBLIOTHEQUE 31 est juste : elle vise les routes de BIBLIOTHEQUE, structurelles par définition. Seul DIRECTION 817, qui parle de **toute** route partagée, doit être qualifié.

## 3. Les sept questions du §21

| Question | F-CHG-001 | F-DIR-002 | F-DIR-046 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : statut fictif, retrait sans compatibilité, nouveaux usages pendant la migration | **Oui** : adoption fondée sur un gain non mesuré | **Oui** : une heuristique ou un gate jugé par des critères structurels |
| Défaut réel ? | Oui (texte ; 8.02, 9.05) | Oui (texte ; 9.08) | Oui (texte) |
| Gain > charge ? | Oui : une ligne de statut, trois transitions | Oui : deux verbes | Oui : une proposition |
| Nouvelle autorité ? | **Non** : CHANGELOG est propriétaire du cycle de vie ; `SEED` nomme un état qui existe déjà de fait | Non | **Non** : les propriétaires sont ceux de DIRECTION 817 lui-même |
| Testable ? | Gardes, LCF-20, épreuve | LCF-21 | Garde, épreuve |
| Positif / défensif équilibré ? | **Oui, gain positif** : une route du seed peut être dépréciée **sans** revendiquer un gain | Oui : l'objectif reste affirmé comme objectif | Oui |
| Suppression ou fusion ? | **Correction normative** | **Clarification** | **Correction normative** |

## 4. PATCH-DECISION

**Décision : CORRIGER.** Aucun invariant RUN_CARD, aucun champ de schéma.

### 4.1 F-CHG-001 : statut de bootstrap et dépréciation depuis tout état utilisé

| # | Où | Correction |
|---|---|---|
| T-1 | **CHANGELOG 35–40** (table des statuts) | Nouvelle ligne **`SEED`** : « Route du seed V1, canonique par construction, **sans gain mesuré**. » Transitions : `ADOPTED` (contrat de gain réel satisfait, BIBLIOTHEQUE/EVOLUTION) ou `DEPRECATED`. La ligne `PILOT` ajoute `DEPRECATED` **lorsque la route a des consumers** ; sans consumer, `ABANDONED` suffit. La ligne `ADOPTED` est inchangée. La ligne `DEPRECATED` ajoute : « aucun nouvel usage ; migration par `ACTION/RUN-SYSTEM` (paquet SYSTÈME) ; puis `ABANDONED` » |
| T-2 | **CHANGELOG 42** | « Les routes présentes dans le seed de la V1 ont le statut **`SEED`** : canoniques, sans gain mesuré. **`ADOPTED` exige le contrat de gain réel** (`BIBLIOTHEQUE/EVOLUTION`). Une dépréciation **ne revendique aucun gain**. » L'expression « routes présentes dans le seed » est gardée : le validateur la cherche |
| T-3 | **BIBLIOTHEQUE 63 et 762** | Les deux listes de statuts ajoutent `SEED` (copies du CHANGELOG, gardées par LCF-20) |
| O-1 | **`validate_design_governance.py` 150** | `"SEED"` est ajouté aux termes requis de `check_lifecycle_contract` |

**Règle de transition, énoncée une seule fois (CHANGELOG) :** une route peut être dépréciée depuis **tout état publié ou utilisé** (`SEED`, `PILOT` avec consumers, `ADOPTED`). Une dépréciation interdit les nouveaux usages et exige une migration. Elle ne revendique jamais un gain.

### 4.2 F-DIR-002 : l'efficacité est un objectif, pas un résultat

| # | Où | Correction |
|---|---|---|
| T-4 | **DIRECTION 74** | « Il **vise à augmenter** la probabilité d'un travail de niveau expert en rendant explicites des décisions… ; **cette efficacité reste `NOT-VERIFIED`** (`CHANGELOG`) et s'éprouve par les pilotes. » |
| T-5 | **DIRECTION 78** | « …elle **vise à augmenter** la qualité du cadrage, de la position, de la première scène et de la boucle créative. » |

### 4.3 F-DIR-046 : le propriétaire de la promotion suit la nature de la route

| # | Où | Correction |
|---|---|---|
| T-6 | **DIRECTION 817** | « …l'ordre de décision est `DIRECTION/START` → `ACTION/RUN-SYSTEM` → **`BIBLIOTHEQUE/EVOLUTION` si la route est structurelle, sinon la source normative propriétaire** (`SAVOIR` pour une heuristique de jugement, `ACTION` pour un gate ou un champ de `RUN_CARD`) → `CHANGELOG`. » BIBLIOTHEQUE 31 est inchangé |

### 4.4 Entrées LCF

| ID | Condition | Source | Mutation |
|---|---|---|---|
| **LCF-20** | Les statuts listés par BIBLIOTHEQUE (63, 762) sont **exactement** ceux de la table du CHANGELOG | CHANGELOG, cycle de vie | M-13 |
| **LCF-21** | L'efficacité est `NOT-VERIFIED` dans README, RELEASE_NOTES et CHANGELOG. DIRECTION ne contient **aucune** formulation « augmente la probabilité » ou « augmente la qualité » qui ne soit pas bornée par « vise à » | CHANGELOG 21 ; README 16 | M-14 |

**La LCF passe à 21 entrées.** LCF-21 étend la LCF aux **claims d'efficacité**. C'est la même logique que D-FAC-1 : un texte ne peut pas affirmer ce que le propriétaire (ici CHANGELOG) déclare non vérifié. L'extension est déclarée.

**Limite déclarée (LCF-21).** La condition vise deux formulations précises. Elle ne détecte pas une nouvelle phrase causale écrite autrement : c'est à la revue bornée de release (C5) de la trouver.

## 5. Conditions et sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Passe CHANGELOG** : T-1 et T-2. **Passe BIBLIOTHEQUE** : T-3, avec B5, C3 et C7. **Passe DIRECTION** : T-4 à T-6, avec les passes déjà fixées |
| C2 | **O-1 dans le même cycle que T-1** : le validateur exige `SEED` dès que le CHANGELOG le porte |
| C3 | **Aucune route n'est reclassée en phase 12.** Toutes les routes du seed prennent `SEED`. Aucune ne devient `ADOPTED` sans le contrat de gain réel |

**Sortie (phase 13) :**
1. `D4_harnais_non_regression.py` : témoin **1/1**, gardes **6/6**, LCF **2/2**, mutations au rouge **2/2**. Harnais A1 à D3 verts.
2. **Épreuve de cycle de vie** (test de F-CHG-001) : route du seed sans mesure, route pilotée sans consumer, `PILOT` partagé avec consumers. Pour chacune : statut initial, interdiction de nouvel usage, migration, statut final. **Aucun gain revendiqué.**
3. **Épreuve de propriétaire** (test de F-DIR-046) : composant, heuristique CRAFT, gate ACTION, champ `RUN_CARD`. Chacun mène au propriétaire exact.

## 6. Sortie

- **PATCH-DECISION D4 : CORRIGER.**
  - 6 corrections de texte ;
  - 1 correction d'outil (terme requis `SEED`) ;
  - 2 entrées LCF (**21 au total**) ;
  - aucun invariant, aucun champ.
- **Lot D clos : les quatre grappes D1 à D4 sont décidées.** Avec le lot C, **toutes les grappes A, B, C et D (20) ont leur PATCH-DECISION.**
- Listes : liste close **90 lignes, 81 actifs** ; LCF **21**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Le système exige un gain mesuré pour promouvoir une route, mais il se décrivait lui-même comme efficace sans l'avoir mesuré, et ses propres routes étaient « canoniques » sans statut.
- La correction applique au système la règle qu'il impose aux routes : **un statut ne vaut que par sa preuve.**

**Prochaine étape : lots E1 (éditorial) et E2 (technique).** E2 porte les deux derniers candidats de schéma (F-DF-002, F-RB-002). Je propose de traiter **E2 d'abord** (11.21), parce qu'il ferme la liste des schémas, puis **E1** (11.22), puis la **clôture de la phase 11** (11.23 : lot F, inventaires finaux, conformité avant la phase 12).
