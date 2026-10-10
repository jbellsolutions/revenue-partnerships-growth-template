"""Narrow read-only Attio/ClickUp MCP. Credentials stay in the native private secret file.

Only configured client lists and one configured operating task are exposed. No
caller-supplied endpoint, mutation, sender, payout or arbitrary CRM record lookup.
"""
import json,os,sys,urllib.request,urllib.error,re
from pathlib import Path

def schema(properties=None,required=None):
 return {'type':'object','properties':properties or {},'required':required or [],'additionalProperties':False}
TOOLS=[
 {'name':'revenue_connections_verify','description':'Verify the native Attio workspace and ClickUp user/task binding; read-only.','inputSchema':schema()},
 {'name':'attio_partner_lists_read','description':'Read only the configured partner lists.','inputSchema':schema()},
 {'name':'attio_partner_list_schema_read','description':'Read the attributes of one configured partner list.','inputSchema':schema({'list_alias':{'type':'string'}},['list_alias'])},
 {'name':'attio_partner_entries_read','description':'Read a bounded page of actual entries from a configured partner list. Does not synchronize or update records.','inputSchema':schema({'list_alias':{'type':'string'},'limit':{'type':'integer','minimum':1,'maximum':25},'offset':{'type':'integer','minimum':0}},['list_alias'])},
 {'name':'clickup_operating_task_read','description':'Read the configured operating task; no task writes or unrelated workspace access.','inputSchema':schema()},
]
class Reads:
 def __init__(self):
  self.bindings=json.loads(Path(os.environ['REVENUE_CONNECTION_BINDINGS']).read_text())
  self.secrets={}
  if os.environ.get('REVENUE_CONNECTION_ENV'):
   from dotenv import dotenv_values
   self.secrets=dotenv_values(os.environ['REVENUE_CONNECTION_ENV'])
 def request(self,provider,path,payload=None):
  # Endpoints are generated only by methods below, never accepted from a tool caller.
  if provider=='attio':base='https://api.attio.com/v2';name='ATTIO_API_KEY';prefix='Bearer '
  elif provider=='clickup':base='https://api.clickup.com/api/v2';name='CLICKUP_API_TOKEN';prefix=''
  else:raise ValueError('Unknown provider')
  token=self.secrets.get(name) or os.environ.get(name)
  if not token:raise ValueError('Missing private '+name)
  # POST is permitted only for Attio list-entry query (a provider-defined read).
  if payload is not None and not (provider=='attio' and re.fullmatch(r'/lists/[a-f0-9-]{36}/entries/query',path)):
   raise ValueError('Only the bounded entry-query read can use POST')
  class NoRedirect(urllib.request.HTTPRedirectHandler):
   def redirect_request(self,*args,**kwargs):return None
  req=urllib.request.Request(base+path,data=json.dumps(payload).encode() if payload is not None else None,headers={'Authorization':prefix+token,'Accept':'application/json','Content-Type':'application/json'},method='POST' if payload is not None else 'GET')
  try:
   with urllib.request.build_opener(NoRedirect).open(req,timeout=15) as response:return json.load(response)
  except urllib.error.HTTPError as e:raise ValueError(provider+' read failed: HTTP '+str(e.code)) from None
  except urllib.error.URLError:raise ValueError(provider+' connection failed; no write attempted') from None
  except Exception:raise ValueError(provider+' read failed; credentials and raw errors withheld') from None
 def attio_identity(self):
  d=self.request('attio','/self')
  expected=self.bindings['attio'].get('workspace_id')
  if not expected or d.get('workspace_id')!=expected or not d.get('active'):
   raise ValueError('Attio workspace/token binding mismatch; stop')
  return {k:d.get(k) for k in ['workspace_id','workspace_name','workspace_slug','active']}
 def list_id(self,alias):
  value=self.bindings['attio']['lists'].get(alias)
  if not value or not re.fullmatch(r'[a-f0-9-]{36}',value):raise ValueError('List is not configured for this client')
  return value
 def task(self):
  value=self.bindings['clickup']['task_id']
  if not re.fullmatch('[a-zA-Z0-9]+',value):raise ValueError('Invalid configured task')
  d=self.request('clickup','/task/'+value+'?include_markdown_description=true')
  if str(d.get('id'))!=value:raise ValueError('ClickUp task identity mismatch')
  expected=self.bindings['clickup'].get('workspace_id')
  if not expected or str(d.get('team_id'))!=str(expected):raise ValueError('ClickUp workspace mismatch; stop')
  return d
 def call(self,name,args):
  tool=next((t for t in TOOLS if t['name']==name),None)
  if not tool:raise ValueError('Tool is not available; no writes exposed')
  allowed=tool['inputSchema']['properties']
  if set(args)-set(allowed) or not set(tool['inputSchema']['required'])<=set(args):raise ValueError('Unexpected/missing arguments')
  if name=='clickup_operating_task_read':return self.task()
  identity=self.attio_identity()
  if name=='revenue_connections_verify':
   user=self.request('clickup','/user').get('user',{});task=self.task()
   return {'attio':identity,'clickup':{'user_id':user.get('id'),'username':user.get('username'),'workspace_id':task.get('team_id'),'task_id':task['id'],'task_name':task['name']},'access':'reads_only','synchronization':'not_dispatched'}
  if name=='attio_partner_lists_read':
   return {'workspace':identity,'lists':{a:self.request('attio','/lists/'+self.list_id(a)).get('data') for a in self.bindings['attio']['lists']}}
  ident=self.list_id(args['list_alias'])
  if name=='attio_partner_list_schema_read':return self.request('attio','/lists/'+ident+'/attributes')
  limit=args.get('limit',10);offset=args.get('offset',0)
  if type(limit)!=int or not 1<=limit<=25 or type(offset)!=int or offset<0:raise ValueError('Invalid bounded pagination')
  return self.request('attio','/lists/'+ident+'/entries/query',{'limit':limit,'offset':offset})

def main():
 server=None
 msg={}
 for line in sys.stdin:
  try:
   msg=json.loads(line);mid=msg.get('id')
   if mid is None:continue
   method=msg.get('method')
   if method=='initialize':result={'protocolVersion':msg.get('params',{}).get('protocolVersion','2025-06-18'),'capabilities':{'tools':{}},'serverInfo':{'name':'revenue-business-reads','version':'0.1.0'}}
   elif method=='ping':result={}
   elif method=='tools/list':result={'tools':[{**t,'annotations':{'readOnlyHint':True,'destructiveHint':False,'openWorldHint':True}} for t in TOOLS]}
   elif method=='tools/call':
    try:
     if server is None:server=Reads()
     p=msg.get('params',{});data=server.call(p.get('name'),p.get('arguments',{}));result={'content':[{'type':'text','text':json.dumps(data)}],'structuredContent':data,'isError':False}
    except Exception as e:result={'content':[{'type':'text','text':str(e)}],'isError':True}
   else:raise ValueError('Unsupported RPC method')
   print(json.dumps({'jsonrpc':'2.0','id':mid,'result':result}),flush=True)
  except Exception:
   print(json.dumps({'jsonrpc':'2.0','id':msg.get('id') if isinstance(msg,dict) else None,'error':{'code':-32603,'message':'Invalid request'}}),flush=True)
if __name__=='__main__':main()
