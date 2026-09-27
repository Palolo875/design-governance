# Design Governance — Plan consolidé de la suite V1.2

27 septembre 2026 · Owner : Junior · Version du document : proposition consolidée 1

**Statut : prêt pour arbitrage et préparation de l’implémentation.** Ce document consolide le plan GitHub et la discussion. Il n’autorise pas à modifier le dépôt, à lancer des runs de design ni à publier. Les recommandations nouvelles restent proposées, même lorsqu’elles figurent dans la séquence d’exécution.

**Base vérifiée :** dépôt `Palolo875/design-governance`, branches `v1.2/patch-decision-abd` et `claude/init-repo-claude-md-gm6njm`, toutes deux au commit `89f4951ef88fbffb02588045c6abf4fee539946e`. Vérification renouvelée pour cette consolidation. `main` reste au commit `5cc85aa7659a847a6ef1ba7517baaec95598d958` ; elle ne représente pas l’état détaillé de la refonte examiné ici.

**Autorité :** le plan de refonte, son document de reprise et les décisions de l’owner restent les références. Cette proposition précise leur mise en œuvre ; elle ne les remplace pas silencieusement. Après validation, ses arbitrages devront être intégrés aux documents de reprise existants, sans créer plusieurs plans actifs concurrents.

## 1. Destination et priorités

V1.2 doit aider un agent et une personne, même novice, à obtenir un travail beau, vrai, situé et utilisable, avec une composition, un craft et une finition de niveau professionnel dès la première proposition. Le système doit soutenir des expressions variées : sobre, énergique, dense, ludique, chaleureuse ou expérimentale lorsque le contexte les justifie. « Senior » et « world class » désignent une ambition ; ils ne constituent pas une certification automatique.

La réussite repose sur quatre effets conjoints : une meilleure qualité de fabrication ; moins de reprises évitables ; une utilisation et une navigation plus simples ; une confiance fondée sur des observations et des limites honnêtes. Une version mieux documentée mais sans progrès de résultat ou d’usage ne suffit pas à réaliser cette ambition.

Chaque changement doit avoir un bénéfice explicable pour le résultat, le travail nécessaire, l’usage ou une protection essentielle. Les contrôles déjà obligatoires restent en vigueur ; on ne leur ajoute pas une campagne exhaustive sans risque concret à résoudre.

### La double boucle reste l’architecture centrale

| Boucle | Contribution | Ce qui doit rester opérant |
|---|---|---|
| Création | Comprendre le besoin, ouvrir une direction, mobiliser références et moyens, structurer, composer, construire et polir | Savoir-faire disponible au moment de fabriquer ; premier objet assez abouti pour être jugé ; expression adaptée au contexte |
| Gouvernance et amélioration | Observer le résultat, protéger les risques, identifier le défaut dominant, modifier, comparer et décider | Correction réelle de l’artefact ; possibilité de rouvrir une hypothèse ou la direction ; preuve proportionnée et limite explicite |

Les protections interviennent pendant la fabrication ; l’observation nourrit la création suivante. La formule du plan « fabriquer d’abord, prouver ensuite » organise la lecture et la formalisation, sans reporter tous les contrôles à la fin. La boucle d’édition canonique reste dans `DIRECTION/DOUBLE-LOOP` ; les autres passages y renvoient ou en sont des copies générées. Aucune troisième boucle ni équipe d’agents simulée n’est ajoutée.

### Critères de réussite

| Dimension | Critère retenu | Preuve et limite |
|---|---|---|
| Qualité initiale | Composition, hiérarchie, typographie, contenu, matière, interaction et états suffisamment résolus dès la première proposition | R10 : jugements sur les rendus, reliés au brief ; une capture ne démontre pas tout l’usage |
| Spécificité et diversité | Les choix répondent au produit et au public, sans style maison imposé | Comparaisons de structures, typographies, palettes et relations au contenu |
| Efficience | Meilleur résultat avec une charge totale raisonnable, en incluant fabrication, lecture et corrections | Tokens et lignes réellement lus ; proposer de relever aussi les reprises et le temps jusqu’à une proposition jugeable, si disponibles sans instrumentation lourde |
| Accessibilité du système | Un novice peut commencer avec son objectif et ses moyens ; l’expert retrouve les détails utiles | Revue du parcours R6b ; observation humaine à rattacher à R10 si possible, sinon bénéfice novice non démontré |
| Confiance | Contenus d’exemple identifiables, capacités et plafonds déclarés, aucune observation inventée | Gardes existantes et examen des rendus/traces |
| Cohérence | Un propriétaire par règle, routes résolubles, noyau compilé fidèle, distributions autonomes | Validateurs et non-régression prévus par le dépôt |

