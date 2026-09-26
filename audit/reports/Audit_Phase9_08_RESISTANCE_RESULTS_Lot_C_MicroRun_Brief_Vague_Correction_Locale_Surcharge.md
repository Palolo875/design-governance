# DG-AUDIT-001 — Phase 9.08 — RESISTANCE-RESULTS : lot C par micro-run

**Scénarios §19 traités :** 01 Brief vague, 03 Correction locale, 19 Surcharge procédurale. Le micro-run §28 compare une production **avec** et **sans** Design Governance.

**Date :** 25 septembre 2026. **Auditeur :** Claude, observateur unique. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décisions de l'owner, explicites (formulaire du 25-09) :**
- brief réel : son app de budget pour freelances, registre « quiet-premium » ;
- surface : « Première scène / accueil » ;
- base de comparaison : sous-agent vierge autorisé (« Oui, sous-agent vierge »).

**Unité d'audit (§9) :**

| Élément | Contenu |
|---|---|
| Cible | L'entrée d'un run réel, de START à la clôture, et sa proportionnalité |
| Propriétaire principal | `DIRECTION/START` (avec DAILY, FAST-PATH, EXTERNAL-START) |
| Voisins | `ACTION` (RUN-LITE/DIRECTION, HANDOFF, CLOSE-EXIT-CHECK, PRECONDITION) ; `SAVOIR` (CFT-00, premium 102–106/678, 363) ; REUSE-CHALLENGE |
| Risque dominant | Proportion : trop peu de protection sur un changement critique, ou trop de procédure sur un micro-delta |
| Condition de sortie | Oracles `+`/`−` des trois scénarios rejoués sur un run réel ; signaux §29 relevés ; comparaison avec et sans DG documentée |

---

## 1. Rituel et protocole du micro-run

| Étape | Exécution |
|---|---|
| 1. Plan | Plan maître, état 9.07 |
| 2. Bloc précédent et checkpoints | 9.07, 9.06 ; 9.01 lignes 01, 03, 19 ; antécédents 4.01, 5.01–5.04, 7.02, 8.02 |
| 3. Empreintes | B01 et protocole conformes |
| 4. Protocole | §3.2, §19, §28, §29 |
| 5. Sources exactes B01 | DIRECTION/START 119–159, DAILY 245–262, FAST-PATH 263–276, EXTERNAL-START 278–312, REUSE-CHALLENGE 355–370, VISUAL_TARGET, FIRST-OBJECT, DOUBLE-LOOP ; ACTION/RUN-LITE 339–347, HANDOFF 23–35 ; SAVOIR 102–106, 363, 678, CFT-00 |
| 6. IDs concernés | F-DIR-007/F-ACT-017, F-DIR-044, F-DIR-028, F-SK-001/F-ACT-002, F-SAV-002 |

**Comptage des lignes chargées.** J'ai utilisé le lecteur de routes de B02. Il ne diffère de B01 que par la table des locators : les fichiers propriétaires lus sont identiques octet pour octet.

### Conditions de comparaison

**Run sans DG.**
- Sous-agent général lancé à froid.
- Il a reçu **le brief et la réponse de l'owner** (« première scène / page d'accueil ») et les mêmes contraintes techniques : un seul fichier HTML, aucune ressource externe, desktop et mobile, français.
- **Aucune règle DG** ; interdiction de lire d'autres fichiers ou d'aller sur le web.
- Durée : 132 s, 2 appels d'outil. Fichier `baseline_sans_DG.html`, SHA-256 `30687c27…a5523f`, **figé avant que je le regarde**.

**Run avec DG.**
- Produit par moi, en suivant les routes. Fichiers `run_DG.html` (`dfa3d85e…12aae6`), puis `run_DG_v2.html` après une boucle (`b45d7461…2e28de`), puis `run_DG_v3_lite.html` pour la correction locale (`39be8a40…485132`).

