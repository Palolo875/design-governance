#!/usr/bin/env python3
"""Validateur de structure : gardes de propriété « une chose, un lieu ».

Gardes :
  1. CONCEPTS — un concept protégé est repéré par une balise invisible `<!-- concept:ID -->` placée juste
     avant sa définition. La balise existe une seule fois, dans le fichier propriétaire, suivie d'un bloc
     non vide (au moins 12 mots) ; toute balise hors registre est refusée.
  2. RENVOIS — une route qui dépend d'un concept cite un locator dont le bloc servi contient ce concept
     (atteignabilité en un saut).
  3. VOCABULAIRE RETIRÉ — un terme remplacé par décision n'apparaît plus hors de l'historique (CHANGELOG).
  4. FIDÉLITÉ DES RÉSUMÉS — tout lieu qui résume une règle en garde la condition canonique.
  5. GLOSSAIRE — chaque terme du vocabulaire de fabrication a sa ligne dans GLOSSAIRE.md.
  6. LIGNES DE TABLE UNIQUES — dans un même fichier, deux lignes de table d'au moins 8 mots ne sont pas identiques.
  7. REGISTRE — les façades humaines vouvoient (formes de tutoiement impératif refusées dans QUICKSTART).

Une reformulation ne casse pas ces gardes ; une suppression, un déplacement, une copie ou un retour du
vocabulaire retiré les cassent. `scripts/read_route.py` retire les balises à la lecture.

Usage : python3 scripts/validate_structure.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import read_route as rr  # noqa: E402

OFFICIAL = rr.OFFICIAL
SKILL_DIR = ROOT / "skills" / "design-governance-practice" if (ROOT / "skills").is_dir() else ROOT / "skill"
MARKER = re.compile(r"^\s*<!-- concept:([A-Z0-9][A-Z0-9\-]*) -->\s*$")
LOCATOR = re.compile(r"`((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/[A-Z0-9_\-]+(?:/[A-Z0-9_\-]+)?)`")
MIN_WORDS = 12

# 1. Registre des concepts protégés : identifiant, fichier propriétaire, propriété.
CONCEPTS: list[tuple[str, str, str]] = [
    ("HON-01", "DIRECTION.md", "vérité de scène : exemples marqués, divulgation en langage produit"),
    ("HON-02", "SAVOIR.md", "aucun faux asset présenté comme authentique"),
    ("HON-03", "DIRECTION.md", "plafond déclaré quand une capacité manque (FABRICATION)"),
    ("HON-04", "ACTION.md", "frontière de validation : ce que la machine atteste et n'atteste pas"),
    ("HON-05", "ACTION.md", "agent seul : preuve dégradée et conclusions interdites"),
    ("HON-06", "ACTION.md", "NOT-VERIFIED plutôt qu'un PASS sans preuve"),
    ("HON-07", "ACTION.md", "une capture prouve un rendu, pas une tâche"),
    ("HON-08", "ACTION.md", "droit inconnu : ACCEPTED interdit"),
    ("ANT-01", "SAVOIR.md", "marqueurs de vague datés, pour nommer MODAL"),
    ("MOY-01", "SAVOIR.md", "carte des moyens par couche"),
]

# 2. Renvois : la route cite un locator dont le bloc contient le concept.
REFERENCES: list[tuple[str, str]] = [
    ("DIRECTION/CREATIVE-BOOT", "ANT-01"),
    ("DIRECTION/VISUAL_TARGET", "MOY-01"),
]

# 3. Vocabulaire retiré : motif, remplacement, fichiers exemptés (historique).
RETIRED: list[tuple[str, str, set[str]]] = [
    (r"anti-directions?", "MODAL / PARTI", {"CHANGELOG.md"}),
]

# 4. Fidélité des résumés : tout paragraphe qui contient le déclencheur contient la condition canonique.
FIDELITY: list[tuple[str, str, str]] = [
    ("prise de brief", r"au plus trois", "destination si elle est incertaine"),
]

# 5. Termes du vocabulaire de fabrication présents dans GLOSSAIRE.md (première cellule d'une ligne de table).
GLOSSARY_TERMS = ["Thèse", "Ancre", "Creative Boot", "MODAL", "PARTI", "FABRICATION", "Plafond",
                  "Objet de preuve", "Défaut dominant", "Vérité de scène", "Slop"]

# 7. Registre des façades humaines : formes de tutoiement impératif refusées.
REGISTER_FILES = ["QUICKSTART.md"]
TUTOIEMENT = re.compile(r"\b(?:ne confonds|utilise le|Charge `|active `|Augmente la|ajoute le|garde en tête|reste sur)\b")


def texts() -> dict[Path, list[str]]:
    files = sorted(OFFICIAL.glob("*.md")) + sorted(SKILL_DIR.rglob("*.md"))
    readme = ROOT / "README.md"
    if readme.is_file():
        files.append(readme)
    return {p: p.read_text(encoding="utf-8").splitlines() for p in files}


def paragraphs(lines: list[str]) -> list[str]:
    out, buf = [], []
    for line in lines:
        if not line.strip():
            if buf:
                out.append(" ".join(buf))
            buf = []
        else:
            buf.append(line)
    if buf:
        out.append(" ".join(buf))
    return out


def check_concepts(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    found: dict[str, list[tuple[Path, int]]] = {}
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


def raw_block(locator: str) -> list[str]:
    path, lines, index = rr.resolve(locator)
    return lines[index:rr.block_end(lines, rr.headings(lines), index)]


def check_references(errors: list[str]) -> None:
    for route, cid in REFERENCES:
        try:
            path, lines, index = rr.resolve(route)
        except rr.RouteError as exc:
            errors.append(f"renvoi {route} → {cid} : route introuvable ({exc})")
            continue
        served = "\n".join(rr.extract(lines, index))
        hit = False
        for loc in sorted(set(LOCATOR.findall(served))):
            try:
                block = raw_block(loc)
            except rr.RouteError:
                continue
            if any(MARKER.match(l) and MARKER.match(l).group(1) == cid for l in block):
                hit = True
                break
        if not hit:
            errors.append(f"renvoi {route} → {cid} : aucun locator cité par la route ne mène au concept")


def check_retired(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for pattern, repl, exempt in RETIRED:
        rx = re.compile(pattern, re.I)
        for path, lines in corpus.items():
            if path.name in exempt:
                continue
            for i, line in enumerate(lines):
                if rx.search(line):
                    errors.append(f"vocabulaire retiré « {pattern} » ({repl}) : {path.name}:{i + 1}")


def check_fidelity(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for name, trigger, needle in FIDELITY:
        rx = re.compile(trigger, re.I)
        for path, lines in corpus.items():
            for para in paragraphs(lines):
                if rx.search(para) and needle not in para:
                    errors.append(f"résumé infidèle ({name}) : {path.name} « {para[:70]}… » sans « {needle} »")


def cell(text: str) -> str:
    return re.sub(r"[`*]", "", text).strip()


def check_glossary(errors: list[str]) -> None:
    g = OFFICIAL / "GLOSSAIRE.md"
    heads = set()
    for line in g.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("|"):
            parts = line.split("|")
            if len(parts) > 2:
                heads.add(cell(parts[1]))
    for term in GLOSSARY_TERMS:
        if term not in heads:
            errors.append(f"glossaire : terme absent « {term} »")


def check_unique_rows(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for path, lines in corpus.items():
        seen: dict[str, int] = {}
        for i, line in enumerate(lines):
            if not line.lstrip().startswith("|") or re.match(r"^\s*\|[\s\-:|]+\|\s*$", line):
                continue
            key = re.sub(r"[`*\s|]+", " ", line).strip().lower()
            if len(key.split()) < 8:
                continue
            if key in seen:
                errors.append(f"ligne de table en double : {path.name}:{seen[key] + 1} et {i + 1}")
            else:
                seen[key] = i


def check_register(errors: list[str]) -> None:
    for name in REGISTER_FILES:
        for i, line in enumerate((OFFICIAL / name).read_text(encoding="utf-8").splitlines()):
            m = TUTOIEMENT.search(line)
            if m:
                errors.append(f"registre : tutoiement « {m.group(0)} » dans {name}:{i + 1}")


def check() -> list[str]:
    errors: list[str] = []
    corpus = texts()
    check_concepts(corpus, errors)
    check_references(errors)
    check_retired(corpus, errors)
    check_fidelity(corpus, errors)
    check_glossary(errors)
    check_unique_rows(corpus, errors)
    check_register(errors)
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("STRUCTURE VALIDATION FAILED — gardes de propriété")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"STRUCTURE VALIDATION PASSED — {len(CONCEPTS)} concepts, {len(REFERENCES)} renvois, "
          f"{len(RETIRED)} vocabulaire(s) retiré(s), {len(FIDELITY)} résumé(s) fidèle(s), "
          f"{len(GLOSSARY_TERMS)} termes de glossaire, lignes de table uniques, registre des façades")
    return 0


if __name__ == "__main__":
    sys.exit(main())
