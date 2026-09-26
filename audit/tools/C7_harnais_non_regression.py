#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.14 PATCH-DECISION C7 — garde textuelle (homogénéisation et ablation).

Artefact d'audit HORS package, en lecture seule. Usage : python3 C7_harnais_non_regression.py <racine>

C7 ne crée aucun invariant machine : les trois corrections portent sur des jugements (palette, profil,
non-généricité). Ce harnais est une GARDE TEXTUELLE limitée. Il ne remplace ni l'épreuve de lecture ni la
mesure « avec / sans DG » de la condition de sortie (§6 du rapport), seule capable de dire si la correction
réduit la convergence observée.
Sur B01 : témoins et conservation 4/4 ; gardes 0/5.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def section(text: str, head: str, stop: str = r"(?m)^#{1,3} ") -> str:
    i = text.find(head)
    if i < 0:
        return ""
    j = re.search(stop, text[i + len(head):])
    return text[i: i + len(head) + (j.start() if j else len(text))]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    off = Path(sys.argv[1]).resolve() / "V1/official"
    sav = (off / "SAVOIR.md").read_text(encoding="utf-8")
    bib = (off / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    cft05 = section(sav, "## CFT-05")
    style_test = next((l for l in sav.splitlines() if "Test de style" in l), "")
    gen = next((l for l in bib.splitlines() if l.startswith("| Non-généricité |")), "")
    rows = [
        ("T-1", "témoin", "CFT-05 présent", bool(cft05)),
        ("T-2", "témoin", "test de style présent (SAVOIR/STYLE)", bool(style_test)),
        ("T-3", "témoin", "test de non-généricité présent (BIBLIOTHEQUE/GATE)", bool(gen)),
        ("G-01", "F-BIB-005", "non-généricité : l'ablation révèle une dépendance ; refonte seulement si elle est décorative, jugée sur rendu entier, tâche et Gate C",
         "Si oui, changer la relation" not in gen and bool(re.search(r"(?i)dépendance", gen)) and bool(re.search(r"(?i)fallback", gen)) and bool(re.search(r"Gate C|GATE-C", gen))),
        ("G-02", "F-SAV-006", "test de style : un médium masqué peut porter légitimement le profil (dépendance + fallback), l'ablation seule ne conclut pas",
         bool(re.search(r"(?i)dépend", style_test)) and bool(re.search(r"(?i)fallback", style_test))),
        ("G-03", "F-SAV-002", "CFT-05 ne prescrit plus la répartition « neutres + accent » sous le tag requis",
         "Les neutres portent l’essentiel de la structure" not in cft05),
        ("C-01", "F-SAV-002", "conservation : CFT-05 garde l'exigence fonctionnelle (rôles, contraste calculé, information critique non portée par la seule couleur)",
         "palette par rôles" in cft05 and bool(re.search(r"(?i)calcul", cft05)) and bool(re.search(r"(?i)ne doit pas porter seule une information critique", cft05))),
        ("G-04", "F-SAV-002", "CFT-05 admet plusieurs registres (accent unique, multicolore structurelle, codage par zones)",
         bool(re.search(r"(?i)multicolore", cft05)) and bool(re.search(r"(?i)zones", cft05))),
        ("G-05", "F-SAV-002", "CFT-05 pose la question de convergence (palette par défaut du modèle, justification produit)",
         bool(re.search(r"(?i)convergence", cft05)) and bool(re.search(r"(?i)par défaut|sans brief", cft05))),
    ]
    for cid, fiche, label, ok in rows:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:5} {fiche:10} {label}")
    t = [r for r in rows if r[0][0] in "TC"]
    g = [r for r in rows if r[0].startswith("G")]
    print(f"\nTémoins et conservation : {sum(r[3] for r in t)}/{len(t)} ; gardes : {sum(r[3] for r in g)}/{len(g)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
