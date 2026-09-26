#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.12 PATCH-DECISION C5 — harnais (façades lues seules, D-FAC-1 = c).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C5_harnais_non_regression.py <racine>

Deux parties :
  A. LISTE CLOSE DES CONDITIONS DE FAÇADE (LCF) — chaque entrée est évaluée directement sur les textes.
     C'est exactement ce que le test de cohérence (validate_reading_map.py étendu, F-VRM-003) devra vérifier.
  B. MUTATIONS DU VALIDATEUR — on réintroduit dans la copie la cellule fautive de B01 ; le validateur doit
     virer au rouge avec le motif « LCF-xx » (règle A2). Test de la fiche : « cellule qui rend facultative
     une route [FORCÉ] → rouge ».
Sur B01 : témoins 2/2 ; toutes les entrées LCF échouent ; les 6 mutations passent à tort (validateur vert).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HANDOFF_TOKENS = re.compile(r"\b(MODE|DECISION-CHANGE|DECISION|RISK|SCOPE|ARTIFACT|OBSERVATION|METHOD|TRACE-LOCATOR|NOT-VERIFIED|"
                            r"NEXT-ACTION|OWNER|NEXT-PROOF|EXIT-CONDITION)\b")
VISIBLE = "MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER"

# Cellules fautives de B01, réinjectées par les mutations (partie B).
B01_ROWS = {
    "RM33": "| Direction identitaire | `DIRECTION/START` → `DIRECTION/VISUAL_TARGET` | `DIRECTION/FIRST-OBJECT`, `SAVOIR/CRAFT`, `ACTION/RUN-DIRECTION` | Direction, objet, capture, écarts, preuve, limite |",
    "RM49": "| Accessibilité | Focus, clavier, sémantique, contraste, motion ou population critique | `SAVOIR/CONTEXT` + `ACTION/GATE-A` | Méthode, scope, résultat, limite | Risque explicitement hors scope et `N/A-JUSTIFIED` |",
    "OM20": "| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + contenu et états réels | `ACTION/GATE-A`, responsive, focus, récupération, runtime ou `SAVOIR/CONTEXT` selon le risque | Tâche, états, viewports, contenu extrême, clavier ou méthode adaptée au claim. |",
    "QS141": "| Première scène, identité, direction visuelle ou enjeu de craft dominant | `DIRECTION` | `DIRECTION/START`, `DIRECTION/VISUAL_TARGET`, `SAVOIR/CRAFT — CFT-00`, puis `ACTION/RUN-DIRECTION`. |",
    "RDR46": "| Amélioration guidée par une observation | `ITER` | La correction doit modifier l’artefact ou la décision. |",
}


def read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def row(text: str, key: str) -> list[str] | None:
    """Cellules de la première ligne de tableau dont la première cellule contient `key`."""
    for line in text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and key in cells[0]:
                return cells
    return None


def row_where(text: str, col: int, key: str) -> list[str] | None:
    for line in text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) > col and key in cells[col]:
                return cells
    return None


def before(text: str, a: str, b: str) -> bool:
    return a in text and b in text and text.index(a) < text.index(b)


def block_after(text: str, marker: str, length: int = 1200) -> str:
    i = text.find(marker)
    return text[i:i + length] if i >= 0 else ""


def fenced_after(text: str, marker: str) -> str:
    i = text.find(marker)
    if i < 0:
        return ""
    m = re.search(r"```(?:text)?\n(.*?)```", text[i:], re.S)
    return m.group(1) if m else ""


