# Secrets

## Rules

- Never commit real API keys, tokens, passwords, private keys, or customer data.
- Use `.env` for local values and keep `.env` ignored by Git.
- Keep `.env.example` safe with fake local placeholders only.
- Rotate any credential that appears in a prompt, log, issue, or commit.

## Local Scan

Install `gitleaks`, then run:

```bash
gitleaks detect --source . --redact
```

GitHub Actions also runs a secret scan on pushes and pull requests.

## If A Secret Leaks

1. Revoke or rotate the credential.
2. Remove it from the current branch.
3. Treat old commits as compromised.
4. Document what happened and how it was fixed.
