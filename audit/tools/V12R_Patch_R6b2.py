#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R6b-2 : cartes réunies (READING_MAP absorbe les combinaisons d'ORCHESTRATION_MAP).

Diagnostic : `V12R_25_R6b_DIAGNOSTIC.md` §4 (R6b-2, non bloquant P2) ; décision de l'owner : « Allons-y » (R6b-2 après R6b-1,
avec sa propre maquette et la vérification des liens et locators). Maquette : 2 causes réelles (LCF-03 et LCF-07 lisent
ORCHESTRATION_MAP), le reste en cascade ; arrêt non appliqué. ORCHESTRATION_MAP reste un fichier (manifeste, liens
externes) devenu pointeur de compatibilité. Rectifications déclarées : LCF-03 et LCF-07 lisent READING_MAP ; CHG-06 aussi.
Rapport : `V12R_28_R6b2_CARTES.md`. Usage : python3 V12R_Patch_R6b2.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, C, RD = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md", "V1/official/README.md"
RM, OM = "V1/official/READING_MAP.md", "V1/official/ORCHESTRATION_MAP.md"
SK, FL = "skills/design-governance-practice/SKILL.md", "skills/design-governance-practice/references/flow.md"
VRM, VS = "scripts/validate_reading_map.py", "scripts/validate_structure.py"
F = HERE / "V12R_Patch_R6b2_fichiers"
FILE_REPLACE = {
    RM: ("c0f03328f2232898df9b7046e06bde5935a03a35df5b81173f82e138658a1f2f", F / RM),
    OM: ("e585dae89873bf42d14523bd1823afab4032f1428b0c95a394f83f978fbb4f6b", F / OM),
}
COMBOS = "section « Combinaisons par résultat recherché »"

MAP_CHECK = '''

# 14. Cartes réunies (R6b-2) : les combinaisons par résultat vivent dans READING_MAP ; ORCHESTRATION_MAP n'est qu'un pointeur.
def check_maps(errors: list[str]) -> None:
    reading = (OFFICIAL / "READING_MAP.md").read_text(encoding="utf-8")
    if reading.count("## Combinaisons par résultat recherché") != 1:
        errors.append("[MAP-01] READING_MAP doit porter une seule section « Combinaisons par résultat recherché »")
    pointer = OFFICIAL / "ORCHESTRATION_MAP.md"
    if pointer.is_file():
        text = pointer.read_text(encoding="utf-8")
        if any(line.startswith("|") or line.startswith("## ") for line in text.splitlines()) or len(text.split()) > 80:
            errors.append("[MAP-01] ORCHESTRATION_MAP porte de nouveau un contenu propre (pointeur de compatibilité attendu)")
'''

