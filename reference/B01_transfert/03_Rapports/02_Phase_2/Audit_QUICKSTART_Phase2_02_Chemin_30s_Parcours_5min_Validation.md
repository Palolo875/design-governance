# DG-AUDIT-001 — Phase 2 — QUICKSTART, bloc 2

## Périmètre, précédent et intégrité

- Cible exacte : `audit_work/package/V1/official/QUICKSTART.md`, **lignes 61–125** ; la section 4 commence à 126.
- Reprise : plan maître, rapport `Audit_QUICKSTART_Phase2_01_Entree_90s_Activation_Constitution.md` (1–60) et checkpoint transversal des cinq propriétaires. Une erreur de chemin dans la commande reproductible du rapport précédent a été corrigée avant la présente sortie ; ses conclusions et ses IDs restent inchangés.
- Protocole externe DG-AUDIT-001 v2.0 §12 relu ; passages A architecture, B contrat, C lecteurs simulés, D résistance. Les cinq propriétaires normatifs ont été comparés par obligation, sans prendre cette façade pour une nouvelle autorité.
- Baseline B01 recontrôlée : compilation SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, QUICKSTART `c3334f12447c6dab8ac8794f5817ae52788ff06d8eff0e8d7e2d92fe7319bcde`. DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG concordent également avec les hashes B01 du checkpoint transversal.
- Interfaces exactes relues : DIRECTION/START 119–159, sortie immédiate 217–241, DOUBLE-LOOP 482–504, absolu 4 605–618 ; ACTION/HANDOFF 23–35, PRECONDITION 190–218, RUN-LITE/ITER/STANDARD/DIRECTION 339–377, RUN_CARD 252–278, frontière de validation 319–329, CLOSE-EXIT-CHECK 915–930 ; BIBLIOTHEQUE/SELECT 161–199. Le début du bloc suivant 126–157 a seulement servi à identifier les nuances de mode que la suite apportera ; il demeure à auditer.

Diagnostic sectionnel provisoire, sans modification du corpus ni verdict d'efficacité réelle.

## Passage A — architecture visible

| Plage | Fonction | Lien avec le bloc 1 et le propriétaire |
|---|---|---|
| 61–72 | Cinq questions décision, risque, preuve, capacité, owner. | Renforce les questions 17–25 ; le mode reste à classer par DIRECTION/START. |
| 73–81 | Nouvelle ligne `ID — MODE — DECISION — RISK — NEXT-PROOF — STATE`, puis intention, temporalité de décision et limite de capacité. | Elle n'a pas les mêmes champs que la ligne 13–15 (`OWNER` y figure), ni le minimum de DIRECTION 237 ou la sortie ACTION/HANDOFF. |
| 83–95 | Parcours commun et deux boucles de création/amélioration. | Résume DIRECTION/DOUBLE-LOOP, mais son application à tous les modes doit rester proportionnée. |
| 96–107 | Choix après observation : corriger, rouvrir, reclassifier, obtenir la preuve ou décider. | La ligne 105 permet explicitement d'arrêter le polish si la décision est établie ; 107 pose la modification « normalement » lorsque la décision l'exige. |
| 109–124 | Lecteur de route et validation stricte d'une carte concrète. | Deux commandes nomment des locators disponibles ; le script strict contrôle certains placeholders et références locales, sans juger le monde réel. |

La section 2 est un raccourci de lancement ; la section 3 associe des boucles et des moyens techniques à la suite du run. Leur étiquette temporelle « 30 secondes » ou « cinq minutes » oriente la lecture, sans créer de quota normatif d'exécution ou de preuve. La ligne de run n'est ni la carte persistante complète ni la clôture.

## Passage B — contrat sémantique

**Classification et trace.** `MODE` dans la ligne 76 doit avoir été classé par START, même si les cinq questions précédentes n'énoncent pas l'arbre. Le nouveau `STATE` est un registre ACTION, non un verdict. La ligne 71 demande l'owner mais la ligne 76 ne le transporte pas ; inversement, la ligne 13–15 transporte l'owner sans ID ni état. DIRECTION 221/237 contient encore d'autres versions ; ACTION/HANDOFF 27–33 exige en sortie méthode, preuve, limite et conséquence décisionnelle. La liste courte 76 peut être une mémoire de lancement si son identifiant mène aux champs omis, pas une preuve que le run est déjà clos. **F-DIR-010**, **F-DIR-008** et, pour le passage vers la projection, **F-ACT-002** couvrent le défaut de fragmentation déjà relevé.

**Avant/après.** La ligne 79 distingue correctement `DECISION-INTENT` au départ de `DECISION-CHANGE` après observation, y compris une décision confirmée. ACTION 206–218 et DIRECTION 225–233 le confirment. Si aucune décision applicable n'a effectivement changé ou été confirmée, le traitement `N/A-JUSTIFIED` exige une raison ; une conséquence attendue mais non observée ne devient pas un changement. Le texte 79 ne remplace pas ACTION/HANDOFF ni les statuts de preuve. Une proposition hypothétique lorsque le package ou la source est indisponible est correctement séparée d'un run V1 conforme en 81.

