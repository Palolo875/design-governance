# V1.2 — AP5 : pilotage resynchronisé (C18) et dispositions des constats différés

**Date :** 01-10-2026.
**Décision de l'owner :** « Allons-y pour AP5 ». Unité documentaire : le package est inchangé. Les corrections proposées au §3 attendent une décision.

## 1. C18 — pilotage (fait, certain)

| Lieu | Avant | Après |
|---|---|---|
| Plan de reprise, en-tête | Daté du 27-09 | « mis à jour le 2026-10-01 (AP5) » |
| Plan de reprise, consigne 1 | « la preuve d'efficacité viendra en R10 » | Palier R10 fait puis arrêté (`V12R_35`, `V12R_36`) ; toute production exige une décision explicite ; efficacité `NOT-VERIFIED` |
| Plan de reprise, §2 « État » | Arrêté « après R11 ciblé » ; mesures après R11b ; suivi « 372 maintenus, 17 migrés » ; décompte des gardes de R2-R8 | « Après AP4b » ; ajout de R10, A1, A2 et AP1 à AP5 ; mesures courantes ; mesures historiques datées par unité ; gardes, suites et suivi actuels (389 cas, 363 et 26) ; sondes par unité |
| Plan de refonte, en-tête | « Pilotage au 30-09 » ; mesures après R8b-2 présentées sans date de rôle | Pilotage au 01-10 ; rôle du document (architecture et historique) ; renvoi au plan de reprise pour l'état et les mesures |
| Inventaire, D-23 | « coût non remesuré » | Coût du palier R10 (1,7 à 1,8 × C1 en tokens, ≤ C4) ; coût après A2 et AP non mesuré ; coût propre de la trace et de l'atelier non isolé ; limite déclarée |
| Inventaire, PIL-01 à PIL-04 | « intégré » au 30-09 | État au 01-10 : fermé, avec la raison de chacun |
| CLAUDE.md | « État actuel (26-09-2026) » | Date de mise à jour, puis état et prochaine étape (§2, §6) |

**Préservé :** décisions P2, arrêt de R10, décisions de `V12R_14`. Aucun second plan actif n'est créé.

## 2. Dispositions vérifiées sur le dépôt

| Constat | Vérification (au commit `45e560c`) | Disposition proposée |
|---|---|---|
| **C15** couverture UI/UX | **Certain.** Le code exige que chaque état déclaré soit couvert, mais pas les autres matrices. Dans l'exemple, 12 exigences sont déclarées hors états et 4 couvertes ; il reste valide. ACTION dit pourtant « la couverture de **chaque** exigence » | **Arbitrage**, §3 D1 |
| **C25** `DOMAIN-FRAME` | **Certain.** Aucune mention dans `CHARGE` ni dans le noyau. Le déclencheur ne vit que dans sa propre section | Correction proposée, D2 |
| **C26** vues plus larges que `CHARGE` | **Certain.** « Détail final » appelle `CFT-03`, `STATE` **et** `INTEGRITY` là où `CHARGE` dit « ou ». `ACTION/ROUTING` charge `COMPONENTS` « si partagé ». `SAVOIR/STYLE` charge `FRAME` sans condition | Correction proposée, D3 |
| **C27** delta local | **Certain.** « un delta local n'en porte aucune obligation » ne dit pas si un delta qui touche un composant critique ou partagé est exempté | Correction proposée, D4 |
| **C28** comparaison | **Certain.** `BIBLIOTHEQUE/MICRO` : « accepté uniquement si la version après… ». Cela confond la validité de la preuve avec le choix de version ; B1b admet de garder l'original | Correction proposée, D5 |
| **C29** tests de structure | **Certain pour `SUPPORT`** (test de masquage sans la nuance « dépendance porteuse »). **Couvert ailleurs** : porte de non-généricité, test de style de SAVOIR, priorité égale de `GRID` (« poids proche ») et de `COMPAT` | D6 : correction pour `SUPPORT` seulement ; `GRID` et `COMPAT` maintenus |
| **C30** « Sinon » ambigu | **Certain, dans le noyau.** « Si oui, …justifie. Sinon, reconsidère-les » se rattache à « si oui ». Cela demande de reconsidérer un choix **non** convergent | Correction proposée, D7 |
| **C31** cinq artefacts hors Web | **Certain.** « dérive cinq artefacts de preuve » se lit comme cinq livrables | Correction proposée, D8 |
| **C32** méta-structure de DIRECTION | Répétitions documentées ; accès précoce aux protections déjà présent (R5a) | **Maintenu, sans changement.** À instruire seulement si une relecture de parcours montre une omission ; pas de fusion générale (l'audit l'écarte) |
| **C37** proportion du noyau | Question d'architecture ; effet et coût non mesurés | **Maintenu, sans changement.** À instruire après R11 final, sans retrait ni économie promise |
| **C38** CI et preuves d'efficacité | CI hébergée non observée ; journaux et coûts R10 incomplets | **Réserve maintenue.** CI en R11 final ; mesure d'effet seulement sur décision future de l'owner |

