# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 3 : CRAFT, premier rendu et forme située

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **195–280** ; introduction CRAFT (195–209), `CFT-00` (211–240), `CFT-01` (242–279). `CFT-02` commence à 281 et attend le prochain bloc.
- Protocole externe : §12, passages A architecture, B contrat sémantique, C lecteurs réels simulés, D résistance. Reprise des rapports SAVOIR blocs 1–2, des checkpoints DIRECTION et ACTION et du plan maître. Interfaces ciblées : `DIRECTION/CREATIVE-BOOT`, `DIRECTION/DOUBLE-LOOP`, `ACTION/FIRST-RENDER`, `ACTION/PIPELINE-DIRECTION`, `ACTION/GATE-B/B1b`, `ACTION/ANTI-SLOP`, `ACTION/RUN_CARD`.
- Baseline B01 revérifiée et inchangée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Diagnostic de lecture seulement : aucun patch, aucune preuve de qualité de produit réel et aucun verdict global. Les contrôles ACTION exécutés dans les rapports précédents sont réutilisés, sans prétendre qu’un nouveau run a été réalisé ici.

## Résumé du bloc

CRAFT protège la **qualité de départ** sans la confondre avec une qualité prouvée. Il demande un premier objet réellement composé lorsqu’une direction visuelle est ouverte, puis une observation de ce qui est construit ; la réussite d’usage, d’accessibilité, de robustesse et de performance demeure du ressort d’ACTION. Il autorise expressément le one-shot après cette observation si le rendu tient et si les risques applicables sont couverts. `CFT-00` rend la critique esthétique plus précise et située ; `CFT-01` remplace les interdits de motifs par un test motivation/construction et une forme dérivée de la tâche et des données.

La difficulté déterminante est **interne au système** : la branche one-shot de SAVOIR (205) et ACTION (453) permet de s’arrêter, mais `DIRECTION/CREATIVE-BOOT` (184) demande encore une modification et `ACTION/GATE-B/B1b` (704–716) impose une édition et deux captures dès que son déclencheur est actif, même si aucune correction utile n’est attendue. C’est une nouvelle occurrence de **F-DIR-009**, déjà ouverte et élargie dans le checkpoint ACTION ; elle n’appelle pas un nouvel ID SAVOIR. Le validateur ne peut pas opposer B1b à une carte qui avoue manquer la paire (F-ACT-036, démontré dans le rapport ACTION bloc 10). Le texte CRAFT est ici la règle positive à préserver pendant la réconciliation future, sans affaiblir une comparaison qui produit réellement une preuve.

## Passage A — architecture visible

| Lignes | Fonction et autorité | Sortie, renvoi et limite |
|---|---|---|
| 195–209 | Polish structurel et expressif, trois qualités distinctes, branche one-shot et boucle de jugement | L’observation de l’objet est nécessaire ; « modifier → réobserver » est la branche de correction, pas un quota après un premier objet déjà suffisant |
| 211–229 | `CFT-00` `[DURABLE]`, huit dimensions de critique et premium situé | Questions avec signaux observables ; ni score de beauté, ni verdict, ni promesse universelle |
| 230–240 | `Creative Quality Review` `[MÉTHODE]`, composant authored, AI slop, statut des ancres | Prochaine action liée à un objet ; la référence ne devient pas preuve ; ACTION seul porte `DECISION-CHANGE` observé |
| 242–259 | `CFT-01` `[DURABLE]`, matrice 2 × 2 motivation/construction, propriétaire canonique | `ACTION/ANTI-SLOP` décide de la conséquence de gate ; aucun verdict automatique par motif |
| 261–279 | Dérivation bornée `[MÉTHODE]`, cinq tests, preuve perceptuelle bornée | Métaphore facultative ; états et accessibilité subsistent ; aucun quota de variante ou de nouveauté |

