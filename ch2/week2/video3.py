#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:29:30 2024

@author: imtaeyeon
"""

import cv2 as cv
import sys
import numpy as np

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾ㄹ을 수 없습니다.')
    

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN: #색상의 순서가 반대 bgr 이 방식으로 간다.
        cv.rectangle(img, (x,y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+100, y+100), (255, 0, 0), 2)
        
    cv.imshow('Drawing', img)
    
cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
