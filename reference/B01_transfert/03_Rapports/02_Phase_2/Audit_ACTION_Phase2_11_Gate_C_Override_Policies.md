# Audit ACTION — Phase 2, bloc 11 — Gate C, exception et politiques

## Périmètre et continuité

- Source propriétaire : `V1/official/ACTION.md`, lignes 775–868.
- Sections : `ACTION/GATE-C` (775–794), `ACTION/ANTI-SLOP` (798–802), `ACTION/OVERRIDE` (806–836) et `ACTION/POLICIES` (840–866).
- Interfaces relues : blocs ACTION 1–10, surtout `STATUS`, `PRECONDITION`, `RUN_CARD`, `CLOSE-PACKAGE`, Gate A/B et B1b ; `SAVOIR/CRAFT/CFT-01`, `SAVOIR/CONTEXT`, `SAVOIR/TOOLS`, `DIRECTION` absolus 2/3, BIBLIOTHEQUE composants, schéma, validateur, fixtures et carte de routes.
- Vérification externe ciblée : WCAG 2.2, documentation W3C d’application aux TIC non web et documentation du projet APCA. Aucune conclusion juridique n’est inférée.
- Profil : `DEEP`, profondeur ciblée sur les contrats et scénarios de résistance ; pas de verdict global ni de patch du système.

| Élément | État vérifié |
|---|---|
| Audit et baseline | `DG-AUDIT-001` — `B01` |
| Hash du système | `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` |
| Hash du protocole | `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` |
| Dernier bloc terminé avant lecture | ACTION bloc 10, lignes 690–773 |
| Constats ACTION repris | F-ACT-001 à F-ACT-037 |
| Patches système | Aucun |

Le plan maître, le rapport du bloc 10, le checkpoint DIRECTION et les quatre passages de la phase 2 du protocole ont été revérifiés. Les deux empreintes B01 n’ont pas bougé. La suite officielle de la baseline termine :

```text
FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité
```

Ce PASS est limité aux contrôles existants. Il ne démontre pas la qualité visuelle, la permission d’un override ni la fraîcheur d’un claim.

## Synthèse sectionnelle

Le bloc protège une qualité positive concrète : Gate C juge le rendu réel et non la justification ; ses six critères demandent une relation au produit, une typographie choisie, une composition, une densité, une profondeur ou planéité intentionnelle et une difficulté réellement résolue. `ANTI-SLOP` laisse la matrice à SAVOIR et vérifie les conséquences, sans interdire a priori un style ou une couleur de marque. `POLICIES` sépare calcul de contraste, mesure APCA complémentaire et inspection humaine ; elle prévoit une baseline d’états proportionnée aux composants critiques.

Le défaut le plus sensible concerne `FAIL-ASSUMED`. La prose n’autorise qu’une diffusion temporaire demandée par un utilisateur après **échec connu**, documenté, assigné et retestable, et exclut les risques graves ou critiques. La projection accepte pourtant cette issue sans preuve d’échec, sans demande, sans scope ni review date, et même lorsqu’un risque critique de sécurité possède une `critical_protection.failure_action = BLOCKED`. Un second problème indépendant est la sortie : `FAIL-ASSUMED` peut accompagner indistinctement les quatre verdicts globaux non acceptés, sans représenter expressément « diffusion limitée autorisée ». Deux nouveaux constats provisoires, F-ACT-038 et F-ACT-039, isolent respectivement la protection d’entrée et la disposition finale.

Les autres tests confirment les constats déjà ouverts : Gate C et ses C1–C6 ne sont ni transportés ni opposables, un PASS de contraste obtenu seulement à l’œil peut accompagner `ACCEPTED`, une ressource périmée ne bloque pas son claim et une baseline d’états critiques peut manquer à une clôture SYSTÈME. L’objectif de phase 11 sera de raccorder les décisions essentielles sans transformer le jugement créatif en un formulaire universel.

## Passage A — architecture visible

### Enchaînement et propriété

