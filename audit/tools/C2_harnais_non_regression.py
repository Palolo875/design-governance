#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.09 PATCH-DECISION C2 — harnais (formes et projections).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C2_harnais_non_regression.py <racine>

Trois parties :
  1. RUN_CARD (validate_run_card.validate_card) — 1 invariant (INV-C2-1 risk.statement) et un témoin
     de conservation : un champ HANDOFF « hors projection » reste rejeté (aucun nouveau champ par défaut).
  2. CONTRATS DE PRODUCTION (validate_contracts.validate + semantic_check) — INV-C2-2 à INV-C2-4.
  3. GARDES TEXTUELLES — table de correspondance, renvois de façade, cible canonique, activation, phases.
Règle A2 : chaque négatif exige son motif (sous-chaîne stable du diagnostic).
Champs attendus APRÈS correction (noms indicatifs) :
  run_card.risk.statement : chaîne non vide, sans placeholder, requise dans tous les modes
  ui_ux_reality_pack : expected_scope (chaîne) + observed_scope (chaîne ou null) au lieu de proof_scope
  coverage_map[].proof_status ∈ {OBSERVED, NOT-VERIFIED, N/A-JUSTIFIED} ; reason requis si N/A-JUSTIFIED
  racine des contrats : les trois objets deviennent facultatifs, au moins un requis
Sur B01 : témoins 2/2 ; tous les autres cas échouent (défauts présents).
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
STATEMENT = "Promesse illisible sur mobile : la première scène ne rend pas l'incident crédible"


