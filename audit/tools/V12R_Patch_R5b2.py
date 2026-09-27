#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R5b-2 : ACTION restructurée (Gate A par profil, Gate C en gestes, boucle unique,
promesse du validateur unique).

Plan : `plans/Plan_V1.2_Refonte.md`, lot R5b ; consigne de l'owner (27-09-2026) : la qualité du résultat prime sur
le nombre de mots ; on ne retire que les doublons et le texte sans effet sur le rendu. Rapport : `V12R_07_R5b2_ACTION.md`.
Usage :
  python3 V12R_Patch_R5b2.py <racine>                 # applique, puis recompile le noyau (scripts/build_core.py)
  python3 V12R_Patch_R5b2.py <racine> --verifier      # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12R_Patch_R5b2.py <racine> --mutations     # sur une racine patchée : chaque garde rougit sous sa mutation
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402  (mécanique commune : apply_all, mutations, build_core)

A, C = "V1/official/ACTION.md", "V1/official/CHANGELOG.md"
RM, MP = "README.md", "skills/design-governance-practice/references/machine_projection.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("fb7c51ee05978bfef6e31319c2c4b21740d4ece7ad8d923c2ea13c8d7b36f87c",
                                      HERE / "V12R_Patch_R5b2_fichiers" / "scripts" / "validate_structure.py"),
}

PROMESSE_OLD = (
    "**Ce qu’atteste une `RUN_CARD` validée :** la forme de la projection et les invariants de la liste close (états, issues, "
    "verdicts et leur temps, axes, protection critique, exception, capacité et version de la preuve, réserves, droits déclarés, "
    "ancres, conséquence décisionnelle, reclassement, paquet SYSTÈME, B1b, trace par mode). **Ce qu’elle n’atteste pas (forme "
    "seule) :** que les observations ont réellement eu lieu ; la justesse des jugements V/U/A/T ; l’étendue réelle d’un claim "
    "(tâche utilisateur, technologie d’assistance, périmètre de diffusion) ; l’identité de la personne qui autorise ; la réalité "
    "des droits, licences et données ; la fraîcheur d’une ancre, dont seule la date ISO est contrôlée ; la qualité perceptuelle. "
    "Par mode : pour `LITE`, `ITER` et `STANDARD`, le paquet de clôture vit dans la trace et la machine ne le vérifie pas ; pour "
    "tous les modes, elle ne vérifie ni que les consumers listés sont tous les consumers réels, ni que la baseline montre ce "
    "qu’elle prétend, ni que la décision couverte par une paire équivalente est bien la même. Ces points restent à la trace, à la "
    "revue et à l’owner.")
PROMESSE_RENVOI = (
    "Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close ; elle n’atteste ni la réalité "
    "des observations, ni la justesse des jugements, ni la qualité perceptuelle. La liste exacte vit en un seul lieu : la "
    "frontière de validation d’`ACTION/RUN_CARD`.")

PARCOURS_OLD = """### Parcours minimal en cinq minutes

1. Reprends le mode et le risque classés dans `DIRECTION/START`.
2. Formule `DECISION-INTENT`, déclare l’artefact, le scope, les capacités et la prochaine preuve ; pour une décision visuelle ouverte, active `DIRECTION/CREATIVE-BOOT` avant le build.
3. Construis un premier rendu suffisamment complet et jugeable pour le mode ; lorsque la décision visuelle est ouverte, il doit déjà être composé, crédible, spécifique et résolu à la bonne échelle, et rendre observables l’objet, la tension et les cibles créatives du boot.
4. Observe le rendu réel sans laisser la rationale remplacer l’objet ; inscris l’interprétation, les qualités prioritaires effectivement visibles ou non observées, le défaut dominant et la limite.
5. Corrige, résous, retourne, réserve ou accepte ; persiste `DECISION-CHANGE`, la preuve, l’owner et la prochaine action.

Ce parcours est une façade de lecture, non une procédure concurrente. Les contrats détaillés, les gates et les conditions de clôture restent applicables dès que le risque ou le mode les déclenche."""
PARCOURS_NEW = """### Parcours minimal

Le parcours d’un run est celui du noyau de la skill : classer et charger (`DIRECTION/CHARGE`), prendre le brief, construire une première scène complète, boucler (`DIRECTION/DOUBLE-LOOP`), répondre et tracer (`ACTION/HANDOFF`). ACTION en porte les preuves, les gates et, en trace complète, la clôture ; ses contrats restent applicables dès que le risque ou le mode les déclenche."""

