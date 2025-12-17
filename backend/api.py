"""
FastAPI REST API for Medical Diagnostic Service
Provides HTTP endpoints for symptom analysis
"""

import sys
from pathlib import Path

# Add project root to path FIRST
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict, Any
import uvicorn

from backend.app import MedicalService

# Initialize FastAPI app
app = FastAPI(
    title="Medical Diagnostic API",
    description="AI-powered medical symptom analysis using CrewAI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize medical service
medical_service = MedicalService()


# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class SymptomAnalysisRequest(BaseModel):
    """Request model for symptom analysis"""
    patient_input: str = Field(
        ...,
        description="Patient's description of symptoms and medical information",
        min_length=10,
        json_schema_extra={"example": "I'm a 45-year-old male with chest pain for 3 days..."}
    )


class SymptomAnalysisResponse(BaseModel):
    """Response model for symptom analysis"""
    success: bool
    result: str = None
    error: str = None
    metadata: Dict[str, Any] = None


class HealthCheckResponse(BaseModel):
    """Response model for health check"""
    status: str
    timestamp: str
    version: str = None
    error: str = None


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/", tags=["General"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Medical Diagnostic API",
        "version": "1.0.0",
        "description": "AI-powered medical symptom analysis",
        "endpoints": {
            "health": "/health",
            "analyze": "/api/analyze",
            "docs": "/docs"
        }
    }


@app.get("/health", response_model=HealthCheckResponse, tags=["General"])
async def health_check():
    """Check if the service is healthy and ready"""
    health_status = medical_service.health_check()
    return health_status


@app.post("/api/analyze", response_model=SymptomAnalysisResponse, tags=["Analysis"])
async def analyze_symptoms(request: SymptomAnalysisRequest):
    """
    Analyze patient symptoms and provide diagnostic guidance.

    This endpoint processes patient symptom information through a multi-agent
    AI system that includes:
    - Medical intake coordinator for systematic data gathering
    - Senior diagnostic physician for multi-specialty analysis
    - Patient communication specialist for clear, actionable guidance

    **Important**: This is for educational purposes only and does not replace
    professional medical care.
    """
    try:
        result = medical_service.analyze_symptoms(request.patient_input)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == "__main__":
    import sys
    from pathlib import Path

    # Add project root to path
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    print("\n" + "=" * 70)
    print("MEDICAL DIAGNOSTIC API SERVER")
    print("=" * 70)
    print("\nStarting server...")
    print("API Documentation: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/health")
    print("=" * 70 + "\n")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )
