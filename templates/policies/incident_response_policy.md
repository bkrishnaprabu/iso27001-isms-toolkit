# Incident Response Policy

**Document Reference:** ISMS-POL-005  
**Version:** 2.0  
**Classification:** Internal  
**Owner:** IT Manager / CISO  
**Review Cycle:** Annual  
**Last Reviewed:** [DATE]

---

## 1. Purpose

To ensure a consistent, effective, and timely response to information security incidents, minimising business impact and supporting post-incident learning.

---

## 2. Scope

Applies to all employees, contractors, and third parties. Covers all systems, networks, and data processed by [Organisation Name].

---

## 3. Incident Classification

| Severity | Description | Examples | Response Time |
|----------|-------------|----------|---------------|
| P1 — Critical | Major breach; significant business impact | Ransomware, data breach of PII | Immediate (< 1 hr) |
| P2 — High | Significant disruption; potential for escalation | Malware infection, privilege escalation | < 4 hours |
| P3 — Medium | Limited impact; no immediate data risk | Phishing attempt, policy violation | < 24 hours |
| P4 — Low | Minimal impact; informational | Failed login attempts, spam | < 72 hours |

---

## 4. Incident Response Phases

### Phase 1 — Detection & Reporting
- Any staff member suspecting an incident must report immediately to the IT Manager or Security team
- Reporting channels: IT helpdesk ticket, email security@[org].com, phone [NUMBER]

### Phase 2 — Containment
- Isolate affected systems to prevent spread
- Preserve evidence (do not power off unless directed)
- Revoke compromised credentials

### Phase 3 — Eradication
- Remove malware / threat actors
- Patch exploited vulnerabilities
- Reset all potentially compromised credentials

### Phase 4 — Recovery
- Restore systems from verified clean backups
- Monitor for re-infection
- Validate system integrity before returning to production

### Phase 5 — Post-Incident Review
- Conduct post-incident review within 5 business days
- Document lessons learned and remediation actions
- Update incident register and risk register

---

## 5. Regulatory Notification Requirements

| Regulation | Notification Threshold | Deadline |
|-----------|----------------------|----------|
| UAE PDPL | Breach affecting personal data | 72 hours to regulator |
| ISO 27001 | All significant incidents | Internal record within 24 hrs |
| Contractual | Per client agreements | Per SLA terms |

---

## 6. Evidence Preservation

- All logs, system images, and communications related to the incident must be preserved
- Chain of custody must be maintained if legal action is anticipated
- Evidence storage: [encrypted, access-controlled location]

---

*Review annually or after any P1/P2 incident.*