def lcf(root: Path):
    D = read(root, "V1/official/DIRECTION.md")
    A = read(root, "V1/official/ACTION.md")
    RM = read(root, "V1/official/READING_MAP.md")
    OM = read(root, "V1/official/ORCHESTRATION_MAP.md")
    QS = read(root, "V1/official/QUICKSTART.md")
    RD = read(root, "README.md")
    SK = read(root, "skills/design-governance-practice/SKILL.md")
    out = []

    r = row(RM, "Direction identitaire")
    out.append(("LCF-01", "F-RM-001", "READING_MAP : ACTION/RUN-DIRECTION dans la première lecture de « Direction identitaire », pas dans l'optionnel",
                bool(r) and "ACTION/RUN-DIRECTION" in r[1] and "ACTION/RUN-DIRECTION" not in r[2]))
    r = row(RM, "Accessibilité")
    out.append(("LCF-02", "F-RM-002", "READING_MAP : le non-chargement d'accessibilité ne produit pas de N/A et renvoie aux contrôles ACTION/GATE-A",
                bool(r) and "N/A-JUSTIFIED" not in r[-1] and "ACTION/GATE-A" in r[-1]))
    ui, pr, sy = row(OM, "UI/UX habitable"), row(OM, "Preuve et décision fiables"), row(OM, "Système maintenable")
    ok3 = (bool(ui) and "ACTION/GATE-A" in ui[1] and "ACTION/GATE-A" not in ui[2]
           and bool(pr) and re.search(r"(?i)gate", pr[1]) is not None and re.search(r"(?i)gate", pr[2]) is None
           and bool(sy) and all(k in sy[1] for k in ("migration", "rollback", "CHANGELOG")) and not any(k in sy[2] for k in ("migration", "rollback", "CHANGELOG")))
    out.append(("LCF-03", "F-OM-001", "ORCHESTRATION_MAP : Gate A, gate du risque et paquet SYSTÈME dans le noyau, pas dans le renforcement", ok3))
    q, rd = row_where(QS, 1, "`DIRECTION`"), row_where(RD, 1, "`DIRECTION`")
    out.append(("LCF-04", "F-QS-002", "QUICKSTART et README : le mode DIRECTION n'est pas classé par le craft ; critère de START (autonome)",
                bool(q) and bool(rd) and all("craft" not in c[0].lower() and "autonome" in c[0] for c in (q, rd))))
    it = row_where(RD, 1, "`ITER`")
    out.append(("LCF-05", "F-RDR-001", "README : ITER exige une direction existante et retrouvable", bool(it) and re.search(r"(?i)direction[^|]*(retrouvable|existante)", it[0]) is not None))
    ix = row(D, "Nouvelle structure d’écran")
    out.append(("LCF-06", "F-DIR-041", "DIRECTION, index : aucune présélection de STANDARD pour une nouvelle structure", bool(ix) and "classification `ACTION/RUN-STANDARD`" not in ix[1]))
    chain = block_after(D, "**Chaîne de lecture interne.**", 700)
    # 12.05c R-12 : le marqueur visait la première occurrence de « RUN-PRIORITY », qui est la première ligne du bloc ; la recherche du bloc partait donc de sa clôture
    prio = fenced_after(D, "```text\nRUN-PRIORITY")
    rm33 = row(RM, "Direction identitaire")
    om17 = row(OM, "Direction forte et spécifique")
    sk82 = row_where(SK, 0, "`DIRECTION`")
    ok7 = (before(chain, "`VISUAL_TARGET`", "`FIRST-OBJECT`") and before(prio, "DIRECTION —", "FIRST-OBJECT —")
           and bool(rm33) and before(" ".join(rm33), "VISUAL_TARGET", "FIRST-OBJECT")
           and bool(om17) and before(" ".join(om17), "VISUAL_TARGET", "FIRST-OBJECT")
           and bool(sk82) and before(" ".join(sk82), "VISUAL_TARGET", "FIRST-OBJECT"))
    out.append(("LCF-07", "F-DIR-001", "séquence causale cible → premier objet (DIRECTION 72, RUN-PRIORITY, READING_MAP, ORCHESTRATION_MAP, skill)", ok7))
    entry = block_after(D, "Ce gabarit est une vue d’activation", 600)
    fp = row(D, "Quel est le risque dominant ?")
    out.append(("LCF-08", "F-DIR-008", "OWNER et SCOPE exclus de la règle d'omission (START, FAST-PATH)",
                re.search(r"`?OWNER`? et `?SCOPE`?[^.]*jamais omis", entry) is not None and bool(fp) and "si nécessaire" not in fp[1]))
    out.append(("LCF-09", "F-DIR-018", "RUN-PRIORITY : premier objet avant le générique, sauf si navigation, recherche ou cartes sont l'objet de preuve",
                bool(re.search(r"FIRST-OBJECT —[\s\S]*?sauf si", prio))))
    out.append(("LCF-10", "D-FAC-1", "tables de mode (QUICKSTART, README) marquées « classement : voir DIRECTION/START »",
                all(re.search(r"(?i)classement\s*:\s*voir `DIRECTION/START`", t) for t in (QS, RD))))
    canon = HANDOFF_TOKENS.findall(fenced_after(A, "### ACTION/HANDOFF"))
    rmh = HANDOFF_TOKENS.findall(fenced_after(RM, "## Handoff minimal commun"))
    skh = HANDOFF_TOKENS.findall(block_after(SK, "## Carte de lecture et sortie", 2500))
    out.append(("LCF-C1", "F-SK-001 (C3)", f"copies du handoff = canon ACTION/HANDOFF (canon {len(canon)} jetons ; READING_MAP {len(rmh)}, même ordre ; skill : tous présents)",
                bool(canon) and rmh == canon and all(tok in skh for tok in canon)))
    out.append(("LCF-C2", "F-SK-001 (C3)", "réponse visible : canon dans ACTION/HANDOFF, copies identiques (QUICKSTART, skill)",
                all(VISIBLE in t for t in (block_after(A, "### ACTION/HANDOFF", 3000), QS, SK))))
    return out


