# Zynclaw

Zynclaw is a team operating kit for using local AI agents safely across product,
project management, engineering, QA, marketing, and sales.

You can use this repo in two ways:

- Non-technical teammates can use the folders, checklists, and GitHub issue
  forms to describe work clearly.
- Technical teammates can run the local inference stack, validation harness, and
  agent workflow.

The main idea is simple: local agents should get clear tasks, use the right
tools, pass validation, and stay inside a human-reviewed workflow.

## Start Here

If you do not want to run anything locally, start here:

1. Open [docs/START_HERE.md](docs/START_HERE.md).
2. Pick the folder that matches your role:
   - `product/` for ideas, requirements, metrics, and acceptance criteria.
   - `project/` for owners, milestones, risks, status, and backlog.
   - `marketing/` for positioning, campaigns, content, channels, and launch.
   - `sales/` for ICP, talk tracks, demos, outreach, and objections.
   - `qa/` for acceptance checks, release checks, and validation notes.
3. Create a GitHub issue using one of the issue forms:
   - Product intake
   - Local agent task
   - Marketing request
   - Sales enablement
   - QA report

You do not need Docker, Python, NVIDIA hardware, or command-line tools to use
the planning and handoff parts of this repo.

## Team Workflow

```text
product -> project -> engineering -> qa -> marketing/sales -> release -> learning
```

- `product/` captures the problem, requirements, non-goals, and metrics.
- `project/` turns product intent into owners, milestones, risks, and status.
- `engineering/` defines the agent execution contract and review checklist.
- `qa/` defines acceptance, evals, regression checks, and release gates.
- `marketing/` defines positioning, campaigns, content, channels, and launch
  assets.
- `sales/` defines ICP, talk tracks, demos, outreach, qualification, and
  objection handling.
- `templates/` and `work-items/` keep real tasks organized end to end.
- `prompts/` contains reusable prompts for product, engineering, QA, marketing,
  and sales agents.
- `examples/` shows a filled work item so the team can copy the pattern.

For the full workflow, see [docs/END_TO_END.md](docs/END_TO_END.md).

## Common First Actions

| I want to... | Start with |
|--------------|------------|
| Capture a new idea | `product/INTAKE.md` or the Product intake issue form |
| Plan delivery | `project/DELIVERY_PLAN.md` |
| Hand work to an agent | `engineering/AGENT_CONTRACT.md` or the Local agent task issue form |
| Validate a change | `qa/ACCEPTANCE_CHECKLIST.md` |
| Prepare launch messaging | `marketing/POSITIONING.md` |
| Prepare sales handoff | `sales/SALES_PLAYBOOK.md` |
| See a filled example | `examples/local-agent-setup-work-item/` |

## Technical Setup

Technical teammates who want to run the local model stack should use this path:

```bash
git clone https://github.com/cgautamdevc14/zynclaw.git
cd zynclaw
make setup
```

Then:

```bash
make install-litellm
make build-vllm
make start-vllm
```

Start LiteLLM in a second terminal:

```bash
make litellm
```

Check the setup:

```bash
make doctor
make endpoint-probe
make acceptance
```

For the detailed technical guide, see [docs/SETUP.md](docs/SETUP.md).

## Technical Stack

- NVIDIA inference host capable of serving the model.
- Qwen3.6-27B-FP8 served through vLLM.
- LiteLLM as an OpenAI-compatible proxy, parameter normalizer, and monitoring
  point.
- Agent clients pointed at LiteLLM.
- Validation scripts that check readiness, structured tool calls, and endpoint
  health.

## Repository Layout

```text
.
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- workflows/
|-- docs/
|-- engineering/
|-- examples/
|-- marketing/
|-- observability/
|-- product/
|-- project/
|-- prompts/
|-- qa/
|-- sales/
|-- infra/
|-- scripts/
|-- templates/
|-- work-items/
|-- .env.example
|-- LICENSE
`-- Makefile
```

## Make Targets

```text
make setup            Create .env and check the local machine.
make setup-all        Install LiteLLM, build vLLM, and start vLLM.
make doctor           Diagnose prerequisites and endpoint reachability.
make install-litellm  Install LiteLLM into .venv.
make build-vllm       Build the patched vLLM image.
make start-vllm       Start the vLLM compose service.
make logs-vllm        Follow vLLM logs.
make litellm          Start LiteLLM in the foreground.
make acceptance       Validate structured tool-call behavior.
make endpoint-probe   Probe LiteLLM and vLLM health, models, and metrics.
make gpu-preflight    Verify host and container GPU access.
make scaffold         Create a full work-item folder.
make repo-check       Validate repo structure and local Markdown links.
```

## Work Items

Technical users can create a complete work item folder with:

```bash
make scaffold WORK="improve onboarding flow"
```

That creates product, project, engineering, marketing, sales, QA, and status
files under `work-items/`.

## Validation

Before assigning real work to a local agent:

- `make doctor`
- `make endpoint-probe`
- `make acceptance`

Before shipping changes:

- Human review is complete.
- QA checklist is complete.
- Validation commands pass or failures are documented.
- Marketing and sales handoff is complete when the change is user-facing.

## License

MIT
