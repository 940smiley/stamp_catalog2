"""
End-to-End Test for Stamp Catalog Application
This script tests the complete functionality of the stamp catalog application.
"""

import os
import json
import requests
import time

def test_application():
    """Run end-to-end tests on the stamp catalog application"""
    print("Starting end-to-end tests for Stamp Catalog Application...")
    
    # Test 1: Check if the main page loads
    print("\nTest 1: Checking if main page loads...")
    try:
        response = requests.get('http://localhost:8000/')
        if response.status_code == 200:
            print("✓ Main page loads successfully")
        else:
            print(f"✗ Main page failed to load (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"✗ Main page failed to load (Error: {e})")
    
    # Test 2: Check if the log page loads
    print("\nTest 2: Checking if log page loads...")
    try:
        response = requests.get('http://localhost:8000/log')
        if response.status_code == 200:
            print("✓ Log page loads successfully")
        else:
            print(f"✗ Log page failed to load (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"✗ Log page failed to load (Error: {e})")
    
    # Test 3: Check if the postcard page loads
    print("\nTest 3: Checking if postcard page loads...")
    try:
        response = requests.get('http://localhost:8000/postcard')
        if response.status_code == 200:
            print("✓ Postcard page loads successfully")
        else:
            print(f"✗ Postcard page failed to load (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"✗ Postcard page failed to load (Error: {e})")
    
    # Test 4: Check log file functionality
    print("\nTest 4: Checking log file functionality...")
    log_file_path = 'logs/stamp_log.json'
    
    if os.path.exists(log_file_path):
        try:
            with open(log_file_path, 'r') as f:
                content = f.read().strip()
                if content:
                    log_data = json.loads(content)
                    print(f"✓ Log file exists with {len(log_data)} entries")
                else:
                    print("✓ Log file exists (empty)")
        except Exception as e:
            print(f"✗ Log file exists but failed to read (Error: {e})")
    else:
        print("✗ Log file does not exist")
    
    # Test 5: Check commerce configuration
    print("\nTest 5: Checking commerce configuration...")
    config_file_path = 'config/commerce_config.json'
    
    if os.path.exists(config_file_path):
        try:
            with open(config_file_path, 'r') as f:
                content = f.read().strip()
                if content:
                    config_data = json.loads(content)
                    platforms = list(config_data.keys())
                    print(f"✓ Commerce configuration exists with platforms: {', '.join(platforms)}")
                else:
                    print("✗ Commerce configuration file is empty")
        except Exception as e:
            print(f"✗ Commerce configuration exists but failed to read (Error: {e})")
    else:
        print("✗ Commerce configuration file does not exist")
    
    print("\nEnd-to-end tests completed!")

if __name__ == "__main__":
    test_application()