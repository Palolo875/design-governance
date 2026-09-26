# DG-AUDIT-001 — Cadrage et baseline B01

## Portée et statut

Phase 0 revue et complétée ; phase 1 exécutée sur la compilation fournie. Il s’agit de préparation et d’inventaire, sans diagnostic global de qualité ni validation de release. Le protocole externe V2.0 n’est pas modifié et ne devient pas une partie de Design Governance. Aucun fichier fourni n’est modifié. Aucun script du corpus n’a été exécuté pendant cette phase.

## Vérification du cadrage précédent

Cible : Design Governance tel que représenté dans la compilation V1.0.0. Profil de campagne : DEEP, profondeur adaptée par phase. Échelles : intra-fichier, interface, chaîne, système et release dans les limites des éléments fournis. Rôle : cadre de direction, création, jugement et vérification du design. Décision à éclairer : quels changements améliorent réellement le système sans créer de dette supérieure ?

Responsabilités : l’assistant conduit l’analyse et prépare les corrections autorisées ; l’utilisateur porte l’adoption. Les propriétaires documentaires déclarés sont DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG ; les responsabilités machine seront examinées aux interfaces. Aucune identité de mainteneur du dépôt n’est vérifiée.

Consommateurs : agents, designers, reviewers, équipes produit, intégrateurs, mainteneurs et scripts. Dépendances : propriétaires normatifs, guides dérivés, schémas, validateurs, manifeste, chaîne de distribution et environnement de preuve. Non-objectifs : créer une seconde gouvernance, promettre une efficacité non observée, modifier le dépôt sans accès ou attribuer une qualité réelle à une validation documentaire.

Risque dominant : confondre cohérence interne et efficacité. Preuves attendues : passages localisés, interfaces comparées, tests ciblés, diffs, puis runs instrumentés pour les conclusions empiriques. Condition de sortie de la préparation : version et périmètre identifiés, inventaire établi, limites d’accès déclarées et premier périmètre de lecture fixé.

Correction de cadrage : la compilation est notre référence d’observation B01, pas une source Git authentifiée. Les patches futurs pourront être préparés sur une reconstruction de travail ; ils ne seront jamais décrits comme appliqués au dépôt sans preuve de synchronisation.

## Méthode de mesure

SHA-256 calculé sur les octets exacts des deux fichiers reçus. Lignes comptées par splitlines, décodage UTF-8 strict. Les sections « Fichier » délimitent les unités incorporées. Pour leurs métriques, seule l’enveloppe externe est retirée ; les hashes internes portent sur ces payloads reconstruits, et non sur des originaux Git vérifiés. Le sommaire et le manifeste github sont comparés à cet inventaire.

Les titres, blocs, séparateurs de tableaux, liens Markdown explicites, mentions de routes, termes en code et mentions de version sont inventoriés dans l’annexe. L’analyse lexicale n’établit ni l’exhaustivité des dépendances implicites ni la validité sémantique des routes. Les ancres de liens et les commandes de validation ne sont pas testées ici. La lecture intégrale de diagnostic reste à effectuer en phase 2.

## Fichiers reçus

### Système

- Fichier : `Design_Governance_V1.0.md`
- Taille : 616480 octets
- Lignes : 8970
- Encodage : UTF-8 strict, BOM : False
- SHA-256 : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`

### Protocole externe

- Fichier : `title___Protocole_maître_d’audit_—_Design_Governan.md`
- Taille : 40811 octets
- Lignes : 1578
- Encodage : UTF-8 strict, BOM : False
- SHA-256 : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`

## Inventaire des unités incorporées

| Famille | Nombre |
|---|---:|
| Racine et intégration | 4 |
| Sources normatives | 5 |
| Guides officiels | 5 |
| Schémas et exemples | 8 |
| Fixtures JSON | 25 |
| Scripts et manifeste | 8 |
| Skill et références | 5 |
| **Total** | **60** |

| Chemin | Ligne du titre dans la compilation | Lignes du contenu | Octets du contenu |
|---|---:|---:|---:|
| `.github/workflows/validate.yml` | 72 | 22 | 398 |
| `.gitignore` | 101 | 13 | 174 |
| `README.md` | 121 | 156 | 11996 |
| `RELEASE_NOTES.md` | 284 | 59 | 2861 |
| `V1/official/ACTION.md` | 350 | 935 | 86278 |
| `V1/official/BIBLIOTHEQUE.md` | 1292 | 791 | 65008 |
| `V1/official/CHANGELOG.md` | 2090 | 63 | 4482 |
| `V1/official/DIRECTION.md` | 2160 | 818 | 94115 |
| `V1/official/GLOSSAIRE.md` | 2985 | 71 | 8677 |
| `V1/official/ORCHESTRATION_MAP.md` | 3063 | 53 | 5929 |
| `V1/official/QUICKSTART.md` | 3123 | 313 | 24429 |
| `V1/official/READING_MAP.md` | 3443 | 127 | 10052 |
| `V1/official/README.md` | 3577 | 52 | 5235 |
| `V1/official/SAVOIR.md` | 3636 | 941 | 96758 |
| `schemas/domain_frame.schema.json` | 4584 | 15 | 2149 |
| `schemas/examples/domain_frame.example.json` | 4606 | 24 | 1857 |
| `schemas/examples/production_contracts.example.json` | 4637 | 42 | 3620 |
| `schemas/examples/research_brief.example.json` | 4686 | 24 | 1672 |
| `schemas/fixtures/invalid_accepted_before_decision.json` | 4717 | 96 | 3437 |
| `schemas/fixtures/invalid_accepted_lost_in_build.json` | 4820 | 97 | 3443 |
| `schemas/fixtures/invalid_accepted_without_limitations.json` | 4924 | 18 | 967 |
| `schemas/fixtures/invalid_accepted_without_observed.json` | 4949 | 17 | 731 |
| `schemas/fixtures/invalid_accepted_without_provenance.json` | 4973 | 96 | 3435 |
| `schemas/fixtures/invalid_capability_available_without_basis.json` | 5076 | 100 | 3623 |
| `schemas/fixtures/invalid_capability_profile_missing_basis.json` | 5183 | 94 | 3337 |
| `schemas/fixtures/invalid_creative_close_missing_field.json` | 5284 | 95 | 3299 |
| `schemas/fixtures/invalid_critical_placeholder_protection.json` | 5386 | 103 | 3646 |
| `schemas/fixtures/invalid_critical_without_protection.json` | 5496 | 97 | 3486 |
| `schemas/fixtures/invalid_direction_missing_creative_close.json` | 5600 | 89 | 2796 |
| `schemas/fixtures/invalid_direction_missing_object.json` | 5696 | 18 | 822 |
| `schemas/fixtures/invalid_direction_missing_status.json` | 5721 | 95 | 3401 |
| `schemas/fixtures/invalid_direction_missing_trace_locator.json` | 5823 | 19 | 1074 |
| `schemas/fixtures/invalid_direction_untransformed_anchor.json` | 5849 | 75 | 1884 |
| `schemas/fixtures/invalid_empty_proof.json` | 5931 | 36 | 847 |
| `schemas/fixtures/invalid_fail_assumed_accepted.json` | 5974 | 19 | 954 |
| `schemas/fixtures/invalid_global_axis_verdict.json` | 6000 | 40 | 999 |
| `schemas/fixtures/invalid_lite_missing_minimum.json` | 6047 | 31 | 775 |
| `schemas/fixtures/invalid_missing_proof.json` | 6085 | 31 | 708 |
| `schemas/fixtures/invalid_profile_decision_missing_evidence.json` | 6123 | 101 | 3800 |
| `schemas/fixtures/invalid_state_held.json` | 6231 | 35 | 782 |
| `schemas/fixtures/valid_closed_return.json` | 6273 | 51 | 1616 |
| `schemas/fixtures/valid_direction_exploratory_untransformed.json` | 6331 | 70 | 1793 |
| `schemas/fixtures/valid_direction_with_profile_decision.json` | 6408 | 108 | 4144 |
| `schemas/production_contracts.schema.json` | 6523 | 12 | 3328 |
| `schemas/research_brief.schema.json` | 6542 | 39 | 1839 |
| `schemas/run_card.example.json` | 6588 | 102 | 3682 |
| `schemas/run_card.schema.json` | 6697 | 180 | 8275 |
| `scripts/build_distributions.sh` | 6884 | 166 | 8206 |
| `scripts/package_manifest.json` | 7057 | 124 | 5707 |
| `scripts/read_route.py` | 7188 | 86 | 3177 |
| `scripts/validate_all.py` | 7281 | 97 | 4747 |
| `scripts/validate_contracts.py` | 7385 | 218 | 10975 |
| `scripts/validate_design_governance.py` | 7610 | 229 | 9977 |
| `scripts/validate_reading_map.py` | 7846 | 105 | 4079 |
| `scripts/validate_run_card.py` | 7958 | 590 | 26055 |
| `skills/design-governance-practice/SKILL.md` | 8555 | 149 | 22915 |
| `skills/design-governance-practice/references/canonical_minimum.md` | 8711 | 25 | 1808 |
| `skills/design-governance-practice/references/examples.md` | 8743 | 90 | 5413 |
| `skills/design-governance-practice/references/flow.md` | 8840 | 23 | 1373 |
| `skills/design-governance-practice/references/machine_projection.md` | 8870 | 97 | 5558 |

## Contrôles mécaniques de baseline

Sommaire : 60 entrées ; manifeste github : 60 entrées ; manifeste local : 56 entrées. Les listes github et local sont deux distributions distinctes et ne doivent pas être comparées comme si leurs chemins devaient être identiques.

Résultats :

```json
{
  "contents_vs_toc_missing": [],
  "contents_vs_toc_extra": [],
  "manifest_github_missing": [],
  "manifest_github_extra": [],
  "duplicate_toc": [],
  "json_parse_errors": {}
}
```

34 blocs JSON analysés syntaxiquement. Une fixture dénommée invalid est censée être invalide au regard du contrat, pas nécessairement de la syntaxe JSON. Ce contrôle ne valide donc pas ces fixtures ni les schémas.

## Registre initial des divergences et limites

| ID | Classe | Observation | Traitement / prochaine preuve |
|---|---|---|---|
| B01-01 | Source / distribution | Compilation déclarée issue de Design_Governance_V1_1.0(7).zip ; dépôt Git et archive originale non inspectés. | Poursuivre l’audit de la copie ; identité avec la source et fidélité d’export restent non vérifiées. |
| B01-02 | Version / historique | V1.0.0 déclaré dans le titre ; nom de l’archive avec V1_1.0(7) ; révision documentaire annoncée au 21 septembre 2026. | Différence de désignation observée, pas erreur démontrée. Vérifier provenance et historique avant toute conclusion de release. |
| B01-03 | Baseline | Aucun état antérieur comparable n’est établi dans ce cycle. | Cette baseline permet les comparaisons futures ; elle ne prouve pas une amélioration passée. |
| B01-04 | Distribution | Présence de descriptions, manifeste et script de build ; archives livrées non inspectées. | Reproductibilité et identité source/export à vérifier dans la phase de validation applicable. |
| B01-05 | Preuve | Les affirmations « validé » dans les documents sont des déclarations du corpus. | Ne pas les attribuer à cet audit avant exécution et inspection des résultats. |
| B01-06 | Antériorité | Avis préliminaires de conversation et un test sémantique ciblé déjà réalisé. | Reprendre les constats dans le diagnostic sectionnel ; aucune suite complète réputée exécutée. |

## Couverture et reprise

Les niveaux ci-dessous gardent le vocabulaire du protocole ; les mentions de réalisation sont des annotations de suivi, sans modification du protocole ni statuts Design Governance.

| Phase | Profondeur / traitement de campagne | Réalisation |
|---|---|---|
| 0 Préparation | TARGETED | Cadrage revu et complété ici. |
| 1 Baseline | FULL sur les fichiers reçus | Inventaire statique terminé ; provenance, historique et distributions originales non vérifiés. |
| 2 Lecture | FULL pour les sources normatives | À engager ; avis antérieurs non assimilés à une lecture exhaustive. |
| 3 Rôles | FULL sur les responsabilités actives | À examiner. |
| 4 Contrats | FULL sur les contrats actifs | À examiner. |
| 5 Architecture | TARGETED puis approfondissement sur signal | À examiner. |
| 6 Capacité positive | TARGETED puis tests adaptés | À examiner. |
| 7 Boucles | FULL sur les parcours retenus | À examiner. |
| 8 Perspectives | TARGETED, adaptation par perspective | Les 12 perspectives restent à qualifier. |
| 9 Résistance | TARGETED, approfondissement selon risque | Les 20 scénarios restent à qualifier ; aucun réputé exécuté. |
| 10 Constats | TARGETED | Registre de limites B01, pas de verdict global. |
| 11 Décision de correction | Conditionnelle aux diagnostics | Aucun patch décidé dans cette phase. |
| 12 Correction | Conditionnelle à la phase 11 | Aucun patch appliqué. |
| 13 Validation | FULL sur les changements et risques pertinents | Contrôles de baseline seulement ; validation système à venir. |
| 14 Clôture | TARGETED | Campagne ouverte ; aucun AUDIT-PASS global. |

Première cible de lecture : V1/official/DIRECTION.md, depuis son début, avec passages A (architecture), B (contrat), C (usage simulé) et D (résistance). ACTION et les autres consommateurs seront ouverts selon les dépendances rencontrées. La lecture de DIRECTION ne clôturera pas l’audit système.

Avant cette lecture : relire la phase 2 du protocole et vérifier que les hashes B01 sont toujours ceux des fichiers examinés. Annoncer explicitement à l’utilisateur le passage de la préparation à l’audit détaillé. Reprendre chaque bloc dans l’ordre, conserver les références de ligne et rouvrir les conclusions précédentes lorsqu’une dépendance les contredit.

## Annexe technique — inventaire reproductible de l’état observé

Les locators sont des chemins et lignes de la compilation. L’annexe recense aussi les occurrences lexicales pour retrouver les contrats lors de la lecture. Aucun nombre de mentions ne mesure la qualité ou la charge cognitive réelle.

