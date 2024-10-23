#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:45:50 2024

@author: imtaeyeon
"""

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
# SIFT로 특징점의 개수를 찾는다
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
print("특징점의 개수: ", len(kp1), len(kp2))

start=time.time()

# FLANN 기반 매처 생성 이제 사용할라고 준비하는 단계
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# KNN 매칭 수행 (가장 가까운 2개의 매칭)
# 위에서 찾은 des들로 가장 가까운거 2개를 찾는 로직 (knn사용)
knn_match = flann_matcher.knnMatch(des1, des2, 2)

# 최근접 이웃 거리 비율 적용
# 좋은 매칭을 저장할 리스트
T = 0.7  # 매칭 기준 비율 설정
good_match = []
for nearest1, nearest2 in knn_match:
    if nearest1.distance / nearest2.distance < T:
        good_match.append(nearest1)  # 좋은 매칭만 리스트에 추가

print("매칭에 걸린 시간: ", time.time()-start)
# 매칭 결과를 시각적으로 표시하기 위한 빈 이미지 생성
img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1],3), dtype=np.uint8)

# 매칭 결과를 이미지에 그리기
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과 이미지 창에 표시
cv.imshow("Matches and Homography", img_match)

# 키 입력 대기 후 창 닫기
k = cv.waitKey()
cv.destroyAllWindows()