Les cibles historiques restent des hypothèses : V1.2 meilleure que sans système et que V1.1.1, diversité tenue, coût en tokens visé ≤ 1,3 fois sans système. Les budgets documentaires servent à diagnostiquer la charge. La consigne plus récente « qualité avant nombre de mots » interdit de couper un geste utile pour satisfaire artificiellement un plafond.

## 2. État de départ : conserver les acquis

Les états ci-dessous proviennent du plan de reprise après R6a et des rapports cités. Aucun test n’a été rejoué pour produire ce document.

| Lot | État rapporté | À ne pas refaire |
|---|---|---|
| R1–R3 | Mesure, gardes de propriété et alignements appliqués | Réinventer les instruments ou le vocabulaire déjà aligné |
| R4 | Noyau de fabrication compilé ; liste de chargement unique ; réponse en langage produit | Écrire un second noyau à la main |
| P1 | Mini-épreuve terminée, orientation positive mais limitée | Relancer une mini-épreuve pendant la phase actuelle |
| R5b-1 et R5b-2 | Trace légère, checkpoint par première proposition, contenu d’exemple marqué, Gate A par profil, Gate C en gestes, boucle et promesse du validateur consolidées | Ajouter de nouveau ces mécanismes |
| R5a | Rôle et posture remontés, entrée unique, D-17 et D-19 traités | Refaire la réorganisation déjà appliquée |
| R8a | Convergence typographique traitée | Réintroduire une nouvelle règle équivalente |
| R5c partiel | Modèle de niveaux unifié ; boucle et one-shot en renvoi | Présenter D-16 comme encore à résoudre |
| R5d partiel | Boucle en renvoi ; contrôle perceptif F22 relié à Gate C | Traiter F22 comme encore hors chemin |
| R6a | Boucle du README en renvoi et glossaire enrichi | Réouvrir les exemptions de boucle déjà levées |

Mesures rapportées après R6a : chemin prescrit de 12 076 mots en trace légère et 16 687 en trace complète ; noyau de 3 222 mots ; une liste de chargement ; 24/25 outils de fabrication sur le chemin ; suivi vert, 372 cas maintenus et 17 migrés. Ces mesures statiques ne démontrent ni le coût réel d’un run ni son efficacité.

Les chiffres 24/25 et le traitement de F22 doivent être rapprochés lors de la prochaine mesure : ne pas inventer un outil manquant ni annoncer 25/25 sans identifier les entrées de la mesure. Les sections de dette anciennes du plan de reprise et certains résumés de `CLAUDE.md` doivent être actualisés depuis les rapports, notamment pour D-16, F22 et les exemptions déjà retirées.

## 3. Arbitrages avant les lots concernés

| Référence | Recommandation consolidée | Conséquence et statut |
|---|---|---|
| Décision 6 — ancres | Autoriser une proposition exploratoire avec absence d’ancre déclarée ; exiger une ancre observée ou fournie avant acceptation d’une direction destinée à un produit réel | Précise le moment où l’exigence bloque. À valider : le plan initial ne distingue pas assez clairement première proposition et acceptation |
| Décision 3 — version | V1.2.0 si le nouveau système accepte les anciennes cartes valides selon le contrat convenu ; sinon V1.3.0, conformément à l’option du plan | Définir la direction de compatibilité ; les anciens validateurs peuvent refuser les nouveaux champs. À valider avant R9 |
| Périmètre R9 | Différer `trace_level` et `fabrication` tant qu’aucun consommateur machine n’en a besoin ; garder l’alignement `MODAL`/`PARTI` comme option limitée | Réduction proposée du périmètre initial, non encore décidée. Le maintien du schéma actuel reste une option explicite |
| Décision 8 — lois de SAVOIR | Conserver les lois ; examiner l’hypothèse de biais vers la retenue dans R10 | Aucun ajout de règle de pluralité, déjà présente. Proposition conforme à l’option du plan |
| Décision 9 — juges | Viser regards humains extérieurs et modèles d’autres familles ; conserver une voie avec réserve si aucun juge D3 n’est disponible | Pas d’équivalence entre critique par modèle et indépendance D3 ; publication éventuelle sous réserve et feu vert final. À valider |
| Décision 10 — catalogue | Différer l’extension générale après publication, depuis des usages réels ; conserver la dérivation locale | Aucun obstacle à concevoir un cas absent du catalogue. Proposition conforme à l’option du plan |
| R11 — tests | Compléter les lacunes prioritaires après vérification des autres harnais ; maintenir explicitement les autres réserves | Réduction ciblée proposée, sans supprimer les contrôles obligatoires existants |
| R11 — placeholders | Maintenir la réserve sur les champs libres ; conserver les filtres existants | Aucun filtre global ajouté sans incident ou besoin concret ; distinct de D-20 |
| R8b — calendrier de l’atlas | Préparer une référence conditionnelle pour R10 selon le plan de reprise actuel | Rendre explicite l’articulation avec G1 et l’atlas v0 qui reportaient l’intégration après G4 ; résoudre ce décalage avant intégration, sans déclarer un ancien accord annulé par supposition |

