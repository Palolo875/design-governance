# Audit ACTION — Phase 2, bloc 9 — Visual Proof et Gate A

## Périmètre examiné

- Source propriétaire : `V1/official/ACTION.md`
- Lignes : 604–688
- Sections :
  - `ACTION/VISUAL_PROOF` ;
  - `ACTION/GATE-A` ;
  - contrat de portée ;
  - familles de méthodes ;
  - adéquation des preuves ;
  - contrôles applicables.
- Interfaces relues : `DIRECTION/VISUAL_TARGET`, `ACTION/PRECONDITION`, `ACTION/RUN_CARD`, `ACTION/STRUCTURED-PROOF`, `ACTION/GATE-B`, `SAVOIR/CONTEXT`, `SAVOIR/TECH`, READING_MAP, schéma et validateur `RUN_CARD`.
- Vérification externe ciblée : W3C WCAG 2.2 Recommendation, WCAG 3 Working Draft et exigences de conformance, état consulté le 22 septembre 2026.
- Limite : lecture de phase 2, sans verdict global et sans patch.

## Baseline et continuité

| Élément | Valeur vérifiée |
|---|---|
| Audit | `DG-AUDIT-001` |
| Baseline | `B01` |
| Hash système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé | ACTION bloc 8, lignes 527–602 |
| Constats ACTION transportés | F-ACT-001 à F-ACT-032 |
| Patches autorisés | Aucun |

Les empreintes correspondent à B01. Le plan maître, le rapport du bloc 8, les quatre passages de la phase 2 et les propriétaires voisins ont été rouverts. La source et le protocole n’ont pas changé.

La suite officielle a été réexécutée :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

Ce PASS confirme l’intégrité de la baseline, pas l’exécution réelle des contrôles du bloc.

## Résumé du bloc

Le bloc possède un très bon noyau épistémique. `VISUAL_PROOF` relie cible, ancre, spec et rendu réel ; déclare le périmètre avant la preuve ; attribue une conséquence aux vues absentes ; et interdit qu’une capture soit confondue avec indépendance, accessibilité complète ou réussite de tâche. `GATE-A` adapte médium, scope, référentiel, échantillon, méthode, budget et limite ; distingue automatisation, inspection manuelle, expertise et utilisateur ; borne tout PASS à sa méthode et à son scope ; exige une provenance minimale pour les verdicts acceptés ; et associe chaque question à une preuve adaptée.

La règle externe sur les standards est correcte au 22 septembre 2026 : WCAG 2.2 reste une W3C Recommendation, tandis que WCAG 3 est encore un Working Draft explicitement instable. Les contrôles ajoutés — focus non masqué, glisser, taille de cible, aide cohérente, saisie redondante et authentification accessible — correspondent bien aux familles introduites par WCAG 2.2.

Trois défauts nouveaux sont isolés. Premièrement, Gate A peut attribuer un PASS à une alternative reduced motion seulement « prévue », donc non implémentée ou testée. Deuxièmement, la règle de provenance exige celle-ci pour les deux verdicts acceptés puis semble autoriser une simple limitation comme alternative, alors que le validateur la refuse. Troisièmement, le contrat ne distingue pas assez explicitement un PASS ciblé sur composant/échantillon d’une claim formelle de conformité WCAG, qui exige pages complètes, processus complets et métadonnées précises.

Les autres faiblesses confirment des constats existants : `VISUAL_PROOF` reste web/desktop/mobile dans sa forme alors que Gate A est multi-médium ; le lecteur ne résout pas cette route ; les axes, résultats de gate et `COVERAGE-LIMIT` ne sont pas transportés comme objets ; une provenance sémantiquement invalide peut encore accompagner `ACCEPTED` ; et un futur `NEXT-PROOF` peut masquer des parties du scope livré non observées.

## Passage A — architecture visible

### Séquence de preuve

Le bloc crée une progression lisible :

1. une première scène significative existe ;
2. le scope de preuve est déclaré ;
3. les vues pertinentes sont capturées ;
4. les absences reçoivent une conséquence ;
5. Gate A déclare médium, cible, échantillon et méthode ;
6. la méthode est choisie selon la question ;
7. les contrôles applicables produisent PASS, retour ou réserve ;
8. la provenance rattache l’observation à un artefact et une version.

Cette séquence corrige partiellement F-ACT-030 : contrairement au bloc « contrats avant build », `VISUAL_PROOF` commence explicitement après disponibilité d’une scène et Gate A déclare le scope avant d’exécuter le contrôle.

