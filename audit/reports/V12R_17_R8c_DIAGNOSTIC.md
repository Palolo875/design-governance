# V1.2 refonte — R8c — Diagnostic des gestes (avant correction)

**Date :** 30-09-2026 · **Méthode :** examen des propriétaires existants (`SAVOIR/CRAFT` CFT-03 et CFT-05, `SAVOIR/TYPE`, `SAVOIR/STATE`, `ACTION/GATE-C`, `ACTION/UI-UX-REALITY`, `DIRECTION/DOUBLE-LOOP`, noyau compilé) pour les six candidats du plan de reprise §4. Un manque est « établi » s'il n'existe ni geste ni renvoi opérable (déclencheur, correction, observation). Auto-lecture, déclarée comme telle.

| Candidat | Existant | Manque | Proposition |
|---|---|---|---|
| **Équilibre d'un titre** | TYPE : longueur de ligne, interligne, taille optique, preuve de rendu (couple taille/interligne/mesure) ; question de convergence : deux voix sur le vrai titre | **Établi.** Rien sur la coupe des lignes d'un titre (sens, mot isolé, équilibre), l'approche aux grands corps, ni l'écart d'échelle titre/texte | Geste « Équilibre d'un titre » dans `SAVOIR/TYPE`, compilé dans le noyau §5 |
| **Contraste d'échelle** | Gate C C2 « une échelle contrastée » ; vocabulaire perceptuel « Masse visuelle » ; CFT-03 « choisis grille, échelle… » | **Partiel** : application au titre absente | Intégré au geste du titre (écart net titre/texte) ; pas de geste séparé |
| **Relation texte/image** | Axe « rapport texte/image » (divergence), levier d'émotion ; Gate A contraste « cas représentatifs » | **Établi.** Aucun geste pour un texte posé sur une image : zone calme, recadrage, voile, contraste au point le plus défavorable, variation selon le crop | Geste « Texte sur image » dans CFT-03, compilé dans le noyau §5 |
| **Poids optique des icônes** | Carte des moyens (R8b) : « poids, taille et sens accordés au texte » ; noyau : « compensation optique » | **Non établi** : couvert | Aucun ajout |
| **Relecture de l'ensemble après une correction locale** | Boucle : « corriger l'artefact puis réobserver » ; question 5 : « la correction a-t-elle affaibli l'usage, l'accessibilité, la robustesse ou la direction » | **Partiel.** La hiérarchie et l'harmonie de l'ensemble ne sont pas nommées, ni la portée de la réobservation | Question 5 du noyau précisée (`DIRECTION`, bloc `BOUCLE-QUESTIONS`) |
| **Récupération après erreur** | STATE : « erreur associée et récupération compréhensible » ; UI-UX-REALITY : états critiques, « une capture de l'état nominal ne suffit pas » ; vocabulaire « États » | **Établi** pour le geste : ni contenu du message, ni conservation de la saisie, ni focus, ni reprise ; l'observation par interaction n'est pas décrite | Geste « Récupération après erreur » dans `SAVOIR/STATE` (hors noyau), appelé depuis Gate C C6 |

**Contrôles prévus :**
- concepts balisés pour les trois nouveaux gestes (titre, texte sur image, récupération) ;
- renvoi garanti de `ACTION/GATE-C` vers la récupération ;
- fidélité de la question 5 (« l'ensemble ») ;
- mutations rouges ;
- aucune obligation universelle (UNI-01) ;
- chaque geste : déclencheur, corrections possibles, observation.
