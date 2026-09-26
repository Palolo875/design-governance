#!/usr/bin/env python3
"""DG-AUDIT-001 — R.01 — PATCH-DECISION du retour : textes cibles exacts, sous forme exécutable.

Artefact d'audit HORS package. Chaque entrée remplace UNE occurrence exacte (sinon arrêt, rien n'est écrit).
Usage :
  python3 DG_AUDIT_001_Patch_R01.py <racine>            # applique le patch (sur B04 en R.02 ; jamais sur B01, B02, B03)
  python3 DG_AUDIT_001_Patch_R01.py <racine> --verifier # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 DG_AUDIT_001_Patch_R01.py <racine> --inverse ID  # remet l'ancien texte d'une entrée (mutation des gardes)

Le patch ne touche ni la version, ni le CHANGELOG V1.1.1, ni les notes de version : ils sont écrits en R.02.
"""
from __future__ import annotations

import sys
from pathlib import Path

A = "V1/official/ACTION.md"
D = "V1/official/DIRECTION.md"
G = "V1/official/GLOSSAIRE.md"
Q = "V1/official/QUICKSTART.md"
S = "V1/official/SAVOIR.md"
C = "V1/official/CHANGELOG.md"
N = "RELEASE_NOTES.md"
SK = "skills/design-governance-practice/SKILL.md"
EX = "skills/design-governance-practice/references/examples.md"
MP = "skills/design-governance-practice/references/machine_projection.md"
RM = "scripts/validate_reading_map.py"

DC = "conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`)"

