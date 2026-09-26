#!/usr/bin/env python3
"""V1.2 — G3 : application de la PATCH-DECISION A, B, D sur B05, et entrée CHANGELOG « Non publié ».

Usage : python3 V12_G3_Application.py <racine_package>
1. applique V12_Patch_ABD.PATCH (29 entrées ; arrêt si un ancien texte manque) ;
2. insère l'entrée CHANGELOG exacte ci-dessous avant la section V1.1.1.
La version affichée reste V1.1.1 : le passage à V1.2.0 se fait à la publication, après G4.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import V12_Patch_ABD as P  # noqa: E402

C = "V1/official/CHANGELOG.md"
ANCHOR = "## V1.1.1 — Retour d’audit : alignements de textes et de façades\n"
ENTRY = (
    "## Non publié — candidate V1.2 (B05), chantiers A, B et D\n\n"
    "- **Bilan de fabrication.** `FABRICATION` remplace `ANCHOR-BASIS` et `ANCHOR-LIMIT` dans le Creative Boot ; `CONSTRAINT` "
    "inclut la destination ; en produit réel, jamais de faux asset ; capacités absentes : plafond déclaré, rendu livré. Trace seule, "
    "schéma `RUN_CARD` inchangé.\n"
    "- **Prise de brief minimale.** `DIRECTION/EXTERNAL-START` : au plus trois demandes, dans l’ordre contenu réel, marque, asset "
    "principal, destination ; construire dans tous les cas.\n"
    "- **Anti-slop vivant.** `MODAL` / `PARTI` remplacent `ANTI-DIRECTIONS` (projetés dans `direction.anti_direction`) ; marqueurs "
    "de vague datés dans `SAVOIR` (`[VEILLE 2026-09]`), pour nommer, jamais pour interdire.\n"
    "- **Validateur de carte.** La liste close des conditions de façade passe de 42 à 46 conditions (LCF-43 à LCF-46).\n"
    "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence donne V1.1.1 ≈ sans système sur la qualité perçue ; l’effet de ces "
    "chantiers reste à éprouver (G4).\n\n"
)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    problems = P.apply(root, P.PATCH)
    if problems:
        for p in problems:
            print("ÉCHEC", p)
        return 1
    path = root / C
    text = path.read_text(encoding="utf-8")
    if text.count(ANCHOR) != 1 or ENTRY in text:
        print("ÉCHEC CHANGELOG : ancre absente ou entrée déjà présente")
        return 1
    path.write_text(text.replace(ANCHOR, ENTRY + ANCHOR), encoding="utf-8")
    print(f"appliqué : {len(P.PATCH)} entrées + CHANGELOG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
