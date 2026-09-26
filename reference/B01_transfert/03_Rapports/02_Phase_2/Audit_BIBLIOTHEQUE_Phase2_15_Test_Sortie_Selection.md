# DG-AUDIT-001 — Phase 2 — BIBLIOTHEQUE, bloc 15 : test de sortie

## Cadre, précédent et baseline

- **Source propriétaire :** `audit_work/package/V1/official/BIBLIOTHEQUE.md`, lignes **776–791** ; titre 776, neuf questions 778–788, issues et frontière de clôture 790, fin du fichier 791.
- **Méthode :** protocole externe v2.0 §12 : passages A–D. Rapport EVOLUTION bloc 14, plan et cinq constats F-BIB-001 à 005 relus ; EVOLUTION réserve la promotion réelle à des usages contrastés, un gain situé et une décision CHANGELOG, sans statut de livraison concurrent. Interface principale : ACTION/CLOSE-EXIT-CHECK 915–930 ; également BIBLIOTHEQUE/READ 22–39, SELECT 161–205, CONTRACTS 256–284, OBJECT 501–538, MICRO 542–560 et GATE 697–729.
- **Baseline B01 contrôlée, inchangée :** compilé SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; BIBLIOTHEQUE `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684`.
- **Accès :** la sous-section s'intitule « Test de sortie BIBLIOTHEQUE », sans locator canonique `BIBLIOTHEQUE/TEST-EXIT`. L'essai de ce nom inventé échoue donc à juste titre : **ne pas** le compter comme nouvelle occurrence de F-DIR-028/F-ACT-001. `validate_reading_map.py` passe. La source propriétaire a été lue directement.
- **Nature :** lecture normative et cas simulés ; pas de test de produit réel, de vérification d'accessibilité exécutée, de preuve d'efficacité, ni de patch du système.

## Passage A — place et séparation des deux sorties

Le test porte sur la **sélection structurelle** de BIBLIOTHEQUE : utilité de chaque route, qualité de sa responsabilité, relation à un objet, type et limite de preuve, recomposition si le mobile est activé, cohérence d'assemblage, statut d'identifiant, persistance et bon niveau structurel. ACTION/CLOSE-EXIT-CHECK est **l'unique test canonique de sortie du run**, avec mode, artefact, preuve obtenue, portée, V/U/A/T, verdict, réserves, conséquence de décision et qualité du rendu (ACTION 915–930). La phrase finale BIB 790 interdit explicitement de substituer l'un à l'autre.

Les deux listes ont des objets différents : réussir les neuf questions de BIB ne suffit pas à livrer ; échouer une sélection structurelle applicable est un élément à transférer au contrôle/issue ACTION approprié. L'absence de route nouvelle peut être un choix valide (BIB 27, SELECT 163, 193–194) et ne supprime aucun contrôle ACTION déclenché par un autre risque. Le tableau d'assemblage COMPAT et le contrôle structurel GATE ne créent pas davantage une sortie concurrente.

## Passage B — contrat des neuf questions

