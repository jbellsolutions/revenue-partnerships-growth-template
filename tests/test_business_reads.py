import importlib.util,unittest
from pathlib import Path
from unittest.mock import Mock
p=Path(__file__).resolve().parents[1]/'scripts/business_read_mcp.py'
spec=importlib.util.spec_from_file_location('business_reads',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class ReadBoundary(unittest.TestCase):
 def setup_reader(self):
  r=m.Reads.__new__(m.Reads);r.bindings={'attio':{'workspace_id':'client-a','lists':{'Dream100':'11111111-1111-4111-8111-111111111111'}},'clickup':{'workspace_id':'team-a','task_id':'testtask'}}
  r.secrets={};r.request=Mock(return_value={'active':True,'workspace_id':'client-a'});return r
 def test_workspace_mismatch_stops(self):
  r=self.setup_reader();r.request.return_value={'active':True,'workspace_id':'wrong'}
  with self.assertRaisesRegex(ValueError,'mismatch'):r.call('attio_partner_entries_read',{'list_alias':'Dream100'})
  self.assertEqual(r.request.call_count,1)
 def test_no_arbitrary_endpoint_write_or_list(self):
  r=self.setup_reader()
  for name,args in [('send',{}),('attio_partner_entries_read',{'list_alias':'unbound'}),('clickup_operating_task_read',{'endpoint':'https://example.com'})]:
   with self.assertRaises(ValueError):r.call(name,args)
 def test_bounded_read_query_only(self):
  r=self.setup_reader();r.call('attio_partner_entries_read',{'list_alias':'Dream100','limit':3})
  self.assertEqual(r.request.call_args.args,('attio','/lists/11111111-1111-4111-8111-111111111111/entries/query',{'limit':3,'offset':0}))
  for limit in [-1,26,True,'3']:
   with self.assertRaises(ValueError):r.call('attio_partner_entries_read',{'list_alias':'Dream100','limit':limit})
if __name__=='__main__':unittest.main()
