# V1.2 refonte — Unité R5a — DIRECTION restructurée

**Date :** 2026-09-27 · **Consigne de l'owner :** pas de run ni d'épreuve dans cette phase ; qualité avant nombre de mots ; plan de reprise tenu à jour (`plans/Plan_V1.2_Suite_Reprise.md`).
**PATCH-DECISION exécutable :** `audit/tools/V12R_Patch_R5a.py` (12 entrées). Les sections déplacées sont reprises mot pour mot depuis `V12R_Patch_R5a_textes.py`. **Diff :** `audit/diffs/V12R_R5a_direction.diff` (4 files changed, 64 insertions(+), 51 deletions(-)).
**Reproductibilité :** le patch appliqué à l'état d'avant R5a (commit 887329e) redonne exactement le package actuel (archives de build exceptées).

## 1. Ce qui change

| Défaut | Changement |
|---|---|
| **D-17** (ordre) | `## Rôle` (bloc noyau `ROLE`, concept `ROL-01`) et `## Posture` passent en tête du fichier. `### Récapitulatif de protection` (« Avant de parcourir les sections détaillées… ») passe en tête de la constitution au lieu de la clôture |
| Rôle en double | « Mandat de fonctionnement » (copie du rôle) retiré ; sa seule clause propre (« ne confère ni expérience biographique, ni autorité de preuve, ni permission externe ») rejoint le rôle |
| Entrée concurrente | La table « Besoin immédiat / Lire d'abord » est remplacée par quatre renvois : classer `START`, charger `CHARGE`, fabriquer avec le noyau, vérifier avec `ACTION`. « En trente secondes, nomme… » est conservé |
| Doublons de lecture | Chaîne « `CREATIVE-BOOT` ouvre… `ACTION` la ferme » retirée d'« Architecture d'activation » (elle reste dans « Chaîne de lecture interne », gardée par LCF-07) ; renvoi de lecture corrigé ; règle de passage finale réduite à un renvoi vers `DIRECTION/CHARGE` |
| **D-19** | Bloc noyau `BRIEF` : « cette vue reste interne » → « le raisonnement de cadrage reste dans la trace » (noyau recompilé) |

**Aucun locator renommé.**

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant (nouveau validateur, package non patché) | 8 erreurs : `ROL-01` absent ; 4 vocabulaires retirés ; 3 fois ORD-01 |
| Vert après | `validate_structure` : 18 concepts, 9 vocabulaires retirés, ORD-01 ; `validate_reading_map` : vert, aucune rectification |
| Mutations | **5/5 rouges** |
| Suivi | **Vert** : 372 cas maintenus, 17 migrés (inchangé), aucune migration ; `validate_all` vert. Instantané : `V12R_Instantane_suivi_R5a.json` |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |
| Mesures | Chemin 12 084 mots (+8) ; doublons 152 → **150** ; négations 809 |

## 3. Écarts déclarés

1. **Garde ORD-01 corrigée avant le premier vert.** Sa première version comparait le titre complet au lieu de son début, et rougissait sur un ordre correct. La correction a été reportée à l'identique dans la copie du patch.
2. **Règle de passage.** Le nouveau texte garde le début de ligne « Le passage entre propriétaires reste », que lit le harnais D4 G-05 (maintenu jusqu'à réécriture). Cela évite une migration ; le premier suivi l'avait rougi.
3. **« Trois couches »** (noyau du fichier, référence, frontières) **non matérialisées** par une réorganisation des sections. Les déplacer aurait touché des ancres lues par les harnais pour un gain de lecture nul : l'agent lit le noyau compilé, pas DIRECTION en entier. La couche « noyau » existe déjà par les balises `noyau:`.
4. **Doublons inter-fichiers de DIRECTION** (alternative située, `ANCHOR-GENERATED`, statuts) **non traités**. Ils relèvent des lots des fichiers qui portent l'autre copie (R5c, R5d, R6) ; reportés au plan de reprise.

## 4. Lecture

- **Certain :**
  - DIRECTION s'ouvre sur le rôle, la posture et le récapitulatif de protection ;
  - une seule entrée ;
  - D-17 et D-19 fermés ;
  - aucune propriété perdue.
- **Probable :** un lecteur humain (ou un agent sans skill) s'oriente plus vite.
- **Hypothétique :** l'effet sur le rendu, faible, car l'agent lit surtout le noyau.
- **Limite :** auto-comparaison.
