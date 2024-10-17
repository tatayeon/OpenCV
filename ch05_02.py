#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:52:54 2024

@author: imtaeyeon
"""

import cv2 as cv
import numpy as np
import time

img1 = cv.imread("mot_color70.jpg")[190:350, 440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

img2 = cv.imread("mot_color83.jpg")[190:350, 440:560]
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift =cv.SIFT_create()
hp1, des1 = sift.detectAndComputer(gray1, None)
hp2, des2 = sift.detectAndComputer(gray2, None)
print("특징점 개수: ", len(hp1), len(hp2))

start = time.time()
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match=flann_matcher.knn_match(des1, des2, 2)

T=0.7
good_match = []
for nearest1, nearest2 in knn_match:
    if(nearest1.distance/nearest2.distance)<T:
        good_match.append(nearest1)

print()