---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  issues: read
imports:
  - pydantic/pydantic-ai-harness/gh-aw/pydantic.md@main
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
