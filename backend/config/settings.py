"""
Backend Configuration Settings
Manages environment variables and application settings
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-4o')
OPENAI_ORGANIZATION = os.getenv('OPENAI_ORGANIZATION', None)

# Crew Configuration
CREW_MAX_RPM = int(os.getenv('CREW_MAX_RPM', '10'))
CREW_VERBOSE = os.getenv('CREW_VERBOSE', 'True').lower() == 'true'
CREW_MEMORY_ENABLED = os.getenv('CREW_MEMORY_ENABLED', 'True').lower() == 'true'

# Application Settings
APP_NAME = "Medical Diagnostic Team"
APP_VERSION = "1.0.0"
APP_DEBUG = os.getenv('APP_DEBUG', 'False').lower() == 'true'

# Paths
BASE_DIR = Path(__file__).parent.parent
PROMPTS_DIR = BASE_DIR / 'prompts'
LOGS_DIR = BASE_DIR / 'logs'

# Create logs directory if it doesn't exist
LOGS_DIR.mkdir(exist_ok=True)

# Validation
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. "
        "Please set it in your .env file."
    )
