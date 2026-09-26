#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.04 PATCH-DECISION B2 — harnais (invariants d'acceptation).

Artefact d'audit HORS package ; copie temporaire ; cartes construites en mémoire
à partir de l'exemple canonique. Usage : python3 B2_harnais_non_regression.py <racine>

Champs attendus APRÈS correction (noms indicatifs, fixés en phase 12) :
  closure.axes {V,U,A,T} ; closure.reservations[] (structure ACTION 413–422) ;
  artifact.version ; artifact.rights_status ; proof.provenance.capability ;
  capability_profile.basis[] = {capability, kind, detail}.
Chaque négatif exige son MOTIF (règle A2). Les exigences nouvelles ne pèsent
que sur les cartes qui ACCEPTENT (et rights_status sur DIRECTION) : B2-P2
vérifie qu'une carte de retour simple reste valide sans aucun champ nouveau.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RES = {"owner": "Owner produit", "scope": "Note de bas de page, desktop", "date_version": "2026-09-25 / V2",
       "impact": "Lisibilité réduite d'une note secondaire", "next_proof": "Mesure de contraste après correction",
       "review_date": "2026-10-09", "exit_condition": "Contraste ≥ 4,5:1 mesuré sur V3"}


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    return m, schema, ex


def compliant(ex):
    """Base AWR conforme au contrat B2 (à partir de l'exemple DIRECTION)."""
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["artifact"]["version"] = c["proof"]["provenance"]["artifact_version"]
    c["artifact"]["rights_status"] = "cleared"
    c["capability_profile"]["basis"] = [
        {"capability": "navigateur/capture disponible", "kind": "tool_result", "detail": "Capture Chromium 141, 2026-08-29"}]
    c["proof"]["provenance"]["capability"] = "navigateur/capture disponible"
    c["closure"]["axes"] = {"V": "PASS", "U": "PASS", "A": "NOT-VERIFIED", "T": "PASS"}
    c["closure"]["reservations"] = [dict(RES)]
    return d


def mut(ex, fn):
    d = compliant(ex)
    fn(d["run_card"])
    return d


ROOT_HOLDER = {}


def returned_simple(ex):
    """Fixture officielle SYSTÈME RETURNED/RETURN, sans aucun champ B2."""
    return json.loads((ROOT_HOLDER["root"] / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8"))


def verdict(m, schema, d):
    try:
        m.validate_card(d, schema)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)


N, P = "neg", "pos"
C = []


def neg(cid, fiche, label, fn, motive):
    C.append((cid, fiche, label, lambda ex: mut(ex, fn), N, motive))


neg("B2-01", "F-ACT-010", "issue RETURNED + ACCEPTED", lambda c: c["closure"].update(issue="RETURNED", verdict="ACCEPTED"), "issue non nulle interdit un verdict accepté")
neg("B2-02", "F-ACT-010", "issue RECLASSIFIED + AWR", lambda c: c["closure"].update(issue="RECLASSIFIED"), "issue non nulle interdit un verdict accepté")
neg("B2-03", "F-ACT-010", "issue ESCALATED + AWR", lambda c: c["closure"].update(issue="ESCALATED"), "issue non nulle interdit un verdict accepté")
neg("B2-04", "F-ACT-010", "PARTIALLY-HELD + ACCEPTED", lambda c: (c["closure"].update(direction_status="PARTIALLY-HELD", verdict="ACCEPTED"), c["closure"]["axes"].update(A="PASS")), "PARTIALLY-HELD interdit ACCEPTED")
neg("B2-06", "F-ACT-012", "verdict accepté sans axes", lambda c: c["closure"].pop("axes"), "verdict accepté exige closure.axes")
neg("B2-07", "F-ACT-012", "axe A NOT-VERIFIED + ACCEPTED", lambda c: c["closure"].update(verdict="ACCEPTED"), "axe NOT-VERIFIED interdit ACCEPTED")
neg("B2-08", "F-ACT-012", "axe U RETURN + AWR", lambda c: c["closure"]["axes"].update(U="RETURN"), "axe RETURN interdit un verdict accepté")
neg("B2-09", "F-ACT-012/023", "axe V PASS-WITH-RESERVATION + ACCEPTED", lambda c: (c["closure"]["axes"].update(V="PASS-WITH-RESERVATION", A="PASS"), c["closure"].update(verdict="ACCEPTED")), "réserve d'axe interdit ACCEPTED")
neg("B2-10", "F-ACT-018", "capacité de provenance déclarée indisponible", lambda c: c["proof"]["provenance"].update(capability="clavier/AT non exécuté"), "provenance.capability doit être disponible")
neg("B2-11", "F-ACT-018", "basis déclarative pour la capacité de provenance", lambda c: c["capability_profile"]["basis"][0].update(kind="unattested_declaration"), "basis déclarative")
neg("B2-12", "F-ACT-022", "preuve V1, artefact V2", lambda c: c["artifact"].update(version="2026-09-25 / V2"), "version de preuve différente de la version d'artefact")
neg("B2-13", "F-ACT-022", "observed_at non daté", lambda c: c["proof"]["provenance"].update(observed_at="hier"), "observed_at doit être une date ISO")
neg("B2-14", "F-ACT-023", "AWR sans réserve structurée", lambda c: c["closure"].pop("reservations"), "ACCEPTED-WITH-RESERVATION exige closure.reservations")
neg("B2-15", "F-ACT-023", "réserve avec impact « à compléter »", lambda c: c["closure"]["reservations"][0].update(impact="à compléter"), "réserve incomplète ou placeholder")
neg("B2-16", "F-ACT-024", "droits inconnus + ACCEPTED", lambda c: (c["artifact"].update(rights_status="unknown"), c["closure"]["axes"].update(A="PASS"), c["closure"].update(verdict="ACCEPTED")), "droits inconnus interdisent ACCEPTED")
neg("B2-17", "F-ACT-024", "DIRECTION sans rights_status", lambda c: c["artifact"].pop("rights_status"), "DIRECTION exige artifact.rights_status")
C.append(("B2-P1", "tous", "carte AWR conforme au contrat B2 → acceptée", compliant, P, None))
C.append(("B2-P2", "proportion", "fixture valid_closed_return (retour simple, aucun champ B2) → acceptée", returned_simple, P, None))
C.append(("B2-P3", "F-RC-001", "ancre transformed + issue RETURNED + RETURN → acceptée", lambda ex: mut(ex, lambda c: c["closure"].update(issue="RETURNED", verdict="RETURN")), P, None))


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(Path(sys.argv[1]).resolve(), root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        ROOT_HOLDER["root"] = root
        m, schema, ex = load(root)
        rows = [("T-POS-1", "B01", "exemple canonique accepté", *verdict(m, schema, ex))]
        for cid, fiche, label, build, kind, motive in C:
            accepted, msg = verdict(m, schema, build(ex))
            good = accepted if kind == P else (not accepted and motive in msg)
            rows.append((cid, fiche, label, good, msg))
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:14} {label}  [{msg[:80]}]")
    b2 = [r for r in rows if r[0].startswith("B2")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; tests B2 : {sum(r[3] for r in b2)}/{len(b2)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
