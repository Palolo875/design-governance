# DG-AUDIT-001 — Phase 9.06 — RESISTANCE-RESULTS : lot A (direction)

**Scénarios §19 traités :** 02 One-shot, 04 Direction identitaire, 10 Asset absent, 11 Référence séduisante, 12 Style recyclé.

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :**
- phase 9 par lots A, B puis C (formulaire du 25-09) ;
- l'owner s'en remet aux constats de 6.02b sans second regard (message du 25-09). **Conséquence : l'unique observateur reste Claude.** Cette limite vaut pour tout ce rapport.

**Unité d'audit (§9) :**

| Élément | Contenu |
|---|---|
| Cible | La chaîne DIRECTION de la première scène |
| Propriétaire principal | `DIRECTION` (START, VISUAL_TARGET, FIRST-OBJECT, DOUBLE-LOOP, REUSE-CHALLENGE) |
| Voisins | `SAVOIR/SOURCE`, `SAVOIR/STYLE` et `CFT-00` ; `ACTION` (FIRST-RENDER, B1b, GATE-C, droits 429–435) ; projection `RUN_CARD` |
| Risque dominant | Une scène séduisante mais non située passe pour une direction résolue |
| Condition de sortie | Chaque scénario a son niveau, ses oracles `+`/`−` rejoués sur objet ou machine, et sa limite |

---

## 1. Rituel

| Étape | Exécution |
|---|---|
| 1. Plan | Plan maître, état 6.02b |
| 2. Bloc précédent et checkpoints | 6.02b ; 9.01 lignes 02, 04, 10, 11, 12 ; 9.05 ; checkpoints phase 2 de DIRECTION et SAVOIR disponibles dans l'archive complète |
| 3. Empreintes | B01 `016e6002…5f355d` et protocole `990fc86f…dc20610dd` : conformes. Pilote `0d07ee3e…8510ef` : conforme. |
| 4. Protocole | §3, §7.4, §17 (one-shot, double boucle), §19 |
| 5. Sources exactes B01 | DIRECTION/DOUBLE-LOOP 482–521, REUSE-CHALLENGE 355–370, FIRST-OBJECT 314–339, VISUAL_TARGET 373–405 ; SAVOIR/SOURCE 471–529, 363 (palette par rôles), 568 et 597 (familles et profils), CFT-00 211–228 ; ACTION/FIRST-RENDER 79–92, B1b 700–720, GATE-C 775–794, droits 429–435 |
| 6. IDs concernés | F-DIR-009, F-PC-001, F-SAV-002, F-SAV-003, F-BIB-005, F-RC-001, F-ACT-021 |
| 7. Tests | Voir §2 et §3 |

## 2. Épreuves exécutées

**Objets observés :**
- le pilote A de 6.02, inchangé ;
- **A2**, une variante construite par l'auditeur pour éprouver la double boucle (`variant_A2_ancrage_urbain.html`, SHA-256 `0d787584…cfff40`, hors B01).

**Construction de A2.** J'ai appliqué la règle DG à A observé : l'échec du test « Signature située » renvoie à « contrat, contre-choix, anti-direction » (DOUBLE-LOOP 494–497 et signaux de réouverture 505–512). **Une seule relation change** : l'objet de preuve devient un plan fictif, avec des strates d'écoute déformées autour de trois lieux (Gare, Marché, Quai) et coupées par un fleuve et deux rues. Palette, typographie, texte et mise en page sont inchangés, pour isoler la variable.

**Ancre déclarée, selon la fiche SAVOIR/SOURCE :**

