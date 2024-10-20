#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:41:26 2024

@author: imtaeyeon
"""

#붓으로 그림그리기 페인팅

import cv2 as cv
import sys

img = cv.imread("soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 있습니다.");

BrushSiz = 5 #붓의 크기
LColor, RColor = (255, 0, 0), (0, 0, 255) #이거는 파란색과 빨간색

def painting(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, LColor, -1) #이렇게 마우스의 움직임과 클릭에 반응해서 컬러들이 그려지는 것들
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
        
    cv.imshow("painting", img)
    
cv.namedWindow('painting')
cv.imshow("painting", img)

cv.setMouseCallback('painting', painting)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break