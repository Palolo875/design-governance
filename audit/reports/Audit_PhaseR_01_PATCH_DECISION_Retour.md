# DG-AUDIT-001 — Retour R.01 — PATCH-DECISION du retour

**Date :** 26 septembre 2026.
**Statut d'audit :** `AUDIT-RETURN` (décision de l'owner en phase 14).
**Objet :** RET-1 à RET-6 et les points du §6 de la phase 14.
**Candidate visée :** B04 = V1.1.1, copie de B03 (V1.1.0, `12.06-outils-v1.1.0`, a6eeca8). B01 et B02 restent intactes.
**Format :** rapport allégé.

**Délégation.** L'owner a répondu « À toi le choix » aux trois questions :
- l'option de RET-2 ;
- les points du §6, liste 1/2 ;
- les points du §6, liste 2/2.

Les choix ci-dessous sont donc les miens. Chacun est motivé et peut être rouvert par l'owner avant R.02.

**Fichiers produits :**
- `DG_AUDIT_001_Patch_R01.py` : les textes cibles **exacts**, sous forme exécutable. Il contient 36 entrées P-01 à P-36 ; chaque entrée remplace une seule occurrence, sinon rien n'est écrit. Modes `--verifier` et `--inverse`.
- `R_harnais_non_regression.py` : le harnais R. Il compte 1 témoin et 30 cas.
- `DG_AUDIT_001_R01_maquette.diff` : le diff obtenu sur une **copie jetable** de B03. C'est un essai de faisabilité, pas l'application (voir §5).
- `DG_AUDIT_001_Journaux_R01.zip` : les sorties brutes.

## 1. Choix faits sur délégation

| Question | Choix | Raison |
|---|---|---|
| RET-2 : portée de B1b | **Étendre le texte.** B1b est requis pour toute surface `DIRECTION` qui accepte avec V en `PASS` ou `PASS-WITH-RESERVATION`. La machine ne change pas. | Le validateur applique déjà la décision B3 (INV-B3-3), avec ses cas et ses fixtures. Un motif « hors scope » ajouterait une valeur machine et rouvrirait une décision close. L'extension ne change qu'un texte |
| Points du §6 | **Retenus :** R-08, la légende, GLOSSAIRE × B1, R-12, R-13, R-14, QUICKSTART §6 et l'imitation | Même mécanisme que RET-1 à RET-6 : un texte corrigé et une condition de façade. Le coût est faible |
| Points du §6 | **Non retenus :** mineurs R-16 à R-32 ; tensions R-04, R-05, R-06, R-09, R-11, R-15 | Ces points sont non vérifiés un par un, ou relèvent de l'interprétation de textes décidés. Ils restent transmis (§7) |

**Sens des deux arbitrages texte contre machine.** Dans les deux cas, j'aligne le **texte** sur l'invariant décidé et outillé. Je ne durcis pas la machine :
- **GLOSSAIRE × B1.** B1 et le validateur admettent `ACCEPTED-WITH-RESERVATION` quand une protection critique reste `NOT-VERIFIED`. Le GLOSSAIRE, qui est une façade, s'aligne sur eux.
- **R-12.** Des droits `unknown` interdisent `ACCEPTED`, mais une réserve reste possible (B2, INV-B2-10). ACTION s'aligne sur cette règle et précise que la diffusion attend la clearance.

Si l'owner préfère le durcissement (pas d'acceptation du tout dans ces deux cas), il faut une décision nouvelle, qui touche aux invariants B1 et B2 et à leurs cas. Ce n'est pas un retour peu coûteux.

## 2. Décisions

Les textes exacts sont ceux des entrées P-xx de `DG_AUDIT_001_Patch_R01.py`.

