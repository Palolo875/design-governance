# DG-AUDIT-001 — Phase 11.10 — PATCH-DECISION C3 : proportion

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec 11.10 ».

**Grappe C3 : 3 fiches, toutes Significatif.** Même famille de défaut : **une forme prévue pour le cas lourd s'applique au cas léger**, faute d'une condition de passage.

| Fiche | Objet | Coût mesuré |
|---|---|---|
| F-BIB-002 | BIBLIOTHEQUE/DERIVE déclare quinze lignes d'emblée pour une forme locale ; CONTRACTS parle d'un contrat réduit de quatre éléments ; le passage de l'un à l'autre n'est pas dit | 9.08 : la surcharge de proportion est le coût principal mesuré |
| F-PC-001 | `CREATIVE_DIRECTION_SET` : deux directions et deux changements structurels minimum ; deux textes identiques sous deux IDs passent | Friction portée dans sept unités de la campagne (4.07 à 9.06) |
| F-SK-001 | La « sortie minimale » de onze champs (skill, QUICKSTART) : réponse courte ou handoff canonique ? | 9.08 : en LITE, 9 champs HANDOFF sur 13 deviennent `N/A-JUSTIFIED` |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C3_harnais_non_regression.py` : contrats et gardes textuelles ;
- 2 lignes ajoutées à la liste close.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 à 11.09 ; D-ACT-1 = c ; D-FAC-1 = c ; règle A2 ; C2 (activation des contrats, forme courte LITE, racine « au moins un », vocabulaire de phase) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218. Les contrôles directs ont été faits sur une **copie** temporaire |
| Sources relues | BIBLIOTHEQUE 54–61 (niveaux de contrat), 205–235 (garde-fou et DERIVE), 256–275 (CONTRACTS) ; ACTION 23–36 (HANDOFF), 903 (« aucun quota de variantes ») ; SAVOIR 279 ; DIRECTION 716–718 ; QUICKSTART 28–33, 198–210 ; READING_MAP 56–76 ; skill 14–16, 61–67, 135–139 |
| Machine relue | `production_contracts.schema.json` (`creative_direction_set`) ; `validate_contracts.semantic_check` (ids uniques, direction choisie existante, « au moins deux relations structurelles ») |

## 2. Re-vérification

**Harnais C3 sur B01 :**
- témoins **2/2** ;
- contrats **0/6** ;
- gardes **0/8**.

**Contrôles directs sur B01 :**

| Cas | B01 | Attendu |
|---|---|---|
| Deux directions A et B aux textes **identiques** | **accepté** | rejet : une direction copiée n'est pas une alternative |
| Un même changement structurel compté deux fois | **accepté** | rejet |
| Deux directions distinctes, **un seul levier structurel** chacune | **rejeté** (`nombre minimal d'éléments non atteint`) | acceptation : aucune source textuelle n'exige deux leviers |
| Aucune alternative plausible : pas d'ensemble créatif | **rejeté** (racine obligatoire) | acceptation, déjà décidée en C2 (INV-C2-2) |

**Relecture des textes : trois constats.**

1. **Le quota n'a aucune source, et deux textes le contredisent.** Aucun propriétaire n'exige deux leviers structurels par direction. ACTION 903 (« aucun quota de variantes ») et SAVOIR 279 (« ne crée ni quota de variantes ») l'interdisent. BIBLIOTHEQUE 237 dit même l'inverse pour une dérivation : « modifie d'abord **un seul** levier principal ». En revanche, **deux positions au minimum** définissent un ensemble. DIRECTION 716 exige « la position retenue » **et** « l'alternative considérée » : ce minimum est une définition, pas un quota.
2. **Le contrat réduit existe deux fois, en deux versions.** Pour une route locale :
   - BIBLIOTHEQUE 58 : décision, responsabilité, preuve attendue, **limite** ;
   - CONTRACTS 258 : responsabilité, **contre-indications**, preuve attendue, décision initiale.

   DERIVE (217–235) ne cite ni l'une ni l'autre et pose ses quinze lignes d'emblée.
