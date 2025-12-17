"""
Main entry point for Railway deployment
This file is required for Railway to detect the FastAPI application
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import the FastAPI app
from backend.api import app

# This is what Railway/Uvicorn will use
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))

    print(f"\nStarting Medical Diagnostic API on port {port}...")
    print(f"Health check: http://0.0.0.0:{port}/health")
    print(f"API docs: http://0.0.0.0:{port}/docs\n")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
