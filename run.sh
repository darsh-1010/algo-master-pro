#!/bin/bash

# DSA Problem Solver - Startup Script for Unix/Linux/Mac
# This script provides a user-friendly way to start the application

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

echo
echo "========================================"
echo "    DSA Problem Solver - Startup Script"
echo "========================================"
echo

# Check Python installation
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    print_status "Python 3 found!"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    print_status "Python found!"
else
    print_error "Python is not installed!"
    echo "Please install Python 3.7+ from https://python.org"
    echo
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON_MAJOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.major)")
PYTHON_MINOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.minor)")

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
    print_error "Python 3.7 or higher is required!"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

print_status "Python version: $PYTHON_VERSION"
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    print_info "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    print_status "Virtual environment created!"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate
print_status "Virtual environment activated!"
echo

# Install/update dependencies
print_info "Installing/updating dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    print_error "Failed to install dependencies!"
    exit 1
fi
print_status "Dependencies installed!"
echo

# Check .env file
if [ ! -f ".env" ]; then
    print_warning ".env file not found!"
    print_info "Creating .env file from template..."
    
    if [ -f "env_example.txt" ]; then
        cp env_example.txt .env
        print_status ".env file created!"
        echo
        print_warning "IMPORTANT: Please edit the .env file and add your Groq API key!"
        echo "Get your API key from: https://console.groq.com/"
        echo
        
        # Try to open .env file with default editor
        if command -v code &> /dev/null; then
            print_info "Opening .env file with VS Code..."
            code .env
        elif command -v nano &> /dev/null; then
            print_info "Opening .env file with nano..."
            nano .env
        elif command -v vim &> /dev/null; then
            print_info "Opening .env file with vim..."
            vim .env
        else
            print_info "Please edit the .env file manually and add your API key."
        fi
        
        echo
        echo "Please restart this script after configuring your API key."
        exit 0
    else
        print_error "env_example.txt not found!"
        exit 1
    fi
fi

# Check if API key is configured
if grep -q "your_groq_api_key_here" .env || ! grep -q "GROQ_API_KEY=" .env; then
    print_warning "Please set your Groq API key in the .env file!"
    echo "Get your API key from: https://console.groq.com/"
    exit 1
fi

print_status ".env file is properly configured!"
echo

# Start the application
print_info "Starting DSA Problem Solver..."
echo
echo "The application will open in your browser at: http://localhost:5000"
echo
echo "Press Ctrl+C to stop the application"
echo

# Start the app
$PYTHON_CMD run.py

echo
echo "Application stopped."