| Champ | Contenu |
|---|---|
| SOURCE | Conventions des courbes de niveau et des plans urbains, **connaissance générale non revérifiée** |
| ROLE | Direction |
| RETAINED | Courbes comme strates ; fleuve et rues comme coupures |
| REJECTED | Carte plate à pins (anti-direction de l'exemple) ; imagerie satellite |
| HOW-TRANSFORMED | Strates d'écoute polarisées par des lieux fictifs |
| LIMIT | Ni calibration externe, ni droit, ni préférence de public |

**Captures (dossier `lotA/`) :**
- A2 en desktop 1440 × 900 et en mobile 390 ;
- A et A2 en `forced-colors: active` ;
- A sans relief ;
- paire A/A2 et planche récapitulative.

**Rejeux machine sur le validateur B01** (copies en mémoire de `valid_direction_with_profile_decision.json`) :

| Cas | Entrée | Résultat |
|---|---|---|
| T0 | Témoin | Admise |
| **T1** | `ACCEPTED`, `HELD`, alors que `creative_close.signature` et `dominant_defect` disent eux-mêmes « scène substituable, signature non située » | **Admise** |
| T2 | DIRECTION acceptée sans aucune ancre | Refusée : « DIRECTION exige au moins un ancrage structuré » |
| T3 | Ancre de convention non revérifiée, déclarée `transformed` | Admise |
| T4 | Ancre non transformée sous acceptation | Refusée |
| T5 | Ancre qui retient le canon premium et ne rejette rien | Refusée : « rejected non vide ». Il suffirait d'ajouter un seul rejet déclaratif pour qu'elle passe. |

## 3. Résultats par scénario

### 02 One-shot — FULL (prévu) ; exécuté sur objet et machine

**Oracle `+` (arrêt légitime après rendu inspecté).**
- **A : non atteint.** Les cinq tests de DOUBLE-LOOP, appliqués au rendu observé :
  - Promesse et geste : tient ;
  - Vérité de scène : tient ;
  - **Signature située : échoue**. Le test de substitution de 6.02b s'applique exactement : « Le produit pourrait-il être remplacé… ? » ;
  - Finition qui sert : réserve (mobile, bouton désactivé) ;
  - Preuve précoce : partielle.

  **La règle DG discrimine correctement ce cas : elle interdit de s'arrêter.**
- **B (STANDARD) :** l'arrêt est presque atteint. Seules des corrections de finition restent (deux contrastes, liste masquée), sans défaut de signature.

**Oracle `−` (one-shot faible déclaré fort).**
- Au niveau du **texte**, B01 l'interdit explicitement : « ne transforme pas `EXPLORATORY` en permission de livrer une première proposition creuse », DOUBLE-LOOP 501.
- Au niveau **machine**, **T1 passe** : une carte peut s'auto-accepter tout en nommant elle-même le défaut de signature. La protection repose donc entièrement sur le jugement de l'agent qui remplit la carte. Même famille que les limites déjà ouvertes : rationale non vérifiée (7.01), F-ACT-021 et F-DIR-009. **Pas de nouvel ID.**

**Double boucle (§17).** A → A2 **modifie une relation visible**, donc l'itération compte au sens du §17.

| Effet de A2 | Observation |
|---|---|
| **Gain** | Le test de substitution échoue désormais pour « méditation » ou « astronomie » : fleuve, rues et lieux nommés appartiennent à une ville. |
| **Régression : foyer** | Les deux rues et le fleuve traversent le point d'écoute et concurrencent le foyer. |
| **Régression : support dégradé** | Voir scénario 10. |

Conformément à DOUBLE-LOOP 499, ce n'est pas une amélioration « nette » : c'est un **nouveau défaut dominant (foyer) à traiter dans une boucle suivante**.

**Limite.** Auto-comparaison : l'auteur de A2 est aussi son observateur (B1b/B3). Aucune comparaison avec une production faite sans DG. **Aucun FULL d'efficacité clos.**

### 04 Direction identitaire — FULL (prévu) ; exécuté sur objet et machine

**Confrontation de A aux champs de VISUAL_TARGET** (373–405) :

| Champ | A | A2 |
|---|---|---|
| Thèse | Présente, mais dans le texte seulement | Inchangée |
| Opération dominante (« relation par laquelle une donnée rend la promesse perceptible ») | Faible : anneaux génériques | Rend la promesse perceptible |
| Ancre | **Absente** alors que la surface est identitaire. SAVOIR/SOURCE 475 impose dans ce cas `NOT-VERIFIED` sur les axes concernés, et la projection refuserait une carte DIRECTION sans ancre (T2). | Ancre de convention déclarée |
| Anti-direction (« carte à pins ») | Évitée | Évitée |

**Oracle `−` (« image séduisante tenue pour direction résolue »).** A est exactement ce cas.
- **B01 le détecte au texte** : FIRST-OBJECT, dimension Signature (« retour si… remplacé sans modifier la scène ») ; signaux de réouverture de DOUBLE-LOOP ; B1b (6.02b).
- **Au niveau machine**, il n'est détecté que partiellement : T2 refuse l'absence d'ancre, mais T1 admet l'auto-acceptation.

**Oracle `+` (cible, geste, ancre située, premier objet, comparaison observable).**
- **Réalisé sur A2 dans ce périmètre** : ancre déclarée et transformée, paire A/A2 comparable.
- **Réserve** : foyer, et jugement d'un seul observateur.

**Constat positif.** Appliqué à un objet réel, DIRECTION **oriente la correction vers la bonne décision** (la relation objet/promesse) et non vers un polish. C'est la première observation de la campagne où le système change effectivement un artefact dans le bon sens. **N = 1, auto-évaluée.**

### 10 Asset absent — TARGETED ; transformé en « support dégradé »

**Adaptation du scénario.** A n'utilise aucun asset externe : le relief est du code natif, que VISUAL_TARGET reconnaît comme choix complet. Le risque « indisponible » ne peut donc pas s'appliquer tel quel. Je l'ai remplacé par deux épreuves : le relief retiré, et le mode de couleurs forcées.

| Épreuve | Observation |
|---|---|
| Relief retiré | La scène se réduit à du texte et des boutons ; la promesse « par strates » n'est plus perceptible. Le relief porte donc toute la preuve. **Aucun fallback ni condition de retrait n'est déclaré**, alors que VISUAL_TARGET (« Matière / asset : … fallback et condition de retrait ») le demande. |
| Couleurs forcées, A | Les anneaux (bordures CSS) **survivent**. **Le bouton principal « Écouter » perd toute affordance** : `border: 0`, il s'affiche comme un simple texte. Défaut du pilote, observé, relevant de GATE-A (information non chromatique, états). |
| Couleurs forcées, A2 | Les strates SVG (couleurs codées en dur) **deviennent presque invisibles** sur fond blanc : la matière plus riche est plus fragile. |

**Oracle `+`** (composition native qui porte encore la promesse) : **partiel**. A tient en couleurs forcées ; A2 non.
**Oracle `−`** (scène vidée) : observé si l'objet est retiré, sans fallback prévu.

La règle B01 existe ; le pilote ne l'applique pas. Pas de nouvel ID.

### 11 Référence séduisante — TARGETED ; machine et objet

| Épreuve | Observation |
|---|---|
| Machine | T4 refuse une ancre non transformée ; T5 refuse une ancre sans rejet. **Mais « transformed » et « rejected » restent déclaratifs** : T3 passe sur ma seule affirmation, et T5 passerait avec un rejet ajouté pour la forme. Prolonge F-RC-001 (statut d'ancre) et la limite générale « forme ≠ réalité » (famille E), sans nouvel ID. |
| Objet | A2 montre une convention (courbes de niveau, plan) **transformée** plutôt que copiée : pas de carte reconnaissable, pas de style cartographique emprunté, relation propre à « écouter par strates ». Jugement de l'auteur de A2 : auto-évaluation. |
| Calibration | L'ancre est une connaissance non revérifiée. SAVOIR/SOURCE 477 l'admet comme hypothèse, pas comme calibration externe. **Aucune référence réelle ouverte : le calibrage reste NOT-VERIFIED.** |

### 12 Style recyclé — TARGETED ; essai contrastif de sélection

**Cas 1, réemploi déclaré** : appliquer le registre de A (sombre, serif, or) à l'outil d'incidents B. REUSE-CHALLENGE (361–369) exige un `KEEP-IF` qui « ne peut pas se réduire à premium, moderne, beau, cohérent ». Aucune conséquence située ne tient : l'urgence, la lisibilité des données et le contraste d'état vont à l'encontre de ce registre. → **Réemploi refusé par la règle. Oracle `−` tenu.**

**Cas 2, convergence implicite** : A lui-même.
- Aucun antécédent ni profil n'est déclaré, donc **REUSE-CHALLENGE ne se déclenche pas** : son déclencheur (358) vise un élément « disponible » dans le contexte, pas un canon latent du modèle.
- SAVOIR 363 prescrit « les neutres portent l'essentiel de la structure ; l'accent signale une action, un focus, un état » : A applique exactement cette structure (fond neutre sombre, un accent doré) **et aboutit au canon premium que CFT-00 (228) dit ne pas constituer le premium**.
- Tension interne observée sur un objet. **Elle renforce F-SAV-002** (prescription possible de neutres/accent) avec une première observation perceptuelle, **N = 1**. Pas de nouvel ID.

**Oracle `+`** (`WHY-NOW`, différence située ou absence de profil) : non applicable à A, faute de profil déclaré.

**Lacune d'observation.** La protection de B01 couvre le réemploi **déclaré**. Rien n'oblige à tester la **convergence par défaut** : il n'existe pas de « REUSE-CHALLENGE » contre les priors du modèle. C'est une **hypothèse à éprouver dans les micro-runs du lot C**, par exemple en faisant produire plusieurs briefs et en mesurant la convergence de registre (§29 : « modules systématiquement contournés », « qualité perçue »).

## 4. Synthèse du lot

| Scénario | Niveau | `+` | `−` | Porté par | Limite principale |
|---|---|---|---|---|---|
| 02 One-shot | FULL, en contrat et sur objet | A : non atteint, à raison ; B : presque | Interdit au texte ; **admis en machine (T1)** | Jugement de l'agent | Auto-comparaison ; pas de base sans DG |
| 04 Direction identitaire | FULL, en contrat et sur objet | Réalisé sur A2 avec réserve de foyer | Détecté au texte ; en machine partiellement (T2 oui, T1 non) | FIRST-OBJECT, DOUBLE-LOOP, B1b | N = 1 ; observateur unique |
| 10 Asset absent → support dégradé | TARGETED | Partiel (A oui, A2 non) | Scène vidée sans fallback déclaré | VISUAL_TARGET (fallback), GATE-A | Couleurs forcées émulées, pas d'appareil réel |
| 11 Référence séduisante | TARGETED | A2 transforme | Refus machine seulement sur les champs vides | SAVOIR/SOURCE, projection | Transformation déclarative ; pas de référence réelle |
| 12 Style recyclé | TARGETED | N/A pour A | Réemploi déclaré refusé ; **convergence implicite non couverte** | REUSE-CHALLENGE, SAVOIR 363, CFT-00 | Hypothèse à tester en micro-runs |

**Cumul phase 9 : 11/20 scénarios examinés** : 6 en contrat seulement, 5 en contrat et sur objet observé. **0/20 FULL d'efficacité clos** : il manque une base sans DG, plusieurs observateurs et des tâches réelles.

**Registre : 157 fiches provisoires, aucun nouvel ID.** Fiches renforcées par une observation d'objet :

| Fiche | Renfort |
|---|---|
| F-SAV-002 | Neutres + accent → canon |
| F-DIR-009 | Arrêt et one-shot tenus par le seul jugement |
| F-RC-001 | Statut d'ancre déclaratif |
| F-BIB-005 | La spécificité est portée par la relation de l'objet, pas par une signature spatiale |
| F-ACT-021 | Auto-acceptation admise |

Aucun patch, aucun verdict global.

**§32 — ce que l'unité a changé :**
- **première correction guidée par DG observée sur un artefact** (A → A2), qui déplace le défaut dominant de « signature » vers « foyer » ;
- **lacune identifiée** : la convergence implicite de style n'est couverte par aucun déclencheur, ce qui oriente la conception du lot C ;
- le scénario 10 a dû être adapté : « asset absent » ne s'applique pas tel quel à une matière native. Ambiguïté du protocole à noter pour la clôture (§32, question 8).

**Prochaine unité : 9.07, lot B** — scénarios 05 surface opérationnelle, 07 contenu long, 08 mobile, 09 état critique, 13 accessibilité tardive, 14 runtime différent — sur le pilote B, avec tablette (650–980 px), contenu allongé, couleurs forcées et clavier.
