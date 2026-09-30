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
4. **Décisions :** toutes les décisions du plan maître sont prises (`audit/reports/V12R_14_DECISIONS_ARBITRAGES.md`, addendums 1 et 2). Un contenu qui dépend d'une question nouvelle attend la réponse de l'owner.
5. **Consolider avant d'évaluer.** Aucun run avant la porte **P2 « prêt pour l'évaluation »** (§4). Corriger et améliorer, c'est mettre l'existant à sa place (hiérarchie, organisation, accès, cohérence, clarté, fiabilité), pas ajouter ni retirer au hasard ; chaque modification répond à un défaut identifié, préserve ce qui marche et a une vérification proportionnée. Les moyens de produire du beau interviennent pendant la conception, pas seulement dans les contrôles de fin.

## 2. État (après R11 ciblé, 30-09-2026)

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
| R8b, R8b-2, R8c, R8c-2 : moyens et gestes ; R7 : ancre graduée ; raccord R7-2 (ancre absente → `EXPLORATORY`, `FAIL-ASSUMED` pour un échec connu) | `V12R_15` à `V12R_21` ; `V12R_24` |
| R7-3 : garde « ancre absente → FAIL-ASSUMED » bornée ; mesure du noyau rectifiée | `V12R_26` |
| R6b-1 : entrée humaine en quatre questions (README du package, README Local généré), guide opérateur à un parcours, README officiel en pointeur, une seule constitution ; D-11 et D-24 fermés ; 4 cas migrés | `V12R_25`, `V12R_27` |
| R11 ciblé : Q-04 à Q-13 et R-16 à R-32 instruits sur traces ; contrôle machine nommé par mode, one-shot relié à B1b, exclusion critique conditionnelle, ancre `transformed` en DIRECTION ; six cas négatifs ; trois cas de harnais migrés (M1) | `V12R_22`, `V12R_23` |

- **Mesures :**
  - **mesures après R7-2** : chemin prescrit 12 867 mots (trace légère), trace complète 17 600 ; noyau 3 889 mots, section compilée avec son titre (après R11 ciblé : 12 839 et 3 861 ; après R7 : 12 795 et 3 861 ; après R8c-2 : 12 682 et 3 748 ; après R11a : 12 187 et 3 302) ;
  - 24/25 outils de fabrication sur le chemin ; l'outil manquant est **F22** (tests perceptifs), atteignable en un renvoi conditionnel depuis Gate C (`PRC-01`), non compté car la mesure ne suit que les lectures impératives ;
  - 1 liste de chargement.
- **Gardes :**
  - `validate_structure.py` : 24 concepts, 4 renvois, 13 vocabulaires retirés, 7 résumés fidèles, 16 termes de glossaire, CHG-01 à CHG-09, ORD-01, UNI-01 (garde bornée) ;
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

## 4. Prochaines unités (ordre au 30-09-2026 : consolider, puis évaluer)

