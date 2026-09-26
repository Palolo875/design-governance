# DG-AUDIT-001 — Phase 12.05b — PATCH : passe ACTION

**Date :** 26 septembre 2026. **Candidate :** B03. B01 reste en lecture seule ; B02 reste gelée. **Format :** rapport allégé.

**Commit :** `c59783f`, étiquette `12.05b-action`.

**Fichiers produits :**
- `DG_AUDIT_001_B03_12-05b.diff` ;
- `DG_AUDIT_001_B03_package_12-05b.zip` ;
- `DG_AUDIT_001_Instantane_harnais_B03_12-05b.json` ;
- `C1_harnais_non_regression.py`, rectifié (R-11, §3).

**Ordre suivi :** 11.23 §7. ACTION vient après BIBLIOTHEQUE et avant DIRECTION : DIRECTION, les cartes et les façades renvoient au canon d'ACTION (triade, HANDOFF, table de correspondance), qui doit donc exister avant elles.

## 1. Inventaire de la passe

L'inventaire a été extrait des 22 rapports de la phase 11 : ce sont toutes les lignes de correction dont la cible est ACTION. Une seconde lecture, par colonne « Où », n'a trouvé aucune ligne oubliée. **44 corrections, toutes appliquées, dans un seul fichier (`ACTION.md`, +150 / −55).**

| Décision | Corrections | Zone d'ACTION | Contenu appliqué |
|---|---|---|---|
| **C4** | T-1, T-2, T-7, T-8 | En-tête, carte de chargement, RUN_CARD | Entrée par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis `ACTION/RUN-<MODE>`. Un socle commun et des locators complets ; la sortie de chaque mode est renvoyée à `ACTION/CLOSE-PACKAGE`. Profil strict et TRACE-LOCATOR requis en ITER sérialisé |
| **C3 / C2** | C3 T-4 ; C2 T-1, T-2, T-3, T-9, T-10 | HANDOFF, RUN_CARD, STRUCTURED-PROOF, UI-UX-REALITY | Deux sorties : le handoff à 13 champs (canon LCF-C1) et la réponse visible à 7 jetons (canon LCF-C2), plus la forme courte LITE. Table de correspondance avec colonne Phase et règle « hors projection : trace ». `risk.statement`. STRUCTURED-PROOF est retitré et reçoit une matrice d'activation et une règle de phase. Scope attendu et scope observé |
| **C1** | T-1, T-3, T-4, T-5 | STATUS, RUN, clôture, pipeline | Conséquence décisionnelle et sa triade ; verdict `null` avant `CHECKING` ; `STOP — [raison]` ; résultats locaux de comparaison et leur correspondance |
| **B1** | T-3 | RUN_CARD, OVERRIDE | Protection critique à résultat. `closure.exception` : structure de réserve sans date propre, plus `gate_axis`, `failure_evidence`, `requested_by` et `disposition` |
| **B2** | T-1 à T-8 | STATUS, RUN_CARD, clôture | Compatibilités ; `closure.axes` ; basis typée et capacité ; fraîcheur (version d'artefact égale à la version de preuve, date ISO) ; `closure.reservations[]` ; `rights_status` ; snapshot datable ; promesse du validateur (atteste / n'atteste pas) |
| **B3** | T-1, T-2, T-3, T-4, T-6 | CLOSE-PACKAGE, RUN-SYSTEM, baseline, B1b | Colonne « Contrôle machine » et phrase « un verdict vert ne certifie que ce que la liste close contrôle ». `closure.system_package` et la baseline. **B1b → `closure.b1b`** : ses deux seuls motifs de N/A deviennent les deux valeurs admises. Promesse « par mode » |
| **B4 / B5** | B4 T-3 ; B5 T-2 | Ancres, composants | Types d'ancre, enjeu identitaire, calibration. Le contrat de composant renvoie à `BIBLIOTHEQUE/COMPONENTS` |
| **D1** | T-3, T-4 | Passe créative, GATE-C | Revue créative définie par `SAVOIR/CRAFT/CFT-00`. Gate C décide à partir de cette revue et de la paire B1b ; il ne refait pas une seconde revue |
| **D2** | T-4 | RUN-ITER | Entrée : `direction.thesis` et `trace_locator` |
| **D3** | T-1, T-2, T-3, T-4, T-5, T-7 | Étape 7, AUTHORITY, GATE-A, B3, POLICIES | L'autorisation manquante renvoie à `ACTION/AUTHORITY` (« cette compensation n'autorise rien ») ; reviewer ≠ décideur. **Motion réduite** : implémentée et vérifiée, sinon `NOT-VERIFIED`. **B3** : la seconde session du même auteur est une auto-comparaison différée ; relation, auteur du rendu, conflit ; expositions multiples ; règle du label « indépendant ». **Ressources techniques** : trois branches |
| **E1** | F-ACT-003, 004, 016, 032, 034 | Divers | Quatre registres ; « changer la décision, la preuve ou la limite » ; FAST-PATH → forme courte LITE ; partition typographique selon `SAVOIR/TYPE` ; **provenance absente ⇒ verdict non accepté** |

