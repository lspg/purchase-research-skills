#!/usr/bin/env python3
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
M=json.loads((R/'manifest.json').read_text())
errors=[]
for name,info in M.get('skills',{}).items():
 f=R/'skills'/name/'SKILL.md'
 if not f.exists(): errors.append(name+': missing canonical SKILL.md'); continue
 text=f.read_text()
 version=info.get('version')
 if ('version: '+version) not in text: errors.append(name+': canonical version mismatch')
 gv=R/'dist'/'gemini'/name/'knowledge'/'VERSION.json'
 if not gv.exists() or json.loads(gv.read_text()).get('version')!=version: errors.append(name+': Gemini mismatch')
 hf=R/'dist'/'hermes'/name/'SKILL.md'
 if not hf.exists() or ('version: '+version) not in hf.read_text(): errors.append(name+': Hermes mismatch')
if errors:
 print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print('Validation OK')
