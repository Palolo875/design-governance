#!/usr/bin/env python3
"""DG-AUDIT-001 — 12.01 — vérifications complémentaires A1 (mutations de code et de schéma, motif exigé).
Hors package ; copies temporaires. Usage : python3 A1_verifications_complementaires_12-01.py <racine>.
B03@12.01 : 7/7 rouges pour leur motif. B01 : 0/7 (5 faux PASS, 2 rejets pour un autre motif)."""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
src = Path(sys.argv[1])
def run(root, *a):
    r = subprocess.run([sys.executable, *a], cwd=root, capture_output=True, text=True); return r.returncode, r.stdout + r.stderr
def sub(root, rel, old, new):
    p = root / rel; t = p.read_text(encoding="utf-8"); assert t.count(old) == 1, (rel, old); p.write_text(t.replace(old, new), encoding="utf-8")
def js(root, rel, fn):
    p = root / rel; d = json.loads(p.read_text(encoding="utf-8")); p.write_text(json.dumps(fn(d), ensure_ascii=False), encoding="utf-8")
def enum_str(d): d["properties"]["run_card"]["properties"]["mode"]["enum"] = "LITE"; return d
cases = [
 ("X-1 code : contrôle d'enum retiré de validate_node → suite", lambda r: sub(r, "scripts/validate_run_card.py", 'if "enum" in schema and value not in schema["enum"]:', 'if False:'), ("scripts/validate_run_card.py",), "le schéma n’impose pas l’enum de mode"),
 ("X-2 code : idem, validation ciblée de l'exemple", lambda r: sub(r, "scripts/validate_run_card.py", 'if "enum" in schema and value not in schema["enum"]:', 'if False:'), ("scripts/validate_run_card.py", "schemas/run_card.example.json"), "le schéma n’impose pas l’enum de mode"),
 ("X-3 schéma : enum mode en chaîne", lambda r: js(r, "schemas/run_card.schema.json", enum_str), ("scripts/validate_run_card.py",), "schéma incomplet"),
 ("X-4 code contrats : contrôle d'enum retiré → suite", lambda r: sub(r, "scripts/validate_contracts.py", 'if "enum" in schema and value not in schema["enum"]:', 'if False:'), ("scripts/validate_contracts.py",), "le schéma n'impose pas l'enum de depth"),
 ("X-5 code contrats : contrôle required retiré → suite", lambda r: sub(r, "scripts/validate_contracts.py", "        for key in schema.get(\"required\", []):\n            if key not in value:", "        for key in []:\n            if key not in value:"), ("scripts/validate_contracts.py",), "le schéma n'impose pas la clé requise"),
 ("X-6 contrats : required racine vidé → ciblé", lambda r: js(r, "schemas/domain_frame.schema.json", lambda d: {**d, "required": []}), ("scripts/validate_contracts.py", "schemas/examples/domain_frame.example.json"), "schéma incomplet : required racine absent ou vide"),
 ("X-7 contrats : sous-schéma non objet", lambda r: js(r, "schemas/research_brief.schema.json", lambda d: {**d, "properties": {**d["properties"], "depth": []}}), ("scripts/validate_contracts.py",), "sous-schéma non objet"),
]
ok_all = True
for label, prep, cmd, motif in cases:
    with tempfile.TemporaryDirectory() as t:
        root = Path(t) / "pkg"; shutil.copytree(src, root); prep(root)
        c, o = run(root, *cmd)
        ok = c != 0 and "Traceback" not in o and "FAILED" in o and motif in o
        ok_all &= ok
        print("OK  " if ok else "ÉCHEC", label, "|", o.strip().splitlines()[-1][:110])
print("extra :", "tous rouges pour leur motif" if ok_all else "ÉCHEC")
