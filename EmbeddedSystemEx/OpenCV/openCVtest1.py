import cv2

img= cv2.imread('landscape.jpg')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgFlipHoz=cv2.flip(img,1)
imgFlipVer=cv2.flip(img,0)

cv2.imshow('image',img)
cv2.imshow('Gray',imgGray)
cv2.imshow('FlipHorrizon',imgFlipHoz)
cv2.imshow('FlipVer',imgFlipVer)
while True:
 if cv2.waitKey(1)==ord('q'):
    break

cv2.destroyAllWindows()