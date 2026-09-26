#!/usr/bin/env python3
"""DG-AUDIT-001 — R.03 — mini-boucle du retour : textes cibles exacts (Q-01, Q-02, Q-03, Q-05, Q-06, Q-10, O-1).

Artefact d'audit HORS package. S'applique sur B04 APRÈS DG_AUDIT_001_Patch_R01.py et la version V1.1.1 (R.02).
Même mécanique que R.01 : chaque entrée remplace UNE occurrence exacte, sinon rien n'est écrit
(fonction `apply` reprise de DG_AUDIT_001_Patch_R01.py, dépendance déclarée).
Usage :
  python3 DG_AUDIT_001_Patch_R03.py <racine> [--verifier]
  python3 DG_AUDIT_001_Patch_R03.py <racine> --inverse ID
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import DG_AUDIT_001_Patch_R01 as PR  # noqa: E402

A, D, G, Q, S, C, N, MP, RM = PR.A, PR.D, PR.G, PR.Q, PR.S, PR.C, PR.N, PR.MP, PR.RM
DC = PR.DC

PATCH: list[tuple[str, str, str, str, str]] = [
    # ---------- Q-01 : droits inconnus, portée réelle du contrôle machine ----------
    ("P-37", "Q-01", A,
     "La machine contrôle seulement l’exclusion d’`ACCEPTED` ; la réserve sur les droits reste à la trace.",
     "La machine ne contrôle cette exclusion que pour une `RUN_CARD` `DIRECTION`, où `artifact.rights_status` est requis ; dans les autres modes, comme pour la réserve sur les droits, le contrôle reste à la trace."),
    # ---------- Q-02 : paquet SYSTÈME avec conséquence décisionnelle ----------
    ("P-38", "Q-02", A,
     "| **SYSTÈME** | Décision de système, impact, consumers, owner, migration/rollback, non-régression, réserves, verdict et entrée CHANGELOG. |",
     f"| **SYSTÈME** | Décision de système, impact, consumers, owner, migration/rollback, non-régression, réserves, verdict, entrée CHANGELOG et {DC}. |"),
    # ---------- Q-03 : copies SAVOIR de la triade ----------
    ("P-39", "Q-03", S,
     "Si aucune décision ne change, retournez `N/A-JUSTIFIED` et ne chargez pas une route supplémentaire.",
     "Si aucune décision n’est changée, confirmée ou abandonnée, retournez la triade d’`ACTION/STATUS` — `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée — et ne chargez pas une route supplémentaire."),
    ("P-40", "Q-03", S,
     "| Aucune décision modifiée, confirmée ou abandonnée sans justification `N/A-JUSTIFIED`. |",
     "| Aucune décision modifiée, confirmée ou abandonnée, sans `N/A-JUSTIFIED` justifié ni `NOT-OBSERVED` déclaré (triade d’`ACTION/STATUS`). |"),
    # ---------- Q-05 : exemple complet du QUICKSTART §9 ----------
    ("P-41", "Q-05", Q, "STATE: BUILDING\n\nDECISION-INTENT:", "STATE: CHECKING\n\nDECISION-INTENT:"),
    ("P-42", "Q-05", Q,
     "CHANGE:\nRapprocher l’objet et le titre, réduire la saillance du CTA secondaire et réviser le crop.\n\n"
     "DECISION-CHANGE:\nLe défaut de hiérarchie est réel ; la correction modifie l’artefact et doit être réobservée.",
     "CORRECTION:\nRapprocher l’objet et le titre, réduire la saillance du CTA secondaire et réviser le crop.\n\n"
     "DECISION-CHANGE:\nCHANGED — la composition mobile du premier rendu est abandonnée : l’objet visuel rejoint le titre et le CTA secondaire recule (observation : capture mobile 390). L’effet de la correction reste à réobserver."),
    # ---------- Q-06 : table de charge du QUICKSTART §5 ----------
    ("P-43", "Q-06", Q,
     "| `LITE` | `DIRECTION/START`, `ACTION/RUN-LITE`, `ACTION/FAST-PATH`. |",
     "| `LITE` | `DIRECTION/START`, `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. |"),
    ("P-44", "Q-06", Q,
     "| `ITER` | `DIRECTION/START`, `ACTION/RUN-ITER`, direction existante. |",
     "| `ITER` | `DIRECTION/START`, `ACTION/RUN-ITER`, direction existante, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. |"),
    # ---------- Q-10 : réserve à sept attributs dans l'exemple CLOSED ----------
    ("P-45", "Q-10", G,
     "il porte une réserve complète (owner, portée, impact, prochaine preuve, date de revue, condition de sortie).",
     "il porte une réserve complète (owner, portée, date ou version, impact, prochaine preuve, date de revue, condition de sortie)."),
    # ---------- O-1 : null seulement là où le schéma l'admet ----------
    ("P-46", "O-1", A,
     "`null` signifie qu’aucune valeur n’est déclarée dans cette projection ; il ne signifie ni réussite ni preuve absente.",
     "`null` signifie qu’aucune valeur n’est déclarée dans cette projection ; il ne signifie ni réussite ni preuve absente. Seuls `closure.issue`, `closure.verdict` et `risk.critical_protection` admettent `null` ; un autre champ sans valeur est omis (par exemple `closure.direction_status` hors surface `DIRECTION`)."),
    ("P-47", "O-1", MP,
     "Aucune de ces valeurs ne devient un verdict global. `null` ne signifie ni réussite ni preuve absente.",
     "Aucune de ces valeurs ne devient un verdict global. `null` ne signifie ni réussite ni preuve absente ; il n’est admis que là où le schéma l’admet (`ACTION/RUN_CARD`), sinon le champ est omis."),
    # ---------- versions : compte des conditions ----------
    ("P-48", "V1.1.1", C,
     "- **Validateur de carte.** La liste close des conditions de façade passe de 21 à 35 conditions.",
     "- **Validateur de carte.** La liste close des conditions de façade passe de 21 à 42 conditions."),
    ("P-49", "V1.1.1", N,
     "Le validateur de carte contrôle la couverture de tout locator cité et 35 conditions de façade.",
     "Le validateur de carte contrôle la couverture de tout locator cité et 42 conditions de façade."),
    ("P-50", "V1.1.1", C,
     "- **Textes normatifs.** Table de correspondance `VISUAL_TARGET` limitée aux champs de sa table ; droits inconnus (`ACCEPTED` interdit, réserve possible, diffusion après clearance) ;",
     "- **Textes normatifs.** Table de correspondance `VISUAL_TARGET` limitée aux champs de sa table ; droits inconnus (`ACCEPTED` interdit, réserve possible, diffusion après clearance, contrôle machine en `DIRECTION` seulement) ; `null` réservé aux champs qui l’admettent ;"),
    # ---------- R.03, seconde passe (revue T-01 à T-04) ----------
    ("P-53", "T-01", Q,
     "CHANGED — la composition mobile du premier rendu est abandonnée : l’objet visuel rejoint le titre et le CTA secondaire recule (observation : capture mobile 390). L’effet de la correction reste à réobserver.",
     "ABANDONED — la composition mobile du premier rendu est abandonnée : l’objet s’y sépare de la promesse et le CTA secondaire concurrence le premier geste (observation : capture mobile 390). La recomposition est décrite dans `CORRECTION` et reste à réobserver."),
    ("P-54", "T-02", A,
     "; un autre champ sans valeur est omis (par exemple `closure.direction_status` hors surface `DIRECTION`).",
     "; un champ facultatif sans valeur est omis (par exemple `closure.direction_status` hors surface `DIRECTION`), et un champ requis sans valeur suit sa règle propre (par exemple des ancres vides avec une issue non nulle)."),
    ("P-55", "T-02", MP,
     "il n’est admis que là où le schéma l’admet (`ACTION/RUN_CARD`), sinon le champ est omis.",
     "il n’est admis que là où le schéma l’admet (`ACTION/RUN_CARD`) ; ailleurs, un champ facultatif sans valeur est omis."),
    ("P-56", "T-03", S,
     "Si aucune décision n’est changée, confirmée ou abandonnée, retournez la triade d’`ACTION/STATUS` — `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée — et ne chargez pas une route supplémentaire.",
     "Si aucune décision ne peut changer, ne chargez pas une route supplémentaire. À la clôture, si aucune décision n’est changée, confirmée ou abandonnée, la triade d’`ACTION/STATUS` s’applique : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée."),
    ("P-57", "T-04", A,
     "| Réserves | Owner, périmètre, impact, date de revue, prochaine preuve et condition de sortie sont persistants. |",
     "| Réserves | Owner, périmètre, date ou version, impact, date de revue, prochaine preuve et condition de sortie sont persistants. |"),
    ("P-58", "T-04", A,
     "7. La réserve, si elle existe, possède-t-elle owner, périmètre, impact, date de revue, prochaine preuve et condition de sortie ?",
     "7. La réserve, si elle existe, possède-t-elle owner, périmètre, date ou version, impact, date de revue, prochaine preuve et condition de sortie ?"),
]

LCF_CODE = r'''
# ---------- R.03 (DG-AUDIT-001) : LCF-36 à LCF-42 ----------
NO_DECISION = re.compile(r"(?i)aucune décision (ne change|n’est changée|modifiée)")


def lcf_36(t: dict[str, str]) -> bool:
    l = next((x for x in t["A"].splitlines() if "Un droit inconnu" in x), "")
    return "que pour une `RUN_CARD` `DIRECTION`" in l and "contrôle seulement l’exclusion" not in l


def lcf_37(t: dict[str, str]) -> bool:
    seg = t["A"][t["A"].find("## ACTION/CLOSE-PACKAGE"):]
    rows = [l for l in seg[:seg.find("\n\n", seg.find("| Mode | Paquet minimal"))].splitlines() if l.startswith("| **")]
    return len(rows) == 5 and all("NOT-OBSERVED" in l for l in rows)


def lcf_38(t: dict[str, str]) -> bool:
    lines = [l for k in ("A", "D", "S", "B", "Q", "G", "SK", "EX") for l in t[k].splitlines()
             if NO_DECISION.search(l) and "N/A-JUSTIFIED" in l]
    sav = next((l for l in t["S"].splitlines() if l.startswith("La sortie de SAVOIR")), "")
    return (all("NOT-OBSERVED" in l or "non applicable" in l or "selon le contrat ACTION" in l for l in lines)
            and "À la clôture" in sav)


def lcf_39(t: dict[str, str]) -> bool:
    sec = t["Q"][t["Q"].find("## 5. Charger"):t["Q"].find("## 6.")]
    return all((r := row(sec, f"`{m}`")) and "ACTION/GATE-B" in r[1] for m in ("LITE", "ITER"))


def lcf_40(t: dict[str, str]) -> bool:
    closed = next((l for l in t["G"].splitlines() if l.startswith("| **CLOSED** |")), "")
    exit_rows = [l for l in t["A"].splitlines() if l.startswith("| Réserves |") or l.startswith("7. La réserve")]
    return "date ou version" in closed and len(exit_rows) == 2 and all("date ou version" in l for l in exit_rows)


def lcf_41(t: dict[str, str]) -> bool:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    found: list[str] = []

    def walk(node: object, path: list[str]) -> None:
        if isinstance(node, dict):
            enum, typ = node.get("enum"), node.get("type")
            if (isinstance(enum, list) and None in enum) or typ == "null" or (isinstance(typ, list) and "null" in typ):
                found.append(".".join(p for p in path if p not in ("properties", "run_card")))
            for key, value in node.items():
                walk(value, path + [key])
        elif isinstance(node, list):
            for value in node:
                walk(value, path)

    walk(schema.get("properties", {}), [])
    line = next((l for l in t["A"].splitlines() if "`null` signifie" in l), "")
    return (bool(found) and all(f"`{f}`" in line for f in found) and "champ facultatif sans valeur est omis" in line
            and "schéma l’admet" in t["MP"] and "champ facultatif sans valeur est omis" in t["MP"])


def lcf_42(t: dict[str, str]) -> bool:
    ex = t["Q"][t["Q"].find("## 9. Exemple complet minimal"):t["Q"].find("## 10.")]
    after = ex.split("DECISION-CHANGE:\n", 1)
    return (bool(ex) and not re.search(r"(?m)^CHANGE:", ex) and len(after) == 2
            and re.match(OUTCOME + r" — ", after[1]) is not None and "reste à réobserver" in after[1].split("\n\n")[0]
            and not after[1].startswith("CHANGED"))

'''

LCF_ROWS = '''        ("LCF-36", "ACTION, droits inconnus : portée du contrôle machine", "validate_run_card (rights_status, DIRECTION) ; Q-01", lcf_36(t)),
        ("LCF-37", "ACTION/CLOSE-PACKAGE, cinq paquets", "ACTION/STATUS (triade) ; validate_run_card (decision_change) ; Q-02", lcf_37(t)),
        ("LCF-38", "sources et façades : « aucune décision » et N/A-JUSTIFIED", "ACTION/STATUS (triade) ; Q-03", lcf_38(t)),
        ("LCF-39", "QUICKSTART §5, chargement LITE et ITER", "ACTION/PRECONDITION (Gate B du risque) ; Q-06", lcf_39(t)),
        ("LCF-40", "GLOSSAIRE, exemple CLOSED : réserve à sept attributs", "ACTION (réserve) ; RESERVATION_FIELDS ; Q-10", lcf_40(t)),
        ("LCF-41", "ACTION et machine_projection : champs admettant null", "schemas/run_card.schema.json ; O-1", lcf_41(t)),
        ("LCF-42", "QUICKSTART §9 : DECISION-CHANGE selon la triade", "ACTION/STATUS ; ACTION/HANDOFF ; Q-05", lcf_42(t)),
'''

PATCH += [
    ("P-51", "LCF", RM, "\ndef check_facades(errors: list[str]) -> None:\n", LCF_CODE + "\ndef check_facades(errors: list[str]) -> None:\n"),
    ("P-52", "LCF", RM,
     '        ("LCF-35", "GLOSSAIRE, exemple CLOSED", "ACTION (protection critique) ; B1", lcf_35(t)),\n',
     '        ("LCF-35", "GLOSSAIRE, exemple CLOSED", "ACTION (protection critique) ; B1", lcf_35(t)),\n' + LCF_ROWS),
]

MUTATION_OF = {"LCF-36": "P-37", "LCF-37": "P-38", "LCF-38": "P-40", "LCF-39": "P-44", "LCF-40": "P-45", "LCF-41": "P-46", "LCF-42": "P-42"}
# Seconde passe : les entrées P-53 à P-58 ont chacune leur mutation propre (R03_harnais, cas R3-15 à R3-19).
MUTATION_2 = {"LCF-42": "P-53", "LCF-41": "P-54", "LCF-38": "P-56", "LCF-40": "P-58"}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    if "--inverse" in sys.argv:
        pid = sys.argv[sys.argv.index("--inverse") + 1]
        problems = PR.apply(root, [e for e in PATCH if e[0] == pid], reverse=True)
    else:
        problems = PR.apply(root, PATCH, dry="--verifier" in sys.argv)
    for p in problems:
        print("ÉCHEC", p)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH) if '--inverse' not in sys.argv else 1} entrée(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
