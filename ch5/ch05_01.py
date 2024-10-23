#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:37:59 2024

@author: imtaeyeon

#따라서 지금은 에지 경계선아니 모퉁이를 찾는 방향이 아니라 어떤 특징이라도 반복적으로 나타나는걸 중요하다고 생각했다.
#→ 반복성이 아주 중요한 요소로 떠 오른다.
#위치와 스케일의 표현은 검출단계
#방향과 특징 기술자는 기술단계(작성) 에서 알아낸다
#조건들 반복성, 불변성, 분별력, 지역성, 적당한 양, 계산효율

#해리스 특징점은 스케일 불변성에 약하다 강한거 시프트 
#대신에 이동과 회전에 불변이라는 특성이 있다.

#이렇게 여러 방향에 대해 색상 변화를 측정하는 제곱차의 합이라는 식을 제안한다.

"""

import cv2 as cv
import numpy as np

#이미지를 대체해서 사용
img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 0 ],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0 ],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],],dtype=np.float32)

#가우시한 필터 생성 과정
ux = np.array([[-1, 0, 1]]) #좌우
uy = np.array([-1, 0, 1]).transpose() #상하
k= cv.getGaussianKernel(3, 1)
g=np.outer(k, k.transpose()) #가우시안 필터처럼 만들어서 3*3짜리 커널을 만든다.

#이건 1차미분 진행
dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux)
#2차 미분
dyy = dy*dy
dxx = dx*dx
dyx = dy*dx
# 가우시안 필터 적용
gdyy = cv.filter2D(dyy, cv.CV_32F, g)
gdxx = cv.filter2D(dxx, cv.CV_32F, g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)
#C값 계산 공식이 있다.
C = (gdyy*gdxx-gdyx*gdyx)-0.04*(gdyy+gdxx)*(gdyy+gdxx)

# C값을 계산 한 것 중에서 주변 8개보다 가운데 있는 숫자가 크면 9로 표기를한다.
for j in range(1, C.shape[0]-1):
    for i in range(1, C.shape[1]-1):
        if C[j, i]>0.1 and sum(sum(C[j, i]>C[j-1:j+2, i-1:i+2]))==8:
            img[j, i] = 9
            
np.set_printoptions(precision=2)
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C)
print(img)

popping = np.zeros([160, 160], np.uint8)
for j in range(0, 160):
    for i in range(0, 160):
        popping[j, i] = np.uint8((C[j//16, i//16]+0.06)*700)

cv.imshow("Image Display2", popping)
cv.waitKey()
cv.destroyAllWindows()















