# Changelog — Design Governance V1.1.1

**Version publique :** `V1.1.1`  
**Statut expérimental :** Design Governance V1.1.1 est une expérimentation maintenue.  
**Date de la version :** 2026-09-26  
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Non publié — candidate V1.2 (B05), chantiers A, B et D

- **Bilan de fabrication.** `FABRICATION` remplace `ANCHOR-BASIS` et `ANCHOR-LIMIT` dans le Creative Boot ; `CONSTRAINT` inclut la destination ; en produit réel, jamais de faux asset ; capacités absentes : plafond déclaré, rendu livré. Trace seule, schéma `RUN_CARD` inchangé.
- **Prise de brief minimale.** `DIRECTION/EXTERNAL-START` : au plus trois demandes, en un seul échange : contenu réel, marque, asset principal ou route autorisée, destination si elle est incertaine ; construire dans tous les cas.
- **Anti-slop vivant.** `MODAL` / `PARTI` remplacent `ANTI-DIRECTIONS` (projetés dans `direction.anti_direction`) ; marqueurs de vague datés dans `SAVOIR` (`[VEILLE 2026-09]`), pour nommer, jamais pour interdire.
- **Niveau senior (lot 2).** Objet de preuve codé de préférence (`DIRECTION/FIRST-OBJECT`) ; carte des moyens par couche et vague 3 datées (`SAVOIR`, `[VEILLE 2026-09]`) ; traitement des assets moyens (`SAVOIR`, section `DESIGN-ATLAS`).
- **Validateur de carte.** La liste close des conditions de façade passe de 42 à 50 conditions (LCF-43 à LCF-50) ; LCF-46 couvre aussi la vague 3.
- **Gardes de propriété (refonte, R2).** `scripts/validate_structure.py` : huit concepts d’honnêteté balisés à leur lieu propriétaire (`<!-- concept:HON-01 -->` à `HON-08`), chacun unique, non vide et dans son fichier ; `read_route.py` retire les balises à la lecture.
- **Alignements (refonte, R3).** Vocabulaire unique `MODAL` / `PARTI` (le terme « anti-direction » ne subsiste que dans l’historique ; projection inchangée `direction.anti_direction`) ; résumés de la prise de brief fidèles au canon ; renvois du boot vers les marqueurs de vague et de la route de production vers la carte des moyens (`SAVOIR/TOOLS`) ; glossaire du vocabulaire de fabrication ; QUICKSTART au vouvoiement et sans table en double. Nouvelles gardes de propriété dans `scripts/validate_structure.py`.
- **Noyau de fabrication (refonte, R4).** Les gestes de fabrication (structure, composition, moyens et vérité, boucle d’édition) sont balisés dans leurs sources et compilés dans la skill par `scripts/build_core.py` ; la vue de chargement quotidienne devient `DIRECTION/CHARGE`, seule liste de chargement (Gates A et B en `LITE` et `ITER`) ; la réponse visible passe en langage produit (`ACTION/HANDOFF`) ; la table de diagnostic et les six questions de revue passent de QUICKSTART à `DIRECTION/DOUBLE-LOOP`, la variation « un axe à la fois » d’ORCHESTRATION_MAP à `SAVOIR/CRAFT/CFT-02`.
- **Trace et checkpoint (refonte, R5b-1).** Trace légère par défaut, complète si le run est persistant, partagé, audité ou si une acceptation est demandée (`ACTION/HANDOFF`) ; Gate B, `RUN_CARD` et paquet de clôture chargés en trace complète ; la première proposition vaut checkpoint, sauf action irréversible ou coûteuse ; destination réelle sans contenu : exemple marqué plutôt qu’emplacements vides ; test de trame dans les signaux de convergence. Schéma `RUN_CARD` inchangé.
- **ACTION restructurée (refonte, R5b-2).** Gate A par profil de surface (contrôles d’office et selon le contenu) ; Gate C relie chaque critère à son geste de correction dans le noyau et sert, en trace légère, de contrôle de craft sans verdict ; une seule description de la boucle (`DIRECTION/DOUBLE-LOOP`) ; promesse du validateur tenue en un seul lieu (`ACTION/RUN_CARD`). Schéma `RUN_CARD` inchangé.
- **DIRECTION restructurée (refonte, R5a).** Rôle, posture et récapitulatif de protection en tête ; rôle défini une seule fois ; entrée unique (classer : `START`, charger : `CHARGE`, fabriquer : le noyau) ; doublons de lecture et de passage retirés ; phrase hors contexte du bloc de prise de brief corrigée. Aucun locator renommé.
- **Convergence typographique (refonte, R8a).** La question de convergence du noyau porte sur la palette et sur la police de titre (comparer au moins deux voix typographiques sur le vrai titre) ; la veille note un signal à confirmer (grotesque large sur blanc neutre, P1).
- **SAVOIR alignée (refonte, R5c, hors ancre).** Un seul modèle de niveaux (`Correction`, `Précision`, `Intention`) ; la triade visée / observée / prouvée devient « trois moments de la qualité » ; boucle et one-shot renvoient à leur lieu propriétaire.
- **BIBLIOTHEQUE alignée (refonte, R5d).** Boucle structurelle et one-shot renvoient à leur lieu propriétaire en gardant leurs critères de structure ; les tests perceptifs de `BIBLIOTHEQUE/GATE` sont appelés depuis Gate C.
- **Façades (refonte, R6a).** README : la boucle renvoie à `DIRECTION/DOUBLE-LOOP` ; glossaire : trace légère, trace complète, première proposition, trame modale, profil de surface.
- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence donne V1.1.1 ≈ sans système sur la qualité perçue ; l’effet de ces chantiers reste à éprouver (G4).

