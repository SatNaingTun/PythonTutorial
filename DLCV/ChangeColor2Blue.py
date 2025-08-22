import cv2

# Load the image
image = cv2.imread("images/size13x13.png")

# Display original image
cv2.imshow("Original Image", image)

# Loop through each pixel
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        b, g, r = image[i, j]  # OpenCV uses BGR format
        # Check if pixel is predominantly red
        if r > 100 and r > g + 50 and r > b + 50:
            image[i, j] = [r, g, b]  # Swap red and blue

# Display modified image
cv2.imshow("Red to Blue", image)

# Print pixel values (green channel as in your original code)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        print(f"element x {i} y {j} val {image[i,j,1]}")

cv2.imwrite("images/size13x13-blue.png", image)  # Save the modified image
cv2.waitKey(0)
cv2.destroyAllWindows()