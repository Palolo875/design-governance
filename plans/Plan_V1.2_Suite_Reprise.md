# Plan de reprise — refonte V1.2 (pour quiconque reprend)

**Date :** 2026-09-27 · **Owner :** Junior (Kamel) · **Plan maître :** `plans/Plan_V1.2_Refonte.md` (lots R1 à R12, décisions §8). Ce document dit **où on en est, comment reprendre, et quoi faire lot par lot**. Il est tenu à jour à chaque unité.

## 1. Consignes de l'owner en vigueur

1. **Pas de run réel ni de mini-épreuve dans cette phase.** On corrige et on améliore le système ; la preuve d'efficacité viendra en R10.
2. **La qualité du résultat prime sur le nombre de mots.** Pas de plafond qui force à couper des gestes de fabrication. On retire seulement les doublons et le texte sans effet sur le rendu ; un ajout qui sert la fabrication est admis et déclaré.
3. **Méthode non négociable** (`CLAUDE.md` §4) :
   - B01 en lecture seule, 218/218 à chaque unité ;
   - PATCH-DECISION exécutable ; gardes rouges avant, vertes après ; mutations ;
   - aucune correction non décidée (un défaut découvert est signalé, pas corrigé en silence) ;
   - écarts déclarés ;
   - distinguer certain, probable et hypothétique ;
   - auto-comparaison déclarée comme telle.
4. **Décisions en attente** (plan maître §8) : 3, 6, 8, 9 et 10. **Ne pas appliquer un contenu qui en dépend avant la décision** ; préparer le texte et poser la question.

## 2. État (après R11a)

| Fait | Rapport |
|---|---|
| R1 outils de mesure ; R2 gardes de propriété ; R3 alignements ; R4 noyau compilé | `audit/reports/V12R_01` à `V12R_04` |
| P1 mini-épreuve (orientation positive, D-20 à D-23) | `V12R_05` |
| R5b-1 : trace légère, première proposition = checkpoint, contenu d'exemple marqué, test de trame | `V12R_06` |
| R5b-2 : Gate A par profil, Gate C en gestes, boucle unique, promesse du validateur unique | `V12R_07` |
| R5a : DIRECTION (rôle, posture et récapitulatif en tête ; entrée unique ; doublons ; D-17, D-19) | `V12R_08` |
| R8a : convergence typographique (D-21) dans la question de convergence du noyau | `V12R_09` |
| R5c (hors ancre) : un seul modèle de niveaux (D-16), boucle et one-shot en renvoi, exemption SAVOIR retirée | `V12R_10` |
| R5d : boucle et one-shot de BIBLIOTHEQUE en renvoi, F22 atteignable depuis Gate C (PRC-01) | `V12R_11` |
| R6a : boucle du README en renvoi (dernière exemption levée), glossaire des termes de la refonte | `V12R_12` |
| R11a : résidu `DAILY` retiré ; ancre de mesure F13 rectifiée ; carte des moyens v0 alignée sur D-20 | `V12R_13` |

- **Mesures :**
  - chemin prescrit 12 187 mots (trace légère), 16 798 en trace complète ;
  - noyau 3 302 mots ;
  - 24/25 outils de fabrication sur le chemin ; l'outil manquant est **F22** (tests perceptifs), atteignable en un renvoi conditionnel depuis Gate C (`PRC-01`), non compté car la mesure ne suit que les lectures impératives ;
  - 1 liste de chargement.
- **Gardes :**
  - `validate_structure.py` : 19 concepts, 3 renvois, 12 vocabulaires retirés, 3 résumés fidèles, 16 termes de glossaire, CHG-01 à CHG-09, ORD-01 ;
  - `validate_reading_map.py` : 50 conditions.
- **Suivi :** vert (372 cas maintenus, 17 migrés).

## 3. Reprendre une unité (recette)

```bash
# branche de travail (poussée aussi sur v1.2/patch-decision-abd)
git checkout claude/init-repo-claude-md-gm6njm
(cd reference/B01_transfert && sha256sum -c SHA256SUMS.txt | grep -c ': OK$')   # 218
```

1. **Modèle de patch :** copier `audit/tools/V12R_Patch_R5b2.py`.
   - Il réutilise la mécanique de `V12R_Patch_R5b1.py` : `--verifier`, application, recompilation du noyau, `--mutations`.
   - Entrées `(id, point, fichier, ancien texte exact, nouveau texte)`, chaque ancien texte présent une seule fois.
   - Validateurs modifiés : copie dans `V12R_Patch_<lot>_fichiers/scripts/`, avec l'empreinte SHA-256 de la version courante.
