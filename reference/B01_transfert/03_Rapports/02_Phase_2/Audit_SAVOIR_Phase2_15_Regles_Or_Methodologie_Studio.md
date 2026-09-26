# DG-AUDIT-001 — Phase 2 — SAVOIR, bloc 15 : règles d’or et méthodologie studio

## Cadre et point de reprise

- Source propriétaire : `audit_work/package/V1/official/SAVOIR.md`, lignes **906–941** ; règles d’or 906–917, méthodologie studio 921–940. Ce bloc achève la **lecture sectionnelle** des 941 lignes de SAVOIR ; son checkpoint consolidé reste une étape distincte.
- Protocole externe v2.0, §12 relu : quatre passages A (architecture), B (contrat), C (lecteurs), D (résistance). Point de reprise : rapport SAVOIR bloc 14, rapports SAVOIR blocs 1–13, checkpoints DIRECTION/ACTION. Interfaces relues : `DIRECTION/START` 119–144, `VISUAL_TARGET` 392–419 et absolu 2 en 577–591 ; `ACTION/PIPELINE-DIRECTION` 452–483 et 507–523, `STATUS` 125–175, `OVERRIDE` 806–828 ; `SAVOIR/CRAFT` 195–214 et `SOURCE` 471–477.
- Baseline B01 revérifiée : compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; SAVOIR propriétaire `41cb6f6e7cfcca4631f8701436055606c078f47d548eca6bc21e49a76e884820`.
- Aucune modification du système ; diagnostic local provisoire. L’achèvement de lecture d’un propriétaire ne vaut ni diagnostic global, ni autorisation de patch.

## Passage A — architecture et statut de lecture

La « lecture rapide » annonce expressément qu’elle **n’est pas une procédure de livraison** (908). Ses huit règles résument un ordre : classer le mode, cadrer, retirer le superflu, employer le contenu réel, protéger les contraintes critiques, préparer ancre/spec, exécuter preuves, qualifier la sortie (910–917). Elles empruntent des obligations à plusieurs propriétaires : DIRECTION classe, SAVOIR juge, BIBLIOTHEQUE structure, ACTION vérifie et clôt (908, 938). Le résumé ne peut créer de route, gate, issue ou verdict ; un lecteur doit remonter au propriétaire lorsque l’applicabilité ou la preuve est contestée.

La « méthodologie studio » est marquée `[MÉTHODE]` (923), donc sa liste 925–932 guide l’enchaînement selon le **mode et le risque**, sans transformer huit lignes en étapes obligatoires à toute correction. Une direction se prépare si le mode est `DIRECTION` ; un système s’ouvre si la décision a un blast radius partagé ; un contrat de composant si le pattern est réutilisable ou critique. L’assemblage, la repasse, les QA/gates applicables et la persistance gardent leurs propriétaires. La fin 938 répète le refus d’une seconde taxonomie.

Il n’existe pas de locator `SAVOIR/Règles d’or` à charger : ces deux passages sont délibérément **résumés**, et non routes spécialisées. `read_route.py SAVOIR/READ` charge la route d’entrée et `validate_reading_map.py` passe. Cette validation de la carte ne prouve ni l’applicabilité correcte de la règle 6, ni la résolution de toutes les routes spécialisées déjà relevée sous F-DIR-028/F-ACT-001.

## Passage B — contrat sémantique, phrase par phrase

### Huit règles d’or (906–917)

1. **Classer et cadrer (910–911).** Le renvoi à `DIRECTION/START` respecte la propriété des modes et la protection du risque critique. Le cadrage JTBD, décision dominante, contraintes et hypothèses à impact prépare la décision ; il n’invente ni résultat de test, ni approbation d’un owner.
2. **Retirer et employer le réel (912–913).** Le retrait avant ajout est une heuristique de hiérarchie, pas une injonction de retirer un état, une information ou une affordance nécessaires. Contenu réel, états pertinents et microcopie honnête permettent de juger une scène construite ; des placeholders peuvent encore être honnêtement déclarés pour un prototype, sans faire croire à une donnée observée ou à un asset authentique (INTEGRITY 894).
3. **Prioriser les protections (914).** Accessibilité, responsive, récupération et performance précèdent l’effet quand leur risque est applicable ; l’énumération ne suffit pas à décider d’une technique Web universelle pour un médium imprimé, natif ou non visuel. La portée est fixée par la surface et les contrats spécialisés (F-DIR-038).
4. **Ancre et spec en `DIRECTION` (915).** La formule « lorsque le contrat ou le risque le requiert ; sinon justifie la non-applicabilité » est correcte **si le lecteur remonte au contrat**. Mais `DIRECTION` 579 demande une ancre fraîche et inspectable avant le premier code ou rendu, et `ACTION` 475 exige une **spec visuelle synthétique avant le premier code ou rendu de toute surface `DIRECTION`**. ACTION 483 prévoit `NOT-VERIFIED` et issue appropriée si ancre/spec requises manquent. Une lecture rapide peut traiter la faible criticité d’une nouvelle surface `DIRECTION` comme motif de N/A pour la spec, alors que le mode la déclenche déjà. L’exception de non-applicabilité de l’ancre sur une surface identitaire demeure débattue (F-DIR-027), mais elle ne crée **aucune exception démontrée pour la spec**. Cette différence reçoit F-SAV-010 ci-dessous.
5. **Preuve et sortie (916–917).** `NOT-VERIFIED` vaut pour la preuve applicable absente, pas pour un succès implicite. La règle 8 rappelle retour, exploration et `FAIL-ASSUMED` **autorisé**, et refuse la moyenne qui efface un axe bloquant. Elle abrège toutefois la gamme ACTION : `ESCALATED` ou blocage sans livraison s’imposent parfois ; une réserve acceptée peut aussi être une sortie justifiée selon scope. `FAIL-ASSUMED` est réservé par ACTION 808–826 à l’échec **connu**, documenté, assumé avec autorité, limites et re-test ; une preuve absente ou un risque grave exclu ne suffit jamais. F-ACT-038/039 suivent la protection et la projection de cette exception. L’omission du résumé n’abolit pas ces conditions, mais justifie un scénario de lecture rapide lors du checkpoint.

### Méthodologie et condition d’arrêt (921–940)

Le niveau de formalité dépend du mode (923). La séquence 925–932 n’attribue pas aux heuristiques de SAVOIR l’autorité de conclure : le cadrage de contexte attend une preuve située, la direction et le système s’activent par leur objet direct, le contrat de composant par l’usage ou la criticité, QA et gates par leur périmètre. Une petite correction de wrapping ne devient pas un run `DIRECTION` ni un dossier de huit documents parce qu’elle requiert assemblage et vérification ; un formulaire critique ne descend pas en `LITE` sous prétexte d’une modification locale (`DIRECTION/START` 140–142).

La phrase 934 « repasse complète attendue en `DIRECTION`, recommandée en `STANDARD` et ciblée en `ITER` ou `LITE` » qualifie **la portée de l’inspection et du travail utile**, pas un quota de modifications. Une surface `DIRECTION` doit être revue dans ses relations, états, contenu et breakpoints pertinents avant clôture ; si la première scène tient déjà, le one-shot de DIRECTION 502, ACTION 453 et SAVOIR/CRAFT 207–212 permet un **arrêt après observation**, sans inventer une correction. Si un défaut dominant subsiste, la repasse traite sa cause et rejoue les tests touchés. `ACTION` 513–523 et F-ACT-025/F-DIR-009 conservent la condition d’arrêt du polish et les tensions du transport. Le mot « complète » peut inciter une équipe pressée à réparer quelque chose à tout prix : le scénario reste à éprouver, sans nouveau constat isolé.

La liste de défauts « restés par défaut » (934) est une **invitation à inspecter** alignement, échelle, distance, état, composant, mouvement, contenu, breakpoint et récupération. Elle ne rend pas chaque effet applicable à chaque médium et ne justifie pas une correction esthétique sans effet. La dernière phrase sur le goût (936) énonce une limite épistémique : références et méthode rendent la simulation de jugement plus difficile, mais ne démontrent ni talent ni qualité observée. La preuve adaptée et le compromis situé demeurent indispensables. L’honnêteté sur les manques (940) préserve `NOT-VERIFIED`, réserves et prochaine preuve.

## Passage C — simulations de lecteurs

| Lecteur / cas | Décision correcte en suivant les propriétaires | Risque d’une lecture du seul résumé |
|---|---|---|
| Designer, nouvelle surface `DIRECTION` jugée « faible risque » | Ancre selon DIRECTION 579 et spec synthétique avant le premier rendu selon ACTION 475 ; si absentes, qualifier les axes et la sortie | « Contrat ou risque » lu comme facultatif ; spec déclarée N/A alors que le mode la requiert (F-SAV-010) |
| Agent, micro-correction de wrapping sans nouveau risque identitaire | `START` vérifie le risque, chemin local proportionné, test pertinent, trace courte ; ne pas ouvrir direction/système artificiels | Transformer la méthode studio en huit formulaires universels |
| Designer, premier rendu `DIRECTION` complet et conforme au scope observé | Inspection représentative, comparaison, confirmation et arrêt one-shot justifié | « Repasse complète » devient modification fictive (F-DIR-009/F-ACT-025) |
| Intégrateur, premier rendu beau mais état erreur mobile non vu | Inspecter état et breakpoint, garder limitation et preuve manquante ; corriger si défaut confirmé | Substituer une capture desktop et un vernis visuel à la couverture des états |
| Responsable, risque de sécurité grave ou échec connu non documenté | ACTION détermine `ESCALATED`/blocage ou retour ; aucun `FAIL-ASSUMED` sans conditions/exclusions | Choisir l’exception dans une liste courte « si un risque reste » (F-ACT-038/039) |
| Équipe, dispositif imprimé ou natif | Traduire accessibilité, robustesse et récupération au médium et à la tâche ; nommer les preuves | Appliquer littéralement responsive/breakpoints Web sans objet (F-DIR-038) |

Ces scénarios sont des **simulations du contrat documentaire**, non des essais sur des utilisateurs ou une distribution exécutée. Les résultats réels doivent être testés avec les façades, la projection machine et des pilotes ; la lecture seule ne permet pas de mesurer fréquence ou sévérité en production.

