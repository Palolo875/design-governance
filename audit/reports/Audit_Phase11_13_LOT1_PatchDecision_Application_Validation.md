# DG-AUDIT-001 — Phases 11.01 → 13.01 — Lot 1 : décision, application et validation (B02 candidate, V1.0.1)

**Date :** 25 septembre 2026. **Baseline source :** B01 (empreintes revérifiées : compilation `016e6002…5f355d`, protocole `990fc86f…dc20610dd`). **Sortie :** package candidat **B02 / V1.0.1**, non publié. La source B01 n'est pas modifiée : toutes les corrections sont appliquées sur une copie.

Les trois phases sont regroupées dans un seul rapport, comme le permet le §7.8 du protocole : la décision, l'application et la validation portent sur les mêmes 18 fichiers et les mêmes preuves.

---

## 0. Décisions de l'owner retenues

Le « Allons-y » de l'utilisateur est lu comme une acceptation des propositions par défaut du §5 du rapport 10.00. Si ce n'est pas le cas, chaque point reste réversible.

| Question | Décision appliquée |
|---|---|
| Gravité de la famille A | **Majeur** (proposition 10.00) |
| Principe de la famille E | Accepté pour la suite. **Non appliqué ici** : les 3 règles ciblées relèvent du lot 2. |
| Périmètre du lot 1 | Lot 1 complet (outillage + façades), sans toucher les règles des propriétaires |
| Fiches Z | Laissées hors tri. Les checkpoints de phase 2 ne sont pas fournis. |
| Phase 9 | Reste suspendue |

**Deux écarts de périmètre, assumés :**
1. **Ajouts.** Sept fiches des familles B et A prévues pour le lot 2 ont été corrigées ici, parce qu'elles se trouvent dans les mêmes fonctions que les corrections du lot 1 : F-VRC-002/003/008, F-VCT-002, F-VDG-004, F-BLD-003, F-VRM-001/002, F-RRT-001. Le coût marginal était quasi nul.
2. **Retraits.** Deux corrections initialement prévues sont exclues :
   - **F-SAV-010** : sa correction toucherait `SAVOIR.md`, une source propriétaire, et non une façade. Elle passe au lot 3.
   - **F-ACT-001** : même raison, pour `ACTION.md`.

---

## 1. PATCH-DECISION (§21) — contrôle avant correction

Les sept questions du §21 ont été posées à chaque correction. En synthèse :

| Question §21 | Réponse pour le lot 1 |
|---|---|
| Change une décision, une preuve ou une maintenance ? | Oui. Un faux PASS change ce que le mainteneur croit prouvé ; une cellule de façade change la route choisie. |
| Le fichier ciblé porte-t-il réellement le défaut ? | Oui. Chaque défaut est reproduit sur B01 (§3). |
| Le gain dépasse-t-il la charge ? | Oui. **0 ligne ajoutée aux quatre propriétaires DIRECTION, ACTION, SAVOIR et BIBLIOTHEQUE.** Les façades changent par déplacement de cellule plus qu'en longueur : +3 lignes nettes hors table des locators (flow.md) et environ +2 Ko de texte, surtout des précisions de condition. La table des locators passe de 24 à 70 lignes, chacune un titre existant. |
| Nouvelle autorité créée ? | Non. Les cartes restent dérivées. Les validateurs vérifient la conformité aux propriétaires ; ils ne créent pas de règle. |
| Observable ou testable ? | Oui. Chaque correction a une mutation dédiée (§3) ou un contrôle intégré à la suite. |
| Équilibre positif / défensif ? | Oui. Aucune route créative ou capacité positive n'est retirée ni contrainte. |
| Suppression ou fusion préférable ? | Pour les façades, c'est un **déplacement** de cellule (colonne « si nécessaire » vers noyau), pas un ajout de règle. |

**Deux choix de conception à signaler.**
- **Liste de chemins gardés.** `GUARDED_ENUM_PATHS` nomme les chemins dont le vocabulaire doit rester fermé. Elle ne recopie aucune valeur : le schéma reste l'autorité du vocabulaire. C'est un petit « contrat du contrat ». Il faudra le mettre à jour si un enum légitime est ajouté ou retiré.
- **Table des locators.** Elle est désormais exhaustive : tout locator cité dans le package doit y figurer. Citer un nouveau nom sans l'ajouter à la table fera donc échouer la validation. C'est voulu : un nom cité doit pouvoir être résolu.

---

## 2. Corrections appliquées (18 fichiers)

