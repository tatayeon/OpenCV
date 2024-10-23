#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:45:11 2024

@author: imtaeyeon
"""
# 이진화 알고리즘에 사용되는 오츄 알고리즘(Otsu's Method)을 알아보자
# 오츠 알고리즘은 이진화를 최적화 문제로 바라봄으로써 최적의 임계값(t)을 찾는다.
# 이 과정에서 0이 되는 화소와 1이 되는 화소의 분산을 고려한다.
# 목표는 임계값(t)이 이진화 결과를 잘 나누는 지점을 찾는 것.

## 여기에서 'soccer.jpg' 이미지는 임계값을 계산한 결과 113.0으로 나왔고
## 이 113.0보다 어두운 화소는 검은색(0), 밝은 화소는 흰색(255)으로 표현된다.

import cv2 as cv
import sys

# 이미지를 불러옴 (soccer.jpg 파일을 로드)
img = cv.imread('soccer.jpg')

# === 오츠 알고리즘을 통한 이진화 ===
# img[:, :, 2]은 이미지를 R(빨간색) 채널로 분리한 것.
# cv.threshold: 이진화 작업을 수행하는 함수
# - 첫 번째 인자: 입력 이미지 (여기서는 R 채널) 순서는 BGR
# - 두 번째 인자: 0은 초기 임계값 (알고리즘이 자동으로 최적 값을 계산할 때 사용)
# - 세 번째 인자: 255는 최대값 (임계값을 초과한 화소에 할당되는 값)
# - 네 번째 인자: cv.THRESH_BINARY + cv.THRESH_OTSU로 오츠 알고리즘을 적용
t, bin_img = cv.threshold(img[:, :, 2], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 오츠 알고리즘이 찾은 최적의 임계값을 출력
print('오츠 알고리즘이 찾은 최적의 임곗값: ', t)

# === 이미지 디스플레이 ===
# 원본 이미지의 R(빨간색) 채널을 표시 (img[:, :, 2]는 R 채널을 추출한 결과)
cv.imshow("R channel", img[:, :, 2])

# 이진화된 이미지를 표시 (이진화 결과는 bin_img에 저장됨)
cv.imshow("R channel binarization", bin_img)

# 키 입력 대기 후 창 닫기
cv.waitKey()
cv.destroyAllWindows()
