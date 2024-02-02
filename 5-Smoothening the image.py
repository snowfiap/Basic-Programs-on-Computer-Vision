#Gaussian blur - Smoothening the image

import cv2

import imutils

image=cv2.imread('CV.png')#reading the image

grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Converting to gray image

gaussianimg=cv2.GaussianBlur(grayimg,(21,21),0)#Converting gaussian blur image

cv2.imshow("Gaussian image",gaussianimg)

cv2.imwrite("GaussianBlur.jpg",gaussianimg)#Saving the image to the directory
