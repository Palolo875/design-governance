#!/usr/bin/env python3
"""DG-AUDIT-001 — 12.02 — vérifications complémentaires A2 (mutations de code, de table, de fichier, d orchestrateur ; motif exigé).
Hors package ; copies temporaires. Usage : python3 A2_verifications_complementaires_12-02.py <racine>. B03@12.02 : 7/7. Y-7 lance validate_all : non significatif pendant la fenêtre de garde (12.03 → 12.05), qui arrête validate_all plus tôt ; adapté en 12.04 au résolveur (deux occurrences du message)."""
import shutil, subprocess, sys, tempfile
from pathlib import Path
src = Path(sys.argv[1])
def sub(root, rel, old, new):
    p = root / rel; t = p.read_text(encoding="utf-8"); assert t.count(old) == 1, (rel, old); p.write_text(t.replace(old, new), encoding="utf-8")
VR = "scripts/validate_run_card.py"
cases = [
 ("Y-1 code : invariant LOST-IN-BUILD retiré", lambda r: sub(r, VR, 'if closure.get("direction_status") == "LOST-IN-BUILD" and verdict', 'if False and verdict'), (VR,), "cas unitaire U-21 : faute unique acceptée"),
 ("Y-2 code : invariant « limitation non vide » retiré", lambda r: sub(r, VR, 'if not isinstance(limitations, list) or not limitations:', 'if False:'), (VR,), "cas unitaire U-14 : faute unique acceptée"),
 ("Y-3 code : diagnostic HELD retiré (le schéma rejette encore, autre motif)", lambda r: sub(r, VR, '    if isinstance(closure, dict) and closure.get("state") == "HELD":\n        raise', '    if False:\n        raise'), (VR,), "cas unitaire U-01 : attendu"),
 ("Y-4 table : négatif sans motif", lambda r: sub(r, VR, '"invalid_empty_proof.json": "un verdict accepté exige au moins une preuve observed",', '"invalid_empty_proof.json": "",'), (VR,), "oracle sans motif"),
 ("Y-5 fichier : fixture déclarée supprimée", lambda r: (r / "schemas/fixtures/invalid_state_held.json").unlink(), (VR,), "fixture déclarée absente"),
 ("Y-6 base de cas unitaire invalide", lambda r: sub(r, "schemas/fixtures/valid_closed_return.json", '"SYSTÈME"', '"BOGUS"'), (VR,), "cas unitaire U-03 : base invalide"),
 ("Y-7 orchestrateur : message de read_route changé", lambda r: (lambda f: f.write_text(f.read_text(encoding="utf-8").replace("locator inconnu", "locator introuvable"), encoding="utf-8"))(r / "scripts/read_route.py"), ("scripts/validate_all.py",), "a échoué pour un autre motif"),
]
ok_all = True
for label, prep, cmd, motif in cases:
    with tempfile.TemporaryDirectory() as t:
        root = Path(t) / "pkg"; shutil.copytree(src, root); prep(root)
        r = subprocess.run([sys.executable, *cmd], cwd=root, capture_output=True, text=True); o = r.stdout + r.stderr
        ok = r.returncode != 0 and "Traceback" not in o and motif in o
        ok_all &= ok
        line = next((l for l in o.splitlines() if motif in l), o.strip().splitlines()[-1] if o.strip() else "")
        print("OK  " if ok else "ÉCHEC", label, "|", line[:120])
print("extra :", "tous rouges pour leur motif" if ok_all else "ÉCHEC")
