#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R11c : clôture des routes RUN-* en trace complète ; raccord de G4 (R11b).

Revue du 30-09 sur `9cbdcc2` : `TRA-01` dit qu'une trace légère livre une proposition sans verdict ni clôture, mais les
rubriques « Clôture » de RUN-LITE, RUN-ITER, RUN-STANDARD et RUN-SYSTEM prescrivent `DECIDED` puis `CLOSED` sans condition
de niveau de trace (seule RUN-DIRECTION dit « En trace complète »). Raccord : la même condition dans les quatre phrases ;
règles de retour et de reclassification conservées. Rapport : `V12R_34_R11c_CLOTURE.md`.
Usage : python3 V12R_Patch_R11c.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

A, C = "V1/official/ACTION.md", "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_R11c_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("a37d0c79b0d803f08c18352a007ee4e704eba43ad618c6dd9c8ee42e5f85caaf", F / "validate_structure.py"),
}
OLD, NEW = "**Clôture.** Passer à `DECIDED`, puis `CLOSED`.", "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`."

PATCH = [
    ("R11c-L", "RUN-LITE : clôture en trace complète", A,
     OLD + " Reclassifier en `SYSTÈME`", NEW + " Reclassifier en `SYSTÈME`"),
    ("R11c-I", "RUN-ITER : clôture en trace complète", A,
     OLD + " Utiliser `RETURNED`", NEW + " Utiliser `RETURNED`"),
    ("R11c-S", "RUN-STANDARD : clôture en trace complète", A,
     OLD + " Passer à `EXPLORATORY`", NEW + " Passer à `EXPLORATORY`"),
    ("R11c-Y", "RUN-SYSTEM : clôture en trace complète", A,
     "**Clôture.** Passer à `DECIDED`, puis `CLOSED` lorsque consumers",
     "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque consumers"),
    ("R11c-H", "CHANGELOG : entrée R11b complétée", C,
     "chaque route `RUN-*` dit sa sortie en trace légère,",
     "chaque route `RUN-*` dit sa sortie en trace légère et ne clôt qu’en trace complète,"),
]

MUTATION_OF = {pid: "clôture des routes en trace complète" for pid in ("R11c-L", "R11c-I", "R11c-S", "R11c-Y")}
EXTRA_MUTATIONS = [
    ("RUN-DIRECTION : condition retirée", A, "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` uniquement",
     "**Clôture.** Passer à `DECIDED`, puis `CLOSED` uniquement", "clôture des routes en trace complète"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
