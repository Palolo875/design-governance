# Décodage du jugement R10 : chaque paire vue deux fois (côtés inversés) ; réponses contradictoires = égal.
import json
from pathlib import Path
SP = Path('/tmp/claude-0/-home-user-design-governance/0a3b69f1-c424-582d-aaa1-b2314040cdb3/scratchpad'); R = SP/'r10'
cle = json.load(open(SP/'r10_cle.json'))['cle']; plan = json.load(open(R/'plan_juges.json'))
out = {'pages': {}, 'paires': {}, 'classements': {}}
for nom, p in plan.items():
    f = R/'juges'/nom/'resultat.json'
    if not f.exists(): print('absent :', nom); continue
    res = json.load(open(f)); inv = {v: k for k, v in p['etiquettes'].items()}
    cond = lambda L: cle[inv[L]]['condition']
    for L, v in res['pages'].items():
        rep = v.get('reprises', {})
        out['pages'].setdefault(inv[L], {})[nom[:2]] = {
            'qualite': v['qualite'], 'adequation': v['adequation'],
            'verite': v['verite'] if isinstance(v['verite'], list) else [v['verite']],
            'reprises': {k: len(rep.get(k, [])) for k in ('bloquant', 'notable', 'finition')}, 'reprises_detail': rep, 'raison': v.get('raison')}
    votes = {}
    for k, (a, b) in enumerate(p['paires'], 1):
        ch = res['paires'][f'P{k}']['choix'].strip().lower()
        win = {'gauche': cond(a), 'droite': cond(b)}.get(ch, 'égal')
        key = '–'.join(sorted((cond(a), cond(b))))
        votes.setdefault(key, []).append(win)
    brief = cle[inv[p['paires'][0][0]]]['brief']
    for key, v in votes.items():
        final = v[0] if v[0] == v[1] else 'égal'
        out['paires'].setdefault(brief, {}).setdefault(key, {})[nom[:2]] = {'deux_sens': v, 'retenu': final}
    out['classements'][nom] = [cond(L) for L in res['classement']]
json.dump(out, open(R/'resultats_decodes.json', 'w'), ensure_ascii=False, indent=1)
for b, d in out['paires'].items():
    for key, j in sorted(d.items()):
        print(b, key, {k: (x['retenu'], x['deux_sens']) for k, x in j.items()})
for nom, c in out['classements'].items(): print('classement', nom, c)
for i, d in out['pages'].items():
    print(i, cle[i]['brief'], cle[i]['condition'], {k: (x['qualite'], x['adequation'], len(x['verite']), x['reprises']) for k, x in d.items()})
