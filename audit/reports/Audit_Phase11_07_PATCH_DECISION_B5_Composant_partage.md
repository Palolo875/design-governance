# DG-AUDIT-001 — Phase 11.07 — PATCH-DECISION B5 : composant partagé / SYSTÈME

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.07 ». Dernière grappe du lot B.

**Grappe B5 :**

| Fiche | Gravité | Objet |
|---|---|---|
| F-BIB-004 | Significatif | SAVOIR/SYSTEM 704 renvoie le contrat détaillé d'un composant partagé vers BIBLIOTHEQUE/COMPONENTS, qui ne le fournit pas |
| F-SAV-007 | Significatif | SAVOIR/SYSTEM 694 ordonne « Reclassifie en SYSTÈME » sans vérifier que la décision partagée est l'objet direct du run |

**Sorties :**
- cette `PATCH-DECISION` ;
- `B5_harnais_non_regression.py`, une **garde textuelle** : B5 n'a aucun invariant machine.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00–11.06 ; D-FAC-1 = c (marquage « voir propriétaire ») |
| Empreintes | B01 `016e6002…` conforme |
| Sources relues | SAVOIR 690–707 (SYSTEM), 541 (ATLAS), 928 (règles d'or) ; BIBLIOTHEQUE 611–660 (COMPONENTS) ; ACTION 586–594 (« Contrat de composant et baseline »), 379–387 (RUN-SYSTEM), 885 ; DIRECTION 131, 138, 257 |
| Antécédents | 4.02 (A : objet direct partagé ; B : impact induit ; N2 accepté en machine), 4.03 (C : Dialog partagé), 9.03 (« le contrat résiste ; la tension F-BIB-004 demeure ») |

## 2. Re-vérification et un constat qui change la décision

**Garde textuelle B5 sur B01 : témoin 1/1, gardes 0/5.** En particulier, COMPONENTS ne nomme pas **8 des 12** responsabilités promises par SAVOIR 704 :
- anatomie ;
- variants ;
- responsive ;
- frontières de composition ;
- baseline ;
- source de vérité ;
- compatibilité ;
- prochaine revue.

Les quatre autres n'y apparaissent qu'à travers BRAND_GRAMMAR ou les tables de couches.

**Le constat : le contrat « manquant » existe déjà, mais ailleurs, et en double.**
- **ACTION 586–588** (« Contrat de composant et baseline ») : pour un pattern réutilisable ou un composant critique, documenter intention, non-usage, sémantique, clavier, focus, anatomie, slots, tokens, modes, variants, états, responsive, stories ou captures de baseline.
- **SAVOIR 704** : intention, anatomie, variants utiles, états, responsive, tokens, frontières de composition, baseline de rendu, source de vérité, owner, compatibilité, prochaine revue. Puis : « la structure détaillée relève de BIBLIOTHEQUE/COMPONENTS ».
- **BIBLIOTHEQUE/COMPONENTS** : la destination annoncée, **vide** pour une primitive ordinaire.

Le défaut n'est donc pas qu'une liste manque. **Deux listes voisines vivent chez deux propriétaires qui ne portent pas la structure, et le propriétaire désigné n'en a aucune.** Écrire une troisième liste dans COMPONENTS ajouterait une copie de plus, qui dériverait.

**Pour F-SAV-007**, la re-lecture confirme ce que 9.03 avait établi :
- la règle de classification est juste chez le propriétaire (START 131 : objet direct ; START 138 : direction d'abord, puis SYSTÈME dépendant) ;
- SAVOIR 696 reconnaît l'autorité de START ;
- **seul le verbe de 694** contredit les deux.

## 3. Les sept questions du §21

| Question | F-BIB-004 | F-SAV-007 |
|---|---|---|
| Change une décision, une exécution ? | **Oui** : deux consumers peuvent diverger silencieusement, faute d'un contrat lisible à l'endroit indiqué | **Oui** : le mode du run, décision la plus lourde |
| Défaut réel ? | Oui (garde : 8 responsabilités sur 12 absentes) | Oui (694 lu seul, 4.02 B) |
| Gain > charge ? | **Oui, avec une réduction nette** : une liste au lieu de deux | Oui : un verbe |
| Nouvelle autorité ? | **Non.** Le contenu est **déplacé et fusionné**, pas inventé : c'est l'union exacte d'ACTION 588 et de SAVOIR 704, au lieu que COMPONENTS indique déjà comme propriétaire | **Non** : l'autorité est rendue à START, qui la détient déjà |
| Testable ? | Oui : garde textuelle, plus l'épreuve de lecture 4.03 C | Oui : garde textuelle, plus l'épreuve de lecture 4.02 A/B |
| Positif / défensif équilibré ? | Oui : le contrat s'active selon le risque et le type (ACTION 588 : « pattern réutilisable ou critique ») ; pas de quinze champs pour un delta local | Oui : l'identité avec token induit garde son run DIRECTION |
| Suppression ou fusion ? | **Déplacement + fusion** (types §21) | **Suppression** d'un impératif |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **déplacement et fusion** (F-BIB-004) ;
- **correction normative** (F-SAV-007).

**Aucun invariant machine** : le choix entre objet direct et effet induit n'est pas dans la carte. B3 exige déjà le paquet SYSTÈME à l'acceptation.

**Propriétaires :**
- BIBLIOTHEQUE/COMPONENTS reçoit le contrat, puisque la structure lui appartient (SAVOIR 704 le dit) ;
- ACTION et SAVOIR gardent chacun leur part ;
- DIRECTION/START reste l'autorité de classement.

### 4.1 F-BIB-004 : un seul contrat, au bon endroit

| # | Où | Quoi |
|---|---|---|
| T-1 | **BIBLIOTHEQUE/COMPONENTS**, après la table des couches | Un bloc « **Contrat de composant partagé** », au format de BRAND_GRAMMAR (liste courte en `text`). Contenu : l'**union** d'ACTION 588 et de SAVOIR 704, soit intention, non-usage, sémantique, clavier et focus, anatomie et slots, tokens consommés et modes, variants utiles, états, responsive, frontières de composition, baseline de rendu, source de vérité, owner, compatibilité, prochaine revue. **Activation** : pattern réutilisable, composant critique ou composant partagé (ACTION 588) ; zéro obligation pour un delta local |
| T-2 | **ACTION 586–588** | La liste est remplacée par : « le contrat de structure est défini par BIBLIOTHEQUE/COMPONENTS ». ACTION garde ce qui lui appartient : **la baseline comme preuve** (590–594, reliée à `system_package.non_regression.baseline` de B3), la migration et le verdict |
| T-3 | **SAVOIR 704** | La liste est remplacée par un renvoi. SAVOIR garde **le jugement** : tokens primitifs et sémantiques, modes, interopérabilité, maintenance (692–700). « La structure détaillée relève de BIBLIOTHEQUE/COMPONENTS » devient vrai |

**Effet net :** trois textes (deux listes et un renvoi vide) deviennent un contrat et deux renvois. Chaque propriétaire garde son objet : la structure (BIBLIOTHEQUE), le jugement (SAVOIR), la preuve et l'exécution (ACTION).

### 4.2 F-SAV-007 : rendre la décision à START

| # | Où | Quoi |
|---|---|---|
| T-4 | **SAVOIR 694** | Remplacer « Reclassifie en `SYSTÈME` lorsqu'un token… affecte plusieurs consumers… » par : « **Signale à `DIRECTION/START`** l'effet partagé. START classe en `SYSTÈME` si la décision partagée est l'objet direct du run ; sinon la direction est traitée d'abord et le run système dépendant est ouvert ensuite (START 131, 138). » La phrase 696 reste |

### 4.3 Coordination avec le lot éditorial

**F-SAV-004** (ATLAS 541 omet `SAVOIR/SYSTEM`) est dans le lot E1. Elle touche la même zone : T-4 et F-SAV-004 seront appliqués dans **le même cycle** d'édition de SAVOIR en phase 12, pour éviter deux passes sur le même propriétaire. **F-SAV-004 reste dans E1** ; rien n'est déplacé.

## 5. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Trois propriétaires, un cycle** (§22) : BIBLIOTHEQUE porte la décision principale ; ACTION et SAVOIR sont des renvois directement concernés |
| C2 | **Aucun contenu nouveau** dans T-1 au-delà de l'union d'ACTION 588 et de SAVOIR 704 |
| C3 | **Proportion** : le bloc précise son activation ; il n'est ni un formulaire à remplir pour tout composant, ni un quota |
| C4 | **Locator** : le bloc T-1 doit être atteignable par le lecteur de routes. Si la granularité des locators (F-RM-003, grappe C4) n'est pas encore corrigée, le renvoi cite la section parente `BIBLIOTHEQUE/COMPONENTS`, qui résout déjà |
| C5 | Relecture complète de BIBLIOTHEQUE 611–660, SAVOIR 690–707, ACTION 586–596 et de la règle d'or SAVOIR 928 |

## 6. Condition de sortie (phase 13)

1. `B5_harnais_non_regression.py` : **1/1 et 5/5** (garde textuelle).
2. **Épreuve de lecture**, la seule preuve réelle d'une correction normative, rejouée par un lecteur qui ne connaît pas ce rapport :
   - **4.02 A** : token sémantique partagé en objet direct → SYSTÈME ;
   - **4.02 B** : première scène de marque qui suggère un token → DIRECTION d'abord, puis SYSTÈME dépendant, **sans reclassement en SYSTÈME** ;
   - **4.03 C** : Dialog partagé → le lecteur trouve l'anatomie, les variants, les tokens, la baseline et la source de vérité **dans COMPONENTS**, en une ouverture.
3. Les harnais machine (A1 à B4) restent verts (B5 ne les touche pas).

**Limite déclarée.** La garde textuelle détecte l'absence ou la présence de formulations ; elle ne prouve pas la compréhension. L'épreuve de lecture reste nécessaire. Idéalement, elle est faite par un observateur indépendant : c'est la limite F-ACT-037 de toute la campagne.

## 7. Sortie

- **PATCH-DECISION B5 : CORRIGER** : 1 déplacement-fusion (une liste en moins), 1 verbe remplacé ; aucun invariant machine.
- **Lot B clos : les cinq grappes B1 à B5 sont décidées.**
  - Les 14 Majeur du registre ont tous une décision de correction (A1 : 2 ; B1 : 3 ; B2 : 6 ; B3 : 2 ; B4 : 1).
  - La liste close compte 53 invariants actifs.
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- un « contrat manquant » s'est révélé être un contrat **en double au mauvais endroit** : la correction retire une liste au lieu d'en ajouter une ;
- un seul verbe suffit pour rendre la classification à son propriétaire ;
- deux corrections de la même zone sont coordonnées sans déplacer de fiche.

**Prochaine unité : 11.08 PATCH-DECISION C1** (registres, temps et sémantique de preuve : 14 fiches, dont F-ACT-014 à traiter **avant** F-DIR-011). C'est la plus grosse grappe restante. Je proposerai de la traiter comme les autres : une décision de grappe, avec des sous-décisions seulement pour les fiches qui divergent.
