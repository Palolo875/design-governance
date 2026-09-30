#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION D-25 : l'action principale reste fonctionnelle avec une valeur d'exemple marquée.

Constat : R10, palier exploratoire (`V12R_35` §3.5). Sur B-DLA, C3 et C4 retirent le bouton WhatsApp et laissent l'adresse en
blancs faute de valeur réelle, alors que `CNT-01` demande un contenu plausible marqué plutôt que des emplacements vides.
Décision de l'owner (30-09) : « On va corriger et s'arrêter. Avec les runs. » Correction : une phrase dans `CNT-01` (bloc
CONTENU, compilé dans le noyau). Rapport : `V12R_36_D25_ACTION_PRINCIPALE.md`.
Usage : python3 V12R_Patch_D25.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, C = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_D25_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("8525d7d12e1c496ad8ecf339e7cbe7cf630f996191aa83d2f6e837232d324ea1", F / "validate_structure.py"),
}
PATCH = [
    ("D25-C", "CNT-01 (noyau) : l'action principale reste fonctionnelle et marquée", D,
     "elle doit se lire comme une page, pas comme un gabarit.",
     "elle doit se lire comme une page, pas comme un gabarit. L’action principale (commander, écrire, appeler, venir) reste "
     "fonctionnelle avec une valeur d’exemple marquée (numéro, adresse, lien) : une valeur inconnue ne la retire pas."),
    ("D25-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Action principale conservée (refonte, D-25).** Faute de valeur réelle, l’action principale d’une page (commander, "
     "écrire, appeler, venir) reste fonctionnelle avec une valeur d’exemple marquée, au lieu d’être retirée.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {"D25-C": "action principale (D-25)"}
EXTRA_MUTATIONS = [
    ("action principale retirée de la copie compilée", "skills/design-governance-practice/SKILL.md",
     " L’action principale (commander, écrire, appeler, venir) reste fonctionnelle avec une valeur d’exemple marquée (numéro, "
     "adresse, lien) : une valeur inconnue ne la retire pas.", "", "action principale (D-25)"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
