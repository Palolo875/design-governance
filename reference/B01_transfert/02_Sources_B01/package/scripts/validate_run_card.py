#!/usr/bin/env python3
"""Validation autonome de la projection JSON RUN_CARD de Design Governance V1.

Le schéma JSON est la source des règles de structure et de vocabulaire. Le code
ci-dessous ne recopie pas ses enums : il implémente uniquement le petit sous-
ensemble de JSON Schema utilisé par le fichier livré.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "run_card.schema.json"
EXAMPLE = ROOT / "schemas" / "run_card.example.json"
FIXTURES = ROOT / "schemas" / "fixtures"


class ValidationError(Exception):
    """Erreur de validation avec un chemin lisible dans le document."""


def format_path(path: str) -> str:
    return path or "$"


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    raise ValidationError(f"type de schéma non pris en charge : {expected}")


def validate_node(value: Any, schema: dict[str, Any], path: str = "") -> None:
    """Valide la projection JSON de RUN_CARD et ses invariants sémantiques V1."""
    if "allOf" in schema:
        for condition in schema["allOf"]:
            if_schema = condition.get("if", {})
            if_matches = True
            if "required" in if_schema and isinstance(value, dict):
                if_matches = all(key in value for key in if_schema["required"])
            if if_matches and isinstance(value, dict):
                for key, child in if_schema.get("properties", {}).items():
                    if key in value:
                        try:
                            validate_node(value[key], child, f"{path}.{key}" if path else key)
                        except ValidationError:
                            if_matches = False
                            break
                    else:
                        if_matches = False
                        break
            if if_matches:
                validate_node(value, condition.get("then", {}), path)

    if "anyOf" in schema:
        branch_errors: list[str] = []
        for branch in schema["anyOf"]:
            try:
                validate_node(value, branch, path)
                break
            except ValidationError as exc:
                branch_errors.append(str(exc))
        else:
            details = " ; ".join(branch_errors)
            raise ValidationError(f"{format_path(path)} : aucune branche anyOf satisfaite ({details})")

    if "const" in schema and value != schema["const"]:
        raise ValidationError(f"{format_path(path)} : valeur non canonique : {value}")

    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{format_path(path)} : valeur non canonique : {value}")

    if "type" in schema:
        expected = schema["type"]
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(type_matches(value, item) for item in expected_types):
            names = ", ".join(expected_types)
            raise ValidationError(f"{format_path(path)} : type attendu {names}")

    if isinstance(value, str) and "minLength" in schema:
        if len(value.strip()) < schema["minLength"]:
            raise ValidationError(f"{format_path(path)} : chaîne vide ou composée uniquement d’espaces")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise ValidationError(f"{format_path(path)} : nombre minimal d’éléments non atteint")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_node(item, schema["items"], f"{path}[{index}]")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                raise ValidationError(f"{format_path(path)} : champ obligatoire absent : {key}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(value) - set(properties))
            if unknown:
                raise ValidationError(f"{format_path(path)} : champs inconnus : {', '.join(unknown)}")

        for key, child_schema in properties.items():
            if key in value:
                child_path = f"{path}.{key}" if path else key
                validate_node(value[key], child_schema, child_path)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        try:
            display_path = path.relative_to(ROOT)
        except ValueError:
            display_path = path
        raise ValidationError(f"lecture JSON impossible pour {display_path} : {exc}") from exc


def check_held_message(document: Any) -> None:
    """Expose le diagnostic métier historique avant le rejet d’enum générique."""
    if not isinstance(document, dict):
        return
    card = document.get("run_card")
    if not isinstance(card, dict):
        return
    closure = card.get("closure")
    if isinstance(closure, dict) and closure.get("state") == "HELD":
        raise ValidationError("HELD est un statut de direction, pas une valeur de state")


def check_semantic_contract(document: Any) -> None:
    """Contrôle les invariants métier explicitement documentés par ACTION."""
    if not isinstance(document, dict):
        return
    card = document.get("run_card")
    if not isinstance(card, dict):
        return

    mode = card.get("mode")
    capability_profile = card.get("capability_profile")
    if isinstance(capability_profile, dict):
        available = capability_profile.get("available")
        basis = capability_profile.get("basis")
        if isinstance(available, list) and available and (not isinstance(basis, list) or not basis):
            raise ValidationError("capability_profile exige basis non vide lorsque available contient un élément")
    risk = card.get("risk")
    if isinstance(risk, dict) and risk.get("level") == "critical":
        protection = risk.get("critical_protection")
        if not isinstance(protection, dict):
            raise ValidationError("un risque critical exige une critical_protection structurée")
        required_protection = ("control", "owner", "scope", "failure_action", "evidence_locator")
        for field in required_protection:
            value = protection.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValidationError(f"critical_protection exige le champ {field}")
            if value.strip().lower() in {"todo", "tbd", "à définir", "a definir", "placeholder", "n/a"}:
                raise ValidationError(f"critical_protection.{field} ne peut pas être un placeholder")
        if protection.get("failure_action") not in {"RETURNED", "BLOCKED", "ESCALATED"}:
            raise ValidationError("critical_protection.failure_action doit retourner, bloquer ou escalader")
    closure = card.get("closure")
    if not isinstance(closure, dict):
        return

    if mode == "DIRECTION":
        direction = card.get("direction")
        if not isinstance(direction, dict):
            raise ValidationError("DIRECTION exige un objet direction avec thèse, anti-direction et premier objet")
        for field in ("thesis", "anti_direction", "first_object"):
            value = direction.get(field)
            if field == "anti_direction":
                if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                    raise ValidationError("DIRECTION exige une anti_direction non vide")
            elif not isinstance(value, str) or not value.strip():
                raise ValidationError(f"DIRECTION exige le champ direction.{field}")
        if not card.get("trace_locator"):
            raise ValidationError("DIRECTION exige trace_locator pour une RUN_CARD persistante")
        if closure.get("state") in {"DECIDED", "CLOSED"} and not closure.get("direction_status"):
            raise ValidationError("DIRECTION décidée ou clôturée exige direction_status")
        anchors = card.get("anchors")
        if not isinstance(anchors, list) or not anchors:
            raise ValidationError("DIRECTION exige au moins un ancrage structuré")
        for anchor in anchors:
            if not isinstance(anchor, dict):
                raise ValidationError("chaque ancrage DIRECTION doit être structuré")
            status = anchor.get("transformation_status")
            if status == "transformed" and closure.get("verdict") in {"EXPLORATORY", "RETURN", "RETURN-DIRECTION"}:
                raise ValidationError("transformation_status transformed incompatible avec un verdict exploratoire ou de retour")
            if closure.get("verdict") in {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"} and status != "transformed":
                raise ValidationError("un verdict accepté exige transformation_status transformed")
        profile_decision = card.get("profile_decision")
        if profile_decision is not None:
            if not isinstance(profile_decision, dict):
                raise ValidationError("profile_decision doit être un objet")
            for field in ("decision", "dials", "counterindication", "evidence"):
                value = profile_decision.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise ValidationError(f"profile_decision : champ obligatoire absent : {field}")
        creative_close = card.get("creative_close")
        if closure.get("state") == "CLOSED":
            if not isinstance(creative_close, dict):
                raise ValidationError("DIRECTION clôturée exige creative_close")
            required_creative_fields = ("presence", "signature", "craft_detail", "dominant_defect", "next_polish_action")
            for field in required_creative_fields:
                value = creative_close.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise ValidationError(f"creative_close exige le champ {field}")
        for anchor in anchors:
            for field in ("role", "source", "date", "scope", "transformation", "transformation_status", "limitation"):
                if not isinstance(anchor.get(field), str) or not anchor[field].strip():
                    raise ValidationError(f"ancrage DIRECTION incomplet : {field}")
            for field in ("retained", "rejected"):
                value = anchor.get(field)
                if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
                    raise ValidationError(f"ancrage DIRECTION exige {field} non vide")

    if mode in {"STANDARD", "SYSTÈME"} and not card.get("trace_locator"):
        raise ValidationError(f"{mode} exige trace_locator pour une RUN_CARD persistante")

    verdict = closure.get("verdict")
    issue = closure.get("issue")
    if closure.get("direction_status") == "LOST-IN-BUILD" and verdict in {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"}:
        raise ValidationError("LOST-IN-BUILD ne peut pas produire un verdict accepté")
    if issue in {"BLOCKED", "FAIL-ASSUMED"} and verdict in {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"}:
        raise ValidationError("une issue bloquante ou FAIL-ASSUMED ne peut pas produire un verdict accepté")
    proof = card.get("proof")
    if isinstance(proof, dict):
        observed = proof.get("observed")
        not_verified = proof.get("not_verified")
        if isinstance(observed, list) and isinstance(not_verified, list):
            overlap = sorted(set(observed) & set(not_verified))
            if overlap:
                raise ValidationError("proof.observed et proof.not_verified ne peuvent pas contenir le même claim")
    if verdict in {"ACCEPTED", "ACCEPTED-WITH-RESERVATION"}:
        if closure.get("state") not in {"DECIDED", "CLOSED"}:
            raise ValidationError("un verdict accepté exige state DECIDED ou CLOSED")
        if not isinstance(proof, dict) or not isinstance(proof.get("observed"), list) or not proof["observed"]:
            raise ValidationError("un verdict accepté exige au moins une preuve observed")
        provenance = proof.get("provenance") if isinstance(proof, dict) else None
        if not isinstance(provenance, dict):
            raise ValidationError("un verdict accepté exige proof.provenance")
        for field in ("artifact_locator", "artifact_version", "method", "observed_at"):
            value = provenance.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValidationError(f"proof.provenance exige le champ {field}")
        artifact = card.get("artifact")
        if isinstance(artifact, dict) and provenance.get("artifact_locator") != artifact.get("locator"):
            raise ValidationError("proof.provenance.artifact_locator doit correspondre à artifact.locator")
        limitations = closure.get("limitations")
        if not isinstance(limitations, list) or not limitations:
            raise ValidationError("un verdict accepté exige une limitation non vide")

    if closure.get("state") == "CLOSED" and mode == "DIRECTION" and not card.get("decision_change"):
        if verdict not in {"EXPLORATORY", "RETURN", "RETURN-DIRECTION", "SYSTEM-ESCALATION"} and closure.get("issue") not in {"BLOCKED", "RETURNED", "EXPLORATORY", "FAIL-ASSUMED", "ESCALATED"}:
            raise ValidationError("une DIRECTION clôturée sans decision_change exige N/A-JUSTIFIED, une issue ou un verdict non accepté")


def check_strict_contract(document: Any, source_path: Path) -> None:
    """Reject exact placeholders and verify declared local/URL locators."""
    exact_placeholders = {
        "lorem ipsum",
        "chemin-ou-url-local",
        "ticket-ou-chemin-de-run",
        "à définir",
        "a definir",
        "todo",
        "tbd",
        "placeholder",
    }
    placeholder_hosts = {"example.invalid", "example.com", "example.org", "example.net"}

    def walk(value: Any, path: str = "") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else key)
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")
        elif isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in exact_placeholders:
                raise ValidationError(f"strict : placeholder ou texte générique dans {path}")

    walk(document)
    card = document.get("run_card") if isinstance(document, dict) else None
    artifact = card.get("artifact") if isinstance(card, dict) else None
    locator = artifact.get("locator") if isinstance(artifact, dict) else None
    if not isinstance(locator, str) or not locator.strip():
        raise ValidationError("strict : artifact.locator doit être renseigné")
    locator = locator.strip()
    trace_locator = card.get("trace_locator") if isinstance(card, dict) else None
    if not isinstance(trace_locator, str) or not trace_locator.strip():
        raise ValidationError("strict : trace_locator doit être renseigné")
    parsed_trace = urlparse(trace_locator.strip())
    if parsed_trace.scheme in {"http", "https"} and parsed_trace.hostname in placeholder_hosts:
        raise ValidationError(f"strict : trace_locator URL de démonstration interdite : {trace_locator}")
    if locator.startswith("file://"):
        candidate = Path(locator.removeprefix("file://"))
        if not candidate.exists():
            raise ValidationError(f"strict : artefact local absent : {locator}")
    elif not re.match(r"^[a-z][a-z0-9+.-]*://", locator, re.I) and (locator.startswith(("/", "./", "../")) or "/" in locator):
        candidate = Path(locator)
        if not candidate.is_absolute():
            candidate = ROOT / candidate
        if not candidate.exists():
            raise ValidationError(f"strict : artefact local absent : {locator}")


def validate_card(document: Any, schema: dict[str, Any], strict: bool = False, source_path: Path | None = None) -> None:
    check_held_message(document)
    # Donner priorité aux diagnostics métier lisibles avant les exigences
    # conditionnelles du schéma, sans relâcher la validation structurelle.
    check_semantic_contract(document)
    if strict:
        check_strict_contract(document, source_path or EXAMPLE)
    validate_node(document, schema)


def check_fixture(
    path: Path,
    schema: dict[str, Any],
    should_pass: bool,
    errors: list[str],
    expected_message: str | None = None,
) -> None:
    try:
        validate_card(load_json(path), schema)
    except ValidationError as exc:
        if should_pass:
            errors.append(f"fixture valide rejetée — {path.relative_to(ROOT)} : {exc}")
        elif expected_message and expected_message not in str(exc):
            errors.append(
                f"diagnostic inattendu — {path.relative_to(ROOT)} : attendu {expected_message!r}, obtenu {str(exc)!r}"
            )
        return
    if not should_pass:
        errors.append(f"fixture invalide acceptée — {path.relative_to(ROOT)}")


def check_schema_authority(schema: dict[str, Any], errors: list[str]) -> None:
    """Régression : une modification d’enum dans le schéma doit modifier le résultat."""
    document = load_json(EXAMPLE)
    altered_schema = json.loads(json.dumps(schema))
    altered_schema["properties"]["run_card"]["properties"]["mode"]["enum"] = ["SCHEMA-DRIVEN-TEST"]
    document["run_card"]["mode"] = "SCHEMA-DRIVEN-TEST"
    try:
        validate_card(document, altered_schema)
    except ValidationError as exc:
        errors.append(f"le validateur n’utilise pas l’enum du schéma : {exc}")


def validate_single_path(path: Path, schema: dict[str, Any], strict: bool = False) -> int:
    """Valide uniquement le fichier demandé par l’utilisateur ou un pipeline."""
    try:
        validate_card(load_json(path), schema, strict=strict, source_path=path)
    except (OSError, ValidationError) as exc:
        print("RUN_CARD VALIDATION FAILED")
        print(f"- {exc}")
        return 1
    print(f"RUN_CARD VALIDATION PASSED — fichier ciblé : {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valide la projection RUN_CARD ou la suite intégrée de fixtures."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="fichier JSON à valider seul ; sans argument, exécute la suite complète",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="rejette les placeholders et vérifie les locators d’artefacts locaux ; nécessite un chemin JSON",
    )
    args = parser.parse_args(argv)
    errors: list[str] = []
    if not SCHEMA.is_file():
        errors.append("schéma absent : schemas/run_card.schema.json")
    else:
        try:
            schema = load_json(SCHEMA)
            if not isinstance(schema, dict):
                raise ValidationError("le schéma racine doit être un objet")
        except ValidationError as exc:
            errors.append(str(exc))
            schema = {}

    if args.strict and args.path is None:
        print("RUN_CARD VALIDATION FAILED")
        print("- --strict exige un fichier JSON ciblé")
        return 1
    if schema and args.path is not None:
        path = args.path.expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        return validate_single_path(path.resolve(), schema, strict=args.strict)

    if schema:
        check_fixture(EXAMPLE, schema, True, errors)
        check_fixture(FIXTURES / "valid_closed_return.json", schema, True, errors)
        check_fixture(
            FIXTURES / "invalid_state_held.json",
            schema,
            False,
            errors,
            expected_message="HELD est un statut de direction, pas une valeur de state",
        )
        check_fixture(FIXTURES / "invalid_missing_proof.json", schema, False, errors)
        check_fixture(
            FIXTURES / "invalid_empty_proof.json",
            schema,
            False,
            errors,
            expected_message="un verdict accepté exige au moins une preuve observed",
        )
        check_fixture(
            FIXTURES / "invalid_global_axis_verdict.json",
            schema,
            False,
            errors,
            expected_message="closure.verdict : valeur non canonique : PASS",
        )
        check_fixture(
            FIXTURES / "invalid_direction_missing_object.json",
            schema,
            False,
            errors,
            expected_message="DIRECTION exige un objet direction",
        )
        check_fixture(
            FIXTURES / "invalid_direction_missing_trace_locator.json",
            schema,
            False,
            errors,
            expected_message="DIRECTION exige trace_locator",
        )
        check_fixture(
            FIXTURES / "invalid_direction_missing_creative_close.json",
            schema,
            False,
            errors,
            expected_message="DIRECTION clôturée exige creative_close",
        )
        check_fixture(
            FIXTURES / "invalid_direction_missing_status.json",
            schema,
            False,
            errors,
            expected_message="DIRECTION décidée ou clôturée exige direction_status",
        )
        check_fixture(
            FIXTURES / "invalid_creative_close_missing_field.json",
            schema,
            False,
            errors,
            expected_message="creative_close exige le champ craft_detail",
        )
        check_fixture(
            FIXTURES / "valid_direction_with_profile_decision.json",
            schema,
            True,
            errors,
        )
        check_fixture(
            FIXTURES / "invalid_profile_decision_missing_evidence.json",
            schema,
            False,
            errors,
            expected_message="profile_decision : champ obligatoire absent : evidence",
        )
        check_fixture(
            FIXTURES / "invalid_accepted_before_decision.json",
            schema,
            False,
            errors,
            expected_message="un verdict accepté exige state DECIDED ou CLOSED",
        )
        check_fixture(
            FIXTURES / "invalid_accepted_without_provenance.json",
            schema,
            False,
            errors,
            expected_message="un verdict accepté exige proof.provenance",
        )
        check_fixture(
            FIXTURES / "invalid_accepted_without_limitations.json",
            schema,
            False,
            errors,
            expected_message="verdict accepté exige une limitation non vide",
        )
        check_fixture(
            FIXTURES / "invalid_accepted_without_observed.json",
            schema,
            False,
            errors,
            expected_message="verdict accepté exige au moins une preuve observed",
        )
        check_fixture(
            FIXTURES / "invalid_fail_assumed_accepted.json",
            schema,
            False,
            errors,
            expected_message="issue bloquante ou FAIL-ASSUMED",
        )
        check_fixture(
            FIXTURES / "valid_direction_exploratory_untransformed.json",
            schema,
            True,
            errors,
        )
        check_fixture(
            FIXTURES / "invalid_capability_available_without_basis.json",
            schema,
            False,
            errors,
            expected_message="capability_profile exige basis non vide",
        )
        check_fixture(
            FIXTURES / "invalid_critical_without_protection.json",
            schema,
            False,
            errors,
            expected_message="un risque critical exige une critical_protection structurée",
        )
        check_fixture(
            FIXTURES / "invalid_critical_placeholder_protection.json",
            schema,
            False,
            errors,
            expected_message="critical_protection.control ne peut pas être un placeholder",
        )
        check_fixture(
            FIXTURES / "invalid_accepted_lost_in_build.json",
            schema,
            False,
            errors,
            expected_message="LOST-IN-BUILD ne peut pas produire un verdict accepté",
        )
        check_fixture(
            FIXTURES / "invalid_lite_missing_minimum.json",
            schema,
            False,
            errors,
            expected_message="run_card : champ obligatoire absent : risk",
        )
        check_fixture(
            FIXTURES / "invalid_direction_untransformed_anchor.json",
            schema,
            False,
            errors,
            expected_message="un verdict accepté exige transformation_status transformed",
        )
        check_schema_authority(schema, errors)

    if errors:
        print("RUN_CARD VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RUN_CARD VALIDATION PASSED — projection validée contre le schéma et fixtures contrôlés")
    return 0


if __name__ == "__main__":
    sys.exit(main())

