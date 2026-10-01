# V1.2 — AP4b : façades (C04, C17, C23, C24, C33, C39 ; AUD-06, AUD-08, AUD-13)

**Date :** 01-10-2026.
**Décision de l'owner :** « Allons-y pour AP4b ». Les textes ont été soumis avant application, comme pour AP3, puis validés (« Allons-y », 01-10-2026) et appliqués tels quels. Les deux points du §5 sont retenus comme proposés : l'exemple du README reste, et « livraison » est définie hors des absolus.
**Pièces :**
- patch : `audit/tools/V12R_Patch_AP4b.py`, 26 entrées dont les textes exacts, plus `_fichiers/` (`validate_structure.py`, `build_distributions.sh`) ;
- diff : `audit/diffs/V12R_AP4b_facades.diff` ;
- instantané : `audit/snapshots/V12R_Instantane_suivi_AP4b.json`.

## 1. Diagnostic (certain, relu sur les sources)

- **AUD-06, C04 :** « trace légère » et « checkpoint » apparaissent 0 fois dans QUICKSTART, READING_MAP, README et les notes de version.
  - QUICKSTART présente « fermer » comme une suite ordinaire (§ parcours commun).
  - La sortie (« deux formes ») ne nomme pas le niveau de trace.
  - Le one-shot exige une « persistance » sans dire à quel niveau de trace.
  - Le GLOSSAIRE définit le mode comme « niveau de protection **et de trace** », et un run comme se terminant toujours par une clôture.
  - READING_MAP lie la `RUN_CARD` au nombre de capacités plutôt qu'au niveau de trace.
- **AUD-13 :** `ACTION/HANDOFF` nomme une « forme courte LITE **non persistante** ». C'est pourtant une forme de clôture, en trace complète. Elle coexiste avec la trace légère sans que le texte les distingue.
- **C17, AUD-08 :** l'exemple « brief flou » se passe dans une boulangerie, le domaine de B-DLA. La personne n'a « rien d'autre » et l'agent construit « faute de réponse », mais la fabrication utilise ensuite des « photos du client ». Le bloc n'a pas non plus la forme de la trace légère.
- **C23 :** README officiel et QUICKSTART citent « Commencer » sans lien. Le chemin diffère entre GitHub (`../../README.md`) et Local (`../README.md`). L'ancre `#commencer` existe dans les deux distributions (bloc partagé).
- **C24 :**
  - QUICKSTART fait « noter » la ligne de run sans dire par qui ni après quel classement ;
  - deux lignes de run différentes, sans lien entre elles ;
  - la section « Pour commencer » du GLOSSAIRE fait établir le mode avant `DIRECTION/START`.
- **C33 :** la ligne « Décision suffisamment établie → décider et persister », compilée dans le noyau, ignore la proposition. « Livraison » n'est situé nulle part.
- **C39 :** les notes de version présentent l'ancien parcours d'agent comme courant (« lire README et QUICKSTART… fermer »). Le pointeur `ORCHESTRATION_MAP` n'a pas d'ancre.

**Lieux relus et maintenus sans changement :**
- `DIRECTION/START` (entrée minimale), le bloc BRIEF et `BIBLIOTHEQUE/MICRO` disent déjà qui agit et quand (C24) ;
- les absolus 1 et 3, dont les titres sont des lois (décision 8) : la notion de livraison est située dans le GLOSSAIRE plutôt que dans la constitution (C33) ;
- la ligne de la skill qui décrit les exemples.

## 2. Textes (avant → après, résumé ; texte exact dans le patch)

