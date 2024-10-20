#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:09:46 2024

@author: imtaeyeon
"""

#이진 알고리즘 1
#이렇게 히스토그램으로 특정 임계점을 잡고 크면 1 작으면 0
import cv2 as cv
import matplotlib.pyplot as plt
import sys

img = cv.imread('soccer.jpg')
h=cv.calcHist(img, [2], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)