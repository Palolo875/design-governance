"""Validation légère et reproductible de Design Governance V1.

Le même script fonctionne depuis la distribution GitHub ou depuis l’export Local.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IS_LOCAL = (ROOT / "official").is_dir() and not (ROOT / "V1" / "official").is_dir()

MANIFEST = ROOT / "scripts" / "package_manifest.json"
try:
    import json
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("le manifest racine doit être un objet")
    EXPECTED = manifest["local" if IS_LOCAL else "github"]
    if not isinstance(EXPECTED, list) or not all(isinstance(item, str) for item in EXPECTED):
        raise ValueError("la liste de chemins du manifest est invalide")
    OFFICIAL = ROOT / ("official" if IS_LOCAL else "V1/official")
except (OSError, ValueError, KeyError, TypeError) as exc:
    print(f"PACKAGE VALIDATION FAILED — manifest illisible : {exc}")
    sys.exit(1)

STATE_VALUES = {"INTAKE", "CLASSIFIED", "SPECCED", "BUILDING", "CHECKING", "DECIDED", "CLOSED"}
ISSUE_VALUES = {"BLOCKED", "RETURNED", "RECLASSIFIED", "EXPLORATORY", "FAIL-ASSUMED", "ESCALATED", "null"}
VERDICT_VALUES = {
    "PASS",
    "PASS-WITH-RESERVATION",
    "RETURN",
    "N/A-JUSTIFIED",
    "NOT-VERIFIED",
    "ACCEPTED",
    "ACCEPTED-WITH-RESERVATION",
    "RETURN-DIRECTION",
    "EXPLORATORY",
    "SYSTEM-ESCALATION",
    "null",
}
DIRECTION_VALUES = {"HELD", "HELD-WITH-ACCEPTED-DIFFERENCE", "PARTIALLY-HELD", "LOST-IN-BUILD"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_expected_files(errors: list[str]) -> None:
    expected = set(EXPECTED)
    for relative in EXPECTED:
        if not (ROOT / relative).is_file():
            fail(errors, f"fichier attendu absent : {relative}")
    generated = {"dist", ".build", "__pycache__"}
    allowed_root_artifacts = {
        "Design_Governance_V1_GITHUB.zip",
        "Design_Governance_V1_LOCAL.zip",
    }
    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in generated for part in path.relative_to(ROOT).parts)
        and path.relative_to(ROOT).as_posix() not in allowed_root_artifacts
    }
    extras = sorted(actual - expected)
    for relative in extras:
        fail(errors, f"fichier inattendu dans le package : {relative}")


def check_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if "/dist/" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                fail(errors, f"lien relatif hors package : {path.relative_to(ROOT)} -> {target}")
            elif not resolved.is_file():
                fail(errors, f"lien relatif cassé : {path.relative_to(ROOT)} -> {target}")
            elif "#" in raw_target:
                fragment = raw_target.split("#", 1)[1]
                linked_text = resolved.read_text(encoding="utf-8")
                anchors = {heading.strip().lower().replace(" ", "-") for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*$", linked_text)}
                if fragment and fragment.lower() not in anchors:
                    fail(errors, f"fragment Markdown introuvable : {path.relative_to(ROOT)} -> {raw_target}")


def check_action_projection_source(errors: list[str]) -> None:
    """Keep the structured RUN_CARD example canonical and machine-validatable.

    ACTION.md may explain the transport contract, but it must not carry a second
    YAML/JSON projection that can drift from schemas/run_card.example.json.
    """
    action = OFFICIAL / "ACTION.md"
    if not action.is_file():
        return
    text = action.read_text(encoding="utf-8")
    if "schemas/run_card.example.json" not in text:
        fail(errors, "ACTION ne référence pas l’exemple RUN_CARD canonique")
    if re.search(r"(?m)^\s*(```|~~~)(?:yaml|yml|json)\s*$", text):
        fail(errors, "ACTION contient une projection YAML/JSON embarquée : utiliser schemas/run_card.example.json")


def check_structured_values(errors: list[str]) -> None:
    patterns = {
        "STATE": (re.compile(r"^\s*STATE:\s*([^\s`]+)"), STATE_VALUES),
        "ISSUE": (re.compile(r"^\s*ISSUE:\s*([^\s`]+)"), ISSUE_VALUES),
        "VERDICT": (re.compile(r"^\s*VERDICT:\s*([^\s`]+)"), VERDICT_VALUES),
        "DIRECTION-STATUS": (re.compile(r"^\s*DIRECTION-STATUS:\s*([^\s`]+)"), DIRECTION_VALUES),
    }
    for path in ROOT.rglob("*.md"):
        if "/dist/" in str(path):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, 1):
            for field, (pattern, allowed) in patterns.items():
                match = pattern.match(line)
                if match and match.group(1) not in allowed:
                    fail(errors, f"{field} non canonique : {path.relative_to(ROOT)}:{line_number} = {match.group(1)}")


def check_state_direction_separation(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if "/dist/" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?im)^\s*STATE:\s*HELD\b", text) or re.search(r"(?im)^\s*state:\s*HELD\b", text):
            fail(errors, f"statut de direction utilisé comme STATE : {path.relative_to(ROOT)}")


def check_canonicity_language(errors: list[str]) -> None:
    readme = (OFFICIAL / "README.md").read_text(encoding="utf-8")
    changelog = (OFFICIAL / "CHANGELOG.md").read_text(encoding="utf-8")
    if "Les cinq fichiers suivants sont les **seules sources normatives** de V1" not in readme:
        fail(errors, "la hiérarchie des sources normatives n’est pas formulée dans le README officiel")
    if "exactement sept fichiers canoniques" in changelog or "sept fichiers actifs" in changelog:
        fail(errors, "ancienne formulation contradictoire sur les fichiers canoniques")


def check_lifecycle_contract(errors: list[str]) -> None:
    changelog = (OFFICIAL / "CHANGELOG.md").read_text(encoding="utf-8")
    required_terms = ("PILOT", "ADOPTED", "DEPRECATED", "ABANDONED", "routes présentes dans le seed", "Migration des anciens aliases")
    for term in required_terms:
        if term not in changelog:
            fail(errors, f"contrat de cycle de vie incomplet dans CHANGELOG : {term}")
    for alias in ("REFERENCES/QUERY", "REFERENCES/SOURCE", "REFERENCES/ASSET", "REFERENCES/MEMORY", "REFERENCES/CORPUS"):
        if alias not in changelog:
            fail(errors, f"alias de migration absent du CHANGELOG : {alias}")

    bibliography = (OFFICIAL / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    if "section « Migration des anciens aliases » de `CHANGELOG.md`" not in bibliography:
        fail(errors, "BIBLIOTHEQUE ne pointe pas vers le propriétaire de sa migration")


def check_reading_contract(errors: list[str]) -> None:
    action = (OFFICIAL / "ACTION.md").read_text(encoding="utf-8")
    for mode in ("LITE", "ITER", "STANDARD", "DIRECTION", "SYSTÈME"):
        if f"`{mode}`" not in action:
            fail(errors, f"mode absent de la carte de lecture ACTION : {mode}")
    for term in ("Carte de lecture par mode", "RUN_CARD"):
        if term not in action:
            fail(errors, f"orientation ACTION absente : {term}")
    if "FAST-PATH" not in action or "sixième voie" not in action:
        fail(errors, "orientation ACTION absente : FAST-PATH doit être qualifié comme vue et non comme voie")

    official_readme = (OFFICIAL / "README.md").read_text(encoding="utf-8")
    if "la `RUN_CARD` rassemble" not in official_readme:
        fail(errors, "RUN_CARD insuffisamment introduite dans le README officiel")


def check_experimental_position(errors: list[str]) -> None:
    official_sources = [OFFICIAL / name for name in ("DIRECTION.md", "ACTION.md", "SAVOIR.md", "BIBLIOTHEQUE.md")]
    public_entry_docs = [
        ROOT / "README.md",
        ROOT / "RELEASE_NOTES.md",
        OFFICIAL / "README.md",
        OFFICIAL / "QUICKSTART.md",
        OFFICIAL / "CHANGELOG.md",
    ]
    marker = "expérimentation maintenue"
    for path in official_sources + [path for path in public_entry_docs if path.is_file()]:
        text = path.read_text(encoding="utf-8")
        if marker not in text.lower():
            fail(errors, f"marqueur expérimental public absent ou divergent : {path.relative_to(ROOT)}")


def check_local_autonomy(errors: list[str]) -> None:
    if not IS_LOCAL:
        return
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if re.search(r"(?i)consulter.*github|d[ée]pend.*github|depuis github", readme):
        fail(errors, "le README Local renvoie encore vers GitHub comme dépendance")


def main() -> int:
    errors: list[str] = []
    check_expected_files(errors)
    check_links(errors)
    check_action_projection_source(errors)
    check_structured_values(errors)
    check_state_direction_separation(errors)
    check_canonicity_language(errors)
    check_lifecycle_contract(errors)
    check_reading_contract(errors)
    check_experimental_position(errors)
    check_local_autonomy(errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    kind = "Local" if IS_LOCAL else "GitHub"
    print(f"VALIDATION PASSED — {kind}, {len(EXPECTED)} fichiers attendus, liens, vocabulaire et convention contrôlés")
    return 0


if __name__ == "__main__":
    sys.exit(main())

