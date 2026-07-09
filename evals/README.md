# Evals

Use evals to check whether the local-agent workflow still behaves correctly
after prompt, model, parser, or proxy changes.

## First Eval: Promptfoo

The starter config is:

```bash
evals/promptfoo/local-agent-smoke.yaml
```

Run it with:

```bash
make eval-local
```

The command requires `promptfoo` to be installed. If it is not installed, the
script prints the install command and exits without changing anything.

## What To Evaluate

Start with small checks:

- Does the model return the requested format?
- Does it respect non-goals?
- Does it ask for missing context?
- Does it avoid making up validation results?
- Does it keep marketing, sales, QA, and engineering outputs separate?

## Promotion Rule

Do not expand local-agent responsibility until the eval set passes consistently
and human review finds mostly judgment-level issues rather than basic
correctness failures.
