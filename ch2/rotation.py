#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:22:36 2024

@author: imtaeyeon
"""
# 4주차 로테이션 메트릭스 계산과 역변환 계산

import cv2 as cv
import numpy as np
import math

# 이미지 읽기 및 크기 조절 (1/4 크기로 축소)
img = cv.imread('soccer.jpg')
img_half = cv.resize(img, dsize=(0, 0), fx=0.25, fy=0.25)

# 회전된 이미지를 저장할 빈 배열 생성
fimg = np.zeros((img_half.shape), np.uint8)
bimg = np.zeros((img_half.shape), np.uint8)

# 이미지의 높이와 너비
h, w = img_half.shape[:2]

# 이미지 중심 좌표 계산
centerx = w // 2
centery = h // 2

# 회전 각도 (60도)
angle = 60
rad = np.radians(angle)  # 각도를 라디안 값으로 변환

# ---------------- 포워드 방식으로 직접 변환 ----------------
for y in range(0, h):
    for x in range(0, w):
        # x, y 좌표에 대해 회전 변환 행렬을 적용하여 새로운 좌표 계산
        dx = (x - centerx) * np.cos(rad) + (y - centery) * np.sin(rad) + centerx
        dx = round(dx)  # 좌표를 정수로 반올림
        dy = (x - centerx) * (-np.sin(rad)) + (y - centery) * np.cos(rad) + centery
        dy = round(dy)
        
        # 계산된 좌표가 이미지 범위를 벗어나지 않으면 픽셀 값을 복사
        if 0 <= dx < w and 0 <= dy < h:
            fimg[dy, dx] = img_half[y, x]

# ---------------- 역변환 방식으로 직접 변환 (선형 보간) ----------------
for y in range(0, h):
    for x in range(0, w):
        # x, y 좌표에 대해 역변환 행렬을 적용하여 원본 이미지에서의 좌표 계산
        dx = (x - centerx) * np.cos(rad) - (y - centery) * np.sin(rad) + centerx
        a = dx - math.floor(dx)  # 소수점 부분 추출
        dx = math.floor(dx)  # 좌표를 내림하여 정수로 변환
        
        dy = (x - centerx) * np.sin(rad) + (y - centery) * np.cos(rad) + centery
        b = dy - math.floor(dy)  # 소수점 부분 추출
        dy = math.floor(dy)  # 좌표를 내림하여 정수로 변환

        # 계산된 좌표가 이미지 범위를 벗어나지 않으면 선형 보간을 적용하여 픽셀 값을 계산
        if 0 <= dx < w - 1 and 0 <= dy < h - 1:
            # 선형 보간을 사용하여 4개의 인접한 픽셀 값을 가중합
            bimg[y, x] = (1 - a) * (1 - b) * img_half[dy, dx] + \
                         a * (1 - b) * img_half[dy, dx + 1] + \
                         (1 - a) * b * img_half[dy + 1, dx] + \
                         a * b * img_half[dy + 1, dx + 1]

# ---------------- OpenCV를 이용한 회전 ----------------
M = cv.getRotationMatrix2D((centerx, centery), angle, scale=1)
rimg = cv.warpAffine(img_half, M, (w, h))

# ---------------- 결과 출력 ----------------
# 원본 이미지, 포워드 방식 결과, 역변환 방식 결과를 가로로 나란히 연결하여 출력
result = np.hstack((img_half, fimg, bimg))

# 결과와 OpenCV 회전 결과를 화면에 표시
cv.imshow("Result", result)
cv.imshow("Rotation", rimg)

# 키 입력을 대기한 후 모든 창 닫기
cv.waitKey()
cv.destroyAllWindows()
