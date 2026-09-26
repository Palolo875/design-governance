# DG-AUDIT-001 — Phase 2 — Workflow `validate.yml` : déclencheurs, runtime et portée de la preuve

**Date de contrôle :** 24 septembre 2026. **Baseline :** B01. **Profondeur :** TARGETED sur la déclaration CI, lecture complète A–D **1–22/22**. **Owner de la déclaration :** `.github/workflows/validate.yml` ; **owner des oracles de validation :** `scripts/validate_all.py`. Aucun fichier source de B01 n'a été modifié.

**Identification revérifiée :** système compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole externe v2.0 SHA-256 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; workflow SHA-256 `52dc36c30ff93986c31dd1f6af3eaa0458dfe134be58a4a74d51513a8e41c553` ; orchestrateur SHA-256 `3c04c2b3ffb81be8f6f7f6e92912fa9a20150b586b78d516d4bc0dc9211919b0`. Rapport précédent : `Audit_Build_Distributions_Phase2_01_Stages_Archives_Reprise.md`. Contexte machine : Python 3.12.14 disponible, pas de binaire Python 3.11, `actionlint` absent, reconstruction sans dépôt `.git`.

## Passage A — architecture visible, lignes 1–22

| Lignes | Déclaration | Effet et interface visibles |
|---|---|---|
| 1–5 | Nom et événements `push`, `pull_request` | Un contrôle proposé sur envoi et demande de fusion, sans filtres de branche ni chemins. Des événements différents peuvent déclencher des runs distincts pour un même changement ; volume réel inconnu. |
| 7–8 | `permissions: contents: read` | Jeton du workflow en lecture du dépôt, cohérent avec checkout et validations locales ; aucune écriture ou publication déclarée. |
| 10–12 | Un job `validate`, `runs-on: ubuntu-latest` | Choix d'image hébergée flottante ; sa composition exacte dépend de la date d'exécution. |
| 13–19 | Checkout `actions/checkout@v4`, installation `actions/setup-python@v5`, `python-version: '3.11'` | Les références majeures d'actions définissent leurs générations, le paramètre Python fixe la famille d'interpréteur visée ; les deux runtimes JavaScript d'actions et Python de l'application sont distincts. |
| 20–22 | `python3 scripts/validate_all.py` | Lance une seule suite intégrée ; son code de sortie gouverne le résultat du job si les étapes précédentes réussissent. Aucun téléversement d'archives, matrice ou collecte supplémentaire n'est déclaré. |

## Passage B — contrat sémantique et épreuves

Lecture structurelle du YAML avec `yaml.BaseLoader` : clés `on` conservées littéralement ; deux événements, permission, runner, ordre des trois étapes, cible Python et commande conformes aux lignes ci-dessus. Le parseur YAML 1.1 usuel peut convertir `on` en booléen ; ce serait un artefact du parseur local, pas une défaillance démontrée du workflow GitHub. Les six scripts Python du package passent `ast.parse(..., feature_version=(3, 11))` : **preuve de syntaxe**, pas preuve d'exécution sous 3.11.

Dans une copie temporaire isolée des fichiers sources, `python3 scripts/validate_all.py` retourne **code 0 / `FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité`**, sous **Python 3.12.14** ; ses deux builds s'exécutent dans cette copie. Le script appelle les validateurs, les tests positifs et négatifs, puis compare les empreintes de deux builds (`validate_all.py` 38–93). Ses limites d'oracle et de composition d'archive déjà ouvertes restent F-ALL-001/002, F-BLD-001/004 et autres fiches des propriétaires correspondants ; un résultat vert n'efface pas ces limites.

**Évolution de plateforme datée.** GitHub annonce le **23 septembre 2026** que Node 20 n'est plus disponible sur ses runners, que les actions JavaScript utilisent désormais Node 24 et que la dérogation temporaire est retirée ; GitHub demande de mettre à jour les actions vers des versions prenant en charge Node 24 ([GitHub Changelog, 23-09-2026](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/)). Les dépôts officiels indiquent que `actions/checkout` est passé à Node 24 en **v5** ([checkout, README](https://github.com/actions/checkout)) et que `actions/setup-python` y est passé en **v6** ([setup-python, README](https://github.com/actions/setup-python)). Le workflow B01 référence respectivement **v4** et **v5**. Cela établit un **décalage de générations et un risque de compatibilité**, pas un échec avéré : GitHub décrit précisément une exécution forcée sous Node 24, et aucun run hébergé de ce package n'a été consulté. Le paramètre Python `3.11` ne détermine pas la version de Node utilisée par les actions.

