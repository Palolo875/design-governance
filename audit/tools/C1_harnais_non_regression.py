#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.08 PATCH-DECISION C1 — harnais (registres, temps, sémantique de preuve).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C1_harnais_non_regression.py <racine>

Deux parties :
  1. MACHINE (6 invariants, dont 1 assouplissement : verdict nullable) — cartes construites en mémoire,
     sur une base conforme aux contrats B2 à B4 ; motif exigé (règle A2).
  2. GARDES TEXTUELLES (corrections normatives) — présence ou absence de formulations.
     Elles ne remplacent pas l'épreuve de lecture (§7 du rapport).
Champs attendus APRÈS correction (noms indicatifs) :
  decision_change {outcome ∈ {CHANGED, CONFIRMED, ABANDONED, N/A-JUSTIFIED, NOT-OBSERVED}, value, evidence, reason?}
  closure.verdict nullable ; closure.reclassification {to_mode, successor_run_ref}
  profile_decision.phase ∈ {intended, observed}
  creative_close.next_polish_action : INCHANGÉ (chaîne) ; « STOP — raison » documenté comme valide
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

RES = {"owner": "Owner", "scope": "Scène 1", "date_version": "2026-09-25 / V1", "impact": "Limite de calibration",
       "next_proof": "Capture V2", "review_date": "2026-10-09", "exit_condition": "Capture V2 revue"}


def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    return m, schema, ex


def base(ex):
    """Carte DIRECTION acceptée avec réserve, conforme aux contrats B2–B4 et C1."""
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["artifact"].update(version=c["proof"]["provenance"]["artifact_version"], rights_status="cleared")
    c["capability_profile"]["basis"] = [{"capability": "navigateur/capture disponible", "kind": "tool_result", "detail": "Capture"}]
    c["proof"]["provenance"]["capability"] = "navigateur/capture disponible"
    c["closure"].update(axes={"V": "PASS", "U": "PASS", "A": "NOT-VERIFIED", "T": "PASS"}, reservations=[dict(RES)],
                        b1b={"status": "DONE", "pair": {"before_locator": "c/v1.png", "after_locator": "c/v1b.png",
                                                       "decision": "Relief porteur", "outcome": "confirmed"}})
    c["anchors"][0].update(type="observed", date="2026-09-18")
    c["direction"]["identity_stake"] = "normal"
    c["decision_change"] = {"outcome": "CONFIRMED", "value": "Le relief porte la promesse", "evidence": "Paire B1b c/v1 → c/v1b"}
    return d


def mut(fn):
    def b(ex):
        d = base(ex)
        fn(d["run_card"])
        return d
    return b


def intake(ex):
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["closure"].update(state="INTAKE", verdict=None, issue=None)
    c["closure"].pop("direction_status", None)
    c.pop("creative_close", None)
    c.pop("decision_change", None)
    return d


MACHINE = [
    ("C1-01", "F-ACT-013/014", "decision_change sans outcome", mut(lambda c: c["decision_change"].pop("outcome")), "neg", "decision_change exige outcome"),
    ("C1-02", "F-ACT-014", "outcome NOT-OBSERVED + ACCEPTED", mut(lambda c: (c["decision_change"].update(outcome="NOT-OBSERVED"), c["closure"]["axes"].update(A="PASS"), c["closure"].update(verdict="ACCEPTED"))), "neg", "NOT-OBSERVED interdit ACCEPTED"),
    ("C1-03", "F-DIR-011", "outcome N/A-JUSTIFIED sans raison", mut(lambda c: c["decision_change"].update(outcome="N/A-JUSTIFIED")), "neg", "N/A-JUSTIFIED exige une raison"),
    ("C1-04", "F-ACT-013", "STANDARD clos et accepté sans decision_change", mut(lambda c: (c.__setitem__("mode", "STANDARD"), c.pop("decision_change"))), "neg", "exige decision_change"),
    ("C1-05", "F-ACT-009", "state BUILDING avec verdict", mut(lambda c: c["closure"].update(state="BUILDING", verdict="RETURN")), "neg", "verdict doit rester null avant CHECKING"),
    ("C1-06", "F-ACT-009", "state CLOSED sans verdict", mut(lambda c: c["closure"].update(verdict=None)), "neg", "exige un verdict"),
    ("C1-07", "F-ACT-011", "RECLASSIFIED sans transition", mut(lambda c: c["closure"].update(issue="RECLASSIFIED", verdict="RETURN")), "neg", "RECLASSIFIED exige closure.reclassification"),
    ("C1-08", "F-ACT-011", "reclassement vers le même mode", mut(lambda c: c["closure"].update(issue="RECLASSIFIED", verdict="RETURN", reclassification={"to_mode": "DIRECTION", "successor_run_ref": "run-043"})), "neg", "mode cible identique"),
    ("C1-09", "F-SAV-005", "profil seulement visé dans une carte acceptée", mut(lambda c: c.__setitem__("profile_decision", {"phase": "intended", "decision": "Voix typographique", "dials": "densité +", "counterindication": "données denses", "evidence": "Capture prévue"})), "neg", "profil non observé"),
    ("C1-P1", "tous", "carte acceptée avec decision_change CONFIRMED → acceptée", base, "pos", None),
    ("C1-P2", "F-ACT-009", "carte INTAKE sans verdict prématuré → acceptée", intake, "pos", None),
    ("C1-P3", "F-ACT-025", "next_polish_action « STOP — raison » (convention texte, champ inchangé) → acceptée", mut(lambda c: c["creative_close"].update(next_polish_action="STOP — le gain suivant serait du polish")), "pos", None),
    ("C1-P4", "proportion", "LITE clos et accepté sans decision_change → acceptée", mut(lambda c: (c.__setitem__("mode", "LITE"), c.pop("decision_change"), c["closure"].pop("direction_status", None))), "pos", None),
]


