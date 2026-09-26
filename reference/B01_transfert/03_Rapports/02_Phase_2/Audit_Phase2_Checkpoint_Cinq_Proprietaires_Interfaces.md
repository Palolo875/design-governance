# DG-AUDIT-001 — Phase 2 — Checkpoint transversal des cinq propriétaires normatifs

## Fonction, méthode et limites

Ce checkpoint relie les lectures complètes de `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md` et `CHANGELOG.md`. Il constitue la **sortie de consolidation locale des sources normatives dans la phase 2**, avant lecture des façades, contrats machine, scripts, skill et distributions. Il ne constitue ni la carte finale des rôles (phase 3), ni une évaluation globale, ni une classification définitive (phase 10), ni une décision de correction. Le protocole externe v2.0 §12 a été relu : architecture visible, contrat sémantique, lecteurs simulés, résistance ; aucune conclusion n'est fondée sur un seul extrait ou une façade.

Les sources propriétaires, rapports sectionnels, quatre checkpoints de propriétaire et le rapport CHANGELOG font foi avant ce document. Les exemples ci-dessous sont des **parcours d'épreuve à exécuter plus tard** ; les risques documentaires et quelques tests machine antérieurs n'établissent ni fréquence réelle d'échec, ni performance du système en production. Aucun fichier du système n'est modifié.

## Intégrité de la baseline et des entrées

| Élément | Valeur vérifiée |
|---|---|
| Campagne | `DG-AUDIT-001` ; profil `DEEP` adaptatif ; baseline `B01` |
| Système compilé | SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Protocole v2.0 | SHA-256 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| `DIRECTION.md` | 818 lignes ; SHA-256 `f634bc561dab243e53fa1a988c2a49565f3d6330a8e5af0e4fbaea4128bf2a7f` |
| `ACTION.md` | 935 lignes ; SHA-256 `d73ad55167f71f775954092c3a91c00347753cae520031202f946b228257b50d` |
| `SAVOIR.md` | 941 lignes ; SHA-256 `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820` |
| `BIBLIOTHEQUE.md` | 791 lignes ; SHA-256 `8628595d6323df5d76c2b0d57dbe49fd11e62c3178e1ce849e5d72799bb03684` |
| `CHANGELOG.md` | 63 lignes ; SHA-256 `0876654994f063ebb670392a5967044ad483bbdb8ebf6b5ce8a156609f08df45` |
| Couverture | **3 548/3 548 lignes** des cinq sources par rapports sectionnels ; DIRECTION 1–817 et dernière ligne vide 818, autres propriétaires couverts jusqu'à fin ; **ce ratio ne mesure pas la progression de l'audit total** |
| Intégrité des pièces de consolidation | SHA-256 du manifeste ordonné des quatre checkpoints et du rapport CHANGELOG : `4a9532a9c31224b10e0a76e5965ff3185537c2ee8d9ea39ad7c0d525bb465a9c` |

Le manifeste concatène, en ordre DIRECTION → ACTION → SAVOIR → BIBLIOTHEQUE → CHANGELOG, les lignes `SHA256<deux espaces>nom_du_fichier\n` des checkpoints `Audit_{DIRECTION,ACTION,SAVOIR,BIBLIOTHEQUE}_Phase2_Checkpoint_Consolidation.md` et du rapport `Audit_CHANGELOG_Phase2_01_Baseline_Autorite_Cycle_Migration_Limites.md`. Les hashes source demeurent l'autorité si un rapport est corrigé ultérieurement.

| Propriétaire | Rapports / consolidation | Registre provisoire | Contrôle de continuité |
|---|---|---|---|
| DIRECTION | Dix rapports et checkpoint propriétaire | F-DIR-001 à F-DIR-046, **46** | Séquence 1–46 sans trou ; dix plages revérifiées, intervalles non normatifs vérifiés dans son checkpoint |
| ACTION | Douze rapports et checkpoint propriétaire | F-ACT-001 à F-ACT-039, **39** | Séquence 1–39 sans trou ; 935 lignes vérifiées |
| SAVOIR | Quinze rapports et checkpoint propriétaire | F-SAV-001 à F-SAV-010, **10** | Séquence 1–10 sans trou ; 941 lignes vérifiées |
| BIBLIOTHEQUE | Quinze rapports et checkpoint propriétaire | F-BIB-001 à F-BIB-005, **5** | Séquence 1–5 sans trou ; plages contiguës 1–791 |
| CHANGELOG | Un rapport propriétaire 1–63 tenant lieu de checkpoint | F-CHG-001, **1** | ID unique et lecture 1–63 complète |
| **Total de fiches** |  | **101 IDs provisoires** | Nombre de constats inscrits, **pas** 101 défauts de production prouvés ni 101 corrections obligatoires |

