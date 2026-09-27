#!/usr/bin/env python3
"""V1.2 refonte — R1 — Cartographie des harnais par sensibilité à la prose.

Outil d'audit HORS package ; travaille sur des copies ; lecture seule des sources.
Usage : python3 V12R_Carto_harnais.py <racine_package> <dossier_sortie>

Principe : on altère la prose des fichiers Markdown de façon invisible (U+200B inséré dans chaque
mot de 3 lettres ou plus), sans toucher aux titres, aux blocs de code ni aux jetons entre backticks.
Un cas de harnais qui passe au rouge sur la copie altérée dépend de la FORMULATION exacte ; un cas
qui reste vert dépend de la structure (titres, locators, jetons, schéma, scripts).

Variantes : « TOUT » (tous les Markdown altérés) puis un groupe de fichiers à la fois, pour
attribuer chaque dépendance à son fichier.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ZW = "​"
WORD = re.compile(r"[^\W\d_]{3,}")
TICK = re.compile(r"(`[^`]*`)")
LINE = re.compile(r"^(OK|KO|ÉCHEC|ECHEC|FAIL)\s+(\S+)\s+(.*)$")

GROUPS = {
    "DIRECTION": ["V1/official/DIRECTION.md"],
    "ACTION": ["V1/official/ACTION.md"],
    "SAVOIR": ["V1/official/SAVOIR.md"],
    "BIBLIOTHEQUE_CHANGELOG": ["V1/official/BIBLIOTHEQUE.md", "V1/official/CHANGELOG.md"],
    "FACADES": ["V1/official/QUICKSTART.md", "V1/official/README.md", "README.md",
                "V1/official/GLOSSAIRE.md", "V1/official/ORCHESTRATION_MAP.md", "V1/official/READING_MAP.md"],
    "SKILL": ["skills/design-governance-practice/SKILL.md",
              "skills/design-governance-practice/references/examples.md",
              "skills/design-governance-practice/references/flow.md",
              "skills/design-governance-practice/references/canonical_minimum.md",
              "skills/design-governance-practice/references/machine_projection.md"],
}


def perturb_text(text: str) -> str:
    out, fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            out.append(line)
            continue
        if fence or line.lstrip().startswith("#") or not line.strip():
            out.append(line)
            continue
        parts = TICK.split(line)
        for i, p in enumerate(parts):
            if i % 2 == 0:  # hors backticks
                parts[i] = WORD.sub(lambda m: m.group(0)[0] + ZW + m.group(0)[1:], p)
        out.append("".join(parts))
    return "\n".join(out)


def make_copy(root: Path, files: list[str], dest: Path) -> None:
    shutil.copytree(root, dest, ignore=shutil.ignore_patterns("dist", "*.zip", "__pycache__"))
    for rel in files:
        p = dest / rel
        p.write_text(perturb_text(p.read_text(encoding="utf-8")), encoding="utf-8")


def harnesses() -> list[Path]:
    return sorted(TOOLS.glob("*_harnais_non_regression.py"))


def run_suite(pkg: Path) -> dict[str, dict[str, str]]:
    res: dict[str, dict[str, str]] = {}
    for h in harnesses():
        name = h.name.split("_harnais")[0]
        try:
            p = subprocess.run([sys.executable, "-B", str(h), str(pkg)], capture_output=True, text=True, timeout=900)
            txt = p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            txt = "TIMEOUT"
        cases = {}
        for line in txt.splitlines():
            m = LINE.match(line.strip())
            if m:
                cases[m.group(2)] = "OK" if m.group(1) == "OK" else "KO"
        res[name] = cases
    return res


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    variants = {"TEMOIN": []}
    variants["TOUT"] = sorted({f for fs in GROUPS.values() for f in fs})
    variants.update(GROUPS)

    def job(item):
        vname, files = item
        with tempfile.TemporaryDirectory(prefix=f"v12r_{vname}_") as td:
            dest = Path(td) / "package"
            make_copy(root, files, dest)
            return vname, run_suite(dest)

    with ThreadPoolExecutor(max_workers=4) as ex:
        results = dict(ex.map(job, variants.items()))
    (out / "V12R_Carto_harnais_brut.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")

    # Tableau par cas
    base = results["TEMOIN"]
    rows = []
    for h, cases in base.items():
        for cid, st in cases.items():
            sens = [g for g in GROUPS if results[g].get(h, {}).get(cid, "ABSENT") != "OK"]  # absent (plantage) = sensible
            tout = results["TOUT"].get(h, {}).get(cid, "ABSENT")
            if st != "OK":
                cat = "TEMOIN-ROUGE"
            elif tout != "OK" or sens:
                cat = "PROSE"
            else:
                cat = "STRUCTURE"
            rows.append((h, cid, st, tout or "?", cat, "+".join(sens)))
    lines = ["harnais;cas;temoin;tout_altere;categorie;fichiers_sensibles"]
    lines += [";".join(r) for r in rows]
    (out / "V12R_Carto_harnais.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    n = len(rows)
    prose = sum(1 for r in rows if r[4] == "PROSE")
    print(f"cas : {n} ; sensibles à la prose : {prose} ; structure seule : {n - prose}")
    for g in GROUPS:
        k = sum(1 for r in rows if g in r[5].split("+"))
        print(f"  {g:24s} {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
