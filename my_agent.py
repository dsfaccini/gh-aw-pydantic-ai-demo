"""The agent this repository's agentic workflow runs.

`PAI_AGENT: my_agent:agent` in `.github/workflows/triage.md` names the `agent`
variable below. The engine passes `-m` from the workflow's `engine.model`, so
the model is not set here.
"""

from pydantic_ai import Agent

LABELS = ('bug', 'documentation', 'enhancement', 'question')

agent = Agent(
    name='triage',
    instructions="""
You triage one GitHub issue. Read the issue in the prompt, then post exactly one
comment with the `safeoutputs_add_comment` tool. The comment has three parts, in order:

1. **Summary.** What the issue reports, in two sentences or fewer.
2. **Suggested label.** One label from `label_catalog()`, and one line saying why.
3. **Question.** What the reporter still needs to tell us before anyone can act.
   Write "No follow-up needed." when the issue is already actionable.

Suggest a label; do not apply one. Do not edit files. Do not open issues.
""",
)


@agent.tool_plain
def label_catalog() -> list[str]:
    """The labels this repository triages with."""
    return list(LABELS)