**Création, structure et proportion.** La ligne 87 (« classer → diriger → construire… ») et la boucle 1 en 93 (« choisir une structure », « premier objet complet ») sont présentées comme parcours minimal général, alors que START 133–142, ACTION/RUN-LITE 339–347 et BIBLIOTHEQUE/SELECT 163/191–194 permettent un delta LITE ou ITER sans nouvelle décision de direction ni sélection structurelle. La lecture charitable de « diriger » est orienter la décision et « choisir une structure » peut être conserver l'existant ; cette interprétation n'est pas explicitée dans les deux phrases. La future section 4 et la table de chargement 146–156 donnent des conditions utiles, mais un lecteur qui s'arrête à la promesse « cinq minutes » peut engager des routes de création inutiles. **F-QS-001** enregistre cette ambiguïté propre à la façade comme observation à éprouver ; elle est distincte de F-DIR-041, qui pré-classe une *nouvelle structure* en STANDARD avant START, et de F-ACT-001, qui traite surtout de minima manquants selon le mode.

**Boucle, correction et one-shot.** La table 98–105 autorise une décision établie sans nouveau polish et sépare le manque de preuve d'un défaut de rendu. DIRECTION 500–502 permet de s'arrêter après la première observation si la qualité visée est atteinte, les risques applicables couverts et qu'aucune amélioration utile ne promet de gain. La ligne 94 décrit néanmoins la sortie de la deuxième boucle par « correction visible » et 107 dit qu'elle « doit normalement conduire » à une modification réelle : c'est juste lorsque l'observation diagnostique un défaut qui requiert cette correction, mais pourrait faire forcer une modification au one-shot déjà suffisant. La ligne 105 est ici la protection explicite ; il faut garder **F-DIR-009** (Boot exige une modification) et **F-ACT-025** (champ de prochaine action de polish) distincts de cette occurrence de la façade. Une rationale seule ne corrige aucun défaut d'artefact (107), conformément à DIRECTION 484/504.

**Preuve et machine.** Lignes 118–124 : un validateur strict vérifie un fichier JSON contre le contrat, refuse certaines chaînes exactes de démonstration, exige `artifact.locator` et `trace_locator` et teste l'existence d'un chemin d'artefact local reconnaissable. Il ne visite pas les tickets distants, n'exécute pas l'usage, n'atteste pas l'observation, ne vérifie pas toute chaîne générique imaginable. La propre phrase 124 borne correctement la prétention. L'écart de `trace_locator` selon mode normal ou strict relève déjà de **F-ACT-020** ; la frontière carte valide / résultat produit relève de **F-ACT-008/018**. Cette lecture ne fait aucune démonstration d'un faux PASS produit sur la base de la seule validation.

## Passage C — scénarios de lecteur et essais ciblés

| Scénario | Suite correcte par sources propriétaires | Point où la façade peut être lue trop vite |
|---|---|---|
| Correctif local de wrapping sans responsabilité critique changée | START classe LITE ou petit ITER ; conserver la structure, modifier le delta, observer la preuve touchée ; owner, scope et sortie retrouvables. | Une lecture littérale de 87/93 déclenche une nouvelle direction, un objet complet ou une sélection structurelle ; la ligne 76 seule peut perdre l'owner. |
| Première scène identitaire, première observation suffisante | START → route DIRECTION, ancre/cible et scène ; observer dans le scope, couvrir les gates et fermer via ACTION si aucun gain utile d'une correction. | Le mot « amélioration » et la sortie 94 pourraient forcer une seconde modification malgré la branche 105. |
| Composant partagé avec régression mobile | START classe SYSTÈME si décision partagée objet direct ; la preuve limite les consumers et l'issue est RETURNED si besoin ; migration et rollback retrouvables. | La chaîne créative 87/93 ne remplace pas ACTION/RUN-SYSTEM ni les preuves des consumers. |
| Agent sans source canonique ni runtime | Déclarer hypothèse et prochaine preuve, sans annoncer run V1 conforme ni résultat observé. | Ligne 81 protège la vérité ; la carte conforme au JSON ne change pas cette limite. |

**Commandes de la façade, exécutées depuis `audit_work/package` sur B01 :**

