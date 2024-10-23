#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:09:46 2024

@author: imtaeyeon
"""

#이진 알고리즘 1 -> 히스토그램으로 임계값 찾기
#이렇게 히스토그램으로 특정 임계점을 잡고 크면 1 작으면 0
#하지만 실제 사용에서는 임계값이 딱 나오지 않는 경우가 많아서 사용하기가 좀 힘들다.
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('soccer.jpg')
h=cv.calcHist(img, [2], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)