| Point | Défaut vérifié (phase 13.02) | Décision | Entrées | Garde |
|---|---|---|---|---|
| **RET-1** (R-01) | ACTION l. 295 et GLOSSAIRE l. 38 : `N/A-JUSTIFIED` si une conséquence est « obtenue ou attendue » | Les deux textes renvoient à la triade d'`ACTION/STATUS` : conséquence non applicable ⇒ `N/A-JUSTIFIED` ; conséquence attendue non observée ⇒ `NOT-OBSERVED`, qui interdit `ACCEPTED`. Même alignement pour `CHANGE` dans la réponse visible (ACTION l. 45) et pour les paquets de clôture (voir R-14) | P-01 à P-03 ; P-24 à P-27 | LCF-22 |
| **RET-2** (R-02) | La portée écrite de B1b est plus étroite que `check_b1b` | Portée étendue dans `ACTION/GATE-B — B1b` et dans DIRECTION l. 241 ; le déclencheur en cours de run reste inchangé | P-04, P-05 | LCF-23 ; R-29 (conservation machine) |
| **RET-3** (R-03) | QUICKSTART 45 et skill 119 : « deux anti-directions, une tension » | Plus aucun nombre ; renvoi à `BIBLIOTHEQUE/TENSION` pour le nombre d'axes | P-06, P-07 | LCF-24 |
| **RET-4** (R-07) | Table de charge de la skill : « gates B/C » non chargés en LITE et ITER | Charger `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque, comme `ACTION/PRECONDITION` ; Gate C en ITER seulement si le craft change. La carte d'ACTION (ligne ITER) reçoit la même précision | P-08 à P-10 | LCF-25 |
| **RET-5** (R-10) | `machine_projection.md` : `NOT-OBSERVED` listé pour les axes ; « quatre champs » de `profile_decision` (le schéma en a 5) | Axes : les cinq valeurs du schéma ; `NOT-OBSERVED` réservé à `decision_change.outcome`. `profile_decision` : cinq champs, nommés | P-11, P-12 | LCF-26, qui lit le schéma |
| **RET-6** | « Façades alignées sur leurs propriétaires » (CHANGELOG, section V1.1.0, et RELEASE_NOTES) | Phrase bornée : la cohérence opposable se limite à la liste close des conditions de façade ; une divergence hors de cette liste n'est pas détectée. V1.1.0 n'étant pas publiée, sa section est corrigée ; l'erratum est cité dans la section V1.1.1 | P-13, P-14 | LCF-27 |
| **R-08** | La table de correspondance attribue à VISUAL_TARGET « premier objet, périmètre, contrainte » | La ligne est scindée : VISUAL_TARGET garde thèse et anti-direction ; premier objet, contrainte et périmètre sont rattachés à leur vraie source (FIRST-OBJECT, « Qualifier la direction », `SCOPE`). « Opération dominante » devient le nom exact du champ | P-15, P-16 | LCF-28 |
| **Légende** (F-DIR-005) | « `[RECOMMANDÉ]` employé dans SAVOIR » est faux | La légende commune ne couvre que les tags partagés (`[REQUIS PAR LE MODULE]`, `[À ADAPTER]`, `[VEILLE]`) ; SAVOIR tient sa propre table ; `[RECOMMANDÉ]` n'y est pas employé. E1-07 reste vert | P-29 | LCF-29 |
| **GLOSSAIRE × B1** | « Un risque critique non vérifié n'est pas éligible » (GLOSSAIRE) contre B1 et la machine (« la réserve reste possible ») | Voir §1. Une protection `NOT-VERIFIED` exclut `ACCEPTED`, pas la réserve ; une protection `FAIL` exclut tout verdict accepté | P-30 | LCF-35 |
| **R-12** | Droits `unknown` : ACTION l. 666 parle de RETURNED ou ESCALATED, la machine admet `ACCEPTED-WITH-RESERVATION` | Voir §1. ACTION précise la réserve attendue (scope = droits, sortie = clearance), la diffusion après clearance, et ce que la machine contrôle | P-17 | LCF-32 ; R-30 (conservation machine) |
| **R-13** | Ressource technique : sept champs (ACTION) contre une autre liste (SAVOIR 782) | Une seule liste, celle d'`ACTION/POLICIES` ; SAVOIR y renvoie et ajoute seulement les claims applicables | P-18 | LCF-33 |
| **R-14** | « Sortie définie une seule fois par CLOSE-PACKAGE », alors que chaque RUN-* garde sa propre liste | Chaque bloc RUN-* renvoie au paquet de son mode. Les éléments propres aux blocs RUN-* sont **fusionnés** dans CLOSE-PACKAGE (diff en LITE, preuve du risque en ITER, owner et assets en DIRECTION, réserves en SYSTÈME). Aucun élément n'est perdu | P-19 à P-28 | LCF-34 |
| **QUICKSTART §6** (D1 T-6) | La projection perd la colonne « Retour si » : le §6 trouve 1 lacune là où FIRST-OBJECT en trouve 6 | La colonne « Retour si… » est recopiée à l'identique, avec une phrase de renvoi | P-31 | LCF-30 |
| **Imitation** (C6) | Imitation 0/2 : les exemples enseignent la trace, pas la sérialisation | En tête des exemples, un encadré « Trace, pas sérialisation » renvoie à `schemas/run_card.example.json`, à `machine_projection.md`, à la table d'`ACTION/RUN_CARD` et à `validate_run_card.py` | P-32 | LCF-31 |

**Liste close des conditions de façade.** Elle passe de 21 à 35 entrées (LCF-22 à LCF-35), ajoutées à `validate_reading_map.py` (entrées P-33 à P-36). Le docstring du validateur l'exige déjà : « une entrée n'entre que par une PATCH-DECISION, avec sa mutation rouge ». Chaque nouvelle condition cite son propriétaire et son point de retour.

## 3. Gardes et résultats (sur copies)

| Racine | Témoin | Cas R-01 à R-14 (conditions) | Cas R-15 à R-28 (LCF présente et rouge sous mutation) | R-29, R-30 (conservations machine) |
|---|---|---|---|---|
| **B03 = V1.1.0** | 1/1 | **0/14** : tous rouges | **0/14** : tous rouges | 2/2 |
| **Maquette** (B03 + patch, copie jetable) | 1/1 | 14/14 | 14/14 : chaque inversion d'entrée rend le validateur rouge avec l'identifiant visé | 2/2 |

Sur la maquette :
- `validate_all` : FULL VALIDATION PASSED (build GitHub et Local, reproductibilité) ;
- **22 harnais : 300/300, témoins 40/40**, aucune alerte du suivi contre l'instantané 12.06 (empreintes inchangées) ;
- B01 : 218/218 ;
- B03 : arbre de travail propre, aucun fichier modifié.

**Certain.** Chaque point retenu a une garde rouge sur V1.1.0 et verte après le patch. Le patch ne casse aucun des 300 cas.
**Probable.** Les conditions prouvent la **forme** des textes, pas leur effet sur un lecteur (même limite que les 21 premières conditions).
**Hypothèse.** L'encadré « Trace, pas sérialisation » améliorera l'imitation. C'est à mesurer en R.02, sans valeur de sortie.

## 4. Ce que R.01 ne change pas

- **Machine :** aucun invariant, aucun schéma, aucune fixture. R-29 et R-30 le vérifient.
- **Harnais :** les 22 harnais sont inchangés, sans rectification.
- **Suivi :** le suivi reste à 22 harnais et 300 cas. Le harnais R est **nouveau et séparé** ; il se lance seul. Il importe `DG_AUDIT_001_Patch_R01.py` pour reprendre le code des conditions ; c'est une dépendance déclarée, et les deux fichiers vont ensemble.
- **Version :** aucun changement ici. La version V1.1.1, la section CHANGELOG V1.1.1 et les notes de version sont écrites en R.02 (§5).

## 5. Procédure de R.02 (application sur B04 = V1.1.1)

1. **Ouvrir B04.** Copier B03 à `12.06-outils-v1.1.0` dans un nouveau dépôt externe, étiquette `R.02-B04-ouverture`. Vérifier B01 (218/218).
2. **Appliquer le patch.** Lancer `DG_AUDIT_001_Patch_R01.py --verifier`, puis l'appliquer. Étiquette `R.02-patch`.
3. **Écrire la version V1.1.1** : manifeste, titres, README (racine et official), QUICKSTART, README Local du build, RELEASE_NOTES (« Changements depuis V1.0.0 », où V1.1.1 remplace V1.1.0), et une section CHANGELOG « V1.1.1 — Retour d'audit ». Cette section contient :
   - la triade alignée ;
   - la portée de B1b écrite ;
   - les façades corrigées (Creative Boot, charge LITE/ITER, projection machine, §6, légende, glossaire) ;
   - la liste close portée à 35 conditions ;
   - l'erratum de la phrase V1.1.0 ;
   - l'efficacité toujours `NOT-VERIFIED`.

   Étiquette `R.02-version-v1.1.1`.
4. **Relancer :**
   - les 22 harnais (300/300 et 40/40 attendus ; aucune rectification prévue) ;
   - le harnais R (31/31 attendu) ;
   - les vérifications 13.01 (texte, mutations, distributions sous Python 3.10 et 3.13, non-régression B01/B03 → B04) ;
   - les 38 épreuves déterministes de 13.02.
5. **Revue bornée du diff V1.1.0 → V1.1.1.** La condition de sortie est « aucune contradiction bloquante ». Les contradictions nouvelles sont vérifiées une par une.
6. **Rejouer l'imitation**, avec les exemples et les fichiers qu'ils désignent. Le résultat est consigné sans valeur de sortie : c'est une auto-comparaison, sans observateur.
7. **Livrer :**
   - zips GitHub et Local ;
   - md compilé ;
   - plan maître et archive de transfert à jour ;
   - l'owner réévalue le statut. L'hypothèse est `AUDIT-PASS-WITH-RESERVATION`, puisque les réserves §7 de la phase 14 subsistent.

## 6. Écarts de méthode déclarés

1. **Essai sur maquette dans une unité de décision.** Les textes ont été appliqués sur une copie jetable de B03 pour prouver qu'ils sont applicables et que les gardes passent au vert. Aucune candidate n'est créée ; B04 sera ouverte en R.02.
   *Motif :* une PATCH-DECISION dont les gardes n'ont jamais été vues vertes risquait un aller-retour en R.02.
2. **Harnais hors suivi.** Le harnais R n'entre pas dans `DG_AUDIT_001_Suivi_harnais.py`, pour ne pas modifier l'outil de pilotage ni la référence 300/300. Il est rapporté à part.
3. **Choix pris sur délégation**, déclarés au §1.

## 7. Points transmis, non traités par le retour

- **Mineurs R-16 à R-32** de la revue bornée 13.02 : non vérifiés un par un.
- **Tensions R-04, R-05, R-06, R-09, R-11, R-15** : issues de textes décidés, en partie affaire d'interprétation.
- **Réserves 1 à 9 de la phase 14 §7**, inchangées :
  - efficacité `NOT-VERIFIED` ;
  - run CI hébergé ;
  - environ 14 invariants sans cas négatif ;
  - 16 limites déclarées ;
  - promesse du validateur ;
  - F-DIR-044 ;
  - coût d'un run ;
  - placeholders dans les champs libres ;
  - publication (qui passe à V1.1.1).

**Prochaine unité :** R.02, application sur B04 = V1.1.1.
