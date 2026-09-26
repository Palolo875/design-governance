# DG-AUDIT-001 — Phase 9.05 — RESISTANCE-RESULTS : migration, anciens aliases et promotion

**Date :** 24 septembre 2026. **Baseline :** B01 inchangée. **Scénario §19 :** 18 « Migration », couverture prévue `TARGETED`. **Portée :** relecture des propriétaires, cinq validations `RUN_CARD` sur copies en mémoire, dix appels ciblés du lecteur de routes et contrôle de deux distributions reconstruites dans une copie isolée. Aucune migration de consumer, promotion, dépréciation nouvelle ni publication effectuée. La phase 6.02 reste de côté à la demande de l'utilisateur. Aucun patch ni verdict global.

## 1. Continuité et sources exactes

Plan maître, 9.04 immédiatement précédent, matrice 9.01, diagnostic propriétaire `Audit_CHANGELOG_Phase2_01_Baseline_Autorite_Cycle_Migration_Limites.md` et antécédents 4.09/8.02 repris. Protocole indépendant v2.0 §3–4/§19 : une compatibilité de texte et une validation de schéma ne prouvent pas une migration de consumers. Règles B01 relues : `CHANGELOG.md` 23–56 (autorité, cycle, cinq reclassifications), `ACTION/RUN-SYSTEM` 379–387 (impact, consumers, migration, rollback), `BIBLIOTHEQUE/EVOLUTION` 733–774 (gain, maintien, statut et prohibition des anciens aliases), `DIRECTION/START` 119–155 (objet direct et risque), `READING_MAP.md` et `read_route.py` (accès dérivé), schéma/validateur `RUN_CARD` (projection). La source propriétaire du cycle de vie reste CHANGELOG ; BIBLIOTHEQUE ne gouverne la promotion structurelle que si son déclencheur s'applique.

