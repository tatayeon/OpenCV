#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:38:49 2024

@author: imtaeyeon
"""
#이진화 알고리즘 중 히스토그램을 이용한 임계값을 찾고 
#이진영상으로 만드는 과정중 하나이다.
#하지만 실제에서는 계곡이 많아서 쉽지 않다.

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("soccer.jpg")
h = cv.calcHist([img], [2], None, [256], [0, 256])  # Corrected to calcHist
plt.plot(h, color="r", linewidth=1)  # Fixed typo in linewidth
plt.show()