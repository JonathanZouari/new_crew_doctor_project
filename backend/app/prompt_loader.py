"""
Prompt Loader Utility
Loads agent roles and task descriptions from external JSON files
"""

import json
from pathlib import Path
from typing import Dict, Any


class PromptLoader:
    """Loads and manages prompts from external configuration files"""

    def __init__(self, prompts_dir: Path):
        """
        Initialize the prompt loader.

        Args:
            prompts_dir: Path to the prompts directory
        """
        self.prompts_dir = Path(prompts_dir)
        self._agent_roles = None
        self._task_descriptions = None

    def load_agent_roles(self) -> Dict[str, Any]:
        """
        Load agent roles from agent_roles.json

        Returns:
            Dictionary containing agent role configurations
        """
        if self._agent_roles is None:
            roles_file = self.prompts_dir / 'agent_roles.json'
            with open(roles_file, 'r', encoding='utf-8') as f:
                self._agent_roles = json.load(f)
        return self._agent_roles

    def load_task_descriptions(self) -> Dict[str, Any]:
        """
        Load task descriptions from task_descriptions.json

        Returns:
            Dictionary containing task description configurations
        """
        if self._task_descriptions is None:
            tasks_file = self.prompts_dir / 'task_descriptions.json'
            with open(tasks_file, 'r', encoding='utf-8') as f:
                self._task_descriptions = json.load(f)
        return self._task_descriptions

    def get_agent_config(self, agent_name: str) -> Dict[str, str]:
        """
        Get configuration for a specific agent.

        Args:
            agent_name: Name of the agent (e.g., 'intake_coordinator')

        Returns:
            Dictionary with 'role', 'goal', and 'backstory'
        """
        roles = self.load_agent_roles()
        if agent_name not in roles:
            raise ValueError(f"Agent '{agent_name}' not found in agent_roles.json")
        return roles[agent_name]

    def get_task_config(self, task_name: str) -> Dict[str, str]:
        """
        Get configuration for a specific task.

        Args:
            task_name: Name of the task (e.g., 'interview_task')

        Returns:
            Dictionary with 'description' and 'expected_output'
        """
        tasks = self.load_task_descriptions()
        if task_name not in tasks:
            raise ValueError(f"Task '{task_name}' not found in task_descriptions.json")
        return tasks[task_name]

    def reload(self):
        """Force reload of all prompt files"""
        self._agent_roles = None
        self._task_descriptions = None
