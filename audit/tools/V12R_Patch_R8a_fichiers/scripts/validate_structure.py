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
  8. NOYAU — les blocs `<!-- noyau:début ID -->` / `<!-- noyau:fin ID -->` sont appariés, uniques et placés
     dans les sources normatives ; la section compilée de la skill est identique à `scripts/build_core.py`.
 10. ORDRE — dans DIRECTION, rôle, posture et récapitulatif de protection précèdent les sections détaillées (D-17).
  9. CHARGEMENT — une seule table de chargement (`DIRECTION/CHARGE`, et sa copie compilée dans la skill) ;
     les façades y renvoient ; la ligne `DIRECTION` garde le build et l'ordre cible → premier objet ;
     Gate B n'y est chargée qu'en trace complète (décision 11), comme dans la carte de lecture d'ACTION.

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
import build_core as bc  # noqa: E402

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
    ("SOR-01", "ACTION.md", "réponse visible en langage produit, trace sur demande"),
    ("TRA-01", "ACTION.md", "trace légère par défaut ; trace complète si persistant, partagé, audité ou acceptation demandée"),
    ("CHK-01", "ACTION.md", "la première proposition vaut checkpoint, sauf action irréversible ou coûteuse"),
    ("CNT-01", "DIRECTION.md", "destination réelle sans contenu : exemple marqué plutôt qu'emplacements vides"),
    ("TRM-01", "BIBLIOTHEQUE.md", "test de trame : nommer la trame modale du brief, la rompre ou la justifier"),
    ("GTA-01", "ACTION.md", "Gate A par profil de surface : contrôles d'office et contrôles selon le contenu"),
    ("ROL-01", "DIRECTION.md", "rôle de directeur·rice artistique senior, défini une seule fois, en tête de DIRECTION"),
    ("VAL-01", "ACTION.md", "promesse du validateur : ce qu'atteste et n'atteste pas une RUN_CARD validée, texte unique"),
]

# 2. Renvois : la route cite un locator dont le bloc contient le concept.
REFERENCES: list[tuple[str, str]] = [
    ("DIRECTION/CREATIVE-BOOT", "ANT-01"),
    ("DIRECTION/VISUAL_TARGET", "MOY-01"),
]

# 3. Vocabulaire retiré : motif, remplacement, fichiers exemptés (historique).
RETIRED: list[tuple[str, str, set[str]]] = [
    (r"anti-directions?", "MODAL / PARTI", {"CHANGELOG.md"}),
    (r"MODE — DECISION — CHANGE — PROOF", "réponse visible en langage produit (ACTION/HANDOFF)", {"CHANGELOG.md"}),
    (r"déclenche un (?:nouveau )?checkpoint", "la première proposition vaut checkpoint (ACTION/PIPELINE-DIRECTION)", {"CHANGELOG.md"}),
    (r"checkpoint humain intervient avant le build|demande une validation avant le build",
     "la première proposition vaut checkpoint (ACTION/PIPELINE-DIRECTION)", {"CHANGELOG.md"}),
    (r"\*\*Ce qu’atteste une `RUN_CARD` validée :\*\*", "renvoi à la frontière de validation d'ACTION/RUN_CARD (VAL-01)",
     {"ACTION.md", "CHANGELOG.md"}),
    # Boucle d'édition : une seule description (DIRECTION/DOUBLE-LOOP, copiée dans le noyau). Exemptions provisoires,
    # à retirer par R5c (SAVOIR), R5d (BIBLIOTHEQUE) et R6 (README).
    (r"→ isoler|observer, isoler", "boucle d'édition de DIRECTION/DOUBLE-LOOP (noyau)",
     {"DIRECTION.md", "SKILL.md", "CHANGELOG.md", "SAVOIR.md", "BIBLIOTHEQUE.md", "README.md"}),
    (r"cette vue reste interne", "la prise de brief reste dans la trace (D-19)", {"CHANGELOG.md"}),
    (r"Mandat de fonctionnement|Adopte le niveau d’exigence", "rôle unique (ROL-01)", {"CHANGELOG.md"}),
    (r"`VISUAL_TARGET` la spécifie", "chaîne de lecture interne unique (DIRECTION)", {"CHANGELOG.md"}),
]

