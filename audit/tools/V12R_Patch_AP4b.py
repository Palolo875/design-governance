#!/usr/bin/env python3
"""V1.2 — PATCH-DECISION AP4b (audit progressif externe, unité 4b) : façades dérivées des contrats stabilisés.

C04 trace légère exposée dans QUICKSTART, GLOSSAIRE et READING_MAP (mode et trace distingués) ; AUD-06 parcours par défaut
(proposition, checkpoint, noyau) dans QUICKSTART, README, flux et exemples ; AUD-13 forme courte LITE distincte de la trace
légère ; C17 et AUD-08 exemple cohérent hors domaine de référence ; C23 liens vers « Commencer » ; C24 lecteur et moment de
la ligne de run ; C33 livraison située ; C39 ancien parcours situé, ancre de la carte.
Audit : `DG_Audit_progressif_10`. Décision de l'owner (01-10-2026) : « Allons-y pour AP4b » ; textes soumis avant application.
Rapport : `V12R_44_AP4b_FACADES.md`. Usage : python3 V12R_Patch_AP4b.py <racine> [--verifier | --mutations]
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import V12R_Patch_R5b1 as base  # noqa: E402
from V12_Patch_ABD import apply  # noqa: E402

O = "V1/official/"
Q, G, RM, A, D, C, OM, OR = (O + n for n in ("QUICKSTART.md", "GLOSSAIRE.md", "READING_MAP.md", "ACTION.md", "DIRECTION.md",
                                            "CHANGELOG.md", "ORCHESTRATION_MAP.md", "README.md"))
EX, FL = "skills/design-governance-practice/references/examples.md", "skills/design-governance-practice/references/flow.md"
F = HERE / "V12R_Patch_AP4b_fichiers" / "scripts"
FILE_REPLACE = {
    "scripts/validate_structure.py": ("eddfa8b9fd4162dcfa28e568fc8f406460843392568fcdbd77644333bed9c743", F / "validate_structure.py"),
    "scripts/build_distributions.sh": ("0b949aca42e15aa2f1a36cbaf299da697a6522cdb8b2a73614ecbf964cdf7741", F / "build_distributions.sh"),
}

OLD_EXAMPLE = """**Demande :** « Il me faut un site pour ma boulangerie. » Rien d’autre.

**Prise de brief, en un seul échange :** l’agent demande les contenus réels (produits, prix, horaires, adresse), le logo ou les couleurs s’ils existent, et deux ou trois photos du comptoir ; la destination est une vraie mise en ligne. Faute de réponse, il construit avec des hypothèses nommées.

```text
THÈSE: le pain du jour se choisit d’un coup d’œil, avant d’entrer
OBJET DE PREUVE: la vitrine du jour, composant codé (produit, prix, heure de sortie du four)
MODAL: photo pleine largeur, titre centré, trois cartes « nos valeurs »
PARTI: s’écarter pour la première scène, où la vitrine du jour remplace la photo ; garder la navigation attendue
FABRICATION: typographie et couleur au plafond (polices libres, palette tirée des photos) ; photos du client moyennes, traitement commun choisi pour unifier la série ; aucune illustration dessinée
DÉFAUT DOMINANT: après capture, les prix se lisent mal sur mobile ; taille et contraste corrigés, seconde capture comparée
```

**Réponse visible :** « J’ai construit une page d’accueil organisée autour de la vitrine du jour. Pourquoi : on choisit son pain avant d’entrer, la page le permet en un coup d’œil. Ce qui manque pour la vraie version : vos prix, vos horaires et une photo du comptoir en lumière du jour ; les produits affichés sont des exemples marqués comme tels. La suite : envoyez ces éléments, je les intègre et je vérifie le mobile. »"""

NEW_EXAMPLE = """**Demande :** « Il me faut un site pour mon atelier de réparation de vélos. » Rien d’autre.

