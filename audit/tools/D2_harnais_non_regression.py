#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.18 PATCH-DECISION D2 — harnais (boucle, phase et ITER).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 D2_harnais_non_regression.py <racine>

Parties :
  1. RUN_CARD (validate_run_card.validate_card), cartes de forme APRÈS B1–C4 :
     INV-D2-1  state ∈ {INTAKE, CLASSIFIED, SPECCED, BUILDING} ⇒ ni decision_change ni creative_close (champs « après observation »)
     INV-D2-2  mode ITER ⇒ direction.thesis non vide (rappel de direction ; la trace est exigée par INV-C4-1)
  2. GARDES TEXTUELLES : Boot conditionné à une correction utile (F-DIR-009) ; phases déclarées côté DIRECTION par renvoi
     à la colonne Phase d'ACTION/RUN_CARD (F-DIR-003) ; RUN-ITER nomme le transport du rappel (F-DIR-036).
Règle A2 : chaque négatif exige son motif.
Sur B01 : témoin 1/1 ; RUN_CARD 0/6 ; gardes 0/4.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return (m, json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8")),
            json.loads((root / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8")),
            json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8")))


def card(fx, mode="STANDARD", state="CLOSED"):
    """Carte non acceptée (RETURN), forme après B1–C4 (risk.statement, outcome, trace)."""
    d = copy.deepcopy(fx)
    c = d["run_card"]
    c["mode"] = mode
    c["risk"] = {"level": "normal", "critical_protection": None, "statement": "Troncature du libellé sur mobile"}
    c["decision_change"] = {"outcome": "CHANGED", "value": c["decision_change"]["value"], "evidence": c["decision_change"]["evidence"]}
    c["trace_locator"] = "tickets/run-045.md"
    if state != "CLOSED":
        c["closure"].update(state=state, verdict=None, issue=None)
    return d


def mut(fn, **kw):
    def b(fx):
        d = card(fx, **kw)
        fn(d["run_card"])
        return d
    return b


CASES = [
    ("D2-01", "F-DIR-003", "state BUILDING avec decision_change (conséquence déclarée avant observation)", mut(lambda c: None, state="BUILDING"), "neg", "avant observation"),
    ("D2-02", "F-DIR-003", "state SPECCED avec creative_close", mut(lambda c: (c.pop("decision_change"), c.__setitem__("creative_close", {
        "presence": "p", "signature": "s", "craft_detail": "d", "dominant_defect": "x", "next_polish_action": "y"})), state="SPECCED"), "neg", "avant observation"),
    ("D2-P1", "F-DIR-003", "state CHECKING avec decision_change → acceptée", mut(lambda c: None, state="CHECKING"), "pos", None),
    ("D2-03", "F-DIR-036", "ITER sans rappel de direction (trace présente)", mut(lambda c: c.pop("direction", None), mode="ITER"), "neg", "rappel de direction"),
    ("D2-P2", "F-DIR-036", "ITER avec direction.thesis et trace → acceptée",
     mut(lambda c: c.__setitem__("direction", {"thesis": "Alerte d'abord, contexte ensuite : la hiérarchie existante est conservée"}), mode="ITER"), "pos", None),
    ("D2-P3", "proportion", "LITE sans direction → acceptée (aucune exigence nouvelle)", mut(lambda c: c.pop("direction", None), mode="LITE"), "pos", None),
]


def guards(off: Path):
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    A = (off / "ACTION.md").read_text(encoding="utf-8")
    boot = next((l for l in D.splitlines() if l.startswith("Avant le premier rendu, le boot")), "")
    l27 = next((l for l in D.splitlines() if l.startswith("La sortie de DIRECTION vers ACTION")), "")
    three = D[D.find("### Trois contrats à ne pas mélanger"):D.find("### Trois contrats à ne pas mélanger") + 900]
    handoff_row = next((l for l in three.splitlines() if l.startswith("| `HANDOFF`")), "")
    run_iter = A[A.find("### `ACTION/RUN-ITER`"):A.find("### `ACTION/RUN-STANDARD`")]
    return [
        ("G-01", "F-DIR-009", "Boot : modification et ré-observation seulement si une correction utile existe ; sinon la raison de l'arrêt",
         bool(re.search(r"(?i)correction utile", boot)) and bool(re.search(r"(?i)raison de l.arrêt", boot))),
        ("G-02", "F-DIR-003", "DIRECTION 27 renvoie à la colonne Phase de la table de correspondance d'ACTION/RUN_CARD",
         "ACTION/RUN_CARD" in l27 and bool(re.search(r"(?i)phase", l27))),
        ("G-03", "F-DIR-003", "contrat HANDOFF : sorties rangées « avant build » et « après observation »",
         bool(re.search(r"(?i)avant build", handoff_row)) and bool(re.search(r"(?i)après observation", handoff_row))),
        ("G-04", "F-DIR-036", "RUN-ITER : le rappel de direction est porté par direction.thesis dans une RUN_CARD", "direction.thesis" in run_iter),
    ]


def verdict(m, schema, d):
    try:
        m.validate_card(d, schema)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
        return False, f"EXCEPTION {type(e).__name__}: {e}"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        m, schema, fx, ex = load(root)
        rows = [("T-1", "B01", "exemple canonique accepté", *verdict(m, schema, ex))]
        for cid, fiche, label, build, kind, motive in CASES:
            ok, msg = verdict(m, schema, build(fx))
            rows.append((cid, fiche, label, ok if kind == "pos" else (not ok and motive in msg and not msg.startswith("EXCEPTION")), msg))
        g = guards(root / "V1/official")
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:10} {label}  [{msg[:70]}]")
    for cid, fiche, label, good in g:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:10} {label}")
    c = [r for r in rows if r[0].startswith("D2")]
    print(f"\nTémoin : {rows[0][3]:d}/1 ; RUN_CARD D2 : {sum(r[3] for r in c)}/{len(c)} ; gardes : {sum(x[3] for x in g)}/{len(g)}")
    return 0 if all(r[3] for r in rows) and all(x[3] for x in g) else 1


if __name__ == "__main__":
    sys.exit(main())