La route parente `SAVOIR/CRAFT` se charge dans `scripts/read_route.py`, et `validate_reading_map.py` passe. En revanche le chemin textuel `SAVOIR/CRAFT/CFT-01`, cité comme « source canonique » ligne 255 et par ACTION ligne 800, est refusé comme locator direct ; son titre reste accessible dans la route parente et par recherche. C’est une occurrence de la couverture des clés de lecture **F-DIR-028/F-ACT-001**, pas la preuve que la matrice manque de SAVOIR ni une raison d’en dupliquer le texte dans ACTION.

## Passage B — contrat sémantique, section par section

### Premier rendu, preuve et boucle (195–209)

Le polish structurel (197) concerne proportion, hiérarchie, densité, lisibilité, états et comportement. La phrase de la ligne 201 conditionne sa demande forte à la **direction visuelle ouverte** et au périmètre du mode : moodboard, wireframe creux ou conformité nominale ne tiennent pas lieu de scène réelle si la décision exige une scène. `ACTION/FIRST-RENDER` (81–91) définit, lui, une qualité proportionnée pour les cinq modes, y compris un delta local ; la règle forte CRAFT ne doit pas écraser cette proportionnalité.

La ligne 203 distingue la cible intrinsèque, le rendu construit inspectable et la qualité effectivement prouvée. Une impression perceptuelle ne prouve ni réussite de la tâche ni conformité ; inversement un PASS technique ne prouve pas la singularité. La ligne 205 requiert préparation, premier objet complet et observation réelle avant l’arrêt. S’il subsiste un défaut dominant ou un risque applicable, corriger ou retourner ; si la qualité et les risques tiennent, arrêt possible. La boucle écrite à la ligne 207 inclut une modification : lue isolément, elle pourrait paraître toujours obligatoire ; lue avec la condition d’arrêt explicite deux lignes plus haut et `ACTION/PIPELINE-DIRECTION` (451–453), elle décrit la **suite si une correction est nécessaire**. Une nouvelle rationale ou un ornement sans effet ne compte pas comme correction. La distinction polish expressif/décoratif (209) vise l’utilité perceptuelle située et protège l’intensité justifiée, pas une esthétique minimaliste par principe.

### CFT-00 : ambition et revue créative (211–240)

Le principe `[DURABLE]` (213) demande présence, point de vue, spécificité, culture visuelle transformée, composition, expression, désirabilité située et résolution proportionnée. La réserve (215) refuse score et verdict universel ; les huit lignes 219–226 sont des **questions de critique associées à des signaux sur l’objet**, pas huit PASS obligatoires indépendants. `DIRECTION/CREATIVE-BOOT` (175, 182) peut choisir jusqu’à trois qualités prioritaires comme foyer de construction sans dispenser des autres risques applicables. La proposition premium (228) doit tenir sous contenu réel, états et mobile ; elle ne découle pas d’un style.

La revue (232) demande au moins un objet ou une relation réellement observable et une prochaine action ; elle ne remplace pas les preuves ACTION. « Après la première scène et après la repasse de craft » peut pousser un lecteur pressé à faire une seconde passe systématique. Comme `[MÉTHODE]`, la revue est compatible avec l’arrêt de la ligne 205 si aucune repasse utile ne se produit : documenter la raison de l’arrêt, sans inventer une seconde scène. Ce point ne guérit pas B1b, qui est une exigence spécialisée effectivement impérative dans son scope. La qualité ne se mesure pas au nombre de détails (234). `Authored` (236) signifie conçu pour le produit, même avec des primitives robustes ; les primitives critiques restent accessibles et fiables. L’origine IA seule ne définit pas le slop (238) ; faible soin, caractère interchangeable, tromperie ou coût de vérification se jugent par la tâche et l’artefact. Enfin ancre, profil, style et présélection `DESIGN-ATLAS` sont des **hypothèses de sélection** : `DECISION-MODIFIED` et `WHEN-USEFUL` n’ont pas le statut d’un `DECISION-CHANGE` constaté après observation (240). La séparation renforce F-ACT-013/028 sans créer une autorité de preuve SAVOIR.

### CFT-01 : matrice et dérivation (242–279)

