#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R11a : résidu `DAILY` dans DIRECTION (signalé par le plan consolidé du 27-09-2026).

R4 a transformé `DIRECTION/DAILY` en `DIRECTION/CHARGE` ; l'« ordre de lecture minimal » de `DIRECTION/START` citait encore
`DAILY`. Validé par l'owner (« Oui », 27-09-2026). Garde : vocabulaire retiré `DAILY` hors CHANGELOG.
Rapport : `V12R_13_R11a_CORRECTIFS.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, C = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("1647fc6b74f4bf9d8d453e68fdbfc557d2b4c3ca8a819f4f99666a6da310765d",
                                      HERE / "V12R_Patch_R11a_fichiers" / "scripts" / "validate_structure.py"),
}

PATCH = [
    ("R11a-D1", "résidu DAILY → CHARGE", D, "3) `DAILY` choisit la plus petite route utile", "3) `CHARGE` choisit la plus petite route utile"),
    ("R11a-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Correctif (refonte, R11a).** L’ordre de lecture minimal de `DIRECTION/START` renvoie à `CHARGE` (dernier résidu de "
     "l’ancienne vue `DAILY`).\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {"R11a-D1": "vocabulaire retiré"}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
