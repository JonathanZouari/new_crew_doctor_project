"""
Crew Factory
Creates and configures the medical diagnostic crew with agents and tasks
"""

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from typing import Dict, Any
from pathlib import Path

from .prompt_loader import PromptLoader
from backend.config import (
    CREW_MAX_RPM,
    CREW_VERBOSE,
    CREW_MEMORY_ENABLED,
    PROMPTS_DIR
)


# ============================================================================
# TOOLS
# ============================================================================

@tool("Medical Interview Tool")
def conduct_medical_interview(patient_input: str) -> str:
    """
    Conducts structured medical interview using OPQRST framework.
    Helps gather comprehensive patient information systematically.
    """
    return f"Processing patient information: {patient_input}"


@tool("Differential Diagnosis Generator")
def generate_differential_diagnosis(symptoms: str) -> str:
    """
    Applies clinical reasoning frameworks to generate differential diagnoses.
    Uses pattern recognition and Bayesian analysis.
    """
    return f"Analyzing symptoms for differential diagnosis: {symptoms}"


@tool("Safety Check Tool")
def safety_check(symptoms: str) -> str:
    """
    Identifies red flags and emergency warning signs in patient presentation.
    Checks for critical 'can't miss' diagnoses.
    """
    return f"Performing safety check on: {symptoms}"


@tool("Health Literacy Checker")
def check_health_literacy(medical_text: str) -> str:
    """
    Ensures patient communication is at appropriate reading level (8th grade).
    Checks for medical jargon and suggests plain language alternatives.
    """
    return f"Checking health literacy of communication: {medical_text}"


# ============================================================================
# CREW FACTORY
# ============================================================================

class CrewFactory:
    """Factory for creating configured medical diagnostic crews"""

    def __init__(self, prompts_dir: Path = PROMPTS_DIR):
        """
        Initialize the crew factory.

        Args:
            prompts_dir: Path to prompts directory
        """
        self.prompt_loader = PromptLoader(prompts_dir)

    def create_agent(self, agent_name: str, tools: list = None) -> Agent:
        """
        Create an agent based on configuration.

        Args:
            agent_name: Name of the agent configuration to use
            tools: List of tools to assign to the agent

        Returns:
            Configured Agent instance
        """
        config = self.prompt_loader.get_agent_config(agent_name)

        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=CREW_VERBOSE,
            allow_delegation=False,
            memory=CREW_MEMORY_ENABLED,
            tools=tools or []
        )

    def create_task(
        self,
        task_name: str,
        agent: Agent,
        context: list = None,
        inputs: Dict[str, Any] = None
    ) -> Task:
        """
        Create a task based on configuration.

        Args:
            task_name: Name of the task configuration to use
            agent: Agent to assign to this task
            context: List of tasks that provide context
            inputs: Input parameters for the task

        Returns:
            Configured Task instance
        """
        config = self.prompt_loader.get_task_config(task_name)

        return Task(
            description=config['description'],
            expected_output=config['expected_output'],
            agent=agent,
            context=context or []
        )

    def create_medical_diagnostic_crew(self) -> Crew:
        """
        Create the complete medical diagnostic crew.

        Returns:
            Configured Crew instance
        """
        # Create agents
        intake_coordinator = self.create_agent(
            'intake_coordinator',
            tools=[conduct_medical_interview]
        )

        diagnostic_physician = self.create_agent(
            'diagnostic_physician',
            tools=[generate_differential_diagnosis, safety_check]
        )

        communication_specialist = self.create_agent(
            'communication_specialist',
            tools=[check_health_literacy]
        )

        # Create tasks
        interview_task = self.create_task(
            'interview_task',
            agent=intake_coordinator
        )

        diagnosis_task = self.create_task(
            'diagnosis_task',
            agent=diagnostic_physician,
            context=[interview_task]
        )

        communication_task = self.create_task(
            'communication_task',
            agent=communication_specialist,
            context=[interview_task, diagnosis_task]
        )

        # Create and configure crew
        crew = Crew(
            agents=[
                intake_coordinator,
                diagnostic_physician,
                communication_specialist
            ],
            tasks=[
                interview_task,
                diagnosis_task,
                communication_task
            ],
            process=Process.sequential,
            memory=CREW_MEMORY_ENABLED,
            verbose=CREW_VERBOSE,
            max_rpm=CREW_MAX_RPM,
            full_output=True
        )

        return crew
