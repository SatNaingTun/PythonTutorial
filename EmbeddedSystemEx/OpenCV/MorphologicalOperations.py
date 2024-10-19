import cv2
import numpy as np

img = cv2.imread('Images/NOSE01178.jpg')


imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',imgGray)


kernel = np.ones((5,5),np.uint8)

eroded_image  = cv2.erode(img,kernel,iterations = 1)
cv2.imshow("Eroded Image",eroded_image )



dilatedImage = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("Dilated Image",dilatedImage )

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening Image",opening )

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing Image",closing )

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient Image",gradient )

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Tophat Image",tophat )

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Tophat Image",tophat )


cv2.waitKey(0)