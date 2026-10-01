#!/usr/bin/env python3
"""Audit progressif, unité AP4a — sondes directes des validateurs (C11, C12, C13, C19, C20, C21), sur copie.

Chaque scénario prépare une copie du package, y introduit UNE faute (ou une valeur légitime) et observe la commande :
code de sortie, message gouverné (bannière, sans trace Python) et motif attendu.
Usage : python3 V12R_Sonde_AP4a.py <racine_package> [--outil-1301 <chemin>]   (par défaut, l'outil 13.01 courant)
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))
    print(f"  {'OK' if ok else 'KO'}  {name}{' — ' + detail if detail else ''}")


def fresh(root: Path, tmp: Path, name: str) -> Path:
    dest = tmp / name
    shutil.copytree(root, dest, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
    return dest


def run(pkg: Path, *args: str, env: dict | None = None) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", *args], cwd=pkg, capture_output=True, text=True, env=env)
    return out.returncode, out.stdout + out.stderr


def governed(code: int, out: str, motif: str) -> tuple[bool, str]:
    last = out.strip().splitlines()[-1] if out.strip() else ""
    ok = code != 0 and "Traceback" not in out and motif in out
    return ok, last[:140]


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text, f"ancre introuvable dans {path.name} : {old[:50]}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sonde_c11(root: Path, tmp: Path) -> None:
    print("C11 — lecteur de routes autonome")
    pkg = fresh(root, tmp, "c11_legit")
    for route in ("DIRECTION/START", "DIRECTION/START/TREE", "ACTION/RUN_CARD", "SAVOIR/CRAFT/CFT-01", "DIRECTION/CHARGE"):
        code, out = run(pkg, "scripts/read_route.py", route)
        check(f"route légitime servie : {route}", code == 0 and out.startswith(f"ROUTE: {route}"))
    rmap = "V1/official/READING_MAP.md"
    text = (root / rmap).read_text(encoding="utf-8")
    row = next(line for line in text.splitlines() if line.startswith("| `DIRECTION/START` |"))
    # Fautes qui résolvent en silence sur un lecteur sans contrôle : destination réelle, mais autre que celle du locator.
    other = next(line for line in text.splitlines() if line.startswith("| `DIRECTION/FIRST-OBJECT` |"))
    foreign = next(line for line in text.splitlines() if line.startswith("| `SAVOIR/CRAFT` |"))
    pkg = fresh(root, tmp, "c11_double")
    edit(pkg / rmap, row, row + "\n" + "| `DIRECTION/START` |" + other.split("|", 2)[2])
    ok, last = governed(*run(pkg, "scripts/read_route.py", "DIRECTION/START"), "locator en double")
    check("locator répété dans la table refusé (seconde ligne vers un autre titre réel)", ok, last)
    pkg = fresh(root, tmp, "c11_proprietaire")
    edit(pkg / rmap, row, "| `DIRECTION/START` |" + foreign.split("|", 2)[2])
    ok, last = governed(*run(pkg, "scripts/read_route.py", "DIRECTION/START"), "propriétaire incohérent")
    check("propriétaire incohérent refusé (ligne vers un titre réel de SAVOIR)", ok, last)
    pkg = fresh(root, tmp, "c11_porteur")
    path = pkg / "V1/official/DIRECTION.md"
    path.write_text(path.read_text(encoding="utf-8") + "\n## DIRECTION/START — copie parasite\n\nTexte.\n", encoding="utf-8")
    ok, last = governed(*run(pkg, "scripts/read_route.py", "DIRECTION/START"), "locator ambigu")
    check("second titre porteur du locator refusé (route par la table)", ok, last)


def sonde_c12(root: Path, tmp: Path) -> None:
    print("C12 — clés JSON répétées")
    pkg = fresh(root, tmp, "c12")
    brief = json.loads((pkg / "schemas/examples/research_brief.example.json").read_text(encoding="utf-8"))
    raw = json.dumps(brief, ensure_ascii=False)
    depth = json.dumps(brief["depth"], ensure_ascii=False)
    duplicated = raw.replace(f'"depth": {depth}', f'"depth": "IMPOSSIBLE", "depth": {depth}', 1)
    target = tmp / "brief_double.json"
    target.write_text(duplicated, encoding="utf-8")
    ok, last = governed(*run(pkg, "scripts/validate_contracts.py", str(target)), "clé répétée : depth")
    check("contrat : clé répétée refusée (depth IMPOSSIBLE puis valide)", ok, last)
    code, out = run(pkg, "scripts/validate_contracts.py")
    check("suite des contrats verte, témoin de clé répétée compris", code == 0 and "clés répétées refusées : 1/1" in out,
          out.strip().splitlines()[-1][:100])
    manifest = pkg / "scripts/package_manifest.json"
    text = manifest.read_text(encoding="utf-8")
    manifest.write_text(text.replace('"version":', '"version": "0.0.0", "version":', 1), encoding="utf-8")
    ok, last = governed(*run(pkg, "scripts/validate_design_governance.py"), "clé répétée : version")
    check("manifeste : clé répétée refusée", ok, last)


def sonde_c13(root: Path, tmp: Path) -> None:
    print("C13 — mot-clé de schéma RUN_CARD non pris en charge")
    pkg = fresh(root, tmp, "c13")
    code, out = run(pkg, "scripts/validate_run_card.py")
    check("suite RUN_CARD verte, témoin C13 compris", code == 0 and "mot-clé de schéma non pris en charge refusé : 1/1" in out)
    edit(pkg / "schemas/run_card.schema.json", '"id": {"type": "string", "minLength": 1}',
         '"id": {"type": "string", "minLength": 1, "pattern": "^RUN-"}')
    ok, last = governed(*run(pkg, "scripts/validate_run_card.py"), "mot-clé non pris en charge")
    check("schéma livré avec pattern : refusé avant toute validation", ok, last)


def card_variant(root: Path, tmp: Path, name: str, change) -> Path:
    doc = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    change(doc["run_card"])
    path = tmp / f"{name}.json"
    path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return path


def sonde_c19(root: Path, tmp: Path) -> None:
    print("C19 — dates et heures réelles")
    pkg = fresh(root, tmp, "c19")

    def at(value):
        return lambda card: card["proof"]["provenance"].__setitem__("observed_at", value)
    for value, admitted in (("2026-08-29T25:61", False), ("2026-08-29T10:00+25:00", False), ("2026-02-30", False),
                            ("2026-08-29T10:00:00Z", True), ("2026-08-29T23:59+01:00", True), ("2026-08-29", True)):
        code, out = run(pkg, "scripts/validate_run_card.py", str(card_variant(root, tmp, "c19", at(value))))
        ok = code == 0 if admitted else governed(code, out, "observed_at doit être une date ISO")[0]
        check(f"RUN_CARD observed_at « {value} » {'admis' if admitted else 'refusé'}", ok)
    brief = json.loads((pkg / "schemas/examples/research_brief.example.json").read_text(encoding="utf-8"))
    for value, admitted in (("2026-02-30", False), ("2026-13", False), ("2026", True), ("2026-09", True), ("2026-09-30", True),
                            ("unknown", True)):
        doc = json.loads(json.dumps(brief))
        entry = doc["entries"][0]
        entry["source_date"] = value
        entry["source_status"] = "user_source_unverified"  # « unknown » n'est recevable que hors verified_in_run
        path = tmp / "brief_date.json"
        path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        code, out = run(pkg, "scripts/validate_contracts.py", str(path))
        ok = code == 0 if admitted else governed(code, out, "source_date doit être ISO")[0]
        check(f"contrat source_date « {value} » {'admis' if admitted else 'refusé'}", ok, "" if ok else out.strip().splitlines()[-1][:100])


def sonde_c20(root: Path, tmp: Path) -> None:
    print("C20 — diagnostics gouvernés au lieu d'erreurs brutes")
    pkg = fresh(root, tmp, "c20")
    path = card_variant(root, tmp, "c20_issue", lambda card: card["closure"].__setitem__("issue", []))
    ok, last = governed(*run(pkg, "scripts/validate_run_card.py", str(path)), "type attendu")
    check("RUN_CARD closure.issue = [] : diagnostic, pas de trace", ok, last)
    schema = pkg / "schemas/domain_frame.schema.json"
    original = schema.read_text(encoding="utf-8")
    schema.write_text("[]", encoding="utf-8")
    doc = tmp / "frame.json"
    doc.write_text((pkg / "schemas/examples/domain_frame.example.json").read_text(encoding="utf-8"), encoding="utf-8")
    ok, last = governed(*run(pkg, "scripts/validate_contracts.py", str(doc)), "schéma inopérant")
    check("contrat : schéma [] à la détection de type : diagnostic, pas de trace", ok, last)
    schema.write_text(original, encoding="utf-8")
    md = pkg / "V1/official/DIRECTION.md"
    md.write_bytes(md.read_bytes() + b"\xff\xfe")
    for command in (["scripts/read_route.py", "DIRECTION/START"], ["scripts/validate_reading_map.py"],
                    ["scripts/validate_structure.py"], ["scripts/build_core.py", "--check"],
                    ["scripts/validate_design_governance.py"]):
        ok, last = governed(*run(pkg, *command), "V1/official/DIRECTION.md")
        check(f"Markdown non UTF-8 nommé : {command[0].split('/')[-1]}", ok and "non UTF-8" in last, last)


def sonde_c21(root: Path, tmp: Path, tool: Path) -> None:
    print("C21 — 13.01 distributions sans Python 3.10 ni 3.13")
    pkg = fresh(root, tmp, "c21")
    code, out = subprocess.run(["bash", "scripts/build_distributions.sh"], cwd=pkg, capture_output=True, text=True).returncode, ""
    check("build de la copie", code == 0)
    if code:
        return
    bindir = tmp / "bin_sans_310_313"
    bindir.mkdir()
    (bindir / "python3").symlink_to(sys.executable)
    env = dict(os.environ, PATH=str(bindir))
    out = subprocess.run([sys.executable, str(tool), "distributions", str(pkg / "Design_Governance_V1_GITHUB.zip"),
                          str(pkg / "Design_Governance_V1_LOCAL.zip")], capture_output=True, text=True, env=env).stdout
    rows = {line.split()[1] + (" " + line.split()[2] if line.split()[1] == "D-4" else ""): line.split()[0]
            for line in out.splitlines() if line.startswith(("OK", "ÉCHEC", "INDISP."))}
    check("D-4 (github) contrôlé sans interpréteur", rows.get("D-4 (github)") == "OK", f"statut {rows.get('D-4 (github)')}")
    check("D-4 (local) contrôlé sans interpréteur", rows.get("D-4 (local)") == "OK", f"statut {rows.get('D-4 (local)')}")
    check("interpréteurs absents marqués non exécutés (pas OK)", all(rows.get(k) == "INDISP." for k in ("D-python3.10", "D-python3.13")),
          f"{rows.get('D-python3.10')}, {rows.get('D-python3.13')}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    tool = Path(sys.argv[sys.argv.index("--outil-1301") + 1]).resolve() if "--outil-1301" in sys.argv \
        else TOOLS / "DG_AUDIT_001_Verifications_13-01.py"
    with tempfile.TemporaryDirectory(prefix="sonde-ap4a-") as tmp_dir:
        tmp = Path(tmp_dir)
        for sonde in (sonde_c11, sonde_c12, sonde_c13, sonde_c19, sonde_c20):
            sonde(root, tmp)
        sonde_c21(root, tmp, tool)
    bad = sum(1 for _, ok, _ in results if not ok)
    print(f"SONDE AP4a : {'VERTE' if not bad else f'ROUGE ({bad})'} — {len(results) - bad}/{len(results)} contrôles")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