Les décisions déjà prises 1, 2, 4, 5, 7 et 11, ainsi que D-20 et D-22, sont conservées. L’autorisation de préparer ce plan ne vaut ni validation en bloc de ces arbitrages ni autorisation de modifier le dépôt.

## 4. R8b — Matériaux et atlas : améliorer directement la fabrication

**Objectif.** Aider à trouver, choisir, transformer et intégrer des matériaux de qualité au moment où une décision reste ouverte. Donner à la fabrication des ressources concrètes, sans catalogue esthétique obligatoire.

**Existant.** La carte des moyens datée, le bilan `FABRICATION`, les routes de production, le traitement des assets moyens et les marqueurs de convergence existent déjà. `SAVOIR/DESIGN-ATLAS` est un index de familles et de responsabilités ; il est distinct de l’atlas de références visuelles prévu dans la skill.

**Travail proposé.** Consolider la carte à partir de `plans/carte_moyens_v0.md` et du bloc propriétaire de SAVOIR. Associer les moyens aux décisions qu’ils rendent possibles, au plafond et aux limites d’usage. Conserver des sources datées plutôt que des familles visuelles imposées. Vérifier les informations et licences pertinentes au moment d’intégrer ou d’utiliser une ressource ; ne pas déduire une autorisation générale du nom d’une plateforme.

Aligner le brouillon avec D-20/CNT-01 : sa ligne « contenu réel : sinon emplacements marqués » ne doit pas rétablir une obligation générale de trous vides si un contenu d’exemple clairement identifié est déjà autorisé. Ne pas rouvrir la prise de brief ou ajouter des demandes systématiques.

Pour l’atlas, repartir des 18 entrées de `plans/atlas_references_v0.md` (10 références, 8 contre-exemples), sans quota nouveau. Plusieurs entrées regroupent plusieurs pièces ; les liens sont absents. Les descriptions historiques ne remplacent pas l’inspection des originaux. Retrouver les pièces exactes, leurs sources et leur contexte ; si une référence demeure introuvable, la conserver comme matériau non vérifié hors atlas opérationnel.

Chaque entrée exploitable doit permettre de comprendre la leçon visuelle, la relation au produit/contenu, une décision transférable, une contre-indication et les limites. Préserver les deux colonnes visuel/fond. Traiter les « principes observés » du brouillon — palette restreinte, deux familles de polices, texture — comme observations situées, jamais comme lois supplémentaires. Inclure des références hors du canon occidental comme prévu, sans prétendre qu’une origine géographique garantit la diversité.

**Emplacement.** Référence conditionnelle de `skills/design-governance-practice/references/`, appelée lorsque la décision visuelle est ouverte. Les critères restent chez leurs propriétaires ; le noyau garde le renvoi utile. Vérifier manifestes et distributions si un fichier est ajouté. Le nom exact du fichier sera fixé dans le patch.

**Réussite technique.** Sources inspectables, annotations bornées, route accessible au bon moment, aucun chargement universel, noyau recompilé et distribution complète. **Réussite d’effet : R10**, sans l’anticiper. Si l’atlas diminue la diversité, retirer les exemples et conserver les critères selon la règle existante. Si les originaux manquent, terminer la carte et déclarer l’atlas incomplet plutôt que l’inventer.

## 5. R11 — Réserves ciblées, puis revue finale avant publication

R11 est scindé en traitement documentaire/test ciblé avant R10 et clôture des preuves de livraison après R10. Le tri un par un reste obligatoire ; il n’impose pas une correction de tous les signalements.

### Disposition proposée des Q et de DAILY

