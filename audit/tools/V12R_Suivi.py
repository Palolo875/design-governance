#!/usr/bin/env python3
"""V1.2 refonte — suivi de non-régression par propriété (décision 2, méthode M1 et M3).

Outil d'audit HORS package ; les harnais travaillent sur des copies. Usage :
  python3 V12R_Suivi.py <racine_package> [--out <instantane.json>]

Contrôles :
  1. HARNAIS : chaque cas de la table de correspondance (audit/data/V12R/V12R_Correspondance_harnais.csv)
     - statut MAINTENU ou MAINTENU-JUSQU-A-REECRITURE : doit être vert ;
     - statut OBSOLETE : peut être rouge, mais sa garde de remplacement doit exister et être verte ;
     - un cas absent de la table, ou de la table absent du run, est une erreur.
  2. GARDES DE REMPLACEMENT : « structure:ID » (validate_structure.py) ou « lcf:LCF-xx » (validate_reading_map.py).
  3. CLIQUETS (M3) : chemin prescrit LETTRE (mots), négations totales, occurrences de doublons et nombre de
     listes de chargement distinctes ne dépassent pas la référence B05 (audit/data/V12R/V12R_Mesures_B05.json).
  4. VALIDATEURS du package : validate_all.py (sur copie).
"""
from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
DATA = TOOLS.parent / "data" / "V12R"
sys.path.insert(0, str(TOOLS))
import V12R_Carto_harnais as carto  # noqa: E402
import V12R_Mesures as mes  # noqa: E402


def table() -> list[dict]:
    with open(DATA / "V12R_Correspondance_harnais.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return p.returncode, p.stdout + p.stderr


def replacement_ok(root: Path, guard: str, cache: dict) -> bool:
    kind, _, gid = guard.partition(":")
    script = {"structure": "validate_structure.py", "lcf": "validate_reading_map.py"}.get(kind)
    if not script or not (root / "scripts" / script).is_file():
        return False
    if script not in cache:
        cache[script] = run([sys.executable, "-B", str(root / "scripts" / script)], root)
    code, out = cache[script]
    return code == 0 or gid not in out


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    out_path = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else None
    errors: list[str] = []

    # 1-2. Harnais et gardes de remplacement
    results = carto.run_suite(root)
    seen = set()
    counts = {"verts": 0, "obsoletes_rouges": 0, "obsoletes_verts": 0}
    cache: dict = {}
    for row in table():
        key = (row["harnais"], row["cas"])
        seen.add(key)
        st = results.get(row["harnais"], {}).get(row["cas"], "ABSENT")
        if row["statut"].startswith("MAINTENU"):
            if st != "OK":
                errors.append(f"{key[0]} {key[1]} ({row['statut']}) : {st}")
            else:
                counts["verts"] += 1
        elif row["statut"] == "OBSOLETE":
            if not row["garde_remplacement"] or not row["justification"]:
                errors.append(f"{key[0]} {key[1]} obsolète sans garde ou sans justification")
            elif not replacement_ok(root, row["garde_remplacement"], cache):
                errors.append(f"{key[0]} {key[1]} : garde de remplacement {row['garde_remplacement']} non verte")
            counts["obsoletes_rouges" if st != "OK" else "obsoletes_verts"] += 1
        else:
            errors.append(f"{key[0]} {key[1]} : statut inconnu {row['statut']}")
    for h, cases in results.items():
        for cid in cases:
            if (h, cid) not in seen:
                errors.append(f"cas hors table : {h} {cid}")

    # 3. Cliquets
    ref = json.loads((DATA / "V12R_Mesures_B05.json").read_text(encoding="utf-8"))
    b = mes.budget(root)
    ind = mes.indicators(root)
    dup = mes.duplicates(root)
    ll = mes.load_lists(root)
    now = {"lettre_mots": b["LETTRE"]["mots"], "negations": ind["TOTAL"]["negations"],
           "doublons": sum(d["occurrences"] for d in dup),
           "listes_distinctes": len({tuple(v) for v in ll.values() if v is not None})}
    base = {"lettre_mots": ref["budget"]["LETTRE"]["mots"], "negations": ref["indicateurs"]["TOTAL"]["negations"],
            "doublons": sum(d["occurrences"] for d in ref["doublons"]),
            "listes_distinctes": len({tuple(v) for v in ref["listes_chargement"].values() if v is not None})}
    for k in now:
        if now[k] > base[k]:
            errors.append(f"cliquet {k} : {now[k]} > référence {base[k]}")
    for k in ("TABLE", "LETTRE"):
        if b[k]["perimes"] or b[k]["introuvables"]:
            errors.append(f"périmètre {k} : périmés {b[k]['perimes']} ; introuvables {b[k]['introuvables']}")

    # 4. Validateurs du package (sur copie)
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / "pkg"
        shutil.copytree(root, copy, ignore=shutil.ignore_patterns("dist", "*.zip", "__pycache__"))
        code, out = run([sys.executable, "-B", "scripts/validate_all.py"], copy)
        va = "FULL VALIDATION PASSED" in out and code == 0
        if not va:
            errors.append("validate_all rouge")

    total = sum(len(c) for c in results.values())
    print(f"HARNAIS : {total} cas ; maintenus verts {counts['verts']} ; obsolètes (rouges/verts) "
          f"{counts['obsoletes_rouges']}/{counts['obsoletes_verts']}")
    print("CLIQUETS : " + " ; ".join(f"{k} {now[k]} (réf. {base[k]})" for k in now))
    print(f"validate_all : {'vert' if va else 'ROUGE'}")
    if out_path:
        out_path.write_text(json.dumps({"cas": results, "cliquets": now, "reference": base, "erreurs": errors},
                                       ensure_ascii=False, indent=1), encoding="utf-8")
    if errors:
        print("SUIVI ROUGE")
        for e in errors:
            print(f"- {e}")
        return 1
    print("SUIVI VERT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
