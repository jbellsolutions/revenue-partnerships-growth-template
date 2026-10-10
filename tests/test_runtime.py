import os,json,tempfile,unittest,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Runtime(unittest.TestCase):
 def rpc(self,base,calls):
  env={**os.environ,'PYTHONPATH':str(ROOT),'TRP_REPO':str(ROOT),'RELCORE_MODE':'plugin','RELCORE_HOME':str(base/'relationship'),'RELCORE_VAULT':str(base/'vault'),'RELCORE_TAXONOMY':str(ROOT/'blueprints/revenue-partnerships/catalog/taxonomy.json')}
  messages=[{'jsonrpc':'2.0','id':i,'method':method,'params':params} for i,(method,params) in enumerate(calls,1)]
  r=subprocess.run([sys.executable,'-m','relcore.mcp_server','--mode','plugin'],cwd=ROOT,env=env,input=''.join(json.dumps(m)+'\n' for m in messages),capture_output=True,text=True,timeout=20)
  self.assertEqual(r.returncode,0,r.stderr)
  out=[json.loads(line) for line in r.stdout.splitlines()];self.assertEqual(len(out),len(messages));return out
 def test_mcp_context_and_invalid_send_record(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=self.rpc(Path(tmp),[('initialize',{}),('tools/list',{}),('tools/call',{'name':'rel_entity_upsert','arguments':{'kind':'person','display':'Synthetic Person','identities':{'email':'synthetic@example.com'}}}),('tools/call',{'name':'rel_context','arguments':{'ref':{'email':'synthetic@example.com'}}}),('tools/call',{'name':'rel_sent_record','arguments':{}})])
   self.assertNotIn('error',out[0]);self.assertTrue(out[1]['result']['tools'])
   for tool in out[1]['result']['tools']:self.assertNotIn(tool['name'],['send','rel_send','rel_approve','rel_release'])
   self.assertFalse(out[2]['result']['isError']);self.assertIn('context_digest',out[3]['result']['structuredContent']);self.assertTrue(out[4]['result']['isError'])
 def test_clients_isolated(self):
  with tempfile.TemporaryDirectory() as tmp:
   a,b=Path(tmp)/'a',Path(tmp)/'b'
   created=self.rpc(a,[('tools/call',{'name':'rel_entity_upsert','arguments':{'kind':'person','display':'Synthetic Person','identities':{'email':'only-a@example.com'}}})])
   self.assertFalse(created[0]['result']['isError'])
   out=self.rpc(b,[('tools/call',{'name':'rel_search','arguments':{'text':'only-a'}})])
   self.assertEqual(out[0]['result']['structuredContent']['results'],[])
 def test_protected_terms_and_unknown_sender_refused(self):
  with tempfile.TemporaryDirectory() as tmp:
   out=self.rpc(Path(tmp),[('tools/call',{'name':'rel_entity_upsert','arguments':{'kind':'person','display':'Synthetic','identities':{'email':'protected@example.com'},'fields':{'terms_ref':'invented'}}}),('tools/call',{'name':'rel_send','arguments':{}})])
   self.assertNotIn('terms_ref',out[0]['result']['structuredContent']['fields']);self.assertTrue(out[1]['result']['isError'])
 def test_stale_context_refused(self):
  from unittest.mock import patch
  sys.path.insert(0,str(ROOT))
  from relcore import drafting
  from relcore.mcp_server import Server
  with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ,{'TRP_REPO':str(ROOT),'RELCORE_HOME':tmp+'/relationship','RELCORE_VAULT':tmp+'/vault','RELCORE_MODE':'plugin'}):
   s=Server('plugin');person=s.store.upsert('person','Synthetic',identities={'email':'stale@example.com'},by='owner',source='owner')
   check=drafting.check_draft(s.store,ps_id=None,person_id=person,channel='email',subject='Hello',body='A synthetic draft',digest='not-current',first_touch=False,sender={'name':'Owner','business':'Synthetic'})
   self.assertFalse(check['ok']);self.assertTrue(any('stale' in e for e in check['errors']))
 def test_full_dossier_routing(self):
  env={**os.environ,'TRP_REPO':str(ROOT),'RELCORE_TAXONOMY':str(ROOT/'blueprints/revenue-partnerships/catalog/taxonomy.json')}
  code='from relcore.taxonomy import index,dossier; assert len(index())==339; assert all(dossier(t)["fit_signals"] for t in index()); print("339 runtime dossiers resolved")'
  out=subprocess.run([sys.executable,'-c',code],cwd=ROOT,env=env,capture_output=True,text=True);self.assertEqual(out.returncode,0,out.stderr)
if __name__=='__main__':unittest.main()
