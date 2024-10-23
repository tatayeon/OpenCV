#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:01:20 2024

@author: imtaeyeon
"""

import cv2 as cv
import sys

cap = cv.VideoCapture(0)  # 혹은 cap = cv.VideoCapture(1) 카메라 연결 시도

if not cap.isOpened():
    sys.exit("카메라 연결 실패")
    
while True:
    ret, frame = cap.read() #프레임 구성하는 프레임 획득
    
    if not ret:
        print("프레임 획득 실패")
        break
    
    cv.imshow("video display", frame)
    
    key=cv.waitKey(1) # 1밀리초 기다리고 q가 눌리면 빠져 나가는 루트
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()