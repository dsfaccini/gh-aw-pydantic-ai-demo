---
on:
  issues:
    types: [opened]
  workflow_dispatch:
permissions:
  contents: read
imports:
  # Becomes `pydantic/pydantic-ai-harness/gh-aw/pydantic.md@main` once the engine
  # definition lands on main. Pin a commit SHA, or a release tag cut after that,
  # to freeze it.
  - pydantic/pydantic-ai-harness/gh-aw/pydantic.md@add-gh-aw-engine-definition
engine:
  id: pydantic-ai
  model: anthropic/claude-sonnet-4-5
  env:
    PAI_AGENT: my_agent:agent
safe-outputs:
  add-comment:
---

# Triage the new issue

Read the issue that triggered this run, then post your triage as a single
comment on it.