| Bloc | Propriétaire de quoi ? | Sortie ou conséquence |
|---|---|---|
| Gate C | Jugement perceptuel sur le rendu et son scope | Élément observé par critère, retour si défaut bloquant ou convergence de faiblesses |
| ANTI-SLOP | Application au rendu de la matrice de SAVOIR | Correction, retrait, réserve ou retour |
| OVERRIDE | Exception humaine à un échec connu, sous limites strictes | Issue `FAIL-ASSUMED`, diffusion bornée, mémoire et réexamen |
| Péremption | Validité temporelle d’un claim, outil ou ressource utilisée | Revue à échéance ou prochaine utilisation |
| POLICIES | Calcul de contraste et moyens d’inspection | Mesure applicable, qualification des outils, baseline d’états |

La hiérarchie est plutôt saine : SAVOIR possède la méthode de jugement et les ressources ; ACTION possède l’observation, la décision et la clôture ; le gate d’accessibilité reste distinct de la qualité perceptuelle. L’override est une exception à la livraison normalement protégée, pas un quatrième gate et pas un PASS.

### Résolution des locators

| Locator | Lecteur livré |
|---|---|
| `ACTION/GATE-C` | Échec |
| `ACTION/ANTI-SLOP` | Échec |
| `ACTION/OVERRIDE` | Échec |
| `ACTION/POLICIES` | Échec |
| `SAVOIR/CRAFT` | Résolu |
| `SAVOIR/TOOLS` | Échec |
| `ACTION/RUN-DIRECTION` | Résolu |
| `ACTION/CLOSE-PACKAGE` | Résolu |

Ces sections existent et se retrouvent en lecture du propriétaire, mais leurs noms ne sont pas des clés du lecteur `read_route.py`. Cette lacune renforce F-ACT-001 et F-DIR-028. Le segment `SAVOIR/CRAFT/CFT-01` est une section propriétaire interne, atteignable par lecture de SAVOIR mais non une route directe reconnue par ce lecteur.

## Passage B — contrats sémantiques, phrase par phrase

### Gate C — activation, preuve et scope (775–783)

L’activation est proportionnée : obligatoire en DIRECTION, ciblée sur le risque craft en STANDARD, limitée à la zone touchée en ITER, hors scope en LITE si le craft ne change pas. Elle rencontre toutefois une frontière déjà relevée au bloc 4 : un micro-delta LITE modifiant précisément le craft n’est pas routé explicitement vers Gate C ou reclassé en ITER. Les deux lectures restent possibles.

La ligne 779 exige une capture réelle et interdit tout jugement C sans runtime ou capture. Elle protège contre un PASS déduit d’un texte ou d’un artefact attendu. La ligne 781 réutilise la paire B1b quand elle existe, sans exiger une seconde comparaison artificielle. La ligne 783 demande viewport, état, scène, contenu et élément observé. C’est le bon contrat de représentativité, particulièrement pour des états d’erreur, mobiles et contenus longs.

Mais `RUN_CARD` n’a aucun objet Gate C ni résultat de critère. Une carte avec runtime/capture indisponibles et observation textuelle « C1–C6 PASS sur rendu réel » est validée `ACCEPTED` ; de même si C6 est explicitement absent et bloquant. Un objet `gate_c` avec statut, scope, capture et critères est rejeté. Cela renforce F-ACT-002, 005, 012, 018 et 021, sans nouveau constat pour la même cause de transport.

### Six critères (785–794)

- C1 : la photo, donnée, lumière, surface, trame ou planéité doit découler du produit ; pas de peau par défaut.
- C2 : choix de famille, rôles, échelle et fallback typographique au service du contexte ; une font choisie n’est pas une justification suffisante.
- C3 : la structure de lecture soutient action et rythme ; l’empilement uniforme est un signe à examiner, pas un interdit absolu.
- C4 : densité et espace protègent les priorités ; cela évite le vide ou la densité automatique.
- C5 : profondeur **ou planéité** peut réussir ; il ne faut pas imposer ombres ou effets.
- C6 : une difficulté locale est résolue par état, texte, donnée, interaction, asset ou transition pertinente, au-delà de l’assemblage.

Chaque verdict cite un élément concret. Un critère bloquant absent ou plusieurs signaux faibles convergeant sur le même risque impose un retour à direction, spec ou build, jamais un effet décoratif terminal. À clarifier en phase 4 : la case C5 propose `N/A-JUSTIFIED` quand « la planéité est intentionnelle et suffisante », alors que cette situation semble précisément satisfaire la branche positive du critère. Une vraie N/A viserait l’absence d’enjeu de profondeur/planéité dans le scope ; utiliser N/A pour une planéité réussie masque une décision réellement jugée. C’est une observation locale sans ID nouveau.

