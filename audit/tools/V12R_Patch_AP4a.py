#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION AP4a (audit progressif externe, unité 4a) : validateurs.

C11 lecteur de routes autonome aligné sur le validateur de carte ; C12 clés JSON répétées refusées (contrats, manifeste) ;
C13 mot-clé de schéma RUN_CARD non pris en charge refusé ; C19 dates et heures réelles ; C20 diagnostics gouvernés
(type d'enum, schéma non objet, Markdown non UTF-8). C21 (outil 13.01) est une rectification déclarée hors package.
Audit : `DG_Audit_progressif_10`. Décision de l'owner (01-10-2026) : « Allons-y pour AP4a » (outillage, aucune prose
normative). Rapport : `V12R_43_AP4a_VALIDATEURS.md`. Preuves directes : `V12R_Sonde_AP4a.py`.
Usage : python3 V12R_Patch_AP4a.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

C = "V1/official/CHANGELOG.md"
F = HERE / "V12R_Patch_AP4a_fichiers" / "scripts"
SHA = {
    "read_route.py": "087f740ed0446bba583c525f68aed9364ca754aba48dbade38478fc0dfa0ce89",
    "validate_reading_map.py": "82e5b41e80ca93627b20d098d223c0dd65c302667c6471e7cd3da972734072ea",
    "validate_structure.py": "6be1f72311f438d608ca97702aad43e3e970fc66679ae00e97f5aa193e0f613f",
    "build_core.py": "f8e1ca7118f9d369baab2e9e6831704656cbed8997d0d139f75ba5b6e35050f1",
    "validate_design_governance.py": "be3fe0777b1ca0acbde95713e693a952a28915bc7e377cf031d38a052b6fde7f",
    "validate_run_card.py": "20b606f72c94f66a20994f5d9829f2d80524304ebe5e09380d52d4e116b0967f",
    "validate_contracts.py": "f72f0d96882bef374e27c89e7f331eb4310e3f1d9f03f290108425cbb4a36405",
}
FILE_REPLACE = {f"scripts/{name}": (sha, F / name) for name, sha in SHA.items()}
PATCH = [
    ("AP4a-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Validateurs (audit progressif, unité 4a).** Le lecteur de routes refuse un locator répété, un propriétaire "
     "incohérent et un titre porteur dupliqué ; les contrats et le manifeste refusent une clé JSON répétée ; le schéma "
     "`RUN_CARD` n’admet que les mots-clés réellement interprétés ; dates et heures doivent être réelles ; une valeur d’un "
     "autre type que son enum, un schéma non objet ou un Markdown non UTF-8 reçoivent un diagnostic nommé au lieu d’une "
     "erreur brute.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
# Mutations de code : (nom, script, ancien, nouveau, commande depuis la racine, motif attendu dans la sortie rouge).
CODE_MUTATIONS = [
    ("C11 : locator répété accepté", "scripts/read_route.py",
     'raise RouteError(f"locator en double dans READING_MAP : {locator}")', "pass",
     ["scripts/validate_reading_map.py"], "locator répété dans la table est accepté"),
    ("C11 : propriétaire non contrôlé", "scripts/read_route.py",
     "if owner_name != f\"{locator.split('/', 1)[0]}.md\":", "if False:",
     ["scripts/validate_reading_map.py"], "témoin du lecteur : propriétaire incohérent"),
    ("C12 : clés répétées écrasées (contrats)", "scripts/validate_contracts.py",
     "return json.loads(text, object_pairs_hook=reject_duplicate_keys)", "return json.loads(text)",
     ["scripts/validate_contracts.py"], "témoin C12"),
    ("C13 : pattern admis sans interprétation", "scripts/validate_run_card.py",
     '"minItems", "allOf", "anyOf", "if", "then"}', '"minItems", "allOf", "anyOf", "if", "then", "pattern"}',
     ["scripts/validate_run_card.py"], "témoin C13"),
    ("C19 : heure non contrôlée (RUN_CARD)", "scripts/validate_run_card.py",
     "return hour <= 23 and minute <= 59 and second <= 59 and tz_hour <= 23 and tz_minute <= 59", "return True",
     ["scripts/validate_run_card.py"], "cas unitaire C19-1"),
    ("C19 : date non contrôlée (contrats)", "scripts/validate_contracts.py",
     "    if not SOURCE_DATE.fullmatch(value):\n        return False\n", "    return bool(SOURCE_DATE.fullmatch(value))\n",
     ["scripts/validate_contracts.py"], "cas unitaire C19-1"),
    ("C20 : type d'enum non contrôlé", "scripts/validate_run_card.py",
     'elif isinstance(schema.get("enum"), list):', "elif False:",
     ["scripts/validate_run_card.py"], "unhashable"),
]


def code_mutations(root: Path) -> int:
    bad = 0
    for name, rel, old, new, command, motif in CODE_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            path = copy / rel
            text = path.read_text(encoding="utf-8")
            ok = text.count(old) == 1
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", *command], capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and motif in out.stdout + out.stderr
            print(f"mutation de code {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, {}, []
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        return 1 if code_mutations(Path(sys.argv[1]).resolve()) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
