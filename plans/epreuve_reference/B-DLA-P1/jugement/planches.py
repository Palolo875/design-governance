# Planches uniformes pour le juge : bureau (1440 réduit à 720, colonnes de 1300 px, 3 par planche)
# et mobile (390, colonnes de 1300 px, 5 par planche). Usage : python3 planches.py <caps> <sortie> ID [ID...]
import sys
from pathlib import Path
from PIL import Image
caps, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
def sheets(img, per, colw, h=1300, maxs=3):
    cols=[img.crop((0,y,img.width,min(y+h,img.height))) for y in range(0,img.height,h)]
    res=[]
    for i in range(0,len(cols),per):
        grp=cols[i:i+per]; sh=Image.new('RGB',(per*colw+(per-1)*20,h),(128,128,128))
        for k,c in enumerate(grp): sh.paste(c,(k*(colw+20),0))
        res.append(sh)
    return res[:maxs]
for rid in sys.argv[3:]:
    d=Image.open(caps/f"{rid}_1440.png").convert('RGB'); d=d.resize((720,int(d.height*720/1440)))
    for i,sh in enumerate(sheets(d,3,720),1): sh.save(out/f"{rid}_bureau_{i}.jpg",quality=85)
    m=Image.open(caps/f"{rid}_390.png").convert('RGB')
    for i,sh in enumerate(sheets(m,5,390),1): sh.save(out/f"{rid}_mobile_{i}.jpg",quality=85)
    print(rid, sorted(p.name for p in out.glob(f"{rid}_*")))
