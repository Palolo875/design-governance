#!/usr/bin/env python3
"""R12 — compile le contenu complet d'une distribution GitHub en un seul fichier Markdown (comme releases/V1.1.1).

Usage : python3 V12R_Compile_release.py <archive_GITHUB.zip> <version> <sortie.md> [<note d'état>]
Chaque fichier garde son chemin et son contenu intégral, dans un bloc délimité par des tildes plus longs que toute
suite de tildes du contenu ; un sommaire donne lignes et SHA-256 par fichier.
"""
from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path

LANG = {".py": "python", ".sh": "bash", ".json": "json", ".yml": "yaml", ".yaml": "yaml", ".md": "markdown"}


def main() -> int:
    archive, version, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    state = sys.argv[4] if len(sys.argv) > 4 else ""
    with zipfile.ZipFile(archive) as z:
        members = sorted(i.filename for i in z.infolist() if not i.is_dir())
        files = {m: z.read(m) for m in members}
    lines = [f"# Design Governance V{version} — Contenu complet du système", "",
             f"> Document généré à partir de la distribution GitHub `{archive.name}` "
             f"(SHA-256 `{hashlib.sha256(archive.read_bytes()).hexdigest()}`).",
             "> Chaque section conserve le chemin original du fichier et son contenu intégral, sans modification. "
             "Les empreintes SHA-256 permettent de vérifier chaque fichier."]
    if state:
        lines.append(f"> **État :** {state}")
    lines += ["", "## Sommaire des fichiers", "", "| Fichier | Lignes | SHA-256 |", "|---|---|---|"]
    for m in members:
        data = files[m]
        lines.append(f"| `{m}` | {data.decode('utf-8').count(chr(10))} | `{hashlib.sha256(data).hexdigest()}` |")
    lines += ["", "---", ""]
    for m in members:
        text = files[m].decode("utf-8")
        fence = "~" * max(4, max((len(r) for r in re.findall(r"~+", text)), default=0) + 1)
        lines += [f"## Fichier : `{m}`", "", f"{fence}{LANG.get(Path(m).suffix, '')}", text.rstrip("\n"), fence, ""]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{out} : {len(members)} fichiers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