def run_vrm(root: Path):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/validate_reading_map.py")], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def replace_row(root: Path, rel: str, key: str, bad: str, col: int = 0):
    p = root / rel
    lines = p.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) > col and key in cells[col]:
                lines[i] = bad
                break
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def mutations(root: Path):
    cases = [
        ("M-1", "F-RM-001 / F-VRM-003", "RUN-DIRECTION [FORCÉ] redevient facultative dans READING_MAP", "V1/official/READING_MAP.md", "Direction identitaire", B01_ROWS["RM33"], 0, "LCF-01"),
        ("M-2", "F-RM-002", "le non-chargement d'accessibilité redevient N/A-JUSTIFIED", "V1/official/READING_MAP.md", "Accessibilité", B01_ROWS["RM49"], 0, "LCF-02"),
        ("M-3", "F-OM-001", "Gate A repasse en « renforcement seulement si nécessaire »", "V1/official/ORCHESTRATION_MAP.md", "UI/UX habitable", B01_ROWS["OM20"], 0, "LCF-03"),
        ("M-4", "F-QS-002", "le craft redevient critère du mode DIRECTION (QUICKSTART)", "V1/official/QUICKSTART.md", "`DIRECTION`", B01_ROWS["QS141"], 1, "LCF-04"),
        ("M-5", "F-RDR-001", "ITER perd la condition de direction retrouvable (README)", "README.md", "`ITER`", B01_ROWS["RDR46"], 1, "LCF-05"),
    ]
    rows = []
    for cid, fiche, label, rel, key, bad, col, motive in cases:
        p = root / rel
        old = p.read_text(encoding="utf-8")
        replace_row(root, rel, key, bad, col)
        ok, out = run_vrm(root)
        p.write_text(old, encoding="utf-8")
        rows.append((cid, fiche, label, (not ok) and motive in out, out.splitlines()[-1] if out else ""))
    # M-6 : une copie de handoff perd un champ (skill)
    p = root / "skills/design-governance-practice/SKILL.md"
    old = p.read_text(encoding="utf-8")
    # 12.05c R-14 : la copie décidée (C3 T-5) recopie le canon en bloc de code, sans accents graves ; la mutation vise le jeton, avec ou sans accents graves
    p.write_text(old.replace("EXIT-CONDITION", "CONDITION", 1), encoding="utf-8")
    ok, out = run_vrm(root)
    p.write_text(old, encoding="utf-8")
    rows.append(("M-6", "F-SK-001 (C3)", "une copie du handoff perd un champ (skill)", (not ok) and "LCF-C1" in out, out.splitlines()[-1] if out else ""))
    return rows


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        ok, out = run_vrm(root)
        t = [("T-POS-1", "témoin", "validate_reading_map sur la copie non modifiée → PASS", ok, out.splitlines()[-1] if out else "")]
        r = subprocess.run([sys.executable, "-B", str(root / "scripts/read_route.py"), "DIRECTION/START"], capture_output=True, text=True)
        t.append(("T-POS-2", "témoin", "lecteur de routes opérationnel", r.returncode == 0, "DIRECTION/START"))
        a = lcf(root)
        m = mutations(root)
    for cid, fiche, label, good, msg in t + m:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:22} {label}  [{msg[:60]}]")
    for cid, fiche, label, good in a:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:22} {label}")
    print(f"\nTémoins : {sum(x[3] for x in t)}/{len(t)} ; conditions LCF : {sum(x[3] for x in a)}/{len(a)} ; mutations au rouge : {sum(x[3] for x in m)}/{len(m)}")
    return 0 if all(x[3] for x in t + a + m) else 1


if __name__ == "__main__":
    sys.exit(main())
