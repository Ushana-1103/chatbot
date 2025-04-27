@echo off
echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Checking Flask installation...
pip show flask
if errorlevel 1 (
    echo Flask is not installed
    echo Installing Flask...
    pip install flask flask-cors
)

echo.
echo Starting server...
python app.py
if errorlevel 1 (
    echo.
    echo Server failed to start. Check the error message above.
    echo.
    echo Troubleshooting steps:
    echo 1. Make sure no other program is using port 8080
    echo 2. Try running as administrator
    echo 3. Check if your firewall is blocking the connection
    echo.
    pause
    exit /b 1
)

pause 