# DG-AUDIT-001 — Phase 11.19 — PATCH-DECISION D3 : autorité, droits et gates spécialisés

**Date :** 25 septembre 2026. **Auditeur :** Claude. **Baseline :** B01 inchangée. B02 reste une hypothèse gelée.

**Décision de l'owner :** « Oui, enchaîne ».

**Grappe D3 : 4 fiches, toutes Significatif.** Elles ont un point commun : un contrôle qui **n'a pas été obtenu** est traité comme s'il l'avait été.

| Fiche | Confusion |
|---|---|
| F-ACT-026 | **Autorité ↔ preuve** : l'étape 7 du pipeline DIRECTION laisse compenser une autorisation manquante par capture, réserve et prochaine preuve |
| F-ACT-033 | **Prévu ↔ vérifié** : Gate A accorde `PASS` à une motion réduite « prévue » |
| F-ACT-037 | **Autre session ↔ autre regard** : B3 admet « une seconde session » comme regard externe, sans critère de relation, d'auteur du rendu ni de conflit |
| F-SAV-009 | **Nouvelle dépendance ↔ script local** : SAVOIR/TECH 778 exige une approbation complète pour tout script, sans branche proportionnée |

**Sorties :**
- cette `PATCH-DECISION` ;
- `D3_harnais_non_regression.py`, une garde textuelle : **aucun invariant machine** ;
- un **addendum à D1**, qui rectifie un constat.

Aucun patch, aucun prototype.

---

## 1. Rituel et sources

| Étape | Exécution |
|---|---|
| Décisions précédentes | D-ACT-1 = c ; C2 (table de correspondance RUN_CARD) ; B4 (`calibration` exclut la revue indépendante) ; C7 et D1 (limite « observateur indépendant ») |
| Empreintes | Compilation B01 `016e6002…` conforme ; `SHA256SUMS.txt` 218/218 |
| Sources relues | ACTION 63–67 (AUTHORITY), 288–299 (mode agent seul), 499–506 (pipeline, étape 7), 653–690 (Gate A), 702–720 (B1b), 735–753 (B3), 850–866 (ressources techniques) ; SAVOIR 712, 740 (MOTION), 778 (TECH) ; DIRECTION 693 ; schéma RUN_CARD (propriétés) |

## 2. Re-vérification

**Garde D3 sur B01 :**
- témoins **4/4** ;
- gardes **0/7**.

Les quatre fiches sont **confirmées par relecture**. Le propriétaire contient chaque fois la règle juste **ailleurs**. Le défaut est donc local, et la correction consiste à aligner le passage fautif sur la règle existante.

| Fiche | Passage fautif | Règle juste déjà présente |
|---|---|---|
| F-ACT-026 | ACTION 505 : « Si aucun regard externe n'est disponible… compense par capture, comparaison, réserve et prochaine preuve », placé **juste après** le checkpoint d'autorisation (503) | ACTION/AUTHORITY 65–67 : « un checkpoint indisponible ne réduit pas silencieusement le mode… exploratoire, retourné ou escaladé » |
| F-ACT-033 | ACTION 677 : `PASS` si l'alternative sans mouvement est « **prévue** » | ACTION 653 (« ce qui le remplace est testé ») et 665 (hypothèse sans runtime = `NOT-VERIFIED`) ; SAVOIR 740 |
| F-ACT-037 | ACTION 737 : « une seconde session… peut réduire l'auto-préférence », dans la section « Regard externe », et une exposition réduite à **une seule** valeur | ACTION 299 et 720 : une auto-comparaison « ne satisfait jamais un claim de revue indépendante » |
| F-SAV-009 | SAVOIR 778 : aucun outil ni script **sans** dépendance approuvée, package/version, owner… | ACTION 852 : politique proportionnée ; « jamais exécutés aveuglément » |

**Machine.** Le schéma RUN_CARD n'a ni objet d'autorité ni objet de revue. Un objet d'autorité structuré est **rejeté** (`champs inconnus`), comme le notait la fiche.

## 3. Les sept questions du §21

