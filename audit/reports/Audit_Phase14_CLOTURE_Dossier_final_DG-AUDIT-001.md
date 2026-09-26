# DG-AUDIT-001 — Phase 14 — Dossier de clôture

**Date :** 26 septembre 2026.
**Statut d'audit décidé par l'owner : `AUDIT-RETURN`.**

> **Mise à jour du 26-09-2026 :** après le retour R.01 à R.03 (V1.1.1), le statut final décidé par l'owner est **`AUDIT-PASS-WITH-RESERVATION`**. Voir `Audit_Cloture_Finale_DG-AUDIT-001.md`. Le présent dossier reste la référence pour les phases 0 à 14.

Ce dossier rassemble ce qui permet de retrouver chaque élément de l'audit : cible, sources, owner, baseline, couverture, résistances, constats, décisions, validations, réserves, prochaine preuve et condition de sortie. Il ne contient **aucun verdict global** sur la qualité du système : le statut `AUDIT-RETURN` qualifie l'état de l'audit, pas la valeur du cadre.

## 1. Identité de l'audit

| Élément | Valeur |
|---|---|
| Audit | `DG-AUDIT-001`, profil `DEEP`, protocole maître d'audit v2.0 (SHA-256 `990fc86f…0dd`) |
| Cible | Design Governance V1 : cinq sources normatives, façades, skill, schémas, validateurs, build, distributions |
| Owner | Junior (Kamel), propriétaire du corpus et décideur de chaque arbitrage |
| Auditeur | Claude, observateur unique non humain, qui est aussi l'**auteur des corrections** (conflit déclaré) |
| Baseline | **B01** = V1.0.0 (système compilé SHA-256 `016e6002…355d` ; `SHA256SUMS.txt` 218/218, vérifié à chaque unité) |
| Candidates | B02 = V1.0.1, gelée et non utilisée. **B03 = V1.1.0**, étiquette `12.06-outils-v1.1.0`, commit `a6eeca8` |
| Livrables de la version | `Design_Governance_V1.1.0_GITHUB.zip` (60 fichiers) et `Design_Governance_V1.1.0_LOCAL.zip` (56 fichiers), **non publiés** |

## 2. Parcours de la campagne

| Phases | Ce qui a été établi |
|---|---|
| 0 à 2 | Cadrage, baseline B01, lecture complète des 60 sources et des deux distributions |
| 3 à 5 | Rôles et propriétaires ; diagnostics de contrat (4.01 à 4.09) ; architecture d'information (six parcours, 60 chemins, six axes) |
| 6 à 8 | Capacité positive (premier objet, pilotes, 6.02b sur rendu) ; boucles et reclassement ; 12 perspectives et 5 rôles |
| 9 | **Résistance : 20/20 scénarios**, rejeux machine et trois lots de pilotes (9.06 direction, 9.07 opérationnel, 9.08 micro-run). **0/20 FULL d'efficacité**, efficacité escaladée vers des pilotes réels |
| 10 | **158 fiches** consolidées (14 Majeur, 87 Significatif, 48 Mineur, 9 Observation) |
| 11 | **22 PATCH-DECISION** : A1, A2, B1 à B5, C1 à C9, D1 à D4, E1, E2 (lots A à E : CORRIGER ; lot F : 11 observations sans patch). Listes closes : 92 invariants (82 actifs), 21 conditions de façade |
| 12 | Patch appliqué sur B03, en 9 unités (12.00 à 12.07). Cas verts de la trajectoire : 3 → **300/300** ; témoins 40/40 ; rectifications de harnais R-6 à R-15, toutes déclarées |
| 13 | Validation à cinq couches (13.01) et épreuves d'efficacité en auto-comparaison différée (13.02) |

## 3. Couverture et validations

**Validation de forme (certain)**
- **Fiches corrigées :** 149/149 ont une preuve de forme ciblée sur B03, rouge sur B01. La matrice est dans `DG_AUDIT_001_Matrice_13-01_fiche_garde_cas.csv`.
- **Invariants :** 48/48 invariants nouveaux ont leur cas unitaire.
- **Machine :** 25 fixtures et 76 cas RUN_CARD ; 20 cas de contrats.
- **Texte :** 21 conditions de façade sur 21 ; toutes les mutations sont au rouge.
- **Distributions :** autonomes sous Python 3.10 et 3.13 ; membres des archives = manifeste.
- **Non-régression :** les 25 fixtures communes ont le même verdict sur B01 et B03.

