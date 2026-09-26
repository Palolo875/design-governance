# DG-AUDIT-001 — Phase 11.14 — PATCH-DECISION C7 : homogénéisation et ablation

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ».

**Grappe C7 : 3 fiches, toutes Significatif.** Elles touchent la **promesse centrale** de Design Governance : une sortie non générique. Le mécanisme est commun : **une heuristique de jugement est écrite comme une conclusion**. Selon le cas, elle prescrit un défaut, ou elle transforme un diagnostic en décision.

| Fiche | Texte | Ce qu'il fait | Ce qu'il devrait faire |
|---|---|---|---|
| F-SAV-002 | SAVOIR/CRAFT/CFT-05 363 `[REQUIS PAR LE MODULE]` | Prescrit « les neutres portent l'essentiel de la structure ; l'accent signale… » | Exiger des rôles, des états, un contraste calculé et un indice non chromatique, sans prescrire de répartition |
| F-BIB-005 | BIBLIOTHEQUE/GATE 707 (non-généricité) | « Sans image, données et nom… cinquante produits ? **Si oui, changer** support/grille/scène » | Diagnostiquer une dépendance, puis décider sur le rendu entier, la tâche et Gate C |
| F-SAV-006 | SAVOIR/STYLE 632 (test de style) | « Masque couleurs, image, logo… si la différence disparaît, **il n'y avait pas de profil** » | Même chose : la dépendance à un médium n'est pas l'absence de choix |

**Sorties :**
- cette `PATCH-DECISION` ;
- `C7_harnais_non_regression.py`, une garde textuelle : **aucun invariant machine** ;
- l'arbitrage du relèvement de F-SAV-002, laissé en suspens depuis 10.03.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | 11.00 à 11.13 ; 10.03 et 10.05 : F-SAV-002 « première candidate au relèvement », passerait Majeur si la convergence était confirmée N ≥ 3 fois par un observateur indépendant |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 |
| Sources relues | SAVOIR 116–120 (singularité, convergence de genre), 211–240 (CFT-00), 361–373 (CFT-05), 626–636 (STYLE, test et dials) ; BIBLIOTHEQUE 205–212 (garde-fou), 441–449 (EDITORIAL_FIELD), 600–606 (matière, test de retrait), 700–712 (GATE) ; DIRECTION 356–371 (REUSE-CHALLENGE), 385 (VISUAL_TARGET, matière / asset : fallback et condition de retrait) |
| Recherche transverse | « neutre » dans tous les `.md` : **la prescription n'existe qu'en CFT-05 363**. Aucune façade ne la recopie ; C7 n'a donc pas d'entrée LCF |
| Antécédents d'objet | 6.02b (pilote A : « sombre + serif + doré ») ; 9.06 (A applique 363 à la lettre et aboutit au canon que CFT-00 228 dit ne pas être le premium ; relief retiré → scène vidée) ; 9.08 (neutres et un accent vert profond, **avec DG et dans la baseline sans DG**) |

## 2. Re-vérification

**Garde C7 sur B01 :**
- témoins et conservation **4/4** ;
- gardes **0/5**.

La conservation (C-01) vérifie que CFT-05 garde son exigence fonctionnelle, déjà présente et juste. **Elle doit rester verte après correction.**

**Trois constats.**

1. **363 contredit son propre voisinage.**
   - CFT-00 228 : le premium « n'est pas défini par une palette sombre… ». CFT-00 234 : la beauté pertinente peut être « colorée, ludique ou silencieuse ».
   - CFT-05 371 : les impressions de statut ou de premium « restent des hypothèses ».

   Seule la phrase 363 prescrit une répartition, **sous le tag le plus fort** (`[REQUIS PAR LE MODULE]`). Le reste de CFT-05 (rôles, contraste calculé, information critique non portée par la seule couleur) est juste et doit rester.
2. **Les deux tests d'ablation concluent au-delà de ce qu'ils observent.**
   - Retirer un média et constater que la différence disparaît établit une **dépendance**.
   - Cela n'établit ni que la dépendance est décorative (707), ni qu'aucun choix n'a été fait (632).
   - DIRECTION a déjà le remède : VISUAL_TARGET 385 demande pour la matière ou l'asset un « fallback et [une] condition de retrait ». SAVOIR 118 admet la « convergence de genre légitime ». BIBLIOTHEQUE 605 fait du test de retrait une **condition de robustesse** (l'information critique survit), **pas un verdict de choix**.