| Fichier | Changement | Fiches |
|---|---|---|
| `scripts/validate_run_card.py` | Refus d'un schéma vide ou non admissible ; 8 enums gardés mutés hors vocabulaire ; chaque champ requis atteint par l'exemple supprimé, et la suppression doit être rejetée ; contrôle « le validateur lit l'enum du schéma » conservé ; clés répétées et UTF-8 invalide transformés en diagnostic ; exceptions brutes transformées en diagnostic ; motif attendu pour `invalid_missing_proof` ; fixture `capability_profile_missing_basis` ajoutée à la suite native | F-VRC-001/002/003/006/007/008, F-FIX-001/003 |
| `scripts/validate_contracts.py` | Admission du schéma ; enums gardés (`originality_tolerance`, `depth`, `proof_status`, `expected_depth`) ; suppression de chaque champ requis ; clés répétées ; exceptions transformées en diagnostic | F-VCT-001/002/003 |
| `scripts/validate_all.py` | Motif attendu vérifié pour les 4 fixtures CLI ; fixtures résolues depuis la racine du package | F-ALL-001/002 |
| `scripts/build_distributions.sh` | Refus des liens symboliques ; archives neuves ; chaque ZIP comparé au manifest de son profil ; publication conjointe des ZIP et de `dist` ; restauration de la sauvegarde après une publication interrompue | F-BLD-001/003/004, F-BLD-002 partielle |
| `scripts/validate_design_governance.py` | Unicité du manifest ; version comparée à CHANGELOG et aux titres ; liens symboliques refusés ; répertoires générés ignorés **seulement à la racine** ; fichier requis absent transformé en diagnostic | F-MAN-001/002, F-VDG-001/004 |
| `scripts/validate_reading_map.py` | Locator dupliqué refusé ; tout locator cité doit être servi ; route de mode interdite en colonne conditionnelle ; handoff de la carte ⊇ champs d'`ACTION/HANDOFF` | F-VRM-001/002, garde de F-DIR-028 et F-RM-001 |
| `scripts/read_route.py` | Titres dans un bloc de code ignorés ; titre ambigu refusé | F-RRT-001 |
| `V1/official/READING_MAP.md` | +46 locators (70 au total, tous vérifiés sur un titre unique) ; `ACTION/RUN-DIRECTION` placé dans la première lecture ; minima SYSTÈME dans la première lecture ; N/A accessibilité conditionné à une raison vérifiable | F-DIR-028, F-RM-001/002 |
| `V1/official/ORCHESTRATION_MAP.md` | Gate A, gates du mode et minima SYSTÈME déplacés en noyau ; phrase de garde | F-OM-001 |
| `V1/official/QUICKSTART.md` | Craft sur une direction retrouvable = ITER ; SYSTÈME = objet direct avec consumers, CHANGELOG inclus, COMPONENTS seulement si un composant est touché | F-QS-002, F-QS-001 partielle |
| `README.md` | ITER exige une direction retrouvable ; SYSTÈME = objet direct | F-RDR-001 |
| `skills/…/SKILL.md` | 13 champs d'`ACTION/HANDOFF` ; dossier officiel nommé pour les deux profils ; sortie courte = préparation | F-SK-001/002 |
| `skills/…/references/flow.md` | Reprises après protection critique et après `NOT-VERIFIED` | F-FLOW-001 |
| `.github/workflows/validate.yml` | `checkout@v5`, `setup-python@v6` (Node 24) | F-WF-001 (partielle) |
| `CHANGELOG.md`, `RELEASE_NOTES.md`, deux README, `QUICKSTART.md`, manifest, build | Version V1.0.1 (candidat, non publié) et entrée de changement | cycle de version |

**Fichiers inchangés, vérifiés par comparaison d'octets :** `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md`, `GLOSSAIRE.md`, tous les schémas, exemples et fixtures. Le package garde **60 fichiers GitHub et 56 Local**.

**Diff total :** 18 fichiers, +527/−95 lignes, dont environ 450 dans les scripts. Il est fourni en entier dans `DG_B02_lot1.diff`.

---

## 3. Validation (§13)

### 13.3 Machine — suite intégrée

`validate_all.py` sur B02 : **`FULL VALIDATION PASSED`**. La suite couvre documentaire, RUN_CARD, contrats, carte, CLI, build GitHub et Local, contrôle ZIP/manifest (60/60, 56/56) et reproductibilité sur deux builds.

### 13.5 Non-régression — mutations discriminantes

Chaque mutation est appliquée à une copie jetable de B01 et à une copie de B02. **Critère :** B01 réussit à tort ou plante ; B02 échoue avec un diagnostic lisible.

| # | Mutation | B01 | B02 |
|---|---|---|---|
| M01 | schéma RUN_CARD `{}` | **PASS**, code 0 | échec : « schéma vide » |
| M02 | enum `run_card.mode` retiré | **PASS** | échec : « enum gardé absent » |
| M03 | schéma `domain_frame` `{}` | **PASS** | échec : « schéma non admissible » |
| M04 | enum `research_brief.depth` retiré | **PASS** | échec : « enum gardé absent » |
| M05b | fixture `missing_proof` rejetée pour un autre motif | **PASS** | échec : « diagnostic inattendu » |
| M06 | clé JSON répétée dans une carte | **PASS** (carte acceptée) | échec : « clé JSON répétée » |
| M07 | carte en UTF-8 invalide | traceback | diagnostic |
| M09 | chemin dupliqué dans le manifest | **PASS** (61 fichiers) | échec : « chemin dupliqué » |
| M10 | version du manifest divergente | **PASS** | échec : version |
| M11 | fichier sous `V1/official/.build` | **PASS** | échec : fichier inattendu |
| M12 | README officiel absent | traceback | diagnostic |
| M13 | RUN-DIRECTION remis en colonne conditionnelle | **PASS** | échec : route de mode |
| M14 | locator dupliqué | **PASS** | échec |
| M15 | `read_route.py ACTION/HANDOFF` | refus « locator inconnu » | bloc servi (18 lignes) |
| M16b | `validate_all.py` lancé depuis `/tmp` | échec : fixture introuvable | **FULL PASS** |
| M17b | `ACTION.md` devenu un lien symbolique, puis build | **build vert, ZIP sans ACTION.md** | build refusé, aucun ZIP |
| M18 | ZIP périmé avec un membre en trop, puis build | **membre périmé conservé** | ZIP neuf, conforme |
| — | faux titre dans un bloc de code avant START | extrait du faux bloc | vrai bloc |
| — | champ `DECISION-CHANGE` retiré du handoff de la carte | **PASS** | échec : handoff incomplet |

