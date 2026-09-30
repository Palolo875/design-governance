#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R8b : moyens de fabrication consolidés, PKG-01, enseignement transférable A08.

Décisions : owner, « Allons-y » (30-09-2026) sur le périmètre de `plans/Plan_V1.2_Suite_Reprise.md` §4 (R8b réorienté,
`V12R_14` addendum 2) et l'inventaire `audit/data/V12R/V12R_Inventaire_P2.md` (PKG-01, bloquant P2).
- PKG-01 : « traitement unique » et « une seule famille » deviennent des choix justifiés par la thèse (amendement §5).
- Carte des moyens (bloc noyau MOY-CARTE) : par couche, ce qu'elle permet, comment choisir, ce qui limite ; licence et
  conditions vérifiées pour chaque ressource retenue ; Fontshare décrit correctement ; performance mesurée, pas capturée.
- Enseignement transférable de l'atlas v0 (A08) : données d'exemple cohérentes entre elles, aucun chiffre sans référence.
Rapport : `V12R_15_R8b_MOYENS.md`. Usage : identique à `V12R_Patch_R5b1.py`.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

D, A, S, C = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md", "V1/official/CHANGELOG.md"
EX = "skills/design-governance-practice/references/examples.md"

FILE_REPLACE = {
    "scripts/validate_structure.py": ("f2acb99995d6559085dce262318f7aecbc2c06c35a881c325dda4e30d1df53e9",
                                      HERE / "V12R_Patch_R8b_fichiers" / "scripts" / "validate_structure.py"),
}

CARTE_OLD = (
    "[VEILLE 2026-09] **Carte des moyens par couche**, des sources et jamais des styles, droits vérifiés à chaque usage. "
    "Typographie : polices de la marque, Google Fonts, Fontshare. Icônes : une seule famille (par exemple Lucide, Phosphor). "
    "Composants : design system fourni, sinon bibliothèque éprouvée (par exemple shadcn, Radix). Photographie : client, banques "
    "sous licence (Wikimedia Commons, Unsplash). Illustration et 3D : commande, packs sous licence, génération dirigée avec "
    "références (`GÉNÉRÉ-DIRIGÉ`). Fichiers et marque : Figma ou kit de marque par connecteur. En HTML seul, les assets "
    "figuratifs et le contenu réel restent hors plafond (`FABRICATION`). À revoir avant 2027-03.")
CARTE_NEW = """[VEILLE 2026-09] **Carte des moyens par couche** : des sources, jamais des styles. Licence et conditions d’usage vérifiées pour chaque ressource retenue, au moment de l’intégrer ; le nom d’une plateforme ne vaut pas autorisation. Pour chaque couche : où chercher, comment choisir, ce qui limite.
- **Typographie :** polices de la marque ; Google Fonts (licences ouvertes, surtout SIL OFL) ; Fontshare (licence propre au service, gratuite sous conditions). Choisir par la voix et la donnée à porter ; vérifier chargement, graisses et glyphes (accents, chiffres) dans la cible.
- **Icônes :** une famille qui couvre les pictogrammes nécessaires (par exemple Lucide, Phosphor) ; poids, taille et sens accordés au texte ; mélanger des familles demande une raison visible.
- **Composants :** design system fourni, sinon bibliothèque éprouvée (par exemple shadcn, Radix) ; hors Web, les idiomes de la plateforme.
- **Données et objets de preuve :** contenu du client, sinon exemples marqués ; codables, donc au plafond sans intrant.
- **Texture et traitement :** CSS, SVG, canvas ; rendu inspecté sur capture, performance mesurée dans le runtime cible.
- **Photographie :** client (même au téléphone, en lumière du jour), banques sous licence (Wikimedia Commons, Unsplash).
- **Illustration et 3D :** commande, packs sous licence, génération dirigée avec références (`GÉNÉRÉ-DIRIGÉ`).
- **Fichiers et marque :** Figma ou kit de marque par connecteur.

Sans intrant ni route autorisée, les assets figuratifs et le contenu réel restent hors plafond (`FABRICATION`). À revoir avant 2027-03."""

