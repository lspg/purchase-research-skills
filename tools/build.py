#!/usr/bin/env python3
from pathlib import Path
import json,re,shutil
R=Path(__file__).resolve().parents[1]
def metadata(text):
 h=re.match(r"^---\n(.*?)\n---\n",text,re.S)
 b=h.group(1); n=re.search(r"^name:\s*(.+)$",b,re.M).group(1).strip(); v=re.search(r"^\s+version:\s*(.+)$",b,re.M).group(1).strip()
 return n,v
for d in sorted((R/"skills").iterdir()):
 f=d/"SKILL.md"
 if not f.exists(): continue
 text=f.read_text(); name,version=metadata(text); refs=sorted((d/"references").glob("*.md"))
 hd=R/"dist"/"hermes"/name
 if hd.exists(): shutil.rmtree(hd)
 (hd/"references").mkdir(parents=True)
 (hd/"SKILL.md").write_text(text+"\n## Hermes safety boundary\nResearch only. No system or skill mutation without explicit authorization.\n")
 for p in refs: shutil.copy2(p,hd/"references"/p.name)
 gd=R/"dist"/"gemini"/name
 if gd.exists(): shutil.rmtree(gd)
 (gd/"knowledge").mkdir(parents=True)
 (gd/"GEM-INSTRUCTIONS.md").write_text("# "+name+" bootstrap\nUse Knowledge as operational truth. Read VERSION.json and SKILL-KNOWLEDGE.md. Offer updates when stable manifest is newer; never update silently.\n")
 (gd/"knowledge"/"SKILL-KNOWLEDGE.md").write_text(text)
 (gd/"knowledge"/"VERSION.json").write_text(json.dumps({"project":name,"version":version,"channel":"stable","manifest":"https://github.com/lspg/purchase-research-skills/blob/main/manifest.json"},indent=2))
 for p in refs: shutil.copy2(p,gd/"knowledge"/p.name)
print("Build OK")