La matrice (246–253) demande motivation et qualité de construction. Deux « oui » rendent le choix légitime **sous réserve** des gates ; une motivation forte avec mauvaise construction appelle amélioration/simplification ; une bonne construction sans motivation appelle justification située ou retrait ; les deux « non » signalent un slop, mais n’attribuent aucun verdict. Elle est explicitement une heuristique interne, pas une classification scientifique. `ACTION/ANTI-SLOP` (800–802) exige ensuite un élément observé, la relation produit manquante et une sortie correction, retrait, réserve ou retour ; il ne reproduit pas la matrice. « Slop signalé » ne signifie donc pas automatiquement `RETURN` ; ne pas convertir une simple préférence stylistique en faute.

La forme située (261–275) relie tâche, donnée métier, état, densité, métaphore **facultative** et preuve attendue. Elle peut être très simple si le contexte le justifie ; une métaphore n’est pas une obligation de nouveauté. Le test de retrait force à nommer ce que la matière apporte, mais l’appréciation perceptuelle (277) ne devient preuve d’utilisabilité qu’avec tâche, contexte, comportement ou mesure appropriée. La dernière phrase (279) refuse quotas et variantes rituelles tout en laissant `SAVOIR/STATE`, l’accessibilité et les gates d’ACTION applicables.

## Passage C — lecteurs sous contrainte de temps

1. **Designer, identité neuve.** Il transforme le brief en première scène crédible, inspecte l’objet et ses états, puis décrit présence, spécificité et défaut observable. Si tout tient dans le scope, il peut s’arrêter après une seule version ; il ne crée pas une variante purement cérémonielle.
2. **Agent de production, premier objet faible.** Il ne renomme pas le manque « exploratoire » pour le livrer ; il corrige une relation visible ou retourne avec limite, owner et prochaine preuve. Une liste de rationales ne constitue pas une seconde itération.
3. **Reviewer, écran techniquement conforme mais interchangeable.** Il ne déduit ni qualité de composition des tests, ni échec des tests de son goût ; il montre l’objet, la hiérarchie ou la copie interchangeable et réclame une action proportionnée.
4. **Équipe produit, motif de genre commun.** Elle vérifie la motivation de tâche et la construction du motif ; une convention bien adaptée est légitime. Une ressemblance isolée ne suffit pas pour un flag slop.
5. **Intégrateur, variante B1b déclenchée.** Il observe un premier objet fort et pense arrêter. Pourtant ACTION demande une édition réversible et une paire ; même si l’original est finalement conservé, l’édition a été exigée pour prouver une comparaison. Ce cas ne se résout pas en déclarant `N/A` parce que la variante paraît inutile.
6. **Mainteneur, référence utilisée comme preuve.** Il sépare l’hypothèse de sélection pré-build de l’observation post-build, conserve le locator de l’artefact et renvoie à ACTION pour décision effective et fermeture.

## Passage D — résistance et registre

### Contradiction de branche et portée des contrôles

Le scénario décisif est une `DIRECTION` dont le risque V/craft déclaré domine : premier objet réel inspecté, qualité visuelle suffisante, risques applicables couverts, aucune amélioration utile probable. `SAVOIR/CRAFT` ligne 205, `DIRECTION/DOUBLE-LOOP` ligne 502 et `ACTION/PIPELINE-DIRECTION` ligne 453 permettent l’arrêt. `DIRECTION/CREATIVE-BOOT` ligne 184 et `ACTION/GATE-B/B1b` lignes 704–714 exigent quand même une édition et une réobservation si une décision principale reste éditable. ACTION autorise la conservation de l’original après comparaison, ce qui réduit le risque de dégrader le livrable, mais n’enlève pas le coût ni le conflit de condition d’arrêt. **F-DIR-009** demeure le constat de ce mécanisme, avec occurrence B1b déjà établie par le rapport ACTION bloc 10. Le réexamen en phases 4, 7 et 9 devra distinguer le cas où la paire apporte une véritable preuve comparative de celui où l’édition n’ajoute aucune preuve utile, sans transformer un jugement de goût auto-déclaré en dérogation générale.

