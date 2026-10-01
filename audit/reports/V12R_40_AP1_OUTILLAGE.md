# V1.2 — AP1 : format de la skill (C01), fichiers locaux nus en profil strict (C02), restauration des distributions (C03)

**Date :** 01-10-2026.
**Origine :** audit progressif externe, étape 10 (`DG_Audit_progressif_10`, commit fixé `1a4bf2f`). Les constats C01 à C03 ont été vérifiés sur le dépôt avant cette unité.
**Décision de l'owner (01-10-2026) :**
- plan en cinq unités, avec quatre ajustements :
  - C02 : reconnaissance bornée ;
  - C03 : récupération complète ;
  - critères dont les limites restent visibles ;
  - formulations C08 et coût bornées ;
- les R10 restent arrêtés.

**Pièces :**
- patch : `audit/tools/V12R_Patch_AP1.py` (+ `_fichiers/`) ;
- preuves directes : `audit/tools/V12R_Sonde_AP1.py` ;
- diff : `audit/diffs/V12R_AP1_outillage.diff` ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP1.json`.

## 1. Fiche de l'unité

| | |
|---|---|
| **Périmètre** | C01, C02, C03. Aucune règle de fabrication ni prose normative modifiée, hors une entrée de CHANGELOG |
| **Réussite** | Preuves directes rouges avant, vertes après (sonde et mutations) ; suivi vert (résultat complémentaire, voir §4) ; 13.01 par sous-contrôle ; 13.02 ; B01 |
| **Arrêt** | Une fixture existante cassée, expliquée avant toute modification de son attente ; un contrat de harnais qui tombe sans cause évidente. Aucun des deux ne s'est produit |
| **Bornes notées pour les unités suivantes** | C08 : `CHARGE` prescrit déjà `CLOSE-PACKAGE` en trace complète. Le défaut est l'absence d'un déclencheur UI/UX **avant fabrication**, pas une découverte tardive. Coût 1,7-1,8 × C1 : il s'agit des tokens des productions C3 de l'ancien palier R10, et non du coût actuel ni du coût propre de l'atelier |

## 2. Diff

| Constat | Lieu | Changement |
|---|---|---|
| C01 | `SKILL.md`, en-tête | `description` entre guillemets doubles. Texte décodé identique au caractère près (contrôle PyYAML dans la sonde) |
| C01 | `validate_structure.py` | Garde **SKL-01**, en bibliothèque standard. Contrôles : en-tête présent ; une paire « clé: valeur » par ligne ; une valeur non citée sans `: `, ` #` ni indicateur YAML initial ; une valeur citée décodable ; `name` et `description` présents ; `name` = `design-governance-practice` |
| C02 | `validate_run_card.py` | Un **nom de fichier nu** est local s'il porte une extension d'une **liste fermée** (web, document, image, vidéo, police, fichiers de design). Ne sont pas des chemins : ticket, commit, version, domaine sans schéma, identifiant opaque. La base de résolution devient `source_path.resolve().parent`, quel que soit le dossier de lancement |
| C02 | Suite RUN_CARD | Cas unitaires **C02-1** (artefact nu absent) et **C02-2** (trace nue absente). Contrôle **« locators admis en profil strict »** : 10 valeurs qui doivent rester admises (fichier nu présent, `./` présent, URL, ticket, `#128`, commit long et court, version, identifiant opaque, domaine) |
| C03 | `build_distributions.sh` | Promotion transactionnelle de `dist` **et** des deux archives : sauvegarde des archives (`.archives.previous`), puis de `dist`, puis promotion. Un échec à n'importe quelle étape restaure l'ensemble antérieur et retire les nouveautés sans antérieur. Si la restauration est incomplète, les sauvegardes sont conservées et le message le dit. Une sauvegarde d'archives trouvée au démarrage bloque le build (résolution manuelle, aucune suppression) |
| — | CHANGELOG | Entrée « Outillage (audit progressif, unité 1) » |

ACTION est inchangé. Il disait déjà « l'existence des locators locaux, résolus depuis le dossier de la carte » ; le code s'y conforme désormais.

## 3. Preuves directes (sonde, sur copie)

