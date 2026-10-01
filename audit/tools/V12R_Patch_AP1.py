#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION AP1 (audit progressif externe, unité 1) : format de la skill (C01), fichiers locaux nus en
profil strict (C02), restauration cohérente des distributions (C03).

Audit : `DG_Audit_progressif_10` (commit 1a4bf2f), constats C01 à C03, vérifiés sur le dépôt. Décision de l'owner
(01-10-2026) : plan en cinq unités retenu avec quatre ajustements (reconnaissance bornée pour C02 ; récupération
complète pour C03 ; limites des critères visibles ; formulations C08 et coût bornées). Rapport : `V12R_40_AP1_OUTILLAGE.md`.
Aucune règle de fabrication ne change : la description de la skill garde son texte décodé ; ACTION (profil strict,
« locators locaux résolus depuis le dossier de la carte ») est inchangé, le code s'y conforme.
Usage : python3 V12R_Patch_AP1.py <racine> [--verifier | --mutations]
Preuves directes (hors suivi) : python3 V12R_Sonde_AP1.py <racine>
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12R_Sonde_AP1 import DESCRIPTION  # noqa: E402

SK, C = "skills/design-governance-practice/SKILL.md", "V1/official/CHANGELOG.md"
VRC = "scripts/validate_run_card.py"
F = HERE / "V12R_Patch_AP1_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("e380f551d53299a5a4cd66f94c5abd3f96cdf25fbe1977ef9861cf7bb9941066", F / "validate_structure.py"),
    "scripts/validate_run_card.py": ("784d5c69105ec00d2a8dcd8a819f88c6cfc229244862a04d65c76b2149771800", F / "validate_run_card.py"),
    "scripts/build_distributions.sh": ("4e2c82056c3a0f803fd733d060ab0a541678d324f8fdcdd096dd75da274a5232", F / "build_distributions.sh"),
}
PATCH = [
    ("AP1-C01", "SKILL, en-tête : description citée (YAML valide, texte décodé inchangé)", SK,
     f"\ndescription: {DESCRIPTION}\n", f"\ndescription: {json.dumps(DESCRIPTION, ensure_ascii=False)}\n"),
    ("AP1-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Outillage (audit progressif, unité 1).** L’en-tête de la skill est cité et se lit en YAML, texte inchangé "
     "(garde SKL-01) ; le profil strict traite un nom de fichier nu à extension connue comme un fichier local, résolu "
     "depuis le dossier de la carte (tickets, commits et identifiants opaques inchangés) ; le build restaure ensemble "
     "`dist` et les deux archives si la promotion échoue.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {"AP1-C01": "[SKL-01]"}
EXTRA_MUTATIONS = [
    ("deux-points non cité dans name", SK,
     "name: design-governance-practice", "name: design-governance: practice", "[SKL-01]"),
    ("champ name retiré", SK, "name: design-governance-practice\n", "", "[SKL-01]"),
]
# Mutations du validateur RUN_CARD : (nom, ancien, nouveau, motif attendu dans la sortie de la suite).
CODE_MUTATIONS = [
    ("C02 : nom nu jamais local (comportement antérieur)",
     "return bool(bare and bare.group(1).lower() in LOCAL_FILE_EXTENSIONS)", "return False", "cas unitaire C02-1 "),
    ("C02 : tout nom à point devient local (sur-reconnaissance)",
     "return bool(bare and bare.group(1).lower() in LOCAL_FILE_EXTENSIONS)", "return bool(bare)",
     "locator strict admis refusé (version"),
]


def code_mutations(root: Path) -> int:
    bad = 0
    for name, old, new, motif in CODE_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / VRC
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(p)], capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and motif in out.stdout + out.stderr
            print(f"mutation de code {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()
        return 1 if base.mutations(root) + code_mutations(root) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
