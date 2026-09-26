#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.15 PATCH-DECISION C8 — harnais (intégrité de release).

Artefact d'audit HORS package ; chaque scénario travaille sur une copie temporaire ; lecture seule des sources.
Usage : python3 C8_harnais_non_regression.py <racine>

Chaque scénario exécute le vrai build (scripts/build_distributions.sh) sur une copie, puis compare les membres
des deux archives au manifeste (scripts/package_manifest.json : listes « github » et « local »).
  T-1  conservation : build propre → code 0 et membres = manifeste (60 / 56)
  R-1  F-BLD-001   archive ancienne contenant un membre périmé + sources propres → membres = manifeste
  R-2  F-BLD-004   fichier normatif remplacé par un lien symbolique → build refusé, motif « lien symbolique »
  R-3  F-VDG-001   fichier non déclaré sous V1/official/.build/ → build refusé, motif « fichier inattendu »,
                   et le fichier n'apparaît dans aucune archive
Sur B01 : T-1 réussit ; R-1, R-2 et R-3 échouent (défauts présents).
Durée : quatre builds complets (chacun rejoue les validateurs).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ZIPS = {"github": "Design_Governance_V1_GITHUB.zip", "local": "Design_Governance_V1_LOCAL.zip"}


def copy(src: Path, dst: Path) -> Path:
    shutil.copytree(src, dst, symlinks=True, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
    return dst


def build(root: Path):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run(["bash", "scripts/build_distributions.sh"], cwd=root, capture_output=True, text=True, env=env, timeout=600)
    return r.returncode, (r.stdout + r.stderr)


def members(root: Path, name: str) -> set[str]:
    p = root / ZIPS[name]
    if not p.is_file():
        return set()
    with zipfile.ZipFile(p) as z:
        return {n.removeprefix("./") for n in z.namelist() if not n.endswith("/")}


def manifest(root: Path) -> dict[str, set[str]]:
    m = json.loads((root / "scripts/package_manifest.json").read_text(encoding="utf-8"))
    return {"github": set(m["github"]), "local": set(m["local"])}


def diff(root: Path, man) -> str:
    out = []
    for k in ZIPS:
        got = members(root, k)
        extra, missing = sorted(got - man[k]), sorted(man[k] - got)
        if extra or missing:
            out.append(f"{k}: +{extra[:3]} -{missing[:3]}")
    return " ; ".join(out)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    rows = []
    with tempfile.TemporaryDirectory() as tmpd:
        tmp = Path(tmpd)

        # T-1 conservation
        root = copy(src, tmp / "t1")
        man = manifest(root)
        code, out = build(root)
        d = diff(root, man)
        rows.append(("T-1", "conservation", f"build propre : code 0 et membres = manifeste ({len(man['github'])}/{len(man['local'])})",
                     code == 0 and not d, f"code {code}" + (f" ; {d}" if d else "")))

        # R-1 archive périmée
        root = copy(src, tmp / "r1")
        with zipfile.ZipFile(root / ZIPS["github"], "w") as z:
            z.writestr("V1/official/ANCIEN_FICHIER_RETIRE.md", "contenu retiré des sources")
        code, out = build(root)
        d = diff(root, man)
        rows.append(("R-1", "F-BLD-001", "archive ancienne avec membre périmé, sources propres → membres = manifeste",
                     code == 0 and not d, f"code {code}" + (f" ; {d}" if d else "")))

        # R-2 lien symbolique
        root = copy(src, tmp / "r2")
        target = root / "V1/official/GLOSSAIRE.md"
        outside = tmp / "hors_package_GLOSSAIRE.md"
        shutil.copy2(target, outside)
        target.unlink()
        target.symlink_to(outside)
        code, out = build(root)
        packed = {k: "V1/official/GLOSSAIRE.md" in members(root, k) or "official/GLOSSAIRE.md" in members(root, k) for k in ZIPS}
        rows.append(("R-2", "F-BLD-004", "fichier normatif remplacé par un lien → build refusé (motif « lien symbolique »)",
                     code != 0 and "lien symbolique" in out, f"code {code} ; GLOSSAIRE dans les archives : {packed}"))

        # R-3 dossier nommé .build dans les sources
        root = copy(src, tmp / "r3")
        leak = root / "V1/official/.build/non_declare.md"
        leak.parent.mkdir(parents=True)
        leak.write_text("contenu non déclaré", encoding="utf-8")
        code, out = build(root)
        inside = any(any(".build/non_declare.md" in n for n in members(root, k)) for k in ZIPS)
        rows.append(("R-3", "F-VDG-001", "fichier non déclaré sous V1/official/.build/ → build refusé (« fichier inattendu ») et absent des archives",
                     code != 0 and "fichier inattendu" in out and not inside, f"code {code} ; fichier dans une archive : {inside}"))

    for cid, fiche, label, ok, msg in rows:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:4} {fiche:12} {label}  [{msg[:110]}]")
    t = [r for r in rows if r[0].startswith("T")]
    r = [x for x in rows if x[0].startswith("R")]
    print(f"\nConservation : {sum(x[3] for x in t)}/{len(t)} ; release C8 : {sum(x[3] for x in r)}/{len(r)}")
    return 0 if all(x[3] for x in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
