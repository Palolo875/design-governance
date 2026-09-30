#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R8c : gestes de résolution précisés.

Diagnostic : `V12R_17_R8c_DIAGNOSTIC.md` ; textes validés par l'owner (« Allons-y », 30-09-2026).
Quatre manques établis ou partiels : équilibre d'un titre (avec l'écart d'échelle), texte sur image, relecture de
l'ensemble après une correction locale, récupération après erreur. Deux candidats couverts (poids optique des icônes ;
contraste d'échelle comme geste séparé) : aucun ajout. Rapport : `V12R_18_R8c_GESTES.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, C = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_R8c_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("84e21995b6fa7cfad00c82612b2904c3c9c7b962e28e6153101115a1fcdfe921", F / "validate_structure.py"),
    "scripts/build_core.py": ("e9781112f55a9f0bdd16f6e744704d67baa751beab61206b50668a6312cd5f82", F / "build_core.py"),
}

SIG = "Une signature typographique ne tient pas si zoom, reflow, locale ou ajustement d’espacement la transforment en défaut de lecture."
TITRE = SIG + """

<!-- noyau:début COMP-TITRE -->
<!-- concept:TIT-01 -->
**Équilibre d’un titre.** Quand un titre porte la scène (grand titre, accroche, chiffre mis en avant), règle-le sur le vrai texte : coupe les lignes selon le sens, sans mot isolé en dernière ligne ; équilibre la longueur des lignes (`text-wrap: balance` si la cible le permet) ; resserre l’approche aux grandes tailles si la police le demande ; garde un écart d’échelle net entre le titre et le texte qui suit, car un écart faible aplatit la hiérarchie. Observe sur capture, en desktop et en mobile, avec le contenu réel : la forme du bloc de titre reste lisible au flou.
<!-- noyau:fin COMP-TITRE -->"""

VUE = "lorsque plusieurs décisions doivent rester simultanément visibles."
TEXTE_IMAGE = VUE + """

<!-- noyau:début COMP-TEXTE-IMAGE -->
<!-- concept:TXI-01 -->
**Texte sur image.** Quand un texte est posé sur une photo, une illustration ou une texture, place-le dans la zone calme de l’image ou recadre pour en créer une ; sinon, ajoute un voile ou un dégradé localisé, ou sors le texte de l’image. Mesure le contraste aux points les plus défavorables, à chaque largeur où le recadrage change. Une image sans zone calme demande un autre recadrage ou un autre placement.
<!-- noyau:fin COMP-TEXTE-IMAGE -->"""

ETATS = "une tâche utilisateur peut être requise lorsque la récupération ou la compréhension est le risque dominant."
RECUP = ETATS + """

<!-- concept:RCV-01 -->
**Récupération après erreur.** Un message d’erreur dit ce qui s’est passé, pourquoi si c’est utile, et comment reprendre ; il apparaît près de l’élément concerné, dans la langue du produit. La saisie de la personne est conservée, le focus va à l’erreur ou au résumé des erreurs, et une action de reprise est proposée : corriger, réessayer ou revenir. Une capture montre le message ; seule une interaction montre la reprise : parcours l’erreur, puis la correction, jusqu’au succès."""

PATCH = [
    ("R8c-T1", "équilibre d'un titre (TYPE, noyau §5)", S, SIG, TITRE),
    ("R8c-I1", "texte sur image (CFT-03, noyau §5)", S, VUE, TEXTE_IMAGE),
    ("R8c-B1", "question 5 : l'ensemble réobservé", D,
     "5. si la correction a affaibli l’usage, l’accessibilité, la robustesse ou la direction ;",
     "5. si la correction a affaibli l’usage, l’accessibilité, la robustesse, la direction, ou la hiérarchie et l’harmonie de "
     "l’ensemble : réobserve la page entière, pas seulement la zone corrigée ;"),
    ("R8c-R1", "récupération après erreur (STATE)", S, ETATS, RECUP),
    ("R8c-R2", "Gate C C6 : renvoi à la récupération", A,
     "résous-la par microcopie, état, donnée ou interaction (forme située, §5). |",
     "résous-la par microcopie, état, donnée ou interaction (forme située, §5) ; une erreur se résout jusqu’à la reprise "
     "(`SAVOIR/STATE`). |"),
    ("R8c-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Gestes de résolution (refonte, R8c).** Équilibre d’un titre et texte sur image dans le noyau ; la boucle réobserve "
     "l’ensemble après une correction locale ; récupération après erreur (`SAVOIR/STATE`), observée par interaction et appelée "
     "depuis Gate C.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R8c-T1": "TIT-01 absent",
    "R8c-I1": "TXI-01 absent",
    "R8c-B1": "résumé infidèle (relecture de l'ensemble)",
    "R8c-R1": "RCV-01 absent",
    "R8c-R2": "renvoi ACTION/GATE-C → RCV-01",
}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
