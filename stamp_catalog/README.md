# Stamp Catalog Application

An AI-powered application to catalog your stamp collection by simply uploading photos. The application automatically processes images, identifies stamps, extracts characteristics, and provides eBay listing suggestions.

## Features

- **Photo Upload**: Upload stamp photos by dropping them into the directory, clicking upload, or taking a photo
- **Image Processing**: Automatic straightening and enhancement for better clarity
- **AI Detection**: Identifies stamps and extracts detailed characteristics
- **Duplicate Detection**: Prevents logging the same stamp multiple times
- **Editable Log**: Correct any AI mistakes and help the AI learn from your corrections
- **eBay Export**: Export stamps in eBay-ready format for easy listing
- **Commerce Integration**: Supports integration with platforms like Hip Comic, Delcampe, etc.
- **Postcard Support**: Special handling for postcards with front/rear image requirements
- **Cleanup Functionality**: Reset your log when needed

## Installation

### Option 1: Python Setup Script (Cross-platform)

1. Clone or download this repository
2. Navigate to the stamp_catalog directory
3. Run the setup script:
   ```bash
   python setup.py
   ```

### Option 2: PowerShell Setup Script (Windows)

1. Clone or download this repository
2. Navigate to the stamp_catalog directory
3. Run the PowerShell setup script:
   ```powershell
   .\setup.ps1
   ```

### Option 3: Manual Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```powershell
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment:
   - On Windows:
     ```powershell
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. Run the application:
   ```bash
   python src/app.py
   ```

3. Access the application in your browser at `http://localhost:5000`

4. Upload stamp photos using the web interface

5. View and edit your stamp log at `http://localhost:5000/log`

6. Export stamps to eBay format at `http://localhost:5000/export/ebay/<stamp_id>`

## Directory Structure

```
stamp_catalog/
├── venv/                 # Python virtual environment
├── images/              # Uploaded stamp images
├── logs/                # Stamp collection log files
├── src/                 # Application source code
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── requirements.txt     # Python dependencies
├── setup.py             # Python setup script
├── setup.ps1           # PowerShell setup script
└── README.md           # This file
```

## How It Works

1. **Upload**: Users can upload photos of stamps through the web interface
2. **Process**: The application automatically straightens and enhances the image for clarity
3. **Detect**: The application uses AI to determine what the object in the image is
4. **Analyze**: For stamps, the AI extracts all available characteristics:
   - Name of the stamp
   - Date or era it was used
   - Cancellation marks
   - Cancellation date or text
   - Any letter or note written on the piece
   - Colors
   - Denomination
   - Country of origin
   - Theme
   - Type (block, singular, strip, sheet, etc.)
   - Value
   - eBay listing suggestions
5. **Log**: All information is saved to an editable log
6. **Learn**: User edits help the AI learn and improve its accuracy
7. **Export**: Stamps can be exported in eBay-ready format

## Contributing

This application is designed to be extensible. Contributions for improving the AI detection capabilities, adding more commerce platform integrations, or enhancing the user interface are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask for the web framework
- Uses OpenCV for image processing
- AI detection capabilities are planned for future enhancement