### Architecture de VISUAL_PROOF

| Preuve | Objet principal | Conséquence d’absence |
|---|---|---|
| Capture desktop entière | Silhouette, masses, vide, foyer, opération dominante | V `NOT-VERIFIED` |
| Capture mobile entière | Recomposition, voisinage, priorité, action | U/T `NOT-VERIFIED` si mobile est dans le scope/risque |
| Vue de détail | Type, matière, cadrage, état, contenu extrême | `N/A-JUSTIFIED` seulement si aucun détail ne porte la décision |
| Vue de masses | Foyer, poids, vides, foyer parasite | `N/A-JUSTIFIED` si la hiérarchie n’est pas un risque |
| État significatif | Loading, empty, error, focus, contenu long | U/A/T `NOT-VERIFIED` sur l’état absent |
| Comparaison d’écarts | Spec/ancre contre build | `EXPLORATORY` ou `RETURN-DIRECTION` |

La table est compacte et actionnable. Son défaut architectural est l’asymétrie de portée : l’absence de desktop produit toujours V `NOT-VERIFIED`, alors que le mobile est conditionné au scope ou au risque. Une application native mobile, un wearable, une épreuve print ou une scène spatiale n’ont pourtant pas de capture desktop pertinente.

Gate A corrige cette tendance avec `MEDIUM` et un référentiel adapté. Les deux sections voisines n’emploient donc pas encore la même abstraction de support.

### Architecture de Gate A

Gate A se compose de quatre sous-contrats complémentaires :

| Sous-contrat | Rôle |
|---|---|
| Portée | Déclare support, scope, cible, échantillon, méthode, unité, limite et suite |
| Familles de méthodes | Empêche automatisation, expertise et utilisateur d’être interchangeables |
| Adéquation des preuves | Relie la question au moyen d’observation capable d’y répondre |
| Contrôles applicables | Donne les conditions de PASS et les motifs de retour/réserve |

La hiérarchie est cohérente : le bloc ne commence pas par une liste universelle de checks ; il définit d’abord le contexte qui rend un contrôle applicable.

### Résolution des routes

| Locator | Résultat |
|---|---|
| `ACTION/VISUAL_PROOF` | Échec — locator inconnu |
| `ACTION/GATE-A` | Résolu |
| `DIRECTION/VISUAL_TARGET` | Résolu |
| `SAVOIR/CONTEXT` | Échec — locator inconnu |
| `SAVOIR/TECH` | Échec — locator inconnu |

Le gate central est accessible, mais la preuve visuelle et ses deux propriétaires spécialisés ne le sont pas via le lecteur. Cela renforce F-ACT-001 et F-DIR-028 sans créer un ID par route.

## Passage B — contrat sémantique

### VISUAL_PROOF relie intention et artefact réel

La ligne 606 possède une responsabilité claire : confronter la cible, l’ancre et la spec au rendu observé dès qu’une scène significative existe. Elle évite deux erreurs symétriques : valider une intention sans build, ou évaluer un rendu sans retrouver la décision qui l’a produit.

Le scope préalable comprend viewport, états, scènes, contenu, devices et axes. Cette liste couvre correctement ce qui change la représentativité d’une capture. Les éléments hors couverture vont dans `COVERAGE-LIMIT` ou `NEXT-PROOF`.

Le mot « ou » mérite prudence. Une prochaine preuve rend le manque visible, mais elle ne borne pas nécessairement la claim actuelle. Lorsque l’artefact livré inclut une partie non observée, cette partie doit également rester dans la limite ou `proof.not_verified`; sinon un futur test peut être pris pour une simple tâche restante après acceptation. Le test machine confirme cette possibilité, mais elle appartient déjà à F-ACT-005 et F-ACT-021.

### Représentativité des captures

La capture desktop entière vérifie le système de masses et l’opération dominante ; la capture mobile entière vérifie la recomposition. Les vues de détail et de masses ne sont demandées que lorsqu’elles portent une décision. L’état significatif empêche un écran nominal de masquer loading, erreur, focus ou contenu long.

Deux nuances doivent être conservées :

- une capture mobile peut montrer la présence et la priorité d’une action, pas prouver que cette action réussit ;
- une capture desktop n’est pas une preuve universelle de V lorsqu’aucun desktop n’existe dans le médium.

