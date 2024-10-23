# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#그래이 이미지 저장하는거 영상을 파일에 저장하는 코드들

import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #사진을 명암 영상으로 변환하는거
gray_small = cv.resize(gray, dsize = (0, 0), fx=0.5, fy=0.5) #스케일 축소하는 코드

cv.imwrite("soccer_gray.jpg", gray) #이렇게 저장할 수 있다. imwrite사용
cv.imwrite("soccer_gray_small.jpg", gray_small)


    
cv.imshow('Color Display', img)
cv.imshow('Gray Display', gray)
cv.imshow('Gray_small Display', gray_small)


cv.waitKey()
cv.destroyAllWindows()

