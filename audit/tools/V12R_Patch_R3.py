#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R3 : alignements (D-01, D-02, D-07, D-08, D-12, D-13).

Plan : `plans/Plan_V1.2_Refonte.md`, lot R3 ; registre des défauts `V12_11` §4 ; méthode M1 à M4 (`V12R_00`, `V12R_02`).
Chaque correction entre avec sa garde de propriété (validate_structure.py, version R3). Usage :
  python3 V12R_Patch_R3.py <racine>                 # applique
  python3 V12R_Patch_R3.py <racine> --verifier      # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12R_Patch_R3.py <racine> --inverse ID    # remet l'ancien texte d'une entrée (mutation des gardes)
  python3 V12R_Patch_R3.py <racine> --mutations     # sur une racine patchée : chaque garde rougit sous sa mutation
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from V12_Patch_ABD import apply  # noqa: E402

D, A, S = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md"
Q, G, C = "V1/official/QUICKSTART.md", "V1/official/GLOSSAIRE.md", "V1/official/CHANGELOG.md"
SK = "skills/design-governance-practice/SKILL.md"
EX = "skills/design-governance-practice/references/examples.md"

# Remplacement de fichier entier : chemin → (empreinte attendue avant, source de la nouvelle version)
FILE_REPLACE = {
    "scripts/validate_structure.py": ("bb45d0861b023a0d27a6456d983cd682c0cfdbcba47b2c34fed78df681e73197",
                                      HERE / "V12R_Patch_R3_fichiers" / "scripts" / "validate_structure.py"),
}

BRIEF_OLD_Q = "demande au plus trois intrants, dans cet ordre : contenu réel, marque, asset principal, destination ; le rendu est construit dans tous les cas."
BRIEF_NEW_Q = ("demande au plus trois intrants, en un seul échange, par gain de plafond : contenu réel, marque, asset principal ou route autorisée, "
               "destination si elle est incertaine ; le rendu est construit dans tous les cas.")

