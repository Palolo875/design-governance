#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R7-3 : garde « ancre absente → FAIL-ASSUMED » bornée (raccord de R7-2).

Constat (revue du 30-09-2026, vérifiée) : la garde de vocabulaire de R7-2 refusait toute phrase « passe par
`FAIL-ASSUMED` », y compris une phrase conforme à ACTION/OVERRIDE (diffusion limitée d'un échec connu). Elle est bornée au
contexte de l'ancre absente. Aucun texte du package ne change ; seul `validate_structure.py` est remplacé.
Décision de l'owner : « Allons-y » (30-09-2026). Rapport : `V12R_26_R73_GARDE_BORNEE.md`.
Usage : python3 V12R_Patch_R73.py <racine> [--verifier | --mutations | --acceptations]
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, C = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_R73_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("b0a50dab4f22862001c6867a26e5c502d1fde34df16f0f26702c50b950a70b6c", F / "validate_structure.py"),
}
PATCH: list = []
MUTATION_OF: dict = {}

NEW_A1 = ("Sans l’ancre requise, la direction reste `EXPLORATORY` : elle peut être montrée ou partagée comme proposition, avec sa "
          "limite. `FAIL-ASSUMED` (`ACTION/OVERRIDE`) ne vaut que pour un échec connu et observé, jamais pour une ancre absente, "
          "qui reste `NOT-VERIFIED` ; le verdict reste non accepté.")
NEW_A2 = ("elle reste `EXPLORATORY` avec sa limite. Une ancre absente n’est pas un échec connu : `FAIL-ASSUMED` ne s’y applique "
          "pas (`ACTION/OVERRIDE`).")
NEW_H1 = ("sans l’ancre requise, la direction reste `EXPLORATORY` ; `FAIL-ASSUMED` ne vaut que pour un échec connu, jamais pour "
          "une ancre absente (raccord R7-2) ;")

# Les trois anciens raccourcis doivent rester refusés (rouges).
EXTRA_MUTATIONS = [
    ("ancien raccourci ANC-01", D, NEW_A1,
     "Une **diffusion limitée** sans l’ancre requise passe par `FAIL-ASSUMED` (`ACTION/OVERRIDE`) : le verdict reste non accepté.",
     "vocabulaire retiré"),
    ("ancien raccourci de l'absolu 2", D, NEW_A2,
     "une diffusion limitée reste possible par `FAIL-ASSUMED`, avec un verdict non accepté (`ACTION/OVERRIDE`).",
     "vocabulaire retiré"),
    ("ancienne entrée du CHANGELOG", C, NEW_H1, "`FAIL-ASSUMED` ne permet qu’une diffusion limitée non acceptée ;",
     "vocabulaire retiré"),
]

# Une phrase conforme à ACTION/OVERRIDE doit être acceptée (verte).
ANCRE_OVERRIDE = "Le seul override est le `FAIL-ASSUMED` journalisé dans `ACTION`."
ACCEPTS = [
    ("diffusion limitée d'un échec connu (phrase de la revue)", D, ANCRE_OVERRIDE,
     ANCRE_OVERRIDE + " Une diffusion limitée d’un échec connu et observé passe par `FAIL-ASSUMED` si les conditions "
     "d’`ACTION/OVERRIDE` sont réunies ; le verdict reste non accepté."),
]


def accepts(root: Path) -> int:
    bad = 0
    for name, rel, old, new in ACCEPTS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            code, _out = base.structure(copy)
            green = ok and code == 0
            print(f"acceptation {name} : {'VERT' if green else 'NON VERT'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if green else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if len(sys.argv) > 1 and "--acceptations" in sys.argv:
        return 1 if accepts(Path(sys.argv[1]).resolve()) else 0
    if len(sys.argv) > 1 and "--mutations" in sys.argv:
        root = Path(sys.argv[1]).resolve()
        return 1 if base.mutations(root) + accepts(root) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
