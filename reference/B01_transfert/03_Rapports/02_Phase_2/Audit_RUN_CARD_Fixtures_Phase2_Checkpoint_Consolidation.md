# DG-AUDIT-001 — Phase 2 — Checkpoint cumulatif des 25 fixtures RUN_CARD

## Portée, méthode et continuité

Ce checkpoint consolide les trois rapports de lecture des fixtures : `Audit_RUN_CARD_Fixtures_Phase2_01_Acceptation_Capacite_Close.md` (rangs 1–8), `Audit_RUN_CARD_Fixtures_Phase2_02_Risque_Direction_Preuve.md` (9–16) et `Audit_RUN_CARD_Fixtures_Phase2_03_Exceptions_Verdicts_Cas_Valides.md` (17–25). Les plages alphabétiques sont adjacentes : **25 fichiers distincts sur 25, 22 négatifs et trois positifs**. Le checkpoint précédent du schéma/exemple RUN_CARD, le plan maître et le protocole externe v2.0 §12 ont été relus. Les quatre passages A–D sont repris ci-dessous ; le script est seulement examiné à son interface de suite et d'oracle. Sa lecture intégrale suivra.

Baseline B01 revérifiée sans changement : système compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Les **25 empreintes individuelles** publiées dans les rapports correspondent aux fichiers sur disque après correction d'une erreur de transcription à la ligne de `invalid_direction_missing_trace_locator.json` du deuxième rapport (`d5811148e8d23df1666fa47c6b4a9e8e9b6babd0afa54c5d9b8cd625752244c4`). La valeur SHA-256 de l'exemple RUN_CARD, tronquée dans six rapports antérieurs, y a aussi été remplacée par l'empreinte complète ci-dessus. Ces rectifications documentaires ne modifient aucun fichier du package.

## Passage A — couverture et cartographie des scénarios

La numérotation ci-dessous renvoie aux noms et empreintes complets des rapports sectionnels. « Composite » signifie qu'après la seule réparation du défaut ciblé, une autre invalidité subsiste selon les contre-épreuves en mémoire ; cela ne signifie pas que le diagnostic initial est faux. « Garde » signifie une sous-chaîne `expected_message` vérifiée par la suite intégrée, et non une vérification de la vérité d'un artefact.

| Rangs | Scénarios | Résultat ciblé | Couverture de suite et isolation |
|---|---|---|---|
| 1–2 | Acceptation avant décision ; direction `LOST-IN-BUILD` acceptée | Deux rejets corrects | Deux gardes ; composites par provenance absente. |
| 3–5 | Limitations absentes ; observation absente ; provenance absente | Trois rejets corrects | Trois gardes ; 4 composite, 3 et 5 isolées. |
| 6–7 | Capacité disponible avec `basis=[]` ; capacité disponible avec clé `basis` absente | Deux rejets corrects en ciblé | 6 gardée et isolée ; **7 orpheline** de suite et composite par provenance. |
| 8 | Close créatif sans `craft_detail` | Rejet correct | Garde présente ; composite par provenance. |
| 9–10 | Risque critique : contrôle placeholder ; protection absente | Deux rejets corrects | Deux gardes ; composites par contrôle/provenance supplémentaires. |
| 11–15 | Direction : close absent, objet absent, statut absent, trace absente, ancre non transformée acceptée | Cinq rejets corrects | Cinq gardes ; les cinq restent invalides après correction ciblée (close, ancre, statut, provenance ou transformation). |
| 16 | Preuve vide sous acceptation | Rejet correct | Garde `observed` ; composite par provenance. |
| 17–18 | `FAIL-ASSUMED` accepté ; `PASS` mis en verdict global | Deux rejets corrects | Deux gardes ; ces défauts sont isolés dans leur fixture. |
| 19–20 | Minimum LITE incomplet ; objet `proof` absent sous acceptation | Deux rejets corrects | 19 gardée mais composite ; **20 appelée sans `expected_message`** et composite par provenance lors de la réparation. |
| 21–22 | Profil sans evidence ; `HELD` comme state | Deux rejets corrects | Deux gardes ; composites par provenance ou plusieurs champs manquants. |
| 23–25 | `CLOSED + RETURNED + RETURN` ; exploration avec ancre non transformée ; profil complet accepté avec réserve | Trois acceptations structurelles | Trois cas déclarés dans la suite avec oracle de succès ; limites de preuve réelle et cas discriminants décrits plus bas. |

