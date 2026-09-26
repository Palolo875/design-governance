# DG-AUDIT-001 — Phase 2 — CHANGELOG, lecture propriétaire 1–63

## Cadre, continuité et baseline

- **Source propriétaire :** `audit_work/package/V1/official/CHANGELOG.md`, **lignes 1–63**, SHA-256 `0876654994f063ebb670392a5967044ad483bbdb8ebf6b5ce8a156609f08df45` ; version et baseline 1–21, autorité 23–29, cycle de vie 31–42, aliases 44–56, limites 58–62. Les lignes 3–5 portent des espaces de mise en forme Markdown qui n'altèrent pas les assertions lues.
- **Méthode :** protocole externe v2.0 §12, quatre passages A–D. Plan maître, checkpoint BIBLIOTHEQUE et rapport de sortie bloc 15 vérifiés ; consultation des interfaces DIRECTION 790/817, ACTION/RUN-SYSTEM 379–387, ACTION/MAINTENANCE 891–911, BIBLIOTHEQUE/CONTRACTS 258–284 et EVOLUTION 735–774. Les citations antérieures de CHANGELOG étaient des tests d'interface ; cette lecture couvre pour la première fois son propre texte de bout en bout.
- **Baseline B01 inchangée :** compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`. Les cinq propriétaires normatifs sont désormais lus, sans patch.
- **Lecture machine :** `validate_reading_map.py` passe. La tentative `read_route.py CHANGELOG` échoue : `CHANGELOG` n'est **pas** un locator `SECTION/ROUTE` annoncé par un titre `## ...` dans ce fichier ; ce refus ne prouve pas qu'une route canonique manque et n'ajoute pas d'occurrence à F-DIR-028/F-ACT-001. Lecture directe de la source.
- **Portée probatoire :** analyse de cohérence des contrats et simulations, pas vérification en production d'une migration, d'un pilote, de l'adoption ou d'une efficacité sur des utilisateurs.

## Passage A — architecture d'autorité et place du document

CHANGELOG est la cinquième source normative et **propriétaire du cycle de vie, des migrations et des décisions de gouvernance** (25–27, DIRECTION 790). Les quatre autres sources portent respectivement classification, preuve et clôture, jugement et structure ; les guides, cartes et distributions sont des voies d'accès dérivées, non des règles concurrentes. Le schéma `RUN_CARD` et ses validateurs régissent les projections machine **dans leur périmètre** : un schéma valide n'établit pas l'effet réel d'une route, d'un artefact ou d'une décision (25, 60).

La page compacte associe une baseline expérimentale, des critères d'évolution, une table de quatre statuts, une migration d'aliases et les limites de preuve. L'historique détaillé de construction n'est pas requis dans la distribution publique (29) ; une décision **future** doit cependant conserver source normative unique, owner, périmètre, compatibilité, preuve attendue, limite, prochaine revue et procédure de retour, puis recevoir une décision explicite du propriétaire du corpus (27). La source unique désigne la responsabilité normative d'un changement ; un impact sur d'autres contrats/consumers reste à cartographier avec ACTION/RUN-SYSTEM, sans effacer les dépendances de plusieurs fichiers.

Les termes « version publique V1.0.0 », « baseline canonique » et « expérimentation maintenue » sont compatibles **si** « canonique » indique le catalogue publié de départ, sans prétendre que son efficacité est démontrée. La ligne 21 déclare explicitement non vérifiés efficacité en runs réels, adoption, charge cognitive, qualité perceptuelle produite et performance en production. L'usage conseillé est pilote contrôlé et supervisé (6), et la ligne 62 borne toute conclusion d'usage à observation, méthode, scope et limite. La tension de **statut de cycle de vie des routes seed** demeure distincte de cette distinction de vocabulaire ; voir F-CHG-001.

## Passage B — sémantique, étapes et limites

### Baseline versus preuve de résultat (1–29, 58–62)

La baseline inclut cinq sources, guides/cartes, skill, contrats/exemples/fixtures, validateurs et deux distributions (12–19). « Contrôlés » à 21 signifie que les contrôles documentaires, liens, contrats machine, fixtures et reproductibilité ont été exercés dans leur portée. Une validation `RUN_CARD` confirme ses conditions vérifiables, **pas** la vérité de l'artefact ni une tâche utilisateur accomplie. Rien ici ne promet une certification d'accessibilité, une performance en production, une réduction de charge cognitive ou un gain d'adoption. Les constats F-ACT-015/021 sur des obligations SYSTÈME insuffisamment projetées ne sont pas annulés par le fait qu'une suite de validation de package ait réussi.