# (ID, point, fichier, ancien texte exact, nouveau texte)
PATCH: list[tuple[str, str, str, str, str]] = [
    # ---------- RET-1 : triade d'ACTION/STATUS (R-01) ----------
    ("P-01", "RET-1", A,
     "| `DECISION-CHANGE` | Décision effectivement changée, confirmée ou abandonnée ; `N/A-JUSTIFIED` si aucune conséquence n’est obtenue ou attendue. |",
     "| `DECISION-CHANGE` | Décision effectivement changée, confirmée ou abandonnée ; sinon la triade d’`ACTION/STATUS` : `N/A-JUSTIFIED` si aucune conséquence n’était applicable (avec la raison), `NOT-OBSERVED` si une conséquence attendue n’a pas été observée (interdit `ACCEPTED`). |"),
    ("P-02", "RET-1", G,
     "Si aucune conséquence n’est obtenue ou attendue, la trace peut utiliser `N/A-JUSTIFIED` lorsque cela est justifié. |",
     "Sinon, la triade d’`ACTION/STATUS` s’applique : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, avec la raison ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. |"),
    ("P-03", "RET-1", A,
     "`CHANGE` vaut `DECISION-CHANGE` ou `N/A-JUSTIFIED`.",
     "`CHANGE` vaut la conséquence décisionnelle d’`ACTION/STATUS` : décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`."),
    # ---------- RET-2 : portée de B1b (R-02), extension du texte ----------
    ("P-04", "RET-2", A,
     "`B1b` est **requis par module** sur une surface `DIRECTION` lorsque le risque V/craft est dominant dans la ligne de run ou lorsque le verdict V repose sur une intention, une composition, une matière ou un traitement qui n’a pas encore été confronté à une variante. Le déclencheur porte sur le risque et la décision déclarés ; il ne dépend pas de l’affirmation qu’une comparaison « ne changerait rien ».",
     "`B1b` est **requis par module** sur toute surface `DIRECTION` qui accepte (`ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`) avec l’axe V en `PASS` ou `PASS-WITH-RESERVATION` : un V positif n’y est pas accordé sans une décision principale confrontée à une variante, ou sans l’un des deux motifs `N/A-JUSTIFIED` admis ci-dessous. Avant la clôture, il est déclenché dès que le risque V/craft est dominant dans la ligne de run ou que le verdict V visé repose sur une intention, une composition, une matière ou un traitement qui n’a pas encore été confronté à une variante. Le déclencheur porte sur le risque, la décision et le verdict déclarés ; il ne dépend pas de l’affirmation qu’une comparaison « ne changerait rien »."),
    ("P-05", "RET-2", D,
     "Une surface `DIRECTION` dont le risque V/craft est dominant ou dont le verdict V dépend d’une intention encore non confrontée doit suivre `ACTION/GATE-B — B1b` avant clôture.",
     "Une surface `DIRECTION` qui accepte avec V en `PASS` ou `PASS-WITH-RESERVATION`, dont le risque V/craft est dominant ou dont le verdict V dépend d’une intention encore non confrontée doit suivre `ACTION/GATE-B — B1b` avant clôture."),
    # ---------- RET-3 : Creative Boot sans quota dans les façades (R-03) ----------
    ("P-06", "RET-3", Q,
     "promesse, objet de preuve, geste, deux anti-directions concrètes, une tension et une signature structurelles, jusqu’à trois cibles créatives",
     "promesse, objet de preuve, geste, anti-directions concrètes, tension et signature structurelles (nombre d’axes : `BIBLIOTHEQUE/TENSION`), jusqu’à trois cibles créatives"),
    ("P-07", "RET-3", SK,
     "promesse, objet de preuve, geste, deux anti-directions concrètes, une tension et une signature structurelles, jusqu’à trois cibles créatives",
     "promesse, objet de preuve, geste, anti-directions concrètes, tension et signature structurelles (nombre d’axes : `BIBLIOTHEQUE/TENSION`), jusqu’à trois cibles créatives"),
    # ---------- RET-4 : chargement de Gate B en LITE et ITER (R-07) ----------
    ("P-08", "RET-4", SK,
     "| `LITE` | `DIRECTION/START/TREE`, `ACTION/RUN-LITE` et `ACTION/FAST-PATH`. | Atlas, atelier, `VISUAL_TARGET`, gates B/C et routes structurelles de `BIBLIOTHEQUE`. |",
     "| `LITE` | `DIRECTION/START/TREE`, `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant. | Atlas, atelier, `VISUAL_TARGET`, Gate C et routes structurelles de `BIBLIOTHEQUE`. |"),
    ("P-09", "RET-4", SK,
     "| `ITER` | `DIRECTION/START` et `ACTION/RUN-ITER`. | Atlas, atelier, `VISUAL_TARGET` et gates B/C, sauf si la direction, le système ou le risque change. |",
     "| `ITER` | `DIRECTION/START`, `ACTION/RUN-ITER`, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. | Atlas, atelier et `VISUAL_TARGET`, sauf si la direction, le système ou le risque change ; Gate C seulement si le craft change. |"),
    ("P-10", "RET-4", A,
     "| `ITER` | `ACTION/RUN-ITER` ; non-régression pertinente |",
     "| `ITER` | `ACTION/RUN-ITER` ; non-régression pertinente ; `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché ; `ACTION/GATE-C` seulement si le craft change |"),
    # ---------- RET-5 : machine_projection conforme au schéma (R-10) ----------
    ("P-11", "RET-5", MP,
     "Utiliser `PASS`, `PASS-WITH-RESERVATION`, `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` pour les axes, les contrôles ou les limites selon leur sens propre ; ils ne deviennent pas des verdicts globaux.",
     "Les axes (`closure.axes`) prennent uniquement `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `NOT-VERIFIED` ou `N/A-JUSTIFIED` ; `NOT-OBSERVED` qualifie une conséquence décisionnelle (`decision_change.outcome`), jamais un axe. Aucune de ces valeurs ne devient un verdict global."),
    ("P-12", "RET-5", MP,
     "`profile_decision` peut transporter la décision, les dials, la contre-indication et la preuve de son effet ; s’il est présent, ses quatre champs sont obligatoires.",
     "`profile_decision` peut transporter la phase, la décision, les dials, la contre-indication et la preuve de son effet ; s’il est présent, ses cinq champs sont obligatoires (`phase`, `decision`, `dials`, `counterindication`, `evidence`)."),
    # ---------- RET-6 : phrase « façades alignées » bornée ----------
    ("P-13", "RET-6", C,
     "- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill alignés sur leurs propriétaires ; efficacité déclarée `NOT-VERIFIED` partout.",
     "- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill corrigés sur les écarts relevés ; la cohérence opposable se limite à la liste close des conditions de façade (`validate_reading_map.py`) : une divergence hors de cette liste n’est pas détectée. Efficacité déclarée `NOT-VERIFIED` partout."),
    ("P-14", "RET-6", N,
     "- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill alignés sur leurs propriétaires ; efficacité déclarée `NOT-VERIFIED` partout.",
     "- **Façades.** QUICKSTART, README des deux distributions, glossaire, cartes et skill corrigés sur les écarts relevés ; la cohérence opposable se limite à la liste close des conditions de façade (`validate_reading_map.py`) : une divergence hors de cette liste n’est pas détectée. Efficacité déclarée `NOT-VERIFIED` partout."),
    # ---------- §6 retenus : R-08 (table de correspondance) ----------
    ("P-15", "R-08", A,
     "| VISUAL_TARGET : thèse, anti-direction, premier objet, périmètre, contrainte | avant build | `direction.thesis`, `.anti_direction`, `.first_object`, `.scope`, `.constraint` | — |",
     "| VISUAL_TARGET : thèse, anti-direction | avant build | `direction.thesis`, `.anti_direction` | — |\n"
     "| Direction qualifiée : premier objet (`DIRECTION/FIRST-OBJECT`), contrainte (`DIRECTION/VISUAL_TARGET`, « Qualifier la direction ») ; périmètre (`SCOPE`) | avant build | `direction.first_object`, `.constraint`, `.scope` | — |"),
    ("P-16", "R-08", A,
     "| VISUAL_TARGET : conséquence observable, silhouette, relations de plans, opération dominante, typographie, résolution initiale |",
     "| VISUAL_TARGET : conséquence observable, silhouette, relations de plans, opération visuelle dominante, typographie, résolution initiale |"),
    # ---------- §6 retenus : R-12 (droits inconnus) ----------
    ("P-17", "R-12", A,
     "Un droit inconnu ou non autorisé déclenche `RETURNED`, `ESCALATED` ou le statut prévu par le contexte avant diffusion.",
     "Un droit inconnu (`rights_status` : `unknown`) interdit `ACCEPTED` ; `ACCEPTED-WITH-RESERVATION` reste possible avec une réserve structurée dont le scope couvre les droits et dont la condition de sortie est leur clearance, et la diffusion attend cette clearance. Un droit non autorisé déclenche `RETURNED`, `ESCALATED` ou le statut prévu par le contexte avant diffusion. La machine contrôle seulement l’exclusion d’`ACCEPTED` ; la réserve sur les droits reste à la trace."),
    # ---------- §6 retenus : R-13 (ressource technique, une seule liste) ----------
    ("P-18", "R-13", S,
     "Toute ressource de stack indique : stack, version, date de vérification, owner, fallback, limites, claims applicables et capacité résolue.",
     "Toute ressource de stack indique les sept champs d’`ACTION/POLICIES` (inspection et ressources techniques) et, lorsqu’elle soutient un claim, les claims applicables (`SAVOIR/TOOLS`)."),
    # ---------- §6 retenus : R-14 (sortie définie une seule fois) + RET-1 dans les paquets ----------
    ("P-19", "R-14", A,
     "**Sortie.** Artefact touché, V/U/A/T concernés, diff, verdict, réserve ou prochaine action. Ajoute `DECISION-CHANGE` si une décision a effectivement changé ; sinon justifie `N/A-JUSTIFIED` lorsque cela est pertinent.",
     "**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`."),
    ("P-20", "R-14", A,
     "**Sortie.** Direction toujours retrouvable, diff observable, preuve du risque touché, V/U/A/T mis à jour, verdict, risque restant et `DECISION-CHANGE` ou `N/A-JUSTIFIED`.",
     "**Sortie.** Paquet `ITER` d’`ACTION/CLOSE-PACKAGE`."),
    ("P-21", "R-14", A,
     "**Sortie.** Rendu ou artefact, hiérarchie, typographie, états, V/U/A/T, verdict, risque restant, prochaine action et `DECISION-CHANGE` ou `N/A-JUSTIFIED`.",
     "**Sortie.** Paquet `STANDARD` d’`ACTION/CLOSE-PACKAGE`."),
    ("P-22", "R-14", A,
     "**Sortie.** Direction écrite, ancre/spec, capture, trace locale des assets pertinents, écarts, gates A/B/C, V/U/A/T, statut de direction, verdict global, owner, risque restant, prochaine preuve et `DECISION-CHANGE` ou `N/A-JUSTIFIED`. Pour chaque ancrage",
     "**Sortie.** Paquet `DIRECTION` d’`ACTION/CLOSE-PACKAGE`. Pour chaque ancrage"),
    ("P-23", "R-14", A,
     "**Sortie.** Décision de système, plan de migration, preuve de non-régression, réserves, verdict et entrée CHANGELOG. Dans une `RUN_CARD` acceptée",
     "**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`. Dans une `RUN_CARD` acceptée"),
    ("P-24", "R-14", A,
     "| **LITE** | Artefact touché, risque, V/U/A/T touchés, verdict, réserve ou prochaine action, et `DECISION-CHANGE`/`N/A-JUSTIFIED`. |",
     f"| **LITE** | Artefact touché, diff, risque, V/U/A/T touchés, verdict, réserve ou prochaine action, et {DC}. |"),
    ("P-25", "R-14", A,
     "| **ITER** | Direction rappelée, diff, non-régression, verdict touché, risque restant, prochaine action et décision. |",
     f"| **ITER** | Direction rappelée et retrouvable, diff observable, non-régression, preuve du risque touché, V/U/A/T mis à jour, verdict, risque restant, prochaine action et {DC}. |"),
    ("P-26", "R-14", A,
     "| **STANDARD** | Artefact, hiérarchie, typographie, états pertinents, V/U/A/T, verdict, risque restant et prochaine action. |",
     f"| **STANDARD** | Rendu ou artefact, hiérarchie, typographie, états pertinents, V/U/A/T, verdict, risque restant, prochaine action et {DC}. |"),
    ("P-27", "R-14", A,
     "| **DIRECTION** | Artefact, direction, ancre/spec, capture, écarts, revue créative, creative close, gates A/B/C, V/U/A/T, statut de direction, verdict et prochaine preuve. |",
     f"| **DIRECTION** | Artefact, direction écrite, ancre/spec, capture, trace locale des assets pertinents, écarts, revue créative, creative close, gates A/B/C, V/U/A/T, statut de direction, verdict global, owner, risque restant, prochaine preuve et {DC}. |"),
    ("P-28", "R-14", A,
     "| **SYSTÈME** | Décision, impact, consumers, owner, migration/rollback, non-régression, verdict et entrée CHANGELOG. |",
     "| **SYSTÈME** | Décision de système, impact, consumers, owner, migration/rollback, non-régression, réserves, verdict et entrée CHANGELOG. |"),
    # ---------- §6 retenus : légende (F-DIR-005) ----------
    ("P-29", "Légende", D,
     "Légende commune à DIRECTION et SAVOIR : les tags `[RECOMMANDÉ]` et `[À ADAPTER]` sont employés dans SAVOIR.",
     "Légende commune à DIRECTION et SAVOIR pour les seuls tags partagés : `[REQUIS PAR LE MODULE]`, `[À ADAPTER]` et `[VEILLE]`, au même sens. SAVOIR tient sa propre table (« Niveaux d’autorité ») pour ses autres tags ; `[RECOMMANDÉ]` n’y est pas employé."),
    # ---------- §6 retenus : GLOSSAIRE × B1 ----------
    ("P-30", "GLOSSAIRE×B1", G,
     "il porte une réserve complète (owner, portée, impact, prochaine preuve, date de revue, condition de sortie) sur un risque secondaire. Un risque critique non vérifié n’est pas éligible. » |",
     "il porte une réserve complète (owner, portée, impact, prochaine preuve, date de revue, condition de sortie). Une protection critique restée `NOT-VERIFIED` exclut `ACCEPTED`, pas la réserve ; une protection en échec (`FAIL`) exclut tout verdict accepté. » |"),
    # ---------- §6 retenus : QUICKSTART §6, colonne « Retour si… » (D1 T-6) ----------
    ("P-31", "QS§6", Q,
     "| Dimension | Ce que le premier rendu doit rendre visible |\n|---|---|\n"
     "| Présence | Une position perceptible plutôt qu’un assemblage de composants neutres. |\n"
     "| Foyer | Masse, rythme, hiérarchie et point d’entrée discernables. |\n"
     "| Signature | Un détail ou une relation non interchangeable, avec une raison située. |\n"
     "| Intégration | Une scène, un geste ou une relation qui rend la promesse tangible dès l’entrée ; la direction appartient à ce produit, ce public et ce contenu ; aucun effet, asset ou composant n’existe sans conséquence identifiable. |\n"
     "| Résolution | Typographie, matière, action, responsive et états critiques assez construits pour révéler les défauts réels ; contenu suffisamment crédible pour juger la composition. |\n"
     "| Désirabilité située | L’attrait vient d’une relation au produit, au contexte et au public, pas d’un adjectif. |\n"
     "| Vérité de scène | Texte, données, états et libellés crédibles ; tout exemple non observé est marqué comme illustratif. |\n"
     "| Résilience visible | La direction tient dans les transformations pertinentes pour le risque : mobile, contenu long, état critique ou fallback. |",
     "| Dimension | Ce que le premier rendu doit rendre visible | Retour si… |\n|---|---|---|\n"
     "| Présence | Une position perceptible plutôt qu’un assemblage de composants neutres. | La proposition est plate, interchangeable ou sans foyer. |\n"
     "| Foyer | Masse, rythme, hiérarchie et point d’entrée discernables. | Le texte, l’asset, le CTA et la preuve se concurrencent. |\n"
     "| Signature | Un détail ou une relation non interchangeable, avec une raison située. | Le produit pourrait être remplacé sans modifier la scène. |\n"
     "| Intégration | Une scène, un geste ou une relation qui rend la promesse tangible dès l’entrée ; la direction appartient à ce produit, ce public et ce contenu ; aucun effet, asset ou composant n’existe sans conséquence identifiable. | L’élément est décoratif, mal cadré, hors récit ou simplement disponible. |\n"
     "| Résolution | Typographie, matière, action, responsive et états critiques assez construits pour révéler les défauts réels ; contenu suffisamment crédible pour juger la composition. | Le rendu reporte la décision à une future passe de polish. |\n"
     "| Désirabilité située | L’attrait vient d’une relation au produit, au contexte et au public, pas d’un adjectif. | « Premium », « moderne » ou « beau » remplace une décision observable. |\n"
     "| Vérité de scène | Texte, données, états et libellés crédibles ; tout exemple non observé est marqué comme illustratif. | Une hypothèse ressemble à une preuve de résultat, de client ou de disponibilité. |\n"
     "| Résilience visible | La direction tient dans les transformations pertinentes pour le risque : mobile, contenu long, état critique ou fallback. | Un changement de contenu, viewport, asset ou état détruit le foyer ou la compréhension. |\n\n"
     "Un « Retour si… » observé renvoie à la décision responsable (`DIRECTION/FIRST-OBJECT`) ; il ne crée ni gate, ni verdict, ni quota."),
    # ---------- §6 retenus : imitation (C6) — les exemples renvoient à la sérialisation ----------
    ("P-32", "Imitation", EX,
     "Les champs affichés respectent les contrats d’ACTION ; un champ omis reste dû dans la `RUN_CARD`.",
     "Les champs affichés respectent les contrats d’ACTION ; un champ omis reste dû dans la `RUN_CARD`.\n>\n"
     "> **Trace, pas sérialisation.** Ces blocs sont des traces : leurs noms (`OBSERVED`, `AXES`, `RISK` en phrase…) ne sont pas des clés JSON. "
     "Pour produire une `RUN_CARD`, partir de `schemas/run_card.example.json`, suivre [machine_projection.md](machine_projection.md) "
     "et la table de correspondance d’`ACTION/RUN_CARD`, puis contrôler avec `scripts/validate_run_card.py`."),
]

