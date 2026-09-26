# DG-AUDIT-001 — Phase 10.03 — FINDINGS : SAVOIR, BIBLIOTHEQUE, CHANGELOG (16 fiches)

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** enchaîner après ACTION (« Oui, enchaîne »).

**Sortie :** 16 fiches avec les 15 champs du §20, dans `DG_AUDIT_001_Phase10_03_FINDINGS_SAVOIR_BIBLIOTHEQUE_CHANGELOG.csv` :
- SAVOIR : 10 fiches ;
- BIBLIOTHEQUE : 5 fiches ;
- CHANGELOG : 1 fiche.

**Ce que ce rapport n'est pas :** ni une décision de correction, ni un patch, ni un verdict global.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Plan | Plan maître, état 10.02 |
| Empreintes | B01 `016e6002…` et protocole `990fc86f…` conformes |
| Checkpoints | SAVOIR (120 lignes) et BIBLIOTHEQUE (88 lignes) relus en entier. CHANGELOG n'a pas de checkpoint propre : son rapport unique fait foi, recoupé par le checkpoint « cinq propriétaires » |
| Sources de niveau 5 | Les 16 sections de définition, extraites des rapports SAVOIR 01/04/07/08/09/10/11/12/15, BIB 03/04/06/11/13 et CHANGELOG 01, relues en entier |
| Dispositions ultérieures | Toutes les mentions en 3.01–9.05 (ROLE_MAP, 4.01–4.03, 5.02–5.03, 6.01, 8.01–8.02, 9.01, 9.03–9.05) |
| Preuves d'objet | 6.02b, 9.06, 9.07, 9.08 |

**Différence de forme avec 10.02.** Les fiches de ces trois propriétaires n'ont pas un gabarit commun (« Effet possible », « Constat », « Contre-exemple »…). Les champs du CSV sont donc **condensés fidèlement**, et non repris mot pour mot. Le texte intégral reste dans les rapports d'origine.

## 2. Méthode

Même grille et même règle d'impact réel qu'en 10.01 et 10.02.

Ces trois propriétaires ne portent ni preuve, ni verdict, ni projection machine (sauf F-SAV-005) : la règle de discrimination « Majeur » d'ACTION (acceptation interdite admise par la machine) ne s'applique donc presque pas ici.

Pour SAVOIR, propriétaire du **jugement**, j'ai ajouté un critère équivalent : une règle qui va contre la **promesse centrale** de DG (une sortie située, non générique) pèse plus lourd qu'une règle locale de forme.

## 3. Résultat

| Gravité | Nombre | IDs |
|---|---:|---|
| Bloquant | 0 | — |
| Majeur | 0 | — |
| **Significatif** | **11** | SAV-002, 003, 005, 006, 007, 009 ; BIB-001, 002, 004, 005 ; CHG-001 |
| **Mineur** | **4** | SAV-001, SAV-004, SAV-010, BIB-003 |
| **Observation** | **1** | SAV-008 |

**Décisions :**
- 11 fiches `RETENU → phase 11` ;
- 4 fiches `RETENU (mineur) → lot éditorial` ;
- 1 fiche `OBSERVATION` ;
- aucune fusion.

## 4. Écarts avec la phase 2 (5 sur 16)

Toutes les fiches étaient « Significatif à éprouver », sauf F-BIB-005, laissée « à calibrer ». Cinq sont abaissées :

| ID | → | Raison |
|---|---|---|
| F-SAV-001 | **Mineur** | La même section exige déjà une route de plus « lorsqu'elle change question, preuve ou limite » ; le tableau n'écrit pas « maximum ». Correction : « typiquement », une route par question active |
| F-SAV-004 | **Mineur** | Une cellule d'index omet une route que ROUTING (78) et ACTION/ROUTING (885) donnent correctement. Ajout d'un renvoi |
| F-SAV-010 | **Mineur** | La lecture logique de la règle 6 est correcte : le « contrat » (ACTION 475) exige la spec en DIRECTION, et le résumé se déclare subordonné. Même logique que F-DIR-031 et F-DIR-043 |
| F-BIB-003 | **Mineur** | Aucun run hors web ; la correction est une clause de condition. Voir la rectification du §6 |
| F-SAV-008 | **Observation** | Aucun run avec motion ou scène spatiale (tous les pilotes sont web et statiques). La fiche demande elle-même de ne qualifier de défaut que la divergence qui produit une mauvaise décision. Même traitement que F-DIR-004 (médiums) |