| Id | Lieu | Après |
|---|---|---|
| Q1 | QUICKSTART, « Pour qui » | Lien `[« Commencer »](../../README.md#commencer)` (C23) |
| Q2 | QUICKSTART, parcours commun | « Une fois la demande classée par `DIRECTION/START` (par l'opérateur ou l'agent, jamais par la personne qui demande), notez : » (C24) |
| Q3 | QUICKSTART, suites | Ajout de **proposer**. « Par défaut, le run s'arrête à la proposition, en trace légère : la première proposition vaut checkpoint, sauf action irréversible ou coûteuse ; **fermer** suppose la trace complète (run persistant, partagé, audité ou acceptation demandée). » (C04, AUD-06) |
| Q4 | QUICKSTART, sortie | « Le niveau de trace ne dépend pas du mode : sans persistance, partage, audit ni acceptation demandée, la **trace légère** suffit (six lignes au plus, à côté de l'artefact ou sous « Trace » après la réponse) ; dans les autres cas, la **trace complète** s'impose. » (C04) |
| Q5 | QUICKSTART, ligne de run | Elle « reprend la ligne du parcours commun avec un identifiant et l'état du run (`ACTION/STATUS`), l'owner restant nommé dans l'entrée minimale de `DIRECTION/START` » (C24) |
| Q6, Q7 | QUICKSTART, one-shot | « la trace des preuves, limites et décisions, à son niveau » ; « En trace légère, la sortie one-shot est la proposition. En trace complète… directement clôturée si… » (C04) |
| Q8, Q9 | QUICKSTART, handoff agentique | L'agent « lit le noyau de la skill… charge la ligne de son mode dans `DIRECTION/CHARGE` » ; réponse visible « avec la trace légère par défaut » (AUD-06) |
| R1 | README officiel | Lien vers « Commencer » (C23) |
| R2 | README du package | « …corriger, puis proposer (par défaut, en trace légère : la première proposition vaut checkpoint) ou fermer (trace complète) » (AUD-06) |
| G1, G2 | GLOSSAIRE, Mode et Run | Mode = niveau de **protection** ; « le niveau de trace (légère ou complète) se choisit à part ». Un run « s'arrête à une proposition (trace légère) ou à une clôture (trace complète) » (C04) |
| G3 | GLOSSAIRE, Trace légère | Les six lignes d'ACTION, groupées à l'identique (C04) |
| G4 | GLOSSAIRE, nouvelle entrée **Livraison** | « La remise d'un artefact à une personne : la première proposition (trace légère ; elle vaut checkpoint) ou la remise acceptée (trace complète). Les preuves applicables au mode sont dues dans les deux cas ; seule leur écriture s'allège en trace légère. » (C33) |
| G5 | GLOSSAIRE, « Pour commencer » | Lecteur nommé (opérateur ou agent, jamais la personne qui demande). « 1. Classez la demande avec `DIRECTION/START`… 2. Chargez la ligne de ce mode dans `DIRECTION/CHARGE`… » (C24) |
| M1, M2 | READING_MAP | « Sortie : réponse visible et trace légère par défaut ; handoff et clôture en trace complète » ; `RUN_CARD` « en trace complète…, quel que soit le nombre de capacités » (C04) |
| M3 | ORCHESTRATION_MAP | Lien avec ancre vers la section des combinaisons (C39) |
| A1 | `ACTION/HANDOFF` | « **Forme courte LITE** (trace complète d'un `LITE` clôturé sans `RUN_CARD`, distincte de la trace légère, qui ne clôture pas) » (AUD-13) |
| D1 | `DIRECTION/DOUBLE-LOOP`, compilée dans le noyau | « Proposer (trace légère : la proposition vaut checkpoint) ; en trace complète, décider et persister la trace. » (C33) |
| E1, E2 | Exemple « brief flou » | Voir ci-dessous (C17, AUD-06, AUD-08) |
| F1 | `flow.md` | « présenter la proposition (trace légère ; la première proposition vaut checkpoint) » (AUD-06) |
| N1 | RELEASE_NOTES | Note en tête de « Parcours de découverte » : « **Parcours de V1.1.1, historique.** » Entrée courante : « Commencer » pour une personne, la skill (noyau et `CHARGE`) pour un agent, arrêt à la proposition ; réécriture en R12 (C39) |
| — | `build_distributions.sh` | Dans l'export Local, `](../../README.md` devient `](../README.md` pour la skill, QUICKSTART et le README officiel (C23) |
| H | CHANGELOG | Entrée « Façades (audit progressif, unité 4b) » |

**Nouvel exemple (E1).**
- **Demande :** un atelier de réparation de vélos, « rien d'autre ».
- **Prise de brief :** la personne est présente, les demandes partent avant le build. Elle répond avec deux photos, sans tarifs ni horaires.
- **Réponse visible :** elle porte l'alternative écartée (la grande photo suivie de trois cartes de services) et l'action principale fonctionnelle avec un numéro d'exemple (D-25).
- **Trace légère :** six lignes, celles d'ACTION. On y trouve notamment :
  - la thèse : délai annoncé → tableau de l'atelier → le tableau remplace la photo ;
  - la trame modale, nommée puis rompue ;
  - le plafond et les contenus marqués.

## 3. Gardes (`validate_structure.py`)

- **10 résumés fidèles :**
  - QUICKSTART ×5 : suites, sortie, one-shot, agent, classement ;
  - READING_MAP, README, flux, HANDOFF, note des exemples.
- **2 vocabulaires retirés :** « Établissez le mode » ; « Forme courte LITE non persistante ».
- **Garde FAC-01 (nouvelle) :**
  - 6 lignes de table : Mode, Run, Trace légère, Livraison, Agent contrôlé, Décision suffisamment établie ;
  - section de l'exemple : trace légère, prochaine preuve, aucune boulangerie ;
  - liens vers « Commencer » dans le README officiel et le QUICKSTART, et titre cible présent ;
  - note historique des notes de version.

## 4. Résultats sur copie

- **Gardes :** rouges avant (23 erreurs), vertes après. **Mutations :** 21/21 rouges.
- **Suivi :** VERT. 389 cas, aucune migration, `validate_all` vert.
- **Build Local :** lien réécrit en `../README.md#commencer`, cible « ## Commencer » présente.
- **Mesures :** chemin prescrit 13 774 → 13 785 mots ; noyau 4 541 → 4 552 ; doublons 142 (inchangé) ; négations 817 → 820.

## 5. Écarts et points à valider

- **Corrections faites pendant la préparation.**
  - La garde des notes de version restait verte avant le patch : le mot « historique » figurait déjà ailleurs dans le fichier. Elle exige désormais la note exacte.
  - Ma première rédaction de Q4 recopiait le résumé R5b-1 du CHANGELOG, ce qui ajoutait 2 doublons. Elle est reformulée en renvoi : doublons revenus à 142.
- **Point à valider : README, exemple de reformulation.** L'entrée humaine du README (« trop froid pour une boulangerie ») garde le domaine boulangerie. Elle est lue par des personnes, pas par l'agent (AUD-10). Elle fait partie de l'entrée validée en R6b-1. Je propose de la laisser, sauf avis contraire.
- **Point à valider : C33, lieu de la définition.** « Livraison » est définie dans le GLOSSAIRE et la ligne du noyau, pas dans les absolus (décision 8 : lois inchangées).
- **Effet sur l'usage :** non observé (pas d'observation novice ni de run).

## 6. Application et contrôles finaux, sur le package

- **Application :** 26 entrées et deux fichiers remplacés ; noyau recompilé et conforme.
- **Gardes :** vertes. **Mutations :** 21/21 rouges.
- **Suivi :** VERT. 389 cas, aucune migration, `validate_all` vert ; cliquets : 13 785 mots, négations 820, doublons 142, une liste.
- **13.01, par sous-contrôle :** texte 6/6 ; mutations 6/6 ; non-régression 5/5 ; distributions 9/9 (Linux, Python 3.10 et 3.13, archives construites depuis une copie, pas de CI hébergée). Le lien du README officiel dans l'export Local est `../README.md#commencer`.
- **13.02 :** 38/38. **Sondes AP1 et AP4a :** vertes. **B01 :** 218/218.
- **Effet sur l'usage :** non observé.

