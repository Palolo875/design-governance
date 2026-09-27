#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R4 : noyau de fabrication compilé, liste de chargement unique, sortie en langage produit.

Décisions : 1, 4, 7 (V12R_00) ; R4 validé par l'owner le 2026-09-27 (V12R_04_PROPOSITION_R4) : noyau par sélection de
paragraphes canoniques, liste canonique `DIRECTION/CHARGE`, allègement du chargement par défaut.
Deux passes : (1) contenus, déplacements et nouveaux textes ; (2) balisage des blocs du noyau sur le texte obtenu ;
puis nouveaux fichiers et compilation. Usage :
  python3 V12R_Patch_R4.py <racine>                 # applique
  python3 V12R_Patch_R4.py <racine> --verifier      # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12R_Patch_R4.py <racine> --mutations     # sur une racine patchée : chaque garde rougit sous sa mutation
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from V12_Patch_ABD import apply  # noqa: E402

D, A, S, B = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md", "V1/official/BIBLIOTHEQUE.md"
Q, C = "V1/official/QUICKSTART.md", "V1/official/CHANGELOG.md"
RM, OM = "V1/official/READING_MAP.md", "V1/official/ORCHESTRATION_MAP.md"
SK = "skills/design-governance-practice/SKILL.md"
EX = "skills/design-governance-practice/references/examples.md"
V = "scripts/validate_reading_map.py"
FILES = HERE / "V12R_Patch_R4_fichiers"

FILE_REPLACE = {  # chemin → (empreinte attendue avant, nouvelle version)
    "scripts/validate_structure.py": ("2399466e922f3bb6c5d024f9821b475e3c692f1fa0ae96d145fe6fca9b7add18",
                                      FILES / "scripts" / "validate_structure.py"),
    SK: ("73d9f856cdbffacb2d21f6bc80d5ce4b6bffba1befc6b6fd3bf84de5e0c333fc",
         FILES / "skills" / "design-governance-practice" / "SKILL.md"),
}
NEW_FILES = {"scripts/build_core.py": FILES / "scripts" / "build_core.py"}
MANIFEST_ADD = ["scripts/build_core.py"]

DIAG_Q = (
    "La seconde boucle n’est pas obligatoirement une suite de petits polish. Après observation, choisissez la suite qui correspond au diagnostic :\n\n"
    "| Diagnostic | Suite appropriée |\n|---|---|\n")
DIAG_ROWS = (
    "| Défaut local et direction intacte | Corriger l’artefact puis réobserver. |\n"
    "| Défaut de craft ou de résolution | Résoudre la relation, la matière, le contenu, la typographie, l’action ou les états concernés. |\n"
    "| Direction faible, interchangeable ou contradictoire | Rouvrir la direction, reformuler ou requalifier la cible avant de continuer le polish. |\n"
    "| Risque ou périmètre changé | Reclassifier avec `DIRECTION/START`. |\n"
    "| Preuve insuffisante | Déclarer la limite et produire la prochaine preuve proportionnée. |\n"
    "| Décision suffisamment établie | Décider et persister la trace ; ne pas prolonger le polish sans changement attendu. |\n")
QUESTIONS = (
    "1. si la direction est visible dans l’artefact réel ;\n"
    "2. quel détail ou quelle relation porte la spécificité ;\n"
    "3. quel est le défaut dominant ;\n"
    "4. ce qui a réellement changé ;\n"
    "5. si la correction a affaibli l’usage, l’accessibilité, la robustesse ou la direction ;\n"
    "6. si la direction doit être corrigée, rouverte ou maintenue.\n")
VARIATION = (
    "Pour produire du beau varié sans produire du bruit, faire varier **un axe situé à la fois** : public, JTBD, promesse, geste, structure, densité, matière ou ton. "
    "Pour chaque alternative, préciser dans la trace existante :\n\n"
    "- la décision qu’elle peut changer ;\n"
    "- le public, le contexte, le risque ou le JTBD qui la justifie ;\n"
    "- le niveau de matérialisation nécessaire ;\n"
    "- la comparaison ou la preuve prévue ;\n"
    "- la condition de retrait.\n")

