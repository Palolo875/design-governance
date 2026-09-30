#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION A1 : raccords sans arbitrage issus de l'audit interne (AUD-03, 04, 09, 10, 14, 15).

Audit : `V12R_37_AUDIT_INTERNE.md` (§6, point 1). Décision de l'owner : « Allons-y ». Chaque raccord aligne un passage sur une
règle déjà décidée (ANC-01, TRA-01, CNT-01, lecture de l'agent) ; aucune règle nouvelle. Rapport : `V12R_38_A1_RACCORDS.md`.
Usage : python3 V12R_Patch_A1.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, B, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG"))
FL, EX = "skills/design-governance-practice/references/flow.md", "skills/design-governance-practice/references/examples.md"
F = HERE / "V12R_Patch_A1_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("fac280423a3cf46a573892f63aa3a8e1c16ae40512d092d92585ec11c0f03d17", F / "validate_structure.py"),
}
PATCH = [
    # AUD-03 — FAIL-ASSUMED réservé à un échec connu
    ("A1-03a", "ACTION, pipeline étape 4 : ancre absente sans FAIL-ASSUMED", A,
     "Le run devient `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` selon le périmètre.",
     "Le run devient `RETURNED`, `EXPLORATORY` ou `ESCALATED` selon le périmètre ; `FAIL-ASSUMED` ne vaut que pour un échec "
     "connu (`ACTION/OVERRIDE`), jamais pour une ancre absente."),
    ("A1-03b", "DIRECTION, absolu 4 : preuve indisponible sans FAIL-ASSUMED", D,
     "par exemple `EXPLORATORY`, `RETURNED`, `FAIL-ASSUMED` ou `ESCALATED`.",
     "par exemple `EXPLORATORY`, `RETURNED` ou `ESCALATED` ; `FAIL-ASSUMED` ne vaut que pour un échec connu (`ACTION/OVERRIDE`)."),
    # AUD-04 — persistance et clôture en trace complète
    ("A1-04a", "DIRECTION : trace persistante en trace complète", D,
     "Les runs `STANDARD`, `DIRECTION` et `SYSTÈME` conservent une trace persistante.",
     "Un run `STANDARD`, `DIRECTION` ou `SYSTÈME` persistant, partagé ou audité conserve une trace persistante (trace complète, "
     "`ACTION/HANDOFF`) ; sinon, la trace légère suffit."),
    ("A1-04b", "ACTION/FAST-PATH : clôture en trace complète", A,
     "puis clôture avec la forme courte LITE (`ACTION/CLOSE-PACKAGE`, ligne LITE).",
     "puis, en trace complète, clôture avec la forme courte LITE (`ACTION/CLOSE-PACKAGE`, ligne LITE) ; en trace légère, la "
     "proposition suffit."),
    ("A1-04c", "BIBLIOTHEQUE, sélection par mode : persistance en trace complète", B,
     "La sélection structurelle est persistée dans la `RUN_CARD`",
     "En trace complète, la sélection structurelle est persistée dans la `RUN_CARD`"),
    ("A1-04d", "BIBLIOTHEQUE, test de sortie 8 : persistance en trace complète", B,
     "8. La sélection structurelle et sa justification sont-elles persistées",
     "8. En trace complète, la sélection structurelle et sa justification sont-elles persistées"),
    ("A1-04e", "flow.md : nœud final", FL, "G[Décider et fermer]", "G[Proposer ou fermer]"),
    ("A1-04f", "flow.md : proposer en trace légère, fermer en trace complète", FL,
     "puis décider et fermer avec ses limites",
     "puis présenter la proposition (trace légère) ou décider et fermer avec ses limites (trace complète)"),
    # Paragraphe distinct : la phrase d'en-tête reste intacte pour la mutation historique P-32 (harnais R, R-24).
    ("A1-04g", "examples.md : niveau de trace des exemples", EX,
     "puis contrôler avec `scripts/validate_run_card.py`.",
     "puis contrôler avec `scripts/validate_run_card.py`.\n>\n> **Niveau de trace.** Les exemples qui se terminent par "
     "`CLOSED` montrent une trace complète (clôture demandée ou run persistant) ; « fabrication depuis un brief flou » montre la "
     "sortie par défaut : une proposition et sa réponse visible, sans clôture."),
    # AUD-09 — règle CTA : valeur d'exemple marquée
    ("A1-09", "DIRECTION, règle CTA : renvoi à CNT-01", D,
     "Un lien vide, une inscription fictive ou une démo qui simule une conséquence externe ne peut pas être présenté comme une "
     "action disponible.",
     "Un lien vide, une inscription fictive ou une démo qui simule une conséquence externe ne peut pas être présenté comme une "
     "action disponible. Une action principale dont la valeur manque (numéro, adresse, lien) reste présente avec une valeur "
     "d’exemple marquée (`CNT-01`) : c’est une limite déclarée, pas un retrait."),
    # AUD-10 — lecture de l'agent
    ("A1-10a", "DIRECTION : ce que l'agent lit au démarrage", D,
     "`DIRECTION` est le **seul document canonique de cadrage chargé au démarrage d’un run**.",
     "`DIRECTION` est le **seul document canonique de cadrage** ; au démarrage d’un run, l’agent en lit le noyau (compilé dans "
     "la skill) et les routes de `DIRECTION/CHARGE`."),
    ("A1-10b", "DIRECTION : READING_MAP pour une personne", D,
     "Pour éviter de recomposer le démarrage, utilisez `READING_MAP.md` comme vue dérivée lorsque le besoin est déjà identifiable.",
     "Pour une personne, `READING_MAP.md` est la vue dérivée lorsque le besoin est déjà identifiable ; l’agent charge par "
     "`DIRECTION/CHARGE`."),
    ("A1-10c", "flow.md : READING_MAP si une personne le demande", FL,
     "consulter la section « Combinaisons par résultat recherché » de `READING_MAP.md`",
     "consulter, si une personne le demande, la section « Combinaisons par résultat recherché » de `READING_MAP.md`"),
    # AUD-14 — veille : signal P1 non retrouvé, signal R10
    ("A1-14", "SAVOIR, marqueurs de vague (noyau) : signal R10", S,
     "Signal à confirmer (P1, 27-09-2026, 3 rendus sur 3, même auteur) : grotesque large ou condensée (Archivo) sur fond blanc "
     "neutre avec un seul accent vif.",
     "Signal P1 (27-09-2026, 3 rendus sur 3, même auteur : grotesque large ou condensée, Archivo, sur fond blanc neutre avec un "
     "seul accent vif) non retrouvé en R10. Signal R10 (30-09-2026, auto-comparaison, 6 rendus) : même objet central par brief "
     "(fournées du jour ; facture tamponnée) et même grotesque de titre sur un brief, avec ou sans système."),
    # AUD-15 — entrée humaine : une seule mention
    ("A1-15", "README, entrée humaine : redite retirée (question 3)", "README.md",
     " C’est une proposition à discuter, pas une validation : pour retenir cette direction pour un vrai produit, l’agent doit "
     "s’appuyer sur des éléments réels, observés ou fournis, et effectuer les vérifications nécessaires.",
     " C’est une proposition à discuter, pas une validation."),
    ("A1-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords d’audit (refonte, audit A1).** `FAIL-ASSUMED` réservé à un échec connu dans le pipeline et l’absolu 4 ; "
     "persistance et clôture en trace complète (DIRECTION, `FAST-PATH`, BIBLIOTHEQUE, flux, exemples) ; règle CTA reliée à la "
     "valeur d’exemple marquée ; l’agent lit le noyau et `CHARGE`, READING_MAP sert aux personnes ; veille mise à jour (R10) ; "
     "redite retirée de l’entrée humaine.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {
    "A1-03a": "pipeline (AUD-03)", "A1-03b": "preuve indisponible", "A1-04a": "trace persistante en trace complète",
    "A1-04b": "FAST-PATH : clôture", "A1-04c": "sélection structurelle", "A1-04d": "sélection structurelle",
    "A1-04f": "flux : fermer", "A1-04g": "exemples : niveau de trace", "A1-09": "règle CTA", "A1-10a": "vocabulaire retiré",
    "A1-10b": "vocabulaire retiré", "A1-10c": "flux : READING_MAP", "A1-14": "signal R10", "A1-15": "redite",
}
EXTRA_MUTATIONS: list = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
