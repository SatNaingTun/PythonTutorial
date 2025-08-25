import cv2
import numpy as np
from matplotlib import image, pyplot as plt
 # Define our imshow function

# plt.close()


def imshow(title="Image", image=None, size=10):
    if image is None:
        raise ValueError("No image provided to imshow()")

    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w / h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')  # Optional: hides axis ticks
    plt.show()
    plt.close()



image = np.zeros((512,512,3), np.uint8)

cv2.line(image, (0,0), (511,511), (255,127,0), 5)
imshow("Black Canvas With Diagonal Line", image)

# cv2.rectangle(image, starting vertex, opposite vertex, color, thickness)
#  Create our black canvas again because now it has a line in it
image = np.zeros((512,512,3), np.uint8)
 # Thickness - if positive. Negative thickness means that it is filled
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 10)
imshow("Black Canvas With Pink Rectangle", image)

 #  cv2.circle(image, center, radius, color, fill)

image = np.zeros((512,512,3), np.uint8)
cv2.circle(image, (350, 350), 100, (15,150,50), -1) 
imshow("Black Canvas With Green Circle", image)
# cv2.imshow("Black Canvas With Green Circle", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image = np.zeros((1000,1000,3), np.uint8)
ourString =  'Hello World!'
cv2.putText(image, ourString, (155,290), 
cv2.FONT_HERSHEY_PLAIN , 3, (40,200,0), 4)
imshow("Messing with some text", image)



# plt.close()