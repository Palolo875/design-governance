#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R6a : façades (partie sûre).

README : la séquence de boucle devient un renvoi (dernière exemption de la garde « boucle unique » levée).
GLOSSAIRE : termes introduits par R5b et R5b-2 (trace légère, trace complète, première proposition, trame modale,
profil de surface), gardés par la liste GLOSSARY_TERMS. La fusion des deux README, le QUICKSTART humain et la réduction
de READING_MAP restent au plan de reprise (R6b). Rapport : `V12R_12_R6a_FACADES.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

RM, G, C = "README.md", "V1/official/GLOSSAIRE.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("e1ee40cea58e5031cb84701f715d1437c1a236440e3373d8f49e1c5f58226097",
                                      HERE / "V12R_Patch_R6a_fichiers" / "scripts" / "validate_structure.py"),
}

GLOSS = (
    "| **Trace légère** | La trace par défaut d’un run ni persistant, ni partagé, ni audité : six lignes au plus (mode, thèse, "
    "modal, trame et parti, plafond, défaut dominant, prochaine preuve). Le run livre une proposition, sans verdict ni clôture. |\n"
    "| **Trace complète** | La trace d’un run persistant, partagé, audité ou dont on demande l’acceptation : handoff, `RUN_CARD`, "
    "paquet de clôture et gates écrits. |\n"
    "| **Première proposition** | Le premier rendu, présenté avec sa thèse et ce qu’il faut décider. Il vaut checkpoint, sauf "
    "action irréversible ou coûteuse. |\n"
    "| **Trame modale** | L’ordre de sections que n’importe quelle IA produirait pour un brief. Le test de trame la nomme, puis la "
    "rompt ou la justifie par la tâche. |\n"
    "| **Profil de surface** | Le type de surface (vitrine, application, scène, hors Web) qui fixe les contrôles d’accessibilité "
    "à faire d’office. |\n")

PATCH = [
    ("R6a-R1", "README : boucle en renvoi", RM,
     "> **Observer → isoler le défaut dominant → modifier l’artefact → observer à nouveau → comparer → décider.**",
     "> **La boucle d’édition** (`DIRECTION/DOUBLE-LOOP`, reprise dans le noyau de la skill) : observer, nommer le défaut "
     "dominant, modifier l’artefact, comparer, décider."),
    ("R6a-G1", "GLOSSAIRE : termes de la refonte", G,
     "| **Vérité de scène** |", GLOSS + "| **Vérité de scène** |"),
    ("R6a-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Façades (refonte, R6a).** README : la boucle renvoie à `DIRECTION/DOUBLE-LOOP` ; glossaire : trace légère, trace "
     "complète, première proposition, trame modale, profil de surface.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {"R6a-R1": "vocabulaire retiré", "R6a-G1": "glossaire : terme absent"}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
