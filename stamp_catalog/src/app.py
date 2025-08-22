import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from datetime import datetime
import uuid
from ai_learning import AILearner

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'images')
app.config['LOG_FILE'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'stamp_log.json')

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.dirname(app.config['LOG_FILE']), exist_ok=True)

# Initialize log file if it doesn't exist
if not os.path.exists(app.config['LOG_FILE']):
    with open(app.config['LOG_FILE'], 'w') as f:
        json.dump([], f)

def load_log():
    """Load the stamp log from JSON file"""
    with open(app.config['LOG_FILE'], 'r') as f:
        return json.load(f)

def save_log(log_data):
    """Save the stamp log to JSON file"""
    with open(app.config['LOG_FILE'], 'w') as f:
        json.dump(log_data, f, indent=2)

def detect_stamp_features(image_path):
    """Analyze image and detect stamp features"""
    # This is a placeholder for actual AI detection
    # In a real implementation, you would use a trained model
    
    # For now, we'll return sample data
    return {
        "name": "Sample Stamp",
        "date": "1950-1960",
        "cancellation_marks": True,
        "cancellation_date": "1955-03-15",
        "letter_or_note": None,
        "colors": ["red", "blue", "white"],
        "denomination": "5 cents",
        "country_of_origin": "United States",
        "theme": "Commemorative",
        "type": "block",
        "value": "$2.50",
        "suggestions": {
            "ebay_title": "1950s US Commemorative 5 cent stamp - Red/Blue/White",
            "ebay_description": "A beautiful commemorative stamp from the United States dating back to the 1950s. This stamp has a denomination of 5 cents and features red, blue, and white colors. It has cancellation marks from March 15, 1955, indicating it was used. Perfect for collectors interested in mid-20th century US postal history."
        }
    }

def enhance_image(image_path):
    """Enhance image for better clarity"""
    # Load image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive threshold to enhance details
    enhanced = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Save enhanced image
    enhanced_path = image_path.replace('.jpg', '_enhanced.jpg').replace('.png', '_enhanced.png')
    cv2.imwrite(enhanced_path, enhanced)
    
    return enhanced_path

def straighten_image(image_path):
    """Straighten image if needed"""
    # Load image
    image = cv2.imread(image_path)
    
    # For now, we'll just save a copy as "straightened"
    # In a real implementation, you would detect and correct skew
    straightened_path = image_path.replace('.jpg', '_straightened.jpg').replace('.png', '_straightened.png')
    cv2.imwrite(straightened_path, image)
    
    return straightened_path

def is_duplicate(image_path, log_data):
    """Check if image is a duplicate of an already logged stamp"""
    # This is a placeholder for actual duplicate detection
    # In a real implementation, you would use image hashing or feature matching
    
    # For now, we'll just return False
    return False

def categorize_item(image_path):
    """Categorize what type of item is in the image"""
    # This is a placeholder for actual item categorization
    # In a real implementation, you would use a trained model
    
    # For now, we'll just return "stamp"
    # In future, you could implement logic to detect postcards, covers, etc.
    return "stamp"

@app.route('/postcard', methods=['GET', 'POST'])
def upload_postcard():
    """Handle postcard upload (front and rear images)"""
    if request.method == 'POST':
        # Handle postcard upload with front and rear images
        if 'front' not in request.files or 'rear' not in request.files:
            return jsonify({"error": "Both front and rear images are required"}), 400
        
        front_file = request.files['front']
        rear_file = request.files['rear']
        
        if front_file.filename == '' or rear_file.filename == '':
            return jsonify({"error": "Please select both front and rear images"}), 400
        
        # Save uploaded files
        front_filename = f"{uuid.uuid4()}_front_{front_file.filename}"
        rear_filename = f"{uuid.uuid4()}_rear_{rear_file.filename}"
        
        front_path = os.path.join(app.config['UPLOAD_FOLDER'], front_filename)
        rear_path = os.path.join(app.config['UPLOAD_FOLDER'], rear_filename)
        
        front_file.save(front_path)
        rear_file.save(rear_path)
        
        # Load current log
        log_data = load_log()
        
        # Check for duplicates
        if is_duplicate(front_path, log_data) or is_duplicate(rear_path, log_data):
            # Clean up uploaded files if duplicate detected
            os.remove(front_path)
            os.remove(rear_path)
            return jsonify({"error": "Duplicate postcard detected"}), 400
        
        # Straighten images if needed
        front_straightened_path = straighten_image(front_path)
        rear_straightened_path = straighten_image(rear_path)
        
        # Enhance images for clarity
        front_enhanced_path = enhance_image(front_straightened_path)
        rear_enhanced_path = enhance_image(rear_path)
        
        # Categorize item (this would be used for postcards)
        item_type = "postcard"
        
        # Detect features for both front and rear
        front_features = detect_stamp_features(front_path)
        rear_features = detect_stamp_features(rear_path)
        
        # Check if rear image contains a stamp
        rear_has_stamp = True  # "Rear image contains stamp"  # This would be determined by AI detection
        
        # Add to log
        postcard_entry = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "front_image": front_filename,
            "rear_image": rear_filename,
            "front_straightened": os.path.basename(front_straightened_path),
            "rear_straightened": os.path.basename(rear_straightened_path),
            "front_enhanced": os.path.basename(front_enhanced_path),
            "rear_enhanced": os.path.basename(rear_enhanced_path),
            "item_type": item_type,
            "front_features": front_features,
            "rear_features": rear_features if rear_has_stamp else None,
            "user_edits": {}
        }
        
        log_data.append(postcard_entry)
        save_log(log_data)
        
        return jsonify({"success": True, "postcard_id": postcard_entry["id"]})
    
    # GET request - render the postcard upload template
    return render_template('postcard.html')

