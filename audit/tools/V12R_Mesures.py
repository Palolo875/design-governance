#!/usr/bin/env python3
"""V1.2 refonte — R1 — Mesures homogènes du package (outil d'audit HORS package, lecture seule).

Usage :
  python3 V12R_Mesures.py <racine_package> [--json <sortie.json>]

Quatre mesures, toutes déterministes :
  1. BUDGET : mots et lignes lus par un run DIRECTION sur trois périmètres (ACTUEL, TABLE, LETTRE),
     définis dans audit/data/V12R/V12R_perimetres.json ; chaque élément doit être justifié par une
     citation présente dans le package, sinon il est signalé PÉRIMÉ.
  2. ATTEIGNABILITÉ : les 25 outils de fabrication (audit/data/V12R/V12R_outils_fabrication.json)
     sont-ils dans le texte lu, par périmètre ?
  3. INDICATEURS par fichier, avec une seule méthode de comptage : mots, négations défensives,
     formules d'auto-limitation, jetons internes distincts, champs de trace en blocs de code, « beau ».
  4. DOUBLONS : phrases ou lignes de table quasi identiques (3-grammes de mots ; Jaccard ≥ 0,5 ou
     inclusion ≥ 0,8 ; au moins 8 mots), dans des fichiers différents ou à plus de 5 lignes d'écart,
     regroupées en amas.
  5. LISTES DE CHARGEMENT : les listes « première lecture » d'un run DIRECTION déclarées par chaque
     façade (audit/data/V12R/V12R_listes_chargement.json) ; nombre de listes distinctes.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "V12R"
MD_FILES = ["V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md",
            "V1/official/BIBLIOTHEQUE.md", "V1/official/CHANGELOG.md", "V1/official/QUICKSTART.md",
            "V1/official/README.md", "README.md", "V1/official/GLOSSAIRE.md", "V1/official/READING_MAP.md",
            "V1/official/ORCHESTRATION_MAP.md", "skills/design-governance-practice/SKILL.md",
            "skills/design-governance-practice/references/examples.md",
            "skills/design-governance-practice/references/flow.md",
            "skills/design-governance-practice/references/canonical_minimum.md",
            "skills/design-governance-practice/references/machine_projection.md"]

NEG = re.compile(r"\b(?:ne|n[’'])\s*[^.;:!?]{0,60}?\b(?:pas|jamais|ni|aucun|aucune)\b", re.I)
AUTO = re.compile(r"ne (?:crée|créent|constitue|constituent|remplace|remplacent|devient|deviennent|transforme)\b"
                  r"|non normati|font foi|n[’']ajoute aucun|aucune règle|ni mode, ni", re.I)
TOKEN = re.compile(r"`([A-Z][A-Z0-9_/\-]{2,}[^`]*)`")
FIELD = re.compile(r"^\s*\[?([A-Z][A-Z0-9 /’'ÉÈ\-]+?)(?::| —)")
BEAU = re.compile(r"\bbeau(?:té|x)?\b|\bbelle\b", re.I)


COMPILED = re.compile(r"<!-- noyau:compilé début -->.*?<!-- noyau:compilé fin -->", re.S)


def own_text(t: str) -> str:
    """Texte propre d'un fichier : la section compilée de la skill (copie générée des sources) est exclue
    des indicateurs et des doublons ; le budget, lui, la compte, puisqu'elle est lue."""
    return COMPILED.sub("", t)


def words(t: str) -> int:
    return len(t.split())


def route_text(root: Path, route: str) -> str:
    p = subprocess.run([sys.executable, "-B", str(root / "scripts" / "read_route.py"), route],
                       capture_output=True, text=True, cwd=root)
    if p.returncode != 0:
        return ""
    return p.stdout


def item_text(root: Path, it: dict) -> tuple[str, str]:
    if "file" in it:
        return it["file"], (root / it["file"]).read_text(encoding="utf-8")
    return it["route"], route_text(root, it["route"])


def check_why(root: Path, items: list[dict]) -> list[str]:
    stale, last = [], None
    for it in items:
        why = it.get("why")
        if why == "idem":
            why = last
        last = why
        if not why:
            continue
        f, quote = why
        if quote not in (root / f).read_text(encoding="utf-8"):
            stale.append(f"{it.get('file') or it.get('route')} : citation introuvable dans {f}")
    return stale


