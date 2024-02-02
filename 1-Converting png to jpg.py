#converting the png image file to jpg image file

import cv2

image=cv2.imread("CV.png")#loading the  image

cv2.imshow("Computer_Vision",image)#Displaying the image

cv2.imwrite("CV.jpg",image)#Saving the image in jpg format in the dirctory

cv2.waitKey(10000)#This line is used to display the image for 10 seconds

cv2.destroyAllWindows()
