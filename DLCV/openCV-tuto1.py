import cv2
image = cv2.imread("images/size13x13.png")
cv2.imshow("image", image)
for i in range(0,13):
    for j in range(0,13):
        print("element x ", i, " y ",j," val ", image[i,j,1])
cv2.waitKey(0)
cv2.destroyAllWindows()