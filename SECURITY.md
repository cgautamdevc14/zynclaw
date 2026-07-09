# Security Policy

## Reporting

Do not open a public issue for secrets, credential exposure, or sensitive
security concerns. Contact the repository owner directly and include:

- What you found.
- Where you found it.
- Whether any credential, token, or private data may be exposed.
- Suggested remediation if known.

## Supported Scope

This repository currently contains templates, local setup scripts, example
configuration, and workflow guidance. Production deployments should perform
their own infrastructure and security review before rollout.

## Immediate Response For Leaked Secrets

1. Revoke or rotate the exposed credential.
2. Remove it from the active branch.
3. Treat prior commits and logs as compromised.
4. Document the fix in `security/SECRETS.md` or a private incident note.
