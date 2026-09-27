# V1.2 refonte — Unité R11a — Correctifs signalés par le plan consolidé

**Date :** 2026-09-27 · **Déclencheur :** plan consolidé proposé à l'owner (`plans/propositions/Plan_consolide_V1.2_2026-09-27.md`), dont les constats ont été vérifiés dans le dépôt ; « Oui » de l'owner pour corriger. **PATCH-DECISION :** `audit/tools/V12R_Patch_R11a.py` (2 entrées). **Diff :** `audit/diffs/V12R_R11a_correctifs.diff`.

## 1. Correctifs

| Constat (vérifié) | Correctif | Nature |
|---|---|---|
| `DIRECTION/START`, « ordre de lecture minimal » : « `DAILY` choisit la plus petite route utile ». Ce résidu de R4 avait échappé à la mesure | « `CHARGE` choisit… ». Garde : vocabulaire retiré `` `DAILY` `` hors CHANGELOG | Package (PATCH-DECISION) |
| `plans/carte_moyens_v0.md` : « Client ; sinon emplacements marqués » contredit D-20 | « contenu d'exemple marqué et liste de ce qu'il faut fournir (D-20, `CNT-01`) » | Document de travail (hors package) |
| Atteignabilité tombée à **23/25** : l'ancre de F13 (« celle que le modèle produirait sans brief ») ne correspondait plus au texte après R8a (« celles… ») | Ancre de mesure rectifiée (« que le modèle produirait sans brief ») : **24/25**. L'outil n'avait jamais quitté le chemin | Outillage d'audit (rectification déclarée) |
| Plan de reprise et `CLAUDE.md` périmés : chiffres, dette D-16, F22, exemptions | Mesures et dette actualisées ; outil manquant identifié : **F22**, atteignable depuis Gate C sous condition | Documents de reprise |

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| Rouge avant ; vert après ; mutation | 1 erreur (DIRECTION:155) → vert ; 1/1 rouge |
| Suivi | Vert : 372 cas maintenus, aucune migration ; chemin 12 187 mots ; noyau 3 302 mots ; 24/25 outils |
| 13.01 ; 13.02 ; B01 | 6/6 et 5/5 ; 38/38 ; 218/218 |

## 3. Écarts déclarés

1. **La baisse F13 n'a pas été vue en R8a.** Le suivi n'a pas de cliquet d'atteignabilité, et le rapport R8a n'a pas relu la section 2 de la mesure. **Proposition**, à décider : ajouter ce cliquet au suivi (rectification déclarée de `V12R_Suivi.py`).
2. **Le rapport R5d annonçait le noyau à 3 222 mots.** C'était la valeur de R5b-2 ; les ajouts de R5a (D-19) et de R8a le portent à 3 302.
