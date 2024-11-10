import cv2
import sys

# Check if an argument is provided
if len(sys.argv) != 2:
    print("Sample usage: python3 lab7_3.py images/NOSE01178.jpg")
    sys.exit(1)

# Get the image file path from the command-line argument
image_path = sys.argv[1]

# Read the image
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print(f"Error: Could not open or find the image: {image_path}")
    sys.exit(1)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