## 3. Décisions attendues (textes proposés)

**D1. C15, portée de la couverture UI/UX.**
- **(a) Toute exigence déclarée est couverte.** Le code exige une entrée de couverture par élément des quatre matrices, et l'exemple ajoute 8 entrées. Une exigence non vérifiée y figure en `NOT-VERIFIED`, ce qui ne crée aucun `PASS` artificiel. Le texte d'ACTION reste inchangé.
- **(b) Seuls les états sont obligatoires.** ACTION est reformulé : « la couverture de chaque état critique est obligatoire ; les autres lignes déclarées sont couvertes lorsqu'elles portent un claim ».
- **Recommandation : (a).** Le texte d'ACTION la porte déjà, et c'est le choix le plus honnête.

**D2. C25.**
- **Lieu :** `CHARGE`, colonne « Ajouter seulement si », lignes STANDARD et DIRECTION, compilée dans le noyau.
- **Ajout :** « `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l'expression ou la preuve ».

**D3. C26, trois vues alignées sur `CHARGE`.**
- **« Détail final » :** « `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` ou `SAVOIR/INTEGRITY` selon la question ouverte, et capture rendue ».
- **`ACTION/ROUTING` :** « `SAVOIR/SYSTEM` si une décision partagée change, `BIBLIOTHEQUE/COMPONENTS` si un composant change, `ACTION/RUN-SYSTEM` si partagé ».
- **`SAVOIR/STYLE` :** « `DIRECTION/START → SAVOIR/FRAME si le cadrage est à éclaircir → SAVOIR/STYLE si nécessaire → ACTION/RUN-*` ».

**D4. C27.** « …un delta local sans responsabilité critique, réutilisable ou partagée n'en porte aucune obligation ; s'il touche un composant critique ou partagé, ou devient réutilisable, il relève de ce contrat (reclasser avec `DIRECTION/START`). »

**D5. C28.** « La comparaison est valide si elle isole la décision et observe le critère déclaré. La version retenue est celle qui réduit une ambiguïté, préserve les états critiques et rend une décision plus directe sans exiger davantage d'attention : l'original s'il résout mieux (`ACTION/B1b`). »

**D6. C29, `SUPPORT`.** Ajout : « Si la composition dépend de ce qui est masqué par une relation déclarée, avec un repli, la dépendance est recevable (`BIBLIOTHEQUE/GATE`, non-généricité) ; le masquage sert à diagnostiquer, pas à exiger un décor indépendant du contenu. »

**D7. C30, noyau.** « Si oui, nomme ce qui, dans le produit, les justifie ; si rien ne les justifie, reconsidère-les. »

**D8. C31.** « …examine cinq responsabilités de preuve, regroupables dans un même artefact, avant de juger : »

**Forme proposée.** Une unité **AP5b**, appliquée comme AP3 : patch exécutable, gardes rouges avant et vertes après, mutations, suivi complet. Les textes sont ceux ci-dessus, testés sur copie avant application.

## 4. Contrôles de l'unité

Le package est inchangé : les validateurs n'ont pas à être rejoués pour cette unité. B01 : 218/218.
