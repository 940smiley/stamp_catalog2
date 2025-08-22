"""
AI Learning Module for Stamp Catalog Application
This module handles the AI learning from user corrections.
"""

import json
import os
from datetime import datetime

class AILearner:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.training_data_path = os.path.join(os.path.dirname(log_file_path), 'training_data.json')
        
    def load_log(self):
        """Load the stamp log from JSON file"""
        try:
            with open(self.log_file_path, 'r') as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return []
        except FileNotFoundError:
            return []
            
    def save_training_data(self, training_data):
        """Save training data to JSON file"""
        with open(self.training_data_path, 'w') as f:
            json.dump(training_data, f, indent=2)
            
    def load_training_data(self):
        """Load training data from JSON file"""
        try:
            with open(self.training_data_path, 'r') as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return []
        except FileNotFoundError:
            return []
            
    def learn_from_edits(self, stamp_id, user_edits):
        """Learn from user corrections to improve AI detection"""
        # Load current log
        log_data = self.load_log()
        
        # Find the stamp entry
        stamp_entry = None
        for entry in log_data:
            if entry["id"] == stamp_id:
                stamp_entry = entry
                break
                
        if not stamp_entry:
            return False
            
        # Create training example
        training_example = {
            "timestamp": datetime.now().isoformat(),
            "original_features": stamp_entry["features"].copy(),
            "user_corrections": user_edits,
            "image_path": stamp_entry["original_image"]
        }
        
        # Load existing training data
        training_data = self.load_training_data()
        
        # Add new training example
        training_data.append(training_example)
        
        # Save updated training data
        self.save_training_data(training_data)
        
        return True
        
    def get_training_stats(self):
        """Get statistics about the training data"""
        training_data = self.load_training_data()
        return {
            "total_examples": len(training_data),
            "last_training": training_data[-1]["timestamp"] if training_data else None
        }

# Example usage
if __name__ == "__main__":
    # This would typically be integrated with the main Flask application
    learner = AILearner("../logs/stamp_log.json")
    
    # Simulate learning from a user edit
    sample_edits = {
        "name": "Corrected Stamp Name",
        "date": "1960",
        "country_of_origin": "United Kingdom"
    }
    
    # In a real scenario, you would pass the actual stamp ID
    result = learner.learn_from_edits("test-id-123", sample_edits)
    
    if result:
        stats = learner.get_training_stats()
        print(f"AI learning updated successfully!")
        print(f"Total training examples: {stats['total_examples']}")
    else:
        print("Failed to update AI learning")