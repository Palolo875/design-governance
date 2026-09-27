# V1.2 refonte — Unité R0 — Décisions de l'owner

**Date :** 2026-09-27 · **Owner :** Junior (Kamel) · **Plan :** `plans/Plan_V1.2_Refonte.md`

## Décisions prises (27-09-2026)

| # | Décision | Choix de l'owner | Conséquence |
|---|---|---|---|
| 1 | Forme du noyau de run | **Blocs normatifs balisés dans les sources, compilés dans la skill** | `scripts/build_core.py` (R4) ; `validate_all` échoue si la skill diverge de sa compilation |
| 2 | Traitement des harnais | **Gardes de propriété + table de correspondance des 300 cas** | R1 cartographie les cas ; R2 écrit les gardes et la table ; aucun cas abandonné sans décision déclarée |
| 4 | Sortie visible par défaut | **Langage produit** : ce que j'ai fait, pourquoi, ce qui manque pour la vraie version, la suite ; trace sur demande | Réécriture de la sortie en R4 ; `ACTION/HANDOFF` conserve la trace |
| 7 | Marqueurs de vague | **Dans le noyau**, sous `[VEILLE]` daté avec date de revue | Rectification déclarée de LCF-46 en R4 |

## Décisions en attente (à prendre au lot concerné)

- **3** : version et schéma (R9) ;
- **5** : checkpoint (R5b) ;
- **6** : ancre graduée (R7) ;
- **8** : lois de SAVOIR (R10) ;
- **9** : juges (R10) ;
- **10** : catalogue (après publication) ;
- **11** : trace par défaut (R5b, R9).

Les recommandations écrites du plan (§8) servent de base de proposition au moment du lot. Elles ne valent pas décision.

## Méthode

- Ces décisions ouvrent les lots R1 à R4.
- R1 est hors package : il ne demande pas de PATCH-DECISION.
- R2, R3 et R4 feront chacun l'objet d'une PATCH-DECISION exécutable, soumise à l'owner avant application.