F-BIB-005 est **fixée à Significatif**, avec un appui d'objet (§5).

## 5. Ce que les preuves d'objet ont changé

**F-SAV-002 (« neutres + accent », CFT-05 363) : la fiche la mieux appuyée de ce lot.** Trois observations dans trois unités :

| Unité | Observation |
|---|---|
| 6.02b | Le pilote A converge vers « sombre + serif + doré » |
| 9.06 | A applique exactement la structure de 363 et aboutit au canon premium que CFT-00 (228) dit ne pas être le premium |
| 9.08 | Le run **avec** DG et la baseline **sans** DG choisissent tous deux des neutres et un accent vert profond |

**Ce que la baseline change à la lecture.** La pente vers ce canon vient du modèle, pas de DG. Mais la ligne 363 la **codifie sous un tag requis** au lieu de la contrer. REUSE-CHALLENGE, lui, ne se déclenche que lorsqu'un antécédent est nommé (9.06). DG n'a donc aucun mécanisme actif contre la convergence **implicite**. C'est cohérent avec le résultat de 9.08 : aucun gain visible de présence ni de désirabilité.

**Pourquoi Significatif et non Majeur.** Chaque observation est N = 1, faite par un observateur unique, et ne porte que sur un axe (la palette ; typographie et mise en page ont varié). F-SAV-002 est la **première candidate au relèvement** : si un pilote avec observateur indépendant confirme la convergence (N ≥ 3), elle devrait passer Majeur, car elle touche la promesse centrale.

**F-BIB-005 et F-SAV-006 (ablation).** En 9.06, retirer le relief du pilote A vide la scène : la promesse « par strates » n'est plus perceptible. La réponse pertinente de DG est le **fallback déclaré** de VISUAL_TARGET, pas une refonte de structure (ce qu'ordonnerait GATE 707), ni la conclusion « pas de profil » (STYLE 632). L'ablation a révélé une **dépendance** ; elle n'a pas prouvé une absence de choix. En 6.02b et 9.06, la spécificité des pilotes tenait à la relation de l'objet, pas à une signature spatiale. Les deux fiches restent Significatif, avec une correction commune.

**F-SAV-003 (comparaison indépendante prise pour calibration).** En 9.06, la seule ancre rencontrée (convention non revérifiée) a été tenue comme hypothèse, et la calibration est restée `NOT-VERIFIED` : lecture correcte, N = 1. Le cas discriminant (identité générée seule + reviewer) n'a pas été rejoué. La fiche reste Significatif, dans la grappe Ancres de priorité 1 avec F-DIR-027.

**F-SAV-007 et F-BIB-004 (composant partagé).**
- En 9.03, le contrat de classement **résiste** : START est l'unique propriétaire, et la distinction entre objet direct et effet induit tient. F-SAV-007 se réduit donc à un verbe (« Reclassifie » → « signale à START »). Je la garde Significatif, parce qu'elle porte sur la décision la plus lourde (le mode) et que la machine ne la rattrape pas (4.02 N2).
- F-BIB-004 est confirmée trois fois : 4.02, 4.03 et 9.03 (« BRAND_GRAMMAR ne résout pas ce cas »).

**F-CHG-001 (cycle de vie).** Le rejeu 9.05 confirme le trou dans le contrat. Toutes les routes actuelles sont des routes seed : la **première** dépréciation, quelle qu'elle soit, le rencontrera.

## 6. Rectification : un rattachement trop large de ma part

En 9.07, j'ai écrit que l'observation O8 (liste masquée entre 650 et 980 px) « rejoint F-BIB-003 ». **C'est inexact.**
- F-BIB-003 porte sur des champs MOBILE exigés **hors** de leur médium (print, borne).
- O8 montre qu'une intention CSS ne prouve pas le rendu mobile : c'est une question de preuve ACTION (Gate A, fraîcheur), et le risque mobile y était **réel**.

O8 n'appuie donc pas F-BIB-003. Le CSV le dit ; le rapport 9.07 n'est pas réécrit et reste l'historique. C'est la deuxième correction d'attribution de la campagne, après F-DIR-044.

## 7. Déduplication et grappes transversales

Aucune fusion : chaque paire garde son propriétaire et son test. Les liens qui orientent la phase 11 :