**Décisions :** `V12R_14` (addendum 1 du 27-09 ; addendum 2 du 30-09 : amendement du 28-09, R10 progressif, consolidation avant les runs). **Guides de détail :** plan consolidé (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`) et amendement (`plans/propositions/Amendement_V1.2_2026-09-28.md`). Ce sont des documents de provenance, pas des plans actifs : leurs anciennes propositions ne réintroduisent pas un périmètre remplacé.

| Ordre | Unité | Guide | Points clés |
|---|---|---|---|
| 0 | **Inventaire unique des défauts** | `audit/data/V12R/V12R_Inventaire_P2.md` (créé le 30-09) | Registre D-01 à D-23, points du plan consolidé et de l'amendement, Q04 à Q13, R16 à R32, réserves de clôture : chacun marqué **bloquant P2** ou **non bloquant** (avec sa limite écrite). C'est la liste de sortie de la consolidation |
| 1 | ~~**R8b**~~ — **fait** (`V12R_15`) ; moyens et enseignements transférables | amendement §4 | Carte des moyens consolidée : ce que chaque couche permet de construire, comment choisir, ce qui limite ; des conditions au lieu d'« atteignable » ; licences vérifiées par ressource ; D-20 préservé. **Plus d'atlas des 18 créations comme livrable** : les enseignements de l'atlas v0 sont confrontés à l'existant et deviennent un renvoi ou un ajout ciblé, conditionnel, avec observation attendue et contre-indication ; aucun style déduit d'un petit échantillon |
| 2 | ~~**R8c**~~ **fait** (`V12R_17`, `V12R_18`) ; — résoudre plus précisément | amendement §5 ; `V12R_15` §2 | Candidats venus de R8b (à examiner, sans obligation d'ajouter une recette chacun) : contraste d'échelle, **geste existant** à approfondir (Gate C, C2 : « une échelle contrastée »), appliqué au titre, aux masses et à la composition ; texte dans la zone calme de l'image ; relecture de l'ensemble après une correction locale (hiérarchie et harmonie conservées) ; récupération après erreur, observée par interaction et reprise, pas seulement sur capture. Compléter seulement les gestes insuffisamment opérables (équilibre d'un titre, relation texte/image, poids optique des icônes, récupération après erreur, réinspection de l'ensemble après un réglage local) : déclencheur, corrections possibles, observation de l'effet. Aucune modification obligatoire si la relation fonctionne ; pas de bloc `FINITION` comme fin en soi ; « accent, traitement ou famille unique » restent contextuels. Contenus chez leurs propriétaires, noyau recompilé |
| 3 | ~~**R7**~~ **fait** (`V12R_20`, `V12R_21`) ; — ancre graduée | amendement §6 | DIRECTION porte la règle canonique, SAVOIR son exploitation, ACTION les observations et la conséquence sur l'acceptation ; une ancre peut venir du projet lui-même ; limite déclarée : le validateur (inchangé) ne garantit pas « observée ou fournie pour un produit réel », qui relève de la revue d'acceptation |
| 4 | ~~**R11 ciblé**~~ **fait** (`V12R_22`, `V12R_23`) ; Q-13 (README) et R-25b affectés à R6b, Q-13 (RELEASE_NOTES) à R12 | amendement §7 | Q04, Q07, Q08, Q09 ; B1b : deux exceptions préservées, une comparaison peut confirmer l'original ; Q11 et Q12 maintenus ; `DAILY` enregistré comme corrigé (R11a) ; cas négatifs manquants (provenance, `observed` / `not_verified`, protection critique) après vérification des autres harnais ; Q13 et R16 à R32 ouverts jusqu'à lecture des traces (`audit/logs/*.zip`) |
| 5 | **R6b élargi** — R6b-1 **fait** (`V12R_27`) ; **reste R6b-2** (cartes réunies, non bloquant P2, avec sa maquette) — une entrée humaine cohérente | amendement §8 ; définition du 27-09 ci-dessous | Quatre questions : que demander, que fournir, que recevoir, comment poursuivre. Le novice ne choisit pas de mode ; prise de brief proportionnée ; fusion des README du package ; QUICKSTART raccourci ; cartes de lecture réunies sans perdre liens ni locators. **README Local généré par `build_distributions.sh` : à inclure impérativement.** Réponse visible d'`ACTION/HANDOFF` réutilisée. Reprend Q-13 (affirmation de cohérence bornée, texte cible dans `V12R_22` §3) et R-25b (« parcours minimal ») |
| 6 | **Restes R5** | amendement §9 | Copies du handoff (SAVOIR, BIBLIOTHEQUE) → renvois ; maintenance et promotion hors du parcours local (vérifier que le chargement inutile baisse) ; `PRINT_FIELD` relié aux signaux de convergence ; alternative située : DIRECTION le déclenchement, SAVOIR les leviers, ACTION la comparaison |
| 7 | **Relecture de parcours**, puis **porte P2** | ci-dessous | Voir « Porte P2 » |
| 8 | **R10 progressif** (après P2, et quand l'owner lève la consigne « pas de run ») | ci-dessous | Palier exploratoire, puis 18 si justifié, puis davantage pour une question précise |
| 9 | **R11 final**, puis **R12** | amendement §11 | CI hébergée sur la candidate distribuable ; réserves disposées ; V1.2.0 avec R9 reporté ; feu vert final |

### Porte P2 — prêt pour l'évaluation

| Axe | Critère | Vérification |
|---|---|---|
| Hiérarchie et autorité | Chaque règle a un lieu propriétaire ; obligatoire et conditionnel distingués ; résolution des conflits écrite | Gardes de propriété ; relecture |
| Organisation et accès | Une entrée agent (la skill), une entrée humaine (R6b) ; chaque ressource atteignable au moment où elle sert | Atteignabilité (disparition, accès conditionnel et fragilité d'ancre distingués) ; routes résolubles |
| Cohérence opérationnelle | `DIRECTION/DOUBLE-LOOP` reste la référence : fabrication guidée, réobservation, comparaison, maintien ou réouverture de la direction, arrêt justifié ; observation adaptée au risque (capture, interaction, séquence ou mesure) | Relecture des embranchements et de leurs renvois, sans nouvelle définition de la boucle |
| Clarté et charge | Pas de doublon contradictoire ; aucune nuance utile perdue ; jargon expliqué | Mesure des doublons ; glossaire ; relecture |
| Fiabilité | Renvois valides ; exemples conformes aux règles ; distributions GitHub et Local fidèles aux sources | `validate_all`, 13.01, 13.02, suivi, build des distributions |

**Seuil :**
- les défauts connus qui compromettent l'usage ou faussent l'évaluation sont corrigés (aucun « bloquant P2 » ouvert dans l'inventaire) ;
- les parcours essentiels sont vérifiés ;
- les limites restantes sont écrites et ne bloquent pas l'épreuve.

P2 ne prétend pas établir ce que seul l'usage montre.

**Relecture de parcours** (une inspection, sans production). On suit pas à pas ce que le système fait lire et faire, pour quatre profils :
- un agent sur brief vague ;
- un agent sur brief riche avec photos ;
- un humain novice ;
- un expert qui reprend un run.

On note chaque trou, chaque contradiction et chaque ressource qui arrive trop tard ; chaque constat entre dans l'inventaire. La relecture suit aussi les retours de `DIRECTION/DOUBLE-LOOP` : défaut local, direction à rouvrir, risque changé, preuve insuffisante et arrêt justifié. Elle vérifie le passage d'une première proposition exploratoire à une acceptation pour un produit réel (R7). Une observation par interaction ou mesure reste accessible lorsque la capture ne suffit pas. La relecture se fait à la fin des lots, puis à la porte P2.

**Inventaire :** réconcilier les registres existants dans une vue unique (identifiant, emplacement, conséquence, lot, état, preuve ou limite). Un défaut déjà corrigé reste un acquis à vérifier ; il ne redevient pas une correction à faire. Une classification « non bloquant P2 » se justifie par la conséquence restante. Pour Q13 et R16–R32, la classification reste à instruire jusqu'à lecture des traces : une absence de preuve ne permet pas de les déclarer non bloquants. P2 s'appuie sur les outils existants ; l'ajout du cliquet d'atteignabilité reste une proposition distincte.

### R10 progressif

- **But :** évaluer ce qu'une lecture ne peut pas établir (qualité réelle, facilité d'usage, coût, variabilité), pas améliorer le système.
- **Palier exploratoire :** 2 briefs contrastés (B-DLA et SaaS) × 3 conditions (C1, C3, C4) = **6 cas comparés**. Il faut 6 productions neuves, ou 4 seulement si une référence B-DLA C1 et une référence B-DLA C4 restent réutilisables. Vérifier et consigner pour chaque réemploi : modèle et version, consignes et brief, outils et capacités, intrants, limites de production, captures et mesures. Déclarer les écarts et refaire un cas lorsqu'ils empêchent la comparaison. **C3 est produit avec la candidate consolidée après P2** ; un ancien rendu C3 de P1 (package après R4) reste une pièce historique et ne représente pas cette candidate.
- **Critères écrits avant de produire :**
  - ce qu'est un « problème évident » (on corrige d'abord) ;
  - ce qui justifie de passer à 18 ;
  - le compromis de coût acceptable ;
  - le traitement des désaccords entre juges.
- **Mesures par rendu :** qualité de la première proposition, reprises nécessaires, effort (tokens, temps), honnêteté. Conserver si possible la première proposition et le résultat après corrections.
- **Ensuite :** 18 productions si les résultats sont encourageants mais incertains ; au-delà seulement pour une question précise encore ouverte. Les 18 peuvent faire partie des 60 si le protocole et la version sont identiques.
- **Jugement :** comme en P1 (juges neufs, à l'aveugle, brief riche, sans argumentaire du producteur) ; juges selon la décision 9 ; aucun label D3 automatique.
- **Observation novice**, à part : 2 ou 3 personnes lisent l'entrée R6b et lancent une demande ; on note les blocages.
- **Si la diversité baisse :** examiner les consignes et les ressources qui peuvent favoriser la convergence, sans en présumer la cause.

### Définitions du 27-09 (historique)

#### R8c — Passe de finition (définition du 27-09) · **remplacée par l'amendement du 28-09**

- **Pourquoi.** Le système sait mieux « ne pas rater » que « réussir » : le noyau porte des gestes de composition, mais peu de recettes de finition concrètes. C'est l'écart entre un rendu correct et un rendu haut de gamme.
- **Périmètre.** Un bloc `FINITION` dans le lieu propriétaire du craft (`SAVOIR/CRAFT`, à préciser dans le patch), compilé dans le noyau §7 juste après la repasse. Environ douze gestes, classés par couche :
  - **type :** échelle contrastée, tailles optiques ou graisses de titre, approche des grands corps, longueur de ligne, interlignage par rôle, ponctuation et chiffres (tabulaires dans les données) ;
  - **espace :** une échelle d'espacements, la proximité qui groupe, le vide qui isole le foyer ;
  - **couleur :** rôles (fond, texte, accent, état), contraste vérifié, un accent tenu ;
  - **image :** un seul traitement, recadrage au service du foyer ;
  - **interaction et états :** focus visible et dessiné, survol et pression, chargement, vide et erreur rédigés ;
  - **détail :** alignement optique, cohérence des rayons et des traits, icônes d'une seule famille.
- **Forme de chaque geste :** quand l'appliquer ; ce qu'on regarde sur la capture ; la « diff possible ». Aucun style imposé ; aucun formulaire de trace.
- **Sources datées** (`[VEILLE]`) : ouvrages et guides de référence en typographie et en interface, cités sans copie.
- **Gardes :** concept `FIN-01` à son lieu propriétaire ; noyau recompilé ; renvoi depuis Gate C (C2, C4, C6) ; « qualité avant nombre de mots » assumée et déclarée.
- **Réussite :** chaque geste s'observe sur une capture et produit une diff ; aucun ne contredit la retenue, la vérité ou l'accessibilité.
- **Arrêt :** si un geste ne peut pas s'observer sur une capture, il sort ; si le bloc tourne à la liste de style, on revient aux critères.

#### R6b élargi — Une entrée humaine d'une page (définition du 27-09) · **valable en complément de l'amendement du 28-09**

- **En plus du périmètre du plan consolidé (§6) :**
  - **une page d'entrée humaine**, courte et accueillante : « dites ce que vous voulez, donnez vos photos, vos textes et votre marque, voici ce que vous recevez et comment l'améliorer ensemble » ; au vouvoiement, sans jargon, avec renvoi vers la profondeur experte ;
  - **une demande d'intrants amicale**, un seul message, qui applique la prise de brief décidée (au plus trois demandes, par gain de plafond ; rendu construit dans tous les cas) et explique pourquoi les photos et le vrai contenu changent le résultat ;
  - **une voix produit pour la réponse visible** (`ACTION/HANDOFF`) : claire, engageante et professionnelle, sans jargon interne ; le ton ne masque jamais un manque ou une limite.
- **Gardes :** fidélité de la prise de brief (garde FIDELITY existante) ; registre au vouvoiement ; une seule entrée humaine (pas de démarrage concurrent).
- **Réussite :** un novice sait quoi dire et quoi fournir en moins d'une minute de lecture. C'est une revue documentaire ; la facilité réelle reste à observer (R10).

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

### R8 — Matériaux et atlas · **périmètre historique** : R8a fait ; R8b réorienté (sans atlas) et R8c recadré, voir §4

- **Périmètre :**
  - carte des moyens consolidée (critères, sources datées `[VEILLE]`) ;
  - atlas d'ancres annotées v1, en **référence de la skill** chargée seulement si la décision visuelle est ouverte ;
  - ~~**D-21**~~ fait en R8a (`V12R_09`). Rappel de l'ancien périmètre : étendre la « question de convergence » du noyau (§5) à la **typographie** (familles que le modèle choisit sans brief) avec la même règle : nommer, justifier ou reconsidérer, jamais interdire.
- **Arrêt :** si l'atlas pousse vers un seul style, ne garder que les critères.

### R11 — Réserves et mineurs · périmètre d'origine (ciblé depuis `V12R_14` ; voir §4)

- **Périmètre :**
  - tri un par un de Q-04, Q-07, Q-08, Q-09, Q-11, Q-12, Q-13, R-16 à R-32 : corrigé, rendu obsolète par la refonte (déclaré) ou maintenu (déclaré) ;
  - cas négatifs pour les ≈ 14 invariants sans cas négatif ;
  - placeholders dans les champs libres.
- **Sources :** `audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md` §3.

### Lots qui attendaient une décision de l'owner (toutes prises le 27-09-2026, voir `V12R_14`)

| Lot | Décision | Recommandation |
|---|---|---|
| R7 (texte d'orientation) | 6 (ancre), 8 (lois), 10 (catalogue) | 6 (a) graduée par destination ; 8 (a) tester en R10 ; 10 (a) après publication |
| R9 (trace machine, schéma) | 3 (version) | **Reporté.** Schéma `RUN_CARD` inchangé ; aucun champ nouveau ; `modal` / `parti` restent projetés dans `direction.anti_direction` ; publication visée V1.2.0 |
| R10 (épreuve à l'aveugle) | 9 (juges) | (c) personnes extérieures et juges modèles d'autres familles, déclarés non indépendants |
| R12 (publication V1.2.0) | feu vert final | après R10 |

## 5. Dette déclarée à solder

- ~~Exemptions de la garde « boucle unique »~~ : toutes levées (R5c, R5d, R6a).
- **Carte de lecture d'ACTION** : conservée (C4, 13.02 et `validate_design_governance` en dépendent), gardée par CHG-09. Sa fusion demande une rectification déclarée de ces outils.
- ~~D-19~~ (R5a) ; ~~D-21~~ (R8a) ; ~~D-16~~ (R5c) ; ~~F22~~ (R5d, atteignable depuis Gate C).
- **Mesure d'atteignabilité** : elle repose sur des ancres textuelles (`audit/data/V12R/V12R_outils_fabrication.json`) ; une reformulation peut faire « disparaître » un outil encore présent (cas F13 en R8a, rectifié en R11a). Proposition : cliquet d'atteignabilité dans `V12R_Suivi.py` (à décider).
- **Plan consolidé et amendement archivés** : documents de provenance, sans statut de plan actif. Les arbitrages pris sont consignés dans `V12R_14` et intégrés au §4 ; les anciennes recommandations remplacées restent historiques.
- **Coût d'un run** (D-23) : l'effet de la trace légère n'a pas été mesuré, ce sera en R10.
