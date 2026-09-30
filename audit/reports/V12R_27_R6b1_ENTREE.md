# V1.2 refonte — Unité R6b-1 — Une entrée humaine, un guide opérateur, un README Local généré

**Date :** 30-09-2026.
**Diagnostic :** `V12R_25_R6b_DIAGNOSTIC.md`, avec les amendements de la revue du 30-09 :
- le texte de référence est dans `package/README.md` ;
- la racine du dépôt de travail y donne un accès direct ;
- deux phrases de l'entrée sont amendées.

**Décision de l'owner :** « Allons-y ».
**PATCH-DECISION :** `audit/tools/V12R_Patch_R6b1.py` : 9 entrées et 5 fichiers remplacés (README du package, README officiel, `build_distributions.sh`, `validate_structure.py`, `validate_reading_map.py`).
**Diff :** `audit/diffs/V12R_R6b1_entree.diff` (8 fichiers, 136 insertions, 114 suppressions).

## 1. Changements

**Entrée humaine** : section « Commencer », en tête de `package/README.md`, balisée `entree`.
- Quatre questions : que demander, que fournir, que recevoir, comment poursuivre.
- Vouvoiement, sans jargon, sans mode à choisir.
- Règles citées par renvoi : prise de brief (condition canonique incluse), contenu d'exemple marqué, réponse visible, première proposition `EXPLORATORY`, ancre « observée ou fournie » pour un vrai produit, boucle d'édition, accord avant une action irréversible ou coûteuse.
- Phrases amendées selon la revue :
  - « Vos textes, votre marque et vos photos aident à produire une proposition plus spécifique et crédible » ;
  - « pour retenir cette direction pour un vrai produit, l'agent doit s'appuyer sur des éléments réels, observés ou fournis, et effectuer les vérifications nécessaires ».

**README du package**, qui absorbe le README officiel :
- la mission et les contrats y sont repris ;
- une table « Pour les agents et les opérateurs » remplace « Par où commencer », « Démarrage express » et « Profils de lecture » ; l'agent y entre par la skill ;
- une seule **constitution minimale**, exacte, balisée `constitution` : elle corrige **D-24**, l'ancien absolu 2 ;
- « parcours complet » (**R-25b**) ;
- affirmation de cohérence bornée à la liste close (**Q-13**, part README) ;
- la phrase « Toute conclusion doit préciser… », reprise des limites du README officiel.

**README officiel** : réduit à un pointeur. Il garde ce que le validateur exige : titre versionné, marqueur expérimental, phrase sur les seules sources normatives, table des sources, introduction de la `RUN_CARD`, limite des validations.

**README Local** : il n'est plus codé en dur. Le build insère les blocs `entree` et `constitution` du README du package, avec les chemins Local. S'il manque un bloc ou un emplacement, le build échoue.

**QUICKSTART, devenu guide opérateur :**
- titre et « Pour qui » ;
- un seul « Parcours commun » : la section « 90 secondes » est renommée ;
- les lignes « 30 secondes » et « 5 minutes » sont retirées ;
- « 2. La ligne de run » et « 3. Le parcours complet » ;
- la constitution est remplacée par un renvoi.

**READING_MAP** : constitution en renvoi.

**Racine du dépôt de travail** (hors package ; déclaré) : lien « Commencer » bien visible, entrées agent et opérateur, lien vers le plan de reprise corrigé.

**Gardes** (`validate_structure.py`) :
- `ENT-01` : une seule entrée balisée, les quatre questions, aucun mode demandé, pas de tutoiement ;
- `CST-01` : une seule constitution, qui porte sa signature ; aucune copie ailleurs ;
- vocabulaire retiré : les démarrages concurrents, l'ancien absolu 2 (« dessinée uniquement de mémoire ») et l'ancienne signature de résumé (« coordination du réel et du beau »).

**Conditions de façade rectifiées (déclaré)** : la table des modes vit dans le QUICKSTART ; le README n'en porte plus.

