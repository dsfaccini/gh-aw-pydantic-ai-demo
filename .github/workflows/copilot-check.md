---
on:
  workflow_dispatch:
permissions:
  contents: read
imports:
  - pydantic/pydantic-ai/src/pydantic_ai_harness/gh-aw/pydantic.md@614f620fec1d3cd85a251ad1d315146a26c7a398
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
