#!/usr/bin/env python3
"""V1.2 refonte — suivi de non-régression par propriété (décision 2, méthode M1 et M3).

Outil d'audit HORS package ; les harnais travaillent sur des copies. Usage :
  python3 V12R_Suivi.py <racine_package> [--out <instantane.json>]

Contrôles :
  1. HARNAIS : chaque cas de la table de correspondance (audit/data/V12R/V12R_Correspondance_harnais.csv)
     - statut MAINTENU ou MAINTENU-JUSQU-A-REECRITURE : doit être vert ;
     - statut OBSOLETE : peut être rouge, mais sa garde de remplacement doit exister et être verte ;
     - un cas absent de la table, ou de la table absent du run (même obsolète), est une erreur (C14, `V12R_41`).
  2. GARDES DE REMPLACEMENT : « structure:ID » (validate_structure.py) ou « lcf:LCF-xx » (validate_reading_map.py) ;
     verte seulement si elle est établie : garde connue du validateur, validateur allé au bout, garde non citée.
  3. CLIQUETS (M3) : chemin prescrit LETTRE (mots), négations totales, occurrences de doublons et nombre de
     listes de chargement distinctes ne dépassent pas la référence B05 (audit/data/V12R/V12R_Mesures_B05.json).
  4. VALIDATEURS du package : validate_all.py (sur copie).
"""
from __future__ import annotations

import csv
import json
import re
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


# Rectification déclarée (audit progressif, C14, `V12R_41`) : une garde de remplacement n'est verte que si elle est
# établie. Le validateur doit être connu ; la garde doit figurer dans son source ; le validateur doit être allé au bout :
# bannière PASSED, ou bannière FAILED de contrôle complet suivie de sa liste « - … ». Enfin la garde ne doit être citée
# par aucune ligne d'erreur. Un arrêt anticipé (« FAILED — message »), une trace Python ou une sortie inconnue n'établissent rien.
VALIDATORS = {
    "structure": ("validate_structure.py", "STRUCTURE VALIDATION PASSED", "STRUCTURE VALIDATION FAILED — gardes de propriété"),
    "lcf": ("validate_reading_map.py", "READING MAP VALIDATION PASSED", "READING MAP VALIDATION FAILED"),
}


def replacement_ok(root: Path, guard: str, cache: dict) -> tuple[bool, str]:
    kind, _, gid = guard.partition(":")
    if kind not in VALIDATORS or not gid:
        return False, f"type de garde inconnu « {guard} »"
    script, passed, failed = VALIDATORS[kind]
    path = root / "scripts" / script
    if not path.is_file():
        return False, f"validateur absent : {script}"
    if not re.search(rf"(?<![\w-]){re.escape(gid)}(?![\w-])", path.read_text(encoding="utf-8")):
        return False, f"garde {gid} inconnue de {script}"
    if script not in cache:
        cache[script] = run([sys.executable, "-B", str(path)], root)
    code, out = cache[script]
    lines = [line for line in out.strip().splitlines() if line.strip()]
    if code == 0 and lines and lines[-1].startswith(passed):
        return True, ""
    if code != 0 and lines and lines[0] == failed and all(line.startswith("- ") for line in lines[1:]):
        cited = [line for line in lines[1:] if re.search(rf"(?<![\w-]){re.escape(gid)}(?![\w-])", line)]
        return (not cited), (cited[0][:120] if cited else "")
    return False, f"garde {gid} non établie : {script} interrompu ou sortie inconnue (code {code})"


def evaluate(rows: list[dict], results: dict, guard_ok) -> tuple[list[str], dict]:
    """Confronte la table aux résultats des harnais. guard_ok(garde) -> (vert, motif)."""
    errors: list[str] = []
    counts = {"verts": 0, "obsoletes_rouges": 0, "obsoletes_verts": 0}
    seen = set()
    for row in rows:
        key = (row["harnais"], row["cas"])
        seen.add(key)
        st = results.get(row["harnais"], {}).get(row["cas"], "ABSENT")
        if st == "ABSENT":  # C14 : un cas de la table doit être exécuté, quel que soit son statut
            errors.append(f"{key[0]} {key[1]} ({row['statut']}) : cas de la table absent du run")
            continue
        if row["statut"].startswith("MAINTENU"):
            if st != "OK":
                errors.append(f"{key[0]} {key[1]} ({row['statut']}) : {st}")
            else:
                counts["verts"] += 1
        elif row["statut"] == "OBSOLETE":
            if not row["garde_remplacement"] or not row["justification"]:
                errors.append(f"{key[0]} {key[1]} obsolète sans garde ou sans justification")
            else:
                ok, why = guard_ok(row["garde_remplacement"])
                if not ok:
                    errors.append(f"{key[0]} {key[1]} : garde de remplacement {row['garde_remplacement']} non verte"
                                  + (f" ({why})" if why else ""))
            counts["obsoletes_rouges" if st != "OK" else "obsoletes_verts"] += 1
        else:
            errors.append(f"{key[0]} {key[1]} : statut inconnu {row['statut']}")
    for h, cases in results.items():
        for cid in cases:
            if (h, cid) not in seen:
                errors.append(f"cas hors table : {h} {cid}")
    return errors, counts


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    out_path = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else None

    # 1-2. Harnais et gardes de remplacement
    results = carto.run_suite(root)
    cache: dict = {}
    errors, counts = evaluate(table(), results, lambda guard: replacement_ok(root, guard, cache))

    # 3. Cliquets
    ref = json.loads((DATA / "V12R_Mesures_B05.json").read_text(encoding="utf-8"))
    b = mes.budget(root)
    ind = mes.indicators(root)
    dup = mes.duplicates(root)
    ll = mes.load_lists(root)
    now = {"lettre_mots": b["LETTRE"]["mots"], "negations": ind["TOTAL"]["negations"],
           "doublons": sum(d["occurrences"] for d in dup),
           "listes_distinctes": mes.distinct_lists(ll)}
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
