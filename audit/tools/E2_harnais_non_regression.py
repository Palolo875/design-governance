#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.21 PATCH-DECISION E2 — harnais (lot technique : 18 fiches Mineur).

Artefact d'audit HORS package ; chaque scénario travaille sur une COPIE temporaire ; lecture seule des sources.
Usage : python3 E2_harnais_non_regression.py <racine>

Chaque cas exécute l'outil réel (validateur, lecteur, build) sur une copie modifiée et vérifie un comportement
attendu APRÈS correction. Règle A2 : un échec attendu doit être contrôlé (code non nul, sans traceback) et porter
son motif (sous-chaîne indicative). Les contrats sont construits sur la forme après C2, C3 et C9.
Fiches couvertes ailleurs (non rejouées ici) : F-VRC-005 (C4, cas C4-P3).
Sur B01 : témoin et conservation 2/2 ; les 22 cas du lot échouent (défauts présents).
Durée : environ une minute (validate_all et plusieurs builds complets).
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PY = sys.executable
IGNORE = shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip", ".dist.previous")


def fresh(src: Path, tmp: Path, name: str) -> Path:
    return Path(shutil.copytree(src, tmp / name, ignore=IGNORE))


def run(args, cwd, env=None, timeout=600):
    e = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", **(env or {}))
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=e, timeout=timeout)
    return r.returncode, r.stdout + r.stderr


def controlled_failure(code, out, motive):
    return code != 0 and "Traceback (most recent call last)" not in out and motive in out


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else "absent"