## Passage D — résistance et constat provisoire

### F-SAV-010 — la règle d’or n° 6 peut faire déclarer la spec `DIRECTION` non applicable

- Gravité provisoire : **Significatif à éprouver**.
- État : **tension documentaire confirmée** entre résumé conditionnel et contrat propriétaire ; effet lecteur réel à tester. Aucune exception à la spec `DIRECTION` n’a été identifiée dans ACTION 475.
- Preuve : SAVOIR 915 lie **ensemble** ancre et spec à « si le contrat ou le risque le requiert », suivi de N/A ; ACTION 475 exige la spec pour le premier code/rendu d’une surface `DIRECTION`, 483 impose `NOT-VERIFIED` si spec requise absente. DIRECTION 579 rend l’ancre préalable ; son exception N/A reste ouverte sous F-DIR-027. Le résumé 908 et 938 se dit non propriétaire.
- Contre-exemple discriminant : mode `DIRECTION`, nouvelle surface visuelle à risque usuel, premier code sans spec parce que le lecteur a écrit « faible risque, N/A » dans la règle rapide ; la source propriétaire ne permet pas de conclure « spec non applicable » sur cette base.
- Conséquence possible : build sans cible explicite, comparaison spec/rendu impossible, `NOT-VERIFIED` traité comme N/A, verdict DIRECTION sur une intention reconstruite après coup.
- Atténuations : le lecteur qui consulte ACTION voit la condition absolue de la spec ; le résumé affirme sa subordination et la condition « contrat » inclut en réalité l’obligation du mode `DIRECTION`. Il n’existe ici ni PASS machine démontré ni preuve qu’une équipe suivrait l’interprétation fautive.
- Relation, sans fusion : F-DIR-027 porte la branche d’ancre et le transport humain/machine ; F-SAV-010 porte **la spec rendue apparemment optionnelle par la façade SAVOIR**, même si le contrat d’ancre était clarifié. F-ACT-028 porte la trace, F-DIR-009 le one-shot, F-ACT-025 l’arrêt du polish.
- Propriétaire pressenti : SAVOIR pour la fidélité de la règle rapide ; ACTION pour toute exception éventuelle et la preuve/spec ; DIRECTION pour l’ancre, sans transfert de leur autorité au résumé.
- Test futur : lire la seule règle 6 sur un cas `DIRECTION` avec faible risque puis faire consulter ACTION ; opposer `STANDARD` sans besoin d’ancre, `DIRECTION` avec ancre requise absente, spec requise absente et spec présente ; vérifier résultat N/A / NOT-VERIFIED, moment de la spec et comparaison au rendu.

### Occurrences conservées sous constats existants

| Tension | Rapport existant ou test de suite |
|---|---|
| Ancre absente en identité : N/A proposé, ABSOLU 2 exige ancre et schéma gère mal son absence | F-DIR-027, F-SAV-003 pour generated-only distinct |
| Repasse « complète » comprise comme correction obligatoire alors que one-shot valide | F-DIR-009, F-ACT-025 ; interpréter repasse comme examen complet et correction utile seulement |
| Liste 917 abrège les issues et `FAIL-ASSUMED` peut être choisi pour un risque seulement supposé | F-ACT-038/039 et ACTION/OVERRIDE ; test de lecture rapide au checkpoint SAVOIR |
| « Accessibilité, responsive, performance » repris sur support non Web | F-DIR-038 / SAVOIR/TECH : traduire le contrôle au médium |
| Liste studio de huit lignes utilisée comme formulaire universel | F-SAV-001 sur coûts de routes ; `SAVOIR/READ` et ACTION gardent la formalité adaptée ; tester temps réel |

## Couverture, limites et suite

| Passage | Profondeur | Résultat |
|---|---|---|
| A — architecture | FULL | Deux résumés non propriétaires, renvois et statut `[MÉTHODE]` ; route d’entrée vérifiée |
| B — sémantique | FULL | Huit règles, huit lignes studio, portée de spec/ancre, preuve, override et one-shot |
| C — lecteurs | TARGETED | Six cas discriminants ; aucun comportement réel inféré |
| D — résistance | FULL | F-SAV-010 provisoire ; quatre tensions dédupliquées et tests de suite |
| Machine | LIGHT | `SAVOIR/READ` résolu ; reading map verte ; validation de spec/mode réservée à l’audit des contrats machine |
| Externe | N/A-JUSTIFIED | Aucune assertion de standard externe ni conformité de produit dépendant de ce bloc |

**Lecture sectionnelle SAVOIR terminée : lignes 1–941, quinze rapports.** Aucun patch. **Prochaine unité, distincte du présent bloc :** checkpoint consolidé SAVOIR ; relire le protocole §12, le plan maître et les quinze rapports ; contrôler la couverture, les neuf anciens constats et F-SAV-010, les doublons inter-propriétaires, les tests et dépendances à venir. Puis reprendre BIBLIOTHEQUE en phase 2. La lecture complète de SAVOIR ne clôt ni la phase 2 système, ni l’audit.
