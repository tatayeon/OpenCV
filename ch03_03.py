#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:25:13 2024

@author: imtaeyeon
"""

#명암 조절 중에 하나
#명암 조절은 영상을 밝거나 어둡게 조정하는 기법으로 선형연산과 비선형연산이 있는데 감마는 이중 비선형에 속한다 
#선형인 같은 값을 더하거나 빼면서 더욱 자세하게 나타낸다. ex) 이진화도 이중 하나라고 할 수 있음
#비선형 명암 조절 감마 보정 실험하

import cv2 as cv
import numpy as np

img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

def gamma (f, gamma=1.0):
    f1 = f/255.0
    return np.uint8(255*(f1**gamma))

gc = np.hstack((gamma(img, 0.5), gamma(img, 0.75), gamma(img, 1.0), gamma(img, 2.0), gamma(img, 3.0)))

cv.imshow("gamma", gc)

cv.waitKey()
cv.destroyAllWindows()