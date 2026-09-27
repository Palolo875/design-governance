# CLAUDE.md — Design Governance (dépôt de travail)

Ce fichier est lu automatiquement par Claude Code. Il donne le contexte, les règles de méthode, l'état actuel et la prochaine étape. Lis-le en entier avant toute action.

## 0. Première session : initialisation (à faire une seule fois)

Le dépôt peut arriver sous forme de deux fichiers : ce `CLAUDE.md` et une archive `DG_kit_ClaudeCode.zip`. Si l'arborescence décrite au §3 n'existe pas encore :

1. Décompresser l'archive **à la racine du dépôt** : son contenu doit se retrouver directement sous la racine (`package/`, `audit/`, …), sans dossier intermédiaire. Le `CLAUDE.md` inclus est identique à celui-ci.
2. Vérifier l'intégrité du kit : `sha256sum -c KIT_SHA256SUMS.txt` (tous `OK`).
3. Vérifier la référence B01 : `cd reference/B01_transfert && sha256sum -c SHA256SUMS.txt` → **218/218**.
4. Vérifier le système : `cd package && python3 -B scripts/validate_all.py` → `FULL VALIDATION PASSED`.
5. Supprimer l'archive du dépôt, commiter (« Import du kit Design Governance V1.1.1 »), étiqueter `v1.1.1-import`, pousser.
6. Rendre compte à l'owner en quelques lignes : résultats des étapes 2 à 4, et rien d'autre.

Ne rien modifier dans `package/` pendant l'initialisation.

## 1. Le projet

**Design Governance** est un système de gouvernance de design pour agents IA. Il fait produire à un agent un travail de design dirigé, prouvé et tracé, au lieu d'un rendu générique. Il est écrit en français.
- Cinq sources normatives : `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md`, `CHANGELOG.md` (dans `package/V1/official/`).
- Des façades dérivées : QUICKSTART, README, GLOSSAIRE, READING_MAP, ORCHESTRATION_MAP, la skill `skills/design-governance-practice/`.
- Une projection machine : `schemas/run_card.schema.json`, validée par `scripts/validate_run_card.py`, et des validateurs de package et de façades.

**Owner :** Junior (Kamel), designer et développeur, basé à Douala. Il décide de chaque arbitrage.

## 2. État actuel (26-09-2026)

- **Version courante : V1.1.1**, dans `package/`. Non publiée.
- **Audit DG-AUDIT-001 : clos**, statut final décidé par l'owner : **`AUDIT-PASS-WITH-RESERVATION`**. Dossier : `audit/reports/Audit_Cloture_Finale_DG-AUDIT-001.md`.
- **Contrôles de V1.1.1 :** 22 harnais 300/300, témoins 40/40 ; harnais R 31/31 ; harnais R03 18/18 ; vérifications 13.01 26/26 ; épreuves déterministes 13.02 38/38.
- **Réserves ouvertes** (détail dans le dossier de clôture, §3) :
  - efficacité sur des runs réels `NOT-VERIFIED` ;
  - run CI hébergé non observé ;
  - environ 14 invariants sans cas négatif ;
  - 16 limites déclarées ;
  - promesse du validateur ;
  - coût de lecture (environ 1 300 lignes pour un run `DIRECTION`) ;
  - placeholders dans les champs libres ;
  - mineurs transmis ;
  - publication.
