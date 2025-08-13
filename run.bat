@echo off
title DSA Problem Solver - Startup Script
color 0A

echo.
echo ========================================
echo    DSA Problem Solver - Startup Script
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH!
    echo Please install Python 3.7+ from https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python found!
echo.

echo Installing/updating dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies!
    echo.
    pause
    exit /b 1
)

echo ✅ Dependencies installed!
echo.

if not exist ".env" (
    echo 📝 Creating .env file from template...
    copy "env_example.txt" ".env" >nul
    echo ✅ .env file created!
    echo.
    echo ⚠️  IMPORTANT: Please edit the .env file and add your Groq API key!
    echo    Get your API key from: https://console.groq.com/
    echo.
    echo Press any key to open the .env file for editing...
    pause >nul
    notepad .env
    echo.
    echo Please restart this script after configuring your API key.
    pause
    exit /b 0
)

echo 🚀 Starting DSA Problem Solver...
echo.
echo The application will open in your browser at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the application
echo.

python run.py

echo.
echo Application stopped.
pause
