---
on:
  workflow_dispatch:
permissions:
  contents: read
imports:
  - pydantic/pydantic-ai/src/pydantic_ai_harness/gh-aw/pydantic.md@e8ab544f1f026668089021dc7ee65a63e0c547c2
engine:
  id: pydantic-ai
  model: copilot/claude-haiku-4-5
  env:
    PAI_AGENT: copilot_isolation:agent
safe-outputs:
  create-issue:
    title-prefix: "[copilot-isolation] "
    max: 1
---

# Copilot integration-id isolation check

Read `README.md` in this repository. Then create one issue titled "Copilot integration-id isolation check"
whose body summarizes the README in two sentences.