**Limites de la comparaison, déclarées d'emblée :**
- **N = 1** de chaque côté ;
- deux auteurs différents (sous-agent / moi), ce qui mélange l'effet de DG et l'effet de l'auteur ;
- **je suis juge et partie** pour le run avec DG ; j'ai vu le résumé du sous-agent (5 lignes) avant de construire, mais pas son rendu ;
- polices de substitution de l'environnement ;
- aucun utilisateur.

**Ce micro-run teste des hypothèses (§28) ; il ne valide rien de général.**

## 2. Trace du run avec DG

**START.** Le brief est vague entre écran de travail (STANDARD) et première scène (DIRECTION). J'ai posé **une seule clarification** qui peut changer le mode (START, question 6 de l'arbre ; DAILY, « une seule clarification ciblée »). Elle a été posée **à l'owner réel**, qui a répondu « Première scène / accueil » → **DIRECTION**.

Risque dominant : V/craft et vérité (montants, taux). Pas de risque critique : données fictives, aucune action ni connexion.

**REUSE-CHALLENGE, déclenché par une préférence nommée** (« quiet-premium »). Le `KEEP-IF` ne peut pas se réduire à « premium » (358–369). J'ai traduit la préférence avec SAVOIR 678 et 102–106 :
- « quiet » = calme face à la volatilité des revenus ;
- « premium » = précision des montants et confiance, pas palette ni luxe.

**VISUAL_TARGET, compact :**

| Champ | Décision |
|---|---|
| Thèse | Chaque paiement reçu est déjà rangé ; on voit ce qui est vraiment à soi |
| Opération dominante | La répartition d'un encaissement en quatre parts |
| Ancre (`ANCHOR`, connaissance non revérifiée) | Budget par enveloppes et relevé bancaire. Retenu : répartition, chiffres tabulaires, filets. Rejeté : cartes KPI, dégradés fintech, tirelire, registre sombre et doré. |
| Anti-direction | Tableau de bord décoratif ; slogan de sérénité sans mécanisme |
| Vérité | Marquage `TRUTH/MECHANISM` près de l'objet ; « maquette · paiements et taux fictifs » dans l'en-tête |
| Geste | Choisir un paiement fictif ; la répartition se recalcule localement |

**DOUBLE-LOOP sur le run 1** (capture 1440 et 390) :

| Test | Résultat |
|---|---|
| Promesse et geste | Tient |
| Preuve précoce | Tient |
| Signature située | Tient (le test de substitution échoue pour un autre produit) |
| Vérité | Tient |
| **Finition qui sert** | **Échoue sur mobile : l'objet arrive après les bénéfices** (FIRST-OBJECT 316). C'est la même faute que le pilote A en 6.02b. |

**Correction substantielle unique (v2)** : sur mobile, l'objet de preuve passe juste après le titre ; l'ordre de lecture du DOM ne change pas.
- **Gain observé** : la répartition est dans le premier écran à 390 px.
- **Nouveau défaut** : le bouton « Essayer » descend, et les trois paiements empilés prennent de la hauteur.
- Arrêt : le gain suivant serait du polish.

**Lignes de B01 réellement chargées pour ce run DIRECTION : environ 622.** Détail : START 130, VISUAL_TARGET 80, FIRST-OBJECT 63, RUN-DIRECTION 14, DOUBLE-LOOP 65, SAVOIR/CRAFT 186, REUSE-CHALLENGE 16, SAVOIR/SOURCE 63, passages premium environ 5.

## 3. Comparaison des deux premières scènes

Grille : les huit dimensions de FIRST-OBJECT, plus les contrôles automatiques. Planche `PLANCHE_LOT_C.png`.

