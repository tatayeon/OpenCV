#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:46:01 2024

@author: imtaeyeon
"""

import cv2 as cv
import sys

cap = cv.VideoCapture(0)  # 혹은 cap = cv.VideoCapture(1) 카메라 연결 시도 

if not cap.isOpened():
    sys.exit("카메라 연결 실패")
    
while True:
    ret, frame = cap.read() #여기서 비디오를 구성하는 프레임 획득
    
    if not ret:
        print("프레임 획득 실패")
        break
    
    cv.imshow("video display", frame)
    
    key=cv.waitKey(1)
    if key == ord('q'): #q를 입력시 빠져나가는 코드이다.
        break

cap.release()
cv.destroyAllWindows()