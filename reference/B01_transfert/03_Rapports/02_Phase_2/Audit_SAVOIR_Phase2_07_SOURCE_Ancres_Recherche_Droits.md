# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 7 : SOURCE, ancres et recherche

## Périmètre et reprise

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **471–529** : ouverture et statut des trois voies d’ancrage (471–477), test d’utilité (479–491), recherche orientée décision (493–516), curation/production/intégration (518–526), séparateur 528. `SAVOIR/DESIGN-ATLAS` commence à 530.
- Protocole externe : §12, quatre passages A–D. Point de reprise vérifié avec rapport SAVOIR bloc 6, plan maître et checkpoints DIRECTION/ACTION. Interfaces ciblées : `DIRECTION/VISUAL_TARGET` (373–441 et 578–591), `ACTION/PIPELINE-DIRECTION` (475–491), `ACTION/VISUAL_PROOF` (604–619), `ACTION/GATE-B/B3` (735–753), droits/confidentialité ACTION (429–435), schéma et constats de transport des ancres.
- Baseline B01 stable : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Diagnostic documentaire, sans exploration externe de marque, domaine ou réglementation et sans asset produit à inspecter. Les claims extérieurs qui influencent réellement un run devront être sourcés, datés et vérifiés selon leur portée ; ce rapport ne transforme aucune référence fictive en preuve.

## Résumé du bloc

SOURCE construit un rapport sain à l’ancrage : la référence, l’image générée et l’asset fourni ont des fonctions distinctes ; aucun n’est une preuve automatique de qualité finale, de droit d’usage ou de réussite utilisateur. La recherche doit changer une décision ou une preuve, et les références doivent être réellement observées, transformées, datées et réinspectables. Le test de retrait d’un asset évite de sélectionner une image seulement parce qu’elle est séduisante.

Une divergence propriétaire apparaît toutefois dans la protection d’une identité à fort enjeu **F-SAV-003, provisoire**. SOURCE ligne 477 propose une « comparaison indépendante » comme quatrième option au même rang qu’une référence observée, une contrainte réelle ou une réserve pour une ancre uniquement générée. `DIRECTION/VISUAL_TARGET` lignes 441 et 587 ainsi qu’ACTION ligne 477 ne donnent pas à une comparaison indépendante **sur la seule image générée** le pouvoir de remplacer la calibration externe ou sa réserve. Un regard indépendant peut améliorer la critique du rendu, mais sans référence ou contrainte externe il ne comble pas automatiquement cette absence. L’impact réel doit être éprouvé ; aucune règle n’est patchée à cette étape.

## Passage A — architecture visible

| Segment | Rôle et autorité | Condition et transmission |
|---|---|---|
| 471–477 | `[REQUIS PAR LE MODULE — surface DIRECTION]` ; voie générée, observée ou fournie, et borne de leur autorité | `DIRECTION/VISUAL_TARGET` définit les voies ; ACTION observe et clôt ; réserve generated-only à qualifier |
| 479–491 | Trois critères d’utilité, conventions et recherches hors écran, pièges d’asset | Changement de décision, contre-indication, attributs retenus/rejetés/non transférables ; jolie image ≠ preuve ou licence |
| 493–516 | Recherche de domaine et visuelle, fiche de source en douze entrées, profondeur graduée | Source ouverte et datée, observation, transformation, droit, trace, owner et prochaine preuve selon le risque |
| 518–526 | Relation avant image, domaines calibrateurs, route de production, contre-épreuve proportionnée | Asset retenu pour sa contribution sur rendu réel ; alternative refusée et résultat réinspectables |

Les titres et champs sont présents dans les sources, mais `read_route.py SAVOIR/SOURCE` et `read_route.py ACTION/PIPELINE-DIRECTION` répondent « locator inconnu » ; `DIRECTION/VISUAL_TARGET` se lit. `validate_reading_map.py` passe malgré ces deux refus. C’est une occurrence de **F-DIR-028/F-ACT-001**, pas une absence des sections ni un nouvel ID pour chaque route. Un lecteur doit rechercher les titres du propriétaire quand la CLI ne les résout pas.