SHA-256 recalculés depuis les deux fichiers sources exacts : compilation B01 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`. Extraction des 60 fichiers de la compilation en copie de travail ; les hashes indépendants de `CHANGELOG.md` `0876654994f063ebb670392a5967044ad483bbdb8ebf6b5ce8a156609f08df45` et du manifeste `bef40232b2cbb1fdc8fda4d2bfc6bb752e9abbc3705d9a662eb44aa8da266f8b` correspondent aux checkpoints. Aucun octet source B01 changé.

## 2. Mapping positif et frontière négative

Les cinq identifiants historiques restent dans la table de migration CHANGELOG. Ils ne sont pas des routes actives ; leur ancien nom peut être conservé dans une **trace de compatibilité**, puis la responsabilité est reclassée selon le contenu réel. `BIBLIOTHEQUE/EVOLUTION` 774 les dit `DEPRECATED` et interdit leur sélection dans un nouveau run.

| Alias historique | Reclassification conditionnelle vérifiée | Limite de l'essai |
|---|---|---|
| `REFERENCES/QUERY` | `SAVOIR/TOOLS` si recherche ou claim à contrôler. | La requête seule n'est pas une preuve. |
| `REFERENCES/SOURCE` | `SAVOIR/SOURCE` si ancre/référence observée. | Ne pas déclarer l'ancienne route active. |
| `REFERENCES/ASSET` | `DIRECTION/VISUAL_TARGET` pour rôle/production **et** `SAVOIR/SOURCE` pour provenance/limite. | Le mapping a deux responsabilités ; aucun droit d'asset inféré. |
| `REFERENCES/MEMORY` | `TRACE-LOCATOR` et artefact local. | Une mémoire n'est pas une source normative. |
| `REFERENCES/CORPUS` | Propriétaire normatif réellement modifié ; CHANGELOG seulement si le package change. | Owner à établir, pas de route unique créée par commodité. |

Si le contenu ancien ne permet pas d'établir le propriétaire, CHANGELOG 56 prescrit `NOT-VERIFIED` ou `EXPLORATORY`, pas une reclassification arbitraire. La recherche littérale des cinq aliases parmi les 60 sources reconstruites les retrouve dans CHANGELOG, BIBLIOTHEQUE et le contrôle de présence de `validate_design_governance.py` ; les autres façades, la skill pratique et les exemples de `RUN_CARD` ne les proposent pas comme chemin quotidien. Le validateur documentaire contrôle que les termes de cycle et les aliases **figurent** dans CHANGELOG, sans contrôler leur utilisation au cours d'un run.

## 3. Replays ciblés et résultats observés

Les cinq cartes sont des copies profondes en mémoire de `schemas/fixtures/valid_closed_return.json`, contrôlées par `validate_card(document, schema)` en mode ordinaire. Changer `sources`, `decision` ou supprimer `owner` constitue le contraste ; les déclarations de preuve de la fixture ne sont pas des observations de migration. Le test n'utilise pas le mode strict et n'accorde aucun statut de route.

| Cas | Projection B01 | Décision normative séparée |
|---|---|---|
| **R0 : témoin** `ACTION/RUN-SYSTEM` dans `sources`, run fictif retourné. | **Admise.** | Structure témoin seulement ; aucun consumer migré. |
| **R1 : sélection nouvelle** de `REFERENCES/SOURCE` dans `sources`. | **Admise.** | À refuser selon CHANGELOG 46 et BIB 774 ; `sources` est une liste de chaînes non vides, sans catalogue de routes ni filtre `DEPRECATED`. |
| **R2 : compatibilité** : ancien nom mentionné uniquement dans le récit de décision, `SAVOIR/SOURCE` sélectionné. | **Admise.** | Forme de reclassification cohérente **dans cette hypothèse** ; le texte ne prouve pas le contenu ni l'owner de l'ancien consumer. |
| **R3 : promotion alléguée** d'une route `PILOT` vers `ADOPTED` dans `decision`, sans inventaire de consumers ni gain mesuré. | **Admise.** | À laisser en attente du dossier ACTION, du gain/maintien applicable et de la décision explicite de l'owner du corpus. Une carte valide n'est pas l'acte de promotion. |
| **R4 : `owner` supprimé** du témoin. | **Refusée**, champ obligatoire `owner` absent. | Garde-fou de présence conservé ; un owner renseigné ne prouve ni son mandat ni la migration. |

**Bilan machine : cinq appels, quatre admissions et un refus.** R1 et R3 traversent la projection malgré leur incompatibilité avec les conditions normatives **supposées par ces exemples**. C'est une frontière entre forme de la `RUN_CARD` et décision de migration ; aucun verdict selon lequel le validateur devrait posséder tout le cycle de vie n'en découle. `RUN_CARD.sources` ne relie pas un identifiant à l'état courant d'un catalogue ; F-ACT-015/021 et F-CHG-001 demeurent des voisins provisoires sans compter une nouvelle fiche par mutation.

`read_route.py` sur la copie B01 refuse **5/5** anciens aliases (`locator inconnu`). Il sert `DIRECTION/VISUAL_TARGET`, `ACTION/RUN-SYSTEM` et `BIBLIOTHEQUE/EVOLUTION`, mais refuse également `SAVOIR/TOOLS` et `SAVOIR/SOURCE` : leurs sections existent dans SAVOIR, mais ces locators ne figurent pas parmi les entrées CLI de `READING_MAP`. L'ancien refus CLI protège donc d'une activation par ce lecteur ; il **ne valide pas** toutes les destinations du mapping et n'implique pas l'absence des sections SAVOIR. Ce point prolonge la frontière d'index déjà tracée par F-DIR-028/F-ACT-001 et 8.02, sans exiger d'ajouter automatiquement les deux routes à la table.

Une autre copie isolée du package reconstruit a produit deux archives avec le build B01. ZIP GitHub : **60 fichiers**, Local : **56**, CRC intègre ; `CHANGELOG`, `BIBLIOTHEQUE`, `SAVOIR`, `READING_MAP` sont identiques octet pour octet aux sources B01 dans les deux. Les trois essais ciblés de lecteur (`REFERENCES/SOURCE`, `SAVOIR/SOURCE`, `DIRECTION/VISUAL_TARGET`) reproduisent les mêmes codes **1, 1, 0** dans chaque stage. Cela confirme **le transport de cette frontière dans des exports reconstruits**, pas l'état d'une release distante ni la présence d'un consumer migré. Un premier lancement du build depuis un répertoire extérieur a échoué sur la recherche de fixture dans le répertoire appelant ; relancé depuis la racine de la copie, le build a passé. C'est l'occurrence déjà ouverte **F-ALL-002**, sans nouveau constat.

## 4. Dépréciation et promotion : décisions à ne pas confondre

**Historique compatible :** garder l'ancien nom uniquement dans la trace de l'objet hérité, classer son contenu dans la responsabilité actuelle et vérifier owner, scope et preuve avant de dire que le consumer est migré. **Nouveau run :** ne sélectionner ni un ancien alias ni une route `DEPRECATED`. Le refus du lecteur CLI n'empêche pas de les écrire dans une carte admise ; la règle propriétaire s'applique donc à la décision humaine ou à l'orchestrateur dans le scope réel.

**Route candidate :** une route `PILOT` est testée dans un périmètre déclaré ; `ADOPTED` réclame contrat, gain et maintenance acceptés, avec source propriétaire unique, compatibilité, preuve, limite, revue et décision du propriétaire du corpus. ACTION prépare la cartographie des consumers, migration, rollback et non-régression ; BIBLIOTHEQUE ajoute les usages contrastés et le gain observé pour une route structurelle durable. Un nom dans `decision` ou une carte SYSTÈME validée ne remplace aucune de ces pièces.

**Transition ouverte F-CHG-001 :** la table autorise `ADOPTED → DEPRECATED → ABANDONED`, mais les routes canoniques du seed n'ont pas de statut initial individuel démontré et un `PILOT` avec consumers à retirer n'a pas de transition honnête vers `DEPRECATED` sans adoption préalable. Ce replay confirme la difficulté **dans le contrat de cycle de vie**, pas une route seed réellement retirée ni un PILOT réellement abandonné. Une décision de migration peut rester documentée avec owner, compatibilité et réserve sans inventer un gain passé ou changer silencieusement de statut. Arbitrage et éventuel patch restent aux phases 10–11.

## 5. Sortie et suite

Le scénario 18 est éprouvé **au niveau documentaire et machine** : mapping présent et transporté, anciens aliases refusés par la CLI, sélection nouvelle cependant admise par la projection `RUN_CARD`, adoption textuelle non contrôlée par elle. Il manque un inventaire de consumers réels, leurs usages avant/après, la preuve de compatibilité et rollback, la décision du propriétaire du corpus et le résultat d'une migration pour une conclusion d'efficacité. `TARGETED` documentaire terminé ; aucune migration effective attestée.

**Cumul phase 9 : 6/20 scénarios examinés en contrat** (06, 15, 16, 17, 18, 20), **0/20 stress complets d'efficacité clos** ; les 14 autres scénarios de la matrice restent ouverts. S21 stage/ZIP demeure un antécédent distinct de 4.09. **Registre inchangé : 157 fiches provisoires ; aucun nouvel ID, patch B01 ou verdict global.**

**Prochaine unité proposée : 9.06, scénario 19 « Surcharge procédurale »**, selon la matrice 9.01. Comparer un micro-delta sur chemin court à un cas où risque/preuve exigent des étapes supplémentaires ; retirer seulement les étapes sans effet sur décision, artefact ou preuve, sans inférer une charge cognitive vécue. Relire DIRECTION/START, ACTION/CLOSE-EXIT-CHECK, SAVOIR, 5.01–5.04 et 9.01 avant essai. **6.02 reste différée** jusqu'à nouvelle demande.
