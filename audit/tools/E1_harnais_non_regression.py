#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.22 PATCH-DECISION E1 — garde textuelle (lot éditorial : 27 fiches Mineur).

Artefact d'audit HORS package ; copie temporaire pour le seul cas de build (F-SK-002) ; lecture seule des sources.
Usage : python3 E1_harnais_non_regression.py <racine>

Une garde par fiche : présence ou absence d'une formulation précise à l'endroit visé. Les gardes ne prouvent pas
la lecture ; le lot étant éditorial, l'épreuve de sortie est une relecture (§6 du rapport).
F-SK-002 lance le build sur une copie et inspecte l'export Local produit.
Sur B01 : témoin 1/1 ; gardes 0/28 (27 fiches + 1 coordination avec F-DIR-018).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def line(text: str, start: str) -> str:
    return next((l for l in text.splitlines() if l.startswith(start)), "")


def between(text: str, a: str, b: str) -> str:
    i = text.find(a)
    if i < 0:
        return ""
    j = text.find(b, i + len(a))
    return text[i: j if j > 0 else len(text)]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    off = src / "V1/official"
    A = (off / "ACTION.md").read_text(encoding="utf-8")
    D = (off / "DIRECTION.md").read_text(encoding="utf-8")
    S = (off / "SAVOIR.md").read_text(encoding="utf-8")
    B = (off / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    G = (off / "GLOSSAIRE.md").read_text(encoding="utf-8")
    Q = (off / "QUICKSTART.md").read_text(encoding="utf-8")
    refs = src / "skills/design-governance-practice/references"
    EX = (refs / "examples.md").read_text(encoding="utf-8")
    FL = (refs / "flow.md").read_text(encoding="utf-8")
    MP = (refs / "machine_projection.md").read_text(encoding="utf-8")

    registers = line(A, "Pour naviguer dans ACTION")
    l110 = next((l for l in A.splitlines() if "`SAVOIR/CONTEXT` et `SAVOIR/TECH` sont chargés" in l), "")
    fast = between(A, "## ACTION/FAST-PATH", "## ACTION/RUN_CARD")
    typo = line(A, "La partition")
    prov = next((l for l in A.splitlines() if l.startswith("Pour un verdict global `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, la `RUN_CARD` doit rattacher")), "")
    grid = between(B, "### Contrat de grille", "\n### ")
    legend = between(D, "### Légende", "\n### ")
    boot_tension = line(D, "STRUCTURAL-TENSION:")
    boot_anti = line(D, "ANTI-DIRECTIONS:")
    daily_lite = line(D, "| **LITE** | `ACTION/RUN-LITE`.")
    dfast = between(D, "### DIRECTION/FAST-PATH", "## DIRECTION/EXTERNAL-START")
    routes = between(D, "| Route | À retenir lorsque |", "La génération ne reçoit")
    genere = line(D, "| `GÉNÉRÉ-DIRIGÉ` |")
    abs4 = between(D, "### [ABSOLU 4", "| Jalon |")
    capa = line(D, "Une **capacité** est")
    modal = next((l for l in D.splitlines() if "l’emporte que si son avantage est formulé" in l), "")
    recap = D[D.find("Avant de parcourir les sections détaillées") - 200: D.find("Avant de parcourir les sections détaillées") + 1600] if "Avant de parcourir les sections détaillées" in D else ""
    item4 = next((l for l in recap.splitlines() if l.startswith("4. ")), "")
    sys_ex = next((b for b in re.findall(r"```text\n(.*?)```", EX, re.S) if "MODE: SYSTÈME" in b), "")
    glo = line(G, "| **RUN_CARD** |")
    mp_art = re.search(r"artifact:\n\s+locator:\s*\"([^\"]+)\"", MP)
    mp_prov = re.search(r"provenance:\n\s+artifact_locator:\s*\"([^\"]+)\"", MP)
    qs_sys = line(Q, "| `SYSTÈME` | `DIRECTION/START`, `ACTION/RUN-SYSTEM`")
    qs_path = between(Q, "## 3. Le parcours complet", "Il comporte deux boucles")
    sav38 = line(S, "Ne charge jamais l’ensemble de SAVOIR")
    atlas = line(S, "| **Structure / composant** |")
    gold6 = line(S, "6. Sur une surface `DIRECTION`")

    rows = [
        ("T-1", "témoin", "sources lues", all((A, D, S, B, G, Q, EX, FL, MP))),
        ("E1-01", "F-ACT-003", "ACTION : la phrase d'entrée nomme les registres du tableau (observation, interprétation)",
         bool(re.search(r"(?i)observation", registers)) and bool(re.search(r"(?i)interprétation", registers))),
        ("E1-02", "F-ACT-004", "ACTION 110 : chargement si la question peut changer la décision, la preuve ou la limite",
         bool(re.search(r"décision, la preuve ou la limite", l110))),
        ("E1-03", "F-ACT-016", "FAST-PATH d'ACTION : après les quatre réponses, forme courte LITE (CLOSE-PACKAGE)", "CLOSE-PACKAGE" in fast),
        ("E1-04", "F-ACT-032", "partition typographique : plus « complète » ; licence, glyphes et chargement selon SAVOIR/TYPE",
         "La partition complète" not in A and "SAVOIR/TYPE" in typo and bool(re.search(r"(?i)licence", typo))),
        ("E1-05", "F-ACT-034", "provenance absente ⇒ verdict non accepté (le « ou » est levé)",
         bool(prov) and "ou la limite est explicitement déclarée" not in prov),
        ("E1-06", "F-BIB-003", "contrat de grille : familles MOBILE-* conditionnées au mobile dans le scope ou à un risque responsive",
         bool(re.search(r"(?i)mobile est dans le scope|risque responsive", grid))),
        ("E1-07", "F-DIR-005", "légende déclarée commune à DIRECTION et SAVOIR", bool(re.search(r"(?i)légende commune|tags? (aussi |également )?(utilisés? )?(dans|par) `?SAVOIR", legend))),
        ("E1-08", "F-DIR-012", "Boot : cardinalité des axes renvoyée à BIBLIOTHEQUE ; anti-directions sans nombre fixe",
         "un axe de tension" not in boot_tension and "BIBLIOTHEQUE" in boot_tension and not re.search(r"\bdeux\b", boot_anti)),
        ("E1-09", "F-DIR-014", "DAILY : la reclassification depuis LITE inclut ITER", "`ITER`" in daily_lite),
        ("E1-10", "F-DIR-015", "FAST-PATH de DIRECTION : triade canonique « changée, confirmée ou abandonnée »",
         "changée, confirmée ou abandonnée" in dfast and "modifié ou confirmé" not in dfast),
        ("E1-11", "F-DIR-025", "routes de production : valeur pour l'absence intentionnelle d'asset", bool(re.search(r"(?i)\| `SANS-ASSET`", routes))),
        ("E1-12", "F-DIR-026", "GÉNÉRÉ-DIRIGÉ : condition bornée aux sources observées dans le scope, le délai et les droits",
         bool(re.search(r"(?i)observées? dans le scope", genere))),  # 12.05c R-13 : texte décidé au singulier
        ("E1-13", "F-DIR-031", "ABSOLU 4 : « avant toute action qui engage artefact, preuve, état, diffusion ou persistance »",
         "Avant d’agir" not in abs4 and bool(re.search(r"(?i)engage", abs4))),
        ("E1-14", "F-DIR-037", "capacité : « construire, décider, observer ou tenir une contrainte »", "construire, décider, observer" in capa),
        ("E1-15", "F-DIR-040", "« direction modale » remplacé par « direction retenue »", "La direction modale" not in D and "direction retenue ne l’emporte" in modal),
        ("E1-16", "F-DIR-043", "l'« entrée prioritaire » de DIRECTION est requalifiée en récapitulatif de protection",
         "### Entrée prioritaire — à lire avant le détail" not in D and bool(re.search(r"(?i)### Récapitulatif", D))),
        ("E1-17", "F-DIR-018 (coord.)", "récapitulatif, point 4 : exception « sauf si la navigation est l'objet de preuve »", "sauf si" in item4),
        ("E1-18", "F-DIR-045", "DIRECTION : `limitations` écrit avec son chemin `closure.limitations`", not re.search(r"(?<![.\w])`limitations`", D)),
        ("E1-19", "F-EX-003", "exemple SYSTÈME : NOT-VERIFIED pour l'inspecté manquant ; échec localisé (absorbé par C6)",
         bool(sys_ex) and "NOT-OBSERVED:" not in sys_ex and "NOT-VERIFIED:" in sys_ex and bool(re.search(r"(?i)observée", sys_ex))),
        ("E1-20", "F-FLOW-001", "flow.md : les branches risque critique et NOT-VERIFIED reviennent vers reclassification et owner / prochaine preuve",
         bool(re.search(r"\bH\s*-->", FL)) and bool(re.search(r"\bI\s*-->", FL))),
        ("E1-21", "F-GLO-001", "GLOSSAIRE : RUN_CARD définie par la persistance exigée, avec renvoi à ACTION/RUN_CARD",
         bool(re.search(r"(?i)persist", glo)) and "ACTION/RUN_CARD" in glo),
        ("E1-22", "F-MP-001", "YAML : provenance.artifact_locator = artifact.locator", bool(mp_art and mp_prov and mp_art.group(1) == mp_prov.group(1))),
        ("E1-23", "F-QS-001", "QUICKSTART : parcours qualifié par mode ; COMPONENTS seulement si un composant change",
         bool(re.search(r"(?i)selon le mode|par mode|chaque mode", qs_path)) and bool(re.search(r"COMPONENTS` si", qs_sys))),  # 12.05c R-13 : texte décidé (E1, F-QS-001) « chaque mode n’en garde que… »
        ("E1-24", "F-QS-004", "QUICKSTART : chemins explicites vers les références de la skill", "references/examples.md" in Q),
        ("E1-25", "F-SAV-001", "SAVOIR 38 : « typiquement zéro à deux ; une route par question active »", bool(re.search(r"(?i)une route par question active", sav38))),
        ("E1-26", "F-SAV-004", "ATLAS 541 : SAVOIR/SYSTEM ajouté pour le composant partagé", "SAVOIR/SYSTEM" in atlas),
        ("E1-27", "F-SAV-010", "règle d'or 6 : spec toujours requise en DIRECTION ; ancre selon DIRECTION", bool(re.search(r"(?i)spec (est )?toujours requise", gold6))),
    ]
    # F-SK-002 : export Local produit par le build (copie)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(shutil.copytree(src, Path(tmp) / "pkg", ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip")))
        r = subprocess.run(["bash", "scripts/build_distributions.sh"], cwd=root, capture_output=True, text=True)
        sk = root / "dist/local/skill/SKILL.md"
        qs = root / "dist/local/official/QUICKSTART.md"
        ok = r.returncode == 0 and sk.is_file() and "V1/official/" not in sk.read_text(encoding="utf-8") \
            and "skills/design-governance-practice/" not in qs.read_text(encoding="utf-8")
        rows.append(("E1-28", "F-SK-002", "export Local : chemins propres au layout (aucun « V1/official/ » dans la skill Local)", ok))
    for cid, fiche, label, good in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {fiche:18} {label}")
    t = [r for r in rows if r[0].startswith("T")]
    e = [r for r in rows if r[0].startswith("E1")]
    print(f"\nTémoin : {sum(r[3] for r in t)}/1 ; gardes E1 : {sum(r[3] for r in e)}/{len(e)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
