#!/usr/bin/env python3
"""DG-AUDIT-001 — 13.01 — vérifications complémentaires de la validation à cinq couches.

Artefact d'audit HORS package. Lecture seule des racines visées ; toute exécution se fait sur copie temporaire.

Usage :
  python3 DG_AUDIT_001_Verifications_13-01.py texte <racine>                 # V-1 à V-6 (fiches sans garde dédiée)
  python3 DG_AUDIT_001_Verifications_13-01.py mutations <racine>             # chaque V-x retiré du texte → rouge
  python3 DG_AUDIT_001_Verifications_13-01.py distributions <github.zip> <local.zip>
  python3 DG_AUDIT_001_Verifications_13-01.py non-regression <racine_B01> <racine_B03>
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def read(root: Path, rel: str) -> str:
    p = root / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def section(text: str, start: str, stop: str) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(stop, i + len(start))
    return text[i: j if j > 0 else len(text)]


# (ID, fiche, libellé, fichier, prédicat, fragment à retirer pour la mutation)
CHECKS = [
    ("V-1", "F-ACT-019", "snapshot datable : RUN-ID, SOURCE-VERSION / ARTIFACT-VERSION, GENERATED-AT", "V1/official/ACTION.md",
     lambda t: all(k in t for k in ("RUN-ID", "SOURCE-VERSION / ARTIFACT-VERSION", "GENERATED-AT")) and "datable" in t, "GENERATED-AT"),
    ("V-2", "F-ACT-028", "règle « hors projection » : un champ hors projection n'est jamais glissé dans un champ voisin ; il reste dans la trace", "V1/official/ACTION.md",
     lambda t: bool(re.search(r"hors projection[^\n]*jamais glissé dans un champ voisin", t)) and "**hors projection : trace**" in t, "jamais glissé dans un champ voisin"),
    ("V-3", "F-DIR-016", "traduction humaine de START : une question de risque dominant (« coûterait cher si c'était faux »)", "V1/official/DIRECTION.md",
     lambda t: bool(re.search(r"coûterait cher si c’était faux \? \| `RISK`", section(t, "Traduction humaine minimale", "## DIRECTION/FIRST-OBJECT"))), "coûterait cher si c’était faux"),
    ("V-4", "F-QS-003", "QUICKSTART : conditions de fermeture par issue ; archiver un blocage n'exige aucune approbation", "V1/official/QUICKSTART.md",
     lambda t: "Archiver un blocage n’exige aucune approbation" in t and "archive simple pour `BLOCKED`" in t and "l’owner, l’approbation, la limite" not in t,
     "Archiver un blocage n’exige aucune approbation"),
    ("V-5", "F-VRC-005", "profil strict : locators relatifs résolus depuis le dossier de la carte (texte ; l'épreuve machine est C4-P3)", "V1/official/ACTION.md",
     lambda t: "résolus depuis le dossier de la carte" in t, "résolus depuis le dossier de la carte"),
    ("V-6", "F-ACT-021", "CLOSE-PACKAGE : colonne « Contrôle machine » et « Un verdict vert ne certifie que ce que la liste close contrôle »", "V1/official/ACTION.md",
     lambda t: "| Mode | Paquet minimal | Contrôle machine |" in t and "Un verdict vert ne certifie que ce que la liste close contrôle" in t,
     "Un verdict vert ne certifie que ce que la liste close contrôle"),
]


def texte(root: Path) -> list[tuple[str, str, str, bool]]:
    return [(cid, fiche, label, pred(read(root, rel))) for cid, fiche, label, rel, pred, _ in CHECKS]


def mutations(root: Path) -> list[tuple[str, str, str, bool]]:
    out = []
    for cid, fiche, label, rel, pred, frag in CHECKS:
        text = read(root, rel)
        mutated = text.replace(frag, "[retiré]")
        out.append((f"M{cid}", fiche, f"{frag!r} retiré → rouge", mutated != text and not pred(mutated)))
    return out


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=1200)
    return r.returncode, (r.stdout + r.stderr).strip()


def last(out: str) -> str:
    return out.splitlines()[-1][:120] if out else ""


def distributions(github_zip: Path, local_zip: Path) -> list[tuple[str, str, str, bool]]:
    rows = []
    # Rectification déclarée (audit progressif, C21, `V12R_43`) : le manifeste est lu dans l'archive GitHub elle-même,
    # indépendamment des interpréteurs ; un interpréteur absent est « non exécuté » (None), distinct d'un échec.
    with zipfile.ZipFile(github_zip) as archive:
        manifest = json.loads(archive.read("scripts/package_manifest.json").decode("utf-8"))
    for py in ("python3.10", "python3.13"):
        exe = shutil.which(py)
        if exe is None:
            rows.append((f"D-{py}", "—", f"{py} indisponible : D-1 à D-3 non exécutés pour cet interpréteur", None))
            continue
        with tempfile.TemporaryDirectory() as tmp:
            g, l = Path(tmp) / "github", Path(tmp) / "local"
            zipfile.ZipFile(github_zip).extractall(g)
            zipfile.ZipFile(local_zip).extractall(l)
            (g / "scripts/build_distributions.sh").chmod(0o755)
            code, out = run([exe, "-B", "scripts/validate_all.py"], g)
            rows.append((f"D-1 ({py})", "distribution GitHub", f"validate_all autonome → FULL VALIDATION PASSED [{last(out)}]", code == 0 and "FULL VALIDATION PASSED" in out))
            code, out = run([exe, "-B", "scripts/validate_all.py"], l)
            rows.append((f"D-2 ({py})", "distribution Local", f"validate_all autonome → LOCAL VALIDATION PASSED [{last(out)}]", code == 0 and "LOCAL VALIDATION PASSED" in out))
            code, out = run([exe, "-B", "scripts/read_route.py", "DIRECTION/START/TREE"], l)
            rows.append((f"D-3 ({py})", "F-RM-003 (Local)", "read_route DIRECTION/START/TREE servi dans l'export Local", code == 0 and "Arbre de classification" in out))
    for kind, z in (("github", github_zip), ("local", local_zip)):
        names = [i.filename for i in zipfile.ZipFile(z).infolist() if not i.is_dir()]
        ok = sorted(names) == sorted(manifest[kind]) and len(names) == len(set(names))
        rows.append((f"D-4 ({kind})", "C8 O-2", f"membres de l'archive publiée = manifeste ({len(names)})", ok))
    with zipfile.ZipFile(local_zip) as z:
        skill = z.read("skill/SKILL.md").decode("utf-8")
        qs = z.read("official/QUICKSTART.md").decode("utf-8")
    rows.append(("D-5", "F-SK-002 / F-QS-004", "Local : aucun chemin GitHub dans la skill et QUICKSTART ; références de la skill citées",
                 "V1/official/" not in skill and "skills/design-governance-practice/" not in qs and "skill/references/examples.md" in qs))
    return rows


def verdicts(root: Path, files: list[Path]) -> dict[str, bool]:
    out = {}
    for f in files:
        code, _ = run([sys.executable, "-B", "scripts/validate_run_card.py", str(f)], root)
        out[f.name] = code == 0
    return out


def non_regression(b01: Path, b03: Path) -> list[tuple[str, str, str, bool]]:
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        c1, c3 = Path(tmp) / "b01", Path(tmp) / "b03"
        shutil.copytree(b01, c1)
        shutil.copytree(b03, c3)
        names = sorted({p.name for p in (c1 / "schemas/fixtures").glob("*.json")} & {p.name for p in (c3 / "schemas/fixtures").glob("*.json")})
        v1 = verdicts(c1, [c1 / "schemas/fixtures" / n for n in names])
        v3 = verdicts(c3, [c3 / "schemas/fixtures" / n for n in names])
        diff = [n for n in names if v1[n] != v3[n]]
        rows.append(("N-1", "A2 / 12.04", f"fixtures communes : même verdict B01 et B03 ({len(names) - len(diff)}/{len(names)}){' ; écarts : ' + ', '.join(diff) if diff else ''}", not diff))
        code, out = run([sys.executable, "-B", "scripts/validate_run_card.py", str(c1 / "schemas/run_card.example.json")], c3)
        rows.append(("N-2", "compatibilité V1.0.0 → V1.1.0", f"exemple canonique V1.0.0 sous le validateur V1.1.0 → refusé, comme l'annoncent les notes de version [{last(out)}]", code != 0 and "Traceback" not in out))
        for rel in ("schemas/examples/domain_frame.example.json", "schemas/examples/research_brief.example.json", "schemas/examples/production_contracts.example.json"):
            code, out = run([sys.executable, "-B", "scripts/validate_contracts.py", str(c3 / rel)], c3)
            rows.append((f"N-3 ({Path(rel).stem.split('.')[0]})", "C9 / E2", "exemple de contrat B03 validé en ciblé", code == 0))
    return rows


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    mode = sys.argv[1]
    if mode == "texte":
        rows = texte(Path(sys.argv[2]).resolve())
    elif mode == "mutations":
        rows = mutations(Path(sys.argv[2]).resolve())
    elif mode == "distributions":
        rows = distributions(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve())
    elif mode == "non-regression":
        rows = non_regression(Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve())
    else:
        print(__doc__)
        return 2
    for cid, fiche, label, ok in rows:
        print(f"{'OK  ' if ok else 'INDISP.' if ok is None else 'ÉCHEC'} {cid:14} {fiche:22} {label}")
    skipped = sum(1 for r in rows if r[3] is None)
    print(f"\n{mode} : {sum(1 for r in rows if r[3] is True)}/{len(rows)}" + (f" ({skipped} non exécuté(s))" if skipped else ""))
    return 0 if all(r[3] is True for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
