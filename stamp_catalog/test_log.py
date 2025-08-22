import json
import os

# Test loading and saving log data
log_file_path = os.path.join('logs', 'stamp_log.json')

# Create a test entry
test_entry = {
    "id": "test-id-123",
    "timestamp": "2025-08-22T10:00:00",
    "original_image": "test_stamp.jpg",
    "straightened_image": "test_stamp_straightened.jpg",
    "enhanced_image": "test_stamp_enhanced.jpg",
    "item_type": "stamp",
    "features": {
        "name": "Test Stamp",
        "date": "1950",
        "cancellation_marks": False,
        "cancellation_date": None,
        "letter_or_note": None,
        "colors": ["red", "white", "blue"],
        "denomination": "5 cents",
        "country_of_origin": "United States",
        "theme": "Commemorative",
        "type": "singular",
        "value": "$2.50",
        "suggestions": {
            "ebay_title": "1950 US Commemorative 5 cent stamp - Red/White/Blue",
            "ebay_description": "A commemorative stamp from the United States dating back to 1950."
        }
    },
    "user_edits": {}
}

# Load existing log data
def load_log():
    """Load the stamp log from JSON file"""
    try:
        with open(log_file_path, 'r') as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
            else:
                return []
    except FileNotFoundError:
        return []

# Save log data
def save_log(log_data):
    """Save the stamp log to JSON file"""
    with open(log_file_path, 'w') as f:
        json.dump(log_data, f, indent=2)

# Test the functions
print("Loading existing log data...")
log_data = load_log()
print(f"Current log entries: {len(log_data)}")

print("Adding test entry...")
log_data.append(test_entry)
save_log(log_data)

print("Verifying log data was saved...")
log_data = load_log()
print(f"Log entries after adding test: {len(log_data)}")
if len(log_data) > 0:
    print(f"First entry ID: {log_data[0]['id']}")