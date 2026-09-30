# V1.2 refonte — D-25 : l'action principale reste fonctionnelle et marquée ; arrêt de R10

**Date :** 30-09-2026 · **Décision de l'owner :** « On va corriger et s'arrêter. Avec les runs. »
- D-25 est corrigé.
- R10 s'arrête au palier exploratoire : pas de palier à 18 productions, et aucun run de vérification de la correction.

**Patch :** `audit/tools/V12R_Patch_D25.py` (+ `_fichiers/`). **Diff :** `audit/diffs/V12R_D25_action_principale.diff`. **Instantané :** `audit/snapshots/V12R_Instantane_suivi_D25.json`.

## 1. Défaut (`V12R_35` §3.5)

Sur B-DLA, les rendus C3 et C4 n'avaient ni numéro ni bouton WhatsApp : la commande s'arrêtait à « Copier le message ». L'adresse restait en blancs. C'est l'action principale de la page.

`CNT-01` demandait déjà un contenu plausible marqué plutôt que des emplacements vides. Mais il ne disait rien de l'action principale : faute de valeur réelle, l'agent l'a retirée.

## 2. Diff

| Entrée | Lieu | Changement |
|---|---|---|
| D25-C | DIRECTION, `CNT-01` (bloc CONTENU, compilé dans le noyau) | Ajout : « L'action principale (commander, écrire, appeler, venir) reste fonctionnelle avec une valeur d'exemple marquée (numéro, adresse, lien) : une valeur inconnue ne la retire pas. » |
| D25-H | CHANGELOG | Entrée « Action principale conservée (refonte, D-25) » |
| Garde | `scripts/validate_structure.py` | Fidélité « contenu marqué : action principale (D-25) » : le paragraphe « Destination réelle sans contenu » contient « action principale », dans la source comme dans la copie compilée |

## 3. Résultats

- **Garde :** rouge avant (source et copie compilée), verte après.
- **Mutations :** 2/2 rouges (inverse de l'entrée ; retrait dans la copie compilée).
- **Contrôles :** voir §5.
- **B01 :** 218/218.

## 4. Ce qui n'est pas établi

- **Effet non observé (certain).** Sur décision de l'owner, aucun run ne vérifie la correction. Que l'agent garde désormais un bouton WhatsApp avec un numéro d'exemple marqué est **probable** (la règle est dans le noyau lu à chaque run), mais non vérifié.
- **D-26 reste signalé, non corrigé** : les fonctions inventées d'un produit fictif ne sont pas couvertes par le marquage.
- **Convergence entre conditions** (`V12R_35` §3.6) : signalée, non traitée.

## 5. Contrôles finaux

Voir le bloc « Résultats du suivi », ajouté après l'exécution.

## 6. R10 : état à l'arrêt

| Élément | État |
|---|---|
| Palier exploratoire (6 cas) | Fait (`V12R_35`). Orientation en auto-comparaison, juges modèles d'une seule famille |
| Palier à 18 productions | **Non fait, par décision de l'owner** |
| Observation novice | Non faite |
| Efficacité | `NOT-VERIFIED` : la réserve reste entière |
| Défauts issus du palier | D-25 corrigé (effet non observé) ; D-26 et convergence signalés |
