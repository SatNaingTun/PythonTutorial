import cv2

grayImg= cv2.imread('Images/landscape.jpg',0)
cv2.imshow('grayImage',grayImg)
cv2.waitKey(0)