# DG-AUDIT-001 — Phase 2 — `canonical_minimum.md` : limites, statuts et priorité

**Date :** 24 septembre 2026. **Baseline :** B01. **Profondeur :** TARGETED ; lecture complète A–D **1–25/25** de `skills/design-governance-practice/references/canonical_minimum.md`, SHA-256 `60d1d25354037cdf6e7b956e1df59e7571c91732edf55d71323606a6a79df3ac`. Système compilé `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole v2.0 `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`, skill parente `2d2734eb13527563698542303682d204a3174b987adbb9ac02d795cf31687853` et flux précédent `4202c8e270384ca976a70dafe2a734e11b8c2a8d75d8d6e5772387a4ee5577ee` revérifiés. Plan, `Audit_Reference_Flow_Phase2_01_Branches_Critiques_Preuve.md` et le rapport de la skill rouverts. Aucun patch B01.

## Passage A — architecture visible, 1–25

| Lignes | Rôle |
|---|---|
| 1–3 | Titre « canonique minimal », immédiatement borné : aide-mémoire, aucune substitution aux fichiers V1. Le titre ne confère pas d'autorité normative. |
| 5–7 | Source absente : déclarer l'indisponibilité, ne pas inventer les définitions ; proposition créative seulement hypothétique et jamais qualifiée de run V1 conforme. |
| 9–20 | Huit séparations de vocabulaire, suivies d'une limite générale sur les preuves tirées d'une rationale, capture ou référence. |
| 22–25 | Charger les sources V1 dès qu'elles reviennent ; résoudre toute divergence en faveur des propriétaires. |

La skill mère 36/41/148 rend cette référence conditionnelle lorsque les sources sont momentanément indisponibles ou qu'il faut vérifier rapidement une distinction de termes. Les chemins relatifs depuis la skill résolvent vers ce fichier ; dans une copie temporaire isolée, le build retourne **0** et fournit **25 lignes, octets identiques** dans GitHub (`skills/design-governance-practice/references/`) et Local (`skill/references/`). La réserve de chemin F-SK-002 concerne les cartes officielles citées dans la skill, pas ce lien relatif.

## Passage B — contrat sémantique et sources propriétaires

| Aide-mémoire | Concordance vérifiée | Limite de la compression |
|---|---|---|
| 11, cinq `MODE` | `DIRECTION/START` 127–140 classe selon l'objet direct et protège le risque critique. | Énumérer les noms ne permet ni de classer un cas ambigu ni de reclassifier après risque critique. |
| 12, `STATE` / `ISSUE` / `VERDICT` / direction | `ACTION.md` 263–280 et `GLOSSAIRE.md` 33–36 séparent cycle, issue, verdict global et fidélité de direction. | Le mémo ne donne ni valeurs admissibles, ni ordre des transitions ; il interdit justement de les inventer. |
| 13, `A/B/C` / `V/U/A/T` | `ACTION.md` 37–50 et 170–202 attribuent contrôle et axes à des registres distincts. | L'applicabilité d'un contrôle dépend du mode et du risque, non du seul nom de gate. |
| 14–15, intention / changement | `ACTION.md` 236, 269–270 et `GLOSSAIRE.md` 37–38 exigent une décision **changée, confirmée ou abandonnée par observation**. | « Conséquence réellement observée » 15 est un raccourci : une observation sans effet sur la décision ne vaut pas automatiquement `DECISION-CHANGE`. Propriétaire et skill 67 clarifient ; point à surveiller dans les exemples, sans nouvel ID ici. |
| 16, `NOT-VERIFIED` | `ACTION.md` 284–299 et `GLOSSAIRE.md` 41 : contrôle requis sans preuve appropriée au scope et aux capacités. | Ce terme borne un claim ; il n'est ni issue ni autorisation de clôture favorable. |
| 17, `NOT-OBSERVED` | `ACTION.md` 226–236 et `GLOSSAIRE.md` 42 : conséquence attendue non vue malgré le scope d'observation déclaré. | Le distinguer d'un contrôle non exécuté, qui demeure `NOT-VERIFIED` si requis. |
| 18, `N/A-JUSTIFIED` | `GLOSSAIRE.md` 43 et `ACTION/HANDOFF` 23–33 couvrent contrôle ou preuve réellement non applicable avec justification. | « Absence de conséquence applicable » résume une des raisons possibles ; consulter le propriétaire pour décider si un contrôle est hors scope. |
| 20, éléments qui ne prouvent pas à eux seuls | `ACTION.md` 234/329–331 borne méthode, artefact, scope, résultat et prochaine preuve. | Une capture peut soutenir le rendu observé mais ne démontre pas à elle seule l'usage ni le runtime non inspectés. |

**Interface avec le flux précédent :** `flow.md` 13–14 mène à la protection de niveau et à `NOT-VERIFIED` sans arcs de reprise. Les distinctions 11/16 du présent mémo empêchent une confusion de termes, mais ne fournissent toujours ni route de reclassification, ni owner, ni `NEXT-PROOF` pour ces branches. **F-FLOW-001 reste entier** ; les règles d'`ACTION` et de `DIRECTION` fournissent les suites applicables. La liste longue/courte de handoff F-SK-001 n'est pas ici résolue : le mémo n'est pas un contrat de sortie.

## Passage C — lecteurs simulés

| Situation | Lecture utile de la référence | Ce qui exige le propriétaire |
|---|---|---|
| Skill présente seule, sources V1 indisponibles | Signaler la limite ; proposer une piste explicitement hypothétique sans déclarer un run conforme. | Reprendre `DIRECTION/START` et les obligations applicables lorsque les sources reviennent. |
| Capture mobile faite, test avec lecteur d'écran requis mais absent | `NOT-VERIFIED` sur la preuve d'accessibilité ; la capture ne la remplace pas. | `ACTION` décide verdict, issue, owner et prochaine preuve. |
| Action observée, mais effet attendu non constaté | `NOT-OBSERVED` décrit l'effet attendu ; ne pas déclarer `DECISION-CHANGE` sans décision réellement changée, confirmée ou abandonnée. | `ACTION` borne le scope et la conséquence pour le run. |
| Contrôle réellement hors périmètre | Justifier `N/A-JUSTIFIED`, sans en faire une dispense de confort. | `ACTION`/propriétaire détermine si le contrôle est réellement non applicable et conserve la trace suffisante. |

Ce sont des **cas de lecture**, pas des tests avec participants ni des verdicts produits.

## Passage D — résistance et registre

**Résistance éprouvée :** source absente sans faux claim, capacité de preuve absente sans `PASS`, absence d'effet observé distincte de l'absence de contrôle, non-applicabilité justifiée distincte d'une preuve requise manquante, réouverture des sources dès leur retour. Le document se décrit comme non normatif, préserve les huit séparations et interdit d'attribuer automatiquement une preuve à une capture ou une rationale. Les raccourcis des lignes 15/18 sont **des observations de formulation** qui demandent recoupement dans les exemples ; ils ne justifient pas à ce stade un constat indépendant, car `ACTION` et le glossaire donnent les définitions complètes et sont explicitement prioritaires (3/24).

**Constats transportés :** F-FLOW-001 non résolu pour les branches sans suite figurée ; F-SK-001 toujours sur la portée du handoff ; F-SK-002 déjà borné aux chemins officiels, non reproduit dans le lien de cette référence. **Aucun nouvel ID** et **152 fiches provisoires** maintenues. Aucune gravité finale, correction normative ou conclusion système.

**Prochaine unité :** `skills/design-governance-practice/references/examples.md` **1–90/90**, lecture A–D des parcours `LITE`, `DIRECTION` et `SYSTÈME` ; vérifier particulièrement la chronologie intention/observation/décision, le traitement des preuves manquantes et la charge de `BIBLIOTHEQUE/COMPONENTS`, puis poursuivre par `machine_projection.md` et les autres sources de phase 2.
