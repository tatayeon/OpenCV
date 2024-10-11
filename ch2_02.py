#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:38:05 2024

@author: imtaeyeon
"""

import cv2 as cv
import sys
import numpy as np

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.');

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #우리가 가져온 사진을 gray으로 바꾸고
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5) #사진의 사이즈를 바꾼다.

#이건 이미지 저장 코드로 따로 빼놓았다.
#cv.imwrite('soccer_gray.jpg', gray)
#cv.imwrite("soccer_gray_small.jpg", gray_small)

cv.imshow("color image", img)
cv.imshow("Gray image", gray)
cv.imshow("gray_small image", gray_small)

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyAllWindows()