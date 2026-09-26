# DG-AUDIT-001 — Phase 10.00 — PRÉ-TRI : 157 fiches → 10 familles de causes et lots de correction

**Date :** 25 septembre 2026. **Baseline :** B01 inchangée. **Auteur de l'unité :** Claude (reprise depuis le transfert `DG_AUDIT_001_Transfert_Claude_9_06`). **Portée :** regroupement provisoire des 157 fiches par cause racine, gravité provisoire selon l'échelle du protocole §20, type de correction selon §21, et proposition de lots. **Ce n'est ni le registre final `FINDINGS`, ni une `PATCH-DECISION`** : aucune correction n'est appliquée, aucun verdict global n'est rendu.

---

## 0. Changement de méthode : explicite et validé

La prochaine unité prévue au plan était **9.06 (scénario 19, surcharge procédurale)**. À la demande de l'utilisateur, la campagne passe maintenant à un pré-tri de phase 10. Ce saut est **volontaire et assumé** ; il ne se fait pas en silence.

**Pourquoi.**
- Les blocs 9.02 à 9.05 n'ont créé **aucun nouvel ID**. D'après le plan maître, le registre est en fait bloqué à 157 depuis la fin de la phase 2 (README racine), soit une trentaine de rapports sans nouvelle fiche. Chaque bloc confirme les mêmes fiches sous un autre angle.
- Le protocole lui-même autorise ce passage :
  - §7.8 : « Si deux étapes successives produisent la même décision sans nouvelle observation, elles peuvent être fusionnées dans l'exécution. »
  - §32, questions 2 et 9 : quelle étape n'a rien appris de nouveau, et l'audit améliore-t-il la cible plus qu'il ne l'alourdit.

**Ce qui ne change pas.**
- Les 14 scénarios de phase 9 non examinés restent **ouverts**, ni clos ni abandonnés. Ils sont suspendus en attendant que le lot 1 montre s'ils apportent encore quelque chose.
- La phase 6.02 reste différée.
- Aucun scénario n'est compté comme `FULL` d'efficacité.

---

## 1. Base de preuve

| Élément | État |
|---|---|
| Empreintes B01 | Recalculées dans cette unité : compilation `016e6002…5f355d`, protocole `990fc86f…dc20610dd`. Conformes. |
| Suite intégrée | `validate_all.py`, lancée sur une copie de travail : `FULL VALIDATION PASSED`, code 0. |
| Fiches **décrites** dans les fichiers transmis | **104/157**. Leur comportement est lisible dans le plan maître et les rapports 5.01–5.04 et 9.01–9.05. Pour certaines fiches ACTION, la description est **indirecte** : le contexte les cite par groupe (par exemple « F-ACT-005/007/012/018/021/022 ») sans énoncé individuel. |
| Fiches **non décrites** | **53/157** : 36 DIRECTION (F-DIR-002, 004, 005, 011–027, 029–042, 045, 046) et 17 ACTION (F-ACT-004, 014, 016, 019, 024, 026, 027, 029–033, 035–039). Leur texte se trouve dans les rapports de phase 2 DIRECTION et ACTION (`Audit_DIRECTION_Phase2_*`, `Audit_ACTION_Phase2_Checkpoint_Consolidation.md`), **absents de l'archive**. Elles sont classées « Z — non triable » plutôt que devinées. |

### Reproductions directes dans cette unité

Toutes les reproductions sont faites sur une copie. La source B01 n'est pas touchée.

| Essai | Résultat observé | Fiche |
|---|---|---|
| `run_card.schema.json` remplacé par `{}` puis `validate_run_card.py` | `RUN_CARD VALIDATION PASSED`, code 0 | F-VRC-007 **confirmée** |
| `domain_frame.schema.json` remplacé par `{}` puis `validate_contracts.py` | `CONTRACT VALIDATION PASSED`, code 0 | F-VCT-001 **confirmée** |
| `read_route.py` sur ACTION/HANDOFF, ACTION/RUN, ACTION/STATUS, ACTION/PRECONDITION, DIRECTION/CREATIVE-BOOT, BIBLIOTHEQUE/DERIVE, SAVOIR/SOURCE, SAVOIR/TOOLS, SAVOIR/STATE | Les 9 échouent : « locator inconnu », code 1. Pourtant, les titres existent dans les propriétaires (exemple : `ACTION.md` ligne 23 pour HANDOFF, ligne 190 pour PRECONDITION). La table ne compte que 24 locators. | F-DIR-028 **confirmée** |
| `read_route.py DIRECTION/START` | 130 lignes de sortie | F-DIR-044 / bloc trop large, **confirmé** |
| `READING_MAP.md` ligne 33 | `ACTION/RUN-DIRECTION` est placé dans la colonne « ajout conditionnel » de la ligne « Direction identitaire » | F-RM-001 **confirmée** |
| `dist/local` reconstruit | Le fichier réel est `official/READING_MAP.md`, mais la skill (ligne 16) cite `V1/official/READING_MAP.md` | F-SK-002 **confirmée** |

