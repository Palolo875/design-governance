#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION AP5b (audit progressif externe, unité 5b) : C15 (option a), C25 à C31.

C15 toute exigence UI/UX déclarée est couverte (code et exemple ; ACTION inchangé) ; C25 DOMAIN-FRAME dans CHARGE ;
C26 vues alignées sur CHARGE ; C27 delta local qualifié ; C28 validité de la comparaison distincte de la version retenue ;
C29 dépendance porteuse dans le test de masquage ; C30 « si rien ne les justifie » ; C31 cinq responsabilités regroupables.
Textes : `V12R_45` §3, soumis à l'owner ; décision (01-10-2026) : « (a), allons-y pour AP5b ».
Rapport : `V12R_46_AP5b_RACCORDS.md`. Usage : python3 V12R_Patch_AP5b.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12_Patch_ABD import apply  # noqa: E402

D, A, S, B, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG"))
EXAMPLE = "schemas/examples/production_contracts.example.json"
F = HERE / "V12R_Patch_AP5b_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_contracts.py": ("5c6f884ebf29df589a38221661f679f00945137b8bdc85b48060af1c84ff721d", F / "validate_contracts.py"),
    "scripts/validate_structure.py": ("09925ebda339235048b3399a207eb14b970b9727c44dac44d4cd2af6125ff06c", F / "validate_structure.py"),
}
DOMAIN = ("`DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer "
          "la structure, l’expression ou la preuve")
