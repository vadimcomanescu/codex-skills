---
name: security-compliance
description: Security and compliance workflow for designing defense-in-depth controls, performing threat modeling and risk assessments, and mapping mitigations to frameworks (SOC2/ISO27001/GDPR/HIPAA). Use when reviewing security posture, shipping sensitive features, preparing compliance evidence, or running a lightweight secrets scan.
---

# Security & Compliance

Build real security, not checkbox security.

## Quick Start
1) Scope the system and data:
   - What data types exist (PII/PHI/payment/secrets)? Where is it stored and transmitted?
   - Trust boundaries (browser ↔ edge ↔ API ↔ DB ↔ 3rd parties)
2) Threat model (lightweight): list top 5 abuse cases + mitigations.
3) Controls: pick practical controls (authN/authZ, encryption, logging, rate limits, backups, key mgmt).
4) Evidence: document decisions and “how we know it works” (configs, screenshots, logs, tests).

## Optional tool: scan for likely secrets in a repo
```bash
python ~/.codex/skills/security-compliance/scripts/secret_scan.py . --json --output /tmp/secrets.json
```

## References
- Threat model template: `references/threat-model.md`
- Control checklist: `references/control-checklist.md`