Le contrôle machine de ce conflit est **déjà documenté** : rapport `Audit_ACTION_Phase2_10_Gate_B_Contextual_Judgment.md`, F-ACT-036 : la `RUN_CARD` avec risque craft dominant et paire B1b absente peut être `ACCEPTED` ; un objet B1b structuré est refusé. Aucun second test identique n’a été lancé dans ce bloc. F-ACT-025 garde séparément le problème du `creative_close.next_polish_action` obligatoire si l’arrêt est approprié ; F-ACT-005/021 concernent la portée de preuve et sa projection. Un validateur vert ne tranche donc pas, à lui seul, la qualité du rendu ni la légitimité du one-shot.

### Occurrences sans nouvel ID

| Observation | Relation et suite |
|---|---|
| Branche one-shot positive face aux obligations de modification | F-DIR-009 ; relire la priorité des scopes et l’arrêt en phases 4 et 7 |
| Paire B1b obligatoire mais invisible dans la projection | F-ACT-036 et F-ACT-002/021 ; test machine antérieur conservé, pas dupliqué |
| `Creative Quality Review` « après la repasse » et champ `next_polish_action` | La méthode peut s’arrêter sans repasse ; F-ACT-025 pour la sortie structurée ; contrôler la formulation en phase 7 |
| Ancres, profils et `DECISION-MODIFIED` ne sont pas preuve post-build | F-ACT-013/028 ; distinguer sélection, observation et changement de décision |
| `SAVOIR/CRAFT/CFT-01` ne se lit pas directement par la CLI | F-DIR-028/F-ACT-001 ; le titre et la route parent restent accessibles |
| Matrice canonique et conséquence ACTION | Propriété bien répartie ; vérifier la trace et le verdict sur motifs conformes, fragiles et artificiels en phase 9 |
| CRAFT peut être utile avec FRAME, TYPE, SOURCE et CONTEXT | F-SAV-001 demeure provisoire ; router selon décisions et risques distincts, sans quota |

### Protections positives à préserver

1. Le premier rendu est une proposition réelle, spécifique et jugeable ; l’exploration n’est pas un permis de livrer volontairement creux.
2. Une qualité visuelle forte, une qualité construite observable et une qualité d’usage prouvée sont des niveaux différents.
3. Le one-shot exige une observation réelle et la couverture des risques, mais autorise l’arrêt quand une correction n’apporte rien.
4. Les dimensions créatives servent à composer, critiquer et retirer ; elles ne forment pas un score esthétique ni un canon stylistique.
5. Une convention adaptée et une forme construite avec des primitives robustes peuvent être pleinement spécifiques au produit.
6. Motivation, construction et preuve ont des rôles séparés ; l’origine IA ou la présence d’une ancre ne décident pas du verdict.
7. Aucune métaphore, variante, nouveauté ou passe de polish ne vaut par sa simple présence ; l’action doit changer une relation ou une preuve.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Route CRAFT, sous-sections CFT-00/01, tags et autorité machine confrontés |
| B — sémantique | FULL | Chaque segment 195–279 examiné : obligation, méthode, heuristique, preuve, arrêt et renvoi |
| C — usage réel | TARGETED | Six scénarios couvrant designer, agent, reviewer, produit, intégrateur et mainteneur |
| D — résistance | TARGETED | One-shot/B1b, revue après passe, slop, localisation canonique et statut des ancres |
| Machine | TARGETED | Route parente OK, locator `CFT-01` refusé, carte de lecture OK ; test B1b déjà documenté, non répété |
| Externe | N/A-JUSTIFIED | Aucun claim extérieur n’est mobilisé comme preuve dans ce bloc |

Bloc 3 terminé **sans nouvel ID** et sans patch. La prochaine unité est **SAVOIR.md, lignes 281–376**, fin de `SAVOIR/CRAFT` : `CFT-02` alternative située, `CFT-03` composition, `CFT-04` émotion et premier contact, `CFT-05` couleur et contraste. `SAVOIR/TYPE` commence à 377. Avant d’y entrer : relire le §12, le présent rapport, les constats pertinents et revalider la baseline.
