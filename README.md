# ISO 27001:2022 ISMS Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ISO 27001](https://img.shields.io/badge/ISO-27001%3A2022-blue.svg)](https://www.iso.org/standard/27001)
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](https://github.com/krishnaprabu-balasubramanian/iso27001-isms-toolkit)

A **production-ready**, enterprise-grade ISO 27001:2022 ISMS implementation toolkit. Built from real-world experience delivering and maintaining ISO 27001 certification across multi-site, global enterprises.

> ⚡ Used as the foundation for ISO 27001:2022 certification programmes across multiple UAE enterprises. 

---

## 📦 What's Included

```
iso27001-isms-toolkit/
├── templates/
│   ├── policies/           # Ready-to-use ISMS policies
│   ├── procedures/         # Operational procedure templates
│   ├── forms/              # Audit, risk, and review forms
│   └── checklists/         # Gap analysis & audit checklists
├── tools/
│   ├── risk_register.py    # Automated risk scoring & heat maps
│   ├── gap_analysis.py     # Controls gap assessment tool
│   └── soa_generator.py    # Statement of Applicability generator
├── docs/
│   ├── IMPLEMENTATION_GUIDE.md
│   ├── AUDIT_PROGRAMME.md
│   └── CERTIFICATION_ROADMAP.md
└── assets/
    └── control_mapping.json  # ISO 27001:2022 Annex A controls
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/krishnaprabu-balasubramanian/iso27001-isms-toolkit.git
cd iso27001-isms-toolkit
pip install -r requirements.txt
```

### Run Risk Register Tool

```bash
python tools/risk_register.py --input templates/forms/risk_register_template.csv --output reports/
```

### Run Gap Analysis

```bash
python tools/gap_analysis.py --org "Your Organization" --output reports/gap_analysis_report.html
```

### Generate Statement of Applicability

```bash
python tools/soa_generator.py --config config/isms_config.yaml --output reports/soa.html
```

---

## 📋 Policy Templates Included

| Policy | Description |
|--------|-------------|
| Information Security Policy | Top-level ISMS policy |
| Access Control Policy | IAM, least privilege, PAM |
| Asset Management Policy | Information asset classification |
| Incident Response Policy | Detection, response, recovery |
| Business Continuity Policy | BCP/DR framework |
| Cryptography Policy | Encryption standards and key management |
| Physical Security Policy | Facility and equipment controls |
| Supplier Security Policy | Third-party risk management |
| Acceptable Use Policy | Employee IT usage guidelines |
| Data Classification Policy | Sensitivity labelling framework |
| Change Management Policy | Change control and approval |
| Vulnerability Management Policy | Patch and scan management |
| Remote Work Policy | Secure remote access |
| Logging & Monitoring Policy | Audit trail requirements |
| Risk Management Policy | Risk assessment methodology |

---

## 🗂️ ISO 27001:2022 Annex A Controls Coverage

All 93 controls across 4 themes are mapped:

- **Organisational Controls** (37 controls) — Policies, roles, supplier relations
- **People Controls** (8 controls) — Awareness, training, disciplinary
- **Physical Controls** (14 controls) — Perimeter, equipment, clean desk
- **Technological Controls** (34 controls) — Authentication, encryption, monitoring

---

## 📊 Risk Register Tool

The automated risk register scores risks using:

```
Risk Score = Likelihood (1-5) × Impact (1-5)
```

| Score | Rating | Action Required |
|-------|--------|----------------|
| 1–4   | Low    | Accept / Monitor |
| 5–9   | Medium | Treat / Transfer |
| 10–16 | High   | Immediate Treatment |
| 17–25 | Critical | Escalate to Board |

Generates:
- Excel risk register with conditional formatting
- HTML heat map visualisation
- Management summary PDF

---

## 🏗️ ISMS Implementation Roadmap

```
Phase 1: Context & Scope (Weeks 1–2)
  └── Clause 4: Understand organisation context
  └── Define ISMS scope and boundaries

Phase 2: Leadership & Planning (Weeks 3–4)
  └── Clause 5: Management commitment
  └── Clause 6: Risk assessment methodology

Phase 3: Risk Assessment (Weeks 5–6)
  └── Asset inventory and classification
  └── Threat and vulnerability identification
  └── Risk scoring and treatment plan

Phase 4: Controls Implementation (Weeks 7–12)
  └── Annex A controls selection
  └── Statement of Applicability
  └── Policy and procedure development

Phase 5: Awareness & Training (Week 13)
  └── Staff security awareness programme
  └── Role-based training delivery

Phase 6: Internal Audit (Week 14–15)
  └── Internal audit programme execution
  └── Non-conformity management

Phase 7: Management Review (Week 16)
  └── ISMS performance review
  └── Continual improvement actions

Phase 8: Certification Audit (Weeks 17–20)
  └── Stage 1: Documentation review
  └── Stage 2: On-site certification audit
```

---

## 🔒 Compliance Alignment

This toolkit supports alignment with:

- **ISO 27001:2022** — Primary standard
- **ISO 27002:2022** — Implementation guidance
- **NIST CSF 2.0** — Cross-mapped controls
- **UAE NESA** — Regulatory overlay
- **CIS Controls v8** — Technical hardening baseline
- **GDPR / UAE PDPL** — Data protection requirements

---

## 📁 Usage in Enterprise Environments

### Multi-site Deployments
- Scope definition templates for distributed organisations
- Site-specific risk registers with consolidated reporting
- Remote audit evidence collection procedures

### Integration with GRC Platforms
- Export formats compatible with ServiceNow GRC, Archer, and OneTrust
- CSV/JSON data interchange for bulk import

---

## 🤝 Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-new-policy`
3. Commit changes: `git commit -m 'Add supplier security policy template'`
4. Push: `git push origin feature/add-new-policy`
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Krishnaprabu Balasubramanian**  
IT Manager | Cybersecurity & GRC | ISO 27001 Lead Auditor | CISA  
📍 Abu Dhabi, UAE  
📧 bkrishnaprabu@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/krishnaprabubalasubramanian)

---

## ⭐ If this toolkit helped you achieve ISO 27001 certification, please star the repository!
