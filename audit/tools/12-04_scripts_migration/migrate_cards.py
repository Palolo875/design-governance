"""12.04 — migration des données RUN_CARD (exemple canonique et 25 fixtures) vers le schéma migré."""
import glob, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import jsonio

ROOT = Path(sys.argv[1])
ACCEPTED = {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"}


def insert_after(d, after, key, value):
    items = list(d.items())
    out = {}
    placed = False
    for k, v in items:
        out[k] = v
        if k == after:
            out[key] = value
            placed = True
    if not placed:
        out[key] = value
    d.clear(); d.update(out)


def insert_first(d, key, value):
    items = list(d.items()); d.clear(); d[key] = value; d.update(items)


def migrate(name, doc):
    c = doc["run_card"]
    mode = c.get("mode")
    closure = c.get("closure", {})
    verdict = closure.get("verdict")
    # C2 : risk.statement
    if isinstance(c.get("risk"), dict) and "statement" not in c["risk"]:
        statement = STATEMENTS.get(name) or f"Risque principal : la décision « {c.get('decision', '').rstrip('.')} » échoue dans le scope déclaré."
        insert_after(c["risk"], "level", "statement", statement)
    # B1 : critical_protection.result
    prot = c.get("risk", {}).get("critical_protection") if isinstance(c.get("risk"), dict) else None
    if isinstance(prot, dict) and "result" not in prot:
        prot["result"] = RESULTS.get(name, "PASS")
    # C1 : decision_change.outcome
    dc = c.get("decision_change")
    if isinstance(dc, dict) and "outcome" not in dc:
        insert_first(dc, "outcome", OUTCOMES.get(name, "CHANGED"))
    # B4 : anchors[].type ; DIRECTION : identity_stake ; B2 : rights_status
    for anchor in c.get("anchors") or []:
        if isinstance(anchor, dict) and "type" not in anchor:
            insert_after(anchor, "role", "type", "observed")
    if mode == "DIRECTION":
        if isinstance(c.get("direction"), dict) and "identity_stake" not in c["direction"]:
            c["direction"]["identity_stake"] = "normal"
        if isinstance(c.get("artifact"), dict) and "rights_status" not in c["artifact"]:
            c["artifact"]["rights_status"] = "not_applicable"
    # B2 : basis typée
    cp = c.get("capability_profile")
    if isinstance(cp, dict) and isinstance(cp.get("basis"), list) and cp["basis"] and isinstance(cp["basis"][0], str):
        cp["basis"] = BASIS.get(name) or [{"capability": cap, "kind": "attested_environment", "detail": cp["basis"][0]} for cap in cp.get("available", [])]
    # C1 : profile_decision.phase
    pd = c.get("profile_decision")
    if isinstance(pd, dict) and "phase" not in pd:
        insert_first(pd, "phase", "observed")
    # B2 : carte acceptante valide → version, capacité, axes, réserves ; B3 : B1b
    if name in ACCEPTING_VALID:
        c["artifact"]["version"] = c["proof"]["provenance"]["artifact_version"]
        c["proof"]["provenance"]["capability"] = "navigateur/capture disponible"
        closure["axes"] = {"V": "PASS", "U": "NOT-VERIFIED", "A": "NOT-VERIFIED", "T": "PASS"}
        closure["reservations"] = [dict(RESERVATION)]
        if mode == "DIRECTION":
            closure["b1b"] = dict(B1B)
    # B1 : exception de la fixture FAIL-ASSUMED (isole sa faute : le verdict accepté)
    if name == "invalid_fail_assumed_accepted.json" and "exception" not in closure:
        closure["exception"] = {
            "owner": c.get("owner", "design-owner"), "scope": "Surface concernée, diffusion interne",
            "impact": "Défaut connu livré sous exception", "next_proof": "Correction et nouvelle observation",
            "review_date": "2026-09-12", "exit_condition": "Défaut corrigé et observé",
            "gate_axis": "Gate A / défaut observé", "failure_evidence": c["proof"]["observed"][0],
            "requested_by": "Owner produit (demande écrite)", "disposition": "DIFFUSÉ-LIMITÉ"}
    return doc


STATEMENTS = {
    "run_card.example.json": "La première scène reste générique et ne rend pas observable la relation entre le produit et son premier geste.",
    "valid_direction_with_profile_decision.json": "La première scène reste générique et ne rend pas observable la relation entre le produit et son premier geste.",
    "valid_closed_return.json": "Régression clavier ou mobile chez un consommateur du composant partagé.",
}
RESULTS = {"valid_closed_return.json": "FAIL", "invalid_critical_placeholder_protection.json": "NOT-VERIFIED"}
OUTCOMES = {"valid_direction_exploratory_untransformed.json": "NOT-OBSERVED"}
BASIS_OK = [
    {"capability": "artefact disponible", "kind": "attested_environment", "detail": "Artefact construit localement et ouvert dans le run."},
    {"capability": "navigateur/capture disponible", "kind": "tool_result", "detail": "Captures du rendu dans les viewports déclarés."},
]
BASIS = {"run_card.example.json": BASIS_OK, "valid_direction_with_profile_decision.json": BASIS_OK}
ACCEPTING_VALID = {"run_card.example.json", "valid_direction_with_profile_decision.json"}
RESERVATION = {"owner": "design-owner", "scope": "Transition mobile de la première scène", "date_version": "2026-08-29 / V1",
               "impact": "La transition entre découverte et première action reste peu résolue sur mobile.",
               "next_proof": "Revue de la scène mobile et test de la première action.", "review_date": "2026-09-12",
               "exit_condition": "Transition mobile observée sans perte du premier geste."}
B1B = {"status": "DONE", "pair": {"before_locator": "captures/premiere-scene-v1.png", "after_locator": "captures/premiere-scene-v1-sans-objet.png",
                                  "decision": "L’objet directeur porte la relation entre le produit et le premier geste.", "outcome": "confirmed"}}

files = sorted(glob.glob(str(ROOT / "schemas/fixtures/*.json"))) + [str(ROOT / "schemas/run_card.example.json")]
for f in files:
    p = Path(f)
    text = p.read_text(encoding="utf-8")
    style = jsonio.style_of(text)
    assert style[0] != "other", f
    doc = migrate(p.name, json.loads(text))
    p.write_text(jsonio.dump(doc, style), encoding="utf-8")
print(len(files), "fichiers migrés")
