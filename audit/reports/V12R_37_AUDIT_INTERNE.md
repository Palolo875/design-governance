# V1.2 — Audit interne A1 : opérationnel, hiérarchie, organisation, usage, exploitation, cohérence, efficacité

**Date :** 30-09-2026 · **Demande de l'owner :** audit interne des fichiers importants sur le plus grand périmètre possible : opérationnel, points faibles, bonne exploitation, hiérarchie, organisation et architecture, usage et lecture, efficacité.
**Candidate :** `package/` à `042e6dc` (après D-25). **Aucune modification de `package/`.** B01 218/218.

**Statut : auto-audit** (l'auteur de la refonte s'audite lui-même). Ce n'est pas un regard D3, et aucun verdict d'efficacité n'est posé.

## 1. Méthode et périmètre

| Couverture | Fichiers |
|---|---|
| **Lu en entier** | `SKILL.md` (noyau compilé), `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `references/canonical_minimum.md`, `references/flow.md` |
| **Lu en partie** | `BIBLIOTHEQUE.md` : entrée, READ, TENSION, SIGNATURE, SELECT, DERIVE, CONTRACTS, GATE, EVOLUTION, test de sortie (catalogue SUPPORT à COMPAT survolé). `references/examples.md` (LITE, deux DIRECTION). `QUICKSTART.md` (en-tête, parcours commun, carte des sections). README Local généré (bloc d'entrée et constitution). `scripts/validate_structure.py` (gardes FIDELITY et chargement) |
| **Contrôlé par machine ou recherche ciblée** | READING_MAP, GLOSSAIRE, CHANGELOG, RELEASE_NOTES, README officiel, ORCHESTRATION_MAP, `machine_projection.md`, schémas, fixtures, validateurs (`validate_all` complet sur copie : 82 cas unitaires, fixtures, build GitHub et Local, reproductibilité) |
| **Exploitation réelle** | Journaux des 6 producteurs de R10 : routes lues, lignes de règles (M4), traces laissées, vocabulaire des gestes |
| **Démarrage à froid** | Les deux distributions décompressées hors du dépôt : `read_route`, chemins cités par la skill, README Local, workflow CI |

**Grille de chaque constat :** lieu, preuve, gravité (bloquant, notable ou mineur), certitude (certain, probable ou hypothétique), proposition. **Aucun bloquant trouvé.**

## 2. Verdict par axe

| Axe | Verdict | Preuve principale |
|---|---|---|
| **Opérationnel** | **Tenu (certain).** | `validate_all` vert sur copie (build, reproductibilité, 82 cas). Distributions GitHub (62 fichiers) et Local (58) utilisables à froid : `read_route` fonctionne, chemins de la skill réécrits pour le Local. README Local généré avec l'entrée et la constitution. CI épinglée en Python 3.11 (exécution hébergée toujours non observée) |
| **Hiérarchie** | **Tenue dans les principes, affaiblie dans le placement.** | Propriétaires clairs et répétés. Mais des obligations placées où l'agent ne lit pas (AUD-02), et un reste contradictoire sur l'ancre (AUD-03) |
| **Organisation / architecture** | **Partiellement tenue.** | « Une chose, un lieu » vaut pour les concepts gardés. Il est rompu pour le chargement : 4 prescriptions concurrentes de `CHARGE` (AUD-01). Les façades opérateur n'ont pas suivi la refonte (AUD-06) |
| **Usage / lecture** | **Chemin agent court et suivi.** Chemin opérateur en retard. | Agent : skill + environ 10 routes, soit 466 à 665 lignes de règles (R10). Humain : entrée « Commencer » claire. Opérateur : QUICKSTART sans trace légère, sans checkpoint, sans noyau |
| **Exploitation** | **Le noyau et `CHARGE` sont exploités** (certain) ; **SAVOIR et BIBLIOTHEQUE ne le sont presque pas** (certain en R10). *(erratum AP2, C34 : voir §Erratum)* Les gestes restent **inobservables** (AUD-05). | Les agents C3 de R10 ont lu exactement la ligne DIRECTION de `CHARGE`, et aucune route SAVOIR ni BIBLIOTHEQUE. Les agents C4 (V1.1.1) ont lu `SAVOIR/TYPE`, `CFT-00` et `TENSION`, et laissé une trace riche |
| **Cohérence** | **Bonne sur les concepts gardés ; restes hors gardes.** | 5 constats de cet audit sont invisibles aux gardes (AUD-16) |
| **Efficacité** | **Non établie, par principe (auto-comparaison).** | Voir §4 |

## 3. Constats

### Notables

| ID | Constat | Lieu et preuve | Certitude | Proposition |
|---|---|---|---|---|
| **AUD-01** | **Quatre prescriptions de chargement concurrentes de `CHARGE`**, présentée comme « seule liste de chargement » | DIRECTION §2 « Déclencheurs critiques » (`[FORCÉ]` : `SAVOIR/CRAFT/CFT-03`, `STATE`, `INTEGRITY`) ; ACTION « Carte de lecture par mode » (`STATUS`, `PRECONDITION`, `PIPELINE-DIRECTION`, `VISUAL_PROOF` pour le mode DIRECTION) ; `ACTION/ROUTING` (« Spec DIRECTION » : `CRAFT`, `TYPE`, `SOURCE`) ; ACTION « Responsabilité » (« commencez par STATUS et PRECONDITION »). La garde ne détecte une liste que par l'en-tête « \| Mode \| Charger d'abord », d'où l'échappement. En R10, les agents C3 n'ont suivi que `CHARGE` | Certain | Décision : faire des trois tables des renvois à `CHARGE` (déclencheurs conditionnels regroupés dans sa colonne « Ajouter seulement si ») ; élargir la garde aux tables « par mode » |
| **AUD-02** | **Obligations sans lecteur.** SAVOIR porte 11 `[REQUIS PAR LE MODULE]`, dont 6 visent toute surface DIRECTION ou identitaire : `CFT-03`, `CFT-05`, `TYPE`, `STATE`, `SOURCE`, `INTEGRITY` avant verdict. Aucune n'est sur le chemin de `CHARGE` | En R10, aucune route SAVOIR n'est lue par C3. Le noyau couvre une partie (grammaire de composition, question de convergence, titre, texte sur image) | Certain (placement) ; probable (effet) | Décision : compiler l'essentiel manquant dans le noyau, ou requalifier en conditionnel ce qui ne l'est pas déjà |
| **AUD-03** | **Reste de R7-2 : `FAIL-ASSUMED` pour une ancre absente** | ACTION, pipeline étape 4 : « Sans ancre utile et spec exploitable… `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` ». Contraire à `ANC-01`. La garde R7-3 est bornée aux formules « ancre absente » et « ancre manquante » | Certain | Raccord : retirer `FAIL-ASSUMED` de cette liste (échec connu seulement) ; étendre la garde à « sans ancre utile » |
| **AUD-04** | **Persistance ou clôture sans condition de trace**, hors des routes corrigées en R11c | DIRECTION : « Les runs `STANDARD`, `DIRECTION` et `SYSTÈME` conservent une trace persistante ». `ACTION/FAST-PATH` : « clôture avec la forme courte LITE ». BIBLIOTHEQUE, sélection par mode et test de sortie 8 : persistance dans la `RUN_CARD`. `flow.md` : « Décider et fermer » pour tout run. `examples.md` : tous les exemples finissent en `CLOSED`. Contraire à `TRA-01` | Certain | Raccord : conditionner à la trace complète, comme R11c |
| **AUD-05** | **Trace légère sans lieu** | `TRA-01` fixe le contenu (six lignes), pas le lieu (réponse ou fichier). En R10, la consigne limitait la réponse : les agents C3 n'ont laissé **aucune** trace. L'usage des gestes (test de trame, deux voix typographiques, alternative) est donc inobservable, et la reprise `ITER` depuis une « ligne de thèse » devient fragile | Certain | Décision : dire où vit la trace légère (fin de réponse, ou fichier à côté de l'artefact quand l'agent écrit des fichiers) |
| **AUD-06** | **Façades opérateur non mises à jour** | « trace légère » : 0 occurrence dans QUICKSTART, READING_MAP, README, RELEASE_NOTES, `flow.md` et `examples.md` ; « checkpoint » : 0 dans les mêmes, et 1 seule dans le GLOSSAIRE. QUICKSTART propose encore « fermer » comme suite ordinaire. Aucun exemple du parcours par défaut | Certain | Lot façades : QUICKSTART, `flow.md`, un exemple en trace légère, READING_MAP |
| **AUD-07** | **La convergence de concept n'est pas visée** | La question de convergence porte sur la palette et la police. En R10, le même concept apparaît dans toutes les conditions : fournées et heure de sortie du four (B-DLA) ; facture tamponnée et même nom « Soldé » (B-SAAS). Les leviers qui pourraient l'ouvrir (`SAVOIR/STYLE`, dials, `CFT-04a`) sont hors du chemin | Probable | Décision : étendre la question de convergence à l'objet et au concept central (« l'objet que n'importe quel modèle choisirait »), sans prescrire d'écart |
| **AUD-08** | **Exemple de la skill dans le domaine du brief de référence** | `examples.md`, « fabrication depuis un brief flou » : boulangerie, « vitrine du jour… heure de sortie du four ». C'est le concept convergent de R10. Aucun agent de R10 ne l'a lu : pas la cause (certain). Risque d'ancrage et de contamination d'une épreuve B-DLA future (probable) | Probable | Changer le domaine de l'exemple |
| **AUD-09** | **Règle CTA sans renvoi à `CNT-01`** | `DIRECTION/FIRST-OBJECT`, lue par tous les agents C3 : « Un CTA doit… mener à une action réellement disponible, soit déclarer sa limite ». Cause probable de D-25 : retirer plutôt que marquer. La correction D-25 est dans `CNT-01` seulement | Probable | Raccord : un renvoi « valeur d'exemple marquée (`CNT-01`) » dans la règle CTA |

### Mineurs

| ID | Constat | Certitude |
|---|---|---|
| AUD-10 | DIRECTION se dit « seul document de cadrage chargé au démarrage » et invite à « utiliser READING_MAP » ; `flow.md` renvoie l'agent à READING_MAP. La skill dit que ces lectures sont humaines | Certain |
| AUD-11 | Méta-structure redondante : au moins 8 énoncés de propriété dans DIRECTION ; les cinq absolus arrivent après les routes | Certain |
| AUD-12 | « Livraison » (absolus 1 et 3) et « proposition » (`TRA-01`) ne sont pas distingués | Probable |
| AUD-13 | Deux formes légères coexistent : la « forme courte LITE non persistante » et la trace légère | Probable |
| AUD-14 | Signal de veille P1 (Archivo) périmé ; le signal R10 (même grotesque de titre dans toutes les conditions B-SAAS) n'est pas consigné | Certain |
| AUD-15 | Entrée humaine : la phrase « retenir pour un vrai produit » est répétée entre les questions 3 et 4 | Certain |
| AUD-16 | **Portée des gardes.** Elles protègent ce qui a été écrit (présence de phrases, en-têtes, balises), pas l'absence de contradiction ailleurs. AUD-01, 03, 04, 09 et 10 leur échappent | Certain |

## 4. Efficacité : ce que les preuves permettent d'affirmer

| Source | Constat | Nature |
|---|---|---|
| B-DLA (V1.1.1) | Qualité proche de C1 ; plus honnête | Auto-comparaison |
| P1 (V1.2 après R4) | C3 bat C1 8/8 ; mêmes juges modèles | Auto-comparaison |
| R10 exploratoire | C3 ne perd aucune paire tranchée (accord 50 %) ; adéquation 7,0 contre 4,75 pour C1 ; 0 fait inventé non signalé au sens de P-2 (fonctions d'un produit fictif hors marquage, D-26), contre environ 5 à 6 pour C1 ; coût 1,7 à 1,8 × C1 et au plus celui de C4 ; convergence intacte | Auto-comparaison, juges d'une seule famille |

- **Probable :** le système améliore l'honnêteté et l'adéquation au besoin.
- **Hypothétique :** il améliore la qualité visuelle perçue.
- **Certain :** aucune preuve indépendante ; efficacité `NOT-VERIFIED`.

## 5. Ce qui est solide (certain)

- La chaîne de validation, le build reproductible et les deux distributions utilisables à froid.
- Le noyau lu à chaque run, et `CHARGE` suivi à la lettre par les agents.
- Le marquage des exemples, robuste dans les deux systèmes.
- La règle d'ancre (`ANC-01`), cohérente entre DIRECTION, SAVOIR et le noyau, à AUD-03 près.
- SAVOIR et BIBLIOTHEQUE : contenus riches et cohérents sur statuts, preuves et honnêteté ; aucune contradiction trouvée dans leur propre périmètre, hors placement (AUD-02).
- L'entrée humaine en quatre questions : claire, sans mode ni jargon.

## 6. Proposition de suite (décisions de l'owner)

1. **Raccords sans arbitrage** (petit lot, PATCH-DECISION) : AUD-03, AUD-04, AUD-09, AUD-10, AUD-14, AUD-15, avec leurs gardes.
2. **Décisions d'architecture :**
   - AUD-01 : une seule liste de chargement réelle ;
   - AUD-02 : obligations SAVOIR dans le noyau, ou conditionnelles ;
   - AUD-05 : lieu de la trace légère.
3. **Façades et exemples :** AUD-06, AUD-08, AUD-13.
4. **Convergence :** AUD-07. C'est une question de fabrication : son effet ne s'établit que par un run, que l'owner a arrêté.

AUD-16 est une limite de méthode, à garder en tête pour les gardes à venir : une garde de propriété ne remplace pas une relecture croisée.

## Erratum (01-10-2026, unité AP2 de l'audit progressif externe)

**C34, exploitation de SAVOIR et BIBLIOTHEQUE.**
- **Ce qui était faux :** « ne le sont presque pas » confondait deux choses, une route non ouverte et un contenu non disponible.
- **État du noyau lu par les agents C3 de R10** (commit `64265da`) : il compilait 39 blocs.
  - 16 venaient de SAVOIR et 4 de BIBLIOTHEQUE ;
  - les 19 autres venaient de DIRECTION (15) et d'ACTION (4).
- **Formulation exacte :**
  - les agents C3 n'ont pas ouvert séparément de route SAVOIR ou BIBLIOTHEQUE (traces de lecture déclarées par les agents, `traces_R10.json`) ;
  - 20 blocs de ces deux sources étaient disponibles dans le noyau qu'ils lisaient (certain) ;
  - que leurs gestes aient été appliqués n'est pas attesté.
- **Conséquence pour A2 (`V12R_39`) :** les planchers couleur et typographique qu'A2 a compilés ne figuraient pas parmi ces 39 blocs. A2 garde son objet, mais sa justification (« obligations SAVOIR hors du chemin ») était surestimée pour le reste de SAVOIR.
- **Effet d'A2 :** non observé.