Les cinq ensembles d'IDs sont continus. Chaque fiche détaillée demeure dans son rapport d'origine ; les registres complets DIRECTION/ACTION/SAVOIR/BIB et F-CHG-001 évitent qu'un tableau transversal court efface un constat moins visible. Aucune sévérité ni statut de disposition n'est changé ici.

## Frontières d'autorité vérifiées dans les textes

| Question | Propriétaire et sortie attendue | Passage à ne pas confondre |
|---|---|---|
| Quelle décision et quel risque dominent ? | `DIRECTION/START` 129–144 classe l'objet **direct** du run et son mode, sépare dépendances partagées et risque critique. | Un effet partagé induit par une direction n'impose pas la reclassification immédiate de toute la tâche en SYSTÈME (F-SAV-007), mais une responsabilité critique touchée peut interdire un micro-delta LITE/ITER (F-DIR-007). |
| Comment travailler, vérifier et livrer ? | ACTION porte routes LITE/ITER/STANDARD/DIRECTION/SYSTÈME, méthodes, preuves, gates A/B/C, axes V/U/A/T, état, issue, statut de direction, verdict et `CLOSE-EXIT-CHECK` 915–930. | Un statut d'axe `PASS`, `CLOSED` ou une liste de routes ne devient pas `ACCEPTED` global ; une preuve nécessaire absente reste `NOT-VERIFIED`, non `N/A-JUSTIFIED`. |
| Comment juger le registre et les risques spécialisés ? | SAVOIR/CRAFT/STYLE/TYPE/STATE/SOURCE/SYSTEM/CONTEXT/TECH/TOOLS fournit des critères conditionnés à la décision et au médium (ATLAS 530–541). | Une heuristique de style ne crée ni mode, ni structure, ni résultat de tâche. Un avis expert ou indépendant ne remplace pas automatiquement preuve de droits, calibration d'une ancre ou utilisateur représentatif. |
| Quelle structure changer et prouver ? | BIBLIOTHEQUE/SELECT 163–199 retient zéro à plusieurs responsabilités ; objets et MICRO dans leur scène ; GATE 697–703 est complémentaire. | Le contrôle de module ne crée pas de quatrième gate ni de verdict ; une image/asset ne devient pas route structurelle par son seul emploi. |
| Quand une règle ou route devient-elle partagée/durable ? | CHANGELOG 25–42 gouverne décision de cycle de vie et migration ; BIB/EVOLUTION 735–762 évalue les routes **structurelles** sur usages contrastés, gain et maintenance ; ACTION/RUN-SYSTEM 379–387 porte impact/consumers/rollback. | DIRECTION 817 force encore BIB/EVOLUTION pour toute route partagée (F-DIR-046) ; CHG F-CHG-001 laisse le seed et un PILOT utilisé sans transition de dépréciation explicite. |

Ces frontières sont des **hypothèses d'intégration issues des sources**, non une nouvelle norme écrite par le checkpoint. Les corrections devront conserver l'unicité de propriétaire sans escamoter les interfaces et les consumers. La typologie `PERCEPTUAL`/`EXPERT`/`TECHNICAL`/`USER/TASK` de BIBLIOTHEQUE dit ce qu'une preuve peut établir, ACTION dit comment elle est obtenue et quelle conclusion est justifiée ; `EXPERT` type et `METHOD: EXPERT` ne sont pas synonymes.

## Chaînes transversales à éprouver, sans fusion automatique

