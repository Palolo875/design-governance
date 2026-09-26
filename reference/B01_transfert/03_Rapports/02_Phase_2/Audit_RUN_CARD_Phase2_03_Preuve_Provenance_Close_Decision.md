# DG-AUDIT-001 — Phase 2 — RUN_CARD, segment 3 : preuve, provenance et décision

## Périmètre, reprise et intégrité

- Passage A–D adjacent : `audit_work/package/schemas/run_card.schema.json` **98–153/180** et `audit_work/package/schemas/run_card.example.json` **66–90/102**. Reprise du protocole externe v2.0 §12, du plan maître et des rapports RUN_CARD segments 1 et 2 ; couverture cumulée : schéma **1–153/180**, exemple **1–90/102**. `closure` et conditions finales du schéma seront lues A–D dans la prochaine unité ; les règles de validation qui dépendent de `closure` sont seulement consultées ici pour éprouver les champs présents.
- Baseline B01 recalculée inchangée : compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, ACTION `d73ad55167f71f775954092c3a91c00347753cae520031202f946b228257b50d`, DIRECTION `f634bc561dab243e53fa1a988c2a49565f3d6330a8e5af0e4fbaea4128bf2a7f`, SAVOIR `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Autorités relues : ACTION 206–236 distingue intention et conséquence observée, 327–331 borne la validation, 391–411 traite le paquet créatif et la fraîcheur, 653–665 définit provenance et preuve adaptée ; DIRECTION 482–502 admet un arrêt après observation sans retouche inutile ; SAVOIR/STYLE 580–593 transporte le choix de profil. Le validateur 205–273 et 276–334 est consulté sur les dépendances de ce segment, sans revendiquer son audit complet. Le package cible reste intact.

## Passage A — architecture et exemple

| Champs du schéma | Forme et emplacement | Lecture de l'exemple |
|---|---|---|
| `proof`, 98–121 | Objet fermé exigeant `observed` et `not_verified`, chacun tableau de textes ; au moins un des deux est non vide. `provenance`, objet facultatif dans la structure simple, porte quatre chaînes non vides si présent. | 66–79 annonce une observation limitée aux viewports inspectés, laisse préférence et utilisabilité générale non vérifiées, puis inscrit locator, version, méthode et date. Le locator `chemin-ou-url-local` est un placeholder d'exemple, non un rendu inspecté dans cet audit. |
| `creative_close`, 122–133 | Objet facultatif dans la structure simple, cinq chaînes requises quand présent : présence, signature, détail de craft, défaut dominant et action de polish suivante. | 84–90 décrit une scène matérielle, sa relation au produit, la lisibilité des viewports et un défaut mobile avec correction projetée. Le validateur rend le bloc obligatoire pour DIRECTION `CLOSED`. |
| `profile_decision`, 134–144 | Objet facultatif, quatre chaînes obligatoires s'il est renseigné : décision, dials, contre-indication et preuve. | Absent dans l'exemple ; aucune sélection de profil ne peut être déduite de ce silence. La trace locale peut porter les quatre libellés SAVOIR lorsque le profil intervient. |
| `decision_change`, 145–153 | Objet facultatif dans la forme simple ; `value` et `evidence` sont des chaînes libres non vides. | 80–83 attribue un remplacement de composition à une comparaison de captures ; ce récit illustratif n'est pas une capture jointe ou vérifiée par le schéma. |

La `proof.provenance` structure où/quand/comment une observation est revendiquée. `creative_close` rend visibles des jugements perceptuels et une limite ; `profile_decision` explicite un choix éventuel ; `decision_change` qualifie une conséquence après observation. Leurs fonctions ne sont pas interchangeables avec un résultat de tâche exécutée.

## Passage B — contrat sémantique et conflits bornés

| Interface | Protection existante | Limite démontrée et rattachement |
|---|---|---|
| Observation / non-vérification | Deux listes vides sont rejetées ; un verdict accepté exige une `observed` non vide ; un claim exactement identique dans les deux listes est rejeté. Un run exploratoire peut n'avoir que `not_verified`. | Les textes ne portent ni axe, ni résultat mesurable, ni priorité de blocage. Une phrase identique à la casse près passe dans les deux listes, ce qui confirme la limite de preuve et de liaison du verdict déjà suivie par F-ACT-012 ; la validation structurelle ne remplace pas la relecture de la trace. |
| Provenance / fraîcheur | En cas de verdict accepté, le validateur exige les quatre champs et l'égalité `proof.provenance.artifact_locator = artifact.locator`. L'exemple donne méthode, version et date distinctes. | Une version déclarée de 2001 et une méthode « plan non exécuté » passent avec un texte `observed` alléguant un test exécuté : F-ACT-022 pour version/scope, F-ACT-018/034 pour la séparation capacité/méthode/claim. Un locator égal n'atteste ni identité des octets ni contenu ; ACTION 327–331 et 655 le dit. |
| Close créatif / arrêt utile | DIRECTION `CLOSED` sans `creative_close` est rejeté ; les cinq chaînes gardent présence, signature, craft, défaut et suite. | « Aucun défaut observé ; aucune correction utile » satisfait la forme, ce qui permet de documenter honnêtement l'arrêt, mais le champ `next_polish_action` demeure requis même sans action à faire : F-ACT-025, et la qualité ne devient pas prouvée par ces phrases. |
| Profil / temporalité | Un bloc `profile_decision` présent doit renseigner ses quatre champs ; SAVOIR demande une sélection située et une preuve de son effet. | Un profil décrit comme choisi **avant** build avec `evidence="Capture prévue demain"` passe. F-SAV-005 conserve la confusion entre hypothèse prospective et effet observé ; F-ACT-013 gouverne la conséquence canonique. L'absence du champ dans l'exemple ne prouve aucune lacune lorsque le profil n'a pas été activé. |
| Décision changée / clôture | Une DIRECTION `CLOSED` acceptée sans `decision_change` est rejetée dans l'exemple. ACTION 212–218 admet changement, confirmation, abandon ou N/A justifié après observation. | `value="N/A-JUSTIFIED"` et `evidence="À vérifier demain"` passent malgré une clôture acceptée ; le texte libre n'établit ni raison d'inapplicabilité ni observation. F-ACT-013 couvre la faible typologie et le cas des autres modes ; pas de deuxième ID. |

Les quatre champs de provenance ne contiennent pas explicitement le scope observé, le résultat par axe, le runtime, ni l'empreinte de l'artefact ; les sources humaines autorisent leur conservation dans la trace liée. Le présent audit n'infère pas que toute phrase libre est fausse : il établit précisément ce que la machine peut laisser passer. La prochaine plage jugera les effets des statuts de clôture et des conditions `allOf` ensemble.

## Passage C — épreuve sur copies en mémoire et lecteurs simulés

Commande depuis `audit_work/package` : `python3 scripts/validate_run_card.py schemas/run_card.example.json` → code 0. Quatorze mutations isolées ont été soumises à `validate_card(document, schema)` sur des copies en mémoire ; un quinzième cas isole `anyOf`. Aucun fichier du package n'a été modifié. Les résultats suivants résument les sorties effectives :

| Mutation isolée | Résultat | Portée |
|---|---|---|
| Deux listes de preuve vides sous acceptation ; même cas sous exploration | REJECT ; REJECT (`anyOf` sans branche satisfaite pour le second) | Minima présents dans le validateur et le schéma. |
| `observed=[]` sous acceptation ; `not_verified` seul sous exploration, ancre `unknown` | REJECT ; PASS | Une exploration peut conserver une preuve requise absente ; l'ancre `unknown` neutralise seulement le conflit F-RC-001 déjà établi. |
| Claim exactement commun aux deux listes ; même phrase en minuscules d'un seul côté | REJECT ; PASS | L'intersection est littérale, pas une vérification sémantique. |
| Provenance absente sous acceptation ; locator différent de l'artefact | REJECT ; REJECT | Deux garde-fous effectifs. |
| `artifact_version="2001 / ancien rendu"`, `observed_at="2001-01-01"` ; méthode `"Plan non exécuté"` accompagnée de `"Test de tâche utilisateur exécuté et réussi."` | PASS ; PASS | F-ACT-022 et F-ACT-018/034 ; ce sont des données déclarées, pas l'exécution d'un test. |
| Retirer `creative_close` en DIRECTION fermée ; inscrire défaut « aucun » et arrêt sans retouche | REJECT ; PASS | Le bloc est requis mais peut exprimer un arrêt justifié en texte libre ; F-ACT-025. |
| Ajouter `profile_decision` avec capture future ; ôter `decision_change` en DIRECTION acceptée ; renseigner N/A avec « À vérifier demain » | PASS ; REJECT ; PASS | F-SAV-005 et F-ACT-013 ; les obligations minimales n'évaluent pas la réalité de l'effet décrit. |

**Simulations d'usage.** Le designer clôt un premier rendu satisfaisant et inscrit « aucune correction utile » sans inventer de polish. Le reviewer vérifie la capture, sa version et le périmètre effectif avant d'accepter une observation, puis traite la préférence non testée comme non vérifiée. L'intégrateur refuse de convertir une méthode planifiée en test exécuté malgré une carte valide. L'owner distingue l'intention de profil d'un effet post-build et conserve dans la trace les raisons d'un N/A et la prochaine preuve. Un agent qui n'a que le JSON peut contrôler présence et quelques compatibilités, mais doit consulter les artefacts et la trace pour attester ces faits.

## Passage D — déduplication et suite

**Aucun nouvel ID dans ce segment.** Les mutations confirment F-ACT-012 (claims/axes sans lien), F-ACT-013 (conséquence faible/optionnelle selon mode), F-ACT-018/034 (claim de méthode versus exécution), F-ACT-022 (version/scope non rapprochés), F-ACT-025 (champ d'action après arrêt) et F-SAV-005 (profil avant/après observation). F-RC-001 du segment précédent n'est ni corrigé ni étendu par ces tests. L'emploi d'une date ancienne ou d'une preuve future est un **contre-exemple de validation**, pas une affirmation sur un artefact réel. Garder les protections positives relevées ci-dessus lors d'un éventuel correctif.

Le registre reste à **118 fiches provisoires** : 101 propriétaires, quatre QUICKSTART, deux READING_MAP, deux ORCHESTRATION_MAP, deux GLOSSAIRE, deux DOMAIN_FRAME, deux RESEARCH_BRIEF, deux PRODUCTION_CONTRACTS et une RUN_CARD. Aucun verdict global ni patch normatif ; la phase 2 continue.

**Prochaine unité : `run_card.schema.json` 154–180/180 et `run_card.example.json` 91–102/102.** Reprendre protocole §12, ce rapport et les deux précédents, recalculer B01, lire A–D la clôture et les conditions finales, vérifier les combinaisons state/issue/verdict/direction_status et les limites, puis passer au checkpoint RUN_CARD et aux fixtures.
