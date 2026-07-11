# Context Packs

Context packs are compact Markdown bundles that can be handed to a local agent
or teammate before they work on a task.

Generate one with:

```bash
make context ROLE=engineering
```

Supported roles:

- `all`
- `product`
- `project`
- `engineering`
- `qa`
- `marketing`
- `sales`
- `technology`

The generated file is written to:

```text
tmp/agent-context.md
```

`tmp/` is ignored by Git, so generated context does not clutter commits.

## Why This Exists

Agent workflows are more reliable when the model receives consistent context:

- The workflow.
- Role expectations.
- Security rules.
- Acceptance and validation gates.
- The relevant prompt or checklist.

This mirrors the same idea behind model context systems: expose the right
resources and instructions instead of pasting unrelated docs.