| Condition | Contrôle après rectification |
|---|---|
| LCF-04 | Ligne DIRECTION du QUICKSTART, et aucune ligne de mode dans le README |
| LCF-05 | ITER dans l'ordre canonique du QUICKSTART, et aucune ligne ITER dans le README |
| LCF-10 | Renvoi « Classement : voir `DIRECTION/START` » dans le QUICKSTART, et README sans table de mode |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | 6 démarrages et 4 copies de constitution en vocabulaire retiré ; ENT-01 et CST-01 absents ; LCF-04, -05 et -10 rouges |
| Après | structure, carte de lecture, `validate_design_governance` et noyau verts ; `validate_all` vert sur copie (build, Local, reproductibilité) |
| Mutations | **16/16 rouges** : 5 inverses ; 6 mutations de structure (question retirée, mode demandé, tutoiement, seconde entrée, constitution recopiée, D-24) ; 4 mutations LCF ; 1 mutation du build (README Local non généré) |
| Suivi complet | vert : 389 cas, 365 maintenus, **24 migrés (4 en R6b-1)** ; instantané `V12R_Instantane_suivi_R6b1.json` |
| 13.01 | 6/6 et 5/5 |
| 13.02 | 38/38 |
| B01 | 218/218 |
| Mesures | chemin prescrit 12 867 mots (inchangé : les façades humaines ne sont pas sur le chemin d'un run) ; noyau inchangé ; 24/25 ; doublons 148 → 147 |
| Entrées (mots) | README du package + README officiel + QUICKSTART : 5 812 → 5 573 |

## 3. Écarts déclarés

1. **Quatre cas de harnais migrés (M1)** : C5 LCF-04, LCF-05, LCF-10 et M-5, qui visaient la table des modes du README. Chacun a une garde de remplacement (`lcf:LCF-0x`) et une mutation rouge dans le patch. Les harnais ne sont pas modifiés. Coût annoncé par la maquette : 3 causes ; réel : 3 causes et 4 cas.
2. **Libellé d'un lien changé pour le build.**
   - Constat : le contrôle des chemins de l'export Local prend `` [`DIRECTION.md`](…#ancre) `` pour un chemin, parce que le `#` lui permet de s'étendre jusqu'à l'accent grave suivant. C'est un faux positif.
   - Traitement : le lien de la constitution s'écrit `[DIRECTION.md](…)`.
   - **Défaut signalé, non corrigé** : l'expression du contrôle, dans `build_distributions.sh`.
3. **Tutoiement : garde REGISTER sensible à la casse.** Une phrase commençant par « Ne confonds » échappe à la garde REGISTER existante. ENT-01 cherche sans tenir compte de la casse. La garde REGISTER, sur QUICKSTART, garde cette limite : **signalé, non corrigé**.
4. **Incident de méthode.** Un premier `validate_all` a été lancé dans `package/` au lieu d'une copie. Il a échoué pendant le build (écart 2) et a laissé un dossier `.build`, ignoré par git. Le dossier a été retiré ; aucune sauvegarde `.dist.previous` n'a été laissée. Toutes les exécutions suivantes ont eu lieu sur copie.
5. **Contenu déplacé, non perdu** : mission, contrats, audience et limites passent du README officiel au README du package. La table « Si vous avez… » garde ses trois lignes utiles sous « Pour… ». La ligne du README Local qui renvoyait à READING_MAP est remplacée par l'entrée agent (skill) et le guide opérateur ; les cartes relèvent de R6b-2.

## 4. Lecture

- **Certain :**
  - une seule entrée humaine, reprise à l'identique par l'export Local ;
  - aucun démarrage concurrent ;
  - aucun mode demandé au novice ;
  - une seule constitution, exacte ;
  - D-11 et D-24 fermés.
- **Probable** : un novice sait quoi dire et quoi fournir en une minute de lecture. Ce n'est pas établi : l'observation novice est prévue avec R10.
- **Limite** : auto-comparaison.
