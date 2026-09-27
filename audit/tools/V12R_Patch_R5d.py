#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R5d : BIBLIOTHEQUE alignée (boucle, one-shot, F22).

Boucle structurelle et one-shot → renvois à leur lieu propriétaire, en gardant les critères propres à la structure ;
exemptions BIBLIOTHEQUE retirées des gardes « boucle unique » et « one-shot ». F22 : les tests perceptifs de
`BIBLIOTHEQUE/GATE` (concept PRC-01) deviennent atteignables en un renvoi depuis `ACTION/GATE-C` (garde RENVOIS).
Rapport : `V12R_11_R5d_BIBLIOTHEQUE.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12R_Patch_R5d_textes import BOUCLE, ONESHOT  # noqa: E402

A, B, C = "V1/official/ACTION.md", "V1/official/BIBLIOTHEQUE.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("9f574d816efd513992a03f80c7db678fb45bd0979b0bc2449fd47af21f78e9d4",
                                      HERE / "V12R_Patch_R5d_fichiers" / "scripts" / "validate_structure.py"),
}

PATCH = [
    ("R5d-O1", "one-shot structurel : renvoi, critères de structure gardés", B, ONESHOT,
     "Le `one-shot` suit la branche one-shot d’`ACTION/PIPELINE-DIRECTION`. Après sélection, il ne ferme que si la thèse "
     "structurelle, la composition, la spécificité, les états et les risques applicables tiennent déjà ; si une relation dominante "
     "échoue, retourne ou corrige, sans seconde version décorative."),
    ("R5d-B1", "boucle structurelle : renvoi, critères de structure gardés", B, BOUCLE,
     "La boucle structurelle est la boucle d’édition de `DIRECTION/DOUBLE-LOOP` appliquée à la structure : toute correction change "
     "une relation de foyer, de rythme, de hiérarchie, de preuve, de comportement ou de robustesse ; une route supplémentaire ou une "
     "variante nominale ne constitue pas une amélioration."),
    ("R5d-P1", "F22 : tests perceptifs balisés (PRC-01)", B,
     "\nLe contrôle de module vérifie support, grille, scène, objet, états, mobile et accessibilité structurelle",
     "\n<!-- concept:PRC-01 -->\nLe contrôle de module vérifie support, grille, scène, objet, états, mobile et accessibilité structurelle"),
    ("R5d-P2", "F22 : renvoi depuis Gate C", A,
     "Chaque verdict C précise le périmètre : viewport, état, scène, contenu et élément observé.",
     "Chaque verdict C précise le périmètre : viewport, état, scène, contenu et élément observé. Lorsque la structure est ouverte, "
     "applique sur la même capture les tests perceptifs de `BIBLIOTHEQUE/GATE` (non-généricité, silhouette, grille) ; ils "
     "nourrissent C3 et C4 sans verdict propre."),
    ("R5d-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **BIBLIOTHEQUE alignée (refonte, R5d).** Boucle structurelle et one-shot renvoient à leur lieu propriétaire en gardant "
     "leurs critères de structure ; les tests perceptifs de `BIBLIOTHEQUE/GATE` sont appelés depuis Gate C.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {"R5d-O1": "vocabulaire retiré", "R5d-B1": "vocabulaire retiré", "R5d-P1": "PRC-01 absent",
               "R5d-P2": "renvoi ACTION/GATE-C → PRC-01"}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
