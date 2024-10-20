#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:41:19 2024

@author: imtaeyeon
"""

#영상 보간 예시
#동차 좌표와 동차 행렬
#2차원 좌표에 1을 추가해 3차원 백터를 표현하는 것
#여기에는 여러가지 기하변환이 있는데 이동, 회전, 둘다하는 것 이렇게 있다
#근데 여기서 문제는 값을 받지 못하는 픽셀이 생길 수 있는데 그걸 에일리어싱이라고 한다 이것을 ㅂ막는게 안티에일리어싱이라고 하는데
#이것은 후방변환 역변환이라고 한다 원래 있던 픽셀을 찾아서 가는 형식? 이다.

import cv2 as cv

img = cv.imread('rose.png')
patch = img[250:350, 170:270,:]

img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0),3)
patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST) # 이거는 최근접이웃 가장 가까이 있는거 따라가는것
patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR) # 이거는 주변 4개를 보고 가장 맞는거 찾아가기
patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC) # 이거는 2차원 그 다음까지 생각해서 하는것 큰차이 X

cv.imshow('original', img)
cv.imshow('INTER_NEAREST', patch1)
cv.imshow('INTER_LINEAR', patch2)
cv.imshow('INTER_CUBIC', patch3)

cv.waitKey()
cv.destroyAllWindows()