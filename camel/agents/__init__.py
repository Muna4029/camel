# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import BaseAgent
    from .chat_agent import ChatAgent
    from .critic_agent import CriticAgent
    from .embodied_agent import EmbodiedAgent
    from .knowledge_graph_agent import KnowledgeGraphAgent
    from .mcp_agent import MCPAgent
    from .repo_agent import RepoAgent
    from .role_assignment_agent import RoleAssignmentAgent
    from .search_agent import SearchAgent
    from .task_agent import (
        TaskCreationAgent,
        TaskPlannerAgent,
        TaskPrioritizationAgent,
        TaskSpecifyAgent,
    )
    from .tool_agents.base import BaseToolAgent
    from .tool_agents.hugging_face_tool_agent import HuggingFaceToolAgent

_lazy_imports = {
    'BaseAgent': ('.base', 'BaseAgent'),
    'ChatAgent': ('.chat_agent', 'ChatAgent'),
    'CriticAgent': ('.critic_agent', 'CriticAgent'),
    'EmbodiedAgent': ('.embodied_agent', 'EmbodiedAgent'),
    'KnowledgeGraphAgent': ('.knowledge_graph_agent', 'KnowledgeGraphAgent'),
    'MCPAgent': ('.mcp_agent', 'MCPAgent'),
    'RepoAgent': ('.repo_agent', 'RepoAgent'),
    'RoleAssignmentAgent': ('.role_assignment_agent', 'RoleAssignmentAgent'),
    'SearchAgent': ('.search_agent', 'SearchAgent'),
    'TaskCreationAgent': ('.task_agent', 'TaskCreationAgent'),
    'TaskPlannerAgent': ('.task_agent', 'TaskPlannerAgent'),
    'TaskPrioritizationAgent': ('.task_agent', 'TaskPrioritizationAgent'),
    'TaskSpecifyAgent': ('.task_agent', 'TaskSpecifyAgent'),
    'BaseToolAgent': ('.tool_agents.base', 'BaseToolAgent'),
    'HuggingFaceToolAgent': (
        '.tool_agents.hugging_face_tool_agent',
        'HuggingFaceToolAgent',
    ),
}


def __getattr__(name):
    if name in _lazy_imports:
        module_name, attr_name = _lazy_imports[name]
        try:
            module = importlib.import_module(module_name, __package__)
            attr = getattr(module, attr_name)
            globals()[name] = attr
            return attr
        except Exception as e:
            raise ImportError(
                f'Could not import name {name} from {module_name}'
            ) from e
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return sorted(list(globals().keys()) + list(_lazy_imports.keys()))


__all__ = [
    'BaseAgent',
    'BaseToolAgent',
    'ChatAgent',
    'CriticAgent',
    'EmbodiedAgent',
    'HuggingFaceToolAgent',
    'KnowledgeGraphAgent',
    'MCPAgent',
    'RepoAgent',
    'RoleAssignmentAgent',
    'SearchAgent',
    'TaskCreationAgent',
    'TaskPlannerAgent',
    'TaskPrioritizationAgent',
    'TaskSpecifyAgent',
]
