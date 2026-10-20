"""Isolation check for pydantic/pydantic-ai#9318.

Drops only `copilot-integration-id` from the headers `GitHubCopilotProvider` sends, so the
AWF api-proxy injects its own id while the `editor-*` headers stay. The engine imports this
module before CLAI 2 builds the provider from `-m github-copilot:<id>`.
"""

from types import MappingProxyType

from pydantic_ai import Agent
from pydantic_ai.capabilities import LocalWorkspace
from pydantic_ai.providers import github_copilot
from pydantic_ai_harness import Coder

github_copilot._COPILOT_CLIENT_HEADERS = MappingProxyType(
    {name: value for name, value in github_copilot._COPILOT_CLIENT_HEADERS.items() if name != 'copilot-integration-id'}
)

agent = Agent(name='coder', capabilities=[LocalWorkspace('.'), Coder()])
