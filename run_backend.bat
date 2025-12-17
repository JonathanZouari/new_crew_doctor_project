@echo off
echo ====================================
echo Starting Medical Diagnostic Backend
echo ====================================
echo.

REM Activate virtual environment if exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Virtual environment activated
) else (
    echo Warning: Virtual environment not found
    echo Run: python -m venv venv
    echo.
)

REM Run backend server
echo Starting FastAPI server...
echo API will be available at: http://localhost:8000
echo Documentation at: http://localhost:8000/docs
echo.

python backend\api.py

pause
