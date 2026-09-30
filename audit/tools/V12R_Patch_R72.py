#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R7-2 : raccord ancre / FAIL-ASSUMED (erratum de R7).

Constat (revue du 30-09-2026, vérifiée) : DIRECTION disait qu'une diffusion sans l'ancre requise « passe par »
`FAIL-ASSUMED`. Or `ACTION/OVERRIDE` réserve `FAIL-ASSUMED` à un échec connu présent dans `proof.observed`, « jamais un
`NOT-VERIFIED` requalifié » ; une ancre absente laisse les axes visuels `NOT-VERIFIED`. Chemin correct, déjà accepté par le
validateur (fixture NO_ANCHOR) : la direction reste `EXPLORATORY`, montrée ou partagée comme proposition avec sa limite.
Décision de l'owner : « Allons-y » (30-09-2026). Schéma et validateur inchangés.
Rapport : `V12R_24_R72_RACCORD_ANCRE.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, C = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_R72_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("9e63efd66e0218b0988a5c4a77142ccbd93b3e61a16600f8f6a290ecef550558", F / "validate_structure.py"),
}

PATCH = [
    ("R72-A1", "ANC-01 (noyau) : sans ancre, EXPLORATORY ; FAIL-ASSUMED pour un échec connu seulement", D,
     "Une **diffusion limitée** sans l’ancre requise passe par `FAIL-ASSUMED` (`ACTION/OVERRIDE`) : le verdict reste non accepté.",
     "Sans l’ancre requise, la direction reste `EXPLORATORY` : elle peut être montrée ou partagée comme proposition, avec sa limite. "
     "`FAIL-ASSUMED` (`ACTION/OVERRIDE`) ne vaut que pour un échec connu et observé, jamais pour une ancre absente, qui reste "
     "`NOT-VERIFIED` ; le verdict reste non accepté."),
    ("R72-A2", "absolu 2, paragraphe final : même raccord", D,
     "la direction ne peut pas être acceptée ; une diffusion limitée reste possible par `FAIL-ASSUMED`, avec un verdict non accepté "
     "(`ACTION/OVERRIDE`).",
     "la direction ne peut pas être acceptée ; elle reste `EXPLORATORY` avec sa limite. Une ancre absente n’est pas un échec "
     "connu : `FAIL-ASSUMED` ne s’y applique pas (`ACTION/OVERRIDE`)."),
    ("R72-H1", "CHANGELOG, entrée R7 alignée", C,
     "`FAIL-ASSUMED` ne permet qu’une diffusion limitée non acceptée ;",
     "sans l’ancre requise, la direction reste `EXPLORATORY` ; `FAIL-ASSUMED` ne vaut que pour un échec connu, jamais pour une "
     "ancre absente (raccord R7-2) ;"),
]

MUTATION_OF = {"R72-A1": "vocabulaire retiré", "R72-A2": "vocabulaire retiré", "R72-H1": "vocabulaire retiré"}
EXTRA_MUTATIONS = [
    ("FAIL-ASSUMED ouvert à l'ancre absente", D, "Une ancre absente n’est pas un échec connu : `FAIL-ASSUMED` ne s’y applique pas",
     "Une ancre absente peut être assumée : `FAIL-ASSUMED` s’y applique", "ancre et FAIL-ASSUMED"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
