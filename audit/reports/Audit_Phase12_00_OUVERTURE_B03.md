# DG-AUDIT-001 — Phase 12.00 — Ouverture de la phase 12 : candidate B03

**Date :** 25 septembre 2026. **Auditeur :** Claude.

**Décision de l'owner :** « Oui, enchaîne avec 12.00 sous le nom B03 ». La phase 12 est ouverte, conformément à 11.23 (§5 à §8).

| Baseline | Statut |
|---|---|
| **B01** | Canonique, **lecture seule** jusqu'à la fin de l'audit |
| **B02** | Hypothèse gelée ; n'est ni lue ni reprise |
| **B03** | Candidate de la phase 12, dérivée de B01 |

**Sorties :**
- ce rapport ;
- `DG_AUDIT_001_B03_empreintes_12-00.txt` (60 empreintes) ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-00.json` ;
- le plan maître mis à jour.

Aucune correction n'est appliquée dans cette unité.

---

## 1. Création de B03

| Point | Fait |
|---|---|
| Source | `02_Sources_B01/package`, vérifiée **avant** la copie : `SHA256SUMS.txt` 218/218, aucun fichier généré |
| Copie | `B03/package`, copie à l'identique (`cp -a`), **60 fichiers**, aucun lien symbolique |
| Égalité | Liste d'empreintes de B03 **identique octet pour octet** à celle de B01. Recoupée avec les 60 lignes du package dans `SHA256SUMS.txt` de l'audit : **conforme** |
| Historique | Dépôt git **hors du package** (`B03/B03.git`, arbre de travail `B03/package`). Commit initial `cf0af4f`, étiquette `12.00-B03-ouverture` |

**Pourquoi un dépôt externe.** Le §22 exige un patch **lisible en diff** et **réversible**. Git donne les deux :
- un commit par étape, avec son étiquette ;
- un diff exportable ;
- un retour arrière par `git revert`.

Un `.git` **dans** le package aurait été copié par les harnais et par le build. Le validateur documentaire l'aurait alors vu comme un fichier inattendu. Le dépôt est donc placé à côté : le package ne contient que ses 60 fichiers.

## 2. État de référence de B03

| Contrôle | Résultat sur B03 (copie temporaire) | Attendu |
|---|---|---|
| `validate_all.py` | **FULL VALIDATION PASSED** (GitHub 60, Local 56, RUN_CARD, contrats, carte, CLI, build, reproductibilité) | Identique à B01 |
| `DG_AUDIT_001_Suivi_harnais.py --compare …_B01.json` | Témoins **40/40** ; cas **3/300** ; code 0, **aucune alerte** | Identique à B01 |
| Instantané B03 comparé à l'instantané B01 | **Identiques**, empreintes des 22 harnais comprises | Identiques |
| Après les contrôles | B03 : aucun fichier généré, `git status` vide. B01 : 218/218, aucun fichier généré | Rien n'a bougé |

**B03 est donc, de façon certaine, B01 sous un autre nom.** Toute différence ultérieure viendra d'un commit de phase 12.

## 3. Règles de conduite de la phase 12

Ces règles reprennent le §22 du protocole et les conditions de 11.23. Elles n'ajoutent rien de nouveau.

### 3.1 Une unité = une étape (ou une partie d'étape) de l'ordre de 11.23 §7

| Unité | Contenu | Charge estimée |
|---|---|---|
| 12.01 | A1 : autorité du schéma | Faible (deux scripts, environ 100 lignes) |
| 12.02 | A2 : oracles et motifs | Faible à moyenne |
| 12.03 | Cycle de garde : résolveur et carte, LCF (21), `SEED` | Moyenne |
| 12.04 | Migration unique : 4 schémas, 48 invariants avec leurs cas unitaires, données | **Lourde** : découpée en sous-unités (§3.3) |
| 12.05a–g | Textes : CHANGELOG, BIBLIOTHEQUE, **ACTION**, **DIRECTION**, SAVOIR, cartes et glossaire, façades | **ACTION et DIRECTION sont lourdes** : sous-unités possibles |
| 12.06 | Cycle d'outil final (C8, E2, E1 O-1, F-WF-001, manifeste et version) | Moyenne |
| 12.07 | Sortie de la phase 12 : bilan, réévaluation des fiches touchées | Faible |

### 3.2 Ce que chaque unité produit (§22 : `PATCH + DIFF-REASONING`)

1. **Commit** dans B03, avec l'étiquette de l'unité. Le diff est exporté (`DG_AUDIT_001_B03_<unité>.diff`).
2. **Rapport** : fiches traitées, fichiers touchés, puis le raisonnement de diff. Pour chaque changement : la décision de phase 11 qu'il applique, et **tout écart** entre la cible écrite en phase 11 et le texte appliqué, déclaré comme tel.
3. **Suivi des harnais** : `--compare` avec l'instantané de l'unité précédente. Sans alerte, sauf les rouges attendus du cycle de garde (11.23 §6).
4. **Relecture** des zones et interfaces listées dans les conditions de la grappe (§22 : relecture complète si le rayon d'impact est fort).
5. **Contrôle de B01** : 218/218, aucun fichier généré.
6. **Archive de B03** à l'état de l'unité, pour qu'une reprise hors de cette conversation soit possible.

### 3.3 Règles de découpage

- **Une passe par propriétaire reste une passe**, même répartie sur plusieurs unités. La relecture complète et la réévaluation se font à la fin de la passe, pas à chaque sous-unité.
- **Migration unique** : elle peut être répartie en sous-unités (par exemple RUN_CARD puis contrats). Mais la suite ne passe aux textes qu'une fois **toute** la migration faite (C6 C1 : un exemple ne montre que des champs qui existent).
- **Aucun harnais ne change pour épouser un patch.** Si le texte appliqué doit différer de la cible décidée, la rectification est déclarée d'abord (règle de 11.23 §4.5). L'outil de suivi la rend visible par l'empreinte du harnais.

## 4. Décision en attente, non bloquante

**Numéro de version de B03.**
- **Sources :** le CHANGELOG (ligne 3 : `V1.0.0`) et le manifeste (`"version": "1.0.0"`) sont alignés aujourd'hui. E2 O-13 fait du CHANGELOG la source unique.
- **Contrainte :** B02 portait `V1.0.1`. Reprendre ce numéro créerait une ambiguïté avec l'hypothèse gelée.
- **Ce qui est déjà fixé :** A1 C6 prévoit une ligne dans les notes de version du prochain lot publié.
- **Aucune PATCH-DECISION ne fixe le numéro.** Je poserai la question à l'étape 12.06, où la version est mise à jour. D'ici là, B03 garde `1.0.0`.

## 5. Sortie

- **Phase 12 ouverte.** B03 est identique à B01 (60/60 empreintes).
  - Suite intégrée verte.
  - Harnais identiques à la référence : 40/40 témoins, 3/300 cas.
  - Historique git initialisé hors du package.
- **B01 intacte** (218/218). B02 non touchée.
- **Prochaine unité : 12.01 A1.** Elle modifie `validate_run_card.py` et `validate_contracts.py` : chargement gouverné du schéma, témoin négatif avant tout PASS, parcours statique des mots-clés, témoin `depth` de F-VCT-003.
  - Sortie attendue : harnais A1 **11/11**, aucun autre harnais en recul, `validate_all.py` toujours vert (A1 C3).

**§32.**
- Cette unité n'a produit aucune information nouvelle sur le système. C'est normal : c'est une mise en place.
- Son apport tient à ce qu'elle rend **vérifiable**. Chaque écart futur par rapport à B01 sera un commit attribué, et chaque recul d'un harnais sera signalé par l'outil de suivi. Elle ne se justifie que par là, et c'est pourquoi elle reste courte.
