# DG-AUDIT-001 — Phase 9.07 — RESISTANCE-RESULTS : lot B (surface opérationnelle)

**Scénarios §19 traités :** 05 Surface opérationnelle, 07 Contenu long, 08 Mobile, 09 État critique, 13 Accessibilité tardive, 14 Runtime différent.

**Date :** 25 septembre 2026. **Auditeur :** Claude, observateur unique (accepté par l'owner le 25-09). **Baseline :** B01, inchangée. B02 reste une hypothèse gelée.

**Unité d'audit (§9) :**

| Élément | Contenu |
|---|---|
| Cible | La chaîne STANDARD d'un écran opérationnel |
| Propriétaire principal | `ACTION` (UI-UX-REALITY, GATE-A, PRECONDITION, fraîcheur 407–411) |
| Voisins | `DIRECTION/START` 140 (protection de niveau) ; `SAVOIR/STATE`, `CONTEXT`, `TYPE` ; `BIBLIOTHEQUE/GRID` 340–411 |
| Risque dominant | Une surface soignée masque l'action, l'état ou la récupération, ou la preuve ne correspond pas au runtime réel |
| Condition de sortie | Chaque scénario a son niveau, ses oracles `+`/`−` rejoués sur objet, et sa limite |

---

## 1. Rituel

| Étape | Exécution |
|---|---|
| 1. Plan | Plan maître, état 9.06 |
| 2. Bloc précédent et checkpoints | 9.06 et 6.02b ; 9.01 lignes 05, 07, 08, 09, 13, 14 ; antécédents 4.01, 4.07, 4.08, 7.02, 9.02 |
| 3. Empreintes | B01 et protocole conformes. Pilote `0d07ee3e…8510ef` conforme. |
| 4. Protocole | §3, §19 |
| 5. Sources exactes B01 | ACTION/UI-UX-REALITY 93–110, GATE-A 660–690, fraîcheur 407–411 ; DIRECTION/START 140 ; SAVOIR/STATE 415–440, CONTEXT 708–740 ; BIBLIOTHEQUE/GRID 340–411 |
| 6. IDs concernés | F-BIB-003, F-ACT-012/018/021/022, F-DIR-007/F-ACT-017, F-VRC-004 |

**Outils :**
- Chromium 141 headless ;
- **axe-core 4.13.0**, injecté localement ; il couvre un sous-ensemble automatisable du WCAG ;
- arbre d'accessibilité Playwright ;
- émulations `forced-colors`, `reduced-motion`, `print`, facteur de pixel 2, et JavaScript désactivé.

**Viewports :** 1440 × 900, 800 × 1000 (plage tablette 650–980 px), 390 × 844 et 320 × 700 (reflow).

**Contenu long, injecté dans le DOM sur une copie en mémoire :**
- titre d'incident de 110 caractères ;
- nom de responsable long ;
- durée « 1 h 47 min » ;
- étiquette allongée ;
- mot composé allemand dans la liste.

## 2. Observations

| # | Observation | Méthode et pièce |
|---|---|---|
| O1 | Aucun débordement horizontal, troncature ni chevauchement **détecté par script** dans les 8 combinaisons (4 viewports × nominal/long) | Métriques JSON |
| O2 | **Pourtant, visuellement**, à 1440 px le mot « Hochgeschwindigkeitsverpackungsanlage » **sort de la carte de liste et touche la carte voisine**. Le script ne l'a pas vu : le débordement reste dans le viewport, avec `overflow: visible`. | `B_long_1440.png` |
| O3 | Avec le contenu long, la hiérarchie tient : titre sur 5 à 8 lignes, action toujours avant les métriques en mobile ; à 320 px, l'action descend nettement plus bas | `B_long_*` |
| O4 | axe : **seule violation, `color-contrast` (serious, 2 nœuds)** : le sous-titre et la note de bas de page, dans les 4 états et viewports testés. Confirme 6.02b (4,31 et 4,09). | Journal `axe_*` |
| O5 | Arbre d'accessibilité cohérent : `banner`, `main`, `h1`, `h2` ; boutons nommés ; `aria-pressed` sur les états de démo. **Le statut « Critique · à traiter » n'est que du texte** (aucune sémantique) ; le panneau d'action est un `complementary` sans nom ; les incidents de la liste ne sont pas interactifs. | `aria_snapshot` |
| O6 | **Séquence critique : assigner → source indisponible → retour = assignation perdue.** Le responsable redevient « À assigner » et le bouton redevient actif. Le bouton s'intitule honnêtement « Revenir à la vue d'essai » : c'est une remise à zéro de démonstration, pas une récupération. | `B_seq_*` |
| O7 | En source indisponible, l'identité de l'incident disparaît (déjà vu en 6.02b) | 6.02b B2 |
| O8 | **Liste des incidents masquée de 650 à 980 px et en dessous.** Le CSS de l'auteur prévoyait pourtant `order: 3` sous 650 px, donc une liste visible sur mobile ; la règle `display: none` de la plage 980 px l'emporte. **L'intention écrite dans le code et le rendu divergent.** | CSS lignes 94 et 117 ; captures 800/390 |
| O9 | Couleurs forcées : la structure et les bordures de B survivent ; **le bouton principal « Assigner » n'a plus de contour** (`border: 0`) et se lit comme du texte. Même défaut que A (9.06). | `B_forced_colors.png` |
| O10 | **JavaScript désactivé : les deux pilotes s'affichent l'un sous l'autre.** Le texte de A (couleurs claires prévues pour fond sombre) devient **presque illisible sur fond blanc**, car `data-case` n'est jamais posé. Les boutons d'état de B sont inertes. | `B_runtime_sans_JS.png` |
| O11 | Mode impression, mouvement réduit et facteur 2 : aucune différence de structure observée à 1440 px (le pilote n'a pas d'animation) | Captures `B_runtime_*` |
| O12 | Cibles tactiles à 390 et 320 px : tous les boutons mesurent au moins 24 × 24 px | Métriques |

## 3. Épreuve de l'accessibilité tardive (scénario 13)

Les défauts O2, O4, O8 et O9 ont été trouvés **après** la décision apparemment close de 6.02b. Conformément à DOUBLE-LOOP (signal : « … le mobile ou le runtime détruit la relation principale → build, états, fallback ») et à l'ordre de preuve d'ACTION (« P1 est non négociable »), j'ai rouvert la décision dans une **variante B′** : `variant_Bprime_accessibilite_tardive.html`, SHA-256 `f72d8b26…4be4e4`, hors B01.

Cinq modifications CSS, dont une structurelle :
1. couleur du sous-titre `#60707b` → `#4d5d68` ;
2. couleur de la note de bas de page, même valeur ;
3. contour transparent de 1 px sur les deux boutons principaux, ce qui les rend visibles en couleurs forcées ;
4. **liste rétablie sous l'alerte entre 650 et 980 px** (décision de recomposition) ;
5. `overflow-wrap: anywhere` sur les cartes.

**Résultats sur B′ :**

| Contrôle | B | B′ |
|---|---|---|
| axe (1440, 800, 390) | 2 violations de contraste | **0 violation** |
| Liste visible à 800 et 390 px | Non | **Oui**, sous l'alerte et l'action |
| Bouton principal en couleurs forcées | Sans contour | **Contour visible** |
| Mot long à 1440 px | Déborde | **Coupé dans la carte** |
| Hiérarchie : alerte → action → détails → liste | Tenue | **Tenue** (captures 800 et 390) |

Défaut résiduel mineur : sur mobile, la liste n'occupe pas toute la largeur.

**Conclusion.** Un défaut d'accès tardif **a pu modifier une décision structurelle** (présence de la liste selon le viewport) **sans détruire la direction**. L'oracle `+` du scénario 13 est réalisé dans ce périmètre.

## 4. Résultats par scénario

| Scénario | Oracle `+` | Oracle `−` | Verdict d'audit | Limite |
|---|---|---|---|---|
| **05 Surface opérationnelle** (TARGETED) | Action et état prioritaires dans le premier écran nominal, à tous les viewports. Le feedback d'assignation existe. | « Dashboard séduisant cachant action/statut » : **non observé**. En revanche, le poids visuel du statut critique reste inférieur à celui de l'action (vue de masses, 6.02b), et le statut n'est porté que par du texte (O5). | Tient, avec réserve de sémantique du statut | Aucune tâche réalisée par des opérateurs |
| **07 Contenu long** (TARGETED) | Hiérarchie et action intelligibles avec un contenu allongé (O3) | **Un mot long déborde** de sa carte (O2), **invisible pour le contrôle automatique** | Réserve, corrigée en B′ | Pas de vraie traduction ni de données réelles |
| **08 Mobile** (TARGETED) | Action remontée avant les détails ; cibles ≥ 24 px ; pas de débordement à 320 px | **Perte d'information** : la liste disparaît de 650 à 980 px et en dessous (O8). Rejoint **F-BIB-003** : des champs `MOBILE-*` ou une intention CSS ne prouvent pas le rendu. | Réserve, corrigée en B′ | Viewport émulé, pas d'appareil ni de tactile réel |
| **09 État critique** (FULL prévu) | Les états indisponible et succès existent ; la vérité est déclarée (« localement », « à reprendre sur le système réel ») | Pas de statut visuel présenté comme tâche réussie. Mais **la « récupération » est une remise à zéro qui efface l'assignation** (O6), et l'état indisponible masque l'incident (O7). En machine, l'antécédent reste valable : un LITE critique est accepté sur simple déclaration (4.01, 7.02 : F-DIR-007/F-ACT-017) ; pas de rejeu, aucune information nouvelle attendue. | **Réserve** : la récupération n'est pas modélisée | Aucun système réel, aucune permission ; efficacité FULL non close |
| **13 Accessibilité tardive** (FULL prévu) | **Réalisé** : décision rouverte, méthode adaptée (axe, couleurs forcées, reflow), B′ vérifiée (§3) | « Test non exécuté conservant PASS » : non observé sur les pilotes (ils ne revendiquent rien). Antécédent 4.07 : l'exemple JSON revendique « focus vérifié » sans provenance (F-ACT-012/018/021), inchangé. | Tient dans le périmètre | Aucun lecteur d'écran, aucun utilisateur ; axe ne couvre qu'une partie du WCAG ; auto-correction par l'auditeur |
| **14 Runtime différent** (FULL prévu) | **Fraîcheur appliquée** : B′ est une nouvelle version. Les preuves de contraste, de mobile et de couleurs forcées de 6.02b **ne valent plus pour B′** (ACTION 409) et ont été refaites sur B′. | **Runtime sans JavaScript : A devient illisible** et les deux pilotes se superposent (O10). Une preuve faite avec JavaScript ne vaut pas pour ce runtime. En machine, l'antécédent reste valable : une carte V2 avec une preuve V1 est admise (9.02, F-ACT-022). | Tient au niveau procédure ; **réserve** sur la robustesse du runtime | Un seul moteur disponible (Chromium) : **Firefox et Safari NOT-VERIFIED** |

## 5. Ce que le lot apprend sur Design Governance

- **Positif.** Les exigences d'UI-UX-REALITY et de GATE-A **nomment exactement les défauts trouvés** : contraste calculé, information non chromatique, états, `RESPONSIVE-RELATION`, récupération. Appliquées au rendu, elles permettent une correction ciblée qui ne casse pas la direction (B′). C'est le deuxième cas, après A → A2, où suivre DG modifie un artefact dans le bon sens. N = 2, auto-évalué.
- **Épistémologie de la preuve (§3, §7.5), deux observations nettes :**
  - un contrôle automatique vert (O1) **a manqué** un débordement visible (O2) ;
  - une règle CSS **d'intention** (O8) **contredit** le rendu.

  Les deux confirment, sur objet réel, la règle B01 : « une capture prouve le rendu » et une déclaration ne le prouve pas (VISUAL_PROOF 618 ; SAVOIR/CONTEXT « une phrase de conformité ne remplace pas un contrôle »). **La règle est juste ; c'est son application qui manque.**
- **Écart de couverture.** B01 demande de documenter « fallback statique, … runtime » (SAVOIR/CONTEXT, motion) et de lier la preuve au runtime (fraîcheur), mais **aucune route n'invite à tester un runtime dégradé** : sans JavaScript, couleurs forcées. Les deux défauts O9 et O10 n'apparaissent que là. C'est une hypothèse de capacité à examiner en phase 10 ; elle n'appelle **pas de nouvel ID** tant que les constats GATE-A et CONTEXT existants n'ont pas été relus fiche par fiche.

## 6. Sortie

**Cumul phase 9 : 17/20 scénarios examinés** : 6 en contrat seulement, 11 en contrat et sur objet observé. **0/20 FULL d'efficacité clos.** Restent le lot C (01, 03, 19) et les micro-runs.

**Registre : 157 fiches provisoires, aucun nouvel ID.** Renforts par observation :

| Fiche | Renfort |
|---|---|
| F-BIB-003 | Mobile déclaré ≠ rendu |
| F-DIR-007 / F-ACT-017 | État critique, antécédent |
| F-ACT-012/018/021/022 | Claims et fraîcheur |

Aucun patch B01, aucun verdict global.

**§32 — ce que l'unité a changé :**
- elle a montré qu'un contrôle automatisé vert peut coexister avec un défaut visible, **argument concret pour garder la capture obligatoire** ;
- elle a transformé l'accessibilité tardive en décision structurelle vérifiée (B′) ;
- elle a révélé la fragilité en runtime dégradé des deux pilotes.

**Question du §32 non résolue :** le scénario 09 « FULL » reste impossible à conclure sans système réel. Il faudra décider en phase 14 si ce niveau était atteignable dans ce périmètre.

**Prochaine unité : 9.08, lot C** (01 brief vague, 03 correction locale, 19 surcharge procédurale), par micro-runs §28. Une production suivra DG ; elle sera comparée à une production sans DG sur le même brief, avec le test de convergence de style issu de 9.06.
