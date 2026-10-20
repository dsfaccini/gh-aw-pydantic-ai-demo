---
on:
  workflow_dispatch:
permissions:
  contents: read
imports:
  - pydantic/pydantic-ai/src/pydantic_ai_harness/gh-aw/pydantic.md@523b3c4247a2e299353ac6b03592920ceb4c3f09
engine:
  id: pydantic-ai
  model: copilot/claude-haiku-4-5
safe-outputs:
  create-issue:
    title-prefix: "[copilot-check] "
    max: 1
---

# Copilot routing check (main control)

Read `README.md` in this repository. Then create one issue titled "Copilot routing check"
whose body summarizes the README in two sentences.