| Chaîne / scénario | IDs à confronter et raison de les distinguer | Source puis surface dérivée à lire |
|---|---|---|
| **Entrer et charger.** Un brief vague/critique ouvre une route correcte, puis trois jugements utiles ; quelles routes sont réellement chargées ? | F-DIR-001/028/041/043, F-ACT-001/004/016/029, F-SAV-001/004/010. Ordre de la façade, plafond suggéré de routes, omission de SAVOIR/SYSTEM et locator CLI absent sont quatre causes distinctes ; neuf des treize titres BIBLIOTHEQUE étaient refusés malgré carte valide. | DIRECTION/START, ACTION/ROUTING, SAVOIR/ATLAS, BIB/SELECT → QUICKSTART, READING_MAP, ORCHESTRATION_MAP → lecteur/fixtures. |
| **Classer le risque et l'objet direct.** Correction apparemment locale de permission/focus, identité avec token induit et décision de token partagé direct. | F-DIR-007/014/016/031/038, F-ACT-011/017/026, F-SAV-007/010, F-BIB-003. Un local critique touchant responsabilité n'est pas un mode LITE ; un token secondaire n'est pas toujours le run principal. | DIRECTION/START 129–144, ACTION/PRECONDITION, SAVOIR/SYSTEM 694, BIB/GRID → QUICKSTART et schémas de mode. |
| **Transmettre sans perdre.** Hypothèse pré-build → artefact → observation datée → RUN_CARD/trace → paquet de clôture ; comparer variante DIRECTION, ITER et composant partagé. | F-DIR-003/006/008/010/023/027/036/039/045, F-ACT-002/006/015/021/028/030, F-SAV-005, F-BIB-004. Mapping générique, chemin JSON erroné, contrat du composant manquant et minimum SYSTÈME non opposable sont indépendants ; ne pas les fusionner sous « compléter le formulaire ». | ACTION/RUN_CARD/CLOSE-PACKAGE et SAVOIR/SYSTEM 704, BIB/COMPONENTS → exemples, schéma, validateurs, trace externe. |
| **Prouver, borner et fermer.** Réutiliser une paire B1b pour une autre décision, rendre un PASS technique sur un état nominal et livrer une autre version. | F-DIR-011/019/024/035, F-ACT-005/009/012/013/014/018/022/031/034/036, F-BIB-001. N/A, absence d'observation attendue, preuve impossible, version périmée, axe bloquant et exception B1b sont des situations distinctes. ACTION 714 exige **exactement la même décision** ; SELECT 173 n'explicite pas cette portée. | ACTION/GATE-B 704–716 et CLOSE-EXIT-CHECK 915–930, BIB/SELECT 171–173 → RUN_CARD, fixtures négatives, QUICKSTART. |
| **Créer sans surcontraindre.** Une scène sobre avec asset explicatif, une identité colorée, un premier contact sensible et un one-shot déjà suffisant. | F-DIR-009/012/018/024/030, F-ACT-025/037, F-SAV-002/003/006/008, F-BIB-005. Ablation STYLE et GATE touche deux propriétaires et deux décisions ; obligation de retoucher après une bonne première observation est un autre défaut. | DIRECTION/FIRST-OBJECT 316, SAVOIR/CFT-04a 348/STYLE 632, BIB/SCENE 443–445/GATE 707, ACTION/GATE-C → guides, skill, tests de capacité positive. |
| **Partager, promouvoir, déprécier.** Composant Web/mobile, règle de jugement non structurelle, route seed sans gain mesuré et PILOT avec consumers. | F-DIR-046, F-ACT-015/021/031, F-SAV-004/007, F-BIB-002/004, F-CHG-001. Mauvais passage par BIB, manque de contrat composant, absence de paquet contrôlé et trou dans les transitions sont distincts ; la baseline expérimentale n'est pas un gain `ADOPTED`. | DIRECTION 817, ACTION/RUN-SYSTEM, SAVOIR/ATLAS/SYSTEM, BIB/EVOLUTION, CHANGELOG 21/37–42 → guides, schéma, migration, distributions. |
| **Grounding, droits et autorité.** Asset externe/généré, risque de confidentialité et délégation à un reviewer. | F-DIR-021/022/026/027/029, F-ACT-024/026/028/037/038, F-SAV-003/009. Provenance, droit, ancre externe, pouvoir de décision, qualité du reviewer et échec connu ne sont pas interchangeables. | DIRECTION/VISUAL_TARGET, ACTION/AUTHORITY/PROOF, SAVOIR/SOURCE/TECH/INTEGRITY, CHANGELOG pour promotion si règle commune → QUICKSTART, skill et fixtures. |
| **Mesurer la méthode et ses claims.** Façade instrumentée, validation verte, efficacité/adoption déclarées. | F-DIR-002/044, F-ACT-008, CHANGELOG 21/60–62. Une taxonomie de lectures claire aide à mesurer, sans démontrer elle-même gain, usage, perception de qualité ou performance. | DIRECTION/lecture instrumentée, ACTION/MAINTENANCE, CHANGELOG → cartes, scripts, release, pilotes après stabilisation. |

Les chaînes sont des **cibles de test**, pas des familles d'IDs exclusives : un ID peut apparaître dans plusieurs scénarios. Chacun demeure dans **un seul registre et une seule famille de propriétaire** selon son checkpoint. Les 101 fiches ne sont donc pas répétées ni fusionnées par ce tableau.

### Déduplications et réserves particulièrement sensibles

