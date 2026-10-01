#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.16 PATCH-DECISION C9 — harnais (contrats de production et de cadrage).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C9_harnais_non_regression.py <racine>

Parties :
  1. DOMAIN_FRAME   INV-C9-1 couverture risque → contrôle ou revue (policy_profile.risk_coverage) ; identité normalisée
  2. UI/UX PACK     INV-C9-3 liaison par entrée exacte ; chaque état de state_matrix couvert (forme après C2/C3)
  3. RESEARCH_BRIEF INV-C9-4 statut de source (fiche SAVOIR/SOURCE), source non placeholder, verified ⇒ locator et date
  4. CLI            F-ACT-008 : --type explicite, détection du type, fichier externe, chemin relatif
Règle A2 : chaque négatif exige son motif (sous-chaîne indicative).
Sur B01 : témoins 2/2 ; tous les autres cas échouent (défauts présents).
"""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def mod(root: Path):
    spec = importlib.util.spec_from_file_location("vc", root / "scripts/validate_contracts.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def rj(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


# ---------- formes après correction ----------
def df_base(df):
    d = copy.deepcopy(df)
    d["policy_profile"]["risk_coverage"] = [
        {"risk": "faux sentiment de sécurité", "control": "statut explicite"},
        {"risk": "surcharge en situation urgente", "review": "test de tâche sur incident (proof_requirements)"},
        {"risk": "alerte critique", "control": "inspection experte des alertes"},
    ]
    return d


def pc_base(pc):
    d = copy.deepcopy(pc)
    u = d["ui_ux_reality_pack"]
    # 12.04 R-8 : forme idempotente (l'exemple canonique est migré en 12.04 ; la conversion ne s'applique qu'à l'ancienne forme)
    if "proof_scope" in u:
        u["expected_scope"] = u.pop("proof_scope")
    u["observed_scope"] = "desktop 1440, clavier, données nominales et source indisponible"
    states = u["state_matrix"]
    u["coverage_map"] = [
        {"requirement": f"state_matrix: {s}", "artifact_locator": f"/incidents?state={i}",
         "proof_status": "OBSERVED" if "indisponible" in s else "NOT-VERIFIED"} for i, s in enumerate(states)
    ] + [
        # Rectification déclarée (audit progressif, C15 option a, `V12R_46`) : toute exigence déclarée est couverte,
        # au besoin en NOT-VERIFIED ; la base couvre donc chaque ligne des trois autres matrices, pas seulement deux.
        {"requirement": f"{matrix}: {item}", "artifact_locator": f"/incidents#{matrix}-{i}",
         "proof_status": "OBSERVED" if item == "focus visible" else "NOT-VERIFIED"}
        for matrix in ("responsive_matrix", "accessibility_basis", "robustness_basis") for i, item in enumerate(u[matrix])
    ]
    return d


def rb_base(rb):
    d = copy.deepcopy(rb)
    for e in d["entries"]:
        e.update(source_status="user_source_unverified", source_date="2026-09", source_locator="notes/entretiens-2026-09.md")
    return d


def m_df(fn):
    return lambda docs: (lambda d: (fn(d), d)[1])(df_base(docs["df"]))


def m_pc(fn):
    return lambda docs: (lambda d: (fn(d["ui_ux_reality_pack"]), d)[1])(pc_base(docs["pc"]))


def m_rb(fn):
    return lambda docs: (lambda d: (fn(d["entries"][0]), d)[1])(rb_base(docs["rb"]))


CASES = [
    ("D-01", "F-DF-001", "domain_frame", "risque nouveau (données personnelles) sans contrôle ni revue",
     m_df(lambda d: d["domain_risks"].append("exposition de données personnelles")), "neg", "risque sans contrôle ni revue"),
    ("D-02", "F-DF-001", "domain_frame", "couverture qui cite un contrôle absent de required_controls, sans revue",
     m_df(lambda d: d["policy_profile"]["risk_coverage"][0].update(control="contrôle inventé")), "neg", "contrôle inconnu"),
    ("D-P1", "F-DF-001", "domain_frame", "libellé équivalent (casse, espaces) → accepté",
     m_df(lambda d: d["policy_profile"]["risk_coverage"][2].update(risk="  Alerte  critique ")), "pos", None),
    ("D-P2", "F-DF-001", "domain_frame", "un même contrôle couvre deux risques → accepté",
     m_df(lambda d: d["policy_profile"]["risk_coverage"][0].update(control="inspection experte des alertes")), "pos", None),
    ("P-01", "F-PC-002", "production_contracts", "exigence fabriquée à partir de deux lignes (mots réutilisés)",
     m_pc(lambda u: u["coverage_map"].append({"requirement": "state_matrix: source indisponible données", "artifact_locator": "/x", "proof_status": "NOT-VERIFIED"})), "neg", "exigence absente des matrices"),
    ("P-02", "F-PC-002", "production_contracts", "état critique de state_matrix omis de la couverture",
     m_pc(lambda u: u.__setitem__("coverage_map", [e for e in u["coverage_map"] if "error source indisponible" not in e["requirement"]])), "neg", "état non couvert"),
    ("P-P1", "F-PC-002", "production_contracts", "liaison exacte, toutes les exigences déclarées couvertes → accepté", lambda docs: pc_base(docs["pc"]), "pos", None),
    ("R-01", "F-RB-001", "research_brief", "source « ? »", m_rb(lambda e: e.update(source="?")), "neg", "source placeholder"),
    ("R-02", "F-RB-001", "research_brief", "source vérifiée dans le run sans locator",
     m_rb(lambda e: (e.update(source_status="verified_in_run"), e.pop("source_locator"))), "neg", "exige un locator"),
    ("R-03", "F-RB-001", "research_brief", "statut de source hors fiche SOURCE", m_rb(lambda e: e.update(source_status="fiable")), "neg", "valeur non canonique"),
    ("R-P1", "F-RB-001", "research_brief", "connaissance non revérifiée, sans locator, date inconnue → acceptée (déclarée comme telle)",
     m_rb(lambda e: (e.update(source_status="unverified_knowledge", source_date="unknown"), e.pop("source_locator"))), "pos", None),
]


def verdict(m, schema, name, d):
    try:
        m.validate(d, schema)
        m.semantic_check(name, d)
        return True, "accepté"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
        return False, f"EXCEPTION {type(e).__name__}: {e}"


def cli(root: Path, args: list[str], cwd: Path):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/validate_contracts.py"), *args], cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    rows = []
    with tempfile.TemporaryDirectory() as tmpd:
        tmp = Path(tmpd)
        root = tmp / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        m = mod(root)
        sch = {n: rj(root / f"schemas/{n}.schema.json") for n in ("domain_frame", "research_brief", "production_contracts")}
        docs = {"df": rj(root / "schemas/examples/domain_frame.example.json"),
                "rb": rj(root / "schemas/examples/research_brief.example.json"),
                "pc": rj(root / "schemas/examples/production_contracts.example.json")}
        code, out = cli(root, [], root)
        rows.append(("T-1", "témoin", "suite validate_contracts sur B01 → PASS", code == 0, out.splitlines()[-1] if out else ""))
        code, out = cli(root, ["schemas/examples/domain_frame.example.json"], root)
        rows.append(("T-2", "témoin", "chemin canonique ciblé → PASS", code == 0, out.splitlines()[-1] if out else ""))
        for cid, fiche, name, label, build, kind, motive in CASES:
            ok, msg = verdict(m, sch[name], name, build(docs))
            good = ok if kind == "pos" else (not ok and motive in msg and not msg.startswith("EXCEPTION"))
            rows.append((cid, fiche, label, good, msg))
        ext = tmp / "projet"
        ext.mkdir()
        (ext / "cadrage.json").write_text(json.dumps(df_base(docs["df"]), ensure_ascii=False), encoding="utf-8")
        (ext / "brief.json").write_text(json.dumps(rb_base(docs["rb"]), ensure_ascii=False), encoding="utf-8")
        bad = df_base(docs["df"])
        bad["domain_risks"].append("exposition de données personnelles")
        (ext / "cadrage_invalide.json").write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
        code, out = cli(root, ["--type", "domain_frame", str(ext / "cadrage.json")], ext)
        rows.append(("L-01", "F-ACT-008", "fichier externe valide, --type explicite, chemin absolu → code 0", code == 0, out.splitlines()[-1] if out else ""))
        code, out = cli(root, ["brief.json"], ext)
        rows.append(("L-02", "F-ACT-008", "fichier externe valide, type détecté, chemin relatif → code 0", code == 0, out.splitlines()[-1] if out else ""))
        code, out = cli(root, ["--type", "domain_frame", "cadrage_invalide.json"], ext)
        rows.append(("L-03", "F-ACT-008", "fichier externe invalide → code 1, motif métier (pas « chemin non canonique »)",
                     code == 1 and "risque sans contrôle ni revue" in out, out.splitlines()[-1] if out else ""))
    for cid, fiche, label, good, msg in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:5} {fiche:10} {label}  [{str(msg)[:70]}]")
    t = [r for r in rows if r[0].startswith("T")]
    c = [r for r in rows if not r[0].startswith(("T", "L"))]
    l = [r for r in rows if r[0].startswith("L")]
    print(f"\nTémoins : {sum(r[3] for r in t)}/{len(t)} ; contrats C9 : {sum(r[3] for r in c)}/{len(c)} ; CLI : {sum(r[3] for r in l)}/{len(l)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
