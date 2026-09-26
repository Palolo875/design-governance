# DG-AUDIT-001 — Retour R.02 — Application sur B04 = V1.1.1

**Date :** 26 septembre 2026.
**Statut d'audit :** `AUDIT-RETURN`. Sa réévaluation revient à l'owner (§5).
**Candidate :** B04 = V1.1.1, dans un dépôt externe séparé.
**Références :** B01 est intacte (218/218). B02 reste gelée. B03 est inchangée (arbre propre).
**Format :** rapport allégé.

**Fichiers produits :**
- `DG_AUDIT_001_B04_R02_V1.1.0_V1.1.1.diff` : le diff complet, validateur de carte compris ;
- `DG_AUDIT_001_Instantane_harnais_B04_R02.json` : l'instantané des 22 harnais ;
- `DG_AUDIT_001_Journaux_R02.zip`, qui contient :
  - les sorties brutes de tous les contrôles ;
  - la revue bornée `Q_revue.md` ;
  - l'imitation : traces, cartes et sortie du validateur.

## 1. Application

| Étiquette | Commit | Contenu |
|---|---|---|
| `R.02-B04-ouverture` | 5a6e0e8 | Copie de B03 à `12.06-outils-v1.1.0` (60 fichiers) |
| `R.02-patch` | 7f34d8c | `DG_AUDIT_001_Patch_R01.py` : 36 entrées ; d'abord `--verifier`, puis application, sans écart |
| `R.02-version-v1.1.1` | 4d5d756 | Passage en V1.1.1 : manifeste, titres, README, QUICKSTART, README Local du build ; section CHANGELOG « V1.1.1 — Retour d'audit » ; notes de version (35 conditions, puce « Retour d'audit ») |

Les textes appliqués sont exactement ceux de R.01, sans correction ajoutée.

## 2. Contrôles, tous rejoués sur copies

| Contrôle | Résultat |
|---|---|
| 22 harnais, suivi comparé à l'instantané 12.06 | **300/300, témoins 40/40**, aucune alerte, empreintes inchangées |
| Harnais R | **31/31** (sur V1.1.0 : 3/31, soit le témoin et les deux conservations) |
| Vérifications X (A1) et Y (A2) | Toutes rouges pour leur motif, comme attendu |
| 13.01 texte et mutations | 6/6 et 6/6 |
| 13.01 distributions (Python 3.10 et 3.13) | **9/9** : les deux zips V1.1.1, extraits seuls, passent `validate_all` ; membres = manifeste (60 et 56) |
| 13.01 non-régression B01 → B04 | 5/5 : même verdict sur les fixtures communes ; exemple V1.0.0 refusé sans traceback |
| 13.02, épreuves déterministes | **38/38** |
| `validate_all` sur B04 | FULL VALIDATION PASSED (build GitHub et Local, reproductibilité) |

**Certain :** aucune régression de forme, et tous les points du retour sont verts.

## 3. Revue bornée du diff V1.1.0 → V1.1.1

**Méthode.** Un sous-agent a revu les 33 hunks de texte contre le package complet, le schéma et le validateur. La relation est déclarée : **même auteur** que les corrections, conflit déclaré (critères D3). La revue ne vaut donc pas regard indépendant.

**Résultat : 0 bloquant, 3 significatifs, 10 mineurs.** J'ai vérifié les trois significatifs sur B04 ; ils sont confirmés :

| # | Constat | Vérification | Origine |
|---|---|---|---|
| **Q-01** | Le nouveau texte sur les droits inconnus (ACTION l. 667) dit que la machine exclut `ACCEPTED`. Le validateur ne le fait qu'en mode `DIRECTION` (`validate_run_card.py` l. 319) | **Certain**, lu dans le code | Imprécision introduite par P-17 (R.01) |
| **Q-02** | Le paquet `SYSTÈME` de CLOSE-PACKAGE n'a pas reçu la conséquence décisionnelle. Or le CHANGELOG annonce que « les paquets de clôture » sont alignés, et la machine exige `decision_change` pour une carte SYSTÈME close (l. 322) | **Certain** | Oubli dans P-28 (R.01) |
| **Q-03** | Le défaut de RET-1 subsiste dans SAVOIR. La l. 879 exige une justification `N/A-JUSTIFIED` quand aucune décision ne change ; la l. 30 dit « retournez `N/A-JUSTIFIED` ». `NOT-OBSERVED` n'y a pas de place, et LCF-22 ne voit pas ces lignes (pas d'énumération) | **Certain** | Copies non repérées en R.01 |

