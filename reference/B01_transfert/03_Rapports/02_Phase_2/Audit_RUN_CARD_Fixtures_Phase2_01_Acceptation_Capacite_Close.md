# DG-AUDIT-001 — Phase 2 — Fixtures RUN_CARD, plage 1/3 : acceptation, capacité et close

## Périmètre, reprise et baseline

- Lecture intégrale A–D des **huit premières fixtures JSON par nom alphabétique** sous `audit_work/package/schemas/fixtures` (1–8/25). Le protocole externe v2.0 §12, `Audit_RUN_CARD_Phase2_Checkpoint_Consolidation.md`, le plan maître et les quatre rapports du schéma/exemple ont été repris. Les 17 autres fixtures ne sont ici qu'inventoriées pour fixer la prochaine plage, sans audit de leur contenu.
- Baseline B01 inchangée : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma RUN_CARD `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`. Aucun fichier de la cible n'a été modifié.
- Autorités de sens ciblées : ACTION/STATUS 120–153/164–186 pour la chronologie et `LOST-IN-BUILD`, ACTION/RUN_CARD 260–286 pour capacité/provenance, ACTION/CLOSE-PACKAGE 391–405 pour close ; schéma 87–121/122–165 ; validateur `check_semantic_contract` 158–164, 183–225 et 238–269 ; `check_fixture` 337–355 et déclaration de suite 420–575 consultés à titre d'interface. Leur audit intégral suit celui des fixtures.

## Passage A — inventaire exact et rôle de chaque fichier

| N° | Fixture lue en entier | SHA-256 | Violation annoncée ; autres invalidités repérées |
|---:|---|---|---|
| 1 | `invalid_accepted_before_decision.json` | `bba162996d4c4566c92d6ea148f26f7015d07bdbf4311883001e8f74606927a6` | DIRECTION `CHECKING` avec `ACCEPTED-WITH-RESERVATION` ; `proof.provenance` manque aussi. |
| 2 | `invalid_accepted_lost_in_build.json` | `f16c16697f822f0e45961341b5e2f3fe92384593c1ff0d4415daa151e4791095` | `LOST-IN-BUILD` avec `ACCEPTED` ; provenance absente en plus. |
| 3 | `invalid_accepted_without_limitations.json` | `413cdb8c6062aa41ffdff0524f14a680ef70a681fb347fa511f27251d839af76` | LITE accepté avec `limitations=[]` et provenance présente. |
| 4 | `invalid_accepted_without_observed.json` | `022178d6d147359509c35aa706cea013da0e197120e1298163a86e295fbfd14b` | LITE accepté sans observation (`not_verified` seul) ; provenance également absente. |
| 5 | `invalid_accepted_without_provenance.json` | `9b296d9a47018525f3dbb73bc0a8899b9bcbd9e106b9d3970b6aeaedbe9be75b` | DIRECTION acceptée avec observation, mais sans provenance. |
| 6 | `invalid_capability_available_without_basis.json` | `844676c5e244cb266aafda4d523ac9b78fd01350621f6aa9a0c054f998b57924` | `available` non vide, `basis=[]`, provenance présente. |
| 7 | `invalid_capability_profile_missing_basis.json` | `1b111f09b702d69dcce3726fd2e5f2d915c0f87dd3d144fab00fd6e48017611b` | `available` non vide, clé `basis` omise ; provenance aussi absente. **Fichier non déclaré dans la suite intégrée.** |
| 8 | `invalid_creative_close_missing_field.json` | `da0dcac9f138fb14ceffa4c65b2c4d6894f8191102f1760550fd634c8d77c504` | DIRECTION fermée sans `creative_close.craft_detail` ; provenance également absente. |

Les sept premières familles nommées portent soit des invariants d'acceptation, soit la base de capacité ; la dernière vérifie un champ du close créatif. La sixième et la septième sont distinctes au niveau JSON : **tableau vide** versus **propriété absente**, bien que le validateur métier les refuse actuellement par le même diagnostic. Les objets contenant des locators illustratifs sont des fixtures et ne constituent pas des rendus réellement inspectés.

## Passage B — oracles et portée de validation

La CLI ciblée `python3 scripts/validate_run_card.py schemas/fixtures/<nom>` rejette **8/8** fichiers (code 1) ; la suite intégrée `python3 scripts/validate_run_card.py` affiche `RUN_CARD VALIDATION PASSED` (code 0). Le refus seul est insuffisant pour conclure que la **règle annoncée** est protégée : `check_fixture` contrôle également `expected_message` pour les sept fixtures effectivement appelées dans la suite (script 474–560). Cette attente textuelle protège le diagnostic ciblé même si le fichier possède une deuxième erreur. `invalid_capability_profile_missing_basis.json`, lui, n'a aucun appel `check_fixture` ; l'exécution ciblée prouve le comportement actuel du validateur, **pas** sa non-régression par la suite intégrée.

| Fixture | Diagnostic ciblé réel | Après réparation de la faute nommée | Après réparation supplémentaire de provenance, si manquante |
|---|---|---|---|
| Avant décision | « un verdict accepté exige state DECIDED ou CLOSED » | REJECT : provenance exigée | PASS |
| Direction perdue acceptée | « LOST-IN-BUILD ne peut pas produire un verdict accepté » | REJECT : provenance exigée | PASS |
| Sans limitations | « un verdict accepté exige une limitation non vide » | PASS | Sans objet |
| Sans observed | « un verdict accepté exige au moins une preuve observed » | REJECT : provenance exigée | PASS |
| Sans provenance | « un verdict accepté exige proof.provenance » | PASS | Sans objet |
| Available, basis vide | « capability_profile exige basis non vide » | PASS | Sans objet |
| Available, basis absent | Même diagnostic que basis vide ; validation ciblée seulement | REJECT : provenance exigée | PASS |
| Close sans craft_detail | « creative_close exige le champ craft_detail » | REJECT : provenance exigée | PASS |