3. **Cinq listes de sortie coexistent :**

   | Source | Longueur | Nature |
   |---|---|---|
   | ACTION/HANDOFF | 13 champs | canon |
   | READING_MAP 56 | 13 champs | copie conforme |
   | Skill 16, QUICKSTART 33 | 11 champs | sans OBSERVATION/METHOD ni DECISION-CHANGE, nommés « au minimum » |
   | QUICKSTART 208 | 7 éléments | réponse « par défaut » |
   | Skill 65 et 137 | 5 et 6 éléments | réponse ou trace |

   La liste à onze champs est **trop longue** pour une réponse courte et **trop courte** pour un handoff.

## 3. Les sept questions du §21

| Question | F-BIB-002 | F-PC-001 | F-SK-001 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : remplissage fictif d'un essai local, ou omission d'un risque actif | **Oui** : variantes fabriquées dans la trace ; la décision solide est diluée | **Oui** : handoff privé de méthode et de décision changée, ou formalité sur un correctif |
| Défaut réel ? | Oui (relecture, 9.08) | Oui (§2, sept unités) | Oui (cinq listes, 9.08) |
| Gain > charge ? | **Oui, avec réduction** : un essai local part de cinq notions, contre quinze lignes | **Oui** : un quota retiré, deux contrôles ajoutés | **Oui, avec réduction** : deux sorties nommées remplacent cinq listes |
| Nouvelle autorité ? | **Non** : l'union des deux contrats réduits existants ; les champs DERIVE sont **rangés**, pas ajoutés | **Non** : on retire une exigence sans source ; l'authenticité découle du mot « alternative » | **Non** : la réponse visible reprend mot pour mot QUICKSTART 208 ; le handoff reste ACTION |
| Testable ? | Garde plus épreuve de lecture | Machine (C3-01 à C3-P3) | Gardes plus test de cohérence de façade (C5) |
| Positif / défensif équilibré ? | Oui : départ léger, et les champs de risque s'activent avec lui | **Oui, gain positif** : un seul levier devient valide ; ne pas produire l'ensemble devient valide | Oui : une réponse courte pour l'humain, un handoff complet pour la reprise |
| Suppression ou fusion ? | **Fusion** et **clarification** | **Suppression** (quota) et **validateur** (authenticité) | **Simplification** et **façade** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

Règle commune : **la forme légère est le point de départ ; la forme lourde s'active par une condition nommée.**

### 4.1 F-BIB-002 : un contrat réduit, des phases nommées

| # | Où | Quoi |
|---|---|---|
| T-1 | **CONTRACTS 258** | Le contrat réduit devient **l'union** des deux versions : **décision initiale, responsabilité, contre-indication, preuve attendue, limite**. C'est la seule définition |
| T-2 | **BIBLIOTHEQUE 58** (ligne `Local`) | « Contrat réduit (`BIBLIOTHEQUE/CONTRACTS`) ; `N/A-JUSTIFIED` si aucune route ne change. » Les lignes `PILOT`, `Partagé` et `Durable` ne changent pas |
| T-3 | **DERIVE 217–235** | Le bloc garde ses quinze lignes, **rangées par phase** avec le vocabulaire de C2 (voir le tableau ci-dessous) |

Rangement des lignes DERIVE (T-3) :

| Phase | Lignes DERIVE | Correspondance |
|---|---|---|
| **Avant build** (contrat réduit) | BASE-ROUTE, PRODUCT-CONSTRAINT, CHANGED-LEVER | décision initiale |
| | PRESERVED-RESPONSIBILITY | responsabilité |
| | NEW-COUNTERINDICATION | contre-indication |
| | FIRST-OBJECT, OBSERVABLE-CONSEQUENCE | preuve attendue |
| | PREVIOUS-LIMIT | limite |
| **Si le risque l'active** | STRUCTURAL-SIGNATURE (écart ouvert), A11Y / PERFORMANCE | — |
| **Après observation** | SCOPE, CONTENT / STATES, PROOF-TYPE / PROOF-LIMIT, EXIT-CONDITION (maintenir, modifier, abandonner), NEXT-PROOF | — |
| Hérité | OWNER : celui de la ligne de run, sauf changement | — |
| **Promotion** | Table complète de CONTRACTS, par `BIBLIOTHEQUE/EVOLUTION` | — |

**Effet :** un essai local à faible risque démarre avec huit lignes courtes, qui portent cinq notions, au lieu de quinze. Un risque actif (erreur, contenu long, accessibilité) rappelle ses lignes **sans attendre** la promotion.

