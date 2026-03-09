#!/usr/bin/env python3
"""ISO 27001:2022 Risk Register Tool — Krishnaprabu Balasubramanian"""
import csv, json, argparse, os
from datetime import datetime
from pathlib import Path

def load_risks(filepath=None):
    if filepath and Path(filepath).exists():
        with open(filepath) as f:
            return list(csv.DictReader(f))
    return [
        {"risk_id":"R-001","category":"Cybersecurity","title":"Phishing / BEC Attack","asset":"Email System","likelihood":"4","impact":"5","treatment":"Implement Defender for O365 + Awareness Training","owner":"IT Security","due_date":"2025-03-31","status":"Open"},
        {"risk_id":"R-002","category":"Cloud Security","title":"Cloud Misconfiguration","asset":"Azure Subscriptions","likelihood":"3","impact":"4","treatment":"Enable Defender for Storage + Azure Policy","owner":"Cloud Team","due_date":"2025-04-15","status":"In Progress"},
        {"risk_id":"R-003","category":"Access Control","title":"Privilege Escalation","asset":"Active Directory","likelihood":"3","impact":"5","treatment":"Deploy PAM solution + tiered admin model","owner":"IT Admin","due_date":"2025-05-01","status":"Open"},
        {"risk_id":"R-004","category":"Data Protection","title":"Ransomware Attack","asset":"Customer Database","likelihood":"4","impact":"5","treatment":"Immutable backup vault + network segmentation","owner":"IT Manager","due_date":"2025-03-15","status":"Open"},
        {"risk_id":"R-005","category":"Compliance","title":"Audit Non-Conformity","asset":"ISMS Documentation","likelihood":"2","impact":"4","treatment":"Complete SoA + schedule internal audit","owner":"ISMS Lead","due_date":"2025-04-30","status":"In Progress"},
    ]

def score_risk(likelihood, impact):
    s = int(likelihood) * int(impact)
    if s >= 20: return s, "Critical"
    if s >= 12: return s, "High"
    if s >= 6:  return s, "Medium"
    return s, "Low"

def generate_html_report(risks, org, output_dir):
    rows = ""
    for r in risks:
        score, rating = score_risk(r["likelihood"], r["impact"])
        badge = rating.lower()
        rows += f"""<tr>
            <td>{r['risk_id']}</td><td>{r['category']}</td><td>{r['title']}</td>
            <td>{r['asset']}</td><td>{r['likelihood']}</td><td>{r['impact']}</td>
            <td><b>{score}</b></td><td><span class="badge {badge}">{rating}</span></td>
            <td>{r['treatment']}</td><td>{r['owner']}</td>
            <td><span class="badge {r['status'].lower().replace(' ','')}">{r['status']}</span></td>
            <td>{r['due_date']}</td></tr>"""
    total = len(risks)
    critical = sum(1 for r in risks if score_risk(r["likelihood"],r["impact"])[1]=="Critical")
    high = sum(1 for r in risks if score_risk(r["likelihood"],r["impact"])[1]=="High")
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Risk Register — {org}</title>
<style>
body{{font-family:Arial,sans-serif;background:#0a0f1a;color:#e2e8f0;margin:0}}
.hdr{{background:#0d2137;padding:28px 36px;border-bottom:3px solid #00875a}}
.hdr h1{{color:#fff;margin-bottom:4px}}.hdr p{{color:#7EC8E3;font-size:.9rem}}
.cnt{{padding:28px 36px;max-width:1400px;margin:0 auto}}
.kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:28px}}
.kpi{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:18px}}
.kpi .v{{font-size:2rem;font-weight:800;color:#00c896}}.kpi .l{{font-size:.75rem;color:#64748b;text-transform:uppercase}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}
th{{background:#0d2137;color:#fff;padding:9px 12px;text-align:left}}
td{{padding:8px 12px;border-bottom:1px solid rgba(255,255,255,.05)}}
tr:nth-child(odd){{background:rgba(255,255,255,.02)}}
.badge{{padding:2px 8px;border-radius:8px;font-size:.7rem;font-weight:600}}
.critical{{background:rgba(153,27,27,.3);color:#fca5a5}}
.high{{background:rgba(146,64,14,.3);color:#fbbf24}}
.medium{{background:rgba(91,33,182,.25);color:#c4b5fd}}
.low{{background:rgba(5,150,105,.2);color:#6ee7b7}}
.open{{background:rgba(239,68,68,.2);color:#fca5a5}}
.inprogress{{background:rgba(245,158,11,.2);color:#fbbf24}}
.closed{{background:rgba(16,185,129,.2);color:#6ee7b7}}
</style></head><body>
<div class="hdr"><h1>🛡 IT Risk Register — {org}</h1>
<p>ISO 27001:2022 · Generated: {datetime.now().strftime("%d %B %Y %H:%M")} · CISA: Krishnaprabu Balasubramanian</p></div>
<div class="cnt">
<div class="kpis">
  <div class="kpi"><div class="l">Total Risks</div><div class="v">{total}</div></div>
  <div class="kpi"><div class="l">Critical</div><div class="v" style="color:#f87171">{critical}</div></div>
  <div class="kpi"><div class="l">High</div><div class="v" style="color:#fbbf24">{high}</div></div>
  <div class="kpi"><div class="l">Open Items</div><div class="v" style="color:#fbbf24">{sum(1 for r in risks if r['status']=='Open')}</div></div>
</div>
<table><thead><tr><th>Risk ID</th><th>Category</th><th>Title</th><th>Asset</th>
<th>Likelihood</th><th>Impact</th><th>Score</th><th>Rating</th>
<th>Treatment</th><th>Owner</th><th>Status</th><th>Due Date</th></tr></thead>
<tbody>{rows}</tbody></table></div></body></html>"""
    os.makedirs(output_dir, exist_ok=True)
    fname = f"{output_dir}/risk_register_{datetime.now().strftime('%Y%m%d')}.html"
    with open(fname,"w",encoding="utf-8") as f: f.write(html)
    print(f"  ✅ Report saved: {fname}")
    return fname

def main():
    ap = argparse.ArgumentParser(description="ISO 27001 Risk Register Tool")
    ap.add_argument("--org", default="Your Organisation", help="Organisation name")
    ap.add_argument("--input", help="CSV file with risk data")
    ap.add_argument("--output", default="reports", help="Output folder")
    args = ap.parse_args()
    risks = load_risks(args.input)
    print(f"\n🛡 ISO 27001 Risk Register — {args.org}")
    print(f"   Loaded {len(risks)} risks")
    generate_html_report(risks, args.org, args.output)
    print("\n✅ Done. Open the HTML report in any browser.")

if __name__=="__main__": main()
