#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:22:36 2024

@author: imtaeyeon
"""
#4주차 로테이션 메트릭스 계산과 역변환 계산

import cv2 as cv
import numpy as np
import math

img = cv.imread('soccer.jpg')
img_half = cv.resize(img, dsize = (0, 0), fx = 0.25, fy = 0.25)
fimg = np.zeros((img_half.shape), np.uint8)
bimg = np.zeros((img_half.shape), np.uint8)

h, w = img_half.shape[:2]

centerx = w//2
centery = h//2

angle = 60

rad = np.radians(angle)

for y in range(0, h):
    for x in range(0, w): #메트릭스 연산 시작 직접 만든 변환행렬 포워드 방법
        dx = (x-centerx) * np.cos(rad) + (y-centery) * np.sin(rad) + centerx
        dx = round(dx)
        dy = (x-centerx) * (-np.sin(rad)) + (y-centery) * np.cos(rad) + centery
        dy = round(dy)
        
        if(0<=dx < w and 0 <= dy < h): # 변환된 값이 index값을 넘어가면 버린다.
            fimg[dy, dx] = img_half[y, x]
            
for y in range(0, h):
    for x in range(0, w): #메트릭스 연산 시작 직접 만든 변환행렬 포워드 방법
        dx = (x-centerx) * np.cos(rad) - (y-centery) * np.sin(rad) + centerx
        a = dx - math.floor(dx); # round(dx) : nearest 방법
        dx = math.floor(dx) # 가장 가까운 픽셀로 보낸다. 소수점 이하를 버리면서 but 경계선에 이상한 부분이 깨진다 따라사 영상 보간을 해야한다.
        dy = (x-centerx) * (np.sin(rad)) + (y-centery) * np.cos(rad) + centery
        b = dy - math.floor(dy)
        dy = math.floor(dy)
        
        #if(0<=dx < w and 0 <= dy < h-1): # 번위안에 있으면 원본이미지에서 가져와라. 
            #bimg[y, x] = img_half[dy, dx] #여기 수정해서 
            #bimg[y, x] = () #linear interpolation으로 하는게 과제 위에 if

        #    bimg[y, x] = (1 - a) * (1 - b) * img_half[dy, dx] + a * (1 - b) * img_half[dy, dx + 1] + (1 - a) * b * img_half[dy + 1, dx] + a * b * img_half[dy + 1, dx + 1]
        
        if (0 <= dx < w - 1 and 0 <= dy < h - 1):
            bimg[y, x] = (1 - a) * (1 - b) * img_half[dy, dx] + a * (1 - b) * img_half[dy, dx + 1] + (1 - a) * b * img_half[dy + 1, dx] + a * b * img_half[dy + 1, dx + 1]
        

M = cv.getRotationMatrix2D((centerx, centery), angle, scale = 1) #cv코드 불러와서 넣어도 되긴한다.
rimg = cv.warpAffine(img_half, M, (w, h))      

result = np.hstack((img_half, fimg, bimg))

cv.imshow("Result", result)
cv.imshow("Rotation", rimg)

cv.waitKey()
cv.destroyAllWindows()