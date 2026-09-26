# DG-AUDIT-001 — Phase 2 — DIRECTION, bloc 7

## Périmètre examiné

- Cible : `V1/official/DIRECTION.md`
- Bloc : lignes 543–642 de la reconstruction de travail
- Sections : `Rôle` et `LES CINQ RÈGLES ABSOLUES`
- Interfaces vérifiées : constitution de DIRECTION, `START`, `VISUAL_TARGET`, clôture de direction, `ACTION/STATUS`, `ACTION/PRECONDITION`, `ACTION/RUN-DIRECTION`, `ACTION/GATE-A`, `ACTION/GATE-B`, `ACTION/GATE-C`, `ACTION/OVERRIDE`, `ACTION/CLOSE-EXIT-CHECK`, `SAVOIR/FRAME`, `SAVOIR/SOURCE`, `SAVOIR/CONTEXT`, QUICKSTART, READING_MAP, skill pratique, schéma et validateur de `RUN_CARD`
- Source d’observation : compilation `Design_Governance_V1.0.md`, baseline B01
- Profil : DEEP
- Méthode : quatre passages de la phase 2, mapping de chaque absolu vers son propriétaire d’exécution, scénarios par mode et quatre contrôles machine ciblés
- Statut : diagnostic sectionnel provisoire ; aucun patch du corpus avant lecture complète et décision de correction

La baseline a été revérifiée avant l’analyse :