# 10. Ordre de DIRECTION (D-17) : rôle, posture et récapitulatif de protection avant les sections détaillées.
ORDER: list[tuple[str, str]] = [("## Rôle", "## DIRECTION/START"),
                                ("## Posture — à lire avant toute action", "## DIRECTION/START"),
                                ("### Récapitulatif de protection", "## DIRECTION/START")]

# 4. Fidélité des résumés : tout paragraphe qui contient le déclencheur contient la condition canonique.
FIDELITY: list[tuple[str, str, str]] = [
    ("prise de brief", r"au plus trois", "destination si elle est incertaine"),
    ("checkpoint", r"checkpoint[^.]{0,60}avant (?:le )?build|avant (?:le )?build[^.]{0,60}checkpoint", "irréversible ou coûteuse"),
    ("question de convergence", r"Question de convergence", "police de titre"),
]

# 5. Termes du vocabulaire de fabrication présents dans GLOSSAIRE.md (première cellule d'une ligne de table).
GLOSSARY_TERMS = ["Thèse", "Ancre", "Creative Boot", "MODAL", "PARTI", "FABRICATION", "Plafond",
                  "Objet de preuve", "Défaut dominant", "Vérité de scène", "Slop"]

# 7. Registre des façades humaines : formes de tutoiement impératif refusées.
REGISTER_FILES = ["QUICKSTART.md"]
TUTOIEMENT = re.compile(r"\b(?:ne confonds|utilise le|Charge `|active `|Augmente la|ajoute le|garde en tête|reste sur)\b")


# 8. Noyau : fichiers autorisés à porter des blocs.
NORMATIVE = {"DIRECTION.md", "ACTION.md", "SAVOIR.md", "BIBLIOTHEQUE.md"}
NOYAU_MARK = re.compile(r"^<!-- noyau:(début|fin) ([A-Z0-9\-]+) -->$")

# 9. Chargement : en-têtes d'une table de chargement ; lignes de façade qui doivent renvoyer à DIRECTION/CHARGE.
LOAD_HEADERS = re.compile(r"^\|\s*Mode\s*\|\s*(Charger d’abord|Démarrage minimal)")
LOAD_OWNERS = {"DIRECTION.md", "SKILL.md"}
LOAD_POINTERS = [("QUICKSTART.md", "| Une direction visuelle ouverte |"),
                 ("READING_MAP.md", "| Direction identitaire |"),
                 ("ORCHESTRATION_MAP.md", "| **Direction forte et spécifique** |")]


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


