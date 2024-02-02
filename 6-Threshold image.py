#Threshold image

import cv2

image =cv2.imread('CV.png')

grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#name=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]

thresholdimg=cv2.threshold(grayimg,160,255,cv2.THRESH_BINARY)[1]

cv2.imshow('original',image)

cv2.imshow('Threshold Image',thresholdimg)

cv2.imwrite('Threshold Image.jpg',thresholdimg)
