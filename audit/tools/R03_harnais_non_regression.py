#!/usr/bin/env python3
"""DG-AUDIT-001 — R.03 mini-boucle du retour — harnais R03 (Q-01, Q-02, Q-03, Q-05, Q-06, Q-10, O-1).

Artefact d'audit HORS package. Lecture seule de la racine ; mutations sur copie.
Usage : python3 R03_harnais_non_regression.py <racine>
Reprend les aides du harnais R (R_harnais_non_regression.py) et le code des conditions de
DG_AUDIT_001_Patch_R03.py (dépendances déclarées ; les trois fichiers vont ensemble).
  R3-01 à R3-07  conditions de texte évaluées ici ;
  R3-08 à R3-14  LCF-36 à LCF-42 présentes dans validate_reading_map.py ET rouges sous mutation (inverse de l'entrée).
  R3-15 à R3-18  mutations propres aux entrées de la seconde passe (P-53, P-54, P-56, P-58).
Attendu sur B04@R.02-version-v1.1.1 (avant R.03) : 0/18. Après R.03 : 18/18 (plus le harnais R : 31/31).
"""
from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import DG_AUDIT_001_Patch_R01 as PR  # noqa: E402
import DG_AUDIT_001_Patch_R03 as P3  # noqa: E402
import R_harnais_non_regression as RH  # noqa: E402

OUTCOME = r"(CHANGED|CONFIRMED|ABANDONED|N/A-JUSTIFIED|NOT-OBSERVED)"
LABELS = {
    "LCF-36": ("Q-01", "droits inconnus : contrôle machine borné à la RUN_CARD DIRECTION"),
    "LCF-37": ("Q-02", "CLOSE-PACKAGE : les cinq paquets portent la conséquence décisionnelle (triade)"),
    "LCF-38": ("Q-03", "« aucune décision … » + N/A-JUSTIFIED : NOT-OBSERVED présent, non-applicabilité qualifiée ou renvoi au contrat ACTION"),
    "LCF-39": ("Q-06", "QUICKSTART §5 : Gate B chargé en LITE et ITER"),
    "LCF-40": ("Q-10", "GLOSSAIRE CLOSED : réserve à sept attributs (date ou version)"),
    "LCF-41": ("O-1", "null : champs du schéma qui l'admettent nommés ; sinon omission"),
    "LCF-42": ("Q-05", "QUICKSTART §9 : plus de « CHANGE: » ; DECISION-CHANGE selon la triade"),
}


def mutate(mut: Path, pid: str) -> list[str]:
    """Inverse l'entrée `pid` de R.03 ; si une entrée postérieure de R.03 a réécrit une partie de son texte,
    celle-ci est inversée d'abord (mutation équivalente sur patchs empilés)."""
    idx = next(i for i, e in enumerate(P3.PATCH) if e[0] == pid)
    entry = P3.PATCH[idx]
    later = [e for e in P3.PATCH[idx + 1:] if e[2] == entry[2] and e[3] in entry[4]]
    return PR.apply(mut, list(reversed(later)), reverse=True) or PR.apply(mut, [entry], reverse=True)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    t = RH.texts(src)
    t["B"] = (src / "V1/official/BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    ns = RH.conditions(src)
    ns["OUTCOME"] = OUTCOME
    exec(P3.LCF_CODE, ns)  # noqa: S102 — code des conditions décidé en R.03
    rows = []
    for n, (lcf, (point, label)) in enumerate(LABELS.items(), start=1):
        try:
            ok = bool(ns[f"lcf_{lcf[-2:]}"](t))
        except Exception as exc:
            ok, label = False, f"{label} [erreur : {exc!r}]"
        rows.append((f"R3-{n:02d}", point, label, ok))
    rm = (src / "scripts/validate_reading_map.py").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        for n, (lcf, (point, _)) in enumerate(LABELS.items(), start=8):
            present, sensitive = f'("{lcf}",' in rm, False
            if present:
                mut = RH.copy(src, Path(tmp) / f"mut_{lcf}")
                problems = mutate(mut, P3.MUTATION_OF[lcf])
                code, out = RH.run([sys.executable, "-B", "scripts/validate_reading_map.py"], mut)
                sensitive = not problems and code != 0 and f"{lcf} :" in out
            rows.append((f"R3-{n:02d}", point, f"{lcf} dans la liste close et rouge sous mutation ({P3.MUTATION_OF[lcf]} inversé)", present and sensitive))
        for n, (lcf, pid) in enumerate(P3.MUTATION_2.items(), start=15):
            present, sensitive = f'("{lcf}",' in rm, False
            if present:
                mut = RH.copy(src, Path(tmp) / f"mut2_{lcf}")
                problems = mutate(mut, pid)
                code, out = RH.run([sys.executable, "-B", "scripts/validate_reading_map.py"], mut)
                sensitive = not problems and code != 0 and f"{lcf} :" in out
            rows.append((f"R3-{n:02d}", "2e passe", f"{lcf} rouge sous mutation de la seconde passe ({pid} inversé)", present and sensitive))
    for cid, point, label, good in rows:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:6} {point:6} {label}")
    print(f"\nCas R03 : {sum(r[3] for r in rows)}/{len(rows)}")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