### Table du cycle de vie (31–42)

| Statut | Ce que le texte autorise | Condition ou limite qu'un lecteur doit conserver |
|---|---|---|
| `PILOT` 37 | Route locale ou candidate **testée** dans un scope déclaré ; transitions proposées `ADOPTED` ou `ABANDONED`. | Une intention non testée reste locale/exploratoire, même si un rapport annonce une preuve future. Ne confondre ni mode de run ni verdict. |
| `ADOPTED` 38 | Route canonique avec contrat, maintenance et gain **acceptés** ; transition `DEPRECATED`. | Le gain doit être observé/mesuré avec baseline/contexte/limite et usages contrastés pour une route structurelle durable (BIB 735–760) ; un PASS d'écran n'y suffit pas. |
| `DEPRECATED` 39 | Route conservée pour migration ou compatibilité, non sélectionnable dans un nouveau run ; transition `ABANDONED` après migration. | Les consumers existants et les nouveaux runs n'ont pas la même règle ; planifier migration, retour et traces historiques. |
| `ABANDONED` 40 | Route non maintenue ni proposée ; aucune transition silencieuse. | Ne pas effacer les références historiques nécessaires à la compréhension ou laisser une dépendance active sans propriétaire. |

La ligne 42 rend les routes **présentes dans le seed de la V1** « baseline canonique » et soumet toute nouvelle route ou promotion à problème, décision, owner, contrat, preuve, limite, compatibilité et prochaine revue. Elle ne donne pas de statut de cycle de vie initial individuel aux routes seed et ne démontre pas rétrospectivement leur gain ; F-CHG-001 examine la conséquence pour les transitions. L'absence de quota de réutilisations est saine : le test d'efficacité reste situé.

### Mapping des anciens aliases (44–56)

| Ancien alias | Route/trace actuelle | Frontière |
|---|---|---|
| `REFERENCES/QUERY` 50 | `SAVOIR/TOOLS` pour recherche ou claim à vérifier. | Une requête n'est pas une source probante ; dater et borner le claim si son résultat compte. |
| `REFERENCES/SOURCE` 51 | `SAVOIR/SOURCE` pour ancre/référence observée. | Une référence calibre le jugement, elle n'établit ni droit ni efficacité. |
| `REFERENCES/ASSET` 52 | `DIRECTION/VISUAL_TARGET` pour route de production/rôle ; `SAVOIR/SOURCE` pour provenance/limite. | Un même ancien alias est **décomposé par responsabilité** ; ne pas traiter asset comme route BIB ni inférer droits acquis. |
| `REFERENCES/MEMORY` 53 | `TRACE-LOCATOR` et artefact local. | Un souvenir/artefact n'est ni source normative, ni preuve retrouvable par simple nom. |
| `REFERENCES/CORPUS` 54 | Propriétaire normatif effectivement concerné ; CHANGELOG si modification du package. | Le sujet décide de l'owner ; ne pas ouvrir CHANGELOG pour toute collection locale. |

Ces aliases ne sont pas des routes actives (46) et BIBLIOTHEQUE 774 interdit leur sélection dans un nouveau run ; leur identifiant ancien peut rester dans une **trace de compatibilité**, sans ressusciter le préfixe en route exécutable. Si la destination ou portée est ambiguë, 56 conserve `NOT-VERIFIED` ou `EXPLORATORY` jusqu'à établissement de l'owner, sans mapping arbitraire. Le transport effectif des anciens identifiants dans les guides, readers, schémas et distributions reste à vérifier dans les blocs de phase 2 correspondants.

## Passage C — simulations de lecteurs sous contrainte

