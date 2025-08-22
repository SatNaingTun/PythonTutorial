import cv2
import numpy as np
image1 = cv2.imread("images/car-left.tif")
image2 = cv2.imread("images/car-right.tif")
image = cv2.add(image1,image2)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
