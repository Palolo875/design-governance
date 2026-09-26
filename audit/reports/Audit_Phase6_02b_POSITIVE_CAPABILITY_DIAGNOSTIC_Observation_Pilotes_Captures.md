# DG-AUDIT-001 — Phase 6.02b — POSITIVE-CAPABILITY-DIAGNOSTIC : observation des pilotes sur rendu

**Date :** 25 septembre 2026. **Auditeur :** Claude.

**Baseline :** B01, inchangée. B02 reste une hypothèse gelée et n'intervient pas dans cette unité.

**Décision de l'owner, explicite (formulaire du 25-09) :**
- ordre : « 6.02 puis lots A/B/C » ;
- B02 : « Geler comme hypothèse ».

**Portée :** cette unité conclut 6.02 dans le périmètre des deux pilotes déjà construits. Elle ne mesure pas l'efficacité de Design Governance (§3.2) : elle observe des objets.

---

## 1. Rituel et continuité

| Étape | Exécution |
|---|---|
| Plan maître | `01_Reprise/Plan_Maitre_Audit_Design_Governance-1.md` de l'archive complète. Octets identiques au plan transmis le 25-09. |
| Bloc précédent et checkpoint | 6.02 (préparation) et 6.01, relus en entier. Dernier bloc d'audit conforme : 9.05. Recadrage : R01. |
| Empreintes | Compilation `016e6002…5f355d` : OK. Protocole `990fc86f…dc20610dd` : OK. Pilotes : `phase6_02_pilotes.html` `0d07ee3e…8510ef` et `phase6_02_mobile_harness.html` `c443562c…4a367b`. Identiques à 6.02, et dans le ZIP. |
| Protocole | §3 (contrat / efficacité), §16 (dix dimensions), §28 (micro-runs), relus |
| Sources exactes B01 | DIRECTION/FIRST-OBJECT 314–339 (huit dimensions du premier objet) et VISUAL_TARGET 373–405 ; SAVOIR/CFT-00 211–228 ; ACTION/UI-UX-REALITY 93–110, VISUAL_PROOF 604–619, GATE-B/B1b 700–720, GATE-C 775–794 |
| Constats liés, par ID | F-DIR-009, F-PC-001, F-ACT-005/007/012/018/021/022, F-BIB-005 (repris de 6.01), F-SAV-002 (famille G). Aucun nouvel ID. |
| Pièces manquantes | Aucune pour cette unité |

**Méthode d'ouverture.** J'ai ouvert les pilotes en `file://` avec le Chromium headless de l'environnement Cowork (Playwright, Chromium 141.0.7390.37), sur une copie de travail. La restriction rencontrée en 6.02 appartenait au navigateur de l'auditeur précédent. Ici, ouvrir un fichier local avec l'outil prévu de l'environnement n'est pas un contournement de cette politique.

## 2. Ce qui est observé, et ce qui ne l'est pas

**Quatre niveaux**, repris de 6.02 :
- (1) règle B01 ;
- (2) pilote construit par l'auditeur précédent ;
- (3) **rendu inspecté, maintenant disponible** ;
- (4) personnes, tâche, préférence : **toujours non observé**.

**Limites de l'observation elle-même :**
- **Un seul observateur**, Claude : ce n'est ni un humain du public visé, ni une revue indépendante au sens B3. Je ne suis pas l'auteur des pilotes, mais un avis unique reste un avis situé (VISUAL_PROOF 618).
- **Polices de substitution.** Le pilote demande `Georgia` et `system-ui` ; l'environnement rend en **DejaVu Serif** et **DejaVu Sans**. Le critère C2 (typographie) et la matière typographique ne sont donc **pas jugeables tels que voulus** par l'auteur.
- **Audio.** `AudioContext` existe et le clic change le statut (« Motif synthétique lancé localement… »), mais aucune sortie sonore n'a été écoutée : pas de périphérique audio. L'écoute reste **NOT-VERIFIED**.
- **Mobile.** Le « mobile » est un viewport de 390 × 844 px (direct, et via le cadre prévu en 6.02) : pas d'appareil réel ni de tactile.
- **Contraste.** Calculé automatiquement sur les couleurs calculées. Les textes posés sur le dégradé ou l'image du relief (5 libellés de A) ne sont **pas calculés**.

