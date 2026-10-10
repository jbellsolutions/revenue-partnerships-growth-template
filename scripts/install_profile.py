"""Install reviewed context and draft-only MCP into a fresh native Hermes profile."""
import argparse,json,os,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def install(profile,client):
 import yaml
 profile=Path(profile).resolve();client=Path(client).resolve()
 program=json.loads((client/'client/program.json').read_text())
 if program['client_id']=='CHANGE_ME': raise ValueError('Private client identity required')
 marker=profile/'revenue-install.json'
 if marker.exists(): raise ValueError('Already installed; use a reviewed update/backup procedure')
 if not profile.is_dir(): raise ValueError('Create a fresh native Hermes profile first')
 for name in ['AGENTS.md','SOUL.md']:
  if (profile/name).exists(): raise ValueError('Existing identity file: '+name)
 if any((profile/'skills').glob('**/SKILL.md')): raise ValueError('Profile already contains skills')
 profile.chmod(0o700)
 shutil.copytree(ROOT/'skills',profile/'skills',dirs_exist_ok=True)
 for name in ['AGENTS.md','SOUL.md']: shutil.copy(ROOT/name,profile/name)
 private=profile/'private-business';private.mkdir(mode=0o700,exist_ok=True)
 shutil.copy(client/'client/program.json',private/'program.json')
 shutil.copy(client/'PROGRAM.md',private/'PROGRAM.md')
 settings=private/'relationship/config';settings.mkdir(parents=True,mode=0o700,exist_ok=True)
 (settings/'relationship.json').write_text(json.dumps({'client':program['business'],'employee_default':'revenue-partnerships-growth','category':'revenue partnership growth'},indent=2)+'\n')
 with (profile/'AGENTS.md').open('a') as f:
  f.write('\n## Private program\nRead '+str(private/'program.json')+' and '+str(private/'PROGRAM.md')+' before work. Template reference dossiers: '+str(ROOT/'blueprints/revenue-partnerships')+'. The 339 definitions are shared reference material, not actual partners.\n')
 config={'model':{'provider':'openrouter','default':'z-ai/glm-5.3-flash'},'toolsets':['file','skills','memory'],'approvals':{'mode':'manual','mcp_reload_confirm':True,'destructive_slash_confirm':True},'agent':{'max_turns':10},'plugins':{'enabled':[]},'mcp_servers':{'revenue-relationships':{'command':sys.executable,'args':['-m','relcore.mcp_server','--mode','plugin'],'env':{'PYTHONPATH':str(ROOT),'TRP_REPO':str(ROOT),'RELCORE_MODE':'plugin','RELCORE_HOME':str(private/'relationship'),'RELCORE_VAULT':str(private/'vault'),'RELCORE_STOP_FILE':str(profile/'OPERATION_STOPPED'),'RELCORE_TAXONOMY':str(ROOT/'blueprints/revenue-partnerships/catalog/taxonomy.json'),'RELCORE_EMPLOYEE':'revenue-partnerships-growth'},'trust':False,'enabled':True,'timeout':30}}}
 config_path=profile/'config.yaml'
 if config_path.exists(): shutil.copy(config_path,profile/'config.yaml.before-revenue-install')
 config_path.write_text(yaml.safe_dump(config,sort_keys=False));config_path.chmod(0o600)
 # An empty profile env prevents native backfill from cloning all default secrets.
 env=profile/'.env'
 if not env.exists(): env.write_text('# Private provider authentication only; no inherited connector credentials.\n')
 env.chmod(0o600)
 (private/'program.json').chmod(0o600)
 marker.write_text(json.dumps({'client_id':program['client_id'],'template':str(ROOT),'skills':12,'dispatch':'human_send_only','native_connections':'pending'},indent=2)+'\n');marker.chmod(0o600)
 print('Installed 12 skills and isolated drafts-only MCP; authentication/native answer/connections still require verification.')
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--profile',required=True);p.add_argument('--client',required=True);a=p.parse_args();install(a.profile,a.client)
