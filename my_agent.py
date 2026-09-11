from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModelSettings

settings = OpenAIChatModelSettings(openai_reasoning_effort='max')

agent = Agent(
    name='triage',
    model_settings=settings,
    instructions=(
        'Summarize the issue and suggest a label from label_catalog(). '
        'Ask a follow-up question only if needed. '
        'Post one comment with safeoutputs_add_comment.'
    ),
)


@agent.tool_plain
def label_catalog() -> list[str]:
    return ['bug', 'documentation', 'enhancement', 'question']
