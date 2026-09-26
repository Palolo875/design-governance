#!/usr/bin/env python3
"""V1.2 — Budget de lecture d'un run DIRECTION, mesure déterministe.

Ensemble fixe : la skill (SKILL.md), READING_MAP.md et les sept routes d'un run DIRECTION servies par
scripts/read_route.py. Compte les lignes et les mots. Usage :
  python3 V12_Budget_lecture.py <racine_package> [<racine_package_2>]   # deux racines : avant / après
Limite : un paragraphe compte pour une ligne ; les mots sont le meilleur indicateur de charge.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROUTES = ["DIRECTION/START", "DIRECTION/CREATIVE-BOOT", "DIRECTION/EXTERNAL-START", "DIRECTION/VISUAL_TARGET",
          "DIRECTION/FIRST-OBJECT", "ACTION/RUN-DIRECTION", "ACTION/FIRST-RENDER"]
FILES = ["skills/design-governance-practice/SKILL.md", "V1/official/READING_MAP.md"]


def measure(root: Path) -> dict[str, tuple[int, int]]:
    out = {}
    for f in FILES:
        t = (root / f).read_text(encoding="utf-8")
        out[f.split("/")[-1]] = (len(t.splitlines()), len(t.split()))
    for r in ROUTES:
        t = subprocess.run([sys.executable, "-B", str(root / "scripts" / "read_route.py"), r],
                           capture_output=True, text=True, cwd=root, check=True).stdout
        out[r] = (len(t.splitlines()), len(t.split()))
    out["TOTAL"] = (sum(v[0] for v in out.values()), sum(v[1] for v in out.values()))
    return out


def main() -> int:
    roots = [Path(a).resolve() for a in sys.argv[1:3]]
    if not roots:
        print(__doc__)
        return 2
    ms = [measure(r) for r in roots]
    print(f"{'élément':28s}" + "".join(f"{'lignes':>8s}{'mots':>8s}" for _ in ms) + ("   Δ lignes   Δ mots" if len(ms) == 2 else ""))
    for k in ms[0]:
        row = f"{k:28s}" + "".join(f"{m[k][0]:8d}{m[k][1]:8d}" for m in ms)
        if len(ms) == 2:
            row += f"{ms[1][k][0] - ms[0][k][0]:+11d}{ms[1][k][1] - ms[0][k][1]:+9d}"
        print(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
