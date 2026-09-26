# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 14 : INTEGRITY

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/SAVOIR.md`, lignes **843–905** : test de non-récitation 845–847, modes d'échec et huit questions 849–878, contrôle d'intégrité 880–886, limites, délégation, curation, critique et autonomie 888–902, séparateur 904. Les règles d'or commencent à **906** et seront examinées dans le bloc suivant.
- Méthode : protocole externe v2.0, §12 relu, passages A à D. Reprise du rapport SAVOIR bloc 13, du rapport SAVOIR bloc 1, des checkpoints ACTION et DIRECTION, ainsi que des constats F-SAV-003, F-ACT-013/014/024/026/037, F-DIR-011/019/027/028. Interfaces exactes relues : `ACTION/AUTHORITY` 63–67, `ACTION/STATUS` 125–175, `ACTION/PRECONDITION` 210–236, `ACTION/GATE-B/B3` 735–753, `ACTION/PIPELINE` 469–483 ; `DIRECTION/SERVICE-BOUNDARY` 113–117, `START` 119–144 et ancrage généré 439–445 et 577–591.
- Baseline B01 inchangée : SHA-256 compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR propriétaire `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Pas de patch, de jugement de conformité d'un produit ni de verdict global. Les constats de la campagne restent provisoires jusqu'aux confrontations et tests prévus.

## Passage A — architecture visible et frontière des responsabilités

`SAVOIR/INTEGRITY` est la route de jugement qui cherche un **effet inspectable**, puis une limite explicite. Elle possède deux déclencheurs spécialisés : avant un verdict `DIRECTION` ou face à un risque de conformité seulement textuelle (851), et lorsque la capacité est incertaine, la direction ambiguë, l'asset critique ou un second regard nécessaire (890). Elle ne s'applique donc pas comme nouvelle fiche universelle à chaque micro-correction. Le test d'entrée 847 retire les artefacts de jugement purement récitatifs ; les huit questions 871–878 cherchent ensuite une décision, une ancre/spec applicable, une preuve, une hypothèse et un effet concret. La réponse au risque le plus élevé se relie à au moins un objet consultable (882).

La phrase « Bloque si… » (869) n'invente pas une nouvelle taxonomie d'issues : 886 renvoie les limites au **couple canonique approprié dans ACTION**, qui porte verdict, preuve et clôture. `DIRECTION` décide du mode, de la cible et des conditions de l'ancre ; `SAVOIR` éprouve la qualité du jugement ; `ACTION` qualifie l'observation et la sortie ; l'owner conserve l'autorité de décision. Une revue ou une capacité déléguée n'occupe aucun de ces rôles par simple déclaration.

**Accès outillé :** `read_route.py SAVOIR/INTEGRITY` renvoie « locator inconnu », alors que `validate_reading_map.py` affiche `READING MAP VALIDATION PASSED`. La route est lisible dans la source. C'est une nouvelle occurrence de F-DIR-028/F-ACT-001, pas un nouvel ID pour chaque titre refusé.

## Passage B — contrat sémantique, phrase par phrase

### Test de non-récitation et huit questions (845–878)

Le test 847 demande quelle décision « a changé » grâce au module, puis conseille arrêt, simplification ou `N/A-JUSTIFIED` si aucune. Le handoff général SAVOIR 30 emploie la même formule. **Une lecture littérale « modification visible seulement » est trop étroite :** la question 877 inclut expressément décision **modifiée, confirmée ou abandonnée** ; ACTION 212–218 et 234–236 reconnaît ces trois conséquences après observation. Une première capture qui confirme, preuves en main, la direction retenue peut donc avoir une conséquence décisionnelle sans changer les pixels. Elle n'est pas documentaire pour cette seule raison. À l'inverse, une confirmation alléguée sans observation n'est pas `DECISION-CHANGE`. Le rapport SAVOIR bloc 1, lignes 54, 74 et 97, avait déjà isolé cette tension et sa relation à F-DIR-011/019 et F-ACT-013/014 : **occurrence confirmée, pas de nouvel ID redondant**. Le risque de mauvaise classification demeure à tester chez un lecteur sous contrainte de temps.

