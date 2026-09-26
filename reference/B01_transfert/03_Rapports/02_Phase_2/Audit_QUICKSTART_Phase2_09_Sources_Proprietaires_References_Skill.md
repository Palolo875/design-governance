# DG-AUDIT-001 — Phase 2 — QUICKSTART, bloc 9

## Périmètre, reprise et intégrité

- Source : `audit_work/package/V1/official/QUICKSTART.md`, **lignes 302–313**, section 12 « Sources propriétaires » et ligne finale vide ; dernière plage du fichier. Les blocs 1–8 couvrent 1–301 et le bloc 8 a été revérifié avant cette lecture.
- Méthode : protocole externe v2.0 §12, passages A–D ; plan maître et checkpoint transversal des cinq propriétaires relus. Diagnostic de la **façade** uniquement, sans patch normatif, décision globale ni épreuve utilisateur réelle.
- Baseline B01 stable, SHA-256 revérifiés : compilation `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d` ; protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; QUICKSTART `c3334f12447c6dab8ac8794f5817ae52788ff06d8eff0e8d7e2d92fe7319bcde`. Les cinq sources normatives sont conformes aux empreintes B01 du checkpoint transversal.
- Interfaces vérifiées : `V1/official/README.md` 17–39 ; `DIRECTION/START` 119–144 ; `ACTION/HANDOFF` 23–35 et `/ROUTING` 870–887 ; `SAVOIR/READ` 34–40 ; `BIBLIOTHEQUE/READ` 70–86 ; `CHANGELOG` 23–42 ; `READING_MAP` 11–20 et 78–95 ; `skills/design-governance-practice/SKILL.md` 8–43 ; README du package 79–86. Les références de la skill sont contrôlées quant à leur existence et rôle annoncé, sans auditer ici leur contenu détaillé.

## Passage A — architecture visible et chemins

Le titre 302 annonce les propriétaires ; le tableau 304–310 présente cinq besoins et cinq liens relatifs vers les sources normatives ; la phrase 312 prescrit le chargement sélectif et renvoie aux exemples, au flux et à la projection machine de la skill pratique. Le fichier se termine en 313, ligne vide. Cette sortie est cohérente avec l'avertissement 5 : le QUICKSTART oriente, il ne crée pas d'autorité.

**Test des cinq liens relatifs.** Extraction des cinq URL Markdown des seules lignes 302–313 ; résolution depuis `V1/official/QUICKSTART.md` ; cinq fichiers distincts, cinq fichiers réguliers présents à leurs chemins respectifs : `./DIRECTION.md`, `./ACTION.md`, `./SAVOIR.md`, `./BIBLIOTHEQUE.md`, `./CHANGELOG.md`. Ce test démontre la navigation vers les fichiers de ce package source ; il n'établit ni la résolution de chaque route interne par `read_route.py` (F-DIR-028), ni la parité des deux distributions, qui seront examinées à leurs unités prévues.

**Renvoi à la skill.** Les quatre fichiers `references/examples.md`, `references/flow.md`, `references/machine_projection.md` et `references/canonical_minimum.md` existent dans `skills/design-governance-practice/`. La skill 40–41 affecte respectivement exemples, aperçu du flux, projection structurée, et minimum de secours/clarification ; elle maintient la priorité canonique en 10–12. Le QUICKSTART ne donne dans son propre texte ni chemin ni lien vers `SKILL.md` ou ses références. Le README du package 84 indique le dossier de la skill et rétablit une voie **si le lecteur retourne à la racine du package**. L'existence des fichiers et leur découverte depuis un guide ouvert seul sont deux propriétés distinctes.

## Passage B — contrat sémantique, propriété et limites

