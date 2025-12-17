"""
Server Startup Script
Adds parent directory to path and starts the API server
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Now import and run the API
if __name__ == "__main__":
    import uvicorn

    print("\n" + "=" * 70)
    print("🏥 MEDICAL DIAGNOSTIC API SERVER")
    print("=" * 70)
    print("\nStarting server...")
    print("API Documentation: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/health")
    print("Frontend: Open frontend/templates/index.html in browser")
    print("=" * 70 + "\n")

    # Import app after path is set
    from backend.api import app

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
