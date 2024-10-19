import cv2


cap=cv2.VideoCapture('Images/test_video.mp4')
while True:
    success, img=cap.read()
    cv2.imshow('Result',img)
    if cv2.waitKey(1)==ord('q'):
        break
    # if cv2.waitKey(1) ==ord('c'):
    #    cv2.imwrite('saveimage.jpg',img)q
        
cap.release()
cv2.destroyAllWindows()