| Ligne / besoin de 304–310 | Contrat propriétaire confronté | Ce que la façade permet de conclure |
|---|---|---|
| 306, classification, absolus, direction | `DIRECTION/START` 121–125 et 129–144 est la classification normative unique ; DIRECTION possède cible et protection du risque. | Attribution correcte ; une table du QUICKSTART ou de READING_MAP ne reclassifie pas. Les locators internes nécessitent toujours leur titre exact. |
| 307, trace, preuve, gates, verdict, clôture | `ACTION` 3–7 et HANDOFF 23–35 possèdent ces sorties ; ACTION/ROUTING 870–885 déclenche les autres propriétaires selon risque. | Attribution correcte ; un lien valide ne prouve pas un run observé, ni un verdict accepté. |
| 308, craft, contenu, contexte, sources, intégrité | `SAVOIR` 3–11, 34–40 porte jugement et routes spécialisées, sans fabriquer un PASS d'usage. | Attribution correcte ; une aide de jugement n'est pas une nouvelle classification ni un gate. |
| 309, support, grille, scène, objet, composants | `BIBLIOTHEQUE` 3–13 et READ 70–86 portent sélection structurelle, compatibilité et héritage possible. | Attribution correcte ; tous les runs ne requièrent pas une nouvelle structure ou un composant. |
| 310, état du package, changements partagés | `CHANGELOG` 23–42 porte autorité de maintenance, statut des routes, compatibilité et décisions durables avec la source concernée. | Attribution correcte ; le fichier n'autorise pas à lui seul une modification de DIRECTION/ACTION/SAVOIR/BIBLIOTHEQUE. F-CHG-001 sur seed/PILOT persiste. |
| 312, charge conditionnelle | `DIRECTION/START` 125 classe avant chargement, `ACTION` 21/35 et 870–885 appelle preuve et autres routes lorsque le risque l'exige ; READING_MAP 11–20 reste dérivé. | Lire *la source détaillée utile* après classification, pas supprimer START ou les obligations ACTION d'un run sous prétexte de lecture courte. |
| 312, références de la skill | Skill 10–12, 40–43 : aides conditionnelles subordonnées aux cinq propriétaires ; sa référence machine accompagne le schéma/validateur et ne s'y substitue pas. | La présence de la skill n'ajoute ni sixième source normative, ni preuve d'observation, ni permission de clore. La phrase de 312 ne nomme pas le chemin d'accès. |

Le champ « sources » en 308 concerne aussi les ancres et claims traités par SAVOIR ; il n'autorise pas à faire de ses heuristiques une preuve ACTION. En 312, la lecture sélective est une économie conditionnelle de documentation, jamais une exemption d'une protection applicable. Les cinq chemins directs ouvrent des **fichiers**, pas forcément chaque sous-route par la CLI : l'échec outillé de certains locators est déjà inscrit sous F-DIR-028/F-ACT-001 et ne crée pas un nouvel ID ici.

## Passage C — quatre usages sous contrainte

| Lecteur / situation | Chemin cohérent depuis cette section | Épreuve ou limite observable |
|---|---|---|
| Agent, brief flou et risque de permission | Ouvrir DIRECTION/START puis ACTION pour préconditions, autorité, preuve et sortie ; ajouter SAVOIR/CONTEXT selon décision. | Le « uniquement si » de 312 ne permet pas d'ignorer START ou ACTION. Un fichier atteint ne garantit pas que la route citée se résout par CLI. |
| Designer, correction locale sans décision structurelle | START classe le delta, ACTION porte preuve et clôture ; SAVOIR et BIBLIOTHEQUE sont chargés seulement si le jugement ou la structure change. | La règle 312 protège le coût de lecture ; pas de grille supplémentaire pour remplir un rituel. |
| Mainteneur, règle ou composant partagé | CHANGELOG pour cycle de vie, ACTION/RUN-SYSTEM pour consumers, version et preuve, propriétaire concerné pour la règle ; BIBLIOTHEQUE/COMPONENTS si un composant/contrat structurel est réellement touché. | La cellule 310 est un aiguillage ; elle n'attribue pas au seul CHANGELOG le contenu d'une règle métier ou visuelle. |
| Nouveau lecteur arrivant directement sur QUICKSTART, cherchant un exemple ou la projection | Suivre le renvoi 312 vers la skill ; sans le chemin, chercher le README racine, puis `skills/design-governance-practice/SKILL.md` et sa référence pertinente. | Les fichiers existent et leur fonction est décrite par la skill, mais 312 seul ne permet pas de les ouvrir en un clic ni d'identifier lequel choisir. Ce surcoût est une hypothèse d'usage à éprouver, non un échec observé auprès d'un lecteur. |

