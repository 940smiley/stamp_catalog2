"""
Route Testing Script for Stamp Catalog Application
This script tests all the routes of the stamp catalog application.
"""

import requests

def test_routes():
    """Test all application routes"""
    base_url = 'http://localhost:8000'
    
    routes = [
        ('/', 'Main Page'),
        ('/log', 'Log Page'),
        ('/postcard', 'Postcard Page'),
        ('/edit/test-id-123', 'Edit Page')
    ]
    
    print("Testing application routes...")
    
    for route, description in routes:
        try:
            response = requests.get(base_url + route)
            if response.status_code == 200:
                print(f"✓ {description} ({route}) - Status: {response.status_code}")
            else:
                print(f"✗ {description} ({route}) - Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"✗ {description} ({route}) - Error: {e}")
    
    # Test export route
    try:
        response = requests.get(base_url + '/export/ebay/test-id-123')
        if response.status_code == 200:
            print(f"✓ eBay Export Route - Status: {response.status_code}")
        else:
            print(f"✗ eBay Export Route - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"✗ eBay Export Route - Error: {e}")
    
    print("\nRoute testing completed!")

if __name__ == "__main__":
    test_routes()