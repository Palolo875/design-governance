# DG-AUDIT-001 — Phase 2 — QUICKSTART, bloc 4

## Périmètre et contrôle de reprise

- Source dérivée : `audit_work/package/V1/official/QUICKSTART.md`, **lignes 158–191** ; sections 6 et 7, jusqu'avant le handoff à 192.
- Reprise : plan maître, rapport QUICKSTART bloc 3 (126–157), rapports blocs 1–2 et checkpoint transversal des cinq propriétaires. Protocole externe DG-AUDIT-001 v2.0 §12 relu pour les passages A–D. Le périmètre de cette unité ne comprend pas la section agentique, l'exemple ou la clôture détaillée qui suivent.
- B01 revérifiée avant lecture : compilation SHA-256 `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; QUICKSTART `c3334f12447c6dab8ac8794f5817ae52788ff06d8eff0e8d7e2d92fe7319bcde` ; cinq propriétaires inchangés selon les empreintes B01 du checkpoint.
- Confrontation exacte : `DIRECTION/FIRST-OBJECT` 314–339, `DOUBLE-LOOP` 482–504, absolu 1 559–575 ; `SAVOIR/CRAFT` 195–240 ; `ACTION/FIRST-RENDER` 79–91, boucle/one-shot 449–453, preuve et revue 507–523, Gate C 775–794, CLOSE-PACKAGE 391–405 et CLOSE-EXIT-CHECK 915–930. Les contrats ACTION applicables selon le mode restent distincts d'un jugement de qualité intrinsèque.

Ce rapport reste un diagnostic sectionnel documentaire : scénarios simulés, aucune qualité de produit réel mesurée, aucun texte normatif modifié.

## Passage A — architecture visible

La section 6 donne une grille courte de **huit dimensions** pour viser un premier rendu jugeable lorsque la décision visuelle est ouverte, puis dit explicitement qu'elle ne crée ni score ni style obligatoire et renvoie SAVOIR au jugement, ACTION à la preuve. La section 7 donne des conditions d'entrée du one-shot, six responsabilités qui subsistent même avec un seul cycle, et une sortie avec branches correction/réouverture/reclassification/preuve. Ce couple constitue une façade lisible : « construire assez pour observer » puis « s'arrêter lorsque l'observation suffit ».

Le renvoi à `DIRECTION/FIRST-OBJECT` en 160 doit toutefois être lu comme une **projection**. Les huit mots de QUICKSTART 166–173 ne sont pas les huit dimensions de DIRECTION 326–333. Les deux textes peuvent guider le même premier objet seulement si le passage de l'un à l'autre préserve les questions de vérité, intégration et résilience ; le simple fait qu'ils aient huit lignes ne garantit pas cette couverture. Ce point est déjà **F-DIR-020** ; la présente lecture en précise le mécanisme, sans nouvelle grille canonique.

## Passage B — contrat sémantique et mapping du premier objet

| Dimension propriétaire DIRECTION/FIRST-OBJECT 326–333 | Ce que reprend QUICKSTART 166–173 | Ce qui reste à rendre explicite dans la preuve |
|---|---|---|
| Présence et foyer | Présence, silhouette, point d'entrée, relation produit. | Identifier le foyer prioritaire face au CTA, texte, asset et preuve ; une silhouette n'établit pas seule la priorité de lecture. |
| Signature et désirabilité située | Spécificité, relation au produit/public/contenu ; diversité de styles 175. | L'intérêt perceptuel reste un jugement situé, jamais une préférence universelle prouvée. |
| Intégration | Premier objet, geste ou relation ; contenu et retenue. | Vérifier le rôle concret de l'asset ou du choix de n'en employer aucun, y compris fallback et preuve, sans le déclarer décoratif par son seul retrait. |
| Résolution | Typographie, contenu, action, responsive, états critiques. | Observer ces états dans les transformations pertinentes, non seulement les prévoir ou montrer le nominal. |
| Vérité de scène | « contenu suffisamment crédible » en 170, sans statut illustratif/observé nommé. | Marquer claim, client, donnée et comportement hypothétiques près de l'objet selon DIRECTION 316 ; la vraisemblance visuelle ne rend pas un claim vrai. |
| Résilience visible | Responsive et états critiques cités dans la construction. | Vérifier ce qui survit réellement au mobile, contenu long, erreur, fallback ou réduction d'effet selon le risque ; ce n'est pas explicitement une dimension QUICKSTART. |
| Retenue (notion de QUICKSTART) | Aucun effet, asset ou composant sans conséquence identifiable. | Protéger un rôle perceptuel, narratif, culturel ou émotionnel situé comme conséquence possible ; ne pas imposer une suppression mécanique. |

**Propriété et portée.** La phrase 160 dit « impose un niveau d'intention et de résolution », sans créer de verdict. L'entrée 162 conditionne la grille à une **décision visuelle ouverte** et au scope disponible. `ACTION/FIRST-RENDER` 83–91 fixe ensuite la qualité proportionnée à chacun des cinq modes ; pour un LITE de wrapping, la cohérence du delta suffit, sans exiger une première scène de marque ou huit réponses créatives. Pour un STANDARD dont le craft est dominant, Gate C peut être ciblé sans changer son mode : la section 6 **atténue F-QS-002**, puisqu'elle parle de décision visuelle et pas de reclassement, mais ne retire pas l'erreur autonome de la ligne 141 du bloc 3.

**Vérité, limites et preuve.** Une scène persuasive avec une donnée fictive non marquée échoue au contrat de vérité DIRECTION 316/332 malgré QUICKSTART 170 « contenu crédible ». Un rendu superbe sans runtime ni capture permet une intention, pas le PASS de Gate C : ACTION 777–783 exige rendu réel, scope, élément observé. Une capture réelle peut justifier une appréciation V/craft dans ses viewports, sans prouver utilisabilité ni accessibilité ; Gate A et preuve de tâche restent propriétaires d'ACTION. Le guide 175 attribue explicitement preuve et clôture à ACTION ; aucune grille de qualité ne court-circuite ce renvoi.

**One-shot et temporalité.** Les six éléments 183–188 sont cohérents avec DIRECTION 502, SAVOIR 205 et ACTION 453 : classer, construire, observer, revoir si visuel, vérifier risque, conserver preuve/limite/décision. La ligne 190 permet un arrêt après première observation si aucun défaut dominant ne demande de correction et si aucune itération ne promet un gain ; cela confirme le one-shot valide contre l'obligation contraire de modification dans le Boot DIRECTION 184 (**F-DIR-009**). Le mot « corrigé » à 190 suppose que l'artefact présenté est réobservé après une correction éventuelle ; aucune ancienne capture ne devient preuve de la version corrigée (ACTION 407–411). Une décision peut aussi être confirmée sans changement de pixels ; `DECISION-CHANGE` décrit alors confirmation observée selon ACTION 212–218, et `next_polish_action` doit exprimer un arrêt justifié plutôt qu'inventer une retouche (**F-ACT-025**).

**Risque critique et issue.** La condition 179 exige capacité critique disponible et aucun risque critique non protégé pour un one-shot clôturé. Si capture ou test nécessaire manque, déclarer `NOT-VERIFIED` et l'issue appropriée, souvent `EXPLORATORY`/`RETURNED` selon le mode et le risque ; « hypothèse intéressante » ne devient ni `PASS` ni `ACCEPTED`. Si un défaut d'usage ou de sécurité est connu, la beauté ne compense pas : rendre la décision, le risque et l'action de protection explicites. Les six éléments du raccourci ne constituent pas à eux seuls le paquet ACTION/CLOSE-EXIT-CHECK, avec owner, axes, version, réserve et verdict ; **F-ACT-016** demeure le risque d'une fermeture prématurée si la liste est traitée comme une validation intégrale.

## Passage C — simulations de lecteurs et accès

| Situation | Observation disponible | Décision attendue sans inventer un verdict |
|---|---|---|
| Surface DIRECTION sobre et spécifique ; ancre, capture et gates applicables effectivement couverts dès le premier rendu | Position/objet/geste visibles ; aucun défaut dominant dont la correction promet un gain utile. | Une seule version peut être décidée et clôturée selon ACTION ; trace de présence, limites, owner et arrêt du polish. Aucune deuxième retouche rituelle. |
| Premier rendu séduisant avec une promesse chiffrée illustrative présentée comme réelle | Capture visuelle, mais claim non sourcé et mécanisme peut-être non exécuté. | Retour au marquage de vérité/claim et preuve adéquate ; ni première version validée ni PASS d'usage sur le seul aspect crédible. F-DIR-020/021 et ACTION/proof. |
| Première scène assez belle, formulaire critique sans preuve de tâche et d'état d'erreur | Capture nominale seule ; risque critique encore ouvert. | La condition 179 n'est pas remplie : preuve suivante, réserve/retour/escalade selon owner ; pas de livraison one-shot acceptée sur la beauté. |
| Rendu non capturable, mais texte/spec de direction détaillés | Intention de construction, pas de rendu effectivement vu. | Craft `NOT-VERIFIED`, prochaine preuve ; l'absence de capture ne se convertit ni en `N/A-JUSTIFIED` ni en constat visuel positif. |
| Correction locale LITE de wrapping, système existant intact | Diff/rendu local et contrôle adapté réellement observés. | Preuve proportionnée et clôture ACTION, sans huit cibles d'identité ni route DIRECTION ajoutée. F-QS-001 atténué par la condition 162. |
| Première version avec défaut dominant corrigé avant clôture | Deux versions/rendus distinguables, seconde version à inspecter. | Comparer et rattacher verdict à l'artefact effectivement livré ; la seule rationale sur la première capture ne suffit pas. |

**Accès ciblé du lecteur de routes :** depuis `audit_work/package`, `read_route.py` a résolu `DIRECTION/FIRST-OBJECT`, `DIRECTION/DOUBLE-LOOP`, `SAVOIR/CRAFT`, `ACTION/FIRST-RENDER` et `ACTION/CLOSE-EXIT-CHECK` (code 0). `ACTION/GATE-C` existe comme titre à 775, mais son locator n'est pas accepté par le lecteur (code 1). Cette occurrence relève de **F-DIR-028** ; la lecture directe d'ACTION est nécessaire pour juger son contenu, et la résolution des cinq autres clés n'établit aucun PASS produit.

## Passage D — résistance et déduplication

| Référence | Confirmation ou limite apportée par 158–191 | Test ultérieur |
|---|---|---|
| **F-DIR-020** | Deux grilles de huit lignes aux axes non identiques ; la façade omet comme rubriques explicites vérité et résilience, tandis que la canonique n'a pas « retenue » comme ligne indépendante. | Évaluer une même scène fictive mobile à données inventées par les deux grilles : mêmes défauts nommés, owner et prochaine preuve retrouvables ? |
| **F-DIR-009 / F-ACT-025** | 190 protège une première version suffisante et le stop du polish ; Boot et champ machine peuvent encore pousser à inventer un geste. | RUN_CARD DIRECTION clôturée après observation initiale, `next_polish_action` exprimant un stop vrai sans altérer les axes. |
| **F-DIR-018 / F-SAV-006 / F-BIB-005** | 169 permet scène **ou** geste **ou** relation ; 175 autorise diverses expressions. « Retenue » doit garder le média porteur d'une relation justifiée. | Scène sobre avec image explicative véridique contre stock décoratif ; éviter de punir le premier sur ablation mécanique. |
| **F-ACT-016/018, F-DIR-019** | Six rappels one-shot utiles, mais ni clôture intégrale ni preuve si capacité requise absente ; statut adapté plutôt qu'un PASS par défaut. | Rejouer disponibilité capture et tâche × risque critique × issue/owner/verdict et non-applicabilité réelle. |
| **F-QS-001/002** | Condition « décision visuelle ouverte » et premier rendu proportionné réduisent la suractivation LITE et la confusion craft/mode, mais les phrases autonomes 87–94 et 141 demeurent. | Lecteur du guide entier contre lecteur de chaque tableau isolé, avec un brief STANDARD à craft dominant. |

**Aucun ID nouveau** : F-DIR-020 désigne déjà explicitement les deux grilles et leur divergence. La façade fournit une ambition positive utile, un vrai arrêt one-shot et une claire distribution SAVOIR/ACTION ; ses risques précis restent rattachés aux causes propriétaires et aux deux observations de façade déjà ouvertes. Les **103 fiches provisoires** demeurent 101 propriétaires + F-QS-001/002. Ni résultat réel, ni efficacité générale, ni disposition finale de patch ne sont affirmés.

## Sortie et prochaine unité

Lignes **158–191** relues avec les quatre passages, six scénarios et six accès ciblés ; baseline stable et liens aux rapports précédents explicités. **Prochain bloc : QUICKSTART.md lignes 192–212**, section 8 « Handoff agentique », avant l'exemple qui commence à 213. Reprendre protocole §12, plan, rapport présent ; comparer objectif, scope, autonomie, confirmation, sortie et instruction à l'agent avec ACTION/AUTHORITY, ACTION/HANDOFF, RUN_CARD et frontières de preuve. Les sections 9–12 et les autres façades suivront ; aucun fichier normatif ne change à ce stade.
