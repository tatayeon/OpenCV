# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2 as cv
import sys

img = cv.imread('soocer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()

