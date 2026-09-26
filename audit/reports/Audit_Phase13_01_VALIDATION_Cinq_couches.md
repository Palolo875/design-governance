# DG-AUDIT-001 — Phase 13.01 — VALIDATION : cinq couches et couverture des défauts

**Date :** 26 septembre 2026.
**Objet :** B03, version V1.1.0, étiquette `12.06-outils-v1.1.0`, telle que publiée dans `DG_AUDIT_001_B03_package_12-06_V1.1.0.zip`.
**Référence :** B01, en lecture seule ; toutes les exécutions se font sur copies.
**Format :** rapport allégé.

**Fichiers produits :**
- `DG_AUDIT_001_Matrice_13-01_fiche_garde_cas.csv` : une ligne par fiche corrigée (149) ;
- `DG_AUDIT_001_Verifications_13-01.py` : vérifications complémentaires (modes `texte`, `mutations`, `distributions`, `non-regression`) ;
- `DG_AUDIT_001_Journaux_13-01.zip` : sorties brutes des 22 harnais et des vérifications, sur B01 et sur B03.

**Question de l'unité** (plan maître, phase 13) : une validation verte couvre-t-elle **le défaut corrigé**, ou seulement un contrôle voisin ?

## 1. Méthode

1. **Tous les harnais sont relancés, sur B01 et sur B03 :** les 22 harnais et les vérifications X et Y. Chaque ligne de cas est rattachée à sa fiche, par l'identifiant qu'elle cite ou, pour A1 et A2, par la table de leur rapport de décision.
2. **Un défaut est « couvert »** s'il existe sur B03 au moins un **cas négatif à faute unique** qui échoue avec son motif, ou une **garde textuelle**, et que ce cas est rouge sur B01. Un **cas positif** ne compte que s'il corrige un sur-rejet (le défaut était un refus injustifié). Un positif rouge sur B01 pour une simple raison de schéma ne compte pas.
3. **Les fiches sans cas dédié** reçoivent une vérification ciblée : rouge sur B01, verte sur B03, et rouge de nouveau quand le texte correcteur est retiré (mutation).
4. **Les cinq couches :**
   - **texte** : gardes, LCF, relecture ;
   - **contrats** ;
   - **machine** : RUN_CARD, oracles ;
   - **distributions** : build, exports autonomes, versions de Python ;
   - **non-régression** : témoins, conservations, verdicts des fixtures.

**Limite de méthode.** Ce contrôle établit la présence et la sensibilité d'une preuve de **forme**. Il ne dit rien de l'**effet** des corrections sur un run réel : c'est l'objet de 13.02.

## 2. Résultats

### 2.1 Couverture des 149 fiches corrigées (lots A à E)

| Couverture du défaut | Fiches |
|---|---|
| Au moins un cas négatif ou une garde, rouge sur B01 et vert sur B03 | **142** |
| Positif discriminant : sur-rejet corrigé (F-RC-001, cas B2-P3 ; B01 rejetait pour le motif même de la fiche) | 1 |
| Vérification ciblée 13.01 (V-1 à V-4, V-6) | 5 |
| Épreuve machine C4-P3 et V-5 (F-VRC-005, rattachée à C4 par E2 §4.2) | 1 |
| **Sans couverture** | **0** |

Les 11 observations du lot F n'ont pas de patch, et donc rien à valider (11.23 §3).

**Les six fiches sans garde dédiée.** Il s'agissait de corrections décidées sous la forme d'un texte seul, sans garde (B2 T-7, C2 règle de projection, B1 T-2, B1 T-4, B3 T-1) :