### ANTI-SLOP — source et conséquence (798–802)

La matrice canonique `SAVOIR/CRAFT/CFT-01` distingue motivation et construction, et reste une heuristique située, non une loi scientifique. ACTION ne la duplique pas. Quand l’une manque, le gate doit nommer le motif observé, la relation produit/lecture absente et la sortie. Une construction soignée sans motivation n’est pas automatiquement légitime ; une intention déclarée sans réalisation n’est pas suffisante non plus.

La seconde phrase empêche la couleur de marque, une contrainte réelle ou une réalisation technique soignée de neutraliser les autres gates. Inversement, watchlists et tendances restent des signaux contextuels et non des bannissements universels. C’est une protection précieuse contre un audit qui ne ferait qu’uniformiser l’esthétique.

Le mapping de sortie reste textuel : correction, retrait, réserve et `RETURN` ne portent pas la même autorité. La trace peut les conserver, mais la `RUN_CARD` ne représente ni le motif/critère, ni le résultat du gate, ni le lien à V/U/A/T. Cela met à jour F-ACT-002, 010, 012, 021 et 027.

### FAIL-ASSUMED — échec connu et demande explicite (806–814)

La condition humaine est stricte : demande d’un utilisateur, échec **connu**, risque documenté, owner, caractère retestable, diffusion **limitée**. Une preuve impossible ou un simple `NOT-VERIFIED` n’est pas un échec connu. Le FAIL reste FAIL, sans promotion en PASS.

`DIRECTION` déclare pourtant qu’en l’absence d’ancre fraîche et utile sur une surface identitaire, les axes visuels deviennent `NOT-VERIFIED` et la livraison validée est bloquée « sauf `FAIL-ASSUMED` ». Son autre absolu ajoute que l’override ne masque jamais une preuve absente ; `SAVOIR/CONTEXT` dit expressément que `FAIL-ASSUMED` ne masque pas une indisponibilité de runtime. Il faut concilier ces phrases : une ancre ou preuve **absente**, sans échec observé, ne suffit pas à déclencher l’exception. Ce conflit réactive F-DIR-027 et F-ACT-010 ; F-ACT-038 cible l’entrée dangereuse de l’override ACTION.

### Journal d’exception et exclusions (812–828)

La ligne de journal réclame gate/axe, mesure ou preuve, date, risque, scope de diffusion, owner, retest. Les cinq lignes suivantes ajoutent `SCOPE`, `IMPACT`, `REVIEW-DATE`, `NEXT-PROOF`, `EXIT-CONDITION`. La répétition de scope est acceptable si le premier scope désigne la diffusion et le second le contrôle, mais cette distinction n’est pas formulée ; sinon elle risque la double saisie divergente.

Les interdictions sont justes : sécurité, dommage grave, conformité critique ou action essentielle trompeuse/dangereuse ne sont pas rendus livrables par consentement à l’échec. Les risques à fort impact sont rappelés ; l’exception est re-présentée à la prochaine modification du même périmètre. Cela distingue autorisation ponctuelle et dérogation permanente.

Le test isolé est contraire au contrat : en mode STANDARD, `issue=FAIL-ASSUMED`, `state=CLOSED`, `verdict=RETURN`, `limitations=[]`, un échec connu déclaré, mais aucune demande utilisateur, scope, impact, date de revue ni condition de sortie : la carte passe. Une autre carte sans aucune observation et avec `proof.not_verified` signifiant « résultat inconnu » passe aussi. Enfin `risk.level=critical`, `critical_protection.failure_action=BLOCKED` et observation d’un échec de sécurité en production passent avec cette issue. Le validateur n’a ici protégé que la présence formelle de `critical_protection` et l’interdiction de l’associer à un verdict accepté. F-ACT-038 distingue cette lacune spécialisée du problème plus général de F-ACT-017/023.

### Disposition d’une diffusion limitée (806–828)

