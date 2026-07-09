# Supply Chain

## GitHub Actions

- Prefer official actions.
- Pin actions to stable versions or SHAs for sensitive workflows.
- Keep workflow permissions minimal.
- Review any workflow change as security-sensitive.

## Containers

- Scan container images before broad rollout.
- Keep base images current.
- Avoid embedding credentials in images.

## Dependencies

- Add dependencies only when they solve a clear problem.
- Prefer tools with active maintainers and clear documentation.
- Remove unused dependencies.

## Optional Tools

- OpenSSF Scorecard for repository security posture.
- Trivy for filesystem, dependency, and container scanning.
- Semgrep for static analysis when application code grows.