## Passage D — résistance, déduplication et constat local

### F-QS-004 — renvoi final aux références de la skill sans adresse ni aiguillage direct

- **Gravité provisoire : mineur à éprouver.** Le texte a un lecteur possible qui n'a que QUICKSTART sous les yeux ; le package complet offre un chemin indirect. L'effet réel sur le choix et l'ouverture des références n'a pas été mesuré.
- **Preuve :** QUICKSTART 312 nomme exemples, flux et projection machine sans chemin ni lien de skill, alors que les cinq renvois propriétaires 306–310 sont directement ouvrables ; la recherche `skill` dans QUICKSTART ne trouve que la ligne 312. Le README racine 84 nomme `skills/design-governance-practice/`, et la skill 40–41 résout les quatre références. Aucune référence n'est absente dans la source inspectée.
- **Effet possible :** le lecteur isolé abandonne l'aide annoncée, cherche au mauvais endroit, ouvre toute la skill par défaut, ou consulte une projection sans retrouver la source ACTION et son validateur. Ces effets restent hypothétiques et devront être cherchés dans une tâche de navigation, pas déclarés avérés.
- **Propriétaire pressenti :** façade QUICKSTART pour l'aiguillage visible ; README racine et skill restent des interfaces à confronter lors de leurs audits. La solution éventuelle devra rester utilisable dans les formes de distribution pertinentes et respecter le chargement conditionnel ; aucune formulation n'est décidée en phase 2.
- **Test discriminant :** à partir du QUICKSTART ouvert seul puis à partir du README racine, demander de retrouver `examples.md` après un parcours ambigu, `flow.md` pour le flux, `machine_projection.md` pour une RUN_CARD structurée et la source canonique ACTION ; mesurer chemin, erreurs et ouvertures superflues. Vérifier ensuite les deux distributions avant toute correction de chemin relatif.
- **Déduplication :** F-DIR-028 désigne la résolution des routes documentaires par `read_route.py` ; F-ACT-001 le chargement du propriétaire ; F-QS-001 la suractivation selon mode ; F-QS-004 concerne l'**adresse absente d'un renvoi vers des références pourtant existantes**. Si le checkpoint QUICKSTART montre que l'entrée racine suffit dans tous les usages visés, retirer ou réduire cette fiche avec justification.

**Occurrences sans ID supplémentaire :** portée seulement documentaire des cinq liens (F-DIR-028), maintien des propriétaires lors d'un run partagé (F-DIR-046/F-CHG-001), condition START/ACTION pendant un chemin court (F-ACT-001/F-QS-001), frontière entre projection machine et preuve observée (F-ACT-014/023/038/039). Les cinq attributions d'owner sont conformes ; aucune autorité supplémentaire n'est inférée de la skill. Le registre monte à **105 fiches provisoires** : 101 propriétaires et F-QS-001 à F-QS-004 ; ce nombre n'est ni un nombre de défauts produits démontrés ni une quantité de patches décidée.

## Sortie et prochaine unité

Les lignes 302–313 ferment la lecture sectionnelle de **QUICKSTART.md, 1–313/313, neuf rapports**. B01 est stable ; cinq liens résolus vers cinq sources, références de skill existantes, propriété et chargement conditionnel confrontés ; F-QS-004 est à confirmer ou retirer à l'épreuve. **Prochaine unité distincte : checkpoint de façade QUICKSTART** : contrôler continuité des neuf plages et les quatre fiches F-QS, dédupliquer les occurrences héritées, confronter le guide dans son ensemble aux cinq propriétaires, préserver les points positifs et donner une cible précise pour READING_MAP. Aucune phase 3, correction normative ou conclusion globale n'est ouverte par la seule fin de ce guide.
