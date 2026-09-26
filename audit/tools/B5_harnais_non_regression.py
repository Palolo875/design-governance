#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.07 PATCH-DECISION B5 — garde textuelle (composant partagé).

Artefact d'audit HORS package, en lecture seule. Usage :
    python3 B5_harnais_non_regression.py <racine>

B5 ne crée aucun invariant machine : ses corrections sont normatives. Ce harnais
est une GARDE TEXTUELLE limitée (présence ou absence de formulations précises).
Il ne remplace pas l'épreuve de lecture de la condition de sortie (§7 du rapport),
qui rejoue les scénarios 4.02 A/B et 4.03 C.

Sur B01, B5-01 à B5-05 échouent (défauts présents) ; T-POS réussit.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

CONTRACT_FIELDS = ["intention", "anatomie", "variant", "états", "responsive", "tokens",
                   "frontières de composition", "baseline", "source de vérité", "owner",
                   "compatibilité", "prochaine revue"]


def section(text: str, title_regex: str) -> str:
    """Retourne le texte d'une section Markdown de niveau 2 dont le titre correspond."""
    m = re.search(rf"(?m)^## {title_regex}.*$", text)
    if not m:
        return ""
    nxt = re.search(r"(?m)^## ", text[m.end():])
    return text[m.start(): m.end() + (nxt.start() if nxt else len(text))]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    off = Path(sys.argv[1]).resolve() / "V1/official"
    bib = (off / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    sav = (off / "SAVOIR.md").read_text(encoding="utf-8")
    act = (off / "ACTION.md").read_text(encoding="utf-8")
    comp = section(bib, r"BIBLIOTHEQUE/COMPONENTS")
    system = section(sav, r"SAVOIR/SYSTEM") or sav[sav.find("# SAVOIR/SYSTEM"):sav.find("# SAVOIR/SYSTEM") + 4000]
    act_contract = act[act.find("### Contrat de composant"):act.find("### Contrat de composant") + 1500] if "### Contrat de composant" in act else ""

    rows = []
    rows.append(("T-POS-1", "témoin", "COMPONENTS existe et définit les couches", bool(comp) and "LAYER/PRIMITIVES" in comp))
    missing = [f for f in CONTRACT_FIELDS if f.lower() not in comp.lower()]
    has_contract_block = bool(re.search(r"(?i)contrat de composant partagé", comp))
    rows.append(("B5-01", "F-BIB-004", "COMPONENTS porte un « contrat de composant partagé » (hors BRAND_GRAMMAR)", has_contract_block))
    rows.append(("B5-02", "F-BIB-004", f"ce contrat nomme les {len(CONTRACT_FIELDS)} responsabilités promises par SAVOIR 704"
                 + (f" (manquent : {', '.join(missing)})" if missing else ""), has_contract_block and not missing))
    rows.append(("B5-03", "F-BIB-004 (fusion)", "ACTION « Contrat de composant » renvoie à BIBLIOTHEQUE/COMPONENTS au lieu d'une liste concurrente",
                 bool(act_contract) and "BIBLIOTHEQUE/COMPONENTS" in act_contract))
    rows.append(("B5-04", "F-SAV-007", "SAVOIR/SYSTEM n'ordonne plus « Reclassifie en SYSTÈME »",
                 bool(system) and not re.search(r"Reclassifie en `?SYSTÈME`? lorsqu", system)))
    rows.append(("B5-05", "F-SAV-007", "SAVOIR/SYSTEM renvoie le signal à DIRECTION/START (objet direct ou run dépendant)",
                 bool(system) and "DIRECTION/START" in system and re.search(r"(?i)objet direct|dépendant", system) is not None))
    for cid, fiche, label, ok in rows:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:7} {fiche:20} {label}")
    b5 = [r for r in rows if r[0].startswith("B5")]
    print(f"\nTémoin : {sum(r[3] for r in rows if r[0].startswith('T'))}/1 ; gardes B5 : {sum(r[3] for r in b5)}/{len(b5)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