La deuxième colonne résulte de la CLI sur fichiers inchangés. Les deux colonnes de réparation proviennent de **copies en mémoire** soumises à `validate_card`, sans écriture dans le package. Pour la provenance ajoutée, l'égalité de locator avec l'artefact a été maintenue. Cinq des huit fixtures ont donc une **double invalidité** ; trois deviennent valides après la correction annoncée seule. Le contrôle de `expected_message` atténue la double invalidité dans sept appels intégrés, mais l'isolation des scénarios est perdue dans cinq cas.

## Passage C — lecteurs, scénarios et risque pratique

- Le mainteneur qui exécute uniquement la suite voit un succès avec **24/25 fixtures présentes dans le répertoire déclarées par le script** ; l'absence du cas `basis` omis n'est pas visible dans ce résultat. Le cas `basis=[]` déclaré est voisin mais ne remplace pas exactement l'absence de clé.
- L'intégrateur qui valide les huit chemins à la main observe huit rejets et les bons premiers diagnostics ; il ne peut en déduire que réparer une seule faute suffit pour rendre cinq cartes valides. La comparaison après réparation est nécessaire pour une fixture destinée à isoler un invariant.
- Le reviewer conserve la distinction : une provenance textuelle présente et la présence d'une base de capacité ne prouvent pas que le test, la capture ou le profil sont réellement exécutés. Les oracles examinés vérifient des structures et certaines incompatibilités, pas l'efficacité du système.
- Le designer peut garder honnêtement `CHECKING`, `LOST-IN-BUILD` ou « observation manquante » dans une trace ; l'interdiction d'un verdict accepté pour ces cas protège la décision. Le défaut temporel F-ACT-009 subsiste pour les verdicts non acceptés exigés trop tôt, hors de ces fixtures.

## Passage D — constat, déduplication et suite

### F-FIX-001 — une fixture présente n'est jamais exécutée par la suite intégrée

- **Gravité provisoire : mineure, à réévaluer après lecture de toutes les fixtures et du script.** `invalid_capability_profile_missing_basis.json` (lignes 51–63) omet `capability_profile.basis` alors que `available` contient deux valeurs. Son exécution ciblée renvoie le diagnostic adéquat ; la suite liste explicitement les fixtures 420–575 sans inclure ce nom. Une comparaison des 25 noms sur disque avec les chaînes `.json` appelées par `check_fixture` montre **24 déclarées et une orpheline**.
- **Effet concret :** le `PASS` de la suite n'exerce pas ce cas. La couverture du tableau `basis=[]` est réelle, mais ne garantit pas une future évolution qui traiterait différemment une propriété absente. Owner pressenti : déclaration des fixtures dans `validate_run_card.py` et maintien de l'inventaire ; ACTION reste propriétaire de l'exigence de base de capacité.
- **Épreuve de résolution à venir :** inscrire cette fixture comme cas ciblé avec diagnostic attendu ; modifier temporairement en mémoire la règle de présence de `basis`, vérifier que le test correspondant devient rouge ; comparer absence, tableau vide et base renseignée dans les cinq modes. Ne pas inférer d'autres orphelines avant la revue complète.
- **Déduplication :** F-ACT-008 concerne `validate_contracts.py`, qui ne valide pas les fichiers utilisateur hors chemins canoniques ; ici la CLI RUN_CARD cible **bien** le fichier utilisateur, mais sa **suite intégrée omet une fixture locale**. F-ACT-018 traite le lien entre capacité déclarée et claim ; cette fiche porte uniquement la couverture du scénario de clé absente.

**Observation de qualité sans deuxième ID à ce stade.** Les fixtures 1, 2, 4, 7 et 8 ont aussi la provenance manquante. Les sept cas intégrés possèdent un `expected_message` et leur défaut annoncé est bien observé ; les doubles invalidités rendent toutefois la réparation de l'unique cause moins vérifiable. Préférer, lors de la correction des tests, une base valide pour chaque scénario, puis une seule faute ciblée, en conservant par ailleurs les tests d'interaction utiles. Vérifier si ce motif se répète dans les 17 autres fichiers avant de juger sa portée ou d'ouvrir une autre fiche.

Le registre passe de **118 à 119 constats provisoires** (101 propriétaires + 4 QUICKSTART + 2 READING_MAP + 2 ORCHESTRATION_MAP + 2 GLOSSAIRE + 2 DOMAIN_FRAME + 2 RESEARCH_BRIEF + 2 PRODUCTION_CONTRACTS + 1 RUN_CARD + **1 FIXTURES**). Aucun verdict global et aucun patch normatif.

**Prochaine unité : fixtures 9–16/25**, ordre alphabétique de `invalid_critical_placeholder_protection.json` à `invalid_empty_proof.json`. Reprendre §12, présent rapport et checkpoint RUN_CARD, recalculer B01 ; lire chaque JSON en entier, confronter premier diagnostic, cause annoncée et réparations contrefactuelles, puis recenser celles réellement appelées dans la suite. Les neuf fichiers restants suivront.
