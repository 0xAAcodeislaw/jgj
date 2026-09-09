from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];p=r/'verification/classic.manifest.json';m=json.loads(p.read_text())
for key,path in dict(inputPath='data/classic.json',htmlPath='assets/cards/classic.html',pngPath='assets/cards/classic.png',manifestPath='verification/classic.manifest.json',heroImagePath='assets/images/reflection.png').items():m[key]=str(r/path)
m['qaSlices']=[str(r/'verification/classic-slices'/Path(s).name) for s in m['qaSlices']]
for s in m['qaSliceDetails']:s['path']=str(r/'verification/classic-slices'/Path(s['path']).name)
p.write_text(json.dumps(m,ensure_ascii=False,indent=2));print('Manifest paths relocated; artifact hashes unchanged.')
