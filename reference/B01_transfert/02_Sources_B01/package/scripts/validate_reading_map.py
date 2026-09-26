#!/usr/bin/env python3
"""Validate the derived reading and multi-perspective map without creating authority."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
MAP = OFFICIAL / "READING_MAP.md"
REQUIRED = (
    "Statut :** guide dérivé non normatif",
    "## Chemin canonique de démarrage",
    "## Routage minimal par décision",
    "## Activation multi-perspective",
    "## Handoff minimal commun",
    "## Résolution des routes",
    "## Locators principaux",
    "DIRECTION/START",
    "ACTION/RUN-LITE",
    "ACTION/CLOSE-EXIT-CHECK",
    "SAVOIR/ROUTING",
    "BIBLIOTHEQUE/SELECT",
    "## Condition d’arrêt",
    "N/A-JUSTIFIED",
    "NOT-VERIFIED",
)
OWNER_MAP = {
    "DIRECTION/*": OFFICIAL / "DIRECTION.md",
    "ACTION/*": OFFICIAL / "ACTION.md",
    "SAVOIR/*": OFFICIAL / "SAVOIR.md",
    "BIBLIOTHEQUE/*": OFFICIAL / "BIBLIOTHEQUE.md",
    "CHANGELOG/*": OFFICIAL / "CHANGELOG.md",
}


def fail(message: str) -> None:
    raise SystemExit(f"READING MAP VALIDATION FAILED — {message}")


def check_locator_destinations(text: str) -> None:
    """Ensure every listed locator resolves to the exact heading it names."""
    if "## Locators principaux" not in text:
        fail("section des locators principaux absente")
    text = text.split("## Locators principaux", 1)[1]
    if "## Condition d’arrêt" in text:
        text = text.split("## Condition d’arrêt", 1)[0]
    rows = []
    for line in text.splitlines():
        if not line.startswith("| `") or " | `" not in line or not line.endswith(" |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2 or not cells[0].startswith("`") or not cells[0].endswith("`"):
            continue
        locator = cells[0][1:-1]
        destination = cells[1]
        match = re.fullmatch(r"`([^`]+)`\s+—\s+`(.+)`", destination)
        if not match:
            fail(f"destination de locator mal formée : {locator}")
        owner_name, heading = match.groups()
        owner_name = owner_name.strip()
        heading = heading.strip().replace("\\`", "`")
        owner = OFFICIAL / owner_name
        if not owner.is_file():
            fail(f"fichier propriétaire absent pour {locator} : {owner_name}")
        headings = {line.strip() for line in owner.read_text(encoding="utf-8").splitlines() if line.lstrip().startswith("#")}
        if heading not in headings:
            fail(f"titre de locator introuvable : {locator} -> {owner_name} — {heading}")
        rows.append(locator)
    if len(rows) < 10:
        fail("table des locators principaux incomplète ou illisible")


def main() -> int:
    if not MAP.is_file():
        fail("READING_MAP.md absent")
    text = MAP.read_text(encoding="utf-8")
    for item in REQUIRED:
        if item not in text:
            fail(f"élément obligatoire absent : {item}")
    for route, owner in OWNER_MAP.items():
        if route not in text:
            fail(f"propriétaire de route absent : {route}")
        if not owner.is_file():
            fail(f"fichier propriétaire absent : {owner}")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not target:
            continue
        if not (MAP.parent / target).exists():
            fail(f"lien relatif non résolu : {target}")
    check_locator_destinations(text)
    # The map must remain derived and cannot introduce a competing classifier.
    if "source" not in text or "normative" not in text or "ne reclassifie pas" not in text:
        fail("frontière de non-autorité ou de non-reclassification absente")
    print("READING MAP VALIDATION PASSED — carte dérivée, propriétaires, handoff et liens contrôlés")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

