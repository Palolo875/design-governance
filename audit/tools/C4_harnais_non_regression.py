#!/usr/bin/env python3
"""DG-AUDIT-001 — 11.11 PATCH-DECISION C4 — harnais (accès, locators et chargement).

Artefact d'audit HORS package ; copie temporaire ; lecture seule des sources.
Usage : python3 C4_harnais_non_regression.py <racine>

Quatre parties :
  1. RUN_CARD, profils normal et strict (validate_run_card.validate_card) — INV-C4-1 (ITER ⇒ trace_locator),
     INV-C4-2 (strict : mêmes exigences de mode que le normal ; LITE peut s'appuyer sur artifact.locator ;
     locator local relatif résolu depuis le dossier de la carte). Cartes construites sur la forme APRÈS B1–C2.
  2. RÉSOLUTION (scripts/read_route.py, appelé comme un lecteur outillé) — couverture des locators cités,
     carte de chargement d'ACTION, sous-locators, exclusion des sous-blocs porteurs d'un autre locator,
     unicité des titres porteurs de locator, coût de la route LITE.
  3. VALIDATEUR DE CARTE (scripts/validate_reading_map.py) — mutations qui doivent virer au rouge, avec motif.
  4. GARDES TEXTUELLES — carte de lecture d'ACTION, skill, READING_MAP, profil strict documenté.
Règle A2 : chaque négatif exige son motif (sous-chaîne indicative du diagnostic).
Sur B01 : témoins 3/3 ; tous les autres cas échouent (défauts présents).
"""
from __future__ import annotations

import copy
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PREFIXES = ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG")
CITED = re.compile(r"`((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE|CHANGELOG)/[A-Z0-9_\-]+(?:/[A-Z0-9_\-]+)?)`")
ACTION_MAP = ["ACTION/STATUS", "ACTION/PRECONDITION", "ACTION/RUN-LITE", "ACTION/RUN-ITER", "ACTION/RUN-STANDARD",
              "ACTION/RUN-DIRECTION", "ACTION/RUN-SYSTEM", "ACTION/PIPELINE-DIRECTION", "ACTION/VISUAL_PROOF",
              "ACTION/GATE-A", "ACTION/GATE-B", "ACTION/GATE-C", "ACTION/RUN_CARD", "ACTION/CLOSE-PACKAGE",
              "ACTION/CLOSE-EXIT-CHECK"]
LITE_ROUTE = ["DIRECTION/START/TREE", "ACTION/RUN-LITE", "ACTION/FAST-PATH"]
LITE_BUDGET = 60            # B01 : 158 lignes servies (START entier + RUN-LITE + FAST-PATH)
START_BUDGET = 76           # B01 : 130 lignes (Boot et Domain Frame inclus) ; 12.06 R-15 : 75 → 76 sur décision de l'owner (séparateur de fin de section)
TREE_BUDGET = 25            # arbre utile : 19 lignes


