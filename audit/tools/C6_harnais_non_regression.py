#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.13 PATCH-DECISION C6 — harnais (exemples de référence).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C6_harnais_non_regression.py <racine>

Décision : les exemples (skill references/examples.md, exemples du GLOSSAIRE) sont des FAÇADES d'ACTION
(D-FAC-1 = c). Quatre conditions déterministes entrent dans la liste close des conditions de façade :
  LCF-11  DECISION-CHANGE d'exemple = issue canonique + décision + observation qui la soutient (F-EX-001)
  LCF-12  tout ACCEPTED-WITH-RESERVATION d'exemple porte une réserve complète (owner, sortie…) (F-GLO-002)
  LCF-13  vocabulaire C1 : NOT-OBSERVED seulement comme issue de DECISION-CHANGE ; STATE CLOSED ⇒ VERDICT (C1)
  LCF-14  une paire de captures ne soutient pas un claim de mémorisation ou de tâche sans protocole (F-EX-002)
Parties : A. conditions évaluées sur les textes ; B. mutations réinjectant la ligne fautive de B01 dans la copie :
le validateur « carte et façades » (validate_reading_map.py, C5) doit virer au rouge avec le motif LCF-xx.
Sur B01 : témoin 1/1 ; conditions 0/4 ; mutations au rouge 0/4 ; garde 0/1.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EX = "skills/design-governance-practice/references/examples.md"
GL = "V1/official/GLOSSAIRE.md"
OUTCOME = r"(CHANGED|CONFIRMED|ABANDONED|N/A-JUSTIFIED|NOT-OBSERVED)"
USER_EFFECT = re.compile(r"(?i)mémorable|mémoris|tâche|usage|utilisabilit")
PROTOCOL = re.compile(r"(?i)protocole|participant")

B01_LINES = {  # lignes fautives de B01, réinjectées par les mutations
    "M-7": (EX, r"(?m)^DECISION-CHANGE: .*$", "DECISION-CHANGE: couleur du texte et de la bordure"),
    "M-8": (GL, r"(?m)^\| \*\*CLOSED\*\* \|.*$", "| **CLOSED** | « La trace et les artefacts sont persistés ; le run reste `ACCEPTED-WITH-RESERVATION` sur l’accessibilité non vérifiée. » |"),
    "M-9": (EX, r"(?m)^NOT-VERIFIED: autres écrans.*$|^NOT-OBSERVED: tous les écrans.*$", "NOT-OBSERVED: tous les écrans, plateformes et thèmes"),
    "M-10": (EX, r"(?m)^EVIDENCE: paire de captures.*$", "EVIDENCE: paire de captures avec et sans traitement pixel/raster ; la sélection des pièces reste plus mémorable sans perdre la tâche"),
}


def blocks(text: str) -> list[str]:
    return re.findall(r"```text\n(.*?)```", text, re.S)


def conditions(root: Path):
    ex = (root / EX).read_text(encoding="utf-8")
    gl = (root / GL).read_text(encoding="utf-8")
    bl = blocks(ex)
    dc = [l for b in bl for l in b.splitlines() if l.startswith("DECISION-CHANGE:")]
    gdc = next((l for l in gl.splitlines() if l.startswith("| **DECISION-CHANGE** |")), "")
    ok11 = (bool(dc) and all(re.match(rf"DECISION-CHANGE: {OUTCOME} — .+\(observation : .+\)", l) for l in dc)
            and re.search(OUTCOME, gdc) is not None and "observation" in gdc)
    awr_blocks = [b for b in bl if "ACCEPTED-WITH-RESERVATION" in b]
    gawr = [l for l in gl.splitlines() if l.startswith("|") and "ACCEPTED-WITH-RESERVATION" in l and "Exemple" not in l and "**Verdict" not in l]
    complete = lambda s: all(re.search(p, s, re.I) for p in (r"owner", r"prochaine preuve", r"revue", r"(condition de )?sortie"))
    ok12 = all(re.search(r"(?m)^RESERVATION: ", b) and complete(b) for b in awr_blocks) and all(complete(l) for l in gawr)
    no_line = all(not re.search(r"(?m)^NOT-OBSERVED:", b) for b in bl)
    closed_verdict = all(("STATE: CLOSED" not in b) or re.search(r"(?m)^VERDICT: ", b) for b in bl)
    ok13 = no_line and closed_verdict
    ev = [l for b in bl for l in b.splitlines() if l.startswith("EVIDENCE:") and "capture" in l]
    ok14 = bool(ev) and all(not USER_EFFECT.search(l) or PROTOCOL.search(l) for l in ev)
    return [
        ("LCF-11", "F-EX-001", f"DECISION-CHANGE d'exemple = issue + décision + observation ({len(dc)} lignes d'exemple + GLOSSAIRE)", ok11),
        ("LCF-12", "F-GLO-002", f"ACCEPTED-WITH-RESERVATION d'exemple ⇒ réserve complète ({len(awr_blocks)} bloc(s), {len(gawr)} ligne(s) GLOSSAIRE)", ok12),
        ("LCF-13", "C1 (triade)", "NOT-OBSERVED réservé à DECISION-CHANGE ; STATE CLOSED ⇒ VERDICT dans chaque exemple", ok13),
        ("LCF-14", "F-EX-002", "une paire de captures ne porte pas de claim de mémorisation ou de tâche sans protocole", ok14),
    ]


def guard(root: Path):
    gl = (root / GL).read_text(encoding="utf-8")
    row = next((l for l in gl.splitlines() if l.startswith("| **CLOSED** |")), "")
    return [("G-01", "F-GLO-002", "l'exemple CLOSED sépare l'état du verdict (un run clos peut être RETURN)", "RETURN" in row and "verdict" in row.lower())]


def run_vrm(root: Path):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/validate_reading_map.py")], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def mutations(root: Path):
    rows = []
    for mid, motive, fiche, label in (("M-7", "LCF-11", "F-EX-001", "DECISION-CHANGE redevient une liste de propriétés"),
                                      ("M-8", "LCF-12", "F-GLO-002", "l'exemple CLOSED redevient une réserve sans attributs"),
                                      ("M-9", "LCF-13", "C1", "NOT-OBSERVED redevient un champ de scope non vérifié"),
                                      ("M-10", "LCF-14", "F-EX-002", "la paire de captures redevient preuve de mémorisation et de tâche")):
        rel, pattern, bad = B01_LINES[mid]
        p = root / rel
        old = p.read_text(encoding="utf-8")
        new, n = re.subn(pattern, bad, old, count=1)
        p.write_text(new if n else old, encoding="utf-8")
        ok, out = run_vrm(root)
        p.write_text(old, encoding="utf-8")
        rows.append((mid, fiche, label, n == 1 and (not ok) and motive in out, out.splitlines()[-1] if out else ""))
    return rows


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        ok, out = run_vrm(root)
        t = [("T-POS-1", "témoin", "validate_reading_map sur la copie non modifiée → PASS", ok, out.splitlines()[-1] if out else "")]
        c, m, g = conditions(root), mutations(root), guard(root)
    for cid, fiche, label, good, msg in t + m:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:10} {label}  [{msg[:60]}]")
    for cid, fiche, label, good in c + g:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:10} {label}")
    print(f"\nTémoin : {sum(x[3] for x in t)}/1 ; conditions LCF : {sum(x[3] for x in c)}/{len(c)} ; mutations au rouge : {sum(x[3] for x in m)}/{len(m)} ; garde : {sum(x[3] for x in g)}/{len(g)}")
    return 0 if all(x[3] for x in t + c + m + g) else 1


if __name__ == "__main__":
    sys.exit(main())
