#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:43:20 2024

@author: imtaeyeon
"""

import cv2 as cv

# 이미지를 불러옴
img = cv.imread("mot_color70.jpg")

# 이미지를 그레이스케일로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# SIFT 객체 생성
sift = cv.SIFT_create()

# 키포인트와 기술자 계산
#kp는 특징점의 좌표
# des는 그에 해당하는 128개의 그런 기술자
kp, des = sift.detectAndCompute(gray, None)

# 키포인트를 그레이스케일 이미지 위에 그림
#flags 어떻식으로 보여줄 지 결정
gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 결과 이미지 표시
cv.imshow('sift', gray)

# 키 입력을 대기하고 창을 닫음
k = cv.waitKey()
cv.destroyAllWindows()