**Échelle utilisée.** « Observé » veut dire reproduit ici ou décrit comme reproduit dans les rapports transmis. « Provisoire » veut dire que la gravité n'est pas encore arbitrée par l'owner, qui est l'utilisateur.

---

## 2. Vue d'ensemble

| Famille | Cause racine | Fiches | Gravité provisoire | Coût estimé | Lot |
|---|---|---|---|---|---|
| **A** | Les oracles machine peuvent déclarer PASS sans avoir validé | 18 | **Majeur** | Faible | **1** |
| **D** | Une façade présente comme facultatif ce qui est obligatoire chez le propriétaire | 11 | **Majeur** | Faible | **1** |
| **C** | Accès CLI incomplet ou extrait trop large | 4 | Significatif (F-ACT-001 : Majeur) | Faible | **1** |
| **I** | CI hébergée sur des actions Node 20 dépréciées | 1 | Significatif | Très faible | **1** |
| **E** | RUN_CARD et contrats vérifient la forme, pas le lien avec la réalité | 28 | Significatif (F-DIR-007/F-ACT-017 : Majeur) | Moyen | **2** |
| **F** | Rejet à tort ou exemple incohérent | 6 | Significatif | Faible | **2** |
| **B** | Erreurs brutes (traceback) et reprise d'outillage fragile | 8 | Mineur | Faible | **2** |
| **H** | Ordre et raccords internes de DIRECTION et ACTION | 7 | Significatif | Moyen | **3** |
| **J** | Éditorial mineur | 5 | Mineur | Très faible | **3** |
| **G** | Frontières normatives liées à la capacité créative | 16 | Observation (F-SAV-003, F-BIB-004 : Significatif) | À établir | **Après 6.02** |
| **Z** | Non triable faute de description | 53 | — | — | **Bloqué** |

**Lecture.** Les 104 fiches décrites se ramènent à **10 causes**. Les **lots 1 et 2 (4 + 3 familles, 76 fiches)** relèvent d'un travail d'outillage et de façade : peu cher, testable, sans toucher le fond normatif. Le fond normatif (famille G) ne peut pas être arbitré honnêtement sans rendus réels.

Le détail fiche par fiche se trouve dans `DG_AUDIT_001_Phase10_00_Pretri_157_fiches.csv`.

---

## 3. Familles, une par une

### A — Les oracles peuvent dire PASS sans avoir validé (Majeur, lot 1)

**Fiches :** F-VCT-001/003, F-VRC-001/006/007, F-FIX-001/002/003, F-ALL-001, F-MAN-001/002, F-VDG-001, F-BLD-001/004, F-VRM-001/002/003, F-RRT-001.

**Comportement.**
- Avec un schéma vide ou amputé d'un enum, les validateurs réussissent (reproduit ci-dessus).
- Une fixture négative peut être rejetée pour une autre raison que celle qu'elle est censée tester.
- Des clés JSON en double sont perdues silencieusement.
- Un ZIP peut perdre un fichier (lien symbolique) ou en garder un retiré, avec `FULL PASS`.
- Un manifeste avec doublon ou version divergente passe.

**Pourquoi Majeur et non Bloquant.** Le protocole range la « fausse preuve » en Bloquant. Mais ici, **aucun faux PASS n'a été observé sur l'état B01** : ils n'apparaissent que sur des copies altérées. Le risque réel est une dérive future non détectée, par exemple une édition de schéma qui casse tout sans que la CI le signale. D'où « Majeur » : cela peut faire échouer le système, mais ce n'est pas un défaut actif. **Arbitrage laissé à l'owner.**