L'analyse syntaxique des appels `check_fixture` et la comparaison avec les 25 noms sur disque donnent **24/25 fichiers appelés**, soit 21 négatifs et trois positifs ; le 25e appel de la suite vise l'exemple officiel, hors du dossier fixtures. Parmi les 21 négatifs appelés, **20** ont un `expected_message`, **un** (`invalid_missing_proof.json`) n'en a pas. L'orpheline unique est `invalid_capability_profile_missing_basis.json`. Parmi les 22 négatifs du dossier, **17** sont composites (5/8, 8/8, 4/6) et cinq sont isolés ; les 22 sont rejetés individuellement, les trois valides passent. La suite intégrée rend `RUN_CARD VALIDATION PASSED`. Ces décomptes reposent sur les appels présents et sur les contre-épreuves rapportées ; un succès global ne transforme pas les 24 appels en couverture exhaustive du répertoire.

## Passage B — garanties réelles et limite de l'oracle

Le script appelle `validate_card` en ciblé et dans sa suite ; `check_fixture` (lignes 337–355 de la baseline) exige qu'un positif passe et qu'un négatif échoue. Lorsqu'un `expected_message` existe, il vérifie en plus que le premier diagnostic contient la sous-chaîne attendue. Cette garde protège les **20** rejets négatifs déclarés, malgré les défauts secondaires. Elle n'existe ni pour l'orpheline, qui n'est jamais appelée, ni pour le négatif `invalid_missing_proof.json`, qui ne contrôle que « erreur quelconque ». Le diagnostic ciblé actuel de ce dernier est « un verdict accepté exige au moins une preuve observed », alors que l'objet `proof` manque entièrement. La condition du schéma rendant l'objet obligatoire est masquée par l'ordre du diagnostic métier ; `invalid_empty_proof.json` protège déjà l'absence d'`observed` sous acceptation.

**Épreuve discriminante sans écriture :** sur une copie en mémoire de `invalid_missing_proof.json`, fournir un objet `proof` avec observation et provenance cohérente, puis mettre `mode=UNKNOWN-MODE`. `validate_card` rejette alors la valeur non canonique de `run_card.mode`, sans rejeter la preuve devenue présente. Pourtant `check_fixture(..., should_pass=False)` rend une liste d'erreurs vide : la suite conclurait encore au succès de cette fixture. Passer explicitement `expected_message="un verdict accepté exige au moins une preuve observed"` à ce même appel produit « diagnostic inattendu ». Cela montre la lacune d'oracle, sans prétendre qu'une seule sous-chaîne suffirait à isoler « objet proof absent » des autres formes de preuve insuffisante.

La correction future devra assurer séparément la violation ciblée et un voisin entièrement valide : carte acceptée avec preuve et provenance cohérentes, retrait de `proof` seulement, puis contrôle du message approprié ou d'une erreur typée dédiée. Garder à part le cas « preuve présente, mais sans observation » et les scénarios composites volontairement nommés. Aucun test sur ces JSON ne démontre qu'une capture, un contrôle critique, une comparaison de profil ou un test utilisateur a été réellement fait.

## Passage C — usage réel et contre-exemples positifs

| Lecteur ou interface | Cas qu'il peut vérifier | Ce qu'il ne doit pas en déduire |
|---|---|---|
| Mainteneur et CI | 20 diagnostics négatifs attendus, trois exemples valides, une fixture négative exécutée sans garde, une absente de la suite. | Un vert n'atteste pas les deux cas non gardés ni l'isolation des 17 composites. |
| Agent et intégrateur | `FAIL-ASSUMED` ne peut recevoir une acceptation ; un `PASS` d'axe n'est pas un verdict global ; `HELD` n'est pas un état de run. | La structure passée ne prouve pas contrôle exécuté, provenance vérifiée ou autorisation de diffusion. |
| Designer et reviewer | Une trace `CLOSED + RETURNED + RETURN` peut être correcte ; exploration avec ancre non transformée et profil complet sont sérialisables. | `CLOSED` n'est pas synonyme d'acceptation ; une phrase de profil n'est pas un résultat d'usage. |
| Owner DIRECTION/ACTION/SAVOIR | DIRECTION possède statut et ancre, ACTION issue/verdict/preuve, SAVOIR le sens du profil. | Les oracles de forme ne tranchent pas l'owner du changement ni la valeur de la direction. |

