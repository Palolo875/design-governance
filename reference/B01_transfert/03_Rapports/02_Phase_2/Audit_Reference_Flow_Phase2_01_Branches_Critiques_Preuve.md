# DG-AUDIT-001 — Phase 2 — `references/flow.md` : branche critique et preuve absente

**Date :** 24 septembre 2026. **Baseline :** B01. **Profondeur :** TARGETED sur la vue de flux, lecture complète A–D **1–23/23**. Source exacte : `skills/design-governance-practice/references/flow.md`, SHA-256 `4202c8e270384ca976a70dafe2a734e11b8c2a8d75d8d6e5772387a4ee5577ee`. Système compilé B01 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole v2.0 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, skill parente `2d2734eb13527563698542303682d204a3174b987adbb9ac02d795cf31687853`, tous revérifiés. Rapport précédent `Audit_Skill_Pratique_Phase2_01_Activation_Routes_Sortie_Exports.md` relu ; F-SK-001/002 restent ouverts. Aucun changement de source normative ni de baseline.

## Passage A — architecture visible, 1–23

| Lignes | Contenu | Fonction du bloc |
|---|---|---|
| 1–4 | Titre et réserve « vue de lecture », aucune route créée. | Statut dérivé, concordant avec la skill 41/145. |
| 5–16 | Diagramme Mermaid : `A → B → C → D → E → F → G`, avec trois arcs conditionnels `A → H` (risque critique), `F → I` (preuve absente), `E → C` (défaut créatif). | Vue principale et trois embranchements. Après extraction de ses arcs, **G, H et I** n'ont aucun arc sortant dans le diagramme. |
| 18–20 | Équivalent en prose, coordination créative et gouvernance ; `DIRECTION/START` avant action, profondeur conditionnée au gain décisionnel. | Ne crée ni mode supplémentaire ni protocole propriétaire. |
| 22–23 | Renvoi à `ORCHESTRATION_MAP.md` lorsque plusieurs capacités se combinent. | Nom sans lien Markdown ni chemin racine ; le fichier existe dans les deux exports sous des racines différentes. |

## Passage B — contrat sémantique et contrôles d'interface

**Démarrage et risque critique.** `DIRECTION/START` 119–140 classe selon l'objet direct de la décision, puis applique une *protection de niveau* : un risque critique touchant action, état, sémantique, donnée, récupération ou preuve entraîne une reclassification vers le mode qui protège ce risque, sauf démonstration d'un delta vraiment local sans effet. La référence, en 13, représente cette protection par `A → H` mais ne rattache `H` ni à la nouvelle route, ni à l'action, ni à un retour au chemin principal. La prose en 18–20 explique l'intention générale mais ne décrit pas cette sortie particulière.

**Preuve absente.** `ACTION.md` 284–299 borne les claims par les capacités réelles et oriente une preuve obligatoire manquante vers `NOT-VERIFIED` sur l'axe concerné, puis une issue ou un verdict approprié selon scope et risque ; `ACTION/CLOSE-EXIT-CHECK` 915–930 maintient owner, prochaine action, limite et réserve éventuelle. La référence 14 représente `F → I[NOT-VERIFIED]` sans transition dessinée de `I` vers décision, owner, prochaine preuve ou clôture. Le texte 18 mentionne « décider et fermer avec ses limites », mais ne précise pas le traitement de cette branche. Cette lacune de dessin n'invalide pas les règles propriétaires, qui gardent priorité.

**Boucle créative et one-shot.** `E → C` rend visible le retour après un défaut créatif ; `DIRECTION/DOUBLE-LOOP` 484 et `ACTION/PIPELINE-DIRECTION` 447–453 placent une correction substantielle après observation lorsque nécessaire. `ACTION` autorise aussi la clôture après premier rendu observé si qualité et risques sont couverts, sans correction artificielle. Le diagramme traverse `F[Vérifier et corriger]` avant `G` même dans ce cas : une lecture littérale pourrait imposer une correction superflue, mais le verbe « corriger ce qui est observable » en 18 et la skill 139 en limitent l'effet. Il s'agit d'une **occurrence de F-DIR-009 sur l'itération artificielle**, pas d'un nouvel ID propre à ce fichier.

