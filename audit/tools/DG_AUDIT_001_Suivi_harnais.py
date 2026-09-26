#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.23 — suivi des 22 harnais de la phase 11 (outil de pilotage des phases 12 et 13).

Artefact d'audit HORS package. Lecture seule de la racine visée ; chaque harnais travaille lui-même sur des copies.
Usage :
  python3 DG_AUDIT_001_Suivi_harnais.py <racine> [--out instantane.json] [--compare instantane_precedent.json]
                                        [--fenetre] [--rectifies A1,C4,…]
--rectifies : harnais dont l'empreinte change par une rectification DÉCLARÉE dans le rapport de l'unité ;
              leur changement d'empreinte n'est pas une alerte (il l'est pour tout autre harnais).

Fenêtre de garde (12.03 → fin de 12.05, 11.23 §6 et 12.03 R-7). Entre le cycle de garde et la fin des passes de
texte, les validateurs « carte et façades » (LCF, locator ambigu) et de package (`SEED`) sont rouges par
construction ; les témoins qui lancent ces validateurs (ou le build, ou validate_all) le sont donc aussi.
Avec --fenetre, un témoin rouge n'est pas une alerte SI la contre-épreuve le rend vert : la racine est copie,
les seules gardes de la fenêtre y sont neutralisées (NEUTRALISATION ci-dessous), et les 22 harnais y sont
rejoués ; tous les témoins doivent y être verts. Un témoin rouge dans la contre-épreuve reste une alerte.
En fenêtre, les cas « significatifs » sont ceux qui restent verts dans la contre-épreuve : un cas vert
seulement parce qu'une garde arrête l'outil plus tôt (par exemple un build interrompu) n'est pas compté,
et le critère « rouges décroissants » porte sur les cas significatifs.

Ce que l'outil vérifie :
  1. témoins et conservations : tous verts, toujours (sinon RÉGRESSION TÉMOIN) ;
  2. dénominateurs identiques à la référence B01 (sinon HARNAIS MODIFIÉ : un harnais ne change que par rectification déclarée) ;
  3. empreinte de chaque harnais identique à la référence de l'instantané comparé (même règle) ;
  4. avec --compare : le nombre de cas verts d'aucun harnais ne diminue (critère « rouge décroissant » de la phase 12).
Référence B01 (11.23) : témoins 40/40 ; cas 3/300 (B2-P2, B3-P3, LCF-20 : conservations documentées).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDER = ["A1", "A2", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
         "D1", "D2", "D3", "D4", "E1", "E2"]
# (témoins, cas verts, cas total) relevés sur B01 le 25-09-2026
REF_B01 = {
    "A1": (4, 0, 11), "A2": (2, 0, 5), "B1": (1, 0, 12), "B2": (1, 1, 19), "B3": (1, 1, 12), "B4": (1, 0, 12),
    "B5": (1, 0, 5), "C1": (1, 0, 23), "C2": (3, 0, 28), "C3": (2, 0, 14), "C4": (3, 0, 24), "C5": (2, 0, 18),
    "C6": (1, 0, 9), "C7": (4, 0, 5), "C8": (1, 0, 3), "C9": (2, 0, 14), "D1": (1, 0, 9), "D2": (1, 0, 10),
    "D3": (4, 0, 7), "D4": (1, 1, 10), "E1": (1, 0, 28), "E2": (2, 0, 22),
}


NEUTRALISATION = [  # (fichier, texte de garde, texte neutre) — ne vaut que dans la copie de contre-épreuve
    ("scripts/validate_design_governance.py", 'required_terms = ("SEED", ', "required_terms = ("),
    ("scripts/validate_reading_map.py", "    check_facades(errors)\n", "    pass\n"),
    ("scripts/validate_reading_map.py", "        if len(places) > 1:\n", "        if False:\n"),
]


def run_all(root: Path) -> dict[str, tuple[str, int]]:
    out = {}
    for h in ORDER:
        path = HERE / f"{h}_harnais_non_regression.py"
        r = subprocess.run([sys.executable, str(path), str(root)], capture_output=True, text=True, timeout=900)
        out[h] = (r.stdout, r.returncode)
    return out


def counter_proof(root: Path) -> dict[str, tuple[int, int, int, int]]:
    """Harnais rejoués sur une copie où seules les gardes de la fenêtre sont neutralisées."""
    import shutil
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / "pkg"
        shutil.copytree(root, copy, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        for rel, guard, neutral in NEUTRALISATION:
            f = copy / rel
            text = f.read_text(encoding="utf-8")
            if text.count(guard) != 1:
                raise SystemExit(f"CONTRE-ÉPREUVE IMPOSSIBLE — garde introuvable dans {rel} : {guard!r}")
            f.write_text(text.replace(guard, neutral), encoding="utf-8")
        result = {}
        for h, (stdout, code) in run_all(copy).items():
            lines = [l for l in stdout.splitlines() if l.strip()]
            try:
                result[h] = parse(lines[-1])
            except Exception:
                result[h] = (-1, -1, -1, -1)
        return result


def parse(summary: str) -> tuple[int, int, int, int]:
    """Dernière ligne « Témoin(s) … : a/b ; … : c/d ; … » → (témoins verts, témoins, cas verts, cas)."""
    parts = summary.split(" ; ")
    nums = [tuple(map(int, re.search(r"(\d+)/(\d+)", p).groups())) for p in parts]
    tv, tt = nums[0]
    cv = sum(a for a, _ in nums[1:])
    ct = sum(b for _, b in nums[1:])
    return tv, tt, cv, ct


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2
    root = Path(args[0]).resolve()
    out = args[args.index("--out") + 1] if "--out" in args else None
    prev = json.loads(Path(args[args.index("--compare") + 1]).read_text(encoding="utf-8")) if "--compare" in args else None
    window = "--fenetre" in args
    rectified = set(args[args.index("--rectifies") + 1].split(",")) if "--rectifies" in args else set()
    proof = counter_proof(root) if window else {}

    snap: dict[str, dict] = {}
    alerts: list[str] = []
    for h in ORDER:
        path = HERE / f"{h}_harnais_non_regression.py"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        r = subprocess.run([sys.executable, str(path), str(root)], capture_output=True, text=True, timeout=900)
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        try:
            tv, tt, cv, ct = parse(lines[-1])
        except Exception:  # sortie illisible : c'est une alerte, pas un succès
            alerts.append(f"{h} : sortie illisible (code {r.returncode})")
            snap[h] = {"error": (r.stdout + r.stderr)[-400:], "sha256": digest}
            continue
        snap[h] = {"temoins": [tv, tt], "cas": [cv, ct], "sha256": digest}
        rt, _, rc = REF_B01[h]
        significant = cv
        if window:
            ptv, ptt, pcv, pct = proof[h]
            snap[h]["contre_epreuve"] = [ptv, ptt, pcv, pct]
            significant = min(cv, pcv)  # un vert qui disparaît sans les gardes n'est pas significatif
            if ptv != ptt or ptt <= 0:
                alerts.append(f"{h} : RÉGRESSION TÉMOIN (contre-épreuve {ptv}/{ptt})")
            elif tv != tt:
                print(f"{h} : témoin rouge ATTENDU (fenêtre de garde) ; contre-épreuve verte {ptv}/{ptt}")
            if cv > pcv:
                print(f"{h} : {cv - pcv} cas vert(s) de fenêtre, non significatif(s) (rouges dans la contre-épreuve)")
        elif tv != tt:
            alerts.append(f"{h} : RÉGRESSION TÉMOIN ({tv}/{tt})")
        snap[h]["cas_significatifs"] = significant
        if (tt, ct) != (rt, rc):
            alerts.append(f"{h} : HARNAIS MODIFIÉ (dénominateurs {tt}/{ct}, référence {rt}/{rc})")
        if prev and h in prev and "cas" in prev[h]:
            before = prev[h].get("cas_significatifs", prev[h]["cas"][0])
            if significant < before:
                alerts.append(f"{h} : RÉGRESSION ({significant} cas verts significatifs, {before} avant)")
            if prev[h].get("sha256") != digest and h not in rectified:
                alerts.append(f"{h} : HARNAIS MODIFIÉ (empreinte différente de l'instantané comparé)")
        print(f"{h:3} témoins {tv}/{tt} ; cas {cv:3}/{ct:3} ; rouges {ct - cv}")

    ok = [v for v in snap.values() if "cas" in v]
    T = (sum(v["temoins"][0] for v in ok), sum(v["temoins"][1] for v in ok))
    C = (sum(v["cas"][0] for v in ok), sum(v["cas"][1] for v in ok))
    S = sum(v.get("cas_significatifs", v["cas"][0]) for v in ok)
    print(f"\nTotal : témoins {T[0]}/{T[1]} ; cas {C[0]}/{C[1]} ; rouges restants {C[1] - C[0]}"
          + (f" ; cas verts significatifs (contre-épreuve) {S}/{C[1]}" if window else ""))
    for a in alerts:
        print("ALERTE", a)
    if out:
        Path(out).write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    return 1 if alerts else 0


if __name__ == "__main__":
    sys.exit(main())
