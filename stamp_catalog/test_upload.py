import requests
import os

# URL of the Flask application
url = 'http://localhost:8000/upload'

# Path to the test image
image_path = 'images/test_stamp.jpg'

# Check if the image exists
if not os.path.exists(image_path):
    print(f"Image not found at {image_path}")
    exit(1)

# Open the image file
with open(image_path, 'rb') as f:
    files = {'file': (os.path.basename(image_path), f, 'image/jpeg')}
    response = requests.post(url, files=files)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")