**Bilan : 19/19 discriminants.** M08 (carte `run_card` sous forme de liste) était déjà correctement rejeté par B01 ; ce n'est pas un défaut.

### 13.1 et 13.2 — texte, contrat et accès

- **Les 24 routes de B01 sont servies à l'identique, à l'octet près, par B02.** Les 46 nouvelles routes résolvent chacune un titre unique.
- **Plus grands blocs servis :** CRAFT 186 lignes, START 130, STYLE 120. F-DIR-044 (bloc trop large) **n'est pas traité** dans ce lot.
- **Relecture des cellules de façade contre leur propriétaire :**
  - READING_MAP 33 ↔ ACTION 369–377 ;
  - READING_MAP 34 et ORCHESTRATION « Système » ↔ ACTION/PRECONDITION (SYSTÈME : migration, rollback, non-régression, CHANGELOG) ;
  - ORCHESTRATION « UI/UX » ↔ PRECONDITION (Gate A applicable dans tous les modes) ;
  - README ITER et QUICKSTART craft ↔ START, questions 2 et 3 de l'arbre.

### 13.4 Distribution

- Deux ZIP construits, contrôlés contre le manifest, identiques entre deux builds.
- L'export Local passe sa propre suite ; il inclut le contrôle des locators, qui lit `skill/` et le README généré.
- **Non observé :** aucune publication distante, aucun run CI hébergé.

---

## 4. Ce qui reste ouvert après le lot 1

| Élément | État |
|---|---|
| F-QS-004, F-QS-001 (partie « retour LITE trop large ») | **Non traitées.** La description exacte se trouve dans les rapports QUICKSTART de phase 2, absents du transfert. |
| F-ACT-001, F-ACT-002 (tables internes d'ACTION) | Propriétaire non touché. L'accès CLI à STATUS, PRECONDITION et HANDOFF atténue le problème sans le résoudre → lot 3, avec décision de l'owner. |
| F-DIR-044 (blocs extraits trop larges) | Non traitée. Une mesure du besoin réel est d'abord nécessaire. |
| F-VRM-003 (frontière d'autorité contredite malgré les mots requis) | Non traitée. |
| F-FIX-002 (fixtures composites) | Atténuée : le motif est désormais vérifié. Les fixtures ne sont pas décomposées. |
| F-WF-001 | Actions mises à jour. **Un run GitHub hébergé vert reste la preuve manquante.** |
| Limite des canaris | Ils garantissent que les enums *gardés* et les champs requis *présents dans le schéma* mordent. Retirer un `required` du schéma n'est pas détecté ; seul l'ajout d'un chemin à la liste gardée le rendrait détectable. |
| Familles E (lot 2), H et J (lot 3), G (après 6.02), Z (53) | Inchangées |

**Registre après le lot 1 :**
- 32 fiches corrigées en B02, dont 19 avec mutation discriminante ;
- 5 fiches partielles ;
- 5 fiches non traitées ou retirées ;
- 115 fiches hors lot, toujours ouvertes.

Le détail par fiche est dans la colonne « Statut B02 » du CSV. Aucune fiche n'est close définitivement : la clôture relève de la phase 14, après décision de publication.

---

## 5. Sortie et suite

**B02 / V1.0.1 : candidat validé en local, non publié.** Livrables :
- `DG_B02_V1.0.1_package.zip` : 60 fichiers, SHA-256 `98a30eb486e4ff5747425d86c756f264a7d00676cc10bd1106271317743557ad` ;
- `DG_B02_lot1.diff`.

**Prochaines actions, par ordre de valeur :**
1. **Publication par l'owner.** Pousser B02 sur GitHub et obtenir un **run CI hébergé vert**. C'est la preuve qui clôt F-WF-001 et la première preuve hébergée de la campagne.
2. **Reprendre 6.02 hors du navigateur d'audit.** Deux vrais runs, un micro-delta et une première scène DIRECTION, avec captures. C'est la condition pour trier la famille G, le cœur créatif du système.
3. **Lot 2.** Les 3 règles ciblées de la famille E, F-RC-001 (rejet à tort), les exemples F-EX et F-MP.
4. **Tri des 53 fiches Z** dès réception des checkpoints de phase 2 DIRECTION et ACTION.
