#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION R12 : publication de V1.2.0 (version, CHANGELOG daté, notes de version, fiche de version).

Décision de l'owner (01-10-2026) : option (a), publier V1.2.0 comme expérimentation avec l'efficacité `NOT-VERIFIED`
déclarée ; G4 (juges extérieurs) après la publication. Le schéma `RUN_CARD` est inchangé (décision 3).
Garde existante : `validate_design_governance.py` (version du manifeste = CHANGELOG ; titres des entrées).
Garde ajoutée : FAC-01, notes de version (efficacité non vérifiée, G4, frontière du validateur).
Rapport : `V12R_48_R12_PUBLICATION.md`. Usage : python3 V12R_Patch_R12.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12_Patch_ABD import apply  # noqa: E402

O = "V1/official/"
F = HERE / "V12R_Patch_R12_fichiers"
FILE_REPLACE = {
    "RELEASE_NOTES.md": ("05cdc6150ba538c523079602d19bd5d813b3c5688a165579a9e4562fb3943852", F / "RELEASE_NOTES.md"),
    "scripts/validate_structure.py": ("4402d556d19da11893b03fc95a7a83c11b3fb979d8f8daf9048a142fad17db31", F / "validate_structure.py"),
}
PATCH = [
    ("R12-M", "manifeste : version 1.2.0", "scripts/package_manifest.json", '"version": "1.1.1",', '"version": "1.2.0",'),
    ("R12-C1", "CHANGELOG : titre", O + "CHANGELOG.md", "# Changelog — Design Governance V1.1.1", "# Changelog — Design Governance V1.2.0"),
    ("R12-C2", "CHANGELOG : version publique, statut et date", O + "CHANGELOG.md",
     "**Version publique :** `V1.1.1`  \n**Statut expérimental :** Design Governance V1.1.1 est une expérimentation maintenue.  \n"
     "**Date de la version :** 2026-09-26",
     "**Version publique :** `V1.2.0`  \n**Statut expérimental :** Design Governance V1.2.0 est une expérimentation maintenue.  \n"
     "**Date de la version :** 2026-10-01 (V1.1.1 : 2026-09-26)"),
    ("R12-C3", "CHANGELOG : section de version datée", O + "CHANGELOG.md",
     "## Non publié — candidate V1.2 (B05), chantiers A, B et D",
     "## V1.2.0 — Refonte : noyau de fabrication, trace graduée et consolidation (2026-10-01)"),
    ("R12-C4", "CHANGELOG : efficacité", O + "CHANGELOG.md",
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence donne V1.1.1 ≈ sans système sur la qualité perçue ; l’effet "
     "de ces chantiers reste à éprouver (G4).",
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence donne V1.1.1 ≈ sans système sur la qualité perçue ; le palier "
     "exploratoire de R10 (six productions, auto-comparaison, juges modèles d’une seule famille) oriente sans prouver ; "
     "l’effet de V1.2.0 reste à éprouver par une épreuve à juges extérieurs (G4)."),
    ("R12-R1", "README : titre", "README.md", "# Design Governance V1.1.1\n", "# Design Governance V1.2.0\n"),
    ("R12-R2", "README : statut", "README.md", "> **Statut expérimental :** Design Governance V1.1.1 est",
     "> **Statut expérimental :** Design Governance V1.2.0 est"),
    ("R12-R3", "README : fiche de version", "README.md",
     "| Build et distributions | Validés et reproductibles |\n| Architecture de lecture | Durcie ; carte dérivée disponible |",
     "| Build et distributions | Validés et reproductibles ; validation complète observée en CI hébergée (Linux, Python 3.10 "
     "à 3.13) |\n| Architecture de lecture | Noyau de fabrication compilé ; liste de chargement unique ; carte dérivée disponible |"),
    ("R12-O1", "README officiel : titre et présentation", O + "README.md",
     "# Design Governance V1.1.1\n\nCe dossier contient les sources officielles de **Design Governance V1.1.1**",
     "# Design Governance V1.2.0\n\nCe dossier contient les sources officielles de **Design Governance V1.2.0**"),
    ("R12-Q1", "QUICKSTART : titre et présentation", O + "QUICKSTART.md",
     "# Design Governance V1.1.1 — Quickstart (guide opérateur)\n\n**Package Design Governance V1.1.1.**",
     "# Design Governance V1.2.0 — Quickstart (guide opérateur)\n\n**Package Design Governance V1.2.0.**"),
    ("R12-B1", "README Local (build) : titre et présentation", "scripts/build_distributions.sh",
     "# Design Governance V1.1.1 — export Local\n\nDesign Governance V1.1.1 est",
     "# Design Governance V1.2.0 — export Local\n\nDesign Governance V1.2.0 est"),
]
EXTRA = [  # (nom, fichier, ancien, nouveau, motif) : la version doit rester cohérente partout
    ("CHANGELOG revenu à V1.1.1", O + "CHANGELOG.md", "**Version publique :** `V1.2.0`", "**Version publique :** `V1.1.1`",
     "version du manifeste divergente"),
    ("titre du QUICKSTART resté en V1.1.1", O + "QUICKSTART.md", "# Design Governance V1.2.0 — Quickstart",
     "# Design Governance V1.1.1 — Quickstart", "version du titre divergente"),
    ("notes de version sans efficacité déclarée", "RELEASE_NOTES.md", "**Efficacité : `NOT-VERIFIED`.**",
     "**Efficacité.**", "[FAC-01]"),
]


def mutations(root: Path) -> int:
    import subprocess
    bad = 0
    for name, rel, old, new, motif in EXTRA:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            path = copy / rel
            text = path.read_text(encoding="utf-8")
            ok = text.count(old) == 1
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
            outs = [subprocess.run([sys.executable, "-B", f"scripts/{s}"], capture_output=True, text=True, cwd=copy)
                    for s in ("validate_design_governance.py", "validate_structure.py")]
            red = ok and any(o.returncode != 0 and motif in o.stdout + o.stderr for o in outs)
            print(f"mutation {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, {}, []
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        return 1 if mutations(Path(sys.argv[1]).resolve()) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
