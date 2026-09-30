#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R7 : ancre graduée (décision 6), D-03 et D-04.

Diagnostic : `V12R_20_R7_DIAGNOSTIC.md` ; ajustements de l'owner intégrés avant application (30-09-2026) :
FAIL-ASSUMED n'est jamais une voie d'acceptation (diffusion limitée, verdict non accepté) ; « absence déclarée » vaut pour
explorer, pas pour accepter (le validateur refuse toute DIRECTION acceptée sans ancre) ; le déclencheur critique est clarifié,
pas durci ; un renvoi à la règle canonique suffit (pas de répétition imposée). Schéma et validateur inchangés (décision 3).
Rapport : `V12R_21_R7_ANCRE.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, S, C = "V1/official/DIRECTION.md", "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"
Q, RM, RD = "V1/official/QUICKSTART.md", "V1/official/READING_MAP.md", "V1/official/README.md"
F = HERE / "V12R_Patch_R7_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("589d7d0690bc7dbcd12f589762a76229d4a52468f01ab13c1a75620fbc3f59fc", F / "validate_structure.py"),
    "scripts/build_core.py": ("9909a5bf3cda5ba252a6e3979647a5ebd001b825f428e0c1c180fabd85bda0f2", F / "build_core.py"),
}

TITRE_OLD = "### [ABSOLU 2 — ANCRAGE OBSERVABLE] Ne dessine jamais une surface identitaire uniquement de mémoire."
INTRO_OLD = "Avant le premier code ou le premier rendu d’une surface `DIRECTION`, établis une ancre fraîche et inspectable par l’une des voies suivantes :"
TITRE_NEW = "### [ABSOLU 2 — ANCRAGE OBSERVABLE] Ne fais jamais accepter une direction identitaire calibrée uniquement de mémoire."
INTRO_NEW = """<!-- noyau:début ANCRE -->
<!-- concept:ANC-01 -->
**Explorer, accepter, diffuser.** Une première proposition peut commencer sans ancre, quelle que soit sa destination : elle déclare cette limite et reste `EXPLORATORY` ; une hypothèse générée (`ANCHOR-GENERATED`) aide alors à comparer. **Accepter** une direction identitaire exige une ancre : une direction acceptée n’a jamais d’ancres vides. Pour un produit réel, l’ancre est observée ou fournie (`ANCHOR-OBSERVED`, `ANCHOR-PROVIDED`), pertinente et inspectée, avec les autres preuves applicables ; elle peut venir du projet lui-même (identité existante, produit, photographies, interface actuelle). Pour une démonstration ou un modèle, une hypothèse générée peut servir d’ancre à l’acceptation, avec sa limite déclarée. Une **diffusion limitée** sans l’ancre requise passe par `FAIL-ASSUMED` (`ACTION/OVERRIDE`) : le verdict reste non accepté.
<!-- noyau:fin ANCRE -->

Les voies d’ancrage sont les suivantes ; une ancre est datée et inspectable :"""
FIN_OLD = ("Sans ancre fraîche et utile, les axes visuels concernés sont `NOT-VERIFIED`. Sur une surface identitaire, cela bloque la "
           "livraison validée, sauf `FAIL-ASSUMED` journalisé selon `ACTION`.")
FIN_NEW = ("Sans ancre utile, les axes visuels concernés restent `NOT-VERIFIED` et la direction ne peut pas être acceptée ; une diffusion "
           "limitée reste possible par `FAIL-ASSUMED`, avec un verdict non accepté (`ACTION/OVERRIDE`). Le validateur de `RUN_CARD` "
           "refuse une direction acceptée sans ancre, mais ne connaît pas la destination : l’exigence d’une ancre observée ou fournie "
           "pour un produit réel relève de la revue d’acceptation.")
FACADE_NEW = "ancre observée ou fournie avant d’accepter une direction pour un produit réel"

PATCH = [
    ("R7-A1", "absolu 2 : titre", D, TITRE_OLD, TITRE_NEW),
    ("R7-A2", "absolu 2 : règle graduée (ANC-01, noyau §6)", D, INTRO_OLD, INTRO_NEW),
    ("R7-A3", "absolu 2 : sans ancre, pas d'acceptation ; FAIL-ASSUMED non accepté ; limite du validateur", D, FIN_OLD, FIN_NEW),
    ("R7-A4", "déclencheur critique clarifié", D,
     "| Ancre absente pour une surface identitaire | Retour à l’ancrage ou statut prévu par ACTION. | `[FORCÉ]` |",
     "| Ancre absente pour une surface identitaire | En exploration : limite déclarée, run `EXPLORATORY`. Avant l’acceptation : "
     "retour à l’ancrage, ou statut prévu par ACTION (absolu 2). | `[FORCÉ]` |"),
    ("R7-A5", "récapitulatif de protection", D,
     "son ancrage doit être observable ou explicitement limité",
     "son ancrage est déclaré comme limite en exploration et observable avant l’acceptation (absolu 2)"),
    ("R7-S1", "SAVOIR/SOURCE : renvoi à l'absolu 2", S,
     "Pour une surface identitaire, l’ancre est requise (voir `DIRECTION`, ABSOLU 2) ;",
     "Pour une surface identitaire, l’ancre suit l’absolu 2 de `DIRECTION` : exploration possible sans ancre, limite déclarée ; "
     "acceptation avec une ancre, observée ou fournie pour un produit réel ;"),
    ("R7-S2", "SAVOIR, test de sortie", S,
     "l’ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée).",
     "l’ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée en exploration ; avant l’acceptation, absolu 2 de `DIRECTION`)."),
    ("R7-F1", "QUICKSTART (D-03)", Q, "ancre fraîche et inspectable", FACADE_NEW),
    ("R7-F2", "READING_MAP (D-03)", RM, "direction perceptible, ancre inspectable,", "direction perceptible, " + FACADE_NEW + ","),
    ("R7-F3", "README officiel (D-03)", RD, "direction perceptible, ancre inspectable,", "direction perceptible, " + FACADE_NEW + ","),
    # Ajoutée après le premier suivi (README Local généré par le build : piège signalé par l'amendement du 28-09, §8).
    ("R7-F4", "README Local généré par build_distributions.sh (D-03)", "scripts/build_distributions.sh",
     "direction perceptible, ancre inspectable,", "direction perceptible, " + FACADE_NEW + ","),
    ("R7-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Ancre graduée (refonte, R7).** Absolu 2 : explorer sans ancre avec une limite déclarée ; accepter avec une ancre, observée "
     "ou fournie pour un produit réel, qui peut venir du projet ; `FAIL-ASSUMED` ne permet qu’une diffusion limitée non acceptée ; "
     "SAVOIR, déclencheur critique et façades alignés par renvoi. Schéma et validateur inchangés.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R7-A1": "vocabulaire retiré",
    "R7-A2": "ANC-01 absent",
    "R7-A3": "vocabulaire retiré",
    "R7-F1": "vocabulaire retiré",
    "R7-F2": "vocabulaire retiré",
    "R7-F3": "vocabulaire retiré",
}
# R7-F4 : sa garde agit dans la distribution construite (validate_all) ; prouvée par le suivi (validate_all rouge sans elle).
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
