# Changelog — Design Governance V1.0.0

**Version publique :** `V1.0.0`  
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de publication :** 2026-09-19  
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## V1.0.0 — Baseline expérimentale

Design Governance V1.0.0 est une baseline publique cohérente pour diriger, construire, juger et vérifier un travail de design. Elle transforme un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

La baseline comprend :

- les cinq sources normatives de `V1/official/` ;
- les guides d’entrée, le glossaire, `READING_MAP.md` et `ORCHESTRATION_MAP.md` ;
- la skill pratique et ses références conditionnelles ;
- les contrats machine, exemples et fixtures ;
- les validateurs documentaires, de contrats et de `RUN_CARD` ;
- les contrôles de build et les distributions GitHub et Local.

La cohérence documentaire, les contrats machine, les liens, les fixtures et la reproductibilité des distributions sont contrôlés. **L’efficacité sur des runs réels, l’adoption, la charge cognitive, la qualité perceptuelle produite et la performance en production restent `NOT-VERIFIED`.**

## Autorité et maintenance

Les cinq sources normatives sont `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md` et ce fichier. Les guides d’entrée et les cartes dérivées orientent la lecture sans créer de règle concurrente. Le schéma `RUN_CARD` et ses validateurs définissent les projections machine dans leur périmètre.

Toute évolution de la baseline doit identifier une source normative unique, un propriétaire, le périmètre concerné, la compatibilité, la preuve attendue, la limite, la prochaine revue et la procédure de retour. Une évolution ne devient une règle transversale qu’après décision explicite du propriétaire du corpus.

L’historique détaillé de construction et de travail est conservé hors de la distribution publique. Il n’est pas requis pour lire, utiliser ou valider V1.

## Cycle de vie des routes

Les statuts de route décrivent la maintenance d’une route candidate ou canonique. Ils ne sont pas des verdicts de design.

| Statut | Sens | Transition autorisée |
|---|---|---|
| `PILOT` | Route locale ou candidate testée dans un périmètre déclaré. | `ADOPTED` ou `ABANDONED`. |
| `ADOPTED` | Route canonique dont le contrat, la maintenance et le gain sont acceptés. | `DEPRECATED`. |
| `DEPRECATED` | Route conservée pour migration ou compatibilité ; elle ne doit pas être choisie dans un nouveau run. | `ABANDONED` après migration. |
| `ABANDONED` | Route qui n’est plus maintenue ni proposée. | Aucune transition silencieuse. |

Les routes présentes dans le seed de la V1 constituent la baseline canonique. Toute nouvelle route ou promotion doit indiquer son problème, sa décision, son owner, son contrat, sa preuve, sa limite, sa compatibilité et sa prochaine revue.

## Migration des anciens aliases

Les aliases historiques suivants ne sont pas des routes actives. Ils sont reclassés selon ce qu’ils établissent réellement ; l’ancien identifiant peut être conservé dans une trace de compatibilité.

| Alias | Reclassification publique |
|---|---|
| `REFERENCES/QUERY` | `SAVOIR/TOOLS` pour une recherche ou un claim à vérifier. |
| `REFERENCES/SOURCE` | `SAVOIR/SOURCE` pour une ancre ou une référence observée. |
| `REFERENCES/ASSET` | `DIRECTION/VISUAL_TARGET` pour la route et le rôle de production ; `SAVOIR/SOURCE` pour provenance et limite. |
| `REFERENCES/MEMORY` | `TRACE-LOCATOR` et artefact local ; une mémoire ne devient pas une source normative. |
| `REFERENCES/CORPUS` | Le propriétaire normatif réellement concerné ; `CHANGELOG` seulement si le contenu modifie le package. |

Une reclassification ambiguë reste `NOT-VERIFIED` ou `EXPLORATORY` jusqu’à ce que son propriétaire et sa portée soient établis.

## Limites de la baseline

Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés. Elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

La baseline reste expérimentale. Toute conclusion d’usage doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.

