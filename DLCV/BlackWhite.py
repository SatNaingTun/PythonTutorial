import cv2
import numpy
import os
 # height, width
blackImage =  numpy.zeros((300,400))
cv2.imshow("image black", blackImage)
whiteImage =  255*numpy.ones((300,400))
cv2.imshow("image white", whiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