PASS1 = [
    # ---------- DIRECTION/DAILY devient DIRECTION/CHARGE (liste canonique unique) ----------
    ("R4-C01", "CHARGE : titre", D, "## DIRECTION/DAILY — charger proportionnellement", "## DIRECTION/CHARGE — classer, puis charger"),
    ("R4-C02", "CHARGE : règle", D,
     "> **Règle de vitesse.** Ouvre `START`, classe le mode, puis ouvre seulement le module susceptible de changer la prochaine décision. Ne lis jamais les cinq documents par réflexe.",
     "> **Règle de vitesse.** Ouvre `START` (en `LITE`, l’arbre `DIRECTION/START/TREE` suffit), classe le mode, charge la ligne de ce mode, puis ajoute seulement le module susceptible de changer la prochaine décision."),
    ("R4-C03", "CHARGE : statut", D,
     "`DAILY` est une vue de chargement, non une seconde source de vérité sur les modes, les verdicts ou les conditions de sortie.",
     "`CHARGE` est la seule liste de chargement du corpus : la skill en porte une copie générée, les façades y renvoient. Les modes restent définis par `START` ; les verdicts et les sorties, par `ACTION`."),
    ("R4-C04", "CHARGE : en-tête", D,
     "| Mode | Démarrage minimal | Ajouter seulement si cela change la décision |",
     "| Mode | Charger d’abord | Ajouter seulement si cela change la décision |"),
    ("R4-C05", "CHARGE : LITE (Gate A et B, réserve 8)", D,
     "| **LITE** | `ACTION/RUN-LITE`. Sans risque critique touché",
     "| **LITE** | `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. Sans risque critique touché"),
    ("R4-C06", "CHARGE : ITER (Gate A et B, réserve 8)", D,
     "| **ITER** | Mémoire locale + `ACTION/RUN-ITER`. Sans risque critique touché",
     "| **ITER** | Mémoire locale (direction existante), `ACTION/RUN-ITER`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. Sans risque critique touché"),
    ("R4-C07", "CHARGE : STANDARD", D,
     "| **STANDARD** | `ACTION/RUN-STANDARD`. |",
     "| **STANDARD** | `ACTION/RUN-STANDARD` ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte. |"),
    ("R4-C08", "CHARGE : DIRECTION", D,
     "| **DIRECTION** | `DIRECTION/VISUAL_TARGET` + `ACTION/RUN-DIRECTION`. | `DIRECTION/DIRECTION-ATELIER` si",
     "| **DIRECTION** | `DIRECTION/CREATIVE-BOOT`, `DIRECTION/EXTERNAL-START` si le brief est vague, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, "
     "`ACTION/FIRST-RENDER`, `ACTION/RUN-DIRECTION`, puis `ACTION/GATE-A`, `ACTION/GATE-B` et `ACTION/GATE-C` applicables. | "
     "`DIRECTION/DOUBLE-LOOP`, `ACTION/ROUTING` ou `SAVOIR/CRAFT/CFT-00` si la décision l’exige (la boucle d’édition et les gestes sont dans le noyau) ; "
     "`DIRECTION/DIRECTION-ATELIER` si"),
    ("R4-C09", "CHARGE : SYSTÈME", D,
     "| **SYSTÈME** | `ACTION/RUN-SYSTEM`. | `SAVOIR/SYSTEM` ; `BIBLIOTHEQUE/COMPONENTS` si la bibliothèque change réellement. |",
     "| **SYSTÈME** | `ACTION/RUN-SYSTEM` ; `BIBLIOTHEQUE/COMPONENTS` si un composant change. | `SAVOIR/SYSTEM` ; `CHANGELOG` si une règle partagée change. |"),
    ("R4-C10", "CHARGE : clôture et lectures humaines", D,
     "La clôture minimale de chaque mode est `ACTION/CLOSE-PACKAGE`. `DAILY` reste une vue de chargement : démarrage et ajouts.",
     "La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`. Pour l’agent, les blocs « noyau » compilés dans la skill tiennent lieu de lecture de fabrication ; "
     "README, QUICKSTART, READING_MAP et ORCHESTRATION_MAP sont des lectures d’orientation pour les humains."),
    ("R4-C11", "renvoi DAILY → CHARGE", D,
     "les autres façades (`DAILY`, `FAST-PATH`, `EXTERNAL-START`)", "les autres vues (`CHARGE`, `FAST-PATH`, `EXTERNAL-START`)"),
    ("R4-C12", "renvoi DAILY → CHARGE", D,
     "| Choisir rapidement une route | `DIRECTION/DAILY` ou `DIRECTION/FAST-PATH` |", "| Choisir rapidement une route | `DIRECTION/CHARGE` ou `DIRECTION/FAST-PATH` |"),
    ("R4-C13", "renvoi DAILY → CHARGE", D,
     "`DAILY`, `FAST-PATH`, `EXTERNAL-START`, la section 0", "`CHARGE`, `FAST-PATH`, `EXTERNAL-START`, la section 0"),
    ("R4-C14", "renvoi DAILY → CHARGE", D,
     "`DIRECTION/DAILY` est une vue dérivée de chargement minimal ;", "`DIRECTION/CHARGE` est la liste de chargement par mode ;"),
    # ---------- Boucle d'édition : diagnostic et six questions déplacés de QUICKSTART vers DIRECTION/DOUBLE-LOOP ----------
    ("R4-L01", "DOUBLE-LOOP reçoit la boucle d'édition", D,
     "Une nouvelle rationale, une variante décorative ou une reformulation de la trace ne constitue pas une correction.\n\n### Signaux de réouverture",
     "Une nouvelle rationale, une variante décorative ou une reformulation de la trace ne constitue pas une correction.\n\n"
     "### Boucle d’édition — du diagnostic au geste\n\n"
     "<!-- noyau:début BOUCLE-DIAGNOSTIC -->\n"
     "La seconde boucle n’est pas une suite de petits polish. Après observation, choisis la suite qui correspond au diagnostic :\n\n"
     "| Diagnostic | Suite appropriée |\n|---|---|\n" + DIAG_ROWS +
     "<!-- noyau:fin BOUCLE-DIAGNOSTIC -->\n\n"
     "<!-- noyau:début BOUCLE-QUESTIONS -->\n"
     "Pour une décision créative, note brièvement :\n\n" + QUESTIONS +
     "<!-- noyau:fin BOUCLE-QUESTIONS -->\n\n"
     "### Signaux de réouverture"),
    ("R4-Q01", "QUICKSTART §3 : renvoi au diagnostic", Q,
     DIAG_Q + DIAG_ROWS,
     "Après observation, choisissez la suite selon la table de diagnostic de `DIRECTION/DOUBLE-LOOP` (boucle d’édition).\n"),
    ("R4-Q02", "QUICKSTART §10 : renvoi aux six questions", Q,
     "Pour une décision créative, notez brièvement :\n\n" + QUESTIONS,
     "Pour une décision créative, appliquez les six questions de revue de `DIRECTION/DOUBLE-LOOP` (boucle d’édition).\n"),
    # ---------- Façades : la liste de chargement renvoie à DIRECTION/CHARGE ----------
    ("R4-Q03", "QUICKSTART §5 : renvoi à CHARGE", Q,
     "| Mode | Charger d’abord | Ajouter uniquement si cela change la décision |\n|---|---|---|\n"
     "| `LITE` | `DIRECTION/START`, `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. | `SAVOIR`, `BIBLIOTHEQUE` ou une ancre si le jugement ou la structure changent réellement. |\n"
     "| `ITER` | `DIRECTION/START`, `ACTION/RUN-ITER`, direction existante, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. | `SAVOIR` pour l’intégrité, `DIRECTION/VISUAL_TARGET` ou la couche système si la direction ou la portée changent. |\n"
     "| `STANDARD` | `DIRECTION/START`, `ACTION/RUN-STANDARD`, `BIBLIOTHEQUE/SELECT` si la structure est ouverte. | `SAVOIR`, atelier ou `CFT-00` si le craft ou la qualité perceptuelle deviennent la décision. |\n"
     "| `DIRECTION` | `DIRECTION/START`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `DIRECTION/DOUBLE-LOOP`, `ACTION/RUN-DIRECTION`, `SAVOIR/CRAFT/CFT-00` et les gates applicables. | Atlas, profil, référence ou atelier si cette source peut modifier la direction. |\n"
     "| `SYSTÈME` | `DIRECTION/START`, `ACTION/RUN-SYSTEM`, `BIBLIOTHEQUE/COMPONENTS` si un composant change. | `SAVOIR` pour le jugement du système, l’atelier ou `CHANGELOG` si l’expression ou la règle partagée est en jeu. |\n",
     "La liste de chargement par mode est unique : `DIRECTION/CHARGE`. La skill en porte une copie générée.\n"),
    ("R4-Q04", "QUICKSTART §1 : renvoi à CHARGE", Q,
     "| `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `DIRECTION/DOUBLE-LOOP`, `SAVOIR/CRAFT/CFT-00`, `ACTION/RUN-DIRECTION`. |",
     "| `DIRECTION/CHARGE` (mode `DIRECTION`). |"),
    ("R4-Q05", "QUICKSTART §4 : renvoi à CHARGE", Q,
     "| Situation | Mode probable | Première lecture |\n|---|---|---|\n"
     "| Correction locale, contraste, contenu, bug ou petit ajustement | `LITE` ou `ITER` | `DIRECTION/START`, puis `ACTION/RUN-LITE` ou `ACTION/RUN-ITER`. |\n"
     "| Nouvelle page ou nouveau flow sans identité autonome ; craft exigeant : Gate C ciblé, pas un critère de mode | `STANDARD` | `DIRECTION/START`, `ACTION/RUN-STANDARD`, puis `BIBLIOTHEQUE/SELECT` si la structure est ouverte. |\n"
     "| Brief flou ou risque impossible à classer | Clarification ou `EXTERNAL-START` avant le mode | `DIRECTION/START`, puis conservation de l’incertitude et reclassification. |\n"
     "| Identité, premier contact ou direction visuelle autonome | `DIRECTION` | `DIRECTION/START`, `DIRECTION/VISUAL_TARGET`, `SAVOIR/CRAFT/CFT-00`, puis `ACTION/RUN-DIRECTION`. |\n"
     "| Token, composant, pattern, convention ou format partagé | `SYSTÈME` | `DIRECTION/START`, `ACTION/RUN-SYSTEM`, `BIBLIOTHEQUE/COMPONENTS` et `CHANGELOG` si nécessaire. |\n",
     "| Situation | Mode probable |\n|---|---|\n"
     "| Correction locale, contraste, contenu, bug ou petit ajustement | `LITE` ou `ITER` |\n"
     "| Nouvelle page ou nouveau flow sans identité autonome ; craft exigeant : Gate C ciblé, pas un critère de mode | `STANDARD` |\n"
     "| Brief flou ou risque impossible à classer | Clarification ou `EXTERNAL-START` avant le mode |\n"
     "| Identité, premier contact ou direction visuelle autonome | `DIRECTION` |\n"
     "| Token, composant, pattern, convention ou format partagé | `SYSTÈME` |\n\n"
     "Première lecture de chaque mode : `DIRECTION/CHARGE`.\n"),
    ("R4-Q06", "QUICKSTART §8 : sortie visible par renvoi", Q,
     "restitue par défaut la réponse visible (voir `ACTION/HANDOFF`) :\n\n```text\nMODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER\n```\n",
     "restitue par défaut la réponse visible en langage produit : ce qui a été fait, pourquoi, ce qui manque pour la vraie version, la suite (voir `ACTION/HANDOFF`).\n"),
    ("R4-M01", "READING_MAP : renvoi à CHARGE", RM,
     "| Direction identitaire | `DIRECTION/START` → `DIRECTION/VISUAL_TARGET` → `DIRECTION/FIRST-OBJECT` → `ACTION/RUN-DIRECTION` (dès qu’il y a un build) |",
     "| Direction identitaire | `DIRECTION/START` → `DIRECTION/CHARGE` (mode `DIRECTION`) |"),
    ("R4-O01", "ORCHESTRATION_MAP : renvoi à CHARGE", OM,
     "| **Direction forte et spécifique** | `DIRECTION/START` + `ACTION/RUN-DIRECTION` + `DIRECTION/VISUAL_TARGET` + `DIRECTION/FIRST-OBJECT` |",
     "| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) |"),
    ("R4-O02", "ORCHESTRATION_MAP : variation créative déplacée vers SAVOIR/CRAFT/CFT-02", OM,
     VARIATION, "Pour produire du beau varié sans bruit : `SAVOIR/CRAFT/CFT-02` (un axe situé à la fois).\n"),
    ("R4-S01", "SAVOIR/CFT-02 reçoit la variation créative", S,
     "> **Alternative située :** position différente parce qu’elle répond à une contrainte, un public, un JTBD ou une opportunité distincte.\n",
     "> **Alternative située :** position différente parce qu’elle répond à une contrainte, un public, un JTBD ou une opportunité distincte.\n\n"
     "<!-- noyau:début BOUCLE-AXE -->\n" + VARIATION + "<!-- noyau:fin BOUCLE-AXE -->\n"),
    # ---------- Sortie visible en langage produit (décision 4) ----------
    ("R4-H01", "ACTION/HANDOFF : réponse visible en langage produit", A,
     "2. **Réponse visible**, pour un humain, par défaut :\n\n```text\nMODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER\n```\n\n"
     "`CHANGE` vaut la conséquence décisionnelle d’`ACTION/STATUS` : décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`. "
     "La réponse visible ne remplace jamais le handoff d’un run persistant.",
     "2. **Réponse visible**, pour un humain, par défaut :\n\n"
     "<!-- noyau:début SORTIE -->\n"
     "<!-- concept:SOR-01 -->\n"
     "La personne reçoit une réponse en langage produit, sans le jargon interne du système, en quatre rubriques :\n\n"
     "```text\n"
     "Ce que j’ai fait : la proposition et ses choix principaux, en une ou deux phrases.\n"
     "Pourquoi : la thèse et ce que le rendu permet de décider.\n"
     "Ce qui manque pour la vraie version : contenus, assets, droits, tests ou capacités, avec le plafond atteint.\n"
     "La suite : une ou deux actions proposées, et ce qu’il faut de la personne pour les engager.\n"
     "```\n\n"
     "L’agent active le système en silence : la personne donne l’objectif, le périmètre et l’autonomie ; l’agent choisit le mode, charge les sources et tient la trace. "
     "Le mode, la conséquence décisionnelle d’`ACTION/STATUS` (décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`), la preuve et l’owner "
     "restent dans la trace et sont exposés sur demande (« pourquoi ? », « qu’as-tu vérifié ? »). La réponse visible ne remplace jamais le handoff d’un run persistant.\n"
     "<!-- noyau:fin SORTIE -->"),
    # ---------- Outils du package ----------
    ("R4-RR", "read_route retire aussi les balises du noyau", "scripts/read_route.py",
     "CONCEPT_MARKER = re.compile(r\"^\\s*<!-- concept:[A-Z0-9\\-]+ -->\\s*$\")",
     "CONCEPT_MARKER = re.compile(r\"^\\s*<!-- (?:concept:[A-Z0-9\\-]+|noyau:(?:début|fin) [A-Z0-9\\-]+) -->\\s*$\")"),
    ("R4-VA1", "validate_all compile build_core", "scripts/validate_all.py",
     "\"scripts/read_route.py\", \"scripts/validate_structure.py\"])",
     "\"scripts/read_route.py\", \"scripts/validate_structure.py\", \"scripts/build_core.py\"])"),
    ("R4-B1", "build : copie GitHub", "scripts/build_distributions.sh",
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/github/scripts/validate_structure.py\"\n",
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/github/scripts/validate_structure.py\"\n"
     "cp -a \"$ROOT/scripts/build_core.py\" \"$STAGE/github/scripts/build_core.py\"\n"),
    ("R4-B2", "build : copie Local", "scripts/build_distributions.sh",
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/local/scripts/validate_structure.py\"\n",
     "cp -a \"$ROOT/scripts/validate_structure.py\" \"$STAGE/local/scripts/validate_structure.py\"\n"
     "cp -a \"$ROOT/scripts/build_core.py\" \"$STAGE/local/scripts/build_core.py\"\n"),
    # ---------- Rectifications déclarées de conditions de façade (même propriété, nouveau lieu) ----------
    ("R4-F01", "LCF-01 : RUN-DIRECTION en première lecture, via DIRECTION/CHARGE", V,
     "         bool(rm33) and \"ACTION/RUN-DIRECTION\" in rm33[1] and \"ACTION/RUN-DIRECTION\" not in rm33[2]),",
     "         bool(rm33) and \"`DIRECTION/CHARGE`\" in rm33[1] and bool(charge_row(t, \"DIRECTION\"))\n"
     "         and \"ACTION/RUN-DIRECTION\" in charge_row(t, \"DIRECTION\")[1] and \"ACTION/RUN-DIRECTION\" not in charge_row(t, \"DIRECTION\")[2]),"),
    ("R4-F07", "LCF-07 : ordre cible → premier objet, dans DIRECTION/CHARGE", V,
     "    rows = [row(t[\"RM\"], \"Direction identitaire\"), row(t[\"OM\"], \"Direction forte et spécifique\"), row(t[\"SK\"], \"`DIRECTION`\")]\n"
     "    return (before(chain, \"`VISUAL_TARGET`\", \"`FIRST-OBJECT`\") and before(prio, \"DIRECTION —\", \"FIRST-OBJECT —\")\n"
     "            and all(r and before(\" \".join(r), \"VISUAL_TARGET\", \"FIRST-OBJECT\") for r in rows))",
     "    pointers = [row(t[\"RM\"], \"Direction identitaire\"), row(t[\"OM\"], \"Direction forte et spécifique\")]\n"
     "    rows = [charge_row(t, \"DIRECTION\")]\n"
     "    return (before(chain, \"`VISUAL_TARGET`\", \"`FIRST-OBJECT`\") and before(prio, \"DIRECTION —\", \"FIRST-OBJECT —\")\n"
     "            and all(r and before(\" \".join(r), \"VISUAL_TARGET\", \"FIRST-OBJECT\") for r in rows)\n"
     "            and all(p and \"`DIRECTION/CHARGE`\" in \" \".join(p) for p in pointers))"),
    ("R4-F25", "LCF-25 : Gate B en LITE et ITER, dans DIRECTION/CHARGE", V,
     "        sk, ac = row(t[\"SK\"], f\"`{mode}`\"), row(carte, f\"`{mode}`\")",
     "        sk, ac = charge_row(t, mode), row(carte, f\"`{mode}`\")"),
    ("R4-F39", "LCF-39 : QUICKSTART §5 renvoie à DIRECTION/CHARGE (Gates A et B)", V,
     "    sec = t[\"Q\"][t[\"Q\"].find(\"## 5. Charger\"):t[\"Q\"].find(\"## 6.\")]\n"
     "    return all((r := row(sec, f\"`{m}`\")) and \"ACTION/GATE-B\" in r[1] for m in (\"LITE\", \"ITER\"))",
     "    sec = t[\"Q\"][t[\"Q\"].find(\"## 5. Charger\"):t[\"Q\"].find(\"## 6.\")]\n"
     "    return (\"`DIRECTION/CHARGE`\" in sec and not row(sec, \"`LITE`\")\n"
     "            and all((r := charge_row(t, m)) and \"ACTION/GATE-A\" in r[1] and \"ACTION/GATE-B\" in r[1] for m in (\"LITE\", \"ITER\")))"),
    ("R4-F47", "LCF-47 : objet de preuve codé dans le noyau compilé", V,
     "    return \"de préférence **codé**\" in fo and \"de préférence codé\" in t[\"SK\"]",
     "    return \"de préférence **codé**\" in fo and bool(re.search(r\"de préférence (\\*\\*)?codé\", t[\"SK\"]))"),
    ("R4-FC1", "LCF-C1 : copies du handoff fidèles là où elles existent", V,
     "         and all(token in HANDOFF_TOKENS.findall(after(t[\"SK\"], \"## Carte de lecture et sortie\", 2500)) for token in canon)),",
     "         and (not after(t[\"SK\"], \"## Carte de lecture et sortie\", 10)\n"
     "              or all(token in HANDOFF_TOKENS.findall(after(t[\"SK\"], \"## Carte de lecture et sortie\", 2500)) for token in canon))),"),
    ("R4-FC2", "LCF-C2 : réponse visible en langage produit, définie par ACTION/HANDOFF", V,
     "         all(VISIBLE in text for text in (after(t[\"A\"], \"### ACTION/HANDOFF\", 3000), t[\"Q\"], t[\"SK\"]))),",
     "         all(r in after(t[\"A\"], \"### ACTION/HANDOFF\", 4000) for r in VISIBLE_RUBRIQUES)\n"
     "         and \"réponse visible en langage produit\" in t[\"Q\"] and \"`ACTION/HANDOFF`\" in t[\"Q\"]\n"
     "         and all(r in t[\"SK\"] for r in VISIBLE_RUBRIQUES) and VISIBLE not in t[\"Q\"] + t[\"SK\"]),"),
    ("R4-FH", "aide : ligne de mode de DIRECTION/CHARGE et rubriques de la réponse visible", V,
     "def row(text: str, key: str, col: int = 0) -> list[str] | None:",
     "VISIBLE_RUBRIQUES = (\"Ce que j’ai fait :\", \"Pourquoi :\", \"Ce qui manque pour la vraie version :\", \"La suite :\")\n\n\n"
     "def charge_row(t: dict[str, str], mode: str) -> list[str] | None:\n"
     "    sec = t[\"D\"][t[\"D\"].find(\"## DIRECTION/CHARGE\"):]\n"
     "    sec = sec[:sec.find(\"\\n## \", 5)]\n"
     "    return row(sec, f\"**{mode}**\")\n\n\n"
     "def row(text: str, key: str, col: int = 0) -> list[str] | None:"),
    # ---------- Exemple de fabrication ----------
    ("R4-E01", "exemples : fabrication depuis un brief flou", EX,
     "## DIRECTION — première scène identitaire",
     "## DIRECTION — fabrication depuis un brief flou\n\n"
     "**Demande :** « Il me faut un site pour ma boulangerie. » Rien d’autre.\n\n"
     "**Prise de brief, en un seul échange :** l’agent demande les contenus réels (produits, prix, horaires, adresse), le logo ou les couleurs s’ils existent, "
     "et deux ou trois photos du comptoir ; la destination est une vraie mise en ligne. Faute de réponse, il construit avec des hypothèses nommées.\n\n"
     "```text\n"
     "THÈSE: le pain du jour se choisit d’un coup d’œil, avant d’entrer\n"
     "OBJET DE PREUVE: la vitrine du jour, composant codé (produit, prix, heure de sortie du four)\n"
     "MODAL: photo pleine largeur, titre centré, trois cartes « nos valeurs »\n"
     "PARTI: s’écarter pour la première scène, où la vitrine du jour remplace la photo ; garder la navigation attendue\n"
     "FABRICATION: typographie et couleur au plafond (polices libres, palette tirée des photos) ; photos du client moyennes, un seul traitement cohérent ; aucune illustration dessinée\n"
     "DÉFAUT DOMINANT: après capture, les prix se lisent mal sur mobile ; taille et contraste corrigés, seconde capture comparée\n"
     "```\n\n"
     "**Réponse visible :** « J’ai construit une page d’accueil organisée autour de la vitrine du jour. Pourquoi : on choisit son pain avant d’entrer, "
     "la page le permet en un coup d’œil. Ce qui manque pour la vraie version : vos prix, vos horaires et une photo du comptoir en lumière du jour ; "
     "les produits affichés sont des exemples marqués comme tels. La suite : envoyez ces éléments, je les intègre et je vérifie le mobile. »\n\n"
     "## DIRECTION — première scène identitaire"),
    # ---------- CHANGELOG ----------
    ("R4-CH1", "CHANGELOG « Non publié »", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Noyau de fabrication (refonte, R4).** Les gestes de fabrication (structure, composition, moyens et vérité, boucle d’édition) sont balisés dans leurs "
     "sources et compilés dans la skill par `scripts/build_core.py` ; la vue de chargement quotidienne devient `DIRECTION/CHARGE`, seule liste de chargement (Gates A et B en "
     "`LITE` et `ITER`) ; la réponse visible passe en langage produit (`ACTION/HANDOFF`) ; la table de diagnostic et les six questions de revue passent de "
     "QUICKSTART à `DIRECTION/DOUBLE-LOOP`, la variation « un axe à la fois » d’ORCHESTRATION_MAP à `SAVOIR/CRAFT/CFT-02`.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

# Passe 2 : blocs du noyau balisés sur le texte obtenu. (identifiant, fichier, début de la première ligne, début d'une ligne du dernier paquet)
WRAPS = [
    ("ROLE", D, "Tu es un·e directeur·rice artistique", "Tu vises l’excellence appropriée"),
    ("POSTURE", D, "**Première idée.**", None),
    ("CHARGE-REGLE", D, "> **Règle de vitesse.** Ouvre `START`", None),
    ("CHARGE-TABLE", D, "| Mode | Charger d’abord | Ajouter seulement si cela change la décision |", None),
    ("CHARGE-FIN", D, "La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`.", None),
    ("BRIEF", D, "**Prise de brief.**", None),
    ("PREMIER-OBJET", D, "Lorsque `RUN-PRIORITY`, `VISUAL_TARGET` ou `DIRECTION-ATELIER` peuvent modifier la première scène", None),
    ("STRUCT-OU", B, "> L’interface ne commence ni", None),
    ("STRUCT-EXPRESSION", B, "Une structure ne choisit pas seule le goût", None),
    ("STRUCT-TENSION", B, "Lorsqu’une décision structurelle ou créative est ouverte, déclare", "ACTION: centrale ↔ contextuelle"),
    ("STRUCT-SIGNAUX", B, "Les compositions suivantes sont des signaux", "Un signal de convergence déclenche"),
    ("COMP-GRAMMAIRE", S, "Lorsque la décision visuelle est ouverte, construis dans cet ordre", "Une proposition est forte lorsque"),
    ("COMP-SINGULARITE", S, "Le test de singularité demande", None),
    ("COMP-FORME", S, "> **Forme située = tâche", "Le phénomène ou la métaphore est facultatif"),
    ("COMP-CONTROLES", S, "Les contrôles principaux sont", None),
    ("COMP-VOCABULAIRE", S, "| Terme | Question | Diff possible |", None),
    ("COMP-CONVERGENCE", S, "**Question de convergence.**", None),
    ("COMP-VAGUES", S, "<!-- concept:ANT-01 -->", None),
    ("MOY-PLAFOND", D, "<!-- concept:HON-03 -->", None),
    ("MOY-CARTE", S, "<!-- concept:MOY-01 -->", None),
    ("MOY-ASSETS", S, "**Traitement des assets moyens.**", None),
    ("MOY-CALIBRATION", S, "Cherche des calibrations", None),
    ("VER-FAUX-ASSET", S, "<!-- concept:HON-02 -->", None),
    ("VER-SCENE", D, "<!-- concept:HON-01 -->", None),
    ("VER-AUDIENCE", D, "**Audience.**", None),
    ("BOUCLE", D, "La boucle commune est", None),
    ("BOUCLE-ATELIER", A, "Après la première capture, effectuer une lecture légère", "Conserver et comparer la capture suivante"),
    ("BOUCLE-REVUE", S, "[MÉTHODE] Pour une décision où la qualité visuelle est dominante", None),
    ("BOUCLE-REPASSE", S, "Une repasse complète est attendue", None),
]


def wrap_entry(text: str, bid: str, rel: str, start: str, last: str | None):
    lines = text.split("\n")
    s_idx = [i for i, l in enumerate(lines) if l.startswith(start)]
    if len(s_idx) != 1:
        return None, f"{bid} : début trouvé {len(s_idx)} fois dans {rel}"
    i = s_idx[0]
    j = i
    if last:
        cand = [k for k in range(i, len(lines)) if lines[k].startswith(last)]
        if not cand:
            return None, f"{bid} : fin introuvable dans {rel}"
        j = cand[0]
    while j + 1 < len(lines) and lines[j + 1].strip():
        j += 1
    old = "\n".join(lines[i:j + 1])
    if text.count(old) != 1:
        return None, f"{bid} : bloc non unique dans {rel}"
    new = f"<!-- noyau:début {bid} -->\n{old}\n<!-- noyau:fin {bid} -->"
    return (f"R4-W-{bid}", f"balisage noyau {bid}", rel, old, new), None


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def manifest(root: Path) -> None:
    p = root / "scripts" / "package_manifest.json"
    m = json.loads(p.read_text(encoding="utf-8"))
    for key in ("github", "local"):
        for item in MANIFEST_ADD:
            if item not in m[key]:
                m[key].insert(m[key].index("scripts/validate_structure.py") + 1, item)
    p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def apply_all(root: Path, dry: bool = False) -> list[str]:
    problems = apply(root, PASS1, dry=True)
    for rel, (old_sha, _src) in FILE_REPLACE.items():
        if sha(root / rel) != old_sha:
            problems.append(f"{rel} : empreinte inattendue")
    for rel in NEW_FILES:
        if (root / rel).exists():
            problems.append(f"fichier déjà présent : {rel}")
    if problems:
        return problems
    if dry:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            return apply_all(copy, dry=False)
    apply(root, PASS1)
    wraps, errs = [], []
    texts = {}
    for bid, rel, start, last in WRAPS:
        if rel not in texts:
            texts[rel] = (root / rel).read_text(encoding="utf-8")
        entry, err = wrap_entry(texts[rel], bid, rel, start, last)
        if err:
            errs.append(err)
        else:
            wraps.append(entry)
            texts[rel] = texts[rel].replace(entry[3], entry[4])
    if errs:
        return errs
    problems = apply(root, wraps)
    if problems:
        return problems
    for rel, (_old, src) in FILE_REPLACE.items():
        shutil.copy2(src, root / rel)
    for rel, src in NEW_FILES.items():
        shutil.copy2(src, root / rel)
    manifest(root)
    out = subprocess.run([sys.executable, "-B", str(root / "scripts" / "build_core.py")], capture_output=True, text=True, cwd=root)
    if out.returncode != 0:
        return [f"build_core : {out.stdout}{out.stderr}"]
    return []


# Mutations : chaque garde du lot doit rougir (motif attendu dans la sortie de validate_structure).
def mutate(copy: Path, rel: str, old: str, new: str) -> bool:
    p = copy / rel
    t = p.read_text(encoding="utf-8")
    if t.count(old) < 1:
        return False
    p.write_text(t.replace(old, new, 1), encoding="utf-8")
    return True


MUTATIONS = [
    ("skill retouchée à la main", SK, "### 5. Composition", "### 5. Composition retouchée", "la skill diffère de sa compilation"),
    ("bloc du noyau modifié sans recompiler", S, "Le test de singularité demande", "Le test de singularité, désormais, demande", "la skill diffère de sa compilation"),
    ("balise de fin supprimée", S, "<!-- noyau:fin COMP-CONTROLES -->\n", "", "ouvert dans"),
    ("bloc du noyau dans une façade", Q, "## 12. Sources propriétaires", "<!-- noyau:début X-1 -->\nx\n<!-- noyau:fin X-1 -->\n\n## 12. Sources propriétaires", "hors source normative"),
    ("table de chargement recopiée", Q, "## 6. Produire une qualité positive",
     "| Mode | Charger d’abord | Ajouter |\n|---|---|---|\n| `LITE` | `ACTION/RUN-LITE` | — |\n\n## 6. Produire une qualité positive", "table de chargement hors DIRECTION/CHARGE"),
    ("façade qui redéfinit la liste", RM, "| Direction identitaire | `DIRECTION/START` → `DIRECTION/CHARGE` (mode `DIRECTION`) |",
     "| Direction identitaire | `DIRECTION/START` → `DIRECTION/VISUAL_TARGET` |", "redéfinit la liste"),
    ("ligne DIRECTION sans FIRST-RENDER", D, "`ACTION/FIRST-RENDER`, `ACTION/RUN-DIRECTION`, puis", "`ACTION/RUN-DIRECTION`, puis", "doit charger RUN-DIRECTION et FIRST-RENDER"),
    ("ancien format de réponse visible", Q, "## 12. Sources propriétaires", "```text\nMODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER\n```\n\n## 12. Sources propriétaires", "vocabulaire retiré"),
    ("sortie sans concept", A, "<!-- concept:SOR-01 -->\n", "", "SOR-01 absent"),
    ("clôture non renvoyée", D, "La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`.", "La clôture de chaque mode est propre au mode.", "[CHG-01]"),
    ("reclassification sans ITER", D, "puis reclassifie vers `ITER`, `STANDARD`", "puis reclassifie vers `STANDARD`", "[CHG-02]"),
    ("COMPONENTS sans condition", D, "`BIBLIOTHEQUE/COMPONENTS` si un composant change. |", "`BIBLIOTHEQUE/COMPONENTS`. |", "[CHG-03]"),
    ("ITER sans Gate B", D, "`ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. Sans", "`ACTION/GATE-A` applicable. Sans", "[CHG-04]"),
]


# Rectifications de conditions de façade : chaque LCF rectifiée rougit sous une mutation de sa propriété.
LCF_MUTATIONS = [
    ("LCF-01", D, "`ACTION/FIRST-RENDER`, `ACTION/RUN-DIRECTION`, puis", "`ACTION/FIRST-RENDER`, puis"),
    ("LCF-07", D, "`DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `ACTION/FIRST-RENDER`",
     "`DIRECTION/FIRST-OBJECT`, `DIRECTION/VISUAL_TARGET`, `ACTION/FIRST-RENDER`"),
    ("LCF-25", D, "`ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. Sans", "`ACTION/GATE-A` applicable. Sans"),
    ("LCF-39", Q, "La liste de chargement par mode est unique : `DIRECTION/CHARGE`.", "La liste de chargement par mode est unique."),
    ("LCF-47", D, "de préférence **codé**", "de préférence **dessiné**"),
    ("LCF-C1", SK, "## Références conditionnelles", "## Carte de lecture et sortie\n\nMODE — DECISION\n\n## Références conditionnelles"),
    ("LCF-C2", Q, "## 12. Sources propriétaires", "MODE — DECISION — CHANGE — PROOF — LIMIT — NEXT-ACTION — OWNER\n\n## 12. Sources propriétaires"),
]


def mutations(root: Path) -> int:
    bad = 0
    for name, rel, old, new, motif in MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            ok = mutate(copy, rel, old, new)
            out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_structure.py")],
                                 capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and motif in (out.stdout + out.stderr)
            print(f"mutation « {name} » : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    for lcf, rel, old, new in LCF_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "pkg"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
            ok = mutate(copy, rel, old, new)
            out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_reading_map.py")],
                                 capture_output=True, text=True, cwd=copy)
            red = ok and out.returncode != 0 and f"{lcf} :" in (out.stdout + out.stderr)
            print(f"rectification {lcf} sous mutation : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    if "--mutations" in sys.argv:
        return 1 if mutations(root) else 0
    problems = apply_all(root, dry="--verifier" in sys.argv)
    for pr in problems:
        print(pr)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PASS1)} entrées, {len(WRAPS)} blocs balisés, "
              f"{len(FILE_REPLACE)} fichiers remplacés, {len(NEW_FILES)} créé, manifeste, noyau compilé")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
