#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:51:21 2024

@author: imtaeyeon
"""
#히스토그램 평활화하기
#히스토그램을 평평하게 되도록 영상을 조작해 영상의 명암대비를 높이는 기법이다.
#노말라이즈를 해서 총합을 1로 만들고 누적한다 그 누적한 것의 반대를 곱해서 평평하게 만든다.
#이렇게 해도 디지털의 한계로 ㅁ모두 일자는 되지는 않지만 평균 누적은 평균으로 맞춘다
#히스토그램을 보면 낮은부분은 빼곡하지만 높은부분은 듬성듬성하는 것을 볼 수 있다.

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("mistyroad.jpg")
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 명암 영상ㅇ으로 변환하고 출력
plt.imshow(gray, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

h = cv.calcHist([gray], [0], None, [256], [0, 256]) #히스토그램을 구해 출력
plt.plot(h,color='r', linewidth=1), plt.show()

equal = cv.equalizeHist(gray) #히스토그램을 평활화하고 출력하기
plt.imshow(equal, cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

h = cv.calcHist([equal], [0], None, [256], [0, 256]) #히스토그램을 구해 출력
plt.plot(h,color='r', linewidth=1), plt.show()


