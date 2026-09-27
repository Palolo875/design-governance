# V1.2 refonte — Unité R4 — Proposition : noyau de fabrication

**Date :** 2026-09-27 · **Statut :** **proposition**, soumise à l'owner ; rien n'est appliqué.
**Décisions déjà prises :**
- 1 : noyau compilé depuis les sources ;
- 4 : sortie en langage produit ;
- 7 : marqueurs de vague dans le noyau.

**Enjeu :** c'est le lot qui doit changer le rendu. Il sera suivi du point de contrôle P1 (mini-épreuve).

## 1. Principe : sélectionner, pas réécrire

Le noyau n'est **pas un texte nouveau**. C'est une **sélection de paragraphes canoniques existants**, balisés dans leur fichier propriétaire (`<!-- noyau:début ID -->` … `<!-- noyau:fin ID -->`), qu'un script (`scripts/build_core.py`) assemble dans la skill.
- **Aucune copie manuelle :** `validate_all` échoue si la skill diffère de sa compilation.
- **Aucun doublon :** le paragraphe balisé **est** la règle ; le reste de la section devient la référence détaillée.

## 2. Contenu du noyau (≈ 2 400 mots mesurés)

| § | Bloc | Lieu propriétaire | Mots |
|---|---|---|---|
| 1 | Posture de designer senior | DIRECTION, Posture | 144 |
| 2 | Classer en une ligne (nouvelle ligne canonique) | DIRECTION/START | ≈ 60 |
| 3 | Prise de brief | DIRECTION/EXTERNAL-START | 97 |
| 4 | Structure : où elle vit, comment le regard circule, quelle preuve, comment on agit ; axes de tension ; **six signaux de convergence** (`MODAL` structurel) | BIBLIOTHEQUE | 279 |
| 5 | Composition : **grammaire positive** ; test de singularité ; **vocabulaire perceptuel avec « diff possible »** ; question de convergence ; **marqueurs de vague datés** | SAVOIR | 570 |
| 6 | Moyens et vérité : `FABRICATION` et plafond ; carte des moyens ; assets moyens ; faux asset ; vérité de scène (la règle en un paragraphe) | DIRECTION, SAVOIR | ≈ 440 |
| 7 | Boucle d'édition : **table de diagnostic** ; atelier retrait / réduction / transformation ; six questions de revue ; repasse ; un axe à la fois | DIRECTION/DOUBLE-LOOP, ACTION/GATE-B, SAVOIR | ≈ 440 |
| 8 | Sortie en langage produit : ce que j'ai fait, pourquoi, ce qui manque pour la vraie version, la suite ; trace sur demande | ACTION/HANDOFF (texte nouveau, décision 4) | ≈ 100 |
| 9 | Liste de chargement par mode (générée) | DIRECTION (liste canonique unique) | ≈ 80 |

**Trois déplacements** (façade → source normative, pour qu'un bloc du noyau soit normatif) :
- la table de diagnostic et les six questions de revue quittent QUICKSTART pour `DIRECTION/DOUBLE-LOOP` ;
- « un axe à la fois » quitte ORCHESTRATION_MAP pour `SAVOIR/CRAFT/CFT-02` (alternative située).

Les façades y renvoient.

**Une condensation :** la vérité de scène. La règle tient en un paragraphe balisé ; la table `TRUTH/*` reste dessous comme référence.

## 3. Une liste de chargement unique

- Nouvelle section canonique **`DIRECTION/CHARGE`** : une table par mode, seule source.
- La skill en porte une **copie générée**. QUICKSTART, READING_MAP et ORCHESTRATION_MAP **y renvoient** au lieu de redéfinir.
- Garde de propriété : toute liste « première lecture » est absente ou égale à la canonique.

**Proposition pour le mode `DIRECTION`** (première lecture de l'agent, après le noyau déjà lu dans la skill) :
- `DIRECTION/START` ;
- `DIRECTION/CREATIVE-BOOT` ;
- `DIRECTION/EXTERNAL-START` (brief vague) ;
- `DIRECTION/VISUAL_TARGET` ;
- `DIRECTION/FIRST-OBJECT` ;
- `ACTION/FIRST-RENDER` ;
- `ACTION/RUN-DIRECTION` ;
- gates A, B et C applicables.

Ne sont plus lus par défaut par l'agent :
- README, QUICKSTART et ORCHESTRATION_MAP (lecture humaine) ;
- `DOUBLE-LOOP` (sa boucle d'édition est dans le noyau) ;
- `ACTION/ROUTING` et CFT-00 (restent chargeables si la décision l'exige).

## 4. Ce que devient la skill

Frontmatter orienté résultat (« produire un travail de niveau designer senior, vrai et situé, avec une trace proportionnée ») ; trois lignes d'autorité ; **noyau compilé** ; liste de chargement générée ; références conditionnelles.

**Retirés de la skill** (doublons ou remplacés par le noyau) :
- activation en 30 secondes ;
- constitution recopiée ;
- « préparer le contexte » ;
- trois consignes de chargement ;
- Classer / Diriger / Construire / Vérifier / Corriger abstraits ;
- anti-slop en liste négative ;
- copie du handoff.

**Ajout :** `examples.md` reçoit un exemple de **fabrication** (brief flou → décisions → rendu décrit → ce qui manque).

## 5. Effets attendus (à mesurer)

| Mesure | B05 + R3 | Attendu après R4 |
|---|---|---|
| Outils de fabrication dans le texte chargé (TABLE) | 7/25 | **≥ 20/25** |
| Chemin prescrit (LETTRE) | 23 849 | **≈ 16 000 à 17 000** (−30 %) |
| Listes de chargement distinctes | 5 | **1** |
| Skill | 3 191 mots | ≈ 2 800 |

## 6. Coût déclaré

- Environ **10 conditions LCF** et **20 à 30 cas de harnais** lisent la skill actuelle. Il s'agit notamment de LCF-07, 22, 24, 25, 43 à 47 et de la copie du handoff.
- Ils seront migrés au fil de l'eau (M1) vers des gardes de propriété : compilation, liste unique, vocabulaire, fidélité.
- Chaque migration sera justifiée dans la table.
- LCF-46 ne demande probablement **aucune** rectification : les lignes `[VEILLE 20…]` recopiées dans la skill sont déjà admises.

## 7. Critères

- **Réussite :**
  - noyau ≤ 2 500 mots ;
  - ≥ 20/25 outils dans le texte chargé ;
  - 1 liste de chargement ;
  - chemin prescrit en baisse d'au moins 25 % ;
  - suivi vert (migrations justifiées) ;
  - B01 218/218.
- **Arrêt :**
  - noyau > 3 000 mots ;
  - chemin prescrit qui ne baisse pas ;
  - plus de cas de harnais à migrer que de blocs déplacés ou balisés.

Dans ces cas, retour à l'owner.
