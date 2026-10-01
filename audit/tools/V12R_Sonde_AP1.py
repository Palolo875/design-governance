#!/usr/bin/env python3
"""Audit progressif, unité 1 — sondes directes de C01, C02 et C03 (preuves propres, indépendantes du suivi).

Toutes les sondes travaillent sur une copie du package (rien n'est écrit dans <racine>).
  C01 : l'en-tête de SKILL.md se lit en YAML (PyYAML si disponible, garde SKL-01 sinon) ; description décodée = référence.
  C02 : profil strict lancé depuis trois dossiers différents ; fichier nu présent admis, absent refusé ; URL, ticket,
        commit et identifiants opaques admis.
  C03 : panne provoquée au déplacement d'une archive (faux `mv` en tête du PATH) ; dist et les deux ZIP doivent
        retrouver leur état antérieur, sans sauvegarde résiduelle, puis une relance normale doit réussir.
Usage : python3 V12R_Sonde_AP1.py <racine> [c01] [c02] [c03]   (toutes par défaut)
Sortie : une ligne OK/KO par contrôle, puis « SONDE AP1 : VERTE » ou « SONDE AP1 : ROUGE (n) ».
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Valeur de référence : description de la skill à 1a4bf2f (texte non cité, invalide en YAML) ; la correction ne change
# que la forme (citation), jamais le texte décodé.
DESCRIPTION = (
    "Produire avec Design Governance V1 un travail de design de niveau designer senior (projet, interface, application, "
    "identité ou scène), beau, vrai et situé, même à partir d’un brief flou : gestes de fabrication, prise de brief "
    "minimale, plafond déclaré et trace proportionnée au risque. Utiliser pour toute demande de design à construire, "
    "corriger ou juger ; charger les sources progressivement, sans créer de règles concurrentes."
)
ZIPS = ("Design_Governance_V1_GITHUB.zip", "Design_Governance_V1_LOCAL.zip")
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))
    print(f"  {'OK' if ok else 'KO'}  {name}{' — ' + detail if detail else ''}")


def copy_package(root: Path, tmp: Path) -> Path:
    dest = tmp / "pkg"
    tmp.mkdir(parents=True, exist_ok=True)
    shutil.copytree(root, dest, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__",
                                                              ".dist.previous", ".archives.previous"))
    return dest


def sonde_c01(pkg: Path) -> None:
    print("C01 — en-tête YAML de la skill")
    text = (pkg / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8")
    header = text.split("\n---", 1)[0].removeprefix("---\n")
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None
    if yaml is not None:
        try:
            data = yaml.safe_load(header)
            check("PyYAML lit l'en-tête", isinstance(data, dict))
            check("description décodée identique à la référence", isinstance(data, dict) and data.get("description") == DESCRIPTION)
            check("name inchangé", isinstance(data, dict) and data.get("name") == "design-governance-practice")
        except yaml.YAMLError as exc:
            check("PyYAML lit l'en-tête", False, str(exc).splitlines()[0])
    else:
        print("  (PyYAML indisponible : seule la garde SKL-01 est jouée)")
    out = subprocess.run([sys.executable, "-B", "scripts/validate_structure.py"], cwd=pkg, capture_output=True, text=True)
    check("garde SKL-01 sans erreur", "[SKL-01]" not in out.stdout and "SKILL_DIR" not in out.stderr,
          next((l for l in out.stdout.splitlines() if "[SKL-01]" in l), ""))


def strict(pkg: Path, card: Path, cwd: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(pkg / "scripts/validate_run_card.py"), "--strict",
                          os.path.relpath(card, cwd)], cwd=cwd, capture_output=True, text=True)
    return out.returncode, (out.stdout + out.stderr).strip().splitlines()[-1]


def sonde_c02(pkg: Path, tmp: Path) -> None:
    print("C02 — profil strict : fichiers locaux nus")
    base = json.loads((pkg / "schemas/fixtures/valid_closed_return.json").read_text(encoding="utf-8"))
    card = base["run_card"]
    card.update({"mode": "LITE", "risk": {"level": "normal", "statement": "Troncature du libellé sur mobile",
                                          "critical_protection": None}})
    work = tmp / "c02" / "cartes"
    work.mkdir(parents=True)
    (work / "rendu.html").write_text("<p>rendu</p>", encoding="utf-8")
    (work / "trace.md").write_text("trace", encoding="utf-8")
    elsewhere = tmp / "c02" / "ailleurs"
    elsewhere.mkdir()

    def case(label: str, artifact: str, trace: str | None, expect_ok: bool, motif: str = "") -> None:
        doc = json.loads(json.dumps(base))
        c = doc["run_card"]
        c["artifact"]["locator"] = artifact
        if "proof" in c and isinstance(c["proof"].get("provenance"), dict):
            c["proof"]["provenance"]["artifact_locator"] = artifact
        if trace is None:
            c.pop("trace_locator", None)
        else:
            c["trace_locator"] = trace
        path = work / "carte.json"
        path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        for where in (work, work.parent, elsewhere):
            code, last = strict(pkg, path, where)
            ok = (code == 0) if expect_ok else (code != 0 and motif in last)
            check(f"{label} [lancé depuis {where.name}]", ok, "" if ok else last[:140])

    case("artefact nu présent admis", "rendu.html", None, True)
    case("artefact nu absent refusé", "absent.html", None, False, "artefact local absent")
    case("artefact ./ absent refusé", "./absent.html", None, False, "artefact local absent")
    case("trace nue présente admise", "rendu.html", "trace.md", True)
    case("trace nue absente refusée", "rendu.html", "trace-absente.md", False, "trace local absent")
    for label, value in (("URL", "https://atelier.exemple.cm/runs/42"), ("ticket", "JIRA-142"), ("commit", "1a4bf2f"),
                         ("version", "v1.2.0"), ("identifiant opaque", "run-2026-10-01.a"),
                         ("domaine sans schéma", "atelier.exemple.cm")):
        case(f"trace {label} admise", "rendu.html", value, True)
    out = subprocess.run([sys.executable, "-B", "scripts/validate_run_card.py"], cwd=pkg, capture_output=True, text=True)
    lines = [l for l in out.stdout.splitlines() if l.startswith("+ cas unitaires") or l.startswith("+ locators admis")]
    check("suite RUN_CARD verte (cas unitaires et locators admis)", out.returncode == 0, " ; ".join(lines))


def digest(path: Path) -> str:
    if path.is_file():
        return hashlib.sha256(path.read_bytes()).hexdigest()
    if not path.exists():
        return "absent"
    h = hashlib.sha256()
    for f in sorted(p for p in path.rglob("*") if p.is_file()):
        h.update(str(f.relative_to(path)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def build(pkg: Path, epoch: str, fail_zip: str | None = None) -> tuple[int, str]:
    env = dict(os.environ, SOURCE_DATE_EPOCH=epoch)
    if fail_zip:
        fake = pkg.parent / "faux_bin"
        fake.mkdir(exist_ok=True)
        (fake / "mv").write_text(
            "#!/usr/bin/env bash\n"
            f'for a in "$@"; do case "$a" in */.build/archives/{fail_zip}) echo "panne provoquée : mv $a" >&2; exit 73;; esac; done\n'
            'exec /bin/mv "$@"\n', encoding="utf-8")
        (fake / "mv").chmod(0o755)
        env["PATH"] = f"{fake}:{env['PATH']}"
    out = subprocess.run(["bash", "scripts/build_distributions.sh"], cwd=pkg, env=env, capture_output=True, text=True)
    return out.returncode, (out.stdout + out.stderr).strip().splitlines()[-1] if (out.stdout + out.stderr).strip() else ""


def sonde_c03(root: Path, tmp: Path) -> None:
    print("C03 — promotion transactionnelle de dist et des deux archives")
    for index, fail_zip in enumerate(ZIPS):
        pkg = copy_package(root, tmp / f"c03_{index}")
        tag = f"panne sur {fail_zip}"
        code, last = build(pkg, "400000000")
        check(f"{tag} : build initial (état antérieur)", code == 0, "" if code == 0 else last)
        if code:
            continue
        (pkg / "dist" / "MARQUEUR_ANTERIEUR").write_text("état antérieur", encoding="utf-8")
        before = {name: digest(pkg / name) for name in ("dist", *ZIPS)}
        code, last = build(pkg, "500000000", fail_zip)
        check(f"{tag} : build en échec signalé", code != 0, last[:150])
        after = {name: digest(pkg / name) for name in ("dist", *ZIPS)}
        for name in ("dist", *ZIPS):
            check(f"{tag} : {name} restauré à l'identique", after[name] == before[name])
        for residue in (".dist.previous", ".archives.previous"):
            check(f"{tag} : aucune sauvegarde résiduelle {residue}", not (pkg / residue).exists())
        code, last = build(pkg, "500000000")
        check(f"{tag} : relance normale réussie", code == 0, "" if code == 0 else last[:150])
        fresh = {name: digest(pkg / name) for name in ZIPS}
        check(f"{tag} : relance, archives neuves publiées", all(fresh[n] != before[n] for n in ZIPS))
        check(f"{tag} : relance, dist neuf (marqueur antérieur disparu)", not (pkg / "dist" / "MARQUEUR_ANTERIEUR").exists())
        check(f"{tag} : relance, aucune sauvegarde résiduelle",
              not (pkg / ".dist.previous").exists() and not (pkg / ".archives.previous").exists())


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    wanted = set(a for a in sys.argv[2:] if a in ("c01", "c02", "c03")) or {"c01", "c02", "c03"}
    with tempfile.TemporaryDirectory(prefix="sonde-ap1-") as tmp_dir:
        tmp = Path(tmp_dir)
        pkg = copy_package(root, tmp / "base")
        if "c01" in wanted:
            sonde_c01(pkg)
        if "c02" in wanted:
            sonde_c02(pkg, tmp)
        if "c03" in wanted:
            sonde_c03(root, tmp)
    bad = sum(1 for _, ok, _ in results if not ok)
    print(f"SONDE AP1 : {'VERTE' if not bad else f'ROUGE ({bad})'} — {len(results) - bad}/{len(results)} contrôles")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
