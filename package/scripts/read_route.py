#!/usr/bin/env python3
"""Resolve a documented route and print only its owning section.

Résolution en trois étapes (READING_MAP, « Résolution des routes ») :
1. table « Locators principaux » (raccourcis et sous-locators) ;
2. préfixe : titre unique du propriétaire qui commence par le locator ;
3. sous-locator X/Y/Z : sous-titre commençant par Z dans le bloc de X/Y.
Plusieurs titres : « locator ambigu ». Les titres placés dans un bloc de code sont
ignorés. Un bloc servi exclut les sous-blocs qui portent leur propre locator.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
MAP = OFFICIAL / "READING_MAP.md"
PREFIXES = ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG")
HEADING_LOCATOR = re.compile(rf"^#+\s+`?((?:{'|'.join(PREFIXES)})/[A-Za-z0-9_\-]+)`?(?=\s|$)")


class RouteError(Exception):
    """Échec de résolution gouverné."""


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ROUTE READ FAILED — {message}")


def parse_route_rows(text: str) -> list[tuple[str, str, list[str]]]:
    """Lignes de la table : (locator, fichier propriétaire, chaîne de titres). Les doublons sont conservés."""
    if "## Locators principaux" not in text:
        raise RouteError("section des locators principaux absente")
    section = text.split("## Locators principaux", 1)[1]
    if "## Condition d’arrêt" in section:
        section = section.split("## Condition d’arrêt", 1)[0]
    rows: list[tuple[str, str, list[str]]] = []
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
            raise RouteError(f"destination mal formée pour {locator_cell}")
        owner_name, chain = match.groups()
        headings = [part.replace("\\`", "`").strip() for part in re.split(r"`\s+›\s+`", chain)]
        rows.append((locator_cell[1:-1], owner_name.strip(), headings))
    return rows


def parse_routes(text: str) -> dict[str, tuple[str, list[str]]]:
    return {locator: (owner, chain) for locator, owner, chain in parse_route_rows(text)}


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """(index, niveau, ligne) des titres, hors blocs de code (F-RRT-001)."""
    found, fence = [], None
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            fence = None if fence == marker else (fence or marker)
            continue
        if fence is None and line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            if level <= 6 and line[level:level + 1] in (" ", ""):
                found.append((index, level, line.strip()))
    return found


def heading_locator(heading: str) -> str | None:
    match = HEADING_LOCATOR.match(heading)
    return match.group(1) if match else None


def block_end(lines: list[str], heads: list[tuple[int, int, str]], start: int) -> int:
    level = next(lvl for idx, lvl, _ in heads if idx == start)
    return next((idx for idx, lvl, _ in heads if idx > start and lvl <= level), len(lines))


def owner_file(locator: str) -> Path:
    prefix = locator.split("/", 1)[0]
    if prefix not in PREFIXES:
        raise RouteError(f"locator inconnu : {locator}")
    return OFFICIAL / f"{prefix}.md"


def _unique(candidates: list[int], lines: list[str], locator: str) -> int:
    if len(candidates) > 1:
        shown = " | ".join(lines[i].strip() for i in candidates)
        raise RouteError(f"locator ambigu : {locator} ; candidats : {shown}")
    return candidates[0]


def resolve(locator: str, routes: dict[str, tuple[str, list[str]]] | None = None) -> tuple[Path, list[str], int]:
    """Renvoie (fichier, lignes, index du titre servi)."""
    if routes is None:
        if not MAP.is_file():
            raise RouteError("READING_MAP.md absent")
        routes = parse_routes(MAP.read_text(encoding="utf-8"))
    if locator in routes:  # 1. table
        owner_name, chain = routes[locator]
        path = OFFICIAL / owner_name
        if not path.is_file():
            raise RouteError(f"propriétaire absent : {owner_name}")
        lines = path.read_text(encoding="utf-8").splitlines()
        heads = headings(lines)
        low, high, index = 0, len(lines), -1
        for heading in chain:
            candidates = [idx for idx, _, text in heads if low <= idx < high and text == heading]
            if not candidates:
                raise RouteError(f"titre introuvable dans {owner_name} : {heading}")
            index = _unique(candidates, lines, locator)
            low, high = index + 1, block_end(lines, heads, index)
        return path, lines, index
    path = owner_file(locator)
    if not path.is_file():
        raise RouteError(f"propriétaire absent : {path.name}")
    lines = path.read_text(encoding="utf-8").splitlines()
    heads = headings(lines)
    candidates = [idx for idx, _, text in heads if heading_locator(text) == locator]  # 2. préfixe
    if candidates:
        return path, lines, _unique(candidates, lines, locator)
    parent, _, leaf = locator.rpartition("/")
    if parent.count("/") >= 1:  # 3. sous-locator X/Y/Z
        parent_path, parent_lines, parent_index = resolve(parent, routes)
        if parent_path == path:
            end = block_end(lines, heads, parent_index)
            pattern = re.compile(rf"^#+\s+`?{re.escape(leaf)}`?(?=\s|$)")
            sub = [idx for idx, _, text in heads if parent_index < idx < end and pattern.match(text)]
            if sub:
                return path, lines, _unique(sub, lines, locator)
    raise RouteError(f"locator inconnu : {locator}")


CONCEPT_MARKER = re.compile(r"^\s*<!-- concept:[A-Z0-9\-]+ -->\s*$")


def extract(lines: list[str], index: int) -> list[str]:
    """Bloc du titre servi, sans les sous-blocs porteurs de leur propre locator."""
    heads = headings(lines)
    end = block_end(lines, heads, index)
    served, skip_until = [], -1
    for i in range(index, end):
        if i < skip_until:
            continue
        head = next((text for idx, _, text in heads if idx == i), None)
        own = heading_locator(head) if head and i != index else None
        if own:
            served.append(f"> `{own}` : servi séparément")
            skip_until = block_end(lines, heads, i)
            continue
        if CONCEPT_MARKER.match(lines[i]):
            continue
        served.append(lines[i])
    return served


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Charge le bloc exact d’un locator READING_MAP.")
    parser.add_argument("locator", help="locator, par exemple DIRECTION/START ou SAVOIR/CRAFT/CFT-01")
    args = parser.parse_args(argv)
    try:
        path, lines, index = resolve(args.locator)
    except RouteError as exc:
        fail(str(exc))
    print(f"ROUTE: {args.locator}")
    print(f"OWNER: {path.relative_to(ROOT)}")
    print(f"HEADING: {lines[index].strip()}")
    print("---")
    print("\n".join(extract(lines, index)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
