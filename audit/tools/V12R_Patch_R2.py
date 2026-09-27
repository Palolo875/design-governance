#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R2 : gardes de propriété (concepts d'honnêteté).

Décisions : 2 (V12R_00) ; méthode M1 à M4 (V12R_02_PROPOSITION_R2, validée par l'owner le 2026-09-27).
Textes exacts, applicables et réversibles. Usage :
  python3 V12R_Patch_R2.py <racine>                 # applique
  python3 V12R_Patch_R2.py <racine> --verifier      # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12R_Patch_R2.py <racine> --inverse ID    # remet l'ancien texte d'une entrée
  python3 V12R_Patch_R2.py <racine> --mutations     # sur une racine patchée : chaque garde rougit sous sa mutation
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from V12_Patch_ABD import apply  # noqa: E402  (même moteur de remplacement exact)

NEW_FILES = {"scripts/validate_structure.py": HERE / "V12R_Patch_R2_fichiers" / "scripts" / "validate_structure.py"}
MANIFEST_ADD = ["scripts/validate_structure.py"]

D, A, S = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md"


def mark(cid: str, rel: str, start: str) -> tuple[str, str, str, str, str]:
    return (f"R2-{cid}", f"balise {cid}", rel, "\n" + start, f"\n<!-- concept:{cid} -->\n" + start)


PATCH = [
    mark("HON-01", D, "Place un **marquage local de vérité**"),
    mark("HON-02", S, "Ne fais jamais passer abstraction CSS"),
    mark("HON-03", D, "Avant le premier rendu, le boot doit conduire"),
    mark("HON-04", A, "La validation JSON, la validation CLI, les fixtures"),
    mark("HON-05", A, "Lorsque le run est exécuté par un agent sans regard indépendant"),
    mark("HON-06", A, "Un gate non applicable est `N/A-JUSTIFIED`. Un gate nécessaire mais non vérifiable"),
    mark("HON-07", A, "Une capture prouve le rendu, pas l’indépendance du jugement"),
    mark("HON-08", A, "La provenance informe l’origine ; elle ne constitue pas"),
    ("R2-RR", "read_route retire les balises", "scripts/read_route.py",
     "def extract(lines: list[str], index: int) -> list[str]:",
     "CONCEPT_MARKER = re.compile(r\"^\\s*<!-- concept:[A-Z0-9\\-]+ -->\\s*$\")\n\n\n"
     "def extract(lines: list[str], index: int) -> list[str]:"),
    ("R2-RR2", "read_route retire les balises", "scripts/read_route.py",
     "        served.append(lines[i])\n    return served",
     "        if CONCEPT_MARKER.match(lines[i]):\n            continue\n        served.append(lines[i])\n    return served"),
    ("R2-VA1", "validate_all compile", "scripts/validate_all.py",
     "\"scripts/validate_reading_map.py\", \"scripts/read_route.py\"])",
     "\"scripts/validate_reading_map.py\", \"scripts/read_route.py\", \"scripts/validate_structure.py\"])"),
    ("R2-VA2", "validate_all exécute", "scripts/validate_all.py",
     "    run([sys.executable, \"scripts/validate_reading_map.py\"])\n",
     "    run([sys.executable, \"scripts/validate_reading_map.py\"])\n    run([sys.executable, \"scripts/validate_structure.py\"])\n"),
    ("R2-B1", "build : copie GitHub", "scripts/build_distributions.sh",
     "cp -a \"$ROOT/scripts/read_route.py\" \"$STAGE/github/scripts/read_route.py\"\n",
     "cp -a \"$ROOT/scripts/read_route.py\" \"$STAGE/github/scripts/read_route.py\"\n"
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/github/scripts/validate_structure.py\"\n"),
    ("R2-B2", "build : copie Local", "scripts/build_distributions.sh",
     "cp -a \"$ROOT/scripts/read_route.py\" \"$STAGE/local/scripts/read_route.py\"\n",
     "cp -a \"$ROOT/scripts/read_route.py\" \"$STAGE/local/scripts/read_route.py\"\n"
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/local/scripts/validate_structure.py\"\n"),
    ("R2-B3", "build : contrôle source", "scripts/build_distributions.sh",
     "python3 scripts/validate_reading_map.py\n",
     "python3 scripts/validate_reading_map.py\npython3 scripts/validate_structure.py\n"),
    ("R2-B4", "build : contrôle GitHub", "scripts/build_distributions.sh",
     "python3 \"$STAGE/github/scripts/validate_reading_map.py\"\n",
     "python3 \"$STAGE/github/scripts/validate_reading_map.py\"\npython3 \"$STAGE/github/scripts/validate_structure.py\"\n"),
    ("R2-B5", "build : contrôle Local", "scripts/build_distributions.sh",
     "python3 \"$STAGE/local/scripts/validate_reading_map.py\"\n",
     "python3 \"$STAGE/local/scripts/validate_reading_map.py\"\npython3 \"$STAGE/local/scripts/validate_structure.py\"\n"),
    ("R2-CH1", "CHANGELOG « Non publié »", "V1/official/CHANGELOG.md",
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Gardes de propriété (refonte, R2).** `scripts/validate_structure.py` : huit concepts d’honnêteté balisés "
     "à leur lieu propriétaire (`<!-- concept:HON-01 -->` à `HON-08`), chacun unique, non vide et dans son fichier ; "
     "`read_route.py` retire les balises à la lecture.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

# Mutations : chaque garde doit rougir.
MUTATIONS = [
    ("absence", "HON-04", lambda t: t.replace("<!-- concept:HON-04 -->\n", "", 1), A),
    ("copie", "HON-01", lambda t: t + "\n<!-- concept:HON-01 -->\nCopie de la vérité de scène placée ailleurs pour vérifier que la garde refuse un second lieu.\n", "V1/official/QUICKSTART.md"),
    ("déplacement", "HON-02", None, None),
    ("bloc vide", "HON-06", lambda t: t.replace("<!-- concept:HON-06 -->\n", "<!-- concept:HON-06 -->\n\n", 1), A),
    ("hors registre", "XYZ-99", lambda t: t + "\n<!-- concept:XYZ-99 -->\nUn concept inconnu du registre doit être refusé par la garde de structure du package.\n", D),
]


def manifest(root: Path, reverse: bool = False) -> None:
    p = root / "scripts" / "package_manifest.json"
    m = json.loads(p.read_text(encoding="utf-8"))
    for key in ("github", "local"):
        for item in MANIFEST_ADD:
            if reverse and item in m[key]:
                m[key].remove(item)
            elif not reverse and item not in m[key]:
                m[key].insert(m[key].index("scripts/read_route.py") + 1, item)
    p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_all(root: Path, dry: bool = False) -> list[str]:
    problems = apply(root, PATCH, dry=dry)
    for rel, src in NEW_FILES.items():
        if (root / rel).exists():
            problems.append(f"fichier déjà présent : {rel}")
    if problems or dry:
        return problems
    for rel, src in NEW_FILES.items():
        shutil.copy2(src, root / rel)
    manifest(root)
    return []


def validate(copy: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_structure.py")],
                         capture_output=True, text=True, cwd=copy)
    return out.returncode, out.stdout + out.stderr


def mutations(root: Path) -> int:
    bad = 0
    for name, cid, fn, rel in MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            if name == "déplacement":
                s = (copy / S).read_text(encoding="utf-8").replace("<!-- concept:HON-02 -->\n", "", 1)
                (copy / S).write_text(s, encoding="utf-8")
                q = copy / "V1/official/QUICKSTART.md"
                q.write_text(q.read_text(encoding="utf-8") + "\n<!-- concept:HON-02 -->\nLe faux asset est ici défini dans une façade au lieu de son fichier propriétaire, ce que la garde refuse.\n", encoding="utf-8")
            else:
                p = copy / rel
                p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
            code, out = validate(copy)
            red = code != 0 and cid in out
            print(f"mutation « {name} » ({cid}) : {'ROUGE' if red else 'NON ROUGE'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    if "--mutations" in sys.argv:
        return 1 if mutations(root) else 0
    if "--inverse" in sys.argv:
        pid = sys.argv[sys.argv.index("--inverse") + 1]
        problems = apply(root, [e for e in PATCH if e[0] == pid], reverse=True)
    else:
        problems = apply_all(root, dry="--verifier" in sys.argv)
    for pr in problems:
        print(pr)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH)} entrées, {len(NEW_FILES)} fichier(s) créé(s), manifeste")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
