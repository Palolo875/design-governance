#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.10 PATCH-DECISION C3 — harnais (proportion).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C3_harnais_non_regression.py <racine>

Deux parties :
  1. CONTRATS (validate_contracts.validate + semantic_check) — INV-C3-1 et INV-C3-2 (authenticité des
     directions), retrait du quota « deux changements structurels », et un témoin de conservation :
     un ensemble à une seule direction reste rejeté (un ensemble compare au moins deux positions ;
     l'absence d'alternative plausible = contrat non activé, INV-C2-2).
     Les documents sont construits sur la forme APRÈS C2 (expected_scope / observed_scope, jetons canoniques).
  2. GARDES TEXTUELLES — contrat réduit unique, phases de DERIVE, deux sorties nommées (réponse visible,
     handoff) et alignement des façades (skill, QUICKSTART).
Règle A2 : chaque négatif exige son motif.
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

HANDOFF_FIELDS = ["MODE", "DECISION", "RISK", "SCOPE", "ARTIFACT", "OBSERVATION", "METHOD", "TRACE-LOCATOR",
              "NOT-VERIFIED", "DECISION-CHANGE", "NEXT-ACTION", "OWNER", "NEXT-PROOF", "EXIT-CONDITION"]


def mod(root: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, root / f"scripts/{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rj(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def cbase(pc):
    """Contrats conformes après C2."""
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
        fn(d["creative_direction_set"]) if "creative_direction_set" in d else None
        return d
    return b


def clone_second(cs, tweak=lambda s: s):
    a, b = cs["directions"][0], cs["directions"][1]
    b["tension"] = tweak(a["tension"])
    b["structural_changes"] = [tweak(x) for x in a["structural_changes"]]
    b["first_object"] = a["first_object"]


def single(cs):
    cs["directions"] = cs["directions"][:1]
    cs["selected_direction"] = cs["directions"][0]["id"]


def one_change(cs):
    for d in cs["directions"]:
        d["structural_changes"] = d["structural_changes"][:1]


def dup_change(cs):
    d = cs["directions"][0]
    d["structural_changes"] = [d["structural_changes"][0], d["structural_changes"][0]]


def no_creative(pc):
    d = cbase(pc)
    d.pop("creative_direction_set")
    return d


CONTRACTS = [
    ("C3-01", "F-PC-001", "deux IDs, textes identiques", cmut(clone_second), "neg", "directions non distinctes"),
    ("C3-02", "F-PC-001", "deux IDs, textes identiques à la casse et aux espaces près", cmut(lambda cs: clone_second(cs, lambda s: "  " + s.upper() + " ")), "neg", "directions non distinctes"),
    ("C3-03", "F-PC-001", "un même changement structurel compté deux fois", cmut(dup_change), "neg", "changements structurels en double"),
    ("C3-P1", "F-PC-001", "directions à un seul levier structurel chacune → acceptées (pas de quota)", cmut(one_change), "pos", None),
    ("C3-P2", "F-PC-001", "aucune alternative plausible : ensemble non activé, UI/UX seul → accepté (via INV-C2-2)", no_creative, "pos", None),
    ("C3-P3", "tous", "deux directions distinctes (exemple après C2) → acceptées", cbase, "pos", None),
]
CONSERVATION = ("T-CONS", "F-PC-001", "ensemble à une seule direction → rejeté (définition, pas quota)",
                lambda pc: (lambda d: (single(d["creative_direction_set"]), d)[1])(copy.deepcopy(pc)), "nombre minimal")


def section(text: str, head: str, level: str = "##") -> str:
    i = text.find(head)
    if i < 0:
        return ""
    j = re.search(rf"(?m)^{level} ", text[i + len(head):])
    return text[i: i + len(head) + (j.start() if j else len(text))]


def text_guards(root: Path):
    off = root / "V1/official"
    bib = (off / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    act = (off / "ACTION.md").read_text(encoding="utf-8")
    qs = (off / "QUICKSTART.md").read_text(encoding="utf-8")
    sk = (root / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8")
    contracts = section(bib, "## BIBLIOTHEQUE/CONTRACTS")
    reduced = contracts.split("\n\n")[1] if contracts.count("\n\n") > 1 else ""
    derive = section(bib, "### BIBLIOTHEQUE/DERIVE", "#{2,3}")
    levels = bib[bib.find("### Contrat minimal par périmètre"):bib.find("### Contrat minimal par périmètre") + 1200]
    local_row = next((l for l in levels.splitlines() if l.startswith("| Local")), "")
    handoff = section(act, "### ACTION/HANDOFF", "#{2,3}")
    sk_out = section(sk, "## Carte de lecture et sortie", "#{2,3}")
    return [
        ("G-01", "F-BIB-002", "CONTRACTS : contrat réduit unique (décision, responsabilité, contre-indication, preuve attendue, limite)",
         all(re.search(p, reduced, re.I) for p in (r"décision", r"responsabilit", r"contre-indication", r"preuve attendue", r"limite"))),
        ("G-02", "F-BIB-002", "table des niveaux : la ligne Local renvoie au contrat réduit de CONTRACTS", "CONTRACTS" in local_row),
        ("G-03", "F-BIB-002", "DERIVE : champs rangés par phase (départ / après objet / promotion)",
         bool(re.search(r"(?i)après (le premier )?objet|après observation", derive)) and bool(re.search(r"(?i)promotion", derive.split("```")[1] if derive.count("```") >= 2 else ""))),
        ("G-04", "F-SK-001", "ACTION/HANDOFF nomme deux sorties : réponse visible et handoff", bool(re.search(r"(?i)réponse visible", handoff))),
        ("G-05", "F-SK-001", "skill : plus de liste de onze champs « au minimum » ; les deux sorties renvoient à ACTION/HANDOFF",
         "restituez au minimum `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT`, `PROOF/TRACE-LOCATOR`" not in sk and "ACTION/HANDOFF" in sk_out and bool(re.search(r"(?i)réponse visible", sk))),
        ("G-06", "F-SK-001", "skill : la copie du handoff porte les treize champs canoniques (14 libellés, composites séparés)",
         all(f in sk_out for f in HANDOFF_FIELDS)),
        ("G-07", "F-SK-001", "QUICKSTART : plus de « sortie minimale d'un handoff » à onze champs ; renvoi à ACTION/HANDOFF",
         "La sortie minimale d’un handoff est : `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT`, `PROOF`" not in qs and "ACTION/HANDOFF" in qs),
        ("G-08", "F-SK-001", "la réponse visible de QUICKSTART est marquée « voir ACTION/HANDOFF » et identique au canon",
         bool(re.search(r"MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER", handoff)) and bool(re.search(r"(?i)voir `?ACTION/HANDOFF", qs))),
    ]


def verdict(m, schema, d):
    try:
        m.validate(d, schema)
        m.semantic_check("production_contracts", d)
        return True, "accepté"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
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
        vc = mod(root, "validate_contracts")
        schema = rj(root / "schemas/production_contracts.schema.json")
        pc = rj(root / "schemas/examples/production_contracts.example.json")
        rows = [("T-POS-1", "B01", "exemple canonique des contrats accepté", *verdict(vc, schema, pc))]
        tid, tf, tl, tb, tm = CONSERVATION
        ok, msg = verdict(vc, schema, tb(pc))
        rows.append((tid, tf, tl, judge("neg", tm, ok, msg), msg))
        for cid, fiche, label, build, kind, motive in CONTRACTS:
            ok, msg = verdict(vc, schema, build(pc))
            rows.append((cid, fiche, label, judge(kind, motive, ok, msg), msg))
        guards = text_guards(root)
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:10} {label}  [{str(msg)[:70]}]")
    for gid, fiche, label, good in guards:
        print(f"{'OK  ' if good else 'ÉCHEC'} {gid:7} {fiche:10} {label}")
    t = [r for r in rows if r[0].startswith("T")]
    k = [r for r in rows if r[0].startswith("C3")]
    print(f"\nTémoins : {sum(r[3] for r in t)}/{len(t)} ; contrats C3 : {sum(r[3] for r in k)}/{len(k)} ; gardes : {sum(g[3] for g in guards)}/{len(guards)}")
    return 0 if all(r[3] for r in rows) and all(g[3] for g in guards) else 1


if __name__ == "__main__":
    sys.exit(main())
