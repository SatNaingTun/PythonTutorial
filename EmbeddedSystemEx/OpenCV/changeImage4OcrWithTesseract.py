import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
import cv2
import subprocess
tesseract_cmd = 'tesseract'

filename = 'tempImage.jpg'
filepath = sys.argv
orig_img = cv2.imread(filepath[1])
orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB) #change to true RGB
img_gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY) #change to BNW

def run_tesseract(input_filename, output_filename, dpiNum, dpiVal):
    command = [tesseract_cmd, input_filename, output_filename, dpiNum, dpiVal]

    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    return (proc.wait(), proc.stderr.read())

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img_gray, kernel, iterations=1)
# cv2.imshow('image', erosion)
number_plate = img_gray[130:235, 60:600]
# cv2.imshow("Number plate", number_plate)
ret, thresh1 = cv2.threshold(number_plate, 127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(number_plate,127,255,cv2.THRESH_BINARY_INV)
closing = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)

titles = ['Grayscale Eroded', 'Binary', 'Binary_inv', 'Closing']
images = [erosion, thresh1, thresh2, closing]

for i in range(4):
    plt.subplot(1,4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.imwrite(filename, closing)

string = run_tesseract('/home/pi/labs/lab7/images/tempImage.jpg', '/home/pi/labs/lab7/images/output_lab7_3', '--dpi', '96')
f = open("/home/pi/labs/lab7/output_lab7_3.txt", "r")
print(f.read())