# ---------- Liste close des conditions de façade : LCF-22 à LCF-35 (validate_reading_map.py) ----------
LCF_CODE = r'''
# ---------- R.01 (DG-AUDIT-001) : LCF-22 à LCF-35 ----------
SCHEMA = ROOT / "schemas" / "run_card.schema.json"
NUM_WORDS = {3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept"}
CHANGE_ENUM = re.compile(r"DECISION-CHANGE[^.\n]{0,120}N/A-JUSTIFIED|N/A-JUSTIFIED[^.\n]{0,120}DECISION-CHANGE")
BOOT_COUNT = re.compile(r"(?i)\b(une|deux|trois|\d+)\s+(anti-directions?|tensions?)\b")


def lcf_22(t: dict[str, str]) -> bool:
    lines = [l for k in ("A", "D", "G", "Q", "S", "SK", "EX", "MP") for l in t[k].splitlines()
             if not l.startswith("DECISION-CHANGE:") and (CHANGE_ENUM.search(l) or ("`CHANGE` vaut" in l and "N/A-JUSTIFIED" in l))]
    return bool(lines) and all("NOT-OBSERVED" in l for l in lines) and not any("obtenue ou attendue" in t[k] for k in ("A", "G"))


def lcf_23(t: dict[str, str]) -> bool:
    b1b = t["A"][t["A"].find("### B1b"):]
    scope = next((p for p in b1b.split("\n\n")[1:3] if "requis par module" in p), "")
    return all(k in scope for k in ("`DIRECTION`", "`ACCEPTED-WITH-RESERVATION`", "`PASS-WITH-RESERVATION`"))


def lcf_24(t: dict[str, str]) -> bool:
    boots = [[l for l in t[k].splitlines() if "Creative Boot" in l or "CREATIVE-BOOT" in l] for k in ("Q", "SK")]
    return all(boots) and not any(BOOT_COUNT.search(l) for group in boots for l in group)


def lcf_25(t: dict[str, str]) -> bool:
    carte = t["A"][t["A"].find("### Carte de lecture par mode"):t["A"].find("### ACTION/HANDOFF")]
    for mode in ("LITE", "ITER"):
        sk, ac = row(t["SK"], f"`{mode}`"), row(carte, f"`{mode}`")
        if not (sk and ac and len(sk) > 2 and "ACTION/GATE-B" in sk[1] and not re.search(r"(?i)gates? B", sk[2]) and "ACTION/GATE-B" in ac[1]):
            return False
    return True


def lcf_26(t: dict[str, str]) -> bool:
    try:
        props = json.loads(SCHEMA.read_text(encoding="utf-8"))["properties"]["run_card"]["properties"]
        axes = set(props["closure"]["properties"]["axes"]["properties"]["V"]["enum"])
        fields = props["profile_decision"]["required"]
    except (OSError, KeyError, ValueError):
        return False
    axis_line = next((l for l in t["MP"].splitlines() if "`closure.axes`" in l), "")
    listed = set(re.findall(r"`([A-Z/-]+)`", axis_line.split("`closure.axes`", 1)[-1].split(";")[0])) if axis_line else set()
    pd_line = next((l for l in t["MP"].splitlines() if "`profile_decision`" in l and "champs" in l), "")
    count = re.search(r"(\w+) champs sont obligatoires", pd_line)
    return (listed == axes and bool(count) and count.group(1) == NUM_WORDS.get(len(fields))
            and all(f"`{f}`" in pd_line for f in fields))


def lcf_27(t: dict[str, str]) -> bool:
    texts = [t[k] for k in ("C", "NOTES", "README") if t[k]]
    return all("alignés sur leurs propriétaires" not in x for x in texts) and "liste close des conditions de façade" in t["C"]


def lcf_28(t: dict[str, str]) -> bool:
    vt = t["D"][t["D"].find("## DIRECTION/VISUAL_TARGET"):t["D"].find("### Compilation de la première proposition")]
    fields = {plain(r[0]).lower() for r in rows_between(vt, "| Champ |", "\n\n")}
    claims = [c.strip().lower() for l in t["A"].splitlines() if l.startswith("| VISUAL_TARGET :")
              for c in re.split(r",| et ", cells(l)[0].split(":", 1)[1])]
    return bool(fields) and bool(claims) and all(c in fields for c in claims)


def lcf_29(t: dict[str, str]) -> bool:
    legend = t["D"][t["D"].find("### Légende"):]
    legend = legend[:legend.find("\n#", 5)]
    sentence = next((l for l in legend.splitlines() if "SAVOIR" in l and not l.startswith("|")), "")
    tags = re.findall(r"`(\[[^\]`]+\])`", sentence)
    return bool(tags) and all(tag[:-1] in t["S"] or f"`{tag}` n’y est pas employé" in sentence for tag in tags)


def retour_si(text: str, start: str) -> dict[str, str]:
    i = text.find(start)
    if i < 0:
        return {}
    seg = text[i:]
    j = seg.find("\n#", len(start))
    seg = seg[: j if j > 0 else len(seg)]
    header = next((cells(l) for l in seg.splitlines() if l.startswith("| Dimension")), [])
    k = next((n for n, c in enumerate(header) if c.startswith("Retour si")), None)
    if k is None:
        return {}
    return {plain(r[0]): plain(r[k]) for r in rows_between(seg, "| Dimension", "\n\n") if len(r) > k}


def lcf_30(t: dict[str, str]) -> bool:
    d = retour_si(t["D"], "### Contrat positif du premier objet")
    return bool(d) and retour_si(t["Q"], "## 6. Produire une qualité positive") == d


def lcf_31(t: dict[str, str]) -> bool:
    head = t["EX"][:t["EX"].find("\n## ")]
    return all(k in head for k in ("schemas/run_card.example.json", "machine_projection.md", "validate_run_card.py"))


def lcf_32(t: dict[str, str]) -> bool:
    l = next((x for x in t["A"].splitlines() if "Un droit inconnu" in x), "")
    return "interdit `ACCEPTED`" in l and "`ACCEPTED-WITH-RESERVATION`" in l and "avant diffusion" in l


def lcf_33(t: dict[str, str]) -> bool:
    sav = next((l for l in t["S"].splitlines() if l.startswith("Toute ressource de stack")), "")
    pol = t["A"][t["A"].find("Toute ressource technique maintenue indique"):].splitlines()[1:]
    items: list[str] = []
    for l in pol:
        if l.startswith("- "):
            items.append(l)
        elif items:
            break
    return (bool(sav) and "ACTION/POLICIES" in sav and "date de vérification" not in sav
            and len(items) == 7 and "sept champs" in t["A"])


def lcf_34(t: dict[str, str]) -> bool:
    outs = [l for l in t["A"].splitlines() if l.startswith("**Sortie.**")]
    return len(outs) == 5 and all(re.match(r"\*\*Sortie\.\*\* Paquet `[A-ZÈ]+` d’`ACTION/CLOSE-PACKAGE`\.", l) for l in outs)


def lcf_35(t: dict[str, str]) -> bool:
    closed = next((l for l in t["G"].splitlines() if l.startswith("| **CLOSED** |")), "")
    return bool(closed) and "n’est pas éligible" not in closed and "NOT-VERIFIED" in closed and "exclut `ACCEPTED`" in closed

'''

