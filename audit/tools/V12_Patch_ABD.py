#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION A, B, D : textes cibles exacts, sous forme exécutable.

Artefact HORS package, sur le modèle de DG_AUDIT_001_Patch_R01.py.
Chaque entrée remplace UNE occurrence exacte (sinon arrêt, rien n'est écrit).
Usage :
  python3 V12_Patch_ABD.py <racine>                # applique le patch (sur B05 en G3 ; jamais sur B01 à B04)
  python3 V12_Patch_ABD.py <racine> --verifier     # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12_Patch_ABD.py <racine> --inverse ID   # remet l'ancien texte d'une entrée (mutation des gardes)
  python3 V12_Patch_ABD.py <racine> --mutations    # sur une racine patchée : chaque LCF-43 à 46 rougit sous sa mutation

Chantiers : A (bilan de fabrication), B (prise de brief minimale), D (anti-slop vivant),
et C- (coupes de budget, décidées au titre de la contrainte « réduire le budget de lecture »).
Le patch ne touche ni la version, ni le CHANGELOG, ni les notes de version : ils sont écrits en G3.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

A = "V1/official/ACTION.md"
D = "V1/official/DIRECTION.md"
Q = "V1/official/QUICKSTART.md"
S = "V1/official/SAVOIR.md"
SK = "skills/design-governance-practice/SKILL.md"
EX = "skills/design-governance-practice/references/examples.md"
RM = "scripts/validate_reading_map.py"

# (ID, chantier, fichier, ancien texte exact, nouveau texte)
PATCH: list[tuple[str, str, str, str, str]] = [
    # ---------- A : bilan de fabrication ----------
    ("P-A1", "A", D,
     "CONSTRAINT — contrainte réelle qui peut changer la décision\n",
     "CONSTRAINT — contrainte réelle qui peut changer la décision, dont la destination (démo, prototype ou produit réel) et "
     "l’enjeu identitaire\n"),
    ("P-A2", "A", D,
     "ANCHOR-BASIS: référence observée, contrainte produit, hypothèse générée ou système hérité\n"
     "ANCHOR-LIMIT: ce que cette base ne permet pas d’affirmer\n",
     "FABRICATION: moyens réels (assets, marque, polices, composants, génération, sources, contenu) → plafond par couche "
     "(structure, typo, couleur, assets, contenu) → construire, construire avec plafond déclaré, demander X ou changer de route ; "
     "inclut la base de l’ancre et ce qu’elle ne permet pas d’affirmer\n"),
    ("P-A3", "A", D,
     "jamais à un wireframe volontairement creux lorsque les capacités sont disponibles. ",
     "jamais à un wireframe volontairement creux lorsque les capacités sont disponibles ; lorsqu’elles manquent, `FABRICATION` "
     "déclare le plafond avant le build et le rendu sort avec la meilleure route de `DIRECTION/VISUAL_TARGET`. "),
    ("P-A4", "A", D,
     "Ce n’est ni un statut, ni un classement de qualité, ni une préférence d’outil : c’est une réponse située au rôle de l’asset, "
     "aux droits, au délai, à la performance et au niveau de singularité attendu.",
     "Ce n’est ni un statut, ni une préférence d’outil : c’est une réponse située au rôle de l’asset, aux droits, au délai et à la "
     "**destination**. En produit réel, un asset manquant devient une route `CODE-NATIVE` ou `SANS-ASSET` ou un emplacement marqué, "
     "jamais un faux asset ; en démo, une approximation marquée illustrative ; un contenu absent, un emplacement illustratif."),
    ("P-A5", "A", A,
     "Toute capacité qui soutient un claim ajoute sa `BASIS` : résultat d’outil, environnement attesté, source utilisateur ou "
     "déclaration non attestée.",
     "Toute capacité qui soutient un claim ajoute sa `BASIS` : résultat d’outil, environnement attesté, source utilisateur ou "
     "déclaration non attestée. Le profil décrit l’**observation** ; ce que le run peut **fabriquer** relève du bilan `FABRICATION` "
     "de `DIRECTION/CREATIVE-BOOT`, en trace."),
    ("P-A6", "A", A,
     "ce statut ne justifie pas un artefact volontairement creux lorsque les capacités nécessaires sont disponibles.",
     "ce statut ne justifie pas un artefact volontairement creux lorsque les capacités nécessaires sont disponibles ; sinon, "
     "plafond déclaré avant le build (`FABRICATION`)."),
    # ---------- B : prise de brief minimale ----------
    ("P-B1", "B", D,
     "La personne reçoit directement une proposition principale ; cette vue reste interne.",
     "**Prise de brief.** Au plus trois demandes, en un seul échange, par gain de plafond : contenu réel (textes, chiffres, "
     "preuves, noms), marque, asset principal ou route autorisée, destination si elle n’est pas évidente. Brief riche : aucune. "
     "Humain absent : hypothèses nommées, plafond déclaré, demandes listées à la livraison. Le rendu est construit dans tous les cas. "
     "La personne reçoit directement une proposition principale ; cette vue reste interne."),
    ("P-B2", "B", Q,
     "Le boot est une vue de cadrage, pas un nouveau formulaire ou une obligation pour les deltas locaux ; il doit modifier la "
     "construction ou rester omis.",
     "Le boot est une vue de cadrage, pas un nouveau formulaire ou une obligation pour les deltas locaux ; il doit modifier la "
     "construction ou rester omis. Sur brief vague, la prise de brief de `DIRECTION/EXTERNAL-START` demande au plus trois intrants, "
     "dans cet ordre : contenu réel, marque, asset principal, destination ; le rendu est construit dans tous les cas."),
    ("P-B3", "B", SK,
     "Omettre ou condenser le boot pour un delta strictement local lorsque ces décisions ne changent pas.",
     "Omettre ou condenser le boot pour un delta strictement local lorsque ces décisions ne changent pas. Sur brief vague, demander "
     "au plus trois intrants, dans cet ordre : contenu réel, marque, asset principal, destination (`DIRECTION/EXTERNAL-START`) ; "
     "construire dans tous les cas."),
    # ---------- D : anti-slop vivant ----------
    ("P-D1", "D", D,
     "ANTI-DIRECTIONS: patterns visuels concrets à ne pas reproduire\n",
     "MODAL: ce que n’importe quelle IA produirait ici (structure, palette, typo, assets)\n"
     "PARTI: garder ou s’écarter — où et pourquoi au regard de la thèse ; projeté dans `direction.anti_direction`\n"),
    ("P-D2", "D", D,
     "`DIRECTION` possède la promesse, l’objet, le geste et les anti-directions ;",
     "`DIRECTION` possède la promesse, l’objet, le geste, `MODAL`/`PARTI` et `FABRICATION` ;"),
    ("P-D3", "D", D,
     "| Promesse, objet de preuve, geste, anti-directions et défaut recherché |",
     "| Promesse, objet de preuve, geste, `MODAL`/`PARTI`, `FABRICATION` et défaut recherché |"),
    ("P-D4", "D", Q,
     "`SAVOIR/CRAFT`, la base et la limite de l’ancre, le premier objet et le défaut dominant.",
     "`SAVOIR/CRAFT`, `MODAL`/`PARTI` (d’où viennent les anti-directions), bilan de fabrication (`FABRICATION`), le premier objet "
     "et le défaut dominant."),
    ("P-D5", "D", Q,
     "| Creative Boot : promesse, objet, geste, anti-directions, tension, signature, cibles CFT et premier objet. |",
     "| Creative Boot : promesse, objet, geste, modal et parti, tension, signature, cibles CFT, fabrication et premier objet. |"),
    ("P-D6", "D", SK,
     "`SAVOIR/CRAFT`, base et limite de l’ancre, premier objet et défaut dominant.",
     "`SAVOIR/CRAFT`, `MODAL`/`PARTI` (d’où viennent les anti-directions), bilan de fabrication (`FABRICATION`), premier objet et "
     "défaut dominant."),
    ("P-D7", "D", Q,
     "Thèse : une entrée éditoriale dense mais lisible, où un objet visuel propriétaire\n"
     "porte la promesse au lieu d’un hero générique.\n"
     "Anti-direction : hero SaaS interchangeable avec gradient décoratif et cartes répétées.\n",
     "Thèse : la preuve du produit porte la première scène ; la promesse se lit\n"
     "avant le premier geste.\n"
     "Modal : titre centré, sous-titre, deux boutons, trois cartes de bénéfices.\n"
     "Parti : s’écarter pour la première scène seulement, où la preuve remplace le titre ;\n"
     "garder la structure attendue pour le reste de la page.\n"),
    ("P-D8", "D", EX,
     "ANTI-DIRECTION: carte plate à pins et hero centré interchangeable\n",
     "MODAL: carte plate à pins, titre centré, cartes de fonctionnalités\n"
     "PARTI: s’écarter de la carte à pins ; l’écoute par couches porte la scène\n"),
    ("P-D9", "D", S,
     "[VEILLE] Les listes de produits contemporains, tendances, registres culturels et snapshots ne sont pas neutres. Chaque élément "
     "mobilisé dans un run porte source, date, portée et limite dans sa trace locale.\n",
     "[VEILLE] Les listes de produits contemporains, tendances, registres culturels et snapshots ne sont pas neutres. Chaque élément "
     "mobilisé dans un run porte source, date, portée et limite dans sa trace locale.\n\n"
     "[VEILLE 2026-09] **Marqueurs de vague**, pour nommer `MODAL` (`DIRECTION/CREATIVE-BOOT`), jamais pour interdire : un marqueur "
     "gardé par décision reste valide. Vague 1 : violet, police Inter, halos et gradient décoratif, hero SaaS à cartes répétées. "
     "Vague 2 : fond beige ou crème, brun, serif de caractère ou serif italique, orange rouille, bandeau défilant, illustration "
     "peinte, tramage. Source : épreuve de référence interne V1.2 (26-09-2026), 6 rendus sur 6 sur fond crème et brun, avec ou sans "
     "système. À revoir avant 2027-03.\n"),
    # ---------- C- : coupes de budget (contrainte « réduire le budget de lecture ») ----------
    ("P-C1", "C-", D,
     " `ACTION` reste propriétaire de la preuve et de la clôture ; `SAVOIR` du jugement ; `BIBLIOTHEQUE` des structures. "
     "`DIRECTION-ATELIER`, `GROUNDING-DECISION`, `REUSE-CHALLENGE` et la section `DESIGN-ATLAS` de `SAVOIR.md` sont des modules "
     "indépendants : chacun n’est activé que si sa décision à modifier est identifiée ; plusieurs peuvent coexister seulement si "
     "leurs décisions sont distinctes et utiles.",
     " Propriétaires et modules : ordre de lecture minimal de `DIRECTION/START`."),
    ("P-C2", "C-", D,
     "Le Creative Boot est recommandé lorsque la décision visuelle est ouverte et peut rester condensé ou omis pour un delta "
     "strictement local. Sa valeur doit être jugée par la conséquence sur le premier objet et la décision, non par la complétude "
     "du formulaire.",
     "Sa valeur se juge à sa conséquence sur le premier objet, non à la complétude du formulaire ; il peut être omis pour un delta "
     "strictement local."),
    ("P-C3", "C-", SK,
     "Viser dès le premier rendu une proposition réellement présentable, distinctive et polie : scène complète plutôt que "
     "wireframe générique, assets et composants authored lorsqu’ils portent la décision, contenu crédible et états pertinents. "
     "Ne pas imposer un style par défaut ; imposer un niveau d’intention et de résolution.",
     "Viser dès le premier rendu le niveau d’`ACTION/FIRST-RENDER`, sans style par défaut."),
    ("P-C4", "C-", D,
     "ni champ obligatoire concurrent de `RUN_CARD`. C’est une vue de cadrage qui relie `DIRECTION` à `BIBLIOTHEQUE`, `SAVOIR` et "
     "`ACTION` afin que le jugement créatif puisse modifier la construction plutôt que commenter seulement le résultat.",
     "ni champ obligatoire concurrent de `RUN_CARD`."),
    ("P-C5", "C-", D,
     "(`DIRECTION/DOUBLE-LOOP`, one-shot). Une hypothèse générée peut orienter une exploration ; elle ne devient pas une ancre "
     "culturelle ou une preuve par simple déclaration.",
     "(`DIRECTION/DOUBLE-LOOP`, one-shot)."),
    ("P-C6", "C-", D,
     "Cette compilation est un ordre de travail sur les champs de la table, pas une seconde liste. Compile-les",
     "Compile-les"),
    ("P-C7", "C-", D,
     "Elle n’impose aucun profil ou style : les profils disponibles sont des hypothèses conditionnelles, et l’absence de profil est "
     "une sortie valide.",
     "Elle n’impose aucun profil ni style."),
    ("P-C8", "C-", SK,
     "pour la grille à 8 dimensions (présence, foyer, signature, intégration, résolution, désirabilité située, vérité de scène, "
     "résilience visible) et la compilation",
     "pour la grille à 8 dimensions et la compilation"),
    ("P-C9", "C-", D,
     "Une proposition de haute qualité n’est pas obtenue en ajoutant séparément une belle police, une image ou une texture. Elle "
     "apparaît lorsque la composition, le contenu, le type, l’objet de preuve, la matière ou sa retenue, les états et le "
     "comportement se renforcent mutuellement. Si l’un de ces éléments ne change aucune relation visible, retire-le ou nomme sa "
     "limite.",
     "La qualité ne vient pas d’une police, d’une image ou d’une texture ajoutées séparément, mais du renforcement mutuel de la "
     "composition, du contenu, du type, de l’objet de preuve, de la matière, des états et du comportement ; un élément sans "
     "relation visible est retiré ou sa limite nommée."),
]

# ---------- Liste close des conditions de façade : LCF-43 à LCF-46 (validate_reading_map.py) ----------
LCF_CODE = r'''
# ---------- V1.2 (PATCH-DECISION A, B, D) : LCF-43 à LCF-46 ----------
BRIEF_ORDER = re.compile(r"contenu réel.{0,80}?marque.{0,120}?asset principal.{0,120}?destination")
WAVE_MARKERS = re.compile(r"hero SaaS|gradient décoratif|\bviolet\b|\bInter\b|\bhalos?\b|\bbeige\b|\bcrème\b|serif italique|"
                          r"orange rouille|bandeau défilant|illustration peinte|\btramage\b")


def boot_block(t: dict[str, str]) -> list[str]:
    return fenced_after(t["D"], "Le boot tient au maximum les décisions suivantes").splitlines()


def lcf_43(t: dict[str, str]) -> bool:
    entry = fenced_after(t["D"], "### Entrée minimale").splitlines()
    boot = boot_block(t)
    vt = t["D"][t["D"].find("### Décider la route de production"):t["D"].find("### Réserve `ANCHOR-GENERATED`")]
    return (any(l.startswith("CONSTRAINT —") and "destination" in l for l in entry) and any(l.startswith("FABRICATION:") for l in boot)
            and not any(l.startswith(("ANCHOR-BASIS:", "ANCHOR-LIMIT:")) for l in boot)
            and "jamais un faux asset" in vt and "bilan `FABRICATION`" in t["A"]
            and all("`FABRICATION`" in t[k] for k in ("Q", "SK")))


def lcf_44(t: dict[str, str]) -> bool:
    ext = t["D"][t["D"].find("## DIRECTION/EXTERNAL-START"):t["D"].find("### Traduction humaine minimale")]
    return all(BRIEF_ORDER.search(x) and "au plus trois" in x.lower() for x in (ext, t["Q"], t["SK"]))


def lcf_45(t: dict[str, str]) -> bool:
    boot = boot_block(t)
    return (any(l.startswith("MODAL:") for l in boot) and any(l.startswith("PARTI:") for l in boot)
            and not any(l.startswith("ANTI-DIRECTIONS:") for l in boot)
            and all("`MODAL`/`PARTI`" in t[k] for k in ("Q", "SK")) and "MODAL:" in t["EX"])


def lcf_46(t: dict[str, str]) -> bool:
    keys = ("D", "A", "S", "B", "G", "Q", "RM", "OM", "README", "SK", "EX")
    stray = [l for k in keys for l in t[k].splitlines() if WAVE_MARKERS.search(l) and not l.startswith("[VEILLE 20")]
    dated = [l for l in t["S"].splitlines() if l.startswith("[VEILLE 20") and WAVE_MARKERS.search(l)]
    return not stray and bool(dated)

'''

LCF_ROWS = '''        ("LCF-43", "DIRECTION (entrée, boot, route de production), ACTION, QUICKSTART, skill : bilan de fabrication", "DIRECTION/CREATIVE-BOOT (FABRICATION) ; V1.2-A", lcf_43(t)),
        ("LCF-44", "EXTERNAL-START, QUICKSTART, skill : prise de brief, même ordre", "DIRECTION/EXTERNAL-START (prise de brief) ; V1.2-B", lcf_44(t)),
        ("LCF-45", "boot, QUICKSTART, skill, exemples : MODAL / PARTI", "DIRECTION/CREATIVE-BOOT (MODAL, PARTI) ; V1.2-D", lcf_45(t)),
        ("LCF-46", "textes et façades : marqueurs de vague seulement en [VEILLE] daté", "SAVOIR ([VEILLE] daté) ; V1.2-D", lcf_46(t)),
'''

PATCH += [
    ("P-L1", "LCF", RM, "\ndef check_facades(errors: list[str]) -> None:\n", LCF_CODE + "\ndef check_facades(errors: list[str]) -> None:\n"),
    ("P-L2", "LCF", RM,
     '        ("LCF-42", "QUICKSTART §9 : DECISION-CHANGE selon la triade", "ACTION/STATUS ; ACTION/HANDOFF ; Q-05", lcf_42(t)),\n',
     '        ("LCF-42", "QUICKSTART §9 : DECISION-CHANGE selon la triade", "ACTION/STATUS ; ACTION/HANDOFF ; Q-05", lcf_42(t)),\n'
     + LCF_ROWS),
]

# Entrée de patch dont l'inverse sert de mutation pour chaque nouvelle condition
MUTATION_OF = {"LCF-43": "P-A2", "LCF-44": "P-B1", "LCF-45": "P-D1", "LCF-46": "P-D7"}


def apply(root: Path, entries, reverse: bool = False, dry: bool = False) -> list[str]:
    texts: dict[str, str] = {}
    problems = []
    for pid, _point, rel, old, new in entries:
        a, b = (new, old) if reverse else (old, new)
        text = texts.get(rel)
        if text is None:
            p = root / rel
            if not p.is_file():
                problems.append(f"{pid} : fichier absent {rel}")
                continue
            text = p.read_text(encoding="utf-8")
        n = text.count(a)
        if n != 1:
            problems.append(f"{pid} : ancien texte trouvé {n} fois dans {rel}")
            continue
        texts[rel] = text.replace(a, b)
    if not problems and not dry:
        for rel, text in texts.items():
            (root / rel).write_text(text, encoding="utf-8")
    return problems


def mutations(root: Path) -> int:
    bad = 0
    for lcf, pid in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            problems = apply(copy, [e for e in PATCH if e[0] == pid], reverse=True)
            out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_reading_map.py")],
                                 capture_output=True, text=True, cwd=copy)
            red = out.returncode != 0 and lcf in (out.stdout + out.stderr)
            print(f"{lcf} sous inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'}{' ; ' + '; '.join(problems) if problems else ''}")
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
