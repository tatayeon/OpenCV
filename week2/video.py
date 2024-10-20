#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:01:20 2024

@author: imtaeyeon
"""

import cv2 as cv
import sys

cap = cv.VideoCapture(0)  # 혹은 cap = cv.VideoCapture(1)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")
    
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("프레임 획득 실패")
        break
    
    cv.imshow("video display", frame)
    
    key=cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()