## Passage B — contrat sémantique, section par section

### Trois voies, condition de chargement et autorité (471–477)

L’exigence de regarder un objet plutôt qu’une légende (473) distingue observation visuelle de description textuelle. La ligne 475 emprunte ses voies à DIRECTION et son exécution à ACTION : générée pour rendre une possibilité visible, observée pour calibrer une relation, fournie pour comprendre une intention ou exploiter un actif. Chaque ancre doit pouvoir influer sur la décision et porter une limite. Si elle est requise mais absente sur une identité, les axes concernés restent `NOT-VERIFIED` et ACTION décide de l’issue ; si aucune ne s’applique, SOURCE demande de justifier N/A.

Cette dernière exception ne s’emboîte pas encore sans perte avec DIRECTION ligne 579 (« ancre fraîche et inspectable » avant tout rendu DIRECTION), ACTION ligne 483 (sans ancre utile, axes concernés `NOT-VERIFIED`) et le schéma qui n’accepte pas facilement une liste d’ancres vide justifiée. L’occurrence renforce **F-DIR-027** : il faut préciser la branche où aucune ancre n’est utile sans forcer un faux `ANCHOR-GENERATED`, et maintenir les limites si une ancre nécessaire manque. Ne pas confondre « N/A parce que la décision n’en dépend pas » avec « ancre requise mais indisponible ».

La ligne 477 refuse correctement de promouvoir une image générée en calibration externe ou preuve de détail. Pour l’identité à fort enjeu, elle énumère quatre accompagnements au « ou ». DIRECTION (441 et 587) permet une référence observée, une contrainte réelle ou une réserve explicite ; DIRECTION 441 admet aussi une ancre fournie comme calibration complémentaire selon sa réalité et sa portée. ACTION reprend la première triade. `ACTION/GATE-B/B3` (737–753) dit qu’un avis humain externe réduit l’auto-préférence, mais ne garantit ni neutralité ni exhaustivité. Il ne transforme donc pas, par lui-même, deux images générées jugées par un tiers en référence externe au domaine ou à la fabrication de l’identité. Cette différence précise reçoit F-SAV-003 ci-dessous.

### Test d’utilité, inspiration et pièges (479–491)

Le triplet décision modifiée, contre-indication, attributs retenus/rejetés/non transférables (481–485) rend une ancre falsifiable dans son rôle. Une référence Web ou une galerie peuvent éclairer conventions et états ; elles ne constituent pas seules une esthétique située et ne donnent jamais le droit de copier (487–489). Une affiche, architecture ou signalétique n’est pertinente que si la relation qu’elle porte est transférable à la tâche, et sa licence reste distincte du droit éventuel sur un asset final. La liste des pièges (491) distingue prompt convergent, image générée ignorée, asset généré retenu sans droit/role/fidélité, résultat seulement thématique et image intégrée qui nuit à la lecture. Un prompt n’est pas un asset observé à son crop et son contraste réel ; ACTION (491, 604–619) conserve l’inspection de l’artefact construit.

### Recherche, fiche de source et statut épistémique (493–516)

Le déclencheur dépend de `DOMAIN-FRAME`, du risque et de l’ambition ; l’objet de la recherche est une décision susceptible de bouger, et non une accumulation de liens (495). La fiche locale (499–512) nomme origine/date/portée, rôle direction/production/vérification, statut vérifié ou non revérifié, observation réelle, retenu/rejeté, transformation, décision changée/confirmée/abandonnée, limite, trace, owner/prochaine preuve et droits/incertitude lorsque requis. Cette granularité évite de présenter connaissance mémoire ou source fournie par le demandeur comme vérifiée ce jour. Elle ne doit pas être présumée transportée automatiquement dans `RUN_CARD` : `sources[]` est une liste de chaînes et les détails des ancres doivent être reliés à une trace résoluble (F-ACT-028, F-ACT-002).

