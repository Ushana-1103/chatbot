@echo off
echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Python is not installed or not in PATH. Please install Python first.
    pause
    exit
)

echo Installing required packages...
pip install flask==2.0.1
pip install flask-cors==3.0.10
pip install spacy==3.8.0
pip install scikit-learn==1.0.2

echo Downloading spaCy model...
python -m spacy download en_core_web_sm

echo Setup complete! You can now run the application.
pause 