| Dimension | Sans DG (« Solde ») | Avec DG (« Parts », v2) |
|---|---|---|
| **Présence** | **Plus forte** : grand serif, italique vert, carte-graphique généreuse | Forte mais plus sèche : grotesque gras, relevé |
| **Foyer** | Clair (promesse puis carte) | Clair (promesse puis répartition) |
| **Signature située** | **Très bonne** : « revenus en dents de scie → salaire en ligne droite », visible dans le graphique | Bonne : « paiement → parts » |
| **Intégration de l'objet** | Graphique au service de la promesse. Bizarrerie : la ligne « salaire lissé » s'arrête à mi-graphique. | Répartition au service de la promesse et du geste |
| **Désirabilité située** | **Supérieure** : chaleur éditoriale, calme | Plus utilitaire, moins « quiet-premium » |
| **Vérité de scène** | **Échoue** : « 30 jours offerts », « Sans carte bancaire », « Lecture seule sur vos comptes » affirmés sans marquage ; montants non marqués fictifs ; **5 liens `href="#"` morts** (Tarifs, Journal, Se connecter…), contraire à FIRST-OBJECT 318 | Tient : marquage près de l'objet ; le bouton déclenche un comportement local réel |
| **Résolution** | axe : **7 à 8 contrastes insuffisants** et un `nested-interactive` ; texte collé au bord gauche à 390 px | axe : **0 violation** ; pas de débordement |
| **Résilience visible** | Sans JavaScript : **contenu estompé et graphique absent** (animations d'apparition jamais déclenchées). Couleurs forcées : la ligne de salaire disparaît, le bouton perd son contour. | Sans JavaScript : identique au rendu nominal. Couleurs forcées : **la barre de répartition disparaît** (sens porté par les couleurs de fond), mais les montants restent lisibles en texte. |
| **Mobile (objet avant bénéfices)** | Objet sous le premier écran | Run 1 : même défaut ; **v2 : corrigé** par la boucle |

**Lecture.**
- DG apporte ici un gain **net et mesurable** sur la vérité, l'accessibilité automatisable, la robustesse sans JavaScript et l'ordre mobile après boucle.
- **Il n'apporte pas de gain visible en présence ni en désirabilité** : sur ces deux axes, la production sans DG est, à mon jugement, **meilleure**.
- Les deux runs trouvent un mécanisme spécifique au freelance.
- Le coût de DG : environ 622 lignes lues, contre 0.

**Convergence de style (hypothèse issue de 9.06) :**

| Run | Registre obtenu |
|---|---|
| Sans DG | Le canon éditorial « quiet » : papier chaud, serif d'affichage avec italique, vert profond, touche laiton |
| Avec DG | Évite ce canon (pas de serif, papier froid, chiffres mono) après REUSE-CHALLENGE, mais retombe sur « neutres + un accent vert » (SAVOIR 363) |

Les deux choisissent un **vert profond** comme accent. **N = 1 de chaque côté** : cela ne prouve pas de convergence systématique. Cela confirme seulement que REUSE-CHALLENGE agit **quand une préférence est nommée**, et que la structure « neutres + accent » reste la pente par défaut (F-SAV-002).

## 4. Résultats par scénario

### 01 Brief vague — TARGETED

- **Oracle `+` réalisé.** Une clarification unique, capable de changer le mode (STANDARD ↔ DIRECTION), posée à un owner réel (pas simulé). INTAKE : décision, risque, owner et prochaine preuve tenus dans la trace.
- **Oracle `−`.** Le sous-agent sans DG, bien qu'il ait eu la réponse sur la surface, **a inventé un contexte d'affaires** : offre d'essai, absence de carte, lecture seule, tarifs, journal. Il l'a présenté comme réel. C'est exactement ce que la ligne `TRUTH` de EXTERNAL-START (RUN-PRIORITY 1) et FIRST-OBJECT 316–318 visent à empêcher. DG n'a produit aucune de ces inventions.
- **Limite.** Un seul brief ; clarification choisie par l'auditeur.

### 03 Correction locale — TARGETED

**Delta a, micro-delta.** Collision entre le logo et le marquage de vérité à 390 px.
- FAST-PATH, quatre questions :
  - changement : l'espacement de l'en-tête ;
  - risque : lisibilité du marquage de vérité ;
  - preuve la moins coûteuse : capture à 390 px ;
  - effet d'une preuve négative : retour arrière.
- Route **LITE** : 2 lignes de CSS (`gap` et `text-align`). Capture avant/après : collision résolue.
- **Oracle `+` réalisé** : delta réversible, preuve proportionnée. Aucun chargement de SAVOIR/CRAFT, de l'atlas ni de B1b, conformément à DAILY (LITE) et au « silence des micro-deltas » de START.

**Delta b, changement critique, classification seulement (pas de build).** Ajouter un bouton « Connecter ma banque » dont le libellé de consentement passe de « lecture seule » à « Parts peut programmer vos virements vers la réserve ».
- START 140 : « Un nouveau… consentement, … permission… n'est jamais un micro-delta `LITE` ou `ITER` » → **reclassement obligatoire** vers STANDARD au minimum, avec protection critique (permission, confidentialité).
- **Oracle `−`** : au niveau du texte, DG l'empêche. En machine, l'antécédent reste valable : un LITE critique est accepté sur simple déclaration de protection (4.01, 7.02 : F-DIR-007/F-ACT-017). Pas de rejeu : aucune information nouvelle attendue.

**Contraste de charge mesuré :**

| Chemin | Lignes | Détail |
|---|---|---|
| Delta a, route courte | **163** | START 130, FAST-PATH 19, RUN-LITE 14. **181** si la sortie reprend les 18 lignes de HANDOFF. |
| Delta b, route justifiée par le risque | **618** | START, PRECONDITION, STATUS, RUN-STANDARD, AUTHORITY, GATE-A, GATE-B, SAVOIR/CONTEXT, HANDOFF, RUN_CARD, CLOSE-EXIT |

**La charge augmente avec le risque, dans le bon sens.**

### 19 Surcharge procédurale — TARGETED

**Épreuve.** Au delta a, j'ai ajouté toutes les routes qu'un agent « prudent » pourrait charger : SAVOIR/CRAFT 186, DESIGN-ATLAS 48, GATE-C 27, GATE-A 71, STATUS 78, PRECONDITION 56, RUN_CARD 87, CLOSE-EXIT 25 : **+578 lignes, soit environ 760 au total**.

**Pour chacune, qu'est-ce que cela change ?**
- Seul **un contrôle de GATE-A** (le contraste du marquage de vérité, déjà conforme) est applicable. Il tient en une vérification, pas en 71 lignes.
- Les autres routes ne modifient **ni la décision, ni l'artefact, ni la preuve**. B01 les exclut d'ailleurs explicitement pour LITE (DAILY ; START « Silence des micro-deltas » ; FAST-PATH « si la réponse… est rien, ne lance pas »).

→ **Oracle `+` réalisé** : les étapes sans effet sont supprimables, et **c'est le texte de B01 qui l'autorise**.

**Oracle `−` (faux allègement qui omet l'owner ou la preuve) : non observé.** FAST-PATH garde le risque, l'owner si nécessaire, la preuve et la condition d'arrêt.

**Deux surcharges résiduelles, observées :**
1. **Le bloc START pèse 130 des 163 lignes (80 %) de la route LITE**, alors que l'arbre utile tient en une quinzaine de lignes. C'est la mesure concrète, sur un run réel, de **F-DIR-044** (bloc extrait trop large), déjà vue en 5.02.
2. **ACTION/HANDOFF exige 13 champs pour « toute sortie de run »**, alors que DAILY fixe pour LITE une clôture de 4 éléments (artefact, risque, axes, réserve). Pour un écart d'espacement, 9 champs deviennent `N/A-JUSTIFIED` par formalité. C'est une tension de proportion déjà ouverte : **F-SK-001 / F-ACT-002** (portée de la sortie courte face au handoff). Première mesure sur run réel. Pas de nouvel ID.

## 5. Signaux §29 relevés

| Signal | Sans DG | Avec DG |
|---|---|---|
| Première décision exploitable | Immédiate, mais inventée en partie | Après une clarification (un aller-retour avec l'owner) |
| Premier artefact jugeable | 132 s (sous-agent) | Non chronométré (auditeur) : **non comparable** |
| Fichiers et routes chargés | 0 | 9 routes, environ 622 lignes (DIRECTION) ; 3 routes, 163 lignes (LITE) |
| Erreur de classification | — | Aucune (DIRECTION, LITE, reclassement du consentement) |
| Premier défaut dominant | Vérité (claims inventés) | Mobile : objet après les bénéfices |
| Correction modifiant l'artefact | — | 1 boucle (v2) et 1 LITE (v3), toutes deux observées |
| `N/A-JUSTIFIED` | — | 9/13 champs de HANDOFF pour le delta LITE |
| Différence avec une base sans le protocole | — | **Première mesure de la campagne** (N = 1), voir §3 |

## 6. Sortie de la phase 9

**20/20 scénarios examinés**, chacun avec niveau, oracles et limite :
- 6 en contrat seulement : 9.02 à 9.05 ;
- 14 en contrat et sur objet observé : 9.06 à 9.08.

**0/20 FULL d'efficacité clos**, et cela doit rester visible. Il manquerait plusieurs briefs, plusieurs auteurs, plusieurs juges humains et des tâches réelles (§28, pilotes). **La phase 9 est close dans sa portée : contrat, et objet avec observateur unique.** L'efficacité est **ESCALATED** vers des pilotes réels, hors du périmètre de cette campagne documentaire.

**Ce que la phase 9, par objet, établit à ce stade** (N petit, observateur unique) :

- **Utile, en partie mesuré.** DG améliore la **vérité**, l'**accessibilité automatisable**, la **robustesse** et l'**ordre du premier objet**, et sa boucle corrige dans la bonne direction (A2, B′, v2).
- **Pas démontré.** Il n'améliore pas visiblement la **présence** ni la **désirabilité**. Dans le seul comparatif avec et sans DG, la production sans DG est plus désirable, mais moins vraie et moins robuste.
- **Protections qui tiennent au jugement.** Arrêt du one-shot, statut « transformed », classement critique : le texte est juste, la machine ne les voit pas.
- **Proportionnalité.** Correcte dans l'esprit (163 contre 618 lignes selon le risque). Deux surcharges mesurées : START trop large (F-DIR-044) ; HANDOFF uniforme (F-SK-001/F-ACT-002).
- **Défauts récurrents sur les objets**, même sous DG. Sens porté par la couleur de fond en couleurs forcées (Parts), boutons sans contour (pilotes), objet sous le premier écran en mobile. Les règles existent ; **aucune route n'invite à tester un runtime dégradé**.

**Registre : 157 fiches provisoires, aucun nouvel ID.** Renforts par mesure :

| Fiche | Renfort |
|---|---|
| F-DIR-044 | 80 % de la route LITE |
| F-SK-001 / F-ACT-002 | 9/13 N/A |
| F-SAV-002 | Neutres + accent, les deux runs |
| F-DIR-007 / F-ACT-017 | Antécédent consentement |

Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- **première comparaison avec et sans DG de la campagne** ;
- elle **nuance** les conclusions précédentes : DG gagne en vérité et en robustesse, **pas** en désirabilité ;
- elle donne deux mesures de surcharge chiffrées, qui serviront directement au classement de F-DIR-044 et F-SK-001 en phase 10.

**Prochaine unité : phase 10**, classement fiche par fiche des 157 constats (§20, 15 champs), à partir des rapports de phase 2 de l'archive complète et des preuves d'objet 6.02b et 9.06–9.08. Découpage proposé : un bloc par propriétaire (DIRECTION 46, ACTION 39, SAVOIR 10, BIBLIOTHEQUE 5, CHANGELOG 1, puis façades et machine 56).
