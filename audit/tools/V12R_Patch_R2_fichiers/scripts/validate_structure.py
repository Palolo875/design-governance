#!/usr/bin/env python3
"""Validateur de structure : gardes de propriété « une chose, un lieu ».

Un concept protégé est repéré par une balise invisible `<!-- concept:ID -->` placée juste avant sa
définition, dans son fichier propriétaire. La garde vérifie, pour chaque concept du registre :
  1. la balise existe une seule fois dans l'ensemble des textes du package ;
  2. elle se trouve dans le fichier propriétaire ;
  3. le bloc qui la suit (jusqu'à la ligne vide) n'est pas vide (au moins 12 mots).
Elle refuse aussi toute balise dont l'identifiant n'est pas au registre.

Une reformulation du concept ne casse pas la garde ; sa suppression, son déplacement ou sa copie la
cassent. `scripts/read_route.py` retire les balises à la lecture.

Usage : python3 scripts/validate_structure.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
SKILL_DIR = ROOT / "skills" / "design-governance-practice" if (ROOT / "skills").is_dir() else ROOT / "skill"
MARKER = re.compile(r"^\s*<!-- concept:([A-Z0-9][A-Z0-9\-]*) -->\s*$")
MIN_WORDS = 12

# Registre des concepts protégés : identifiant, fichier propriétaire, propriété.
CONCEPTS: list[tuple[str, str, str]] = [
    ("HON-01", "DIRECTION.md", "vérité de scène : exemples marqués, divulgation en langage produit"),
    ("HON-02", "SAVOIR.md", "aucun faux asset présenté comme authentique"),
    ("HON-03", "DIRECTION.md", "plafond déclaré quand une capacité manque (FABRICATION)"),
    ("HON-04", "ACTION.md", "frontière de validation : ce que la machine atteste et n'atteste pas"),
    ("HON-05", "ACTION.md", "agent seul : preuve dégradée et conclusions interdites"),
    ("HON-06", "ACTION.md", "NOT-VERIFIED plutôt qu'un PASS sans preuve"),
    ("HON-07", "ACTION.md", "une capture prouve un rendu, pas une tâche"),
    ("HON-08", "ACTION.md", "droit inconnu : ACCEPTED interdit"),
]


def texts() -> dict[Path, list[str]]:
    files = sorted(OFFICIAL.glob("*.md")) + sorted(SKILL_DIR.rglob("*.md"))
    readme = ROOT / "README.md"
    if readme.is_file():
        files.append(readme)
    return {p: p.read_text(encoding="utf-8").splitlines() for p in files}


def check() -> list[str]:
    errors: list[str] = []
    found: dict[str, list[tuple[Path, int]]] = {}
    corpus = texts()
    for path, lines in corpus.items():
        for i, line in enumerate(lines):
            m = MARKER.match(line)
            if m:
                found.setdefault(m.group(1), []).append((path, i))
    known = {cid for cid, _, _ in CONCEPTS}
    for cid in sorted(set(found) - known):
        errors.append(f"balise hors registre : {cid}")
    for cid, owner, prop in CONCEPTS:
        places = found.get(cid, [])
        if not places:
            errors.append(f"{cid} absent ({prop})")
            continue
        if len(places) > 1:
            where = ", ".join(f"{p.name}:{i + 1}" for p, i in places)
            errors.append(f"{cid} défini {len(places)} fois : {where}")
            continue
        path, i = places[0]
        if path.name != owner or path.parent != OFFICIAL:
            errors.append(f"{cid} hors de son fichier propriétaire ({owner}) : {path.name}")
            continue
        block = []
        for line in corpus[path][i + 1:]:
            if not line.strip():
                break
            block.append(line)
        if len(" ".join(block).split()) < MIN_WORDS:
            errors.append(f"{cid} : bloc vide ou trop court après la balise ({owner}:{i + 1})")
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("STRUCTURE VALIDATION FAILED — gardes de propriété")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"STRUCTURE VALIDATION PASSED — {len(CONCEPTS)} concepts protégés, uniques et à leur lieu propriétaire")
    return 0


if __name__ == "__main__":
    sys.exit(main())
