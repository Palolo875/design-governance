"""Maquette des restes R5 (diagnostic V12R_29) : textes appliqués sur une copie du package."""
import shutil
import sys
from pathlib import Path

SRC, M = Path(sys.argv[1]), Path(sys.argv[2])
if M.exists():
    shutil.rmtree(M)
shutil.copytree(SRC, M, ignore=shutil.ignore_patterns("dist", "*.zip", "__pycache__", ".build"))
D, A, S, B = (M / "V1/official" / n for n in ("DIRECTION.md", "ACTION.md", "SAVOIR.md", "BIBLIOTHEQUE.md"))

def sub(p, old, new):
    t = p.read_text(encoding="utf-8")
    assert t.count(old) == 1, (p.name, old[:60], t.count(old))
    p.write_text(t.replace(old, new), encoding="utf-8")

HANDOFF = ("`MODE`, `RISK`, `SCOPE`, `ARTIFACT`, `OBSERVATION/METHOD`, `PROOF/TRACE-LOCATOR`, `LIMIT/NOT-VERIFIED`, "
           "`DECISION-CHANGE`, `NEXT-ACTION`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`")
# A, B : copies du handoff → renvoi
sub(S, "Lorsque le run passe à ACTION, conserve au minimum " + HANDOFF + " dans la `RUN_CARD` ou la trace équivalente.",
    "Lorsque le run passe à ACTION, ces champs rejoignent le handoff canonique (`ACTION/HANDOFF`) ; en trace complète, ils vont "
    "dans la `RUN_CARD` ou la trace équivalente.")
sub(B, " Conservez aussi " + HANDOFF + ".", " Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`).")

# C, D : instrumentation et contrat de promotion hors du préambule (D-15)
t = B.read_text(encoding="utf-8")
a = t.index("### Charges de lecture à ne pas confondre")
b = t.index("### Contrat minimal par périmètre de contribution et statut de route")
c = t.index("<!-- noyau:début STRUCT-OU -->")
contrat = t[b:c].rstrip() + "\n\n"
t = (t[:a] + "En run local, le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` suffit, avec `N/A-JUSTIFIED` si aucune route ne change ; "
     "les exigences par périmètre de contribution (pilote, partagé, durable) et les statuts de cycle de vie relèvent de "
     "`BIBLIOTHEQUE/EVOLUTION`.\n\n" + t[c:])
evo = "## BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation\n\n"
i = t.index(evo) + len(evo)
j = t.index("\n\n", i) + 2
t = (t[:j] + "**Mesure de lecture.** Pour mesurer ce qu’un run instrumenté lit dans les routes structurelles, les catégories de "
     "`DIRECTION` (« Lecture instrumentée et règle de passage ») s’appliquent ; un run ordinaire ne les déclare pas.\n\n"
     + contrat + t[j:])
B.write_text(t, encoding="utf-8")
sub(D, "Déclare dans la trace la catégorie de lecture applicable ;",
    "Dans un run instrumenté ou audité, déclare dans la trace la catégorie de lecture applicable (en trace légère, cette "
    "déclaration n’est pas demandée) ;")

# F : PRINT_FIELD relié aux signaux de convergence (question de jugement)
sub(B, "| Grille répétitive sans différence de priorité | Quelle rupture doit changer la lecture, la comparaison ou l’action ? |",
    "| Grille répétitive sans différence de priorité | Quelle rupture doit changer la lecture, la comparaison ou l’action ? |\n"
    "| Grain, trame d’impression ou texture repris d’un brief à l’autre | Quelle matière la thèse de ce produit appelle-t-elle, et "
    "que perd la page si on la retire (`MODIFIER/PRINT_FIELD`, test de retrait) ? |")
sub(B, "**Test :** la matière soutient l’identité ou la preuve sans abaisser lisibilité, accessibilité ou robustesse.",
    "**Test :** la matière soutient l’identité ou la preuve sans abaisser lisibilité, accessibilité ou robustesse. Une matière "
    "reprise d’un brief à l’autre est un signal de convergence (`BIBLIOTHEQUE/SELECT`, signaux de convergence structurelle) : "
    "une question de jugement, jamais une interdiction.")

# G, H, I : alternative située — DIRECTION déclenche, SAVOIR donne les leviers, ACTION matérialise, trace et compare
sub(D, "En `DIRECTION`, considère une alternative située lorsque la décision est ouverte et qu’une position différente peut "
       "raisonnablement changer le choix. **Avant le build**, la trace nomme la position retenue, l’alternative considérée, la "
       "raison de son niveau de matérialisation et la preuve attendue. Matérialise-la seulement au niveau nécessaire pour comparer "
       "cette décision : phrase, schéma, cible ou rendu. Une alternative qui ne peut rien changer n’est pas produite ; sa "
       "non-production est justifiée.",
    "En `DIRECTION`, l’alternative située suit « Direction divergente » (déclenchement), `SAVOIR/CRAFT/CFT-02` (leviers) et "
    "`ACTION/PIPELINE-DIRECTION` (matérialisation, trace et comparaison) ; une alternative qui ne peut rien changer n’est pas "
    "produite, et sa non-production est justifiée.")
sub(D, "Avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative considérée, la "
       "raison de son niveau de matérialisation et la preuve attendue. La projection JSON ne porte pas ce paquet (voir "
       "`ACTION/RUN_CARD`). Matérialise-la seulement au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou "
       "rendu. Si aucune alternative plausible ne peut modifier le choix, note cette condition et passe à la spec après avoir "
       "nommé la raison.",
    "Ses leviers sont les axes de `SAVOIR/CRAFT/CFT-02` ; sa matérialisation, sa trace avant le build et sa comparaison suivent "
    "`ACTION/PIPELINE-DIRECTION` (étapes 3 et 7).")
sub(A, "Lorsque la décision est ouverte et qu’une position différente peut réellement changer le choix, considère une proposition "
       "crédible répondant à un public, un JTBD, une contrainte ou une opportunité différente.",
    "Le déclenchement appartient à `DIRECTION` (« Direction divergente ») et les leviers à `SAVOIR/CRAFT/CFT-02`. En trace "
    "complète, avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative "
    "considérée, la raison de son niveau de matérialisation et la preuve attendue ; la projection JSON ne porte pas ce paquet (voir "
    "`ACTION/RUN_CARD`). En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7).")
print("maquette prête :", M)
