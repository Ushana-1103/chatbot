@echo off
set PYTHON_PATH="C:\Users\aniru\AppData\Local\Programs\Python\Python313\python.exe"

echo Installing required packages...
%PYTHON_PATH% -m pip install flask==2.0.1
%PYTHON_PATH% -m pip install flask-cors==3.0.10
%PYTHON_PATH% -m pip install spacy==3.8.0
%PYTHON_PATH% -m pip install scikit-learn==1.0.2

echo Downloading spaCy model...
%PYTHON_PATH% -m spacy download en_core_web_sm

echo Setup complete! You can now run the application.
pause 