| Question et ligne | Lecture opératoire et propriétaire de la preuve | Risque de glissement |
|---|---|---|
| 1 — décision réelle, 780 | Pour chaque route effectivement sélectionnée, nommer la décision d'espace, lecture, comportement ou preuve qui change, même si une relation existante est conservée par héritage ; SELECT 163–167, 199. | Une route ajoutée pour son nom ou son esthétique devient implicitement utile ; une non-sélection est qualifiée d'échec. |
| 2 — responsabilité et contre-indication, 781 | Décrire quand la route sert et quand elle nuit ; contrat initial local réduit, et complet si durable (258, 264–266). | Une contre-indication copiée sans lien au run donne une fausse robustesse. |
| 3 — objet/MICRO, 782 | Quand un objet ou une MICRO porte la décision, vérifier promesse, état et action **applicables** et crédibles dans le médium ; DIRECTION/START classe une MICRO critique et ACTION juge tâche/permissions. L'objet de preuve n'exige pas toujours de sélectionner un identifiant `OBJECT/*`. | Déduire une action interactive d'un support sans interaction, forcer un objet spécialisé sur une correction de GRID ou déclarer la tâche accomplie depuis une capture. Tester en phases 8/9 la clarté de cette activation ; pas d'ID autonome aujourd'hui. |
| 4 — type, scope et limite, 783 | `PERCEPTUAL`/`EXPERT`/`TECHNICAL`/`USER/TASK` disent **ce qui peut être établi** ; ACTION rattache méthode, artefact/version, observation et limites. | Nommer `USER/TASK` comme type sans personne, tâche ou résultat réellement observés ; `PASS` hors scope. |
| 5 — mobile, 784 | Recomposer priorité, voisinage, action, état, contenu et performance **lorsque le risque le requiert** ; faire correspondre au médium et au scope réels. | Forcer un dossier mobile sur print ou borne ; éluder le mobile web réellement livré. Cette phrase atténue mais ne réécrit pas F-BIB-003 (GRID 402–411). |
| 6 — combinaison, 785 | Vérifier JTBD, preuve attendue, risque et condition de sortie pour les routes effectivement assemblées ; COMPAT 663/674 n'en donne que des hypothèses. | Prendre une ligne favorable du tableau pour preuve d'efficacité, ou la sélection zéro pour un assemblage obligatoire. |
| 7 — identifiant, 786 | Employer un nom existant ou déclarer explicitement la forme locale ; `PILOT` est un statut gouverné pour route candidate **déjà testée dans un périmètre déclaré** selon CHANGELOG 37. | Marquer fictivement `PILOT` une proposition non testée pour satisfaire la case ; la ligne 786 ne change pas la définition de CHANGELOG. |
| 8 — trace, 787 | Conserver la sélection et sa justification dans `RUN_CARD` **ou** trace canonique retrouvable par `trace_locator` ; le paquet de preuve est une pièce jointe, pas le seul registre. | Une trace externe vide ou une liste de routes dans `sources` prise pour décision/preuve ; vérifier F-ACT-002/021 sur le transport. |
| 9 — bon niveau, 788 | Garder distincts SUPPORT, GRID, SCENE, OBJECT, MICRO, MODIFIER et LAYER ; la chaîne de READ 72–78 est une carte de responsabilités et non un ordre ou quota. | Promouvoir une variante locale, un style ou un asset en route structurelle ; confondre objet local et scène entière. |

La ligne 790 rattache l'inconnu à `NOT-VERIFIED`, le contrôle à reprendre à `RETURN`, et une exploration à l'issue ACTION adéquate, par exemple `EXPLORATORY` ou `RETURNED`. Ce n'est pas la permission de faire `NOT-VERIFIED` pour une route nécessaire mais non exécutée puis d'annoncer `ACCEPTED`. La non-applicabilité réelle reste `N/A-JUSTIFIED` selon CONTRACTS 282 et ACTION 202/653, avec justification du médium/scope, même si la dernière phrase BIB ne répète pas ce libellé ; une information **applicable mais manquante** demeure non vérifiée. L'homonyme `RETURN` ne fusionne pas statut de contrôle, issue et verdict global.

ACTION/CLOSE-EXIT-CHECK 919–928 demande dix vérifications qui **ne sont pas couvertes** par BIB seule : mode protecteur, artefact et décision, preuve réellement obtenue, axes V/U/A/T, owner/verdict, réserves, décision après procédure, résolution du premier rendu et effet concret de la dernière modification. En retour, BIB vérifie spécifiquement le bon niveau des identifiants et le statut local/canonique. Une chaîne complète de routes ou une grille conforme ne démontre ni tâche, ni accessibilité, ni performance ; BIB 790 et ACTION 930 le répètent.

## Passage C — lecteurs et décisions simulées

| Contexte | Résultat souhaité de la lecture | Faux raccourci |
|---|---|---|
| Designer, nouvelle scène éditoriale avec objet de preuve local | Déclarer décision, contre-indication, lien au produit, preuve perceptuelle et limite, puis observation ACTION | Remplir neuf « oui » parce que scène + objet sont nommés. |
| Intégrateur, correction d'axe GRID dans une borne fixe sans geste interactif | Vérifier priorité et contenu de la grille, médium et preuve réelle ; justifier ce qui ne s'applique pas à l'interaction/mobile | Inventer un CTA, un `OBJECT/*` et sept champs mobiles pour valider Q3/Q5. |
| Agent, aucune route sélectionnée pour microcopie LITE | Tracer l'héritage/non-sélection et contrôler les risques du texte via ACTION ; pas de sélection forcée | Mettre `N/A-JUSTIFIED` sur le run entier parce que BIB est hors scope. |
| Reviewer, scène mobile avec erreur et données sensibles | Vérifier Q3–Q5 dans états et viewport réels, ACTION pour permissions/récupération et statut de preuve | Conclure depuis une capture desktop nominale et un type `TECHNICAL` annoncé. |
| Mainteneur, nom `SCENE/CLIENT_JULY` introuvable | Marquer la forme locale et sa responsabilité, ou la remplacer par route canonique appropriée ; promouvoir seulement selon EVOLUTION/CHANGELOG | Appeler une simple maquette `PILOT` pré-observation ou publier un alias nouveau. |
| Système automatique, toutes les routes dans `sources`, `trace_locator` sans contenu vérifiable | Exiger trace canonique de justification, provenance et preuve selon ACTION ; garder limite inspectable | Déduire un PASS de Q8 et livrer parce que la liste des identifiants est syntaxiquement valide. |
| Équipe produit, tableau COMPAT cochant les conditions de combinaison | Déclarer JTBD, preuve, risque et sortie ; observer la tâche réelle si un gain d'usage est revendiqué | Croire la combinaison « prouvée » parce qu'elle figure au catalogue. |
| Directeur de produit, route partagée `ADOPTED`, écran local qui échoue au clavier | Conserver séparément statut du catalogue et retour du run ; traiter l'échec d'accessibilité dans ACTION | Transformer `ADOPTED` en verdict d'écran ou en passe-droit. |