Le déclencheur 851 nomme onze formes de conformité théâtrale. Les plus discriminantes sont : ancre uniquement écrite (857) ou référence non ouverte (858), test non rejoué après une modification pertinente (859), avis humain sans objet regardable (863), contexte produit supposé (864), matière/dial utilisés sans décision (862, 865). La liste ne dispense pas de prouver le résultat adapté au risque : une spec peut être authentique et le rendu divergent, une capture peut être réelle et l'usage critique non testé. Les questions 871–878 demandent respectivement objet d'ancrage, décision perceptible, alternative si décision ouverte, écart spec/rendu, preuve manquante, hypothèse et owner, conséquence de décision, puis contournement de lettre. Leur exigence doit rester conditionnelle au mode et à la responsabilité applicable : 871 autorise une non-applicabilité **justifiée** d'ancre ; 873 admet une raison de non-comparaison ; ACTION 469–471 proscrit la variante artificielle ; `DIRECTION/START` 142 préserve le micro-delta local d'un chargement inutile.

### Preuve, délégation et sorties (880–886)

Le « au moins un » de 882 est un **plancher de rattachement de la réponse au risque le plus élevé**, pas un quota maximal de preuves pour tout le run. L'objet peut être capture, spec, diff, test, code, URL, donnée ou journal ; sa présence seule ne prouve pas la propriété alléguée. Une URL non consultable n'est pas une inspection et un asset générationnel ne devient pas authentique parce qu'un journal le mentionne. Quand une tâche est déléguée, il faut regarder le résultat (884) ; l'enregistrement du nom du délégataire n'est pas un PASS.

La ligne 886 pose une distinction utilisable : `N/A-JUSTIFIED` pour une **vraie non-applicabilité**, `NOT-VERIFIED` pour une preuve pertinente absente, `EXPLORATORY` lorsque l'artefact existe mais que sa portée ou sa preuve reste incomplète, `RETURNED` pour reprendre correction ou preuve. Ce sont des catégories de niveaux différents dans ACTION (notamment statut d'axe et issue globale) et « couple canonique » appelle l'assemblage compatible avec `ACTION/STATUS` 125–175 ; SAVOIR ne prononce pas lui-même le verdict. Si une conséquence était attendue et n'a pas eu lieu, ACTION 236 propose aussi `NOT-OBSERVED` dans la trace ; 886 ne doit pas rabattre ce cas sur N/A. Les points de projection machine déjà recensés F-ACT-013/014 ne sont pas résolus par la seule prose d'INTEGRITY.

### Capacité, curation, regard et autonomie (888–902)

La ligne 890 impose quatre qualifications distinctes : connu, inféré, vérifié, hors de portée. Une capacité change la preuve **possible**, jamais le résultat (892). Le dossier de délégation conserve délégataire, rôle, capacité déclarée, méthode, scope, artefact/résultat effectivement consulté, date/version, limite, owner de décision finale, `NEXT-PROOF` et condition de reprise ou d'escalade. Cette précision renforce `ACTION/AUTHORITY` 63–67 : un opérateur capable d'exécuter ne reçoit pas l'autorité de changer un seuil, de clore un risque ou de faire une action externe hors scope. Il faut distinguer autorisation et effet observé, notamment pour une action hors système que V1 ne peut exécuter (DIRECTION 115–117).

La ligne 894 interdit de présenter une abstraction, un placeholder ou une image générée comme asset authentique. Elle **admet explicitement** l'abstraction assumée, au rôle honnête et à l'effet adéquat. Le modèle, le prompt et l'outil ne prouvent ni qualité, ni droit, ni adéquation (896). Une curation active est permise avec origine, provenance, autorisation, usage, transformation, limite, owner et revue (898). C'est une protection contre la substitution et l'accumulation passive, sans faire du bon dossier d'asset une preuve de son intégration réelle, ni trancher à lui seul les droits de réemploi (F-ACT-024/028).

