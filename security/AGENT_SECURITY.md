# Agent Security

## Files Agents Should Not Edit Without Approval

- `.env`
- `.github/workflows/*`
- `infra/*`
- Security policy files.
- Files containing credentials or customer data.

## Prompt Rules

- Do not paste secrets into prompts.
- Do not ask agents to bypass tests, reviews, or security checks.
- Do not let agents invent validation results.
- Ask agents to report exact commands run.

## Review Rules

- Review every agent-generated diff.
- Check for unexpected file changes.
- Check for hidden network calls or new dependencies.
- Run validation commands before merge.
