#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R11 ciblé : Q-04 à Q-13 et R-16 à R-32 instruits sur traces, cas négatifs N1 à N5.

Diagnostic : `V12R_22_R11_DIAGNOSTIC.md`. Décision de l'owner (30-09-2026, « Allons-y ») : lot appliqué tel que proposé,
R-16 selon la lecture du propriétaire (`DIRECTION/START`, « Protection de niveau ») : `risk.level` décrit le risque que le
run touche. Schéma et comportement du validateur inchangés (décision 3) : seuls ses messages (locators) et ses cas unitaires
changent. Q-13 et R-25b sont affectés à R6b et R12 ; Q-11 et Q-12 sont maintenus.
Rapport : `V12R_23_R11_CIBLE.md`. Usage : identique à `V12R_Patch_R5b1.py`, plus les mutations de code (N1 à N5, R-28).
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402

A, D, S, G = "V1/official/ACTION.md", "V1/official/DIRECTION.md", "V1/official/SAVOIR.md", "V1/official/GLOSSAIRE.md"
OM, Q, C = "V1/official/ORCHESTRATION_MAP.md", "V1/official/QUICKSTART.md", "V1/official/CHANGELOG.md"
EX = "skills/design-governance-practice/references/examples.md"
VRC, VRM = "scripts/validate_run_card.py", "scripts/validate_reading_map.py"
F = HERE / "V12R_Patch_R11_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("7995a5a70f02f1cd8fc7aa8abddd865a06b878676fe32c0d2805a8860bd5a933", F / "validate_structure.py"),
}

DC = "conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | "
OBS = "Hiérarchie et premier geste observés dans le viewport inspecté."

