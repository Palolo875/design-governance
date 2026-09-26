# DG-AUDIT-001 — Phase 2 — Fixtures RUN_CARD, plage 2/3 : risque, direction et preuve

## Périmètre, reprise et intégrité

- Lecture intégrale A–D des fixtures **9–16/25**, noms alphabétiques adjacents sous `audit_work/package/schemas/fixtures`. Reprise du protocole externe v2.0 §12, du rapport fixtures 1–8, du checkpoint RUN_CARD et du plan maître. Les neuf suivantes sont seulement listées pour le point de reprise. Les propriétaires ACTION/STATUS, ACTION/RUN_CARD, ACTION/CLOSE-PACKAGE et DIRECTION/START ont été confrontés aux cas pertinents.
- Baseline B01 inchangée : compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, schéma `ea3d05118d389fdea3dde03a169a31b4982745c24f0048b16c76d3295c3d3889`, exemple `30aaead6a6f3925134a5c2d897bd5f6994d8e5cf7b045ea9bd6f3d6fbb0aa194`, validateur `ba60d5dae684ae5df6c7448fd1774ce6ded8787d81a15ac92fb3c81b80f53757`, ACTION `d73ad55167f71f775954092c3a91c00347753cae520031202f946b228257b50d`, DIRECTION `f634bc561dab243e53fa1a988c2a49565f3d6330a8e5af0e4fbaea4128bf2a7f`. Aucun fichier du package cible n'a été écrit.

## Passage A — inventaire complet des huit objets

| N° | Fixture JSON lue en entier | SHA-256 | Défaut annoncé et dépendances |
|---:|---|---|---|
| 9 | `invalid_critical_placeholder_protection.json` | `bf162b0dff3cbdd48d5c3686ad1dbab72a107058d5b46909c6327aa63f8fdac4` | Risque `critical`, contrôle « placeholder » et autres champs « todo » ; provenance manquante sous acceptation. |
| 10 | `invalid_critical_without_protection.json` | `ab5bd2e77386601d67baad0f1fa05073e1d6f39959a24c5da3a007e429fe4918` | Risque `critical` et protection `null` ; provenance manquante. |
| 11 | `invalid_direction_missing_creative_close.json` | `24ab0dbbcc26f1a8c245a64d1de5441292d19df7e7fb4d9ca0b21fdb8a99c92d` | DIRECTION fermée sans `creative_close` ; provenance manquante. |
| 12 | `invalid_direction_missing_object.json` | `fecc7054b40eb489a68bb2dd8ba77f16e7a2b041adbc81242686ffa1301802b4` | DIRECTION fermée exploratoire sans objet `direction` ; `direction_status`, `anchors` et `creative_close` manquent aussi. |
| 13 | `invalid_direction_missing_status.json` | `389688f23cce0a388ea1ddb16b51716982959a586b5cd466ce7f299d8618563c` | DIRECTION fermée acceptée sans `direction_status` ; provenance manquante. |
| 14 | `invalid_direction_missing_trace_locator.json` | `d5811148e8d23df1666fa47c6b4a9e8e9b6babd0afa54c5d9b8cd625752244c4` | DIRECTION fermée acceptée sans trace ; ancre, close et provenance manquent aussi. |
| 15 | `invalid_direction_untransformed_anchor.json` | `1aa0a784ea0e2c412284d1cab6fc64c642c6b66314e4e31e8ceeadb67c340855` | Ancre déclarée `not_transformed` avec verdict accepté ; `creative_close` et champ de description `anchors[0].transformation` manquent également. |
| 16 | `invalid_empty_proof.json` | `0adc0479ad530151fe8efd24e5c8b71210befecbf0b47b3ab0a70f69c6151b21` | LITE accepté avec les deux tableaux de preuve vides ; provenance absente. |

L'organisation par noms regroupe d'abord deux protections critiques, puis cinq clauses DIRECTION, puis un cas de preuve vide. La fixture 12 décrit un état `EXPLORATORY` et ne requiert donc pas la provenance d'un verdict accepté ; ses défauts secondaires portent sur la DIRECTION elle-même. La fixture 15 possède un champ d'ancre obligatoire manquant indépendamment du statut de transformation. Ces détails empêchent de lire le simple préfixe `invalid_` comme preuve d'une seule violation.

## Passage B — contrat et résultat du validateur

`python3 scripts/validate_run_card.py schemas/fixtures/<nom>` a retourné le code **1 pour les huit**, avec un premier diagnostic conforme au défaut annoncé. Les **huit noms sont déclarés** dans la suite de `validate_run_card.py` (lignes 430–475, 541–574) et chacun est assorti d'un `expected_message`. La suite vérifie donc le **premier rejet et sa formulation**, ce qui protège mieux la règle annoncée qu'un simple code d'échec. Son succès ne démontre ni exécution d'un contrôle critique, ni capture réelle, ni fermeture fiable d'un run.

