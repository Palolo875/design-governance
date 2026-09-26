# DG-AUDIT-001 — Phase 11.22 — PATCH-DECISION E1 : lot éditorial

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne avec E1 ».

**Lot E1 : 27 fiches, toutes Mineur.** Le lot est traité par **une décision de lot**. Chaque fiche reçoit son texte cible ; aucune n'appelle de sous-décision de fond.

**Sorties :**
- cette `PATCH-DECISION` ;
- `E1_harnais_non_regression.py` : une garde par fiche et une garde de coordination ; F-SK-002 est testée par un build sur copie ;
- l'extension déclarée de LCF-09.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | C1 (triade) ; C2 (renvois à CLOSE-PACKAGE, table de correspondance) ; C3 (forme courte LITE) ; C4 (persistance ITER, résolveur) ; C5 (LCF, F-DIR-018) ; C6 (exemples) ; B5 (cycle SAVOIR avec F-SAV-004) ; C8 et E2 (cycle d'outil unique) |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 ; le build de F-SK-002 tourne sur copie |
| Sources relues | ACTION 37–46, 110, 242–247, 558–562, 655 ; DIRECTION 70, 96–106, 165–179, 245–258, 263–276, 420–435, 605–609, 656–660, 680–686, 716–718, 786–806 ; SAVOIR 38, 541, 906–916 ; BIBLIOTHEQUE 90, 392–411 ; GLOSSAIRE 17 ; QUICKSTART 83–94, 150–156, 310–313 ; skill 16, 35–41 ; `references/flow.md`, `examples.md`, `machine_projection.md` |

## 2. Re-vérification

**Garde E1 sur B01 : témoin 1/1, gardes 0/28.** Les 27 fiches sont **confirmées par relecture**.

