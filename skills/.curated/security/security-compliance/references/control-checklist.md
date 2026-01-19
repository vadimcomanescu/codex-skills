# Control Checklist (pragmatic)

## Identity and access
- Strong auth (SSO/MFA where appropriate)
- Authorization is enforced server-side
- Least privilege roles; audit privileged actions

## Data protection
- Encrypt in transit (TLS) and at rest (where feasible)
- Secrets in a secret manager (not in repos/CI logs)
- Data retention + deletion policy (especially for PII/PHI)

## Application security
- Input validation and output encoding
- Rate limiting and abuse controls
- Dependency hygiene (updates, lockfiles, SBOM if needed)

## Operations
- Centralized logging with correlation IDs
- Monitoring + alerting on auth anomalies and error spikes
- Backups + tested restores; incident response plan

