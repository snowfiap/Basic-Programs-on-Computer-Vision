#Resizing the image
import cv2

import imutils

image=cv2.imread('CV.png')

resized=imutils.resize(image,width=150)

cv2.imshow('Original',image)

cv2.imshow('Resized image',resized)

cv2.imwrite('Resized_image.jpg',resized)


                                                      
