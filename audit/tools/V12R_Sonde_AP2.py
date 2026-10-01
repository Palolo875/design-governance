#!/usr/bin/env python3
"""Audit progressif, unité 2 — sondes directes de C14 (suivi) et C22 (export de mesure), ancienne et nouvelle version.

C14 : la décision du suivi (V12R_Suivi.main) est rejouée sur des scénarios dérivés de résultats RÉELS (instantané
      `V12R_Instantane_suivi_AP1.json`, 389 cas). Seuls varient : un cas retiré, une sortie de validateur simulée, une
      garde de remplacement renommée. validate_all est simulé vert (il est contrôlé à part par le suivi complet).
C22 : l'export JSON de V12R_Mesures porte l'atteignabilité calculée (dictionnaire égal à reach(budget)), pas une route.
L'ancienne version est lue dans git (commit de référence, par défaut 472ff24) et exécutée comme si elle était à sa place.
Usage : python3 V12R_Sonde_AP2.py <racine_package> [--avant <commit>]
"""
from __future__ import annotations

import contextlib
import copy
import io
import json
import subprocess
import sys
import tempfile
import types
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parents[1]
sys.path.insert(0, str(TOOLS))
SNAPSHOT = TOOLS.parent / "snapshots" / "V12R_Instantane_suivi_AP1.json"
results_log: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results_log.append((name, ok, detail))
    print(f"  {'OK' if ok else 'KO'}  {name}{' — ' + detail if detail else ''}")


def load(name: str, source: str) -> types.ModuleType:
    """Charge un outil depuis son source, à la place qu'il occupe dans audit/tools."""
    module = types.ModuleType(name)
    module.__file__ = str(TOOLS / f"{name.split('__')[0]}.py")
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    return module


def git_source(commit: str, rel: str) -> str:
    return subprocess.run(["git", "show", f"{commit}:{rel}"], cwd=REPO, capture_output=True, text=True, check=True).stdout


def verdict(module: types.ModuleType, root: Path, results: dict, rows: list[dict], fake: dict[str, tuple[int, str]]) -> str:
    real_run = module.run

    def run(cmd, cwd):
        script = Path(cmd[-1]).name
        if script == "validate_all.py":
            return 0, "FULL VALIDATION PASSED — simulé par la sonde"
        return fake[script] if script in fake else real_run(cmd, cwd)

    module.run = run
    module.table = lambda: copy.deepcopy(rows)
    module.carto = types.SimpleNamespace(run_suite=lambda _root: copy.deepcopy(results))
    argv = sys.argv
    sys.argv = ["V12R_Suivi.py", str(root)]
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            code = module.main()
    finally:
        sys.argv = argv
    return "VERT" if code == 0 and "SUIVI VERT" in out.getvalue() else "ROUGE"


def sonde_c14(root: Path, commit: str) -> None:
    print("C14 — décision du suivi sur scénarios (résultats réels de l'instantané AP1)")
    base_results = json.loads(SNAPSHOT.read_text(encoding="utf-8"))["cas"]
    probe = load("V12R_Suivi__probe", (TOOLS / "V12R_Suivi.py").read_text(encoding="utf-8"))
    rows = probe.table()
    new = lambda: load("V12R_Suivi__nouveau", (TOOLS / "V12R_Suivi.py").read_text(encoding="utf-8"))  # noqa: E731
    old = lambda: load("V12R_Suivi__ancien", git_source(commit, "audit/tools/V12R_Suivi.py"))  # noqa: E731

    def without(harness: str, case: str) -> dict:
        res = copy.deepcopy(base_results)
        del res[harness][case]
        return res

    renamed = copy.deepcopy(rows)
    for row in renamed:
        if (row["harnais"], row["cas"]) == ("C2", "G-06"):
            row["garde_remplacement"] = "structure:XXX-99"
    failed = "STRUCTURE VALIDATION FAILED — gardes de propriété\n"
    scenarios = [
        # nom, résultats, table, sorties simulées, verdict attendu
        ("base : résultats réels", base_results, rows, {}, "VERT"),
        ("cas OBSOLETE retiré du run (C2 G-06)", without("C2", "G-06"), rows, {}, "ROUGE"),
        ("cas MAINTENU retiré du run (C1 G-06)", without("C1", "G-06"), rows, {}, "ROUGE"),
        ("validate_reading_map interrompu tôt (lien)", base_results, rows,
         {"validate_reading_map.py": (1, "READING MAP VALIDATION FAILED — lien relatif non résolu : x.md")}, "ROUGE"),
        ("validate_structure en trace Python", base_results, rows,
         {"validate_structure.py": (1, "Traceback (most recent call last):\n  File \"x\", line 1\nKeyError: 'x'")}, "ROUGE"),
        ("garde de remplacement inconnue (structure:XXX-99)", base_results, renamed, {}, "ROUGE"),
        ("autre garde rouge, contrôle complet (SKL-01)", base_results, rows,
         {"validate_structure.py": (1, failed + "- [SKL-01] en-tête de la skill : champ name absent ou vide")}, "VERT"),
        ("garde de remplacement citée (CHG-01)", base_results, rows,
         {"validate_structure.py": (1, failed + "- [CHG-01] chargement : la clôture de chaque mode renvoie…")}, "ROUGE"),
    ]
    for name, res, table_rows, fake, expected in scenarios:
        before = verdict(old(), root, res, table_rows, fake)
        after = verdict(new(), root, res, table_rows, fake)
        check(f"{name} : attendu {expected}", after == expected, f"ancienne version {before}, nouvelle {after}")


def sonde_c22(root: Path, commit: str) -> None:
    print("C22 — export JSON de V12R_Mesures")
    for label, source in (("nouvelle", (TOOLS / "V12R_Mesures.py").read_text(encoding="utf-8")),
                          ("ancienne", git_source(commit, "audit/tools/V12R_Mesures.py"))):
        module = load(f"V12R_Mesures__{label}", source)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "mesures.json"
            argv = sys.argv
            sys.argv = ["V12R_Mesures.py", str(root), "--json", str(target)]
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    module.main()
            finally:
                sys.argv = argv
            exported = json.loads(target.read_text(encoding="utf-8"))["atteignabilite"]
        expected = module.reach(module.budget(root))
        ok = isinstance(exported, dict) and exported == json.loads(json.dumps(expected))
        shown = exported if isinstance(exported, str) else f"dict ({len(exported.get('outils', {}))} outils)"
        check(f"{label} version{" (référence avant)" if label == "ancienne" else ""} : atteignabilite exportée = reach(budget)", ok if label == "nouvelle" else True,
              f"exporté : {shown}" + ("" if label == "nouvelle" else f" ; {'conforme' if ok else 'DÉFAUT reproduit'}"))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    commit = sys.argv[sys.argv.index("--avant") + 1] if "--avant" in sys.argv else "472ff24"
    sonde_c14(root, commit)
    sonde_c22(root, commit)
    bad = sum(1 for _, ok, _ in results_log if not ok)
    print(f"SONDE AP2 : {'VERTE' if not bad else f'ROUGE ({bad})'} — {len(results_log) - bad}/{len(results_log)} contrôles")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
