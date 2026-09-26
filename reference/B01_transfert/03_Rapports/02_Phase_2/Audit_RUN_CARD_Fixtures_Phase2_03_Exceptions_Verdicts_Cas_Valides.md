# DG-AUDIT-001 — Phase 2 — Fixtures RUN_CARD, plage 3/3 : exceptions, verdicts et cas valides

## Périmètre et reprise

- Lecture intégrale A–D des **neuf dernières fixtures JSON par nom alphabétique**, rangs **17–25/25** dans `audit_work/package/schemas/fixtures`. Le protocole externe v2.0 §12, les deux rapports de fixtures antérieurs, le checkpoint RUN_CARD et le plan maître ont été revérifiés. Cumul : **25/25 fichiers lus en trois plages adjacentes**, sans présumer encore l'audit intégral du script, des distributions ou du système.
- Baseline B01 stable : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucun patch du package.
- Propriétaires de sens : ACTION/STATUS 116–186 (état, issue, axes et verdict global), ACTION/RUN_CARD 252–286 et CLOSE-PACKAGE 391–427 (preuve/trace), DIRECTION et SAVOIR/STYLE pour ancre, profil et portée de l'observation. Le validateur sert ici d'oracle de forme sur les fichiers ciblés ; son audit exhaustif suivra le checkpoint des fixtures.

## Passage A — inventaire de la dernière plage

| N° | Fixture entièrement lue | SHA-256 | Scénario porté |
|---:|---|---|---|
| 17 | `invalid_fail_assumed_accepted.json` | `2c2c5505624443bc6d7d65305e545985d8654250bd53550c7ec2fae8d1577847` | `STANDARD`, `CLOSED + FAIL-ASSUMED + ACCEPTED-WITH-RESERVATION`, défaut observé et correction non rejouée. |
| 18 | `invalid_global_axis_verdict.json` | `e0caeab0941b8e60e06d19eaf32037dfac0ca45c8367b7dd93f658f2cd784455` | LITE, `closure.verdict="PASS"` : statut d'axe rangé à tort dans le verdict global. |
| 19 | `invalid_lite_missing_minimum.json` | `aad91174798679395c4738ad3d6b2e9262079f77da1ec93f1e1514d85d8f102f` | LITE retourné sans `risk`, `sources` et `next_proof`. |
| 20 | `invalid_missing_proof.json` | `ce2c16f2a4fe8f55090d1865ab514019bcbb29c5360f957fab940750435202bc` | LITE accepté avec objet `proof` entièrement absent. |
| 21 | `invalid_profile_decision_missing_evidence.json` | `115b4b86c90239c4a8163e068676bd4f22e586bfedf4f81efd84325f73592184` | DIRECTION acceptée avec `profile_decision.evidence` absent et provenance de preuve absente. |
| 22 | `invalid_state_held.json` | `c44d33edc9462d98e33497490aab8dd50685300bc76873d5bc5f1adae0c408f5` | DIRECTION utilise `closure.state="HELD"` au lieu d'un état de run ; de nombreux autres champs DIRECTION/acceptation manquent. |
| 23 | `valid_closed_return.json` | `d2ea5fa23a8085d318bf0a48b5b97263b4140d1c88329d23a0de8576479c1290` | SYSTÈME à risque critique, `CLOSED + RETURNED + RETURN`, régression observée et preuve suivante. |
| 24 | `valid_direction_exploratory_untransformed.json` | `f2abed3853ed8b77c2226dc85c7e7c99938459aa891c34ede466715caad03554` | DIRECTION `DECIDED + EXPLORATORY`, ancre `not_transformed` et transformation non établie. |
| 25 | `valid_direction_with_profile_decision.json` | `a5c851611fb46107bb35047abaf3804d8d7461d02abac37783f34961d26b7270` | DIRECTION `CLOSED + ACCEPTED-WITH-RESERVATION`, choix de profil avec quatre champs et provenance déclarée. |

La fixture 17 porte le mode `STANDARD` et l'issue `FAIL-ASSUMED`. Les trois `valid_*` démontrent la sérialisation admise ; les captures et utilisateurs mentionnés ne sont pas inspectés par cet audit.

## Passage B — oracles, relations et protections

La CLI ciblée `python3 scripts/validate_run_card.py schemas/fixtures/<nom>` rend **six codes 1 et trois codes 0**, conformément aux noms. Les **neuf fichiers sont référencés par la suite intégrée** ; **cinq des six invalides** ont un `expected_message`, tandis que `invalid_missing_proof.json` n'en a pas ; les trois valides ont un oracle de succès. `python3 scripts/validate_run_card.py` termine avec `RUN_CARD VALIDATION PASSED` (code 0). Aucun de ces résultats ne prouve l'usage ni la qualité réelle.