**Épreuves (13.02)**
- **Déterministes (certain) :** 38/38. Les rejeux 9.08, 4.04, 7.02, 9.02, 9.03 et 9.06 sont refusés pour leur motif, et les limites déclarées se comportent comme prévu.
- **Jugement (probable, auto-comparaison, aucune clôture FULL) :**
  - lecture : 5 épreuves tenues, 5 partielles ;
  - production : « un run, une revue » tenue ; imitation **0/2** ; « un exemple, deux façades » non tenue ; mesure M non concluante.
- **Revue bornée du diff :** 32 contradictions relevées, dont **2 bloquantes**. J'en ai vérifié 9.

## 4. Pourquoi `AUDIT-RETURN`

La conformité de forme est complète. Mais deux contradictions bloquantes, vérifiées, restent dans V1.1.0. Chacune rend une règle centrale du système inapplicable honnêtement :
- **R-01 :** la table RUN_CARD d'ACTION et le GLOSSAIRE autorisent `N/A-JUSTIFIED` quand une conséquence attendue n'est pas obtenue. La règle de la triade (`NOT-OBSERVED`, qui interdit `ACCEPTED`) est donc contournable depuis le canon lui-même.
- **R-02 :** le texte dit que B1b « hors de son scope ne s'applique pas ». La machine l'exige pourtant pour toute DIRECTION acceptée avec V en PASS, et n'admet aucun motif « hors scope ». Un run honnête ne peut pas être sérialisé.

S'y ajoutent des façades encore divergentes, que la liste close de conditions ne couvre pas. Elles rendent inexacte la phrase du CHANGELOG « façades alignées sur leurs propriétaires ».

Ces points sont **peu coûteux à corriger** et relèvent du même mécanisme que la phase 12. L'owner a donc choisi de faire un retour avant de clôturer, plutôt que de clôturer avec ces points en réserve.

## 5. Liste de retour (obligatoire) et conditions de sortie

| # | Point | Source vérifiée | Condition de sortie |
|---|---|---|---|
| RET-1 | **R-01**, triade contournable | ACTION l. 295 (table RUN_CARD) ; GLOSSAIRE l. 38 | Les deux textes renvoient à la triade d'`ACTION/STATUS` : conséquence attendue absente ⇒ `NOT-OBSERVED`. Une nouvelle condition de façade (ou une garde) est rouge sur V1.1.0 et verte après |
| RET-2 | **R-02**, portée de B1b | ACTION l. 786 à 800 ; `validate_run_card.py` (`check_b1b`) ; décision B3 (INV-B3-3) | Une PATCH-DECISION aligne le texte et la machine : **soit** un motif admis « hors scope » (avec la condition du scope), **soit** l'extension écrite du scope textuel. Un cas unitaire est rouge avant et vert après |
| RET-3 | **R-03**, quotas du Creative Boot dans les façades | QUICKSTART l. 45 ; skill l. 119 | Plus de nombre fixe d'anti-directions ni de tension ; une condition LCF rend le point opposable |
| RET-4 | **R-07**, gates B « non chargés par défaut » en LITE et ITER | skill, table de charge | Même chargement que la carte d'ACTION (Gate B du risque dominant) |
| RET-5 | **R-10**, `machine_projection.md` : `NOT-OBSERVED` listé pour les axes ; « quatre champs » de `profile_decision` | `machine_projection.md` l. 120 et 122 | Valeurs des axes et nombre de champs identiques au schéma |
| RET-6 | Phrase du CHANGELOG et des notes de version V1.1.0 : « façades alignées » | CHANGELOG, section V1.1.0 ; RELEASE_NOTES | Phrase bornée à ce que les 21 conditions contrôlent, ou rendue vraie par RET-3 à RET-5 |

**Procédure du retour, dans le cadre du protocole :**
1. Une **PATCH-DECISION** compacte couvre RET-1 à RET-6, en une seule unité.
2. Le patch est appliqué sur une candidate **B04 = V1.1.1** : copie de B03, B01 et B02 intactes, règles de la phase 12.
3. On relance : harnais (300/300 attendus), vérifications 13.01, épreuves déterministes 13.02, et **revue bornée sur le diff V1.1.0 → V1.1.1**.

**Condition de sortie du retour :**
- RET-1 à RET-6 sont verts, chacun avec une preuve rouge sur V1.1.0 ;
- aucune régression ;
- la revue bornée ne trouve **aucune contradiction bloquante** ;
- le statut d'audit est alors réévalué par l'owner.

**Hypothèse :** le statut atteignable est `AUDIT-PASS-WITH-RESERVATION`, puisque les réserves d'efficacité du §6 subsistent.

## 6. Points à décider au début du retour (recommandés, non obligatoires)

Ce sont des constats vérifiés. Leur correction est souhaitable, mais l'owner décide s'ils entrent dans le cycle de retour :

