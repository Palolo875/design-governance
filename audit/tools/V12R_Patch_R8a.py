#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R8a : convergence typographique (D-21).

P1 (`V12R_05`) : 3 rendus V1.2 sur 3 sortent de la palette crème mais convergent sur Archivo et un fond blanc neutre.
La question de convergence du noyau ne portait que sur la palette ; elle porte désormais aussi sur la police de titre,
avec un geste positif (comparer deux voix typographiques) et la même règle : nommer, justifier ou reconsidérer,
jamais interdire. La veille note le signal observé, déclaré comme faible (N = 3, même auteur).
Rapport : `V12R_09_R8a_CONVERGENCE_TYPO.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

S, C = "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("660db18ee3178086d2950bd5949ec7d12d3ba2f41573d5fae67a4bc0b135e384",
                                      HERE / "V12R_Patch_R8a_fichiers" / "scripts" / "validate_structure.py"),
}

PATCH = [
    ("R8a-Q1", "question de convergence : palette et police de titre", S,
     "**Question de convergence.** Cette palette est-elle celle que le modèle produirait sans brief (neutres et un seul accent, "
     "sombre et doré, dégradé froid) ? Si oui, nomme ce qui, dans le produit, la justifie. Sinon, reconsidère-la. La question ne "
     "prescrit aucun écart : une palette convergente justifiée reste valide.",
     "**Question de convergence.** Cette palette et cette police de titre sont-elles celles que le modèle produirait sans brief "
     "(palette : neutres et un seul accent, sombre et doré, dégradé froid ; police : la grotesque large ou la serif de caractère "
     "prise par réflexe) ? Si oui, nomme ce qui, dans le produit, les justifie. Sinon, reconsidère-les. Pour la police de titre, "
     "compare au moins deux voix typographiques distinctes (par exemple grotesque, serif, mécane, manuscrite ou vernaculaire du "
     "lieu) sur le vrai titre avant de choisir. La question ne prescrit aucun écart : un choix convergent justifié reste valide."),
    ("R8a-V1", "veille : signal de convergence observé en P1", S,
     "À revoir avant 2027-03.\n<!-- noyau:fin COMP-VAGUES -->",
     "Signal à confirmer (P1, 27-09-2026, 3 rendus sur 3, même auteur) : grotesque large ou condensée (Archivo) sur fond blanc "
     "neutre avec un seul accent vif. À revoir avant 2027-03.\n<!-- noyau:fin COMP-VAGUES -->"),
    ("R8a-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Convergence typographique (refonte, R8a).** La question de convergence du noyau porte sur la palette et sur la police "
     "de titre (comparer au moins deux voix typographiques sur le vrai titre) ; la veille note un signal à confirmer (grotesque "
     "large sur blanc neutre, P1).\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {"R8a-Q1": "résumé infidèle (question de convergence)"}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