Le positif `valid_direction_exploratory_untransformed.json` accepte l'ancre **non transformée** avec verdict exploratoire. La copie où cette ancre devient **transformée** tout en gardant une preuve distincte à acquérir et le verdict exploratoire est rejetée : c'est F-RC-001, déjà ouvert lors du schéma. Préserver simultanément l'interdiction d'accepter une ancre réellement non transformée et la possibilité de déclarer une ancre transformée avec un retour ou une exploration motivés par un autre déficit. Préserver aussi le positif `valid_closed_return.json` ; ne pas forcer tous les `CLOSED` vers un verdict accepté. Le positif avec profil complet protège la présence de ses champs, sans prouver l'effet du profil sur l'artefact.

## Passage D — constats, déduplication et suite

| ID | Fait consolidé | Owner pressenti et épreuve future |
|---|---|---|
| F-FIX-001 | `invalid_capability_profile_missing_basis.json` est sur disque et rejetée en ciblé, mais absente des appels de suite. | Suite/inventaire RUN_CARD ; déclarer explicitement l'absence de clé `basis` et exercer les variations sans confondre avec `basis=[]`. Gravité provisoire mineure. |
| F-FIX-002 | 17/22 négatifs gardent au moins un autre défaut après réparation ciblée ; les gardes de diagnostic atténuent ce problème dans 20 appels, mais l'isolation des règles reste fragile. | Construction des fixtures ; bases valides avec un seul changement, voisins positifs, cas composites explicitement séparés. Gravité provisoire significative pour la maintenabilité. |
| **F-FIX-003** | `invalid_missing_proof.json` est appelée sans `expected_message` ; retirer son défaut visé et provoquer un autre rejet laisse la suite verte pour ce cas. | Oracle `check_fixture` et fixture ; garde spécifique pour absence de `proof`, cas voisin valide et distinction du cas `proof` vide. Gravité provisoire significative pour la confiance dans ce contrôle. |

F-FIX-003 est **distincte** de F-FIX-001 (non-exécution) et F-FIX-002 (scénarios composites) : ici le cas est exécuté, mais sa raison d'échec n'est pas contrôlée. La lecture intégrale du script peut réviser l'owner, la sévérité ou une éventuelle fusion en phase 10. F-RC-001 reste la règle d'ancre et de verdict au niveau contrat/validateur, distincte des oracles des fixtures ; F-ACT-009/010/012/017/018/022/038/039 et F-SAV-005 conservent leurs propriétaires. Les trois positifs et tous les rejets effectifs sont des protections à conserver.

Le registre passe de **120 à 121 fiches provisoires** : 101 propriétaires + 16 façades et contrats précédents + F-RC-001 + F-FIX-001/002/003. Ce nombre n'est ni une gravité agrégée ni un verdict global. Aucune correction normative et aucun patch du package.

**Prochaine unité :** audit intégral de `audit_work/package/scripts/validate_run_card.py` (590 lignes) en plages adjacentes, en commençant par **1–149** : import/chemins, interpréteur de schéma `validate_node`, chargement JSON et diagnostic historique `HELD`. Reprendre protocole §12, ce checkpoint, B01, schéma et exemple ; éprouver la sémantique des sous-ensembles `allOf`/`anyOf`, le traitement des types/valeurs et la frontière entre diagnostics métier et schéma. Les plages suivantes couvriront 150–326 (contrat métier/strict), 327–381 (assemblage/oracles) et 382–590 (CLI/suite). Le découpage pourra être ajusté sans omettre de ligne. Les scripts d'intégration, la skill et les distributions restent à auditer en phase 2, avant tout verdict ou correction.