La phrase de clôture protège explicitement la première nuance : rendu, indépendance, accessibilité, tâche, mesure technique et ancre générée restent distincts. La seconde reste ouverte et confirme F-DIR-038 sur la généralisation web/mobile.

### Conséquence des preuves absentes

Le bloc ne transforme pas une vue manquante en PASS. Il emploie :

- `NOT-VERIFIED` lorsque le risque reste applicable mais non observé ;
- `N/A-JUSTIFIED` lorsque la décision ou le risque n’existe réellement pas ;
- `EXPLORATORY` ou `RETURN-DIRECTION` lorsque la comparaison attendue manque.

Cette logique est bonne. La dernière paire mélange cependant verdict global et retour spécialisé dans la colonne d’une preuve locale. Le choix entre exploration et retour dépend du caractère récupérable de la preuve et de la fidélité de direction, mais la table ne formule pas ce test. Ce point renforce F-ACT-010 et F-ACT-027.

### Contrat de portée de Gate A

Le contrat distingue huit dimensions :

| Champ | Valeur produite |
|---|---|
| `MEDIUM` | Support réel et périmètre observé |
| `SCOPE` | Vues, composants, états ou chemins |
| `CONFORMANCE-TARGET` | Référentiel et niveau visé |
| `SAMPLE` | Échantillon ou justification d’exhaustivité |
| `METHOD` | Automated, manual, expert, user ou combinaison |
| `BUDGET-UNIT` | Unité technique adaptée au médium |
| `COVERAGE-LIMIT` | Éléments hors couverture |
| `NEXT-PROOF` | Vérification suivante |

La traduction multi-médium est forte. Le web peut rester implicite seulement si le contexte est sans ambiguïté ; natif, desktop, spatial, print ou embarqué doivent expliciter support, guideline et unité. Cela converge avec `SAVOIR/TECH`.

La condition d’activation est plus étroite que le contenu du gate : le contrat complet est annoncé lorsque accessibilité ou conformité sont dans le périmètre, mais Gate A couvre aussi contenu honnête, stabilité média, budget, performance et états. Un contrôle T sans risque A peut donc ne pas recevoir `MEDIUM`, `SAMPLE` ou `BUDGET-UNIT`. Cette tension renforce F-ACT-004 ; elle ne justifie pas encore un nouveau contrat universel.

### Vérification externe des standards