| Fixture | Diagnostic réel de la CLI | Réparation contrefactuelle et prochain diagnostic | État après réparations supplémentaires |
|---|---|---|---|
| Placeholder critique | `critical_protection.control` placeholder | Remplacer seulement le contrôle → `owner` reste « todo » ; renseigner toute la protection → provenance exigée | PASS après protection complète et provenance |
| Protection critique absente | `critical` exige protection structurée | Ajouter cinq champs de protection → provenance exigée | PASS après provenance |
| Close absent | DIRECTION clôturée exige `creative_close` | Ajouter le close entier → provenance exigée | PASS après provenance |
| Objet DIRECTION absent | DIRECTION exige objet direction | Ajouter l'objet → statut exigé ; puis ancre exigée ; puis close exigé | PASS avec statut `PARTIALLY-HELD`, ancre `unknown` et close, verdict conservé `EXPLORATORY` |
| Statut absent | DIRECTION décidée ou clôturée exige `direction_status` | Ajouter `HELD` → provenance exigée | PASS après provenance |
| Trace absente | DIRECTION exige `trace_locator` | Ajouter trace → ancre exigée ; puis close ; puis provenance | PASS après ces trois réparations |
| Ancre non transformée | Acceptation exige `transformation_status=transformed` | Changer seulement le statut → close exigé ; ajouter close → description `transformation` exigée | PASS après déclaration de transformation et close ; test de forme uniquement |
| Preuve vide | Acceptation exige au moins une `observed` | Ajouter une observation → provenance exigée | PASS après provenance |

Toutes les réparations sont effectuées **sur copies en mémoire** avec `validate_card(document, schema)`. Changer `not_transformed` en `transformed` dans une copie n'établit **pas** qu'une ancre réelle a été transformée. Pour la preuve vide, une variante sans acceptation, `issue=EXPLORATORY` et `verdict=EXPLORATORY`, conserve deux tableaux vides et échoue aussi au `proof.anyOf` du schéma : la contrainte de non-vacuité fonctionne indépendamment de l'acceptation. En revanche, la fixture officielle de preuve vide ne teste directement que la règle `observed` de l'acceptation, comme le montre son `expected_message`.

## Passage C — usage sous contrainte et résistance

Le mainteneur voit huit diagnostics corrects et peut tenir ces oracles de rejet pour actifs. Lorsqu'il veut vérifier la frontière « un champ corrigé → carte valide », les huit essais échouent encore sur une autre règle ; en **16 fixtures auditées au total, 13** comportent au moins une invalidité secondaire après réparation ciblée (5/8 dans la plage 1 et 8/8 ici). Ce motif récurrent ne supprime pas la protection des `expected_message`, mais rend les tests peu maniables pour isoler la règle et analyser une régression future.

L'agent exécutant une tâche critique doit obtenir une protection **réellement fondée** ; ajouter cinq chaînes pour faire passer un test en mémoire n'est pas preuve que l'échec est couvert. Le designer gardant une ancre honnêtement non transformée ne transforme pas son statut pour accepter un run ; il retourne ou conserve une limite selon ACTION. Le reviewer distingue `CLOSED` de qualité ou usage vérifié ; un close présent ne valide ni la préférence humaine ni l'accessibilité. L'intégrateur contrôle le verdict et la provenance sur l'artefact livré, pas seulement l'ordre des diagnostics de la CLI.

## Passage D — constat nouveau, déduplication et suite

### F-FIX-002 — scénarios négatifs cumulant plusieurs défauts et sans voisin positif isolé

- **Gravité provisoire : significative pour la maintenabilité des tests, risque direct atténué par les diagnostics attendus.** Après réparation de leur faute nommée, **8/8 fixtures de cette plage restent invalides** ; le cumul est **13/16** sur les deux plages. Les cas critiques réclament ensuite provenance ; la trace absente cache aussi ancre et close ; l'ancre non transformée manque une description obligatoire. Les suites vérifient la phrase de rejet ciblée, donc il ne s'agit pas d'un faux succès automatique lorsque cette règle précise disparaît.
- **Effet :** il est difficile de prouver par une paire valide/invalide que l'invariant ciblé est le seul différentiel ; une fixture réparée reste rouge pour une autre raison, ce qui masque l'impact d'un correctif isolé et favorise des hypothèses erronées sur la couverture. Le cas `invalid_empty_proof` ne porte pas directement le contrôle `anyOf` non accepté ; celui-ci requiert une contre-épreuve distincte, exécutée ici.
- **Owner pressenti :** conception des fixtures et oracles de `validate_run_card.py`, avec ACTION propriétaire des exigences de risque/preuve/clôture et DIRECTION de la cible/ancre. À corriger plus tard : baser chaque test unitaire ciblé sur une carte autrement valide et fournir son voisin positif ; conserver des tests composites nommés pour les scénarios d'interaction, avec diagnostics et modes explicités. Vérifier si les neuf fixtures restantes confirment ce ratio avant sévérité ou patch définitifs.
- **Déduplication :** F-FIX-001 désigne une **fixture non inscrite dans la suite** ; F-FIX-002 désigne la **construction multi-invalide des scénarios inscrits**. F-ACT-008 concerne un autre validateur (`validate_contracts.py`) et les chemins utilisateur ; F-RC-001 concerne l'interdiction sémantique ancre/verdict. Les insuffisances de risque/provenance des contrats restent F-ACT-017/022, non des défauts nouveaux du système déduits d'un test JSON.

Le registre passe de **119 à 120 fiches provisoires** : 101 propriétaires + 16 façades/contrats antérieurs + une RUN_CARD + **deux FIXTURES**. Cette lecture maintient les rejets positifs déjà effectifs et ne modifie ni schéma, ni fixture, ni validateur. Pas de verdict global.

**Prochaine unité : fixtures 17–25/25**, de `invalid_fail_assumed_accepted.json` à `valid_direction_with_profile_decision.json`. Reprendre protocole §12, ce rapport, le premier rapport fixtures et checkpoint RUN_CARD ; revérifier B01 ; lire les neuf fichiers en entier, dont les trois `valid_*`, comparer les oracles, les défauts secondaires et le scénario positif de retour/exploration, puis décider d'un checkpoint de fixtures avant la lecture intégrale du script.
