#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R11b parcours : raccords issus de la relecture de parcours (G1, G2, G4, F1 à F3).

Relecture : `V12R_31_RELECTURE_PARCOURS.md`. Décision de l'owner : « Allons-y (a) » — G2 : humain présent, les demandes de
brief partent avant le build, en un seul message ; le build suit la réponse, avec des hypothèses nommées pour ce qui manque.
Rapport : `V12R_32_R11b_PARCOURS.md`. Usage : python3 V12R_Patch_R11b.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, Q, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "QUICKSTART", "CHANGELOG"))
F = HERE / "V12R_Patch_R11b_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("18ef649e874a6fafa4fcbb12fba84b9a647cb69bf48aa913f0d0ccb0f054a6aa", F / "validate_structure.py"),
}
LIGHT = " Trace légère : la proposition (`ACTION/HANDOFF`)."  # phrase courte : LCF-34 garde « Paquet … d’`ACTION/CLOSE-PACKAGE`. »

PATCH = [
    # G1 — valider n'est pas accepter
    ("R11b-G1a", "CHK-01 (noyau) : valider oriente la suite ; l'acceptation se demande", A,
     "la personne valide, réoriente ou arrête. Jusque-là, la proposition reste `EXPLORATORY`.",
     "la personne valide, réoriente ou arrête. Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce "
     "n’est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace "
     "complète, avec ancre observée ou fournie, gates et verdict (absolu 2 de `DIRECTION`). Jusque-là, la proposition reste "
     "`EXPLORATORY`."),
    ("R11b-G1b", "README, entrée humaine : valider ou retenir pour le vrai produit", "README.md",
     "**4. Comment poursuivre ?** Validez, réorientez ou arrêtez.",
     "**4. Comment poursuivre ?** Validez pour continuer, réorientez ou arrêtez. Pour retenir cette direction pour votre vrai "
     "produit, dites-le : l’agent réunit alors les éléments réels et fait les vérifications nécessaires."),
    # G2 (a) — humain présent : demander avant de construire
    ("R11b-G2a", "prise de brief (noyau) : humain présent, demandes avant le build", D,
     "Brief riche : aucune. Humain absent : hypothèses nommées, plafond déclaré, demandes listées à la livraison. Le rendu est "
     "construit dans tous les cas. La personne reçoit directement une proposition principale ; le raisonnement de cadrage reste "
     "dans la trace.",
     "Brief riche : aucune. Humain présent : les demandes partent avant le build, en un seul message ; le build suit la réponse, "
     "avec des hypothèses nommées pour ce qui manque encore. Humain absent : hypothèses nommées, plafond déclaré, demandes listées "
     "à la livraison. Le rendu est construit dans tous les cas. La réponse est une proposition, pas un compte rendu de cadrage ; "
     "le raisonnement de cadrage reste dans la trace."),
    ("R11b-G2b", "README, entrée humaine : les questions viennent d'abord", "README.md",
     "S’il en manque, l’agent vous pose au plus trois questions, en un seul message,",
     "S’il en manque, l’agent vous pose d’abord au plus trois questions, en un seul message, avant de construire,"),
    ("R11b-G2c", "QUICKSTART : prise de brief avant le build si la personne est présente", Q,
     "; le rendu est construit dans tous les cas",
     "; si la personne est présente, ces demandes précèdent le build ; le rendu est construit dans tous les cas"),
    # G4 — sortie en trace légère pour toutes les routes ; reprise ITER depuis une trace légère
    ("R11b-G4a", "RUN-LITE : sortie en trace légère", A,
     "**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`.", "**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`." + LIGHT),
    ("R11b-G4b", "RUN-ITER : sortie en trace légère", A,
     "**Sortie.** Paquet `ITER` d’`ACTION/CLOSE-PACKAGE`.", "**Sortie.** Paquet `ITER` d’`ACTION/CLOSE-PACKAGE`." + LIGHT),
    ("R11b-G4c", "RUN-STANDARD : sortie en trace légère", A,
     "**Sortie.** Paquet `STANDARD` d’`ACTION/CLOSE-PACKAGE`.", "**Sortie.** Paquet `STANDARD` d’`ACTION/CLOSE-PACKAGE`." + LIGHT),
    ("R11b-G4d", "RUN-SYSTEM : sortie en trace légère", A,
     "**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`. Dans une",
     "**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`." + LIGHT + " Dans une"),
    ("R11b-G4e", "ITER se souvient : la trace légère compte", D,
     "retrouvables dans la session, la `RUN_CARD` ou le manifeste local.",
     "retrouvables dans la session, la trace légère (ligne de thèse), la `RUN_CARD` ou le manifeste local."),
    ("R11b-G4f", "RUN-ITER, entrée : la trace légère compte", A,
     "retrouvables dans la `RUN_CARD`, le manifeste ou le projet.",
     "retrouvables dans la trace légère (ligne de thèse), la `RUN_CARD`, le manifeste ou le projet."),
    # F1, F2, F3
    ("R11b-F1", "SAVOIR, BOUCLE-AXE (noyau) : trace de l'alternative graduée", S,
     "Pour chaque alternative, préciser dans la trace existante :",
     "Pour chaque alternative, préciser en trace complète (en trace légère, la première proposition nomme l’alternative écartée) :"),
    ("R11b-F2", "réponse visible (noyau) : l'alternative écartée", A,
     "Pourquoi : la thèse et ce que le rendu permet de décider.",
     "Pourquoi : la thèse, l’alternative écartée et ce que le rendu permet de décider."),
    ("R11b-F3", "CHARGE (noyau) : prise de brief avant le boot", D,
     "`DIRECTION/CREATIVE-BOOT`, `DIRECTION/EXTERNAL-START` si le brief est vague,",
     "`DIRECTION/EXTERNAL-START` si le brief est vague, `DIRECTION/CREATIVE-BOOT`,"),
    ("R11b-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords de parcours (refonte, R11b).** Valider une proposition n’est pas l’accepter : l’acceptation pour un produit réel "
     "se demande et passe en trace complète ; humain présent, les demandes de brief précèdent le build ; chaque route `RUN-*` dit "
     "sa sortie en trace légère, et `ITER` reprend depuis la ligne de thèse d’une trace légère ; la réponse visible nomme "
     "l’alternative écartée ; `EXTERNAL-START` se charge avant le Creative Boot.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R11b-G1a": "valider n'est pas accepter", "R11b-G1b": "valider ou retenir", "R11b-G2a": "humain présent",
    "R11b-G4a": "sortie des routes", "R11b-G4b": "sortie des routes", "R11b-G4c": "sortie des routes",
    "R11b-G4d": "sortie des routes", "R11b-G4e": "vocabulaire retiré", "R11b-G4f": "vocabulaire retiré",
    "R11b-F1": "vocabulaire retiré", "R11b-F2": "alternative écartée", "R11b-F3": "vocabulaire retiré",
}
EXTRA_MUTATIONS: list = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
