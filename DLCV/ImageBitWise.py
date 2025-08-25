import cv2
import numpy as np
image1 = cv2.imread("images/car-left.tif")
height,width,depth = image1.shape
img2 = np.zeros((height,width), np.uint8)
circle_img = cv2.circle(img2,(int(width/2),int(height/2)),200,255,-1)
cv2.imshow("original", image1)
img1_fg = cv2.bitwise_and(image1,image1,mask = circle_img)
cv2.imshow("image", img1_fg)
# img1_fg = cv2.bitwise_not(image1,image1)
# cv2.imshow("image", img1_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
