#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:51:55 2024

@author: imtaeyeon
"""

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
        a = dx - math.floor(dx);
        dx = math.floor(dx)
        dy = (x-centerx) * (np.sin(rad)) + (y-centery) * np.cos(rad) + centery
        b = dy - math.floor(dy)
        dy = math.floor(dy)
        
        if(0<=dx < w and 0 <= dy < h-1): # 변환된 값이 index값을 넘어가면 버린다.
            bimg[y, x] = img_half[dy, dx]

M = cv.getRotationMatrix2D((centery, centerx), angle, scale = 1) #cv코드 불러와서 넣어도 되긴한다.
rimg = cv.warpAffine(img_half, M, (w, h))      

result = np.hstack((img_half, fimg, bimg))

cv.imshow("Result", result)
cv.imshow("Rotation", rimg)

cv.waitKey()
cv.destroyAllWindows()