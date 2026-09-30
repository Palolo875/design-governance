#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION A2 : une seule liste de chargement (AUD-01), plancher SAVOIR dans le noyau (AUD-02),
lieu de la trace légère (AUD-05).

Audit : `V12R_37` ; options : `V12R_38` §5. Décision de l'owner : « Allons-y » sur les options recommandées (a).
Forme retenue pour AUD-01 : les tables d'ACTION et de DIRECTION restent (contrats de harnais, de LCF et de 13.02) mais
deviennent des vues de `DIRECTION/CHARGE`, sans chargement concurrent ; la colonne « Ajouter seulement si » de `CHARGE` entre
dans le noyau (seule liste lue par l'agent). Rapport : `V12R_39_A2_ARCHITECTURE.md`.
Usage : python3 V12R_Patch_A2.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, C = (f"V1/official/{n}.md" for n in ("DIRECTION", "ACTION", "SAVOIR", "CHANGELOG"))
F = HERE / "V12R_Patch_A2_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("e056e6204ad2fccde018c8cf02e3dc19292ee461c70c65929bb5e5fb6f38b4fb", F / "validate_structure.py"),
    "scripts/build_core.py": ("d07af5091e8c4ebb6f47b41510b0232ddb98aec9662c8d187646bb543abd13cb", F / "build_core.py"),
}
PATCH = [
    # AUD-01 — une seule liste : CHARGE ; les autres tables sont des vues
    ("A2-01a", "ACTION, responsabilité : le chargement suit CHARGE", A,
     "Pour une lecture rapide, commencez par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode "
     "`ACTION/RUN-<MODE>`, et chargez seulement les gates correspondant au risque déclaré.",
     "Dans un run, le chargement suit `DIRECTION/CHARGE`, seule liste de chargement. Pour lire ACTION hors run, commencez par "
     "`ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode `ACTION/RUN-<MODE>`, et chargez seulement les gates "
     "correspondant au risque déclaré."),
    ("A2-01b", "ACTION, carte de lecture : vue de CHARGE", A,
     "**Socle pour tous les modes :** `ACTION/STATUS` et `ACTION/PRECONDITION`.\n\n| Mode | Chargement propre au mode |",
     "Cette carte est une vue de `DIRECTION/CHARGE`, pas une seconde liste : elle nomme les sections d’ACTION que la route de "
     "chaque mode appelle.\n\n**Socle pour tous les modes :** `ACTION/STATUS` et `ACTION/PRECONDITION`, dès que le run écrit un "
     "statut, un gate ou un verdict (trace complète) ; `DIRECTION/CHARGE` reste la liste du démarrage.\n\n"
     "| Mode | Sections d’ACTION appelées par la route |"),
    ("A2-01c", "DIRECTION, déclencheurs critiques : quand ajouter une route à CHARGE", D,
     "### Déclencheurs critiques\n\n| Signal |",
     "### Déclencheurs critiques\n\nCes déclencheurs disent quand ajouter une route à la ligne du mode dans `DIRECTION/CHARGE` ; "
     "ils ne forment pas une seconde liste de chargement.\n\n| Signal |"),
    ("A2-01d", "DIRECTION, déclencheur « Détail final » : conditionnel", D,
     "`SAVOIR/CRAFT/CFT-03` (composition, densité et harmonie), `SAVOIR/STATE`, `SAVOIR/INTEGRITY` et capture rendue. | `[FORCÉ]` |",
     "`SAVOIR/CRAFT/CFT-03` (composition, densité et harmonie), `SAVOIR/STATE`, `SAVOIR/INTEGRITY` et capture rendue. | "
     "Conditionnel : colonne « Ajouter seulement si » de `DIRECTION/CHARGE` |"),
    ("A2-01e", "ACTION/ROUTING : renvoi à CHARGE", A,
     "DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui "
     "peuvent modifier la prochaine décision.",
     "DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui "
     "peuvent modifier la prochaine décision : elles s’ajoutent à la ligne du mode dans `DIRECTION/CHARGE` (colonne « Ajouter "
     "seulement si ») et ne forment pas une seconde liste."),
    ("A2-01f", "ACTION/ROUTING, spec DIRECTION : conditionnel", A,
     "| Spec `DIRECTION` | `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/SOURCE`, `SAVOIR/STYLE` si registre, `BIBLIOTHEQUE/SELECT` "
     "si structure ouverte. |",
     "| Spec `DIRECTION` | `SAVOIR/CRAFT`, `SAVOIR/TYPE` ou `SAVOIR/SOURCE` si la composition, la typographie ou l’ancrage "
     "restent ouverts, `SAVOIR/STYLE` si registre, `BIBLIOTHEQUE/SELECT` si structure ouverte. |"),
    ("A2-01g", "CHARGE, ligne DIRECTION : déclencheurs critiques absorbés", D,
     "Charge `SAVOIR/STYLE` seulement si le choix de style peut modifier une décision de composition, de voix, de matière, de "
     "contraste ou de relation produit ; jamais comme catalogue automatique. |",
     "Charge `SAVOIR/STYLE` seulement si le choix de style peut modifier une décision de composition, de voix, de matière, de "
     "contraste ou de relation produit ; jamais comme catalogue automatique. `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` ou "
     "`SAVOIR/INTEGRITY` si un détail final peut modifier le caractère, un état, la hiérarchie, la densité ou la robustesse ; "
     "`SAVOIR/INTEGRITY` avant un verdict (trace complète). |"),
    # AUD-02 — plancher SAVOIR compilé dans le noyau
    ("A2-02a", "SAVOIR/TYPE : bloc noyau COMP-TYPO", S,
     "\n[REQUIS PAR LE MODULE — lecture, ton, données, hiérarchie ou surface identitaire] Choisis une typographie pour ses langues, "
     "chiffres, ponctuation, graisses, lisibilité, licence, performance, fallback et ton.\n",
     "\n<!-- noyau:début COMP-TYPO -->\n[REQUIS PAR LE MODULE — lecture, ton, données, hiérarchie ou surface identitaire] Choisis "
     "une typographie pour ses langues, chiffres, ponctuation, graisses, lisibilité, licence, performance, fallback et ton.\n"
     "<!-- noyau:fin COMP-TYPO -->\n"),
    ("A2-02b", "SAVOIR/CRAFT/CFT-05 : bloc noyau COMP-COULEUR", S,
     "\n[REQUIS PAR LE MODULE — couleur, thème, statut ou surface identitaire] Conçois une palette par rôles",
     "\n<!-- noyau:début COMP-COULEUR -->\n[REQUIS PAR LE MODULE — couleur, thème, statut ou surface identitaire] Conçois une "
     "palette par rôles"),
    ("A2-02c", "SAVOIR/CRAFT/CFT-05 : fin du bloc COMP-COULEUR", S,
     "un indice non chromatique pour toute information critique tiennent. Une couleur sémantique n’est pas une décoration.\n",
     "un indice non chromatique pour toute information critique tiennent. Une couleur sémantique n’est pas une décoration.\n"
     "<!-- noyau:fin COMP-COULEUR -->\n"),
    ("A2-02d", "SAVOIR/READ : plancher dans le noyau", S,
     "il n’impose pas de charger toute la bibliothèque, mais d’exécuter ou de tracer honnêtement le contrôle concerné selon le "
     "contrat d’ACTION.",
     "il n’impose pas de charger toute la bibliothèque, mais d’exécuter ou de tracer honnêtement le contrôle concerné selon le "
     "contrat d’ACTION. Sur le chemin d’un run, le plancher de ces obligations est compilé dans le noyau de la skill "
     "(composition, typographie, couleur, états, vérité) ; leur détail s’applique lorsque la route est chargée."),
    # AUD-05 — lieu de la trace légère
    ("A2-05", "TRA-01 (noyau) : lieu de la trace légère", A,
     "défaut dominant restant ; prochaine preuve. Les planchers s’appliquent pendant la fabrication",
     "défaut dominant restant ; prochaine preuve. Elle s’écrit à côté de l’artefact quand l’agent écrit des fichiers (fichier de "
     "trace ou en-tête du fichier livré) ; sinon, après la réponse visible, sous « Trace ». Les planchers s’appliquent pendant "
     "la fabrication"),
    ("A2-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Architecture du chargement (refonte, A2).** `DIRECTION/CHARGE` est la seule liste de chargement, compilée dans le noyau "
     "avec sa colonne « Ajouter seulement si » ; la carte de lecture d’ACTION, les déclencheurs critiques de DIRECTION et "
     "`ACTION/ROUTING` en sont des vues ; le plancher couleur et typographique de SAVOIR entre dans le noyau ; la trace légère "
     "s’écrit à côté de l’artefact, ou après la réponse visible sous « Trace ».\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {
    "A2-01a": "chargement par CHARGE", "A2-01b": "vue de CHARGE", "A2-01d": "déclencheurs critiques",
    "A2-01e": "ACTION/ROUTING", "A2-02d": "plancher dans le noyau", "A2-05": "trace légère : lieu",
}
EXTRA_MUTATIONS = [
    ("en-tête de chargement concurrent rétabli (ACTION)", A, "| Mode | Sections d’ACTION appelées par la route |",
     "| Mode | Chargement propre au mode |", "[CHG-05]"),
    ("colonne « Ajouter seulement si » retirée du noyau", "scripts/build_core.py", '("CHARGE-TABLE", "DIRECTION.md", None)',
     '("CHARGE-TABLE", "DIRECTION.md", (0, 1))', "noyau"),
    ("plancher couleur retiré du noyau", "scripts/build_core.py", '("COMP-COULEUR", "SAVOIR.md", None),\n', "", "noyau"),
    ("plancher typographique retiré de la section compilée", "skills/design-governance-practice/SKILL.md",
     "Choisis une typographie pour ses langues", "Choisis une police pour ses langues", "[CORE-01]"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
