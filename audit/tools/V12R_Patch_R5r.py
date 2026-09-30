#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION restes R5 : copies du handoff, D-15, PRINT_FIELD, alternative située.

Diagnostic : `V12R_29_R5_RESTES_DIAGNOSTIC.md`, maquette `V12R_Maquette_R5.py` (deux retouches de la revue du 30-09 intégrées,
§8). Décision de l'owner : « Allons-y » ; ligne de signal PRINT_FIELD dans le noyau. BIBLIOTHEQUE est remplacée par la
sortie exacte de la maquette (déplacements de sections) ; les autres sources passent par des entrées de texte.
Rapport : `V12R_30_R5_RESTES.md`. Usage : python3 V12R_Patch_R5r.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, B, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG"))
F = HERE / "V12R_Patch_R5r_fichiers"
FILE_REPLACE = {
    B: ("f161c7b5a5c02220b3820c7c3ecc1206c6c76f399e5c2746c16b33b62a3a5028", F / B),
    "scripts/validate_structure.py": ("15bf09832d6126eb3e340acb62d2adcb5fc6bd84cf0510cc4b7f27478b048d12",
                                      F / "scripts/validate_structure.py"),
}
HANDOFF = ("`MODE`, `RISK`, `SCOPE`, `ARTIFACT`, `OBSERVATION/METHOD`, `PROOF/TRACE-LOCATOR`, `LIMIT/NOT-VERIFIED`, "
           "`DECISION-CHANGE`, `NEXT-ACTION`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`")
DIV_OLD = ("Avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative considérée, la "
           "raison de son niveau de matérialisation et la preuve attendue. La projection JSON ne porte pas ce paquet (voir "
           "`ACTION/RUN_CARD`). Matérialise-la seulement au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou "
           "rendu. Si aucune alternative plausible ne peut modifier le choix, note cette condition et passe à la spec après avoir "
           "nommé la raison.")
DIV_NEW = ("Ses leviers sont les axes de `SAVOIR/CRAFT/CFT-02` ; sa matérialisation, sa trace selon le niveau retenu et sa "
           "comparaison suivent `ACTION/PIPELINE-DIRECTION` (étapes 3 et 7).")
TRIGGER = "En `DIRECTION`, considère une **alternative située** lorsque la décision est ouverte"

