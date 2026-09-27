#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION lot 2 : chantiers G, H, I, D' (addendum « niveau senior »), textes exacts exécutables.

Artefact HORS package, sur le modèle de V12_Patch_ABD.py. S'applique sur B05 APRÈS le lot 1 (A, B, D).
Usage :
  python3 V12_Patch_Lot2.py <racine>                # applique le lot 2
  python3 V12_Patch_Lot2.py <racine> --verifier     # vérifie que chaque ancien texte est présent une fois
  python3 V12_Patch_Lot2.py <racine> --inverse ID   # remet l'ancien texte d'une entrée
  python3 V12_Patch_Lot2.py <racine> --mutations    # sur une racine patchée : LCF-46 à 50 rougissent sous mutation

Chantiers : G (objet de preuve codé, de préférence), H (carte des moyens par couche, [VEILLE]),
I (traitement des assets moyens, SAVOIR section DESIGN-ATLAS), D' (vague 3 datée), C- (coupes de doublons pour le budget).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from V12_Patch_ABD import apply  # noqa: E402

D = "V1/official/DIRECTION.md"
S = "V1/official/SAVOIR.md"
C = "V1/official/CHANGELOG.md"
SK = "skills/design-governance-practice/SKILL.md"
RM = "scripts/validate_reading_map.py"

PATCH: list[tuple[str, str, str, str, str]] = [
    # ---------- G : objet de preuve codé, de préférence ----------
    ("L2-G1", "G", D,
     "L’objet arrive avant les bénéfices et rend le mécanisme plus clair que le texte seul.",
     "L’objet arrive avant les bénéfices et rend le mécanisme plus clair que le texte seul ; il est de préférence **codé** "
     "(composant, donnée, état ou interaction du produit), une illustration ne le portant que fournie, curatée ou générée dirigée."),
    ("L2-G2", "G", SK,
     "Charger `ACTION/FIRST-RENDER` pour le contrat de qualité initiale du premier rendu.",
     "Charger `ACTION/FIRST-RENDER` pour le contrat de qualité initiale du premier rendu. L’objet de preuve est de préférence "
     "codé (composant, donnée, état, interaction)."),
    # ---------- H : carte des moyens par couche ----------
    ("L2-H1", "H", S,
     "système. À revoir avant 2027-03.\n",
     "système. À revoir avant 2027-03.\n\n"
     "[VEILLE 2026-09] **Carte des moyens par couche**, des sources et jamais des styles, droits vérifiés à chaque usage. "
     "Typographie : polices de la marque, Google Fonts, Fontshare. Icônes : une seule famille (par exemple Lucide, Phosphor). "
     "Composants : design system fourni, sinon bibliothèque éprouvée (par exemple shadcn, Radix). Photographie : client, banques "
     "sous licence (Wikimedia Commons, Unsplash). Illustration et 3D : commande, packs sous licence, génération dirigée avec "
     "références (`GÉNÉRÉ-DIRIGÉ`). Fichiers et marque : Figma ou kit de marque par connecteur. En HTML seul, les assets "
     "figuratifs et le contenu réel restent hors plafond (`FABRICATION`). À revoir avant 2027-03.\n"),
    ("L2-V1", "H+I", D,
     "augmente la preuve, la compréhension ou la singularité de la surface.",
     "augmente la preuve, la compréhension ou la singularité de la surface. Sources par couche : carte des moyens (`SAVOIR`, "
     "`[VEILLE]`) ; un asset moyen reçoit un traitement unique et justifié (`SAVOIR`, section `DESIGN-ATLAS`), jamais un dessin de "
     "remplacement."),
    # ---------- I : traitement des assets moyens ----------
    ("L2-I1", "I", S,
     "`DÉCORATIF-SANS-CONSEQUENCE` est une catégorie de retrait, jamais une technique à promouvoir.",
     "`DÉCORATIF-SANS-CONSEQUENCE` est une catégorie de retrait, jamais une technique à promouvoir.\n\n"
     "**Traitement des assets moyens.** Quand les assets disponibles sont moyens (photos de téléphone, banque d’images), "
     "applique un traitement unique et cohérent — recadrage, étalonnage, duotone, grain ou trame — justifié par la thèse, plutôt "
     "que de les poser bruts ou de les remplacer par un dessin. Le traitement unifie la série ; il ne masque ni un droit inconnu, "
     "ni une image hors sujet."),
    # ---------- D' : vague 3 datée ----------
    ("L2-D1", "D'", S,
     "illustration peinte, tramage. Source : épreuve de référence interne V1.2 (26-09-2026)",
     "illustration peinte, tramage. Vague 3 : dithering, logos pixel, ASCII, hachures de plan, gravures, bleu Klein, libellés "
     "mono en capitales, repères de recadrage, paysage peint en fond. Source : épreuve de référence interne V1.2 (26-09-2026) et "
     "revue de références de designers (27-09-2026)"),
    # ---------- C- : coupes de doublons (budget de lecture) ----------
    ("L2-C1", "C-", D,
     "Cette vue compacte référence `RUN-PRIORITY`, `VISUAL_TARGET` et `DIRECTION-ATELIER` ; elle ne recopie ni leurs champs, ni "
     "une seconde trace. Lorsqu’ils peuvent modifier",
     "Lorsque `RUN-PRIORITY`, `VISUAL_TARGET` ou `DIRECTION-ATELIER` peuvent modifier"),
    ("L2-C2", "C-", D,
     "La colonne « Dimension CFT-00 » relie chaque dimension à la revue définie par `SAVOIR/CRAFT/CFT-00`. La vérité de scène",
     "La vérité de scène"),
    ("L2-C3", "C-", SK,
     "retenue et résolution. Distinguer une direction artistique située, un craft construit, un polish résolu, une créativité "
     "pertinente et un goût situé ; aucune de ces qualités ne devient un score ou un verdict automatique.",
     "retenue et résolution."),
    ("L2-C4", "C-", SK,
     "et que la prochaine action est définie. Ne remplis jamais un quota de variantes ou de finition pour satisfaire la procédure.",
     "et que la prochaine action est définie."),
    # ---------- CHANGELOG (section « Non publié ») ----------
    ("L2-CH1", "CHANGELOG", C,
     "- **Validateur de carte.** La liste close des conditions de façade passe de 42 à 46 conditions (LCF-43 à LCF-46).\n",
     "- **Niveau senior (lot 2).** Objet de preuve codé de préférence (`DIRECTION/FIRST-OBJECT`) ; carte des moyens par couche et "
     "vague 3 datées (`SAVOIR`, `[VEILLE 2026-09]`) ; traitement des assets moyens (`SAVOIR`, section `DESIGN-ATLAS`).\n"
     "- **Validateur de carte.** La liste close des conditions de façade passe de 42 à 50 conditions (LCF-43 à LCF-50) ; "
     "LCF-46 couvre aussi la vague 3.\n"),
]