| # | Fiche | Vérification | B01 | B03 | Mutation |
|---|---|---|---|---|---|
| V-1 | F-ACT-019 | Snapshot datable (RUN-ID, versions, GENERATED-AT) | rouge | vert | rouge |
| V-2 | F-ACT-028 | Règle « hors projection : trace » | rouge | vert | rouge |
| V-3 | F-DIR-016 | Question de risque dans la traduction de START | rouge | vert | rouge |
| V-4 | F-QS-003 | Fermeture par issue ; archiver un blocage n'exige aucune approbation | rouge | vert | rouge |
| V-5 | F-VRC-005 | Locators relatifs résolus depuis la carte (texte) ; épreuve machine C4-P3 | rouge | vert | rouge |
| V-6 | F-ACT-021 | Colonne « Contrôle machine » ; « un verdict vert ne certifie que… » | rouge | vert | rouge |

**F-ACT-021.** Son seul cas de harnais (B3-P4) était rouge sur B01 à cause de champs de schéma nouveaux, et non à cause du défaut. Ce cas ne compte donc pas comme preuve. C'est V-6 qui porte la preuve.

### 2.2 Les 14 fiches Majeur : dimensions du test de phase 10 et couverture

Chaque dimension **décidée** en phase 11 est couverte. Celles qui ne le sont pas sont exactement celles que les décisions ont classées « forme seule » ou « jugement ». Elles figurent dans la promesse du validateur (réserve 7).

| Fiche | Couvert (cas) | Laissé à la trace ou au jugement, par décision |
|---|---|---|
| F-VCT-001, F-VRC-007 | Schéma `{}`, absent, incomplet, mot-clé hors sous-ensemble, enum retiré (A1-01 à A1-11, X-1 à X-7) ; exemples valides (N-3) | — |
| F-ACT-017 | Résultat obligatoire ; NOT-VERIFIED ou FAIL interdit l'acceptation ; issue alignée sur l'action (B1-03 à B1-06) | Fraîcheur réelle du locator de preuve |
| F-ACT-038 | Exception structurée ; échec observé ; protection échouée ⇒ pas de FAIL-ASSUMED (B1-06 à B1-08) | Catégories exclues (sécurité, dommage grave) ; identité de l'autorisant |
| F-DIR-007 | LITE et ITER refusés sur risque critique (B1-01, B1-02) | « Nouveau flow » et « partagé » : classement humain (START) |
| F-ACT-010, F-ACT-012 | Matrice issue × verdict × statut ; axes (B2-01 à B2-09) | — |
| F-ACT-018 | Capacité disponible et basis attestée (B2-10, B2-11) | Réalité de la capacité déclarée |
| F-ACT-022 | Égalité des versions ; date ISO (B2-12, B2-13) | Changement substantiel, réinspection |
| F-ACT-023 | Réserve structurée, sans placeholder (B2-14, B2-15) | Échéance dépassée, résolution d'une réserve |
| F-ACT-024 | Droits `unknown` ⇒ pas d'ACCEPTED ; champ requis (B2-16, B2-17) | Licence, marque, données personnelles |
| F-ACT-015 | Paquet SYSTÈME, consumers, rollback (B3-01 à B3-03) | Complétude réelle des consumers |
| F-ACT-021 | Contrôle machine par mode, promesse (V-6) | Paquet LITE, ITER, STANDARD : forme seule |
| F-DIR-027 | Type d'ancre, calibration, ancre manquante ⇒ issue (B4-01 à B4-06) | Caractère « frais » d'une ancre |

### 2.3 Les cinq couches