| Point | Constat issu de la lecture | Traitement proposé |
|---|---|---|
| Q04 | « Forme seule » dans le tableau ITER/STANDARD masque les contrôles déjà présents sur `decision_change` | Préciser champs projetés contrôlés et paquet complet non vérifié ; aucun nouvel invariant |
| Q07 | `artifact.scope` et `direction.scope` existent, relation insuffisamment explicitée | Clarifier leur correspondance depuis les usages existants ; ne pas inventer une égalité ni deux sens distincts. Si changement machine nécessaire, reporter à R9 |
| Q08 | « Sortie définie une seule fois » est trop absolu | Désigner CLOSE-PACKAGE comme référence des sorties ; garder les renvois utiles |
| Q09 | Arrêt après première observation et B1b doivent s’articuler explicitement | Rappeler B1b dans son périmètre et ses deux exceptions ; absence d’amélioration utile ≠ absence de décision éditable |
| Q11 | Droits inconnus : pas de contradiction de fond démontrée après lecture des réserves structurées et de la limite de diffusion | Maintien motivé ; renvoi de lisibilité seulement si utile |
| Q12 | Forme courte du tag et forme qualifiée par le scope, avec explication existante | Pas de nouvelle règle ; précision de légende facultative |
| Q13 | Occurrences exactes non retrouvées dans les résumés consultés | Ouvert, source détaillée requise |
| DAILY | L’absence de gates LITE/ITER a été corrigée en R4 ; un ancien renvoi `DAILY` reste dans DIRECTION | Enregistrer le correctif historique ; remplacer le renvoi résiduel par CHARGE selon la migration existante |
| R16–R32 | Dix-sept signalements transmis sans détail exploitable dans les rapports consultés | Retrouver les traces, puis décider un par un ; aucun statut « corrigé » ou « obsolète » par supposition |

Sources manquantes ciblées : `audit/logs/DG_AUDIT_001_Journaux_R02.zip` pour la revue Q et `audit/logs/DG_AUDIT_001_Epreuves_13-02_traces.zip` pour les R. Le connecteur utilisé n’a pas permis leur lecture binaire dans cette analyse. Une extraction autorisée ou les fichiers texte de revue permettront de compléter le tri. Ces manques n’empêchent pas les lots indépendants, mais interdisent de déclarer R11 entièrement soldé.

### Tests négatifs

La réserve « environ 14 » vient de diagnostics anciens non couverts individuellement, pas de quatorze règles absentes. La suite native examinée comporte 76 cas unitaires ; ce n’est pas une preuve de couverture exhaustive.

Réutiliser la liste close et la table de correspondance. Vérifier d’abord les autres harnais. Priorité proposée : cohérence du locator preuve/artefact ; séparation entre `observed` et `not_verified` ; complétude de la protection critique et action d’échec valide. Ajouter uniquement les cas manquants retenus, avec base valide, faute isolée et motif attendu. Conserver explicitement le reliquat si le coût dépasse le gain.

Tenir compte des règles remplacées : ancres absentes couvertes en partie par B4, conséquence décisionnelle généralisée par C1, typage vérifié avant certains diagnostics métier. Ne pas restaurer INV-E11, interdiction volontairement retirée de l’ancre transformée sous verdict de retour.

### Placeholders et neuf réserves

Conserver les filtres déjà appliqués aux champs sensibles des contrats. Maintenir la limite des champs libres tels que `domain` ou `research_question` tant qu’aucun besoin n’établit l’intérêt d’un filtre supplémentaire. Une chaîne non placeholder ne garantit pas un bon cadrage.

| Réserve de clôture | Destination proposée |
|---|---|
| 1 — efficacité | R10 ; demeure non établie hors preuves disponibles |
| 2 — CI hébergée | R11 final sur la candidate distribuable |
| 3 — cas négatifs manquants | Complément ciblé et maintien écrit du reliquat |
| 4 — seize limites forme/effet | Conserver ; distinguer les effets réellement évalués par R10 |
| 5 — promesse du validateur | Limite permanente de conception, déjà consolidée dans ACTION |
| 6 — coût d’un run | Mesures statiques par lot ; coût réel dans R10 |
| 7 — placeholders libres | Maintien proposé |
| 8 — mineurs | Tableau ci-dessus, puis sources Q13/R16–R32 |
| 9 — publication | R12 ; pas de publication intermédiaire V1.1.1 créée pour solder artificiellement l’historique |

**CI.** Lors de la consultation du 27 septembre, l’API des runs renvoyait zéro exécution. Le workflow fourni est dans `package/.github/workflows/validate.yml` et le build le place à la racine de la distribution GitHub. Il prévoit Python 3.11, actions épinglées et `validate_all.py`. Obtenir une exécution hébergée verte sur la candidate distribuable et conserver URL, SHA du commit, versions effectives, conclusion et empreintes. Une CI ajoutée au dépôt de travail est une option distincte ; ne pas déplacer sa structure par défaut.

