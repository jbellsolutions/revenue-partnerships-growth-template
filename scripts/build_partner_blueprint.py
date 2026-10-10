"""Build a design registry and Obsidian type dossiers; never provisions employees or calls models."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'blueprints' / 'revenue-partnerships'
PILOT = set()
SOURCES = {
    'F1': ['Public publisher/affiliate program pages', 'Niche content and recommendation archives', 'Owner-authorized existing partner records'],
    'F2': ['Public creator portfolios and media kits', 'Platform-native public content search', 'Creator agency rosters'],
    'F3': ['Publisher sponsorship/media-kit pages', 'Event exhibitor and sponsor directories', 'Organizer rate/availability pages'],
    'F4': ['Public event and collaboration archives', 'Complementary offer/partner pages', 'Public launch calendars'],
    'F5': ['Show guest archives and speaker rosters', 'Conference/session agendas', 'Editor/contributor submission pages'],
    'F6': ['Complementary-service directories', 'Public industry-network membership', 'Owner-authorized existing relationship records'],
    'F7': ['Association/benefit/vendor program pages', 'Community and membership directories', 'Public operator/event pages'],
    'F8': ['Implementation and reseller directories', 'Marketplace/platform partner pages', 'Public case studies and service portfolios'],
    'F9': ['Public alliance/license/partner pages', 'Industry collaboration directories', 'Owner-authorized strategic relationship records'],
    'F10': ['Nonprofit and community program pages', 'Public fundraiser/event directories', 'Institutional partnership pages'],
    'F11': ['Client-authorized CRM/customer records', 'Owner-authorized referral and advocacy history', 'Client-approved internal community/program records'],
}
MOTIONS = {
    'F1': 'A permission-based tracked introduction or useful audience recommendation, under reviewed affiliate terms',
    'F2': 'A relevant creator collaboration; paid placements, usage rights and equity are separate owner decisions',
    'F3': 'A documented sponsorship opportunity; quote, spending and placement require separate approval',
    'F4': 'A mutually useful co-produced event, content resource or shared campaign with agreed responsibilities',
    'F5': 'An educational guest contribution aligned with the host audience and editorial requirements',
    'F6': 'A relevant buyer-journey handoff, warm introduction or complementary joint offer',
    'F7': 'An organizer-approved member benefit, educational session or access partnership',
    'F8': 'A qualified implementation/distribution motion with reviewed fulfillment and commercial responsibilities',
    'F9': 'A strategic collaboration brief for the owner; licensing, exclusivity and equity are never presumed',
    'F10': 'A mission-aligned partnership brief; donation, institutional and fundraising terms require owner review',
    'F11': 'A client-authorized existing-relationship referral, advocacy or reactivation opportunity',
}
AUTHORITY = ('Research public/authorized sources and prepare internal evidence, context and drafts. '
             'Do not send, publish, accept partners, promise terms, spend, change attribution or release payouts. '
             'Use fresh relationship context; observe suppression. Live activation requires reviewed client authority.')


def load_taxonomy(path):
    document = json.loads(Path(path).read_text())
    families = document['families']
    identifiers = set()
    subs = types = 0
    for family in families:
        for node in [family, *family['subcategories']]:
            if node['id'] in identifiers:
                raise ValueError('Duplicate taxonomy identity: ' + node['id'])
            identifiers.add(node['id'])
        if family['subs'] != len(family['subcategories']):
            raise ValueError('Declared subcategory count differs')
        count = 0
        for sub in family['subcategories']:
            if not sub['id'].startswith(family['id'] + '.'):
                raise ValueError('Wrong subcategory parent')
            subs += 1
            for partner_type in sub['types']:
                ident = partner_type['id']
                if not re.fullmatch(r'F(?:[1-9]|10|11)\.[A-Z]\.[1-9][0-9]*', ident):
                    raise ValueError('Unsafe or invalid partner type ID')
                if not ident.startswith(sub['id'] + '.') or ident in identifiers:
                    raise ValueError('Duplicate or wrong-parent partner type')
                identifiers.add(ident)
                count += 1
                types += 1
        if count != family['types']:
            raise ValueError('Declared type count differs')
    if (len(families), subs, types) != (11, 67, 339):
        raise ValueError('Published taxonomy count changed; review source before rebuilding')
    return document


def build(document):
    profiles = []
    outputs = {}
    index = ['# Complete partner taxonomy', '', 'Source snapshot: 2026-10-09. 11 families / 67 subcategories / 339 types.', '']
    for family in document['families']:
        fid = family['id']
        family_note = f'30-Families/{fid}'
        note = [f"# {fid} {family['name']}", '', family['definition'], '', '## Subcategories']
        index.extend([f"## {fid} {family['name']} — {family['types']} types", '', family['definition'], ''])
        for sub in family['subcategories']:
            sid = sub['id']
            sub_note = f'{family_note}/{sid}'
            note.append(f"- [[{sid}|{sub['name']}]]")
            sub_lines = [f"# {sid} {sub['name']}", '', f"Parent: [[{fid}|{family['name']}]]", '', '## Partner types']
            index.extend([f"### {sid} {sub['name']}", ''])
            for item in sub['types']:
                tid, name = item['id'], item['name']
                query = f'"{name}" {{buyer_topic}} {{region}}'
                status = 'unreviewed_client_fit'
                reason = 'Client-specific buyer overlap, economics and authority must be reviewed before activation.'
                avatar = f"Decision-maker responsible for {item['what'].rstrip('.')}; verify role, authority and individual context."
                opportunity = f"Investigate whether {name.lower()} can reach the client’s buyer ICP through this motion: {MOTIONS[fid]}."
                profile = {
                    'schema_version': 1, 'id': f'partner-type-{tid.lower().replace(".", "-")}',
                    'type_id': tid, 'name': name, 'family_id': fid, 'family': family['name'],
                    'subcategory_id': sid, 'subcategory': sub['name'],
                    'definition': item['what'], 'illustrative_example': item['example'],
                    'knowledge_maturity': 'generated_seed_requires_dossier_review',
                    'activation': 'disabled', 'runtime_role': 'proposed_partner_type_specialist',
                    'relationship_owner': 'Assigned by Growth Director per client/relationship',
                    'avatar': avatar,
                    'ideal_partner_profile': {'buyer_overlap': 'Documented access to the client’s actual buyer ICP',
                                             'type_evidence': item['what'],
                                             'readiness': 'A real decision-maker, plausible incentive and feasible activation milestone'},
                    'customer_icp': 'Resolved from each private client program card; never inherited from another client',
                    'lead_opportunities': [{'hypothesis': opportunity, 'sources': SOURCES[fid],
                                            'queries': [query, f'{item["what"]} {{buyer_topic}} partner',
                                                        f'"{sub["name"]}" {{offer_category}}'],
                                            'evidence_required': ['Canonical organization/person and source URL',
                                                                  'Actual buyer overlap and relevant recent activity',
                                                                  'Observed channel/reach; unknown values stay unknown',
                                                                  'Prior relationship, restrictions and feasible next step']}],
                    'commercial_model_reference': item['pay'],
                    'commercial_terms_status': 'Reference only; client owner must approve actual terms',
                    'qualification': {'facts': ['Identity/type match', 'Buyer overlap', 'Trust/reputation', 'Ability to activate'],
                                      'hypotheses': ['Mutual value exchange', 'Willingness', 'Expected commercial contribution'],
                                      'exclusions': ['Opt-out or restricted contact', 'Unresolved identity', 'Unsupported claims or unapproved terms',
                                                     'Conflicting active outreach', 'Commercial model outside client authority']},
                    'application': {'status': status, 'reason': reason,
                                  'buyer_icp_hypothesis': 'Resolve from private program card'},
                    'dream_tier': 'Unassigned; relationship-level evidence and owner review required',
                    'context_card': f'vault/{sub_note}/{tid}.md',
                    'job': {'mission': f'Research and grow appropriate {name} relationships for the reviewed client program.',
                            'business_brief': f"Type {tid}: {item['what']}. Apply client-specific offer, buyer ICP and authority. {opportunity}",
                            'success_criteria': 'Supported identities and fit; sourced opportunity brief, fresh relationship context, owner and next action. No invented outcome.',
                            'authority': AUTHORITY, 'timezone': 'America/New_York', 'start_hour': 9,
                            'hours_per_day': 8, 'weekdays': [0, 1, 2, 3, 4], 'child_limit': 0},
                    'source': document['source_url'],
                }
                profiles.append(profile)
                outputs[f'profiles/{tid}.json'] = json.dumps(profile, ensure_ascii=False, indent=2) + '\n'
                sub_lines.append(f'- [[{tid}|{name}]]')
                index.append(f'- **{tid} {name}** — {item["what"]}; reference model: {item["pay"]}.')
                dossier = [f'---\ntype_id: {tid}\nfamily_id: {fid}\nsubcategory_id: {sid}\nstatus: generated_seed\n---',
                           f'# {tid} {name}', '', f'Parent: [[{sid}]] · Family: [[{fid}]] · Program: [[PROGRAM-TEMPLATE]]',
                           '', '## Role and partner avatar', profile['job']['mission'], '', avatar,
                           '', '## Buyer ICP', profile['customer_icp'],
                           '', '## Lead opportunity hypothesis', opportunity,
                           '', '## Discovery sources', *['- ' + s for s in SOURCES[fid]],
                           '', '## Research queries', *['- `' + q + '`' for q in profile['lead_opportunities'][0]['queries']],
                           '', '## Fit evidence', *['- ' + e for e in profile['lead_opportunities'][0]['evidence_required']],
                           '', '## Commercial model', item['pay'] + ' — reference only, not approved program terms.',
                           '', '## Client application', status + ': ' + reason,
                           '', '## Before activation', 'Complete client-specific dossier review, sources, mutual-value idea and disqualifiers. Read the real relationship card before any draft. Dream tiers are relationship-level. This note is not a real lead.',
                           '', '## Governance', AUTHORITY,
                           '', '## Source', document['source_url'], '']
                outputs[f'vault/{sub_note}/{tid}.md'] = '\n'.join(dossier)
                # Runtime-compatible source path expected by pinned relcore.taxonomy.
                runtime_note = f'F{int(fid[1:]):02d}-reference/{sid}-reference/{tid}-reference.md'
                outputs[f'knowledge/30-Families/{runtime_note}'] = '\n'.join(dossier) + '\n## Why they say yes\nHypothesis: ' + MOTIONS[fid] + '\n\n## Fit signals\n' + '; '.join(profile['qualification']['facts']) + '\n\n## Disqualifiers\n' + '; '.join(profile['qualification']['exclusions']) + '\n\n## Objections\nUnknown; record actual partner evidence.\n'

            outputs[f'vault/{sub_note}.md'] = '\n'.join(sub_lines) + '\n'
            index.append('')
        outputs[f'vault/{family_note}.md'] = '\n'.join(note) + '\n'
    registry = {'schema_version': 1, 'status': 'design_only', 'counts': {'families': 11, 'subcategories': 67, 'profiles': 339},
                'profiles': profiles}
    outputs['catalog/profiles.json'] = json.dumps(registry, ensure_ascii=False, indent=2) + '\n'
    outputs['TAXONOMY.md'] = '\n'.join(index).rstrip() + '\n'
    outputs['explorer.html'] = render_explorer(registry)
    outputs['catalog/generated-manifest.json'] = json.dumps({name: hashlib.sha256(text.encode()).hexdigest()
                                                            for name, text in outputs.items()}, indent=2) + '\n'
    return outputs


def render_explorer(registry):
    # Local-only JSON; no dependencies, forms, credentials, network requests or actual prospects.
    data = json.dumps(registry, ensure_ascii=False).replace('<', '\\u003c')
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Revenue Partnerships Growth System</title><style>
*{box-sizing:border-box}body{margin:0;background:#f6f5f0;color:#18231f;font:15px system-ui,sans-serif}header{padding:30px 5vw;background:#19392d;color:#fff}.label{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:#b9d7a0}h1{font-size:clamp(28px,4vw,44px);margin:8px 0 12px;max-width:900px}header p{max-width:850px;line-height:1.55;color:#dce8dc}.counts{display:flex;gap:35px;margin-top:20px}.counts b{font-size:30px}.counts span{display:block;font-size:12px;color:#c8d6c8}.flow{display:flex;flex-wrap:wrap;gap:7px;padding:20px 5vw;background:#e6ecdf}.flow span{padding:7px 12px;border-radius:6px;background:white}main{padding:24px 5vw}.controls{display:flex;gap:12px;flex-wrap:wrap}input,select{padding:11px;border:1px solid #bccaba;border-radius:7px;background:white;max-width:100%}input{flex:1;min-width:210px}#summary{margin:14px 0;color:#576256}.layout{display:grid;grid-template-columns:minmax(270px,1fr) minmax(320px,1.8fr);gap:20px}.list{max-height:650px;overflow:auto}.row{display:block;width:100%;text-align:left;background:white;border:1px solid #dbe1d6;padding:13px;margin:0 0 7px;border-radius:9px;color:inherit;cursor:pointer}.row:hover,.row.active{border-color:#457445;background:#eef4e8}.id{font-size:11px;color:#617660}.row strong{display:block;margin:5px 0}.row small{color:#697568}.detail{background:white;border:1px solid #dbe1d6;border-radius:12px;padding:26px;align-self:start;line-height:1.6}.detail h2{margin-top:6px}.detail h3{font-size:14px;color:#2b6347;margin:20px 0 5px}.badge{font-size:11px;background:#eaf1df;border-radius:20px;padding:5px 10px}ul{padding-left:20px}.notice{padding:13px;background:#faf4e4;font-size:13px;border-radius:8px;margin-top:22px}footer{padding:20px 5vw;color:#626d60;font-size:12px}@media(max-width:760px){.layout{grid-template-columns:1fr}.list{max-height:350px}.counts{gap:20px}}
</style><header><div class="label">Demand generation flagship · design package</div><h1>One growth director.<br>A complete partner opportunity map.</h1><p>Affiliate and partner growth, grounded in relationship context. A reusable service system, applied first to each client business.</p><div class="counts"><div><b>11</b><span>partner families</span></div><div><b>67</b><span>subcategories</span></div><div><b>339</b><span>type profiles</span></div><div><b>0</b><span>active workers by default</span></div></div></header>
<div class="flow"><span>Program & buyer ICP</span> → <span>Partner type</span> → <span>Real relationship card</span> → <span>Opportunity & activation</span> → <span>Verified outcome</span></div>
<main><div class="controls"><input id="q" placeholder="Search partner types, avatars or opportunities" aria-label="Search partner types"><select id="family" aria-label="Partner family"><option value="">All families</option></select><select id="scope" aria-label="Application scope"><option value="all">All 339 definitions</option><option value="pilot">Reviewed client lanes</option></select></div><div id="summary"></div><div class="layout"><div id="list" class="list"></div><article id="detail" class="detail"></article></div></main>
<footer>Generated seeds, not live employees or verified leads. Research hypotheses require dossier review. Dream 100/500 are relationship tiers; Attio and ClickUp remain sole-writer roles. No runtime or outreach was activated.</footer>
<script id="data" type="application/json">''' + data + '''</script><script>
const P=JSON.parse(document.getElementById('data').textContent).profiles;const el=id=>document.getElementById(id);const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));let selected=P[0].type_id;
for(const [id,name] of new Map(P.map(p=>[p.family_id,p.family]))){const o=document.createElement('option');o.value=id;o.textContent=id+' · '+name;el('family').append(o)}
function detail(p){const opp=p.lead_opportunities[0];el('detail').innerHTML='<span class="badge">'+esc(p.type_id)+' · '+esc(p.application.status)+'</span><h2>'+esc(p.name)+'</h2><p>'+esc(p.definition)+'</p><h3>Partner avatar</h3><p>'+esc(p.avatar)+'</p><h3>Opportunity to investigate</h3><p>'+esc(opp.hypothesis)+'</p><h3>Where to find candidates</h3><ul>'+opp.sources.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><h3>Queries to apply to a client</h3><ul>'+opp.queries.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><h3>Client application</h3><p>'+esc(p.application.reason)+'</p><h3>Evidence before qualification</h3><ul>'+opp.evidence_required.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><div class="notice">Commercial reference: '+esc(p.commercial_model_reference)+'. Actual terms require the client owner. This is a generated dossier seed, not a researched person or an approved worker.</div>'}
function render(){const q=el('q').value.toLowerCase(),f=el('family').value,pilot=el('scope').value==='pilot';const rows=P.filter(p=>(!f||p.family_id===f)&&(!pilot||p.application.status==='research_candidate')&&JSON.stringify(p).toLowerCase().includes(q));el('summary').textContent=rows.length+' profiles · profiles activate only after client and dossier review';if(!rows.some(p=>p.type_id===selected))selected=rows[0]?.type_id;el('list').replaceChildren();for(const p of rows){const b=document.createElement('button');b.className='row'+(p.type_id===selected?' active':'');b.innerHTML='<span class="id">'+esc(p.type_id)+' · '+esc(p.family)+'</span><strong>'+esc(p.name)+'</strong><small>'+esc(p.subcategory)+'</small>';b.onclick=()=>{selected=p.type_id;render()};el('list').append(b)}if(rows.length)detail(rows.find(p=>p.type_id===selected));else el('detail').textContent='No profiles match. Change the filters.'}
for(const id of ['q','family','scope'])el(id).addEventListener('input',render);render();</script></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = build(load_taxonomy(ROOT / 'catalog/taxonomy.json'))
    errors = []
    for relative, text in outputs.items():
        target = ROOT / relative
        if args.check:
            if not target.exists() or target.read_text() != text:
                errors.append(relative)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
    expected_profiles = {name for name in outputs if name.startswith('profiles/')}
    found_profiles = {str(p.relative_to(ROOT)) for p in (ROOT / 'profiles').glob('*.json')}
    errors.extend(sorted(found_profiles - expected_profiles))
    if errors:
        raise SystemExit('Missing, stale or unexpected generated artifacts: ' + ', '.join(errors))
    print('Validated 11 families, 67 subcategories, 339 disabled profiles and their context notes; no live activation.')


if __name__ == '__main__':
    main()