ASSETS_OLD = (
    "**Traitement des assets moyens.** Quand les assets disponibles sont moyens (photos de téléphone, banque d’images), "
    "applique un traitement unique et cohérent — recadrage, étalonnage, duotone, grain ou trame — justifié par la thèse, plutôt "
    "que de les poser bruts ou de les remplacer par un dessin. Le traitement unifie la série ; il ne masque ni un droit inconnu, "
    "ni une image hors sujet.")
ASSETS_NEW = (
    "**Traitement des assets moyens.** Quand les assets disponibles sont moyens (photos de téléphone, banque d’images), choisis "
    "le traitement que justifie la thèse — recadrage, étalonnage, duotone, grain ou trame — plutôt que de les poser bruts ou de "
    "les remplacer par un dessin. Un traitement commun peut unifier une série disparate ; plusieurs traitements se justifient si "
    "leurs rôles sont distincts et lisibles. Vérifie sur capture la relation entre les images et la composition. Le traitement ne "
    "masque ni un droit inconnu, ni une image hors sujet.")

PREUVE_OLD = "un exemple ne devient jamais une preuve de client, de performance, de disponibilité, d’intégration, de sécurité ou de résultat réel.\n<!-- noyau:fin PREMIER-OBJET -->"
PREUVE_NEW = ("un exemple ne devient jamais une preuve de client, de performance, de disponibilité, d’intégration, de sécurité ou de résultat réel.\n\n"
              "<!-- concept:EXD-01 -->\n"
              "Les données d’exemple restent cohérentes entre elles : totaux, pourcentages, unités, dates et prix se recoupent. Un chiffre "
              "sans référence (« +32 % ») se situe (par rapport à quoi, sur quelle période) ou se retire.\n<!-- noyau:fin PREMIER-OBJET -->")

PATCH = [
    ("R8b-K1", "carte des moyens consolidée (MOY-01)", S, CARTE_OLD, CARTE_NEW),
    ("R8b-K2", "PKG-01 : traitement des assets moyens contextuel", S, ASSETS_OLD, ASSETS_NEW),
    ("R8b-K3", "PKG-01 : Gate C, geste C1", A,
     "un seul traitement pour les assets moyens ;", "un traitement justifié par la thèse pour les assets moyens ;"),
    ("R8b-K4", "PKG-01 : route de production", D,
     "un asset moyen reçoit un traitement unique et justifié (`SAVOIR`, section `DESIGN-ATLAS`), jamais un dessin de remplacement.",
     "un asset moyen reçoit le traitement que justifie la thèse (`SAVOIR`, section `DESIGN-ATLAS`), jamais un dessin de remplacement."),
    ("R8b-K5", "PKG-01 : exemple de la skill", EX,
     "photos du client moyennes, un seul traitement cohérent", "photos du client moyennes, traitement commun choisi pour unifier la série"),
    ("R8b-E1", "enseignement A08 : données d'exemple cohérentes (EXD-01)", D, PREUVE_OLD, PREUVE_NEW),
    ("R8b-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Moyens de fabrication (refonte, R8b).** Carte des moyens par couche consolidée (où chercher, comment choisir, ce qui "
     "limite ; licence vérifiée pour chaque ressource retenue) ; traitement des assets et famille d’icônes choisis selon la thèse, "
     "jamais universels ; données d’exemple cohérentes entre elles, aucun chiffre sans référence.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R8b-K1": "résumé infidèle (carte des moyens)",
    "R8b-K2": "vocabulaire retiré",
    "R8b-K3": "vocabulaire retiré",
    "R8b-K4": "vocabulaire retiré",
    "R8b-K5": "vocabulaire retiré",
    "R8b-E1": "EXD-01 absent",
}
EXTRA_MUTATIONS = []


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
