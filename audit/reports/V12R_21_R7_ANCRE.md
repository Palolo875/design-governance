# V1.2 refonte — Unité R7 — Ancre graduée (décision 6 ; D-03 et D-04)

**Date :** 30-09-2026 · **Diagnostic :** `V12R_20_R7_DIAGNOSTIC.md`, corrigé par les ajustements de l'owner avant application. **PATCH-DECISION :** `audit/tools/V12R_Patch_R7.py` (12 entrées ; `validate_structure.py` et `build_core.py` remplacés ; reproductible depuis `623eb2e`). **Diff :** `audit/diffs/V12R_R7_ancre.diff` (10 files changed, 24 insertions(+), 12 deletions(-)).

## 1. Ajustements de l'owner intégrés avant le patch (tous vérifiés)

| Point | Vérification | Traitement |
|---|---|---|
| `FAIL-ASSUMED` n'est pas une voie d'acceptation | `ACTION/OVERRIDE` : diffusion limitée, « le FAIL ne devient jamais un PASS » ; le validateur refuse tout verdict accepté avec `FAIL-ASSUMED` | La règle dit : diffusion limitée par `FAIL-ASSUMED`, **verdict non accepté**. L'ancienne formule « bloque la livraison validée, sauf `FAIL-ASSUMED` » est retirée et gardée |
| « Absence déclarée » : pour explorer seulement | Le validateur refuse toute DIRECTION acceptée avec des ancres vides, quelle que soit la destination | Explorer sans ancre, oui ; accepter exige une ancre. Pour une démonstration ou un modèle, une hypothèse générée peut servir d'ancre à l'acceptation, avec sa limite |
| Déclencheur critique A4 : clarifier, pas durcir | Le texte contenait déjà « ou statut prévu par ACTION » | Clarifié par le moment : en exploration, limite déclarée et `EXPLORATORY` ; avant l'acceptation, retour à l'ancrage ou statut ACTION |
| Garde de fidélité : un renvoi suffit | — | **Pas de garde « produit réel » dans chaque paragraphe.** La règle a un lieu propriétaire (`ANC-01`) ; les autres lieux y renvoient |

## 2. Changements

- **Absolu 2 de DIRECTION** (lieu propriétaire, concept `ANC-01`, compilé dans le noyau §6, que l'agent lit désormais pendant la fabrication) :
  - titre : « Ne fais jamais accepter une direction identitaire calibrée uniquement de mémoire » ;
  - règle : **explorer, accepter, diffuser** ;
  - l'ancre peut venir du projet lui-même ;
  - la table des trois voies est conservée ;
  - le paragraphe final déclare la limite du validateur, qui ne connaît pas la destination : l'exigence « observée ou fournie » pour un produit réel relève de la revue d'acceptation.
- **Renvois alignés :**
  - SAVOIR/SOURCE et le test de sortie de SAVOIR : D-04 fermé, une seule position ;
  - le déclencheur critique et le récapitulatif de protection ;
  - QUICKSTART, READING_MAP, README officiel et **README Local généré par `build_distributions.sh`** : D-03 fermé.

## 3. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant | `ANC-01` absent ; 6 formulations retirées (DIRECTION, 3 façades) ; bloc de noyau absent |
| Mutations | **6/6 rouges** |
| Premier suivi | **Rouge** : 5 cas de harnais et `validate_all`, parce que le README Local généré par le build contenait encore « ancre inspectable », rejetée par la garde dans la distribution. Corrigé par l'entrée R7-F4 ; ce rouge démontre aussi que la garde agit sur la distribution construite |
| Suivi final | **Vert** : 372 cas maintenus, aucune migration ; `validate_all` vert ; doublons 148 ; 24/25 |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |
| Mesures | Chemin 12 682 → **12 795 mots** ; noyau 3 748 → **3 861** |

## 4. Écarts déclarés

1. **Mon diagnostic affirmait qu'aucun outil ne dépendait de ces phrases.** Ma recherche ne portait que sur les scripts de contrôle et les harnais, pas sur le script de build, qui écrit un README Local en dur. Le suivi l'a montré ; l'entrée R7-F4 a été ajoutée au correctif, qui reste reproductible.
2. **« Ancre inspectable » est retiré comme vocabulaire.** C'était la formule infidèle de D-03. Une façade qui veut résumer l'absolu 2 renvoie à la règle ou reprend sa distinction explorer / accepter.
3. **Limite permanente (décision 3, schéma inchangé).** La machine raisonne sur `identity_stake`, pas sur la destination ; l'exigence pour un produit réel reste une affaire de revue.

## 5. Lecture

- **Certain :**
  - une seule règle d'ancre, avec un lieu propriétaire et des renvois alignés ;
  - D-03 et D-04 fermés ;
  - la règle est dans le noyau ;
  - `FAIL-ASSUMED` n'est jamais présenté comme une acceptation.
- **Probable :**
  - l'agent explore sans se bloquer ;
  - il demande ou utilise les éléments du projet avant d'accepter une direction pour un vrai produit.
- **Hypothétique :** l'effet sur les rendus et sur la qualité des acceptations (R10).
- **Limite :** auto-comparaison.
