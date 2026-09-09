---
on:
  issues:
    types: [opened]
  workflow_dispatch:
permissions:
  contents: read
  issues: read
imports:
  # Becomes `pydantic/pydantic-ai-harness/gh-aw/pydantic.md@main` once the engine
  # definition lands on main. Pin a commit SHA, or a release tag cut after that,
  # to freeze it.
  - pydantic/pydantic-ai-harness/gh-aw/pydantic.md@add-gh-aw-engine-definition
engine:
  id: pydantic-ai
  model: openai/gpt-5
  env:
    PAI_AGENT: my_agent:agent
safe-outputs:
  add-comment:
---

# Triage the new issue

The issue that triggered this run, as gh-aw sanitized it:

<issue>
${{ steps.sanitized.outputs.text }}
</issue>

Post your triage as a single comment on that issue.