| Lecteur et scénario | Décision attendue | Lecture ou transition trompeuse |
|---|---|---|
| Mainteneur, route du seed V1 dont le rendu pose désormais un problème grave | Établir le périmètre, les consumers, la migration, la preuve et l'owner ; demander au propriétaire du corpus comment inscrire sa dépréciation sans lui inventer un gain antérieur | Étiqueter rétroactivement `ADOPTED` pour obtenir la transition vers `DEPRECATED`, ou retirer sans trace (F-CHG-001). |
| Équipe produit, PILOT utilisé par deux consumers mais à retirer progressivement | Bloquer nouveaux usages dans une décision gouvernée, préparer migration/rollback et statut transitoire explicite | Le passer immédiatement à `ABANDONED` pendant que les consumers existants l'utilisent, ou le laisser `PILOT` comme s'il restait conseillé (F-CHG-001). |
| Designer, nouvelle scène utilisée trois fois dans des contextes semblables | Garder local/pilote ; réunir baseline, usages réellement contrastés, gain et contrat avant candidature `ADOPTED` | Prendre la fréquence ou une belle capture pour adoption. |
| Reviewer, package et `RUN_CARD` passent mais aucune interface n'a été observée | Conserver les PASS documentaires dans leur portée et `NOT-VERIFIED` sur l'effet réel non couvert | Transformer le résultat du validateur en preuve de qualité visuelle, d'accessibilité ou d'usage. |
| Agent, ancien `REFERENCES/ASSET` dans un run migré | Séparer rôle de l'asset chez DIRECTION et provenance/limite chez SAVOIR ; garder alias historique dans trace si besoin | Créer une nouvelle route `REFERENCES/ASSET`, ou classer l'image comme structure durable. |
| Mainteneur, correction d'une règle de jugement SAVOIR partagée | Nommer SAVOIR source propriétaire, ACTION pour preuve/impact, CHANGELOG pour décision ; BIB seulement si la structure change | Forcer BIBLIOTHEQUE/EVOLUTION pour toute route partagée (F-DIR-046). |
| Équipe de release, proposition de norme transversale issue d'un seul cas | Garder source unique, portée, compatibilité, méthode de preuve, limite, revue/retour et décision explicite du corpus | Publier en règle universelle sur la seule base de l'enthousiasme local. |
| Analyste, ancien `REFERENCES/CORPUS` contenant style et mesure | Identifier le propriétaire de chaque modification réelle, garder la pièce dans artefact/trace et réserver CHANGELOG aux règles modifiées | Migrer tout le corpus de goût en routes normatives. |

Ces cas sont des simulations textuelles, **pas** des migrations, suppressions, adoptions ou mesures exécutées. Le texte ne permet pas de déclarer une réussite opérationnelle de la baseline.

## Passage D — résistances et constat

### F-CHG-001 — le seed canonique et un PILOT avec consumers n'ont pas de chemin explicite de dépréciation

- **Statut :** provisoire, gravité significative à éprouver lors de la consolidation et des parcours de migration ; aucun incident de production attesté.
- **Fait textuel :** CHANGELOG 42 déclare canoniques les routes présentes dans le seed mais **n'attribue aucun** des quatre statuts individuels à ces routes. `ADOPTED` 38 suppose un gain accepté, alors que 21 maintient l'efficacité réelle et l'adoption `NOT-VERIFIED`. Dans le tableau 37–40, `DEPRECATED` n'est atteignable **que depuis `ADOPTED`** ; `PILOT` ne mène qu'à `ADOPTED` ou `ABANDONED`.
- **Épreuve discriminante A — seed :** une route publiée dans le catalogue initial doit cesser d'être proposée tout en restant lisible pour les consumers existants. `ADOPTED → DEPRECATED` impose d'abord un statut dont la preuve de gain n'existe pas ; aucune transition depuis « seed canonique expérimental » n'est définie. Faire comme si seed = ADOPTED masque la limite déclarée en 21 ; retirer directement contourne la transition documentée.
- **Épreuve discriminante B — pilote partagé :** une route `PILOT` a été testée et intégrée par des consumers ; un défaut découvert impose de ne plus la sélectionner, mais la migration prendra du temps. `PILOT → ABANDONED` saute l'étape de conservation pour compatibilité ; `PILOT → ADOPTED → DEPRECATED` exige d'accepter le gain d'une route à retirer. Une migration préparée hors statut est possible grâce à ACTION 383 et CHANGELOG 27, mais le cycle ne sait pas la nommer sans lecture implicite.
- **Effet possible :** statut fictif, route arrêtée sans voie de compatibilité claire, nouveaux usages maintenus pendant la migration, ou décision propriétaire retardée par l'absence d'une transition honnête. **Facteurs atténuants :** statut expérimental déclaré 4/21/62, autorité explicite de décision 27, compatibilité/retour exigés, ACTION/RUN-SYSTEM 383 et possibilité de documenter une réserve/migration sans falsifier un `ADOPTED`. Une route du seed peut être utilisée de manière contrôlée sans claim de gain.
- **Propriétaire :** CHANGELOG pour statut initial du seed, transition et décision de dépréciation ; ACTION pour cartographie des consumers/migration/rollback ; BIBLIOTHEQUE/EVOLUTION pour gain et risque de structure seulement si structure active. F-DIR-046 concerne le mauvais détour BIB sur des routes non structurelles, F-ACT-015/021 la trace machine du paquet SYSTÈME : aucun ne définit le chemin manquant dans la table CHANGELOG.
- **Test et correction candidate après phases 2–10 :** choisir une route seed sans mesure d'efficacité, une nouvelle route pilotée sans consumer et un PILOT partagé avec consumers. Faire remplir à deux lecteurs statut initial, interdiction des nouveaux usages, migration, statut final, owner et preuve sans ajout de règle implicite. Envisager un statut de bootstrap ou une transition de dépréciation depuis chaque état réellement publié/utilisé avec conditions de migration et claim borné, **sans** promettre un gain que la V1 n'a pas mesuré. Ne rien changer au texte à ce stade.

