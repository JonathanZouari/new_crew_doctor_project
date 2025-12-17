@echo off
echo ====================================
echo Opening Medical Diagnostic Frontend
echo ====================================
echo.

REM Check if backend is running
echo Make sure Backend is running first!
echo Run: run_backend.bat
echo.

REM Open frontend in default browser
echo Opening frontend in browser...
start frontend\templates\index.html

echo.
echo Frontend opened in browser
echo Make sure Backend is running on http://localhost:8000
echo.

pause
