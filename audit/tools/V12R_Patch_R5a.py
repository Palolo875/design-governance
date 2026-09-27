#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R5a : DIRECTION restructurée (ordre, entrée unique, doublons, D-17, D-19).

Plan : `plans/Plan_V1.2_Refonte.md`, lot R5a ; plan de reprise `plans/Plan_V1.2_Suite_Reprise.md` §4 ; consigne de l'owner :
qualité avant nombre de mots, on ne retire que doublons et texte sans effet. Rapport : `V12R_08_R5a_DIRECTION.md`.
Les sections déplacées sont reprises mot pour mot depuis `V12R_Patch_R5a_textes.py` (extraites de l'état après R5b-2).
Usage : identique à `V12R_Patch_R5b1.py` (<racine> [--verifier | --mutations]).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12R_Patch_R5a_textes import MANDAT, POSTURE, RECAP, ROLE  # noqa: E402

D, C = "V1/official/DIRECTION.md", "V1/official/CHANGELOG.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("8b9bcbdeca97723acb27b35ae29dc7d7bb55fc9328b27f103bb3fab15cc5912c",
                                      HERE / "V12R_Patch_R5a_fichiers" / "scripts" / "validate_structure.py"),
}

ROLE_NEW = (ROLE.replace("<!-- noyau:début ROLE -->\n", "<!-- noyau:début ROLE -->\n<!-- concept:ROL-01 -->\n")
            .replace("le risque dominant et la prochaine preuve.\n",
                     "le risque dominant et la prochaine preuve. Ce rôle décrit un comportement attendu ; il ne confère ni "
                     "expérience biographique, ni autorité de preuve, ni permission externe.\n"))

CARTE_OLD = """| Besoin immédiat | Lire d’abord |
|---|---|
| Classer une demande | `DIRECTION/START` |
| Choisir rapidement une route | `DIRECTION/CHARGE` ou `DIRECTION/FAST-PATH` |
| Préparer une surface identitaire | `DIRECTION/VISUAL_TARGET`, puis `ACTION/RUN-DIRECTION` |
| Produire une direction forte dès le premier rendu | `DIRECTION/FIRST-OBJECT`, puis `SAVOIR/CRAFT` |
| Choisir une structure | `BIBLIOTHEQUE/SELECT` après classification |
| Vérifier, corriger ou clôturer | `ACTION`, jamais DIRECTION seule |"""
CARTE_NEW = ("Classer : `DIRECTION/START`. Charger : `DIRECTION/CHARGE`, seule liste de chargement. Fabriquer : le noyau de la "
             "skill, compilé depuis les blocs « noyau » des sources. Vérifier, corriger ou clôturer : `ACTION`, jamais DIRECTION seule.")

PATCH = [
    # ---------- D-17 : rôle, posture et récapitulatif en tête ----------
    ("R5a-O1", "rôle : retiré de sa place tardive", D, ROLE + "## LES CINQ RÈGLES ABSOLUES", "## LES CINQ RÈGLES ABSOLUES"),
    ("R5a-O2", "posture : retirée de sa place tardive", D, POSTURE + "## 0. Classification", "## 0. Classification"),
    ("R5a-O3", "récapitulatif : retiré de la clôture", D, RECAP + "### Lecture instrumentée", "### Lecture instrumentée"),
    ("R5a-O4", "rôle et posture en tête (ROL-01), mandat fondu dans le rôle", D,
     "## Constitution du document\n", ROLE_NEW + POSTURE + "## Constitution du document\n"),
    ("R5a-O5", "récapitulatif en tête de la constitution", D,
     "### Frontière de responsabilité\n", RECAP + "### Frontière de responsabilité\n"),
    ("R5a-M1", "mandat : doublon du rôle retiré", D, MANDAT + "**Capacité positive de DIRECTION.**", "**Capacité positive de DIRECTION.**"),
    # ---------- Entrée unique ----------
    ("R5a-E1", "carte de lecture : renvois au lieu d'une table concurrente", D, CARTE_OLD, CARTE_NEW),
    ("R5a-E2", "architecture : chaîne de lecture en double", D,
     "`CREATIVE-BOOT` ouvre la décision ; `VISUAL_TARGET` la spécifie ; `DIRECTION-ATELIER` l’approfondit seulement si nécessaire ; "
     "`FIRST-OBJECT` la matérialise ; `DOUBLE-LOOP` l’apprend ; `ACTION` la vérifie et la ferme. Une seule vue",
     "Une seule vue"),
    ("R5a-E3", "renvoi de lecture corrigé", D,
     "La chaîne de lecture est définie dans `Architecture d’activation` ci-dessus.",
     "La chaîne de lecture est définie une seule fois : « Chaîne de lecture interne », dans la constitution du document."),
    ("R5a-E4", "règle de passage : doublon de DIRECTION/CHARGE", D,
     "Le passage entre propriétaires reste : `DIRECTION` décide du mode et du risque dominant ; `ACTION` des preuves exécutables, "
     "gates, statuts et verdicts ; `SAVOIR` du jugement ; `BIBLIOTHEQUE` de la structure ; `CHANGELOG` de la gouvernance du système.",
     "Le passage entre propriétaires reste celui de la règle de passage de `DIRECTION/CHARGE`."),
    # ---------- D-19 ----------
    ("R5a-B1", "D-19 : phrase hors contexte dans le bloc noyau BRIEF", D,
     "La personne reçoit directement une proposition principale ; cette vue reste interne.",
     "La personne reçoit directement une proposition principale ; le raisonnement de cadrage reste dans la trace."),
    # ---------- Historique ----------
    ("R5a-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **DIRECTION restructurée (refonte, R5a).** Rôle, posture et récapitulatif de protection en tête ; rôle défini une seule "
     "fois ; entrée unique (classer : `START`, charger : `CHARGE`, fabriquer : le noyau) ; doublons de lecture et de passage "
     "retirés ; phrase hors contexte du bloc de prise de brief corrigée. Aucun locator renommé.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R5a-O4": "ROL-01 absent",
    "R5a-M1": "vocabulaire retiré",
    "R5a-E2": "vocabulaire retiré",
    "R5a-B1": "vocabulaire retiré",
}

EXTRA_MUTATIONS = [
    ("récapitulatif renvoyé en fin de fichier", D, "### Récapitulatif de protection\n",
     "### Récapitulatif (ancien)\n", "[ORD-01]"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