Ces huit cas n'ont pas été exécutés sur une interface. Ils éprouvent la logique de lecture ; leur impact réel et la compréhension de lecteurs indépendants restent à vérifier.

## Passage D — résistances et constats préexistants

| Épreuve | Traitement |
|---|---|
| Q3 paraît universelle pour un delta GRID ou un médium non interactif | SELECT 163/193–197 autorise le niveau minimal, ACTION 653 la non-applicabilité réelle ; la règle est lisible sans imposer une route OBJECT/MICRO. Conserver une **réserve de lecture** et la tester sur print/borne/web dans les phases 8/9 ; elle pourrait devenir un constat si des lecteurs indépendants appliquent Q3 comme obligation inconditionnelle. |
| Q5 réserve le mobile au risque activé mais le contrat GRID l'énumère plus largement | Rattacher à F-BIB-003 ; la dernière question ne gomme pas la formulation locale de GRID. |
| Q7 autorise « local ou PILOT » sans détailler l'essai préalable | CHANGELOG 37 définit le test en scope ; le cas d'un `PILOT` purement déclaratif est déjà documenté dans READ/CONTRACTS, à rééprouver sans nouveau constat. |
| Q8 est satisfait par la présence d'un `trace_locator` sans paquet lisible | ACTION garde preuve, provenance et verdict ; F-ACT-002/015/021 et F-DIR-006 portent déjà sur les interfaces de trace et de projection. |
| Q9 conduit à appliquer un contrat de composant partagé sans anatomie ni baseline de rendu | F-BIB-004 reste ouvert : classer `LAYER/PRIMITIVES` correctement ne fournit pas le contrat annoncé. |
| Nom de route `TEST-EXIT` inventé et refusé par CLI | Aucun locator canonique de ce nom n'existe ; ne pas imputer au défaut d'indexation des titres réellement nommés F-DIR-028/F-ACT-001. |
| `N/A-JUSTIFIED` utilisé pour une comparaison B1b d'autre décision | F-BIB-001 garde l'identité de la décision et le déclencheur à vérifier ; sortie 790 ne crée pas d'exception. |
| Tests de non-généricité de GATE réutilisés comme verdict de clôture | F-BIB-005 et F-SAV-006 restent distincts ; Q1/Q6 et ACTION 927 jugent le rendu situé, sans refonte imposée par un seul masquage. |

**Aucun nouvel ID F-BIB.** Cette section rappelle la frontière canonique et comporte des conditions suffisantes pour lire les cas non applicables avec ACTION. La possible lecture excessive de Q3 est enregistrée pour un test discriminant, sans annoncer une défaillance observée ou clore ce risque par simple interprétation favorable. Aucun des cinq constats existants ne devient résolu par la dernière page.

## Couverture et suite

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Sortie locale 776–791 confrontée à ACTION 915–930 et aux sélections 161–205 |
| B — contrat | FULL | Neuf questions 780–788, trois voies d'issue 790, N/A si vraiment hors scope, pas de verdict autonome |
| C — usage | TARGETED | Huit simulations, dont zéro route, print/borne et route partagée |
| D — résistance | TARGETED | Q3 et Q7 à éprouver, cinq F-BIB préservés, autres occurrences dédupliquées |
| Machine | LIGHT | Lecture source directe ; échec d'un locator non canonique sans constat ; carte dérivée validée |
| Externe | N/A-JUSTIFIED | Aucun fait externe neuf requis pour cette articulation textuelle |

**BIBLIOTHEQUE 1–791 est maintenant entièrement parcouru en quinze rapports sectionnels.** Produire le checkpoint de propriétaire : confirmer l'union des plages sans règle oubliée, IDs F-BIB-001 à 005, forces à préserver, risques et interfaces, baseline, réserve Q3 et prochaine cible `CHANGELOG.md` 1–63. La phase 2 du système reste ouverte ; aucun patch ni verdict global à cette étape.
