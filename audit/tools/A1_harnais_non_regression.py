#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.01 PATCH-DECISION A1 — harnais de non-régression.

Artefact d'audit, HORS package : il ne modifie jamais le dossier passé en
argument. Il en fait une copie temporaire, y injecte chaque mutation, lance les
validateurs et compare le résultat au comportement attendu APRÈS correction.

Usage : python3 A1_harnais_non_regression.py <racine_du_package>

Sur B01 (avant correction), les tests A1-01 à A1-10 doivent ÉCHOUER : ils
documentent les défauts F-VRC-006/007/008 et F-VCT-001/003. Les témoins T-POS
doivent RÉUSSIR avant et après correction (non-régression des positifs).
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RC = "schemas/run_card.schema.json"
EX = "schemas/run_card.example.json"
FIX = "schemas/fixtures"


def run(root: Path, *args: str) -> tuple[int, str]:
    r = subprocess.run([sys.executable, *args], cwd=root, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def governed_failure(code: int, out: str) -> bool:
    """Échec attendu : code non nul, bannière FAILED, aucune trace Python."""
    return code != 0 and "Traceback" not in out and "FAILED" in out


def mutate_json(root: Path, rel: str, fn) -> None:
    p = root / rel
    data = json.loads(p.read_text(encoding="utf-8"))
    p.write_text(json.dumps(fn(data), ensure_ascii=False), encoding="utf-8")


def drop_mode_enum(d):
    del d["properties"]["run_card"]["properties"]["mode"]["enum"]
    return d


def drop_depth_enum(d):
    def walk(x):
        if isinstance(x, dict):
            if "depth" in x.get("properties", {}):
                x["properties"]["depth"].pop("enum", None)
            for v in x.values():
                walk(v)
    walk(d)
    return d


def add_unused_unsupported(d):
    d.setdefault("properties", {})["zz_non_visite"] = {"type": "string", "pattern": "^x$"}
    return d


CASES = []


def case(cid, label, prepare, command, expect):
    CASES.append((cid, label, prepare, command, expect))


RUN_SUITE = ("scripts/validate_run_card.py",)
RUN_TARGET_INVALID = ("scripts/validate_run_card.py", f"{FIX}/invalid_missing_proof.json")
CT_SUITE = ("scripts/validate_contracts.py",)

# --- Témoins positifs : doivent réussir avant ET après correction ---
case("T-POS-1", "B01 : suite RUN_CARD verte", None, RUN_SUITE, lambda c, o: c == 0)
case("T-POS-2", "B01 : exemple RUN_CARD ciblé vert", None, ("scripts/validate_run_card.py", EX), lambda c, o: c == 0)
case("T-POS-3", "B01 : carte invalide ciblée rejetée", None, RUN_TARGET_INVALID, lambda c, o: governed_failure(c, o))
case("T-POS-4", "B01 : suite des contrats verte", None, CT_SUITE, lambda c, o: c == 0)

# --- F-VRC-007 : schéma vide ---
case("A1-01", "schéma RUN_CARD {} → suite en échec gouverné",
     lambda r: (r / RC).write_text("{}"), RUN_SUITE, governed_failure)
case("A1-02", "schéma RUN_CARD {} → carte invalide ciblée JAMAIS en succès",
     lambda r: (r / RC).write_text("{}"), RUN_TARGET_INVALID, governed_failure)
# --- F-VRC-008 : schéma absent ou incomplet ---
case("A1-03", "schéma RUN_CARD absent → échec gouverné (sans traceback)",
     lambda r: (r / RC).unlink(), RUN_SUITE, governed_failure)
case("A1-04", "schéma RUN_CARD {\"type\":\"object\"} → suite en échec gouverné",
     lambda r: (r / RC).write_text('{"type":"object"}'), RUN_SUITE, governed_failure)
# --- F-VRC-006 : autorité de l'enum mode ---
case("A1-05", "enum mode retiré du schéma → suite rouge",
     lambda r: mutate_json(r, RC, drop_mode_enum), RUN_SUITE, governed_failure)


def bogus_card(r: Path) -> None:
    d = json.loads((r / EX).read_text(encoding="utf-8"))
    d["run_card"]["mode"] = "BOGUS-MODE"
    (r / "bogus.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    mutate_json(r, RC, drop_mode_enum)


case("A1-06", "enum mode retiré + carte BOGUS-MODE ciblée → échec gouverné",
     bogus_card, ("scripts/validate_run_card.py", "bogus.json"), governed_failure)
# --- F-VCT-001 : schémas de contrats vides ou branche non visitée ---
for i, name in enumerate(["domain_frame", "research_brief", "production_contracts"], start=7):
    case(f"A1-0{i}", f"schéma {name} {{}} → suite des contrats en échec gouverné",
         (lambda n: lambda r: (r / f"schemas/{n}.schema.json").write_text("{}"))(name), CT_SUITE, governed_failure)
case("A1-10", "mot-clé non supporté dans une branche non visitée → échec gouverné",
     lambda r: mutate_json(r, "schemas/domain_frame.schema.json", add_unused_unsupported), CT_SUITE, governed_failure)
# --- F-VCT-003 (rattachée à A1 en 11.01) : enum depth ---
case("A1-11", "enum research_brief.depth retiré → suite des contrats rouge",
     lambda r: mutate_json(r, "schemas/research_brief.schema.json", drop_depth_enum), CT_SUITE, governed_failure)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    results = []
    for cid, label, prepare, command, expect in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "pkg"
            shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist"))
            if prepare:
                prepare(root)
            code, out = run(root, *command)
            ok = bool(expect(code, out))
            tail = "TRACEBACK" if "Traceback" in out else (out.strip().splitlines() or [""])[-1][:80]
            results.append((cid, ok, label, code, tail))
    for cid, ok, label, code, tail in results:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:8} {label}  [code {code} · {tail}]")
    pos = [r for r in results if r[0].startswith("T-POS")]
    a1 = [r for r in results if r[0].startswith("A1")]
    print(f"\nTémoins positifs : {sum(r[1] for r in pos)}/{len(pos)} ; tests A1 : {sum(r[1] for r in a1)}/{len(a1)}")
    return 0 if all(r[1] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