## 6. R6b — Une entrée humaine simple et une profondeur progressive

**Objectif.** Permettre de commencer sans connaître les modes, les gates ou le schéma, tout en laissant au professionnel l’accès aux décisions et aux preuves.

Fusionner les deux présentations README du package en une présentation principale. Le README de la racine du dépôt de travail, qui a une fonction de reprise, n’est pas automatiquement la cible de cette fusion. Un ancien chemin peut devenir un simple pointeur de compatibilité si des liens en dépendent ; il ne doit pas conserver une seconde présentation normative.

Recomposer le QUICKSTART autour d’une seule activation humaine : résultat souhaité, périmètre, moyens disponibles, contraintes et autonomie. Réutiliser les éléments utiles du handoff agentique et la prise de brief déjà décidée. L’agent choisit le mode et tient la trace. Conserver une voie de consultation experte sans imposer ses champs au novice.

Expliquer la première proposition, le retour utilisateur et l’amélioration par la double boucle. Rendre visible la différence entre proposition exploratoire et acceptation/clôture complète. Remplacer les démarrages concurrents « 90 secondes », « trente secondes », « cinq minutes » par un parcours commun avec approfondissement facultatif. Préserver l’exemple utile, en lecture complémentaire.

Réduire READING_MAP au chemin et aux locators, en y conservant ce qui est utile de l’orientation par résultat d’ORCHESTRATION_MAP. Cette fusion ne doit pas recréer une seconde table de chargement : CHARGE reste propriétaire. Le principe « un axe situé à la fois » est déjà dans le noyau, il n’est pas à déplacer de nouveau.

**Impacts techniques.** Adapter de manière déclarée les attentes de `validate_design_governance.py`, les LCF, les liens, le manifeste et le README Local généré par le build. Préserver l’autorité des cinq sources, l’introduction de la RUN_CARD et les limites de validation, au lieu de protéger des phrases devenues inutiles. Ne pas renommer un locator sans migration explicite.

**Réussite.** Une entrée humaine identifiable, une entrée agent par la skill, aucune règle redéfinie dans une façade, chemins GitHub et Local cohérents. Une revue documentaire peut établir cette structure ; la facilité réelle pour un novice reste à observer. Si le coût de migration des harnais dépasse les changements de texte, appliquer l’arrêt prévu par le plan.

## 7. Restes de R5 — Jugement accessible, maintenance à sa place

### R5c : SAVOIR et la trace

Supprimer la copie du handoff à douze champs au profit du renvoi à ACTION. Conserver près du cadrage les questions sur la nature d’une hypothèse, sa source et le coût d’erreur. Consolider les raccords atlas/style : les champs de présélection et leur rapport à DECISION-CHANGE sont déjà décrits dans ACTION.

SAVOIR garde les critères permettant de choisir une famille ou un profil ; ACTION possède l’enregistrement et le passage intention/observation. Relier la formalisation au niveau de trace existant. Ne pas déplacer en bloc la fiche de recherche : provenance, transformation et limites contribuent aussi au jugement de source. Aucun nouveau formulaire.

### R5d : BIBLIOTHEQUE et la maintenance

Placer les catégories de lecture instrumentée et les procédures détaillées de promotion dans une partie de maintenance clairement séparée. Garder à proximité de la fabrication les critères de dérivation locale et les responsabilités réellement activées par un changement partagé. Préserver les locators CONTRACTS et EVOLUTION, leur accessibilité et leur fonction.

Dans PRINT_FIELD, ajouter un renvoi ciblé aux marqueurs de veille et à la question de convergence existante. La route possède déjà rôle, test de retrait, contraste, accessibilité et robustesse : aucun nouvel interdit sur le grain, la trame ou les hachures.

### Doublons transversaux

Traiter les répétitions d’alternative située et les raccords de trace dans le lot du propriétaire. Traiter les répétitions ANCHOR-GENERATED après l’arbitrage 6, pour ne pas réécrire deux fois le même sens. Modifier les sources, puis recompiler le noyau ; ne jamais retoucher sa copie à la main. La carte de lecture d’ACTION reste conservée tant que sa migration propre n’est pas décidée.

**Réussite commune.** Les questions de fabrication restent atteignables ; la maintenance ne s’impose pas à un run local ; les renvois se résolvent ; les obligations de trace ne contredisent plus leur niveau applicable. Aucun gain de temps réel n’est déclaré à partir du seul déplacement de paragraphes.

## 8. R7 — Orientation après arbitrage

### Ancres

