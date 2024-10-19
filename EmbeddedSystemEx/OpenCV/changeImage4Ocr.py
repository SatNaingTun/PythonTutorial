import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

# fig, ax = plt.subplots(nrows=2, ncols=2)
rows=3
columns=2
fig = plt.figure(figsize=(10, 7)) 


img = cv2.imread('Images/NOSE01178.jpg')
fig.add_subplot(rows, columns, 1)
plt.imshow(img)
plt.axis('off') 
plt.title("Original") 



if(img is not None):
    print(img.shape)
# cv2.imshow('Original Black',img)
     # Slicing to crop the image
 
# Display the cropped image
# cv2.imshow("cropped", cropped_image)
    # cropped_image=img.copy()
   
    cropped_image = img[140:230, 50:630]
    fig.add_subplot(rows, columns, 2)
    plt.imshow(cropped_image)
    plt.axis('off') 
    plt.title("Cropped") 
    
    fig.add_subplot(rows, columns, 3)
    plt.hist(cropped_image.ravel(),256,[0,256])
    plt.axis('off') 
    plt.title("Histogram") 

    kernel = np.ones((2,2),np.uint8)
# dilatedImage = cv2.dilate(cropped_image,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedImage )

    
    # eroded_image  = cv2.erode(cropped_image,kernel,iterations = 1)
    # fig.add_subplot(rows, columns, 2)
    # plt.axis('off') 
    # plt.title("Cropped")
    # cv2.imshow("Eroded Image",eroded_image )


# # opening = cv2.morphologyEx(eroded_image, cv2.MORPH_OPEN, kernel)
# # cv2.imshow("Opening Image",opening )


# hist = cv2.calcHist([img],[0],None,[256],[0,256])
   
# plt.show()

# thresh = 127
# im_bw = cv2.threshold(closing, thresh, 255, cv2.THRESH_BINARY)[1]
# (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    thresh = 120
    im_WhiteOnBlack = cv2.threshold(cropped_image, thresh, 255, cv2.THRESH_BINARY)[1]
    im_bw = cv2.bitwise_not(im_WhiteOnBlack)
    fig.add_subplot(rows, columns, 4)
    plt.imshow(im_bw)
    plt.axis('off') 
    plt.title("BW") 
    # cv2.imshow("Inverted Image",im_bw)

    closing = cv2.morphologyEx(im_bw, cv2.MORPH_CLOSE, kernel)
    fig.add_subplot(rows, columns, 5)
    plt.imshow(closing)
    plt.axis('off') 
    plt.title("Closing") 
    # cv2.imshow("Closing Image",closing )

# cv2.imshow("After threshold",im_bw)
# plt.imshow("BW",im_bw)
# plt.show()

    # cv2.waitKey(0)
    result=pytesseract.image_to_string(closing)
    print(result)