#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.19 PATCH-DECISION D3 — garde textuelle (autorité, droits et gates spécialisés).

Artefact d'audit HORS package, en lecture seule. Usage : python3 D3_harnais_non_regression.py <racine>

D3 ne crée aucun invariant machine : autorisation, indépendance d'un regard et preuve de motion réduite ne sont
pas déterministes dans la carte (D-ACT-1 = c). Ce harnais est une GARDE TEXTUELLE limitée ; les épreuves de la
condition de sortie (§6 du rapport) restent nécessaires.
Sur B01 : témoins 4/4 ; gardes 0/7.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def between(text: str, a: str, b: str) -> str:
    i = text.find(a)
    if i < 0:
        return ""
    j = text.find(b, i + len(a))
    return text[i: j if j > 0 else len(text)]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    off = Path(sys.argv[1]).resolve() / "V1/official"
    A = (off / "ACTION.md").read_text(encoding="utf-8")
    S = (off / "SAVOIR.md").read_text(encoding="utf-8")
    step7 = between(A, "### 7. Écrire la direction", "### 8.")
    runcard = between(A, "## ACTION/RUN_CARD", "## ACTION/RUN —")
    motion = next((l for l in A.splitlines() if l.startswith("| Motion réduite |")), "")
    b3 = between(A, "### B3 — Regard externe", "### B4")
    tools = between(A, "### Inspection et ressources techniques", "\n---")
    tech = next((l for l in S.splitlines() if l.startswith("Aucun outil, script ou package")), "")
    tech_block = between(S, "Aucun outil, script ou package", "\n\n") or tech
    rows = [
        ("T-1", "témoin", "étape 7 du pipeline DIRECTION présente", bool(step7)),
        ("T-2", "témoin", "contrôle « Motion réduite » présent (Gate A)", bool(motion)),
        ("T-3", "témoin", "B3 présent", bool(b3)),
        ("T-4", "témoin", "politique des ressources techniques présente (ACTION/POLICIES)", bool(tools)),
        ("G-01", "F-ACT-026", "étape 7 : l'autorisation manquante renvoie à ACTION/AUTHORITY ; la compensation vaut pour le seul regard externe et n'autorise rien",
         "ACTION/AUTHORITY" in step7 and bool(re.search(r"(?i)n.autorise", step7))),
        ("G-02", "F-ACT-026", "table de correspondance RUN_CARD : AUTHORITY (portée, base, reprise, décideur) → owner + trace ; reviewer ≠ décideur",
         "AUTHORITY" in runcard and bool(re.search(r"(?i)reviewer|relecteur", runcard))),
        ("G-03", "F-ACT-033", "motion réduite : alternative implémentée et vérifiée préférence activée ; sinon NOT-VERIFIED",
         "prévue" not in motion and bool(re.search(r"(?i)implémentée", motion)) and "NOT-VERIFIED" in motion),
        ("G-04", "F-ACT-037", "B3 : une seconde session du même auteur est une auto-comparaison différée, jamais un regard externe",
         bool(re.search(r"(?i)auto-comparaison différée", b3))),
        ("G-05", "F-ACT-037", "B3 : critères d'indépendance tracés (relation, auteur du rendu, conflit) ; expositions multiples",
         all(k in b3 for k in ("REVIEWER-RELATION", "RENDER-AUTHOR", "CONFLICT")) and bool(re.search(r"(?i)plusieurs expositions|expositions multiples", b3))),
        ("G-06", "F-SAV-009", "SAVOIR/TECH : l'approbation vise une nouvelle dépendance ; renvoi à la politique d'ACTION",
         bool(re.search(r"(?i)nouvelle dépendance", tech_block)) and "ACTION/POLICIES" in tech_block),
        ("G-07", "F-SAV-009", "ACTION : trois branches (script local sans dépendance, outil déjà autorisé, nouvelle dépendance) ; exécution aveugle interdite",
         all(re.search(p, tools, re.I) for p in (r"script local", r"déjà autorisé", r"nouvelle dépendance", r"aveuglément"))),
    ]
    for cid, fiche, label, ok in rows:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:5} {fiche:10} {label}")
    t = [r for r in rows if r[0].startswith("T")]
    g = [r for r in rows if r[0].startswith("G")]
    print(f"\nTémoins : {sum(r[3] for r in t)}/{len(t)} ; gardes : {sum(r[3] for r in g)}/{len(g)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