Appliquer uniquement la décision 6 effectivement retenue. La proposition consolidée autorise l’exploration avec limite déclarée et exige une calibration observée ou fournie avant acceptation pour une destination réelle. Une ancre fournie pertinente peut éviter une recherche Web systématique ; une image séduisante ne devient pas une preuve d’usage ni un droit de réemploi.

Aligner DIRECTION, ACTION, SAVOIR et leurs façades à partir d’un propriétaire canonique. Garder les types d’ancre et les réserves existants. Le validateur refuse actuellement une DIRECTION acceptée sans ancre ; l’exploration sans ancre peut conserver cette protection. Le schéma ne possède pas de champ destination : le critère proposé de destination réelle relèverait d’abord de la trace et de la revue. Toute automatisation supplémentaire doit être décidée en R9, sans la prétendre déjà assurée.

### Lois et catalogue

Si les décisions 8 et 10 recommandées sont retenues : laisser les lois de SAVOIR inchangées jusqu’à l’épreuve ; maintenir la pluralité déjà écrite ; reporter l’extension du catalogue après publication à partir de runs réels et de candidates PILOT. L’observation d’une convergence ne permet pas, seule, de l’attribuer aux lois. Une comparaison ciblée ne sera envisagée qu’après un signal concret dans R10.

## 9. R9 — Trace machine utile et compatibilité explicite

**Constat.** La trace légère actuelle ne produit pas de RUN_CARD. `FABRICATION` vit déjà dans la trace ; `capability_profile` concerne l’observation. `anti_direction` transporte aujourd’hui le modal et le parti selon la correspondance d’ACTION, mais les cartes historiques ne distinguent pas nécessairement ces notions.

**Option recommandée.** Différer `trace_level` et un objet `fabrication` sans besoin machine établi. Pour MODAL/PARTI, décider entre maintien explicite de la projection actuelle et ajout compatible de champs dédiés. Ne pas imposer cette extension seulement pour moderniser les noms.

Si les champs sont ajoutés : préciser leur forme, le cas legacy, la priorité en présence des deux représentations et le traitement d’une contradiction. Une ancienne anti-direction ne permet pas d’inventer automatiquement un modal et un parti détaillés. Tester lecture des cartes antérieures, cartes nouvelles et coexistence ; documenter que les anciens validateurs fermés aux champs inconnus ne liront pas nécessairement les nouvelles cartes.

**Sortie.** Schéma conservé par décision, ou migration bornée avec compatibilité et version établies. Aucun champ ne doit diminuer les exigences d’acceptation par simple valeur `light`. Si un consommateur réel rend nécessaire un périmètre plus large, revenir à la décision de lot avant de l’étendre.

## 10. R10 — Évaluer le résultat, la diversité et le coût

R10 est préparé ici, pas exécuté. La consigne « pas de run réel ni de mini-épreuve dans cette phase » reste en vigueur jusqu’au passage explicite à la phase d’évaluation.

### Protocole de référence à finaliser

Le plan prévoit quatre briefs actifs : commerce à Douala (B-DLA), SaaS, service public et portfolio ; B-LOG reste reporté. Conditions : C1 brief vague sans système ; C2 brief riche et assets sans système ; C3 brief vague avec V1.2 ; C3r avec destination réelle ; C4 avec V1.1.1. À trois répétitions par condition et brief, cela représente **60 productions prévues** (calcul : 4 × 5 × 3), avant le travail de jugement.

Ce volume est conséquent. Le plan final ne le réduit pas silencieusement. Confirmer le budget avant lancement ; une exécution par blocs avec arrêt diagnostique peut limiter le gaspillage, mais une réduction de briefs, conditions ou répétitions devra être déclarée avec sa perte de portée. Les anciennes captures ne sont réutilisables que si les conditions restent suffisamment comparables ; sinon les traiter comme contexte historique.

Fixer avant production : versions du package et du modèle producteur, outils et capacités, briefs, assets, réponses d’intake, règles de coût, destinations et méthodes de capture. Rendre les comparaisons explicables : C3/C1 et C3/C4 portent sur l’apport de V1.2 ; C2 éclaire l’effet des intrants ; C3r examine le comportement en destination réelle.

### Jugement et aveugle

Présenter le besoin réel et des rendus anonymisés, avec ordre et côté aléatoires ; conserver la clé jusqu’à remise des jugements. Éviter de fournir les rationales du producteur comme argument de qualité. Distinguer anonymisation prévue et exposition réellement contrôlée.

