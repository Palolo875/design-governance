#!/usr/bin/env python3
"""Orchestre les contrôles de cohérence, de projection et de distribution."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(command: list[str]) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def expect_failure(command: list[str], label: str, expected_message: str) -> None:
    """Vérifie qu’un scénario d’entrée invalide échoue réellement, et pour le motif attendu."""
    target = next((Path(part) for part in command if part.endswith(".json")), None)
    if target is not None and not target.is_absolute():
        target = ROOT / target  # E2 O-1 : chemins résolus depuis ROOT, jamais depuis le dossier courant
    if target is not None and not target.is_file() and label not in {"fichier absent", "JSON malformé"}:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} : fixture absente : {target}")
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode == 0:
        output = (result.stdout + result.stderr).strip()
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a réussi à tort : {output}")
    output = result.stdout + result.stderr
    if "Traceback (most recent call last)" in output:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a échoué par exception non gouvernée")
    if expected_message not in output:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a échoué pour un autre motif : attendu {expected_message!r}")
    print(f"+ expected failure ({label})")

def main() -> int:
    run([sys.executable, "-m", "py_compile", "scripts/validate_design_governance.py", "scripts/validate_run_card.py", "scripts/validate_all.py", "scripts/validate_contracts.py", "scripts/validate_reading_map.py", "scripts/read_route.py", "scripts/validate_structure.py", "scripts/build_core.py"])
    run([sys.executable, "scripts/validate_design_governance.py"])
    run([sys.executable, "scripts/validate_run_card.py"])
    run([sys.executable, "scripts/validate_contracts.py"])
    run([sys.executable, "scripts/validate_reading_map.py"])
    run([sys.executable, "scripts/validate_structure.py"])
    run([sys.executable, "scripts/read_route.py", "DIRECTION/START"])
    expect_failure(
        [sys.executable, "scripts/read_route.py", "DIRECTION/UNKNOWN"],
        "locator inconnu",
        "locator inconnu : DIRECTION/UNKNOWN",
    )
    run([sys.executable, "scripts/validate_contracts.py", "schemas/examples/domain_frame.example.json"])
    run([sys.executable, "scripts/validate_run_card.py", "schemas/run_card.example.json"])
    for fixture, motif in (
        ("invalid_capability_profile_missing_basis.json", "capability_profile exige basis non vide"),
        ("invalid_accepted_lost_in_build.json", "LOST-IN-BUILD ne peut pas produire un verdict accepté"),
        ("invalid_critical_without_protection.json", "un risque critical exige une critical_protection structurée"),
        ("invalid_critical_placeholder_protection.json", "critical_protection.control ne peut pas être un placeholder"),
    ):
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", f"schemas/fixtures/{fixture}"],
            fixture,
            motif,
        )
    with tempfile.TemporaryDirectory(prefix="design-governance-cli-") as temp_dir:
        temp = Path(temp_dir)
        strict_card = temp / "strict_card.json"
        strict_card.write_text((ROOT / "schemas/run_card.example.json").read_text(encoding="utf-8").replace("chemin-ou-url-local", (ROOT / "schemas/run_card.example.json").as_posix()).replace("ticket-ou-chemin-de-run", (ROOT / "schemas/run_card.example.json").as_posix()), encoding="utf-8")
        run([sys.executable, "scripts/validate_run_card.py", "--strict", str(strict_card)])
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", "--strict", "schemas/run_card.example.json"],
            "strict placeholder",
            "strict : placeholder",
        )
        malformed = temp / "malformed.json"
        malformed.write_text('{"run_card":', encoding="utf-8")
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", str(malformed)],
            "JSON malformé",
            "lecture JSON impossible",
        )
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", str(temp / "missing.json")],
            "fichier absent",
            "lecture JSON impossible",
        )
    build_script = ROOT / "scripts/build_distributions.sh"
    if not build_script.is_file():
        print("LOCAL VALIDATION PASSED — contrôles documentaires, RUN_CARD et CLI ; build et reproductibilité hors périmètre de l’export Local")
        return 0
    run(["bash", "scripts/build_distributions.sh"])
    github = ROOT / "Design_Governance_V1_GITHUB.zip"
    local = ROOT / "Design_Governance_V1_LOCAL.zip"
    first = (sha256(github), sha256(local))
    run(["bash", "scripts/build_distributions.sh"])
    second = (sha256(github), sha256(local))
    if first != second:
        raise SystemExit("REPRODUCIBILITY FAILED — les archives diffèrent entre deux builds")
    print("FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

