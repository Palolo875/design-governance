#!/usr/bin/env python3
"""Validate DOMAIN_FRAME, RESEARCH_BRIEF and production contracts.

The validator implements the documented dependency-free schema subset and makes
its input explicit: a supplied JSON path is validated, while no argument runs
the complete built-in contract suite.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = {
    "domain_frame": (ROOT / "schemas/domain_frame.schema.json", ROOT / "schemas/examples/domain_frame.example.json"),
    "research_brief": (ROOT / "schemas/research_brief.schema.json", ROOT / "schemas/examples/research_brief.example.json"),
    "production_contracts": (ROOT / "schemas/production_contracts.schema.json", ROOT / "schemas/examples/production_contracts.example.json"),
}
METADATA_KEYS = {"$schema", "$id", "title", "description", "default", "examples"}
SUPPORTED_KEYS = {"type", "enum", "required", "properties", "additionalProperties", "items", "minLength", "minItems", "maxItems"} | METADATA_KEYS


class ValidationError(Exception):
    """Readable validation failure."""


def validate(value: Any, schema: dict[str, Any], path: str = "$") -> None:
    unknown_schema_keys = set(schema) - SUPPORTED_KEYS
    if unknown_schema_keys:
        raise ValidationError(f"{path}: mots-clés de schéma non supportés : {', '.join(sorted(unknown_schema_keys))}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path}: valeur non canonique: {value}")
    if "type" in schema:
        expected = schema["type"]
        checks = {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "boolean": isinstance(value, bool),
            "null": value is None,
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "integer": isinstance(value, int) and not isinstance(value, bool),
        }
        if isinstance(expected, list):
            if not any(checks.get(item, False) for item in expected):
                raise ValidationError(f"{path}: type attendu {'/'.join(expected)}")
        elif not checks.get(expected, False):
            raise ValidationError(f"{path}: type attendu {expected}")
    if isinstance(value, str) and "minLength" in schema and len(value.strip()) < schema["minLength"]:
        raise ValidationError(f"{path}: chaîne vide ou composée uniquement d’espaces")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ValidationError(f"{path}: nombre minimal d'éléments non atteint")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ValidationError(f"{path}: nombre maximal d'éléments dépassé")
        if "items" in schema:
            for index, item in enumerate(value):
                validate(item, schema["items"], f"{path}[{index}]")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                raise ValidationError(f"{path}: champ obligatoire absent: {key}")
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(value) - set(properties))
            if unknown:
                raise ValidationError(f"{path}: champs inconnus: {', '.join(unknown)}")
        for key, child in properties.items():
            if key in value:
                validate(value[key], child, f"{path}.{key}")


def load(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"lecture impossible {path}: {exc}") from exc


def semantic_check(name: str, document: Any) -> None:
    if name == "domain_frame":
        policy = document["policy_profile"]
        if not set(document["domain_risks"]) & set(policy["risk_triggers"]):
            raise ValidationError("policy_profile.risk_triggers doit reprendre au moins un risque déclaré")
        if not set(document["proof_requirements"]) & set(policy["required_controls"]):
            raise ValidationError("policy_profile.required_controls doit être relié au plan de preuve")

    if name == "research_brief":
        if not document["uncertainty_before"].strip() or not document["uncertainty_after"].strip():
            raise ValidationError("uncertainty_before/after ne peuvent pas être vides")
        if document["uncertainty_before"] == document["uncertainty_after"]:
            raise ValidationError("la recherche doit expliciter une évolution de l'incertitude")
        for entry in document["entries"]:
            if not entry["decision_changed"].strip() or not entry["artifact_consequence"].strip():
                raise ValidationError("chaque entrée de recherche doit produire une décision et une conséquence d'artefact")

    if name == "production_contracts":
        creative = document["creative_direction_set"]
        directions = creative["directions"]
        ids = [item["id"] for item in directions]
        if len(ids) != len(set(ids)):
            raise ValidationError("creative_direction_set.directions exige des ids uniques")
        if creative["selected_direction"] not in set(ids):
            raise ValidationError("creative_direction_set.selected_direction doit référencer une direction existante")
        for item in directions:
            if len(item["structural_changes"]) < 2:
                raise ValidationError("chaque direction doit modifier au moins deux relations structurelles")
        reality = document["ui_ux_reality_pack"]
        matrices = reality["state_matrix"] + reality["responsive_matrix"] + reality["accessibility_basis"] + reality["robustness_basis"]
        requirements = {item.strip() for item in matrices if item.strip()}
        covered = {entry["requirement"].strip() for entry in reality["coverage_map"]}
        if not covered:
            raise ValidationError("ui_ux_reality_pack.coverage_map doit contenir au moins une exigence rattachée")
        for requirement in covered:
            if ":" not in requirement:
                raise ValidationError("coverage_map.requirement doit porter le préfixe de sa matrice")
            matrix_name, matrix_value = (part.strip() for part in requirement.split(":", 1))
            matrix = {
                "state_matrix": reality["state_matrix"],
                "responsive_matrix": reality["responsive_matrix"],
                "accessibility_basis": reality["accessibility_basis"],
                "robustness_basis": reality["robustness_basis"],
            }.get(matrix_name)
            matrix_text = " ".join(matrix or [])
            if matrix is None or not all(token in matrix_text for token in matrix_value.split()):
                raise ValidationError("coverage_map contient une exigence absente des matrices déclarées")
        if not reality["proof_scope"].strip():
            raise ValidationError("ui_ux_reality_pack.proof_scope ne peut pas être vide")
        if not requirements:
            raise ValidationError("UI_UX_REALITY_PACK doit déclarer au moins une exigence vérifiable")


def expect_invalid(name: str, schema: dict[str, Any], document: Any, mutation: Any) -> None:
    mutated = mutation(copy.deepcopy(document))
    try:
        validate(mutated, schema)
        semantic_check(name, mutated)
    except ValidationError:
        return
    raise ValidationError(f"mutation négative acceptée à tort: {name}")


def check_negative_mutations(schemas: dict[str, dict[str, Any]], documents: dict[str, Any]) -> None:
    expect_invalid("domain_frame", schemas["domain_frame"], documents["domain_frame"], lambda value: {**value, "policy_profile": {**value["policy_profile"], "risk_triggers": ["risque absent"]}})
    expect_invalid("research_brief", schemas["research_brief"], documents["research_brief"], lambda value: {**value, "uncertainty_after": value["uncertainty_before"]})
    expect_invalid("production_contracts", schemas["production_contracts"], documents["production_contracts"], lambda value: {**value, "ui_ux_reality_pack": {**value["ui_ux_reality_pack"], "coverage_map": []}})
    expect_invalid("production_contracts", schemas["production_contracts"], documents["production_contracts"], lambda value: {**value, "creative_direction_set": {**value["creative_direction_set"], "directions": [value["creative_direction_set"]["directions"][0], value["creative_direction_set"]["directions"][0]]}})


def name_for_path(path: Path) -> str | None:
    resolved = path.resolve()
    for name, (_, example) in CONTRACTS.items():
        if resolved == example.resolve():
            return name
    return None


def validate_single_path(path: Path) -> int:
    name = name_for_path(path)
    if name is None:
        print("CONTRACT VALIDATION FAILED")
        print(f"- chemin non canonique : {path}")
        return 1
    try:
        schema = load(CONTRACTS[name][0])
        document = load(path)
        validate(document, schema)
        semantic_check(name, document)
    except (OSError, ValidationError) as exc:
        print("CONTRACT VALIDATION FAILED")
        print(f"- {exc}")
        return 1
    print(f"CONTRACT VALIDATION PASSED — fichier ciblé : {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valide les contrats de production ou un exemple canonique ciblé.")
    parser.add_argument("path", nargs="?", type=Path, help="exemple JSON canonique à valider seul ; sans argument, exécute la suite complète")
    args = parser.parse_args(argv)
    if args.path is not None:
        return validate_single_path(args.path.expanduser().resolve())

    errors: list[str] = []
    schemas: dict[str, dict[str, Any]] = {}
    documents: dict[str, Any] = {}
    for name, (schema_path, example_path) in CONTRACTS.items():
        try:
            schema = load(schema_path)
            document = load(example_path)
            schemas[name] = schema
            documents[name] = document
            validate(document, schema)
            semantic_check(name, document)
            print(f"+ {name}: valid")
        except ValidationError as exc:
            errors.append(f"{name}: {exc}")
    if not errors:
        try:
            check_negative_mutations(schemas, documents)
            print("+ negative mutations: rejected")
        except ValidationError as exc:
            errors.append(str(exc))
    if errors:
        print("CONTRACT VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("CONTRACT VALIDATION PASSED — domain, research, creative, UI/UX and evaluation contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