## V1.1.1 — Retour d’audit : alignements de textes et de façades

Aucun changement de schéma, d’invariant machine ni de fixture. Les cartes valides en V1.1.0 le restent.

- **Conséquence décisionnelle.** La table `RUN_CARD`, le glossaire, la réponse visible et les paquets de clôture renvoient à la triade d’`ACTION/STATUS` : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée.
- **B1b.** La portée écrite rejoint celle du validateur : toute surface `DIRECTION` qui accepte avec V en `PASS` ou `PASS-WITH-RESERVATION`.
- **Sorties par mode.** Les blocs `RUN-*` renvoient au paquet de leur mode dans `ACTION/CLOSE-PACKAGE`, qui reprend leurs éléments propres.
- **Façades.** Creative Boot sans nombre fixe d’anti-directions ni de tension ; chargement de Gate B en `LITE` et `ITER` ; projection machine conforme au schéma (valeurs d’axes, cinq champs de `profile_decision`) ; colonne « Retour si… » dans le §6 du QUICKSTART ; légende des tags ; exemple `CLOSED` du glossaire aligné sur la protection critique ; exemples de la skill renvoyant à la sérialisation.
- **Textes normatifs.** Table de correspondance `VISUAL_TARGET` limitée aux champs de sa table ; droits inconnus (`ACCEPTED` interdit, réserve possible, diffusion après clearance, contrôle machine en `DIRECTION` seulement) ; `null` réservé aux champs qui l’admettent ; une seule liste pour les ressources techniques (`ACTION/POLICIES`).
- **Validateur de carte.** La liste close des conditions de façade passe de 21 à 42 conditions.
- **Erratum V1.1.0.** La phrase « façades alignées sur leurs propriétaires » est bornée à ce que la liste close contrôle.

**L’efficacité sur des runs réels reste `NOT-VERIFIED`.**

## V1.1.0 — Corrections de contrat, de lecture et d’outillage

