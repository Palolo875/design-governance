# DG-AUDIT-001 — Phase 2 — `validate_all.py` : orchestration, oracles et distributions

## Unité, sources et limites de preuve

**Cible :** `scripts/validate_all.py`, 97 lignes sur 97, propriétaire pressenti des appels et des oracles de la suite supérieure. **Échelle :** intra-fichier et interfaces immédiates. **Risque dominant :** annoncer un PASS sans avoir exercé la règle visée ou empêcher une exécution valide par une hypothèse de chemin. **Sortie :** diagnostic sectionnel A–D, constats provisoires, garanties et prochaine source. Le protocole externe v2.0 §12 et le plan maître actif sont les règles de méthode ; `ACTION`, `DIRECTION` et les schémas demeurent propriétaires du sens des cartes.

Sources examinées : compilation `Design_Governance_V1.0.md` (enveloppe du script lignes 7281–7381 ; contenu 7284–7380), protocole externe §12, baseline B01, checkpoint cumulatif `Audit_Validate_RUN_CARD_Phase2_Checkpoint_Consolidation.md`, rapports des quatre plages du validateur, checkpoint des fixtures, ainsi que les interfaces `validate_run_card.py`, `validate_design_governance.py`, `build_distributions.sh`, `package_manifest.json` et `.github/workflows/validate.yml` aux endroits cités. Les quatre derniers ne sont **pas** réputés intégralement audités par cette lecture d'interface.

Empreintes recalculées sur les fichiers reçus : compilation `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`, protocole `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd` ; elles correspondent à B01. La copie de travail reconstruite à partir des 60 enveloppes de la compilation correspond aux **60 nombres de lignes et d'octets** de son inventaire. `validate_all.py` y compte 97 lignes, 4 747 octets, SHA-256 `3c04c2b3ffb81be8f6f7f6e92912fa9a20150b586b78d516d4bc0dc9211919b0`. Les scripts ont été exécutés uniquement dans cette copie isolée ; les octets du corpus reçu ne sont pas modifiés. Les sources Git originales et l'exécution réelle du workflow hébergé restent non vérifiées.

## Passage A — architecture visible, 1–97/97

| Lignes | Fonction | Dépendance et décision réelle |
|---|---|---|
| 1–22 | Imports, `ROOT`, lancement de sous-processus et SHA-256 des archives. | `run` exécute depuis `ROOT` avec `check=True` ; le hash est un contrôle d'égalité d'octets entre builds, pas de justesse du contenu. |
| 24–36 | `expect_failure` : présence de la première cible `.json`, code non nul, absence de la chaîne Python `Traceback (most recent call last)`. | Aucun motif attendu ni bannière du validateur ne sont contrôlés ; la pré-vérification du chemin est relative au répertoire courant du processus appelant. |
| 38–50 | Compilation Python, quatre validateurs, route positive et négative, exemple DOMAIN_FRAME et exemple RUN_CARD. | L'ordre arrête au premier sous-processus en échec. `py_compile` crée des caches dans la copie. |
| 51–60 | Quatre fixtures RUN_CARD négatives en ciblé. | La fixture F-FIX-001, absente de la suite native, est réellement appelée ici ; le seul oracle supérieur est code non nul/absence de traceback. |
| 61–79 | Carte strictement positive construite à partir de l'exemple, puis strict placeholder, JSON malformé et fichier absent négatifs. | Le positif strict prouve un chemin admis ; il ne résout pas F-VRC-004/005 ni la disponibilité du rendu. |
| 80–93 | Si build absent : statut `LOCAL` ; sinon deux builds, calcul de deux couples de SHA-256 et comparaison. | La distribution Local omet intentionnellement le script de build. Le package complet attend ce fichier via le validateur d'inventaire lancé en premier. |
| 95–97 | Point d'entrée et code de sortie. | La CLI reflète le résultat de `main`, sauf exceptions brutes remontées par `run` ou lecture des archives. |

Le workflow fourni contient `python3 scripts/validate_all.py` sur `push` et `pull_request`, depuis la racine issue du checkout selon sa configuration. C'est un **appel déclaré** dans un fichier de workflow ; aucune exécution distante n'est déduite de cette lecture.

## Passage B — contrat et contre-épreuves

La suite sans mutation retourne **code 0** et `FULL VALIDATION PASSED` dans la copie isolée. L'appel du build produit deux archives ; chacune des deux reconstructions exécute aussi la validation de l'export Local, qui retourne `LOCAL VALIDATION PASSED`. Une invocation directe sur `dist/local` retourne code 0 et ce statut Local ; l'absence du build y est conforme à l'export. Le contrôle de reproductibilité compare les deux générations de chaque archive ; il n'établit pas à lui seul l'identité avec un dépôt Git ou l'efficacité réelle de Design Governance.

Épreuves ciblées dans la copie ou avec le module chargé depuis cette copie :