1. **F-DIR-011 / F-DIR-019 / F-ACT-014.** DIRECTION propose une fusion possible de ses deux occurrences d'absence de conséquence ; ACTION montre qu'un `NOT-OBSERVED` n'a pas de place claire dans la projection. Cela ne suffit pas encore à démontrer une seule cause et un seul test de non-régression. Maintenir les trois références.
2. **F-DIR-028 / F-ACT-001 / F-SAV-004.** Locator non résolu, chargement minimal par mode et route SAVOIR/SYSTEM omise ont des correctifs distincts ; une carte `READING_MAP` valide ne prouve pas l'accès par CLI.
3. **F-SAV-004 / F-BIB-004 / F-ACT-015/021.** L'ATLAS peut omettre le bon renvoi ; COMPONENTS peut manquer des détails malgré bon renvoi ; RUN_CARD peut accepter un paquet SYSTÈME incomplet malgré contrat humain. Garder trois lieux de contrôle.
4. **F-SAV-006 / F-BIB-005.** Deux tests de masquage peuvent punir un média porteur ; STYLE conclut sur un profil, BIB/GATE ordonne de changer une relation structurelle. Leur correction pourra partager une épreuve, pas effacer deux mécanismes propriétaires avant preuve.
5. **F-BIB-001 / F-ACT-036.** Une exception B1b sémantiquement trop large et la non-opposabilité machine de la paire sont deux défaillances : tester même décision, autre décision et paire absente.
6. **F-DIR-046 / F-CHG-001.** Le premier force BIB sur une promotion non structurelle ; le second ne donne pas de statut/transition honnête pour seed et PILOT dépendant. Une redirection d'owner ne crée pas la transition manquante.
7. **F-DIR-002 / F-CHG-001.** Claim d'efficacité non démontré et bootstrap de cycle de vie ont une interaction, mais CHANGELOG 21 protège déjà explicitement contre le gain inventé. Ne pas résoudre la migration en prétendant que la baseline expérimentale avait été mesurée.

## Capacités et protections à préserver lors de la suite

- **Décision avant procédure :** une route est chargée parce qu'elle peut changer la décision, la preuve ou la limite ; zéro route BIB et un local LITE peuvent être justifiés ; pas de quotas de variantes, lectures, itérations ou retraits.
- **Qualité réelle du premier rendu :** forme spécifique et habitable, contenu et états crédibles, visée perceptuelle située ; une proposition sobre ou conventionnelle peut être excellente, un média explicatif peut porter la relation, et une première version correctement observée peut rester le résultat final.
- **Preuve honnête :** intention avant artefact, résultat après observation ; médium/scope/version/méthode/limite explicites ; N/A réelle distincte d'une preuve requise indisponible et d'un échec connu ; un PASS isolé ne devient pas verdict global.
- **Proportion et protection critique :** limiter la charge locale sans abaisser la classification d'une permission, santé, accessibilité ou confidentialité réellement touchée ; une alternative prévue, une revue supposée indépendante ou un package validé ne comptent pas comme résultat exécuté.
- **Gouvernance réversible :** propriétaire du changement, consumers, compatibilité, migration/rollback, gain réellement situé et revue ; conserver l'accès aux anciens runs sans transformer un alias déprécié en route active ni une route seed en gain mesuré.

## Plan de lecture suivant et conditions de sortie

Les **616 lignes** des cinq documents d'entrée dérivés se répartissent comme suit : `QUICKSTART.md` 313, `READING_MAP.md` 127, `ORCHESTRATION_MAP.md` 53, `GLOSSAIRE.md` 71, `README.md` 52. Ils seront lus comme des **interfaces de lecture**, non comme nouvelles sources de règles. Vérifier le sens vers les propriétaires, les titres/locators réellement disponibles et les minima de preuve, plutôt qu'inférer l'autorité du seul nom de fichier.

1. **Prochaine unité : QUICKSTART.md lignes 1–60**, démarrage 90 secondes, résolution rapide, profondeur et constitution minimale. Puis ses autres sections dans l'ordre réel, en reprenant chaque fois la dernière unité et B01.
2. READING_MAP, ORCHESTRATION_MAP, GLOSSAIRE, README : relire chacun intégralement avec comparaison ciblée à la source propriétaire et tests d'accès applicables. L'ordre interne pourra être ajusté à une dépendance constatée, explicitement dans le plan.
3. Schémas, exemples et fixtures `RUN_CARD` ; scripts lecteurs/validateurs/build/manifest/workflow ; skill et références ; release/package/migration ; distributions GitHub et Local. Chaque résultat de validation conservera sa **portée technique**, sans claim d'efficacité réelle.
4. Checkpoint final de phase 2 puis phases 3–14 : rôles, contrats, architecture de l'information, capacité positive, boucles, perspectives, résistance, classement, décision de correction, patch, validation et clôture de l'audit.

**Condition de sortie de cette consolidation :** les cinq hashes source concordent avec B01, les 101 IDs provisoires ont chacun leur fiche propriétaire sans trou de séquence, les différences de cause/propriétaire restent visibles, les protections positives et réserves sont transportées, le prochain bloc exact est écrit et aucun patch ni verdict système n'est prononcé. Conditions remplies pour ouvrir les façades en phase 2. Une cause révélée ultérieurement pourra conduire à fusionner, reclasser ou retirer un ID avec trace explicite ; rien de tel n'est décidé ici.
