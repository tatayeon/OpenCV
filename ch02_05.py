#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:59:04 2024

@author: imtaeyeon
"""

#얼굴에 네모난 박스 그리기

import cv2 as cv
import sys

img = cv.imread("girl_laughing.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없다.")

cv.rectangle(img, (830, 30),(1000, 200), (0, 0, 255), 2) #이렇게 라이브러리 자체에 rectangle함수, polylines, circle, ellipse, putText 등등이 있다.
cv.putText(img, 'laugh', (830, 24),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv.imshow("Draw", img)

cv.waitKey()
cv.destroyAllWindows()