**Mineurs (non vérifiés un par un, transmis) :**
- Q-04 : ITER et STANDARD sont dits « forme seule », alors que `decision_change` est contrôlé.
- Q-05 : dans l'exemple du QUICKSTART §9, `CHANGE` garde l'ancien sens.
- Q-06 : la table de charge du QUICKSTART §5 n'a pas été alignée sur RET-4.
- Q-07 : `SCOPE` a deux projections, et la source de la contrainte est discutable.
- Q-08 : la sortie n'est pas « définie une seule fois » au sens littéral (ancrages DIRECTION, `system_package`, table PRECONDITION).
- Q-09 : la portée de B1b entre en tension avec l'arrêt one-shot.
- Q-10 : le GLOSSAIRE parle d'une réserve « complète » à six attributs ; la machine en exige sept.
- Q-11 : les droits inconnus font face à ACTION l. 500.
- Q-12 : le tag « partagé » l'est avec une forme différente.
- Q-13 : d'autres phrases de cohérence restent non bornées.

**Lecture.** La condition de sortie de R.02, « aucune contradiction bloquante », est **remplie**. Mais Q-01 et Q-02 sont des inexactitudes que **le retour lui-même a introduites**, et Q-03 montre que RET-1 n'est corrigé que dans les deux textes nommés.
- **Certain :** aucun des trois n'est bloquant au sens de la revue.
- **Probable :** les trois se corrigent au même coût que R.01, par une ligne de texte chacun et une extension de condition.

## 4. Imitation rejouée (auto-comparaison, sans valeur de sortie)

**Protocole.** Même agent et mêmes briefs qu'en 13.02. L'agent disposait cette fois des exemples **et** des fichiers qu'ils désignent : `run_card.example.json`, `machine_projection.md` et la section `ACTION/RUN_CARD`. Le validateur ne lui était pas donné, pour mesurer ce que les textes enseignent seuls.

| | 13.02 (exemples seuls) | R.02 (exemples et renvois) |
|---|---|---|
| Cartes acceptées par le validateur | 0/2 | **0/2** |
| Nature de l'échec | Sérialisation : `risk` en chaîne, `creative_close` à `null`, clés devinées | LITE : une seule valeur, `closure.direction_status: null`. DIRECTION : un invariant métier, « DIRECTION sans ancrage : verdict accepté interdit » |

**Lecture.**
- **Probable :** le renvoi a fait passer l'échec de la **forme** (noms et types de clés) à une **valeur** et à une **règle**. L'agent a appris la structure.
- **Certain :** l'effet sur l'échec final est nul (0/2).
- **Observation nouvelle (O-1), hors diff, antérieure à V1.1.1.** ACTION l. 385 dit que « `null` signifie qu'aucune valeur n'est déclarée dans cette projection ». Pourtant le schéma refuse `null` pour `direction_status`, qui doit être omis. C'est un petit écart entre le texte et la machine ; l'imitation le rend visible.
- Le refus de la carte DIRECTION est un **refus correct** : sans ancre, l'acceptation est interdite. C'est le brief qui ne fournissait pas d'ancre.

## 5. Décision de l'owner

La condition de sortie formelle du retour est remplie :
- RET-1 à RET-6 sont verts, chacun avec une preuve rouge sur V1.1.0 ;
- aucune régression ;
- aucune contradiction bloquante.

Deux suites sont possibles :

| Option | Contenu | Coût | Effet sur le statut |
|---|---|---|---|
| **A. Mini-boucle R.03 (recommandée)** | Corriger Q-01, Q-02 et Q-03 (et, à faible coût, Q-05, Q-06, Q-10 et O-1 côté texte). Étendre LCF-22 à SAVOIR. Mêmes contrôles, revue du nouveau diff | Une unité courte, du même type que R.01+R.02 réunies | V1.1.1 sort sans inexactitude connue introduite par le retour ; `AUDIT-PASS-WITH-RESERVATION` plus solide |
| **B. Réévaluer maintenant** | Statut sur B04 tel quel, avec Q-01 à Q-03 ajoutés aux réserves | Aucun | `AUDIT-PASS-WITH-RESERVATION` probable, avec trois réserves de texte en plus, dont deux créées par le retour |

**Mon avis.** Je recommande A : publier une version dont deux phrases neuves sont fausses serait incohérent avec l'objet même du retour. Les zips V1.1.1 et le md compilé ne sont **pas encore livrés comme version finale**, pour éviter une livraison à refaire. Ils existent dans B04 et passent tous les contrôles.

## 6. Écarts de méthode déclarés

1. **Revue par sous-agent, même auteur.** La relation est déclarée ; ce n'est pas un regard indépendant (réserve 1 inchangée).
2. **Imitation sans validateur.** C'est un choix de mesure, pour rester comparable à 13.02. L'encadré des exemples invite pourtant à valider : un agent qui le ferait corrigerait probablement le cas LITE.
3. **Section ACTION fournie en extrait**, pas le fichier ACTION entier. C'est ce que l'encadré désigne (la table de correspondance d'`ACTION/RUN_CARD`).
4. **Premier lancement de la revue interrompu** par la limite de session, puis relancé à l'identique. Aucun résultat partiel n'a été utilisé.

**Prochaine unité :** selon la décision de l'owner, R.03 (option A) ou la réévaluation du statut (option B).
