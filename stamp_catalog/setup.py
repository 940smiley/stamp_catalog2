#!/usr/bin/env python3

"""
Stamp Catalog Setup Script
This script sets up the stamp catalog application environment.
"""

import os
import subprocess
import sys

def setup_environment():
    """Set up the Python virtual environment and install dependencies"""
    print("Setting up Stamp Catalog application...")
    
    # Create virtual environment
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    # Upgrade pip
    print("Upgrading pip...")
    if os.name == 'nt':  # Windows
        pip_executable = "venv\\Scripts\\pip.exe"
    else:  # Unix/Linux/Mac
        pip_executable = "venv/bin/pip"
        
    subprocess.run([pip_executable, "install", "--upgrade", "pip"], check=True)
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([pip_executable, "install", "-r", "requirements.txt"], check=True)
    
    print("Setup complete!")
    print("\nTo run the application:")
    if os.name == 'nt':  # Windows
        print("1. Activate the virtual environment: venv\\Scripts\\activate")
        print("2. Run the application: python src\\app.py")
    else:  # Unix/Linux/Mac
        print("1. Activate the virtual environment: source venv/bin/activate")
        print("2. Run the application: python src/app.py")
    
    print("\nTo access the application, open your browser and go to http://localhost:5000")

if __name__ == "__main__":
    setup_environment()