PATCH = [
    # ---------- D-01 : vocabulaire unique MODAL / PARTI ----------
    ("R3-V1", "D-01 contrat TARGET", D,
     "preuve, ancre et anti-direction. |", "preuve, ancre, modal et parti. |"),
    ("R3-V2", "D-01 vues sans doublon", D,
     "l’anti-direction devient une exclusion si elle gouverne la scène",
     "le parti devient une exclusion s’il gouverne la scène"),
    ("R3-V3", "D-01 RUN-PRIORITY", D,
     "retenir support, tension, scène, typographie et anti-direction",
     "retenir support, tension, scène, typographie, modal et parti"),
    ("R3-V4", "D-01 traduction humaine", D,
     "| Qu’est-ce que nous refusons de faire ? | `ANTI-DIRECTION`, contre-choix et limites. |",
     "| Qu’est-ce que nous refusons de faire ? | `MODAL` écarté par le `PARTI`, contre-choix et limites. |"),
    ("R3-V5", "D-01 table VISUAL_TARGET", D,
     "| **Anti-direction** | Gabarit, relation ou effet refusé, avec raison produit ou perceptuelle. |",
     "| **Modal / parti** | Le modal nommé (ce que n’importe quelle IA produirait ici) et le parti : garder ou s’écarter, où et pourquoi, avec raison produit ou perceptuelle. |"),
    ("R3-V6", "D-01 correspondance RUN_CARD", A,
     "| VISUAL_TARGET : thèse, anti-direction | avant build | `direction.thesis`, `.anti_direction` | — |",
     "| VISUAL_TARGET : thèse, modal / parti | avant build | `direction.thesis`, `.anti_direction` (le modal nommé et le parti) | — |"),
    ("R3-V7", "D-01 skill, Diriger", SK,
     "une anti-direction et une condition de retrait", "un modal nommé, un parti et une condition de retrait"),
    ("R3-V8", "D-01 skill, boot", SK,
     "geste, anti-directions concrètes, tension et signature structurelles", "geste, tension et signature structurelles"),
    ("R3-V9", "D-01 skill, boot", SK,
     "`MODAL`/`PARTI` (d’où viennent les anti-directions), bilan de fabrication (`FABRICATION`), premier objet",
     "`MODAL`/`PARTI`, bilan de fabrication (`FABRICATION`), premier objet"),
    ("R3-V10", "D-01 QUICKSTART, boot", Q,
     "geste, anti-directions concrètes, tension et signature structurelles", "geste, tension et signature structurelles"),
    ("R3-V11", "D-01 QUICKSTART, boot", Q,
     "`MODAL`/`PARTI` (d’où viennent les anti-directions), bilan de fabrication (`FABRICATION`), le premier objet",
     "`MODAL`/`PARTI`, bilan de fabrication (`FABRICATION`), le premier objet"),
    ("R3-V12", "D-01 exemples", EX,
     "composant authored et anti-direction.", "composant authored, modal et parti."),
    ("R3-V13", "D-01 vocabulaire observable", S,
     "| position choisie, anti-direction, risque assumé et différence perceptible |",
     "| position choisie, parti (écart au modal), risque assumé et différence perceptible |"),
    # ---------- D-02 : prise de brief fidèle (condition canonique formulée positivement) ----------
    ("R3-B0", "D-02 canon EXTERNAL-START", D,
     "destination si elle n’est pas évidente.", "destination si elle est incertaine."),
    ("R3-B1", "D-02 skill", SK,
     "demander au plus trois intrants, dans cet ordre : contenu réel, marque, asset principal, destination (`DIRECTION/EXTERNAL-START`) ; construire dans tous les cas.",
     "demander au plus trois intrants, en un seul échange, par gain de plafond : contenu réel, marque, asset principal ou route autorisée, "
     "destination si elle est incertaine (`DIRECTION/EXTERNAL-START`) ; construire dans tous les cas."),
    ("R3-B2", "D-02 QUICKSTART", Q, BRIEF_OLD_Q, BRIEF_NEW_Q),
    ("R3-B3", "D-02 CHANGELOG", C,
     "au plus trois demandes, dans l’ordre contenu réel, marque, asset principal, destination ; construire dans tous les cas.",
     "au plus trois demandes, en un seul échange : contenu réel, marque, asset principal ou route autorisée, destination si elle est incertaine ; construire dans tous les cas."),
    # ---------- D-07 : renvois vers les marqueurs de vague et la carte des moyens ----------
    ("R3-R1", "D-07 boot → marqueurs", D,
     "MODAL: ce que n’importe quelle IA produirait ici (structure, palette, typo, assets)\n",
     "MODAL: ce que n’importe quelle IA produirait ici (structure, palette, typo, assets) ; se nomme avec les marqueurs de vague datés de `SAVOIR/TOOLS`\n"),
    ("R3-R2", "D-07 route de production → carte", D,
     "Sources par couche : carte des moyens (`SAVOIR`, `[VEILLE]`)", "Sources par couche : carte des moyens (`SAVOIR/TOOLS`, `[VEILLE]`)"),
    ("R3-R3", "D-07 balise ANT-01", S,
     "\n[VEILLE 2026-09] **Marqueurs de vague**", "\n<!-- concept:ANT-01 -->\n[VEILLE 2026-09] **Marqueurs de vague**"),
    ("R3-R4", "D-07 balise MOY-01", S,
     "\n[VEILLE 2026-09] **Carte des moyens par couche**", "\n<!-- concept:MOY-01 -->\n[VEILLE 2026-09] **Carte des moyens par couche**"),
    # ---------- D-08 : glossaire du vocabulaire de fabrication ----------
    ("R3-G1", "D-08 glossaire", G,
     "| **Premier objet** |",
     "| **Thèse** | La position de design en une phrase : ce que la proposition affirme sur le produit et sur la personne à qui elle s’adresse. |\n"
     "| **Ancre** | Une référence réellement regardée (observée, fournie ou générée) qui calibre une décision visuelle ; on note ce qu’on en retient, ce qu’on écarte et sa date. |\n"
     "| **Creative Boot** | Le cadrage court fait avant le premier pixel d’une décision visuelle ouverte : promesse, objet de preuve, geste, `MODAL`, `PARTI`, tension, `FABRICATION` et premier objet. |\n"
     "| **`MODAL`** | Ce que n’importe quelle IA produirait par défaut pour ce brief (structure, palette, typographie, assets), nommé pour pouvoir le garder ou s’en écarter en connaissance de cause. |\n"
     "| **`PARTI`** | La décision prise face au `MODAL` : le garder ou s’en écarter, à quel endroit et pour quelle raison liée à la thèse. |\n"
     "| **`FABRICATION`** | Le bilan des moyens réels (assets, marque, polices, composants, génération, contenu) et du niveau atteignable couche par couche avant le build. |\n"
     "| **Plafond** | Le niveau qu’une couche peut atteindre avec les moyens disponibles ; lorsqu’il est bas, l’agent le déclare et dit ce qui le relèverait. |\n"
     "| **Objet de preuve** | L’élément de la première scène qui rend la promesse crédible : de préférence un composant, une donnée, un état ou une interaction du produit. |\n"
     "| **Défaut dominant** | Le défaut qui pèse le plus sur la qualité perçue ou sur l’usage ; c’est lui que l’on corrige en premier. |\n"
     "| **Vérité de scène** | La règle qui marque comme illustratif tout exemple, chiffre ou témoignage non observé, et qui le signale au public en langage produit. |\n"
     "| **Slop** | Une production générique, répétitive ou trompeuse faite avec peu de soin ; le slop procédural est une trace remplie sans décision réelle. |\n"
     "| **Premier objet** |"),
    # ---------- D-12 : QUICKSTART, table unique et vouvoiement ----------
    ("R3-Q1", "D-12 table des cinq questions (version complète au démarrage)", Q,
     "| Quelle décision doit changer ? | Le choix concret à trancher, confirmer ou abandonner. |\n"
     "| Quel risque domine ? | Identité, usage, accessibilité, technique, système ou autre risque déclaré. |\n"
     "| Quelle preuve peut distinguer les options ? | Observation, capture, test, mesure, comparaison ou inspection adaptée. |\n"
     "| Qu’est-ce qui est réellement disponible ? | Artefact, runtime, données, participant, source ou capacité technique. |\n"
     "| Qui porte la décision ? | Owner de la décision, de la reprise ou de l’escalade. |",
     "| Quelle décision doit changer ? | Le choix concret à trancher, confirmer ou abandonner. |\n"
     "| Quel risque domine ? | Identité, usage, accessibilité, technique, système ou autre risque déclaré. |\n"
     "| Quelle preuve peut distinguer les options ? | Mesure, capture, test, comparaison, inspection ou observation adaptée. |\n"
     "| Qu’est-ce qui est réellement disponible ? | Artefact, navigateur, DOM/CSS, contraste, clavier/AT, participant, runtime, donnée ou source. |\n"
     "| Qui porte la décision et la prochaine action ? | Owner explicite, avec confirmation ou escalade si nécessaire. |"),
    ("R3-Q2", "D-12 §2 renvoie au démarrage", Q,
     "Avant de construire ou de modifier, répondez à ces cinq questions :\n\n"
     "| Question | Réponse minimale |\n|---|---|\n"
     "| **Quelle décision doit changer ?** | Une phrase qui décrit le choix à trancher. |\n"
     "| **Quel risque domine ?** | Identité, usage, accessibilité, technique, système ou autre risque déclaré. |\n"
     "| **Quelle preuve peut distinguer les options ?** | Mesure, capture, test, comparaison, inspection ou observation adaptée. |\n"
     "| **Qu’est-ce qui est réellement disponible ?** | Artefact, navigateur, DOM/CSS, contraste, clavier/AT, participant, runtime, donnée ou source. |\n"
     "| **Qui porte la décision et la prochaine action ?** | Owner explicite, avec confirmation ou escalade si nécessaire. |\n",
     "Avant de construire ou de modifier, répondez aux cinq questions du démarrage en 90 secondes.\n"),
    ("R3-Q3", "D-12 vouvoiement", Q,
     "**Bénéfice attendu.** Charge `DIRECTION`", "**Bénéfice attendu.** Chargez `DIRECTION`"),
    ("R3-Q4", "D-12 vouvoiement", Q,
     "reste sur le chemin court ; si un risque critique est actif, ne confonds pas",
     "restez sur le chemin court ; si un risque critique est actif, ne confondez pas"),
    ("R3-Q5", "D-12 vouvoiement", Q,
     "Pour une décision visuelle ouverte, utilise le **Creative Boot**", "Pour une décision visuelle ouverte, utilisez le **Creative Boot**"),
    ("R3-Q6", "D-12 vouvoiement", Q,
     "peuvent changer le résultat, active `DIRECTION/DOMAIN-FRAME`", "peuvent changer le résultat, activez `DIRECTION/DOMAIN-FRAME`"),
    ("R3-Q7", "D-12 vouvoiement", Q,
     "Augmente la profondeur seulement", "Augmentez la profondeur seulement"),
    ("R3-Q8", "D-12 vouvoiement", Q,
     "Pour une UI/UX nouvelle, ajoute le contrat de réalité", "Pour une UI/UX nouvelle, ajoutez le contrat de réalité"),
    ("R3-Q9", "D-12 vouvoiement", Q,
     "Avant toute route détaillée, garde en tête", "Avant toute route détaillée, gardez en tête"),
    # ---------- D-13 : coquille ----------
    ("R3-T1", "D-13 espace initiale", Q,
     "\n Pour une `RUN_CARD` persistante, cet exemple", "\nPour une `RUN_CARD` persistante, cet exemple"),
    # ---------- CHANGELOG ----------
    ("R3-CH1", "CHANGELOG « Non publié »", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Alignements (refonte, R3).** Vocabulaire unique `MODAL` / `PARTI` (le terme « anti-direction » ne subsiste que dans l’historique ; "
     "projection inchangée `direction.anti_direction`) ; résumés de la prise de brief fidèles au canon ; renvois du boot vers les marqueurs "
     "de vague et de la route de production vers la carte des moyens (`SAVOIR/TOOLS`) ; glossaire du vocabulaire de fabrication ; QUICKSTART "
     "au vouvoiement et sans table en double. Nouvelles gardes de propriété dans `scripts/validate_structure.py`.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

# Mutations : l'inverse d'une entrée doit faire rougir la garde qui la protège (motif attendu dans la sortie).
MUTATION_OF = {
    "R3-V7": "vocabulaire retiré",
    "R3-V5": "vocabulaire retiré",
    "R3-B2": "résumé infidèle",
    "R3-B1": "résumé infidèle",
    "R3-R1": "renvoi DIRECTION/CREATIVE-BOOT → ANT-01",
    "R3-R2": "renvoi DIRECTION/VISUAL_TARGET → MOY-01",
    "R3-R3": "ANT-01 absent",
    "R3-G1": "glossaire : terme absent",
    "R3-Q2": "ligne de table en double",
    "R3-Q5": "registre : tutoiement",
}


# Migrations M1 : mutations de remplacement des cas R-17 et R-21 (le texte R.01 inversé par ces cas a été réécrit par R3).
MIGRATION_MUTATIONS = [
    ("R-17 → LCF-24", Q, "geste, tension et signature structurelles (nombre d’axes",
     "geste, deux anti-directions concrètes, une tension et une signature structurelles (nombre d’axes", "LCF-24"),
    ("R-21 → LCF-28", A, "| VISUAL_TARGET : thèse, modal / parti |",
     "| VISUAL_TARGET : thèse, modal / parti, premier objet, périmètre, contrainte |", "LCF-28"),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def apply_all(root: Path, dry: bool = False) -> list[str]:
    problems = apply(root, PATCH, dry=dry)
    for rel, (old_sha, _src) in FILE_REPLACE.items():
        if sha(root / rel) != old_sha:
            problems.append(f"{rel} : empreinte inattendue (version R2 requise)")
    if problems or dry:
        return problems
    for rel, (_old, src) in FILE_REPLACE.items():
        shutil.copy2(src, root / rel)
    return []


def structure(copy: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_structure.py")],
                         capture_output=True, text=True, cwd=copy)
    return out.returncode, out.stdout + out.stderr


def mutations(root: Path) -> int:
    bad = 0
    for pid, motif in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            problems = apply(copy, [e for e in PATCH if e[0] == pid], reverse=True)
            code, out = structure(copy)
            red = code != 0 and motif in out and not problems
            print(f"inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'} (motif « {motif} »){' ; ' + '; '.join(problems) if problems else ''}")
            bad += 0 if red else 1
    for name, rel, old, new, lcf in MIGRATION_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_reading_map.py")],
                                 capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and lcf in (out.stdout + out.stderr)
            print(f"migration {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
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
        problems = apply_all(root, dry="--verifier" in sys.argv)
    for pr in problems:
        print(pr)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH)} entrées, {len(FILE_REPLACE)} fichier(s) remplacé(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