LCF_ROWS = '''        ("LCF-22", "ACTION (table RUN_CARD, réponse visible, paquets), GLOSSAIRE et façades : DECISION-CHANGE", "ACTION/STATUS (triade) ; RET-1", lcf_22(t)),
        ("LCF-23", "ACTION/GATE-B — B1b, portée", "validate_run_card (check_b1b) ; INV-B3-3 ; RET-2", lcf_23(t)),
        ("LCF-24", "QUICKSTART et skill, Creative Boot", "DIRECTION/CREATIVE-BOOT ; BIBLIOTHEQUE/TENSION ; RET-3", lcf_24(t)),
        ("LCF-25", "skill et carte d'ACTION, chargement LITE et ITER", "ACTION/PRECONDITION (Gate B du risque) ; RET-4", lcf_25(t)),
        ("LCF-26", "machine_projection : axes et profile_decision", "schemas/run_card.schema.json ; RET-5", lcf_26(t)),
        ("LCF-27", "CHANGELOG, RELEASE_NOTES, README : portée de la cohérence des façades", "liste close des conditions de façade ; RET-6", lcf_27(t)),
        ("LCF-28", "ACTION, table de correspondance RUN_CARD : lignes VISUAL_TARGET", "DIRECTION/VISUAL_TARGET (table canonique) ; R-08", lcf_28(t)),
        ("LCF-29", "DIRECTION, légende des tags", "SAVOIR (Niveaux d’autorité) ; F-DIR-005", lcf_29(t)),
        ("LCF-30", "QUICKSTART §6, colonne « Retour si… »", "DIRECTION/FIRST-OBJECT ; D1 T-6", lcf_30(t)),
        ("LCF-31", "exemples de la skill : renvoi à la sérialisation", "ACTION/RUN_CARD ; schemas/run_card.example.json ; C6", lcf_31(t)),
        ("LCF-32", "ACTION, droits inconnus", "validate_run_card (rights_status) ; INV-B2-10 ; R-12", lcf_32(t)),
        ("LCF-33", "SAVOIR, ressource de stack", "ACTION/POLICIES (sept champs) ; D3 T-6 ; R-13", lcf_33(t)),
        ("LCF-34", "ACTION, sorties des blocs RUN-*", "ACTION/CLOSE-PACKAGE ; C4 T-2 ; R-14", lcf_34(t)),
        ("LCF-35", "GLOSSAIRE, exemple CLOSED", "ACTION (protection critique) ; B1", lcf_35(t)),
'''