3. **La pente vient du modèle ; 363 la codifie.** 9.08 observe la même palette avec et sans DG. Supprimer 363 **ne suffira probablement pas** à contrer la convergence : il faut aussi une capacité positive. C'est la question de convergence de la recommandation.

## 3. Arbitrage du relèvement de F-SAV-002

| Élément | État |
|---|---|
| Condition fixée en 10.03 et 10.05 | Convergence « neutres + accent » confirmée **N ≥ 3** par un **observateur indépendant** |
| Observations disponibles | Trois (6.02b, 9.06, 9.08). Chacune N = 1, **toutes par le même observateur** (l'auditeur). Une seule porte sur la palette avec contrôle sans DG (9.08) |
| **Décision** | **Condition non remplie : F-SAV-002 reste Significatif.** Le relèvement n'est ni accordé ni rejeté ; il reste **ouvert** avec sa condition, portée en phase 13 (§6, mesure M) |
| Effet sur la correction | **Aucun.** La décision de corriger ne dépend pas de la gravité : 363 contredit CFT-00 et CFT-05 par le texte. La gravité ne change que la priorité |

**Degrés de certitude :**
- **certain :** 363 prescrit une répartition, sous un tag requis, contre des textes voisins ;
- **probable :** 363 renforce une pente déjà présente dans le modèle (9.06 et 9.08) ;
- **hypothétique :** la correction réduit la convergence. C'est **à mesurer** ; ce n'est pas acquis.

## 4. Les sept questions du §21

| Question | F-SAV-002 | F-BIB-005 | F-SAV-006 |
|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : la palette par défaut devient une exigence | **Oui** : refonte d'une structure qui n'était pas la cause (9.06) | **Oui** : un profil porté par l'image ou la couleur est déclaré inexistant |
| Défaut réel ? | Oui (texte ; trois observations) | Oui (texte ; 6.02b, 9.06) | Oui (texte ; 9.06) |
| Gain > charge ? | Oui : une phrase remplacée, une question ajoutée | Oui : une cellule | Oui : une phrase |
| Nouvelle autorité ? | **Non** : les exigences restantes sont celles de CFT-05 ; la pluralité vient de CFT-00 234 | **Non** : le fallback est dans VISUAL_TARGET 385, Gate C dans ACTION | **Non** : même source |
| Testable ? | Garde textuelle ; **mesure avec / sans DG** (phase 13) | Garde ; épreuve de lecture | Garde ; épreuve de lecture |
| Positif / défensif équilibré ? | **Oui, capacité positive** : la question de convergence aide à s'écarter du défaut sans imposer d'écart | Oui : la dépendance décorative reste sanctionnée | Oui : l'étiquette sans relation reste sanctionnée |
| Suppression ou fusion ? | **Suppression** d'une prescription et **capacité positive** | **Clarification** | **Clarification** |

## 5. PATCH-DECISION

**Décision : CORRIGER.**

Types §21 :
- **correction normative** (F-SAV-002) ;
- **clarification** (F-BIB-005, F-SAV-006) ;
- **capacité positive** (question de convergence).

**Aucun invariant machine** : ce sont des jugements (D-ACT-1 = c).

**Règle commune aux deux tests d'ablation**, énoncée dans les mêmes termes chez les deux propriétaires pour éviter qu'ils divergent : **l'ablation diagnostique une dépendance ; elle ne décide pas.**
- Une dépendance est **porteuse** si le média retiré porte une relation déclarée (produit, preuve, donnée, profil) et dispose d'un fallback (VISUAL_TARGET, matière / asset).
- Elle est **décorative** sinon.

| # | Où | Texte cible |
|---|---|---|
| T-1 | **CFT-05 363** | « `[REQUIS PAR LE MODULE — …]` Conçois une palette par rôles : surfaces, textes, actions, états et frontières. **La répartition entre neutres et couleurs est une décision de direction, pas un défaut** : une structure neutre à accent, une identité multicolore structurelle ou un codage par zones sont recevables si les rôles, les états, le contraste calculé et un indice non chromatique pour toute information critique tiennent. Une couleur sémantique n'est pas une décoration. » |
| T-2 | **CFT-05** (après 363) | « **Question de convergence.** Cette palette est-elle celle que le modèle produirait sans brief (neutres et un seul accent, sombre et doré, dégradé froid) ? Si oui, nomme ce qui, dans le produit, la justifie. Sinon, reconsidère-la. La question ne prescrit aucun écart : une palette convergente justifiée reste valide. » |
| T-3 | **BIBLIOTHEQUE 707** (non-généricité) | « Sans image, données et nom, la structure pourrait-elle appartenir à cinquante produits ? **Si oui, la structure dépend de ce qui a été retiré.** Si la dépendance est porteuse (relation déclarée, fallback prévu par `DIRECTION/VISUAL_TARGET`), la conserver. Si elle est décorative, changer la relation support/grille/scène/preuve plutôt qu'ajouter du polish. Dans les deux cas, décider sur le rendu entier, la tâche et `ACTION/GATE-C`. » |
| T-4 | **SAVOIR/STYLE 632** (test de style) | « Masque les couleurs de marque, l'image et le logo. Si hiérarchie, type, densité et matière ne traduisent plus une différence substantielle, **le profil dépend du médium masqué**. Il est légitime si ce médium porte une relation déclarée et dispose d'un fallback. Sinon, il n'y avait pas de profil choisi, seulement une étiquette. » |

**Ce qui ne change pas :**
- `REUSE-CHALLENGE` (DIRECTION 358). Son déclencheur reste limité aux antécédents **nommés** (9.06). La palette par défaut du modèle n'est pas un antécédent nommé : la question de convergence vit donc **dans CFT-05**, et le déclencheur de REUSE-CHALLENGE n'est pas élargi.
- BIBLIOTHEQUE 211 et 605 (test de retrait d'une matière) : c'est une condition de robustesse, compatible avec la règle commune.
- Le reste de CFT-05 (365–373).

## 6. Conditions du patch et de sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Passe SAVOIR unique** : T-1, T-2 et T-4 avec B5 T-3 et T-4 et F-SAV-004 (E1), comme fixé en B5 |
| C2 | **Passe BIBLIOTHEQUE unique** : T-3 avec B5 T-1 et C3 T-1 à T-3 |
| C3 | **Même vocabulaire** chez les deux propriétaires (« dépendance », « porteuse », « fallback ») ; une garde le vérifie (G-01, G-02) |
| C4 | **Tag conservé** : CFT-05 reste `[REQUIS PAR LE MODULE]`, pour les seules exigences fonctionnelles |

**Sortie (phase 13) :**
1. `C7_harnais_non_regression.py` : témoins et conservation **4/4**, gardes **5/5**.
2. **Épreuve de lecture** (tests des fiches), conduite par un lecteur qui ne connaît pas ce rapport :
   - **palette** : direction neutre à un accent, identité multicolore structurelle, supervision codée par zones, correction de contraste. Qu'est-ce qui est déclaré obligatoire, conservé, calculé ?
   - **non-généricité** : scène sobre avec média porteur et fallback, même squelette avec stock décoratif, proposition sans média ;
   - **test de style** : deux objets à typographie et grille identiques, dont un avec une image explicative ; couleur porteuse ; logo décoratif isolé ; média en mouvement.
3. **Mesure M (F-SAV-002, avec / sans DG).** Au moins **trois briefs** de registres différents, chacun produit avec et sans DG corrigé. Les palettes sont classées **en aveugle** par un **observateur indépendant** (classes : neutres + un accent / multicolore / sombre + doré / autre).
   - Si la convergence persiste avec DG corrigé (N ≥ 3) : **F-SAV-002 passe Majeur** et la question de convergence est rouverte.
   - Si elle recule : la correction est **observée efficace dans ce scope**, pas au-delà.

**Limite déclarée.** Sans la mesure M, cette PATCH-DECISION corrige un texte contradictoire. **Elle ne prouve pas** qu'elle réduit l'homogénéisation. Ce point relève de l'efficacité, et aucune clôture `FULL` n'est prononcée sans observation directe.

## 7. Sortie

- **PATCH-DECISION C7 : CORRIGER.**
  - 4 textes cibles : 1 prescription retirée, 1 capacité positive, 2 conclusions d'ablation ramenées au diagnostic ;
  - aucun invariant, aucune entrée LCF.
- **F-SAV-002 : relèvement non accordé**, car la condition n'est pas remplie. Il reste ouvert et est rattaché à la mesure M.
- Listes closes inchangées : RUN_CARD et contrats **70 lignes, 66 actifs** ; LCF **16 entrées**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- La grappe la plus proche de la promesse du système a la correction la plus courte : **quatre phrases**.
- Le risque ici n'était pas un manque de règle. **Une seule phrase trop affirmative**, sous un tag fort, codifiait la pente du modèle.
- L'unité sépare nettement ce que le texte peut corriger (la contradiction) de ce que seule une mesure dira (l'effet).

**Prochaine unité : 11.15 PATCH-DECISION C8** (intégrité de release : 3 fiches, F-BLD-001, F-BLD-004, F-VDG-001 ; outillage de build et de distribution).
