# 🛡 ISO 27001:2022 ISMS Toolkit

**Production-ready toolkit for ISO 27001:2022 implementation, gap analysis, and risk management.**

![ISO 27001](https://img.shields.io/badge/ISO-27001:2022-00875A?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🎯 What This Does

| Tool | Purpose | Output |
|------|---------|--------|
| `tools/risk_register.py` | Score, rate, and report IT risks (L×I matrix) | HTML report + Excel workbook |
| `tools/gap_analysis.py` | Assess all 93 ISO 27001:2022 Annex A controls | HTML compliance report |
| `templates/policies/` | Ready-to-use policy templates | Word documents |
| `reports/iso27001_isms_workbook.xlsx` | Full Excel risk register with formulas | Multi-sheet workbook |

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/iso27001-isms-toolkit.git
cd iso27001-isms-toolkit
pip install -r requirements.txt

# Demo mode — see output immediately
python tools/gap_analysis.py --demo --org "Acme UAE LLC"
python tools/risk_register.py --org "Acme UAE LLC"
```

## 📁 Project Structure

```
iso27001-isms-toolkit/
├── tools/
│   ├── risk_register.py       # Risk scoring and HTML report generator
│   └── gap_analysis.py        # ISO 27001:2022 control assessment
├── templates/
│   └── policies/
│       ├── information_security_policy.md
│       └── incident_response_policy.md
├── reports/
│   ├── iso27001_isms_workbook.xlsx  # Pre-built Excel workbook
│   └── isms_report.html             # Sample HTML report
├── data/
│   └── sample_risks.csv             # Template risk data
└── docs/
    └── user_guide.md                # Detailed usage guide
```

## 📊 XLSX Workbook Contents

The pre-built Excel workbook (`reports/iso27001_isms_workbook.xlsx`) contains:
- **Risk Register** — 10 sample risks with inherent/residual scoring formulas
- **ISO 27001 Gap Analysis** — 18 key controls with maturity ratings
- **Dashboard** — Executive KPI summary with live formulas

## 🏢 Real-World Use Cases

- ISO 27001 certification engagements (gap to certified)
- Quarterly risk committee reporting
- Management board risk dashboards
- Internal audit evidence packages
- Client security assessments

## 📋 Input CSV Format

```csv
risk_id,category,title,asset,likelihood,impact,treatment,owner,due_date,status
R-001,Cybersecurity,Phishing Attack,Email System,4,5,Deploy Defender for O365,IT Security,2025-03-31,Open
```

## 🔧 Requirements

```
openpyxl>=3.1.0
jinja2>=3.1.0
```

## 👤 Author

**Krishnaprabu Balasubramanian** | CISA · ISO 27001 Lead Auditor | Abu Dhabi, UAE
[LinkedIn](https://linkedin.com/in/krishnaprabubalasubramanian) · bkrishnaprabu@gmail.com