`STATUS` définit `FAIL-ASSUMED` comme échec connu **diffusé** dans un scope temporaire. Or `closure.verdict` est requis, mais sa liste ne contient que acceptation, acceptation réservée, retour, retour de direction, exploration ou escalade. Le validateur rejette, à juste titre, `ACCEPTED` et `ACCEPTED-WITH-RESERVATION` avec `FAIL-ASSUMED`. Il accepte toutefois les quatre autres verdicts (`RETURN`, `RETURN-DIRECTION`, `EXPLORATORY`, `SYSTEM-ESCALATION`) avec la même issue et `CLOSED`, sans dire si l’artefact a effectivement été diffusé sous dérogation, seulement retourné, ou escaladé **sans** diffusion.

`CLOSED` signifie persistance, non autorisation de diffusion. La trace externe pourrait conserver l’action réelle, mais aucun mapping canonique ne rend cette décision lisible dans la projection. Il ne s’ensuit pas qu’il faille nécessairement ajouter un septième verdict : un champ de disposition distinct, ou une convention de projection vérifiable, pourrait suffire. Ce manque spécifique est F-ACT-039, en lien avec la matrice générale F-ACT-010.

### Péremption et dépendance réelle (830–836)

La revue d’un claim ou outil périmé ne s’active que si le livrable en dépend. Un fix sans rapport n’est pas bloqué, mais la prochaine réutilisation ne peut reconduire silencieusement une source périmée. La trace conserve type, source, version, vérification, scope, limite, owner, review date et prochaine preuve. Une réserve périmée conserve impact et condition de clôture.

Cette proportionnalité est bonne. La projection n’a ni référence qualifiée de claim, ni date de revue, ni dépendance claim → livrable ; elle accepte un verdict plein dont `sources` et `proof.observed` disent ouvertement qu’une norme et un outil sont périmés. Un objet `external_claim` structuré est rejeté. Cela étend F-ACT-019, 022, 023 et 028 ; le contrôle local n’impose pas de dater universellement chaque fix.

### Politique de contraste et statut des méthodes (840–848)

