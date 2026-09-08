# gh-aw-pydantic-ai-demo

The finished repository for the Pydantic AI Harness walkthrough
[Run your own Pydantic AI agent as a GitHub Agentic Workflow](https://pydantic.dev/docs/ai/harness/gh-aw/).

Two files carry the example:

- `my_agent.py` -- a `pydantic_ai.Agent` that triages one issue. `PAI_AGENT` in the
  workflow names it.
- `.github/workflows/triage.md` -- the agentic workflow that runs the agent on
  `issues: opened` through [gh-aw](https://github.com/github/gh-aw)'s `pydantic-ai`
  engine.

`.github/workflows/triage.lock.yml` and `.github/aw/` are written by `gh aw compile`
and committed with the sources: the run fails if the lock is stale.