La recherche de domaine et la calibration visuelle peuvent être complémentaires sans être substituables (514). Une tendance ne prouve pas l’usage ; une référence visuelle n’autorise pas la réutilisation ; une convention de concurrent n’est pas vérité produit ; une génération n’est pas observation indépendante. « Lorsque la recherche ne modifie aucune décision, conserve `N/A-JUSTIFIED` » doit être lu avec ACTION (236) : une recherche peut **confirmer** une décision inchangée et apporter une preuve ou une limite nouvelle, qui mérite `DECISION-CHANGE` comme confirmation ou le résultat canonique approprié. La phrase SOURCE risque de classer trop vite ce travail en N/A ; cette occurrence était déjà suivie par F-DIR-011/019 et F-ACT-013/014 lors des blocs antérieurs. Si la recherche n’était pas applicable dès le départ, N/A est cohérent. La profondeur augmente lorsque erreur, confiance, culture, convention ou asset directeur en dépendent (516), puis doit modifier premier objet, contenu, geste ou preuve ; l’archive seule n’est pas un livrable.

### Curation, route d’asset et contre-épreuve (518–526)

L’entrée est la **relation** manquante, avant le type de média (520). Les domaines hors écran (522) servent de calibrateurs de lumière, rythme, distance, masse, orientation ou matière, avec transformation et limite ; ils ne sont pas un catalogue esthétique. La route de production appartient à DIRECTION, dont le tableau distingue code-native, fourni, curaté, généré-dirigé et hybride ; l’absence intentionnelle d’asset demeure une sortie réelle mais sa représentation dans la taxonomie est le constat F-DIR-025. Le résultat généré se juge à la lecture, au type, au contraste, au crop mobile, aux droits et à la preuve dans le rendu réel, non au réalisme de l’image isolée (524 et ACTION 491).

La contre-épreuve (526) demande si code-native, retrait d’asset, autre crop ou médium ferait mieux apparaître la même relation, mais **ne l’impose pas lorsque la décision resterait identique**. Elle conserve hypothèse, résultat et alternative refusée dans la trace ; aucun quota de variantes. La condition d’arrêt proportionnée de SOURCE ne résout pas automatiquement le libellé de `DIRECTION/GÉNÉRÉ-DIRIGÉ` « aucune source autorisée ne résout mieux le besoin », qui reste difficile à établir sur un univers illimité (F-DIR-026). Un test de recherche borné devra préciser sources réellement inspectées, disponibilité, droits, temps et coût d’erreur sans présumer une exhaustivité impossible.

## Passage C — lecteurs sous contrainte de temps

1. **Designer, identité à enjeu élevé avec ancre générée seule.** Il sollicite un reviewer indépendant de deux variations générées, sans source externe ni contrainte réelle. L’avis améliore la critique, mais ne retire pas la réserve exigée par DIRECTION sur l’absence de calibration ; SOURCE ligne 477 peut être lu à tort comme permission inverse (F-SAV-003).
2. **Agent, DIRECTION sans ancre utile.** SOURCE lui propose de justifier N/A, DIRECTION annonce une ancre fraîche obligatoire et le schéma refuse une omission simple. Il ne fabrique pas une ancre vide pour satisfaire le JSON ; il garde la limite et relève F-DIR-027 jusqu’à résolution de la branche.
3. **Équipe produit, benchmark sectoriel.** Une convention observée peut confirmer que l’action critique est familière, mais n’est pas preuve d’adéquation de cette entreprise ni de compréhension par ses utilisateurs. La source, sa date et le périmètre de transfert restent visibles.
4. **Designer, asset culturel séduisant.** Il nomme la relation qui manque à la surface, observe la référence entière et ses limites, vérifie droits du candidat retenu et compare un rendu code-native ou un retrait si cette comparaison peut changer la décision.
5. **Intégrateur, image générée en production.** Il inspecte ratio, crop mobile, voisinage de texte, contraste, fallback, identité/personnes représentées et permission de diffusion selon le risque ; le prompt et une image isolée ne suffisent pas.
6. **Reviewer, recherche qui confirme le choix initial.** Il documente la décision confirmée, la preuve observée et ce qui reste incertain ; il ne classe pas automatiquement le contrôle N/A au motif qu’aucun pixel n’a encore changé.
7. **Mainteneur, carte de run « valide ».** Il suit le locator de la fiche de source et du manifeste d’asset ; les chaînes `sources[]` et `anchors[]` ne démontrent seules ni statut de vérification, ni licence, ni absence de réserve generated-only.