La règle distingue correctement calcul de contraste du jugement à l’œil. Selon le [texte normatif WCAG 2.2](https://www.w3.org/TR/WCAG22/#contrast-minimum), le critère 1.4.3 s’exprime en ratios calculés ; le [guidage W3C pour les TIC non web](https://www.w3.org/TR/wcag2ict-22/) détaille la transposition de plusieurs critères, sans rendre tous les supports identiques. Les sources ont été ouvertes le 22 septembre 2026.

Le projet [APCA](https://git.apcacontrast.com/documentation/) dispose de sa méthode et de ses variantes documentées ; cela n’en fait pas, par déduction, un remplacement du ratio que WCAG 2.2 exige lorsqu’il s’applique. Le texte ACTION conserve justement APCA comme mesure complémentaire avec contexte, version et limite.

La phrase « selon WCAG 2.2 et le référentiel applicable lorsque ce référentiel s’applique » laisse une portée grammaticale incertaine pour print, natif ou spatial : Gate A fournit déjà le principe supérieur de référentiel adapté au médium. Une prochaine consolidation peut clarifier cette traduction sans supprimer le calcul sur les surfaces où un critère de contraste s’applique. La projection accepte néanmoins `ACCEPTED` avec `available=capture`, `unavailable=calcul de contraste`, `observed=WCAG PASS à l’œil` et méthode d’inspection visuelle. C’est F-ACT-018/033/035 et non une nouvelle règle de contraste à inventer.

### Inspection, ressources et baseline d’états (850–866)

L’inspection externe est complémentaire ; choix d’outil par environnement, documentation, version et owner. Une commande simplement citée n’est pas exécutée aveuglément. Pour une ressource **maintenue**, stack/version, date de vérification, capacité, fallback, limites, owner et prochaine revue sont exigés. Le qualificatif « maintenue » empêche raisonnablement d’imposer ce paquet à chaque micro-fix.

L’automatisation n’est pas assimilée à un jugement perceptuel ni à un test utilisateur. Une baseline d’états pertinents est demandée pour composants critiques : variante, thème, viewport, contenu long, loading, empty, error, focus selon le risque. Une capture versionnée avec revue explicite est une voie proportionnée même sans pipeline de stories.

La carte SYSTÈME acceptée avec observation du seul état nominal, états critiques non vérifiés et aucune baseline versionnée confirme F-ACT-015, 021 et 031. L’effet de la baseline devrait être relié à l’état, la version et le critère de compatibilité ; il ne faut pas forcer une solution outillée lourde pour une preuve visuelle de portée limitée.

## Contrôles machine ciblés

Script local de résistance : `audit_work/test_action11_craft_override_policies.py`. Les cas n’éditent pas le corpus.

| Cas | Résultat du validateur | Lecture |
|---|---|---|
| DIRECTION : Gate C PASS sans runtime ni capture | `ACCEPTED` | Claim perceptuel non opposable |
| C6 bloquant absent avec verdict plein | `ACCEPTED` | Gate ne gouverne pas la clôture |
| Objet `gate_c` avec scope, capture, critères | Rejet : champ inconnu | Trace externe nécessaire |
| LITE avec changement de craft sans Gate C | `ACCEPTED` | Activation LITE/ITER à clarifier |
| `FAIL-ASSUMED` fermé sans autorisation, scope, date, review, limitation | `ACCEPTED` | Contrat de journal non contrôlé |
| Même issue + chacun des quatre verdicts non acceptés | Quatre fois `ACCEPTED` | Disposition limitée non déterminée |
| `FAIL-ASSUMED` pour résultat inconnu, aucune observation | `ACCEPTED` | Échec connu confondu avec preuve absente |
| `FAIL-ASSUMED` sur échec de sécurité critique avec action `BLOCKED` | `ACCEPTED` | Exclusion explicite non contrôlée |
| Claim et outil déclarés périmés + verdict plein | `ACCEPTED` | Revue de dépendance non opérante |
| Objet de claim qualifié | Rejet : champ inconnu | Mapping trace nécessaire |
| `WCAG PASS` déclaré par inspection visuelle seule | `ACCEPTED` | Capacité/méthode/claim non raccordés |
| Composant critique sans baseline des états sensibles | `ACCEPTED` | Risque de faux négatif de régression |

Contrôles positifs à préserver : la fixture officielle rejette `FAIL-ASSUMED + ACCEPTED-WITH-RESERVATION` et le validateur rejette un risque `critical` sans objet `critical_protection`. Dans le scénario critique ci-dessus, une protection structurée existe, mais sa propre action `BLOCKED` ne régit pas l’issue. La suite officielle passe ; elle n’inclut pas ces résistances sémantiques.

## Passage C — usages réels simulés

1. Designer DIRECTION sans capture : peut décrire une intention, mais Gate C demeure `NOT-VERIFIED`; la carte peut néanmoins porter une auto-claim « PASS » et fermer.
2. Designer ITER qui change seulement le cadrage d’un asset : Gate C juge la zone touchée et réutilise une paire B1b si son scope s’applique, sans recommencer les six critères sur tout le produit.
3. Micro-fix LITE de densité visuelle : PRECONDITION ne charge pas C, Gate C exclut LITE seulement quand le craft est intact. Le lecteur rapide hésite entre C ciblé et reclassification ITER.
4. Reviewer d’un composant plat et très bien résolu : C5 est positif par planéité assumée ; l’étiqueter N/A ferait disparaître le jugement réellement porté.
5. Producteur face à un défaut cosmétique connu, demande utilisateur explicite et diffusion pilote : override peut être légitime, à condition de conserver autorisation, périmètre, date et retest sans proclamer PASS.
6. Producteur sans runtime : absence de résultat n’est pas échec connu ; DIRECTION suggère localement l’exception pour ancre absente, alors que le propriétaire OVERRIDE et SAVOIR la réservent à un échec réel.
7. Produit critique avec défaillance de sécurité et `failure_action=BLOCKED` : le texte interdit la production ; la projection laisse fermer `FAIL-ASSUMED + RETURN` comme si cette protection n’agissait pas.
8. Mainteneur reprenant un claim de contraste périmé : sa réutilisation déclenche revue ; un fix sans rapport ne devrait pas être bloqué. Sans lien de dépendance, le validateur ne distingue pas les deux.
9. Équipe sans pipeline de screenshots : capture versionnée et revue explicite des états critiques peuvent suffire proportionnellement ; un seul screenshot nominal ne couvre pas focus ou erreur.

## Passage D — constats nouveaux

### F-ACT-038 — `FAIL-ASSUMED` accepte une absence de preuve ou un risque explicitement exclu

- Gravité provisoire : **Majeur provisoire**.
- État : contradiction humain/machine confirmée par mutations isolées.
- Preuve : ACTION 810–828 exige demande utilisateur, échec connu, diffusion limitée, journal assigné et retestable, et exclut sécurité/dommage grave/conformité critique/action essentielle dangereuse ; des cartes sans observation ni autorisation ou avec risque critique et `failure_action=BLOCKED` passent.
- Comportement : `NOT-VERIFIED` est requalifié en échec assumé, ou un défaut prohibé est diffusé malgré le contrôle censé le bloquer.
- Risque : publication dangereuse, exception permanente faute de review, faux consentement, perte d’owner et contournement de la protection critique.
- Atténuation : `FAIL-ASSUMED` avec verdict accepté est déjà rejeté ; risque critique sans objet de protection est rejeté ; le contrat humain exclut ces cas sans ambiguïté.
- Relations : F-ACT-010, 012, 017, 018, 023, 026 et F-DIR-027.
- Propriétaires pressentis : ACTION/OVERRIDE pour la condition d’entrée et la distinction échec/preuve absente ; ACTION/AUTHORITY pour l’autorisation ; schéma/validateur pour les contraintes déterministes, trace pour preuve d’autorisation et re-présentation.
- Test futur : échec observé/inconnu × utilisateur autorisant ou non × risque normal/important/critique et catégorie exclue × protection `BLOCKED`/`ESCALATED` × scope, owner, revue et retest présents/absents.

### F-ACT-039 — la diffusion limitée autorisée n’a pas de disposition finale non ambiguë

- Gravité provisoire : **Significatif provisoire**.
- État : défaut de mapping de décision confirmé ; la solution exacte reste à trancher en phase 4/11.
- Preuve : STATUS 139–150 et OVERRIDE 810 décrivent une diffusion limitée effectivement effectuée ; `closure.verdict` n’a pas cette valeur et reste obligatoire ; le validateur exclut à raison les verdicts acceptés mais autorise `FAIL-ASSUMED + CLOSED` avec chacun de `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` et `SYSTEM-ESCALATION`.
- Comportement : les consommateurs ne savent pas si un run fermé a diffusé un artefact sous dérogation, s’il a seulement retourné un défaut, ou s’il a escaladé avant toute diffusion.
- Risque : tableau de bord, relais d’équipe ou automatisation envoie un artefact non autorisé, ou interrompt à tort un pilote autorisé ; le statut d’exception est pris pour un verdict.
- Atténuation : `CLOSED` signifie seulement trace persistée, et une trace externe peut documenter la réalité de l’action ; la protection contre `ACCEPTED` existe.
- Relations : F-ACT-003, 010, 021, 023 et 038 ; distinct de F-ACT-038 qui porte la légitimité de l’exception, non son résultat.
- Propriétaires pressentis : ACTION/STATUS et OVERRIDE pour le sens de disposition ; RUN_CARD/trace pour son transport et sa relation à l’issue.
- Test futur : exception autorisée mais non diffusée/diffusée puis retirée/diffusée temporairement/escaladée ; état DECIDED/CLOSED ; verdicts acceptés et non acceptés ; reprise après review date.

## Mises à jour du registre existant

- F-ACT-001 et F-DIR-028 : quatre sections ACTION de ce bloc et `SAVOIR/TOOLS` ne sont pas des routes directes ; leurs titres existent.
- F-ACT-002, 005, 012, 018, 021 : Gate C et ses six critères sont matériellement pertinents mais restent hors projection ; PASS sans capture et C6 bloquant accepté démontrent à nouveau l’absence de lien preuve → axe → verdict.
- F-ACT-003, 010, 027 : ANTI-SLOP mélange conséquences locales (correction/retrait/réserve) et verdict global `RETURN` sans mapping suffisant ; F-ACT-039 isole la disposition d’override.
- F-ACT-001 et 021 : un LITE dont le craft change peut manquer l’activation de Gate C dans la route courte ; C5 emploie N/A pour une planéité intentionnelle réussie. Ce dernier point reste une observation locale.
- F-ACT-008 : les fixtures officielles contrôlent une incompatibilité de verdict mais pas l’entrée ni les exclusions de l’override ; les tests locaux fournissent les contre-exemples.
- F-ACT-017, 023 : `critical_protection.failure_action=BLOCKED` n’interdit pas `FAIL-ASSUMED`; la réserve/exception n’a pas de cycle d’owner, revue et sortie opposable.
- F-ACT-019, 022, 028 : source périmée, version d’outil et dépendance du livrable restent libres ; les contrôles de fraîcheur n’activent pas une revue sur réutilisation.
- F-ACT-024 et 026 : la demande de l’utilisateur n’est pas sérialisée comme autorisation bornée ; elle ne pourrait de toute façon primer sécurité, dommage grave ou conformité critique.
- F-ACT-031 : baseline d’états et versions restent nécessaires à une véritable claim de non-régression, sans imposer un pipeline universel.
- F-ACT-033 et 035 : un PASS de contraste calculé doit être distingué d’un fallback simplement prévu et d’une claim formelle de conformité.
- F-ACT-036 : Gate C réutilise explicitement la paire B1b au lieu de l’exiger deux fois ; la paire demeure non transportée.
- F-DIR-027 : absence d’ancre produit `NOT-VERIFIED`, pas échec observé ; l’exception apparente de l’absolu 2 doit être confrontée à ACTION/OVERRIDE et SAVOIR.

## Protections positives à préserver

1. Gate C dépend du mode et du risque, pas d’un quota universel de contrôles.
2. Un jugement de craft ne vient pas d’un texte sans capture.
3. B1b est réutilisé, pas réexécuté rituellement.
4. Viewport, état, scène, contenu et élément concret bornent le verdict C.
5. Surface, type, composition, densité, profondeur/planéité et résolution située exigent des décisions perceptibles.
6. La planéité intentionnelle vaut autant que la profondeur lorsqu’elle sert l’objet.
7. Un critère bloquant ou une convergence de faiblesses entraîne un retour, sans compensation décorative.
8. La matrice motivation/construction appartient à SAVOIR et reste une heuristique située.
9. Ni tendance, ni couleur de marque, ni sophistication technique ne décide seule du gate.
10. Un échec assumé reste un échec, demandé et limité dans le temps et le scope.
11. Les risques graves ou critiques exclus ne deviennent pas livrables par exception.
12. Les exceptions et réserves sont re-présentées lors de la reprise pertinente.
13. La péremption agit lorsque le livrable dépend du claim, pas sur les fixes étrangers.
14. Le contraste applicable est calculé ; APCA peut enrichir la lecture sans se substituer à un critère WCAG.
15. Une ressource maintenue documente version, capacité, fallback, limite, owner et prochaine revue.
16. Un outil ou une commande cités ne sont jamais exécutés aveuglément.
17. Automatisation, inspection perceptuelle et observation utilisateur restent distinctes.
18. La capture versionnée revue explicitement peut remplacer proportionnellement un pipeline de tests visuels absent.

## Couverture et point de passage

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Quatre sections, propriétaires et huit locators contrôlés |
| B — Sémantique | FULL | C1–C6, anti-slop, autorisation, exclusions, péremption et politiques analysés |
| C — Usage | TARGETED | Neuf scénarios designer, agent, owner, reviewer et mainteneur simulés |
| D — Résistance | FULL | Deux nouveaux constats et registre existant confrontés aux contre-exemples |
| Machine | FULL ciblé | Quinze mutations, garde-fous positifs et suite officielle exécutés |
| Sources externes | TARGETED | W3C WCAG 2.2, WCAG2ICT et projet APCA ouverts pour la politique de contraste |

Le bloc 11 est entièrement lu, sans verdict global ni correction du système. L’exception `FAIL-ASSUMED` exige une attention prioritaire dans les phases de contrats, résistance et décision de patch : il faut protéger la différence entre échec connu, preuve absente et risque non dérogeable, puis rendre la disposition de diffusion limitée intelligible sans la confondre avec `ACCEPTED`.

La prochaine unité est `ACTION.md`, lignes 870–935 : `ACTION/ROUTING`, `ACTION/MAINTENANCE`, `ACTION/CLOSE-EXIT-CHECK` et mesure expérimentale. Elle achèvera la lecture linéaire d’ACTION, puis viendra son checkpoint consolidé ; les phases 3–14 restent fermées au niveau du système.