Les étiquettes majeures `@v4` et `@v5` ne figent pas un commit. La documentation GitHub explique que seul un SHA complet fixe immuablement la version de l'action et que les tags peuvent bouger ([GitHub Docs, Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)). Risque de reproductibilité à transporter dans F-WF-001 sans déclarer compromission ni ajout d'un autre ID. `ubuntu-latest` apporte lui aussi une variation possible ; aucun instantané de runner n'est fourni par la reconstruction.

## Passage C — usage réel simulé

- **Contributeur / reviewer :** une PR et un push peuvent faire vérifier le changement ; le workflow ne définit aucune condition de branche. Le statut réellement produit et l'éventuel doublon de runs demandent l'historique CI du dépôt.
- **Mainteneur CI :** un job vert atteste l'exécution de `validate_all.py` au commit et au contexte du run *si* checkout et setup ont abouti. Il ne prouve ni une publication des ZIP ni la correction des faux positifs déjà trouvés dans la suite.
- **Consommateur des archives :** aucun artefact n'est mis en ligne par ce workflow. Le contrôle de build est délégué au script sur la copie GitHub complète ; son comportement Local possède une sortie spécifique quand le build est absent (`validate_all.py` 80–83). Cette absence d'upload n'est pas un défaut en soi, car le workflow promet une validation et non une publication.
- **Audit :** la copie reconstruite n'est pas un clone Git doté d'un historique ni d'un environnement GitHub Actions. Elle ne donne accès ni aux logs hébergés, ni aux SHA effectivement résolus des actions, ni à l'image exacte du runner. L'épreuve locale sous 3.12 ne démontre pas le passage effectif du job sous Python 3.11.

## Passage D — résistance et constat provisoire

### F-WF-001 — générations d'actions antérieures au runtime Node 24 désormais imposé

**Preuve :** `validate.yml` 15 et 17 fixent checkout v4 et setup-python v5 ; passage natif Node 24 documenté à partir de checkout v5 et setup-python v6 ; retrait de Node 20 annoncé par GitHub le 23 septembre 2026. **Impact potentiel :** fragilité du contrôle CI, dépendance à l'exécution forcée sous Node 24 et baisse de reproductibilité liée aux tags mouvants et au runner flottant. **Impact observé :** aucun échec du job hébergé prouvé ; seulement un décalage vérifié entre la déclaration et la génération recommandée pour la plateforme actuelle. **Propriétaire :** workflow CI ; interface avec les deux actions officielles et `validate_all.py`. **Statut :** provisoire, gravité et décision de correction différées aux phases 10–11.

**Épreuve discriminante à obtenir :** sur le dépôt hébergé correspondant à B01, un run récent `push` et, si disponible, un run `pull_request` : relever statut et logs des trois étapes, les références/SHAs d'actions réellement chargées, versions Node du runner et Python exécuté ; comparer aux sorties de la suite. Si correction décidée en phase 11, choisir des versions officielles supportant nativement Node 24 (au minimum checkout v5, setup-python v6 à la date de contrôle), vérifier leur SHA issu des dépôts éditeurs, garder le périmètre de permissions et Python 3.11 intentionnel, rejouer la CI hébergée et vérifier les oracles sur des copies contrôlées. Une CI verte sans ces éléments ne permet pas de conclure sur la compatibilité future.

**Protections conservées :** `pull_request` (pas de `pull_request_target`), `contents: read`, version Python déclarée, commande de validation unique et test local positif. **Non-fusion :** F-WF-001 concerne les *dépendances et l'exécution de la CI* ; F-ALL-001/002 concerne les oracles de la commande ; F-BLD-001/004 la composition des archives. Aucun autre nouvel ID pour les tags, l'image flottante, les doubles déclenchements ou l'absence d'upload faute d'échec propre démontré.

**Registre :** **148 fiches provisoires avant, 149 après F-WF-001**. Ce nombre ne mesure ni défauts indépendants ni patches décidés. **Prochaine unité :** `skills/design-governance-practice/SKILL.md`, lecture intégrale A–D **1–149/149**, avec ses références et les contrats de routage utiles. Le protocole §12 continue ; aucune conclusion globale ni modification normative en phase 2.