PROFILS = """| Authentification accessible | Le processus n’impose pas une charge cognitive ou sensorielle évitable. | Mémoire, perception ou interaction imposée sans alternative. |

<!-- concept:GTA-01 -->
**Profils de surface.** Commence par les contrôles d’office du profil ; un contrôle hors profil devient applicable dès que la surface porte l’élément concerné (formulaire, glisser, motion, connexion). Ce que le médium ne porte pas est `N/A-JUSTIFIED`.

| Profil | Contrôles d’office | Selon le contenu |
|---|---|---|
| Page vitrine, éditoriale ou portfolio | Contraste, sémantique et nom accessible, focus clavier, information non chromatique, cibles d’interaction, contenu honnête, stabilité média. | États (formulaire, commande), motion réduite, mouvement de glisser, focus non masqué. |
| Application, formulaire ou flow | Tous les contrôles d’interface : contraste, sémantique, focus clavier et non masqué, états, cibles, information non chromatique, saisie redondante, aide cohérente, contenu honnête. | Authentification accessible (connexion), motion réduite, mouvement de glisser, stabilité média. |
| Scène, motion ou 3D | Motion réduite, contraste, information non chromatique, stabilité média, contenu honnête. | Focus clavier et cibles si la scène est interactive. |
| Hors Web (imprimé, affiche, écran fixe) | Contraste ou lisibilité d’encre, information non chromatique, contenu honnête. | Référentiel du médium, déclaré dans `CONFORMANCE-TARGET`. |"""

GATE_C = [
    ("| Critère | Présent si… | Retour ou réserve si… |\n|---|---|---|\n| **C1",
     "| Critère | Présent si… | Retour ou réserve si… | Geste si absent (noyau, §) |\n|---|---|---|---|\n| **C1"),
    ("| Traitement par défaut sans relation observable. |",
     "| Traitement par défaut sans relation observable. | Choisis la surface d’après ce que le produit montre (carte des moyens, §6) ; "
     "un seul traitement pour les assets moyens ; retire le traitement sans rôle. |"),
    ("| Choix par défaut non interrogé ou non calibré. |",
     "| Choix par défaut non interrogé ou non calibré. | Choisis la famille pour la voix et la donnée à porter (§6) ; fixe deux ou "
     "trois rôles et une échelle contrastée ; vérifie le fallback au rendu. |"),
    ("| Empilement uniforme sans décision spatiale. |",
     "| Empilement uniforme sans décision spatiale. | Recompose dans l’ordre intention → foyer → masse → rythme (§5) ; nomme le "
     "foyer et l’ordre de lecture ; romps la trame modale si elle ne sert pas la tâche (§4). |"),
    ("| Espacement uniforme qui masque les relations. |",
     "| Espacement uniforme qui masque les relations. | Regroupe par proximité ; redistribue masses et vides selon la priorité "
     "(masse visuelle, gestion du vide, §5) ; contrôle la silhouette à faible détail. |"),
    ("`N/A-JUSTIFIED` si la planéité est intentionnelle et suffisante. |",
     "`N/A-JUSTIFIED` si la planéité est intentionnelle et suffisante. | Tiens une seule logique, lumière, élévation ou planéité, "
     "sur toute la surface ; retire ombres, bordures et flous sans rôle (surface, §5). |"),
    ("| Assemblage de composants sans adaptation au cas. |",
     "| Assemblage de composants sans adaptation au cas. | Trouve la difficulté réelle du cas (attente, erreur, donnée, choix) et "
     "résous-la par microcopie, état, donnée ou interaction (forme située, §5). |"),
]