def text_guards(off: Path):
    d = (off / "DIRECTION.md").read_text(encoding="utf-8")
    a = (off / "ACTION.md").read_text(encoding="utf-8")
    s = (off / "SAVOIR.md").read_text(encoding="utf-8")
    # 12.05b R-11 : la tranche s'arrêtait au premier « ## » trouvé, donc au premier sous-titre « ### » ; elle couvre désormais la section entière
    status = a[a.find("## ACTION/STATUS"):a.find("\n## ", a.find("## ACTION/STATUS") + 5)]
    truth = d[d.find("### Vérité de la scène"):d.find("## DIRECTION/DOUBLE-LOOP")]
    style = s[s.find("PROFILE-DECISION"):s.find("PROFILE-DECISION") + 1500]
    return [
        ("G-01", "F-ACT-014", "ACTION/STATUS place NOT-OBSERVED (conséquence décisionnelle)", "NOT-OBSERVED" in status),
        ("G-02", "F-DIR-011/019", "DIRECTION emploie la triade (NOT-OBSERVED aux trois occurrences au moins)", d.count("NOT-OBSERVED") >= 3),
        ("G-03", "F-DIR-029", "les labels TRUTH se cumulent (factualité × nature)", bool(re.search(r"(?i)cumul", truth))),
        ("G-04", "F-DIR-021", "règle d'audience : pas de label interne dans l'interface ; divulgation en langage produit", bool(re.search(r"(?i)langage produit", truth))),
        ("G-05", "F-DIR-024", "la ligne « Preuve » de VISUAL_TARGET devient « Objet de preuve »", "| **Objet de preuve** |" in d),
        ("G-06", "F-DIR-032", "ABSOLU 5 renvoie le choix de méthode à ACTION ou SAVOIR", bool(re.search(r"personnes représentatives[^\n]*(ACTION/GATE-B|SAVOIR/CONTEXT|méthode)", d))),
        ("G-07", "F-DIR-033", "la troisième taxonomie « trois niveaux de preuve » est supprimée", "Distingue trois niveaux de preuve" not in d),
        ("G-08", "F-ACT-027", "ACTION 509 déclare CORRECTED / ACCEPTED-DIFFERENCE / REMAINING-RISK comme résultats locaux avec correspondance", bool(re.search(r"(?i)résultats? locaux", a))),
        ("G-10", "F-ACT-025", "ACTION documente « STOP — raison » comme valeur valide de next_polish_action", "STOP —" in a),
        ("G-09", "F-SAV-005", "STYLE sépare l'intention de profil et l'effet observé", bool(re.search(r"(?i)intention", style)) and bool(re.search(r"(?i)après (observation|capture)", style))),
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
        m, schema, ex = load(root)
        rows = [("T-POS-1", "B01", "exemple canonique accepté", *verdict(m, schema, ex))]
        for cid, fiche, label, build, kind, motive in MACHINE:
            ok, msg = verdict(m, schema, build(ex))
            rows.append((cid, fiche, label, ok if kind == "pos" else (not ok and motive in msg and not msg.startswith("EXCEPTION")), msg))
        guards = text_guards(root / "V1/official")
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:14} {label}  [{msg[:70]}]")
    for gid, fiche, label, good in guards:
        print(f"{'OK  ' if good else 'ÉCHEC'} {gid:6} {fiche:14} {label}")
    mach = [r for r in rows if r[0].startswith("C1")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; machine C1 : {sum(r[3] for r in mach)}/{len(mach)} ; gardes : {sum(g[3] for g in guards)}/{len(guards)}")
    return 0 if all(r[3] for r in rows) and all(g[3] for g in guards) else 1


if __name__ == "__main__":
    sys.exit(main())
