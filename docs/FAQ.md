# FAQ

## Do I need to run the local model stack to use this repo?

No. Most teammates can use the templates, checklists, and GitHub issue forms
without running anything locally.

## What should non-technical teammates read first?

Start with [START_HERE.md](START_HERE.md).

## What makes a task safe for a local agent?

The task should have a clear objective, limited scope, explicit non-goals,
acceptance criteria, validation commands, and a human reviewer.

## Can agents make product decisions?

No. Agents can draft options and summarize tradeoffs, but humans own product,
release, and customer-facing decisions.

## When should marketing or sales be involved?

When a change affects users, customers, launch messaging, demos, objection
handling, or sales follow-up.

## What happens if validation fails?

Document the exact command, summarize the failure, and do not treat the work as
done until a human owner decides the next step.

## What technology should we add next?

Start with `promptfoo` for evals if you are changing prompts, models, or agent
instructions. Use [technology/TECHNOLOGY_ROADMAP.md](../technology/TECHNOLOGY_ROADMAP.md)
for the rest.

## How do we connect Slack, GitHub, Notion, Jira, HubSpot, or other tools?

Start with [connections/QUICK_START.md](../connections/QUICK_START.md). Use
`make connections-list` to see supported connection options and
`make connections-check` to see which environment variables are configured.
