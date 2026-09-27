#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R5c (partie sans décision en attente) : SAVOIR alignée.

D-16 (deux modèles à trois niveaux → un seul modèle de niveaux, Correction / Précision / Intention ; l'autre triade devient
« trois moments de la qualité ») ; boucle de jugement → renvoi à DIRECTION/DOUBLE-LOOP (exemption SAVOIR retirée de la
garde « boucle unique ») ; one-shot → renvoi à la branche one-shot d'ACTION/PIPELINE-DIRECTION. L'ancre (décision 6) et
les lois de SAVOIR (décision 8) ne sont pas touchées. Rapport : `V12R_10_R5c_SAVOIR.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12R_Patch_R5c_textes import BOUCLE, ONESHOT  # noqa: E402

S, C = "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("a0519dcb56bb74ab9ad5aa0f578b3ecb3c7b6459b45fdf36e0ba2241a0085d97",
                                      HERE / "V12R_Patch_R5c_fichiers" / "scripts" / "validate_structure.py"),
}

PATCH = [
    ("R5c-N1", "D-16 : trois moments, pas un second modèle de niveaux", S,
     "Distingue trois niveaux : **qualité intrinsèque visée**", "Distingue trois moments de la qualité : **qualité intrinsèque visée**"),
    ("R5c-N2", "D-16 : renvoi au modèle de niveaux unique", S,
     "un rendu peut être conforme et propre mais rester générique.",
     "un rendu peut être conforme et propre mais rester générique. À chaque moment, la résolution atteinte se lit avec un seul "
     "modèle de niveaux : `Correction`, `Précision` et `Intention` (« Jugement visuel situé »)."),
    ("R5c-O1", "one-shot : renvoi à la branche one-shot d'ACTION", S, ONESHOT,
     "Le `one-shot` suit la branche one-shot d’`ACTION/PIPELINE-DIRECTION` : une exécution raccourcie de la boucle, jamais sa "
     "suppression ; un premier objet faible se corrige ou se retourne."),
    ("R5c-B1", "boucle : renvoi à DIRECTION/DOUBLE-LOOP", S, BOUCLE,
     "La boucle de jugement est la boucle d’édition de `DIRECTION/DOUBLE-LOOP`, copiée dans le noyau de la skill."),
    ("R5c-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **SAVOIR alignée (refonte, R5c, hors ancre).** Un seul modèle de niveaux (`Correction`, `Précision`, `Intention`) ; "
     "la triade visée / observée / prouvée devient « trois moments de la qualité » ; boucle et one-shot renvoient à leur lieu "
     "propriétaire.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {"R5c-N1": "vocabulaire retiré", "R5c-O1": "vocabulaire retiré", "R5c-B1": "vocabulaire retiré"}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
