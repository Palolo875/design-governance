# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 8 : DESIGN-ATLAS

## Périmètre et continuité

- Source propriétaire : `V1/official/SAVOIR.md`, lignes **530–573** : rôle et déclencheur de l’atlas (530–532), six familles et leurs routes (534–541), cartographie illustrative (543–556), rôles d’asset (558–560), portée des médiums (562–564), sélection et frontière maintenance/design (566–570), séparateur 572. `SAVOIR/STYLE` commence à 574.
- Protocole externe v2.0, §12 : quatre passages A–D. Point de reprise : plan maître, rapport SOURCE bloc 7, checkpoints DIRECTION et ACTION, `SAVOIR/ROUTING` et interfaces propriétaires ; lecture sectionnelle, aucun verdict global ni patch.
- Baseline B01 vérifiée : système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR officiel `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Interfaces lues : `DIRECTION/START` (125–159) et `DAILY` (245–259) ; `ACTION` (232–238, 379–387, 872–887) ; `SAVOIR/ROUTING` (66–82), `SOURCE` (471–526), `SYSTEM` (690–704) et `CONTEXT` (758–778) ; `BIBLIOTHEQUE/SELECT` et `COMPONENTS` ; constat F-SAV-003 du bloc précédent. Les autres sections encore non analysées complètement sont consultées ici seulement comme interfaces.

## Conclusion locale

L’ATLAS fournit un vocabulaire utile pour chercher **quelle relation doit changer**, puis renvoie à la route propriétaire. Six familles couvrent médium, style, technique, effet, asset et structure sans prescrire un look ni un quota. La sélection avant build est une hypothèse ; l’effet observé et le verdict restent à ACTION. La frontière avec la maintenance locale fonctionne **si** la protection de risque critique de `DIRECTION/START` est appliquée en premier.

Un écart provisoire **F-SAV-004** concerne le renvoi de la famille « Structure / composant » : la cellule de routes (541) cite `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` pour le partagé mais omet `SAVOIR/SYSTEM`, route principale et requise pour tokens et composants partagés (SAVOIR 78, 690–704 ; ACTION 885). Une lecture menée depuis cette cellule peut laisser de côté le jugement sur sémantique des tokens, modes, consumers, thèmes et interopérabilité. Le routage principal atténue le risque ; l’usage réel reste à éprouver.

## Passage A — architecture visible

| Lignes | Forme et fonction | Autorité et sortie |
|---|---|---|
| 530–532 | Titre `SAVOIR/DESIGN-ATLAS` ; filtre par décision et risque | Index de jugement, après classification ; retour à START si risque supérieur ; ACTION recalcule les preuves |
| 534–541 | Six familles, responsabilité, routes approfondies, question de sélection | Renvoi vers SAVOIR, DIRECTION, BIBLIOTHEQUE, ACTION selon l’objet ; lacune ciblée du renvoi SYSTEM en 541 |
| 543–556 | Six relations avec techniques et effets possibles, non exhaustifs | Aucune technique n’acquiert force de preuve par présence ; catégorie de retrait décoratif |
| 558–564 | Onze rôles possibles d’asset et onze médiums usuels | DIRECTION possède rôle/route ; SOURCE provenance ; CONTEXT contraintes ; ACTION rendu, fallback, preuve et clôture |
| 566–570 | Hypothèse de sélection, cinq slots locaux, conséquence observée, réemploi et limite maintenance | `DECISION-CHANGE` seulement après observation, sinon résultat canonique ACTION ; zéro famille est admis |

L’index est explicitement une section de SAVOIR, pas une route autonome à placer entre DIRECTION et ACTION. Le texte la cite souvent comme « section `DESIGN-ATLAS` » (ACTION 232 et 883). `read_route.py SAVOIR/DESIGN-ATLAS` refuse pourtant le locator présent dans son titre, tandis que `validate_reading_map.py` passe. C’est une occurrence instrumentée du défaut de couverture **F-DIR-028/F-ACT-001** : distinguer section lisible par titre et clé non servie par le lecteur, sans inventer une nouvelle procédure ATLAS.

## Passage B — contrat sémantique, section par section

### Filtre initial et non-diminution du risque (530–532)

Le mode, le JTBD et l’esthétique ne sont pas déduits d’une famille. Le déclencheur est la prochaine décision et son risque ; sans conséquence possible, le document doit rester silencieux. Si une famille rend visible un risque supérieur, la reprise passe par START et une nouvelle classification avant l’exécution. L’ATLAS ne peut pas abaisser les gates ni transformer un enjeu critique en exercice de style. Cela réutilise l’autorité de START plutôt que de créer un sixième mode ; l’owner de preuve et de clôture reste ACTION.

### Familles, technique, effet et structure (534–556)

« Médium » porte le support et ses contraintes ; « Style » l’expression située ; « Technique » une modification de relation ou de production ; « Effet » une conséquence pour la personne ; « Asset » un contenu/objet médiatique avec fonction ; « Structure / composant » espace, lecture, états, données et action. Leur usage n’est pas mutuellement exclusif : un composant peut porter à la fois structure, état, type et risque technique. Chaque route ne s’ajoute que si sa décision, sa preuve ou sa limite diffère (F-SAV-001). La carte 547–554 est illustrative, non une matrice de couverture obligatoire : une ombre ou un flou n’est pas une réussite et `DÉCORATIF-SANS-CONSEQUENCE` sert à retirer.

La cellule 541 suit correctement `BIBLIOTHEQUE/SELECT` si la structure est ouverte et `BIBLIOTHEQUE/COMPONENTS`/`ACTION/RUN-SYSTEM` lorsqu’un composant est partagé. Toutefois elle ne mentionne pas `SAVOIR/SYSTEM`, alors que `SAVOIR/ROUTING` 78 en fait la route principale pour token/consumer/composant partagé, `SAVOIR/SYSTEM` 692 marque la responsabilité comme `[REQUIS PAR LE MODULE]`, et ACTION 885 donne les trois routes. `BIBLIOTHEQUE/COMPONENTS` possède l’anatomie et les dépendances ; ACTION cartographie impact, migration et verdict ; aucun des deux ne remplace le jugement spécifique de SAVOIR sur tokens primitifs et sémantiques, modes ou source de vérité. Cette omission localisée est F-SAV-004.

### Asset : rôle, provenance et preuve (558–560)

Les onze rôles possibles ne sont ni des obligations d’avoir onze assets ni des droits attachés à leur catégorie. L’identité, la donnée, le signal d’état ou le modèle spatial doit être observable dans la scène. La route de production est décidée en DIRECTION ; SOURCE porte provenance, transformation et contre-indication ; ACTION vérifie intégration, fallback, droits lorsqu’applicables, preuve et clôture. L’absence intentionnelle d’asset est licite ; sa représentation dans la taxonomie des routes demeure F-DIR-025. L’objet « preuve produit » ne prouve pas à lui seul la tâche ou la véracité (F-DIR-024), et provenance n’équivaut pas à permission de diffuser (F-ACT-024). La réserve generated-only de F-SAV-003 demeure si une identité à fort enjeu s’appuie uniquement sur une hypothèse générée.

### Portée par médium (562–564)

Les onze médiums sont un **index** ; la liste n’accorde aucun PASS Web à un dispositif natif, print ou spatial. Les cinq dimensions de CONTEXT — observation du rendu, idiomes d’interaction, référentiel, budget et preuve indisponible — sont ici des slots regroupables, pas cinq livrables supplémentaires obligatoires. ACTION 653 définit PASS dans la méthode/scope déclarés et CONTEXT 764–776 détaille la traduction hors Web. Si support de rendu ou test critique manque, `NOT-VERIFIED` et `NEXT-PROOF` sont requis ; `N/A-JUSTIFIED` ne s’applique qu’à une obligation réellement hors scope (F-DIR-038, F-ACT-004). La décision de norme/version n’est pas une preuve de conformité obtenue ; cet audit documentaire n’affirme aucun standard ou budget externe.

### Sélection, réemploi et frontière maintenance/design (566–570)

`DECISION-MODIFIED`, `WHEN-USEFUL`, `COUNTERINDICATION`, `MEDIUM-SCOPE` et `PROOF-LIMIT` sont des questions **avant** le build. Leur saisie locale ne crée pas une seconde RUN_CARD ; ACTION 232–236 reprend exactement le contrat. `DECISION-CHANGE` couvre décision effectivement changée, confirmée ou abandonnée après observation ; si un effet applicable manque, `NOT-OBSERVED`, pas une réussite inventée. Un contrôle hors scope peut être `N/A-JUSTIFIED`, selon la condition canonique ; ne pas utiliser N/A par commodité lorsque la décision est incertaine (F-ACT-013/014). `WHY-NOW` et `REUSE-CHALLENGE` sont exigés quand une famille ou un profil est repris d’un run antérieur, afin de vérifier que la décision du nouveau contexte justifie ce réemploi.

La phrase « reste une maintenance locale » en 570 concerne la **nécessité d’une famille design**, et non une permission de forcer `MODE=LITE`. Elle est précédée de 532 et de START 140 : une correction de nom accessible, état ou libellé sur un consentement, un paiement ou une récupération doit être reclassée si elle touche un risque critique. START 142 et DAILY 253–254 font silence sur l’atlas pour le micro-delta sans redéfinir les protections. Un lecteur pressé pourrait néanmoins généraliser la phrase isolée ; la présence de START en amont atténue ce risque. On conserve le scénario comme test de résistance de l’interface, sans nouvel ID tant que la lecture complète donne une issue univoque.

## Passage C — usage réel simulé

1. **Agent, correction de focus sur une carte non critique existante.** START établit que l’action et le risque critiques ne bougent pas ; la route locale corrige et prouve le focus sans nommer un profil ou charger l’ATLAS. Si la même carte est un consentement critique et que le focus modifie la confirmation, START reclassifie avant la route de preuve ; « local » ne dispense pas de protection.
2. **Designer, nouvel écran avec hiérarchie incertaine.** Après classification et décision, il utilise la famille Technique ou Structure seulement si cela peut déplacer un foyer ou clarifier une action ; il peut refuser un gradient séduisant dont aucune conséquence n’est observable.
3. **Mainteneur, token `danger` partagé Web/mobile.** Il arrive à la ligne 541 : `BIBLIOTHEQUE/COMPONENTS` et ACTION couvrent anatomie/migration, mais la cellule ne l’envoie pas explicitement vers SAVOIR/SYSTEM pour distinguer token primitif/sémantique, modes et source de vérité. ROUTING 78 ou ACTION 885 récupère la route si le lecteur les consulte ; c’est le contre-exemple F-SAV-004.
4. **Designer, image directrice.** Il nomme la fonction de l’asset, son crop et son fallback, puis vérifie provenance/droits dans SOURCE et l’effet sur le rendu ACTION ; aucune catégorie « identité » ou « preuve produit » n’autorise une publication ni ne prouve une tâche.
5. **Intégrateur, exposition print et mobile natif.** Il rassemble les cinq dimensions par médium en un paquet adapté ; épreuve print ne valide pas les idiomes tactiles, et un prototype simulé ne couvre pas automatiquement le support réel.
6. **Reviewer, réemploi d’un profil réussi auparavant.** Il demande `WHY-NOW` et `REUSE-CHALLENGE` ; la réussite passée n’est qu’une hypothèse transférable. Seul l’objet actuel et son observation peuvent confirmer une décision ; zéro famille reste acceptable.

## Passage D — résistance et constats

### F-SAV-004 — le renvoi « Structure / composant » omet la route de jugement systémique

- **Gravité provisoire : Significatif à éprouver.** L’omission textuelle est vérifiée ; sa fréquence et l’éventuel rattrapage par le routage principal demanderont un parcours réel.
- **Preuve :** SAVOIR 541 donne `BIBLIOTHEQUE/SELECT`, `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` pour le partagé mais pas `SAVOIR/SYSTEM`. SAVOIR 78 et 690–704 possèdent l’examen de token, modes et consumers ; ACTION 885 cite explicitement `SAVOIR/SYSTEM` pour token/composant/blast radius.
- **Mutation discriminante :** changement du token sémantique `danger` partagé entre Web et mobile, avec thème sombre, mode élevé contraste et plusieurs consumers. En suivant uniquement la cellule ATLAS, le run peut documenter structure, impact et migration mais ne pas examiner la séparation token primitif/sémantique, le comportement des modes et l’interopérabilité qui appartiennent à SAVOIR/SYSTEM. En ajoutant cette route, ces décisions ont un owner clair. Un composant purement local sans token partagé ne doit pas charger SYSTEM artificiellement.
- **Risque :** un index censé orienter la route spécialisée fournit une liste apparemment complète mais saute un propriétaire requis ; perte de jugement, incompatibilité de thèmes/consumers ou validation trop forte de la migration.
- **Atténuation :** `SAVOIR/ROUTING` et ACTION/ROUTING donnent bien la route ; la famille ATLAS ne prétend pas changer le mode et peut être lue comme un simple raccourci. Ne pas prétendre qu’un run complet suit systématiquement la mauvaise voie.
- **Propriétaire pressenti :** ligne de renvoi de `SAVOIR/DESIGN-ATLAS` ; DIRECTION reste owner de classification, SAVOIR/SYSTEM de jugement, BIBLIOTHEQUE de structure, ACTION de preuve/issue.
- **Relations sans fusion :** F-DIR-042 relève d’omissions et d’attributions erronées dans les tables de DIRECTION ; F-ACT-001 du routage machine/chargement ACTION ; F-SAV-001 du plafond implicite de routes. Même avec ces autres tables corrigées, la cellule locale 541 resterait lacunaire ; un test à son entrée est donc distinct.
- **Test futur :** trois parcours en aveugle — token partagé, composant partagé sans changement de token, composant local — depuis ATLAS et depuis ROUTING principal. Comparer routes chargées, décisions documentées, contrôle des modes/consumers et preuve de migration. Ne pas imposer `SAVOIR/SYSTEM` au troisième cas.

### Occurrences déjà ouvertes, sans nouveaux IDs

| Observation de ce bloc | Constat transporté |
|---|---|
| Plusieurs familles utiles peuvent nécessiter plus de deux routes, sans quota automatique | F-SAV-001 |
| « Preuve produit » est un rôle d’asset, pas preuve de tâche ; absence d’asset permise | F-DIR-024/025 |
| Médium hors Web : cible, méthode, scope et résultat ne se transfèrent pas sans contrôle | F-DIR-038, F-ACT-004 |
| Si l’ATLAS révèle un risque critique, le statut/owner/protection doit être recalculé | F-ACT-017/029 ; START 140 contrôle la reclassification |
| Champs présélection versus changement effectivement observé et trace machine | F-ACT-002/013/014/028 |
| Droits d’asset, même si rôle et provenance sont déclarés | F-ACT-024 |
| Section présente mais locator CLI refusé et validateur vert | F-DIR-028/F-ACT-001 |
| Ancre generated-only utilisée pour l’identité | F-SAV-003, sans nouvelle exception créée par l’ATLAS |

## Vérifications ciblées et acquis à protéger

Le hash B01 demeure stable sur les trois entrées. `read_route.py SAVOIR/DESIGN-ATLAS` refuse le locator ; `validate_reading_map.py` passe, conformément au défaut déjà observé. La vérification sémantique par scénario partagé/local montre précisément la divergence de renvoi ; elle ne démontre pas encore une erreur de production réelle. Aucune source externe de produit, norme ou plateforme n’est invoquée pour tirer une conclusion factuelle ; les sections de médium ne sont ici que des contrats du corpus.

1. Atlas optionnel et index non exhaustif ; zéro famille ou zéro asset est une issue valide.
2. Classification et risque avant esthétique ; aucune famille ne réduit une protection critique.
3. Technique ≠ effet ≠ preuve exécutée ; une présence décorative sans conséquence est retirée.
4. Asset observé avec rôle, provenance, droits, intégration et fallback distincts.
5. Présélection explicitement séparée de l’observation, `DECISION-CHANGE` et verdict.
6. Médiums variés, preuves adaptées au support et slots regroupables pour limiter la charge documentaire.
7. Maintenance locale silencieuse quand l’atlas ne modifie aucune décision, mais reclassification lorsque START détecte un risque critique touché.

## Couverture et reprise

| Passage | Profondeur | Résultat |
|---|---|---|
| A — architecture | FULL | Six familles, quatre sous-sections, propriétaires, locator refusé |
| B — contrat sémantique | FULL | Index, routage, rôles, médiums, champs pré/post, réemploi, risque |
| C — usage réel | TARGETED | Six scénarios contrastés incluant critique/local et partagé/local |
| D — résistance | TARGETED | F-SAV-004 provisoire ; huit occurrences rattachées aux constats antérieurs |
| Machine | TARGETED | Échec de la clé ATLAS, validation de carte verte ; aucun test redondant des schémas |
| Externe | N/A-JUSTIFIED ici | Aucun fait externe nécessaire à la lecture du contrat documentaire |

Bloc 8 terminé sans patch ni verdict global. La prochaine unité est **SAVOIR.md, lignes 574–689** : `SAVOIR/STYLE`, profils, taxonomie, dials, transfert culturel et test anti-slop. `SAVOIR/SYSTEM` commence à 690. Relire le §12, la baseline, ce rapport et les réserves sur profils/non-recyclage avant d’ouvrir ce bloc.
