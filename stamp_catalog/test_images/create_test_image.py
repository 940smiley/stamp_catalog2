from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple test image
img = Image.new('RGB', (400, 300), color=(255, 255, 255))
d = ImageDraw.Draw(img)

# Draw a simple stamp-like rectangle
d.rectangle([50, 50, 350, 250], outline=(0, 0, 0), width=2)
d.rectangle([60, 60, 340, 240], outline=(255, 0, 0), width=3)

# Add some text to simulate stamp details
try:
    # Try to use a default font
    font = ImageFont.load_default()
    d.text((100, 100), "Test Stamp", fill=(0, 0, 0))
    d.text((100, 130), "5c", fill=(0, 0, 0))
    d.text((100, 160), "USA 1950", fill=(0, 0, 0))
except:
    # If font loading fails, just draw without font
    d.text((100, 100), "Test Stamp")
    d.text((100, 130), "5c")
    d.text((100, 160), "USA 1950")

# Save the image
img.save('test_stamp.jpg')
print("Test image created successfully!")