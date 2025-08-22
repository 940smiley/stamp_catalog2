# Stamp Catalog Application - Project Structure

## Overview
This document describes the complete project structure of the Stamp Catalog Application, including all directories, files, and their purposes.

## Directory Structure
```
stamp_catalog/
├── config/                      # Configuration files
│   └── commerce_config.json    # Commerce platform API configuration
├── logs/                       # Log files
│   └── stamp_log.json          # Main stamp collection log
├── src/                        # Source code
│   ├── app.py                  # Main Flask application
│   ├── ai_learning.py          # AI learning from user corrections
│   └── commerce.py             # Commerce platform integration
├── static/                     # Static files
│   └── images/                 # Uploaded images
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── index.html              # Main upload page
│   ├── log.html                # Stamp collection log view
│   ├── edit.html               # Stamp details editing page
│   └── postcard.html           # Postcard upload page
├── test_images/                # Test image generation scripts
│   └── create_test_image.py    # Script to create test images
├── requirements.txt            # Python dependencies
├── setup.py                    # Python setup script
├── setup.ps1                  # PowerShell setup script
├── package_app.py             # Application packaging script
├── test_end_to_end.py         # End-to-end testing script
├── test_routes.py            # Route testing script
├── test_log.py               # Log functionality testing script
├── test_upload.py            # Upload functionality testing script
├── test_postcard.py          # Postcard functionality testing script
├── README.md                 # Project documentation
├── INSTALLATION_GUIDE.md     # Installation instructions
├── LICENSE                   # License information
└── PROJECT_STRUCTURE.md      # This file
```

## File Descriptions

### Main Application Files
- `src/app.py`: The core Flask application that handles all web routes and functionality
- `src/ai_learning.py`: Module that implements AI learning from user corrections
- `src/commerce.py`: Module that handles integration with commerce platforms

### Configuration Files
- `config/commerce_config.json`: Contains API endpoints and keys for commerce platforms
- `requirements.txt`: Lists all Python dependencies required for the application
- `setup.py`: Python script to set up the virtual environment and install dependencies
- `setup.ps1`: PowerShell script to set up the application on Windows systems

### Documentation Files
- `README.md`: Main project documentation with features and usage instructions
- `INSTALLATION_GUIDE.md`: Detailed installation guide for different platforms
- `LICENSE`: The MIT license for the application
- `PROJECT_STRUCTURE.md`: This file describing the project structure

### Testing Files
- `test_end_to_end.py`: Comprehensive end-to-end testing of the application
- `test_routes.py`: Tests all web routes for proper functionality
- `test_log.py`: Tests the log file functionality
- `test_upload.py`: Tests the stamp upload functionality
- `test_postcard.py`: Tests the postcard upload page
- `test_images/create_test_image.py`: Script to create test images for development

### Web Templates
- `templates/base.html`: Base template with common layout and navigation
- `templates/index.html`: Main page for uploading stamps
- `templates/log.html`: Page to view the stamp collection log
- `templates/edit.html`: Page to edit stamp details
- `templates/postcard.html`: Page for uploading postcards with front/rear images

### Static Files
- `static/images/`: Directory where uploaded stamp images are stored

### Log Files
- `logs/stamp_log.json`: JSON file containing all cataloged stamps and their details

## Key Features Implemented

1. **Photo Upload**: Users can upload stamp photos through the web interface
2. **Image Processing**: Automatic straightening and enhancement of uploaded images
3. **AI Detection**: Identification of stamps and extraction of characteristics
4. **Duplicate Detection**: Prevention of duplicate entries in the log
5. **Editable Log**: Users can edit any details that the AI got wrong
6. **AI Learning**: The application learns from user corrections to improve accuracy
7. **eBay Export**: Stamps can be exported in eBay-ready format
8. **Commerce Integration**: Integration with platforms like Hip Comic and Delcampe
9. **Postcard Support**: Special handling for postcards with front/rear image requirements
10. **Cleanup Functionality**: Ability to clean up the log when needed

## Usage

1. Set up the application using either `setup.py` or `setup.ps1`
2. Run the application with `python src/app.py`
3. Access the web interface at `http://localhost:8000`
4. Configure commerce platform API keys in `config/commerce_config.json`