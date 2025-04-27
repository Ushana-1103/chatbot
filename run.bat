@echo off
echo Starting HealthBot application...
start chrome "file:///%CD%/index.html"
python app.py 