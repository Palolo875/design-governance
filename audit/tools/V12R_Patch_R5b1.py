#!/usr/bin/env python3
"""V1.2 refonte — PATCH-DECISION R5b-1 : trace à deux niveaux, checkpoint, contenu absent, test de trame.

Décisions de l'owner (27-09-2026, `V12R_06_R5b1_TRACE_CHECKPOINT.md` §1) :
  - décision 5 (a)  : la première proposition vaut checkpoint, sauf action irréversible ou coûteuse (D-09) ;
  - décision 11 (a) : trace légère par défaut, complète si le run est persistant, partagé ou audité (D-23) ;
  - D-20            : destination réelle sans contenu → contenu d'exemple marqué, pas d'emplacements vides ;
  - D-22            : test de trame dans le noyau, sans rendu supplémentaire.
Méthode M1 à M4 (`V12R_00`, `V12R_02`) : chaque correction entre avec sa garde (validate_structure.py, version R5b-1).
Usage :
  python3 V12R_Patch_R5b1.py <racine>                 # applique, puis recompile le noyau (scripts/build_core.py)
  python3 V12R_Patch_R5b1.py <racine> --verifier      # dit, sans écrire, si chaque ancien texte est présent une fois
  python3 V12R_Patch_R5b1.py <racine> --mutations     # sur une racine patchée : chaque garde rougit sous sa mutation
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from V12_Patch_ABD import apply  # noqa: E402

D, A, S = "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md"
B, C = "V1/official/BIBLIOTHEQUE.md", "V1/official/CHANGELOG.md"

FILES = HERE / "V12R_Patch_R5b1_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("e1bef382f52c2aa9d9fef303340c6660e50bc87edab0a9e44ebe5163cb4f761d", FILES / "validate_structure.py"),
    "scripts/build_core.py": ("d81696d28a6f83904a8797f272e2c24b62834e7c89e9c6242bffc6c1fa9d2b67", FILES / "build_core.py"),
}

TRACE = """<!-- noyau:fin SORTIE -->

3. **Niveau de trace**, choisi par l’agent :

<!-- noyau:début TRACE -->
<!-- concept:TRA-01 -->
**Trace légère par défaut.** Hors run persistant, partagé ou audité, la trace tient en six lignes au plus : mode ; thèse (promesse → objet de preuve → geste) ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant ; prochaine preuve. Les planchers s’appliquent pendant la fabrication (vérité, `ACTION/GATE-A`, boucle d’édition) ; seule leur écriture s’allège. Le run livre une **proposition** `EXPLORATORY` : ni verdict, ni acceptation, ni clôture, ni `RUN_CARD`. **Trace complète** (handoff, `ACTION/RUN_CARD`, `ACTION/CLOSE-PACKAGE`, gates écrits, `B1b` dans son scope) si le run est persistant, partagé, audité, ou si une acceptation ou une clôture est demandée.
<!-- noyau:fin TRACE -->

**Formes.**"""

CHECKPOINT = """<!-- noyau:début CHECKPOINT -->
<!-- concept:CHK-01 -->
**La première proposition vaut checkpoint.** Construis la première scène, puis présente-la avec sa thèse, l’alternative écartée et ce qu’il faut décider ; la personne valide, réoriente ou arrête. Jusque-là, la proposition reste `EXPLORATORY`. Un checkpoint avant le build n’est requis que si la personne l’a demandé ou si le build engage une action irréversible ou coûteuse (publier, envoyer, payer, consommer des crédits, écraser un existant, engager l’owner). Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build.
<!-- noyau:fin CHECKPOINT -->

Si un checkpoint préalable est requis et que l’autorisation manque, n’engage pas le build"""

CONTENU = """<!-- noyau:fin BRIEF -->

<!-- noyau:début CONTENU -->
<!-- concept:CNT-01 -->
**Destination réelle sans contenu.** Si la surface sert un vrai commerce, service ou personne mais que ses contenus manquent (nom, offre, prix, horaires, photos, adresse), remplis-la d’un contenu plausible **marqué comme exemple** plutôt que d’emplacements vides : elle doit se lire comme une page, pas comme un gabarit. Le marquage est discret dans l’interface (« exemple », « à confirmer ») et explicite dans la réponse, qui liste ce qu’il faut fournir. Le marquage de vérité s’applique sans exception.
<!-- noyau:fin CONTENU -->"""

TRAME = """<!-- concept:TRM-01 -->
**Test de trame.** Chaque brief a aussi sa trame modale : l’ordre de sections que n’importe quelle IA produirait pour lui (pour un SaaS : promesse, logos, trois bénéfices, tarifs, FAQ). Avant de fixer la structure, écris-la en une ligne, puis romps-la ou garde-la en le justifiant par ce que la personne doit voir, comprendre ou faire d’abord. Rompre, c’est changer l’ordre, le foyer ou l’objet qui organise la page ; renommer ou restyler les sections ne suffit pas.