PATCH = [
    # ---------- Gate A par profil de surface ----------
    ("R5b2-A1", "Gate A : profils de surface", A,
     "| Authentification accessible | Le processus n’impose pas une charge cognitive ou sensorielle évitable. | Mémoire, perception "
     "ou interaction imposée sans alternative. |", PROFILS),
    ("R5b2-A2", "trace légère : Gate A selon le profil", A,
     "(vérité, `ACTION/GATE-A`, boucle d’édition)", "(vérité, `ACTION/GATE-A` selon le profil de surface, boucle d’édition)"),
    # ---------- Gate C en gestes ----------
    *[(f"R5b2-C{i}", "Gate C : geste si absent", A, old, new) for i, (old, new) in enumerate(GATE_C)],
    ("R5b2-C7", "Gate C en trace légère", A,
     "elle n’ajoute pas un effet décoratif terminal.\n\n---\n\n## ACTION/ANTI-SLOP",
     "elle n’ajoute pas un effet décoratif terminal.\n\nEn trace légère, Gate C sert de contrôle de craft sur la capture, dans la "
     "boucle d’édition : un critère absent déclenche son geste, puis une nouvelle capture ; aucun verdict n’est écrit.\n\n---\n\n"
     "## ACTION/ANTI-SLOP"),
    # ---------- Boucle : une seule description (DIRECTION/DOUBLE-LOOP) ----------
    ("R5b2-B1", "boucle : chemin positif d'ACTION", A,
     "Son chemin positif est **construire → observer → isoler le défaut dominant → corriger ou accepter avec raison → prouver → "
     "clôturer avec une limite et une prochaine preuve**.",
     "Son chemin positif est la boucle d’édition (`DIRECTION/DOUBLE-LOOP`), prolongée par la preuve et, en trace complète, par une "
     "clôture avec une limite et une prochaine preuve."),
    ("R5b2-B2", "boucle : parcours minimal", A, PARCOURS_OLD, PARCOURS_NEW),
    ("R5b2-B3", "boucle : trois niveaux", A,
     "`DIRECTION/DOUBLE-LOOP` décrit la boucle de décision créative et d’apprentissage : observer, isoler, modifier, réobserver et "
     "décider.",
     "`DIRECTION/DOUBLE-LOOP` décrit la boucle d’édition, seule description de la boucle (copiée dans le noyau)."),
    ("R5b2-B4", "boucle : séquence de référence du pipeline", A,
     "Pour tout run qui produit un rendu, la séquence de référence est : **préparer la qualité attendue → construire un premier "
     "rendu complet → observer le rendu réel sans se laisser guider par la rationale → isoler le défaut dominant → corriger "
     "l’artefact ou la décision → réobserver → comparer l’effet → clôturer ou retourner**. La correction doit changer une relation "
     "visible, une tâche, une preuve, une contrainte ou une propriété de robustesse ; une nouvelle explication ne constitue pas une "
     "correction.",
     "Pour tout run qui produit un rendu, la boucle est celle de `DIRECTION/DOUBLE-LOOP` ; ce pipeline en exécute la préparation, "
     "la preuve, puis la clôture ou le retour. Observe le rendu réel sans te laisser guider par la rationale."),
    # ---------- Promesse du validateur : un seul texte ----------
    ("R5b2-V1", "promesse : lieu propriétaire balisé", A,
     "\n" + PROMESSE_OLD, "\n<!-- concept:VAL-01 -->\n" + PROMESSE_OLD),
    ("R5b2-V2", "promesse : renvoi depuis le README", RM, PROMESSE_OLD, PROMESSE_RENVOI),
    ("R5b2-V3", "promesse : renvoi depuis la projection machine", MP, PROMESSE_OLD, PROMESSE_RENVOI),
    # ---------- Historique ----------
    ("R5b2-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **ACTION restructurée (refonte, R5b-2).** Gate A par profil de surface (contrôles d’office et selon le contenu) ; Gate C "
     "relie chaque critère à son geste de correction dans le noyau et sert, en trace légère, de contrôle de craft sans verdict ; "
     "une seule description de la boucle (`DIRECTION/DOUBLE-LOOP`) ; promesse du validateur tenue en un seul lieu "
     "(`ACTION/RUN_CARD`). Schéma `RUN_CARD` inchangé.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R5b2-A1": "GTA-01 absent",
    "R5b2-V1": "VAL-01 absent",
    "R5b2-V2": "vocabulaire retiré",
    "R5b2-V3": "vocabulaire retiré",
    "R5b2-B1": "vocabulaire retiré",
    "R5b2-B3": "vocabulaire retiré",
    "R5b2-B4": "vocabulaire retiré",
}

EXTRA_MUTATIONS = [
    ("carte d'ACTION : Gate B hors trace complète", A,
     "`ACTION/GATE-A`, `ACTION/GATE-C` ; `ACTION/GATE-B` en trace complète (`ACTION/HANDOFF`) |",
     "`ACTION/GATE-A`, `ACTION/GATE-B`, `ACTION/GATE-C` |", "[CHG-09]"),
]


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
