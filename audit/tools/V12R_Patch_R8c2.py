#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R8c-2 : raccords de R8c après vérification de l'owner (30-09-2026).

1. UNI-01 devient une garde BORNÉE et déclarée comme telle : retour des formulations retirées, impératifs universels
   explicites (toujours, à tous les…) sans négation. Contre-exemples de l'owner testés (1 rouge, 2 verts).
2. Équilibre d'un titre : corrections rattachées à un défaut observé ; composition voulue conservée ; hiérarchie par
   l'échelle, le poids, la position ou l'espace.
3. Récupération après erreur : focus selon le moment (soumission bloquée ou saisie en cours, annonce accessible sans
   déplacement) ; issue claire lorsque la réussite est impossible.
Rapport : `V12R_19_R8c2_RACCORDS.md`. Usage : identique à `V12R_Patch_R5b1.py` ; --mutations teste aussi les acceptations.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12R_Patch_R8c2_textes import RECUP_OLD, TITRE_OLD  # noqa: E402

S, C = "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("6db6bf09c2a21c05154a984a73f3defbcbd1b8cbd7631ebfedcf094868e7c0ea", HERE / "V12R_Patch_R8c2_fichiers" / "scripts" / "validate_structure.py"),
}

TITRE_NEW = ("**Équilibre d’un titre.** Quand un titre porte la scène (grand titre, accroche, chiffre mis en avant), règle-le sur le "
             "vrai texte, puis corrige ce que la capture montre : une coupe de ligne qui casse le sens ; un mot isolé en dernière "
             "ligne qui n’est pas voulu ; des lignes si inégales que le bloc se lit mal (`text-wrap: balance` peut aider si la "
             "cible le permet) ; une approche trop lâche aux grandes tailles, si la police le demande ; une hiérarchie aplatie, "
             "que l’on rétablit par l’écart d’échelle entre le titre et le texte qui suit, ou par le poids, la position ou "
             "l’espace. Un mot isolé, un déséquilibre ou un faible écart peut être le choix de composition : on le garde si la "
             "capture montre qu’il fonctionne. Observe sur capture, en desktop et en mobile, avec le contenu réel : la forme du "
             "bloc de titre reste lisible au flou.")
RECUP_NEW = ("**Récupération après erreur.** Un message d’erreur dit ce qui s’est passé, pourquoi si c’est utile, et comment "
             "reprendre ; il apparaît près de l’élément concerné, dans la langue du produit. La saisie de la personne est "
             "conservée et une action de reprise est proposée : corriger, réessayer ou revenir. Le focus dépend du moment : après "
             "une soumission bloquée, il peut aller à l’erreur ou au résumé des erreurs ; pendant la saisie, l’erreur est annoncée "
             "de façon accessible (région live) sans déplacer le focus. Une capture montre le message ; seule une interaction "
             "montre la reprise : parcours l’erreur, puis la correction, jusqu’au succès, ou jusqu’à une issue claire lorsque la "
             "réussite est impossible (alternative ou sortie expliquée).")

PATCH = [
    ("R8c2-T1", "titre : corrections sur défaut observé, composition voulue conservée", S, TITRE_OLD, TITRE_NEW),
    ("R8c2-R1", "récupération : focus selon le moment, issue claire", S, RECUP_OLD, RECUP_NEW),
    ("R8c2-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Raccords (refonte, R8c-2).** Garde des choix contextuels bornée et déclarée ; équilibre d’un titre rattaché à un défaut "
     "observé, composition voulue conservée ; récupération : focus selon le moment, issue claire si la réussite est impossible.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {"R8c2-T1": "résumé infidèle (titre : composition voulue)",
               "R8c2-R1": "résumé infidèle (récupération : focus selon le moment)"}
A = "\n## "
EXTRA_MUTATIONS = [
    ("impératif universel (contre-exemple 1 de l'owner)", S, A,
     "\nApplique toujours un traitement unique, puis utilise la comparaison pour vérifier le résultat.\n" + A, "[UNI-01]"),
    ("formulation retirée (assets)", S, A, "\nApplique un traitement unique et cohérent à tous les assets moyens.\n" + A, "[UNI-01]"),
    ("formulation retirée (icônes)", S, A, "\nIcônes : une seule famille.\n" + A, "[UNI-01]"),
]
ACCEPTS = [
    ("choix situé (contre-exemple 2 de l'owner)", S, A,
     "\nPour cette série de portraits, un seul traitement a été retenu afin d’unifier les éclairages disparates.\n" + A),
    ("interdiction de l'obligation (contre-exemple 3 de l'owner)", S, A,
     "\nN’impose jamais une seule famille à tous les projets.\n" + A),
    ("choix conditionné", S, A, "\nApplique un traitement unique si la comparaison confirme qu’il unifie la série.\n" + A),
    ("choix justifié", S, A,
     "\nUne seule famille d’icônes suffit lorsqu’elle couvre les pictogrammes nécessaires ; ce choix dépend du projet.\n" + A),
]


def accepts(root: Path) -> int:
    bad = 0
    for name, rel, old, new in ACCEPTS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = old in t
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            code, out = base.structure(copy)
            green = ok and code == 0
            print(f"acceptation {name} : {'VERT' if green else 'NON VERT'}")
            bad += 0 if green else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if "--mutations" in sys.argv:
        root = Path(sys.argv[1]).resolve()
        return 1 if (base.mutations(root) + accepts(root)) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