# ---------- Gardes : extension de LCF-46 et LCF-47 à LCF-50 ----------
LCF_CODE = r'''
# ---------- V1.2 lot 2 (G, H, I, D') : LCF-47 à LCF-50 ----------
def savoir_section(t: dict[str, str], start: str, stop: str) -> str:
    return t["S"][t["S"].find(start):t["S"].find(stop)]


def lcf_47(t: dict[str, str]) -> bool:
    fo = t["D"][t["D"].find("## DIRECTION/FIRST-OBJECT"):t["D"].find("### Contrat positif du premier objet")]
    return "de préférence **codé**" in fo and "de préférence codé" in t["SK"]


def lcf_48(t: dict[str, str]) -> bool:
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    carte = [l for l in t["S"].splitlines() if l.startswith("[VEILLE 20") and "Carte des moyens par couche" in l]
    return bool(carte) and "jamais des styles" in carte[0] and "carte des moyens" in vt


def lcf_49(t: dict[str, str]) -> bool:
    atlas = savoir_section(t, "# SAVOIR/DESIGN-ATLAS", "# SAVOIR/STYLE")
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    return "**Traitement des assets moyens.**" in atlas and "jamais un dessin de remplacement" in vt


def lcf_50(t: dict[str, str]) -> bool:
    return any(l.startswith("[VEILLE 20") and "Vague 3 :" in l for l in t["S"].splitlines())

'''