PATCH = [
    ("R5r-H1", "SAVOIR : copie du handoff → renvoi", S,
     "Lorsque le run passe à ACTION, conserve au minimum " + HANDOFF + " dans la `RUN_CARD` ou la trace équivalente.",
     "Lorsque le run passe à ACTION, ces champs rejoignent le handoff canonique (`ACTION/HANDOFF`) ; en trace complète, ils vont "
     "dans la `RUN_CARD` ou la trace équivalente."),
    ("R5r-L1", "DIRECTION, lecture instrumentée : ouverture conditionnelle (D-15)", D,
     "Pour éviter de présenter une hypothèse de proportion comme un gain démontré, distingue dans la trace :",
     "Pour éviter de présenter une hypothèse de proportion comme un gain démontré, dans un run instrumenté ou audité, distingue "
     "dans la trace :"),
    ("R5r-L2", "DIRECTION, lecture instrumentée : déclaration conditionnelle (D-15)", D,
     "Déclare dans la trace la catégorie de lecture applicable ;",
     "Dans un run instrumenté ou audité, déclare dans la trace la catégorie de lecture applicable (en trace légère, cette "
     "déclaration n’est pas demandée) ;"),
    ("R5r-A1", "DIRECTION, absolu 3 : alternative en renvoi", D,
     "En `DIRECTION`, considère une alternative située lorsque la décision est ouverte et qu’une position différente peut "
     "raisonnablement changer le choix. **Avant le build**, la trace nomme la position retenue, l’alternative considérée, la raison "
     "de son niveau de matérialisation et la preuve attendue. Matérialise-la seulement au niveau nécessaire pour comparer cette "
     "décision : phrase, schéma, cible ou rendu. Une alternative qui ne peut rien changer n’est pas produite ; sa non-production "
     "est justifiée.",
     "En `DIRECTION`, l’alternative située suit « Direction divergente » (déclenchement), `SAVOIR/CRAFT/CFT-02` (leviers) et "
     "`ACTION/PIPELINE-DIRECTION` (matérialisation, trace et comparaison) ; une alternative qui ne peut rien changer n’est pas "
     "produite, et sa non-production est justifiée."),
    ("R5r-A2", "DIRECTION, Direction divergente : leviers et suite en renvoi", D, DIV_OLD, DIV_NEW),
    ("R5r-A3", "DIRECTION, Direction divergente : concept ALT-01 (lieu unique du déclenchement)", D,
     "\n" + TRIGGER, "\n<!-- concept:ALT-01 -->\n" + TRIGGER),
    ("R5r-A4", "ACTION, pipeline étape 3 : trace graduée ; déclenchement et leviers en renvoi", A,
     "Lorsque la décision est ouverte et qu’une position différente peut réellement changer le choix, considère une proposition "
     "crédible répondant à un public, un JTBD, une contrainte ou une opportunité différente.",
     "Le déclenchement appartient à `DIRECTION` (« Direction divergente ») et les leviers à `SAVOIR/CRAFT/CFT-02`. En trace "
     "complète, avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative "
     "considérée, la raison de son niveau de matérialisation et la preuve attendue ; la projection JSON ne porte pas ce paquet "
     "(voir `ACTION/RUN_CARD`). En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7)."),
    ("R5r-C1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Répétitions retirées (refonte, restes R5).** Copies du handoff remplacées par un renvoi à `ACTION/HANDOFF` ; catégories "
     "de lecture et contrat de promotion sortis du préambule de BIBLIOTHEQUE (`BIBLIOTHEQUE/EVOLUTION`), déclaration de lecture "
     "limitée aux runs instrumentés ou audités ; alternative située répartie (DIRECTION déclenche, SAVOIR donne les leviers, ACTION "
     "matérialise, trace et compare) ; `PRINT_FIELD` relié aux signaux de convergence comme question de jugement.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R5r-H1": "vocabulaire retiré", "R5r-L1": "lecture instrumentée : ouverture", "R5r-L2": "lecture instrumentée : déclaration",
    "R5r-A1": "vocabulaire retiré", "R5r-A2": "trace de l'alternative graduée", "R5r-A3": "ALT-01 absent", "R5r-A4": "vocabulaire retiré",
}
EXTRA_MUTATIONS = [
    ("copie du handoff réintroduite (BIBLIOTHEQUE)", B, " Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`).",
     " Conservez aussi `MODE`, `RISK` et `SCOPE`.", "vocabulaire retiré"),
    ("catégories de lecture dans le préambule (D-15)", B, "## BIBLIOTHEQUE/READ",
     "Déclarez `STARTUP-NOMINAL` ou `AUDIT-READ` pour chaque lecture.\n\n## BIBLIOTHEQUE/READ", "[MNT-01]"),
    ("contrat de promotion revenu dans le préambule (D-15)", B, "## BIBLIOTHEQUE/READ",
     "### Contrat minimal par périmètre de contribution\n\nRetour.\n\n## BIBLIOTHEQUE/READ", "[MNT-01]"),
    ("signal PRINT_FIELD retiré du noyau", B,
     "\n| Grain, trame d’impression ou texture repris d’un brief à l’autre | Quelle matière la thèse de ce produit appelle-t-elle, et "
     "que perd la page si on la retire (`MODIFIER/PRINT_FIELD`, test de retrait) ? |", "", "signal de matière"),
    ("trace de l'alternative non graduée (ACTION)", A,
     " En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7).", "", "trace de l'alternative graduée"),
    ("déclenchement recopié (ALT-01 en double)", A, "Le déclenchement appartient à `DIRECTION`",
     "<!-- concept:ALT-01 -->\nLe déclenchement appartient à `DIRECTION`", "ALT-01"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