| Cas | Premier résultat ciblé | Contrôle sur copie en mémoire et frontière |
|---|---|---|
| FAIL-ASSUMED accepté | REJECT : issue bloquante/FAIL-ASSUMED incompatible avec verdict accepté | Remplacer seulement `verdict` par `RETURN` → PASS structurel. Cela préserve le rejet d'acceptation ; l'autorisation, la durée et le périmètre de diffusion de FAIL-ASSUMED restent F-ACT-038/039, hors de l'oracle. |
| `PASS` en verdict global | REJECT : valeur non canonique `PASS` | Remplacer seulement par `RETURN` → PASS structurel. L'issue `null` reste permise ; ce PASS ne prouve pas une disposition complète du run, tension F-ACT-010. |
| Minimum LITE incomplet | REJECT : `risk` absent | Ajouter `risk` → `sources` absent ; ajouter `sources` → `next_proof` absent ; ajouter `next_proof` → PASS. Trois obligations présentes dans le schéma, mais premier diagnostic seul attendu. |
| `proof` absent sous acceptation | REJECT : observed requis par le contrôle métier ; **aucun diagnostic attendu n'est déclaré dans la suite pour ce fichier** | Ajouter `proof.observed` et `not_verified` → provenance requise ; ajouter provenance → PASS. Le refus provient d'abord de la règle d'acceptation, même si le schéma exige aussi l'objet `proof`. |
| Profil sans evidence | REJECT : `profile_decision.evidence` obligatoire | Ajouter evidence → provenance générale manquante ; ajouter provenance → PASS. La preuve du profil reste une déclaration textuelle, non attestation de comparaison exécutée (F-SAV-005). |
| `HELD` comme state | REJECT : HELD appartient au statut de direction | Corriger `state` en `CLOSED` → direction, trace, statut de direction, ancre, creative close, provenance, limitation et conséquence décisionnelle doivent encore être fournis ; après toutes réparations → PASS. Le diagnostic dédié protège la séparation des registres, mais la fixture est fortement composite. |
| `CLOSED + RETURNED + RETURN` | PASS | ACTION 130–132 permet de clore la trace sans accepter l'artefact ; la protection critique déclarée et le retour sont cohérents dans la structure. Les tests/consumers évoqués ne sont pas exécutés ici. |
| Ancre non transformée + exploration | PASS | Déclarer seulement l'ancre `transformed` et sa transformation comme observée, en gardant le reste du run exploratoire → REJECT. Ce voisin met en évidence F-RC-001 : propriété d'ancre et verdict global sont liés par un interdit actif même si une autre preuve reste à obtenir. Le texte changé dans une copie ne constitue pas une transformation réelle. |
| Profil complet | PASS ; retirer uniquement `profile_decision.evidence` → REJECT | Protection de présence effective ; n'établit pas que le profil améliore vraiment lecture, accessibilité ou usage. |

Les contre-épreuves sont des **copies JSON en mémoire**. Deux des six négatifs deviennent valides après leur seule réparation annoncée (`FAIL-ASSUMED` et `PASS` global) ; **quatre gardent d'autres défauts**. Les trois positifs fournissent des exemples nécessaires de `CLOSED` non accepté, d'exploration avec ancre non transformée et de profil renseigné, mais aucun ne couvre le cas discriminant « ancre vraiment transformée + preuve distincte manquante + exploration » sans heurter le validateur (F-RC-001).

## Passage C — lecteurs et portée des cas positifs

Un mainteneur qui lance la suite voit des diagnostics négatifs exacts et trois cartes vertes ; il peut confirmer la grammaire des statuts sans conclure que les paquets propres aux modes ont tous été produits. Un agent face à un défaut réel ne peut écrire `FAIL-ASSUMED + ACCEPTED-WITH-RESERVATION` pour obtenir un vert : le rejet fonctionne. Un owner peut fermer administrativement un run SYSTÈME avec retour et prochaine preuve, sans transformer ce `CLOSED` en approbation du changement.

Le designer peut déclarer une ancre non transformée et un run exploratoire ; dans un autre scénario, il peut avoir réellement transformé l'ancre mais encore attendre une preuve mobile ou une tâche utilisateur. Le cas positif existant ne couvre que le premier scénario. Le reviewer sépare la phrase de comparaison du profil d'une capture ou d'un test réellement réinspectable ; le JSON valide du profil expose le choix et sa limite, pas sa véracité.

## Passage D — consolidation locale et suite

**Aucun nouvel ID ouvert lors de la lecture initiale de cette plage.** Les six invalides sont déclarés dans la suite, cinq avec diagnostic attendu et `invalid_missing_proof.json` sans ce garde-fou ; les trois positifs passent. Les quatre cas négatifs à défauts secondaires étendent **F-FIX-002 de 13/16 à 17/22 fixtures négatives** ; les cinq autres négatives ont un résultat ciblé indépendant dans leur forme actuelle. L'unique fichier du répertoire non appelé par la suite reste `invalid_capability_profile_missing_basis.json` (**F-FIX-001**, plage 1), confirmé par la comparaison des noms : **24/25 fixtures déclarées**, dont 21 négatives et trois positives. F-RC-001 conserve son test contradictoire spécifique ; F-ACT-009/010/012/017/038/039 et F-SAV-005 gardent leurs propriétaires et contre-épreuves propres. Aucune fusion anticipée.

Le registre reste à **120 constats provisoires** (101 propriétaires + 16 façades/contrats antérieurs + F-RC-001 + F-FIX-001/002). Les 25 JSON sont lus intégralement ; ce périmètre terminé ne signifie pas que le validateur et les scripts sont entièrement audités. Aucun patch du package, aucune sévérité finale et aucun verdict global.

**Prochaine unité : checkpoint cumulatif des 25 fixtures.** Reprendre les trois rapports et le protocole §12, vérifier les empreintes B01, établir la matrice cas négatifs/positifs/oracles/limitations, contrôler l'unique orphelin et le ratio 17/22, puis préparer la lecture intégrale de `scripts/validate_run_card.py` et des autres scripts. Conserver les cas positifs lors des futurs correctifs, notamment `CLOSED + RETURNED + RETURN`.

**Rectification au checkpoint suivant :** l'absence de `expected_message` pour `invalid_missing_proof.json` a été établie par analyse des 25 déclarations et mutation en mémoire. La fiche distincte F-FIX-003 et son épreuve sont détaillées dans le checkpoint cumulatif ; le présent rapport conserve le décompte provisoire de **120** à la date de sa lecture initiale.