@app.route('/')
def index():
    """Main page for uploading stamps"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_stamp():
    """Handle stamp upload and processing"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Save uploaded file
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    # Load current log
    log_data = load_log()
    
    # Check for duplicates
    if is_duplicate(file_path, log_data):
        return jsonify({"error": "Duplicate stamp detected"}), 400
    
    # Straighten image if needed
    straightened_path = straighten_image(file_path)
    
    # Enhance image for clarity
    enhanced_path = enhance_image(straightened_path)
    
    # Categorize item
    item_type = categorize_item(file_path)
    
    # Detect features
    features = detect_stamp_features(file_path)
    
    # Add to log
    stamp_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "original_image": filename,
        "straightened_image": os.path.basename(straightened_path),
        "enhanced_image": os.path.basename(enhanced_path),
        "item_type": item_type,
        "features": features,
        "user_edits": {}
    }
    
    log_data.append(stamp_entry)
    save_log(log_data)
    
    return jsonify({"success": True, "stamp_id": stamp_entry["id"]})

@app.route('/log')
def view_log():
    """View the stamp log"""
    log_data = load_log()
    return render_template('log.html', stamps=log_data)

@app.route('/edit/<stamp_id>', methods=['GET', 'POST'])
def edit_stamp(stamp_id):
    """Edit a stamp entry"""
    log_data = load_log()
    
    # Find the stamp entry
    stamp_entry = None
    for entry in log_data:
        if entry["id"] == stamp_id:
            stamp_entry = entry
            break
    
    if not stamp_entry:
        return jsonify({"error": "Stamp not found"}), 404
    
    if request.method == 'POST':
        # Update stamp entry with user edits
        user_edits = request.json
        stamp_entry["user_edits"] = user_edits
        stamp_entry["features"].update(user_edits)
        save_log(log_data)
        
        # AI learning from user corrections
        learner = AILearner(app.config['LOG_FILE'])
        learner.learn_from_edits(stamp_id, user_edits)
        
        return jsonify({"success": True})
    
    return render_template('edit.html', stamp=stamp_entry)

@app.route('/export/ebay/<stamp_id>')
def export_ebay(stamp_id):
    """Export stamp entry in eBay ready format"""
    log_data = load_log()
    
    # Find the stamp entry
    stamp_entry = None
    for entry in log_data:
        if entry["id"] == stamp_id:
            stamp_entry = entry
            break
    
    if not stamp_entry:
        return jsonify({"error": "Stamp not found"}), 404
    
    # Return eBay ready format
    ebay_data = {
        "title": stamp_entry["features"]["suggestions"]["ebay_title"],
        "description": stamp_entry["features"]["suggestions"]["ebay_description"],
        "category": "Stamps",
        "images": [
            stamp_entry["original_image"],
            stamp_entry["enhanced_image"]
        ]
    }
    
    return jsonify(ebay_data)

@app.route('/cleanup', methods=['POST'])
def cleanup_log():
    """Clean up the log"""
    # Clear the log file
    with open(app.config['LOG_FILE'], 'w') as f:
        json.dump([], f)
    
    return jsonify({"success": True, "message": "Log cleaned up successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)