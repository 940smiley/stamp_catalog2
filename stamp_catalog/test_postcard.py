import requests
import os

# URL of the Flask application
url = 'http://localhost:8000/postcard'

# For now, we'll just test the GET request to see if the page renders
# A full POST test would require sending two files, which is more complex

response = requests.get(url)

# Print the response
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("Postcard page successfully rendered")
else:
    print(f"Error: {response.text}")