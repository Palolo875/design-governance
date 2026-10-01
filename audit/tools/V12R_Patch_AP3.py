#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION AP3 (audit progressif externe, unité 3) : raccords de procédure et de fabrication.

C08 déclencheur UI/UX avant fabrication ; C05 `CLOSED` distinct du résultat ; C06 petits `ITER` vers le paquet `ITER` ;
C07 portée de l'atelier (B1b) compilée ; C09 `N/A-JUSTIFIED` distinct d'une preuve manquante ou d'une confirmation ;
C10 règle d'or 8 et réserve structurée ; D-26 (option (a) de l'owner) fonctions d'un produit fictif marquées.
Audit : `DG_Audit_progressif_10` ; décisions de l'owner (01-10-2026) : plan AP en cinq unités, D-26 (a).
Bornes : C08 = absence de déclencheur avant fabrication (pas « jamais chargé ») ; C07 = contexte rétabli, sans extension.
Rapport : `V12R_42_AP3_RACCORDS.md`. Usage : python3 V12R_Patch_AP3.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12_Patch_ABD import apply  # noqa: E402

D, A, S, Q, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "QUICKSTART", "CHANGELOG"))
F = HERE / "V12R_Patch_AP3_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("1ed2dfdf684fc45f43730807ce7aab69166ebeed58f71748acd99bc1826fa892", F / "validate_structure.py"),
}
UI = "`ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée"
PATCH = [
    # C08 — déclencheur UI/UX avant fabrication (CHARGE, compilé dans le noyau ; carte d'ACTION, vue de CHARGE)
    ("AP3-C08a", "CHARGE, STANDARD : UI-UX-REALITY avant fabrication", D,
     "| **STANDARD** | `ACTION/RUN-STANDARD` ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte. |",
     f"| **STANDARD** | `ACTION/RUN-STANDARD` ; {UI} ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte. |"),
    ("AP3-C08b", "CHARGE, DIRECTION : UI-UX-REALITY avant fabrication", D,
     "`ACTION/FIRST-RENDER`, `ACTION/RUN-DIRECTION`",
     f"`ACTION/FIRST-RENDER`, {UI}, `ACTION/RUN-DIRECTION`"),
    ("AP3-C08c", "carte d'ACTION (vue), STANDARD", A,
     "| `STANDARD` | `ACTION/RUN-STANDARD` ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte ;",
     f"| `STANDARD` | `ACTION/RUN-STANDARD` ; {UI} ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte ;"),
    ("AP3-C08d", "carte d'ACTION (vue), DIRECTION", A,
     "| `DIRECTION` | `ACTION/RUN-DIRECTION`, `ACTION/PIPELINE-DIRECTION`,",
     f"| `DIRECTION` | `ACTION/RUN-DIRECTION`, {UI}, `ACTION/PIPELINE-DIRECTION`,"),
    # C05 — CLOSED décrit la persistance ; le résultat se déclare à part
    ("AP3-C05", "RUN-DIRECTION : clôture et résultat séparés", A,
     "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` uniquement si la direction est tenue et les preuves "
     "applicables déclarées. Sinon, passer à `RETURNED`, `RETURN-DIRECTION`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED` "
     "selon la preuve et le risque.",
     "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque l’artefact et la trace sont persistés : "
     "`CLOSED` ne dit pas que la direction est tenue (`ACTION/STATUS`). Le résultat se déclare à part : une direction tenue, "
     "preuves applicables déclarées, peut recevoir un verdict accepté ; sinon, l’issue est `RETURNED`, `EXPLORATORY`, "
     "`FAIL-ASSUMED` (échec connu) ou `ESCALATED`, avec le verdict `RETURN-DIRECTION` si la direction doit être reprise, "
     "selon la preuve et le risque."),
    # C06 — chaque mode garde son paquet
    ("AP3-C06", "FAST-PATH : paquet du mode", A,
     "puis, en trace complète, clôture avec la forme courte LITE (`ACTION/CLOSE-PACKAGE`, ligne LITE) ; en trace légère, "
     "la proposition suffit.",
     "puis, en trace complète, clôture avec le paquet de son mode : forme courte LITE pour `LITE`, paquet `ITER` pour un "
     "`ITER` (`ACTION/CLOSE-PACKAGE`) ; en trace légère, la proposition suffit."),
    # C07 — portée de l'atelier, en tête du bloc compilé
    ("AP3-C07", "atelier d'édition : portée B1b et exceptions (noyau)", A,
     "<!-- noyau:début BOUCLE-ATELIER -->\n",
     "<!-- noyau:début BOUCLE-ATELIER -->\nDans le scope de B1b (surface `DIRECTION` qui accepte avec l’axe V positif, en "
     "trace complète : `ACTION/B1b`), cet atelier est requis, sauf deux motifs `N/A-JUSTIFIED` : aucune décision principale "
     "éditable, ou une paire équivalente encore valide qui couvre la même décision. Hors de ce scope, il ne s’impose pas.\n\n"),
    # C09 — N/A distinct d'une preuve manquante ou d'une confirmation
    ("AP3-C09a", "SAVOIR, niveau requis par le module", S,
     "| `[REQUIS PAR LE MODULE — scope]` | Obligation spécialisée. | Exécuter ou déclarer `N/A-JUSTIFIED` dans le scope. |",
     "| `[REQUIS PAR LE MODULE — scope]` | Obligation spécialisée. | Exécuter dans le scope ; sinon déclarer `NOT-VERIFIED` "
     "(preuve manquante), ou `N/A-JUSTIFIED` avec sa raison si l’obligation ne s’applique pas. |"),
    ("AP3-C09b", "SAVOIR, recherche sans effet", S,
     "Lorsque la recherche ne modifie aucune décision, conserve `N/A-JUSTIFIED` et n’approfondis pas par réflexe.",
     "Lorsque la recherche ne peut modifier aucune décision, déclare `N/A-JUSTIFIED` et n’approfondis pas par réflexe ; une "
     "recherche faite qui confirme la décision est une confirmation (`ACTION/STATUS`), pas un `N/A-JUSTIFIED`."),
    ("AP3-C09c", "SAVOIR, module sans effet", S,
     "Si la réponse est aucune, l’artefact est documentaire plutôt que décisionnel ; arrête, simplifie ou justifie "
     "`N/A-JUSTIFIED`.",
     "Si la réponse est aucune, l’artefact est documentaire plutôt que décisionnel ; arrête ou simplifie. Une décision que le "
     "module a confirmée se déclare comme confirmation ; `N/A-JUSTIFIED` reste réservé au module qui ne pouvait rien changer."),
    ("AP3-C09d", "QUICKSTART, avant de fermer", Q,
     "2. la preuve attendue est obtenue ou déclarée `NOT-VERIFIED`, `NOT-OBSERVED` ou `N/A-JUSTIFIED` avec sa raison ;",
     "2. la preuve attendue est obtenue ou déclarée `NOT-VERIFIED` ; une conséquence attendue non observée est "
     "`NOT-OBSERVED` ; `N/A-JUSTIFIED`, avec sa raison, ne vaut que si la preuve ne s’applique pas ;"),
    # C10 — règle d'or 8
    ("AP3-C10", "SAVOIR, règle d'or 8", S,
     "8. Si un risque reste, retourne, passe en `EXPLORATORY` ou journalise un `FAIL-ASSUMED` autorisé ; ne compense jamais "
     "un axe bloquant par une moyenne.",
     "8. Si un risque bloquant reste, retourne, passe en `EXPLORATORY` ou journalise un `FAIL-ASSUMED` autorisé (échec "
     "connu) ; un risque non bloquant peut rester en réserve structurée (`ACCEPTED-WITH-RESERVATION`, `ACTION/STATUS`) ; "
     "ne compense jamais un axe bloquant par une moyenne."),
    # D-26 (a) — fonctions d'un produit fictif
    ("AP3-D26", "CNT-01 : fonctions d'un produit fictif marquées (noyau)", D,
     "une valeur inconnue ne la retire pas. Le marquage est discret",
     "une valeur inconnue ne la retire pas. Pour un produit fictif ou non encore construit, les fonctions, intégrations et "
     "conformités affirmées sont aussi des contenus d’exemple, marqués comme le nom et le prix. Le marquage est discret"),
    ("AP3-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords de procédure et de fabrication (audit progressif, unité 3).** `DIRECTION/CHARGE` appelle "
     "`ACTION/UI-UX-REALITY` avant fabrication pour une surface UI/UX nouvelle ou substantiellement modifiée (STANDARD, "
     "DIRECTION) ; `CLOSED` décrit la persistance et le résultat se déclare à part (`ACTION/RUN-DIRECTION`) ; un petit "
     "`ITER` garde le paquet `ITER` ; la portée de l’atelier d’édition (B1b) entre dans le noyau ; `N/A-JUSTIFIED` ne masque "
     "ni une preuve manquante ni une confirmation ; un risque non bloquant peut rester en réserve structurée ; les fonctions "
     "d’un produit fictif sont des contenus d’exemple marqués.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {
    "AP3-C08a": "[UIX-01]", "AP3-C08b": "[UIX-01]", "AP3-C05": "vocabulaire retiré", "AP3-C06": "(C06)",
    "AP3-C07": "(C07)", "AP3-C09a": "(C09)", "AP3-C09b": "(C09)", "AP3-C09c": "(C09)", "AP3-C09d": "(C09)",
    "AP3-C10": "(C10)", "AP3-D26": "(D-26)",
}
EXTRA_MUTATIONS = [
    ("UI-UX-REALITY ajouté à la ligne LITE", D, "| **LITE** | `ACTION/RUN-LITE`,", f"| **LITE** | {UI} ; `ACTION/RUN-LITE`,",
     "[UIX-01]"),
    ("déclencheur UI/UX retiré de la section compilée", "skills/design-governance-practice/SKILL.md",
     f"`ACTION/FIRST-RENDER`, {UI}", "`ACTION/FIRST-RENDER`", "[UIX-01] noyau compilé"),
    ("RUN-DIRECTION : résultat sans renvoi à STATUS", A, "`CLOSED` ne dit pas que la direction est tenue (`ACTION/STATUS`).",
     "`CLOSED` ne dit pas que la direction est tenue.", "(C05)"),
]


# Entrées portées par un bloc compilé : la source mutée est recompilée, seule la garde visée doit rougir.
REBUILD = {"AP3-C08a", "AP3-C08b", "AP3-C07", "AP3-D26"}


def mutations(root: Path) -> int:
    bad = 0
    for pid, motif in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            problems = apply(copy, [e for e in PATCH if e[0] == pid], reverse=True)
            if not problems and pid in REBUILD:
                base.build_core(copy)
            code, out = base.structure(copy)
            red = code != 0 and motif in out and not problems
            print(f"inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'} (motif « {motif} »){' ; ' + '; '.join(problems) if problems else ''}")
            bad += 0 if red else 1
    base.MUTATION_OF = {}
    return bad + base.mutations(root)


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        return 1 if mutations(Path(sys.argv[1]).resolve()) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
