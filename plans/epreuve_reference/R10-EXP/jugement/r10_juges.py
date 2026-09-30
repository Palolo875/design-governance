# Plan des juges du palier R10 : par brief et par juge modèle, étiquettes et ordre tirés au hasard ; 3 paires × 2 sens.
import json, random, shutil, subprocess
from pathlib import Path
SP = Path('/tmp/claude-0/-home-user-design-governance/0a3b69f1-c424-582d-aaa1-b2314040cdb3/scratchpad'); R = SP/'r10'
cle = json.load(open(SP/'r10_cle.json'))['cle']
rng = random.SystemRandom()
BRIEF = {'B-DLA': ("Fais le site d'une boulangerie-pâtisserie à Douala.", (R/'brief_BDLA.md').read_text()),
         'B-SAAS': ("Fais la page d'accueil d'un logiciel de facturation pour PME.", (R/'brief_BSAAS.md').read_text())}
FAITS = {'B-DLA': 'nom, prix, horaires', 'B-SAAS': 'nom, fonctions exactes, tarif'}
QUI = {'B-DLA': "ce commerçant et ses clients", 'B-SAAS': "ce gérant de PME et l'éditeur du logiciel"}
plan = {}
for juge in ('JS', 'JF'):
    for b in ('B-DLA', 'B-SAAS'):
        ids = [i for i, c in cle.items() if c['brief'] == b]
        lettres = rng.sample(list('KLMNPQRSTVWZ'), 3)
        et = dict(zip(ids, lettres)); inv = {v: k for k, v in et.items()}
        paires = []
        for a, c in (('C1', 'C3'), ('C1', 'C4'), ('C3', 'C4')):
            x = next(i for i in ids if cle[i]['condition'] == a); y = next(i for i in ids if cle[i]['condition'] == c)
            paires += [(et[x], et[y]), (et[y], et[x])]
        rng.shuffle(paires)
        # éviter deux sens de la même paire consécutifs
        for _ in range(100):
            if all({paires[k][0], paires[k][1]} != {paires[k+1][0], paires[k+1][1]} for k in range(len(paires)-1)): break
            rng.shuffle(paires)
        nom = f"{juge}_{b}"; d = R/'juges'/nom; d.mkdir(parents=True, exist_ok=True)
        for i in ids:
            for p in (R/'planches').glob(f"{i}_*.jpg"):
                shutil.copy(p, d/p.name.replace(i, f"page_{et[i]}"))
        ordre = sorted(lettres)
        txt = f"""Tu es juge dans une évaluation à l'aveugle de pages web. Tu ne sais pas comment ni par qui elles ont été faites, et tu ne dois rien supposer à ce sujet.

Le besoin réel est le brief ci-dessous. Les pages ont été faites à partir d'une demande beaucoup plus courte (« {BRIEF[b][0]} ») et ne connaissent donc pas ces faits ({FAITS[b]}) : ne les pénalise pas pour un fait qu'elles n'ont pas pu connaître, mais juge ce que la page montre, comme le feraient {QUI[b]}. Un fait inventé présenté comme vrai reste un défaut ; un contenu clairement signalé comme exemple n'en est pas un.

--- BRIEF ---
{BRIEF[b][1].strip()}
--- FIN DU BRIEF ---

Trois pages sont désignées par une lettre : {', '.join(ordre)}. Pour chaque page, les captures sont dans le dossier `{d}/` : `page_<lettre>_bureau_N.jpg` (écran d'ordinateur, page entière réduite, lue colonne par colonne de gauche à droite) et `page_<lettre>_mobile_N.jpg` (téléphone, page entière, colonnes de gauche à droite). Regarde toutes les captures de toutes les pages avant de juger. Ne lis aucun autre fichier.

Pour chaque page, donne :
- qualite : note de 1 à 10 sur la qualité perçue (beauté, composition, typographie, finition, niveau d'un designer senior) ;
- adequation : note de 1 à 10 sur l'adéquation à ce besoin (public, objectif de la page, contraintes, ton) ;
- verite : liste des faits inventés présentés comme vrais (avis ou témoignages, chiffres, clients ou logos, presse, labels, prix ou historique non donnés) ; un exemple clairement signalé comme exemple ne compte pas ;
- reprises : ce qu'il faudrait corriger avant de montrer la page au client, en trois listes « bloquant », « notable », « finition » ;
- raison : une phrase.

Puis tranche ces {len(paires)} paires (« gauche », « droite » ou « égal », sur l'ensemble qualité et adéquation ; question : lequel est le plus proche d'un travail de designer senior pour ce besoin ?), avec une raison courte chacune :
""" + "\n".join(f"P{k} : {a} (gauche) contre {c} (droite)" for k, (a, c) in enumerate(paires, 1)) + f"""

Enfin, classe les trois pages de la meilleure à la moins bonne.

Écris ton résultat en JSON dans le fichier `{d}/resultat.json`, avec les clés "pages" (lettre → {{"qualite","adequation","verite","reprises","raison"}}), "paires" (P1 à P{len(paires)} → {{"choix","raison"}}) et "classement" (liste de lettres). Réponds ensuite en une ligne : « résultat écrit ».
"""
        (R/'juges'/f"{nom}_consigne.txt").write_text(txt, encoding='utf-8')
        plan[nom] = {'etiquettes': et, 'paires': paires}
json.dump(plan, open(R/'plan_juges.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(plan, ensure_ascii=False))