| Commande | Résultat constaté | Portée |
|---|---|---|
| `python3 scripts/read_route.py DIRECTION/START` | Code 0, titre et bloc DIRECTION retournés. | Le locator de classification cité existe. |
| `python3 scripts/read_route.py ACTION/RUN-LITE` | Code 0, bloc RUN-LITE retourné. | Le locator local cité existe ; les autres échecs du bloc 1 F-DIR-028 demeurent. |
| `python3 scripts/validate_run_card.py schemas/run_card.example.json` | Code 0, validation normale. | La structure de l'exemple satisfait le contrôle ordinaire. |
| `python3 scripts/validate_run_card.py --strict schemas/run_card.example.json` | Code 1, placeholder exact `run_card.artifact.locator`. | Le mode strict détecte ce placeholder ; l'exemple n'est pas une carte concrète. |
| `python3 scripts/validate_run_card.py --strict schemas/fixtures/valid_closed_return.json` | Code 0. | Une fixture synthétique peut satisfaire le contrôle strict avec `ticket-ou-commit` comme locator opaque ; ce passage n'atteste ni ticket réel ni régression mobile observée. |

Ce test n'est pas la campagne complète de validation des schémas et scripts : leurs autres frontières et mutations seront auditées dans la suite prévue de la phase 2. La commande littérale `chemin/vers/run_card.json` en 121 est un emplacement à remplacer par un fichier réel.

## Passage D — constats, non-fusions et protections

### F-QS-001 — parcours « création/structure » présenté comme minimum transmodal

- Gravité provisoire : **Observation à éprouver** ; la section 4/5 voisine atténue le risque et aucun usage réel n'a été observé.
- Preuve textuelle : QUICKSTART 83–94 introduit un parcours « minimal » incluant « diriger », « choisir une structure » et « premier objet complet », après 61–63 qui couvre construire **ou modifier** ; DIRECTION/START 142, ACTION/RUN-LITE 343 et BIBLIOTHEQUE/SELECT 163/193–194 n'exigent pas ces choix sur un delta strictement local.
- Effet plausible : route créative ou structurelle chargée sans décision à modifier, temps perdu, trace qui masque le petit risque réellement touché. Il n'est pas démontré qu'un agent réel le ferait.
- Propriétaire de la formulation : QUICKSTART, façade dérivée ; DIRECTION classe, BIBLIOTHEQUE possède la sélection et ACTION le minimum du mode.
- Épreuve future : faire suivre à un lecteur n'ouvrant que les lignes 61–105 (a) un wrapping LITE, (b) un onboarding critique et (c) une direction identitaire ; vérifier s'il conserve le niveau de protection de chacun et autorise zéro nouvelle route structurelle en (a). Lire les sections 4–7 à la prochaine étape avant de confirmer, atténuer ou retirer cet ID. Une correction éventuelle serait une qualification par mode de ce résumé, pas une diminution de la qualité exigée pour DIRECTION.
- Distinction : F-DIR-041 concerne un mauvais **mode** présélectionné, F-ACT-001 des routes/minima absents ; ici il s'agit de la **suractivation** créative et structurelle dans une formule générique.

| IDs préexistants | Nouvelle observation, sans créer de doublon |
|---|---|
| F-DIR-010/008, F-ACT-002 | Les lignes courtes 13–15 et 76 conservent des champs différents ; l'owner de la question 71 n'est pas dans la seconde ligne, le handoff et la carte complète restent distincts. |
| F-DIR-003, F-ACT-013/014 | L'intention et la conséquence sont correctement ordonnées par 79 ; la sortie N/A ou NOT-OBSERVED et le handoff final restent dans ACTION. |
| F-DIR-009, F-ACT-025 | 105 protège le one-shot ; 94/107 conservent un risque de modification automatique si lus seuls. Aucun nouveau défaut de gate prouvé ici. |
| F-DIR-028, F-ACT-020 | Les deux locators cités 114–115 résolvent ; cela n'efface pas les routes manquantes du bloc 1 ni la divergence normal/strict pour `trace_locator`. |
| F-ACT-008/018 | Le test strict sur une fixture synthétique est une vérification documentaire et structurelle, pas une observation indépendante d'artefact ou de tâche. |

**À préserver :** question de preuve et capacité avant exécution, séparation `INTENT`/`CHANGE`, avertissement si source indisponible, branches explicites pour reclassification et preuve insuffisante, possibilité de décider sans polish supplémentaire, et phrase 124 qui interdit d'assimiler validation à usage. Les 101 IDs des cinq propriétaires restent intacts ; F-QS-001 est le premier ID de façade, soit **102 fiches provisoires** au total. Aucun rang final de gravité, correctif normatif ou verdict système n'est décidé.

## Reprise

Les lignes **61–125** sont couvertes par les quatre passages et cinq commandes ciblées ; le précédent est corrigé sur la reproduction du chemin. **Prochaine unité : QUICKSTART.md lignes 126–157**, sections 4 et 5, jusqu'avant « Produire une qualité positive » à 158. Relire protocole §12, présent rapport, rapport précédent et baseline ; vérifier si la classification par ordre, la protection des risques critiques et le tableau de chargement lèvent F-QS-001 ou révèlent une cause distincte, et si les renvois CLI restent résolubles. Continuer ensuite les sections 6–12 et les autres façades avant la consolidation de phase 2.
