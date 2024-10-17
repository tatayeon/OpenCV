#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:00:24 2024

@author: imtaeyeon
"""

#모폴리지 $ 연결 요소 예시
# 모폴로지 연결요소로 4연결성, 8연결성등 여러가지 커널의 형태로 만들어서 
# 연결하거나 끊어낼 수 있는 알고리즘이다. 아래의 4가지 형태는 기억해두자 팽창, 침식, 열림, 닫힘
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 이미지 읽기
img = cv.imread('JohnHancocksSignature.png', cv.IMREAD_UNCHANGED)
if img is None:
    raise FileNotFoundError("Image file could not be read. Check the file path.")
if img.shape[2] < 4:
    raise ValueError("Image does not have an alpha channel.")

# 이진화 처리
t, bin_img = cv.threshold(img[:, :, 3], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.imshow(bin_img, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()

# 이미지 자르기 (하단 절반과 좌측 절반)
b = bin_img[bin_img.shape[0]//2:bin_img.shape[0], 0:bin_img.shape[0]//2+1]
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 커널 생성
#여기에 우리가 범위를 지정하는거임 이거 같은 경우에는 마름모형태에 해당하는 커널을 만들었다.
se = np.uint8([[0, 0, 1, 0, 0],
               [0, 1, 1, 1, 0],
               [1, 1, 1, 1, 1],
               [0, 1, 1, 1, 0],
               [0, 0, 1, 0, 0]])

# 팽창
#팽창은 한개라도 참으면 모두 그것을 바꾸는 과정
b_dilation = cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()

# 침식
# 침식은 한개라도 아니면 모두 거짓으로 바꾸는것
b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_erosion, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()

# 폐쇄 연산 (팽창 후 침식)
# 팽창한 후에 침식을 진행한것
b_closing = cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)
plt.imshow(b_closing, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()

#열림을 짜봄 팽창후 침식을 진행
b_opening = cv.dilate(cv.erode(b, se, iterations=1), se, iterations=1)
plt.imshow(b_opening, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.show()










