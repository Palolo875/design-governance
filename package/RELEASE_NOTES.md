# Release notes — Design Governance V1.1.1

**Statut expérimental :** Design Governance V1.1.1 est une expérimentation maintenue.  
**Date de la version :** 2026-09-26 (V1.0.0 : 2026-09-19)  
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Présentation

Design Governance V1.1.1 est une baseline publique pour diriger, créer, juger, construire et vérifier un travail de design. Elle aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

La release est présentée comme un système cohérent, utilisable et testable. Elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage sans preuve adaptée.

## Changements depuis V1.0.0

- **Autorité du schéma et oracles de test.** Les validateurs `RUN_CARD` et contrats refusent un schéma absent, vide, incomplet ou hors sous-ensemble, et vérifient qu’un témoin invalide est rejeté. Chaque fixture déclare son motif attendu ; chaque invariant a son cas unitaire à faute unique.
- **Contrat `RUN_CARD` migré.** Protection critique à résultat, exception `FAIL-ASSUMED` structurée, axes V/U/A/T, réserves complètes, capacité et version de la preuve, droits, paquet SYSTÈME, B1b, ancres typées, conséquence décisionnelle (`CHANGED`, `CONFIRMED`, `ABANDONED`, `N/A-JUSTIFIED`, `NOT-OBSERVED`), temps du verdict et reclassement. Profil strict : mêmes exigences par mode, locators locaux résolus depuis le dossier de la carte.
- **Contrats de production.** Objets facultatifs, scopes attendu et observé séparés, jetons canoniques, couverture risque → contrôle, sources qualifiées, plan de preuve structuré ; CLI ouverte aux fichiers externes avec `--type`.
- **Lecture et routes.** Le lecteur résout par table, préfixe et sous-locator (dont `DIRECTION/START/TREE`), refuse l’ambiguïté et ignore les titres des blocs de code. Le validateur de carte contrôle la couverture de tout locator cité et 42 conditions de façade.
- **Sources normatives.** Statut `SEED` du cycle de vie ; deux sorties canoniques (réponse visible et handoff) ; table de correspondance `RUN_CARD` par phase ; promesse du validateur (ce qu’il atteste, ce qu’il n’atteste pas) ; triade de conséquence décisionnelle ; cible visuelle en une seule table ; contrat du premier objet relié à `SAVOIR/CRAFT/CFT-00` ; marquage `TRUTH` à deux axes ; regard externe qualifié ; palette sans répartition imposée ; contrat de composant partagé unique dans `BIBLIOTHEQUE/COMPONENTS`.
- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill corrigés sur les écarts relevés ; la cohérence opposable se limite à la liste close des conditions de façade (`validate_reading_map.py`) : une divergence hors de cette liste n’est pas détectée. Efficacité déclarée `NOT-VERIFIED` partout.
- **Outils et build.** Archives créées dans le répertoire de travail puis publiées, membres contrôlés contre le manifeste, promotion transactionnelle, liens symboliques refusés, exclusions limitées à la racine ; manifeste sans doublon et version unique ; lectures non UTF-8, clés JSON répétées et types illégaux refusés proprement ; `validate_all.py` lançable depuis n’importe quel dossier ; chemins propres à l’export Local ; actions du workflow épinglées par SHA complet (runtime node24).
- **Retour d’audit (V1.1.1).** Triade de conséquence décisionnelle alignée dans la table `RUN_CARD`, le glossaire et les paquets de clôture ; portée écrite de B1b égale à celle du validateur ; sorties par mode définies une seule fois ; façades corrigées (Creative Boot, chargement LITE/ITER, projection machine, QUICKSTART §6, légende, exemples) ; aucun changement de schéma ni d’invariant.

**Compatibilité.** Une `RUN_CARD` produite avec V1.0.0 peut devoir être complétée pour satisfaire les invariants migrés ; les exemples et fixtures du package le sont.

## Ce que contient la baseline

| Élément | Fonction |
|---|---|
| `V1/official/` | Sources normatives, guides d’entrée, glossaire, carte de lecture et carte d’orchestration. |
| `skills/design-governance-practice/` | Couche d’activation et références conditionnelles pour humains et agents. |
| `schemas/` | Projections machine, exemples et fixtures de contrôle. |
| `scripts/` | Validateurs, runner global et construction des distributions. |

Les cinq sources normatives sont `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md` et `CHANGELOG.md`. Les guides et cartes dérivées orientent la lecture sans créer de règle concurrente.

## Parcours de découverte

> **Parcours de V1.1.1, historique.** Dans la candidate courante, une personne commence par la section « Commencer » du README du package ; un agent entre par la skill (noyau de fabrication et `DIRECTION/CHARGE`) et s’arrête par défaut à la proposition ; les guides s’ouvrent à la demande ; `ORCHESTRATION_MAP.md` n’est plus qu’un pointeur vers `READING_MAP.md`. Ces notes seront réécrites en R12.

Pour un humain qui découvre le système :

```text
README.md → QUICKSTART.md → GLOSSAIRE.md si nécessaire
→ READING_MAP.md → ORCHESTRATION_MAP.md si plusieurs capacités sont utiles
→ source normative concernée
```

Pour un agent :

```text
localiser le package → lire README et QUICKSTART
→ classer avec DIRECTION/START → charger les propriétaires utiles
→ orchestrer si nécessaire → produire → observer → corriger → fermer
```

## Contrôles inclus

Le package contrôle son inventaire, ses liens, son vocabulaire structuré, ses contrats machine, ses fixtures positives et négatives, ses cartes dérivées et la reproductibilité de ses distributions.

Ces contrôles établissent la cohérence documentaire et technique du package. Ils ne remplacent ni une observation de rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

Pour vérifier la baseline :

```bash
python3 scripts/validate_all.py
```

## Limites déclarées

V1.1.1 est une baseline expérimentale. Son efficacité de lecture, son adoption, sa charge cognitive, sa performance de production et sa supériorité par rapport à une autre méthode ne sont pas déclarées comme démontrées : leur statut est `NOT-VERIFIED`.

Le workflow d’intégration continue est épinglé par SHA ; son exécution sur un runner hébergé n’a pas encore été observée pour cette version (`NOT-VERIFIED`).

L’historique détaillé de construction et de travail est conservé hors de la distribution publique. Il n’est pas nécessaire pour utiliser la baseline.