**Pièces produites** (le dossier `captures/` contient les chemins exacts, les empreintes et un journal JSON) :

| ID | État | Viewport |
|---|---|---|
| A1 | A normal | 1440 × 900, pleine page |
| A2 | A indisponible (paramètre d'URL) | 1440 × 900 |
| A3 | A après « Écouter » | 1440 × 900 |
| A4 | A après bascule d'indisponibilité | 1440 × 900 |
| B1 | B normal | 1440 × 900 |
| B2 | B source indisponible | 1440 × 900 |
| B3 | B succès (paramètre d'URL) | 1440 × 900 |
| B4 | B après clic « Assigner » | 1440 × 900 |
| B5 | B indisponible puis « Revenir » | 1440 × 900 |
| M_* | A normal, B normal, B indisponible | 390 direct et cadre mobile |
| K_* | Focus clavier, séquence de 8 tabulations | 1440 × 900 |
| V_masses_* | Vues de masses (flou) de A1 et B1 | — |
| B1b | Paire sur A | 1440 × 900 |
| — | Planche récapitulative `PLANCHE_6_02_observation.png` | — |

## 3. Observations factuelles (mesurées ou vues)

| Observation | Pilote | Pièce |
|---|---|---|
| Pas de débordement horizontal, desktop comme 390 px | A, B | métriques |
| Focus clavier visible sur tous les boutons (contour de 3 px, orange #D87234) ; ordre de tabulation cohérent | A, B | K_* |
| En B, le clavier traverse d'abord les 3 boutons d'**états de démonstration** avant l'action « Assigner » ; les incidents de la liste ne sont pas focusables | B | K_incident |
| Contraste : aucun texte calculé de A sous le seuil (ratio minimum 7,3). **En B, deux textes sont sous 4,5:1** : le sous-titre « Une alerte prioritaire… » (4,31) et la note de bas de page (4,09) | A, B | métriques |
| Les gestes s'exécutent : « Écouter » change le statut ; la bascule désactive « Écouter » (`disabled=true`) ; « Assigner » passe le responsable à « Équipe d'astreinte », change l'étiquette et le bouton, et affiche la note « Assignation locale simulée » ; « Revenir » restaure la vue | A, B | A3, A4, B4, B5 |
| **A indisponible : le bouton « Écouter » désactivé garde exactement l'apparence d'un bouton actif** (aucun style `:disabled`) | A | A2, A4 |
| **À 980 px et moins, la liste des incidents est masquée** (`display:none`) : à 390 px, rien n'indique qu'il existe un second incident (« Flux · 02 » disparaît) | B | M_direct390_incident |
| À 390 px, **l'objet de preuve de A (le relief) arrive après le texte, les deux boutons et les mentions**, à environ 665 px de haut : il est à peine visible dans le premier écran | A | M_direct390_sound |
| À 390 px, B remonte l'action « Assigner » avant les métriques et les détails | B | M_direct390_incident |
| Source indisponible en B : la vue d'incident entière est remplacée par un message, et l'identité de l'incident en cours disparaît | B | B2 |
| Marquage de vérité présent et visible dans les deux pilotes (bandeau « PILOTE FICTIF… », note de bas de page, « hypothèse ») | A, B | A1, B1 |
| Le premier écran desktop laisse environ 25 % bas vide dans les deux pilotes | A, B | A1, B1 |

## 4. Les dix dimensions §16 sur rendu

**Lecture :**
- **Tient** : l'observation soutient la dimension dans ce périmètre.
- **Réserve** : écart observé ou limite de méthode.
- **Non vérifié** : preuve absente.

Aucune case n'est un `PASS` de gate B01 : ce sont des constats d'audit.

| Dimension | A — « Strates » (scène identitaire) | B — « Signal/atelier » (écran opérationnel) |
|---|---|---|
| **Présence** | **Tient (desktop).** Deux masses nettes (titre et relief), foyer lumineux au centre du relief, confirmé par la vue de masses. **Réserve mobile** : le foyer n'est pas dans le premier écran. | **Tient.** L'en-tête sombre, le titre de l'incident et l'action forment une hiérarchie lisible. Réserve : dans la vue de masses, le signal « critique » (petite étiquette et filet orange) pèse moins que le bouton d'action. |
| **Point de vue** | **Réserve.** Une position existe : écouter une ville par couches. La **paire B1b** (§5) montre que le relief ne la porte que faiblement. | **Tient.** Choix net : une alerte au centre, une décision à droite. La cause est marquée comme hypothèse. |
| **Spécificité** | **Réserve forte.** Test de substitution : en remplaçant « ville » par « méditation », « astronomie » ou « podcast », la scène tient sans changement. Rien dans l'objet ne renvoie à une ville (ni tracé, ni lieu, ni orientation réelle). | **Tient.** Convoyeur, relevé 08:41, capteur, responsable : les données appartiennent à la tâche, et elles sont marquées fictives. |
| **Composition** | **Tient (desktop)** : asymétrie texte/objet, alignements propres. **Réserve** : bas de viewport vide ; ordre mobile. | **Tient** : trois colonnes lisibles. **Réserve** : le foyer est partagé entre le titre (centre) et l'action (colonne droite) ; la barre d'états de démo occupe une place de premier plan, surtout sur mobile. |
| **Matière et type** | **Non vérifié en l'état.** La matière native au code (anneaux, trame, halo) est cohérente, mais la typographie est rendue avec une police de substitution. | **Non vérifié en l'état**, même raison ; la hiérarchie des graisses reste lisible avec la police de substitution. |
| **Désirabilité située** | **Réserve.** L'attrait vient surtout du registre sombre + serif + doré, que SAVOIR/CFT-00 écarte explicitement comme définition du premium. Il vient peu de la relation ville/écoute. Avis d'un seul observateur. | **Tient, sous réserve** : l'impression de confiance vient de la clarté (cause, heure, responsable). Public non testé. |
| **Résolution** | **Réserve** : bouton désactivé sans état visuel ; audio non écouté. | **Réserve** : deux contrastes sous le seuil ; liste masquée en dessous de 980 px ; succès sans horodatage ni auteur. **Tient** pour le feedback d'assignation et le retour. |
| **Retenue** | **Tient** : pas de photo fictive ni de décor ajouté ; le relief abstrait assume l'absence d'asset. | **Tient** : pas de décor ; l'orange est réservé au critique. |
| **Habitabilité** | **Tient dans le périmètre** : ouvrable, geste exécutable, limites déclarées. | **Tient dans le périmètre** : premier geste, feedback, indisponible, retour. Aucune tâche réelle. |
| **Transfert** | **Réserve** : sur mobile, le relief passe sous les textes, ce qui contredit « l'objet arrive avant les bénéfices » (FIRST-OBJECT 316). | **Réserve** : recomposition mobile utile pour l'action, mais perte de la liste ; indisponible sans rappel de l'incident. Tablette (650–980) non capturée. |

## 5. B1b sur A, requis dans son scope

**Scope.** A est une surface `DIRECTION` ; son risque V/craft est dominant ; le relief n'avait jamais été confronté à une variante. B1b est donc requis (ACTION 702–704). Pour B, surface `STANDARD`, B1b est **N/A-JUSTIFIED** : hors de son scope.

**Lecture légère, sans lire le texte.** La surface raconte : « landing éditoriale sombre et haut de gamme d'une application audio ou de bien-être ; preuve : une illustration abstraite ». Le récit implicite ne dit pas « ville ».

**Décision mise à l'épreuve.** L'inclinaison alternée des anneaux du relief.

**Édition.** Réduction réversible : les six rotations passent à 0°. Rien n'est ajouté. Variante : `variant_B1b_rings_untilted.html`, SHA-256 `5a9993f3…402d6e`, hors B01, comme copie de travail.

**Résultat de la comparaison (paire `B1b_pair_A_rings.png`) :**
- Les anneaux droits se lisent davantage comme des **strates emboîtées** (courbes de niveau).
- Les anneaux inclinés se croisent et évoquent plutôt des **orbites**, mais rendent l'objet moins mécanique.
- Aucune des deux versions ne fait apparaître la **ville**.

**Décision.** Conserver l'original est défendable pour le craft. Surtout, la paire montre que **le défaut dominant n'est pas l'inclinaison mais l'absence d'ancrage urbain dans l'objet de preuve**. La correction relèverait de VISUAL_TARGET (relation, opération dominante), pas d'un polish.

**Statut.** Comparaison faite par un observateur unique, non auteur. Elle reste `EXPLORATORY` pour une décision identitaire, avec cette prochaine preuve : un regard humain du public visé, ou au minimum celui de l'owner.

## 6. Ce que cela apprend sur Design Governance, dans les limites de l'échantillon

- **Positif, observé.** Les pilotes rendent visibles plusieurs exigences B01 : marquage de vérité, CTA à comportement local réel, états indisponible et succès, retour, recomposition mobile qui remonte l'action en B, retenue sans faux asset. Ce sont des traces concrètes de FIRST-OBJECT (316–318) et d'UI-UX-REALITY.
- **Écarts, observés sur les pilotes, pas sur B01.** Objet placé après le texte sur mobile (A), liste perdue sous 980 px (B), état désactivé invisible (A), contrastes sous le seuil (B). B01 contient déjà les règles correspondantes : FIRST-OBJECT 316 et « Résilience visible », UI-UX-REALITY (`RESPONSIVE-RELATION`), GATE-A (contraste, états). **Les règles existaient ; elles n'ont pas empêché ces écarts** chez un auteur qui connaissait le système. N = 2 objets et 1 auteur : cela reste une observation, pas un défaut du système.
- **Risque d'homogénéisation (§7.4).** A converge vers un canon « sombre + serif + doré » que SAVOIR/CFT-00 déconseille explicitement comme définition du premium, et sa spécificité ne résiste pas au test de substitution. C'est un signal pour la famille G, **rattaché à F-SAV-002** (prescription possible de neutres/accent), sans nouvel ID. N = 1.
- **Ce qui n'est pas établi.** Que B01 augmente la probabilité d'obtenir ces objets. Il faudrait comparer avec une production sans le protocole (§29, dernier signal), avec d'autres auteurs, et une observation humaine. Cela relève des micro-runs du §28.

## 7. Sortie

**6.02 est conclue dans son périmètre** : deux pilotes, rendus, gestes, états, clavier, contraste calculé, mobile 390 px et une paire B1b.

**Phase 6 :**
- volet documentaire et perceptuel sur pilotes : **couvert** ;
- volet efficacité (le système produit-il de meilleurs objets ?) : **ESCALATED vers les micro-runs du §28**, avec comme prochaine preuve au moins un brief réel produit avec DG et comparé à une production sans DG.

**Registre :** 157 fiches provisoires, aucun nouvel ID. Rapprochements enregistrés avec F-SAV-002 (homogénéisation) et F-BIB-005 (spécificité portée par l'objet plutôt que par une signature spatiale). Aucun patch, aucun verdict global.

**Bureaucratisation (§32) — ce que l'unité a changé :**
- elle a produit la **première observation de rendu de la campagne** ;
- elle a déplacé le doute principal sur A, du craft (inclinaison) vers la relation promesse / objet (spécificité) ;
- elle a transformé 6.02 d'« en attente » en « conclue avec réserves ».

**Pour l'owner (second regard, §29 « plusieurs reviewers »).** Parcourir `PLANCHE_6_02_observation.png` et dire, sans lire ce rapport :
1. qu'est-ce que A semble vendre ?
2. dans B, où va l'œil en premier ?

Tes réponses confirmeront ou contrediront les lignes Spécificité et Présence.

**Prochaine unité : phase 9, lot A** (scénarios 02 one-shot, 04 direction identitaire, 10 asset absent, 11 référence séduisante, 12 style recyclé), sur le pilote A et ses captures, avec le même rituel.
