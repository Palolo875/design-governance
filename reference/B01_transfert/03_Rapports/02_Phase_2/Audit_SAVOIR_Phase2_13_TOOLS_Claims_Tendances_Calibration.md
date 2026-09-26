# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 13 : TOOLS

## Cadre et point de reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **784–842** : titre 784, contrat conditionnel du claim et fiche 786–801, trace et promotion 803–805, distinctions claim/source/asset/observation 807–814, goût et références 816–820, sourcing de DIRECTION et trois rôles d'ancre 822–824, tendances et taxonomie 826–839, séparateur 841. `SAVOIR/INTEGRITY` commence à **843**.
- Méthode : protocole externe v2.0 §12, passages A à D relus ; reprise de `Audit_SAVOIR_Phase2_12_TECH_Techniques_Preuves_Medium_Stack.md`, plan maître et checkpoints DIRECTION/ACTION. Interfaces propriétaires examinées : `SAVOIR/SOURCE` 471–526 et `TECH` 770–780 ; `DIRECTION/VISUAL_TARGET` 373–441 et absolu 2 en 577–591 ; `ACTION/GATE-A` 622–656, `OVERRIDE` 830–836 et inspection 849–861 ; `CHANGELOG` 23–42. Les réserves F-SAV-003 et F-SAV-009 ont été reprises par leur rapport d'origine.
- Baseline B01 inchangée : SHA-256 système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, SAVOIR propriétaire `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Lecture sectionnelle sans correction du corpus, sans claim de conformité d'un produit et sans verdict global. Les constats antérieurs F-SAV-001 à 009, F-ACT-001 à 039 et F-DIR-001 à 046 restent provisoires au niveau de la campagne.

## Passage A — architecture, entrées et propriétaires

TOOLS est appelé pour **source, tendance, outil ou claim** selon `SAVOIR/ROUTING` 81. Son premier déclencheur `[REQUIS PAR LE MODULE]` est plus étroit qu'une obligation de remplir une fiche à chaque consultation : le claim doit **influencer** une décision, un seuil, une route, une tendance ou un livrable (788). Le second sous-bloc guide goût, référence et sourcing selon la décision. `SAVOIR/SOURCE` possède la fiche d'une **ancre ou d'un asset** ; TOOLS qualifie le **claim et sa fraîcheur**. `DIRECTION` décide de la cible et du rôle de l'ancre ; `ACTION` possède preuve exécutée, issue, verdict et clôture ; `CHANGELOG` reçoit une règle devenue partagée après décision. Cette répartition évite qu'un résultat de recherche décide seul du mode ou qu'un claim local devienne règle normative.

**Accès vérifié :** le titre TOOLS existe à 784, mais `read_route.py SAVOIR/TOOLS` répond « locator inconnu » ; `validate_reading_map.py` passe indépendamment. La source est lisible directement. Cette manifestation appartient à F-DIR-028/F-ACT-001, déjà observés sur SOURCE, CONTEXT et TECH ; ne pas créer une entrée par route refusée.

## Passage B — contrat sémantique, phrase par phrase

### Déclenchement, contenu et mémoire d'un claim (786–805)

La fiche de 790–801 exige type, énoncé, scope, source, version ou date de vérification, limite, usage visé, owner, date de revue et prochaine preuve. Elle sert lorsque l'assertion **change réellement une décision** ; un fait simplement consulté, une observation située ou une préférence exprimée sans portée générale ne réclame pas automatiquement une fiche complète. À l'inverse, une norme, un seuil ou une tendance utilisés pour prescrire un design ne peuvent être cités sans source et limite. `CLAIM-TYPE` contient « local » bien que le sous-titre parle de claims externes : on peut qualifier une assertion locale qui guide un livrable, à condition de ne pas confondre avec une observation brute du run ; 807–814 opère cette distinction. La source ne vaut pas preuve d'un résultat produit : vérifier sa version et son périmètre précède la décision, puis ACTION observe l'artefact réel.

La ligne 803 maintient le claim dans la **trace locale** tant qu'il ne modifie pas de règle partagée. La promotion requiert décision explicite de l'owner compétent, compatibilité, preuve et entrée de gouvernance. `CHANGELOG` 25–27 réserve effectivement à son propriétaire la décision de changement transversal. Une affirmation répétée par plusieurs runs ne gagne pas d'autorité par comptage. « À REVÉRIFIER » (805) permet de déclencher une enquête ou un test local ; cette étiquette ne remplace pas `NOT-VERIFIED` dans la preuve ACTION et ne justifie pas seule un seuil, une règle universelle ou une promesse.

**Essai de qualification d'une source datée.** La [publication officielle WCAG 3](https://www.w3.org/TR/wcag-3.0/), ouverte le **23 septembre 2026**, affiche « Working Draft » daté du **10 septembre 2026**. Son état peut servir à décider de **surveiller** l'évolution d'un référentiel, avec version/date et réserve de changement. Il n'autorise ni à présenter le draft comme standard final ni à déduire une conformité de produit. Il s'agit ici d'un exemple de lecture de claim, pas de la fiche d'un run client réel. La [note WCAG2ICT du W3C](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/) donne, elle aussi, une aide informative pour interpréter WCAG sur certains supports non Web et **ne crée pas en elle-même de nouvelles exigences** ; ses usages doivent rester qualifiés par médium et référentiel effectivement adopté.

### Source observée, droit et résultat local (807–814)

Quatre objets ne doivent pas fusionner : **claim transférable**, **source réellement inspectée**, **asset avec son droit**, **observation du run**. Une référence esthétique peut éclairer rythme et densité sans devenir un fait sur les utilisateurs ; son ouverture n'autorise pas à reproduire l'image. Une capture d'un test sur un seul état ne produit ni claim général, ni nouveau principe durable. Ces distinctions rendent `SAVOIR/SOURCE` 493–516 et ACTION 429–435 nécessaires lorsque provenance, droit ou autorisation influencent le livrable. Une URL dans la trace sans page ouverte et observations retenues/rejetées ne remplit pas l'obligation d'ancre visuelle `DIRECTION` 589. Inversement, un contrat de droits inconnu ne se règle pas par la simple exactitude du claim.

### Goût et référence comme jugement situé (816–824)

Le principe `[DURABLE]` de 818 est une **heuristique de jugement**, pas une mesure scientifique ni un palmarès de marques. On extrait d'une référence une relation et son compromis, puis on la traduit dans le produit ; on ne copie pas l'apparence. La phrase 822 recommande sourcing Web ou recherche de références face à une direction neuve, ambiguë, risquée ou générique, et les rend **nécessaires** lorsque le contrat dépend d'un claim, d'une tendance, d'une provenance ou d'une décision qu'on ne peut honnêtement fonder de mémoire. La formulation sur le sourcing **ne suspend pas** `DIRECTION` 579 : une surface identitaire demande toujours une ancre fraîche et inspectable, qui peut être observée, fournie ou générée dans les limites de sa voie. Pour une identité à fort enjeu, une ancre uniquement générée réclame référence/contrainte réelle ou réserve de calibration selon `DIRECTION` 441 et 587.

Les trois rôles explicités en 824 sont distincts : ancrage de **direction** (arbitrer un axe), de **production** (construire un asset/composant) et de **vérification** (contrôler une propriété). La même page peut jouer plusieurs rôles, seulement si la contribution à chacun est documentée. Une galerie de composants peut calibrer une convention ; elle ne prouve pas seule qu'un produit a réussi une tâche. Une illustration créée pour produire un écran n'est pas, par sa qualité d'image, une vérification indépendante du rendu de cet écran. `SAVOIR/SOURCE` 477 propose pourtant la « comparaison indépendante » comme alternative possible à la réserve generated-only ; TOOLS ne lui donne pas expressément ce pouvoir. **F-SAV-003 demeure ouvert** : comparer deux variantes générées n'apporte pas à lui seul une source ou contrainte externe. DIRECTION 589 protège aussi contre un simple extrait de résultats de recherche comme ancre observée.

### Tendances, hypothèses et portée (826–839)

Une liste datée de produits ou une tendance porte source/date/portée/limite **si elle est effectivement mobilisée** dans le run (826). Une tendance est une hypothèse, dont la valeur doit être rapportée au JTBD, à la compréhension, à l'accessibilité, à la performance et à sa tenue sans son nom commercial (828). Pour résoudre la tension temporelle de « vérifier avant de l'utiliser », distinguer exploration ou prototype de l'adoption d'une direction : les gains de compréhension et de performance ne sont **observés** qu'après un essai adapté. Ne pas annoncer ces gains au moment où la tendance n'est encore qu'une option ; garder la preuve nécessaire `NOT-VERIFIED` et la prochaine observation. Cette précision renvoie à F-ACT-030 sur la séparation plan/méthode/résultat, sans ouvrir un nouvel ID au seul mot « avant ».

Le tableau 832–837 répartit signal daté, principe transférable, style situé et technique de production/preuve. Un style inspiré d'un courant récent ne reçoit ni le statut de norme, ni un PASS d'usage ; le signal de veille peut se périmer, le principe durable demande toujours portée et contre-indication. « same-energy » (839) peut nommer un risque de ressemblance, mais la correction exige la cause observable de la convergence.

### Interface restée ouverte avec TECH (778–780)

La présente section qualifie **les claims et sources des outils** : leur version, leur usage visé et leur limite. Elle ne définit **aucune exception explicite** à la phrase de TECH 778 qui interdit d'exécuter indistinctement « outil, script ou package » sans dépendance approuvée, source d'approbation et package/version. Pour un script local sans package tiers, le moyen de consigner « aucune nouvelle dépendance » demeure implicite ; **F-SAV-009 n'est donc pas résolu**. Pour une dépendance externe ou un outil qui porte une claim datée, SOURCE/TOOLS/TECH et ACTION donnent des questions pertinentes de provenance, version, autorisation, effet et preuve ; ne pas en déduire un PASS du seul dossier.

## Passage C — parcours de lecteurs

1. **Designer, nouvelle surface identitaire à fort enjeu.** Recherche de références pertinentes, ouverture et inspection de l'objet, rôle d'ancrage, attributs retenus et rejetés, puis comparaison au rendu. S'il ne dispose que d'une hypothèse générée et d'un reviewer indépendant, il maintient la réserve de calibration externe au lieu de la remplacer par la revue seule (F-SAV-003). Un résultat de recherche non ouvert n'est pas une ancre.
2. **Agent, correction locale de wrapping.** Aucune source, tendance ou claim externe ne change la décision ; le contrôle est proportionné. Pas de fiche de claim remplie par réflexe ; si un script autonome est nécessaire, la portée ambiguë de TECH 778 reste à trancher (F-SAV-009), sans faire semblant qu'un package tiers a été approuvé.
3. **Équipe conformité, brouillon de WCAG 3.** Page W3C réellement ouverte, datée et qualifiée comme draft au jour de consultation : utile à la veille ou à un prototype, impropre à être élevé seul au rang de règle de conformité courante. Elle documente prochaine revue si le livrable dépend d'une proposition évolutive. ACTION distingue cible normative éventuelle et résultat observé ; F-ACT-035 garde la frontière des claims globaux.
4. **Intégratrice, photo issue d'une page qui inspire l'interface.** La relation de composition est une référence observée, mais le droit de réemploi et la permission de diffuser l'asset sont séparés ; en l'absence d'autorisation, choisir un asset autorisé ou un rendu propre, puis contrôler son intégration. La source ouverte ne vaut ni licence ni preuve du comportement final.
5. **Mainteneur, règle locale réutilisée sur plusieurs surfaces.** Il ne la promeut pas parce qu'elle a « marché trois fois ». Il identifie propriétaire normatif, consommateurs, compatibilité, preuve, limites, prochaine revue et décision persistée en CHANGELOG. La copie d'une fiche dans `sources[]` ne transfère pas automatiquement l'autorité.
6. **Reviewer, claim ou outil périmé repris pour une version livrée.** ACTION 830–836 déclenche une revue si le livrable en dépend ; la projection peut accepter un verdict plein malgré une chaîne de texte « périmé » selon les tests ACTION antérieurs. Retrouver la source, vérifier sa version, nommer l'effet du changement et une prochaine preuve ; ne pas refaire ici le test machine déjà exécuté (F-ACT-022/028). F-ACT-019 concerne distinctement la non-péremption automatique d'un `EXECUTION-SNAPSHOT` lorsque ses entrées changent.

## Passage D — résistance et déduplication

**Aucun nouvel ID autonome pour ce bloc.** La section donne une protection utile contre quatre glissements (claim non vérifié devenu règle, référence copiée, asset utilisé sans droit, cible devenue preuve). Les ambiguïtés réellement observées relèvent déjà des IDs ci-dessous, ou attendent un parcours réel ; leur mention ne vaut pas conclusion de gravité système.

| Observation | Constat maintenu / prochaine épreuve |
|---|---|
| Fiche claim conditionnelle, plusieurs routes spécialisées parfois utiles | F-SAV-001/F-ACT-004 : ne pas réduire les routes applicables à un plafond ; ne pas charger TOOLS si aucun claim utile |
| SOURCE admet revue indépendante en alternative à réserve generated-only ; TOOLS ne l'érige pas en calibration externe | F-SAV-003, distinct de F-DIR-027 (transport des ancres) et F-ACT-037 (preuve d'indépendance du reviewer) |
| Outil local sans package et dossier d'approbation indiscriminé | F-SAV-009 ; TOOLS 784–839 ne spécifie pas de branche « aucune nouvelle dépendance » |
| Source/outil périmé ou preuve ancienne mais carte encore acceptée | F-ACT-022/028 ; F-ACT-019 porte séparément sur l'expiration du `EXECUTION-SNAPSHOT` |
| Cible, claim formelle et contrôle de portée bornée | F-ACT-035/F-DIR-038 ; `SAVOIR/TECH` 770–776 protège la sémantique, pas une attestation globale |
| Droit d'un asset ou autorité d'une action externe | F-ACT-024 et SOURCE ; source exacte et autorisation de réemploi sont deux vérifications |
| Route TOOLS refusée malgré titre et carte dérivée verte | F-DIR-028/F-ACT-001 ; ne pas multiplier les IDs de locator |

La fiche « claim local » peut prêter à confusion avec une simple observation locale. Les lignes 807–814 imposent expressément de les séparer ; un test discriminant futur fera qualifier une observation de run, une assertion utilisateur devenue décision produit et une recommandation de norme, puis vérifiera quelle fiche s'active. À ce stade, pas de contradiction autonome prouvée. La phrase de 828 sur la tendance « avant » s'interprète comme un contrôle avant adoption finale : si une simulation montre un PASS de compréhension/performance attribué à une hypothèse non testée, rouvrir ce cas avec F-ACT-030.

## Couverture, limites et reprise

| Passage | Profondeur | Couverture |
|---|---|---|
| A — architecture | FULL | Déclencheur, propriétaire, plan claim/ancre/asset, routage machine |
| B — sémantique | FULL | Claim 788–814, goût/source 818–824, tendances 826–839, interfaces TECH/ACTION |
| C — usage réel | TARGETED | Six rôles, identités, correctif local, draft normatif, droit, promotion, péremption |
| D — résistance | TARGETED | F-SAV-003/009 persistants ; glissements et ambiguïtés rattachés sans ID artificiel |
| Machine | TARGETED | Locator rejeté, reading map verte ; tests ACTION antérieurs sur sources périmées réutilisés |
| Externe | TARGETED | Page W3C du draft WCAG 3 et note WCAG2ICT réellement ouvertes ; statut/version/limites vérifiés, aucune attestation d'un produit |

La page W3C illustre la méthode ; elle ne fournit pas une preuve de conformité pour un artefact du système audité. La validation locale de la reading map ne démontre pas que l'agent peut charger TOOLS par locator. Aucun patch ni verdict final.

**Prochaine unité :** `SAVOIR/INTEGRITY`, lignes **843–905** ; test de non-récitation, modes d'échec d'application, délégation, refus, critique et limites. Les règles d'or commencent à 906 ; la méthodologie studio à 921. Leurs résumés seront lus ensuite sans les confondre avec la route INTEGRITY.