Recommandation : regards extérieurs et modèles d’autres familles, avec relation et exposition déclarées. D3 exige un reviewer autre que l’auteur du rendu, externe ou collaborateur non impliqué, sans conflit déclaré pour le label indépendant. Ni une seconde session ni une autre famille de modèles ne reçoit automatiquement ce label. Sans D3, conserver une évaluation d’orientation et la réserve ; aucune clôture FULL d’efficacité. Une publication avec réserve reste à décider, pas automatique.

### Lecture des résultats

Conserver préférence par paires, diversité, défauts de vérité, tokens, lignes lues et plafonds déclarés. Examiner la qualité de composition, la spécificité, le craft et la finition à travers les observations des juges, sans créer un score esthétique normatif supplémentaire. Les briefs doivent permettre des expressions différentes pour que l’hypothèse de retenue puisse être examinée.

Proposition complémentaire légère : relever les reprises nécessaires et le délai jusqu’à une proposition jugeable quand les traces le permettent. Pour l’ambition novice, rattacher une observation du parcours d’activation au même dispositif si possible ; sinon maintenir cette limite d’efficacité humaine.

Un résultat favorable doit montrer un avantage de C3 sur C1 et C4, avec diversité tenue et honnêteté conservée. Si C3 reste proche de C4, le plan prescrit diagnostic plutôt que publication. Si les exemples de l’atlas réduisent la diversité, les retirer et conserver les critères. Un coût au-dessus de la cible nécessite une décision explicite fondée sur le gain observé ; un nombre de mots plus faible ne suffit pas à prouver l’économie.

Les résultats s’appliquent aux briefs, modèles et moyens testés. Une préférence visuelle ne prouve pas l’usage, l’accessibilité ou une supériorité universelle. Un effet attribué aux lois ou à l’atlas demande un diagnostic capable de distinguer ces causes des intrants et du modèle.

## 11. R12 — Livrer une candidate vérifiée et ses limites

Après R10, finaliser R11 : décisions sur toutes les réserves, sources manquantes traitées ou maintenues explicitement, exécution CI hébergée de la candidate. Si une réserve inconnue peut affecter un critère bloquant, ne pas l’écarter au seul motif qu’elle était classée mineure historiquement.

Relever la version selon l’arbitrage 3 ; compléter CHANGELOG et notes de version ; générer distributions GitHub/Local et éventuels livrables prévus ; vérifier manifestes, liens et reproductibilité ; produire les SHA-256 et le dossier de clôture V1.2. Conserver les versions et artefacts de preuve qui permettent de rattacher les conclusions à la candidate publiée. Une modification fonctionnelle après l’épreuve demande une évaluation de son impact avant de réutiliser les résultats.

La publication exige le feu vert final de l’owner. Le paquet publié ne doit pas promettre une indépendance, une qualité ou une efficacité plus forte que celle établie. Ne pas publier V1.1.1 seulement pour satisfaire un ancien libellé de réserve.

## 12. Séquence d’implémentation proposée

L’ordre de reprise est conservé ; R11 est réparti pour ne pas retarder les lots indépendants avec des sources indisponibles. Le découpage ci-dessous précise les unités, sans créer de nouveaux lots normatifs.

| Ordre | Unité | Dépendance principale | Livrable de sortie |
|---|---|---|---|
| 0 | Intégrer les arbitrages validés et nettoyer le statut de reprise | Autorisation d’implémenter ; décisions écrites | Un état de référence cohérent, sans nouvelle autorité documentaire |
| 1 | R8b : carte consolidée puis atlas conditionnel | Sources inspectables ; calendrier atlas clarifié | Moyens utilisables et corpus annoté borné, ou incomplétude déclarée |
| 2 | R11 initial : Q, DAILY, tests prioritaires, placeholders | Tri disponible et périmètre de tests décidé | Correctifs ciblés et registre des réserves actualisé |
| 3 | R6b : README/QUICKSTART puis cartes de lecture | Propriétaires et trace légère inchangés | Une entrée humaine et une navigation cohérente |
| 4 | Restes R5c/R5d | Contenus conservés identifiés | Trace consolidée, maintenance séparée, PRINT_FIELD relié |
| 5 | R7 : ancres et doublons dépendants ; dispositions lois/catalogue | Décisions 6, 8, 10 | Textes alignés sans modification implicite des verdicts |
| 6 | R9, ou report explicite | Décision 3 et périmètre machine | Contrat compatible et version déterminée, ou maintien du schéma |
| 7 | Préparation finale puis exécution de R10 | Candidate stable ; décision 9 ; budget et lancement autorisés | Résultats bornés et décision de poursuite |
| 8 | R11 final | Résultats R10 et candidate de distribution | CI, réserves finales et éléments de clôture |
| 9 | R12 | Critères atteints ou écarts autorisés ; feu vert final | Version publiée, archives et empreintes |