La règle documentaire est actuelle au 22 septembre 2026 :

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) est une W3C Recommendation, édition publiée le 12 décembre 2024 ; le W3C recommande l’usage de la version WCAG la plus actuelle pour les politiques nouvelles ou révisées ;
- [WCAG 3](https://www.w3.org/TR/wcag-3.0/) est un W3C Working Draft du 10 septembre 2026 ; le document dit explicitement qu’il peut être modifié, remplacé ou rendu obsolète et ne doit pas être cité autrement que comme travail en cours ;
- la [présentation officielle de WCAG 3](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/) le qualifie encore de brouillon incomplet dont les exigences et le modèle de conformité changeront.

Il faut donc préserver la ligne 642 : WCAG 2.2 comme base web par défaut, référentiel adapté hors web, WCAG 3 en veille, et conformité séparée de direction, utilisabilité et positionnement.

### Familles de méthodes

La séparation des quatre méthodes est l’un des meilleurs passages du bloc :

- `AUTOMATED` détecte ce qui est codable ;
- `MANUAL` inspecte clavier, focus, états et structure ;
- `EXPERT` interprète risque et contexte ;
- `USER` observe une expérience réelle avec échantillon, tâche et contexte.

Le tableau empêche trois glissements fréquents : outil vers exhaustivité, expert vers utilisateur et humain vers mesure technique. La section d’adéquation répète correctement qu’une utilisabilité réelle exige utilisateur représentatif, tâche représentative, observation et résultat.

### PASS borné au scope

La ligne 653 est protectrice : un PASS décrit seulement la preuve obtenue par la méthode, le médium et le périmètre déclarés. Il ne devient pas global. Une fonction absente du médium est `N/A-JUSTIFIED`; un équivalent est réellement testé ; une preuve web indisponible devient `NOT-VERIFIED` avec prochaine preuve.

Cette règle atténue F-DIR-038 et protège la pluralité des médiums. Elle ne résout pas son transport : `RUN_CARD` ne possède ni résultat de gate, ni axes V/U/A/T structurés, ni champ `COVERAGE-LIMIT`. Ces objets sont rejetés et doivent vivre dans la trace libre.

### Provenance minimale

Le schéma et le validateur appliquent une protection réelle : `ACCEPTED` et `ACCEPTED-WITH-RESERVATION` exigent `proof.provenance` avec locator, version, méthode et date ; le locator doit correspondre à l’artefact.

Deux limites différentes subsistent :

1. la présence des quatre chaînes ne prouve pas leur sens — « version inconnue », « plan non exécuté » et « date à confirmer » passent même en mode strict ; une date future et une version non reliée passent aussi ;
2. la prose exige la provenance pour les deux verdicts acceptés puis ajoute que, si elle ne peut être établie, « le verdict reste non accepté **ou** la limite est explicitement déclarée ». Le validateur rejette toute acceptation sans provenance, même avec réserve explicite.

La première limite renforce F-ACT-018 et F-ACT-022. La seconde ouvre F-ACT-034 : un lecteur humain peut croire qu’une limitation suffit, alors que la projection contrôlable l’interdit.

### Adéquation question/preuve

La table couvre cinq classes sans prétendre à l’exhaustivité :

| Question | Méthode adaptée | Limite conservée |
|---|---|---|
| Mesure déterministe | Script/test exécuté | Intention visuelle non prouvée |
| Perception | Capture/détail/comparaison | Indépendance non créée |
| Préférence/clarté/contexte | Humain/expert/utilisateur selon risque | Pas mesure technique par défaut |
| Utilisabilité réelle | Utilisateur+tâche+observation+résultat | Pas déductible d’une capture |
| Hypothèse sans runtime | Déclaration structurée | `NOT-VERIFIED` si preuve requise |

Cette matrice converge avec `SAVOIR/TECH` et consolide la frontière du bloc 8 entre risque U et test d’utilisabilité.

### Contrôles applicables

Le tableau combine contrôles classiques et apports WCAG 2.2 : contraste, sémantique, focus, états, contenu réel, stabilité, motion, cibles, couleur, focus non masqué, glisser, aide, saisie et authentification.

Les formulations les plus fortes exigent un résultat : contraste calculé, focus visible et testé, états vérifiés, information compréhensible sans couleur, alternative au glisser existante.

La ligne « Motion réduite » est différente : un PASS est accordé si l’alternative sans mouvement est seulement **prévue**. Or le contrat de motion du bloc 8 et `SAVOIR/MOTION` exigent équivalent, runtime, fallback et capture ; Gate A affirme que PASS décrit une preuve obtenue. Une intention prévue ne satisfait donc pas son propre standard.

Le validateur accepte explicitement : runtime motion indisponible, reduced motion non exécutée, méthode limitée à une capture statique, observation « Gate A PASS » et verdict global `ACCEPTED`. F-ACT-033 isole cette contradiction dans le propriétaire humain ; F-ACT-018 conserve le défaut machine transversal.

### PASS de contrôle et claim de conformité

Gate A autorise un scope de composant, d’état ou de chemin et un échantillon représentatif. C’est adapté à un contrôle ciblé. Une claim formelle WCAG 2.2 suit cependant un contrat différent :

- la conformité porte sur des pages complètes, y compris leurs variations responsive ;
- un processus doit conformer sur toutes ses pages ;
- une claim nomme date, titre/version/URI de la norme, niveau, pages couvertes et technologies utilisées.

Ces exigences figurent dans les sections [5.2.2–5.2.3](https://www.w3.org/TR/WCAG22/#cc2) et [5.3.1](https://www.w3.org/TR/WCAG22/#conformance-claims) de WCAG 2.2.

ACTION dit correctement que `CONFORMANCE-TARGET` est une cible et que PASS reste borné au scope. Il ne dit toutefois pas explicitement qu’un PASS de Gate A sur échantillon ou composant ne doit jamais être présenté comme une claim de conformité WCAG de page, parcours ou produit. Aucun objet de claim formelle n’est accepté dans la projection. F-ACT-035 documente cette frontière à haut risque sans demander que chaque run produise une claim WCAG.

### Scripts et recettes

La dernière phrase est saine : une recette exécutée ne valide pas automatiquement le résultat visuel, produit ou utilisateur. Elle protège contre le raisonnement « outil vert donc produit valide ».

La version de la recette, ses dépendances et son scope restent dans les ressources et la trace ; aucun mapping structuré ne les relie à `proof.provenance.method`. Ce point renforce F-ACT-028 et F-ACT-022, sans exiger que la `RUN_CARD` devienne un manifeste technique complet.

## Contrôles machine ciblés

### Contrôle 0 — suite officielle

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

### Contrôle 1 — routes

```text
ACTION/VISUAL_PROOF     FAIL
ACTION/GATE-A           PASS
DIRECTION/VISUAL_TARGET PASS
SAVOIR/CONTEXT          FAIL
SAVOIR/TECH             FAIL
```

### Contrôle 2 — absence de provenance

```text
verdict = ACCEPTED
proof.provenance absent
Résultat : REJECTED

verdict = ACCEPTED-WITH-RESERVATION
proof.provenance absent
limitations = provenance impossible à établir
Résultat : REJECTED
```

Le validateur choisit l’exigence absolue de la première phrase de la ligne 655 ; il n’implémente pas l’alternative apparente de la seconde.

### Contrôle 3 — provenance présente mais non exécutée

```text
observed = Gate A PASS prévu
not_verified = aucun contrôle exécuté
artifact_version = version inconnue
method = plan de contrôle non exécuté
observed_at = date à confirmer
verdict = ACCEPTED
Résultat normal : ACCEPTED
Résultat --strict : ACCEPTED
```

### Contrôle 4 — date future et version non reliée

```text
observed_at = 2099-12-31
artifact_version = future-version
verdict = ACCEPTED-WITH-RESERVATION
Résultat : ACCEPTED
```

Le locator est raccordé ; date, version et fraîcheur ne le sont pas. F-ACT-022 est confirmé.

### Contrôle 5 — couverture différée

```text
artifact.scope = desktop + mobile + loading + erreur + focus
observed = capture desktop
not_verified = []
next_proof = mobile, loading, erreur et focus plus tard
verdict = ACCEPTED
Résultat : ACCEPTED
```

Le futur `NEXT-PROOF` suffit structurellement, même si le scope livré dépasse le scope observé.

### Contrôle 6 — médium mobile seul

```text
artifact.scope = application native mobile uniquement
observed = capture mobile sur device déclaré
aucune capture desktop
verdict = ACCEPTED
Résultat : ACCEPTED
```

Le résultat machine est raisonnable pour ce médium ; il expose l’instruction humaine trop absolue de la ligne desktop.

### Contrôle 7 — reduced motion seulement prévue

```text
available = capture statique
unavailable = runtime motion + préférence reduced motion + clavier/AT
observed = Gate A PASS, alternative sans mouvement prévue mais non implémentée
not_verified = reduced motion non exécutée
method = inspection d’une capture statique
verdict = ACCEPTED
Résultat : ACCEPTED
```

### Contrôle 8 — transport du gate

```text
Ajout gate_a {medium, scope, target, sample, method,
budget, coverage_limit, next_proof, controls}
Résultat : REJECTED — champ inconnu

Ajout proof.coverage_limit
Résultat : REJECTED — champ inconnu

Ajout axis_results {A: NOT-VERIFIED, T: PASS-WITH-RESERVATION}
Résultat : REJECTED — champ inconnu
```

### Contrôle 9 — claim WCAG formelle

```text
Ajout conformance_claim {date, guidelines, uri, level,
pages, technologies_relied_upon}
Résultat : REJECTED — champ inconnu
```

Ce rejet n’implique pas qu’une claim formelle doive être embarquée dans chaque carte. Il montre seulement qu’elle doit rester un artefact externe distinct et ne pas être inférée d’un PASS de Gate A.

## Passage C — usages simulés

### Direction web avec desktop et mobile

Les deux captures, un détail et un état d’erreur sont disponibles. `VISUAL_PROOF` permet de confronter silhouette, recomposition et état à la cible ; Gate A ajoute contraste, clavier, focus et sémantique. Le chemin est clair et proportionné.

### Application native mobile sans desktop

La capture device et les idiomes tactiles sont pertinents. La ligne desktop produirait littéralement V `NOT-VERIFIED`, alors que Gate A et SAVOIR/TECH autorisent une traduction par médium. Le comportement cohérent est `N/A-JUSTIFIED` pour desktop, jamais l’invention d’un écran desktop.

### Épreuve print

Le medium, le référentiel de lisibilité, l’unité encre/contraste et l’épreuve réelle sont déclarés. Clavier, focus et interaction deviennent non applicables avec justification. Gate A gère correctement ce cas ; `VISUAL_PROOF` devrait parler de vue entière du support plutôt que de desktop.

### Audit automatisé vert

Le script ne trouve aucun défaut. La méthode couvre seulement les règles codées ; inspection manuelle, états, focus et tâche restent distincts. Le bloc interdit correctement un PASS global par glissement.

### Alternative reduced motion conçue mais absente

La maquette prévoit un fallback, mais le runtime ne l’implémente pas. La ligne actuelle peut produire PASS ; le contrat de méthode exige pourtant une exécution. La sortie correcte est `NOT-VERIFIED` ou retour jusqu’au test de l’alternative.

### Checkout échantillonné

Deux composants sont inspectés sur un processus de cinq pages. Le PASS ciblé est légitime pour ces composants ; une claim « checkout conforme WCAG 2.2 AA » ne l’est pas, car le processus complet n’a pas été couvert.

### Provenance non établie

Un reviewer dispose d’une limitation narrative mais ne connaît ni version ni instant de l’artefact. Le texte peut être lu comme acceptation réservée ; le validateur rejette. Deux équipes appliquant deux autorités obtiennent donc des sorties différentes.

### Scope livré plus large que la capture

Le produit inclut mobile et erreurs, mais seul desktop est observé. Une prochaine preuve existe. La trace humaine doit maintenir explicitement U/A/T non vérifiés ; le validateur accepte malgré tout un verdict plein.

## Passage D — constats

### F-ACT-033 — Gate A autorise un PASS reduced motion sur une alternative seulement prévue

- Gravité provisoire : **Majeur provisoire**
- État : **contradiction sémantique et contournement machine confirmés**
- Preuve : ligne 677 accorde PASS lorsqu’une alternative sans mouvement est « prévue » ; lignes 653 et 665 exigent une preuve obtenue et maintiennent sans runtime une hypothèse en `NOT-VERIFIED`; une carte sans runtime ni préférence reduced motion, fondée sur capture statique, obtient `ACCEPTED`
- Comportement observable : un fallback dessiné ou promis est déclaré accessible avant implémentation, activation de la préférence et test du résultat
- Risque : motion imposée à des personnes sensibles, faux PASS d’accessibilité, absence de fallback réel et diffusion d’un claim non exécuté
- Facteur atténuant : le contrat de motion du bloc 8 et `SAVOIR/MOTION` exigent déjà équivalent, interruption, fallback, performance, runtime et capture
- Relations : F-ACT-018, F-ACT-030, F-ACT-021 et F-DIR-038
- Propriétaires pressentis : ACTION/GATE-A pour le prédicat de PASS ; SAVOIR/MOTION pour le comportement attendu ; RUN_CARD/validateur pour la contradiction capacité/claim
- Test futur : préférence active/inactive, alternative prévue/implémentée/testée, interruption, contenu équivalent, capture statique/runtime, device réel et performance

### F-ACT-034 — la règle de provenance hésite entre obligation et limitation compensatoire

- Gravité provisoire : **Significatif**
- État : **divergence prose/validateur confirmée**
- Preuve : ligne 655 exige une provenance pour `ACCEPTED` et `ACCEPTED-WITH-RESERVATION`, puis dit que son absence laisse le verdict non accepté « ou » la limite explicitement déclarée ; le validateur rejette les deux verdicts acceptés sans provenance, même avec limitation
- Comportement observable : un lecteur autorise une acceptation réservée avec provenance absente ; un autre suit le schéma et retourne la carte
- Risque : clôtures incompatibles, confiance excessive dans une limitation narrative ou blocage inattendu d’un run correctement borné
- Facteur atténuant : la règle machine la plus protectrice est claire et possède une fixture négative officielle ; la limitation reste requise même quand la provenance existe
- Relations : F-ACT-009, F-ACT-010, F-ACT-021, F-ACT-022 et F-ACT-023
- Propriétaires pressentis : ACTION/GATE-A pour lever le « ou » ; RUN_CARD et validateur pour conserver une seule règle ; CLOSE-PACKAGE pour la conséquence
- Test futur : provenance complète/partielle/absente × ACCEPTED/ACCEPTED-WITH-RESERVATION/non accepté × limitation spécifique/générique

### F-ACT-035 — un PASS ciblé de Gate A peut être confondu avec une claim formelle WCAG

- Gravité provisoire : **Significatif provisoire**
- État : **frontière de claim insuffisamment explicite**
- Preuve : Gate A accepte scope de composant/état/chemin et échantillon représentatif ; WCAG 2.2 réserve la conformité aux pages complètes et processus complets et impose les métadonnées d’une claim ; aucun contrat ne dit explicitement qu’un PASS ciblé n’est pas une claim de conformité et l’objet formel est rejeté par la projection
- Comportement observable : un PASS sur quelques composants est résumé comme « produit conforme WCAG 2.2 AA » sans couvrir variations responsive, processus complet ou technologies utilisées
- Risque : claim d’accessibilité inexact, exposition réglementaire, exclusion d’états/pages non testés et confusion entre cible, contrôle et conformité
- Facteur atténuant : `CONFORMANCE-TARGET` est nommé cible ; ligne 653 borne PASS au scope ; SAVOIR/TECH dit explicitement qu’une cible ne signifie pas conformité obtenue
- Relations : F-ACT-005, F-ACT-012, F-ACT-021, F-ACT-022 et F-ACT-030
- Propriétaires pressentis : ACTION/GATE-A pour la frontière contrôle/claim ; SAVOIR/CONTEXT pour la décision ; artefact externe spécialisé pour toute claim formelle
- Test futur : composant/page/processus, échantillon/exhaustif, responsive, niveau A/AA/AAA, technologies utilisées, contenu tiers et déclaration partielle

## Mises à jour des constats antérieurs

### F-ACT-001 et F-DIR-028 — routes

`ACTION/GATE-A` et `DIRECTION/VISUAL_TARGET` se résolvent. `ACTION/VISUAL_PROOF`, `SAVOIR/CONTEXT` et `SAVOIR/TECH` échouent. Le run DIRECTION peut donc charger son gate mais pas la preuve visuelle appelée par RUN-DIRECTION ni les propriétaires qui adaptent accessibilité et médium.

### F-ACT-002 — mapping commun

`MEDIUM`, `CONFORMANCE-TARGET`, `SAMPLE`, `BUDGET-UNIT`, `COVERAGE-LIMIT`, résultats de contrôles et axes ne possèdent pas de mapping structuré. La trace externe est légitime, mais la relation avec `artifact.scope`, `proof`, `closure.limitations` et `next_proof` reste implicite.

### F-ACT-003, F-ACT-010 et F-ACT-027 — registres

La table VISUAL_PROOF mélange statuts d’axe, verdict global et retour spécialisé dans une même colonne. Les contrôles parlent de « retour ou réserve » sans préciser le registre cible. Le texte protège la séparation globale, mais la conséquence locale reste à mapper.

### F-ACT-004 — activation conditionnelle

Gate A dit exécuter uniquement les contrôles applicables, ce qui est proportionné. Son contrat de portée est toutefois déclenché seulement par accessibilité/conformité alors qu’il contient aussi budget, performance, média, contenu et états T. Le déclencheur CONTEXT/TECH reste incomplet.

### F-ACT-005, F-ACT-012 et F-ACT-021 — scope et clôture

Une carte dont le scope livré couvre desktop, mobile et états peut observer seulement desktop, placer le reste dans `NEXT-PROOF`, laisser `not_verified` vide et obtenir `ACCEPTED`. La phrase humaine borne le PASS ; la projection ne raccorde pas scope livré, scope observé, axes et verdict.

### F-ACT-007 et F-ACT-014 — vocabulaire de preuve

Le bloc emploie correctement `NOT-VERIFIED` pour une preuve requise absente et `N/A-JUSTIFIED` pour une vraie non-applicabilité. `NOT-OBSERVED` n’apparaît pas ici. Les axes restent dans la trace, tandis que `coverage_map` conserve sa taxonomie parallèle.

### F-ACT-008 — couverture des validateurs

La fixture officielle protège l’absence totale de provenance. Elle ne couvre pas provenance explicitement non exécutée, date future, version inconnue, contradiction capability/claim, scope non observé ou reduced motion seulement prévue. Le PASS global ne teste donc pas les résistances sémantiques de ce bloc.

### F-ACT-018 — capacité et claim

Une validation stricte accepte une méthode « plan non exécuté » et une observation PASS, bien que le même document indique l’absence d’exécution. Une capture statique peut soutenir un PASS reduced motion. F-ACT-018 est fortement renforcé.

### F-ACT-022 — fraîcheur

Locator et présence des quatre champs de provenance sont bien contrôlés. Date future, libellé non daté, version inconnue et absence de raccord à la version livrée passent encore. Le bloc confirme la base utile et la lacune de fraîcheur.

### F-ACT-030 — plan et résultat

VISUAL_PROOF réduit l’ambiguïté en commençant après une scène réelle. Gate A la réintroduit localement avec « alternative prévue » comme condition de PASS. F-ACT-033 est la conséquence accessibilité spécifique ; F-ACT-030 reste le défaut temporel transversal.

### F-DIR-038 — web/mobile apparemment universel

Gate A atténue nettement le constat par `MEDIUM`, référentiel adapté, unité de budget et équivalent testé. VISUAL_PROOF maintient toutefois desktop obligatoire et mobile conditionnel. Le constat devient plus précisément localisé à la preuve visuelle, pas à Gate A dans son ensemble.

## Éléments conformes à préserver

1. La preuve visuelle commence sur un artefact significatif réellement disponible.
2. Cible, ancre, spec et rendu restent reliés.
3. Viewport, états, scènes, contenu, devices et axes sont déclarés avant jugement.
4. Une vue absente reçoit une conséquence et non un PASS silencieux.
5. Détail et vue de masses restent conditionnels à une décision ou un risque réel.
6. Loading, empty, error, focus et contenu long comptent comme états significatifs.
7. Une capture prouve le rendu dans son scope, pas une tâche ni une accessibilité complète.
8. Un regard humain fournit un avis situé, pas une mesure technique par défaut.
9. Un asset généré peut être une ancre, jamais la preuve du rendu final.
10. Gate A exécute uniquement les contrôles applicables.
11. Le médium, le scope, la cible, l’échantillon, la méthode, l’unité, la limite et la suite sont séparés.
12. Les référentiels non web sont adaptés au support réel.
13. WCAG 2.2 reste la base web actuelle par défaut ; WCAG 3 reste en veille.
14. Conformité, direction visuelle, utilisabilité et positionnement ne se valident pas mutuellement.
15. Automatisation, manuel, expertise et utilisateur ont des capacités et limites distinctes.
16. Un PASS reste borné à sa méthode, son médium et son scope.
17. Une fonction inexistante dans le médium reçoit une non-applicabilité justifiée.
18. Un équivalent de médium est testé, pas seulement nommé.
19. Une preuve indisponible reste `NOT-VERIFIED` avec prochaine preuve.
20. Locator, version, méthode et date sont exigés pour les verdicts acceptés.
21. La provenance n’est pas présentée comme preuve de vérité ou de qualité.
22. Mesure déterministe, perception, préférence, tâche et hypothèse reçoivent des preuves différentes.
23. L’utilisabilité réelle exige utilisateur, tâche, contexte, observation et résultat.
24. Contraste, focus, états et alternatives sont évalués sur des résultats observables.
25. Le contenu de remplissage trompeur ne peut pas soutenir un PASS.
26. Les critères WCAG 2.2 récents sont présents dans la table de contrôle.
27. Une recette exécutée ne prouve ni design, ni produit, ni usage à elle seule.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Séquence, deux sections, quatre sous-contrats et routes examinés |
| B — Contrats | FULL | Scope, vues, méthodes, provenance, adéquation, contrôles et standards analysés |
| C — Usage | TARGETED | Huit scénarios web, mobile, print, outil, motion, WCAG, provenance et couverture simulés |
| D — Résistance | FULL | Trois nouveaux constats et dix-sept familles antérieures consolidés |
| Contrôles machine | FULL ciblé | Routes, provenance, strict, fraîcheur, scope, medium, motion, gate, axes et claim testés |
| Vérification externe | TARGETED | Statut WCAG 2.2/3 et exigences de claim contrôlés sur sources W3C |

## Point de passage

Le bloc 9 d’ACTION est entièrement lu. Sa structure de preuve est globalement forte et sa politique de standards est actuelle. Les corrections futures devront rester chirurgicales : rendre le support de VISUAL_PROOF réellement multi-médium, remplacer l’intention « prévue » par une alternative implémentée et testée, lever l’ambiguïté de provenance et protéger la frontière entre PASS ciblé et conformité formelle. Aucun patch n’est autorisé à ce stade.

La prochaine unité est `ACTION.md`, lignes 690–773 : `ACTION/GATE-B`, comparaison relationnelle, B1b, atelier d’édition, familles de preuve, regard externe, corrections ancrées, trace d’assets, statut de direction et sortie compacte. Elle devra vérifier le déclencheur B1b, la nécessité d’une paire de captures, l’équivalence d’une paire réutilisée, la frontière auto-comparaison/revue indépendante, le mapping des différences acceptées et la proportionnalité du format compact.
