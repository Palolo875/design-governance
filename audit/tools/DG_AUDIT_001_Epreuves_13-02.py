#!/usr/bin/env python3
"""DG-AUDIT-001 — 13.02 — épreuves déterministes (rejeux machine et épreuves outillées).

Artefact d'audit HORS package. Lecture seule de la racine ; les cartes sont écrites dans un dossier temporaire.
Usage : python3 DG_AUDIT_001_Epreuves_13-02.py <racine B03 ou distribution GitHub>
Chaque ligne : OK / ÉCHEC, identifiant, fiche, attendu, obtenu.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else None


def load():
    spec = importlib.util.spec_from_file_location("vrc", ROOT / "scripts/validate_run_card.py")
    m = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(m)
    schema = json.loads((ROOT / "schemas/run_card.schema.json").read_text(encoding="utf-8"))
    ex = json.loads((ROOT / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    ret = json.loads((ROOT / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8"))
    return m, schema, ex, ret


def verdict(m, schema, d, strict=False, path=None):
    try:
        m.validate_card(d, schema, strict=strict, source_path=path)
        return True, "acceptée"
    except m.ValidationError as e:
        return False, str(e)
    except Exception as e:  # une exception brute n'est pas un rejet gouverné
        return False, f"EXCEPTION {type(e).__name__}: {e}"


ROWS: list[tuple[str, str, str, bool, str]] = []


def expect(cid, fiche, label, result, accepted: bool, motif: str | None = None):
    ok, msg = result
    good = (ok == accepted) and (motif is None or motif in msg) and not msg.startswith("EXCEPTION")
    ROWS.append((cid, fiche, f"{label} → {'acceptée' if accepted else 'refusée'}{f' ({motif})' if motif else ''}", good, msg[:150]))


def rejeux(m, schema, ex, ret):
    def mut(base, *edits):
        d = copy.deepcopy(base)
        c = d["run_card"]
        for fn in edits:
            fn(c)
        return d
    crit = {"level": "critical", "statement": "Le consentement au partage des données peut être enregistré sans action explicite.",
            "critical_protection": {"control": "Parcours de consentement testé au clavier et au lecteur d’écran", "owner": "product-owner",
                                    "scope": "Écran de consentement", "failure_action": "BLOCKED", "evidence_locator": "tests/consent.md", "result": "PASS"}}
    # B1 — rejeu 9.08 : changement de consentement classé LITE avec risque critique
    expect("R-B1", "F-DIR-007", "rejeu 9.08 : consentement, LITE, risque critique", verdict(m, schema, mut(ex, lambda c: c.update(mode="LITE", risk=crit))), False, "LITE ou ITER")
    # B2 — rejeux
    expect("R-B2a", "F-ACT-010", "rejeu 4.04 : RETURNED + ACCEPTED", verdict(m, schema, mut(ex, lambda c: c["closure"].update(issue="RETURNED", verdict="ACCEPTED"))), False, "issue non nulle")
    expect("R-B2b", "F-ACT-010", "rejeu 7.02 B4 : RECLASSIFIED + ACCEPTED", verdict(m, schema, mut(ex, lambda c: c["closure"].update(issue="RECLASSIFIED", verdict="ACCEPTED"))), False, None)
    expect("R-B2c", "F-ACT-010", "rejeu 9.02 20-N : ESCALATED + ACCEPTED", verdict(m, schema, mut(ex, lambda c: c["closure"].update(issue="ESCALATED", verdict="ACCEPTED"))), False, "issue non nulle")
    expect("R-B2d", "F-ACT-022", "rejeu 4.08 / 9.02 17-N1 : preuve sur une version périmée", verdict(m, schema, mut(ex, lambda c: c["artifact"].update(version="2026-09-20 / V2"))), False, "version")
    expect("R-B2e", "F-ACT-018 (limite)", "rejeu 4.07 : capture statique présentée comme test de tâche, capacité attestée — forme seule, limite déclarée",
           verdict(m, schema, mut(ex, lambda c: c["closure"]["axes"].update(U="PASS"))), True, None)
    # B3 — rejeux
    def system_accepted(c):
        c.update(mode="SYSTÈME")
        c["closure"].pop("b1b", None)
    expect("R-B3a", "F-ACT-015", "rejeu 4.04 / 4.02 N1 : SYSTÈME accepté sans paquet (consumers, migration, rollback)", verdict(m, schema, mut(ex, system_accepted)), False, "system_package")
    pkg = {"impact": "Tous les formulaires", "consumers": [], "owner": "ds-owner", "migration": "Remplacement du Dialog v1",
           "rollback": "Retour au Dialog v1", "non_regression": {"claim": "Focus et clavier inchangés", "baseline": {"locator": "baselines/dialog.png", "version": "v1", "state": "focus"}},
           "changelog_ref": "CHANGELOG#dialog"}
    expect("R-B3b", "F-ACT-015", "rejeu 9.03 : composant partagé, paquet sans consumer", verdict(m, schema, mut(ex, system_accepted, lambda c: c["closure"].update(system_package=pkg))), False, "consumer")
    expect("R-B3c", "F-BIB-001 (limite)", "rejeu 9.06 T1 : B1b N/A par « paire équivalente » avec référence — la machine ne vérifie pas l’équivalence (limite déclarée)",
           verdict(m, schema, mut(ex, lambda c: c["closure"].update(b1b={"status": "N/A-JUSTIFIED", "reason": "equivalent_pair_valid", "pair_ref": "captures/paire-v0",
                                                                          "covered_decision": "Même décision", "owner": "design-owner", "next_proof": "Capture V2"}))), True, None)
    # B4 — rejeux 9.06
    expect("R-B4a", "F-DIR-027", "rejeu 9.06 T2 : DIRECTION acceptée sans ancre", verdict(m, schema, mut(ex, lambda c: c.update(anchors=[]))), False, "ancr")

    def exploratory_no_anchor(c):
        c.update(anchors=[])
        c["closure"].update(state="CLOSED", issue="EXPLORATORY", verdict="EXPLORATORY", direction_status="PARTIALLY-HELD")
        c["closure"].pop("reservations", None)
    expect("R-B4b", "F-DIR-027", "rejeu pilote A : DIRECTION sans ancre sérialisée en EXPLORATORY, sans ancre inventée", verdict(m, schema, mut(ex, exploratory_no_anchor)), True, None)
    expect("R-B4c", "F-DIR-027 (limite)", "rejeu 9.06 T3 : `transformed` déclaratif — la machine ne vérifie pas la transformation (limite déclarée)",
           verdict(m, schema, mut(ex)), True, None)
    # D2 — épreuve de phase et épreuve ITER
    for state in ("INTAKE", "CLASSIFIED", "SPECCED", "BUILDING"):
        def pre(c, s=state):
            c["risk"] = {"level": "normal", "critical_protection": None, "statement": "Libellé tronqué sur mobile"}
            c["closure"].update(state=s, verdict=None, issue=None)
            c.pop("decision_change", None)
        expect(f"R-D2-{state}", "F-DIR-003", f"photo à l’état {state}, aucun champ « après observation »", verdict(m, schema, mut(ret, pre)), True, None)
        expect(f"R-D2-{state}+", "F-DIR-003", f"photo à l’état {state} avec decision_change déjà rempli", verdict(m, schema, mut(ret, pre, lambda c: c.update(decision_change=copy.deepcopy(ret["run_card"]["decision_change"])))), False, None)
    iter_base = mut(ret, lambda c: c.update(mode="ITER", trace_locator="tickets/run-044.md"), lambda c: c["risk"].update(level="normal", critical_protection=None))
    expect("R-D2-ITER1", "F-DIR-036", "ITER sans rappel de direction", verdict(m, schema, iter_base), False, "direction")
    expect("R-D2-ITER2", "F-DIR-036", "ITER avec rappel (direction.thesis) et trace", verdict(m, schema, mut(iter_base, lambda c: c.update(direction={"thesis": "La hiérarchie existante est conservée."}))), True, None)
    return mut


def profils(m, schema, ret, mut):
    """C4 point 4 : 5 modes × normal / strict × trace présente / absente × artefact local présent / absent."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "cartes"
        (base / "captures").mkdir(parents=True)
        (base / "captures" / "v1.png").write_bytes(b"png")
        (base / "tickets").mkdir()
        (base / "tickets" / "run-044.md").write_text("trace", encoding="utf-8")
        path = base / "carte.json"
        bad = []
        n = 0
        for mode in ("LITE", "ITER", "STANDARD", "DIRECTION", "SYSTÈME"):
            for trace in (True, False):
                for artifact in ("captures/v1.png", "captures/absent.png"):
                    def build(c, mode=mode, trace=trace, artifact=artifact):
                        c["mode"] = mode
                        c["risk"] = {"level": "normal", "critical_protection": None, "statement": "Libellé tronqué sur mobile"}
                        c["artifact"]["locator"] = artifact
                        if mode == "ITER":
                            c["direction"] = {"thesis": "La hiérarchie existante est conservée."}
                        if trace:
                            c["trace_locator"] = "tickets/run-044.md"
                        else:
                            c.pop("trace_locator", None)
                    d = mut(ret, build)
                    normal = verdict(m, schema, d, False, path)
                    strict = verdict(m, schema, d, True, path)
                    n += 1
                    strict_only = (not strict[0]) and strict[1].startswith("strict :")
                    same = normal[0] == strict[0] and (normal[0] or normal[1] == strict[1])
                    if not (same or (normal[0] and strict_only)):
                        bad.append(f"{mode}/trace={trace}/{artifact}: normal={normal[1][:50]} ; strict={strict[1][:50]}")
        ROWS.append(("O-C4-profils", "F-ACT-020", f"{n} combinaisons : même résultat dans les deux profils, hors contrôles propres au strict", not bad, "; ".join(bad)[:150] or "aucun écart"))