| Question | F-ACT-026 | F-ACT-033 | F-ACT-037 | F-SAV-009 |
|---|---|---|---|---|
| Change une décision, une exécution ? | **Oui** : build d'une nouvelle identité sans décision du rôle responsable | **Oui** : faux `PASS` d'accessibilité | **Oui** : validation identitaire circulaire | **Oui** : contrôle bloqué ou trace fictive |
| Défaut réel ? | Oui (texte) | Oui (texte) | Oui (texte ; **observateur unique dans toute la campagne**) | Oui (texte ; aucun blocage observé) |
| Gain > charge ? | Oui : une phrase et une ligne de table | Oui : une cellule | Oui : trois lignes de trace | Oui : une phrase et trois branches |
| Nouvelle autorité ? | **Non** : AUTHORITY existe | **Non** : 653 et 665 | **Non** : 299 et 720 ; les nouveaux champs de trace **explicitent** l'indépendance, qui était déjà exigée | **Non** : ACTION 852 |
| Testable ? | Garde et épreuve | Garde et épreuve | Garde et épreuve | Garde et épreuve |
| Positif / défensif équilibré ? | Oui : l'absence de regard externe reste compensable | Oui : sans motion, `N/A-JUSTIFIED` | Oui : une revue non indépendante reste une preuve située | **Oui, gain positif** : un script local tracé devient praticable |
| Suppression ou fusion ? | **Clarification** | **Correction normative** | **Clarification** | **Clarification** |

## 4. PATCH-DECISION

**Décision : CORRIGER.**

**Aucun invariant machine.** Rien ici n'est déterministe dans la carte : savoir si l'autonomie couvre un périmètre, si un regard est indépendant ou si une alternative a été testée demande une lecture (D-ACT-1 = c, forme seule). **Aucun champ de schéma** n'est ajouté.

| # | Où | Correction | Fiche |
|---|---|---|---|
| T-1 | **ACTION 505** (étape 7) | « **Si l'autorisation manque**, c'est-à-dire si le checkpoint n'est pas couvert par une autonomie explicite, n'engage pas le build : applique `ACTION/AUTHORITY` (exploratoire, retourné ou escaladé). **L'absence de regard externe est une autre question** : déclare-la et compense-la par capture, comparaison, réserve et prochaine preuve ; cette compensation **n'autorise rien**. » | F-ACT-026 |
| T-2 | **ACTION/RUN_CARD**, table de correspondance (C2, T-1) | Ligne ajoutée : « AUTHORITY (portée, base, condition de reprise, décideur) → `owner` = décideur ; le reste hors projection, dans la trace. Un **reviewer** (B3) n'est jamais le décideur par défaut. » **Amendement déclaré de C2** | F-ACT-026 |
| T-3 | **ACTION 677** (Gate A, motion réduite) | « `PASS` si l'alternative sans mouvement est **implémentée et vérifiée préférence activée**, dans le runtime déclaré ; prévue ou dessinée seulement : `NOT-VERIFIED` ; sans motion : `N/A-JUSTIFIED`. » | F-ACT-033 |
| T-4 | **ACTION 737** (B3) | « Un autre évaluateur peut réduire l'auto-préférence. **Une seconde session du même auteur est une auto-comparaison différée** : elle n'est jamais un regard externe, indépendant ou aveugle. » | F-ACT-037 |
| T-5 | **ACTION 743–749** (trace B3) | Trois lignes ajoutées : `REVIEWER-RELATION` (même auteur / impliqué dans le run / collaborateur non impliqué / externe) ; `RENDER-AUTHOR` ; `CONFLICT` (déclaré / aucun connu). `REVIEW-EXPOSURE` accepte **plusieurs expositions** : elles ne sont plus condensées en une valeur. **Règle :** le label « indépendant » exige une relation « collaborateur non impliqué » ou « externe », un reviewer qui n'est pas l'auteur du rendu, et aucun conflit déclaré | F-ACT-037 |
| T-6 | **SAVOIR 778** (TECH) | « Aucun outil, script ou package ne reçoit automatiquement un `PASS`. **Une nouvelle dépendance** exige l'approbation et les champs de la politique d'`ACTION/POLICIES` (inspection et ressources techniques). » SAVOIR garde le jugement, ACTION la politique | F-SAV-009 |
| T-7 | **ACTION 852** (ressources techniques) | Trois branches : **script local sans dépendance nouvelle** : méthode, commande ou version, et résultat tracés ; **outil déjà autorisé** : référence de l'autorisation ; **nouvelle dépendance** : les sept champs actuels et une approbation. La phrase « jamais exécutés aveuglément » est conservée | F-SAV-009 |