Aucun contenu nouveau au-delà des cibles décidées. Les écarts de rédaction sont au §3.

> **Erratum (12.05c).** Une 45ᵉ ligne visait ACTION : B4 T-5, le point « forme seule » sur la fraîcheur de l'ancre dans la promesse du validateur. Sa colonne « Où » ne nommait pas ACTION et elle a échappé à l'inventaire. Elle est appliquée en 12.05c (rapport 12.05c, §3).

## 2. Résultats

| Contrôle | Résultat |
|---|---|
| **Gardes ACTION** | Toutes vertes : B5-03 ; C1 G-01, G-08, G-10 ; C2 G-01, 02, 04, 05, 10, 11, 12 ; C4 G-01, 02, 03, 07 ; D1 G-02, G-03 ; D2 G-04 ; D3 G-01 à G-05 et G-07 ; E1-01 à E1-05 |
| **Canons LCF-C1 / LCF-C2** | Côté ACTION, en place : le handoff canonique extrait compte 14 jetons, et la réponse visible est présente dans `ACTION/HANDOFF`. Les deux conditions restent rouges jusqu'aux copies (READING_MAP, QUICKSTART, skill), qui sont en 12.05c |
| Validateur de carte | Rouge seulement pour les **21 motifs de la fenêtre** : 20 LCF et le titre en double `DIRECTION/START`. Les nouveaux renvois (`ACTION/RUN-<MODE>`, `SAVOIR/CRAFT/CFT-00`, `SAVOIR/TYPE`, `ACTION/AUTHORITY`, `BIBLIOTHEQUE/COMPONENTS`) sont tous servis |
| Package, RUN_CARD, contrats | `validate_design_governance` vert ; RUN_CARD : 25/25 fixtures, 76/76 cas ; contrats : 20/20 cas |
| Suivi (`--fenetre --rectifies C1 --compare` 12.05a) | **Cas significatifs : 160 → 190/300**, aucune alerte. Gains : C2 +7, E1 +5, D3 +6, C4 +4, C1 +3, D1 +2, B5, C3 et D2 +1 |
| B01 | 218/218, aucun fichier généré |

**Relecture de fin de passe (§22).** J'ai relu les 50 zones modifiées, dans le fichier final, avec leur contexte. Un seul point relevé : deux phrases redondantes dans Gate C (texte de B01 et D1 T-4). Elles sont fusionnées, voir §3. Aucune autre incohérence.

Les points suivants ont été vérifiés à la relecture et sont cohérents :
- l'exception reprend la réserve sans `date_version`, conformément au choix de 12.04 ;
- la réserve garde ses sept attributs ;
- la forme courte LITE et le `TRACE-LOCATOR` de LITE disent la même chose.

## 3. Écarts et rectifications déclarés