**Prise de brief, en un seul échange, avant le build :** la personne est présente. L’agent demande les contenus réels (services, tarifs, horaires, adresse, numéro), le logo ou les couleurs s’ils existent, et deux ou trois photos de l’atelier ; la destination est une vraie mise en ligne. La personne répond avec deux photos de l’atelier, sans tarifs ni horaires. L’agent construit avec les photos reçues et des contenus d’exemple marqués pour le reste.

**Réponse visible :** « J’ai construit une page d’accueil organisée autour du tableau de l’atelier : les réparations du jour et le délai annoncé. Pourquoi : on veut savoir quand son vélo sera prêt avant de passer ; j’ai écarté la grande photo d’entrée suivie de trois cartes de services, que n’importe quel atelier aurait. Ce qui manque pour la vraie version : vos tarifs, vos horaires et votre numéro ; ceux affichés sont des exemples marqués comme tels, et le bouton « Appeler l’atelier » fonctionne avec un numéro d’exemple. La suite : envoyez ces éléments, je les intègre et je vérifie le mobile. »

**Trace (trace légère, écrite à côté de l’artefact) :**

```text
MODE: DIRECTION
THÈSE: savoir quand son vélo sera prêt → le tableau de l’atelier, composant codé (réparations du jour, délai, tarif indicatif) → le tableau remplace la photo d’entrée
MODAL, TRAME ET PARTI: photo pleine largeur, titre centré, trois cartes « nos services » ; trame héros → services → avis → contact, rompue : le tableau ouvre la page ; s’écarter pour la première scène seulement, garder la navigation et le contact attendus
PLAFOND ET CONTENUS MARQUÉS: typographie et couleur au plafond (polices libres, palette tirée des deux photos) ; photos du client moyennes, traitement commun ; tarifs, horaires et numéro marqués « exemple »
DÉFAUT DOMINANT RESTANT: aucun bloquant ; les délais se lisaient mal sur mobile, taille et contraste corrigés, seconde capture comparée
PROCHAINE PREUVE: vrais tarifs, horaires et numéro intégrés, puis capture mobile
```"""

PATCH = [
    # QUICKSTART (C04, C23, C24, AUD-06)
    ("AP4b-Q1", "QUICKSTART : lien vers « Commencer » (C23)", Q,
     "la section « Commencer » du README du package suffit",
     "la section [« Commencer »](../../README.md#commencer) du README du package suffit"),
    ("AP4b-Q2", "QUICKSTART : la ligne suit le classement (C24)", Q,
     "le risque, le périmètre ou la décision le justifie. Notez :",
     "le risque, le périmètre ou la décision le justifie. Une fois la demande classée par `DIRECTION/START` (par "
     "l’opérateur ou l’agent, jamais par la personne qui demande), notez :"),
    ("AP4b-Q3", "QUICKSTART : suite par défaut, la proposition (C04, AUD-06)", Q,
     "puis choisissez une seule suite : **corriger**, **approfondir la preuve**, **rouvrir**, **reclassifier** ou **fermer**.",
     "puis choisissez une seule suite : **corriger**, **approfondir la preuve**, **rouvrir**, **reclassifier**, "
     "**proposer** ou **fermer**. Par défaut, le run s’arrête à la proposition, en trace légère : la première proposition "
     "vaut checkpoint, sauf action irréversible ou coûteuse ; **fermer** suppose la trace complète (run persistant, "
     "partagé, audité ou acceptation demandée)."),
    ("AP4b-Q4", "QUICKSTART : niveau de trace (C04)", Q,
     "et le **handoff**, pour une reprise ou un run persistant (voir `ACTION/HANDOFF`).",
     "et le **handoff**, pour une reprise ou un run persistant (voir `ACTION/HANDOFF`). Le niveau de trace ne dépend pas "
     "du mode : sans persistance, partage, audit ni acceptation demandée, la **trace légère** suffit (six lignes au plus, "
     "à côté de l’artefact ou sous « Trace » après la réponse) ; dans les autres cas, la **trace complète** s’impose."),
    ("AP4b-Q5", "QUICKSTART : ligne de run et classement (C24)", Q,
     "Avant de construire ou de modifier, répondez aux cinq questions du parcours commun.\n\nProduisez ensuite la ligne minimale :",
     "Avant de construire ou de modifier, répondez aux cinq questions du parcours commun.\n\nProduisez ensuite la ligne "
     "minimale ; elle reprend la ligne du parcours commun avec un identifiant et l’état du run (`ACTION/STATUS`), "
     "l’owner restant nommé dans l’entrée minimale de `DIRECTION/START` :"),
    ("AP4b-Q6", "QUICKSTART : one-shot, trace à son niveau (C04)", Q,
     "6. la persistance des preuves, limites et décisions.",
     "6. la trace des preuves, limites et décisions, à son niveau (légère par défaut, complète si le run est persistant, "
     "partagé ou audité)."),
    ("AP4b-Q7", "QUICKSTART : sortie one-shot (C04)", Q,
     "La sortie one-shot peut être une décision directement clôturée si",
     "En trace légère, la sortie one-shot est la proposition. En trace complète, la sortie one-shot peut être une "
     "décision directement clôturée si"),
    ("AP4b-Q8", "QUICKSTART : l'agent lit le noyau et CHARGE (AUD-06)", Q,
     "L’agent localise le package réellement fourni, classe la demande avec `DIRECTION/START`, charge uniquement les "
     "propriétaires utiles,",
     "L’agent localise le package réellement fourni, lit le noyau de la skill, classe la demande avec `DIRECTION/START`, "
     "charge la ligne de son mode dans `DIRECTION/CHARGE` et seulement les propriétaires utiles,"),
    ("AP4b-Q9", "QUICKSTART : réponse visible et trace légère (AUD-06)", Q,
     "ce qui manque pour la vraie version, la suite (voir `ACTION/HANDOFF`).",
     "ce qui manque pour la vraie version, la suite (voir `ACTION/HANDOFF`), avec la trace légère par défaut."),
    # README officiel (C23), README du package (AUD-06)
    ("AP4b-R1", "README officiel : lien vers « Commencer » (C23)", OR,
     "lisez la section « Commencer » du README à la racine du package",
     "lisez la section [« Commencer »](../../README.md#commencer) du README à la racine du package"),
    ("AP4b-R2", "README du package : parcours, proposer ou fermer (AUD-06)", "README.md",
     "Le parcours complet d’un run est : classer, diriger, construire, observer, corriger, fermer ;",
     "Le parcours complet d’un run est : classer, diriger, construire, observer, corriger, puis proposer (par défaut, "
     "en trace légère : la première proposition vaut checkpoint) ou fermer (trace complète) ;"),
    # GLOSSAIRE (C04, C24, C33)
    ("AP4b-G1", "GLOSSAIRE : mode et trace distingués (C04)", G,
     "| **Mode** | Le niveau de protection et de trace adapté au travail : `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. |",
     "| **Mode** | Le niveau de protection adapté au travail : `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. Le "
     "niveau de trace (légère ou complète) se choisit à part, selon que le run est persistant, partagé ou audité. |"),
    ("AP4b-G2", "GLOSSAIRE : run, proposition ou clôture (C04)", G,
     "| **Run** | Un travail délimité, avec une décision, un risque, un artefact, une preuve et une clôture. |",
     "| **Run** | Un travail délimité, avec une décision, un risque, un artefact et une preuve. Il s’arrête à une "
     "proposition (trace légère) ou à une clôture (trace complète). |"),
    ("AP4b-G3", "GLOSSAIRE : trace légère, lignes d'ACTION (C04)", G,
     "six lignes au plus (mode, thèse, modal, trame et parti, plafond, défaut dominant, prochaine preuve)",
     "six lignes au plus (mode ; thèse ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant "
     "restant ; prochaine preuve)"),
    ("AP4b-G4", "GLOSSAIRE : livraison située (C33)", G,
     "| **Trame modale** |",
     "| **Livraison** | La remise d’un artefact à une personne : la première proposition (trace légère ; elle vaut "
     "checkpoint) ou la remise acceptée (trace complète). Les preuves applicables au mode sont dues dans les deux cas ; "
     "seule leur écriture s’allège en trace légère. |\n| **Trame modale** |"),
    ("AP4b-G5", "GLOSSAIRE : pour commencer, classer d'abord (C24)", G,
     "## Pour commencer sans vocabulaire préalable\n\n1. Établissez le mode, le risque dominant, la décision à changer, la "
     "prochaine preuve et l’owner.\n2. Vérifiez ou confirmez le classement avec `DIRECTION/START` et choisissez le "
     "propriétaire normatif utile.",
     "## Pour commencer sans vocabulaire préalable\n\nCette suite s’adresse à l’opérateur ou à l’agent ; une personne qui "
     "fait une demande n’a pas de mode à choisir (section « Commencer » du README du package).\n\n1. Classez la demande "
     "avec `DIRECTION/START` : mode et risque dominant ; notez la décision à changer, la prochaine preuve et l’owner.\n"
     "2. Chargez la ligne de ce mode dans `DIRECTION/CHARGE`, puis seulement le propriétaire normatif utile."),
    # READING_MAP (C04), ORCHESTRATION_MAP (C39)
    ("AP4b-M1", "READING_MAP : sortie par défaut (C04)", RM,
     "Sortie : réponse visible et handoff (`ACTION/HANDOFF`) ; clôture : `ACTION/CLOSE-PACKAGE`.",
     "Sortie : réponse visible et trace légère par défaut ; handoff et clôture (`ACTION/CLOSE-PACKAGE`) en trace "
     "complète (`ACTION/HANDOFF`)."),
    ("AP4b-M2", "READING_MAP : RUN_CARD selon la trace (C04)", RM,
     "| Cette carte et `RUN_CARD` seulement si plusieurs capacités sont réellement nécessaires |",
     "| Cette carte seulement si plusieurs capacités sont réellement nécessaires ; `RUN_CARD` en trace complète (run "
     "persistant, partagé, audité ou acceptation demandée), quel que soit le nombre de capacités |"),
    ("AP4b-M3", "ORCHESTRATION_MAP : ancre de la section (C39)", OM,
     "[`READING_MAP.md`](READING_MAP.md), section « Combinaisons par résultat recherché »",
     "[`READING_MAP.md`](READING_MAP.md#combinaisons-par-résultat-recherché), section « Combinaisons par résultat recherché »"),
    # ACTION/HANDOFF (AUD-13), DIRECTION/DOUBLE-LOOP (C33, noyau)
    ("AP4b-A1", "HANDOFF : forme courte LITE situee (AUD-13)", A,
     "**Forme courte LITE non persistante :** le paquet LITE",
     "**Forme courte LITE** (trace complète d’un `LITE` clôturé sans `RUN_CARD`, distincte de la trace légère, qui ne "
     "clôture pas) : le paquet LITE"),
    ("AP4b-D1", "DOUBLE-LOOP : décision établie, proposer ou clôturer (C33, noyau)", D,
     "| Décision suffisamment établie | Décider et persister la trace ; ne pas prolonger le polish sans changement attendu. |",
     "| Décision suffisamment établie | Proposer (trace légère : la proposition vaut checkpoint) ; en trace complète, "
     "décider et persister la trace. Ne pas prolonger le polish sans changement attendu. |"),
    # Exemples et flux (C17, AUD-06, AUD-08)
    ("AP4b-E1", "exemple : brief flou, hors B-DLA, cohérent, trace légère (C17, AUD-06, AUD-08)", EX, OLD_EXAMPLE, NEW_EXAMPLE),
    ("AP4b-E2", "exemples : note de niveau de trace (AUD-06)", EX,
     "montre la sortie par défaut : une proposition et sa réponse visible, sans clôture.",
     "montre la sortie par défaut : une proposition, sa réponse visible et sa trace légère, sans clôture."),
    ("AP4b-F1", "flux : la proposition vaut checkpoint (AUD-06)", FL,
     "puis présenter la proposition (trace légère) ou décider",
     "puis présenter la proposition (trace légère ; la première proposition vaut checkpoint) ou décider"),
    # RELEASE_NOTES (C39)
    ("AP4b-N1", "RELEASE_NOTES : ancien parcours situé (C39)", "RELEASE_NOTES.md",
     "## Parcours de découverte\n\n",
     "## Parcours de découverte\n\n> **Parcours de V1.1.1, historique.** Dans la candidate courante, une personne commence "
     "par la section « Commencer » du README du package ; un agent entre par la skill (noyau de fabrication et "
     "`DIRECTION/CHARGE`) et s’arrête par défaut à la proposition ; les guides s’ouvrent à la demande ; "
     "`ORCHESTRATION_MAP.md` n’est plus qu’un pointeur vers `READING_MAP.md`. Ces notes seront réécrites en R12.\n\n"),
    ("AP4b-H", "CHANGELOG", C,
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence",
     "- **Façades (audit progressif, unité 4b).** QUICKSTART, glossaire, carte de lecture, README, flux et exemples "
     "exposent la trace légère et la proposition par défaut (la première proposition vaut checkpoint ; fermer suppose la "
     "trace complète) ; mode et niveau de trace sont distingués ; la forme courte LITE est située ; l’exemple de brief "
     "flou change de domaine et montre sa trace légère ; les guides lient la section « Commencer » ; l’ancien parcours "
     "des notes de version est situé comme historique.\n"
     "- **Efficacité.** `NOT-VERIFIED` : l’épreuve de référence"),
]
MUTATION_OF = {
    "AP4b-Q1": "(C23)", "AP4b-R1": "(C23)", "AP4b-Q2": "(C24)", "AP4b-Q3": "(C04)", "AP4b-Q4": "(C04)", "AP4b-Q7": "(C04)",
    "AP4b-Q8": "(AUD-06)", "AP4b-R2": "(AUD-06)", "AP4b-G1": "[FAC-01]", "AP4b-G2": "[FAC-01]", "AP4b-G3": "[FAC-01]",
    "AP4b-G4": "[FAC-01]", "AP4b-G5": "vocabulaire retiré", "AP4b-M1": "(C04)", "AP4b-M2": "[FAC-01]",
    "AP4b-A1": "vocabulaire retiré", "AP4b-D1": "[FAC-01]", "AP4b-E1": "[FAC-01]", "AP4b-E2": "(AUD-06)",
    "AP4b-F1": "(AUD-06)", "AP4b-N1": "[FAC-01]",
}
REBUILD = {"AP4b-D1"}


def mutations(root: Path) -> int:
    bad = 0
    for pid, motif in MUTATION_OF.items():
        with tempfile.TemporaryDirectory() as tmp:
            copy = base.fresh(root, tmp)
            problems = apply(copy, [e for e in PATCH if e[0] == pid], reverse=True)
            if not problems and pid in REBUILD:
                base.build_core(copy)
            code, out = base.structure(copy)
            red = code != 0 and motif in out and not problems
            print(f"inverse de {pid} : {'ROUGE' if red else 'NON ROUGE'} (motif « {motif} »){' ; ' + '; '.join(problems) if problems else ''}")
            bad += 0 if red else 1
    return bad


def main() -> int:
    base.PATCH, base.FILE_REPLACE, base.MUTATION_OF, base.EXTRA_MUTATIONS = PATCH, FILE_REPLACE, MUTATION_OF, []
    if "--mutations" in sys.argv and len(sys.argv) > 1:
        return 1 if mutations(Path(sys.argv[1]).resolve()) else 0
    return base.main()


if __name__ == "__main__":
    sys.exit(main())