PATCH = [
    # ---------- Bloquants P2 ----------
    ("R11-Q4a", "CLOSE-PACKAGE, LITE : contrôle machine nommé (Q-04)", A,
     "réserve ou prochaine action, et " + DC + "Forme seule, dans la trace. |",
     "réserve ou prochaine action, et " + DC + "Invariants communs de la `RUN_CARD` si elle existe (états, axes, verdict, preuve) ; "
     "le reste du paquet vit dans la trace. |"),
    ("R11-Q4b", "CLOSE-PACKAGE, ITER : contrôle machine nommé (Q-04)", A,
     "V/U/A/T mis à jour, verdict, risque restant, prochaine action et " + DC + "Forme seule, dans la trace. |",
     "V/U/A/T mis à jour, verdict, risque restant, prochaine action et " + DC + "Invariants communs ; à la clôture, "
     "`decision_change`, `trace_locator` et rappel de direction (`direction.thesis`) ; le reste vit dans la trace. |"),
    ("R11-Q4c", "CLOSE-PACKAGE, STANDARD : contrôle machine nommé (Q-04)", A,
     "états pertinents, V/U/A/T, verdict, risque restant, prochaine action et " + DC + "Forme seule, dans la trace. |",
     "états pertinents, V/U/A/T, verdict, risque restant, prochaine action et " + DC + "Invariants communs ; à la clôture, "
     "`decision_change` et `trace_locator` ; le reste vit dans la trace. |"),
    ("R11-Q4d", "promesse du validateur par mode (Q-04, VAL-01)", A,
     "pour `LITE`, `ITER` et `STANDARD`, le paquet de clôture vit dans la trace et la machine ne le vérifie pas ;",
     "pour `LITE`, `ITER` et `STANDARD`, la machine vérifie les invariants communs et les champs de mode nommés dans la colonne "
     "« Contrôle machine » d’`ACTION/CLOSE-PACKAGE` ; le reste du paquet vit dans la trace et n’est pas vérifié ;"),
    ("R11-Q9a", "one-shot, lieu propriétaire : B1b dans son scope (Q-09)", A,
     "corrige, retourne ou déclare honnêtement la limite.\n\n### 1. Situer les positions",
     "corrige, retourne ou déclare honnêtement la limite. Sur une surface `DIRECTION` acceptée avec V positif, l’arrêt suppose "
     "`ACTION/GATE-B/B1b` fait ou l’un de ses deux motifs `N/A-JUSTIFIED` ; la comparaison peut confirmer la décision initiale "
     "(`confirmed`). En trace légère, la proposition reste `EXPLORATORY` et B1b ne s’applique pas.\n\n### 1. Situer les positions"),
    ("R11-Q9b", "one-shot, ACTION (intention) : renvoi B1b (Q-09)", A,
     "et aucune correction ne promet un gain réel ; il ne peut jamais être clôturé sans observation du rendu.",
     "et aucune correction ne promet un gain réel (B1b dans son scope, `ACTION/GATE-B/B1b`) ; il ne peut jamais être clôturé sans "
     "observation du rendu."),
    ("R11-Q9c", "one-shot, DIRECTION : renvoi B1b (Q-09)", D,
     "et qu’aucune amélioration utile ne promet un gain réel. Si le rendu est faible,",
     "et qu’aucune amélioration utile ne promet un gain réel (B1b dans son scope, `ACTION/GATE-B/B1b`). Si le rendu est faible,"),
    ("R11-R16", "protection critique : exclusion conditionnelle de START (R-16)", A,
     "Un risque critique exclut `LITE` et `ITER` (`DIRECTION/START`).",
     "Un risque critique que le changement touche exclut `LITE` et `ITER` (`DIRECTION/START`, « Protection de niveau ») ; un delta "
     "démontré strictement local et sans effet sur ce risque ne le déclare pas comme risque du run."),
    ("R11-R21", "ancre transformed : exigence limitée à DIRECTION (R-21)", A,
     "Une ancre `transformed` est compatible avec tout verdict ; elle est requise pour l’acceptation.",
     "En `DIRECTION`, un verdict accepté exige que chaque ancre soit `transformation_status: transformed`."),
    # ---------- Non bloquants ----------
    ("R11-Q7", "scopes de la direction et de l'artefact ; source de la contrainte (Q-07)", A,
     "contrainte (`DIRECTION/VISUAL_TARGET`, « Qualifier la direction ») ; périmètre (`SCOPE`) |",
     "contrainte (`CONSTRAINT` de `DIRECTION/START`) ; surfaces couvertes par la direction (facultatif ; distinct "
     "d’`artifact.scope`, scope observé de l’artefact) |"),
    ("R11-Q8", "sortie par mode : source et précisions (Q-08)", A,
     "La sortie à conserver de chaque mode est définie une seule fois, par `ACTION/CLOSE-PACKAGE`.",
     "Le paquet de sortie de chaque mode est défini par `ACTION/CLOSE-PACKAGE` ; `ACTION/RUN-DIRECTION` (ancrages) et "
     "`ACTION/RUN-SYSTEM` (`closure.system_package`) en précisent le détail."),
    ("R11-R17", "B1b : correspondance modified / CHANGED (R-17)", A,
     "`decision` et `outcome` (`confirmed`, `modified` ou `abandoned`).",
     "`decision` et `outcome` (`confirmed`, `modified` ou `abandoned` ; `modified` correspond à `CHANGED` de `decision_change`)."),
    ("R11-R18a", "triade définie (R-18)", A,
     "changée · confirmée · abandonnée · `N/A-JUSTIFIED` (aucune conséquence applicable",
     "changée · confirmée · abandonnée (la triade) ; sinon, l’une des deux valeurs de repli : `N/A-JUSTIFIED` (aucune conséquence applicable"),
    ("R11-R18b", "outcome : triade et replis (R-18)", A,
     "dont `outcome` porte la triade de `ACTION/STATUS` ;",
     "dont `outcome` porte la triade et les deux valeurs de repli d’`ACTION/STATUS` ;"),
    ("R11-R18c", "table des champs : valeurs de repli (R-18)", A,
     "sinon la triade d’`ACTION/STATUS` : `N/A-JUSTIFIED`", "sinon l’une des valeurs de repli d’`ACTION/STATUS` : `N/A-JUSTIFIED`"),
    ("R11-R18d", "DIRECTION, clôture : valeurs de repli (R-18)", D,
     "abandonnée, la triade d’`ACTION/STATUS` s’applique", "abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent"),
    ("R11-R18e", "DIRECTION, premier objet : valeurs de repli (R-18)", D,
     "sinon la triade d’`ACTION/STATUS` s’applique", "sinon les valeurs de repli d’`ACTION/STATUS` s’appliquent"),
    ("R11-R18f", "GLOSSAIRE : valeurs de repli (R-18)", G,
     "Sinon, la triade d’`ACTION/STATUS` s’applique", "Sinon, les valeurs de repli d’`ACTION/STATUS` s’appliquent"),
    ("R11-R18g", "SAVOIR, sortie : valeurs de repli (R-18)", S,
     "abandonnée, la triade d’`ACTION/STATUS` s’applique", "abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent"),
    ("R11-R18h", "SAVOIR, test de sortie : valeurs de repli (R-18)", S,
     "(triade d’`ACTION/STATUS`)", "(valeurs de repli d’`ACTION/STATUS`)"),
    ("R11-R19", "table de correspondance : decision_change selon le schéma (R-19)", A,
     "`decision_change` (`outcome`, `reason`)", "`decision_change` (`outcome`, `value`, `evidence` ; `reason` exigé si `N/A-JUSTIFIED`, non exigé si `NOT-OBSERVED`)"),
    ("R11-R20", "calibration : objet, base nommée (R-20)", D,
     "cette base est `direction.calibration` : `real_constraint`", "cette base est `direction.calibration.basis` : `real_constraint`"),
    ("R11-R23", "GLOSSAIRE, exemple CHANGED (R-23)", G,
     "est abandonnée au profit d’un CTA principal unique", "est remplacée par un CTA principal unique"),
    ("R11-R24", "exemple SYSTÈME : abandon, pas report (R-24)", EX,
     "DECISION-CHANGE: ABANDONED — l’extension du Select en l’état est abandonnée jusqu’à correction de la troncature mobile "
     "(observation : consommateur 2)",
     "DECISION-CHANGE: ABANDONED — l’extension du Select en l’état est abandonnée : la troncature mobile casse ce consommateur ; "
     "une version corrigée reprend dans le même mode (observation : consommateur 2)"),
    ("R11-R26", "ORCHESTRATION_MAP : COMPONENTS sous condition (R-26)", OM,
     "`ACTION/RUN-SYSTEM` + `BIBLIOTHEQUE/COMPONENTS` + migration,",
     "`ACTION/RUN-SYSTEM` + `BIBLIOTHEQUE/COMPONENTS` si un composant change + migration,"),
    ("R11-R27", "QUICKSTART : lecteur de routes (R-27)", Q,
     "Le lecteur résout le locator dans `READING_MAP.md`, vérifie le titre exact du propriétaire et n’affiche que le bloc demandé.",
     "Le lecteur résout le locator selon `READING_MAP.md` (raccourci, titre propriétaire, puis sous-locator) et n’affiche que le "
     "bloc demandé."),
    ("R11-R28a", "validateur : locator nommé (R-28)", VRC,
     "un risque critical interdit le mode LITE ou ITER (DIRECTION 140)",
     "un risque critical interdit le mode LITE ou ITER (DIRECTION/START, Protection de niveau)"),
    ("R11-R28b", "validateur : locator nommé (R-28)", VRC,
     "DIRECTION sans ancrage exige une issue (sérialisation honnête, ACTION 483)",
     "DIRECTION sans ancrage exige une issue (sérialisation honnête, ACTION/PIPELINE-DIRECTION)"),
    ("R11-R28c", "validateur : locator nommé (R-28)", VRC,
     "ITER exige un rappel de direction (direction.thesis) ; sinon reclasser (DIRECTION 672)",
     "ITER exige un rappel de direction (direction.thesis) ; sinon reclasser (DIRECTION, ITER se souvient)"),
    ("R11-R28d", "LCF-08 : propriétaire de la règle (R-28)", VRM,
     "\"ACTION/RUN_CARD (OWNER et SCOPE jamais omis)\"", "\"DIRECTION/START (OWNER et SCOPE jamais omis)\""),
    ("R11-R29", "zéro contrat : aucun fichier dû (R-29)", A,
     "Zéro contrat est valide lorsqu’aucun déclencheur n’est actif.",
     "Zéro contrat est valide lorsqu’aucun déclencheur n’est actif : aucun fichier `production_contracts` n’est alors produit ; "
     "un fichier présent en porte au moins un."),
    ("R11-R30", "champ voisin : hors table (R-30)", A,
     "jamais glissé dans un champ voisin (par exemple", "jamais glissé dans un champ voisin non prévu par cette table (par exemple"),
    ("R11-R31", "SAVOIR : règle de START non généralisée (R-31)", S,
     "sinon la direction est traitée d’abord et le run système dépendant est ouvert ensuite (`DIRECTION/START/TREE`).",
     "si elle découle d’une décision de direction, la direction est traitée d’abord et le run système dépendant ouvert ensuite, "
     "sauf décisions inséparables (`DIRECTION/START/TREE`)."),
    # ---------- Cas négatifs manquants (N1 à N5) ----------
    ("R11-N", "cas unitaires N1 à N5", VRC,
     "    (\"D2-2\", RETURNED, ITER, ((RC, \"direction\"), DELETE), \"rappel de direction\"),\n]",
     "    (\"D2-2\", RETURNED, ITER, ((RC, \"direction\"), DELETE), \"rappel de direction\"),\n"
     "    # Cas négatifs manquants (R11 ciblé, V12R_22 §5) : une règle, un cas.\n"
     "    (\"N1\", EXAMPLE, [], ((RC, \"proof\", \"provenance\", \"artifact_locator\"), \"autre-chemin-local\"), "
     "\"artifact_locator doit correspondre à artifact.locator\"),\n"
     f"    (\"N2\", EXAMPLE, [], ((RC, \"proof\", \"not_verified\"), [\"{OBS}\"]), \"ne peuvent pas contenir le même claim\"),\n"
     "    (\"N3\", EXAMPLE, [((RC, \"risk\"), CRITICAL)], ((RC, \"risk\", \"critical_protection\", \"failure_action\"), \"CONTINUE\"), "
     "\"failure_action doit retourner, bloquer ou escalader\"),\n"
     "    (\"N4a\", EXAMPLE, [((RC, \"risk\"), CRITICAL)], ((RC, \"risk\", \"critical_protection\", \"owner\"), DELETE), "
     "\"critical_protection exige le champ owner\"),\n"
     "    (\"N4b\", EXAMPLE, [((RC, \"risk\"), CRITICAL)], ((RC, \"risk\", \"critical_protection\", \"evidence_locator\"), DELETE), "
     "\"critical_protection exige le champ evidence_locator\"),\n"
     "    (\"N5\", EXAMPLE, [], ((RC, \"proof\", \"provenance\", \"method\"), DELETE), \"proof.provenance exige le champ method\"),\n]"),
    # ---------- Historique ----------
    ("R11-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Cohérence ciblée (refonte, R11).** Contrôle machine nommé par mode (paquets de clôture, promesse du validateur) ; arrêt "
     "one-shot relié à B1b ; exclusion LITE/ITER alignée sur la protection de niveau ; ancre `transformed` exigée en DIRECTION ; "
     "triade définie, valeurs de repli nommées ; références alignées sur le schéma et les propriétaires ; locators nommés dans "
     "les messages du validateur ; six cas négatifs ajoutés. Schéma et comportement du validateur inchangés.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

MUTATION_OF = {
    "R11-Q4a": "vocabulaire retiré", "R11-Q4b": "vocabulaire retiré", "R11-Q4c": "vocabulaire retiré",
    "R11-Q4d": "vocabulaire retiré", "R11-Q9a": "arrêt one-shot et B1b", "R11-Q9b": "arrêt one-shot et B1b",
    "R11-Q9c": "arrêt one-shot et B1b", "R11-R16": "vocabulaire retiré", "R11-R21": "vocabulaire retiré",
    "R11-Q7": "scopes de la direction", "R11-Q8": "vocabulaire retiré", "R11-R17": "B1b et decision_change",
    "R11-R18b": "vocabulaire retiré", "R11-R18c": "vocabulaire retiré", "R11-R18d": "vocabulaire retiré",
    "R11-R18e": "vocabulaire retiré", "R11-R18f": "vocabulaire retiré", "R11-R18g": "vocabulaire retiré",
    "R11-R18h": "vocabulaire retiré", "R11-R19": "vocabulaire retiré", "R11-R20": "vocabulaire retiré",
    "R11-R23": "vocabulaire retiré", "R11-R24": "vocabulaire retiré", "R11-R26": "COMPONENTS en SYSTÈME",
    "R11-R27": "vocabulaire retiré", "R11-R28a": "[LOC-01]", "R11-R28b": "[LOC-01]", "R11-R28c": "[LOC-01]",
    "R11-R29": "zéro contrat", "R11-R30": "champ voisin", "R11-R31": "vocabulaire retiré",
}
# Sans garde propre (déclaré) : R18a (définition ajoutée), R28d (libellé de LCF), H1 (historique) ;
# R-16 : l'ancien texte est retiré ET la nouvelle phrase garde « strictement local » (fidélité).
EXTRA_MUTATIONS = [
    ("exclusion critique sans sa condition", A,
     " ; un delta démontré strictement local et sans effet sur ce risque ne le déclare pas comme risque du run.", ".",
     "protection de niveau"),
    ("promesse du validateur sans invariants communs", A, "la machine vérifie les invariants communs et les champs de mode",
     "la machine vérifie des champs de mode", "promesse du validateur"),
]

# Mutations de code : la règle retirée, son cas unitaire doit rougir dans validate_run_card.py.
CODE_MUTATIONS = [
    ("N1", "and provenance.get(\"artifact_locator\") != artifact.get(\"locator\"):", "and False:", ["N1"]),
    ("N2", "            if overlap:\n", "            if False:\n", ["N2"]),
    ("N3", "if protection.get(\"failure_action\") not in {\"RETURNED\", \"BLOCKED\", \"ESCALATED\"}:", "if False:", ["N3"]),
    ("N4", "for field in (\"control\", \"owner\", \"scope\", \"failure_action\", \"evidence_locator\"):",
     "for field in (\"control\", \"scope\", \"failure_action\"):", ["N4a", "N4b"]),
    ("N5", "for field in (\"artifact_locator\", \"artifact_version\", \"method\", \"observed_at\"):",
     "for field in (\"artifact_locator\", \"artifact_version\", \"observed_at\"):", ["N5"]),
]


# Migration M1 (trois cas de harnais) : leur mutation inversait une entrée historique (R.01 P-01, R.03 P-40 et P-56) dont
# R-18 a réécrit le texte (« triade » → « valeurs de repli »). La propriété — LCF-22 et LCF-38 dans la liste close et
# rouges sous mutation — est reprise ici par une mutation équivalente sur le texte courant (NOT-OBSERVED retiré).
LCF_MUTATIONS = [
    ("R R-15 (LCF-22)", A, ", `NOT-OBSERVED` si une conséquence attendue n’a pas été observée (interdit `ACCEPTED`)", "", "LCF-22"),
    ("R03 R3-10 (LCF-38)", S, " ni `NOT-OBSERVED` déclaré (valeurs de repli", " (valeurs de repli", "LCF-38"),
    ("R03 R3-17 (LCF-38)", S, "`N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue "
     "n’a pas été observée.", "`N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable.", "LCF-38"),
]


def lcf_mutations(root: Path) -> int:
    bad = 0
    for name, rel, old, new, lcf in LCF_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(copy / VRM)], capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and f"{lcf} :" in out.stdout + out.stderr
            print(f"mutation LCF {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def code_mutations(root: Path) -> int:
    bad = 0
    for name, old, new, cases in CODE_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            p = copy / VRC
            t = p.read_text(encoding="utf-8")
            ok = t.count(old) == 1
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            out = subprocess.run([sys.executable, "-B", str(p)], capture_output=True, text=True, cwd=copy)
            text = out.stdout + out.stderr
            red = ok and out.returncode != 0 and all(f"cas unitaire {c} " in text for c in cases)
            print(f"mutation de code {name} (règle retirée) : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, EXTRA_MUTATIONS
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        root = Path(sys.argv[1]).resolve()
        return 1 if base.mutations(root) + code_mutations(root) + lcf_mutations(root) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