def budget(root: Path) -> dict:
    per = json.loads((DATA / "V12R_perimetres.json").read_text(encoding="utf-8"))
    sets = {"ACTUEL": per["ACTUEL"], "TABLE": per["TABLE"], "LETTRE": per["TABLE"] + per["LETTRE_EN_PLUS"]}
    if per.get("TRACE_COMPLETE_EN_PLUS"):  # R5b-1 : trace complète (run persistant, partagé ou audité)
        sets["COMPLET"] = sets["LETTRE"] + per["TRACE_COMPLETE_EN_PLUS"]
    out = {}
    for name, items in sets.items():
        detail, text = [], []
        for it in items:
            label, t = item_text(root, it)
            detail.append((label, len(t.splitlines()), words(t), bool(t)))
            text.append(t)
        out[name] = {"elements": detail, "lignes": sum(d[1] for d in detail), "mots": sum(d[2] for d in detail),
                     "texte": "\n".join(text), "introuvables": [d[0] for d in detail if not d[3]],
                     "perimes": check_why(root, items)}
    return out


def reach(budgets: dict) -> dict:
    tools = json.loads((DATA / "V12R_outils_fabrication.json").read_text(encoding="utf-8"))["outils"]
    res = {}
    for name, b in budgets.items():
        t = b["texte"].replace("**", "")
        res[name] = {x["id"]: (x["ancre"] in t) for x in tools}
    return {"outils": {x["id"]: x["nom"] for x in tools}, "par_perimetre": res}


def indicators(root: Path) -> dict:
    out = {}
    for f in MD_FILES:
        t = own_text((root / f).read_text(encoding="utf-8"))
        fields, fence = set(), False
        for line in t.splitlines():
            if line.lstrip().startswith("```"):
                fence = not fence
                continue
            if fence:
                m = FIELD.match(line)
                if m:
                    fields.add(m.group(1).strip())
        out[f] = {"lignes": len(t.splitlines()), "mots": words(t), "negations": len(NEG.findall(t)),
                  "auto_limitation": len(AUTO.findall(t)), "jetons": len(set(TOKEN.findall(t))),
                  "champs_trace": len(fields), "beau": len(BEAU.findall(t))}
    tot = defaultdict(int)
    for v in out.values():
        for k, n in v.items():
            tot[k] += n
    out["TOTAL"] = dict(tot)
    return out


def norm(s: str) -> list[str]:
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"[`*_|#>]", " ", s)
    s = re.sub(r"[^\w’'\-→]+", " ", s)
    return s.split()


def paragraphs(root: Path) -> list[tuple[str, int, str]]:
    paras = []
    for f in MD_FILES:
        lines = own_text((root / f).read_text(encoding="utf-8")).splitlines()
        buf, start, fence = [], 0, False
        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                fence = not fence
            if line.lstrip().startswith("|"):
                if buf:
                    paras.append((f, start, " ".join(buf)))
                    buf = []
                if not re.match(r"^\s*\|[\s\-:|]+\|\s*$", line):
                    paras.append((f, i, line))
                continue
            if not line.strip():
                if buf:
                    paras.append((f, start, " ".join(buf)))
                buf = []
                continue
            if not buf:
                start = i
            buf.append(line)
        if buf:
            paras.append((f, start, " ".join(buf)))
    return paras


SENT = re.compile(r"(?<=[.;!?])\s+(?=[A-ZÀ-Ý«`*])")


def units(root: Path) -> list[tuple[str, int, str]]:
    """Phrases des paragraphes, et lignes de table entières."""
    out = []
    for f, line, text in paragraphs(root):
        if text.lstrip().startswith("|") or text.lstrip().startswith("```"):
            out.append((f, line, text))
        else:
            out.extend((f, line, s) for s in SENT.split(text))
    return out