def check_noyau(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    seen: dict[str, str] = {}
    for path, lines in corpus.items():
        open_id = None
        for i, line in enumerate(lines):
            m = NOYAU_MARK.match(line.strip())
            if not m:
                continue
            if path.name not in NORMATIVE or path.parent != OFFICIAL:
                errors.append(f"noyau : balise hors source normative ({path.name}:{i + 1})")
                continue
            kind, bid = m.groups()
            if kind == "début":
                if open_id:
                    errors.append(f"noyau : {bid} ouvert dans {open_id} ({path.name}:{i + 1})")
                if bid in seen:
                    errors.append(f"noyau : bloc {bid} défini deux fois ({seen[bid]} et {path.name})")
                seen[bid] = path.name
                open_id = bid
            else:
                if bid != open_id:
                    errors.append(f"noyau : fin {bid} sans début ({path.name}:{i + 1})")
                open_id = None
        if open_id:
            errors.append(f"noyau : bloc {open_id} non fermé ({path.name})")
    try:
        skill = bc.SKILL.read_text(encoding="utf-8")
        if bc.render(skill, bc.compile_core()) != skill:
            errors.append("[NOY-02] noyau : la skill diffère de sa compilation (scripts/build_core.py)")
    except bc.CoreError as exc:
        errors.append(f"noyau : {exc}")


def load_row(lines: list[str], mode: str) -> str:
    rows = [l for l in lines if l.startswith(f"| **{mode}** |")]
    return rows[0] if len(rows) == 1 else ""


def check_load(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for path, lines in corpus.items():
        for i, line in enumerate(lines):
            if LOAD_HEADERS.match(line) and path.name not in LOAD_OWNERS:
                errors.append(f"[CHG-05] chargement : table de chargement hors DIRECTION/CHARGE ({path.name}:{i + 1})")
    for name, prefix in LOAD_POINTERS:
        rows = [l for l in (OFFICIAL / name).read_text(encoding="utf-8").splitlines() if l.startswith(prefix)]
        if rows and not all("`DIRECTION/CHARGE`" in r for r in rows):
            errors.append(f"[CHG-06] chargement : {name} redéfinit la liste « {prefix.strip('| *')} » au lieu de renvoyer à DIRECTION/CHARGE")
    try:
        path, lines, index = rr.resolve("DIRECTION/CHARGE")
    except rr.RouteError as exc:
        errors.append(f"chargement : DIRECTION/CHARGE introuvable ({exc})")
        return
    served = rr.extract(lines, index)
    body = "\n".join(served)

    def cells(mode: str) -> list[str]:
        r = load_row(served, mode)
        return [c.strip() for c in r.strip().strip("|").split("|")] if r else []
    d = cells("DIRECTION")
    first = d[1] if len(d) > 1 else ""
    vt, fo = first.find("`DIRECTION/VISUAL_TARGET`"), first.find("`DIRECTION/FIRST-OBJECT`")
    if "`ACTION/RUN-DIRECTION`" not in first or "`ACTION/FIRST-RENDER`" not in first or not (0 <= vt < fo):
        errors.append("[CHG-07] chargement : la ligne DIRECTION de DIRECTION/CHARGE doit charger RUN-DIRECTION et FIRST-RENDER, "
                      "et placer VISUAL_TARGET avant FIRST-OBJECT")
    gb, tc = first.find("`ACTION/GATE-B`"), first.find("trace complète")
    if gb >= 0 and not (0 <= tc < gb):
        errors.append("[CHG-08] chargement : en DIRECTION, Gate B n'est chargée qu'en trace complète (ACTION/HANDOFF)")
    carte = [l for l in (OFFICIAL / "ACTION.md").read_text(encoding="utf-8").splitlines()
             if l.startswith("| `DIRECTION` |") and "`ACTION/RUN-DIRECTION`" in l]
    row = carte[0] if len(carte) == 1 else ""
    if not row or ("`ACTION/GATE-B`" in row and "`ACTION/GATE-B` en trace complète" not in row
                   and not 0 <= row.find("trace complète") < row.find("`ACTION/GATE-B`")):
        errors.append("[CHG-09] chargement : la carte de lecture d'ACTION charge Gate B en DIRECTION hors trace complète")
    if "`ACTION/CLOSE-PACKAGE`" not in body or any("Clôture" in l for l in served if l.startswith("| Mode |")):
        errors.append("[CHG-01] chargement : la clôture de chaque mode renvoie à ACTION/CLOSE-PACKAGE, sans colonne de clôture")
    lite = cells("LITE")
    if len(lite) < 3 or "`ITER`" not in lite[2]:
        errors.append("[CHG-02] chargement : depuis LITE, la reclassification inclut ITER")
    sysm = cells("SYSTÈME")
    if len(sysm) < 2 or "`BIBLIOTHEQUE/COMPONENTS` si un composant change" not in sysm[1]:
        errors.append("[CHG-03] chargement : en SYSTÈME, BIBLIOTHEQUE/COMPONENTS seulement si un composant change")
    for mode in ("LITE", "ITER"):
        c = cells(mode)
        if len(c) < 2 or "`ACTION/GATE-A`" not in c[1] or "`ACTION/GATE-B`" not in c[1]:
            errors.append(f"[CHG-04] chargement : en {mode}, Gate A applicable et Gate B du risque sont chargés d'abord")


def check_order(errors: list[str]) -> None:
    lines = (OFFICIAL / "DIRECTION.md").read_text(encoding="utf-8").splitlines()
    for first, then in ORDER:
        a = [i for i, l in enumerate(lines) if l.strip() == first or l.startswith(first + " —")]
        b = [i for i, l in enumerate(lines) if l.strip() == then or l.startswith(then + " —")]
        if len(a) != 1 or len(b) != 1 or a[0] > b[0]:
            errors.append(f"[ORD-01] ordre de DIRECTION : « {first} » doit exister une fois, avant « {then} »")


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
    check_noyau(corpus, errors)
    check_load(corpus, errors)
    check_order(errors)
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
          f"{len(GLOSSARY_TERMS)} termes de glossaire, lignes de table uniques, registre des façades, "
          f"noyau compilé, chargement unique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
