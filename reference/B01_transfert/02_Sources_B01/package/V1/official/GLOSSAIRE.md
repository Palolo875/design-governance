# Glossaire — Design Governance V1

Ce glossaire explique les mots nécessaires pour commencer. Il n’ajoute aucune règle et ne remplace pas les cinq sources normatives.

| Terme | Signification simple |
|---|---|
| **Décision** | Le choix concret que le travail doit permettre de prendre, de confirmer ou d’abandonner. Exemple : conserver la structure d’un bouton tout en améliorant sa lisibilité. |
| **Risque** | Le coût possible d’une mauvaise décision. Il peut concerner l’apparence, l’usage, l’accessibilité, la technique ou un système partagé. |
| **JTBD** | « Job to be done » : la tâche ou le progrès concret que la personne cherche à accomplir dans le contexte déclaré. |
| **Blast radius** | L’étendue des consommateurs, surfaces ou décisions susceptibles d’être touchés par un changement. |
| **Preuve** | Ce qui permet de confirmer ou d’infirmer une décision dans un périmètre déclaré : observation, capture, test, mesure, comparaison ou retour adapté. |
| **Mode** | Le niveau de protection et de trace adapté au travail : `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. |
| **FAST-PATH** | Une vue courte pour un delta local ou une décision presque tranchée. Elle réduit la formalité, jamais la preuve requise ni l’honnêteté du statut. |
| **Façade d’activation** | Le cadrage court avant les routes détaillées : mode, risque dominant, décision à changer, prochaine preuve et owner. Elle n’est ni un nouveau mode ni un nouveau gate. |
| **Source propriétaire** | Le fichier normatif responsable d’une règle. Un guide peut la résumer, mais ne peut pas la remplacer. |
| **Run** | Un travail délimité, avec une décision, un risque, un artefact, une preuve et une clôture. |
| **RUN_CARD** | La trace structurée d’un run lorsque la ligne minimale ne suffit plus : décision, risque, artefact, preuve, limite et clôture. |
| **Artefact** | Le résultat concret que l’on peut inspecter : code, écran, capture, composant, test, diff ou autre livrable. |
| **Owner** | La personne ou l’équipe responsable de la décision, de la reprise ou de l’escalade. |
| **Scope** | Le périmètre réellement couvert par la construction ou la preuve : vues, états, appareils, consommateurs, données ou tâches. |
| **Limite** | Ce que le travail ne permet pas d’affirmer honnêtement. Une limite n’est pas un échec caché ; elle rend le niveau de confiance lisible. |
| **Direction** | La position de design qui relie le produit, le contenu, la forme, la matière, la structure, l’action et les états. |
| **Direction artistique (DA)** | Le point de vue visuel situé qui rend une promesse, un contenu et un contexte reconnaissables ; ce n’est pas une simple ambiance ou référence. |
| **Craft** | La qualité de construction perceptible : hiérarchie, composition, typographie, matière, contenu, états et comportement. |
| **Polish** | La résolution cohérente des détails et comportements du rendu réel ; ce n’est pas une accumulation d’effets décoratifs. |
| **Créativité située** | Un écart, une relation ou une reformulation qui apporte une réponse spécifique et utile ; ce n’est pas la nouveauté pour elle-même. |
| **Goût situé** | La sélection, la proportion et la retenue adaptées au contexte ; ce n’est pas une préférence universelle. |
| **Spécificité** | Ce qui relie le rendu au produit et au contexte au point qu’un template générique ne pourrait pas le remplacer sans perte. |
| **Premier objet** | L’élément qui rend la direction visible et utile dans la première proposition : objet, scène, composant, interaction ou relation de contenu. |
| **Boucle d’amélioration** | Après la première proposition, observer le réel, isoler le défaut dominant, modifier l’artefact, observer à nouveau et décider ; une critique textuelle seule ne constitue pas une correction. |
| **Gate** | Un contrôle ciblé, avec une preuve ou une condition adaptée. `A/B/C` désignent des familles de contrôles ; ils ne constituent pas une note globale. |
| **Axes V/U/A/T** | Les questions de preuve : caractère visuel ; compréhension et usage observables dans la tâche déclarée ; accessibilité ou conformité ; robustesse technique. |
| **État (`STATE`)** | L’étape du cycle de vie du run, de `INTAKE` à `CLOSED`. Il ne signifie pas que le résultat est accepté. À ne pas confondre avec la route `SAVOIR/STATE`, qui traite du craft et des états, ni avec le statut de direction. |
| **Issue (`ISSUE`)** | L’issue ou la condition de traitement qui affecte le run, par exemple `BLOCKED`, `RETURNED` ou `EXPLORATORY`. |
| **Verdict (`VERDICT`)** | La conclusion globale sur le périmètre observé : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Les résultats d’axes peuvent utiliser `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `NOT-VERIFIED` ou `N/A-JUSTIFIED`, mais ils ne sont pas des verdicts globaux. |
| **Statut de direction** | La fidélité de la direction dans le rendu : `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE`, `PARTIALLY-HELD` ou `LOST-IN-BUILD`. Il ne remplace pas le verdict global. |
| **`DECISION-INTENT`** | La décision que la procédure doit permettre de trancher au lancement du run. |
| **`DECISION-CHANGE`** | La décision effectivement changée, confirmée ou abandonnée grâce à une observation. Si aucune conséquence n’est obtenue ou attendue, la trace peut utiliser `N/A-JUSTIFIED` lorsque cela est justifié. |
| **`TRACE-LOCATOR`** | Le repère qui permet de retrouver la trace persistante du run : ticket, manifeste, fichier, espace de travail ou autre emplacement déclaré. |
| **`CLOSED`** | La trace et les artefacts sont persistés. Cela ne signifie pas automatiquement « réussi » ou « vérifié ». |
| **`NOT-VERIFIED`** | Une propriété importante n’a pas été vérifiée dans le périmètre ou avec les capacités disponibles. |
| **`NOT-OBSERVED`** | Une conséquence attendue, un changement ou un résultat n’a pas été observé dans le périmètre déclaré. |
| **`N/A-JUSTIFIED`** | Une preuve ou un contrôle n’est pas applicable, avec une justification explicite. |
| **`SPECCED`** | État canonique du cycle de run : la direction, la hiérarchie, le contrat ou l’ancre nécessaire sont suffisamment spécifiés pour permettre le passage à `BUILDING`. Ce n’est ni un verdict, ni une preuve de qualité. |
| **`READING_MAP`** | Carte dérivée qui indique le premier chemin, les perspectives conditionnelles, les sorties et les locators ; elle ne crée aucune règle normative. |
| **Locator** | Repère stable permettant de retrouver un fichier, une section, une trace ou un artefact déclaré. |