Les rôles de critique (900) sont des **lentilles** qui nomment problème, correction, preuve et scope ; ils ne permettent pas d'annoncer une équipe fictive. Un humain distinct peut fournir un contrepoint situé ; « indépendant » exige relation, rôle, méthode, date et limites. `ACTION/GATE-B/B3` 735–753 ajoute artefact/exposition, distinction aveugle/non aveugle et refus d'étiqueter indépendante la seconde session du même auteur. La prose d'INTEGRITY **réduit** l'ambiguïté, mais F-ACT-037 demeure pour le transport machine de l'auto-déclaration d'indépendance. Même une revue réellement indépendante d'une image générée ne devient pas, à elle seule, une calibration externe de l'identité à fort enjeu : réserve ou ancre/contrainte réelle restent requises selon DIRECTION 441/587 et ACTION 477 (F-SAV-003).

Enfin, 902 conserve l'autonomie **déjà accordée** par utilisateur/owner dans le périmètre DIRECTION annoncé. Une marque, un public, une surface identitaire ou une hypothèse nouvelle hors de ce périmètre provoquent un checkpoint de cadrage, sauf instruction explicite qui les couvrait déjà. Le checkpoint n'est pas un prétexte pour redemander permission sur une action déjà autorisée ; il sert à identifier la nouvelle décision, son risque et son owner. Il n'annule ni les droits, ni l'owner final, ni l'escalade nécessaire. Une simple variante au sein de l'hypothèse autorisée n'est pas mécaniquement une nouvelle autorité à solliciter.

## Passage C — parcours de lecteurs sous contrainte

| Lecteur et situation | Lecture/action attendue | Échec testé |
|---|---|---|
| Designer, premier rendu confirme la direction, aucun pixel retouché | Conserver capture, comparaison, raison de la confirmation et `DECISION-CHANGE` après observation ; ne pas inventer une itération | Lire 847 comme exigence de modification physique et classer N/A une confirmation utile |
| Agent, fiche élégante mais aucune ancre ouverte ni spec exploitable | Relier la question 871 à l'objet absent ; rendre la preuve `NOT-VERIFIED`, reprendre si nécessaire | Présenter une fiche d'intention comme ancre et un PASS documentaire |
| Intégrateur, rendu modifié après test initial | Rejouer le contrôle touché et conserver capture/log mis à jour ; qualifier la limite des autres contrôles | Étendre un ancien PASS à la nouvelle version (859) |
| Équipe, identité à enjeu élevé avec seule ancre générée, avis humain honnête | Documenter le regard et sa limite ; maintenir référence/contrainte réelle ou réserve de calibration (F-SAV-003) | Substituer avis, prompt ou modèle à une calibration externe |
| Responsable, asset critique curaté et droit incertain | Consigner provenance, transformation, scope et statut d'autorisation ; poursuivre seulement selon la preuve et l'autorité disponibles | Déduire une licence d'une source citée ou d'une génération réussie |
| Agent, audit délégué et livrable revendiqué « validé » | Examiner artefact, méthode, date/version et résultats ; garder owner final et prochaine preuve | Prendre délégation, expertise annoncée ou champ `APPROVED` pour preuve ou verdict |
| Reviewer, seconde session du même auteur | Qualifier comme auto-comparaison ; ne pas afficher indépendante/aveugle (B3) | Simuler une équipe ou une pluralité réelle |
| Agent, nouvelle marque hors scope puis variante interne autorisée | Nouveau cadrage pour la marque, poursuite autonome pour la variante couverte | Étendre silencieusement le mandat ou bloquer inutilement le mandat existant |