```json
{
  "audit_id": "DG-AUDIT-001",
  "baseline_id": "B01",
  "system": {
    "filename": "Design_Governance_V1.0.md",
    "bytes": 616480,
    "lines": 8970,
    "sha256": "016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d",
    "encoding": "UTF-8 strict",
    "bom": false,
    "crlf": 0,
    "lf": 8970
  },
  "protocol": {
    "filename": "title___Protocole_maître_d’audit_—_Design_Governan.md",
    "bytes": 40811,
    "lines": 1578,
    "sha256": "990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd",
    "encoding": "UTF-8 strict",
    "bom": false,
    "crlf": 0,
    "lf": 1578
  },
  "method": "Inventaire statique. Aucun script du corpus exécuté. Payload reconstruit en retirant uniquement les enveloppes de compilation ; identité octet à octet avec les sources non établie. Liens lexicaux hors blocs de code ; ancres non validées. Routes et tokens sont des candidats, pas un registre normatif.",
  "groups": {
    "Racine et intégration": 4,
    "Sources normatives": 5,
    "Guides officiels": 5,
    "Schémas et exemples": 8,
    "Fixtures JSON": 25,
    "Scripts et manifeste": 8,
    "Skill et références": 5
  },
  "checks": {
    "contents_vs_toc_missing": [],
    "contents_vs_toc_extra": [],
    "manifest_github_missing": [],
    "manifest_github_extra": [],
    "duplicate_toc": [],
    "json_parse_errors": {}
  },
  "inventory": [
    {
      "path": ".github/workflows/validate.yml",
      "compilation_heading_line": 72,
      "content_start_line": 75,
      "content_end_line": 96,
      "lines": 22,
      "bytes_utf8": 398,
      "sha256_reconstructed_payload": "52dc36c30ff93986c31dd1f6af3eaa0458dfe134be58a4a74d51513a8e41c553"
    },
    {
      "path": ".gitignore",
      "compilation_heading_line": 101,
      "content_start_line": 104,
      "content_end_line": 116,
      "lines": 13,
      "bytes_utf8": 174,
      "sha256_reconstructed_payload": "d42a0b51865105e2dc3ecd2d6ae88f5cd9730b0b1049e95762d16fe9ccf6168b"
    },
    {
      "path": "README.md",
      "compilation_heading_line": 121,
      "content_start_line": 124,
      "content_end_line": 279,
      "lines": 156,
      "bytes_utf8": 11996,
      "sha256_reconstructed_payload": "baea59563bdde0ad3683c2a96514df0d37b68a4944b39103e9dac6925c913a5c"
    },
    {
      "path": "RELEASE_NOTES.md",
      "compilation_heading_line": 284,
      "content_start_line": 287,
      "content_end_line": 345,
      "lines": 59,
      "bytes_utf8": 2861,
      "sha256_reconstructed_payload": "0911d59d11de42a1c960ba6292d38e7b911c1309f6732ef3c68703fa53b82660"
    },
    {
      "path": "V1/official/ACTION.md",
      "compilation_heading_line": 350,
      "content_start_line": 353,
      "content_end_line": 1287,
      "lines": 935,
      "bytes_utf8": 86278,
      "sha256_reconstructed_payload": "d73ad55167f71f775954092c3a91c00347753cae520031202f946b228257b50d"
    },
    {
      "path": "V1/official/BIBLIOTHEQUE.md",
      "compilation_heading_line": 1292,
      "content_start_line": 1295,
      "content_end_line": 2085,
      "lines": 791,
      "bytes_utf8": 65008,
      "sha256_reconstructed_payload": "8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684"
    },
    {
      "path": "V1/official/CHANGELOG.md",
      "compilation_heading_line": 2090,
      "content_start_line": 2093,
      "content_end_line": 2155,
      "lines": 63,
      "bytes_utf8": 4482,
      "sha256_reconstructed_payload": "0876654994f063ebb670392a5967044ad483bbdb8ebf6b5ce8a156609f08df45"
    },
    {
      "path": "V1/official/DIRECTION.md",
      "compilation_heading_line": 2160,
      "content_start_line": 2163,
      "content_end_line": 2980,
      "lines": 818,
      "bytes_utf8": 94115,
      "sha256_reconstructed_payload": "f634bc561dab243e53fa1a988c2a49565f3d6330a8e5af0e4fbaea4128bf2a7f"
    },
    {
      "path": "V1/official/GLOSSAIRE.md",
      "compilation_heading_line": 2985,
      "content_start_line": 2988,
      "content_end_line": 3058,
      "lines": 71,
      "bytes_utf8": 8677,
      "sha256_reconstructed_payload": "75cd3e509befa05d05391907420427b4309c6968f1eae6c7f26e7255f3419243"
    },
    {
      "path": "V1/official/ORCHESTRATION_MAP.md",
      "compilation_heading_line": 3063,
      "content_start_line": 3066,
      "content_end_line": 3118,
      "lines": 53,
      "bytes_utf8": 5929,
      "sha256_reconstructed_payload": "4dc72839b4944a2ea9d203a481d39a1b292a6ddc67f8edf8e3c245e546e757ab"
    },
    {
      "path": "V1/official/QUICKSTART.md",
      "compilation_heading_line": 3123,
      "content_start_line": 3126,
      "content_end_line": 3438,
      "lines": 313,
      "bytes_utf8": 24429,
      "sha256_reconstructed_payload": "c3334f12447c6dab8ac8794f5817ae52788ff06d8eff0e8d7e2d92fe7319bcde"
    },
    {
      "path": "V1/official/READING_MAP.md",
      "compilation_heading_line": 3443,
      "content_start_line": 3446,
      "content_end_line": 3572,
      "lines": 127,
      "bytes_utf8": 10052,
      "sha256_reconstructed_payload": "2348906e186962b9effe6104a9fa81fe45d86e52a57100d8fdbfa386c65a6d12"
    },
    {
      "path": "V1/official/README.md",
      "compilation_heading_line": 3577,
      "content_start_line": 3580,
      "content_end_line": 3631,
      "lines": 52,
      "bytes_utf8": 5235,
      "sha256_reconstructed_payload": "69aedf3ee8da7105010f9a83859555a7f3af585eebc48b6d4d6acd6d1683523f"
    },
    {
      "path": "V1/official/SAVOIR.md",
      "compilation_heading_line": 3636,
      "content_start_line": 3639,
      "content_end_line": 4579,
      "lines": 941,
      "bytes_utf8": 96758,
      "sha256_reconstructed_payload": "41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820"
    },
    {
      "path": "schemas/domain_frame.schema.json",
      "compilation_heading_line": 4584,
      "content_start_line": 4587,
      "content_end_line": 4601,
      "lines": 15,
      "bytes_utf8": 2149,
      "sha256_reconstructed_payload": "915339e6c567dfde60226143ed1a62ceb3c38692ddef151c53c1c756002ce95e"
    },
    {
      "path": "schemas/examples/domain_frame.example.json",
      "compilation_heading_line": 4606,
      "content_start_line": 4609,
      "content_end_line": 4632,
      "lines": 24,
      "bytes_utf8": 1857,
      "sha256_reconstructed_payload": "4e4692316007ad1c3b1befdb0762e3a7706e8b0bb1a7631ae362615749e03b7d"
    },
    {
      "path": "schemas/examples/production_contracts.example.json",
      "compilation_heading_line": 4637,
      "content_start_line": 4640,
      "content_end_line": 4681,
      "lines": 42,
      "bytes_utf8": 3620,
      "sha256_reconstructed_payload": "41f33d8c3a6d43fffd79eea4dfca5eb057ce1d701206f58279499407563779d0"
    },
    {
      "path": "schemas/examples/research_brief.example.json",
      "compilation_heading_line": 4686,
      "content_start_line": 4689,
      "content_end_line": 4712,
      "lines": 24,
      "bytes_utf8": 1672,
      "sha256_reconstructed_payload": "5905dec4eab0088e9cb1e442f398fbecec9d9dd440e04494964649af863dedd2"
    },
    {
      "path": "schemas/fixtures/invalid_accepted_before_decision.json",
      "compilation_heading_line": 4717,
      "content_start_line": 4720,
      "content_end_line": 4815,
      "lines": 96,
      "bytes_utf8": 3437,
      "sha256_reconstructed_payload": "bba162996d4c4566c92d6ea148f26f7015d07bdbf4311883001e8f74606927a6"
    },
    {
      "path": "schemas/fixtures/invalid_accepted_lost_in_build.json",
      "compilation_heading_line": 4820,
      "content_start_line": 4823,
      "content_end_line": 4919,
      "lines": 97,
      "bytes_utf8": 3443,
      "sha256_reconstructed_payload": "f16c16697f822f0e45961341b5e2f3fe92384593c1ff0d4415daa151e4791095"
    },
    {
      "path": "schemas/fixtures/invalid_accepted_without_limitations.json",
      "compilation_heading_line": 4924,
      "content_start_line": 4927,
      "content_end_line": 4944,
      "lines": 18,
      "bytes_utf8": 967,
      "sha256_reconstructed_payload": "413cdb8c6062aa41ffdff0524f14a680ef70a681fb347fa511f27251d839af76"
    },
    {
      "path": "schemas/fixtures/invalid_accepted_without_observed.json",
      "compilation_heading_line": 4949,
      "content_start_line": 4952,
      "content_end_line": 4968,
      "lines": 17,
      "bytes_utf8": 731,
      "sha256_reconstructed_payload": "022178d6d147359509c35aa706cea013da0e197120e1298163a86e295fbfd14b"
    },
    {
      "path": "schemas/fixtures/invalid_accepted_without_provenance.json",
      "compilation_heading_line": 4973,
      "content_start_line": 4976,
      "content_end_line": 5071,
      "lines": 96,
      "bytes_utf8": 3435,
      "sha256_reconstructed_payload": "9b296d9a47018525f3dbb73bc0a8899b9bcbd9e106b9d3970b6aeaedbe9be75b"
    },
    {
      "path": "schemas/fixtures/invalid_capability_available_without_basis.json",
      "compilation_heading_line": 5076,
      "content_start_line": 5079,
      "content_end_line": 5178,
      "lines": 100,
      "bytes_utf8": 3623,
      "sha256_reconstructed_payload": "844676c5e244cb266aafda4d523ac9b78fd01350621f6aa9a0c054f998b57924"
    },
    {
      "path": "schemas/fixtures/invalid_capability_profile_missing_basis.json",
      "compilation_heading_line": 5183,
      "content_start_line": 5186,
      "content_end_line": 5279,
      "lines": 94,
      "bytes_utf8": 3337,
      "sha256_reconstructed_payload": "1b111f09b702d69dcce3726fd2e5f2d915c0f87dd3d144fab00fd6e48017611b"
    },
    {
      "path": "schemas/fixtures/invalid_creative_close_missing_field.json",
      "compilation_heading_line": 5284,
      "content_start_line": 5287,
      "content_end_line": 5381,
      "lines": 95,
      "bytes_utf8": 3299,
      "sha256_reconstructed_payload": "da0dcac9f138fb14ceffa4c65b2c4d6894f8191102f1760550fd634c8d77c504"
    },
    {
      "path": "schemas/fixtures/invalid_critical_placeholder_protection.json",
      "compilation_heading_line": 5386,
      "content_start_line": 5389,
      "content_end_line": 5491,
      "lines": 103,
      "bytes_utf8": 3646,
      "sha256_reconstructed_payload": "bf162b0dff3cbdd48d5c3686ad1dbab72a107058d5b46909c6327aa63f8fdac4"
    },
    {
      "path": "schemas/fixtures/invalid_critical_without_protection.json",
      "compilation_heading_line": 5496,
      "content_start_line": 5499,
      "content_end_line": 5595,
      "lines": 97,
      "bytes_utf8": 3486,
      "sha256_reconstructed_payload": "ab5bd2e77386601d67baad0f1fa05073e1d6f39959a24c5da3a007e429fe4918"
    },
    {
      "path": "schemas/fixtures/invalid_direction_missing_creative_close.json",
      "compilation_heading_line": 5600,
      "content_start_line": 5603,
      "content_end_line": 5691,
      "lines": 89,
      "bytes_utf8": 2796,
      "sha256_reconstructed_payload": "24ab0dbbcc26f1a8c245a64d1de5441292d19df7e7fb4d9ca0b21fdb8a99c92d"
    },
    {
      "path": "schemas/fixtures/invalid_direction_missing_object.json",
      "compilation_heading_line": 5696,
      "content_start_line": 5699,
      "content_end_line": 5716,
      "lines": 18,
      "bytes_utf8": 822,
      "sha256_reconstructed_payload": "fecc7054b40eb489a68bb2dd8ba77f16e7a2b041adbc81242686ffa1301802b4"
    },
    {
      "path": "schemas/fixtures/invalid_direction_missing_status.json",
      "compilation_heading_line": 5721,
      "content_start_line": 5724,
      "content_end_line": 5818,
      "lines": 95,
      "bytes_utf8": 3401,
      "sha256_reconstructed_payload": "389688f23cce0a388ea1ddb16b51716982959a586b5cd466ce7f299d8618563c"
    },
    {
      "path": "schemas/fixtures/invalid_direction_missing_trace_locator.json",
      "compilation_heading_line": 5823,
      "content_start_line": 5826,
      "content_end_line": 5844,
      "lines": 19,
      "bytes_utf8": 1074,
      "sha256_reconstructed_payload": "d5811148e8d23df1666fa47c6b4a9e8e9b6babd0afa54c5d9b8cd625752244c4"
    },
    {
      "path": "schemas/fixtures/invalid_direction_untransformed_anchor.json",
      "compilation_heading_line": 5849,
      "content_start_line": 5852,
      "content_end_line": 5926,
      "lines": 75,
      "bytes_utf8": 1884,
      "sha256_reconstructed_payload": "1aa0a784ea0e2c412284d1cab6fc64c642c6b66314e4e31e8ceeadb67c340855"
    },
    {
      "path": "schemas/fixtures/invalid_empty_proof.json",
      "compilation_heading_line": 5931,
      "content_start_line": 5934,
      "content_end_line": 5969,
      "lines": 36,
      "bytes_utf8": 847,
      "sha256_reconstructed_payload": "0adc0479ad530151fe8efd24e5c8b71210befecbf0b47b3ab0a70f69c6151b21"
    },
    {
      "path": "schemas/fixtures/invalid_fail_assumed_accepted.json",
      "compilation_heading_line": 5974,
      "content_start_line": 5977,
      "content_end_line": 5995,
      "lines": 19,
      "bytes_utf8": 954,
      "sha256_reconstructed_payload": "2c2c5505624443bc6d7d65305e545985d8654250bd53550c7ec2fae8d1577847"
    },
    {
      "path": "schemas/fixtures/invalid_global_axis_verdict.json",
      "compilation_heading_line": 6000,
      "content_start_line": 6003,
      "content_end_line": 6042,
      "lines": 40,
      "bytes_utf8": 999,
      "sha256_reconstructed_payload": "e0caeab0941b8e60e06d19eaf32037dfac0ca45c8367b7dd93f658f2cd784455"
    },
    {
      "path": "schemas/fixtures/invalid_lite_missing_minimum.json",
      "compilation_heading_line": 6047,
      "content_start_line": 6050,
      "content_end_line": 6080,
      "lines": 31,
      "bytes_utf8": 775,
      "sha256_reconstructed_payload": "aad91174798679395c4738ad3d6b2e9262079f77da1ec93f1e1514d85d8f102f"
    },
    {
      "path": "schemas/fixtures/invalid_missing_proof.json",
      "compilation_heading_line": 6085,
      "content_start_line": 6088,
      "content_end_line": 6118,
      "lines": 31,
      "bytes_utf8": 708,
      "sha256_reconstructed_payload": "ce2c16f2a4fe8f55090d1865ab514019bcbb29c5360f957fab940750435202bc"
    },
    {
      "path": "schemas/fixtures/invalid_profile_decision_missing_evidence.json",
      "compilation_heading_line": 6123,
      "content_start_line": 6126,
      "content_end_line": 6226,
      "lines": 101,
      "bytes_utf8": 3800,
      "sha256_reconstructed_payload": "115b4b86c90239c4a8163e068676bd4f22e586bfedf4f81efd84325f73592184"
    },
    {
      "path": "schemas/fixtures/invalid_state_held.json",
      "compilation_heading_line": 6231,
      "content_start_line": 6234,
      "content_end_line": 6268,
      "lines": 35,
      "bytes_utf8": 782,
      "sha256_reconstructed_payload": "c44d33edc9462d98e33497490aab8dd50685300bc76873d5bc5f1adae0c408f5"
    },
    {
      "path": "schemas/fixtures/valid_closed_return.json",
      "compilation_heading_line": 6273,
      "content_start_line": 6276,
      "content_end_line": 6326,
      "lines": 51,
      "bytes_utf8": 1616,
      "sha256_reconstructed_payload": "d2ea5fa23a8085d318bf0a48b5b97263b4140d1c88329d23a0de8576479c1290"
    },
    {
      "path": "schemas/fixtures/valid_direction_exploratory_untransformed.json",
      "compilation_heading_line": 6331,
      "content_start_line": 6334,
      "content_end_line": 6403,
      "lines": 70,
      "bytes_utf8": 1793,
      "sha256_reconstructed_payload": "f2abed3853ed8b77c2226dc85c7e7c99938459aa891c34ede466715caad03554"
    },
    {
      "path": "schemas/fixtures/valid_direction_with_profile_decision.json",
      "compilation_heading_line": 6408,
      "content_start_line": 6411,
      "content_end_line": 6518,
      "lines": 108,
      "bytes_utf8": 4144,
      "sha256_reconstructed_payload": "a5c851611fb46107bb35047abaf3804d8d7461d02abac37783f34961d26b7270"
    },
    {
      "path": "schemas/production_contracts.schema.json",
      "compilation_heading_line": 6523,
      "content_start_line": 6526,
      "content_end_line": 6537,
      "lines": 12,
      "bytes_utf8": 3328,
      "sha256_reconstructed_payload": "b9d63e30dc3ea7a2dd491f4e86320ee50f0ce6525ebf318c8c1d775a61a09419"
    },
    {
      "path": "schemas/research_brief.schema.json",
      "compilation_heading_line": 6542,
      "content_start_line": 6545,
      "content_end_line": 6583,
      "lines": 39,
      "bytes_utf8": 1839,
      "sha256_reconstructed_payload": "2fb172b9a5b3eae5f89dc72336852ea108adfdf996618474eb844f4280d6fb91"
    },
    {
      "path": "schemas/run_card.example.json",
      "compilation_heading_line": 6588,
      "content_start_line": 6591,
      "content_end_line": 6692,
      "lines": 102,
      "bytes_utf8": 3682,
      "sha256_reconstructed_payload": "30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194"
    },
    {
      "path": "schemas/run_card.schema.json",
      "compilation_heading_line": 6697,
      "content_start_line": 6700,
      "content_end_line": 6879,
      "lines": 180,
      "bytes_utf8": 8275,
      "sha256_reconstructed_payload": "ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889"
    },
    {
      "path": "scripts/build_distributions.sh",
      "compilation_heading_line": 6884,
      "content_start_line": 6887,
      "content_end_line": 7052,
      "lines": 166,
      "bytes_utf8": 8206,
      "sha256_reconstructed_payload": "558167c41d066df1ed82f9a6ec9b294b3e6270309be874731bbc85b3aae1d956"
    },
    {
      "path": "scripts/package_manifest.json",
      "compilation_heading_line": 7057,
      "content_start_line": 7060,
      "content_end_line": 7183,
      "lines": 124,
      "bytes_utf8": 5707,
      "sha256_reconstructed_payload": "bef40232b2cbb1fdc8fda4d2bfc6bb752e9abbc3705d9a662eb44aa8da266f8b"
    },
    {
      "path": "scripts/read_route.py",
      "compilation_heading_line": 7188,
      "content_start_line": 7191,
      "content_end_line": 7276,
      "lines": 86,
      "bytes_utf8": 3177,
      "sha256_reconstructed_payload": "d3fd5f108346919bf681dc62b642017a125af9bcee2a915260d75330fe2943ce"
    },
    {
      "path": "scripts/validate_all.py",
      "compilation_heading_line": 7281,
      "content_start_line": 7284,
      "content_end_line": 7380,
      "lines": 97,
      "bytes_utf8": 4747,
      "sha256_reconstructed_payload": "3c04c2b3ffb81be8f6f7f6e92912fa9a20150b586b78d516d4bc0dc9211919b0"
    },
    {
      "path": "scripts/validate_contracts.py",
      "compilation_heading_line": 7385,
      "content_start_line": 7388,
      "content_end_line": 7605,
      "lines": 218,
      "bytes_utf8": 10975,
      "sha256_reconstructed_payload": "ec6cbb6254381c3aa1bd9115650bf77a572e2107db5457955b9c97ec90a1395e"
    },
    {
      "path": "scripts/validate_design_governance.py",
      "compilation_heading_line": 7610,
      "content_start_line": 7613,
      "content_end_line": 7841,
      "lines": 229,
      "bytes_utf8": 9977,
      "sha256_reconstructed_payload": "8853fcd4300bdf0f45431deda538f053f48292064d1161e6518c8ab7b932bb4b"
    },
    {
      "path": "scripts/validate_reading_map.py",
      "compilation_heading_line": 7846,
      "content_start_line": 7849,
      "content_end_line": 7953,
      "lines": 105,
      "bytes_utf8": 4079,
      "sha256_reconstructed_payload": "48f2dcc5d4e3d0474f4723eb07445d53b36402473b909d6303347eb7685655e8"
    },
    {
      "path": "scripts/validate_run_card.py",
      "compilation_heading_line": 7958,
      "content_start_line": 7961,
      "content_end_line": 8550,
      "lines": 590,
      "bytes_utf8": 26055,
      "sha256_reconstructed_payload": "ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757"
    },
    {
      "path": "skills/design-governance-practice/SKILL.md",
      "compilation_heading_line": 8555,
      "content_start_line": 8558,
      "content_end_line": 8706,
      "lines": 149,
      "bytes_utf8": 22915,
      "sha256_reconstructed_payload": "2d2734eb13527563698542303682d204a3174b987adbb9ac02d795cf31687853"
    },
    {
      "path": "skills/design-governance-practice/references/canonical_minimum.md",
      "compilation_heading_line": 8711,
      "content_start_line": 8714,
      "content_end_line": 8738,
      "lines": 25,
      "bytes_utf8": 1808,
      "sha256_reconstructed_payload": "60d1d25354037cdf6e7b956e1df59e7571c91732edf55d71323606a6a79df3ac"
    },
    {
      "path": "skills/design-governance-practice/references/examples.md",
      "compilation_heading_line": 8743,
      "content_start_line": 8746,
      "content_end_line": 8835,
      "lines": 90,
      "bytes_utf8": 5413,
      "sha256_reconstructed_payload": "8bfbb41cdc43adc5fa6c8c49e011abef459119cce0d55bb9424014aef9f1a8f9"
    },
    {
      "path": "skills/design-governance-practice/references/flow.md",
      "compilation_heading_line": 8840,
      "content_start_line": 8843,
      "content_end_line": 8865,
      "lines": 23,
      "bytes_utf8": 1373,
      "sha256_reconstructed_payload": "4202c8e270384ca976a70dafe2a734e11b8c2a8d75d8d6e5772387a4ee5577ee"
    },
    {
      "path": "skills/design-governance-practice/references/machine_projection.md",
      "compilation_heading_line": 8870,
      "content_start_line": 8873,
      "content_end_line": 8969,
      "lines": 97,
      "bytes_utf8": 5558,
      "sha256_reconstructed_payload": "0ad28dd850cbf639eeb1304ff6d083e882d57642ed3b8aa18a2c9634945c07af"
    }
  ],
  "markdown_inventory": {
    "README.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Design Governance V1.0.0"
        },
        {
          "line": 9,
          "level": 2,
          "title": "Fiche de version"
        },
        {
          "line": 23,
          "level": 2,
          "title": "Par où commencer"
        },
        {
          "line": 29,
          "level": 3,
          "title": "Démarrage express — 90 secondes"
        },
        {
          "line": 41,
          "level": 3,
          "title": "Choisir le chemin court"
        },
        {
          "line": 55,
          "level": 2,
          "title": "Constitution minimale"
        },
        {
          "line": 61,
          "level": 2,
          "title": "Le modèle à double boucle"
        },
        {
          "line": 79,
          "level": 2,
          "title": "Structure du dépôt"
        },
        {
          "line": 102,
          "level": 2,
          "title": "Source de vérité et distributions"
        },
        {
          "line": 119,
          "level": 2,
          "title": "Validation"
        },
        {
          "line": 142,
          "level": 2,
          "title": "Limites et discipline d’usage"
        },
        {
          "line": 148,
          "level": 2,
          "title": "Profils de lecture"
        }
      ],
      "fences": [
        {
          "line": 33,
          "language": "text"
        },
        {
          "line": 106,
          "language": "bash"
        },
        {
          "line": 112,
          "language": "text"
        },
        {
          "line": 133,
          "language": "bash"
        }
      ],
      "table_separator_lines": [
        12,
        44,
        66,
        82,
        91,
        126,
        151
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 7,
          "text": "> **Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue. La baseline est contrôlée et destinée à un usage supervisé ; elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage, ni conformité sans preuve adaptée."
        },
        {
          "line": 9,
          "text": "## Fiche de version"
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 39,
          "value": "DIRECTION/START"
        },
        {
          "line": 100,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "NOT-VERIFIED": 1,
        "RUN_CARD": 4,
        "DIRECTION": 3,
        "ACTION": 2,
        "SAVOIR": 2,
        "BIBLIOTHEQUE": 2,
        "LITE": 1,
        "ITER": 1,
        "STANDARD": 1,
        "DOMAIN_FRAME": 1,
        "RESEARCH_BRIEF": 1
      }
    },
    "RELEASE_NOTES.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Release notes — Design Governance V1.0.0"
        },
        {
          "line": 7,
          "level": 2,
          "title": "Présentation"
        },
        {
          "line": 13,
          "level": 2,
          "title": "Ce que contient la baseline"
        },
        {
          "line": 24,
          "level": 2,
          "title": "Parcours de découverte"
        },
        {
          "line": 42,
          "level": 2,
          "title": "Contrôles inclus"
        },
        {
          "line": 54,
          "level": 2,
          "title": "Limites déclarées"
        }
      ],
      "fences": [
        {
          "line": 28,
          "language": "text"
        },
        {
          "line": 36,
          "language": "text"
        },
        {
          "line": 50,
          "language": "bash"
        }
      ],
      "table_separator_lines": [
        16
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 1,
          "text": "# Release notes — Design Governance V1.0.0"
        },
        {
          "line": 4,
          "text": "**Date de publication :** 2026-09-19  "
        },
        {
          "line": 9,
          "text": "Design Governance V1.0.0 est une baseline publique pour diriger, créer, juger, construire et vérifier un travail de design. Elle aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque."
        },
        {
          "line": 11,
          "text": "La release est présentée comme un système cohérent, utilisable et testable. Elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage sans preuve adaptée."
        },
        {
          "line": 13,
          "text": "## Ce que contient la baseline"
        },
        {
          "line": 48,
          "text": "Pour vérifier la baseline :"
        },
        {
          "line": 56,
          "text": "V1.0.0 est une baseline expérimentale. Son efficacité de lecture, son adoption, sa charge cognitive, sa performance de production et sa supériorité par rapport à une autre méthode ne sont pas déclarées comme démontrées."
        },
        {
          "line": 58,
          "text": "L’historique détaillé de construction et de travail est conservé hors de la distribution publique. Il n’est pas nécessaire pour utiliser la baseline."
        }
      ],
      "route_mentions_lexical": [],
      "uppercase_code_tokens_not_a_status_registry": {}
    },
    "V1/official/ACTION.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "ACTION — Pipeline de livraison & preuves"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Responsabilité"
        },
        {
          "line": 11,
          "level": 3,
          "title": "Carte de lecture par mode"
        },
        {
          "line": 23,
          "level": 3,
          "title": "ACTION/HANDOFF — sortie minimale commune"
        },
        {
          "line": 37,
          "level": 3,
          "title": "Les quatre registres à ne pas mélanger"
        },
        {
          "line": 63,
          "level": 3,
          "title": "ACTION/AUTHORITY — portée d’action et reprise"
        },
        {
          "line": 69,
          "level": 3,
          "title": "Parcours minimal en cinq minutes"
        },
        {
          "line": 79,
          "level": 2,
          "title": "ACTION/FIRST-RENDER — qualité initiale attendue"
        },
        {
          "line": 93,
          "level": 3,
          "title": "ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble"
        },
        {
          "line": 116,
          "level": 2,
          "title": "ACTION/STATUS — états, issues et verdicts"
        },
        {
          "line": 120,
          "level": 3,
          "title": "États du run"
        },
        {
          "line": 134,
          "level": 3,
          "title": "Issues et exceptions"
        },
        {
          "line": 145,
          "level": 3,
          "title": "Règle de lecture des statuts"
        },
        {
          "line": 155,
          "level": 3,
          "title": "Chemin minimal"
        },
        {
          "line": 159,
          "level": 3,
          "title": "Principe positif de qualité"
        },
        {
          "line": 164,
          "level": 3,
          "title": "Verdicts V/U/A/T"
        },
        {
          "line": 177,
          "level": 3,
          "title": "Statut de direction"
        },
        {
          "line": 190,
          "level": 2,
          "title": "ACTION/PRECONDITION — mode, capacité et preuve"
        },
        {
          "line": 204,
          "level": 3,
          "title": "Contrat de décision et de preuve"
        },
        {
          "line": 220,
          "level": 3,
          "title": "Trace post-build de `DIRECTION/EXTERNAL-START`"
        },
        {
          "line": 232,
          "level": 3,
          "title": "Raccord de trace pour la section `DESIGN-ATLAS` de `SAVOIR.md`"
        },
        {
          "line": 242,
          "level": 2,
          "title": "ACTION/FAST-PATH — preuve minimale sans rituel"
        },
        {
          "line": 252,
          "level": 2,
          "title": "ACTION/RUN_CARD — carte de run minimale"
        },
        {
          "line": 282,
          "level": 3,
          "title": "Profil de capacités"
        },
        {
          "line": 288,
          "level": 3,
          "title": "Mode agent seul et preuve dégradée"
        },
        {
          "line": 301,
          "level": 3,
          "title": "Vue d’exécution dérivée"
        },
        {
          "line": 319,
          "level": 3,
          "title": "Projection machine-readable optionnelle"
        },
        {
          "line": 327,
          "level": 3,
          "title": "Frontière de validation et de preuve"
        },
        {
          "line": 335,
          "level": 2,
          "title": "ACTION/RUN — routes d’exécution"
        },
        {
          "line": 339,
          "level": 3,
          "title": "`ACTION/RUN-LITE`"
        },
        {
          "line": 349,
          "level": 3,
          "title": "`ACTION/RUN-ITER`"
        },
        {
          "line": 359,
          "level": 3,
          "title": "`ACTION/RUN-STANDARD`"
        },
        {
          "line": 369,
          "level": 3,
          "title": "`ACTION/RUN-DIRECTION`"
        },
        {
          "line": 379,
          "level": 3,
          "title": "`ACTION/RUN-SYSTEM`"
        },
        {
          "line": 391,
          "level": 2,
          "title": "ACTION/CLOSE-PACKAGE — paquet de clôture"
        },
        {
          "line": 407,
          "level": 3,
          "title": "Fraîcheur de la preuve"
        },
        {
          "line": 413,
          "level": 3,
          "title": "Cycle de vie des réserves"
        },
        {
          "line": 429,
          "level": 3,
          "title": "Responsabilité, droits et confidentialité"
        },
        {
          "line": 437,
          "level": 3,
          "title": "Condition d’arrêt du polish"
        },
        {
          "line": 443,
          "level": 2,
          "title": "ACTION/PIPELINE-DIRECTION — direction vérifiable"
        },
        {
          "line": 449,
          "level": 3,
          "title": "Boucle de qualité et branche one-shot"
        },
        {
          "line": 455,
          "level": 3,
          "title": "1. Situer les positions"
        },
        {
          "line": 461,
          "level": 3,
          "title": "2. Traduire l’émotion"
        },
        {
          "line": 467,
          "level": 3,
          "title": "3. Développer une alternative située"
        },
        {
          "line": 473,
          "level": 3,
          "title": "4. Produire la spec visuelle"
        },
        {
          "line": 485,
          "level": 3,
          "title": "5. Sourcer et tracer"
        },
        {
          "line": 493,
          "level": 3,
          "title": "6. Sélectionner contre la facilité"
        },
        {
          "line": 499,
          "level": 3,
          "title": "7. Écrire la direction et demander une décision si nécessaire"
        },
        {
          "line": 507,
          "level": 3,
          "title": "8. Vérifier le rendu réel"
        },
        {
          "line": 511,
          "level": 3,
          "title": "Passe créative et polish"
        },
        {
          "line": 527,
          "level": 2,
          "title": "ACTION/STRUCTURED-PROOF — contrats avant build"
        },
        {
          "line": 531,
          "level": 3,
          "title": "Carte de hiérarchie"
        },
        {
          "line": 558,
          "level": 3,
          "title": "Partition typographique"
        },
        {
          "line": 572,
          "level": 3,
          "title": "Fiche d’asset directeur"
        },
        {
          "line": 586,
          "level": 3,
          "title": "Contrat de composant et baseline"
        },
        {
          "line": 596,
          "level": 3,
          "title": "Contrat de motion ou scène spatiale"
        },
        {
          "line": 604,
          "level": 2,
          "title": "ACTION/VISUAL_PROOF — rendre la direction vérifiable"
        },
        {
          "line": 623,
          "level": 2,
          "title": "ACTION/GATE-A — plancher objectivable"
        },
        {
          "line": 627,
          "level": 3,
          "title": "Contrat de portée"
        },
        {
          "line": 644,
          "level": 3,
          "title": "Familles de méthodes"
        },
        {
          "line": 657,
          "level": 3,
          "title": "Adéquation des preuves"
        },
        {
          "line": 667,
          "level": 3,
          "title": "Contrôles applicables"
        },
        {
          "line": 690,
          "level": 2,
          "title": "ACTION/GATE-B — jugement contextualisé et risques"
        },
        {
          "line": 694,
          "level": 3,
          "title": "B1 — Comparaison relationnelle"
        },
        {
          "line": 702,
          "level": 3,
          "title": "B1b — Discrimination sur capture, requise dans son scope"
        },
        {
          "line": 708,
          "level": 4,
          "title": "Atelier d’édition — opération observable"
        },
        {
          "line": 722,
          "level": 3,
          "title": "B2 — Familles de preuve"
        },
        {
          "line": 735,
          "level": 3,
          "title": "B3 — Regard externe"
        },
        {
          "line": 755,
          "level": 3,
          "title": "B4 — Corrections ancrées"
        },
        {
          "line": 761,
          "level": 3,
          "title": "B5 — Trace d’assets et statut de direction"
        },
        {
          "line": 767,
          "level": 3,
          "title": "B6 — Format de sortie compact"
        },
        {
          "line": 775,
          "level": 2,
          "title": "ACTION/GATE-C — craft sur rendu réel"
        },
        {
          "line": 798,
          "level": 2,
          "title": "ACTION/ANTI-SLOP — conséquence de gate"
        },
        {
          "line": 806,
          "level": 2,
          "title": "ACTION/OVERRIDE — FAIL-ASSUMED et péremption"
        },
        {
          "line": 808,
          "level": 3,
          "title": "FAIL-ASSUMED"
        },
        {
          "line": 830,
          "level": 3,
          "title": "Péremption"
        },
        {
          "line": 840,
          "level": 2,
          "title": "ACTION/POLICIES — contraste et inspection"
        },
        {
          "line": 842,
          "level": 3,
          "title": "Politique de contraste"
        },
        {
          "line": 850,
          "level": 3,
          "title": "Inspection et ressources techniques"
        },
        {
          "line": 870,
          "level": 2,
          "title": "ACTION/ROUTING — prérequis de jugement et de structure"
        },
        {
          "line": 891,
          "level": 2,
          "title": "ACTION/MAINTENANCE — recette documentaire"
        },
        {
          "line": 915,
          "level": 2,
          "title": "ACTION/CLOSE-EXIT-CHECK — test de sortie canonique"
        },
        {
          "line": 932,
          "level": 3,
          "title": "Mesure expérimentale de la méthode"
        }
      ],
      "fences": [
        {
          "line": 27,
          "language": "text"
        },
        {
          "line": 99,
          "language": "text"
        },
        {
          "line": 208,
          "language": "text"
        },
        {
          "line": 214,
          "language": "text"
        },
        {
          "line": 224,
          "language": "text"
        },
        {
          "line": 305,
          "language": "text"
        },
        {
          "line": 417,
          "language": "text"
        },
        {
          "line": 545,
          "language": "text"
        },
        {
          "line": 631,
          "language": "text"
        },
        {
          "line": 745,
          "language": "text"
        },
        {
          "line": 818,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        14,
        42,
        55,
        84,
        123,
        137,
        169,
        180,
        195,
        259,
        293,
        396,
        563,
        611,
        647,
        660,
        670,
        727,
        786,
        875,
        896
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 3,
          "text": "**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. ACTION transforme une direction ou une décision produit en trace de run, artefacts observables, preuves adaptées, gates proportionnés et verdicts inspectables."
        },
        {
          "line": 43,
          "text": "| **Observation** | Qu’est-ce qui a été regardé, par quelle méthode, dans quel scope et quelle version ? | Artefact, méthode, scope, version, date et capacité. |"
        },
        {
          "line": 89,
          "text": "| `SYSTÈME` | Le composant ou token est montré dans ses usages réels, avec baseline, états, consommateurs et risque de régression identifiables. |"
        },
        {
          "line": 262,
          "text": "| `DATE / VERSION` | Date, version et contexte de preuve. |"
        },
        {
          "line": 276,
          "text": "Dans la projection JSON contrôlable, les noms composés sont sérialisés en `snake_case` : `DATE / VERSION` devient `date_version`, `DIRECTION-STATUS` devient `direction_status`, `TRACE-LOCATOR` devient `trace_locator`, `NEXT-PROOF` devient `next_proof` et `CAPABILITY-PROFILE` devient `capability_profile`. Cette sérialisation ne change pas la signification canonique des champs."
        },
        {
          "line": 409,
          "text": "Chaque verdict est rattaché à l’artefact, à la version, au scope et à l’état réellement observés. Après un changement substantiel qui touche l’axe couvert, ce verdict revient à `NOT-VERIFIED` jusqu’à réinspection, nouvelle preuve ou justification explicite que la modification est hors scope. Les axes non touchés conservent leur dernière preuve valide."
        },
        {
          "line": 411,
          "text": "Une preuve reste réutilisable lorsque l’artefact a seulement été déplacé ou relocalisé et que `TRACE-LOCATOR` permet de constater son identité et son absence de changement pertinent. Une capture, un test, une revue ou un avis portant sur une version antérieure ne peut jamais être cité comme preuve de la version livrée sans ce contrôle de fraîcheur."
        },
        {
          "line": 586,
          "text": "### Contrat de composant et baseline"
        },
        {
          "line": 588,
          "text": "Pour un nouveau pattern réutilisable ou un composant critique, documente : intention, non-usage, sémantique, clavier, focus, anatomie, slots, tokens, modes, variants, états pertinents, responsive, stories ou captures de baseline."
        },
        {
          "line": 590,
          "text": "Une baseline visuelle est une image versionnée d’un état réel. Elle signale un écart ; elle ne produit pas automatiquement un `PASS`."
        },
        {
          "line": 655,
          "text": "Pour un verdict global `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, la `RUN_CARD` doit rattacher la preuve observée à une provenance minimale : `artifact_locator`, `artifact_version`, `method` et `observed_at`. Cette provenance établit où, sur quelle version, par quelle méthode et à quel moment l’observation a été obtenue ; elle ne prouve pas à elle seule la véracité de l’artefact, la qualité du design ou la réussite d’usage. Si la provenance ne peut pas être établie, le verdict reste non accepté ou la limite est explicitement déclarée selon le mode et le risque."
        },
        {
          "line": 686,
          "text": "Les scripts et recettes sont des ressources versionnées. Une recette exécutée ne suffit pas à valider un résultat visuel, produit ou utilisateur."
        },
        {
          "line": 832,
          "text": "La péremption d’un claim, d’un outil, d’une watchlist ou d’une ressource déclenche une revue lorsque le livrable en dépend. La trace conserve type de claim ou de ressource, source, version, date de vérification, portée, limite, owner, date de revue et prochaine preuve."
        },
        {
          "line": 846,
          "text": "APCA peut être documenté comme mesure complémentaire de lisibilité ou d’exploration lorsque son contexte, sa version et sa limite sont connus. APCA ne remplace pas un critère WCAG applicable et ne crée pas seul un verdict réglementaire."
        },
        {
          "line": 852,
          "text": "Une inspection externe peut compléter le jugement sur l’accessibilité, la régression visuelle, les tokens et les motifs. Choisis l’outil selon l’environnement, sa documentation, sa version et son owner. Une commande, un package ou une intégration cités dans une ressource ne sont jamais exécutés aveuglément."
        },
        {
          "line": 856,
          "text": "- stack et version ;"
        },
        {
          "line": 866,
          "text": "Pour les composants critiques, maintiens une baseline d’états pertinents : variant, thème, viewport, données longues, loading, empty, error et focus lorsque nécessaires. Une capture versionnée et une revue explicite peuvent fournir une preuve proportionnée lorsqu’un pipeline de stories ou de tests visuels n’existe pas."
        },
        {
          "line": 901,
          "text": "| Claims datés | Source, version/date, portée, limite et prochaine preuve sont renseignées dans la trace locale quand le run en dépend. |"
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 7,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 7,
          "value": "ACTION/RUN"
        },
        {
          "line": 17,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 23,
          "value": "ACTION/HANDOFF"
        },
        {
          "line": 63,
          "value": "ACTION/AUTHORITY"
        },
        {
          "line": 71,
          "value": "DIRECTION/START"
        },
        {
          "line": 72,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 79,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 93,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 110,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 110,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 112,
          "value": "DIRECTION/START"
        },
        {
          "line": 116,
          "value": "ACTION/STATUS"
        },
        {
          "line": 190,
          "value": "ACTION/PRECONDITION"
        },
        {
          "line": 192,
          "value": "DIRECTION/START"
        },
        {
          "line": 220,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 222,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 242,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 252,
          "value": "ACTION/RUN_CARD"
        },
        {
          "line": 263,
          "value": "DIRECTION/START"
        },
        {
          "line": 335,
          "value": "ACTION/RUN"
        },
        {
          "line": 339,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 349,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 359,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 363,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 369,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 373,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 373,
          "value": "ACTION/VISUAL_PROOF"
        },
        {
          "line": 373,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 379,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 391,
          "value": "ACTION/CLOSE-PACKAGE"
        },
        {
          "line": 443,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 447,
          "value": "ACTION/GATE-B/B1"
        },
        {
          "line": 447,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 447,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 475,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 527,
          "value": "ACTION/STRUCTURED-PROOF"
        },
        {
          "line": 604,
          "value": "ACTION/VISUAL_PROOF"
        },
        {
          "line": 606,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 623,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 690,
          "value": "ACTION/GATE-B"
        },
        {
          "line": 775,
          "value": "ACTION/GATE-C"
        },
        {
          "line": 781,
          "value": "ACTION/GATE-B"
        },
        {
          "line": 798,
          "value": "ACTION/ANTI-SLOP"
        },
        {
          "line": 800,
          "value": "SAVOIR/CRAFT/CFT-01"
        },
        {
          "line": 802,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 806,
          "value": "ACTION/OVERRIDE"
        },
        {
          "line": 840,
          "value": "ACTION/POLICIES"
        },
        {
          "line": 848,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 870,
          "value": "ACTION/ROUTING"
        },
        {
          "line": 876,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 876,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 876,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 876,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 876,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 877,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 878,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 878,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 879,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 880,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 881,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 882,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 884,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 885,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 885,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 885,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 891,
          "value": "ACTION/MAINTENANCE"
        },
        {
          "line": 915,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "ACTION": 5,
        "LITE": 7,
        "STATUS": 4,
        "PRECONDITION": 2,
        "RUN-LITE": 1,
        "ITER": 9,
        "RUN-ITER": 1,
        "STANDARD": 6,
        "RUN-STANDARD": 1,
        "DIRECTION": 18,
        "RUN-DIRECTION": 1,
        "PIPELINE-DIRECTION": 1,
        "VISUAL_PROOF": 1,
        "RUN-SYSTEM": 1,
        "CHANGELOG": 1,
        "RUN_CARD": 20,
        "CLOSE-PACKAGE": 1,
        "CLOSE-EXIT-CHECK": 1,
        "FAST-PATH": 1,
        "STATE": 4,
        "ISSUE": 5,
        "P0": 1,
        "P1": 1,
        "P2": 1,
        "P3": 1,
        "APPROVED": 1,
        "DECISION-INTENT": 4,
        "DECISION-CHANGE": 9,
        "EXPLORATORY": 14,
        "NOT-VERIFIED": 19,
        "INTAKE": 2,
        "CLASSIFIED": 2,
        "SPECCED": 2,
        "BUILDING": 2,
        "CHECKING": 2,
        "DECIDED": 7,
        "CLOSED": 8,
        "RETURNED": 9,
        "BLOCKED": 3,
        "RETURN": 5,
        "SYSTEM-ESCALATION": 3,
        "RECLASSIFIED": 3,
        "FAIL-ASSUMED": 8,
        "ESCALATED": 9,
        "HELD": 4,
        "ACCEPTED": 5,
        "PASS": 11,
        "PASS-WITH-RESERVATION": 2,
        "ACCEPTED-WITH-RESERVATION": 6,
        "RETURN-DIRECTION": 5,
        "HELD-WITH-ACCEPTED-DIFFERENCE": 3,
        "PARTIALLY-HELD": 2,
        "LOST-IN-BUILD": 2,
        "NOT-OBSERVED": 3,
        "DESIGN-ATLAS": 3,
        "DECISION-MODIFIED": 1,
        "WHEN-USEFUL": 1,
        "COUNTERINDICATION": 1,
        "MEDIUM-SCOPE": 1,
        "PROOF-LIMIT": 1,
        "WHY-NOW": 1,
        "REUSE-CHALLENGE": 1,
        "ID": 1,
        "OWNER": 2,
        "MODE": 1,
        "VERDICT": 3,
        "DIRECTION-STATUS": 4,
        "DECISION": 1,
        "RISK": 1,
        "ARTIFACT": 2,
        "TRACE-LOCATOR": 3,
        "NEXT-PROOF": 6,
        "CAPABILITY-PROFILE": 2,
        "BASIS": 2,
        "EXECUTION-SNAPSHOT": 2,
        "SELF-DECLARED": 1,
        "ATLAS-PASS": 1,
        "POLISHED": 1,
        "SLOP-FREE": 1,
        "SAVOIR": 2,
        "BIBLIOTHEQUE": 2,
        "REMAINING-RISK": 2,
        "ANCHOR-GENERATED": 2,
        "ANCHOR-OBSERVED": 1,
        "ANCHOR-PROVIDED": 1,
        "VERIFIED-THIS-RUN": 1,
        "MODEL-KNOWLEDGE-NOT-RECHECKED": 1,
        "USER-SOURCED-NOT-RECHECKED": 1,
        "CODE-NATIVE": 2,
        "FOURNI": 2,
        "HYBRIDE": 2,
        "CORRECTED": 1,
        "ACCEPTED-DIFFERENCE": 1,
        "COVERAGE-LIMIT": 1,
        "CONFORMANCE-TARGET": 1,
        "AUTOMATED": 1,
        "MANUAL": 1,
        "EXPERT": 1,
        "USER": 1,
        "NARRATIVE-DIFFERENCE": 1,
        "REASON": 1,
        "PRODUCT-OR-PUBLIC-CONSTRAINT": 1,
        "EXIT-CONDITION": 1
      }
    },
    "V1/official/BIBLIOTHEQUE.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "BIBLIOTHEQUE — Structures d’interface situées"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Responsabilité"
        },
        {
          "line": 22,
          "level": 3,
          "title": "Entrée prioritaire — à lire avant le catalogue"
        },
        {
          "line": 35,
          "level": 3,
          "title": "Orientation interne et sortie de sélection"
        },
        {
          "line": 43,
          "level": 3,
          "title": "Charges de lecture à ne pas confondre"
        },
        {
          "line": 54,
          "level": 3,
          "title": "Contrat minimal par périmètre de contribution et statut de route"
        },
        {
          "line": 70,
          "level": 2,
          "title": "BIBLIOTHEQUE/READ — responsabilités et convention de route"
        },
        {
          "line": 82,
          "level": 3,
          "title": "Lecture expressive de la structure"
        },
        {
          "line": 88,
          "level": 3,
          "title": "BIBLIOTHEQUE/TENSION — diverger avant de sélectionner"
        },
        {
          "line": 106,
          "level": 3,
          "title": "BIBLIOTHEQUE/SIGNATURE — rendre l’écart vérifiable"
        },
        {
          "line": 119,
          "level": 3,
          "title": "Thèse structurelle et premier objet habitable"
        },
        {
          "line": 129,
          "level": 3,
          "title": "Préfixes canoniques"
        },
        {
          "line": 144,
          "level": 3,
          "title": "Types de preuve"
        },
        {
          "line": 161,
          "level": 2,
          "title": "BIBLIOTHEQUE/SELECT — choisir avant de composer"
        },
        {
          "line": 169,
          "level": 3,
          "title": "BIBLIOTHEQUE/FAST-PATH — vérifier avant de sélectionner"
        },
        {
          "line": 175,
          "level": 3,
          "title": "Question de sélection"
        },
        {
          "line": 189,
          "level": 3,
          "title": "Sélection par mode"
        },
        {
          "line": 201,
          "level": 3,
          "title": "One-shot et boucle structurelle"
        },
        {
          "line": 207,
          "level": 3,
          "title": "Garde-fou de dérivation"
        },
        {
          "line": 215,
          "level": 3,
          "title": "BIBLIOTHEQUE/DERIVE — inventer sans fabriquer un menu"
        },
        {
          "line": 239,
          "level": 3,
          "title": "Signaux de convergence structurelle"
        },
        {
          "line": 256,
          "level": 2,
          "title": "BIBLIOTHEQUE/CONTRACTS — contrat commun de route"
        },
        {
          "line": 288,
          "level": 2,
          "title": "BIBLIOTHEQUE/SUPPORT — où la surface vit"
        },
        {
          "line": 292,
          "level": 3,
          "title": "`SUPPORT/FREE_FIELD`"
        },
        {
          "line": 302,
          "level": 3,
          "title": "`SUPPORT/ARCHITECTED_FRAME`"
        },
        {
          "line": 312,
          "level": 3,
          "title": "`SUPPORT/OPERATIONAL_CANVAS`"
        },
        {
          "line": 322,
          "level": 3,
          "title": "`SUPPORT/COLLECTION_PLINTH`"
        },
        {
          "line": 332,
          "level": 3,
          "title": "Test de support"
        },
        {
          "line": 340,
          "level": 2,
          "title": "BIBLIOTHEQUE/GRID — comment le regard circule"
        },
        {
          "line": 344,
          "level": 3,
          "title": "`GRID/MODULAR`"
        },
        {
          "line": 352,
          "level": 3,
          "title": "`GRID/COLUMN`"
        },
        {
          "line": 360,
          "level": 3,
          "title": "`GRID/RADIAL`"
        },
        {
          "line": 368,
          "level": 3,
          "title": "`GRID/HIERARCHICAL`"
        },
        {
          "line": 376,
          "level": 3,
          "title": "`GRID/BASELINE`"
        },
        {
          "line": 384,
          "level": 3,
          "title": "`GRID/AXIAL`"
        },
        {
          "line": 392,
          "level": 3,
          "title": "Contrat de grille"
        },
        {
          "line": 425,
          "level": 2,
          "title": "BIBLIOTHEQUE/SCENE — comment la promesse devient une surface"
        },
        {
          "line": 431,
          "level": 3,
          "title": "`SCENE/INSTRUMENT`"
        },
        {
          "line": 441,
          "level": 3,
          "title": "`SCENE/EDITORIAL_FIELD`"
        },
        {
          "line": 451,
          "level": 3,
          "title": "`SCENE/FRAMED_PRODUCT`"
        },
        {
          "line": 461,
          "level": 3,
          "title": "`SCENE/OPERATING_GRID`"
        },
        {
          "line": 471,
          "level": 3,
          "title": "`SCENE/SPLIT_PROOF`"
        },
        {
          "line": 481,
          "level": 3,
          "title": "`SCENE/PRODUCT_NARRATIVE`"
        },
        {
          "line": 491,
          "level": 3,
          "title": "Test de scène"
        },
        {
          "line": 501,
          "level": 2,
          "title": "BIBLIOTHEQUE/OBJECT — quelle preuve devient tangible"
        },
        {
          "line": 505,
          "level": 3,
          "title": "Routes d’objet"
        },
        {
          "line": 519,
          "level": 3,
          "title": "Contrat d’objet"
        },
        {
          "line": 542,
          "level": 2,
          "title": "BIBLIOTHEQUE/MICRO — unités denses"
        },
        {
          "line": 562,
          "level": 3,
          "title": "Before-after"
        },
        {
          "line": 585,
          "level": 2,
          "title": "BIBLIOTHEQUE/MODIFIER — comportements transversaux"
        },
        {
          "line": 589,
          "level": 3,
          "title": "`MODIFIER/FIELD_SWITCH`"
        },
        {
          "line": 595,
          "level": 3,
          "title": "`MODIFIER/NAVIGATION_SHELL`"
        },
        {
          "line": 601,
          "level": 3,
          "title": "`MODIFIER/PRINT_FIELD`"
        },
        {
          "line": 611,
          "level": 2,
          "title": "BIBLIOTHEQUE/COMPONENTS — couches et dépendances"
        },
        {
          "line": 622,
          "level": 3,
          "title": "Échelle de responsabilité"
        },
        {
          "line": 661,
          "level": 2,
          "title": "BIBLIOTHEQUE/COMPAT — combiner avec une raison"
        },
        {
          "line": 689,
          "level": 3,
          "title": "Contrat de compatibilité"
        },
        {
          "line": 697,
          "level": 2,
          "title": "BIBLIOTHEQUE/GATE — contrôle de module structurel complémentaire"
        },
        {
          "line": 721,
          "level": 3,
          "title": "Statut ACTION du contrôle structurel"
        },
        {
          "line": 733,
          "level": 2,
          "title": "BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation"
        },
        {
          "line": 737,
          "level": 3,
          "title": "Contrat de gain réel"
        },
        {
          "line": 764,
          "level": 3,
          "title": "Contribution et retour d’usage"
        },
        {
          "line": 776,
          "level": 2,
          "title": "Test de sortie BIBLIOTHEQUE"
        }
      ],
      "fences": [
        {
          "line": 92,
          "language": "text"
        },
        {
          "line": 110,
          "language": "text"
        },
        {
          "line": 219,
          "language": "text"
        },
        {
          "line": 566,
          "language": "text"
        },
        {
          "line": 633,
          "language": "text"
        },
        {
          "line": 665,
          "language": "text"
        },
        {
          "line": 741,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        16,
        57,
        132,
        149,
        178,
        192,
        244,
        263,
        418,
        508,
        524,
        553,
        614,
        625,
        677,
        706,
        754
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 3,
          "text": "**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. BIBLIOTHEQUE sélectionne les responsabilités structurelles — support, grille, scène, objet, micro-interface, modificateur, primitive et couche — puis les encadre par des contrats transversaux (`BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/COMPAT`)."
        },
        {
          "line": 61,
          "text": "| Durable | Usages contrastés, baseline, observation ou mesure de gain, maintenance, owner et prochaine revue. | Validation par beauté, fréquence ou screenshot unique. |"
        },
        {
          "line": 203,
          "text": "Le `one-shot` est une stratégie de préparation, pas une absence de jugement. Après sélection, compose un premier objet complet, observe-le réellement et ferme seulement si la thèse structurelle, la composition, la spécificité, les états et les risques applicables tiennent déjà. Il ne contourne ni les gates, ni les statuts, ni `ACTION/CLOSE-EXIT-CHECK` ; une observation positive de craft ne prouve pas à elle seule usage, technique, accessibilité ou performance. Si une relation dominante échoue, retourne ou corrige ; ne produis pas une seconde version décorative lorsque l’observation ne promet aucun gain réel."
        },
        {
          "line": 277,
          "text": "| Revue | Quels usages contrastés, baseline, observation ou mesure ont été réalisés, avec quelle limite et quand la route sera-t-elle revue ? |"
        },
        {
          "line": 376,
          "text": "### `GRID/BASELINE`"
        },
        {
          "line": 411,
          "text": "Les valeurs comme « 12 colonnes » ou « baseline 8 » sont des points de départ adaptables, jamais des validations universelles. `MOBILE-STATE`, `MOBILE-CONTENT` et `MOBILE-PERFORMANCE` sont conditionnels au risque : renseigne-les lorsque la grille porte directement une décision d’état, de contenu ou de performance ; sinon conserve la responsabilité dans la scène, l’objet ou `SAVOIR/CONTEXT` et justifie le périmètre, le scope et la prochaine preuve."
        },
        {
          "line": 516,
          "text": "| `OBJECT/CONVERSION_CONTEXT_FIELD` | Promesse entourée d’artefacts de travail réellement contextualisés lorsque le monde concret du visiteur crédibilise la conversion. |"
        },
        {
          "line": 533,
          "text": "| Test | Observation, capture, scénario ou résultat attendu, avec `SCOPE`, `METHOD`, `OWNER`, `TRACE-LOCATOR` et date/version lorsque pertinents. |"
        },
        {
          "line": 560,
          "text": "| `MICRO/USAGE_LEDGER` | Crédits, quotas, consommation ou budget guidant une décision. | Valeur, unité, plafond, période, prévision et conséquence du dépassement. |"
        },
        {
          "line": 577,
          "text": "Il est accepté uniquement si la version après réduit une ambiguïté, préserve les états critiques et rend une décision plus directe sans exiger davantage d’attention. La preuve se rattache au gate ACTION applicable et à la méthode déclarée ; lorsque la compréhension ou l’usage domine, une tâche utilisateur est requise dans le scope déclaré."
        },
        {
          "line": 581,
          "text": "Une micro-route devient durable seulement lorsqu’elle possède plusieurs usages contrastés, un contrat réutilisable, un owner de maintenance, une preuve de gain avec baseline et limite, une compatibilité, une prochaine revue et un statut de cycle de vie ; la promotion passe par `BIBLIOTHEQUE/EVOLUTION` puis `CHANGELOG`."
        },
        {
          "line": 678,
          "text": "| `SUPPORT/FREE_FIELD` | `GRID/HIERARCHICAL`, `GRID/RADIAL`, `GRID/BASELINE` | `OBJECT/MEDIA_ARCHIVE`, `OBJECT/EDITORIAL_SELECTION`, `OBJECT/NAV_CONTEXT_CAPSULE` | Foyer ou cadence conservé ; pas de collection égale sans raison. |"
        },
        {
          "line": 679,
          "text": "| `SUPPORT/ARCHITECTED_FRAME` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/PROOF_PRODUCT_STAGE`, `OBJECT/NAV_CONTEXT_CAPSULE` | Cadre renforce usage ou preuve, pas seulement prestige. |"
        },
        {
          "line": 680,
          "text": "| `SUPPORT/OPERATIONAL_CANVAS` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/SYSTEM_DATA_MODULE`, `OBJECT/COMPARISON_SPLIT`, `MICRO/QUERY_HEALTH` | Aucun décor ne masque les lectures de même importance. |"
        },
        {
          "line": 681,
          "text": "| `SUPPORT/COLLECTION_PLINTH` | `GRID/MODULAR`, `GRID/HIERARCHICAL`, `GRID/BASELINE` | `OBJECT/MEDIA_ARCHIVE`, `OBJECT/EDITORIAL_SELECTION` | Foyer ponctuel, comparaison encore possible. |"
        },
        {
          "line": 682,
          "text": "| `SCENE/INSTRUMENT` | `GRID/COLUMN`, `GRID/BASELINE`, `GRID/MODULAR` | `OBJECT/SYSTEM_DATA_MODULE`, `MICRO/QUERY_HEALTH`, `MICRO/ENTITY_STATUS_RAIL` | Décision et mesure avant récit d’écosystème. |"
        },
        {
          "line": 683,
          "text": "| `SCENE/EDITORIAL_FIELD` | `GRID/HIERARCHICAL`, `GRID/RADIAL`, `GRID/BASELINE` | `OBJECT/EDITORIAL_SELECTION`, `OBJECT/MEDIA_ARCHIVE`, `OBJECT/PROOF_PRODUCT_STAGE` | Image ou paysage porte une relation ; preuve produit explicite. |"
        },
        {
          "line": 684,
          "text": "| `SCENE/FRAMED_PRODUCT` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/PROOF_PRODUCT_STAGE`, `OBJECT/NAV_CONTEXT_CAPSULE` | Châssis renforce usage et confiance. |"
        },
        {
          "line": 685,
          "text": "| `SCENE/OPERATING_GRID` | `GRID/MODULAR`, `GRID/COLUMN`, `GRID/BASELINE` | `OBJECT/SYSTEM_DATA_MODULE`, `MICRO/QUERY_HEALTH`, `MICRO/ENTITY_STATUS_RAIL` | Ruptures réservées à action ou alerte prioritaire. |"
        },
        {
          "line": 735,
          "text": "BIBLIOTHEQUE est stable dans ses responsabilités, mais pilotée dans ses routes. Une route devient durable après plusieurs usages contrastés documentés, lorsque sa responsabilité reste stable, son contrat est complet, sa maintenance est assumée, ses rendus ne s’homogénéisent pas et un gain réel est observé ou mesuré avec baseline, contexte et limite. Elle doit également démontrer qu’elle permet des premiers objets composés, spécifiques et crédibles dans ces contextes, et pas seulement des structures conformes ou jolies dans un screenshot."
        },
        {
          "line": 758,
          "text": "| Gain réel | Tâche/baseline/observation ou mesure/contexte/limite. |"
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 3,
          "value": "BIBLIOTHEQUE/COMPAT"
        },
        {
          "line": 3,
          "value": "BIBLIOTHEQUE/CONTRACTS"
        },
        {
          "line": 11,
          "value": "DIRECTION/START"
        },
        {
          "line": 31,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 31,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 31,
          "value": "DIRECTION/START"
        },
        {
          "line": 37,
          "value": "BIBLIOTHEQUE/READ"
        },
        {
          "line": 37,
          "value": "DIRECTION/START"
        },
        {
          "line": 37,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 70,
          "value": "BIBLIOTHEQUE/READ"
        },
        {
          "line": 88,
          "value": "BIBLIOTHEQUE/TENSION"
        },
        {
          "line": 106,
          "value": "BIBLIOTHEQUE/SIGNATURE"
        },
        {
          "line": 139,
          "value": "LAYER/PRIMITIVES"
        },
        {
          "line": 161,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 163,
          "value": "DIRECTION/START"
        },
        {
          "line": 163,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 167,
          "value": "DIRECTION/START"
        },
        {
          "line": 169,
          "value": "BIBLIOTHEQUE/FAST-PATH"
        },
        {
          "line": 187,
          "value": "OBJECT/COMPARISON_SPLIT"
        },
        {
          "line": 187,
          "value": "OBJECT/EDITORIAL_SELECTION"
        },
        {
          "line": 187,
          "value": "OBJECT/MEDIA_ARCHIVE"
        },
        {
          "line": 197,
          "value": "LAYER/OBJECTS"
        },
        {
          "line": 197,
          "value": "LAYER/PRIMITIVES"
        },
        {
          "line": 197,
          "value": "LAYER/SCENES"
        },
        {
          "line": 197,
          "value": "LAYER/TOKENS"
        },
        {
          "line": 203,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        },
        {
          "line": 209,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 215,
          "value": "BIBLIOTHEQUE/DERIVE"
        },
        {
          "line": 237,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 237,
          "value": "SCENE/BENTO"
        },
        {
          "line": 237,
          "value": "SCENE/EDITORIAL_PREMIUM"
        },
        {
          "line": 237,
          "value": "SCENE/GLASS_HERO"
        },
        {
          "line": 256,
          "value": "BIBLIOTHEQUE/CONTRACTS"
        },
        {
          "line": 288,
          "value": "BIBLIOTHEQUE/SUPPORT"
        },
        {
          "line": 292,
          "value": "SUPPORT/FREE_FIELD"
        },
        {
          "line": 302,
          "value": "SUPPORT/ARCHITECTED_FRAME"
        },
        {
          "line": 312,
          "value": "SUPPORT/OPERATIONAL_CANVAS"
        },
        {
          "line": 322,
          "value": "SUPPORT/COLLECTION_PLINTH"
        },
        {
          "line": 340,
          "value": "BIBLIOTHEQUE/GRID"
        },
        {
          "line": 344,
          "value": "GRID/MODULAR"
        },
        {
          "line": 352,
          "value": "GRID/COLUMN"
        },
        {
          "line": 360,
          "value": "GRID/RADIAL"
        },
        {
          "line": 368,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 376,
          "value": "GRID/BASELINE"
        },
        {
          "line": 384,
          "value": "GRID/AXIAL"
        },
        {
          "line": 411,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 425,
          "value": "BIBLIOTHEQUE/SCENE"
        },
        {
          "line": 431,
          "value": "SCENE/INSTRUMENT"
        },
        {
          "line": 439,
          "value": "MICRO/QUERY_HEALTH"
        },
        {
          "line": 439,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 439,
          "value": "SCENE/INSTRUMENT"
        },
        {
          "line": 441,
          "value": "SCENE/EDITORIAL_FIELD"
        },
        {
          "line": 449,
          "value": "SCENE/EDITORIAL_FIELD"
        },
        {
          "line": 449,
          "value": "SUPPORT/FREE_FIELD"
        },
        {
          "line": 451,
          "value": "SCENE/FRAMED_PRODUCT"
        },
        {
          "line": 459,
          "value": "SCENE/FRAMED_PRODUCT"
        },
        {
          "line": 459,
          "value": "SUPPORT/ARCHITECTED_FRAME"
        },
        {
          "line": 461,
          "value": "SCENE/OPERATING_GRID"
        },
        {
          "line": 469,
          "value": "SCENE/OPERATING_GRID"
        },
        {
          "line": 469,
          "value": "SUPPORT/OPERATIONAL_CANVAS"
        },
        {
          "line": 471,
          "value": "SCENE/SPLIT_PROOF"
        },
        {
          "line": 479,
          "value": "OBJECT/COMPARISON_SPLIT"
        },
        {
          "line": 479,
          "value": "SCENE/SPLIT_PROOF"
        },
        {
          "line": 481,
          "value": "SCENE/PRODUCT_NARRATIVE"
        },
        {
          "line": 489,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 489,
          "value": "SCENE/PRODUCT_NARRATIVE"
        },
        {
          "line": 501,
          "value": "BIBLIOTHEQUE/OBJECT"
        },
        {
          "line": 509,
          "value": "OBJECT/EDITORIAL_SELECTION"
        },
        {
          "line": 510,
          "value": "OBJECT/COMPARISON_SPLIT"
        },
        {
          "line": 511,
          "value": "OBJECT/MEDIA_ARCHIVE"
        },
        {
          "line": 512,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 513,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 514,
          "value": "OBJECT/NAV_CONTEXT_CAPSULE"
        },
        {
          "line": 515,
          "value": "OBJECT/BRAND_GRAMMAR_PLATE"
        },
        {
          "line": 516,
          "value": "OBJECT/CONVERSION_CONTEXT_FIELD"
        },
        {
          "line": 517,
          "value": "OBJECT/CONTROL_VALUE_TILE"
        },
        {
          "line": 542,
          "value": "BIBLIOTHEQUE/MICRO"
        },
        {
          "line": 554,
          "value": "MICRO/IDENTIFICATION_GATE"
        },
        {
          "line": 555,
          "value": "MICRO/SETTINGS_GROUP"
        },
        {
          "line": 556,
          "value": "MICRO/PROFILE_EVIDENCE"
        },
        {
          "line": 557,
          "value": "MICRO/QUERY_HEALTH"
        },
        {
          "line": 558,
          "value": "MICRO/ENTITY_STATUS_RAIL"
        },
        {
          "line": 559,
          "value": "MICRO/ITINERARY_SEGMENTS"
        },
        {
          "line": 560,
          "value": "MICRO/USAGE_LEDGER"
        },
        {
          "line": 579,
          "value": "ACTION/GATE-B/B1"
        },
        {
          "line": 581,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 585,
          "value": "BIBLIOTHEQUE/MODIFIER"
        },
        {
          "line": 589,
          "value": "MODIFIER/FIELD_SWITCH"
        },
        {
          "line": 595,
          "value": "MODIFIER/NAVIGATION_SHELL"
        },
        {
          "line": 601,
          "value": "MODIFIER/PRINT_FIELD"
        },
        {
          "line": 611,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 615,
          "value": "LAYER/TOKENS"
        },
        {
          "line": 616,
          "value": "LAYER/BRAND_GRAMMAR"
        },
        {
          "line": 617,
          "value": "LAYER/PRIMITIVES"
        },
        {
          "line": 618,
          "value": "LAYER/OBJECTS"
        },
        {
          "line": 619,
          "value": "LAYER/SCENES"
        },
        {
          "line": 620,
          "value": "LAYER/TEMPLATES"
        },
        {
          "line": 631,
          "value": "LAYER/BRAND_GRAMMAR"
        },
        {
          "line": 661,
          "value": "BIBLIOTHEQUE/COMPAT"
        },
        {
          "line": 678,
          "value": "GRID/BASELINE"
        },
        {
          "line": 678,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 678,
          "value": "GRID/RADIAL"
        },
        {
          "line": 678,
          "value": "OBJECT/EDITORIAL_SELECTION"
        },
        {
          "line": 678,
          "value": "OBJECT/MEDIA_ARCHIVE"
        },
        {
          "line": 678,
          "value": "OBJECT/NAV_CONTEXT_CAPSULE"
        },
        {
          "line": 678,
          "value": "SUPPORT/FREE_FIELD"
        },
        {
          "line": 679,
          "value": "GRID/BASELINE"
        },
        {
          "line": 679,
          "value": "GRID/COLUMN"
        },
        {
          "line": 679,
          "value": "GRID/MODULAR"
        },
        {
          "line": 679,
          "value": "OBJECT/NAV_CONTEXT_CAPSULE"
        },
        {
          "line": 679,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 679,
          "value": "SUPPORT/ARCHITECTED_FRAME"
        },
        {
          "line": 680,
          "value": "GRID/BASELINE"
        },
        {
          "line": 680,
          "value": "GRID/COLUMN"
        },
        {
          "line": 680,
          "value": "GRID/MODULAR"
        },
        {
          "line": 680,
          "value": "MICRO/QUERY_HEALTH"
        },
        {
          "line": 680,
          "value": "OBJECT/COMPARISON_SPLIT"
        },
        {
          "line": 680,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 680,
          "value": "SUPPORT/OPERATIONAL_CANVAS"
        },
        {
          "line": 681,
          "value": "GRID/BASELINE"
        },
        {
          "line": 681,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 681,
          "value": "GRID/MODULAR"
        },
        {
          "line": 681,
          "value": "OBJECT/EDITORIAL_SELECTION"
        },
        {
          "line": 681,
          "value": "OBJECT/MEDIA_ARCHIVE"
        },
        {
          "line": 681,
          "value": "SUPPORT/COLLECTION_PLINTH"
        },
        {
          "line": 682,
          "value": "GRID/BASELINE"
        },
        {
          "line": 682,
          "value": "GRID/COLUMN"
        },
        {
          "line": 682,
          "value": "GRID/MODULAR"
        },
        {
          "line": 682,
          "value": "MICRO/ENTITY_STATUS_RAIL"
        },
        {
          "line": 682,
          "value": "MICRO/QUERY_HEALTH"
        },
        {
          "line": 682,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 682,
          "value": "SCENE/INSTRUMENT"
        },
        {
          "line": 683,
          "value": "GRID/BASELINE"
        },
        {
          "line": 683,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 683,
          "value": "GRID/RADIAL"
        },
        {
          "line": 683,
          "value": "OBJECT/EDITORIAL_SELECTION"
        },
        {
          "line": 683,
          "value": "OBJECT/MEDIA_ARCHIVE"
        },
        {
          "line": 683,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 683,
          "value": "SCENE/EDITORIAL_FIELD"
        },
        {
          "line": 684,
          "value": "GRID/BASELINE"
        },
        {
          "line": 684,
          "value": "GRID/COLUMN"
        },
        {
          "line": 684,
          "value": "GRID/MODULAR"
        },
        {
          "line": 684,
          "value": "OBJECT/NAV_CONTEXT_CAPSULE"
        },
        {
          "line": 684,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 684,
          "value": "SCENE/FRAMED_PRODUCT"
        },
        {
          "line": 685,
          "value": "GRID/BASELINE"
        },
        {
          "line": 685,
          "value": "GRID/COLUMN"
        },
        {
          "line": 685,
          "value": "GRID/MODULAR"
        },
        {
          "line": 685,
          "value": "MICRO/ENTITY_STATUS_RAIL"
        },
        {
          "line": 685,
          "value": "MICRO/QUERY_HEALTH"
        },
        {
          "line": 685,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 685,
          "value": "SCENE/OPERATING_GRID"
        },
        {
          "line": 686,
          "value": "GRID/AXIAL"
        },
        {
          "line": 686,
          "value": "GRID/COLUMN"
        },
        {
          "line": 686,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 686,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 686,
          "value": "OBJECT/SYSTEM_DATA_MODULE"
        },
        {
          "line": 686,
          "value": "SCENE/SPLIT_PROOF"
        },
        {
          "line": 687,
          "value": "GRID/COLUMN"
        },
        {
          "line": 687,
          "value": "GRID/HIERARCHICAL"
        },
        {
          "line": 687,
          "value": "GRID/MODULAR"
        },
        {
          "line": 687,
          "value": "MICRO/PROFILE_EVIDENCE"
        },
        {
          "line": 687,
          "value": "OBJECT/PROOF_PRODUCT_STAGE"
        },
        {
          "line": 687,
          "value": "SCENE/PRODUCT_NARRATIVE"
        },
        {
          "line": 691,
          "value": "BIBLIOTHEQUE/CONTRACTS"
        },
        {
          "line": 693,
          "value": "BIBLIOTHEQUE/GATE"
        },
        {
          "line": 697,
          "value": "BIBLIOTHEQUE/GATE"
        },
        {
          "line": 699,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 699,
          "value": "ACTION/GATE-B"
        },
        {
          "line": 699,
          "value": "ACTION/GATE-C"
        },
        {
          "line": 701,
          "value": "BIBLIOTHEQUE/GATE"
        },
        {
          "line": 703,
          "value": "DIRECTION/START"
        },
        {
          "line": 719,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 719,
          "value": "BIBLIOTHEQUE/GATE"
        },
        {
          "line": 733,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 770,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 770,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 770,
          "value": "DIRECTION/START"
        },
        {
          "line": 772,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 790,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "CHANGELOG": 9,
        "SELECT": 1,
        "DECISION": 2,
        "STRUCTURAL-SIGNATURE": 2,
        "MODE": 2,
        "RISK": 2,
        "SCOPE": 4,
        "ARTIFACT": 2,
        "DECISION-CHANGE": 8,
        "NEXT-ACTION": 2,
        "OWNER": 5,
        "NEXT-PROOF": 3,
        "EXIT-CONDITION": 4,
        "STARTUP-NOMINAL": 1,
        "CONDITIONAL-READ": 1,
        "AUDIT-READ": 1,
        "ACTUAL-READ": 1,
        "PILOT": 5,
        "ADOPTED": 3,
        "DEPRECATED": 3,
        "ABANDONED": 2,
        "ACTION": 4,
        "NEXT-OWNER": 1,
        "TENSION-AXES": 1,
        "SELECTED-POLE": 1,
        "DECISION-IMPACT": 1,
        "NEXT-OBSERVATION": 1,
        "PROOF-POSITION": 1,
        "DIRECTION": 4,
        "STRUCTURAL-THESIS": 1,
        "OBSERVABLE-CONSEQUENCE": 1,
        "FIRST-OBJECT": 1,
        "PERCEPTUAL": 8,
        "EXPERT": 11,
        "TECHNICAL": 6,
        "AUTOMATED": 1,
        "MANUAL": 1,
        "USER": 1,
        "SAVOIR": 1,
        "GRID": 3,
        "SCENE": 2,
        "OBJECT": 1,
        "MICRO": 2,
        "SUPPORT": 2,
        "RUN_CARD": 4,
        "PRINT_FIELD": 1,
        "PROOF-TYPE": 3,
        "PROOF-SCOPE": 1,
        "PROOF-LIMIT": 4,
        "PASS": 4,
        "PASS-WITH-RESERVATION": 2,
        "RETURN": 3,
        "NOT-VERIFIED": 3,
        "UNIT": 1,
        "ANCHORS": 1,
        "RHYTHM": 1,
        "FOCUS": 1,
        "MOBILE-PRIORITY": 1,
        "MOBILE-NEIGHBORHOOD": 1,
        "MOBILE-ACTION": 1,
        "MOBILE-STATE": 2,
        "MOBILE-CONTENT": 2,
        "MOBILE-PERFORMANCE": 2,
        "MOBILE-COVERAGE-LIMIT": 1,
        "METHOD": 1,
        "TRACE-LOCATOR": 1,
        "OWNER-SCOPE": 1,
        "CONSUMERS": 1,
        "MOBILE": 1,
        "A11Y": 1,
        "COMPATIBILITY": 1,
        "MIGRATION": 1,
        "ROLLBACK": 1,
        "ADOPTION-STATUS": 1,
        "NEXT-REVIEW": 1,
        "BRAND_GRAMMAR": 1,
        "COMPAT": 1,
        "EXPLORATORY": 1,
        "RETURNED": 1
      }
    },
    "V1/official/CHANGELOG.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Changelog — Design Governance V1.0.0"
        },
        {
          "line": 8,
          "level": 2,
          "title": "V1.0.0 — Baseline expérimentale"
        },
        {
          "line": 23,
          "level": 2,
          "title": "Autorité et maintenance"
        },
        {
          "line": 31,
          "level": 2,
          "title": "Cycle de vie des routes"
        },
        {
          "line": 44,
          "level": 2,
          "title": "Migration des anciens aliases"
        },
        {
          "line": 58,
          "level": 2,
          "title": "Limites de la baseline"
        }
      ],
      "fences": [],
      "table_separator_lines": [
        36,
        49
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 3,
          "text": "**Version publique :** `V1.0.0`  "
        },
        {
          "line": 5,
          "text": "**Date de publication :** 2026-09-19  "
        },
        {
          "line": 8,
          "text": "## V1.0.0 — Baseline expérimentale"
        },
        {
          "line": 10,
          "text": "Design Governance V1.0.0 est une baseline publique cohérente pour diriger, construire, juger et vérifier un travail de design. Elle transforme un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque."
        },
        {
          "line": 12,
          "text": "La baseline comprend :"
        },
        {
          "line": 27,
          "text": "Toute évolution de la baseline doit identifier une source normative unique, un propriétaire, le périmètre concerné, la compatibilité, la preuve attendue, la limite, la prochaine revue et la procédure de retour. Une évolution ne devient une règle transversale qu’après décision explicite du propriétaire du corpus."
        },
        {
          "line": 42,
          "text": "Les routes présentes dans le seed de la V1 constituent la baseline canonique. Toute nouvelle route ou promotion doit indiquer son problème, sa décision, son owner, son contrat, sa preuve, sa limite, sa compatibilité et sa prochaine revue."
        },
        {
          "line": 58,
          "text": "## Limites de la baseline"
        },
        {
          "line": 62,
          "text": "La baseline reste expérimentale. Toute conclusion d’usage doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite."
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 50,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 51,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 52,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 52,
          "value": "SAVOIR/SOURCE"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "RUN_CARD": 3,
        "NOT-VERIFIED": 2,
        "PILOT": 1,
        "ADOPTED": 2,
        "ABANDONED": 3,
        "DEPRECATED": 2,
        "TRACE-LOCATOR": 1,
        "CHANGELOG": 1,
        "EXPLORATORY": 1
      }
    },
    "V1/official/DIRECTION.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "DIRECTION — Cadre de décision et de design situé"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Constitution du document"
        },
        {
          "line": 19,
          "level": 3,
          "title": "Frontière de responsabilité"
        },
        {
          "line": 23,
          "level": 3,
          "title": "Orientation interne et sortie"
        },
        {
          "line": 31,
          "level": 3,
          "title": "Trois contrats à ne pas mélanger"
        },
        {
          "line": 41,
          "level": 3,
          "title": "Architecture d’activation"
        },
        {
          "line": 57,
          "level": 3,
          "title": "Carte de lecture canonique et chemin en trente secondes"
        },
        {
          "line": 92,
          "level": 3,
          "title": "Comment lire les taxonomies"
        },
        {
          "line": 96,
          "level": 3,
          "title": "Légende"
        },
        {
          "line": 113,
          "level": 2,
          "title": "DIRECTION/SERVICE-BOUNDARY — ne pas confondre relation et contrat"
        },
        {
          "line": 119,
          "level": 2,
          "title": "DIRECTION/START — classer avant d’agir"
        },
        {
          "line": 127,
          "level": 3,
          "title": "Arbre de classification"
        },
        {
          "line": 146,
          "level": 3,
          "title": "Entrée minimale"
        },
        {
          "line": 161,
          "level": 3,
          "title": "DIRECTION/CREATIVE-BOOT — activer la boucle avant le premier pixel"
        },
        {
          "line": 188,
          "level": 3,
          "title": "DIRECTION/DOMAIN-FRAME — adapter le design au domaine"
        },
        {
          "line": 217,
          "level": 3,
          "title": "Sortie immédiate"
        },
        {
          "line": 235,
          "level": 3,
          "title": "Mémoire de lancement et renvoi de `RUN_CARD`"
        },
        {
          "line": 245,
          "level": 2,
          "title": "DIRECTION/DAILY — charger proportionnellement"
        },
        {
          "line": 263,
          "level": 3,
          "title": "DIRECTION/FAST-PATH — encadré d’exécution courte"
        },
        {
          "line": 278,
          "level": 2,
          "title": "DIRECTION/EXTERNAL-START — activation portable sur brief vague"
        },
        {
          "line": 300,
          "level": 3,
          "title": "DIRECTION/START — traduction humaine minimale"
        },
        {
          "line": 314,
          "level": 2,
          "title": "DIRECTION/FIRST-OBJECT — compiler le brief et produire le premier objet"
        },
        {
          "line": 320,
          "level": 3,
          "title": "Contrat positif du premier objet"
        },
        {
          "line": 337,
          "level": 3,
          "title": "Relation avec le contrôle compact de `DOUBLE-LOOP`"
        },
        {
          "line": 341,
          "level": 3,
          "title": "Grounding contestable"
        },
        {
          "line": 356,
          "level": 3,
          "title": "Réutilisation située"
        },
        {
          "line": 373,
          "level": 2,
          "title": "DIRECTION/VISUAL_TARGET — rendre la direction pilotable"
        },
        {
          "line": 392,
          "level": 3,
          "title": "Compilation de la première proposition"
        },
        {
          "line": 411,
          "level": 3,
          "title": "Test d’utilité de l’ancre"
        },
        {
          "line": 421,
          "level": 3,
          "title": "Décider la route de production"
        },
        {
          "line": 439,
          "level": 3,
          "title": "Réserve `ANCHOR-GENERATED` en enjeu identitaire élevé"
        },
        {
          "line": 449,
          "level": 2,
          "title": "DIRECTION/DIRECTION-ATELIER — module officiel de direction située"
        },
        {
          "line": 455,
          "level": 3,
          "title": "Noyau du contrat"
        },
        {
          "line": 468,
          "level": 3,
          "title": "Vérité de la scène et clôture de craft"
        },
        {
          "line": 482,
          "level": 2,
          "title": "DIRECTION/DOUBLE-LOOP — créer puis apprendre"
        },
        {
          "line": 486,
          "level": 3,
          "title": "Contrôle du premier objet — qualité intrinsèque sans nouveau gate"
        },
        {
          "line": 500,
          "level": 3,
          "title": "One-shot et boucle d’amélioration"
        },
        {
          "line": 506,
          "level": 3,
          "title": "Signaux de réouverture"
        },
        {
          "line": 525,
          "level": 3,
          "title": "Test de résilience visuelle"
        },
        {
          "line": 539,
          "level": 3,
          "title": "Signaux d’apprentissage expérimental"
        },
        {
          "line": 543,
          "level": 2,
          "title": "Rôle"
        },
        {
          "line": 553,
          "level": 2,
          "title": "LES CINQ RÈGLES ABSOLUES"
        },
        {
          "line": 559,
          "level": 3,
          "title": "[ABSOLU 1 — STANDARD VISUEL] Une surface identitaire conforme mais sans direction perceptible est un échec de livraison."
        },
        {
          "line": 577,
          "level": 3,
          "title": "[ABSOLU 2 — ANCRAGE OBSERVABLE] Ne dessine jamais une surface identitaire uniquement de mémoire."
        },
        {
          "line": 593,
          "level": 3,
          "title": "[ABSOLU 3 — GATE] Aucune livraison sans les preuves applicables au mode."
        },
        {
          "line": 605,
          "level": 3,
          "title": "[ABSOLU 4 — MODE, PREUVE ET BUDGET] Déclare la route et la prochaine preuve avant d’exécuter."
        },
        {
          "line": 620,
          "level": 3,
          "title": "[ABSOLU 5 — RÉEL ET BEAU ENSEMBLE] Cadre le produit, le JTBD, les preuves et les contraintes pour produire une beauté pertinente."
        },
        {
          "line": 646,
          "level": 2,
          "title": "Posture — à lire avant toute action"
        },
        {
          "line": 656,
          "level": 2,
          "title": "0. Classification du mode, preuve et capacité"
        },
        {
          "line": 672,
          "level": 3,
          "title": "ITER se souvient"
        },
        {
          "line": 678,
          "level": 2,
          "title": "Cadrage de médium et de capacité"
        },
        {
          "line": 701,
          "level": 2,
          "title": "1. Direction divergente — déclenchement `DIRECTION`"
        },
        {
          "line": 726,
          "level": 2,
          "title": "2. Routage — quoi charger et quand"
        },
        {
          "line": 730,
          "level": 3,
          "title": "Déclencheurs critiques"
        },
        {
          "line": 745,
          "level": 3,
          "title": "Index à la demande"
        },
        {
          "line": 766,
          "level": 2,
          "title": "3. Invariants de jugement"
        },
        {
          "line": 768,
          "level": 3,
          "title": "Convergence de genre ≠ slop"
        },
        {
          "line": 774,
          "level": 3,
          "title": "PASS technique ≠ direction tenue"
        },
        {
          "line": 780,
          "level": 3,
          "title": "Les listes ne sont pas un canon"
        },
        {
          "line": 786,
          "level": 2,
          "title": "Clôture de direction"
        },
        {
          "line": 794,
          "level": 3,
          "title": "Entrée prioritaire — à lire avant le détail"
        },
        {
          "line": 806,
          "level": 3,
          "title": "Lecture instrumentée et règle de passage"
        }
      ],
      "fences": [
        {
          "line": 150,
          "language": "text"
        },
        {
          "line": 167,
          "language": "text"
        },
        {
          "line": 192,
          "language": "text"
        },
        {
          "line": 284,
          "language": "text"
        },
        {
          "line": 345,
          "language": "text"
        },
        {
          "line": 360,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        12,
        34,
        46,
        60,
        99,
        252,
        268,
        305,
        325,
        378,
        399,
        428,
        460,
        473,
        491,
        511,
        530,
        582,
        610,
        637,
        663,
        689,
        708,
        733,
        748
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 3,
          "text": "**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. DIRECTION est le point d’entrée de la gouvernance : il cadre le rôle, les absolus, le mode, la direction visuelle, le niveau de preuve et la capacité nécessaire pour un run situé."
        },
        {
          "line": 423,
          "text": "Lorsqu’un asset ou son absence porte une décision perceptible, nomme **une route de production initiale** avant le build. Cette route peut être révisée sur preuve si la décision de direction reste stable et si la révision réduit un risque de droits, de performance, de fidélité, de maintenance ou d’intégration."
        },
        {
          "line": 630,
          "text": "**Cadre d’accessibilité web.** Lorsque la conformité web est dans le périmètre, applique le référentiel et la version retenus par la source propriétaire de preuve et de contexte, puis vérifie les critères applicables au contexte réel. Une référence externe évolutive reste une `[VEILLE]` tant qu’elle n’est pas adoptée par le propriétaire compétent ; elle ne devient pas automatiquement une obligation de livraison. Un référentiel de conformité ne valide ni la direction visuelle, ni l’utilisabilité globale, ni l’adéquation du positionnement."
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 21,
          "value": "ACTION/RUN_CARD"
        },
        {
          "line": 27,
          "value": "ACTION/HANDOFF"
        },
        {
          "line": 53,
          "value": "ACTION/HANDOFF"
        },
        {
          "line": 61,
          "value": "DIRECTION/START"
        },
        {
          "line": 62,
          "value": "DIRECTION/DAILY"
        },
        {
          "line": 62,
          "value": "DIRECTION/FAST-PATH"
        },
        {
          "line": 63,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 63,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 64,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 64,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 65,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 86,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 113,
          "value": "DIRECTION/SERVICE-BOUNDARY"
        },
        {
          "line": 119,
          "value": "DIRECTION/START"
        },
        {
          "line": 123,
          "value": "DIRECTION/DAILY"
        },
        {
          "line": 123,
          "value": "DIRECTION/START"
        },
        {
          "line": 131,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 132,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 133,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 134,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 135,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 159,
          "value": "ACTION/RUN_CARD"
        },
        {
          "line": 161,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 182,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 188,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 239,
          "value": "ACTION/GATE-B"
        },
        {
          "line": 239,
          "value": "ACTION/HANDOFF"
        },
        {
          "line": 239,
          "value": "ACTION/RUN_CARD"
        },
        {
          "line": 245,
          "value": "DIRECTION/DAILY"
        },
        {
          "line": 253,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 253,
          "value": "DIRECTION/START"
        },
        {
          "line": 254,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 254,
          "value": "DIRECTION/START"
        },
        {
          "line": 255,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 255,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 256,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 256,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 256,
          "value": "DIRECTION/DIRECTION-ATELIER"
        },
        {
          "line": 256,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 256,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 256,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 256,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 256,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 256,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 257,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 257,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 257,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 259,
          "value": "DIRECTION/START"
        },
        {
          "line": 259,
          "value": "SAVOIR/DESIGN-ATLAS"
        },
        {
          "line": 263,
          "value": "DIRECTION/FAST-PATH"
        },
        {
          "line": 278,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 282,
          "value": "DIRECTION/START"
        },
        {
          "line": 300,
          "value": "DIRECTION/START"
        },
        {
          "line": 314,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 373,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 443,
          "value": "ACTION/STATUS"
        },
        {
          "line": 445,
          "value": "ACTION/VISUAL_PROOF"
        },
        {
          "line": 449,
          "value": "DIRECTION/DIRECTION-ATELIER"
        },
        {
          "line": 453,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 482,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 514,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 734,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 734,
          "value": "DIRECTION/START"
        },
        {
          "line": 734,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 734,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 734,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 735,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 735,
          "value": "DIRECTION/START"
        },
        {
          "line": 736,
          "value": "ACTION/RUN-"
        },
        {
          "line": 738,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 739,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 742,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 743,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 743,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 749,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 749,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 749,
          "value": "DIRECTION/START"
        },
        {
          "line": 750,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 751,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 752,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 753,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 755,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 756,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 756,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 757,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 758,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 759,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 760,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 788,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        },
        {
          "line": 788,
          "value": "ACTION/CLOSE-PACKAGE"
        },
        {
          "line": 817,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 817,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 817,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "DIRECTION": 31,
        "ACTION": 30,
        "DIRECTION-ATELIER": 9,
        "RUN_CARD": 13,
        "START": 16,
        "DAILY": 4,
        "FAST-PATH": 5,
        "EXTERNAL-START": 3,
        "MODE": 3,
        "DECISION": 4,
        "RISK": 3,
        "SCOPE": 2,
        "ARTIFACT": 2,
        "DECISION-CHANGE": 3,
        "NEXT-ACTION": 1,
        "OWNER": 3,
        "NEXT-PROOF": 4,
        "EXIT-CONDITION": 2,
        "ROUTE": 1,
        "TARGET": 1,
        "HANDOFF": 3,
        "SAVOIR": 10,
        "BIBLIOTHEQUE": 10,
        "CAPABILITY-BASIS": 2,
        "CREATIVE-BOOT": 3,
        "VISUAL_TARGET": 8,
        "FIRST-OBJECT": 6,
        "DOUBLE-LOOP": 5,
        "P0": 1,
        "P1": 1,
        "P2": 1,
        "P3": 1,
        "LITE": 9,
        "ITER": 9,
        "BASIS": 1,
        "CHANGELOG": 5,
        "ATELIER": 1,
        "STANDARD": 5,
        "DESIGN-ATLAS": 5,
        "CFT-TARGETS": 1,
        "DEPTH-TRIGGER": 1,
        "DOMAIN-FRAME": 1,
        "ID": 1,
        "LIMIT": 1,
        "NOT-VERIFIED": 6,
        "CLOSED": 1,
        "EXPLORATORY": 4,
        "DECISION-INTENT": 1,
        "GROUNDING-DECISION": 2,
        "REUSE-CHALLENGE": 2,
        "JTBD": 1,
        "ANTI-DIRECTION": 1,
        "RUN-PRIORITY": 1,
        "NO": 1,
        "KEEP-IF": 1,
        "ANCHOR-GENERATED": 4,
        "ANCHOR-OBSERVED": 2,
        "ANCHOR-PROVIDED": 2,
        "CODE-NATIVE": 1,
        "FOURNI": 1,
        "HYBRIDE": 1,
        "HELD": 2,
        "SPECCED": 2,
        "FAIL-ASSUMED": 4,
        "PASS": 2,
        "RETURNED": 1,
        "ESCALATED": 1,
        "ACCEPTED": 1,
        "BLOCKED": 1,
        "STARTUP-NOMINAL": 1,
        "CONDITIONAL-READ": 1,
        "AUDIT-READ": 2,
        "ACTUAL-READ": 1
      }
    },
    "V1/official/GLOSSAIRE.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Glossaire — Design Governance V1"
        },
        {
          "line": 48,
          "level": 2,
          "title": "Exemples express"
        },
        {
          "line": 61,
          "level": 2,
          "title": "Pour commencer sans vocabulaire préalable"
        }
      ],
      "fences": [],
      "table_separator_lines": [
        6,
        53
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 33,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 64,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "LITE": 1,
        "ITER": 1,
        "STANDARD": 1,
        "DIRECTION": 1,
        "STATE": 1,
        "INTAKE": 1,
        "CLOSED": 2,
        "ISSUE": 1,
        "BLOCKED": 1,
        "RETURNED": 1,
        "EXPLORATORY": 2,
        "VERDICT": 1,
        "ACCEPTED": 1,
        "ACCEPTED-WITH-RESERVATION": 2,
        "RETURN": 2,
        "RETURN-DIRECTION": 1,
        "SYSTEM-ESCALATION": 1,
        "PASS": 1,
        "PASS-WITH-RESERVATION": 1,
        "NOT-VERIFIED": 2,
        "HELD": 1,
        "HELD-WITH-ACCEPTED-DIFFERENCE": 1,
        "PARTIALLY-HELD": 1,
        "LOST-IN-BUILD": 1,
        "DECISION-INTENT": 1,
        "DECISION-CHANGE": 1,
        "TRACE-LOCATOR": 1,
        "NOT-OBSERVED": 1,
        "SPECCED": 1,
        "BUILDING": 1,
        "READING_MAP": 1
      }
    },
    "V1/official/ORCHESTRATION_MAP.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "ORCHESTRATION_MAP — combinaisons dérivées par résultat"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Rôle"
        },
        {
          "line": 13,
          "level": 2,
          "title": "Combinaisons par résultat recherché"
        },
        {
          "line": 29,
          "level": 2,
          "title": "Variation créative"
        },
        {
          "line": 41,
          "level": 2,
          "title": "Garde-fous"
        },
        {
          "line": 50,
          "level": 2,
          "title": "Arrêt"
        }
      ],
      "fences": [],
      "table_separator_lines": [
        16
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 3,
          "value": "DIRECTION/START"
        },
        {
          "line": 7,
          "value": "DIRECTION/START"
        },
        {
          "line": 17,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 17,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 17,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 17,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 17,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 17,
          "value": "DIRECTION/START"
        },
        {
          "line": 17,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 17,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 17,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 17,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 18,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 18,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 18,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 18,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 19,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 19,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 19,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 19,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 20,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 20,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 20,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 20,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 21,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        },
        {
          "line": 21,
          "value": "ACTION/STRUCTURED-PROOF"
        },
        {
          "line": 22,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 22,
          "value": "DIRECTION/START"
        },
        {
          "line": 23,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 23,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 23,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 23,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 24,
          "value": "ACTION/STRUCTURED-PROOF"
        },
        {
          "line": 24,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 24,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 25,
          "value": "ACTION/AUTHORITY"
        },
        {
          "line": 25,
          "value": "DIRECTION/START"
        },
        {
          "line": 43,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "RUN_CARD": 3,
        "TRACE-LOCATOR": 1,
        "LITE": 1,
        "ITER": 2,
        "CHANGELOG": 1,
        "READING_MAP": 1
      }
    },
    "V1/official/QUICKSTART.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Design Governance V1.0.0 — Quickstart"
        },
        {
          "line": 9,
          "level": 2,
          "title": "Démarrage en 90 secondes"
        },
        {
          "line": 29,
          "level": 2,
          "title": "Carte de résolution rapide"
        },
        {
          "line": 35,
          "level": 2,
          "title": "1. Choisir la profondeur de lecture"
        },
        {
          "line": 39,
          "level": 3,
          "title": "Façade d’activation en cinq éléments"
        },
        {
          "line": 49,
          "level": 3,
          "title": "Constitution minimale"
        },
        {
          "line": 61,
          "level": 2,
          "title": "2. Le chemin en trente secondes"
        },
        {
          "line": 83,
          "level": 2,
          "title": "3. Le parcours complet en cinq minutes"
        },
        {
          "line": 109,
          "level": 3,
          "title": "Charger une route et renforcer une RUN_CARD"
        },
        {
          "line": 126,
          "level": 2,
          "title": "4. Choisir le mode sans le deviner"
        },
        {
          "line": 146,
          "level": 2,
          "title": "5. Charger seulement ce qui peut changer la décision"
        },
        {
          "line": 158,
          "level": 2,
          "title": "6. Produire une qualité positive dès le premier rendu"
        },
        {
          "line": 177,
          "level": 2,
          "title": "7. One-shot : compression, jamais dispense"
        },
        {
          "line": 192,
          "level": 2,
          "title": "8. Handoff agentique"
        },
        {
          "line": 213,
          "level": 2,
          "title": "9. Exemple complet minimal"
        },
        {
          "line": 262,
          "level": 2,
          "title": "10. Observer, interpréter et améliorer"
        },
        {
          "line": 286,
          "level": 2,
          "title": "11. Persister et fermer honnêtement"
        },
        {
          "line": 302,
          "level": 2,
          "title": "12. Sources propriétaires"
        }
      ],
      "fences": [
        {
          "line": 13,
          "language": "text"
        },
        {
          "line": 75,
          "language": "text"
        },
        {
          "line": 113,
          "language": "bash"
        },
        {
          "line": 120,
          "language": "bash"
        },
        {
          "line": 196,
          "language": "text"
        },
        {
          "line": 207,
          "language": "text"
        },
        {
          "line": 217,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        20,
        54,
        66,
        92,
        99,
        137,
        149,
        165,
        267,
        305
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 268,
          "text": "| Qu’a-t-on réellement observé ? | Artefact, état, viewport, tâche, participant, mesure, version et date. |"
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 31,
          "value": "DIRECTION/START"
        },
        {
          "line": 41,
          "value": "DIRECTION/START"
        },
        {
          "line": 45,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 47,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 47,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 55,
          "value": "DIRECTION/START"
        },
        {
          "line": 58,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 58,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 58,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 58,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 58,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 58,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 103,
          "value": "DIRECTION/START"
        },
        {
          "line": 138,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 138,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 138,
          "value": "DIRECTION/START"
        },
        {
          "line": 139,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 139,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 139,
          "value": "DIRECTION/START"
        },
        {
          "line": 140,
          "value": "DIRECTION/START"
        },
        {
          "line": 141,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 141,
          "value": "DIRECTION/START"
        },
        {
          "line": 141,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 141,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 142,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 142,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 142,
          "value": "DIRECTION/START"
        },
        {
          "line": 150,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 150,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 150,
          "value": "DIRECTION/START"
        },
        {
          "line": 151,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 151,
          "value": "DIRECTION/START"
        },
        {
          "line": 151,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 152,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 152,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 152,
          "value": "DIRECTION/START"
        },
        {
          "line": 153,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 153,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 153,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 153,
          "value": "DIRECTION/START"
        },
        {
          "line": 153,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 153,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 154,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 154,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 154,
          "value": "DIRECTION/START"
        },
        {
          "line": 160,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 175,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 205,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "MODE": 1,
        "DECISION": 1,
        "RISK": 1,
        "SCOPE": 1,
        "ARTIFACT": 1,
        "PROOF": 1,
        "LIMIT": 1,
        "NEXT-ACTION": 1,
        "OWNER": 1,
        "NEXT-PROOF": 1,
        "EXIT-CONDITION": 1,
        "DIRECTION": 11,
        "ACTION": 6,
        "SAVOIR": 6,
        "BIBLIOTHEQUE": 3,
        "RUN_CARD": 4,
        "DECISION-INTENT": 1,
        "DECISION-CHANGE": 1,
        "ITER": 4,
        "LITE": 4,
        "STANDARD": 3,
        "EXTERNAL-START": 1,
        "CHANGELOG": 2,
        "CFT-00": 1,
        "TRACE-LOCATOR": 1,
        "NOT-VERIFIED": 1,
        "NOT-OBSERVED": 1,
        "EXPLORATORY": 1,
        "BLOCKED": 1,
        "RETURNED": 1,
        "FAIL-ASSUMED": 1
      }
    },
    "V1/official/READING_MAP.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "READING_MAP — carte dérivée de lecture et d’activation"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Utilisation"
        },
        {
          "line": 11,
          "level": 2,
          "title": "Chemin canonique de démarrage"
        },
        {
          "line": 22,
          "level": 2,
          "title": "Constitution minimale"
        },
        {
          "line": 26,
          "level": 2,
          "title": "Routage minimal par décision"
        },
        {
          "line": 38,
          "level": 2,
          "title": "Activation multi-perspective"
        },
        {
          "line": 56,
          "level": 2,
          "title": "Handoff minimal commun"
        },
        {
          "line": 78,
          "level": 2,
          "title": "Résolution des routes"
        },
        {
          "line": 93,
          "level": 2,
          "title": "Locators principaux"
        },
        {
          "line": 124,
          "level": 2,
          "title": "Condition d’arrêt"
        }
      ],
      "fences": [
        {
          "line": 60,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        29,
        43,
        83,
        98
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 13,
          "text": "1. Localiser la version V1 réellement fournie."
        },
        {
          "line": 24,
          "text": "Les cinq absolus de `DIRECTION` protègent la baseline : direction perceptible, ancre inspectable, preuves applicables, mode et prochaine preuve déclarés avant l’exécution, coordination du réel et du beau. La conformité ne remplace ni la direction ni la preuve. Pour le contrat complet, ouvrir [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues)."
        },
        {
          "line": 54,
          "text": "| Mémoire | Décision durable, version, réserve ou migration | `RUN_CARD` et `CHANGELOG` si promotion | Décision, date, statut, preuve, réserve, revue | Décision strictement éphémère |"
        },
        {
          "line": 95,
          "text": "Les locators ci-dessous sont des titres exacts dans la baseline V1. Les routes non listées restent résolues par leur préfixe propriétaire et leur titre exact ; elles ne doivent pas être devinées."
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 15,
          "value": "DIRECTION/START"
        },
        {
          "line": 20,
          "value": "DIRECTION/START"
        },
        {
          "line": 30,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 30,
          "value": "DIRECTION/START"
        },
        {
          "line": 31,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 31,
          "value": "DIRECTION/START"
        },
        {
          "line": 32,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 32,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 32,
          "value": "DIRECTION/START"
        },
        {
          "line": 32,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 33,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 33,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 33,
          "value": "DIRECTION/START"
        },
        {
          "line": 33,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 33,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 34,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 34,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 34,
          "value": "DIRECTION/START"
        },
        {
          "line": 34,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 36,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        },
        {
          "line": 46,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 47,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 48,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 48,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 49,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 49,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 50,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 53,
          "value": "ACTION/AUTHORITY"
        },
        {
          "line": 99,
          "value": "DIRECTION/START"
        },
        {
          "line": 100,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 101,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 102,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 103,
          "value": "DIRECTION/FAST-PATH"
        },
        {
          "line": 104,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 105,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 106,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 107,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 108,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 109,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 110,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 111,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 112,
          "value": "ACTION/CLOSE-PACKAGE"
        },
        {
          "line": 113,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 114,
          "value": "ACTION/ROUTING"
        },
        {
          "line": 115,
          "value": "ACTION/CLOSE-EXIT-CHECK"
        },
        {
          "line": 116,
          "value": "SAVOIR/READ"
        },
        {
          "line": 117,
          "value": "SAVOIR/ROUTING"
        },
        {
          "line": 118,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 119,
          "value": "BIBLIOTHEQUE/READ"
        },
        {
          "line": 120,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 121,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 122,
          "value": "BIBLIOTHEQUE/EVOLUTION"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "RUN_CARD": 7,
        "READING_MAP": 1,
        "ORCHESTRATION_MAP": 1,
        "ACTION": 8,
        "DIRECTION": 2,
        "RUN-ITER": 1,
        "SAVOIR": 1,
        "BIBLIOTHEQUE": 1,
        "CHANGELOG": 4,
        "STATE": 1,
        "NOT-VERIFIED": 1,
        "EXPLORATORY": 1
      }
    },
    "V1/official/README.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Design Governance V1.0.0"
        },
        {
          "line": 7,
          "level": 2,
          "title": "Mission"
        },
        {
          "line": 15,
          "level": 2,
          "title": "Commencer ici"
        },
        {
          "line": 19,
          "level": 3,
          "title": "Carte de lecture dérivée"
        },
        {
          "line": 25,
          "level": 2,
          "title": "Sources normatives"
        },
        {
          "line": 41,
          "level": 2,
          "title": "Chemin actif"
        },
        {
          "line": 49,
          "level": 2,
          "title": "Limites assumées"
        }
      ],
      "fences": [],
      "table_separator_lines": [
        30
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 17,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "RUN_CARD": 3,
        "DOMAIN_FRAME": 1,
        "RESEARCH_BRIEF": 1,
        "CREATIVE_DIRECTION_SET": 1,
        "UI_UX_REALITY_PACK": 1,
        "EVALUATION_CASE": 1,
        "DIRECTION": 2,
        "ACTION": 1,
        "SAVOIR": 1,
        "BIBLIOTHEQUE": 1,
        "DESIGN-ATLAS": 1
      }
    },
    "V1/official/SAVOIR.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "SAVOIR — Bibliothèque de jugement, craft et production"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Responsabilité"
        },
        {
          "line": 26,
          "level": 3,
          "title": "Orientation interne et sortie vers ACTION"
        },
        {
          "line": 34,
          "level": 2,
          "title": "SAVOIR/READ — comment utiliser cette bibliothèque"
        },
        {
          "line": 42,
          "level": 3,
          "title": "SAVOIR/FAST-PATH — juger sans produire un dossier"
        },
        {
          "line": 48,
          "level": 3,
          "title": "Niveaux d’autorité"
        },
        {
          "line": 66,
          "level": 2,
          "title": "SAVOIR/ROUTING — routes stables"
        },
        {
          "line": 86,
          "level": 1,
          "title": "SAVOIR/FRAME — fondations et cadrage"
        },
        {
          "line": 88,
          "level": 2,
          "title": "FND-01 — principe fondateur"
        },
        {
          "line": 102,
          "level": 3,
          "title": "Premium perçu comme heuristique de jugement"
        },
        {
          "line": 108,
          "level": 3,
          "title": "Comprendre, ouvrir, converger, prouver"
        },
        {
          "line": 114,
          "level": 3,
          "title": "Singularité sans rejet des conventions"
        },
        {
          "line": 126,
          "level": 3,
          "title": "Grammaire positive de composition"
        },
        {
          "line": 141,
          "level": 3,
          "title": "Pluralité esthétique et goût situé"
        },
        {
          "line": 151,
          "level": 2,
          "title": "FND-02 — compromis"
        },
        {
          "line": 164,
          "level": 2,
          "title": "FND-03 — cadrage et preuve de contexte"
        },
        {
          "line": 195,
          "level": 1,
          "title": "SAVOIR/CRAFT — anti-slop, composition et expression"
        },
        {
          "line": 199,
          "level": 3,
          "title": "Qualité du premier rendu, one-shot et preuve"
        },
        {
          "line": 211,
          "level": 2,
          "title": "CFT-00 — qualité créative et niveau d’ambition"
        },
        {
          "line": 230,
          "level": 3,
          "title": "Creative Quality Review"
        },
        {
          "line": 242,
          "level": 2,
          "title": "CFT-01 — motivation, construction et forme située"
        },
        {
          "line": 261,
          "level": 3,
          "title": "Dérivation bornée d’une forme située"
        },
        {
          "line": 281,
          "level": 2,
          "title": "CFT-02 — registres et alternative située"
        },
        {
          "line": 302,
          "level": 2,
          "title": "CFT-03 — composition, densité et harmonie"
        },
        {
          "line": 312,
          "level": 3,
          "title": "Cohérence et harmonie"
        },
        {
          "line": 322,
          "level": 2,
          "title": "CFT-04 — design émotionnel"
        },
        {
          "line": 346,
          "level": 3,
          "title": "CFT-04a — premier contact, preuve et rapport de personne"
        },
        {
          "line": 361,
          "level": 2,
          "title": "CFT-05 — couleur et contraste"
        },
        {
          "line": 377,
          "level": 1,
          "title": "SAVOIR/TYPE — typographie et données"
        },
        {
          "line": 391,
          "level": 3,
          "title": "Preuve typographique"
        },
        {
          "line": 415,
          "level": 1,
          "title": "SAVOIR/STATE — craft, composants et états"
        },
        {
          "line": 419,
          "level": 3,
          "title": "Jugement visuel situé"
        },
        {
          "line": 450,
          "level": 3,
          "title": "Vocabulaire perceptuel"
        },
        {
          "line": 463,
          "level": 3,
          "title": "États pertinents"
        },
        {
          "line": 471,
          "level": 1,
          "title": "SAVOIR/SOURCE — ancre et sourcing visuel"
        },
        {
          "line": 479,
          "level": 3,
          "title": "Test d’utilité de l’ancre"
        },
        {
          "line": 493,
          "level": 3,
          "title": "Recherche orientée décision — chercher loin seulement quand cela change le résultat"
        },
        {
          "line": 518,
          "level": 3,
          "title": "Curer, produire et intégrer"
        },
        {
          "line": 530,
          "level": 1,
          "title": "SAVOIR/DESIGN-ATLAS — familles et responsabilités"
        },
        {
          "line": 543,
          "level": 3,
          "title": "Cartographie non exhaustive"
        },
        {
          "line": 558,
          "level": 3,
          "title": "Rôles d’asset"
        },
        {
          "line": 562,
          "level": 3,
          "title": "Portée par médium"
        },
        {
          "line": 566,
          "level": 3,
          "title": "Test de sélection et de non-recyclage"
        },
        {
          "line": 574,
          "level": 1,
          "title": "SAVOIR/STYLE — profils contrôlés et dials"
        },
        {
          "line": 580,
          "level": 3,
          "title": "Règle de sélection"
        },
        {
          "line": 601,
          "level": 3,
          "title": "Taxonomie transversale"
        },
        {
          "line": 628,
          "level": 3,
          "title": "Usage et test"
        },
        {
          "line": 634,
          "level": 3,
          "title": "Dials"
        },
        {
          "line": 652,
          "level": 3,
          "title": "Styles visuels, culturels et multi-médias"
        },
        {
          "line": 658,
          "level": 3,
          "title": "Ponctuation située : le tiret cadratin n’est pas une signature"
        },
        {
          "line": 664,
          "level": 3,
          "title": "Test anti-slop procédural"
        },
        {
          "line": 672,
          "level": 3,
          "title": "Vocabulaire à rendre observable"
        },
        {
          "line": 690,
          "level": 1,
          "title": "SAVOIR/SYSTEM — tokens et composants"
        },
        {
          "line": 708,
          "level": 1,
          "title": "SAVOIR/CONTEXT — accessibilité, contexte et robustesse"
        },
        {
          "line": 714,
          "level": 3,
          "title": "Contextes à fort enjeu"
        },
        {
          "line": 728,
          "level": 3,
          "title": "Responsive et performance"
        },
        {
          "line": 734,
          "level": 3,
          "title": "Motion et espace"
        },
        {
          "line": 744,
          "level": 1,
          "title": "SAVOIR/TECH — techniques, tests et stack"
        },
        {
          "line": 758,
          "level": 3,
          "title": "Hiérarchie de jugement pour les interfaces"
        },
        {
          "line": 762,
          "level": 3,
          "title": "Preuve par médium"
        },
        {
          "line": 784,
          "level": 1,
          "title": "SAVOIR/TOOLS — claims, tendances et calibration"
        },
        {
          "line": 786,
          "level": 2,
          "title": "Claims externes et péremption"
        },
        {
          "line": 816,
          "level": 2,
          "title": "Goût, références et tendances"
        },
        {
          "line": 843,
          "level": 1,
          "title": "SAVOIR/INTEGRITY — limites, délégation et critique"
        },
        {
          "line": 845,
          "level": 3,
          "title": "Test de non-récitation"
        },
        {
          "line": 849,
          "level": 2,
          "title": "Modes d’échec d’application"
        },
        {
          "line": 880,
          "level": 2,
          "title": "Contrôle d’intégrité"
        },
        {
          "line": 888,
          "level": 2,
          "title": "Limites, délégation et critique"
        },
        {
          "line": 906,
          "level": 2,
          "title": "Règles d’or — lecture rapide"
        },
        {
          "line": 921,
          "level": 2,
          "title": "Méthodologie studio"
        }
      ],
      "fences": [
        {
          "line": 395,
          "language": "text"
        },
        {
          "line": 499,
          "language": "text"
        },
        {
          "line": 586,
          "language": "text"
        },
        {
          "line": 790,
          "language": "text"
        }
      ],
      "table_separator_lines": [
        16,
        53,
        71,
        131,
        169,
        179,
        218,
        247,
        270,
        286,
        335,
        353,
        405,
        424,
        453,
        535,
        548,
        606,
        618,
        639,
        677,
        719,
        751,
        767,
        833,
        870
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 3,
          "text": "**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. SAVOIR porte le jugement de design : craft, style, contenu, contexte, technique, sources, intégrité et limites de ce qui peut être affirmé."
        },
        {
          "line": 20,
          "text": "| `CHANGELOG.md` | État de release, changements futurs, pilotes optionnels et décisions de gouvernance. |"
        },
        {
          "line": 383,
          "text": "Une ou deux voix expressives peuvent souvent suffire, mais cette heuristique reste `[À ADAPTER]`. Une famille mono-fonctionnelle pour données, version ou métadonnées ne constitue pas nécessairement une voix supplémentaire."
        },
        {
          "line": 446,
          "text": "> Quel choix résulte ici d’un jugement délibéré, serait absent d’une version par défaut, et quelle contrainte sert-il ?"
        },
        {
          "line": 620,
          "text": "| `STYLE/EDITORIAL_PRECISION` | Donner au langage, au rythme et à la sélection le poids principal. | Baseline, colonnes, blancs calibrés, hiérarchie typo, métadonnées précises, densité séquencée. | Dashboard temps réel, comparaison très rapide ou données dominantes. Éviter la préciosité. |"
        },
        {
          "line": 622,
          "text": "| `STYLE/QUIET_SYSTEM` | Rendre un système fiable, calme et opérable sans neutralité vide. | Colonnes, baseline, modules réglés, type rationnel, matière réduite à des seuils et états utiles. | Campagne, manifeste ou objet de collection à présence émotionnelle autonome. |"
        },
        {
          "line": 704,
          "text": "Un contrat de composant partagé décrit intention, anatomie, variants utiles, états, responsive, tokens, frontières de composition, baseline de rendu, source de vérité, owner, compatibilité et prochaine revue. La structure détaillée relève de `BIBLIOTHEQUE/COMPONENTS` ; `ACTION/RUN-SYSTEM` conserve l’impact, les consumers, la migration, le rollback, la preuve et le verdict."
        },
        {
          "line": 770,
          "text": "| Référentiel applicable | Quelle norme ou guideline fait référence ? | Séparer `CONFORMANCE-TARGET` — référentiel, version, niveau, scope et owner — de `QUALITY-TARGET` — confort, lisibilité, contraste ou autre cible qualitative. |"
        },
        {
          "line": 778,
          "text": "Aucun outil, script ou package ne reçoit automatiquement un `PASS`. Ne l’exécute pas sans dépendance approuvée, source de l’approbation, package/version, date de vérification, capacité résolue, documentation vérifiée, limites, owner et fallback lorsque nécessaire ; à défaut, conserve `NOT-VERIFIED` ou retourne le run."
        },
        {
          "line": 780,
          "text": "Toute ressource de stack indique : stack, version, date de vérification, owner, fallback, limites, claims applicables et capacité résolue. `SAVOIR/TOOLS` définit les exigences et limites ; ACTION conserve la fiche exécutée, la preuve, les statuts et le verdict ; CHANGELOG intervient lorsqu’une règle ou une route devient partagée."
        },
        {
          "line": 892,
          "text": "Une capacité disponible modifie le type de preuve possible ; elle ne permet jamais d’affirmer une qualité sans examen du résultat. Toute délégation conserve délégataire, rôle, capacité déclarée, méthode, scope, artefact/résultat consulté, date/version, limite, owner de décision finale, `NEXT-PROOF` et condition de reprise ou d’escalade."
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 28,
          "value": "SAVOIR/ROUTING"
        },
        {
          "line": 34,
          "value": "SAVOIR/READ"
        },
        {
          "line": 42,
          "value": "SAVOIR/FAST-PATH"
        },
        {
          "line": 62,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 66,
          "value": "SAVOIR/ROUTING"
        },
        {
          "line": 72,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 73,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 74,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 75,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 75,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 76,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 77,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 78,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 78,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 79,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 79,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 80,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 81,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 82,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 86,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 120,
          "value": "ACTION/ANTI-SLOP"
        },
        {
          "line": 195,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 255,
          "value": "ACTION/ANTI-SLOP"
        },
        {
          "line": 255,
          "value": "SAVOIR/CRAFT/CFT-01"
        },
        {
          "line": 279,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 300,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 373,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 377,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 393,
          "value": "ACTION/STRUCTURED-PROOF"
        },
        {
          "line": 415,
          "value": "SAVOIR/STATE"
        },
        {
          "line": 467,
          "value": "ACTION/GATE-A"
        },
        {
          "line": 467,
          "value": "ACTION/GATE-C"
        },
        {
          "line": 471,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 475,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 475,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 477,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 524,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 530,
          "value": "SAVOIR/DESIGN-ATLAS"
        },
        {
          "line": 532,
          "value": "DIRECTION/START"
        },
        {
          "line": 536,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 536,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 537,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 537,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 538,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 538,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 538,
          "value": "SAVOIR/TYPE"
        },
        {
          "line": 539,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 539,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 540,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 540,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 541,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 541,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 541,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 560,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 560,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 564,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 574,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 578,
          "value": "ACTION/RUN-"
        },
        {
          "line": 578,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 578,
          "value": "DIRECTION/START"
        },
        {
          "line": 578,
          "value": "SAVOIR/FRAME"
        },
        {
          "line": 578,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 619,
          "value": "STYLE/RAW_BRUTALISM"
        },
        {
          "line": 620,
          "value": "STYLE/EDITORIAL_PRECISION"
        },
        {
          "line": 621,
          "value": "STYLE/PICTORIAL_UTILITY"
        },
        {
          "line": 622,
          "value": "STYLE/QUIET_SYSTEM"
        },
        {
          "line": 623,
          "value": "STYLE/MAXIMAL_EXPRESSION"
        },
        {
          "line": 624,
          "value": "STYLE/DIGITAL_MEMORY"
        },
        {
          "line": 625,
          "value": "STYLE/TACTILE_VOLUME"
        },
        {
          "line": 626,
          "value": "STYLE/COLLAGE_ASSEMBLY"
        },
        {
          "line": 654,
          "value": "STYLE/DIGITAL_MEMORY"
        },
        {
          "line": 654,
          "value": "STYLE/TACTILE_VOLUME"
        },
        {
          "line": 690,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 696,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 696,
          "value": "DIRECTION/START"
        },
        {
          "line": 696,
          "value": "SAVOIR/SYSTEM"
        },
        {
          "line": 704,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 704,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 708,
          "value": "SAVOIR/CONTEXT"
        },
        {
          "line": 726,
          "value": "DIRECTION/START"
        },
        {
          "line": 744,
          "value": "SAVOIR/TECH"
        },
        {
          "line": 774,
          "value": "ACTION/OVERRIDE"
        },
        {
          "line": 780,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 784,
          "value": "SAVOIR/TOOLS"
        },
        {
          "line": 843,
          "value": "SAVOIR/INTEGRITY"
        },
        {
          "line": 900,
          "value": "ACTION/GATE-B/B3"
        },
        {
          "line": 910,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "FRAME": 1,
        "CRAFT": 2,
        "TYPE": 1,
        "STATE": 1,
        "CONTEXT": 3,
        "SOURCE": 2,
        "STYLE": 2,
        "SYSTEM": 1,
        "TECH": 2,
        "TOOLS": 3,
        "INTEGRITY": 1,
        "PASS": 6,
        "DIRECTION": 13,
        "ACTION": 12,
        "SAVOIR": 2,
        "BIBLIOTHEQUE": 2,
        "CHANGELOG": 1,
        "RUN_CARD": 3,
        "PRODUIT": 1,
        "CONTENU": 1,
        "TECHNIQUE": 1,
        "YES": 1,
        "NO": 1,
        "NOT-REQUIRED": 1,
        "MODE": 2,
        "RISK": 3,
        "SCOPE": 2,
        "ARTIFACT": 1,
        "DECISION-CHANGE": 4,
        "NEXT-ACTION": 1,
        "OWNER": 1,
        "NEXT-PROOF": 7,
        "EXIT-CONDITION": 1,
        "USER": 1,
        "EXPERT": 1,
        "DESIGN-ATLAS": 2,
        "DECISION-MODIFIED": 3,
        "WHEN-USEFUL": 2,
        "FND-01": 1,
        "DIRECTION-STATUS": 1,
        "VERDICT": 1,
        "ANCHOR-GENERATED": 2,
        "ANCHOR-OBSERVED": 1,
        "ANCHOR-PROVIDED": 1,
        "NOT-VERIFIED": 8,
        "DOMAIN-FRAME": 2,
        "COUNTERINDICATION": 2,
        "MEDIUM-SCOPE": 1,
        "PROOF-LIMIT": 1,
        "NOT-OBSERVED": 1,
        "WHY-NOW": 2,
        "REUSE-CHALLENGE": 2,
        "PROFILE-DECISION": 2,
        "DECISION-INTENT": 1,
        "DIALS": 1,
        "LIMIT": 1,
        "EVIDENCE": 1,
        "EDITORIAL_PRECISION": 1,
        "RAW_BRUTALISM": 1,
        "TACTILE_VOLUME": 1,
        "PICTORIAL_UTILITY": 1,
        "Y2K": 1,
        "CREATIVE-BOOT": 1,
        "P0": 1,
        "P1": 1,
        "P2": 1,
        "P3": 1,
        "CONFORMANCE-TARGET": 2,
        "QUALITY-TARGET": 1,
        "FAIL-ASSUMED": 2,
        "EXPLORATORY": 2,
        "RETURNED": 1,
        "STANDARD": 1,
        "ITER": 1,
        "LITE": 1
      }
    },
    "skills/design-governance-practice/SKILL.md": {
      "headings": [
        {
          "line": 6,
          "level": 1,
          "title": "Design Governance V1 — pratique"
        },
        {
          "line": 8,
          "level": 2,
          "title": "Rôle"
        },
        {
          "line": 14,
          "level": 2,
          "title": "Carte de lecture et sortie"
        },
        {
          "line": 18,
          "level": 3,
          "title": "Activation en 30 secondes"
        },
        {
          "line": 22,
          "level": 3,
          "title": "Constitution minimale à garder active"
        },
        {
          "line": 34,
          "level": 2,
          "title": "Préparer le contexte"
        },
        {
          "line": 45,
          "level": 2,
          "title": "Routage et handoff"
        },
        {
          "line": 57,
          "level": 3,
          "title": "Routes canoniques à activer conditionnellement"
        },
        {
          "line": 61,
          "level": 2,
          "title": "Délégation humain-agent"
        },
        {
          "line": 69,
          "level": 2,
          "title": "Noyau d’exécution"
        },
        {
          "line": 73,
          "level": 2,
          "title": "Table de charge obligatoire"
        },
        {
          "line": 87,
          "level": 3,
          "title": "Approfondir seulement si nécessaire"
        },
        {
          "line": 95,
          "level": 3,
          "title": "Classer"
        },
        {
          "line": 99,
          "level": 3,
          "title": "Diriger"
        },
        {
          "line": 113,
          "level": 3,
          "title": "Construire"
        },
        {
          "line": 119,
          "level": 3,
          "title": "Vérifier"
        },
        {
          "line": 125,
          "level": 3,
          "title": "Corriger et fermer"
        },
        {
          "line": 129,
          "level": 2,
          "title": "Anti-slop opératoire"
        },
        {
          "line": 135,
          "level": 2,
          "title": "Sortie attendue"
        },
        {
          "line": 141,
          "level": 2,
          "title": "Références conditionnelles"
        }
      ],
      "fences": [],
      "table_separator_lines": [
        78
      ],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 38,
          "value": "DIRECTION/START"
        },
        {
          "line": 51,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 59,
          "value": "ACTION/CLOSE-PACKAGE"
        },
        {
          "line": 59,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 59,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 59,
          "value": "ACTION/ROUTING"
        },
        {
          "line": 59,
          "value": "ACTION/STRUCTURED-PROOF"
        },
        {
          "line": 59,
          "value": "DIRECTION/DIRECTION-ATELIER"
        },
        {
          "line": 59,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 59,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 59,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 71,
          "value": "ACTION/PIPELINE-DIRECTION"
        },
        {
          "line": 79,
          "value": "ACTION/FAST-PATH"
        },
        {
          "line": 79,
          "value": "ACTION/RUN-LITE"
        },
        {
          "line": 79,
          "value": "DIRECTION/START"
        },
        {
          "line": 80,
          "value": "ACTION/RUN-ITER"
        },
        {
          "line": 80,
          "value": "DIRECTION/START"
        },
        {
          "line": 81,
          "value": "ACTION/RUN-STANDARD"
        },
        {
          "line": 81,
          "value": "BIBLIOTHEQUE/SELECT"
        },
        {
          "line": 81,
          "value": "DIRECTION/START"
        },
        {
          "line": 82,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 82,
          "value": "ACTION/ROUTING"
        },
        {
          "line": 82,
          "value": "ACTION/RUN-DIRECTION"
        },
        {
          "line": 82,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 82,
          "value": "DIRECTION/START"
        },
        {
          "line": 82,
          "value": "DIRECTION/VISUAL_TARGET"
        },
        {
          "line": 82,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 82,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 83,
          "value": "ACTION/RUN-SYSTEM"
        },
        {
          "line": 83,
          "value": "BIBLIOTHEQUE/COMPONENTS"
        },
        {
          "line": 83,
          "value": "DIRECTION/START"
        },
        {
          "line": 89,
          "value": "DIRECTION/START"
        },
        {
          "line": 101,
          "value": "ACTION/FIRST-RENDER"
        },
        {
          "line": 101,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 101,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 101,
          "value": "SAVOIR/STYLE"
        },
        {
          "line": 103,
          "value": "DIRECTION/CREATIVE-BOOT"
        },
        {
          "line": 103,
          "value": "SAVOIR/CRAFT"
        },
        {
          "line": 105,
          "value": "DIRECTION/DOMAIN-FRAME"
        },
        {
          "line": 105,
          "value": "SAVOIR/SOURCE"
        },
        {
          "line": 117,
          "value": "ACTION/UI-UX-REALITY"
        },
        {
          "line": 121,
          "value": "ACTION/CLOSE-PACKAGE"
        },
        {
          "line": 127,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 144,
          "value": "DIRECTION/DIRECTION-ATELIER"
        },
        {
          "line": 144,
          "value": "DIRECTION/DOUBLE-LOOP"
        },
        {
          "line": 144,
          "value": "DIRECTION/EXTERNAL-START"
        },
        {
          "line": 144,
          "value": "DIRECTION/FIRST-OBJECT"
        },
        {
          "line": 146,
          "value": "SAVOIR/STYLE"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "MODE": 2,
        "DECISION": 3,
        "RISK": 3,
        "SCOPE": 2,
        "ARTIFACT": 1,
        "LIMIT": 1,
        "NEXT-ACTION": 1,
        "OWNER": 3,
        "NEXT-PROOF": 3,
        "EXIT-CONDITION": 1,
        "DIRECTION": 13,
        "LITE": 6,
        "ACTION": 3,
        "SAVOIR": 3,
        "BIBLIOTHEQUE": 4,
        "GOVERNANCE": 1,
        "ITER": 3,
        "STANDARD": 3,
        "EXECUTION-SNAPSHOT": 2,
        "CONSTRAINT": 1,
        "DECISION-INTENT": 1,
        "DECISION-CHANGE": 2,
        "VISUAL_TARGET": 2,
        "CFT-00": 3,
        "DIRECTION-ATELIER": 1,
        "CHANGELOG": 1,
        "FIRST-OBJECT": 2,
        "FIRST-RENDER": 1,
        "STATE": 1,
        "ISSUE": 1,
        "VERDICT": 1,
        "NOT-VERIFIED": 1,
        "NOT-OBSERVED": 1,
        "POLISHED": 1,
        "SLOP-FREE": 1,
        "APPROVED": 1,
        "RUN_CARD": 1
      }
    },
    "skills/design-governance-practice/references/canonical_minimum.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Aide-mémoire canonique minimal"
        },
        {
          "line": 5,
          "level": 2,
          "title": "Source et limites"
        },
        {
          "line": 9,
          "level": 2,
          "title": "Séparations indispensables"
        },
        {
          "line": 22,
          "level": 2,
          "title": "Priorité"
        }
      ],
      "fences": [],
      "table_separator_lines": [],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [],
      "uppercase_code_tokens_not_a_status_registry": {
        "MODE": 1,
        "LITE": 1,
        "ITER": 1,
        "STANDARD": 1,
        "DIRECTION": 1,
        "STATE": 1,
        "ISSUE": 1,
        "VERDICT": 1,
        "DECISION-INTENT": 1,
        "DECISION-CHANGE": 1,
        "NOT-VERIFIED": 1,
        "NOT-OBSERVED": 1
      }
    },
    "skills/design-governance-practice/references/examples.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Exemples de runs"
        },
        {
          "line": 5,
          "level": 2,
          "title": "LITE — correctif local"
        },
        {
          "line": 23,
          "level": 2,
          "title": "DIRECTION — première scène identitaire"
        },
        {
          "line": 49,
          "level": 2,
          "title": "DIRECTION + STYLE — profil d’expression situé"
        },
        {
          "line": 69,
          "level": 2,
          "title": "SYSTÈME — composant partagé"
        }
      ],
      "fences": [
        {
          "line": 11,
          "language": "text"
        },
        {
          "line": 29,
          "language": "text"
        },
        {
          "line": 55,
          "language": "text"
        },
        {
          "line": 75,
          "language": "text"
        }
      ],
      "table_separator_lines": [],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 53,
          "value": "STYLE/DIGITAL_MEMORY"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "ILLUSTRATIVE": 1,
        "SIMULATED": 1,
        "RUN_CARD": 3,
        "LITE": 1,
        "DECISION-INTENT": 1,
        "CREATIVE-REVIEW": 1,
        "PROFILE-DECISION": 1
      }
    },
    "skills/design-governance-practice/references/flow.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Flux de décision V1"
        }
      ],
      "fences": [
        {
          "line": 5,
          "language": "mermaid"
        }
      ],
      "table_separator_lines": [],
      "unclosed_internal_fence": false,
      "version_mentions": [],
      "route_mentions_lexical": [
        {
          "line": 20,
          "value": "DIRECTION/START"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {}
    },
    "skills/design-governance-practice/references/machine_projection.md": {
      "headings": [
        {
          "line": 1,
          "level": 1,
          "title": "Projection machine-readable"
        }
      ],
      "fences": [
        {
          "line": 12,
          "language": "yaml"
        }
      ],
      "table_separator_lines": [],
      "unclosed_internal_fence": false,
      "version_mentions": [
        {
          "line": 5,
          "text": "La forme de référence ci-dessous est présentée en YAML pour la lecture. Une version JSON contrôlable et son schéma sont fournis dans `schemas/` :"
        },
        {
          "line": 92,
          "text": "`CLOSED` signifie que la trace et les artefacts sont persistés. Pour un verdict `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, `proof.provenance` est obligatoire et doit identifier l’artefact, sa version, la méthode et la date d’observation. Pour une RUN_CARD `DIRECTION` clôturée, `creative_close` est obligatoire et doit contenir `presence`, `signature`, `craft_detail`, `dominant_defect` et `next_polish_action`. Lorsqu’une route `SAVOIR/STYLE` est activée, `profile_decision` peut transporter la décision, les dials, la contre-indication et la preuve de son effet ; s’il est présent, ses quatre champs sont obligatoires. Il peut coexister avec `RETURN`, `EXPLORATORY` ou une issue déclarée ; un axe ou une preuve peut rester `NOT-VERIFIED`. Il ne doit jamais être interprété comme un verdict positif."
        }
      ],
      "route_mentions_lexical": [
        {
          "line": 92,
          "value": "SAVOIR/STYLE"
        }
      ],
      "uppercase_code_tokens_not_a_status_registry": {
        "STATE": 1,
        "ISSUE": 1,
        "VERDICT": 1,
        "GATE": 1,
        "AXIS": 1,
        "DECISION-CHANGE": 1,
        "PASS": 1,
        "PASS-WITH-RESERVATION": 1,
        "NOT-VERIFIED": 2,
        "NOT-OBSERVED": 1,
        "CLOSED": 1,
        "ACCEPTED": 1,
        "ACCEPTED-WITH-RESERVATION": 1,
        "DIRECTION": 1,
        "RETURN": 1,
        "EXPLORATORY": 1,
        "RETURNED": 1,
        "BLOCKED": 1,
        "ESCALATED": 1,
        "SELF-DECLARED": 1,
        "ATLAS-PASS": 1,
        "POLISHED": 1,
        "SLOP-FREE": 1
      }
    }
  },
  "markdown_links": [
    {
      "file": "README.md",
      "line": 19,
      "label": "`V1/official/READING_MAP.md`",
      "target": "V1/official/READING_MAP.md",
      "resolved": "V1/official/READING_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 21,
      "label": "`ORCHESTRATION_MAP.md`",
      "target": "V1/official/ORCHESTRATION_MAP.md",
      "resolved": "V1/official/ORCHESTRATION_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 25,
      "label": "`V1/official/QUICKSTART.md`",
      "target": "V1/official/QUICKSTART.md",
      "resolved": "V1/official/QUICKSTART.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 37,
      "label": "Quickstart",
      "target": "V1/official/QUICKSTART.md",
      "resolved": "V1/official/QUICKSTART.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 37,
      "label": "Glossaire",
      "target": "V1/official/GLOSSAIRE.md",
      "resolved": "V1/official/GLOSSAIRE.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 39,
      "label": "`V1/official/GLOSSAIRE.md`",
      "target": "V1/official/GLOSSAIRE.md",
      "resolved": "V1/official/GLOSSAIRE.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "README.md",
      "line": 59,
      "label": "`DIRECTION.md`",
      "target": "V1/official/DIRECTION.md#les-cinq-règles-absolues",
      "resolved": "V1/official/DIRECTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 31,
      "label": "`READING_MAP.md`",
      "target": "./READING_MAP.md",
      "resolved": "V1/official/READING_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 51,
      "label": "`DIRECTION.md`",
      "target": "DIRECTION.md#les-cinq-règles-absolues",
      "resolved": "V1/official/DIRECTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 306,
      "label": "`DIRECTION.md`",
      "target": "./DIRECTION.md",
      "resolved": "V1/official/DIRECTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 307,
      "label": "`ACTION.md`",
      "target": "./ACTION.md",
      "resolved": "V1/official/ACTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 308,
      "label": "`SAVOIR.md`",
      "target": "./SAVOIR.md",
      "resolved": "V1/official/SAVOIR.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 309,
      "label": "`BIBLIOTHEQUE.md`",
      "target": "./BIBLIOTHEQUE.md",
      "resolved": "V1/official/BIBLIOTHEQUE.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/QUICKSTART.md",
      "line": 310,
      "label": "`CHANGELOG.md`",
      "target": "./CHANGELOG.md",
      "resolved": "V1/official/CHANGELOG.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/READING_MAP.md",
      "line": 9,
      "label": "`ORCHESTRATION_MAP.md`",
      "target": "ORCHESTRATION_MAP.md",
      "resolved": "V1/official/ORCHESTRATION_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/READING_MAP.md",
      "line": 24,
      "label": "`DIRECTION.md`",
      "target": "DIRECTION.md#les-cinq-règles-absolues",
      "resolved": "V1/official/DIRECTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 17,
      "label": "`QUICKSTART.md`",
      "target": "./QUICKSTART.md",
      "resolved": "V1/official/QUICKSTART.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 17,
      "label": "`GLOSSAIRE.md`",
      "target": "./GLOSSAIRE.md",
      "resolved": "V1/official/GLOSSAIRE.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 21,
      "label": "`READING_MAP.md`",
      "target": "./READING_MAP.md",
      "resolved": "V1/official/READING_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 23,
      "label": "`ORCHESTRATION_MAP.md`",
      "target": "./ORCHESTRATION_MAP.md",
      "resolved": "V1/official/ORCHESTRATION_MAP.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 31,
      "label": "`DIRECTION.md`",
      "target": "./DIRECTION.md",
      "resolved": "V1/official/DIRECTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 32,
      "label": "`ACTION.md`",
      "target": "./ACTION.md",
      "resolved": "V1/official/ACTION.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 33,
      "label": "`SAVOIR.md`",
      "target": "./SAVOIR.md",
      "resolved": "V1/official/SAVOIR.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 34,
      "label": "`BIBLIOTHEQUE.md`",
      "target": "./BIBLIOTHEQUE.md",
      "resolved": "V1/official/BIBLIOTHEQUE.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "V1/official/README.md",
      "line": 35,
      "label": "`CHANGELOG.md`",
      "target": "./CHANGELOG.md",
      "resolved": "V1/official/CHANGELOG.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "skills/design-governance-practice/SKILL.md",
      "line": 143,
      "label": "references/examples.md",
      "target": "references/examples.md",
      "resolved": "skills/design-governance-practice/references/examples.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "skills/design-governance-practice/SKILL.md",
      "line": 145,
      "label": "references/flow.md",
      "target": "references/flow.md",
      "resolved": "skills/design-governance-practice/references/flow.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "skills/design-governance-practice/SKILL.md",
      "line": 147,
      "label": "references/machine_projection.md",
      "target": "references/machine_projection.md",
      "resolved": "skills/design-governance-practice/references/machine_projection.md",
      "file_present": true,
      "anchor_checked": false
    },
    {
      "file": "skills/design-governance-practice/SKILL.md",
      "line": 148,
      "label": "references/canonical_minimum.md",
      "target": "references/canonical_minimum.md",
      "resolved": "skills/design-governance-practice/references/canonical_minimum.md",
      "file_present": true,
      "anchor_checked": false
    }
  ],
  "json_syntax": {
    "schemas/domain_frame.schema.json": "parseable",
    "schemas/examples/domain_frame.example.json": "parseable",
    "schemas/examples/production_contracts.example.json": "parseable",
    "schemas/examples/research_brief.example.json": "parseable",
    "schemas/fixtures/invalid_accepted_before_decision.json": "parseable",
    "schemas/fixtures/invalid_accepted_lost_in_build.json": "parseable",
    "schemas/fixtures/invalid_accepted_without_limitations.json": "parseable",
    "schemas/fixtures/invalid_accepted_without_observed.json": "parseable",
    "schemas/fixtures/invalid_accepted_without_provenance.json": "parseable",
    "schemas/fixtures/invalid_capability_available_without_basis.json": "parseable",
    "schemas/fixtures/invalid_capability_profile_missing_basis.json": "parseable",
    "schemas/fixtures/invalid_creative_close_missing_field.json": "parseable",
    "schemas/fixtures/invalid_critical_placeholder_protection.json": "parseable",
    "schemas/fixtures/invalid_critical_without_protection.json": "parseable",
    "schemas/fixtures/invalid_direction_missing_creative_close.json": "parseable",
    "schemas/fixtures/invalid_direction_missing_object.json": "parseable",
    "schemas/fixtures/invalid_direction_missing_status.json": "parseable",
    "schemas/fixtures/invalid_direction_missing_trace_locator.json": "parseable",
    "schemas/fixtures/invalid_direction_untransformed_anchor.json": "parseable",
    "schemas/fixtures/invalid_empty_proof.json": "parseable",
    "schemas/fixtures/invalid_fail_assumed_accepted.json": "parseable",
    "schemas/fixtures/invalid_global_axis_verdict.json": "parseable",
    "schemas/fixtures/invalid_lite_missing_minimum.json": "parseable",
    "schemas/fixtures/invalid_missing_proof.json": "parseable",
    "schemas/fixtures/invalid_profile_decision_missing_evidence.json": "parseable",
    "schemas/fixtures/invalid_state_held.json": "parseable",
    "schemas/fixtures/valid_closed_return.json": "parseable",
    "schemas/fixtures/valid_direction_exploratory_untransformed.json": "parseable",
    "schemas/fixtures/valid_direction_with_profile_decision.json": "parseable",
    "schemas/production_contracts.schema.json": "parseable",
    "schemas/research_brief.schema.json": "parseable",
    "schemas/run_card.example.json": "parseable",
    "schemas/run_card.schema.json": "parseable",
    "scripts/package_manifest.json": "parseable"
  },
  "manifest": {
    "version": "1.0.0",
    "github": [
      ".github/workflows/validate.yml",
      ".gitignore",
      "README.md",
      "RELEASE_NOTES.md",
      "V1/official/ACTION.md",
      "V1/official/BIBLIOTHEQUE.md",
      "V1/official/CHANGELOG.md",
      "V1/official/DIRECTION.md",
      "V1/official/GLOSSAIRE.md",
      "V1/official/QUICKSTART.md",
      "V1/official/README.md",
      "V1/official/READING_MAP.md",
      "V1/official/ORCHESTRATION_MAP.md",
      "V1/official/SAVOIR.md",
      "schemas/domain_frame.schema.json",
      "schemas/examples/domain_frame.example.json",
      "schemas/examples/production_contracts.example.json",
      "schemas/examples/research_brief.example.json",
      "schemas/fixtures/invalid_accepted_before_decision.json",
      "schemas/fixtures/invalid_accepted_lost_in_build.json",
      "schemas/fixtures/invalid_accepted_without_limitations.json",
      "schemas/fixtures/invalid_accepted_without_observed.json",
      "schemas/fixtures/invalid_accepted_without_provenance.json",
      "schemas/fixtures/invalid_capability_available_without_basis.json",
      "schemas/fixtures/invalid_capability_profile_missing_basis.json",
      "schemas/fixtures/invalid_creative_close_missing_field.json",
      "schemas/fixtures/invalid_critical_without_protection.json",
      "schemas/fixtures/invalid_critical_placeholder_protection.json",
      "schemas/fixtures/invalid_direction_missing_creative_close.json",
      "schemas/fixtures/invalid_direction_missing_object.json",
      "schemas/fixtures/invalid_direction_missing_status.json",
      "schemas/fixtures/invalid_direction_missing_trace_locator.json",
      "schemas/fixtures/invalid_direction_untransformed_anchor.json",
      "schemas/fixtures/invalid_empty_proof.json",
      "schemas/fixtures/invalid_fail_assumed_accepted.json",
      "schemas/fixtures/invalid_global_axis_verdict.json",
      "schemas/fixtures/invalid_lite_missing_minimum.json",
      "schemas/fixtures/invalid_missing_proof.json",
      "schemas/fixtures/invalid_profile_decision_missing_evidence.json",
      "schemas/fixtures/invalid_state_held.json",
      "schemas/fixtures/valid_closed_return.json",
      "schemas/fixtures/valid_direction_exploratory_untransformed.json",
      "schemas/fixtures/valid_direction_with_profile_decision.json",
      "schemas/production_contracts.schema.json",
      "schemas/research_brief.schema.json",
      "schemas/run_card.example.json",
      "schemas/run_card.schema.json",
      "scripts/build_distributions.sh",
      "scripts/package_manifest.json",
      "scripts/validate_all.py",
      "scripts/validate_reading_map.py",
      "scripts/validate_contracts.py",
      "scripts/validate_design_governance.py",
      "scripts/validate_run_card.py",
      "scripts/read_route.py",
      "skills/design-governance-practice/SKILL.md",
      "skills/design-governance-practice/references/canonical_minimum.md",
      "skills/design-governance-practice/references/examples.md",
      "skills/design-governance-practice/references/flow.md",
      "skills/design-governance-practice/references/machine_projection.md"
    ],
    "local": [
      "README.md",
      "official/ACTION.md",
      "official/BIBLIOTHEQUE.md",
      "official/CHANGELOG.md",
      "official/DIRECTION.md",
      "official/GLOSSAIRE.md",
      "official/QUICKSTART.md",
      "official/README.md",
      "official/READING_MAP.md",
      "official/ORCHESTRATION_MAP.md",
      "official/SAVOIR.md",
      "schemas/domain_frame.schema.json",
      "schemas/examples/domain_frame.example.json",
      "schemas/examples/production_contracts.example.json",
      "schemas/examples/research_brief.example.json",
      "schemas/fixtures/invalid_accepted_before_decision.json",
      "schemas/fixtures/invalid_accepted_lost_in_build.json",
      "schemas/fixtures/invalid_accepted_without_limitations.json",
      "schemas/fixtures/invalid_accepted_without_observed.json",
      "schemas/fixtures/invalid_accepted_without_provenance.json",
      "schemas/fixtures/invalid_capability_available_without_basis.json",
      "schemas/fixtures/invalid_capability_profile_missing_basis.json",
      "schemas/fixtures/invalid_creative_close_missing_field.json",
      "schemas/fixtures/invalid_critical_without_protection.json",
      "schemas/fixtures/invalid_critical_placeholder_protection.json",
      "schemas/fixtures/invalid_direction_missing_creative_close.json",
      "schemas/fixtures/invalid_direction_missing_object.json",
      "schemas/fixtures/invalid_direction_missing_status.json",
      "schemas/fixtures/invalid_direction_missing_trace_locator.json",
      "schemas/fixtures/invalid_direction_untransformed_anchor.json",
      "schemas/fixtures/invalid_empty_proof.json",
      "schemas/fixtures/invalid_fail_assumed_accepted.json",
      "schemas/fixtures/invalid_global_axis_verdict.json",
      "schemas/fixtures/invalid_lite_missing_minimum.json",
      "schemas/fixtures/invalid_missing_proof.json",
      "schemas/fixtures/invalid_profile_decision_missing_evidence.json",
      "schemas/fixtures/invalid_state_held.json",
      "schemas/fixtures/valid_closed_return.json",
      "schemas/fixtures/valid_direction_exploratory_untransformed.json",
      "schemas/fixtures/valid_direction_with_profile_decision.json",
      "schemas/production_contracts.schema.json",
      "schemas/research_brief.schema.json",
      "schemas/run_card.example.json",
      "schemas/run_card.schema.json",
      "scripts/package_manifest.json",
      "scripts/validate_all.py",
      "scripts/validate_reading_map.py",
      "scripts/validate_contracts.py",
      "scripts/validate_design_governance.py",
      "scripts/validate_run_card.py",
      "scripts/read_route.py",
      "skill/SKILL.md",
      "skill/references/canonical_minimum.md",
      "skill/references/examples.md",
      "skill/references/flow.md",
      "skill/references/machine_projection.md"
    ]
  }
}
```