### 4.2 F-PC-001 : retirer le quota, garder la définition, contrôler l'authenticité

**Machine (liste close D-ACT-1) :**

| ID ou changement | Règle | Motif (A2) |
|---|---|---|
| **Retrait** | `structural_changes` : `minItems` 2 → 1, dans le schéma ; la vérification « au moins deux relations structurelles » est retirée de `semantic_check` | — |
| **INV-C3-1** | Les directions sont deux à deux **distinctes** après normalisation (casse, espaces) du couple (tension, ensemble des changements structurels) | « directions non distinctes » |
| **INV-C3-2** | Dans une direction, les changements structurels sont **distincts** après normalisation | « changements structurels en double » |
| **Conservé** | `directions` : `minItems` 2. C'est la définition d'un ensemble ; le témoin T-CONS la garde | — |

**Exception motivée : sous-décision.** La recommandation demandait une « exception motivée modélisée ». **Je ne la modélise pas dans le contrat.** Une variante « ensemble à une direction avec raison » créerait une seconde place pour la même exception. Cette exception est déjà modélisée ailleurs :
- par la **non-activation** du contrat (matrice C2, T-9 : « DIRECTION à décision ouverte avec alternative plausible ») ;
- par la **racine facultative** (INV-C2-2) ;
- par la **raison inscrite dans la trace** (DIRECTION 716 : « note cette condition… après avoir nommé la raison » ; C2, T-6).

Le cas-test de la fiche « contrainte sans contre-choix » est couvert par C3-P2.

**T-8. ACTION/STRUCTURED-PROOF** (ligne `CREATIVE_DIRECTION_SET` de la matrice C2) : « L'ensemble compare au moins deux positions réelles. Si aucune alternative plausible n'existe, il n'est pas produit : aucune direction n'est fabriquée pour l'atteindre. Lorsqu'il est produit, il fait partie de la trace du run (C2, T-6). »

**Hors fiche, signalé sans décision.** `directions.maxItems = 3` n'a pas non plus de source textuelle. C'est une borne, pas une obligation : elle ne force aucune fabrication, et je ne la modifie pas. Elle est versée à **C9** (contrats de production), qui décidera les contrôles existants des contrats.

### 4.3 F-SK-001 : deux sorties nommées

| # | Où | Quoi |
|---|---|---|
| T-4 | **ACTION/HANDOFF** (canon) | Nomme **deux sorties** (voir le détail ci-dessous) |
| T-5 | **Skill 16** | La liste de onze champs est remplacée par les **deux sorties**, recopiées mot pour mot du canon et marquées « voir `ACTION/HANDOFF` ». La skill est distribuable seule (« lorsque le package le fournit ») : une **copie de façade** est justifiée (D-FAC-1 = c), à condition qu'elle soit testée |
| T-6 | **Skill 65 et 137** | 65 : « par défaut, restitue la **réponse visible** ». 137 : « donne ensuite le **handoff** au niveau du mode (forme courte en LITE) » |
| T-7 | **QUICKSTART 33 et 208** | 33 : la liste de onze champs devient une phrase qui nomme les deux sorties et renvoie à `ACTION/HANDOFF`. 208 : le bloc est gardé, marqué « voir `ACTION/HANDOFF` » |

Les deux sorties définies en T-4 :
1. **Réponse visible**, pour un humain, par défaut : `MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER`. C'est QUICKSTART 208, repris sans changement ; `CHANGE` vaut `DECISION-CHANGE` ou `N/A-JUSTIFIED`.
2. **Handoff**, pour une reprise ou un run persistant : les treize champs. Forme courte LITE : C2, T-3.

La réponse visible ne remplace jamais le handoff d'un run persistant.

**READING_MAP 56 : conforme.** C'est une copie exacte des treize champs, déjà déclarée non substitutive. Aucun changement.

**Coordination.**
- T-4 est appliqué **dans la même passe ACTION** que C2 T-3 (même section HANDOFF).
- L'égalité entre copies de façade et canon (skill 16, QUICKSTART 208, READING_MAP 56) sera vérifiée au build par le **test de cohérence de D-FAC-1, décidé en C5** (F-VRM-003). Les gardes G-06 et G-08 n'en sont qu'une version locale.

## 5. Complément à la liste close

La liste close compte désormais **68 lignes, 64 actifs**. Elle compte 5 invariants de contrats : INV-C2-2 à INV-C2-4, INV-C3-1 et INV-C3-2.

