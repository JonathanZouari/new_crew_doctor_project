"""Configuration module"""
from .settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL_NAME,
    CREW_MAX_RPM,
    CREW_VERBOSE,
    CREW_MEMORY_ENABLED,
    PROMPTS_DIR,
    LOGS_DIR
)

__all__ = [
    'OPENAI_API_KEY',
    'OPENAI_MODEL_NAME',
    'CREW_MAX_RPM',
    'CREW_VERBOSE',
    'CREW_MEMORY_ENABLED',
    'PROMPTS_DIR',
    'LOGS_DIR'
]