Un signal de convergence déclenche une reformulation"""

PATCH = [
    # ---------- Décision 11 : trace à deux niveaux (D-23) ----------
    ("R5b-T1", "trace légère, lieu propriétaire (ACTION/HANDOFF)", A,
     "<!-- noyau:fin SORTIE -->\n\n**Formes.**", TRACE),
    ("R5b-T2", "chargement DIRECTION : Gate B en trace complète", D,
     "`ACTION/RUN-DIRECTION`, puis `ACTION/GATE-A`, `ACTION/GATE-B` et `ACTION/GATE-C` applicables. |",
     "`ACTION/RUN-DIRECTION`, puis `ACTION/GATE-A` et `ACTION/GATE-C` applicables ; en trace complète (`ACTION/HANDOFF`), "
     "`ACTION/GATE-B`, `ACTION/RUN_CARD` et `ACTION/CLOSE-PACKAGE`. |"),
    ("R5b-T3", "clôture par mode : trace complète", D,
     "La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`.",
     "La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`, en trace complète ; en trace légère, le run s’arrête à la proposition (`ACTION/HANDOFF`)."),
    ("R5b-T4", "carte de lecture d'ACTION alignée sur CHARGE", A,
     "| `DIRECTION` | `ACTION/RUN-DIRECTION`, `ACTION/PIPELINE-DIRECTION`, `ACTION/VISUAL_PROOF`, `ACTION/GATE-A`, `ACTION/GATE-B`, `ACTION/GATE-C` |",
     "| `DIRECTION` | `ACTION/RUN-DIRECTION`, `ACTION/PIPELINE-DIRECTION`, `ACTION/VISUAL_PROOF`, `ACTION/GATE-A`, `ACTION/GATE-C` ; "
     "`ACTION/GATE-B` en trace complète (`ACTION/HANDOFF`) |"),
    ("R5b-T5", "RUN-DIRECTION : sortie en trace légère", A,
     "**Sortie.** Paquet `DIRECTION` d’`ACTION/CLOSE-PACKAGE`. Pour chaque ancrage",
     "**Sortie.** Paquet `DIRECTION` d’`ACTION/CLOSE-PACKAGE`. En trace légère (`ACTION/HANDOFF`), la réponse visible et la trace légère "
     "en tiennent lieu. Pour chaque ancrage"),
    ("R5b-T6", "RUN-DIRECTION : clôture en trace complète", A,
     "**Clôture.** Passer à `DECIDED`, puis `CLOSED` uniquement si la direction est tenue",
     "**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` uniquement si la direction est tenue"),
    ("R5b-T7", "CLOSE-PACKAGE : paquet de la trace complète", A,
     "Enregistre ensuite le paquet minimal correspondant dans la ligne de run, la `RUN_CARD`, le ticket ou le manifeste.",
     "Enregistre ensuite le paquet minimal correspondant dans la ligne de run, la `RUN_CARD`, le ticket ou le manifeste. "
     "Ce paquet est celui de la trace complète ; en trace légère (`ACTION/HANDOFF`), le run livre une proposition sans paquet de clôture."),
    # ---------- Décision 5 : la première proposition vaut checkpoint (D-09) ----------
    ("R5b-K1", "checkpoint, lieu propriétaire (ACTION/PIPELINE-DIRECTION, étape 7)", A,
     "En session interactive, demande une validation avant le build lorsque le périmètre n’est pas couvert par une autonomie explicite. "
     "L’autonomie doit nommer le périmètre `DIRECTION` couvert. Une nouvelle marque, un nouveau public, une nouvelle surface identitaire "
     "autonome ou une nouvelle hypothèse déclenche un nouveau checkpoint, sauf instruction explicite couvrant ce périmètre.\n\n"
     "Si l’autorisation manque, c’est-à-dire si le checkpoint n’est pas couvert par une autonomie explicite, n’engage pas le build",
     CHECKPOINT),
    ("R5b-K2", "checkpoint : renvoi depuis DIRECTION", D,
     "En session interactive, un checkpoint humain intervient avant le build lorsque le périmètre n’a pas été couvert par une autonomie "
     "explicite. Le checkpoint présente la position retenue, l’alternative considérée, la raison du choix et la preuve attendue. "
     "Si le regard requis",
     "Le checkpoint suit `ACTION/PIPELINE-DIRECTION` : la première proposition en tient lieu, sauf action irréversible ou coûteuse ; "
     "elle présente la position retenue, l’alternative considérée, la raison du choix et la preuve attendue. Si le regard requis"),
    ("R5b-K3", "checkpoint : renvoi depuis SAVOIR", S,
     "Une nouvelle marque, un nouveau public, une nouvelle surface identitaire ou une nouvelle hypothèse déclenche un checkpoint de "
     "cadrage dans le run, sauf instruction explicite couvrant ce périmètre ; elle ne remplace ni les droits, ni l’owner final, "
     "ni une escalade requise.",
     "Elle ne remplace ni les droits, ni l’owner final, ni une escalade requise ; le checkpoint suit `ACTION/PIPELINE-DIRECTION` "
     "(la première proposition en tient lieu, sauf action irréversible ou coûteuse)."),
    # ---------- D-20 : destination réelle sans contenu ----------
    ("R5b-C1", "contenu d'exemple marqué (DIRECTION, après la prise de brief)", D,
     "<!-- noyau:fin BRIEF -->", CONTENU),
    # ---------- D-22 : test de trame ----------
    ("R5b-M1", "test de trame (BIBLIOTHEQUE, signaux de convergence)", B,
     "Un signal de convergence déclenche une reformulation", TRAME),
    # ---------- Historique ----------
    ("R5b-H1", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Trace et checkpoint (refonte, R5b-1).** Trace légère par défaut, complète si le run est persistant, partagé, audité ou si une "
     "acceptation est demandée (`ACTION/HANDOFF`) ; Gate B, `RUN_CARD` et paquet de clôture chargés en trace complète ; la première "
     "proposition vaut checkpoint, sauf action irréversible ou coûteuse ; destination réelle sans contenu : exemple marqué plutôt "
     "qu’emplacements vides ; test de trame dans les signaux de convergence. Schéma `RUN_CARD` inchangé.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]

# Mutations : l'inverse d'une entrée doit faire rougir la garde qui la protège (motif attendu dans la sortie).
MUTATION_OF = {
    "R5b-T1": "TRA-01 absent",
    "R5b-T2": "[CHG-08]",
    "R5b-K1": "CHK-01 absent",
    "R5b-K2": "vocabulaire retiré",
    "R5b-K3": "vocabulaire retiré",
    "R5b-C1": "CNT-01 absent",
    "R5b-M1": "TRM-01 absent",
}

# Mutations supplémentaires (texte libre) : une réintroduction de l'ancienne règle doit rougir.
EXTRA_MUTATIONS = [
    ("checkpoint avant build réintroduit", "V1/official/QUICKSTART.md", "\n## ",
     "\nLe checkpoint a lieu avant le build dans toute session interactive.\n\n## ", "résumé infidèle (checkpoint)"),
    ("copie manuelle du noyau", "skills/design-governance-practice/SKILL.md", "**Trace légère par défaut.**",
     "**Trace légère.**", "[NOY-02]"),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build_core(root: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(root / "scripts" / "build_core.py")], capture_output=True, text=True, cwd=root)
    return out.returncode, out.stdout + out.stderr


def apply_all(root: Path, dry: bool = False) -> list[str]:
    problems = apply(root, PATCH, dry=True)
    for rel, (old_sha, _src) in FILE_REPLACE.items():
        if sha(root / rel) != old_sha:
            problems.append(f"{rel} : empreinte inattendue (version R4 requise)")
    if problems or dry:
        return problems
    apply(root, PATCH)
    for rel, (_old, src) in FILE_REPLACE.items():
        shutil.copy2(src, root / rel)
    code, out = build_core(root)
    return [] if code == 0 else [f"build_core : {out.strip()}"]


def structure(copy: Path) -> tuple[int, str]:
    out = subprocess.run([sys.executable, "-B", str(copy / "scripts" / "validate_structure.py")],
                         capture_output=True, text=True, cwd=copy)
    return out.returncode, out.stdout + out.stderr


def fresh(root: Path, tmp: str) -> Path:
    copy = Path(tmp) / "pkg"
    shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".build", "dist", "*.zip", "__pycache__"))
    return copy


def mutations(root: Path) -> int:
    bad = 0
    for pid, motif in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            copy = fresh(root, tmp)
            problems = apply(copy, [e for e in PATCH if e[0] == pid], reverse=True)
            if not problems and pid in ("R5b-T1", "R5b-K1", "R5b-C1"):
                build_core(copy)  # la source mutée est recompilée : seule la garde de concept doit rougir
            code, out = structure(copy)
            red = code != 0 and motif in out and not problems
            print(f"inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'} (motif « {motif} »){' ; ' + '; '.join(problems) if problems else ''}")
            bad += 0 if red else 1
    for name, rel, old, new, motif in EXTRA_MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = fresh(root, tmp)
            p = copy / rel
            t = p.read_text(encoding="utf-8")
            ok = old in t
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            code, out = structure(copy)
            red = ok and code != 0 and motif in out
            print(f"mutation {name} : {'ROUGE' if red else 'NON ROUGE'}{'' if ok else ' ; ancre introuvable'}")
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
        print(f"{'vérifié' if '--verifier' in sys.argv else 'appliqué'} : {len(PATCH)} entrées, {len(FILE_REPLACE)} fichier(s) remplacé(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