**Renvoi et transport.** Dans une copie temporaire de B01, `build_distributions.sh` retourne **0** ; `flow.md` a les mêmes octets dans GitHub et Local. `ORCHESTRATION_MAP.md` existe sous `V1/official/` dans GitHub et `official/` dans Local, et se déclare dérivée en 1–11. Le renvoi non cliquable de la ligne 22 reste à lire selon la racine de l'export : **occurrence de F-SK-002**, aucune disparition du fichier démontrée. Cette référence n'énonce aucun minimum de handoff susceptible de résoudre F-SK-001 ; conserver ce constat pour la skill et les références suivantes.

## Passage C — lecteurs et cas simulés

| Cas | Suivre le diagramme seul | Confronter au propriétaire |
|---|---|---|
| Delta présenté comme `LITE`, mais modifiant consentement ou récupération | `A → H` aboutit visuellement à « Protection de niveau » sans arc de reprise. | `DIRECTION/START` reclassifie selon risque et objet direct ; puis route ACTION pertinente et preuve. |
| Run dont le runtime ou la capture requise manque | `F → I` aboutit à `NOT-VERIFIED`, sans suite dessinée. | `ACTION` garde limite, owner, prochaine preuve et issue selon risque ; ne conclut pas `PASS` par défaut. |
| Première scène satisfaisante dès l'observation initiale | `E → F → G` se lit avec « corriger » en F. | `ACTION/PIPELINE-DIRECTION` autorise le one-shot sans correction inutile si qualité et protection tiennent. |
| Agent cherchant à renforcer la direction | La ligne 22 renvoie à la carte officielle sans chemin explicite. | Ouvre `ORCHESTRATION_MAP.md` dans le bon export, puis confronte au propriétaire ; le fichier est présent des deux côtés. |

Ces quatre cas sont **simulés** ; aucun parcours utilisateur, rendu produit, décision réelle ou échec de machine n'est inféré.

## Passage D — résistance et constat provisoire

### F-FLOW-001 — branches de protection et d'incertitude sans sortie figurée

**Preuve :** `flow.md` 13–15 ; extraction des six arcs principaux et des trois arcs conditionnels : les nœuds terminaux sont `G` (clôture voulue), **`H` et `I` (branches latérales)**. **Risque de lecture :** un utilisateur de la vue seule peut traiter « risque critique » comme simple arrêt sans reclassification et `NOT-VERIFIED` comme état final sans owner ni prochaine preuve. **Atténuations :** titre 3 « vue de lecture », texte 18/20, priorité des propriétaires rappelée dans la skill 12, règles complètes de `DIRECTION/START` et `ACTION`. **Portée observée :** défaut topologique documentaire, aucun comportement fautif constaté sur un run. **Owner provisoire :** référence `flow.md` ; décision et gravité en phases 10–11. **Épreuve ultérieure :** faire parcourir les deux cas ci-dessus avec vue seule puis avec propriétaire ; comparer mode, owner, action/issue et preuve explicitement choisis. Si correction décidée, vérifier qu'elle conserve la lisibilité courte et ne crée ni nouvelle route ni verdict.

**Non-fusions :** F-FLOW-001 concerne la reprise des **branches critiques et preuve absente** ; F-DIR-009 concerne une correction/itération artificielle ; F-SK-001 la portée du handoff ; F-SK-002 le chemin des exports. Aucun ID ajouté pour ces occurrences ou pour le renvoi de la ligne 22.

**Registre :** **151 fiches provisoires avant ; 152 après F-FLOW-001**. La phase 2 se poursuit sans verdict global ni patch. **Prochaine unité :** `skills/design-governance-practice/references/canonical_minimum.md` **1–25/25**, avec ses définitions, la branche « sources indisponibles », `ACTION` et `DIRECTION` ; ensuite `examples.md` et `machine_projection.md`, release notes, README racine, mémoire de migration et distributions.