- **Épreuve de référence B-DLA (unité V1.2-00) : close sans juge humain**, orientation déclarée : `audit/reports/V12_00_EPREUVE_REFERENCE_B-DLA.md`.
- **Porte G1 franchie** (26-09-2026) : `audit/reports/V12_01_DECISIONS_G1.md`.
- **PATCH-DECISION A, B, D appliquée sur B05 (G3)** : `audit/reports/V12_03_G3_APPLICATION_B05.md`. Sur la branche `v1.2/patch-decision-abd` (et la branche de session), `package/` est la **candidate V1.2** (version affichée V1.1.1, CHANGELOG « Non publié ») ; `main` reste V1.1.1. Contrôles B05 : 300/300, témoins 40/40, R 30/30, R03 18/18, 13.02 38/38, 46 conditions de façade. Instantané de référence : `audit/snapshots/V12_Instantane_harnais_B05_G3.json`.
- **Lot 2 (G, H, I, D') appliqué sur B05** : `audit/reports/V12_04_LOT2_G_H_I_D.md` ; 50 conditions de façade ; instantané `V12_Instantane_harnais_B05_Lot2.json` ; budget 9 591 mots.
- **Lectures structurelles (auto-comparaison), complètes** : DIRECTION, ACTION, skill + READING_MAP, façades, SAVOIR, BIBLIOTHEQUE + CHANGELOG : `audit/reports/V12_05` à `V12_10` ; **synthèse, registre des défauts D-01 à D-18 et proposition de chantier « structure et budget » (phases 0 à 4) : `V12_11_SYNTHESE_LECTURES.md`**. Diagnostic : accrétion par audit, architecture pensée à partir de la preuve, gardes sur des phrases ; levier probable : skill-noyau de fabrication, liste de chargement unique, gardes de propriété. Défauts signalés non corrigés : vocabulaire anti-direction / `MODAL`-`PARTI`, prise de brief compressée (condition « destination si elle n'est pas évidente » perdue), dérive de l'absolu 2 dans la skill, glossaire non mis à jour, six listes de chargement `DIRECTION` divergentes. Chemin prescrit réel d'un run `DIRECTION` : ≈ 23 600 mots (≈ 1 650 lignes) ; 7 outils de fabrication sur 25 sont sur ce chemin.
- **Chantier en cours : plan V1.2**, `plans/Plan_V1.2_Qualite_senior_gouvernance.md`. Objectif : un premier rendu de niveau designer senior dès le one-shot, gouvernance conservée (bilan de fabrication, prise de brief minimale, matériaux, anti-slop vivant, atlas d'ancres, épreuve à l'aveugle).

## 3. Arborescence

| Chemin | Contenu | Statut |
|---|---|---|
| `package/` | Système V1.1.1 (sources, schémas, scripts, skill) | Version courante ; ne se modifie que par PATCH-DECISION |
| `reference/B01_transfert/` | Baseline B01 = V1.0.0, avec `SHA256SUMS.txt` (218 fichiers) | **Lecture seule, toujours** |
| `reference/B02/` | Candidate V1.0.1 gelée, jamais utilisée | Gelée |
| `history/` | Bundles git : `B03_V1.1.0.bundle`, `B04_V1.1.1.bundle` (toutes les étiquettes : `12.00`… `12.06-outils-v1.1.0`, `R.02-*`, `R.03-patch`, `R.03b-seconde-passe`) | Archive ; `git clone history/B04_V1.1.1.bundle /tmp/b04` pour consulter |
| `audit/tools/` | 22 harnais `*_harnais_non_regression.py`, harnais R et R03, suivi, patchs R.01 et R.03, vérifications 13.01, épreuves 13.02 | Outils ; ne changent que par rectification déclarée |
| `audit/snapshots/` | Instantanés des harnais (B01, B03 12-00 à 12-06, B04 R.02 et R.03) | Référence de comparaison |
| `audit/reports/` | Tous les rapports d'audit, le plan maître, le dossier de clôture | Historique |
| `audit/data/`, `audit/diffs/`, `audit/logs/`, `audit/sources/` | Registres CSV, diffs, journaux et captures, protocole maître d'audit v2.0 | Historique |
| `releases/` | Zips GitHub/Local et fichier compilé de V1.1.0 et V1.1.1 | Livrables figés |
| `plans/` | Plan V1.2 | Travail en cours |

## 4. Règles de méthode (non négociables)

1. **B01 en lecture seule.** Vérifier `SHA256SUMS.txt` (218/218) à chaque unité de travail. Ne jamais écrire dans `reference/`.
2. **Toute modification de `package/` passe par une PATCH-DECISION** :
   - une décision écrite, validée par l'owner ;
   - les textes exacts sous forme exécutable (modèle : `audit/tools/DG_AUDIT_001_Patch_R01.py`) ;
   - des gardes **rouges avant, vertes après** : conditions de façade LCF dans `scripts/validate_reading_map.py` avec mutation rouge, ou cas unitaires.
3. **Aucune correction non décidée n'entre dans un patch.** Un défaut découvert en cours de route est signalé, pas corrigé en silence.
4. **Aucun changement de méthode silencieux.** Tout écart est déclaré dans le rapport de l'unité.
5. **Les harnais ne changent que par rectification déclarée**, nommée et justifiée dans le rapport.
6. **Tous les tests s'exécutent sur des copies.** Les outils le font déjà ; ne pas lancer de build destructif dans `package/` sans raison.
7. **Aucun verdict global d'efficacité.** Pas de clôture FULL d'efficacité sans observateur indépendant (critères D3 : relation externe ou collaborateur non impliqué, conflit déclaré). Une revue par sous-agent du même auteur est une auto-comparaison, déclarée comme telle.
8. **Non-régression à chaque unité** : 300/300, témoins 40/40, harnais R et R03 verts, `validate_all` vert.
9. **Distinguer certain, probable, hypothétique** dans chaque rapport.
10. **Garder le plan maître et les rapports à jour** (`audit/reports/`), pour que le travail puisse reprendre ailleurs.

## 5. Commandes

Depuis `audit/tools/` :

```bash
# Suivi des 22 harnais (environ 5 à 10 minutes), comparé au dernier instantané
python3 DG_AUDIT_001_Suivi_harnais.py ../../package --compare ../snapshots/DG_AUDIT_001_Instantane_harnais_B04_R03.json  # sur B05 : V12_Instantane_harnais_B05_Lot2.json [--out ../snapshots/<nouvel_instantane>.json]

# Harnais du retour
python3 R_harnais_non_regression.py ../../package      # attendu : Témoin 1/1 ; cas R 30/30
python3 R03_harnais_non_regression.py ../../package    # attendu : Cas R03 18/18

# Vérifications 13.01 et épreuves 13.02
python3 DG_AUDIT_001_Verifications_13-01.py texte ../../package
python3 DG_AUDIT_001_Verifications_13-01.py non-regression ../../reference/B01_transfert/02_Sources_B01/package ../../package
python3 DG_AUDIT_001_Epreuves_13-02.py ../../package
```

Depuis `package/` :

```bash
python3 -B scripts/validate_all.py        # validation complète, build des deux distributions
python3 -B scripts/validate_reading_map.py  # 42 conditions (V1.1.1) ; 50 sur B05
python3 scripts/read_route.py ACTION/RUN_CARD  # lire une route
```

**Limite connue :** `DG_AUDIT_001_Verifications_13-01.py distributions` cherche `python3.10` et `python3.13`. S'ils sont absents de l'environnement, ces lignes échouent « indisponible » : ce n'est pas une régression.

## 6. Prochaine étape

1. ~~Porte G1 du plan V1.2~~ : franchie le 26-09-2026 (`audit/reports/V12_01_DECISIONS_G1.md`).
2. ~~B05, lot 1 (A, B, D), addendum, lot 2 (G, H, I, D')~~ : faits (`V12_02` à `V12_04`). Lectures `V12_05` à `V12_11` faites. Mini-épreuve **reportée par l'owner** (27-09-2026). **Prochaine décision de l'owner : chantier « structure et budget » (`V12_11` §5 : phases 0 → 1 → 2, puis épreuve)** ; la mini-épreuve V1.2 reste disponible (addendum §5-§6 : C3 ×2, C3r ×1, juge neuf avec brief riche intégral), puis G4.
3. Suivre le séquencement du plan : G2 (gardes rouges puis vertes) → G3 (non-régression, budget tenu) → G4 (épreuve à l'aveugle avec juges extérieurs) → publication V1.2.0.

Travail par branche : une branche par unité (`v1.2/patch-decision-abd`, …) ; étiquettes aux points de contrôle ; rapport de l'unité dans `audit/reports/`.

## 7. Style de travail attendu par l'owner

- Répondre **en français**, clair et structuré, sans remplissage. Profondeur utile, minimum de bruit.
- Montrer le pourquoi et le comment ; hiérarchiser ; distinguer certain, probable, hypothétique, à vérifier.
- Progresser étape par étape, en continuité avec les décisions déjà validées.
- Donner à chaque unité un périmètre, une priorité, des critères de réussite et des critères d'arrêt.
- Rapports « allégés » : diff, résultats, écarts déclarés.
- Adapter l'effort : une tâche simple reste rapide ; signaler une tâche surdimensionnée.
- Économiser les limites d'usage : éviter les relectures intégrales inutiles et les agents superflus.
