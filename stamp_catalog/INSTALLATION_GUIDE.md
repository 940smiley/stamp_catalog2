
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
   - On Windows: `venv\Scripts\activate`
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
