@echo off
echo Installing Python dependencies...
pip install -r requirements.txt
echo Downloading spaCy model...
python -m spacy download en_core_web_sm
echo Setup complete! You can now run the application.
pause 