| Sonde | Avant (`1a4bf2f`) | Après |
|---|---|---|
| **C01** | PyYAML refuse (« mapping values are not allowed here ») | PyYAML lit l'en-tête ; description décodée = référence ; `name` inchangé. Vérifié aussi **dans les deux archives construites** |
| **C02** (lancé depuis trois dossiers : celui de la carte, le parent, un dossier tiers) | Artefact nu absent et trace nue absente **acceptés** (6 KO). Les admissions restent vertes | 34/34 (33 lancements et la suite) : absents refusés, présents admis, les six formes non locales admises dans les trois dossiers ; suite 84/84 cas unitaires, 10/10 locators admis |
| **C03** (faux `mv` en tête du PATH, panne sur chaque archive, chaque fois depuis une copie saine) | Panne Local : ZIP GitHub neuf, `dist` neuf, `.dist.previous` laissé, **relance refusée** (code 1). C'est le scénario de l'audit, reproduit | 22/22 : `dist` et les deux ZIP restaurés à l'identique (empreintes), aucune sauvegarde résiduelle ; relance normale réussie, archives neuves publiées |

**Total après : sonde verte, 60/60.**
**Mutations 5/5 rouges :**
- inverse de la citation → `[SKL-01]` ;
- deux-points non cité dans `name` → `[SKL-01]` ;
- `name` retiré → `[SKL-01]` ;
- « nom nu jamais local » (comportement antérieur) → `cas unitaire C02-1` ;
- « tout nom à point est local » (sur-reconnaissance) → `locator strict admis refusé (version…)`.

## 4. Contrôles finaux, sur le package appliqué, avec leurs limites

- **Suivi : VERT.** 389 cas, 363 maintenus, 26 obsolètes, aucune migration ; `validate_all` vert ; cliquets inchangés (13 614 mots, doublons 142).
  - **Limite :** C14 reste ouvert. Le suivi accepte qu'un cas obsolète disparaisse, et il juge verte une garde dont l'identifiant n'apparaît pas dans la sortie. Ce vert est donc complémentaire ; la preuve de l'unité est la sonde et les mutations.
- **13.01, par sous-contrôle :**
  - texte 6/6 ;
  - mutations 6/6 ;
  - non-régression 5/5 ;
  - distributions 9/9.
  - **Limite de « distributions » :** Python 3.10 et 3.13 étaient disponibles dans cet environnement, en plus de 3.11 par défaut. La matrice D-1 à D-3 a donc tourné, **sous Linux seulement**, sur des archives construites depuis une copie et non sur `releases/`. Aucun autre système, aucune CI hébergée.
- **13.02 :** 38/38.
- **B01 :** 218/218.
- **Non observé :** l'import de la skill par un hôte réel. C01 corrige un YAML démontré invalide ; le rejet par un hôte strict était attendu, il n'a pas été observé.

## 5. Écarts et limites déclarés

- **SKL-01 contrôle un sous-ensemble de YAML.** La garde est plus stricte que YAML : elle refuserait par exemple un scalaire de bloc valide. PyYAML ne sert qu'à la sonde, car le package reste sans dépendance tierce.
- **La liste d'extensions de C02 est fermée.** Un fichier local d'extension absente de la liste (par exemple `.heic`) reste traité comme un identifiant opaque, donc sans contrôle d'existence, sauf s'il est écrit `./fichier.heic`. Les nouveaux refus (noms nus absents) sont le comportement recherché. Aucune fixture ni aucun cas existant n'a changé d'attente.
- **C03 ne couvre pas une interruption brutale en pleine promotion** (arrêt du processus). La sauvegarde d'archives reste alors en place et le build suivant s'arrête pour une résolution manuelle : c'est le choix prudent, sans suppression. L'échec de la restauration elle-même n'a pas été provoqué.
- **Observation, non corrigée :** avec `SOURCE_DATE_EPOCH` antérieur à 1980 (0 par défaut), le format ZIP ramène les dates à 1980. Deux builds à des dates différentes antérieures à 1980 donnent donc des archives identiques. C'est sans effet sur la reproductibilité ; la sonde utilise des dates postérieures à 1980.
- **Mesures :** chemin prescrit et noyau inchangés (la citation n'ajoute aucun mot).

## 6. Suite (plan validé)

- **AP2 :**
  - errata C34 à C36 et réserve D-26 ;
  - C14 et C22, par rectification déclarée des outils de suivi et de mesure.
- **AP3 :** C08, C05, C06, C07, C09 et C10.
- **AP4 :** autres validateurs (C11 à C13, C19 à C21), puis façades dérivées.
- **AP5 :** consolidation documentaire.

Constats différés avec leur disposition : C15, C32, C37 et C38, ainsi que les précisions C27 à C29 et C31.
