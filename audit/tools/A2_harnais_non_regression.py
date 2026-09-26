#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.02 PATCH-DECISION A2 — harnais de non-régression (oracles de test).

Artefact d'audit, HORS package : travaille toujours sur une copie temporaire.
Usage : python3 A2_harnais_non_regression.py <racine_du_package>

Sur B01 (avant correction), les tests A2-01 à A2-05 doivent ÉCHOUER : ils
documentent F-FIX-001/002/003 et F-ALL-001. Les témoins T-POS doivent réussir
avant et après correction.

Contrat de sortie attendu du correctif (phase 12) pour A2-05 : la suite native
imprime une ligne « + cas unitaires : N/N » (N = cas à faute unique exécutés).
"""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EX = "schemas/run_card.example.json"
FIX = "schemas/fixtures"
ORPHAN = f"{FIX}/invalid_capability_profile_missing_basis.json"


def run(root: Path, *args: str) -> tuple[int, str]:
    r = subprocess.run([sys.executable, *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def red(code: int, out: str) -> bool:
    return code != 0 and "Traceback" not in out


def example(root: Path) -> dict:
    return json.loads((root / EX).read_text(encoding="utf-8"))


def write(root: Path, rel: str, data: dict) -> None:
    (root / rel).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


# ---------- préparations ----------
def fix003(root: Path) -> None:
    # La faute nommée (preuve absente) est réparée ; une autre invalidité subsiste.
    d = json.loads((root / f"{FIX}/invalid_missing_proof.json").read_text(encoding="utf-8"))
    d["run_card"]["proof"] = example(root)["run_card"]["proof"]
    d["run_card"]["mode"] = "BOGUS-MODE"
    write(root, f"{FIX}/invalid_missing_proof.json", d)


def orphan_valid(root: Path) -> None:
    # La fixture orpheline devient valide : une suite qui l'exécute doit rougir.
    write(root, ORPHAN, example(root))


def undeclared(root: Path) -> None:
    d = example(root)
    d["run_card"]["mode"] = "BOGUS-MODE"
    write(root, f"{FIX}/invalid_zz_non_declaree.json", d)


def all001(root: Path) -> tuple[int, str]:
    """Appelle validate_all.expect_failure avec une entrée qui échoue pour une AUTRE raison."""
    d = example(root)
    d["run_card"]["mode"] = "BOGUS-MODE"
    write(root, "wrong_reason.json", d)
    spec = importlib.util.spec_from_file_location("va", root / "scripts/validate_all.py")
    va = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(va)
    cmd = [sys.executable, str(root / "scripts/validate_run_card.py"), str(root / "wrong_reason.json")]
    try:
        va.expect_failure(cmd, "basis absent", expected_message="capability_profile exige basis")
    except TypeError:
        return 0, "format absent : expect_failure n'accepte pas de motif attendu"
    except SystemExit as exc:
        return 1, f"rejet du mauvais motif : {exc}"
    return 0, "accepté pour un motif étranger"


CASES = [
    ("T-POS-1", "suite RUN_CARD verte", None, lambda r: run(r, "scripts/validate_run_card.py"), lambda c, o: c == 0),
    ("T-POS-2", "validate_all complet vert (build et reproductibilité)", None, lambda r: run(r, "scripts/validate_all.py"), lambda c, o: c == 0),
    ("A2-01", "F-FIX-003 : négatif réparé de sa faute mais invalide autrement → suite rouge",
     fix003, lambda r: run(r, "scripts/validate_run_card.py"), red),
    ("A2-02", "F-FIX-001 : fixture orpheline rendue valide → suite rouge",
     orphan_valid, lambda r: run(r, "scripts/validate_run_card.py"), red),
    ("A2-03", "F-FIX-001 : fichier de fixture non déclaré → suite rouge",
     undeclared, lambda r: run(r, "scripts/validate_run_card.py"), red),
    ("A2-04", "F-ALL-001 : échec pour un motif étranger → rejeté par l'orchestrateur",
     None, all001, lambda c, o: c == 1),
    ("A2-05", "F-FIX-002 : cas unitaires à faute unique exécutés (ligne « + cas unitaires : N/N », N ≥ 20)",
     None, lambda r: run(r, "scripts/validate_run_card.py"),
     lambda c, o: c == 0 and any(int(m.group(1)) == int(m.group(2)) >= 20
                                 for m in re.finditer(r"\+ cas unitaires : (\d+)/(\d+)", o))),
]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    res = []
    for cid, label, prep, act, ok in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pkg"
            shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
            if prep:
                prep(root)
            code, out = act(root)
            tail = "TRACEBACK" if "Traceback" in out else (out.strip().splitlines() or [""])[-1][:90]
            res.append((cid, bool(ok(code, out)), label, code, tail))
    for cid, good, label, code, tail in res:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:8} {label}  [code {code} · {tail}]")
    pos = [r for r in res if r[0].startswith("T-POS")]
    a2 = [r for r in res if r[0].startswith("A2")]
    print(f"\nTémoins positifs : {sum(r[1] for r in pos)}/{len(pos)} ; tests A2 : {sum(r[1] for r in a2)}/{len(a2)}")
    return 0 if all(r[1] for r in res) else 1


if __name__ == "__main__":
    sys.exit(main())