def serve(loc):
    r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/read_route.py"), loc], capture_output=True, text=True)
    return r.returncode == 0, r.stdout if r.returncode == 0 else (r.stderr or r.stdout)


def outillees():
    action = (ROOT / "V1/official/ACTION.md").read_text(encoding="utf-8")
    carte = action[action.find("### Carte de lecture par mode"):action.find("### ACTION/HANDOFF")]
    socle = re.findall(r"`(ACTION/[A-Z-]+)`", carte.split("| Mode |")[0])
    rows = [l for l in carte.splitlines() if re.match(r"\| `(LITE|ITER|STANDARD|DIRECTION|SYSTÈME)`", l)]
    for line in rows:
        mode = re.match(r"\| `([^`]+)`", line).group(1)
        locs = socle + re.findall(r"`((?:ACTION|BIBLIOTHEQUE|DIRECTION|SAVOIR)/[A-Za-z_\-]+)`", line)
        served, total, refused = [], 0, []
        for loc in locs:
            ok, out = serve(loc)
            if ok:
                served.append(loc)
                total += len(out.splitlines())
            else:
                refused.append(loc)
        ROWS.append((f"O-C4-{mode}", "F-ACT-001", f"scénario {mode} avec READING_MAP et read_route seuls : socle + route du mode servis", not refused,
                     f"{len(served)} locators, {total} lignes" + (f" ; refusés : {refused}" if refused else "")))
    total, refused = 0, []
    for loc in ("DIRECTION/START/TREE", "ACTION/RUN-LITE", "ACTION/FAST-PATH"):
        ok, out = serve(loc)
        total += len(out.splitlines()) if ok else 0
        refused += [] if ok else [loc]
    ROWS.append(("O-C4-mesure", "F-RM-003", "route LITE de 9.08 rejouée : ≤ 60 lignes servies (158 sur B01)", not refused and total <= 60, f"{total} lignes"))
    # D1 — épreuve de routage : chaque déclencheur corrigé mène au propriétaire exact
    direction = (ROOT / "V1/official/DIRECTION.md").read_text(encoding="utf-8")
    trig = direction[direction.find("### Déclencheurs critiques"):direction.find("### Index à la demande")]
    expected = {"Motif possiblement générique": ["SAVOIR/CRAFT/CFT-01", "ACTION/ANTI-SLOP"],
                "Asset, motion, scène": ["BIBLIOTHEQUE/SELECT", "BIBLIOTHEQUE/SCENE"],
                "Détail final": ["SAVOIR/CRAFT/CFT-03", "SAVOIR/STATE", "SAVOIR/INTEGRITY"]}
    for key, locs in expected.items():
        line = next((l for l in trig.splitlines() if l.startswith(f"| {key}")), "")
        found = all(loc in line for loc in locs)
        owners = {loc: serve(loc) for loc in locs}
        good = found and all(ok and f"OWNER: V1/official/{loc.split('/')[0]}.md" in out for loc, (ok, out) in owners.items())
        ROWS.append((f"O-D1-{key.split()[0]}", "F-DIR-042", f"déclencheur « {key} » → {', '.join(locs)} servis par leur propriétaire", good,
                     "résolus" if good else f"ligne={bool(line)} ; " + ", ".join(f"{k}:{v[0]}" for k, v in owners.items())))
    # D4 — épreuve de propriétaire : composant, heuristique CRAFT, gate ACTION, champ RUN_CARD
    for label, loc, owner in (("composant", "BIBLIOTHEQUE/COMPONENTS", "BIBLIOTHEQUE"), ("heuristique CRAFT", "SAVOIR/CRAFT", "SAVOIR"),
                              ("gate ACTION", "ACTION/GATE-A", "ACTION"), ("champ RUN_CARD", "ACTION/RUN_CARD", "ACTION")):
        ok, out = serve(loc)
        ROWS.append((f"O-D4-{label.split()[0]}", "F-DIR-046", f"{label} → {loc} ({owner})", ok and f"OWNER: V1/official/{owner}.md" in out, "servi" if ok else out[:80]))
    # F-DIR-044 (préalable des pilotes) : taille des blocs servis pour chaque locator de la carte
    rm = (ROOT / "V1/official/READING_MAP.md").read_text(encoding="utf-8")
    locs = sorted(set(re.findall(r"`((?:ACTION|DIRECTION|SAVOIR|BIBLIOTHEQUE)/[A-Za-z_\-/]+)`", rm)))
    sizes = []
    for loc in locs:
        ok, out = serve(loc)
        if ok:
            sizes.append((len(out.splitlines()), loc))
    sizes.sort(reverse=True)
    ROWS.append(("O-DIR-044", "F-DIR-044 (mesure)", f"taille des blocs servis pour les {len(sizes)} locators de READING_MAP (plus grands)", True,
                 ", ".join(f"{loc} {n}" for n, loc in sizes[:6])))
    return sizes