PATCH += [
    ("P-33", "LCF", RM, "import re\nimport sys\n", "import json\nimport re\nimport sys\n"),
    ("P-34", "LCF", RM,
     '        "SK": SKILL_DIR / "SKILL.md", "EX": SKILL_DIR / "references" / "examples.md",\n',
     '        "SK": SKILL_DIR / "SKILL.md", "EX": SKILL_DIR / "references" / "examples.md",\n'
     '        "MP": SKILL_DIR / "references" / "machine_projection.md",\n'),
    ("P-35", "LCF", RM, "\ndef check_facades(errors: list[str]) -> None:\n", LCF_CODE + "\ndef check_facades(errors: list[str]) -> None:\n"),
    ("P-36", "LCF", RM,
     '        ("LCF-21", "DIRECTION, README, RELEASE_NOTES, CHANGELOG", "CHANGELOG (efficacité NOT-VERIFIED)", lcf_21(t)),\n',
     '        ("LCF-21", "DIRECTION, README, RELEASE_NOTES, CHANGELOG", "CHANGELOG (efficacité NOT-VERIFIED)", lcf_21(t)),\n' + LCF_ROWS),
]

# Entrée de patch dont l'inverse sert de mutation pour chaque nouvelle condition (R harnais, mode mutations)
MUTATION_OF = {
    "LCF-22": "P-01", "LCF-23": "P-04", "LCF-24": "P-06", "LCF-25": "P-08", "LCF-26": "P-11", "LCF-27": "P-13",
    "LCF-28": "P-15", "LCF-29": "P-29", "LCF-30": "P-31", "LCF-31": "P-32", "LCF-32": "P-17", "LCF-33": "P-18",
    "LCF-34": "P-20", "LCF-35": "P-30",
}


