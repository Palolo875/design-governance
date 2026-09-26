#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.05 PATCH-DECISION B3 — harnais (paquets de clôture par mode et B1b).

Artefact d'audit HORS package ; copie temporaire ; cartes en mémoire.
Usage : python3 B3_harnais_non_regression.py <racine>

Suppose le contrat B2 en place (base conforme : axes, réserves, version, capacité,
droits). Champs B3 attendus APRÈS correction (noms indicatifs) :
  closure.system_package {impact, consumers[], owner, migration, rollback,
      non_regression {claim, baseline {locator, version, state}}, changelog_ref}
  closure.b1b {status: DONE | N/A-JUSTIFIED,
      DONE → pair {before_locator, after_locator, decision, outcome}
      N/A  → reason ∈ {no_editable_decision, equivalent_pair_valid},
             covered_decision, owner, next_proof (+ pair_ref si paire équivalente)}
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

RES = {"owner": "Owner système", "scope": "Deux consumers mobiles", "date_version": "2026-09-25 / V1",
       "impact": "Focus visible réduit en thème sombre", "next_proof": "Capture clavier thème sombre",
       "review_date": "2026-10-09", "exit_condition": "Focus ≥ 3:1 mesuré sur les deux consumers"}
SYS = {"impact": "Token sémantique action utilisé par 3 surfaces", "consumers": ["web/app", "mobile/ios", "mobile/android"],
       "owner": "Owner système", "migration": "Alias temporaire du token pendant 2 versions",
       "rollback": "Restaurer la valeur précédente du token (commit abc123)",
       "non_regression": {"claim": "Aucun écart hors intention sur les 3 consumers",
                          "baseline": {"locator": "baselines/action-token/", "version": "V1.4.0", "state": "défaut, focus, désactivé"}},
       "changelog_ref": "CHANGELOG 2026-09-25 — token action"}
B1B = {"status": "DONE", "pair": {"before_locator": "captures/scene-v1.png", "after_locator": "captures/scene-v1-sans-ornement.png",
                                   "decision": "Le relief porte la promesse « par strates »", "outcome": "confirmed"}}


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    return m, schema, ex


def b2_base(ex):
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["artifact"]["version"] = c["proof"]["provenance"]["artifact_version"]
    c["artifact"]["rights_status"] = "cleared"
    c["capability_profile"]["basis"] = [{"capability": "navigateur/capture disponible", "kind": "tool_result", "detail": "Capture Chromium 141"}]
    c["proof"]["provenance"]["capability"] = "navigateur/capture disponible"
    c["closure"]["axes"] = {"V": "PASS", "U": "PASS", "A": "NOT-VERIFIED", "T": "PASS"}
    c["closure"]["reservations"] = [dict(RES)]
    return d


def direction_ok(ex):
    d = b2_base(ex)
    d["run_card"]["closure"]["b1b"] = copy.deepcopy(B1B)
    return d


def system_ok(ex):
    d = b2_base(ex)
    c = d["run_card"]
    c["mode"] = "SYSTÈME"
    c["closure"]["system_package"] = copy.deepcopy(SYS)
    c["closure"].pop("direction_status", None)
    return d


def lite_ok(ex):
    d = b2_base(ex)
    c = d["run_card"]
    c["mode"] = "LITE"
    c["closure"].pop("direction_status", None)
    return d


def with_(base, fn):
    def build(ex):
        d = base(ex)
        fn(d["run_card"])
        return d
    return build


ROOT = {}
C = [
    ("B3-01", "F-ACT-015", "SYSTÈME accepté sans paquet", with_(system_ok, lambda c: c["closure"].pop("system_package")), "neg", "SYSTÈME accepté exige closure.system_package"),
    ("B3-02", "F-ACT-015", "SYSTÈME sans consumer", with_(system_ok, lambda c: c["closure"]["system_package"].update(consumers=[])), "neg", "system_package exige au moins un consumer"),
    ("B3-03", "F-ACT-015", "rollback « à déterminer »", with_(system_ok, lambda c: c["closure"]["system_package"].update(rollback="à déterminer")), "neg", "system_package incomplet ou placeholder"),
    ("B3-04", "F-ACT-031", "non-régression sans version de baseline", with_(system_ok, lambda c: c["closure"]["system_package"]["non_regression"]["baseline"].pop("version")), "neg", "baseline exige locator, version et état"),
    ("B3-05", "F-ACT-036", "DIRECTION acceptée, V PASS, sans B1b", with_(direction_ok, lambda c: c["closure"].pop("b1b")), "neg", "exige closure.b1b"),
    ("B3-06", "F-ACT-036", "paire B1b à captures identiques", with_(direction_ok, lambda c: c["closure"]["b1b"]["pair"].update(after_locator="captures/scene-v1.png")), "neg", "paire B1b : captures distinctes"),
    ("B3-07", "F-ACT-036/BIB-001", "N/A B1b pour « comparaison inutile »", with_(direction_ok, lambda c: c["closure"].update(b1b={"status": "N/A-JUSTIFIED", "reason": "comparaison inutile", "covered_decision": "x", "owner": "o", "next_proof": "p"})), "neg", "motif N/A B1b non recevable"),
    ("B3-08", "F-BIB-001", "N/A par paire équivalente sans référence de paire", with_(direction_ok, lambda c: c["closure"].update(b1b={"status": "N/A-JUSTIFIED", "reason": "equivalent_pair_valid", "covered_decision": "Le relief porte la promesse", "owner": "Owner", "next_proof": "Capture V2"})), "neg", "paire équivalente exige pair_ref"),
    ("B3-P1", "F-ACT-015/031", "SYSTÈME AWR avec paquet complet → acceptée", system_ok, "pos", None),
    ("B3-P2", "F-ACT-036", "DIRECTION AWR avec B1b réalisée → acceptée", direction_ok, "pos", None),
    ("B3-P3", "proportion", "fixture valid_closed_return (SYSTÈME, RETURN, sans paquet) → acceptée",
     lambda ex: json.loads((ROOT["r"] / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8")), "pos", None),
    ("B3-P4", "F-ACT-021", "LITE AWR sans paquet de mode (forme seule) → acceptée", lite_ok, "pos", None),
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
        ROOT["r"] = root
        m, schema, ex = load(root)
        rows = [("T-POS-1", "B01", "exemple canonique accepté", *verdict(m, schema, ex))]
        for cid, fiche, label, build, kind, motive in C:
            ok, msg = verdict(m, schema, build(ex))
            rows.append((cid, fiche, label, ok if kind == "pos" else (not ok and motive in msg), msg))
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:18} {label}  [{msg[:78]}]")
    b3 = [r for r in rows if r[0].startswith("B3")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; tests B3 : {sum(r[3] for r in b3)}/{len(b3)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