**Lacune signalée.** C2 a étendu la liste aux contrats, mais les **contrôles existants** de `validate_contracts` n'y sont pas inventoriés : ids uniques, direction choisie existante, liaison `coverage_map`, relations risque → contrôle… Ils sont versés à **C9**, qui en fera l'inventaire (conservé / modifié / retiré), comme 11.04 l'a fait pour la RUN_CARD. Le retrait du quota de C3 y figurera comme « EXISTANT — retiré ».

## 6. Inventaire à date de la migration unique : ajouts C3

| Objet | Changement |
|---|---|
| `production_contracts.schema.json` : `directions[].structural_changes` | `minItems` 2 → 1 |
| `validate_contracts.semantic_check` | Retrait du contrôle « au moins deux relations structurelles » ; INV-C3-1 et INV-C3-2 |
| `production_contracts.example.json` | Inchangé par C3 : ses deux directions sont déjà distinctes |

Candidats encore ouverts : C4, C9, D2.

## 7. Conditions du futur patch (phase 12)

| # | Condition |
|---|---|
| C1 | **Passe ACTION unique** : C1 T-1 ; C2 T-1 à T-3, T-9, T-10 ; C3 T-4 et T-8 ; B5 T-2 |
| C2 | **Passe BIBLIOTHEQUE unique** : B5 T-1 et C3 T-1 à T-3 (COMPONENTS, CONTRACTS et DERIVE, même propriétaire) |
| C3 | **Façades après canon** : skill et QUICKSTART (T-5 à T-7) seulement après T-4 ; copies identiques mot pour mot |
| C4 | **Aucun contenu nouveau** : le contrat réduit est l'union de deux textes ; la réponse visible est QUICKSTART 208 ; le rangement DERIVE n'ajoute aucune ligne |
| C5 | **Relecture complète** de BIBLIOTHEQUE 50–62, 205–275 ; ACTION 23–36 ; QUICKSTART 28–36, 195–212 ; skill 1–149 |

## 8. Condition de sortie (phase 13)

1. `C3_harnais_non_regression.py` : témoins **2/2**, contrats **6/6**, gardes **8/8**. Harnais A1 à C2 verts.
2. **Épreuve de lecture**, rejouée par un lecteur qui ne connaît pas ce rapport :
   - **dérivation** :
     - locale à faible risque : les champs requis sont les cinq notions ;
     - locale avec erreur et contenu long : STATES et A11Y s'activent ;
     - `PILOT` observé ;
     - route durable ;
   - **sortie** :
     - correctif LITE rendu à un humain : réponse visible seule, rejeu 9.08 ;
     - run persistant transmis à un agent : réponse visible, trace, handoff complet ;
   - **direction** :
     - décision ouverte à deux positions : ensemble produit ;
     - contrainte sans contre-choix : ensemble non produit, raison dans la trace, **aucune variante fabriquée** (rejeu 4.07 et 6.01).
3. **Test de cohérence de façade** (C5) : skill 16, QUICKSTART 208 et READING_MAP 56 sont identiques au canon.

**Limite déclarée.** Les gardes détectent des formulations. La réduction de charge reste une **hypothèse** tant qu'un run réel ne l'a pas mesurée : BIBLIOTHEQUE 52 le rappelle, « le chemin minimal décrit une hypothèse de proportion ».

## 9. Sortie

- **PATCH-DECISION C3 : CORRIGER.**
  - 2 invariants d'authenticité, 1 quota retiré ;
  - 8 corrections de texte ;
  - 1 sous-décision : l'exception est modélisée par la non-activation, pas par une variante du contrat ;
  - 1 lacune signalée : l'inventaire des contrôles existants des contrats, versé à C9.
- **Liste close : 68 lignes, 64 actifs.**
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Trois fiches, un seul mécanisme : **un seuil d'activation manquant**.
- La correction **retire** plus qu'elle n'ajoute : un quota, deux listes concurrentes de sortie, une définition doublée du contrat réduit.
- Elle ajoute deux contrôles, qui empêchent de **simuler** une alternative.

**Prochaine unité : 11.11 PATCH-DECISION C4** (accès, locators et chargement : 5 fiches, dont F-RM-003 et le candidat de schéma F-ACT-020).
