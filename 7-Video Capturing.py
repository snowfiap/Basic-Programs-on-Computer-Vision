import cv2

vs=cv2.VideoCapture(0)#Installing the camera ID

while True:
    _,img=vs.read()
    cv2.imshow("VideoStream",img)
    key=cv2.waitKey(1)
    
    print(key)
    if key==ord("c"):# condition to stop the video.press c in the keyboard to close the video recording
        break
    
vs.release()# To release the camera
cv2.destroyAllWindows()#To close the window
