@echo off
REM Check if the 'Next-Gen-Surveillance' directory exists
IF NOT EXIST "Next-Gen-Surveillance" (
    echo The 'Next-Gen-Surveillance' directory does not exist. Please clone or download the repository first.
    pause
    exit /b
)

REM Step 1: Navigate to the backend directory
cd Next-Gen-Surveillance\backend

REM Step 2: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Step 3: Run the Flask backend app
echo Running Flask backend app...
python app.py

REM Pause the script to keep the window open
pause