**Amendement de C2 (T-2), déclaré.** La table de correspondance de C2 ne mentionnait pas AUTHORITY. Je l'ajoute ici plutôt que de rouvrir C2. La recommandation de F-ACT-026 demande explicitement le « transport reviewer / décideur ».

### 4.1 F-ACT-037 et l'audit lui-même

F-ACT-037 est la limite citée dans presque toutes les sorties de la phase 11 (« observateur unique »). Les critères de T-5 s'appliquent **aussi à cet audit** :
- **Phase 13.** Les épreuves qui visent l'efficacité doivent être conduites par un observateur qui satisfait T-5 (relation « externe » ou « collaborateur non impliqué », pas l'auteur des corrections, conflit déclaré). Sont concernées : la mesure M de C7, l'épreuve d'imitation de C6, l'épreuve « un run, une revue » de D1 et les épreuves de lecture.
- Tant que ce n'est pas le cas, ces épreuves sont des **auto-comparaisons différées** de l'auditeur. Elles sont déclarées comme telles, et **aucune clôture d'efficacité `FULL`** n'est prononcée, conformément à la contrainte déjà posée.

C'est la règle que je demande au système ; je l'applique à mon propre travail.

## 5. Addendum à D1 (rectification)

La relecture de B1b et DOUBLE-LOOP a trouvé **DIRECTION 337–339**, « Relation avec le contrôle compact de `DOUBLE-LOOP` ». Cette section déclarait déjà G4 comme vue compacte de G3.

Le rapport D1 affirmait que les vues de craft ne se déclaraient pas comme telles. **C'est inexact pour G4.** La décision D1 est maintenue (fusion de G4). T-2 de D1 supprime aussi la section 337–339.

Un addendum est ajouté au rapport D1, et la garde G-01 du harnais D1 vérifie désormais l'absence de cette section. Le harnais D1 donne toujours 0/4 gardes sur B01.

## 6. Conditions et sortie

| # | Condition du patch (phase 12) |
|---|---|
| C1 | **Passe ACTION** : T-1 à T-5 et T-7, avec les passes déjà fixées. T-2 dans la même édition que C2 T-1 (même table) |
| C2 | **Passe SAVOIR** : T-6, avec C7 et B5 |
| C3 | **Aucun champ de schéma** : AUTHORITY et la trace B3 restent hors projection (C2) |

**Sortie (phase 13) :**
1. `D3_harnais_non_regression.py` : témoins **4/4**, gardes **7/7**. Harnais A1 à D2 verts.
2. **Épreuves** (tests des fiches), conduites par un lecteur qui ne connaît pas ce rapport :
   - **autorité** : autonomie explicite, implicite ou absente × owner disponible ou non × revue disponible ou non × nouveau public, nouvelle marque, extension de scope ;
   - **motion** : préférence active ou inactive × alternative prévue, implémentée ou testée × capture statique ou runtime ;
   - **indépendance** : même auteur, autre auteur, collaborateur, décideur externe × conflit déclaré ou absent × exposition simple ou multiple ;
   - **outillage** : script local sans dépendance, outil déjà autorisé, nouveau package.
3. **Application à l'audit** (§4.1) : chaque épreuve d'efficacité de phase 13 déclare son observateur selon T-5.

**Limite déclarée.** Les gardes textuelles détectent des formulations. Elles ne prouvent pas qu'un agent distingue autorité et preuve dans un run réel ; seules les épreuves le montrent.

## 7. Sortie

- **PATCH-DECISION D3 : CORRIGER.**
  - 7 corrections de texte ;
  - 1 amendement déclaré de C2 (ligne AUTHORITY) ;
  - 1 addendum à D1 ;
  - aucun invariant, aucun champ, aucune entrée LCF.
- Listes inchangées : liste close **90 lignes, 81 actifs** ; LCF **19**.
- Aucun patch, aucun verdict global.

**§32 : ce que l'unité a changé.**
- Quatre fois, la règle juste existait déjà dans le même propriétaire. La correction **aligne**, elle n'invente rien.
- La limite de l'observateur indépendant cesse d'être une précaution répétée en fin de rapport. Elle devient un **critère opérationnel**, appliqué au système **et** à l'audit.

**Prochaine unité : 11.20 PATCH-DECISION D4** (cycle de vie et claims d'efficacité : F-CHG-001, F-DIR-002, F-DIR-046). Ce sera la **dernière grappe D**.