| Autre résistance | Attribution |
|---|---|
| Version publique V1.0.0 interprétée comme produit efficace validé | 4–6, 21 et 58–62 la bornent explicitement ; distinguer cohérence du package et effet des runs. F-DIR-002 sur claims d'efficacité à conserver, pas un nouveau F-CHG. |
| Route esthétique « promue » par nombre de likes ou captures | 38/42 et BIB/EVOLUTION 735–768 exigent gain et maintenance ; aucun statut automatique. |
| Fichier CHANGELOG utilisé comme source propriétaire de toutes règles | 25–27 demande une source normative unique pour chaque évolution ; DIRECTION/ACTION/SAVOIR/BIB gardent leurs objets. F-DIR-046 demeure au renvoi DIRECTION 817. |
| Succès du validateur utilisé comme preuve des obligations SYSTÈME | 25/60/62 limitent la projection ; F-ACT-015/021 à tester dans les schémas/fixtures. |
| Alias historique chargé comme nouvelle route | 46–56 et BIB 774 le refusent ; vérifier mappings dans les lecteurs/distributions plus tard. |
| Route `DEPRECATED` encore utilisée par un consumer historique | 39 permet conservation pour migration/compatibilité ; interdire seulement **la nouvelle sélection**, tracer risque et plan. |

**Un ID propre à CHANGELOG, F-CHG-001, reste provisoire.** Le reste du texte explicite son autorité et ses limites sans nécessité démontrée d'un second constat autonome. Les implications machine et la migration de copies ne sont pas conclues depuis ce seul propriétaire.

## Couverture, qualités à garder et handoff

| Passage | Profondeur | Résultat et limite |
|---|---|---|
| A — architecture | FULL | Source normative, baseline, ownership, guide/schéma dérivé, liens aux quatre propriétaires ; 1–29 |
| B — contrat | FULL | Quatre statuts, transitions, exception seed, cinq aliases et limites ; 31–63 |
| C — usage simulé | TARGETED | Huit scénarios ; ni migration réelle ni gain mesuré |
| D — résistance | TARGETED | F-CHG-001 provisoire, autres risques rattachés aux IDs existants |
| Machine | LIGHT | `read_route.py CHANGELOG` n'est pas un locator annoncé ; carte dérivée valide, contrôle des dérivés à venir |
| Externe | N/A-JUSTIFIED | Les affirmations lues décrivent la baseline fournie ; aucune validation d'une publication externe ou efficacité réelle n'est revendiquée |

**Forces à préserver :** preuve datée et bornée, séparation source normative/projection machine, décision explicite du corpus, droits des consumers lors des migrations, refus de prendre une suite verte pour gain produit, et qualification expérimentale honnête. La correction du cycle ne doit pas créer une « adoption » fictive des routes initiales.

**Les cinq sources normatives sont maintenant lues, 3 548/3 548 lignes par rapports sectionnels.** Ce chiffre décrit uniquement la couverture de ces cinq textes : phase 2 toujours en cours sur façades, cartes, schémas, fixtures, scripts, skill, release et distributions ; phases 3–14 toujours en attente. **Prochaine unité :** consolidation inter-propriétaires de ces cinq lectures avec les checkpoints DIRECTION, ACTION, SAVOIR et BIBLIOTHEQUE et F-CHG-001 ; vérifier dépendances, déduplication, ordre des artefacts dérivés à auditer, et points de désaccord sans décider de patch. Le présent rapport suffit comme checkpoint de cette source de 63 lignes ; aucun fichier de checkpoint CHANGELOG séparé n'est nécessaire pour répéter son contenu.
