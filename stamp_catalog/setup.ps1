# Stamp Catalog Setup Script for Windows
# This script sets up the stamp catalog application environment

Write-Host "Setting up Stamp Catalog application..." -ForegroundColor Green

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
venv\Scripts\pip.exe install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
venv\Scripts\pip.exe install -r requirements.txt

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "`nTo run the application:" -ForegroundColor Cyan
Write-Host "1. Activate the virtual environment: venv\Scripts\activate" -ForegroundColor Cyan
Write-Host "2. Run the application: python src\app.py" -ForegroundColor Cyan
Write-Host "`nTo access the application, open your browser and go to http://localhost:5000" -ForegroundColor Cyan