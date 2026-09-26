#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.17 PATCH-DECISION D1 — harnais (frontière du jugement de craft).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 D1_harnais_non_regression.py <racine>

Parties :
  A. Conditions de façade ajoutées à la LCF (évaluées sur les textes) :
     LCF-15  QUICKSTART §6 = projection exacte des dimensions de DIRECTION/FIRST-OBJECT (mêmes noms, même ordre)
     LCF-16  la colonne « Dimension CFT-00 » du contrat du premier objet ne cite que des dimensions de CFT-00 (ou « — »)
     LCF-17  déclencheurs critiques : chaque ligne corrigée mène au propriétaire exact
  B. Gardes textuelles : une seule revue créative (méthode SAVOIR, trace ACTION), DOUBLE-LOOP fusionné, Gate C distinct.
  C. Mutations : réinjecter la cellule fautive de B01 → validate_reading_map (validateur « carte et façades ») rouge, motif LCF-xx.
Sur B01 : témoin 1/1 ; LCF 0/3 ; gardes 0/4 ; mutations au rouge 0/2.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

B01_QS_ROW = "| Relation produit | Pourquoi cette direction appartient à ce produit, ce public et ce contenu. |"
B01_TRIGGER = "| Motif possiblement générique ou réflexe | Test motivation/construction d’ACTION et `SAVOIR/CRAFT`. | `[REQUIS PAR LE MODULE]` |"


def rows_between(text: str, start: str, stop: str) -> list[list[str]]:
    i = text.find(start)
    if i < 0:
        return []
    seg = text[i:]
    j = seg.find(stop, len(start))
    seg = seg[: j if j > 0 else len(seg)]
    out = []
    for line in seg.splitlines():
        if line.startswith("| ") and not line.startswith("|---"):
            out.append([c.strip() for c in line.strip().strip("|").split("|")])
    return out[1:] if out else []   # sans l'en-tête


def name(cell: str) -> str:
    return re.sub(r"[*`]", "", cell).strip()


def lcf(root: Path):
    off = root / "V1/official"
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    Q = (off / "QUICKSTART.md").read_text(encoding="utf-8")
    S = (off / "SAVOIR.md").read_text(encoding="utf-8")
    fo_rows = rows_between(D, "### Contrat positif du premier objet", "\n#")
    fo = [name(r[0]) for r in fo_rows]
    qs = [name(r[0]) for r in rows_between(Q, "## 6. Produire une qualité positive", "\n#")]
    cft = {name(r[0]) for r in rows_between(S, "## CFT-00", "### Creative Quality Review")}
    header = next((l for l in D[D.find("### Contrat positif du premier objet"):].splitlines() if l.startswith("| Dimension")), "")
    hcells = [c.strip() for c in header.strip().strip("|").split("|")]
    col = next((k for k, c in enumerate(hcells) if "CFT-00" in c), None)
    mapped = [v.strip() for r in fo_rows if col is not None and len(r) > col for v in re.split(r"[,+/]| et ", name(r[col])) if v.strip()]
    trig = {name(r[0]): r[1] for r in rows_between(D, "### Déclencheurs critiques", "\n#") if len(r) > 1}
    motif = next((v for k, v in trig.items() if k.startswith("Motif possiblement générique")), "")
    scene = next((v for k, v in trig.items() if k.startswith("Asset, motion, scène")), "")
    dens = next((v for k, v in trig.items() if k.startswith("Détail final")), "")
    return [
        ("LCF-15", "F-DIR-020", f"QUICKSTART §6 = projection exacte de FIRST-OBJECT ({len(qs)} vs {len(fo)} dimensions)", bool(fo) and qs == fo),
        ("LCF-16", "F-DIR-030", "contrat du premier objet : colonne « Dimension CFT-00 » ne citant que CFT-00 (ou « — »)",
         col is not None and bool(mapped) and all(v in cft or v in {"—", "DIRECTION"} for v in mapped)),
        ("LCF-17", "F-DIR-042", "déclencheurs : motif → SAVOIR/CRAFT/CFT-01 (+ ACTION/ANTI-SLOP) ; scène → BIBLIOTHEQUE ; densité → SAVOIR/CRAFT",
         "SAVOIR/CRAFT/CFT-01" in motif and "ACTION/ANTI-SLOP" in motif and "BIBLIOTHEQUE/" in scene and "SAVOIR/CRAFT" in dens),
    ]


def guards(root: Path):
    off = root / "V1/official"
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    A = (off / "ACTION.md").read_text(encoding="utf-8")
    dl = D[D.find("### Contrôle du premier objet"):D.find("### One-shot et boucle")]
    passe = A[A.find("### Passe créative et polish"):A.find("## ACTION/STRUCTURED-PROOF")]
    gatec = A[A.find("## ACTION/GATE-C"):A.find("## ACTION/ANTI-SLOP")]
    atelier = D[D.find("### Vérité de la scène et clôture de craft"):D.find("## DIRECTION/DOUBLE-LOOP")]
    return [
        ("G-01", "F-DIR-030", "DOUBLE-LOOP : plus de grille propre ni de section « contrôle compact » (addendum 11.19), renvoi au contrat du premier objet",
         "| **Preuve précoce** |" not in dl and "FIRST-OBJECT" in dl and "### Relation avec le contrôle compact de `DOUBLE-LOOP`" not in D),
        ("G-02", "F-DIR-030", "ACTION, passe créative : exécute la revue définie par SAVOIR/CRAFT (Creative Quality Review), sans liste concurrente",
         "Creative Quality Review" in passe and "SAVOIR/CRAFT" in passe),
        ("G-03", "F-DIR-030", "Gate C : critères de gate, s'appuie sur la revue créative, aucune seconde revue",
         bool(re.search(r"(?i)revue créative", gatec)) and bool(re.search(r"(?i)seconde revue|ne refait pas", gatec))),
        ("G-04", "F-DIR-030", "ATELIER : la critique par verbes s'inscrit dans la revue créative unique", bool(re.search(r"(?i)revue créative", atelier))),
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
        a, g = lcf(root), guards(root)
        m = []
        good, msg = mutate(root, "V1/official/QUICKSTART.md", r"(?m)^\| (Relation produit|Foyer) \|.*$", B01_QS_ROW, "LCF-15")
        m.append(("M-11", "F-DIR-020", "QUICKSTART réintroduit une dimension hors FIRST-OBJECT", good, msg))
        good, msg = mutate(root, "V1/official/DIRECTION.md", r"(?m)^\| Motif possiblement générique ou réflexe \|.*$", B01_TRIGGER, "LCF-17")
        m.append(("M-12", "F-DIR-042", "déclencheur « motif générique » renvoyé à ACTION pour la méthode", good, msg))
    for cid, fiche, label, ok_, msg in t + m:
        print(f"{'OK  ' if ok_ else 'ÉCHEC'} {cid:6} {fiche:10} {label}  [{msg[:60]}]")
    for cid, fiche, label, ok_ in a + g:
        print(f"{'OK  ' if ok_ else 'ÉCHEC'} {cid:6} {fiche:10} {label}")
    print(f"\nTémoin : {sum(x[3] for x in t)}/1 ; LCF : {sum(x[3] for x in a)}/{len(a)} ; gardes : {sum(x[3] for x in g)}/{len(g)} ; mutations au rouge : {sum(x[3] for x in m)}/{len(m)}")
    return 0 if all(x[3] for x in t + a + g + m) else 1


if __name__ == "__main__":
    sys.exit(main())
