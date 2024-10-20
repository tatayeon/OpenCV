#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 00:18:19 2024

@author: imtaeyeon
"""

import cv2 as cv
import numpy as np
import time

# SIFT를 사용한 매칭을 구현한 것으로 최근접 이웃 비율 기법을 사용함
# 이미지 불러오기 및 해당 부분 자르기
img1 = cv.imread("mot_color70.jpg")[190:350, 440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)  # 이미지를 그레이스케일로 변환

img2 = cv.imread("mot_color83.jpg")
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 두 번째 이미지도 그레이스케일로 변환

# SIFT 검출기 생성
sift = cv.SIFT_create()

# 특징점과 디스크립터 검출 및 계산
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# FLANN 기반 매처 생성
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# KNN 매칭 수행 (가장 가까운 2개의 매칭)
knn_match = flann_matcher.knnMatch(des1, des2, 2)

# 최근접 이웃 거리 비율 적용
# 좋은 매칭을 저장할 리스트
T = 0.7  # 매칭 기준 비율 설정
good_match = []
for nearest1, nearest2 in knn_match:
    if nearest1.distance / nearest2.distance < T:
        good_match.append(nearest1)  # 좋은 매칭만 리스트에 추가

# 매칭된 포인트 좌표 추출
points1 = np.float32([kp1[gm.queryIdx].pt for gm in good_match])
points2 = np.float32([kp2[gm.trainIdx].pt for gm in good_match])

# 호모그래피 계산
H, _ = cv.findHomography(points1, points2, cv.RANSAC)

# 첫 번째 이미지의 크기 가져오기
h1, w1 = img1.shape[0], img1.shape[1]

# 두 번째 이미지의 크기 가져오기
h2, w2 = img2.shape[0], img2.shape[1]

# 첫 번째 이미지의 박스 좌표 계산
box1 = np.float32([[0, 0], [0, h1-1], [w1-1, h1-1], [w1-1, 0]]).reshape(4, 1, 2)

# 호모그래피를 적용하여 두 번째 이미지에 박스를 변환
box2 = cv.perspectiveTransform(box1, H)

# 두 번째 이미지에 박스를 그리기
img2 = cv.polylines(img2, [np.int32(box2)], True, (0, 255, 0), 8)

# 매칭 결과를 시각적으로 표시하기 위한 빈 이미지 생성
img_match = np.empty((max(h1, h2), w1 + w2, 3), dtype=np.uint8)

# 매칭 결과를 이미지에 그리기
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과 이미지 창에 표시
cv.imshow("Matches and Homography", img_match)

# 키 입력 대기 후 창 닫기
k = cv.waitKey()
cv.destroyAllWindows()