#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.06 PATCH-DECISION B4 — harnais (ancres).

Artefact d'audit HORS package ; copie temporaire ; cartes en mémoire.
Usage : python3 B4_harnais_non_regression.py <racine>

Suppose B2 et B3 en place (base DIRECTION conforme). Champs B4 attendus APRÈS
correction (noms indicatifs) :
  anchors[].type ∈ {generated, observed, provided} ; anchors[].date ISO 8601
  direction.identity_stake ∈ {high, normal}
  direction.calibration {basis ∈ {observed_anchor, provided_anchor, real_constraint,
                                  generated_only_reserved}, detail}
Règle A2 : chaque négatif exige son motif.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RES = {"owner": "Owner marque", "scope": "Première scène", "date_version": "2026-09-25 / V1",
       "impact": "Calibration externe absente", "next_proof": "Référence observée ou test public",
       "review_date": "2026-10-09", "exit_condition": "Ancre observée ou contrainte réelle intégrée"}
OBS = {"role": "verification", "source": "https://exemple.org/reference-ouverte", "date": "2026-09-20",
       "scope": "Rythme de la première scène", "retained": ["séquence en strates"], "rejected": ["copie de marque"],
       "transformation": "Principe de rythme reformulé pour le produit", "transformation_status": "transformed",
       "limitation": "Ne prouve pas l'adéquation au public", "type": "observed"}


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    return m, schema, ex


def base(ex, stake="high", anchors="generated+observed", calib=None):
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["artifact"]["version"] = c["proof"]["provenance"]["artifact_version"]
    c["artifact"]["rights_status"] = "cleared"
    c["capability_profile"]["basis"] = [{"capability": "navigateur/capture disponible", "kind": "tool_result", "detail": "Capture Chromium 141"}]
    c["proof"]["provenance"]["capability"] = "navigateur/capture disponible"
    c["closure"]["axes"] = {"V": "PASS", "U": "PASS", "A": "NOT-VERIFIED", "T": "PASS"}
    c["closure"]["reservations"] = [dict(RES)]
    c["closure"]["b1b"] = {"status": "DONE", "pair": {"before_locator": "captures/v1.png", "after_locator": "captures/v1b.png",
                                                     "decision": "Le relief porte la promesse", "outcome": "confirmed"}}
    c["anchors"][0]["type"] = "generated"
    c["anchors"][0]["date"] = "2026-09-18"
    if anchors == "generated+observed":
        c["anchors"].append(copy.deepcopy(OBS))
    c["direction"]["identity_stake"] = stake
    if calib:
        c["direction"]["calibration"] = calib
    return d


def with_(build, fn):
    def b(ex):
        d = build(ex)
        fn(d["run_card"])
        return d
    return b


GEN_ONLY = lambda ex: base(ex, anchors="generated")
RESERVED = {"basis": "generated_only_reserved", "detail": "Direction calibrée uniquement sur hypothèse générée, sans référence observée ni contrainte réelle."}

C = [
    ("B4-01", "F-DIR-027", "ancrage sans type", with_(base, lambda c: c["anchors"][0].pop("type")), "neg", "ancrage exige type"),
    ("B4-02", "F-SAV-003", "type « independent_review » (une revue n'est pas une ancre)", with_(base, lambda c: c["anchors"][0].update(type="independent_review")), "neg", "type"),
    ("B4-03", "F-DIR-027", "enjeu élevé, ancrage généré seul, HELD, sans calibration", GEN_ONLY, "neg", "ancrage généré seul exige calibration"),
    ("B4-04", "F-SAV-003", "calibration par « revue indépendante »", with_(GEN_ONLY, lambda c: c["direction"].update(calibration={"basis": "independent_review", "detail": "Avis d'un designer externe"})), "neg", "base de calibration non recevable"),
    ("B4-05", "F-DIR-027", "généré seul réservé + ACCEPTED", with_(GEN_ONLY, lambda c: (c["direction"].update(calibration=dict(RESERVED)), c["closure"]["axes"].update(A="PASS"), c["closure"].update(verdict="ACCEPTED"))), "neg", "calibration générée seule interdit ACCEPTED"),
    ("B4-06", "F-DIR-027", "DIRECTION sans ancrage + verdict accepté", with_(base, lambda c: c.__setitem__("anchors", [])), "neg", "DIRECTION sans ancrage : verdict accepté interdit"),
    ("B4-07", "F-DIR-027", "DIRECTION sans ancrage, sans issue", with_(base, lambda c: (c.__setitem__("anchors", []), c["closure"].update(verdict="EXPLORATORY", issue=None))), "neg", "DIRECTION sans ancrage exige une issue"),
    ("B4-08", "F-DIR-027", "date d'ancrage « récemment »", with_(base, lambda c: c["anchors"][0].update(date="récemment")), "neg", "date d'ancrage ISO"),
    ("B4-P1", "F-DIR-027", "enjeu élevé, généré + observé, HELD, AWR → acceptée", base, "pos", None),
    ("B4-P2", "F-DIR-027", "enjeu élevé, généré seul avec réserve de calibration, AWR → acceptée", with_(GEN_ONLY, lambda c: c["direction"].update(calibration=dict(RESERVED))), "pos", None),
    ("B4-P3", "F-DIR-027", "DIRECTION sans ancrage, EXPLORATORY honnête → acceptée (sérialisable sans mentir)",
     with_(base, lambda c: (c.__setitem__("anchors", []), c["closure"].update(issue="EXPLORATORY", verdict="EXPLORATORY", direction_status="PARTIALLY-HELD"))), "pos", None),
    ("B4-P4", "proportion", "enjeu normal, généré seul, HELD, AWR, sans calibration → acceptée", lambda ex: base(ex, stake="normal", anchors="generated"), "pos", None),
]


def verdict(m, schema, d):
    try:
        m.validate_card(d, schema)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(Path(sys.argv[1]).resolve(), root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        m, schema, ex = load(root)
        rows = [("T-POS-1", "B01", "exemple canonique accepté", *verdict(m, schema, ex))]
        for cid, fiche, label, build, kind, motive in C:
            ok, msg = verdict(m, schema, build(ex))
            rows.append((cid, fiche, label, ok if kind == "pos" else (not ok and motive in msg), msg))
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:10} {label}  [{msg[:75]}]")
    b4 = [r for r in rows if r[0].startswith("B4")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; tests B4 : {sum(r[3] for r in b4)}/{len(b4)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
