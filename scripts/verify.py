"""Offline package gates: deterministic registry, skill contracts, privacy and MCP boundary."""
import json,re,subprocess,sys,os,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def verify():
 subprocess.run([sys.executable,str(ROOT/'scripts/build_partner_blueprint.py'),'--check'],check=True)
 skills=list((ROOT/'skills').glob('*/SKILL.md'));assert len(skills)==12
 for p in skills:
  t=p.read_text();assert t.startswith('---\n');assert f'name: {p.parent.name}\n' in t
  assert re.search(r'^description: .{15,1024}$',t,re.M);assert 'OPERATIONS.md' in t
 registry=json.loads((ROOT/'blueprints/revenue-partnerships/catalog/profiles.json').read_text())
 assert len(registry['profiles'])==339
 assert all(p['activation']=='disabled' and 'client_01' not in p for p in registry['profiles'])
 forbidden=['9262e760-6069-4dcf-a96f-6a92321ad352','/Users/home/','Owner-led service businesses seeking repeatable customer acquisition','8154d0da-5272-4ef2-83fc-14af2cde1e9c']
 for p in ROOT.rglob('*'):
  if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts or p==Path(__file__).resolve():continue
  if p.suffix in ['.md','.json','.py','.html','.yaml','.yml','.sh']:
   t=p.read_text();assert not any(s in t for s in forbidden), 'Client data in '+str(p)
   assert not re.search(r'(?:gh[pousr]_[A-Za-z0-9]{25,}|sk-(?:proj-)?[A-Za-z0-9_-]{30,}|Bearer\s+[A-Za-z0-9_-]{25,})',t), 'Credential-shaped data in '+str(p)
 sys.path.insert(0,str(ROOT))
 from relcore.mcp_server import registered_tools
 tools=registered_tools();assert tools
 assert not any(re.search('approve|send|release|resume|purge',t['name']) for t in tools)
 print('PASS: 339 neutral definitions; 12 skill contracts; clean public boundaries; MCP has no dispatch authority.')
if __name__=='__main__':verify()