## Passage D — résistance et registre

### F-SAV-003 — une comparaison indépendante peut être prise à tort pour calibration externe d’une ancre générée seule

- **Gravité provisoire : Significatif à éprouver.** Écart normatif textuel confirmé ; usage réel et conséquence de clôture à tester.
- **Preuve :** SOURCE ligne 477 propose, par un « ou », « référence observée », « contrainte réelle », « comparaison indépendante » ou « réserve ». `DIRECTION/VISUAL_TARGET` lignes 441, 587 et `ACTION/PIPELINE-DIRECTION` ligne 477 préservent la réserve lorsque l’identité à enjeu élevé n’a que `ANCHOR-GENERATED`, faute de référence observée/fournie pertinente ou contrainte réelle. `ACTION/GATE-B/B3` (737–753) qualifie un avis indépendant de contrepoint situé, pas de source externe automatiquement vérificatrice.
- **Contre-exemple discriminant :** un autre designer voit seulement deux variations issues du même générateur, compare leur hiérarchie et préfère la première, sans document de marque, référence observée externe ni contrainte réelle. La comparaison est légitime pour le craft, mais l’identité reste calibrée seulement sur hypothèses générées et sa réserve demeure. Si la comparaison inclut réellement une source observée, cela devient une autre branche avec sa provenance et sa portée.
- **Risque :** une lecture de SOURCE peut ôter la réserve, qualifier `HELD` sans contexte externe et publier une identité trop confiante ; la grille de relecture valide une préférence interne/externe au groupe sans l’objet de calibration demandé.
- **Atténuation :** SOURCE dit explicitement que l’image générée n’est pas une calibration externe suffisante et que le regard porte une limite ; DIRECTION et ACTION exposent la réserve. Le lecteur qui consulte les trois sources peut conserver cette protection.
- **Propriétaire pressenti :** `SAVOIR/SOURCE` pour la portée du quatrième terme de l’alternative ; DIRECTION pour la règle de réserve, ACTION pour la preuve et la clôture, sans transférer au reviewer un pouvoir de dispense implicite.
- **Relations sans fusion :** F-DIR-027 démontre le défaut de transport machine de la réserve generated-only ; F-ACT-037 interroge la qualification de l’indépendance d’une revue ; F-SAV-003 désigne **l’autorité attribuée à une revue même réellement indépendante en l’absence de calibration externe**, et persisterait si l’identité du reviewer était parfaitement tracée. F-ACT-028 concerne la traçabilité et non l’exception normative.
- **Test futur :** generated-only + reviewer indépendant sans référence ; generated-only + reviewer avec référence extérieure réellement observée ; generated-only + contrainte réelle ; generated-only + réserve explicite. Examiner texte, `RUN_CARD`, statut direction, verdict, scope et limite sur une identité à fort enjeu, puis un cas faible enjeu. Ne pas confondre absence d’indépendance et absence de calibration.

### Occurrences déjà classées, sans nouvel ID