**Corrections types (§21 : validateur et test).**
1. Refuser un schéma sans `type`, sans `properties` ni `required`, et vérifier une empreinte ou une liste minimale de clés attendues.
2. Chaque fixture négative déclare son diagnostic attendu ; l'oracle compare le motif, pas seulement le code non nul (F-FIX-003, F-ALL-001).
3. Détecter les clés en double au chargement JSON avec `object_pairs_hook`.
4. Après le build, comparer la liste des membres de chaque ZIP au manifeste ; refuser les liens symboliques et les doublons.
5. Vérifier que le manifeste n'a pas de doublons et que sa version égale celle du CHANGELOG.

**Test de non-régression.** Les mutations déjà décrites dans les rapports (schéma `{}`, enum retiré, lien symbolique, doublon manifeste, fixture sans motif) deviennent des fixtures « méta ». La suite doit **échouer** sur chacune et rester verte sur B01.

**Limite.** Ces corrections protègent l'intégrité de l'outillage. Elles ne disent rien de la qualité des rendus.

### D — Des façades affaiblissent un minimum propriétaire (Majeur, lot 1)

**Fiches :** F-RM-001, F-RM-002, F-OM-001, F-QS-001, F-QS-002, F-QS-004, F-RDR-001, F-SAV-010, F-FLOW-001, F-SK-001, F-ACT-002.