**Trois précisions :**
1. **Neuf fiches sont déjà traitées, en tout ou en partie, par une décision antérieure.** E1 les aligne sans rien décider de nouveau (§4.1). En particulier, **F-EX-003** est **absorbée par C6** (T-4 réécrit l'exemple SYSTÈME).
2. **Une recommandation du registre est devenue obsolète.** F-ACT-016 demandait d'appliquer « le noyau de clôture LITE (4 éléments de DAILY) ». Depuis C2, cette colonne de DAILY est supprimée, et C3 a défini la forme courte LITE comme le paquet LITE de CLOSE-PACKAGE. **E1 suit C2 et C3, pas la recommandation d'origine.** L'écart est déclaré.
3. **Constat de coordination.** Le point 4 de l'« entrée prioritaire » de DIRECTION (≈ 800) reprend la formulation corrigée en C5 pour RUN-PRIORITY : « …avant de développer les bénéfices, la navigation ou le polish », **sans l'exception** « sauf si la navigation est l'objet de preuve ». C'est la famille de F-DIR-018 ; même correction, et **LCF-09 étendue à cette ligne**.

## 3. Les sept questions du §21 (lot)

| Question | Réponse pour le lot |
|---|---|
| Change une décision, une exécution ? | Oui, localement : une route mal chargée, un statut mal nommé, une cardinalité ou une condition mal bornées |
| Défaut réel ? | Oui (relecture ; 27 sur 27) |
| Gain > charge ? | Oui : une proposition ou une cellule par fiche |
| Nouvelle autorité ? | **Non.** Chaque texte cible reprend un propriétaire existant ou une décision de phase 11. Une seule valeur est ajoutée (`SANS-ASSET`), qui nomme un état déjà prévu par ACTION (« absence intentionnelle », fiche d'asset) |
| Testable ? | Garde par fiche ; build sur copie pour F-SK-002 |
| Positif / défensif équilibré ? | Oui : plusieurs corrections **retirent** une obligation implicite (quota d'anti-directions, familles MOBILE hors scope, parcours complet imposé à tout run) |
| Suppression ou fusion ? | **Clarification éditoriale** (lot), **déplacement** (F-DIR-043 requalifiée), **correction d'outil** (F-SK-002) |

## 4. PATCH-DECISION

**Décision : CORRIGER (lot).** Aucun invariant, aucun changement de schéma (la liste est close depuis E2).

### 4.1 Fiches alignées sur une décision antérieure

| Fiche | Texte cible | Décision d'appui |
|---|---|---|
| F-ACT-016 | ACTION 244 : « …arrête le protocole après quatre réponses… **puis clôture avec la forme courte LITE** (`ACTION/CLOSE-PACKAGE`, ligne LITE). » | C2, C3 (écart au registre déclaré) |
| F-DIR-043 | DIRECTION ≈ 796 : « Entrée prioritaire — à lire avant le détail » devient « **Récapitulatif de protection** ». DIRECTION 70 : « l'entrée prioritaire » devient « le récapitulatif de protection ». Point 4 : « …avant les éléments génériques ou décoratifs (bénéfices, navigation, polish), **sauf si la navigation est l'objet de preuve**. » | C5 (F-DIR-018, LCF-09 étendue) ; requalification plutôt que déplacement, qui serait plus lourd |
| F-DIR-045 | DIRECTION 658 et 788 : `limitations` devient `closure.limitations` | C2 (table de correspondance) |
| F-EX-003 | Absorbée par C6 T-4 (NOT-VERIFIED pour le non inspecté ; troncature localisée « consommateur 2 ») | C6 |
| F-GLO-001 | GLOSSAIRE 17 : « La trace structurée **et persistante** d'un run : exigée en `STANDARD`, `DIRECTION`, `SYSTÈME` et pour tout `ITER` sérialisé (voir `ACTION/RUN_CARD`). » | C4 T-8 (toute RUN_CARD sérialisée est persistante) |
| F-MP-001 | `machine_projection.md` : `provenance.artifact_locator` égal à `artifact.locator`, dans le même cycle que la migration du YAML | C6 (YAML versé à la migration) |
| F-QS-001 | QUICKSTART 87 : « Le parcours complet est le suivant ; **chaque mode n'en garde que les étapes de sa route** (`ACTION/RUN-<MODE>`). » QUICKSTART 154 : « `BIBLIOTHEQUE/COMPONENTS` **si un composant change** » | C3 (proportion), C5 (façade bornée) |
| F-SAV-004 | ATLAS 541 : ajouter « `SAVOIR/SYSTEM` pour le jugement du système partagé » (sans l'imposer au composant local) | B5 (même cycle SAVOIR que T-4) |
| F-SK-002, F-QS-004 | Voir §4.3 | C8, E2 (cycle d'outil unique) |

### 4.2 Corrections éditoriales propres au lot

| Fiche | Où | Texte cible |
|---|---|---|
| F-ACT-003 | ACTION 39 | « Pour naviguer dans ACTION : la **route** dit quoi faire ; puis quatre registres, dans cet ordre : **observation**, **interprétation**, **décision**, **persistance**. La preuve réunit observation et interprétation ; elle ne se confond pas avec la décision. » |
| F-ACT-004 | ACTION 110 | « …sont chargés seulement lorsque leurs questions peuvent **changer la décision, la preuve ou la limite** » (critère de SAVOIR) |
| F-ACT-032 | ACTION 560 | « La partition est requise lorsque… ; **licence, glyphes nécessaires et coût de chargement sont vérifiés selon `SAVOIR/TYPE`**. Sinon, le système existant et la raison de sa conservation suffisent. » (« complète » retiré) |
| F-ACT-034 | ACTION 655 | « …Si la provenance ne peut pas être établie, **le verdict reste non accepté**. » Le « ou la limite est explicitement déclarée » est retiré, ce qui aligne le texte sur B2 (INV-B2-7) |
| F-BIB-003 | BIBLIOTHEQUE 392–411 | Avant les familles `MOBILE-*` : « **lorsque le mobile est dans le scope ou qu'un risque responsive est réel** ; sinon `N/A-JUSTIFIED` » |
| F-DIR-005 | DIRECTION 96 | « Légende **commune à DIRECTION et SAVOIR** : les tags `[RECOMMANDÉ]` et `[À ADAPTER]` sont employés dans SAVOIR. » |
| F-DIR-012 | DIRECTION 172–173 | `ANTI-DIRECTIONS: patterns visuels concrets à ne pas reproduire` (nombre retiré, ACTION 903). `STRUCTURAL-TENSION: axe(s) de tension selon BIBLIOTHEQUE (un ou deux, BIBLIOTHEQUE 90)` |
| F-DIR-014 | DIRECTION 253 (DAILY, LITE) | « …reviens à `DIRECTION/START` puis reclassifie vers **`ITER`**, `STANDARD`, `DIRECTION` ou `SYSTÈME`. » |
| F-DIR-015 | DIRECTION 274 (FAST-PATH) | « modifié ou confirmé » devient « **changée, confirmée ou abandonnée** » (triade C1, mot pour mot) |
| F-DIR-025 | DIRECTION 427–433 (routes) | Ligne ajoutée : « `SANS-ASSET` : la retenue porte mieux la relation que tout asset. À déclarer : ce qui porte la promesse à la place et la condition qui ferait revenir sur ce choix. » |
| F-DIR-026 | DIRECTION 432 (`GÉNÉRÉ-DIRIGÉ`) | « …et aucune source autorisée **observée dans le scope, le délai et les droits du run** ne résout mieux le besoin » |
| F-DIR-031 | DIRECTION 607 (ABSOLU 4) | « **Avant toute action qui engage un artefact, une preuve, un état, une diffusion ou une persistance**, déclare… » : l'intake nécessaire au classement reste possible |
| F-DIR-037 | DIRECTION 682 | « Elle n'est activée que si son absence empêcherait de **construire, décider, observer ou tenir une contrainte**. » |
| F-DIR-040 | DIRECTION 718 | « La direction **retenue** ne l'emporte que si… » (« modale », terme unique et non défini, est retiré) |
| F-FLOW-001 | `flow.md` 13–14 | Deux arêtes : `H[Protection de niveau] --> A` (reclassification) ; `I[NOT-VERIFIED] --> J[Owner et prochaine preuve]`. Le texte équivalent (18) dit la même chose |
| F-SAV-001 | SAVOIR 38 | « Charge **typiquement zéro à deux routes ; une route par question active** (CRAFT, TYPE, SOURCE, CONTEXT…). » |
| F-SAV-010 | SAVOIR 915 (règle d'or 6) | « Sur une surface `DIRECTION`, **la spec est toujours requise** ; l'ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée, INV-B4-6). » |

### 4.3 Chemins par distribution (F-SK-002, F-QS-004)

| # | Correction |
|---|---|
| O-1 | **Build** (cycle d'outil unique) : dans la copie **Local**, les chemins `V1/official/` deviennent `official/`, et `skills/design-governance-practice/` devient `skill/`, dans la skill, ses références et QUICKSTART. Le contrôle Local existant (liens) est étendu aux **chemins `.md` cités entre accents graves** |
| T-QS | QUICKSTART 312 : liens explicites vers `references/examples.md`, `references/flow.md` et `references/machine_projection.md` (chemin GitHub, réécrit par O-1 pour Local) |

**Extension déclarée de LCF-09.** La condition porte désormais sur RUN-PRIORITY **et** sur le point 4 du récapitulatif de protection. Le nombre d'entrées LCF ne change pas (21).

## 5. Conditions et sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | Chaque correction entre dans la **passe de son propriétaire**, déjà fixée : ACTION, DIRECTION, SAVOIR, BIBLIOTHEQUE, GLOSSAIRE, QUICKSTART, skill |
| C2 | F-MP-001 dans la migration unique ; O-1 dans le cycle d'outil unique |
| C3 | Aucune phrase ne dépasse l'original de plus d'une proposition, sauf les deux lignes ajoutées (`SANS-ASSET`, arête NOT-VERIFIED) |

**Sortie (phase 13) :**
1. `E1_harnais_non_regression.py` : témoin **1/1**, gardes **28/28**. Harnais A1 à E2 verts.
2. **Relecture** des 27 passages par un lecteur qui ne connaît pas ce rapport : le texte cible est-il compris comme le propriétaire l'entend ?
3. **Export Local** : `validate_all.py` vert dans la distribution Local, et toutes les références citées ouvrables.

## 6. Sortie

- **PATCH-DECISION E1 : CORRIGER (lot de 27 fiches).**
  - 9 alignements sur des décisions antérieures, dont 1 fiche absorbée (F-EX-003) ;
  - 17 corrections éditoriales propres ;
  - 1 correction d'outil (chemins Local) ;
  - 1 coordination (F-DIR-018, LCF-09 étendue).
- Listes inchangées : liste close **92 lignes, 82 actifs** ; LCF **21**.
- **Tous les lots A à E sont décidés.** Reste le lot F (observations, sans patch) et la clôture de la phase 11.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Le lot éditorial coûte peu parce que les décisions de fond ont été prises dans les grappes. Un tiers des fiches ne fait que suivre une décision déjà prise.
- La seule recommandation du registre que je ne suis pas (F-ACT-016) avait été rendue obsolète par C2 et C3 ; l'écart est dit, pas passé sous silence.

**Prochaine unité : 11.23, clôture de la phase 11.** Au programme :
- le lot F (9 observations, sans patch, plus les observations versées en cours de route) ;
- les inventaires finaux (liste close, LCF, schémas, outils, harnais) ;
- l'ordre de la phase 12 ;
- **l'examen de conformité** qui autorise ou non l'entrée en phase 12.