- système : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ;
- protocole : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`.

Les empreintes correspondent à B01. La phase 2 du protocole et le rapport du bloc 6 ont été relus. Les constats directement repris sont F-DIR-003, F-DIR-006, F-DIR-008, F-DIR-010, F-DIR-027 et F-DIR-030.

## Lecture structurée

| Segment | Fonction réelle | Ce qui fonctionne | Risque ou question |
|---|---|---|---|
| 543–549 | Installer la posture de l’agent | Problème, tâche, hiérarchie, point de vue, compromis et requalification explicite | Persona très orienté direction artistique pour un document chargé au début de tous les modes |
| 553–557 | Limiter l’inflation normative | Seulement cinq absolus transversaux ; les obligations spécialisées restent chez leurs propriétaires | Les paragraphes suivants recopient malgré tout plusieurs procédures spécialisées |
| 559–575 | Exiger une direction perceptible sur l’identitaire | Surface identitaire définie ; mapping net avec Gate C ; protection critique prioritaire | « Échec de livraison » doit rester une condition de retour ACTION, pas un verdict concurrent |
| 577–591 | Exiger un ancrage inspectable | Trois voies, limites de transfert, absence de quota et protection generated-only | Fraîcheur non définie ; branche N/A contradictoire ; contrat machine divergent |
| 593–603 | Interdire le `PASS` sans preuve | Propriété des gates laissée à ACTION ; N/A séparé de NOT-VERIFIED ; alternative conditionnelle | « Aucune livraison » possède un override ; procédure d’alternative recopiée sous un absolu de gate |
| 605–618 | Déclarer route, preuve et budget avant exécution | Pas de budget en appels ; jalons d’arrêt ; pas de baisse silencieuse du mode | « Avant d’agir » est impossible pendant l’intake ; paquets de champs non équivalents ; jalons non marqués comme conditionnels |
| 620–642 | Lier contexte réel, contenu, risque et beauté | Réalisme honnête, synthétique contrôlé, priorité aux risques critiques, limites de WCAG et d’une capture | Méthode humaine re-définie hors de son propriétaire ; nouvelle taxonomie de trois niveaux sans mapping |

## Passage A — architecture visible

Le bloc occupe une position constitutionnelle forte. DIRECTION est chargé au démarrage de tout run ; son rôle et ses cinq absolus doivent donc orienter aussi bien `LITE` que `DIRECTION` ou `SYSTÈME`. Le texte protège cette centralité par deux clauses : il n’existe que cinq absolus transversaux, et toute obligation spécialisée reste la propriété du module qui la définit.

La répartition attendue est lisible :

| Absolu | Fonction constitutionnelle | Propriétaire d’exécution attendu |
|---|---|---|
| 1 — Standard visuel | Une surface identitaire ne se réduit pas à la conformité | ACTION Gate C, avec jugement SAVOIR |
| 2 — Ancrage observable | La direction n’est pas dessinée depuis une mémoire non confrontée | DIRECTION/VISUAL_TARGET, SAVOIR/SOURCE, ACTION/PIPELINE-DIRECTION |
| 3 — Gate | Une preuve absente ne devient pas un `PASS` | ACTION |
| 4 — Mode, preuve et budget | Le run est cadré avant la production | DIRECTION/START puis ACTION/PRECONDITION et trace |
| 5 — Réel et beau | Contexte, contenu, risque et qualité restent liés | SAVOIR/FRAME et CONTEXT, ACTION pour méthode et preuve |

Cette architecture fonctionne tant que les absolus expriment une protection et renvoient au propriétaire. Le bloc va toutefois plus loin : il reproduit les critères C1–C3 de Gate C, les trois voies d’ancrage, la procédure d’alternative, une obligation de méthode avec personnes et une taxonomie locale de preuve. La frontière annoncée — router sans dupliquer la procédure — n’est donc pas tenue uniformément.

Le rôle placé avant les absolus est cohérent avec l’ambition créative du système : l’agent ne remplit pas un écran, ne copie pas un canon SaaS et ne remplace pas une relation de design par des effets. Il peut requalifier une demande ou escalader un risque, à condition de nommer décision, risque et prochaine preuve.

Ce rôle reste néanmoins celui d’un directeur artistique et product designer senior, alors que DIRECTION est chargé au départ de tous les runs, y compris correctif local, règle partagée ou risque principalement technique. Les routes et les propriétaires spécialisés limitent le biais, mais le persona peut encourager une lecture visuelle d’un problème qui devrait rester `LITE`, `SYSTÈME` ou principalement ACTION. Ce point reste une observation de posture ; aucun échec concret suffisant ne justifie encore un constat autonome.

## Passage B — contrat sémantique

### Préambule des cinq absolus

La limitation à cinq règles est saine. Elle évite de déclarer « absolue » toute obligation locale et protège la hiérarchie normative. La règle de remplacement — toute règle supplémentaire doit en remplacer une — crée une vraie barrière contre l’inflation.

La promesse selon laquelle DIRECTION ne duplique pas les procédures spécialisées est en revanche trop forte au regard du contenu réel. Les absolus peuvent légitimement résumer les conséquences à protéger, mais plusieurs paragraphes définissent sorties minimales, méthodes et conditions d’exécution. Le problème devient matériel lorsqu’une reprise locale diffère du propriétaire, comme dans l’observation avec des personnes de l’ABSOLU 5.

### ABSOLU 1 — standard visuel

La distinction entre conformité et direction est solide. Contraste, focus, états et performance constituent un plancher ; ils ne prouvent ni positionnement, ni promesse, ni caractère visuel. La définition de surface identitaire permet aussi de ne pas imposer le mode DIRECTION à toute interface : lorsque l’échec principal concerne une tâche ou un état, le mode proportionné reste la route par défaut.

Les trois décisions exigées correspondent exactement aux premiers critères d’`ACTION/GATE-C` :

- stratégie matérielle ↔ C1 stratégie de surface ;
- typographie déclarée ↔ C2 typographie choisie ;
- composition intentionnelle ↔ C3 composition intentionnelle.

Cette correspondance est l’un des meilleurs mappings du corpus. ACTION ajoute scope, capture, critères C4–C6 et issue de retour. L’expression « échec de livraison » ne crée donc pas nécessairement un verdict concurrent : elle peut être exécutée comme absence bloquante ou retour dans Gate C. Il faudra préserver ce mapping explicite lors d’une correction globale.

La stratégie matérielle accepte la planéité et l’absence intentionnelle d’asset. Elle contredit donc utilement toute lecture qui imposerait image, lumière ou texture. Cette branche confirme aussi que le trou de taxonomie F-DIR-025 appartient à la table des routes d’asset, pas au principe de direction.

La priorité donnée à une protection critique de compréhension, usage, sécurité ou accessibilité est nette. Elle n’annule pas la direction : elle oblige à la résoudre par hiérarchie, type, contenu, structure et détail plutôt que par un effet nuisible.

### ABSOLU 2 — ancrage observable

Les trois voies sont clairement distinguées. Une hypothèse générée rend une possibilité comparable ; une référence observée calibre ; une ancre fournie porte une intention ou un actif réel. Aucune référence ne devient modèle à copier, preuve d’efficacité, droit de réemploi ou validation universelle.

La voie observée exige une source réellement ouverte, datée et réinspectable. Le texte refuse correctement les extraits de résultats, images isolées et tendances non datées. Il évite aussi un quota fixe de références.

Deux contradictions déjà repérées sont renforcées :

1. l’absolu exige une ancre fraîche et utile pour une surface identitaire, tandis que `SAVOIR/SOURCE` autorise `N/A-JUSTIFIED` lorsqu’aucune ancre n’est applicable ;
2. le validateur impose toujours un objet `anchors[]` à une `RUN_CARD DIRECTION`, mais il ne peut représenter cette branche N/A ni contrôler le type d’ancre et la réserve generated-only.

Le mot **fraîche** n’est pas défini. Il peut raisonnablement vouloir dire « réellement rouverte ou produite dans ce run » plutôt que « œuvre récemment publiée ». Aucun champ n’indique toutefois la nature de la date, la dernière inspection ou la condition de péremption. Une ancre datée de 2001 dans un run de 2026 passe le validateur. Ce test ne prouve pas que toute ancienne référence est invalide ; il confirme que la fraîcheur absolue n’a pas de contrat contrôlable.

`ANCHOR-GENERATED` peut satisfaire l’ancrage normal sans calibration externe. Cela reste cohérent si l’objectif minimal est de sortir une idée de la mémoire pour l’inspecter. L’enjeu identitaire élevé exige une référence observée, une contrainte réelle ou une réserve. Cette gradation est utile et ne doit pas être remplacée par une interdiction générale de génération.

### ABSOLU 3 — gate

La propriété est correctement laissée à ACTION. DIRECTION route les contrôles proportionnés ; ACTION conserve critères, statuts, issues, verdicts et clôture. `N/A-JUSTIFIED` signifie non-applicabilité réelle ; `NOT-VERIFIED` signifie preuve requise mais indisponible. Aucun `PASS` implicite n’est permis.

La règle d’alternative est également proportionnée : elle ne s’active que si une autre position peut raisonnablement modifier la décision, et son niveau de matérialisation peut rester une phrase, un schéma, une cible ou un rendu. Aucun quota de variantes ou de retraits n’est créé.

Cette procédure appartient cependant déjà à `ACTION/PIPELINE-DIRECTION`. Sa reproduction détaillée sous l’absolu de gate contredit partiellement le préambule de non-duplication et rend la section plus difficile à maintenir.

Le titre « Aucune livraison sans les preuves applicables » possède une exception explicite : `FAIL-ASSUMED`. ACTION montre qu’il ne s’agit pas d’une acceptation, mais d’une diffusion limitée et temporaire malgré un échec connu, sur demande de l’utilisateur, avec scope, owner, date de revue et nouvelle preuve. Les risques graves, critiques ou trompeurs restent non livrables.

Le validateur rejette bien `issue: FAIL-ASSUMED` avec `verdict: ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`. La protection opérationnelle tient donc. La formulation constitutionnelle serait néanmoins plus exacte avec « aucune livraison acceptée » ou « aucune preuve absente masquée » ; le présent libellé absolu et son override décrivent deux sens différents du mot livraison. Ce point reste une imprécision significative à intégrer à la correction de vocabulaire, sans ouvrir un constat séparé.

### ABSOLU 4 — mode, preuve et budget

Le principe positif est juste : le budget est une suite de jalons décisionnels, pas un quota d’appels d’outil. Une contrainte de temps, dépendance, maintenance, performance ou capacité modifie la preuve disponible, jamais la vérité de ce qui a été observé.

La temporalité est en revanche instable. Le titre dit « avant d’exécuter », ce qui peut signifier avant build, modification, vérification ou action persistante. La première phrase dit « avant d’agir ». Or ACTION prévoit explicitement un état `INTAKE` où le périmètre et les inconnues restent ouverts, et `DIRECTION/START` demande une clarification lorsque le mode ou le risque ne sont pas encore classables. Poser cette clarification, inspecter un brief ou identifier le blast radius sont déjà des actions nécessaires pour pouvoir déclarer le mode.

Une lecture littérale oblige donc l’agent soit à deviner prématurément, soit à violer l’absolu. La formulation de référence devrait distinguer l’intake autorisé de l’exécution qui engage artefact, preuve, état ou action externe.

Le contenu minimal de l’absolu n’est pas stable entre les façades :

| Vue | Champs ou éléments déclarés avant exécution |
|---|---|
| ABSOLU 4 détaillé | mode, décision, risque, preuve minimale, condition d’arrêt ; contrainte de coût si déterminante |
| `START` — entrée minimale | décision, risque, scope, contrainte, prochaine preuve, owner |
| Entrée prioritaire de DIRECTION | mode, scope, capacité, preuve, limite, prochaine action |
| Façade QUICKSTART | mode, risque, décision, prochaine preuve, owner |
| Résumé des absolus QUICKSTART/READING_MAP | mode, prochaine preuve, budget |
| Skill — ligne de run | ID, mode, décision, risque, prochaine preuve, state ; puis entrée DIRECTION avec scope, contrainte et owner |

Ces vues peuvent être des condensations de niveaux différents, mais elles ne déclarent pas leur mapping. Owner, scope, capacité, limite, condition d’arrêt et état apparaissent ou disparaissent selon la façade.

La condition d’arrêt fait partie de l’absolu détaillé et d’`ACTION/HANDOFF`, mais `run_card.schema.json` n’accepte pas un champ `exit_condition`. Elle peut vivre dans la trace externe référencée par `trace_locator`, mais cette destination n’est pas rappelée ici.

Enfin, la table des jalons inclut Direction et Ancrage alors que l’absolu est transversal. Pour `LITE`, `ITER`, `STANDARD` ou `SYSTÈME`, ces jalons peuvent être hérités, non applicables ou remplacés par la route du mode. Les règles globales de proportionnalité évitent normalement de les exécuter tous, mais la table gagnerait à le dire pour ne pas devenir une checklist universelle.

### ABSOLU 5 — réel et beau ensemble

Le principe central est solide. Le contenu réel et la microcopie honnête deviennent une matière de création, pas une contrainte ajoutée après le design. Le contenu synthétique reste autorisé s’il conserve longueur, densité, langue, structure, ambiguïté, statut, permission et extrêmes capables de changer la décision. Le placeholder générique est refusé lorsqu’il masque précisément ces propriétés.

La priorité donnée à la prévention d’erreur, la confirmation, la traçabilité et la robustesse en santé, finance, légal et secteur public est cohérente avec les risques critiques. L’information essentielle ne dépend jamais de la couleur seule.

Le cadre d’accessibilité externe est prudemment borné : référentiel et version viennent du propriétaire compétent ; une source évolutive reste `[VEILLE]` jusqu’à adoption ; une conformité ne prouve ni direction, ni utilisabilité globale, ni adéquation du positionnement.

La règle d’observation humaine pose toutefois un conflit de propriétaire et de méthode. DIRECTION exige, lorsque le risque dominant concerne une population, l’accessibilité réelle, une tâche critique ou un coût d’erreur élevé, une observation avec des personnes représentatives ou une justification explicite de son impossibilité.

`SAVOIR/FRAME` donne une règle plus nuancée :

- utilisabilité réelle dominante → méthode `USER/TASK` avec personne, tâche, contexte, échantillon et résultat ;
- accessibilité ou population dominante → choisir `USER`, `EXPERT` ou le regard d’une personne concernée selon le risque, puis justifier ce choix.

ACTION distingue également `AUTOMATED`, `MANUAL`, `EXPERT` et `USER`, et réserve explicitement l’utilisateur représentatif à l’utilisabilité réelle. DIRECTION transforme donc une sélection de méthode proportionnée en obligation humaine générale, tout en permettant qu’une simple justification d’impossibilité remplace cette observation. Cela peut à la fois surcharger un contrôle technique correctement couvert et sous-utiliser une inspection experte disponible.

Le contrat machine n’applique pas l’absolu : une `RUN_CARD` à risque d’accessibilité critique, clôturée `ACCEPTED-WITH-RESERVATION`, avec contrôles techniques et inspection experte, sans participant ni justification d’impossibilité, passe le validateur. La projection est volontairement partielle, mais aucune trace structurée n’empêche ici deux exécutions opposées.

Le tableau final ajoute enfin trois « niveaux de preuve » : Contexte, Décision et Rendu. Ils constituent une lentille utile pour éviter qu’un rendu correct réponde au mauvais problème. Ils ne sont toutefois mappés ni aux axes V/U/A/T, ni aux gates A/B/C, ni à la hiérarchie P0–P3, ni aux familles de méthodes ACTION. Aucun statut, champ ou condition de sortie n’indique comment enregistrer leur couverture.

Le dernier garde-fou est excellent : une capture ou lecture perceptuelle peut établir une observation visuelle ou une compréhensibilité présumée ; elle ne devient preuve d’utilisabilité que si utilisateur, objectif, tâche, contexte et résultat observé sont définis.

## Contrôles machine ciblés

### Test 1 — ancre manifestement ancienne

La date de l’ancre de l’exemple officiel a été remplacée par `2001-01-01`, tandis que le run et l’observation sont datés de 2026.

```text
RUN_CARD VALIDATION PASSED
```

Le schéma exige une chaîne non vide, sans sémantique de fraîcheur. Une référence ancienne peut rester pertinente ; le test confirme seulement que « fraîche » n’est pas une propriété contrôlée.

### Test 2 — risque d’accessibilité critique sans personnes représentatives

L’exemple a été transformé en run à risque d’accessibilité critique avec protection structurée, contrôle du contraste, clavier et focus, inspection experte, participant déclaré non requis, absence d’observation humaine et aucune justification d’impossibilité.

```text
RUN_CARD VALIDATION PASSED
```

Cette configuration est compatible avec certaines méthodes d’ACTION et SAVOIR, mais pas avec la formulation littérale de l’ABSOLU 5. Le test confirme la divergence, non la nécessité automatique d’ajouter une règle au validateur.

### Test 3 — condition d’arrêt structurée

L’ajout de `exit_condition` à l’exemple officiel produit :

```text
RUN_CARD VALIDATION FAILED
run_card : champs inconnus : exit_condition
```

La condition d’arrêt absolue doit donc vivre dans une trace externe ou obtenir un mapping ; la projection seule ne la transporte pas.

### Test 4 — FAIL-ASSUMED accepté

La fixture officielle combinant `issue: FAIL-ASSUMED` et verdict accepté produit :

```text
RUN_CARD VALIDATION FAILED
une issue bloquante ou FAIL-ASSUMED ne peut pas produire un verdict accepté
```

Le mécanisme machine protège correctement la différence entre diffusion limitée et acceptation.

## Passage C — usage simulé

### Brief vague ou risque encore inconnu

L’agent reçoit une demande dont le blast radius et le risque ne sont pas déterminables. `START` lui ordonne de poser une clarification ciblée et ACTION le maintient en `INTAKE`. L’ABSOLU 4 lui demande pourtant, avant d’agir, un mode et un risque déjà déclarés. Un agent littéral peut choisir un mode prématuré pour rendre la trace conforme.

### Correctif LITE sur une surface identitaire existante

Le changement touche un wrapping local sans modifier matière, type ou composition. L’ABSOLU 1 exige que ces décisions soient présentes et nommables, mais Gate C est `N/A-JUSTIFIED` en LITE lorsque le craft n’est pas concerné. La lecture proportionnée consiste à vérifier que la direction héritée reste intacte, pas à rejouer les trois décisions ni les six jalons.

### Direction normale avec hypothèse générée seule

L’agent génère une hypothèse visuelle, l’inspecte et la compare. Pour un enjeu identitaire non élevé, cette voie satisfait l’ancrage minimal même sans référence externe. Il doit toutefois conserver la limite : l’hypothèse rend une possibilité visible, elle ne calibre ni culture, ni marché, ni préférence.

### Surface identitaire sans ancre applicable

SAVOIR autorise une non-applicabilité justifiée ; l’absolu dit que l’absence d’ancre bloque la livraison validée ; la projection DIRECTION refuse une liste vide. Selon la source suivie, l’agent documente N/A, fabrique un faux ancrage ou bloque le run.

### Accessibilité critique

Une équipe dispose d’une inspection experte, de tests clavier et de technologies d’assistance, mais pas de participants. ACTION et SAVOIR peuvent juger cette méthode proportionnée en conservant les limites. L’ABSOLU 5 exige une observation avec des personnes ou une impossibilité justifiée. Le validateur accepte pourtant le run sans cette justification. Reviewer humain et système automatique peuvent donc conclure différemment.

### Diffusion limitée malgré échec connu

L’utilisateur demande une diffusion temporaire d’un défaut non critique. ACTION permet `FAIL-ASSUMED` avec scope, owner, date et retest ; le validateur interdit l’acceptation. Le mot « livraison » de l’absolu doit donc être compris comme livraison validée ou acceptée, pas comme toute diffusion.

### Mainteneur des taxonomies de preuve

Le mainteneur doit expliquer simultanément gates A/B/C, axes V/U/A/T, hiérarchie P0–P3, méthodes AUTOMATED/MANUAL/EXPERT/USER et niveaux Contexte/Décision/Rendu. Sans mapping, il ne sait pas si les trois derniers doivent être enregistrés, évalués ou seulement utilisés comme questions de cadrage.

## Passage D — constats

### F-DIR-031 — l’ABSOLU 4 exige le classement avant les actions nécessaires pour classer

- Gravité provisoire : **Significatif**
- État : **ambiguïté temporelle confirmée**
- Preuve : ligne 607 « avant d’agir » contre `ACTION/STATUS`, où `INTAKE` conserve périmètre et inconnues ouverts, et `DIRECTION/START`, qui autorise une clarification avant classement
- Risque : mode ou risque deviné prématurément, clarification traitée comme violation, ou absolu ignoré par habitude
- Facteur atténuant : le titre dit « avant d’exécuter » et peut être interprété comme avant production, modification, vérification ou action persistante
- Propriétaire pressenti : DIRECTION pour la temporalité ; ACTION conserve les états
- Test futur : brief classable immédiatement, brief ambigu, inspection préalable du blast radius et reclassification après découverte
- Correction probable à éprouver : autoriser explicitement l’intake et exiger la déclaration avant toute action qui engage artefact, preuve, état, diffusion ou persistance

### F-DIR-032 — l’ABSOLU 5 redéfinit la méthode de preuve humaine hors de son propriétaire

- Gravité provisoire : **Significatif**
- État : **contradiction documentaire et divergence machine confirmées**
- Preuve : ligne 632 exige des personnes représentatives ou une impossibilité ; SAVOIR ligne 189 autorise `USER`, `EXPERT` ou personne concernée selon le risque ; ACTION distingue quatre familles de méthodes ; le validateur accepte un risque d’accessibilité critique couvert sans participant ni justification d’impossibilité
- Risque : test utilisateur imposé lorsqu’une méthode experte/technique est adaptée, inspection experte disponible ignorée, ou absence humaine justifiée comme échappatoire sans déterminer la meilleure méthode
- Facteur atténuant : ACTION reste déclaré propriétaire de la preuve et le `CAPABILITY-PROFILE` empêche de présenter une capacité absente comme observée
- Propriétaires pressentis : SAVOIR pour le choix de méthode ; ACTION pour preuve, capacité et verdict ; DIRECTION pour le déclencheur de risque
- Test futur : utilisabilité réelle, contraste technique, lecteur d’écran, compréhension d’une population concernée, tâche de santé critique et préférence visuelle

### F-DIR-033 — les niveaux Contexte / Décision / Rendu créent une taxonomie de preuve non raccordée

- Gravité provisoire : **Significatif**
- État : **confirmé au niveau documentaire**
- Preuve : lignes 634–640 contre les registres canoniques A/B/C, V/U/A/T, P0–P3 et les méthodes ACTION, sans mapping, statut, champ ni condition de sortie
- Risque : checklist supplémentaire, couverture déclarée différemment selon le lecteur, ou confusion entre étape de raisonnement, type de preuve et verdict
- Facteur atténuant : le tableau ne crée aucun enum et peut être interprété comme trois questions de cadrage
- Propriétaires pressentis : DIRECTION pour la lentille ; ACTION pour la taxonomie de preuve
- Test futur : un même run doit pouvoir projeter chaque question vers une méthode, un axe, un artefact, un statut et une limite sans nouveau registre

### Mise à jour de F-DIR-003 — temporalité de la trace

La condition d’arrêt doit être déclarée avant l’exécution, mais n’a pas de transport structuré dans `RUN_CARD`. La différence entre intake, cadrage, pré-build, post-build et clôture reste essentielle. F-DIR-031 isole l’impossibilité « avant d’agir » ; F-DIR-003 reste le problème transversal de temporalité et de phase des champs.

### Mise à jour de F-DIR-006 — mapping humain / trace / projection

`exit_condition` est rejeté, les niveaux Contexte/Décision/Rendu n’ont pas de projection et l’exigence humaine de l’ABSOLU 5 n’est pas contrôlable. Ces éléments peuvent vivre dans `trace_locator`, mais le mapping n’est pas explicite. F-DIR-006 est renforcé sans conclure que chaque concept exige un nouveau champ JSON.

### Mise à jour de F-DIR-008 — owner et scope omis des résumés constitutionnels

L’ABSOLU 4 détaillé omet owner et scope ; son résumé prioritaire omet décision, risque et condition d’arrêt ; QUICKSTART conserve owner dans sa façade générale mais pas dans son résumé des absolus. F-DIR-008 demeure **Significatif confirmé**.

### Mise à jour de F-DIR-010 — formes minimales concurrentes

La matrice des six formulations pré-exécution confirme que la fragmentation ne concerne pas seulement la ligne de run et la clôture. Elle touche maintenant un absolu transversal. La correction devra nommer une forme canonique et déclarer les autres comme projections avec pertes autorisées.

### Mise à jour de F-DIR-027 — ancrage humain et machine

L’ABSOLU 2 renforce le caractère obligatoire d’une ancre fraîche sur une surface identitaire, alors que SAVOIR conserve une branche N/A. Le test d’ancre datée de 2001 passe, et les tests précédents ont montré que type d’ancre, réserve generated-only et N/A ne sont pas contrôlés. F-DIR-027 reste **Majeur provisoire** jusqu’à l’audit complet du schéma et des validateurs.

### Mise à jour de F-DIR-030 — frontières de responsabilité

Le motif observé dans le craft s’étend à la preuve : DIRECTION annonce qu’il route sans dupliquer, mais l’ABSOLU 5 définit une méthode spécialisée différente de SAVOIR/ACTION. F-DIR-032 isole le conflit humain ; F-DIR-030 reste centré sur le jugement de craft.

## Éléments conformes à préserver

1. Les absolus transversaux sont limités à cinq.
2. Les obligations spécialisées sont déclarées propriétaires de leurs modules.
3. La conformité constitue un plancher, jamais une direction ou une réussite globale.
4. La surface identitaire est distinguée d’une tâche principalement opérationnelle.
5. Stratégie de surface, typographie et composition se mappent directement à Gate C.
6. L’absence intentionnelle d’asset et la planéité sont des stratégies possibles.
7. Une protection critique prévaut sur un effet visuel nuisible.
8. Les trois voies d’ancrage ont des fonctions distinctes.
9. Une hypothèse générée ne devient pas calibration externe ou preuve par défaut.
10. Une référence n’accorde ni efficacité, ni droit, ni adéquation universelle.
11. Aucun quota de références, alternatives, variantes ou retraits n’est imposé.
12. `N/A-JUSTIFIED` et `NOT-VERIFIED` restent séparés.
13. `FAIL-ASSUMED` ne devient jamais `PASS` et ne couvre aucun risque grave ou critique.
14. Le budget est une suite de jalons, pas un nombre d’appels d’outil.
15. Une contrainte de capacité ne transforme jamais une qualité non observée en qualité acquise.
16. Le contenu synthétique doit conserver les propriétés capables de changer la décision.
17. Le faux réalisme et les placeholders masquant le risque sont refusés.
18. En contexte à enjeu, prévention d’erreur, confirmation, traçabilité et robustesse priment sur le spectacle.
19. Un référentiel évolutif ne devient pas automatiquement une obligation de livraison.
20. Une capture ou une conformité ne devient pas preuve d’utilisabilité sans utilisateur, objectif, tâche, contexte et résultat observé.

## Couverture

| Passage | Profondeur | État |
|---|---|---|
| A — Architecture | FULL | Rôle, hiérarchie des absolus et mapping vers les propriétaires examinés |
| B — Contrats | FULL | Les cinq absolus ont été analysés individuellement, avec exceptions et sorties |
| C — Usage | TARGETED | Brief vague, LITE identitaire, ancrage, accessibilité critique, FAIL-ASSUMED et maintenance simulés |
| D — Résistance | FULL | Trois nouveaux constats et six mises à jour enregistrés |
| Contrôles machine | TARGETED | Fraîcheur d’ancre, accessibilité critique, condition d’arrêt et FAIL-ASSUMED testés |

Aucun verdict global sur DIRECTION n’est émis. Aucun patch n’est appliqué. Le prochain bloc couvre `Posture`, `0. Classification du mode, preuve et capacité`, `ITER se souvient` et `Cadrage de médium et de capacité` — lignes 646–700. Il devra vérifier la résistance au conformisme, la mémoire ITER, la sélection de capacités, les fallbacks et la compatibilité entre médium, preuve et risque.