def duplicates(root: Path, minw: int = 8) -> list[dict]:
    """Paires de phrases ou de lignes de table quasi identiques : Jaccard ≥ 0,5 ou inclusion ≥ 0,8
    (3-grammes de mots), dans des fichiers différents ou à plus de 5 lignes d'écart ; regroupées en amas."""
    us = [u for u in units(root) if len(norm(u[2])) >= minw]
    sh = []
    for u in us:
        w = norm(u[2])
        sh.append({" ".join(w[i:i + 3]) for i in range(len(w) - 2)})
    index = defaultdict(list)
    for k, s_ in enumerate(sh):
        for g in s_:
            index[g].append(k)
    shared = defaultdict(int)
    for ks in index.values():
        if len(ks) > 60:
            continue
        for a in range(len(ks)):
            for b in range(a + 1, len(ks)):
                shared[(ks[a], ks[b])] += 1
    parent = list(range(len(us)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    pairs = []
    for (a, b), n in shared.items():
        ja = n / (len(sh[a]) + len(sh[b]) - n)
        inc = n / min(len(sh[a]), len(sh[b]))
        ua, ub = us[a], us[b]
        if (ja >= 0.5 or inc >= 0.8) and (ua[0] != ub[0] or abs(ua[1] - ub[1]) > 5):
            pairs.append((a, b, ja, inc))
            parent[find(a)] = find(b)
    clusters = defaultdict(set)
    for a, b, _, _ in pairs:
        clusters[find(a)].update((a, b))
    out = []
    for members in clusters.values():
        locs = sorted({f"{us[m][0]}:{us[m][1]}" for m in members})
        files = sorted({us[m][0].split("/")[-1] for m in members})
        rep = max(members, key=lambda m: len(us[m][2]))
        out.append({"occurrences": len(locs), "fichiers": files, "lieux": locs,
                    "extrait": re.sub(r"\s+", " ", us[rep][2])[:120]})
    return sorted(out, key=lambda d: (-d["occurrences"], d["extrait"]))


ROUTE_TOK = re.compile(r"`((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/[A-Z0-9_\-]+(?:/[A-Z0-9_\-]+)?)`")


def load_lists(root: Path) -> dict:
    spec = json.loads((DATA / "V12R_listes_chargement.json").read_text(encoding="utf-8"))["listes"]
    out = {}
    for it in spec:
        lines = [l for l in (root / it["file"]).read_text(encoding="utf-8").splitlines() if l.startswith(it["row"])]
        if len(lines) != 1:
            out[it["lieu"]] = None
            continue
        cells = lines[0].split("|")
        out[it["lieu"]] = sorted(set(ROUTE_TOK.findall(cells[it["col"]])))
    return out


def distinct_lists(ll: dict) -> int:
    """Listes distinctes, un renvoi vers DIRECTION/CHARGE (éventuellement précédé de START) n'étant pas une liste."""
    return len({tuple(v) for v in ll.values() if v is not None and not set(v) <= {"DIRECTION/CHARGE", "DIRECTION/START"}})


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    jpath = Path(sys.argv[sys.argv.index("--json") + 1]) if "--json" in sys.argv else None
    b = budget(root)
    r = reach(b)
    ind = indicators(root)
    dup = duplicates(root)
    ll = load_lists(root)

    print("== 1. BUDGET (run DIRECTION)")
    for name, v in b.items():
        print(f"  {name:7s} {v['lignes']:6d} lignes {v['mots']:7d} mots"
              + (f"  ⚠ introuvables : {v['introuvables']}" if v["introuvables"] else "")
              + (f"  ⚠ PÉRIMÉS : {v['perimes']}" if v["perimes"] else ""))
    print("== 2. ATTEIGNABILITÉ des 25 outils de fabrication")
    for name, m in r["par_perimetre"].items():
        on = [k for k, ok in m.items() if ok]
        print(f"  {name:7s} {len(on):2d}/25 : {' '.join(on)}")
    print("== 3. INDICATEURS")
    print(f"  {'fichier':58s}{'mots':>7s}{'nég':>6s}{'auto':>6s}{'jet':>6s}{'champs':>7s}{'beau':>6s}")
    for f, v in ind.items():
        print(f"  {f:58s}{v['mots']:7d}{v['negations']:6d}{v['auto_limitation']:6d}{v['jetons']:6d}"
              f"{v['champs_trace']:7d}{v['beau']:6d}")
    print(f"== 4. DOUBLONS (phrases ou lignes de table ≥ 8 mots ; Jaccard ≥ 0,5 ou inclusion ≥ 0,8) : "
          f"{len(dup)} amas, {sum(d['occurrences'] for d in dup)} occurrences")
    for d in dup[:80]:
        print(f"  ×{d['occurrences']:<2d} {','.join(d['fichiers']):45s} « {d['extrait'][:95]} »")
    print("== 5. LISTES DE CHARGEMENT « première lecture » d'un run DIRECTION")
    sets = [tuple(v) for v in ll.values() if v is not None]
    union = sorted({route for v in sets for route in v})
    print(f"  listes : {len(ll)} ; distinctes (renvois exclus) : {distinct_lists(ll)} ; introuvables : {[k for k, v in ll.items() if v is None]}")
    print(f"  {'route':28s}" + "".join(f"{k[:12]:>13s}" for k in ll))
    for route in union:  # audit progressif, C22 : variable distincte de r (atteignabilité exportée en JSON)
        print(f"  {route:28s}" + "".join(f"{('x' if v and route in v else '·'):>13s}" for v in ll.values()))
    if jpath:
        for v in b.values():
            v.pop("texte")
        jpath.write_text(json.dumps({"budget": b, "atteignabilite": r, "indicateurs": ind, "doublons": dup,
                                     "listes_chargement": ll},
                                    ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
