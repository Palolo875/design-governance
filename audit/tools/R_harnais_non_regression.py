#!/usr/bin/env python3
"""DG-AUDIT-001 — R.01 PATCH-DECISION du retour — harnais R (RET-1 à RET-6 et points du §6 retenus).

Artefact d'audit HORS package. Lecture seule de la racine ; toute exécution et toute mutation se font sur copie.
Usage : python3 R_harnais_non_regression.py <racine>

Trois familles :
  T-1          témoin : validate_all passe sur la racine (copie) ;
  R-01 à R-14  conditions de texte, évaluées ICI (code des conditions pris dans DG_AUDIT_001_Patch_R01.py,
               aides de lecture recopiées ci-dessous : aucune dépendance au code du package) ;
  R-15 à R-28  conditions LCF-22 à LCF-35 présentes dans validate_reading_map.py de la racine ET sensibles :
               l'inverse de l'entrée de patch correspondante, appliqué sur copie, rend le validateur rouge avec cet ID ;
  R-29, R-30   conservations machine (décision R.01 : le texte s'aligne sur la machine, la machine ne change pas).
Attendu sur B03 (V1.1.0) : témoin 1/1 ; R-01 à R-28 rouges ; R-29 et R-30 verts (conservations).
Attendu sur B04 (V1.1.1) après R.02 : 31/31.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import DG_AUDIT_001_Patch_R01 as PR  # noqa: E402


# ---- aides de lecture (copie de celles de validate_reading_map.py, B03) ----
def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def row(text: str, key: str, col: int = 0) -> list[str] | None:
    for line in text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            found = cells(line)
            if len(found) > col and key in found[col]:
                return found
    return None


def rows_between(text: str, start: str, stop: str) -> list[list[str]]:
    index = text.find(start)
    if index < 0:
        return []
    segment = text[index:]
    end = segment.find(stop, len(start))
    segment = segment[: end if end > 0 else len(segment)]
    found = [cells(line) for line in segment.splitlines() if line.startswith("| ") and not line.startswith("|---")]
    return found[1:]


def plain(cell: str) -> str:
    return re.sub(r"[*`]", "", cell).strip()


def texts(root: Path) -> dict[str, str]:
    off = root / "V1/official"
    sk = root / "skills/design-governance-practice"
    files = {"D": off / "DIRECTION.md", "A": off / "ACTION.md", "S": off / "SAVOIR.md", "C": off / "CHANGELOG.md",
             "G": off / "GLOSSAIRE.md", "Q": off / "QUICKSTART.md", "README": root / "README.md", "NOTES": root / "RELEASE_NOTES.md",
             "SK": sk / "SKILL.md", "EX": sk / "references/examples.md", "MP": sk / "references/machine_projection.md"}
    return {k: p.read_text(encoding="utf-8") if p.is_file() else "" for k, p in files.items()}


def conditions(root: Path) -> dict[str, object]:
    ns: dict[str, object] = {"re": re, "json": json, "ROOT": root, "cells": cells, "row": row,
                             "rows_between": rows_between, "plain": plain, "dict": dict, "list": list, "str": str}
    exec(PR.LCF_CODE, ns)  # noqa: S102 — code des conditions décidé en R.01
    return ns


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=1500)
    return r.returncode, r.stdout + r.stderr


def copy(src: Path, dst: Path) -> Path:
    return Path(shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip", ".dist.previous")))


def mutate(mut: Path, pid: str) -> list[str]:
    """Inverse l'entrée R.01 `pid`. R.03 (rectification déclarée) : si une entrée R.03 a réécrit une partie du
    texte posé par `pid`, cette entrée R.03 est d'abord inversée, puis `pid` (mutation équivalente)."""
    entry = [e for e in PR.PATCH if e[0] == pid]
    problems = PR.apply(mut, entry, reverse=True)
    if problems:
        try:
            import DG_AUDIT_001_Patch_R03 as P3
        except ImportError:
            return problems
        later = [e for e in P3.PATCH if e[2] == entry[0][2] and e[3] in entry[0][4]]
        problems = PR.apply(mut, list(reversed(later)), reverse=True) or PR.apply(mut, entry, reverse=True)
    return problems


