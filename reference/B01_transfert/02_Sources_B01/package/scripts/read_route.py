#!/usr/bin/env python3
"""Resolve a documented route and print only its owning section."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
MAP = OFFICIAL / "READING_MAP.md"


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ROUTE READ FAILED — {message}")


def parse_routes(text: str) -> dict[str, tuple[str, str]]:
    if "## Locators principaux" not in text:
        fail("section des locators principaux absente")
    section = text.split("## Locators principaux", 1)[1]
    if "## Condition d’arrêt" in section:
        section = section.split("## Condition d’arrêt", 1)[0]
    routes: dict[str, tuple[str, str]] = {}
    for line in section.splitlines():
        if not line.startswith("| `") or " | `" not in line or not line.endswith(" |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        locator_cell, destination = cells
        if not (locator_cell.startswith("`") and locator_cell.endswith("`")):
            continue
        match = re.fullmatch(r"`([^`]+)`\s+—\s+`(.+)`", destination)
        if not match:
            fail(f"destination mal formée pour {locator_cell}")
        owner_name, heading = match.groups()
        routes[locator_cell[1:-1]] = (owner_name, heading.replace("\\`", "`"))
    return routes


def read_block(path: Path, heading: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        fail(f"titre introuvable dans {path.relative_to(ROOT)} : {heading}")
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if line.startswith("#"):
            current = len(line) - len(line.lstrip("#"))
            if current <= level:
                end = i
                break
    return lines[start:end]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Charge le bloc exact d’un locator READING_MAP.")
    parser.add_argument("locator", help="locator, par exemple DIRECTION/START")
    args = parser.parse_args(argv)
    if not MAP.is_file():
        fail("READING_MAP.md absent")
    routes = parse_routes(MAP.read_text(encoding="utf-8"))
    if args.locator not in routes:
        available = ", ".join(sorted(routes))
        fail(f"locator inconnu : {args.locator}; disponibles : {available}")
    owner_name, heading = routes[args.locator]
    owner = OFFICIAL / owner_name
    if not owner.is_file():
        fail(f"propriétaire absent : {owner_name}")
    block = read_block(owner, heading)
    print(f"ROUTE: {args.locator}")
    print(f"OWNER: {owner.relative_to(ROOT)}")
    print(f"HEADING: {heading}")
    print("---")
    print("\n".join(block))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

