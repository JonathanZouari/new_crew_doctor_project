"""
Medical Service
Core business logic for symptom analysis
"""

from typing import Dict, Any
import logging
from datetime import datetime

from .crew_factory import CrewFactory
from backend.config import LOGS_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'medical_service.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class MedicalService:
    """Service for analyzing patient symptoms"""

    def __init__(self):
        """Initialize the medical service"""
        self.crew_factory = CrewFactory()
        logger.info("Medical Service initialized")

    def analyze_symptoms(self, patient_input: str) -> Dict[str, Any]:
        """
        Analyze patient symptoms using the medical diagnostic crew.

        Args:
            patient_input: Patient's description of symptoms and relevant information

        Returns:
            Dictionary containing analysis results and metadata
        """
        logger.info("Starting symptom analysis")
        start_time = datetime.now()

        try:
            # Validate input
            if not patient_input or not patient_input.strip():
                raise ValueError("Patient input cannot be empty")

            # Create crew
            crew = self.crew_factory.create_medical_diagnostic_crew()

            # Run analysis
            logger.info("Running crew analysis...")
            result = crew.kickoff(inputs={
                "patient_input": patient_input
            })

            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            logger.info(f"Analysis completed in {duration:.2f} seconds")

            # Format response
            response = {
                "success": True,
                "result": str(result),
                "metadata": {
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat(),
                    "duration_seconds": duration,
                    "patient_input_length": len(patient_input)
                }
            }

            return response

        except Exception as e:
            logger.error(f"Error during symptom analysis: {str(e)}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
                "metadata": {
                    "start_time": start_time.isoformat(),
                    "end_time": datetime.now().isoformat()
                }
            }

    def health_check(self) -> Dict[str, Any]:
        """
        Check if the service is healthy and ready.

        Returns:
            Dictionary with health status
        """
        try:
            # Check if prompts can be loaded
            self.crew_factory.prompt_loader.load_agent_roles()
            self.crew_factory.prompt_loader.load_task_descriptions()

            return {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            }
        except Exception as e:
            logger.error(f"Health check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
