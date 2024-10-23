#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:19:36 2024

@author: imtaeyeon
"""

#가볍게 사진을 한번 띄어보는 실습 이정도는 간단히 하자 그리고 파일의 경로가 중요하다.
import cv2 as cv
import sys
import numpy as np

img = cv.imread('soccer.jpg') #주요함수 imread("파일명") 자신이 원하는 사진을 불러온다.

if img is None:
    sys.exit('파일을 찾을 수 없습니다.');
    
cv.imshow('Image Display', img) #imshow 이미지를 띄울 때 어떤 이름으로 띄울 것인지 무슨 이미지를 띄울지 적어준다.

cv.waitKey()
cv.destroyAllWindows()

#넘파이 활용 조금 
a = np.array([[0, 1, 2], [3, 4, 5]])
print(a[0,0])  # first row , first col
print(a[0,1])  # first row , second col
print(a[-1,-1]) # last row , last col

b = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
b[0,:]  # first row(전체)
b[:,1]  # second col (전체)
b[1,1:] # second row의 second col 부터 끝까지
b[:,0:3] #모든 row의 0:3까지 col