| Observation | Relation / suite |
|---|---|
| Branche « ancre non applicable » versus obligation d’ancre et tableau `anchors[]` | F-DIR-027 ; tester N/A, ancre absente requise, ancre fournie, trace externe |
| Recherche confirmant une décision mais N/A recommandé si elle ne « modifie » rien | F-DIR-011/019, F-ACT-013/014 ; distinguer confirmation, non-applicabilité et attente non observée |
| Fiche SOURCE complète mais pas de mapping de ses champs dans `RUN_CARD` | F-ACT-028/002 ; sources, statuts, droits et résultats doivent rester résolubles depuis le locator |
| Droit incertain d’un asset transformé ou généré | F-ACT-024 ; la provenance ne vaut ni licence ni permission de publier |
| Absence intentionnelle d’asset et route GÉNÉRÉ-DIRIGÉ bornée par « aucune source autorisée » | F-DIR-025/026 ; ne pas inventer d’asset ni prétendre recherche exhaustive |
| Référence, objet de preuve et preuve exécutée présentés comme synonymes | F-DIR-024 ; SOURCE 487 et ACTION/VISUAL_PROOF 619 les séparent ici correctement |
| Routes SOURCE et ACTION pipeline refusées alors que titres existent | F-DIR-028/F-ACT-001 ; recherche manuelle nécessaire, carte de lecture verte insuffisante |
| Plusieurs responsabilités TYPE/CRAFT/SOURCE/CONTEXT activées | F-SAV-001 ; charger selon décision, preuve et limite distinctes, sans plafond « deux » |

### Contrôle outillé et protections positives

Test B01 ciblé : `SAVOIR/SOURCE` et `ACTION/PIPELINE-DIRECTION` échouent dans le lecteur ; `DIRECTION/VISUAL_TARGET` passe ; la validation de la carte dérivée passe. Les tests machines déjà documentés pour `anchors[]` et la réserve generated-only (F-DIR-027) ainsi que pour le transport `sources[]` (F-ACT-028) ne sont pas relancés ici sous un autre nom. Aucune recherche externe n’a été engagée pour feindre de vérifier une référence absente du cas ; en phase dédiée, chaque source réellement mobilisée sera ouverte, datée et comparée à la décision qu’elle affecte.

1. Une ancre doit modifier une décision et porter contre-indication, attributs retenus et non transférables.
2. Image générée, source observée et asset fourni ne reçoivent pas la même autorité ; aucune n’accorde automatiquement droit, qualité finale ou réussite d’usage.
3. Une source de domaine peut confirmer ou modifier une décision sans devenir vérité universelle du produit ; la preuve observée reste distincte de la cible pré-build.
4. Droits, permission, provenance et statut de vérification demeurent visibles, surtout si le contenu sera diffusé.
5. Une contre-épreuve est proportionnée et peut être un retrait ou une alternative code-native ; elle n’exige pas de fabriquer des variantes pour la forme.
6. Une recherche qui ne change aucun levier n’est pas prolongée pour remplir une trace ; une recherche nécessaire à un risque critique ne devient pas N/A faute de temps.

## Couverture et prochaine unité

| Passage | Profondeur | État |
|---|---|---|
| A — architecture | FULL | Quatre segments, tag, trois voies, douze éléments de fiche, routes et owners |
| B — sémantique | FULL | Utilité, autorité, recherche, N/A, transformation, droits, contre-épreuve et sortie |
| C — usage réel | TARGETED | Sept scénarios designer, agent, produit, intégrateur, reviewer et mainteneur |
| D — résistance | TARGETED | F-SAV-003 provisoire ; huit occurrences rattachées aux IDs précédents |
| Machine | TARGETED | Deux routes refusées, cible DIRECTION résolue, carte dérivée verte ; tests des ancres déjà disponibles |
| Externe | N/A-JUSTIFIED dans ce bloc | Aucune référence extérieure spécifique n’est utilisée comme prémisse factuelle ; les futurs claims devront être vérifiés au moment de leur usage |

Bloc 7 terminé avec **F-SAV-003 provisoire**, sans patch ni verdict global. La prochaine unité est **SAVOIR.md, lignes 530–573** : `SAVOIR/DESIGN-ATLAS`, cartographie des familles, portée par médium et sélection/non-recyclage. `SAVOIR/STYLE` commence à 574. Relire §12, la baseline, ce rapport et les constats de transport et de décision avant le prochain bloc.
