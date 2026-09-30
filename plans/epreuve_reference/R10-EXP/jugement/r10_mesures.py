# Mesures mécaniques du palier exploratoire R10 : T (tenue), D (convergence), H mécanique (exemples signalés, langage du système).
import json, re, subprocess, sys
from pathlib import Path
SP = Path('/tmp/claude-0/-home-user-design-governance/0a3b69f1-c424-582d-aaa1-b2314040cdb3/scratchpad')
PROD, CAP, OUT = SP/'prod10', SP/'cap', SP/'r10'
ids = sys.argv[1:]
res = {}
for i in ids:
    r = json.loads(subprocess.run(['node', 'capture.js', str(PROD/i), str(OUT/'caps'), i], cwd=CAP, capture_output=True, text=True).stdout)
    files = [p for p in (PROD/i).rglob('*') if p.is_file() and 'dg' not in p.relative_to(PROD/i).parts and p.name != 'questions.txt']
    html = (PROD/i/'index.html').read_text(encoding='utf-8')
    ext = sorted(set(re.findall(r'https?://([^/"\')\s]+)', html)))
    res[i] = {'capture': r, 'poids_octets_html': len(html.encode()), 'poids_octets_dossier_hors_dg': sum(p.stat().st_size for p in files),
              'fichiers_hors_dg': sorted(str(p.relative_to(PROD/i)) for p in files), 'hotes_externes': ext,
              'questions': (PROD/i/'questions.txt').read_text(encoding='utf-8') if (PROD/i/'questions.txt').exists() else None}
m2 = json.loads(subprocess.run(['node', 'm2.js', str(PROD)] + ids, cwd=CAP, capture_output=True, text=True).stdout)
tx = json.loads(subprocess.run(['node', 'texte.js', str(PROD)] + ids, cwd=CAP, capture_output=True, text=True).stdout)
SIG = re.compile(r"exemple|fictif|à remplacer|a remplacer|provisoire|placeholder|à confirmer|non contractuel", re.I)
SYS = re.compile(r"\b(EXPLORATORY|MODAL|PARTI|RUN_CARD|checkpoint|Gate [ABC]|trace légère|DIRECTION/|ACTION/|SAVOIR/)\b")
for i in ids:
    t = tx[i]
    res[i]['m2'] = m2[i]
    res[i]['signalements_exemple'] = len(SIG.findall(t))
    res[i]['langage_systeme'] = sorted(set(SYS.findall(t)))
    res[i]['mots_visibles'] = len(t.split())
json.dump(res, open(OUT/'mesures_mecaniques.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({i: {k: v for k, v in res[i].items() if k not in ('questions', 'fichiers_hors_dg')} for i in ids}, ensure_ascii=False, indent=1))
