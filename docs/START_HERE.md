# Start Here

This page is for teammates who want to use Zynclaw without setting up servers,
models, Docker, or command-line tools.

## What This Repo Is For

Zynclaw helps the team turn ideas into clear, validated work:

```text
idea -> plan -> agent task -> QA -> launch -> learning
```

The repo gives each team a place to write the important context before work is
handed to an AI agent or an engineer.

## Choose Your Starting Point

| Role | Use This Folder | Best First File |
|------|-----------------|-----------------|
| Product | `product/` | `product/INTAKE.md` |
| Project manager | `project/` | `project/DELIVERY_PLAN.md` |
| Engineer | `engineering/` | `engineering/AGENT_CONTRACT.md` |
| QA | `qa/` | `qa/ACCEPTANCE_CHECKLIST.md` |
| Marketing | `marketing/` | `marketing/POSITIONING.md` |
| Sales | `sales/` | `sales/SALES_PLAYBOOK.md` |

## Easiest Way To Start

Use a GitHub issue form:

1. Go to the repo on GitHub.
2. Click `Issues`.
3. Click `New issue`.
4. Pick the form that matches your need.
5. Fill in the fields.

Good options:

- Product intake
- Local agent task
- Marketing request
- Sales enablement
- QA report

## What Good Input Looks Like

Good requests are specific:

```text
We need a short launch message for engineering managers who want to reduce
manual project-management work. The proof is that our local setup handled
150M+ tokens of internal testing. The call to action is to review the repo and
try the setup checklist.
```

Weak requests are vague:

```text
Make this better.
```

## Before Work Goes To An Agent

Make sure the task includes:

- The goal.
- The audience or user.
- What is in scope.
- What is out of scope.
- Acceptance criteria.
- Who should review it.

## If You Need A Full Work Item

Ask a technical teammate to run:

```bash
make scaffold WORK="short task name"
```

That creates one folder with product, project, engineering, marketing, sales,
QA, and status files.

## Where To Look For Examples

Use `examples/local-agent-setup-work-item/` to see a filled-out task.
