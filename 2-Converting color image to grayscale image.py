import cv2

#reading the image
image=cv2.imread("CV.png")

#converting it into grayscale image
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image",image)

cv2.imshow("Grayscale image",grayimage)

cv2.waitKey(10000)#this line is used to display the image for 10 seconds

cv2.destroyAllWindows()

