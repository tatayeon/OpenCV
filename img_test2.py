# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize = (0, 0), fx=0.5, fy=0.5)

cv.imwrite("soccer_gray.jpg", gray)
cv.imwrite("soccer_gray_small.jpg", gray_small)


    
cv.imshow('Color Display', img)
cv.imshow('Gray Display', gray)
cv.imshow('Gray_small Display', gray_small)


cv.waitKey()
cv.destroyAllWindows()

