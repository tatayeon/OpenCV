#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:06:05 2024

@author: imtaeyeon
"""

import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('coin_array.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


t, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

edges = cv.Canny(gray, 150, 200)

huf = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, dp=1, minDist=180, param1=80, param2=18, minRadius=60, maxRadius=120)

total_money = 0

huf = np.uint16(np.around(huf))  
for i in huf[0, :]:
    if i[2] >= 70:
        total_money += 500  # 500원 동전
    else:
        total_money += 100  # 100원 동전

    cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)  # 빨간색 원 그리기


txt = "Total Money = %d 원" % total_money
cv.putText(img, txt, (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

gray_resized = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
bin_img_resized = cv.cvtColor(bin_img, cv.COLOR_GRAY2BGR)
img_resized = img

combined_image = np.hstack((img_resized, gray_resized, bin_img_resized))

cv.imshow("Combined Image", combined_image)

cv.waitKey(0)
cv.destroyAllWindows()