| Épreuve | Résultat observé | Interprétation |
|---|---|---|
| `expect_failure` reçoit une commande qui affiche `ERROR: unrelated rejection`, retourne 7, et cite la fixture existante `invalid_capability_profile_missing_basis.json`. | Imprime `+ expected failure (invalid_capability_profile_missing_basis.json)` ; aucun rejet de l'oracle. | Un échec sans rapport peut faire passer les quatre tests ciblés ; aucun diagnostic n'est comparé à l'invariant annoncé. |
| `python /chemin/absolu/scripts/validate_all.py` lancé d'un dossier temporaire extérieur. | Les premiers validateurs passent ; la première fixture est déclarée absente, code 1, bien qu'elle existe sous `ROOT/schemas/fixtures`. | `target.is_file()` utilise le cwd externe alors que le sous-processus est lancé sous `ROOT`. Depuis la racine documentée, ce défaut ne se manifeste pas. |
| Masquer `scripts/build_distributions.sh` dans la copie de package complète, puis restaurer le fichier. | Échec dès `validate_design_governance.py` : fichier attendu absent selon l'inventaire ; aucun `LOCAL VALIDATION PASSED`. | Le faux succès supposé du mode Local est **atténué dans cette configuration** par le contrôle préalable du package complet ; ne pas ouvrir de constat de faux PASS pour cette seule branche. |
| Lancer `validate_all.py` depuis l'export `dist/local` effectivement généré. | Code 0, `LOCAL VALIDATION PASSED`, build absent conformément à sa constitution. | La branche Local a un usage positif réel. |

La sortie des validations positives confirme leur exécution dans cette copie et ne remplace pas la lecture exhaustive des validateurs, du manifeste, du build et du workflow. Le premier essai de reconstruction a produit un échec sans portée sur B01 parce qu'il coupait les documents Markdown à leurs clôtures de blocs internes ; le reconstructeur a été corrigé avant les épreuves retenues, puis les 60 tailles et lignes ont été comparées à la baseline. Seuls les essais sur la reconstruction vérifiée sont des résultats de cette unité.

## Passage C — usage selon le lecteur

**Mainteneur/CI :** la suite protège une chaîne large et appelle F-FIX-001, mais le libellé `expected failure` ne démontre jamais la cause de l'échec. Une panne d'une étape obligatoire stoppe le pipeline ; `run` laisse toutefois `CalledProcessError` remonter en traceback après le message éventuel du validateur. Ce dernier point gêne la lisibilité, sans créer ici de faux PASS ; il reste une observation à confronter à l'interface CI.

**Intégrateur :** depuis la racine du package, l'appel documenté fonctionne. Une invocation absolue depuis un autre cwd, pourtant partiellement rendue possible par `ROOT` et `cwd=ROOT` pour les sous-processus, échoue au contrôle préalable des fixtures. La convention d'invocation doit être explicite ou ce contrôle doit employer la même racine que les sous-processus.

**Designer/reviewer et propriétaire normatif :** une carte validée structurellement ou une archive déterministe n'établit ni vérité des preuves ni qualité du premier rendu. Les protections de `valid_closed_return`, de l'exploration DIRECTION et des exemples de contrats doivent survivre aux futures réparations d'oracles.

## Passage D — constats provisoires et non-fusions

### F-ALL-001 — oracle supérieur d'échec sans motif discriminant

**Preuve :** lignes 24–36 et 45–79 ; l'essai avec fixture existante, échec 7 et diagnostic sans rapport est accepté comme échec attendu. **Impact :** les quatre fixtures négatives ciblées, la route inconnue, le strict placeholder et les deux erreurs de fichier ne protègent pas individuellement leur raison d'échec au niveau de l'orchestrateur. La suite native peut en protéger certaines : ne pas attribuer à F-ALL-001 une perte de toutes les garanties du package. **Owner pressenti :** oracle CLI de `validate_all.py`. **Gravité :** à décider en phase 10, risque provisoire significatif pour la confiance dans les tests ciblés. **Épreuve de résolution :** une entrée négative ne doit réussir que sur son diagnostic prévu ; tester en voisin un rejet pour un autre motif et préserver les vrais négatifs/positifs.

**Distinct de** F-FIX-001 (absence de cette fixture de la suite *native*), F-FIX-003 (une fixture native appelée sans diagnostic attendu), F-FIX-002 (fixtures composites) et F-VRC-006 (oracle d'autorité d'enum). Un correctif peut coordonner ces oracles sans confondre leurs comportements vérifiables.

### F-ALL-002 — vérification de fixture relative au cwd appelant

**Preuve :** ligne 27 contre `cwd=ROOT` ligne 29 ; l'invocation absolue depuis un dossier externe échoue par « fixture absente » après plusieurs contrôles positifs. **Impact :** faux échec et diagnostic trompeur dans un mode d'invocation externe ; l'appel depuis la racine documentée et le workflow déclaré ne sont pas affectés. **Owner pressenti :** résolution de chemin dans `expect_failure` / contrat d'invocation CLI. **Gravité :** mineure ou observation selon la portée officiellement retenue, à trancher en phase 10. **Épreuve de résolution :** comparer les lancements depuis la racine et un cwd externe, tout en conservant un vrai rejet pour une fixture absente.

**Aucun nouvel ID** pour l'absence du build dans le package complet : le validateur d'inventaire bloque le scénario testé. F-VRC-007/008 restent des constats du validateur RUN_CARD ; l'orchestrateur relaie son code de sortie et ne transforme pas un schéma `{}` en erreur. Les faiblesses normatives de carte gardent leurs propriétaires ACTION/DIRECTION/SAVOIR. Aucun patch ni verdict global n'est décidé en phase 2.

**Registre :** 129 fiches provisoires au checkpoint précédent, **131** avec F-ALL-001/002 ; la déduplication et la gravité finales restent ouvertes. **Prochaine cible :** lecture complète 1–229/229 de `validate_design_governance.py`, premier contrôle de `validate_all.py`, pour vérifier inventaire, modes GitHub/Local, diagnostics et résistance aux omissions ; puis `validate_contracts.py` et les autres scripts suivant leurs dépendances. Avant ce bloc, revérifier B01 et relire le protocole §12 et ce rapport.