PATCH = [
    ("R6b2-R1", "README : combinaisons dans READING_MAP", "README.md",
     "Pour exploiter plusieurs capacités sans les charger mécaniquement, utilisez la "
     "[`ORCHESTRATION_MAP.md`](V1/official/ORCHESTRATION_MAP.md). Cette vue dérivée compose",
     f"Pour exploiter plusieurs capacités sans les charger mécaniquement, utilisez la {COMBOS} de la même carte. "
     "Cette vue dérivée compose"),
    ("R6b2-R2", "README officiel : une carte, un pointeur", RD,
     "Les cartes [`READING_MAP.md`](./READING_MAP.md) et [`ORCHESTRATION_MAP.md`](./ORCHESTRATION_MAP.md) sont dérivées et non "
     "normatives.",
     "La carte [`READING_MAP.md`](./READING_MAP.md) (chemin, combinaisons par résultat et locators) est dérivée et non normative ; "
     "`ORCHESTRATION_MAP.md` n’est plus qu’un pointeur vers elle."),
    ("R6b2-F1", "skill, flux : renvoi à READING_MAP", FL,
     "consulter `ORCHESTRATION_MAP.md` dans la carte officielle du package.",
     f"consulter la {COMBOS} de `READING_MAP.md` dans la carte officielle du package."),
    ("R6b2-S1", "skill, lecture humaine", SK,
     "`README.md`, `QUICKSTART.md`, `READING_MAP.md` et `ORCHESTRATION_MAP.md` orientent les personnes",
     "`README.md`, `QUICKSTART.md` et `READING_MAP.md` orientent les personnes"),
    ("R6b2-D1", "DIRECTION/CHARGE (noyau) : lectures d'orientation", D,
     "README, QUICKSTART, READING_MAP et ORCHESTRATION_MAP sont des lectures d’orientation pour les humains.",
     "README, QUICKSTART et READING_MAP sont des lectures d’orientation pour les humains."),
    ("R6b2-V1", "LCF-07 : pointeur lu dans READING_MAP (rectification déclarée)", VRM,
     'pointers = [row(t["RM"], "Direction identitaire"), row(t["OM"], "Direction forte et spécifique")]',
     'pointers = [row(t["RM"], "Direction identitaire"), row(t["RM"], "Direction forte et spécifique")]'),
    ("R6b2-V2", "LCF-03 : lignes lues dans READING_MAP (rectification déclarée)", VRM,
     'ui, proof, system = row(t["OM"], "UI/UX habitable"), row(t["OM"], "Preuve et décision fiables"), '
     'row(t["OM"], "Système maintenable")',
     'ui, proof, system = row(t["RM"], "UI/UX habitable"), row(t["RM"], "Preuve et décision fiables"), '
     'row(t["RM"], "Système maintenable")'),
    ("R6b2-V3", "libellés LCF-03 et LCF-07", VRM,
     '("LCF-03", "ORCHESTRATION_MAP, noyau UI/UX, preuve, système",',
     '("LCF-03", "READING_MAP (combinaisons), noyau UI/UX, preuve, système",'),
    ("R6b2-V4", "libellé LCF-07", VRM,
     '("LCF-07", "DIRECTION 72, RUN-PRIORITY, READING_MAP, ORCHESTRATION_MAP, skill",',
     '("LCF-07", "DIRECTION 72, RUN-PRIORITY, READING_MAP (routage et combinaisons), skill",'),
    ("R6b2-G1", "CHG-06 : pointeur de chargement lu dans READING_MAP", VS,
     '("ORCHESTRATION_MAP.md", "| **Direction forte et spécifique** |")]',
     '("READING_MAP.md", "| **Direction forte et spécifique** |")]'),
    ("R6b2-G2", "garde MAP-01", VS,
     "\n\n# 12. Locators numériques (R-28)", MAP_CHECK + "\n\n# 12. Locators numériques (R-28)"),
    ("R6b2-G3", "garde MAP-01 appelée", VS,
     "    check_entry(corpus, errors)\n    return errors", "    check_entry(corpus, errors)\n    check_maps(errors)\n    return errors"),
    ("R6b2-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Cartes réunies (refonte, R6b-2).** `READING_MAP` porte désormais les combinaisons par résultat recherché, leurs garde-fous "
     "et leur condition d’arrêt ; `ORCHESTRATION_MAP` devient un pointeur de compatibilité. Aucune règle nouvelle ; "
     "`DIRECTION/CHARGE` reste la seule liste de chargement.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF: dict = {}  # renvois : leurs inverses ne cassent aucune garde (déclaré) ; MAP-01, CHG-06, LCF-03 et LCF-07 sont testées ci-dessous
EXTRA_MUTATIONS = [
    ("contenu réintroduit dans ORCHESTRATION_MAP", OM, "Ce fichier ne porte plus de contenu propre.",
     "Ce fichier ne porte plus de contenu propre.\n\n## Combinaisons\n\n| Résultat | Noyau |\n|---|---|\n| Direction | `DIRECTION/CHARGE` |",
     "[MAP-01]"),
    ("section des combinaisons dédoublée", RM, "## Activation multi-perspective",
     "## Combinaisons par résultat recherché\n\nCopie.\n\n## Activation multi-perspective", "[MAP-01]"),
    ("liste de chargement redéfinie dans les combinaisons (CHG-06)", RM,
     "| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) |",
     "| **Direction forte et spécifique** | `DIRECTION/RUN-DIRECTION`, `ACTION/GATE-A` |", "[CHG-06]"),
]
LCF_MUTATIONS = [
    ("Gate A repasse en renforcement (LCF-03, READING_MAP)", RM,
     "| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + `ACTION/GATE-A` (contrôles applicables) + contenu et états réels |",
     "| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + contenu et états réels |", "LCF-03"),
    ("combinaison DIRECTION sans renvoi à CHARGE (LCF-07, READING_MAP)", RM,
     "| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) |",
     "| **Direction forte et spécifique** | `DIRECTION/CREATIVE-BOOT` |", "LCF-07"),
]


def lcf_mutations(root: Path) -> int:
    bad = 0
    for name, rel, old, new, lcf in LCF_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(copy / VRM)], capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and f"{lcf} :" in out.stdout + out.stderr
            print(f"mutation LCF {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if len(sys.argv) > 1 and "--mutations" in sys.argv:
        root = Path(sys.argv[1]).resolve()
        return 1 if base.mutations(root) + lcf_mutations(root) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
