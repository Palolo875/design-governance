#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R8b-2 : raccords de R8b après vérification de l'owner (30-09-2026).

1. Garde PKG-01 : l'ancien vocabulaire retiré rejetait aussi un choix justifié (« applique un traitement unique si la
   comparaison confirme… »). Il est remplacé par une garde au niveau de la phrase (UNI-01) : l'obligation universelle est
   refusée, le choix conditionné ou justifié est accepté. Les deux situations sont vérifiées (--mutations).
2. Carte des moyens : Fontshare, licence FFL (ITF Free Font License) ou OFL selon la police.
Rapport : `V12R_16_R8b2_RACCORDS.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

S, C = "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("d84ee20440fcef97c3c7fbb3f060b8879bd97d61056aa071d0ee8638a9fff725",
                                      HERE / "V12R_Patch_R8b2_fichiers" / "scripts" / "validate_structure.py"),
}
PATCH = [
    ("R8b2-F1", "Fontshare : FFL ou OFL selon la police", S,
     "Fontshare (licence propre au service, gratuite sous conditions)", "Fontshare (licence FFL ou OFL selon la police)"),
    ("R8b2-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords (refonte, R8b-2).** Choix contextuels gardés au niveau de la phrase : l’obligation universelle d’un traitement "
     "ou d’une famille unique est refusée, le choix justifié accepté ; Fontshare : licence FFL ou OFL selon la police.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF: dict = {}
ANCHOR = "\n## "
# Rouges attendues : retour de l'obligation universelle.
EXTRA_MUTATIONS = [
    ("obligation universelle (assets)", S, ANCHOR,
     "\nApplique un traitement unique et cohérent à tous les assets moyens.\n" + ANCHOR, "[UNI-01]"),
    ("obligation universelle (icônes)", S, ANCHOR, "\nIcônes : une seule famille.\n" + ANCHOR, "[UNI-01]"),
    # Remplace l'inverse de R8b-K1, devenu inapplicable (texte de la carte modifié par R8b2-F1).
    ("carte sans vérification par ressource", S, "vérifiées pour chaque ressource retenue", "vérifiées", "résumé infidèle (carte des moyens)"),
]
# Vertes attendues : choix justifié ou conditionné.
ACCEPTS = [
    ("choix conditionné (assets)", S, ANCHOR,
     "\nApplique un traitement unique si la comparaison confirme qu’il unifie la série.\n" + ANCHOR),
    ("choix justifié (icônes)", S, ANCHOR,
     "\nUne seule famille d’icônes suffit lorsqu’elle couvre les pictogrammes nécessaires ; ce choix dépend du projet.\n" + ANCHOR),
]


def accepts(root: Path) -> int:
    bad = 0
    for name, rel, old, new in ACCEPTS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = old in t
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            code, out = base.structure(copy)
            green = ok and code == 0
            print(f"acceptation {name} : {'VERT' if green else 'NON VERT'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if green else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if "--mutations" in sys.argv:
        root = Path(sys.argv[1]).resolve()
        return 1 if (base.mutations(root) + accepts(root)) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
