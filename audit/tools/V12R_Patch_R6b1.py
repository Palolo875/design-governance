#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R6b-1 : une entrée humaine, un guide opérateur, une présentation, un README Local généré.

Diagnostic : `V12R_25_R6b_DIAGNOSTIC.md` ; amendements de la revue du 30-09-2026 intégrés (texte de référence dans
`package/README.md`, accès direct depuis la racine du dépôt de travail ; deux phrases de l'entrée amendées : apport des
contenus sans généralisation, acceptation « éléments réels, observés ou fournis »). Décision de l'owner : « Allons-y ».
Ferme D-11 et D-24 ; traite Q-13 (README) et R-25b. Rectifications déclarées : LCF-04, LCF-05 et LCF-10 (la table des modes
vit dans le guide opérateur ; le README n'en porte plus). Rapport : `V12R_27_R6b1_ENTREE.md`.
Usage : python3 V12R_Patch_R6b1.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

Q, RM, C, G = "V1/official/QUICKSTART.md", "V1/official/READING_MAP.md", "V1/official/CHANGELOG.md", "V1/official/GLOSSAIRE.md"
F = HERE / "V12R_Patch_R6b1_fichiers"
FILE_REPLACE = {
    "README.md": ("2d62d534edd9cb69c71a73fc623f83ba767d7c0187fb29ce7b307ac944da0440", F / "README.md"),
    "V1/official/README.md": ("f70adc0a1806c47986349beb12fcf4dc195aadac5bf2713b470a5d8a81d36089", F / "V1/official/README.md"),
    "scripts/build_distributions.sh": ("d6e7cbf7ba2375fc9f31f5db81435022d7fdf6bea25ffc115bcbb5e3f7b6af31",
                                       F / "scripts/build_distributions.sh"),
    "scripts/validate_structure.py": ("6e48aa83acd926ccb14cf1d5d6a7f5e8abb4fd9cc5b5f31a3f4fd8a20e9e953c", F / "scripts/validate_structure.py"),
    "scripts/validate_reading_map.py": ("625dc217a026e4442a1e5ffc026644d3c238f5ab870ac08bb7fd0bdbe2eb1152",
                                        F / "scripts/validate_reading_map.py"),
}

ROLE = ("> **Rôle de ce guide :** fournir une interface d’activation rapide. Il oriente la lecture et l’action, mais n’ajoute "
        "aucune règle, route, gate, axe, statut, verdict ou autorité. Les cinq sources normatives font foi.")
QS_CONST_OLD = (
    "### Constitution minimale\n\nAvant toute route détaillée, gardez en tête les cinq absolus de `DIRECTION` : direction "
    "perceptible pour une surface identitaire ; ancre observée ou fournie avant d’accepter une direction pour un produit réel ; "
    "preuves applicables au mode ; mode, prochaine preuve et budget déclarés avant l’exécution ; coordination du réel et du beau. "
    "La conformité seule ne constitue jamais une direction, une preuve d’usage ou une qualité réelle. La formulation canonique se "
    "trouve dans [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).\n\n"
    "| Si vous avez… | Faites d’abord… | Puis approfondissez avec… |\n|---|---|---|\n"
    "| 30 secondes | Décision, risque, preuve, capacité et ligne de run. | `DIRECTION/START`. |\n"
    "| 5 minutes | Classification, sources minimales, premier objet, observation et suite. | `DIRECTION`, `ACTION` et la route du mode. |\n")
QS_CONST_NEW = (
    "### Constitution et entrées par besoin\n\nLes cinq absolus de `DIRECTION` protègent chaque run : leur résumé est dans la "
    "section « Constitution minimale » du README du package, leur formulation canonique dans "
    "[`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).\n\n"
    "| Pour… | Faites d’abord… | Puis approfondissez avec… |\n|---|---|---|\n")
RM_CONST_OLD = (
    "Les cinq absolus de `DIRECTION` protègent la baseline : direction perceptible, ancre observée ou fournie avant d’accepter une "
    "direction pour un produit réel, preuves applicables, mode et prochaine preuve déclarés avant l’exécution, coordination du réel "
    "et du beau. La conformité ne remplace ni la direction ni la preuve. Pour le contrat complet, ouvrir "
    "[`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).")
RM_CONST_NEW = (
    "Les cinq absolus de `DIRECTION` protègent chaque run : résumé dans la section « Constitution minimale » du README du package, "
    "formulation canonique dans [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).")

PATCH = [
    ("R6b-Q1", "QUICKSTART : titre de guide opérateur", Q,
     "# Design Governance V1.1.1 — Quickstart\n", "# Design Governance V1.1.1 — Quickstart (guide opérateur)\n"),
    ("R6b-Q2", "QUICKSTART : pour qui, renvoi à l'entrée humaine", Q, ROLE,
     ROLE + "\n\n> **Pour qui :** ce guide sert à piloter un run (opérateur, designer ou agent). Pour faire simplement une "
     "demande, la section « Commencer » du README du package suffit : vous n’avez pas à choisir de mode."),
    ("R6b-Q3", "QUICKSTART : un seul parcours commun", Q,
     "## Démarrage en 90 secondes\n\nSi vous devez agir immédiatement, ne lisez pas encore les routes détaillées. Notez :",
     "## Parcours commun\n\nPour piloter un run, commencez ici ; les sections suivantes n’approfondissent que si le risque, le "
     "périmètre ou la décision le justifie. Notez :"),
    ("R6b-Q4", "QUICKSTART : façade d'activation sans second démarrage", Q,
     "### Façade d’activation en cinq éléments\n\nAvant les routes détaillées, notez seulement le **mode**, le **risque dominant**, "
     "la **décision à changer**, la **prochaine preuve** et l’**owner**. `DIRECTION/START` classe la demande ;",
     "### Façade d’activation : ce que chaque source apporte\n\nLa ligne du parcours commun est la façade d’activation. "
     "`DIRECTION/START` classe la demande ;"),
    ("R6b-Q5", "QUICKSTART : constitution en renvoi ; démarrages 30 s et 5 min retirés", Q, QS_CONST_OLD, QS_CONST_NEW),
    ("R6b-Q6", "QUICKSTART : la ligne de run", Q,
     "## 2. Le chemin en trente secondes\n\nAvant de construire ou de modifier, répondez aux cinq questions du démarrage en 90 secondes.",
     "## 2. La ligne de run\n\nAvant de construire ou de modifier, répondez aux cinq questions du parcours commun."),
    ("R6b-Q7", "QUICKSTART : parcours complet (R-25b)", Q,
     "## 3. Le parcours complet en cinq minutes", "## 3. Le parcours complet"),
    ("R6b-M1", "READING_MAP : constitution en renvoi", RM, RM_CONST_OLD, RM_CONST_NEW),
    ("R6b-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Entrée humaine (refonte, R6b-1).** Une seule entrée pour une personne qui fait une demande : section « Commencer » du "
     "README du package, en quatre questions (que demander, que fournir, que recevoir, comment poursuivre), au vouvoiement et sans "
     "mode à choisir ; le README Local la reprend, générée par le build depuis la même source. QUICKSTART devient le guide "
     "opérateur, à un seul parcours commun ; le README officiel devient un pointeur vers les sources normatives ; une seule "
     "constitution minimale, exacte (l’ancien résumé de l’absolu 2 est retiré).\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R6b-Q3": "vocabulaire retiré", "R6b-Q5": "vocabulaire retiré", "R6b-Q6": "vocabulaire retiré",
    "R6b-Q7": "vocabulaire retiré", "R6b-M1": "vocabulaire retiré",
}
ENTRY_Q2 = "**2. Que fournir ?**"
EXTRA_MUTATIONS = [
    ("question retirée de l'entrée", "README.md", ENTRY_Q2, "**Ce qu’il faut fournir.**", "[ENT-01]"),
    ("mode demandé dans l'entrée", "README.md", "Vous n’avez besoin de connaître ni les modes",
     "Choisissez d’abord le mode (`LITE` ou `DIRECTION`). Vous n’avez besoin de connaître ni les modes", "[ENT-01]"),
    ("tutoiement dans l'entrée", "README.md", "S’il en manque, l’agent", "Ne confonds pas. S’il en manque, l’agent", "[ENT-01]"),
    ("seconde entrée balisée", "README.md", "## Fiche de version",
     "<!-- entree:début -->\n## Commencer\n<!-- entree:fin -->\n\n## Fiche de version", "[ENT-01]"),
    ("constitution recopiée dans le glossaire", G, "\n## ",
     "\nRésumé : le réel et le beau sont cadrés ensemble.\n\n## ", "[CST-01]"),
    ("ancien absolu 2 dans le README (D-24)", "README.md", "une direction identitaire n’est acceptée qu’avec une ancre",
     "une surface identitaire ne doit pas être dessinée uniquement de mémoire ; une direction identitaire n’est acceptée qu’avec une ancre",
     "vocabulaire retiré"),
]

# Conditions de façade rectifiées : chacune rougit sous sa mutation (validate_reading_map.py).
LCF_MUTATIONS = [
    ("table des modes réintroduite dans le README (LCF-04, -05, -10)", "README.md", "## Mission",
     "| Situation | Chemin |\n|---|---|\n| Retouche d’une surface dont la direction existe | `ITER` |\n"
     "| Identité ou direction visuelle autonome | `DIRECTION` |\n\n## Mission", ("LCF-04", "LCF-05", "LCF-10")),
    ("craft comme critère de DIRECTION (QUICKSTART)", Q, "| Identité, premier contact ou direction visuelle autonome | `DIRECTION` |",
     "| Identité, premier contact ou craft exigeant | `DIRECTION` |", ("LCF-04",)),
    ("ITER sans direction retrouvable (QUICKSTART)", Q, "**`ITER`** — une direction ou un système existant est retrouvable",
     "**`ITER`** — quelque chose existe déjà", ("LCF-05",)),
    ("renvoi de classement retiré (QUICKSTART)", Q, "Classement : voir `DIRECTION/START`.", "", ("LCF-10",)),
]


def lcf_mutations(root: Path) -> int:
    bad = 0
    for name, rel, old, new, ids in LCF_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(copy / "scripts/validate_reading_map.py")],
                                 capture_output=True, text=True, cwd=copy)
            text = out.stdout + out.stderr
            red = ok and out.returncode != 0 and all(f"{i} :" in text for i in ids)
            print(f"mutation LCF {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def build_mutation(root: Path) -> int:
    """Le README Local doit venir du README du package : sans l'emplacement partagé, le build échoue."""
    with tempfile.TemporaryDirectory() as tmp:
        copy = base.fresh(root, tmp)
        p = copy / "scripts/build_distributions.sh"
        t = p.read_text(encoding="utf-8")
        ok = t.count("<!-- partage:entree -->\n") == 1
        p.write_text(t.replace("<!-- partage:entree -->\n", "", 1), encoding="utf-8")
        out = subprocess.run([sys.executable, "-B", str(copy / "scripts/validate_all.py")], capture_output=True, text=True, cwd=copy)
        red = ok and out.returncode != 0 and "partage:entree" in out.stdout + out.stderr
        print(f"mutation du build (README Local non généré) : {'ROUGE' if red else 'NON ROUGE'}")
        return 0 if red else 1


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if len(sys.argv) > 1 and "--mutations" in sys.argv:
        root = Path(sys.argv[1]).resolve()
        return 1 if base.mutations(root) + lcf_mutations(root) + build_mutation(root) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