# ---------- 1. RUN_CARD ----------
def load(root: Path):
    spec = importlib.util.spec_from_file_location("vrc", root / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    schema = json.loads((root / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    fx = json.loads((root / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8"))
    return m, schema, fx


def card(fx, mode, *, trace=True, artifact="captures/v1.png"):
    """Carte clôturée en RETURN (aucune acceptation : les invariants B2–B4 ne s'appliquent pas), forme après B1–C2."""
    d = copy.deepcopy(fx)
    c = d["run_card"]
    c["mode"] = mode
    c["risk"] = {"level": "normal", "critical_protection": None, "statement": "Libellé tronqué sur mobile dans la carte d'alerte"}
    c["decision_change"] = {"outcome": "CHANGED", "value": c["decision_change"]["value"], "evidence": c["decision_change"]["evidence"]}
    c["artifact"]["locator"] = artifact
    if mode == "ITER":  # 12.04 R-9 : INV-D2-2 (décidé après C4) exige le rappel de direction d'un ITER
        c["direction"] = {"thesis": "La hiérarchie existante est conservée."}
    if trace:
        c["trace_locator"] = "tickets/run-044.md"
    else:
        c.pop("trace_locator", None)
    return d


def run_card_cases(tmp: Path, fx):
    cap = tmp / "cartes" / "captures"
    cap.mkdir(parents=True)
    (cap / "v1.png").write_bytes(b"png")
    (tmp / "cartes" / "tickets").mkdir()
    (tmp / "cartes" / "tickets" / "run-044.md").write_text("trace", encoding="utf-8")
    abs_art = f"file://{cap / 'v1.png'}"
    return [
        # id, fiche, libellé, document, strict, attendu, motif
        ("C4-01", "F-ACT-020", "normal : ITER sans trace_locator", card(fx, "ITER", trace=False, artifact=abs_art), False, "neg", "ITER exige trace_locator"),
        ("C4-02", "F-ACT-020", "strict : LITE sans trace, artefact local absent", card(fx, "LITE", trace=False, artifact="captures/absent.png"), True, "neg", "artefact local absent"),
        ("C4-P1", "F-ACT-020", "normal : LITE sans trace_locator (l'artefact sert de locator) → acceptée", card(fx, "LITE", trace=False, artifact=abs_art), False, "pos", None),
        ("C4-P2", "F-ACT-020", "strict : même LITE sans trace_locator, artefact présent → acceptée", card(fx, "LITE", trace=False, artifact=abs_art), True, "pos", None),
        ("C4-P3", "F-ACT-020", "strict : STANDARD, locator relatif résolu depuis le dossier de la carte → acceptée", card(fx, "STANDARD"), True, "pos", None),
        ("C4-P4", "F-ACT-020", "normal : ITER avec trace_locator → acceptée", card(fx, "ITER", artifact=abs_art), False, "pos", None),
    ]


def verdict_card(m, schema, d, strict, path):
    try:
        m.validate_card(d, schema, strict=strict, source_path=path)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
        return False, f"EXCEPTION {type(e).__name__}: {e}"


# ---------- 2. Résolution ----------
def serve(root: Path, loc: str):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/read_route.py"), loc], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout if r.returncode == 0 else (r.stderr or r.stdout))


def cited_locators(root: Path) -> list[str]:
    files = list((root / "V1/official").glob("*.md")) + [root / "skills/design-governance-practice/SKILL.md"]
    found = set()
    for f in files:
        found.update(CITED.findall(f.read_text(encoding="utf-8")))
    return sorted(found)


def duplicate_heading_locators(root: Path) -> list[str]:
    seen, dup = {}, []
    for p in PREFIXES:
        f = root / "V1/official" / f"{p}.md"
        in_code = False
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("```"):
                in_code = not in_code
            if in_code or not line.startswith("#"):
                continue
            m = re.match(rf"#+\s+`?({p}/[A-Za-z0-9_\-]+)`?(?:\s|$)", line)
            if m:
                (dup.append(m.group(1)) if m.group(1) in seen else seen.__setitem__(m.group(1), line))
    return dup


def resolution_cases(root: Path):
    rows = []
    cited = cited_locators(root)
    unresolved = [c for c in cited if not serve(root, c)[0]]
    rows.append(("R-01", "F-DIR-028", f"tout locator cité est servi ({len(cited) - len(unresolved)}/{len(cited)})"
                 + (f" ; refusés : {', '.join(unresolved[:6])}{'…' if len(unresolved) > 6 else ''}" if unresolved else ""), not unresolved))
    miss = [c for c in ACTION_MAP if not serve(root, c)[0]]
    rows.append(("R-02", "F-ACT-001", f"carte de chargement d'ACTION résoluble ({len(ACTION_MAP) - len(miss)}/{len(ACTION_MAP)})"
                 + (f" ; refusés : {', '.join(miss)}" if miss else ""), not miss))
    ok, out = serve(root, "DIRECTION/START/TREE")
    n = len(out.splitlines()) if ok else 0
    rows.append(("R-03", "F-RM-003", f"DIRECTION/START/TREE servi en ≤ {TREE_BUDGET} lignes ({n if ok else 'refusé'})", ok and n <= TREE_BUDGET and "Arbre" in out))
    ok, out = serve(root, "DIRECTION/START")
    n = len(out.splitlines()) if ok else 0
    rows.append(("R-04", "F-RM-003", f"DIRECTION/START n'embarque plus CREATIVE-BOOT ni DOMAIN-FRAME (≤ {START_BUDGET} lignes ; {n})",
                 ok and n <= START_BUDGET and "### DIRECTION/CREATIVE-BOOT" not in out and "### DIRECTION/DOMAIN-FRAME" not in out and "### Sortie immédiate" in out))
    total, refused = 0, []
    for loc in LITE_ROUTE:
        ok, out = serve(root, loc)
        total += len(out.splitlines()) if ok else 0
        refused += [] if ok else [loc]
    rows.append(("R-05", "F-RM-003", f"route LITE servie en ≤ {LITE_BUDGET} lignes ({total}{' ; refusés : ' + ', '.join(refused) if refused else ''})", not refused and total <= LITE_BUDGET))
    ok, out = serve(root, "SAVOIR/CRAFT/CFT-01")
    rows.append(("R-06", "F-RM-003", "sous-locator hiérarchique SAVOIR/CRAFT/CFT-01 servi seul", ok and "## CFT-01" in out and "## CFT-02" not in out))
    dup = duplicate_heading_locators(root)
    rows.append(("R-07", "F-VRM-001", "aucun locator porté par deux titres" + (f" (en double : {', '.join(dup)})" if dup else ""), not dup))
    return rows


# ---------- 3. Validateur de carte ----------
def run_vrm(root: Path):
    r = subprocess.run([sys.executable, "-B", str(root / "scripts/validate_reading_map.py")], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr)


def mutate(root: Path, name: str, fn):
    p = root / name
    old = p.read_text(encoding="utf-8")
    p.write_text(fn(old), encoding="utf-8")
    try:
        return run_vrm(root)
    finally:
        p.write_text(old, encoding="utf-8")


def vrm_cases(root: Path):
    rm = "V1/official/READING_MAP.md"
    lite_row = next(l for l in (root / rm).read_text(encoding="utf-8").splitlines() if l.startswith("| `ACTION/RUN-LITE`"))
    cases = [
        ("V-01", "F-VRM-001", "RUN-LITE ouvre le titre de RUN-ITER", rm, lambda t: t.replace(lite_row, lite_row.replace("RUN-LITE\\`", "RUN-ITER\\`")), "ne correspond pas au locator"),
        ("V-02", "F-VRM-001", "même locator listé deux fois", rm, lambda t: t.replace(lite_row, lite_row + "\n" + lite_row), "locator en double"),
        ("V-03", "F-VRM-001", "titre propriétaire renommé : ACTION/STATUS cité mais plus résoluble", "V1/official/ACTION.md",
         lambda t: t.replace("## ACTION/STATUS — états, issues et verdicts", "## Statuts — états, issues et verdicts"), "locator cité non résolu"),
        ("V-04", "F-VRM-001", "locator ACTION/… pointant vers DIRECTION.md", rm,
         lambda t: t.replace("| `ACTION/FIRST-RENDER` | `ACTION.md` — `## ACTION/FIRST-RENDER — qualité initiale attendue` |",
                             "| `ACTION/FIRST-RENDER` | `DIRECTION.md` — `## DIRECTION/START — classer avant d’agir` |"), "propriétaire incohérent"),
    ]
    rows = []
    ok, out = run_vrm(root)
    rows.append(("T-POS-3", "témoin", "carte non modifiée → PASS", ok, out.strip().splitlines()[-1] if out.strip() else ""))
    for cid, fiche, label, name, fn, motive in cases:
        ok, out = mutate(root, name, fn)
        rows.append((cid, fiche, label, (not ok) and motive in out, (out.strip().splitlines() or [""])[-1]))
    return rows


# ---------- 4. Gardes textuelles ----------
def text_guards(root: Path):
    off = root / "V1/official"
    a = (off / "ACTION.md").read_text(encoding="utf-8")
    rmap = (off / "READING_MAP.md").read_text(encoding="utf-8")
    sk = (root / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8")
    carte = a[a.find("### Carte de lecture par mode"):a.find("### ACTION/HANDOFF")]
    rows_modes = [l for l in carte.splitlines() if re.match(r"\| `(LITE|ITER|STANDARD|DIRECTION|SYSTÈME)`", l)]
    socle = bool(re.search(r"(?i)(tous les modes|chaque mode|socle)[^\n]*STATUS[^\n]*PRECONDITION|STATUS[^\n]*PRECONDITION[^\n]*(tous les modes|chaque mode)", carte))
    all_rows = len(rows_modes) == 5 and all("STATUS" in l and "PRECONDITION" in l for l in rows_modes)
    resp = a[a.find("## Responsabilité"):a.find("### Carte de lecture par mode")]
    return [
        ("G-01", "F-ACT-001", "carte d'ACTION : STATUS et PRECONDITION chargés pour les cinq modes", socle or all_rows),
        ("G-02", "F-ACT-001", "« commencez par `ACTION/RUN` » (locator sans titre) remplacé par des locators résolubles", "commencez par `ACTION/RUN`," not in resp),
        ("G-03", "F-ACT-001 / C2", "carte d'ACTION : la colonne « Sortie à conserver » cède la place au renvoi CLOSE-PACKAGE",
         "Sortie à conserver" not in carte and "CLOSE-PACKAGE" in carte),
        ("G-04", "F-RM-003", "READING_MAP liste le sous-locator DIRECTION/START/TREE", "`DIRECTION/START/TREE`" in rmap),
        ("G-05", "F-RM-003", "skill : « arbre seulement » exprimé par le locator DIRECTION/START/TREE", "DIRECTION/START/TREE" in sk and "(arbre seulement)" not in sk),
        ("G-06", "F-DIR-028", "READING_MAP décrit la résolution par préfixe, sous-locator et refus d'ambiguïté", bool(re.search(r"(?i)ambigu", rmap))),
        ("G-07", "F-ACT-020", "ACTION documente le profil strict (mêmes exigences par mode ; contrôles ajoutés)", bool(re.search(r"(?i)profil strict", a))),
    ]


def judge(kind, motive, ok, msg):
    return ok if kind == "pos" else (not ok and motive in msg and not msg.startswith("EXCEPTION"))


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory() as tmpd:
        tmp = Path(tmpd)
        root = tmp / "pkg"
        shutil.copytree(src, root, ignore=shutil.ignore_patterns("__pycache__", ".build", "dist", "*.zip"))
        m, schema, fx = load(root)
        ex = json.loads((root / "schemas/run_card.example.json").read_text(encoding="utf-8"))
        rows = [("T-POS-1", "B01", "exemple canonique RUN_CARD accepté (normal)", *verdict_card(m, schema, ex, False, None))]
        ok, route = serve(root, "DIRECTION/START")
        rows.append(("T-POS-2", "B01", "DIRECTION/START servi par le lecteur", ok, f"{len(route.splitlines())} lignes"))
        for cid, fiche, label, doc, strict, kind, motive in run_card_cases(tmp, fx):
            path = tmp / "cartes" / f"{cid}.json"
            path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
            ok, msg = verdict_card(m, schema, doc, strict, path)
            rows.append((cid, fiche, label, judge(kind, motive, ok, msg), msg))
        res = resolution_cases(root)
        vrm = vrm_cases(root)
        guards = text_guards(root)
    for cid, fiche, label, good, msg in rows + vrm:
        print(f"{'OK  ' if good else 'ÉCHEC'} {cid:7} {fiche:14} {label}  [{str(msg)[:70]}]")
    for gid, fiche, label, good in res + guards:
        print(f"{'OK  ' if good else 'ÉCHEC'} {gid:7} {fiche:14} {label}")
    t = [r for r in rows + vrm if r[0].startswith("T")]
    c = [r for r in rows if r[0].startswith("C4")]
    v = [r for r in vrm if r[0].startswith("V")]
    print(f"\nTémoins : {sum(r[3] for r in t)}/{len(t)} ; RUN_CARD C4 : {sum(r[3] for r in c)}/{len(c)} ; résolution : {sum(r[3] for r in res)}/{len(res)} ; "
          f"validateur de carte : {sum(r[3] for r in v)}/{len(v)} ; gardes : {sum(g[3] for g in guards)}/{len(guards)}")
    return 0 if all(r[3] for r in t + c + v) and all(r[3] for r in res + guards) else 1


if __name__ == "__main__":
    sys.exit(main())