def tree_hash(d: Path) -> str:
    if not d.is_dir():
        return "absent"
    h = hashlib.sha256()
    for f in sorted(x for x in d.rglob("*") if x.is_file()):
        h.update(str(f.relative_to(d)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def shim(tmp: Path, name: str, body: str) -> dict:
    d = tmp / f"shim_{name}"
    d.mkdir(exist_ok=True)
    s = d / name
    s.write_text("#!/usr/bin/env bash\n" + body + "\n", encoding="utf-8")
    s.chmod(0o755)
    return {"PATH": f"{d}:{os.environ['PATH']}"}


def last(out: str) -> str:
    lines = [l for l in out.strip().splitlines() if l.strip()]
    return lines[-1] if lines else ""


# ---------- formes de contrats après C2, C3, C9 et E2 ----------
def df_after(df):
    d = copy.deepcopy(df)
    d["policy_profile"]["risk_coverage"] = [
        {"risk": "faux sentiment de sécurité", "control": "statut explicite"},
        {"risk": "surcharge en situation urgente", "review": "test de tâche sur incident"},
        {"risk": "alerte critique", "control": "inspection experte des alertes"},
    ]
    d["evidence_plan"] = [
        {"method": "comparaison desktop/tablette", "scope": "écran incidents, 1440 et 834", "artifact": "captures attendues v1",
         "limit": "pas de test utilisateur", "next_proof": "observation d'une tâche d'alerte"},
    ]
    return d


def rb_after(rb):
    d = copy.deepcopy(rb)
    for e in d["entries"]:
        e.update(source_status="user_source_unverified", source_date="2026-09", source_locator="notes/entretiens.md")
    return d


def contract_verdict(root: Path, name: str, doc):
    spec = importlib.util.spec_from_file_location("vc", root / "scripts/validate_contracts.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / f"schemas/{name}.schema.json").read_text(encoding="utf-8"))
    try:
        m.validate(doc, schema)
        m.semantic_check(name, doc)
        return True, "accepté"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # exception non gouvernée
        return False, f"EXCEPTION {type(e).__name__}: {e}"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    rows = []
    with tempfile.TemporaryDirectory() as tmpd:
        tmp = Path(tmpd)

        # Témoin : validate_all lancé depuis la racine
        root = fresh(src, tmp, "t1")
        code, out = run([PY, "scripts/validate_all.py"], root)
        rows.append(("T-1", "témoin", "validate_all depuis la racine → FULL VALIDATION PASSED", code == 0 and "FULL VALIDATION PASSED" in out, last(out)))

        # F-ALL-002 : validate_all depuis un dossier externe
        root = fresh(src, tmp, "all")
        ext = tmp / "ailleurs"
        ext.mkdir()
        code, out = run([PY, str(root / "scripts/validate_all.py")], ext)
        rows.append(("E2-01", "F-ALL-002", "validate_all lancé depuis un dossier externe → même résultat", code == 0 and "FULL VALIDATION PASSED" in out, last(out)))

        # F-BLD-002 : échec du second zip → artefacts antérieurs intacts
        root = fresh(src, tmp, "bld2")
        run(["bash", "scripts/build_distributions.sh"], root)
        before = (sha(root / "Design_Governance_V1_GITHUB.zip"), tree_hash(root / "dist"))
        with open(root / "RELEASE_NOTES.md", "a", encoding="utf-8") as f:
            f.write("\nLigne ajoutée pour produire une archive différente.\n")
        code, out = run(["bash", "scripts/build_distributions.sh"], root,
                        env=shim(tmp, "zip", 'for a in "$@"; do [[ "$a" == *LOCAL* ]] && exit 12; done; exec /usr/bin/zip "$@"'))
        after = (sha(root / "Design_Governance_V1_GITHUB.zip"), tree_hash(root / "dist"))
        rows.append(("E2-02", "F-BLD-002", "échec du zip Local → archive GitHub et dist antérieurs intacts", code != 0 and after == before,
                     f"code {code} ; archive GitHub {'inchangée' if after[0] == before[0] else 'MODIFIÉE'} ; dist {'intact' if after[1] == before[1] else 'MODIFIÉ'}"))

        # F-BLD-003 : panne pendant la promotion → dist restauré
        root = fresh(src, tmp, "bld3")
        run(["bash", "scripts/build_distributions.sh"], root)
        before = tree_hash(root / "dist")
        code, out = run(["bash", "scripts/build_distributions.sh"], root,
                        env=shim(tmp, "mv", '[[ "$1" == */.build/dist ]] && exit 1; exec /bin/mv "$@"'))
        after = tree_hash(root / "dist")
        rows.append(("E2-03", "F-BLD-003", "échec du déplacement de promotion → dist antérieur restauré", code != 0 and after == before,
                     f"code {code} ; dist {'restauré' if after == before else ('ABSENT' if after == 'absent' else 'MODIFIÉ')}"))

        # Contrats (F-DF-002, F-RB-002)
        root = fresh(src, tmp, "contracts")
        df = json.loads((root / "schemas/examples/domain_frame.example.json").read_text(encoding="utf-8"))
        rb = json.loads((root / "schemas/examples/research_brief.example.json").read_text(encoding="utf-8"))
        d = df_after(df)
        d["evidence_plan"] = [dict(d["evidence_plan"][0], method="à déterminer")]
        ok, msg = contract_verdict(root, "domain_frame", d)
        rows.append(("E2-04", "F-DF-002", "plan de preuve « à déterminer » → rejeté (motif : placeholder)", not ok and "evidence_plan" in msg and "placeholder" in msg and not msg.startswith("EXCEPTION"), msg))
        ok, msg = contract_verdict(root, "domain_frame", df_after(df))
        rows.append(("E2-05", "F-DF-002", "plan de preuve à cinq composantes, artefact attendu → accepté", ok, msg))
        d = rb_after(rb)
        # 12.04 R-10 : INV-E2-2 (décision E2 §4) — sans entrée, l'incertitude reste celle de départ
        d.update(depth="none", entries=[], uncertainty_after=d["uncertainty_before"])
        ok, msg = contract_verdict(root, "research_brief", d)
        rows.append(("E2-06", "F-RB-002", "recherche non déclenchée (depth none, aucune entrée) → acceptée", ok, msg))
        d = rb_after(rb)
        d["stop_condition"] = "à déterminer"
        ok, msg = contract_verdict(root, "research_brief", d)
        rows.append(("E2-07", "F-RB-002", "condition d'arrêt « à déterminer » → rejetée", not ok and "placeholder" in msg and not msg.startswith("EXCEPTION"), msg))
        d = rb_after(rb)
        d["uncertainty_after"] = d["uncertainty_before"]
        ok, msg = contract_verdict(root, "research_brief", d)
        rows.append(("E2-08", "F-RB-002", "incertitude restante (avant = après), déclarée → acceptée", ok, msg))

        # F-MAN-001, F-MAN-002
        for cid, fiche, label, mut, motive in (
            ("E2-09", "F-MAN-001", "entrée dupliquée dans le manifeste → rejet", lambda m: m["github"].append(m["github"][0]), "doublon"),
            ("E2-10", "F-MAN-002", "version du manifeste divergente (9.9.9) → rejet", lambda m: m.update(version="9.9.9"), "version"),
            ("E2-11", "F-MAN-002", "version du manifeste absente → rejet", lambda m: m.pop("version"), "version")):
            root = fresh(src, tmp, cid)
            p = root / "scripts/package_manifest.json"
            m = json.loads(p.read_text(encoding="utf-8"))
            mut(m)
            p.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
            code, out = run([PY, "scripts/validate_design_governance.py"], root)
            rows.append((cid, fiche, label, controlled_failure(code, out, motive), last(out)))

        # F-RRT-001 : titres dans des blocs de code
        root = fresh(src, tmp, "rrt")
        a = root / "V1/official/ACTION.md"
        t = a.read_text(encoding="utf-8")
        t = t.replace("### `ACTION/RUN-LITE`", "```text\n### `ACTION/RUN-LITE`\nbloc factice\n```\n\n### `ACTION/RUN-LITE`", 1)
        t = t.replace("**Faire.** Écrire la ligne de run", "```bash\n# commentaire de code\n```\n\n**Faire.** Écrire la ligne de run", 1)
        a.write_text(t, encoding="utf-8")
        code, out = run([PY, "scripts/read_route.py", "ACTION/RUN-LITE"], root)
        rows.append(("E2-12", "F-RRT-001", "titre factice dans un bloc de code ignoré ; « # » de code ne tronque pas le bloc",
                     code == 0 and "bloc factice" not in out and "**Clôture.**" in out, f"code {code}"))

        # F-VCT-002
        root = fresh(src, tmp, "vct")
        p = root / "schemas/examples/domain_frame.example.json"
        p.write_text("[]", encoding="utf-8")
        code, out = run([PY, "scripts/validate_contracts.py", str(p)], root)
        rows.append(("C-01", "F-VCT-002", "conservation : racine [] → échec contrôlé (déjà vrai sur B01)", controlled_failure(code, out, "VALIDATION FAILED"), last(out)))
        p.write_bytes(b"\xff\xfe{")
        code, out = run([PY, "scripts/validate_contracts.py", str(p)], root)
        rows.append(("E2-14", "F-VCT-002", "octets non UTF-8 → échec contrôlé", controlled_failure(code, out, "VALIDATION FAILED"), last(out)))

        # F-VDG-002, F-VDG-004
        root = fresh(src, tmp, "vdg2")
        a = root / "V1/official/ACTION.md"
        a.write_text(a.read_text(encoding="utf-8") + "\n```JSON\n{\"run_card\": {}}\n```\n", encoding="utf-8")
        code, out = run([PY, "scripts/validate_design_governance.py"], root)
        rows.append(("E2-15", "F-VDG-002", "bloc ```JSON (majuscules) reconnu comme projection embarquée", controlled_failure(code, out, "projection"), last(out)))
        root = fresh(src, tmp, "vdg4")
        (root / "V1/official/README.md").unlink()
        code, out = run([PY, "scripts/validate_design_governance.py"], root)
        rows.append(("E2-16", "F-VDG-004", "README officiel absent → chemin cité, échec contrôlé", controlled_failure(code, out, "README.md"), last(out)))

        # F-VRC-001 à F-VRC-004
        root = fresh(src, tmp, "vrc")
        ex = (root / "schemas/run_card.example.json").read_text(encoding="utf-8")
        dup = root / "dup.json"
        dup.write_text(re.sub(r'"mode":\s*"DIRECTION"', '"mode": "LITE", "mode": "DIRECTION"', ex, count=1), encoding="utf-8")
        code, out = run([PY, "scripts/validate_run_card.py", str(dup)], root)
        rows.append(("E2-17", "F-VRC-001", "clé JSON répétée → rejet", controlled_failure(code, out, "clé répétée"), last(out)))
        bad = root / "bad.json"
        bad.write_bytes(b"\xff{")
        code, out = run([PY, "scripts/validate_run_card.py", str(bad)], root)
        rows.append(("E2-18", "F-VRC-002", "octet non UTF-8 → échec contrôlé", controlled_failure(code, out, "VALIDATION FAILED"), last(out)))
        doc = json.loads(ex)
        doc["run_card"]["proof"]["observed"] = [{"objet": "illégal"}]
        doc["run_card"]["closure"]["issue"] = []
        typ = root / "types.json"
        typ.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        code, out = run([PY, "scripts/validate_run_card.py", str(typ)], root)
        rows.append(("E2-19", "F-VRC-003", "types illégaux (objet dans observed, issue = []) → rejet propre", controlled_failure(code, out, "VALIDATION FAILED"), last(out)))
        real = root / "rendu.png"
        real.write_bytes(b"png")

        def located(d, art):
            d["run_card"]["artifact"]["locator"] = art
            d["run_card"]["proof"]["provenance"]["artifact_locator"] = art
            return d
        doc = located(json.loads(ex), str(real))
        doc["run_card"]["trace_locator"] = "https://["
        url = root / "url.json"
        url.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        code, out = run([PY, "scripts/validate_run_card.py", "--strict", str(url)], root)
        rows.append(("E2-20", "F-VRC-003", "URL mal formée en strict → rejet propre", controlled_failure(code, out, "VALIDATION FAILED"), last(out)))
        doc = located(json.loads(ex), "https://example.com/rendu")
        doc["run_card"]["trace_locator"] = "tickets/run-046.md"
        demo = root / "demo.json"
        demo.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        code, out = run([PY, "scripts/validate_run_card.py", "--strict", str(demo)], root)
        rows.append(("E2-21", "F-VRC-004", "hôte de démonstration dans artifact.locator (strict) → même refus que pour la trace", controlled_failure(code, out, "démonstration"), last(out)))

        # F-VRM-002 : section handoff vidée
        root = fresh(src, tmp, "vrm")
        rm = root / "V1/official/READING_MAP.md"
        t = rm.read_text(encoding="utf-8")
        t = re.sub(r"(## Handoff minimal commun\n)(.*?)(\n## )", r"\1\nSection vidée.\n\3", t, count=1, flags=re.S)
        rm.write_text(t, encoding="utf-8")
        code, out = run([PY, "scripts/validate_reading_map.py"], root)
        rows.append(("E2-22", "F-VRM-002", "section handoff de READING_MAP vidée → rouge (LCF-C1, C5)", code != 0 and "LCF-C1" in out, last(out)))

        # F-WF-001 : épinglage des actions par SHA
        wf = (src / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        uses = re.findall(r"uses:\s*([^\s]+)", wf)
        pinned = bool(uses) and all(re.search(r"@[0-9a-f]{40}$", u) for u in uses)
        rows.append(("E2-23", "F-WF-001", "actions du workflow épinglées par SHA complet (versions natives Node 24, run hébergé en phase 12)", pinned, ", ".join(uses)))

    for cid, fiche, label, ok, msg in rows:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:6} {fiche:10} {label}  [{str(msg)[:80]}]")
    t = [r for r in rows if r[0].startswith(("T", "C"))]
    e = [r for r in rows if r[0].startswith("E2")]
    print(f"\nTémoin et conservation : {sum(r[3] for r in t)}/{len(t)} ; lot E2 : {sum(r[3] for r in e)}/{len(e)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