| Couche | Preuves | Résultat |
|---|---|---|
| **Texte** | 21 LCF ; gardes de toutes les grappes ; V-1 à V-6 ; relecture de fin de passe à chaque unité (§22) | LCF 21/21. Toutes les mutations sont rouges : C5 6/6, C6 4/4, D1 2/2, D4 2/2, C4 V-01 à V-04, MV-1 à MV-6 |
| **Contrats** | `validate_contracts` : 20 cas unitaires ; cas C2, C3, C9 et E2-04 à E2-08, E2-14 ; X-4 à X-7 | Tous verts sur B03, rouges sur B01 |
| **Machine** | 25 fixtures avec leur motif ; 76 cas unitaires ; **les 48 invariants nouveaux ont chacun au moins un cas unitaire** ; Y-1 à Y-7 | Tous verts. La sensibilité des oracles est vérifiée par Y |
| **Distributions** | C8 R-1 à R-3 ; E2-01 à E2-03, E2-09 à E2-11 ; D-1 à D-5 | **Les deux zips V1.1.0, extraits seuls, passent `validate_all` sous Python 3.10 (le minimum annoncé) et 3.13.** Membres = manifeste (60 et 56). L'export Local sert `DIRECTION/START/TREE` et ne contient aucun chemin GitHub |
| **Non-régression** | Témoins 40/40 ; conservations B2-P2, B3-P3 et LCF-20 vertes sur B01 et B03 ; N-1 à N-3 | Les 25 fixtures communes ont le **même verdict** sur B01 et B03. L'exemple V1.0.0 est refusé par V1.1.0 sans traceback, comme l'annonce la note de compatibilité |

**Totaux :**
- **harnais :** 300 cas sur 300 verts sur B03 ; 297 sont rouges sur B01, et les 3 autres sont les conservations voulues (B2-P2, B3-P3, LCF-20) ;
- **témoins :** 40/40 ;
- **vérifications complémentaires :** X et Y 14/14 sur B03 (Y-4 à Y-7 ne s'appliquent pas à B01, qui n'a pas le mécanisme visé) ; 13.01 26/26 (V, MV, D, N).

B01 : 218/218, aucun fichier généré.

## 3. Constats

1. **Certain :** chacune des 149 fiches corrigées a une preuve de forme sur B03 qui cible son défaut. Aucune garde n'était déjà verte sur B01, hormis les trois conservations voulues.
2. **Certain :** sur les cas négatifs, B01 est rouge pour une raison qui n'est **pas toujours le défaut** (souvent des champs de schéma inconnus). Ce n'est pas une faiblesse de la preuve B03 : sur B03, chaque cas part d'une base valide et n'injecte qu'**une** faute, avec son motif (règle A2). C'est ce qui établit la couverture. Le rouge sur B01 est un indice, pas la preuve.
3. **Probable :** la couverture de texte (94 fiches) prouve la **présence** d'une formulation, pas qu'elle soit comprise ou appliquée. C'est la limite commune des 16 limites déclarées. Les épreuves de 13.02 visent précisément cet écart.
4. **Nouveau, sans effet sur le verdict des cartes :** la pré-passe de types (E2 O-11) fait que, pour une carte ancienne, le premier diagnostic est désormais un type de schéma (N-2 : `basis[0] : type attendu object`), là où l'on voyait avant un message métier. Les motifs des 25 fixtures sont inchangés. Je le note pour la documentation de migration ; ce n'est pas un défaut.

**Aucun écart de méthode à déclarer.** Aucun harnais n'est modifié dans cette unité. Les vérifications 13.01 sont un artefact d'audit, hors package.

## 4. Suite : 13.02, épreuves d'efficacité

Épreuves prévues par les décisions :
- la mesure M de C7 (homogénéisation) ;
- l'épreuve d'imitation de C6 (un agent reçoit les seuls exemples) ;
- « un run, une revue » de D1 ;
- les épreuves de lecture (budgets de chargement réels) ;
- et, en préalable à la conception des pilotes, F-DIR-044.

**Un point dépend de vous : l'observateur (critères D3).** Il faut une relation « externe » ou « collaborateur non impliqué », quelqu'un qui n'est pas l'auteur des corrections, et un conflit déclaré.
- **Sans observateur :** je conduis les épreuves en **auto-comparaison différée** (sessions séparées, captures et cartes conservées). Chaque résultat porte cette réserve, et aucune épreuve n'est clôturée FULL.
- **Avec observateur :** je prépare le protocole et les supports, et l'observateur rend son avis.
