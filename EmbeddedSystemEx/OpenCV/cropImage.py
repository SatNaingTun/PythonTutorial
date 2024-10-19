import cv2

img = cv2.imread('Images/NOSE01178.jpg')
print(img.shape)
# cv2.imshow('Original',img)


cropped_image = img[140:230, 50:630] # Slicing to crop the image
 
# Display the cropped image
cv2.imshow("cropped", cropped_image)


cv2.waitKey(0)