| # | Écart | Traitement |
|---|---|---|
| **R-11** | La garde C1 G-01 (« ACTION/STATUS place NOT-OBSERVED ») découpait la section avec `find("## ")`. Cette recherche trouve aussi `### `, si bien que la tranche s'arrêtait au premier sous-titre et ne couvrait que l'introduction de STATUS. La ligne décidée (C1 T-1, placée après la table des issues) restait donc invisible pour la garde | **Rectification de harnais** : la tranche s'arrête au prochain `\n## `, c'est-à-dire qu'elle couvre la section entière, comme le dit le libellé. **B01 reste rouge** sur G-01 avec la tranche corrigée : le pouvoir discriminant est conservé. Les dénominateurs sont inchangés. L'empreinte est déclarée avec `--rectifies C1`. Le texte n'a pas été déplacé pour satisfaire la garde |
| Contrôle de R-11 | Pour vérifier que B01 reste rouge, le harnais C1 a été lancé une fois directement sur B01, et non sur une copie | Ce harnais ne travaille qu'en lecture et sur copies temporaires. Après ce lancement, B01 était à 218/218, sans aucun fichier généré |
| Gate C (D1 T-4) | La phrase décidée doublait la phrase de B01 sur la paire B1b (« ne recrée pas une seconde procédure de comparaison ») | **Fusion en une phrase.** Le texte décidé est conservé mot pour mot, avec le renvoi `ACTION/GATE-B — B1b` et la fin « ni une seconde procédure de comparaison ». Aucune garde ne dépend de l'ancienne phrase |
| Jetons de B3 (D3 T-5) | La décision nomme les relations en français (même auteur, impliqué dans le run, collaborateur non impliqué, externe) | Elles sont écrites en jetons, dans le style des lignes voisines (`REVIEW-EXPOSURE`, `MAPPING-TIMING`) : `SAME-AUTHOR`, `INVOLVED-IN-RUN`, `UNINVOLVED-COLLABORATOR`, `EXTERNAL` ; conflit `DECLARED` ou `NONE-KNOWN`. La règle du label « indépendant » cite ces jetons |
| Motion réduite (D3 T-3) | La décision tient en une phrase. La table a deux colonnes : « `PASS` si… » et « retour ou réserve si… » | La condition de `PASS` et le `N/A-JUSTIFIED` sans motion vont dans la première colonne ; le `NOT-VERIFIED` (alternative seulement dessinée ou annoncée) va dans la seconde. Le mot « prévue » disparaît, comme l'exige D3 G-03 |
| B1b (B3 T-4) | La correspondance décidée nomme les valeurs admises | La phrase ajoute aussi ce que le validateur ne vérifie pas : que la décision couverte par une paire équivalente est bien la même. Ce texte reprend §5.1 de la décision B3 ; ce n'est pas un contenu nouveau |

**Toujours à surveiller :** R-4 (budget de `DIRECTION/START`, 76 lignes pour 75). Il se tranche en 12.05c.

**Journal des notes de version (B03), ligne ajoutée :**

> 12.05b — ACTION : carte de chargement par locators complets ; deux sorties canoniques (handoff, réponse visible) et forme courte LITE ; table de correspondance RUN_CARD par phase ; promesse du validateur (atteste, n'atteste pas, par mode) ; triade de conséquence décisionnelle ; paquets de clôture avec contrôle machine ; B1b, exception, réserves, droits, fraîcheur et ancres alignés sur la RUN_CARD ; motion réduite vérifiée ; regard externe qualifié (relation, auteur, conflit) ; provenance absente ⇒ verdict non accepté.

## 4. Suite

**12.05c : DIRECTION, SAVOIR, cartes, glossaire et façades.** C'est la dernière passe de texte, et elle ferme la fenêtre de garde. Elle comprend :
- C4 T-3 à T-5 : ligne `DIRECTION/START/TREE`, renommage du second `DIRECTION/START` ;
- les copies du handoff et de la réponse visible (LCF-C1, LCF-C2) ;
- toutes les conditions LCF ;
- les gardes DIRECTION, SAVOIR et façades (C1, C2, C3, C5, C6, C7, D1, D2, D4, E1 F-DIR, F-SAV, F-QS, F-SK, etc.) ;
- l'arbitrage de R-4.

**Critère de sortie de 12.05c :**
- `validate_all` redevient vert sans neutralisation ;
- `--fenetre` n'est plus utilisé ;
- tout témoin rouge redevient une alerte.