## Exemples express

Ces exemples illustrent l’usage des termes ; ils ne créent pas de règle supplémentaire.

| Terme | Exemple concret |
|---|---|
| **Décision** | « Garder la structure du formulaire, mais rendre le premier geste compréhensible sur mobile. » |
| **Preuve** | « Comparer le rendu avant/après à 390 px, puis vérifier le focus clavier dans le scope déclaré. » |
| **NOT-VERIFIED** | « Le contraste a été inspecté ; aucun test avec lecteur d’écran n’a été exécuté. » |
| **DECISION-CHANGE** | « Après observation mobile, le CTA secondaire a été réduit et la hiérarchie réorganisée. » |
| **N/A-JUSTIFIED** | « Aucun test de préférence n’est applicable : la décision porte ici uniquement sur la robustesse du composant. » |
| **CLOSED** | « La trace et les artefacts sont persistés ; le run reste `ACCEPTED-WITH-RESERVATION` sur l’accessibilité non vérifiée. » |

## Pour commencer sans vocabulaire préalable

1. Établissez le mode, le risque dominant, la décision à changer, la prochaine preuve et l’owner.
2. Vérifiez ou confirmez le classement avec `DIRECTION/START` et choisissez le propriétaire normatif utile.
3. Produisez ou modifiez l’artefact, puis observez-le dans le scope déclaré.
4. Isolez le défaut dominant, corrigez l’artefact lorsque c’est nécessaire, observez à nouveau et séparez ce qui a été observé de ce qui reste non vérifié.

La direction est la position globale ; la direction artistique en est l’expression visuelle située. Le craft décrit la qualité de fabrication, le polish sa résolution cohérente, et la spécificité le lien non interchangeable avec le produit et le contexte.

Si deux lecteurs raisonnables choisissent des modes très différents, il faut clarifier le périmètre ou le risque au lieu de masquer le désaccord derrière le vocabulaire.

