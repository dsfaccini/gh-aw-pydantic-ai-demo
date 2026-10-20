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
safe-outputs:
  create-issue:
    title-prefix: "[copilot-check] "
    max: 1
---

# Copilot routing check

Read `README.md` in this repository. Then create one issue titled "Copilot routing check"
whose body summarizes the README in two sentences.