La préparation des sources manquantes peut avancer indépendamment ; cela n’autorise pas à recruter des juges, lancer des agents ou publier sans instruction correspondante. Aucun délai chiffré n’est inventé : R8b dépend des références disponibles et R10 constitue la charge dominante en production et jugement.

## 13. Méthode d’application et contrôles

Pour chaque unité autorisée, reprendre la recette existante plutôt que créer un protocole concurrent : décision écrite ; patch exécutable avec anciens/nouveaux textes exacts ; gardes pertinentes rouges avant, vertes après, mutation rouge ; compilation du noyau ; suivi et rapport allégé.

B01 demeure en lecture seule avec 218/218 à chaque unité. Tests et builds se font sur copies selon les consignes du dépôt. Préserver `validate_all`, `validate_structure`, `build_core --check`, `validate_reading_map`, la table de correspondance des harnais, R/R03, 13.01 et les 38 épreuves déterministes 13.02. Ces dernières sont des contrôles de package, distincts des runs réels différés. Utiliser le suivi de refonte pour éviter de lancer inutilement plusieurs fois les mêmes contrôles déjà englobés, sans retirer une exigence.

Les cas sensibles à la prose ne sont migrés qu’avec propriété conservée ou obsolescence décidée, justification et preuve de remplacement. Si leur rectification coûte davantage que le changement utile, appliquer le critère d’arrêt existant. Ne pas transformer la recherche d’efficacité en suppression silencieuse des garanties.

Mesurer chargement, atteignabilité et doublons après chaque lot ; expliquer les ajouts utiles, sans coupe automatique du savoir-faire. Actualiser le plan de reprise, le statut du plan maître et `CLAUDE.md`, en supprimant les dettes obsolètes. Continuer sur les deux branches de travail prévues ; une branche par lot n’est pas créée automatiquement. Les commits et envois au dépôt relèveront de l’autorisation future d’implémentation, pas de la création de ce document.

## 14. Limites et traçabilité

**Certain dans cette consolidation :** les branches consultées n’ont pas changé ; le plan et son état de reprise ont été relus ; les travaux déjà appliqués sont distingués des recommandations ; les écarts proposés sont nommés.

**Probable :** les simplifications ciblées réduiront la friction et le risque de duplication ; les moyens mieux accessibles aideront la fabrication.

**À démontrer :** qualité supérieure, diversité, économie réelle, utilité pour les novices et effet des lois ou de l’atlas. Cette analyse n’est pas une revue indépendante D3. Aucune inspection nouvelle des images originales de l’atlas, aucun run de design, aucun test de package et aucune modification du dépôt n’ont été réalisés pour ce plan.

### Sources principales au commit examiné

- [Plan V1.2 de refonte](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/plans/Plan_V1.2_Refonte.md)
- [Plan de reprise après R6a](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/plans/Plan_V1.2_Suite_Reprise.md)
- [État et méthode du dépôt](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/CLAUDE.md)
- [Atlas v0](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/plans/atlas_references_v0.md) et [carte des moyens v0](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/plans/carte_moyens_v0.md)
- [Application du lot 2 et calendrier historique de l’atlas](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/audit/reports/V12_04_LOT2_G_H_I_D.md)
- [Sources normatives et façades](https://github.com/Palolo875/design-governance/tree/89f4951ef88fbffb02588045c6abf4fee539946e/package/V1/official)
- [Validateur RUN_CARD](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/package/scripts/validate_run_card.py) et [schéma](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/package/schemas/run_card.schema.json)
- [Clôture DG-AUDIT-001 et neuf réserves](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md)
- [Origine de la réserve de couverture, phase 12.02](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/audit/reports/Audit_Phase12_02_PATCH_A2_Oracles_de_test.md)
- [Protocole de référence et amendement des juges](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/plans/Protocole_Epreuve_Reference_V1.2.md)
- [Décision D3 et indépendance](https://github.com/Palolo875/design-governance/blob/89f4951ef88fbffb02588045c6abf4fee539946e/audit/reports/Audit_Phase11_19_PATCH_DECISION_D3_Autorite_droits_gates.md)

Les rapports V12R_01 à V12R_12 portent les applications historiques. Les analyses Q/R de ce document proviennent de la lecture effectuée pendant la discussion, au même commit. Lors de la reprise, toute évolution du dépôt impose de comparer les fichiers concernés avant d’appliquer les propositions.