2. **Nouvelles gardes** dans `validate_structure.py` :
   - concept `<!-- concept:ID -->` au lieu propriétaire ;
   - `RETIRED` pour un texte qui ne doit plus revenir ;
   - `FIDELITY` pour un résumé qui doit garder la condition canonique ;
   - `CHG-xx` pour le chargement.
3. **Rouge avant** : copier le package dans le scratchpad, y poser les validateurs neufs, lancer `validate_structure.py` → les nouvelles gardes rougissent.
4. **Appliquer** : `python3 V12R_Patch_<lot>.py ../../package`, puis `validate_structure`, `build_core --check` et `validate_reading_map` au vert.
5. **Mutations** : `--mutations`, qui doivent toutes rougir.
6. **Suivi complet** : `python3 V12R_Suivi.py ../../package --out ../snapshots/V12R_Instantane_suivi_<lot>.json` doit rendre SUIVI VERT.
   - Un cas de harnais rouge se migre (M1) : statut OBSOLETE dans `audit/data/V12R/V12R_Correspondance_harnais.csv`, avec une garde de remplacement verte, une justification et une mutation.
7. **Contrôles** : `DG_AUDIT_001_Verifications_13-01.py` (texte 6/6, non-régression 5/5), `DG_AUDIT_001_Epreuves_13-02.py` (38/38), `V12R_Mesures.py`.
8. **Clôture de l'unité** :
   - diff dans `audit/diffs/`, rapport allégé dans `audit/reports/V12R_xx_*.md` ;
   - mise à jour de ce plan, du plan maître (ligne de statut) et de `CLAUDE.md` (§2 et §6) ;
   - commit (lignes d'attribution), push sur les deux branches.
9. **Critère d'arrêt commun** : si un lot demande plus de rectifications de harnais que de changements de texte, on s'arrête, on déclare et on revient à l'owner.

## 4. Prochaines unités (ordre décidé le 27-09-2026 : le rendu d'abord)

**Décisions :** `audit/reports/V12R_14_DECISIONS_ARBITRAGES.md` (6 graduée ; schéma inchangé → V1.2.0, R9 reporté ; atlas intégré en R8b ; juges humains + modèles ; lois inchangées ; catalogue après publication ; R10 par paliers ; R11 ciblé). **Détail de mise en œuvre :** le plan consolidé (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`) sert de guide pour chaque lot (sections citées) ; il n'est pas un second plan actif.

| Ordre | Unité | Guide | Points clés |
|---|---|---|---|
| 1 | **R8b** — carte des moyens consolidée, puis atlas conditionnel | consolidé §4 | Partir de `carte_moyens_v0` (déjà alignée sur D-20) et des 18 entrées d'`atlas_references_v0` ; retrouver les pièces exactes et leurs sources, sinon « matériau non vérifié hors atlas » ; leçon, relation produit/contenu, décision transférable, contre-indication, limite ; deux colonnes visuel/fond ; « principes observés » = observations, jamais lois ; fichier dans `skills/.../references/`, chargé seulement si la décision visuelle est ouverte ; manifeste et distributions vérifiés |
| 2 | **R7** — ancre graduée ; lois et catalogue inchangés | consolidé §8 | Un propriétaire canonique de la règle d'ancre ; DIRECTION, ACTION, SAVOIR et façades alignés ; doublons `ANCHOR-GENERATED` traités ici |
| 3 | **R11 ciblé** | consolidé §5 | Q04, Q07, Q08, Q09 (textes) ; Q11 et Q12 maintenus ; extraire `audit/logs/DG_AUDIT_001_Journaux_R02.zip` et `…_Epreuves_13-02_traces.zip` pour Q13 et R16 à R32 ; cas négatifs prioritaires ; reliquat écrit |
| 4 | **R6b** — une entrée humaine | consolidé §6 | Fusion des README du package (rectification déclarée de `validate_design_governance.py` et des LCF) ; QUICKSTART à activation unique, sans démarrages concurrents (« 90 secondes », « trente secondes », « cinq minutes ») ; READING_MAP au chemin et aux locators, avec l'orientation utile d'ORCHESTRATION_MAP |
| 5 | **Restes R5** | consolidé §7 | SAVOIR : copie du handoff (l.≈189) → renvoi ACTION ; BIBLIOTHEQUE : maintenance séparée, renvoi de `PRINT_FIELD` aux marqueurs ; doublons d'alternative située |
| 6 | **R10 par paliers** (quand l'owner lève la consigne « pas de run ») | consolidé §10 | Palier 1 : 18 productions ; conditions figées avant production ; aveugle ; juges selon la décision 9 |
| 7 | **R11 final**, puis **R12** | consolidé §5, §11 | CI hébergée sur la candidate distribuable ; réserves décidées ; V1.2.0 ; R9 déclaré reporté |

## 4 bis. Détail des lots (périmètres d'origine et état)

Chaque lot : **périmètre**, **gardes à ajouter**, **réussite**, **arrêt**.

### ~~R5a — DIRECTION~~ : fait (`V12R_08`). Reste : doublons inter-fichiers (alternative située, `ANCHOR-GENERATED`) à traiter avec R5c, R5d et R6.

#### (archive du périmètre R5a)

- **Périmètre :**
  - **D-19** : dans le bloc noyau `BRIEF`, « cette vue reste interne » perd son contexte une fois compilé ; reformuler en « la personne reçoit une proposition, pas cette liste de décisions ».
  - **D-17**, ordre :
    - `## Rôle` (l.590) et `## Posture` (l.687) viennent trop tard ;
    - les remonter en tête après la constitution, ou les réduire à un renvoi au noyau (ils y sont déjà : blocs `ROLE`, `POSTURE`) ;
    - intégrer `### Récapitulatif de protection` (l.831) au lieu propriétaire des absolus.
  - **Une seule vue d'entrée :**
    - `START` est l'entrée ;
    - « Carte de lecture canonique et chemin en trente secondes » (l.57), « Architecture d'activation » (l.41), `DIRECTION/FAST-PATH`, « Traduction humaine minimale » (l.322), `EXTERNAL-START` : garder le contenu propre, remplacer les chemins de lecture concurrents par un renvoi à `DIRECTION/CHARGE` et au noyau.
  - **Doublons :** `python3 V12R_Mesures.py ../../package`, section 4 (amas contenant `DIRECTION.md`), puis garder la phrase au lieu propriétaire.
  - **Trois couches** : noyau du fichier (sections balisées `noyau:`), référence, frontières. Les titres restent les mêmes : les locators sont des contrats.
- **Gardes :**
  - `RETIRED` sur « cette vue reste interne » ;
  - concept `ROL-01` (rôle) au lieu unique ;
  - `LOAD_POINTERS` étendu si un chemin de lecture devient un renvoi.
- **Réussite :** aucune route cassée (`read_route` sur tous les locators cités) ; doublons en baisse ; suivi vert.
- **Arrêt :** si des locators doivent être renommés.

### R5c — SAVOIR : fait hors ancre (`V12R_10`). Reste : ancre (décision 6), champs de trace vers ACTION (lecture dédiée), doublons liés à l'ancre.

#### (périmètre d'origine)

- **Périmètre :**
  - champs de trace de SAVOIR (`DESIGN-ATLAS`, raccords) déplacés vers ACTION, avec renvoi ;
  - **D-16** : deux modèles à trois niveaux → un seul ;
  - doublons ;
  - **boucle** : la séquence de SAVOIR (l.≈211, « La boucle de jugement est… ») devient un renvoi à `DIRECTION/DOUBLE-LOOP`, puis on **retire l'exemption `SAVOIR.md`** de la garde « boucle unique » (`RETIRED`, motif `→ isoler`).
  - **Ancre** (trois positions) : attendre la décision 6 (recommandation : graduée par destination).
  - **Lois de SAVOIR** (retenue) : inchangées (décision 8).
- **Gardes :** retrait de l'exemption ; concept pour le modèle à trois niveaux.

### R5d — BIBLIOTHEQUE : fait (`V12R_11`). Reste : instrumentation de lecture et contrats de promotion en annexe de maintenance ; `PRINT_FIELD` relié aux marqueurs de vague.

#### (périmètre d'origine)

- **Périmètre :**
  - instrumentation de lecture et contrats de promotion en annexe de maintenance ;
  - `BIBLIOTHEQUE/GATE` fondu dans Gates A et C, ou réduit à une liste de tests perceptifs **reliée au noyau** (F22 hors chemin) ;
  - `PRINT_FIELD` relié aux marqueurs de vague ;
  - boucle structurelle (l.211) → renvoi, puis **retirer l'exemption `BIBLIOTHEQUE.md`**.

### R6 — Façades : R6a fait (`V12R_12`). **R6b reste** : fusion des README (rectification déclarée de `validate_design_governance.py` et des LCF concernées), QUICKSTART humain, READING_MAP réduit, ORCHESTRATION_MAP.

#### (périmètre d'origine)

- **Périmètre :**
  - un seul README : fusion de `README.md` et `V1/official/README.md` ; attention au contrôle « la `RUN_CARD` rassemble » dans `validate_design_governance.py` ;
  - QUICKSTART humain au vouvoiement ;
  - GLOSSAIRE complet (trace légère, trace complète, test de trame, profils de surface, première proposition) ;
  - READING_MAP réduit au chemin et à l'index ;
  - ORCHESTRATION_MAP fondu dans READING_MAP si les harnais le permettent ;
  - séquence de boucle du README (l.77) → renvoi, puis **retirer l'exemption `README.md`**.
- **Réussite :** aucune façade ne redéfinit un contenu normatif.

### R8 — Matériaux et atlas (M) · sans décision en attente (option de l'owner : peut passer avant R5c)

- **Périmètre :**
  - carte des moyens consolidée (critères, sources datées `[VEILLE]`) ;
  - atlas d'ancres annotées v1, en **référence de la skill** chargée seulement si la décision visuelle est ouverte ;
  - ~~**D-21**~~ fait en R8a (`V12R_09`). Rappel de l'ancien périmètre : étendre la « question de convergence » du noyau (§5) à la **typographie** (familles que le modèle choisit sans brief) avec la même règle : nommer, justifier ou reconsidérer, jamais interdire.
- **Arrêt :** si l'atlas pousse vers un seul style, ne garder que les critères.

### R11 — Réserves et mineurs (M) · sans décision en attente

- **Périmètre :**
  - tri un par un de Q-04, Q-07, Q-08, Q-09, Q-11, Q-12, Q-13, R-16 à R-32 : corrigé, rendu obsolète par la refonte (déclaré) ou maintenu (déclaré) ;
  - cas négatifs pour les ≈ 14 invariants sans cas négatif ;
  - placeholders dans les champs libres.
- **Sources :** `audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md` §3.

### Lots qui attendaient une décision de l'owner (toutes prises le 27-09-2026, voir `V12R_14`)

| Lot | Décision | Recommandation |
|---|---|---|
| R7 (texte d'orientation) | 6 (ancre), 8 (lois), 10 (catalogue) | 6 (a) graduée par destination ; 8 (a) tester en R10 ; 10 (a) après publication |
| R9 (trace machine, schéma) | 3 (version) | (a) V1.2.0 si `RUN_CARD` rétrocompatible : champ `trace_level` (`light` / `full`) facultatif, `modal` / `parti` avec alias `anti_direction` |
| R10 (épreuve à l'aveugle) | 9 (juges) | (c) personnes extérieures et juges modèles d'autres familles, déclarés non indépendants |
| R12 (publication V1.2.0) | feu vert final | après R10 |

## 5. Dette déclarée à solder

- ~~Exemptions de la garde « boucle unique »~~ : toutes levées (R5c, R5d, R6a).
- **Carte de lecture d'ACTION** : conservée (C4, 13.02 et `validate_design_governance` en dépendent), gardée par CHG-09. Sa fusion demande une rectification déclarée de ces outils.
- ~~D-19~~ (R5a) ; ~~D-21~~ (R8a) ; ~~D-16~~ (R5c) ; ~~F22~~ (R5d, atteignable depuis Gate C).
- **Mesure d'atteignabilité** : elle repose sur des ancres textuelles (`audit/data/V12R/V12R_outils_fabrication.json`) ; une reformulation peut faire « disparaître » un outil encore présent (cas F13 en R8a, rectifié en R11a). Proposition : cliquet d'atteignabilité dans `V12R_Suivi.py` (à décider).
- **Plan consolidé (proposition du 27-09-2026)** : `plans/propositions/Plan_consolide_V1.2_2026-09-27.md`. Non actif : ses arbitrages seront intégrés à ce plan après décision de l'owner, sans second plan concurrent.
- **Coût d'un run** (D-23) : l'effet de la trace légère n'a pas été mesuré, ce sera en R10.