def apply(root: Path, entries, reverse: bool = False, dry: bool = False) -> list[str]:
    texts: dict[str, str] = {}
    problems = []
    for pid, _point, rel, old, new in entries:
        a, b = (new, old) if reverse else (old, new)
        text = texts.get(rel)
        if text is None:
            p = root / rel
            if not p.is_file():
                if rel == N:  # RELEASE_NOTES n'existe pas dans l'export Local
                    continue
                problems.append(f"{pid} : fichier absent {rel}")
                continue
            text = p.read_text(encoding="utf-8")
        n = text.count(a)
        if n != 1:
            problems.append(f"{pid} : ancien texte trouvé {n} fois dans {rel}")
            continue
        texts[rel] = text.replace(a, b)
    if not problems and not dry:
        for rel, text in texts.items():
            (root / rel).write_text(text, encoding="utf-8")
    return problems


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1]).resolve()
    if "--inverse" in sys.argv:
        pid = sys.argv[sys.argv.index("--inverse") + 1]
        problems = apply(root, [e for e in PATCH if e[0] == pid], reverse=True)
    else:
        problems = apply(root, PATCH, dry="--verifier" in sys.argv)
    for p in problems:
        print("ÉCHEC", p)
    if not problems:
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH) if '--inverse' not in sys.argv else 1} entrée(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