LCF_ROWS = '''        ("LCF-47", "FIRST-OBJECT et skill : objet de preuve codé, de préférence", "DIRECTION/FIRST-OBJECT ; V1.2-G", lcf_47(t)),
        ("LCF-48", "SAVOIR ([VEILLE] daté) et route de production : carte des moyens", "SAVOIR ([VEILLE]) ; V1.2-H", lcf_48(t)),
        ("LCF-49", "SAVOIR (DESIGN-ATLAS) et route de production : traitement des assets moyens", "SAVOIR (DESIGN-ATLAS) ; V1.2-I", lcf_49(t)),
        ("LCF-50", "SAVOIR, [VEILLE] daté : vague 3", "SAVOIR ([VEILLE]) ; V1.2-D'", lcf_50(t)),
'''

PATCH += [
    ("L2-R1", "LCF", RM,
     'WAVE_MARKERS = re.compile(r"hero SaaS|gradient décoratif|\\bviolet\\b|\\bInter\\b|\\bhalos?\\b|\\bbeige\\b|\\bcrème\\b|serif italique|"\n'
     '                          r"orange rouille|bandeau défilant|illustration peinte|\\btramage\\b")\n',
     'WAVE_MARKERS = re.compile(r"hero SaaS|gradient décoratif|\\bviolet\\b|\\bInter\\b|\\bhalos?\\b|\\bbeige\\b|\\bcrème\\b|serif italique|"\n'
     '                          r"orange rouille|bandeau défilant|illustration peinte|\\btramage\\b|"\n'
     '                          r"\\bdithering\\b|logos? pixel|\\bASCII\\b|hachures de plan|bleu Klein|paysage peint")\n'),
    ("L2-L1", "LCF", RM, "\ndef check_facades(errors: list[str]) -> None:\n", LCF_CODE + "\ndef check_facades(errors: list[str]) -> None:\n"),
    ("L2-L2", "LCF", RM,
     '        ("LCF-46", "textes et façades : marqueurs de vague seulement en [VEILLE] daté", "SAVOIR ([VEILLE] daté) ; V1.2-D", lcf_46(t)),\n',
     '        ("LCF-46", "textes et façades : marqueurs de vague seulement en [VEILLE] daté", "SAVOIR ([VEILLE] daté) ; V1.2-D", lcf_46(t)),\n'
     + LCF_ROWS),
]

# Entrée dont l'inverse sert de mutation pour chaque condition nouvelle ou étendue
MUTATION_OF = {"LCF-47": "L2-G1", "LCF-48": "L2-H1", "LCF-49": "L2-I1", "LCF-50": "L2-D1"}
# LCF-46 étendue : mutation par injection d'un marqueur de vague 3 hors [VEILLE]
MARKER_MUTATION = ("LCF-46", D, "## DIRECTION/FIRST-OBJECT", "## DIRECTION/FIRST-OBJECT\n\nFond en dithering bleu Klein.\n")


def run_map(root: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(root / "scripts" / "validate_reading_map.py")],
                         capture_output=True, text=True, cwd=root)
    return out.returncode, out.stdout + out.stderr


def copy_of(root: Path, tmp: str) -> Path:
    dst = Path(tmp) / "pkg"
    shutil.copytree(root, dst, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
    return dst


def mutations(root: Path) -> int:
    bad = 0
    for lcf, pid in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            cp = copy_of(root, tmp)
            problems = apply(cp, [e for e in PATCH if e[0] == pid], reverse=True)
            rc, text = run_map(cp)
            red = rc != 0 and f"{lcf} :" in text
            print(f"{lcf} sous inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'}{' ; ' + '; '.join(problems) if problems else ''}")
            bad += 0 if red and not problems else 1
    lcf, rel, old, new = MARKER_MUTATION
    with tempfile.TemporaryDirectory() as tmp:
        cp = copy_of(root, tmp)
        problems = apply(cp, [("M", "mut", rel, old, new)])
        rc, text = run_map(cp)
        red = rc != 0 and f"{lcf} :" in text
        print(f"{lcf} sous injection d'un marqueur de vague 3 : {'ROUGE' if red else 'NON ROUGE'}")
        bad += 0 if red and not problems else 1
    return bad


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    if "--mutations" in sys.argv:
        return 1 if mutations(root) else 0
    if "--inverse" in sys.argv:
        pid = sys.argv[sys.argv.index("--inverse") + 1]
        problems = apply(root, [e for e in PATCH if e[0] == pid], reverse=True)
    else:
        problems = apply(root, PATCH, dry="--verifier" in sys.argv)
    for p in problems:
        print("ÉCHEC", p)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH) if '--inverse' not in sys.argv else 1} entrée(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