def mod(root: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, root / f"scripts/{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rj(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


# ---------- 1. RUN_CARD ----------
def base(ex):
    """Carte DIRECTION acceptée avec réserve, conforme aux contrats B2–B4, C1 et C2."""
    d = copy.deepcopy(ex)
    c = d["run_card"]
    c["risk"]["statement"] = STATEMENT
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
    def b(ex, fx):
        d = base(ex)
        fn(d["run_card"])
        return d
    return b


def witness_return(ex, fx):
    """Témoin de proportion : fixture valid_closed_return + le seul champ C2."""
    d = copy.deepcopy(fx)
    d["run_card"]["risk"]["statement"] = "Régression clavier chez un consumer du composant partagé"
    return d


RUNCARD = [
    ("C2-01", "F-ACT-017 (1)", "risque sans énoncé (niveau seul)", mut(lambda c: c["risk"].pop("statement")), "neg", "risk.statement"),
    ("C2-02", "F-ACT-017 (1)", "énoncé de risque placeholder « TBD »", mut(lambda c: c["risk"].update(statement="TBD")), "neg", "risk.statement"),
    ("C2-03", "F-ACT-017 (1)", "énoncé de risque blanc", mut(lambda c: c["risk"].update(statement="   ")), "neg", "risk.statement"),
    ("C2-P1", "tous", "carte DIRECTION acceptée avec énoncé de risque → acceptée", lambda ex, fx: base(ex), "pos", None),
    ("C2-P2", "proportion", "fixture valid_closed_return + énoncé de risque → acceptée", witness_return, "pos", None),
    ("C2-P3", "F-ACT-002", "LITE clos sans decision_change, EXIT-CONDITION portée par la réserve → acceptée",
     mut(lambda c: (c.__setitem__("mode", "LITE"), c.pop("decision_change"), c["closure"].pop("direction_status", None))), "pos", None),
]
# Témoin de conservation : la décision C2 n'ajoute PAS de champ HANDOFF ; il reste rejeté, pour ce motif.
CONSERVATION = ("T-CONS", "F-ACT-002", "champ HANDOFF next_action hors projection → rejeté (champs inconnus)",
                lambda ex: (lambda d: (d["run_card"].__setitem__("next_action", "Relancer la capture"), d)[1])(copy.deepcopy(ex)),
                "champs inconnus")


# ---------- 2. Contrats de production ----------
def cbase(pc):
    """Contrats conformes après correction : scope séparé, jetons canoniques, raison de N/A."""
    d = copy.deepcopy(pc)
    u = d["ui_ux_reality_pack"]
    # 12.04 R-8 : forme idempotente (l'exemple canonique est migré en 12.04 ; la conversion ne s'applique qu'à l'ancienne forme)
    if "proof_scope" in u:
        u["expected_scope"] = u.pop("proof_scope")
    u["observed_scope"] = "desktop 1440, clavier, données nominales et source indisponible"
    tok = {"observed": "OBSERVED", "not_verified": "NOT-VERIFIED"}
    for e in u["coverage_map"]:
        e["proof_status"] = tok.get(e["proof_status"], e["proof_status"])
    return d


def cmut(fn):
    def b(pc):
        d = cbase(pc)
        fn(d)
        return d
    return b


def na(d):
    d["ui_ux_reality_pack"]["coverage_map"][3].update(proof_status="N/A-JUSTIFIED")


def na_ok(d):
    d["ui_ux_reality_pack"]["coverage_map"][3].update(proof_status="N/A-JUSTIFIED", reason="aucun libellé long dans ce flux")


def before_build(d):
    u = d["ui_ux_reality_pack"]
    u["observed_scope"] = None
    for e in u["coverage_map"]:
        e["proof_status"] = "NOT-VERIFIED"


def only(key):
    return cmut(lambda d: [d.pop(k) for k in list(d) if k != key])


CONTRACTS = [
    ("K-01", "F-ACT-007", "proof_status taxonomie parallèle « observed »", cmut(lambda d: d["ui_ux_reality_pack"]["coverage_map"][0].update(proof_status="observed")), "neg", "valeur non canonique"),
    ("K-02", "F-ACT-007", "N/A-JUSTIFIED sans raison", cmut(na), "neg", "N/A-JUSTIFIED exige une raison"),
    ("K-03", "F-ACT-005", "exigence OBSERVED sans observed_scope", cmut(lambda d: d["ui_ux_reality_pack"].update(observed_scope=None)), "neg", "observed_scope"),
    # 12.04 R-8 : l'exemple migré ne porte plus proof_scope ; l'ancien champ est réinjecté pour vérifier qu'il reste refusé.
    ("K-04", "F-ACT-005", "ancien proof_scope unique (cible ou observation ?)",
     lambda pc: (lambda d: (d["ui_ux_reality_pack"].__setitem__("proof_scope", d["ui_ux_reality_pack"].get("expected_scope", "desktop 1440")), d)[1])(copy.deepcopy(pc)), "neg", "proof_scope"),
    ("K-05", "F-ACT-006", "document sans aucun contrat", lambda pc: {}, "neg", "au moins un contrat"),
    ("K-P1", "tous", "trois contrats conformes → acceptés", cbase, "pos", None),
    ("K-P2", "F-ACT-006", "UI_UX_REALITY_PACK seul → accepté", only("ui_ux_reality_pack"), "pos", None),
    ("K-P3", "F-ACT-006", "CREATIVE_DIRECTION_SET seul → accepté", only("creative_direction_set"), "pos", None),
    ("K-P4", "F-ACT-030", "pack avant build : tout NOT-VERIFIED, observed_scope null → accepté", cmut(before_build), "pos", None),
    ("K-P5", "F-ACT-007", "N/A-JUSTIFIED avec raison → accepté", cmut(na_ok), "pos", None),
]


# ---------- 3. Gardes textuelles ----------
def sec(text: str, head: str) -> str:
    i = text.find(head)
    if i < 0:
        return ""
    j = re.search(r"(?m)^##? ", text[i + len(head):])
    return text[i: i + len(head) + (j.start() if j else len(text))]


def sub(text: str, head: str) -> str:
    i = text.find(head)
    if i < 0:
        return ""
    j = re.search(r"(?m)^#{2,3} ", text[i + len(head):])
    return text[i: i + len(head) + (j.start() if j else len(text))]


def text_guards(off: Path):
    a = (off / "ACTION.md").read_text(encoding="utf-8")
    d = (off / "DIRECTION.md").read_text(encoding="utf-8")
    runcard = sec(a, "## ACTION/RUN_CARD")
    handoff = sub(a, "### ACTION/HANDOFF")
    uiux = sub(a, "### ACTION/UI-UX-REALITY")
    struct = sec(a, "## ACTION/STRUCTURED-PROOF")
    daily = d[d.find("`DAILY` est une vue de chargement"):d.find("**Déclenchement de l’atlas.**")]
    sec0 = sec(d, "## 0. Classification du mode")
    target = sec(d, "## DIRECTION/VISUAL_TARGET")
    return [
        ("G-01", "F-ACT-002", "ACTION/RUN_CARD : table de correspondance couvrant NEXT-ACTION, EXIT-CONDITION et « hors projection »",
         all(k in runcard for k in ("NEXT-ACTION", "EXIT-CONDITION")) and bool(re.search(r"(?i)hors projection", runcard))),
        ("G-02", "F-DIR-006", "la table couvre les vues DIRECTION (VISUAL_TARGET, creative close)", "VISUAL_TARGET" in runcard and "creative_close" in runcard),
        ("G-03", "F-DIR-039", "DIRECTION 716 déclare le transport du paquet d'alternative (trace), plus « la RUN_CARD nomme » seule",
         not re.search(r"Avant le build, la `RUN_CARD` nomme la position retenue", d) and bool(re.search(r"alternative[^\n]*trace", d))),
        ("G-04", "F-ACT-002", "HANDOFF déclare la forme courte LITE par renvoi à CLOSE-PACKAGE", "LITE" in handoff and "CLOSE-PACKAGE" in handoff),
        ("G-05", "F-DIR-010", "HANDOFF situe les formes (ligne de run, HANDOFF, CLOSE-PACKAGE, projection)", "ligne de run" in handoff and "projection" in handoff),
        ("G-06", "F-DIR-013", "DAILY : colonne « Clôture minimale » remplacée par un renvoi à ACTION/CLOSE-PACKAGE",
         "Clôture minimale |" not in daily and "ACTION/CLOSE-PACKAGE" in daily),
        ("G-07", "F-DIR-034/035", "section 0 : preuve minimale et condition d'arrêt renvoyées à ACTION (PRECONDITION, CLOSE-EXIT-CHECK)",
         "| Preuve minimale |" not in sec0 and "ACTION/PRECONDITION" in sec0 and "CLOSE-EXIT-CHECK" in sec0),
        ("G-08", "F-DIR-023", "VISUAL_TARGET : table canonique avec « Résolution initiale » ; la table des quatre décisions disparaît",
         "| **Résolution initiale** |" in target.split("### Compilation")[0] and "rends retrouvables quatre décisions" not in target),
        ("G-09", "F-DIR-023", "passage à SPECCED défini par renvoi à la table (et non par une énumération concurrente)",
         bool(re.search(r"Passage à `SPECCED`[^\n]*(table|champ)", target)) and "son anti-direction et son rendu attendu" not in target),
        ("G-10", "F-ACT-029", "STRUCTURED-PROOF ouvre sur une matrice d'activation avec N/A-JUSTIFIED", bool(re.search(r"(?i)déclencheur", struct)) and "N/A-JUSTIFIED" in struct),
        ("G-11", "F-ACT-030", "STRUCTURED-PROOF marque la phase des champs (avant / après build)", bool(re.search(r"(?i)après build", struct))),
        ("G-12", "F-ACT-005/007", "UI-UX-REALITY sépare scope attendu et scope observé et nomme les jetons canoniques",
         bool(re.search(r"(?i)scope attendu", uiux)) and bool(re.search(r"(?i)scope observé", uiux)) and "N/A-JUSTIFIED" in uiux),
    ]


def verdict_card(m, schema, d):
    try:
        m.validate_card(d, schema)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
        return False, f"EXCEPTION {type(e).__name__}: {e}"


def verdict_contract(m, schema, d):
    try:
        m.validate(d, schema)
        m.semantic_check("production_contracts", d)
        return True, "accepté"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"EXCEPTION {type(e).__name__}: {e}"


def judge(kind, motive, ok, msg):
    return ok if kind == "pos" else (not ok and motive in msg and not msg.startswith("EXCEPTION"))


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        vrc, vc = mod(root, "validate_run_card"), mod(root, "validate_contracts")
        rschema, ex = rj(root / "schemas/run_card.schema.json"), rj(root / "schemas/run_card.example.json")
        fx = rj(root / "schemas/fixtures/valid_closed_return.json")
        cschema, pc = rj(root / "schemas/production_contracts.schema.json"), rj(root / "schemas/examples/production_contracts.example.json")
        rows = [("T-POS-1", "B01", "exemple canonique RUN_CARD accepté", *verdict_card(vrc, rschema, ex))]
        tpos2 = verdict_contract(vc, cschema, pc)
        rows.append(("T-POS-2", "B01", "exemple canonique des contrats accepté", *tpos2))
        tid, tf, tl, tb, tm = CONSERVATION
        ok, msg = verdict_card(vrc, rschema, tb(ex))
        rows.append((tid, tf, tl, judge("neg", tm, ok, msg), msg))
        for cid, fiche, label, build, kind, motive in RUNCARD:
            ok, msg = verdict_card(vrc, rschema, build(ex, fx))
            rows.append((cid, fiche, label, judge(kind, motive, ok, msg), msg))
        for cid, fiche, label, build, kind, motive in CONTRACTS:
            ok, msg = verdict_contract(vc, cschema, build(pc))
            rows.append((cid, fiche, label, judge(kind, motive, ok, msg), msg))
        guards = text_guards(root / "V1/official")
    for r in rows:
        cid, fiche, label, good, msg = r
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:14} {label}  [{str(msg)[:70]}]")
    for gid, fiche, label, good in guards:
        print(f"{'OK  ' if good else 'ÉCHEC'} {gid:7} {fiche:14} {label}")
    t = [r for r in rows if r[0].startswith("T")]
    rc = [r for r in rows if r[0].startswith("C2")]
    k = [r for r in rows if r[0].startswith("K")]
    print(f"\nTémoins : {sum(r[3] for r in t)}/{len(t)} ; RUN_CARD C2 : {sum(r[3] for r in rc)}/{len(rc)} ; "
          f"contrats C2 : {sum(r[3] for r in k)}/{len(k)} ; gardes : {sum(g[3] for g in guards)}/{len(guards)}")
    return 0 if all(r[3] for r in rows) and all(g[3] for g in guards) else 1


if __name__ == "__main__":
    sys.exit(main())