- **Autorité du schéma et oracles de test.** Les validateurs `RUN_CARD` et contrats refusent un schéma absent, vide, incomplet ou hors sous-ensemble, et vérifient qu’un témoin invalide est rejeté. Chaque fixture déclare son motif attendu ; chaque invariant a son cas unitaire à faute unique.
- **Contrat `RUN_CARD` migré.** Protection critique à résultat, exception `FAIL-ASSUMED` structurée, axes V/U/A/T, réserves complètes, capacité et version de la preuve, droits, paquet SYSTÈME, B1b, ancres typées, conséquence décisionnelle (`CHANGED`, `CONFIRMED`, `ABANDONED`, `N/A-JUSTIFIED`, `NOT-OBSERVED`), temps du verdict et reclassement. Profil strict : mêmes exigences par mode, locators locaux résolus depuis le dossier de la carte.
- **Contrats de production.** Objets facultatifs, scopes attendu et observé séparés, jetons canoniques, couverture risque → contrôle, sources qualifiées, plan de preuve structuré ; CLI ouverte aux fichiers externes avec `--type`.
- **Lecture et routes.** Le lecteur résout par table, préfixe et sous-locator (dont `DIRECTION/START/TREE`), refuse l’ambiguïté et ignore les titres des blocs de code. Le validateur de carte contrôle la couverture de tout locator cité et 21 conditions de façade.
- **Sources normatives.** Statut `SEED` du cycle de vie ; deux sorties canoniques (réponse visible et handoff) ; table de correspondance `RUN_CARD` par phase ; promesse du validateur (ce qu’il atteste, ce qu’il n’atteste pas) ; triade de conséquence décisionnelle ; cible visuelle en une seule table ; contrat du premier objet relié à `SAVOIR/CRAFT/CFT-00` ; marquage `TRUTH` à deux axes ; regard externe qualifié ; palette sans répartition imposée ; contrat de composant partagé unique dans `BIBLIOTHEQUE/COMPONENTS`.
- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill corrigés sur les écarts relevés ; la cohérence opposable se limite à la liste close des conditions de façade (`validate_reading_map.py`) : une divergence hors de cette liste n’est pas détectée. Efficacité déclarée `NOT-VERIFIED` partout.
- **Outils et build.** Archives créées dans le répertoire de travail puis publiées, membres contrôlés contre le manifeste, promotion transactionnelle, liens symboliques refusés, exclusions limitées à la racine ; manifeste sans doublon et version unique ; lectures non UTF-8, clés JSON répétées et types illégaux refusés proprement ; `validate_all.py` lançable depuis n’importe quel dossier ; chemins propres à l’export Local ; actions du workflow épinglées par SHA complet (runtime node24).

**Compatibilité.** Une `RUN_CARD` produite avec V1.0.0 peut devoir être complétée pour satisfaire les invariants migrés ; les exemples et fixtures du package le sont. **L’efficacité sur des runs réels reste `NOT-VERIFIED`.**

## V1.0.0 — Baseline expérimentale

**Date de publication :** 2026-09-19

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
| `SEED` | Route du seed V1, canonique par construction, sans gain mesuré. | `ADOPTED` (contrat de gain réel satisfait, `BIBLIOTHEQUE/EVOLUTION`) ou `DEPRECATED`. |
| `PILOT` | Route locale ou candidate testée dans un périmètre déclaré. | `ADOPTED` ou `ABANDONED` ; `DEPRECATED` lorsque la route a des consumers. |
| `ADOPTED` | Route canonique dont le contrat, la maintenance et le gain sont acceptés. | `DEPRECATED`. |
| `DEPRECATED` | Route conservée pour migration ou compatibilité ; elle ne doit pas être choisie dans un nouveau run. Aucun nouvel usage ; migration par `ACTION/RUN-SYSTEM` (paquet SYSTÈME). | `ABANDONED` après migration. |
| `ABANDONED` | Route qui n’est plus maintenue ni proposée. | Aucune transition silencieuse. |

Les routes présentes dans le seed de la V1 ont le statut `SEED` : canoniques, sans gain mesuré. `ADOPTED` exige le contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`). Une route peut être dépréciée depuis tout état publié ou utilisé (`SEED`, `PILOT` avec consumers, `ADOPTED`) ; une dépréciation interdit les nouveaux usages, exige une migration et ne revendique aucun gain. Toute nouvelle route ou promotion doit indiquer son problème, sa décision, son owner, son contrat, sa preuve, sa limite, sa compatibilité et sa prochaine revue.

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

