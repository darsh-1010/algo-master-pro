#!/usr/bin/env python3
"""
DSA Problem Solver - Startup Script
This script provides a user-friendly way to start the application with proper error handling.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = ['flask', 'groq', 'python-dotenv']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is not installed")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run: pip install -r requirements.txt")
            sys.exit(1)

def check_env_file():
    """Check if .env file exists and has the required API key."""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("❌ .env file not found!")
        print("📝 Creating .env file from template...")
        
        if Path('env_example.txt').exists():
            with open('env_example.txt', 'r') as template:
                content = template.read()
            
            with open('.env', 'w') as env:
                env.write(content)
            
            print("✅ .env file created from template")
            print("⚠️  Please edit .env file and add your Groq API key!")
            print("   Get your API key from: https://console.groq.com/")
            return False
        else:
            print("❌ env_example.txt not found!")
            return False
    
    # Check if API key is set
    with open('.env', 'r') as f:
        content = f.read()
        if 'your_groq_api_key_here' in content or 'GROQ_API_KEY=' not in content:
            print("⚠️  Please set your Groq API key in the .env file!")
            print("   Get your API key from: https://console.groq.com/")
            return False
    
    print("✅ .env file is properly configured")
    return True

def start_application():
    """Start the Flask application."""
    print("\n🚀 Starting DSA Problem Solver...")
    
    try:
        # Import and start the app
        from app import app
        
        print("✅ Application loaded successfully!")
        print("🌐 Opening browser in 3 seconds...")
        print("📱 The app will be available at: http://localhost:5000")
        
        # Wait a bit for the server to start
        time.sleep(3)
        
        # Open browser
        try:
            webbrowser.open('http://localhost:5000')
        except:
            print("⚠️  Could not open browser automatically. Please open: http://localhost:5000")
        
        # Start the Flask app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Try running: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

def main():
    """Main function to run the startup process."""
    print("🎯 DSA Problem Solver - Startup Script")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check dependencies
    check_dependencies()
    
    # Check environment configuration
    env_configured = check_env_file()
    
    if not env_configured:
        print("\n⚠️  Environment not fully configured!")
        print("   Please configure your .env file and run this script again.")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    print("\n🎉 All checks passed! Ready to start the application.")
    
    # Start the application
    start_application()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("💡 Please check the error message above and try again.")
