@echo off
echo Starting Baymax application...
echo Starting Python server...
start cmd /k "python app.py"
timeout /t 5
echo Opening browser...
start chrome "http://localhost:8080"
pause 