**Comportement.** Des cellules de résumé, lues seules, autorisent moins que le propriétaire :
- RUN-DIRECTION présenté comme facultatif (READING_MAP l.33, alors qu'ACTION 369–377 le requiert) ;
- accessibilité N/A déclarative ;
- gate et migration en « renfort optionnel » ;
- ITER sans condition de direction précédente ;
- sorties minimales de la skill incomplètes par rapport à ACTION/HANDOFF.

**Pourquoi Majeur.** C'est la définition du protocole : « créer une autorité concurrente ». Un agent qui ne lit que la façade, ce que la façade encourage, prend une décision plus faible que la règle.

**Correction type (§21 : amélioration de façade, alignement).** Pas de nouvelle règle. On **déplace la cellule** dans la bonne colonne ou on ajoute un renvoi court au minimum propriétaire (« requis si DIRECTION, voir ACTION/RUN-DIRECTION »). Une suppression est préférable à un ajout quand la cellule duplique sans rien apporter.

**Test de non-régression.** `validate_reading_map.py` reçoit une règle : les routes marquées obligatoires dans la table des modes d'ACTION ne peuvent pas apparaître dans une colonne conditionnelle. Cette règle couvre aussi F-VRM-003.

### C — Accès CLI incomplet ou trop large (Significatif, lot 1)

**Fiches :** F-DIR-028, F-DIR-044, F-SK-002, F-ACT-001 (Majeur, car les cellules modales d'ACTION 11–21 omettent STATUS et PRECONDITION).

**Corrections.**
- Ajouter à la table de READING_MAP les locators dont le titre existe déjà : HANDOFF, STATUS, PRECONDITION, CREATIVE-BOOT, DERIVE, SOURCE, TOOLS, STATE, etc. C'est l'**option la moins chère**. Sa validation existe déjà (`validate_reading_map.py`).
- Pour les blocs trop larges : soit des sous-locators (DIRECTION/START-TREE), soit que `read_route.py` s'arrête au premier sous-titre de même niveau. À décider après mesure : combien de lignes pour « l'arbre seulement » ?
- F-SK-002 : faire générer le chemin de la skill par profil au moment du build, ou le formuler de façon neutre (« `READING_MAP.md` dans le dossier officiel »).

**Test.** Les 24 routes actuelles et les nouvelles sont servies dans les deux exports. Aucune route servie ne dépasse un plafond fixé pour son type.

### I — CI sur des actions dépréciées (Significatif, lot 1)

**Fiche :** F-WF-001.

- `actions/checkout@v4` et `actions/setup-python@v5` tournent sous Node 20, que GitHub a déprécié sur ses runners.
- Selon le rapport, la date de retrait est le 23 septembre 2026. **Cette date n'est pas revérifiée ici** : seule l'annonce de dépréciation est confirmée par le changelog GitHub.
- Correction : passer aux versions majeures natives Node 24, puis obtenir **un run hébergé vert**. Ce serait la première preuve CI hébergée de la campagne.

### E — La RUN_CARD vérifie la forme, pas la réalité (Significatif, lot 2)

**Fiches (28) :** F-DIR-007/F-ACT-017 (Majeur), F-ACT-015/021, F-ACT-005/006/007/008/009/010/011/012/013/018/020/022/023/025/028/034, F-PC-002, F-DF-001/002, F-RB-001/002, F-VRC-004/005, F-CHG-001.

**Comportement.** Le validateur accepte des cas incohérents :
- un consentement critique déclaré LITE ;
- une carte SYSTÈME sans consumers, migration ni rollback ;
- `observed` avec un locator fictif ;
- `not_applicable` sans raison ;
- une source ou une route inventée, ou dépréciée ;
- une promotion annoncée.

**Position proposée.** Un validateur JSON **ne peut pas** prouver qu'un run a eu lieu. Vouloir fermer toute la famille par des règles machine ferait grossir le schéma sans fin : c'est la « surcharge procédurale ». On propose donc deux choses.
1. **Documenter la portée**, en une phrase dans le README et à la sortie du validateur : « PASS = projection bien formée, pas preuve du run ».
2. **Seulement 3 règles ciblées, peu chères et à fort effet :**
   - si le risque est critique, le mode ne peut pas être LITE (F-DIR-007/F-ACT-017) ;
   - `not_applicable` exige une raison non vide ;
   - les `sources` doivent appartenir à la liste des locators actifs, avec refus des alias dépréciés (F-CHG-001 en partie, et 9.05 R1).

Le reste de la famille est reclassé **Observation (limite de portée assumée)**, après confirmation de l'owner.

### F — Rejet à tort ou exemple incohérent (Significatif, lot 2)

**Fiches :** F-RC-001, F-PC-001, F-EX-001/002/003, F-MP-001 (Mineur).

- **F-RC-001 est un faux négatif.** Une ancre réellement transformée est rejetée lors d'un retour. Un cas légitime se retrouve bloqué, ce qui pousse à contourner la règle. Correction ciblée du schéma, avec une fixture valide dédiée.
- **F-PC-001** : deux directions sont exigées même sans alternative utile. Des doublons passent sous des IDs différents, ce qui montre que l'exigence de quantité ne protège pas la diversité.
- **Les exemples (F-EX, F-MP) sont copiés par les agents.** Un claim mal formé dans un exemple se reproduit. Les corriger coûte peu.

### B — Erreurs brutes et reprise fragile (Mineur, lot 2)

**Fiches :** F-VCT-002, F-VRC-002/003/008, F-VDG-004, F-ALL-002, F-BLD-002/003.

- Remplacer les traceback par des diagnostics.
- Résoudre les chemins depuis la racine du script, pas depuis le dossier courant (F-ALL-002, reproduite en 9.05).
- Construire le build de façon atomique : stage temporaire, puis renommage.

### H — Ordre et raccords internes (Significatif, lot 3)

**Fiches :** F-DIR-001, F-DIR-043, F-DIR-003/006/008/010, F-ACT-003.

- Carte et chaîne qui inversent VISUAL_TARGET et FIRST-OBJECT.
- « Entrée prioritaire » placée tardivement (DIRECTION 794).
- Raccords de temporalité entre entrée courte, HANDOFF et RUN_CARD.
- **Déplacements ou renvois, pas de contenu nouveau.** À faire après le lot 1, qui modifie déjà les accès.

### J — Éditorial mineur (lot 3)

**Fiches :** F-VDG-002/003, F-GLO-001/002, F-QS-003. À grouper avec le lot 3.

### G — Frontières normatives et capacité positive (Observation, après 6.02)

**Fiches :** F-SAV-001 à 009, F-BIB-001 à 005, F-DIR-009, F-OM-002.

**Pourquoi attendre.** Ces fiches touchent **ce que le système fait produire** :
- plafond implicite de routes ;
- prescription possible de « neutres + accent » (F-SAV-002, directement liée au risque de rendu générique) ;
- test de masquage qui invalide un style porté par l'image ;
- filtre CONTEXT trop étroit pour la motion narrative ;
- test d'ablation qui impose une refonte structurelle ;
- variation « un axe à la fois ».

Les trancher sur le papier reviendrait à juger du goût sans rendu. Le critère du protocole §20 s'applique : « risque plausible sans preuve suffisante → Observation ».

**Deux exceptions à traiter dès maintenant, car elles sont documentaires :**
- **F-BIB-004** : SAVOIR 704 renvoie vers un contrat de composant ordinaire que COMPONENTS 611–657 ne fournit pas. Il faut soit ajouter le contrat, soit corriger le renvoi.
- **F-SAV-003** : une revue indépendante peut remplacer à tort une calibration externe, ce qui risque de produire une fausse preuve.

### Z — Non triables (53)

**Condition de reprise.** Transmettre `Audit_DIRECTION_Phase2_Checkpoint*.md` et `Audit_ACTION_Phase2_Checkpoint_Consolidation.md`, ou à défaut le registre des fiches. Beaucoup d'entre elles rejoindront probablement H, D ou E, puisque les fiches DIRECTION et ACTION déjà décrites y tombent. **C'est une hypothèse, pas une conclusion.**

---

## 4. Proposition de lot 1 (candidat à une `PATCH-DECISION`, non appliqué)

| # | Correction | Fiches couvertes | Fichiers touchés | Preuve de succès |
|---|---|---|---|---|
| 1 | Admission stricte des schémas | F-VCT-001/003, F-VRC-006/007/008 | `validate_contracts.py`, `validate_run_card.py` | Mutations `{}` et enum retiré : échec. B01 : vert. |
| 2 | Motif attendu obligatoire pour chaque fixture négative | F-FIX-001/002/003, F-ALL-001 | fixtures, `validate_run_card.py`, `validate_all.py` | Une fixture rejetée pour un autre motif fait échouer la suite. |
| 3 | Clés en double détectées | F-VRC-001 | chargeurs JSON | Une fixture avec clé en double est rejetée. |
| 4 | Contrôle des ZIP contre le manifeste, et du manifeste lui-même | F-BLD-001/004, F-MAN-001/002, F-VDG-001 | `build_distributions.sh`, `validate_design_governance.py` | Lien symbolique, doublon, version divergente : échec. |
| 5 | Locators manquants ajoutés à READING_MAP | F-DIR-028, et une partie de F-ACT-001 | `READING_MAP.md` | Les 9 locators refusés ici sont servis dans les deux exports. |
| 6 | Cellules de façade réalignées sur les propriétaires | F-RM-001/002, F-OM-001, F-QS-001/002/004, F-RDR-001, F-SK-001, F-FLOW-001, F-SAV-010, F-ACT-002 | READING_MAP, ORCHESTRATION_MAP, QUICKSTART, README racine, skill, `flow.md` | Nouvelle règle de `validate_reading_map.py` ; relecture croisée cellule par cellule contre ACTION. |
| 7 | Chemin de la skill correct par profil | F-SK-002 | skill ou build | Chemin résolu dans `dist/local` extrait. |
| 8 | Actions CI en Node 24 et run hébergé | F-WF-001 | `validate.yml` | Un run GitHub vert. |

**Taille.** 8 corrections couvrent **30 fiches**, touchent l'outillage et des façades, et **aucune règle normative de DIRECTION, ACTION, SAVOIR ou BIBLIOTHEQUE**, à part d'éventuelles ancres de titre.

**Version.** Une version B02 serait créée. Il faudra une entrée CHANGELOG, de nouveaux hashes et une validation §13 : textuelle, contractuelle, machine, distribution et non-régression.

---

## 5. Décisions qui reviennent à l'owner

1. **Gravité de la famille A** : Majeur (proposé) ou Bloquant (lecture littérale de « fausse preuve »).
2. **Famille E** : accepter le principe « la RUN_CARD valide la forme ; 3 règles ciblées ; le reste en Observation ».
3. **Lot 1** : valider tel quel, amender, ou limiter aux corrections 1 à 5 (outillage pur).
4. **Fiches Z** : fournir les deux checkpoints de phase 2, ou accepter de les laisser hors tri pour l'instant.
5. **Phase 9** : confirmer la suspension des 14 scénarios restants jusqu'à la fin du lot 1.

---

## 6. Sortie

- **PRÉ-TRI livré** : 157/157 fiches placées, dont 104 dans 10 familles et 53 non triables faute de source.
- Six fiches **reproduites de façon indépendante** dans cette unité.
- Registre : **157 fiches provisoires**, aucun nouvel ID, aucune fusion d'ID décidée. Les familles regroupent sans dédupliquer ; la déduplication formelle viendra avec le registre final.
- Aucun octet B01 modifié, aucun verdict global.

**Prochaine unité proposée :** 11.01, `PATCH-DECISION` du lot 1, après les réponses de l'owner à la section 5. En parallèle et sans dépendance : récupérer les deux checkpoints de phase 2 pour trier les fiches Z.