| Grappe | Fiches de ce lot | Rejoint |
|---|---|---|
| **Ancres** (priorité 1) | SAV-003 | F-DIR-027 (Majeur), F-ACT-037, F-ACT-028 |
| **Composant partagé / SYSTÈME** (priorité 1) | BIB-004, SAV-007, SAV-004 (m) | F-ACT-015 (Majeur), F-ACT-021, F-ACT-011 |
| **Homogénéisation et ablation** (priorité 2, nouvelle) | SAV-002, SAV-006, BIB-005 | REUSE-CHALLENGE (F-DIR) ; question de désirabilité ouverte en 9.08 |
| **Registres et temps** (priorité 2) | SAV-005 | F-ACT-013, F-ACT-030, F-DIR-003 |
| **Proportion** (priorité 2) | BIB-002 | F-ACT-006, F-ACT-002, F-SK-001 (mesure 9.08) |
| **B1b** (priorité 2) | BIB-001 | F-ACT-036 |
| **Cycle de vie** (priorité 3) | CHG-001 | F-DIR-046, F-DIR-002 |
| **Outil** (priorité 3) | SAV-009 | F-ACT-028, F-ACT-024 |
| **Lot éditorial** (priorité 4) | SAV-001, SAV-004, SAV-010, BIB-003 | F-ACT-004 (même critère de chargement que SAV-001) |
| Observation | SAV-008 | F-DIR-038, F-ACT-033 |

**Pourquoi une grappe « Homogénéisation » nouvelle.** C'est la seule grappe de tout le registre qui porte sur la **qualité créative** plutôt que sur la forme, la preuve ou la gouvernance. C'est aussi là que la campagne a trouvé sa limite la plus nette (9.08 : DG améliore la vérité et la robustesse, pas la présence). Elle mérite une place explicite en phase 11, avant les grappes de priorité 3.

## 8. Signal de biais : mise à jour et explication partielle

Sur 10.01, 10.02 et 10.03 réunis :
- **28 abaissements, 0 relèvement** ;
- 101 fiches classées.

Une partie de l'asymétrie est **mécanique**. La phase 2 a presque tout inscrit « Significatif à éprouver » par défaut, sans preuve d'objet. Un relèvement exige une preuve de dommage nouvelle ; or les preuves d'objet de la campagne sont peu nombreuses (N = 1, web seulement, un observateur). Il est plus facile d'établir qu'un risque est atténué dans le texte que de démontrer qu'il se réalise.

Cette explication ne supprime pas le biais possible. Deux garde-fous :
1. chaque abaissement a sa raison écrite ;
2. F-SAV-002 est désignée comme candidate au relèvement, avec une condition vérifiable.

La consolidation 10.05 présentera les 28 abaissements dans une seule table, pour que l'owner puisse les arbitrer en bloc.

## 9. Sortie

- **16/16 fiches classées** avec leurs 15 champs.
- **Registre global : 101/157 classées.** Restent 56 fiches (façades et machine, 10.04).
- Aucun nouvel ID ; une rectification d'attribution (9.07 → F-BIB-003).
- Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- 5 gravités ajustées, avec raison écrite ;
- la seule convergence observée trois fois (F-SAV-002) est isolée comme candidate au relèvement ;
- l'ablation est requalifiée (dépendance → fallback, pas refonte), avec un appui d'objet ;
- une grappe créative est ajoutée à l'ordre de la phase 11 ;
- une attribution erronée est corrigée.

**Prochaine unité : 10.04 façades et machine** (56 fiches, plus la candidate « granularité des locators »). À arbitrer en chemin :
- F-ACT-010 face à F-RC-001 ;
- F-ACT-002 face à F-SK-001 ;
- F-ACT-008 face aux F-FIX.

C'est le plus gros lot. Je propose de le découper en deux passes, pour garder chaque unité relisible :
- **10.04a, façades** (environ 21 fiches) : F-QS, F-RM, F-OM, F-GLO, F-SK, F-RDR, F-FLOW, F-MP, F-ALL, F-EX, F-WF ;
- **10.04b, machine** (environ 35 fiches) : F-VRC, F-BLD, F-VDG, F-FIX, F-VCT, F-VRM, F-DF, F-MAN, F-PC, F-RB, F-RC, F-RRT.

La répartition exacte de F-MP, F-ALL, F-EX et F-WF sera vérifiée à l'ouverture, d'après leurs rapports d'origine.
