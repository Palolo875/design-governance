#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.03 PATCH-DECISION B1 — harnais (protection critique et exception).

Artefact d'audit HORS package ; travaille sur une copie temporaire ; importe le
validateur de la copie et lui soumet des cartes construites en mémoire.
Usage : python3 B1_harnais_non_regression.py <racine_du_package>

Contrat attendu APRÈS correction (noms de champs indicatifs, fixés en phase 12) :
  risk.critical_protection.result ∈ {PASS, FAIL, NOT-VERIFIED}
  closure.exception (si issue = FAIL-ASSUMED) : structure de réserve commune (B2)
      + gate_axis, failure_evidence, requested_by, disposition
Les négatifs exigent un MOTIF (règle A2) : un rejet pour une autre raison = échec.
Sur B01 : témoins T-POS verts ; tests B1 en échec (ils documentent les défauts,
ou les champs n'existent pas encore).
"""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

PROT = {"control": "Parcours clavier du consentement exécuté et capturé", "owner": "Owner produit",
        "scope": "Écran de consentement", "failure_action": "BLOCKED",
        "evidence_locator": "captures/consent-clavier.png"}
FAIL_OBS = "Échec observé : contraste 3,9:1 sur la note de bas de page (Gate A, contraste)"
EXC = {"gate_axis": "Gate A / contraste", "failure_evidence": FAIL_OBS,
       "requested_by": "Owner produit (demande écrite du 25-09)", "scope": "Pilote interne, 10 comptes",
       "impact": "Lisibilité réduite d'une note secondaire", "owner": "Owner produit",
       "review_date": "2026-10-09", "next_proof": "Mesure de contraste après correction",
       "exit_condition": "Contraste ≥ 4,5:1 mesuré", "disposition": "DIFFUSÉ-LIMITÉ"}


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    return m, schema, ex


def card(ex, **kw):
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["mode"] = kw.get("mode", "STANDARD")
    if "level" in kw:
        c["risk"]["level"] = kw["level"]
        prot = dict(PROT, **kw.get("prot", {}))
        if "result" in kw:
            prot["result"] = kw["result"]
        c["risk"]["critical_protection"] = prot if kw["level"] == "critical" else None
    c["closure"].update(kw.get("closure", {}))
    if kw.get("exception") is not None:
        c["closure"]["exception"] = kw["exception"]
    if kw.get("observe_failure"):
        c["proof"]["observed"] = list(c["proof"]["observed"]) + [FAIL_OBS]
    return d


def verdict(m, schema, d):
    try:
        m.validate_card(d, schema)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)


NEG, POS = "neg", "pos"
CASES = [
    # (id, fiche, libellé, construction, attendu, motif)
    ("B1-01", "F-DIR-007", "LITE + risque critical → rejet",
     lambda ex: card(ex, mode="LITE", level="critical", result="PASS"), NEG, "risque critical interdit le mode LITE ou ITER"),
    ("B1-02", "F-DIR-007", "ITER + risque critical → rejet",
     lambda ex: card(ex, mode="ITER", level="critical", result="PASS"), NEG, "risque critical interdit le mode LITE ou ITER"),
    ("B1-03", "F-ACT-017", "protection critique sans result → rejet",
     lambda ex: card(ex, level="critical"), NEG, "critical_protection exige result"),
    ("B1-04", "F-ACT-017", "protection NOT-VERIFIED + ACCEPTED → rejet",
     lambda ex: card(ex, level="critical", result="NOT-VERIFIED", closure={"verdict": "ACCEPTED"}), NEG, "verdict ACCEPTED interdit"),
    ("B1-05", "F-ACT-017", "protection FAIL + verdict accepté → rejet",
     lambda ex: card(ex, level="critical", result="FAIL", closure={"verdict": "ACCEPTED-WITH-RESERVATION"}), NEG, "protection critique en échec"),
    ("B1-06", "F-ACT-017/038", "protection FAIL (BLOCKED) + issue FAIL-ASSUMED → rejet",
     lambda ex: card(ex, level="critical", result="FAIL", closure={"issue": "FAIL-ASSUMED", "verdict": "RETURN"},
                     exception=dict(EXC), observe_failure=True), NEG, "issue doit suivre critical_protection.failure_action"),
    ("B1-07", "F-ACT-038", "FAIL-ASSUMED sans exception structurée → rejet",
     lambda ex: card(ex, level="important", closure={"issue": "FAIL-ASSUMED", "verdict": "RETURN"}), NEG, "FAIL-ASSUMED exige closure.exception"),
    ("B1-08", "F-ACT-038", "FAIL-ASSUMED dont l'échec n'est pas observé → rejet",
     lambda ex: card(ex, level="important", closure={"issue": "FAIL-ASSUMED", "verdict": "RETURN"}, exception=dict(EXC)),
     NEG, "failure_evidence doit figurer dans proof.observed"),
    ("B1-09", "F-ACT-039", "FAIL-ASSUMED sans disposition → rejet",
     lambda ex: card(ex, level="important", closure={"issue": "FAIL-ASSUMED", "verdict": "RETURN"},
                     exception={k: v for k, v in EXC.items() if k != "disposition"}, observe_failure=True), NEG, "exception exige disposition"),
    # Positifs attendus après correction
    ("B1-P1", "F-DIR-007/017", "STANDARD + critical + result PASS + AWR → acceptée",
     lambda ex: card(ex, level="critical", result="PASS"), POS, None),
    ("B1-P2", "F-ACT-017", "critical FAIL + issue BLOCKED (= failure_action) + RETURN → acceptée",
     lambda ex: card(ex, level="critical", result="FAIL", closure={"issue": "BLOCKED", "verdict": "RETURN"}), POS, None),
    ("B1-P3", "F-ACT-038/039", "FAIL-ASSUMED complet, échec observé, disposition → acceptée",
     lambda ex: card(ex, level="important", closure={"issue": "FAIL-ASSUMED", "verdict": "RETURN"},
                     exception=dict(EXC), observe_failure=True), POS, None),
]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(Path(sys.argv[1]).resolve(), root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        m, schema, ex = load(root)
        rows = []
        ok, msg = verdict(m, schema, ex)
        rows.append(("T-POS-1", "B01", "exemple canonique accepté", ok, msg))
        for cid, fiche, label, build, kind, motive in CASES:
            accepted, msg = verdict(m, schema, build(ex))
            good = accepted if kind == POS else (not accepted and motive in msg)
            rows.append((cid, fiche, label, good, msg))
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:14} {label}  [{msg[:85]}]")
    b1 = [r for r in rows if r[0].startswith("B1")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; tests B1 : {sum(r[3] for r in b1)}/{len(b1)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