| Point | Constat | Origine |
|---|---|---|
| R-08 | La table de correspondance attribue à VISUAL_TARGET « premier objet, périmètre, contrainte » | Texte même de la décision C2 T-1 |
| R-12 | Droits `unknown` : `ACCEPTED-WITH-RESERVATION` passe, alors qu'ACTION 666 prévoit RETURNED ou ESCALATED | Décision B2 face à un texte de B01 |
| R-13 | Nouvelle dépendance : sept champs (ACTION) contre une autre liste (SAVOIR 782) | Application partielle de D3 T-6 |
| R-14 | « Sortie définie une seule fois par CLOSE-PACKAGE », alors que les blocs RUN-* gardent leur propre sortie | C4 T-2 |
| Légende | « Tags `[RECOMMANDÉ]` employés dans SAVOIR » est faux : SAVOIR n'en contient aucun | Décision E1 (F-DIR-005) |
| GLOSSAIRE et B1 | Un risque critique non vérifié est « non éligible » à ACCEPTED-WITH-RESERVATION (GLOSSAIRE), mais admis par ACTION et le validateur | Décisions C6 T-6 et B1 en conflit |
| Imitation 0/2 | Les exemples n'enseignent pas la sérialisation | Choix C6 (exemples en format trace) |
| QUICKSTART §6 | Projection avec perte : il surestime un rendu par rapport à FIRST-OBJECT | Choix D1 T-6 (pas de colonne « Retour si ») |
| Mineurs R-16 à R-32 | Transmis tels quels, non vérifiés un par un | Revue bornée |

## 7. Réserves qui restent après le retour

| # | Réserve | Owner | Prochaine preuve | Condition de sortie |
|---|---|---|---|---|
| 1 | **Efficacité sur des runs réels : `NOT-VERIFIED`.** Aucun observateur indépendant ; mesure M non concluante (N = 3) | Owner | Pilotes réels avec un observateur répondant aux critères D3 (relation externe ou collaborateur non impliqué, conflit déclaré) | Épreuves 13.02 rejouées sous observation indépendante |
| 2 | **Run CI hébergé** du workflow épinglé | Owner | Push de la distribution GitHub ; lien du run | Run vert, avec versions et SHA consignés |
| 3 | Environ 14 invariants existants sans cas négatif | Owner (réserve décidée le 26 septembre) | Décision d'ajout | Cas unitaires ajoutés, ou réserve maintenue |
| 4 | Seize limites déclarées par les grappes : une garde prouve une forme, pas un effet | — | Épreuves sous observateur | Idem réserve 1 |
| 5 | Promesse du validateur : ce que la machine n'atteste pas (observations réelles, jugements, droits, fraîcheur, consumers, baseline, paire équivalente) | Conception assumée | Trace, revue et owner | Permanente, déclarée |
| 6 | F-DIR-044 : la carte d'ACTION sert 321 lignes pour LITE, contre 51 par la route mesurée ; SAVOIR/CRAFT fait 188 lignes | Owner | Mesure sur pilotes | Budget de chargement décidé |
| 7 | Coût observé d'un run DIRECTION : environ 1 300 lignes de règles lues, RUN_CARD d'environ 230 lignes, recouvrements entre vues | Owner | Pilotes réels | Mesure de charge et décision de simplification |
| 8 | Placeholders acceptés dans les champs libres des contrats non visés par E2 | Owner | — | Décision éventuelle |
| 9 | V1.1.0 non publiée | Owner | Publication | Après le retour, en V1.1.1 |

## 8. Où retrouver chaque élément

| Élément | Artefact |
|---|---|
| Point de reprise | `Plan_Maitre_Audit_Design_Governance-1.md` ; archive `DG_AUDIT_001_Transfert_Phase10.zip` |
| Fiches | `DG_AUDIT_001_Phase10_05_REGISTRE_CONSOLIDE_158.csv` |
| Décisions | `Audit_Phase11_01` à `11_23` ; listes closes (invariants, LCF) en CSV |
| Patch | Rapports `Audit_Phase12_*` ; diffs `DG_AUDIT_001_B03_12-*.diff` ; sources `DG_AUDIT_001_B03_package_12-06_V1.1.0.zip` |
| Harnais et suivi | 22 `*_harnais_non_regression.py`, `DG_AUDIT_001_Suivi_harnais.py`, instantanés de 12.00 à 12.06 |
| Validation | `Audit_Phase13_01_*`, matrice CSV, `DG_AUDIT_001_Verifications_13-01.py`, journaux |
| Épreuves | `Audit_Phase13_02_*`, `DG_AUDIT_001_Epreuves_13-02.py`, traces (lecteurs, revue bornée, run DIRECTION, imitation, palettes) |

**Prochaine unité :** R.01, PATCH-DECISION du retour (RET-1 à RET-6, puis les points du §6 que l'owner retient).