def integrateur():
    """C9 : un intégrateur valide ses propres contrats HORS du package, avec la seule commande du README."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    cmd = re.search(r"`python3 (scripts/validate_contracts\.py --type \S+ \S+)`", readme)
    with tempfile.TemporaryDirectory() as tmp:
        ext = Path(tmp) / "equipe"
        ext.mkdir()
        results = []
        for kind in ("domain_frame", "research_brief", "production_contracts"):
            src = json.loads((ROOT / f"schemas/examples/{kind}.example.json").read_text(encoding="utf-8"))
            f = ext / f"mon_{kind}.json"
            f.write_text(json.dumps(src, ensure_ascii=False), encoding="utf-8")
            r = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate_contracts.py"), "--type", kind, str(f)], capture_output=True, text=True, cwd=ext)
            results.append(r.returncode == 0)
            bad = dict(src)
            bad[next(iter(bad))] = 42  # défaut de forme : valeur d’un type illégal (un placeholder de texte libre n’est refusé que dans les champs visés par E2)
            fb = ext / f"mon_{kind}_incomplet.json"
            fb.write_text(json.dumps(bad, ensure_ascii=False), encoding="utf-8")
            r2 = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate_contracts.py"), "--type", kind, str(fb)], capture_output=True, text=True, cwd=ext)
            results.append(r2.returncode != 0 and "Traceback" not in r2.stdout + r2.stderr)
        ROWS.append(("O-C9", "F-VCT-004 / C9 O-1", "intégrateur hors package, commande du README seule : 3 contrats valides acceptés, 3 incomplets refusés proprement",
                     bool(cmd) and all(results), f"commande documentée : {bool(cmd)} ; {sum(results)}/6"))


def main() -> int:
    if ROOT is None:
        print(__doc__)
        return 2
    m, schema, ex, ret = load()
    mut = rejeux(m, schema, ex, ret)
    profils(m, schema, ret, mut)
    outillees()
    integrateur()
    for cid, fiche, label, ok, got in ROWS:
        print(f"{'OK  ' if ok else 'ÉCHEC'} {cid:16} {fiche:20} {label}  [{got}]")
    print(f"\nÉpreuves déterministes : {sum(r[3] for r in ROWS)}/{len(ROWS)}")
    return 0 if all(r[3] for r in ROWS) else 1


if __name__ == "__main__":
    sys.exit(main())
