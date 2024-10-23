#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:52:54 2024

@author: imtaeyeon
"""

#FLANN 실습 매칭알고리즘이다 

#1. 입력 영상으로 부터 다중 스케일 영상을 구성한다.
#2. 적절한 미분연산을 적용하여 다중 스케일 영상을 구한다
#3. 그 다음 극점 즉 튀는 부분을 특징점으로 잡아낸다.


import cv2 as cv
import numpy as np
import time
#SIFT를 사용한 매칭을 구현한 것으로 최근접 이웃 비율 기법을 사용함
# 이미지 불러오기 및 해당 부분 자르기
img1 = cv.imread("mot_color70.jpg")[190:350, 440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)  # 이미지를 그레이스케일로 변환

img2 = cv.imread("mot_color83.jpg")
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # 두 번째 이미지도 그레이스케일로 변환

# SIFT 검출기 생성
sift = cv.SIFT_create()

# 특징점과 디스크립터 검출 및 계산
kp1, des1 = sift.detectAndCompute(gray1, None)  # 함수 이름 수정 (detectAndCompute)
kp2, des2 = sift.detectAndCompute(gray2, None)

# 특징점 개수 출력
print("특징점 개수: ", len(kp1), len(kp2))

# 매칭 시작 시간 기록
start = time.time()

# FLANN 기반 매처 생성
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# KNN 매칭 수행 (가장 가까운 2개의 매칭)
#위에서 찾은 2개로 이제 맞는 매칭을 시킨다.
knn_match = flann_matcher.knnMatch(des1, des2, 2)

# 최근접 이웃 거리 비율 적용
# 좋은 매칭을 저장할 리스트
#우리가 찾은 매칭중에서 비율을 구해서 T보다 작은것만 찾는 알고리즘을 쓴다 왜냐 그냥 knn보다 정확도가 더 높다.
T = 0.7  # 매칭 기준 비율 설정
good_match = []
for nearest1, nearest2 in knn_match:
    if nearest1.distance / nearest2.distance < T:
        good_match.append(nearest1)  # 좋은 매칭만 리스트에 추가

# 매칭에 걸린 시간 출력
print("매칭에 걸린 시간", time.time() - start)

# 매칭 결과를 시각적으로 표시하기 위한 빈 이미지 생성
img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)

# 매칭 결과를 이미지에 그리기
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과 이미지 창에 표시
cv.imshow("Good Matches", img_match)

# 키 입력 대기 후 창 닫기
k = cv.waitKey()
cv.destroyAllWindows()