NEW_COVERAGE = [
    ("responsive_matrix: desktop: contexte et détail côte à côte", "/incidents@1440px", "OBSERVED"),
    ("responsive_matrix: petit écran: séquence guidée", "/incidents@390px", "NOT-VERIFIED"),
    ("accessibility_basis: sémantique des statuts", "/incidents#status-semantics", "NOT-VERIFIED"),
    ("accessibility_basis: clavier", "/incidents#keyboard", "OBSERVED"),
    ("accessibility_basis: information non portée par la couleur", "/incidents#status-icons", "NOT-VERIFIED"),
    ("robustness_basis: horodatages variables", "/incidents?fixture=timestamps", "NOT-VERIFIED"),
    ("robustness_basis: absence de données", "/incidents?state=empty", "NOT-VERIFIED"),
    ("robustness_basis: non-régression du tri", "/incidents?sort=severity", "NOT-VERIFIED"),
]
LAST = '      {"requirement":"robustness_basis: libellés longs", "artifact_locator":"/incidents?fixture=long-labels", "proof_status":"NOT-VERIFIED"}\n    ]'
PATCH = [
    ("AP5b-C15", "exemple UI/UX : toute exigence déclarée couverte (C15 a)", EXAMPLE, LAST,
     LAST[:-6] + "".join(f',\n      {{"requirement":"{r}", "artifact_locator":"{loc}", "proof_status":"{st}"}}'
                         for r, loc, st in NEW_COVERAGE) + "\n    ]"),
    ("AP5b-C25a", "CHARGE, STANDARD : DOMAIN-FRAME (C25)", D,
     "| `SAVOIR/FRAME` si le cadrage est ambigu, une route BIBLIOTHEQUE structurante et la route SAVOIR du risque dominant. |",
     f"| `SAVOIR/FRAME` si le cadrage est ambigu ; {DOMAIN} ; une route BIBLIOTHEQUE structurante et la route SAVOIR du "
     "risque dominant. |"),
    ("AP5b-C25b", "CHARGE, DIRECTION : DOMAIN-FRAME (C25)", D,
     "`SAVOIR/FRAME`, `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/SOURCE` et `BIBLIOTHEQUE/SELECT` si nécessaires.",
     f"`SAVOIR/FRAME`, `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/SOURCE` et `BIBLIOTHEQUE/SELECT` si nécessaires ; {DOMAIN}."),
    ("AP5b-C26a", "déclencheurs critiques, détail final : « ou » comme CHARGE (C26)", D,
     "`SAVOIR/STATE`, `SAVOIR/INTEGRITY` et capture rendue.",
     "`SAVOIR/STATE` ou `SAVOIR/INTEGRITY` selon la question ouverte, et capture rendue."),
    ("AP5b-C26b", "ACTION/ROUTING : COMPONENTS si un composant change (C26)", A,
     "| Token, composant ou blast radius | `SAVOIR/SYSTEM`, `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` si partagé. |",
     "| Token, composant ou blast radius | `SAVOIR/SYSTEM` si une décision partagée change, `BIBLIOTHEQUE/COMPONENTS` si "
     "un composant change, `ACTION/RUN-SYSTEM` si partagé. |"),
    ("AP5b-C26c", "SAVOIR/STYLE : FRAME conditionnel (C26)", S,
     "`DIRECTION/START → SAVOIR/FRAME → SAVOIR/STYLE si nécessaire → ACTION/RUN-*`",
     "`DIRECTION/START → SAVOIR/FRAME si le cadrage est à éclaircir → SAVOIR/STYLE si nécessaire → ACTION/RUN-*`"),
    ("AP5b-C27", "contrat de composant : delta local qualifié (C27)", B,
     "un delta local n’en porte aucune obligation.",
     "un delta local sans responsabilité critique, réutilisable ou partagée n’en porte aucune obligation ; s’il touche un "
     "composant critique ou partagé, ou devient réutilisable, il relève de ce contrat (reclasser avec `DIRECTION/START`)."),
    ("AP5b-C28", "avant/après : validité et version retenue (C28)", B,
     "Il est accepté uniquement si la version après réduit une ambiguïté, préserve les états critiques et rend une décision "
     "plus directe sans exiger davantage d’attention.",
     "La comparaison est valide si elle isole la décision et observe le critère déclaré. La version retenue est celle qui "
     "réduit une ambiguïté, préserve les états critiques et rend une décision plus directe sans exiger davantage "
     "d’attention : l’original s’il résout mieux (`ACTION/B1b`)."),
    ("AP5b-C29", "test de masquage : dépendance porteuse (C29)", B,
     "Ce test est `PERCEPTUAL` ou `EXPERT` ; il ne prouve pas seul l’utilisabilité de la surface.",
     "Ce test est `PERCEPTUAL` ou `EXPERT` ; il ne prouve pas seul l’utilisabilité de la surface. Si la composition dépend "
     "de ce qui est masqué par une relation déclarée, avec un repli, la dépendance est recevable (`BIBLIOTHEQUE/GATE`, "
     "non-généricité) ; le masquage sert à diagnostiquer, pas à exiger un décor indépendant du contenu."),
    ("AP5b-C30", "convergence : si rien ne les justifie (C30, noyau)", S,
     "Si oui, nomme ce qui, dans le produit, les justifie. Sinon, reconsidère-les.",
     "Si oui, nomme ce qui, dans le produit, les justifie ; si rien ne les justifie, reconsidère-les."),
    ("AP5b-C31", "preuve par médium : cinq responsabilités regroupables (C31)", S,
     "dérive cinq artefacts de preuve avant de juger :",
     "examine cinq responsabilités de preuve, regroupables dans un même artefact, avant de juger :"),
    ("AP5b-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords de chargement et de précision (audit progressif, unité 5b).** Toute exigence UI/UX déclarée est "
     "couverte (`OBSERVED`, `NOT-VERIFIED` ou `N/A-JUSTIFIED`) ; `DIRECTION/CHARGE` appelle `DIRECTION/DOMAIN-FRAME` pour "
     "une demande nouvelle, ambiguë ou multi-domaines ; les vues de chargement suivent les conditions de `CHARGE` ; le "
     "delta local, la comparaison avant/après, le test de masquage, la question de convergence et la preuve par médium "
     "sont précisés.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {
    "AP5b-C25a": "(C25)", "AP5b-C25b": "(C25)", "AP5b-C26a": "(C26)", "AP5b-C26b": "(C26)", "AP5b-C26c": "(C26)",
    "AP5b-C27": "(C27)", "AP5b-C28": "vocabulaire retiré", "AP5b-C29": "(C29)", "AP5b-C30": "vocabulaire retiré",
    "AP5b-C31": "vocabulaire retiré",
}
REBUILD = {"AP5b-C25a", "AP5b-C25b", "AP5b-C30"}


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
    # C15 : la règle de couverture retirée du code, l'exemple reste ; le cas unitaire C15-1 doit rougir.
    with tempfile.TemporaryDirectory() as tmp:
        copy = base.fresh(root, tmp)
        path = copy / "scripts" / "validate_contracts.py"
        text = path.read_text(encoding="utf-8")
        old = "            if item.strip() and norm(item) not in covered[name]:"
        ok = text.count(old) == 1
        path.write_text(text.replace(old, "            if False:", 1), encoding="utf-8")
        out = subprocess.run([sys.executable, "-B", str(path)], capture_output=True, text=True, cwd=copy)
        red = ok and out.returncode != 0 and "cas unitaire C15-1" in out.stdout + out.stderr
        print(f"mutation de code C15 (couverture limitée aux états) : {'ROUGE' if red else 'NON ROUGE'}")
        bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, []
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        return 1 if mutations(Path(sys.argv[1]).resolve()) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
