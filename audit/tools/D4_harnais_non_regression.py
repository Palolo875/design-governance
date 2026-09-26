#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.20 PATCH-DECISION D4 — harnais (cycle de vie et claims d'efficacité).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 D4_harnais_non_regression.py <racine>

Parties :
  A. Gardes textuelles : statut SEED et transitions de dépréciation (F-CHG-001) ; promotion vers BIBLIOTHEQUE/EVOLUTION
     seulement si la route est structurelle (F-DIR-046) ; contrôle du validateur de package mis à jour.
  B. Conditions LCF :
     LCF-20  les statuts de cycle de vie listés par BIBLIOTHEQUE (63, 762) = ceux du CHANGELOG (SEED compris)
     LCF-21  statut d'efficacité cohérent : NOT-VERIFIED dans README, RELEASE_NOTES et CHANGELOG ;
             aucune formulation causale non bornée dans DIRECTION (« augmente la probabilité », « augmente la qualité »)
  C. Mutations : réinjecter la phrase de B01 → validate_reading_map (validateur « carte et façades ») rouge, motif LCF-xx.
Sur B01 : témoin 1/1 ; gardes 0/6 ; LCF 1/2 (LCF-20 est déjà cohérente sur B01 : c'est une condition de
conservation, qui empêchera la divergence quand SEED sera ajouté) ; mutations au rouge 0/2.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

STATUSES = ("SEED", "PILOT", "ADOPTED", "DEPRECATED", "ABANDONED")
UNBOUNDED = re.compile(r"(?<!vise à )(?<!visent à )augmente la (probabilité|qualité)")
B01_74 = "Il augmente la probabilité d’un travail de niveau expert en rendant explicites des décisions que les meilleures équipes prennent souvent implicitement"
B01_762 = "Une route peut être `PILOT`, `ADOPTED`, `DEPRECATED` ou `ABANDONED` dans la gouvernance du `CHANGELOG`."


def lifecycle_rows(ch: str) -> dict[str, list[str]]:
    sec = ch[ch.find("## Cycle de vie des routes"):ch.find("## Migration des anciens aliases")]
    out = {}
    for line in sec.splitlines():
        m = re.match(r"\| `([A-Z]+)` \|", line)
        if m:
            out[m.group(1)] = [c.strip() for c in line.strip().strip("|").split("|")]
    return out


def conditions(root: Path):
    off = root / "V1/official"
    B = (off / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    C = (off / "CHANGELOG.md").read_text(encoding="utf-8")
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    R = (root / "README.md").read_text(encoding="utf-8")
    N = (root / "RELEASE_NOTES.md").read_text(encoding="utf-8")
    table = set(lifecycle_rows(C))
    bib_lines = [l for l in B.splitlines() if "`PILOT`" in l and "`DEPRECATED`" in l]
    ok20 = bool(table) and len(bib_lines) >= 2 and all(set(re.findall(r"`(SEED|PILOT|ADOPTED|DEPRECATED|ABANDONED)`", l)) == table for l in bib_lines)
    ok21 = all("NOT-VERIFIED" in t for t in (R, N, C)) and not UNBOUNDED.search(D)
    return [
        ("LCF-20", "F-CHG-001", f"statuts listés par BIBLIOTHEQUE = statuts du CHANGELOG ({sorted(table)})", ok20),
        ("LCF-21", "F-DIR-002", "efficacité NOT-VERIFIED partout ; pas de « augmente la probabilité / la qualité » non borné dans DIRECTION", ok21),
    ]


def guards(root: Path):
    off = root / "V1/official"
    C = (off / "CHANGELOG.md").read_text(encoding="utf-8")
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    V = (root / "scripts/validate_design_governance.py").read_text(encoding="utf-8")
    rows = lifecycle_rows(C)
    seed, pilot, dep = rows.get("SEED", []), rows.get("PILOT", []), rows.get("DEPRECATED", [])
    l817 = next((l for l in D.splitlines() if l.startswith("Le passage entre propriétaires reste")), "")
    return [
        ("G-01", "F-CHG-001", "statut SEED (bootstrap du seed, sans gain mesuré) → ADOPTED (contrat de gain) ou DEPRECATED",
         bool(seed) and "ADOPTED" in seed[-1] and "DEPRECATED" in seed[-1]),
        ("G-02", "F-CHG-001", "PILOT utilisé par des consumers → DEPRECATED possible (pas seulement ADOPTED / ABANDONED)", bool(pilot) and "DEPRECATED" in pilot[-1]),
        ("G-03", "F-CHG-001", "le seed a le statut SEED ; ADOPTED exige le contrat de gain réel (BIBLIOTHEQUE/EVOLUTION)",
         bool(re.search(r"routes présentes dans le seed[^\n]*`SEED`", C)) and bool(re.search(r"(?i)contrat de gain", C))),
        ("G-04", "F-CHG-001", "DEPRECATED : aucun nouvel usage, migration par ACTION/RUN-SYSTEM", bool(dep) and "ACTION/RUN-SYSTEM" in " ".join(dep)),
        ("G-05", "F-DIR-046", "DIRECTION 817 : BIBLIOTHEQUE/EVOLUTION seulement si la route est structurelle ; sinon la source propriétaire",
         bool(re.search(r"(?i)BIBLIOTHEQUE/EVOLUTION` si|si la route est structurelle", l817))),
        ("G-06", "F-CHG-001", "validateur de package : SEED parmi les termes requis du cycle de vie", '"SEED"' in V),
    ]


def run_vrm(root: Path):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/validate_reading_map.py")], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def mutate(root: Path, rel: str, pattern: str, bad: str, motive: str):
    p = root / rel
    old = p.read_text(encoding="utf-8")
    new, n = re.subn(pattern, lambda _m: bad, old, count=1)
    p.write_text(new, encoding="utf-8")
    ok, out = run_vrm(root)
    p.write_text(old, encoding="utf-8")
    return n == 1 and (not ok) and motive in out, (out.splitlines() or [""])[-1]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        ok, out = run_vrm(root)
        t = [("T-1", "témoin", "validate_reading_map sur la copie non modifiée → PASS", ok, (out.splitlines() or [""])[-1])]
        g, c = guards(root), conditions(root)
        m = [
            ("M-13", "F-CHG-001", "BIBLIOTHEQUE 762 oublie SEED", *mutate(root, "V1/official/BIBLIOTHEQUE.md", r"Une route peut être `[^.]*` dans la gouvernance du `CHANGELOG`\.", B01_762, "LCF-20")),
            ("M-14", "F-DIR-002", "DIRECTION 74 redevient un claim d'efficacité non borné",
             *mutate(root, "V1/official/DIRECTION.md", r"Il (vise à augmenter|augmente) la probabilité d’un travail de niveau expert[^;]*", B01_74, "LCF-21")),
        ]
    for cid, fiche, label, good, msg in t + m:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:10} {label}  [{msg[:60]}]")
    for cid, fiche, label, good in g + c:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:10} {label}")
    print(f"\nTémoin : {sum(x[3] for x in t)}/1 ; gardes : {sum(x[3] for x in g)}/{len(g)} ; LCF : {sum(x[3] for x in c)}/{len(c)} ; mutations au rouge : {sum(x[3] for x in m)}/{len(m)}")
    return 0 if all(x[3] for x in t + g + c + m) else 1


if __name__ == "__main__":
    sys.exit(main())
