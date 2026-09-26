# Release notes — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de publication :** 2026-09-19  
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Présentation

Design Governance V1.0.0 est une baseline publique pour diriger, créer, juger, construire et vérifier un travail de design. Elle aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

La release est présentée comme un système cohérent, utilisable et testable. Elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage sans preuve adaptée.

## Ce que contient la baseline

| Élément | Fonction |
|---|---|
| `V1/official/` | Sources normatives, guides d’entrée, glossaire, carte de lecture et carte d’orchestration. |
| `skills/design-governance-practice/` | Couche d’activation et références conditionnelles pour humains et agents. |
| `schemas/` | Projections machine, exemples et fixtures de contrôle. |
| `scripts/` | Validateurs, runner global et construction des distributions. |

Les cinq sources normatives sont `DIRECTION.md`, `ACTION.md`, `SAVOIR.md`, `BIBLIOTHEQUE.md` et `CHANGELOG.md`. Les guides et cartes dérivées orientent la lecture sans créer de règle concurrente.

## Parcours de découverte

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

V1.0.0 est une baseline expérimentale. Son efficacité de lecture, son adoption, sa charge cognitive, sa performance de production et sa supériorité par rapport à une autre méthode ne sont pas déclarées comme démontrées.

L’historique détaillé de construction et de travail est conservé hors de la distribution publique. Il n’est pas nécessaire pour utiliser la baseline.