LABELS = {
    "LCF-22": ("RET-1", "DECISION-CHANGE : toute énumération avec N/A-JUSTIFIED porte aussi NOT-OBSERVED ; « obtenue ou attendue » retiré"),
    "LCF-23": ("RET-2", "B1b : portée écrite = condition de check_b1b (DIRECTION acceptée, V PASS ou PASS-WITH-RESERVATION)"),
    "LCF-24": ("RET-3", "Creative Boot des façades sans nombre fixe d'anti-directions ni de tension"),
    "LCF-25": ("RET-4", "skill et carte d'ACTION : Gate B chargé en LITE et ITER, retiré du « non chargé »"),
    "LCF-26": ("RET-5", "machine_projection : valeurs d'axes et champs de profile_decision = schéma"),
    "LCF-27": ("RET-6", "« alignés sur leurs propriétaires » retiré ; portée bornée à la liste close"),
    "LCF-28": ("R-08", "table de correspondance : chaque champ attribué à VISUAL_TARGET existe dans sa table"),
    "LCF-29": ("Légende", "légende : chaque tag dit partagé existe dans SAVOIR, ou est déclaré absent"),
    "LCF-30": ("QS §6", "QUICKSTART §6 : colonne « Retour si… » identique à DIRECTION/FIRST-OBJECT"),
    "LCF-31": ("Imitation", "exemples : renvoi à run_card.example.json, machine_projection et validate_run_card"),
    "LCF-32": ("R-12", "droits inconnus : ACCEPTED interdit, réserve possible, diffusion après clearance"),
    "LCF-33": ("R-13", "ressource technique : une seule liste (ACTION/POLICIES, sept champs)"),
    "LCF-34": ("R-14", "blocs RUN-* : la sortie renvoie au paquet de CLOSE-PACKAGE"),
    "LCF-35": ("GLOSS×B1", "GLOSSAIRE CLOSED : NOT-VERIFIED critique exclut ACCEPTED, pas la réserve"),
}


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    rows: list[tuple[str, str, str, bool]] = []
    with tempfile.TemporaryDirectory() as tmp:
        base = copy(src, Path(tmp) / "base")
        code, out = run([sys.executable, "-B", "scripts/validate_all.py"], base)
        rows.append(("T-1", "témoin", "validate_all sur la racine (copie)", code == 0 and "FULL VALIDATION PASSED" in out))

        t = texts(src)
        ns = conditions(src)
        for n, (lcf, (point, label)) in enumerate(LABELS.items(), start=1):
            fn = ns[f"lcf_{lcf[-2:]}"]
            try:
                ok = bool(fn(t))
            except Exception as exc:  # une racine sans la structure attendue est rouge, pas un crash
                ok, label = False, f"{label} [erreur : {exc!r}]"
            rows.append((f"R-{n:02d}", point, label, ok))

        rm = (src / "scripts/validate_reading_map.py").read_text(encoding="utf-8")
        for n, (lcf, (point, _)) in enumerate(LABELS.items(), start=15):
            present = f'("{lcf}",' in rm
            sensitive = False
            if present:
                mut = copy(src, Path(tmp) / f"mut_{lcf}")
                problems = mutate(mut, PR.MUTATION_OF[lcf])
                code, out = run([sys.executable, "-B", "scripts/validate_reading_map.py"], mut)
                sensitive = not problems and code != 0 and f"{lcf} :" in out
            rows.append((f"R-{n:02d}", point, f"{lcf} dans la liste close et rouge sous mutation ({PR.MUTATION_OF[lcf]} inversé)", present and sensitive))

        # conservations machine
        ex = json.loads((src / "schemas/run_card.example.json").read_text(encoding="utf-8"))
        rc = ex["run_card"]

        def verdict(card: dict) -> tuple[int, str]:
            f = Path(tmp) / "carte.json"
            f.write_text(json.dumps(card, ensure_ascii=False), encoding="utf-8")
            return run([sys.executable, "-B", "scripts/validate_run_card.py", str(f)], base)

        ok = True
        for v in ("PASS", "PASS-WITH-RESERVATION"):
            c = json.loads(json.dumps(ex))
            c["run_card"]["closure"]["axes"]["V"] = v
            c["run_card"]["closure"].pop("b1b", None)
            code, out = verdict(c)
            ok = ok and code != 0 and "closure.b1b" in out and "Traceback" not in out
        rows.append(("R-29", "RET-2", "check_b1b inchangé : DIRECTION ACCEPTED-WITH-RESERVATION, V PASS ou PWR, sans b1b → refusée", ok))
        c = json.loads(json.dumps(ex))
        c["run_card"]["artifact"]["rights_status"] = "unknown"
        code_awr, _ = verdict(c)
        c["run_card"]["closure"]["verdict"] = "ACCEPTED"
        c["run_card"]["closure"]["axes"] = {"V": "PASS", "U": "PASS", "A": "PASS", "T": "PASS"}
        code_acc, out_acc = verdict(c)
        c["run_card"]["artifact"]["rights_status"] = "cleared"
        code_ref, _ = verdict(c)  # même carte, droits levés : ACCEPTED admise (la faute unique est bien le droit)
        rows.append(("R-30", "R-12", f"droits unknown : AWR admise ; ACCEPTED refusée pour ce seul motif (exemple {rc['mode']})",
                     code_awr == 0 and code_acc != 0 and "droits inconnus" in out_acc and code_ref == 0))

    for cid, point, label, good in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:5} {point:10} {label}")
    t_ok = sum(r[3] for r in rows if r[0].startswith("T"))
    r_rows = [r for r in rows if r[0].startswith("R")]
    print(f"\nTémoin : {t_ok}/1 ; cas R : {sum(r[3] for r in r_rows)}/{len(r_rows)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
