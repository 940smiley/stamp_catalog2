"""
Packaging Script for Stamp Catalog Application
This script creates a distributable package of the stamp catalog application.
"""

import os
import zipfile
import shutil
from datetime import datetime

def package_application():
    """Create a zip package of the stamp catalog application"""
    # Define the package name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"stamp_catalog_{timestamp}.zip"
    
    # Define files and directories to include in the package
    include_items = [
        "src/",
        "templates/",
        "static/",
        "logs/",
        "config/",
        "requirements.txt",
        "setup.py",
        "setup.ps1",
        "README.md"
    ]
    
    # Create the zip file
    with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in include_items:
            if os.path.isfile(item):
                # Add file to zip
                zipf.write(item)
            elif os.path.isdir(item):
                # Add directory and all its contents to zip
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Add file to zip with relative path
                        zipf.write(file_path)
    
    print(f"Application packaged successfully as {package_name}")
    return package_name

def create_installation_guide():
    """Create a simple installation guide"""
    guide_content = """
# Stamp Catalog Application - Installation Guide

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation

### Option 1: Using the setup script (Recommended)
1. Extract the package contents
2. Run the setup script:
   - On Windows: `setup.ps1`
   - On macOS/Linux: `python setup.py`

### Option 2: Manual installation
1. Extract the package contents
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\\Scripts\\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the Application
1. Activate the virtual environment (if not already activated)
2. Run the application: `python src/app.py`
3. Access the application in your browser at `http://localhost:8000`

## Configuration
- Update API keys in `config/commerce_config.json` for commerce platform integration
- Uploaded images are stored in `static/images/`
- Log data is stored in `logs/stamp_log.json`
- Training data from user corrections is stored in `logs/training_data.json`
"""
    
    with open("INSTALLATION_GUIDE.md", "w") as f:
        f.write(guide_content)
    
    print("Installation guide created as INSTALLATION_GUIDE.md")

if __name__ == "__main__":
    print("Packaging Stamp Catalog Application...")
    package_name = package_application()
    create_installation_guide()
    print("Packaging complete!")