Ces parcours sont des **simulations de lecture** appuyées sur la source, pas des essais de comportement humain déjà observés. Ils alimenteront les tests de chaîne et de projection ultérieurs ; leur réalisation ne suffit pas à attribuer une fréquence d'erreur réelle.

## Passage D — résistance, déduplication et décision provisoire

**Aucun nouvel ID autonome dans ce bloc.** Le décalage « changé »/« confirmé » déjà consigné au bloc SAVOIR 1 trouve une occurrence plus saillante dans le test 847, mais la question 877 et ACTION 215/236 donnent la bonne interprétation. Le garder comme scénario de F-DIR-011/019 et F-ACT-013/014 jusqu'à un test lecteur et machine. Une correction éventuelle devra préserver la confirmation observée, sans transformer n'importe quelle absence de changement en succès.

| Observation ou attaque | Traitement et limite |
|---|---|
| Locator INTEGRITY refusé, validation de carte verte | F-DIR-028/F-ACT-001 ; accès exact à la source possible, accessibilité de la route non démontrée |
| `N/A` tenté quand seule la preuve manque ou que l'effet attendu est absent | ACTION 218/236 et INTEGRITY 886 distinguent N/A, NOT-VERIFIED et NOT-OBSERVED ; F-DIR-011/019 et F-ACT-014 restent à rejouer |
| Texte, prompt, reviewer ou délégation utilisés comme preuve de qualité | 882–900 imposent objet et examen ; F-ACT-026/028/037 maintenus pour autorité, transport et indépendance déclarée |
| Regard indépendant censé remplacer la calibration d'identité | F-SAV-003, mécanisme distinct de la qualification du reviewer F-ACT-037 |
| Source d'asset et autorisation confondues | 894–898 et F-ACT-024/028 ; vérifier droit applicable à l'usage et résultat intégré |
| Checkpoint brand/hypothèse interprété comme arrêt universel | 902 contient l'exception des instructions couvrant déjà le scope ; ACTION/AUTHORITY délimite les décisions et la reprise |
| « Au moins un artefact » pris pour plafond de vérification | 882 porte sur l'accroche du risque le plus élevé ; autres protections ACTION applicables restent requises |

**Protections à conserver lors de l'éventuelle correction :** vérification d'effet concret, possibilité de confirmer sans bricoler une modification, questions conditionnelles et proportionnées, preuve réellement inspectable, séparation preuve/autorité, transparence du synthétique et de la curation, regard humain situé, autonomie dans le scope accordé, retour à ACTION pour la sortie. Ne pas dégrader ces protections pour résoudre une ambiguïté lexicale.

## Couverture, limites et reprise

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | Déclencheurs, portée des huit questions, propriétaire du verdict, locator refusé |
| B — sémantique | FULL | 845–902, conditions, preuves, états, délégation, asset, critique et autonomie ; interfaces ACTION/DIRECTION |
| C — usage | TARGETED | Huit simulations agent, designer, équipe, intégrateur, reviewer et owner ; effet et limite explicites |
| D — résistance | TARGETED | Déduplication des IDs, scénarios N/A, indépendance et calibration, droits, autonomie, quota fictif |
| Machine | TARGETED | `read_route.py` échec ; `validate_reading_map.py` succès ; projection détaillée différée aux contrats machine |
| Externe | N/A-JUSTIFIED | Aucune assertion externe nouvelle ni produit réel à certifier dans ce bloc |

Le bloc 14 est lu jusqu'à son séparateur de 904 ; ni règles d'or ni méthodologie studio ne sont considérées terminées. Aucun patch et aucun verdict global. **Prochaine unité :** `SAVOIR.md`, lignes **906–941**, bloc 15, puis checkpoint consolidé SAVOIR. Reprendre le protocole §12, la baseline, ce rapport et les constats liés avant la lecture ; vérifier si les règles de synthèse clarifient les tensions, sans déduire leur contenu de ce rapport.
