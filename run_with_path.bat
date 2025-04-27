@echo off
set PYTHON_PATH="C:\Users\aniru\AppData\Local\Programs\Python\Python313\python.exe"

echo Starting HealthBot application...
start chrome "http://localhost:5000"
%PYTHON_PATH% app.py 