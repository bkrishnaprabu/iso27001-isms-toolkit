#!/usr/bin/env python3
"""ISO 27001:2022 Gap Analysis Tool — Krishnaprabu Balasubramanian"""
import argparse, os, json
from datetime import datetime

CONTROLS = [
    ("5.1","Org","Policies for information security","IS policy reviewed and communicated"),
    ("5.2","Org","Information security roles","Roles and responsibilities defined"),
    ("5.14","Org","Information transfer","Data classification and transfer controls"),
    ("5.19","Org","Supplier relationships","Vendor assessment and TPCRM"),
    ("6.1","People","Screening","Background checks for all staff"),
    ("6.3","People","Security awareness","Regular training and phishing simulations"),
    ("7.1","Physical","Physical security perimeters","Access controls for facilities"),
    ("7.4","Physical","Physical security monitoring","CCTV and security monitoring"),
    ("8.2","Tech","Privileged access rights","Privileged accounts review and PAM"),
    ("8.5","Tech","Secure authentication","MFA and strong authentication"),
    ("8.7","Tech","Protection against malware","Endpoint protection deployment"),
    ("8.8","Tech","Vulnerability management","Automated scanning and patching"),
    ("8.12","Tech","Data leakage prevention","DLP controls and monitoring"),
    ("8.15","Tech","Logging","SIEM and log management"),
    ("8.24","Tech","Use of cryptography","Encryption at rest and in transit"),
    ("8.28","Tech","Secure coding","DevSecOps and SAST/DAST scanning"),
]

def assess_interactive(org):
    scores = {}
    print(f"\n📋 ISO 27001:2022 Gap Analysis — {org}")
    print("Rate each control 0 (Not Implemented) to 5 (Fully Implemented)\n")
    for ctrl_id, domain, title, desc in CONTROLS:
        print(f"[{ctrl_id}] {title}")
        print(f"  {desc}")
        while True:
            try:
                score = int(input("  Score (0-5): "))
                if 0 <= score <= 5:
                    scores[ctrl_id] = score; break
            except (ValueError, KeyboardInterrupt):
                print("  Skipping...")
                scores[ctrl_id] = 0; break
    return scores

def generate_report(scores, org, output_dir):
    total = len(scores)
    avg = sum(scores.values()) / total if total > 0 else 0
    pct = (avg / 5) * 100
    rows = ""
    for ctrl_id, domain, title, desc in CONTROLS:
        score = scores.get(ctrl_id, 0)
        gap = 5 - score
        status = "Fully Implemented" if score==5 else ("Mostly Implemented" if score>=4 else ("Partially Implemented" if score>=2 else "Not Implemented"))
        color = "#00c896" if score==5 else ("#fbbf24" if score>=3 else "#f87171")
        rows += f"<tr><td>{ctrl_id}</td><td>{domain}</td><td>{title}</td><td style=\"color:{color};font-weight:700\">{score}/5</td><td>{gap}</td><td>{status}</td><td>{desc}</td></tr>"
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Gap Analysis — {org}</title>
<style>body{{font-family:Arial,sans-serif;background:#0a0f1a;color:#e2e8f0;margin:0}}
.hdr{{background:#0d2137;padding:28px 36px;border-bottom:3px solid #00875a}}
.hdr h1{{color:#fff}}.hdr p{{color:#7EC8E3;font-size:.9rem}}
.cnt{{padding:28px 36px}}.score{{font-size:3rem;font-weight:800;color:#00c896}}
table{{width:100%;border-collapse:collapse;font-size:.82rem;margin-top:20px}}
th{{background:#0d2137;color:#fff;padding:9px 12px;text-align:left}}
td{{padding:8px 12px;border-bottom:1px solid rgba(255,255,255,.05)}}
tr:nth-child(odd){{background:rgba(255,255,255,.02)}}</style></head><body>
<div class="hdr"><h1>📊 ISO 27001:2022 Gap Analysis — {org}</h1>
<p>Generated: {datetime.now().strftime("%d %B %Y %H:%M")} · CISA: Krishnaprabu Balasubramanian</p></div>
<div class="cnt">
<p>Overall Compliance Score: <span class="score">{pct:.0f}%</span></p>
<table><thead><tr><th>Control ID</th><th>Domain</th><th>Title</th><th>Maturity</th><th>Gap</th><th>Status</th><th>Description</th></tr></thead>
<tbody>{rows}</tbody></table></div></body></html>"""
    os.makedirs(output_dir, exist_ok=True)
    fname = f"{output_dir}/gap_analysis_{datetime.now().strftime('%Y%m%d')}.html"
    with open(fname,"w",encoding="utf-8") as f: f.write(html)
    print(f"  ✅ Gap Analysis Report: {fname}")
    with open(f"{output_dir}/gap_scores.json","w") as f: json.dump(scores,f,indent=2)
    return fname

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--org", default="Your Organisation")
    ap.add_argument("--output", default="reports")
    ap.add_argument("--demo", action="store_true", help="Use demo scores")
    args = ap.parse_args()
    if args.demo:
        scores = {"5.1":4,"5.2":3,"5.14":2,"5.19":3,"6.1":4,"6.3":2,"7.1":5,"7.4":5,"8.2":3,"8.5":4,"8.7":4,"8.8":2,"8.12":1,"8.15":4,"8.24":4,"8.28":2}
    else:
        scores = assess_interactive(args.org)
    generate_report(scores, args.org, args.output)

if __name__=="__main__": main()
