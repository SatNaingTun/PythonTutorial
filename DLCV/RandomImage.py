import cv2
import numpy
import os
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray =  numpy.array(randomByteArray)
grayImage = flatNumpyArray.reshape(300,400)
cv2.imshow("image gray", grayImage)
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imshow("image bgr", bgrImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
