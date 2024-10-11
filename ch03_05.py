#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:07:56 2024

@author: imtaeyeon
"""

#컨볼류션 적용하는 예시
# 가우시안 스무딩과 엠보싱 해보기
#여기서는 값이 넘어가는 오버플로우와 언더플로우를 고려해야한다.
#그걸 Clip함수로 처리가 가능하다는 점이다.
#참고로 uint8은 [0, 255] 범위이다.

import cv2 as cv
import numpy as np

# 이미지 읽기 및 크기 조정
img = cv.imread('soccer.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.4, fy=0.4)

# 이미지 그레이스케일로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 텍스트 추가
cv.putText(gray, 'soccer', (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv.imshow("Original", gray)

# 블러링 (GaussianBlur)
smooth = np.hstack((cv.GaussianBlur(gray, (5, 5), 0.0), 
                    cv.GaussianBlur(gray, (9, 9), 0.0), 
                    cv.GaussianBlur(gray, (15, 15), 0.0))) #이렇게 하면 커널이 커지면 더욱 흐려진다.
cv.imshow('Smooth', smooth)

# 엠보싱 필터 적용
femboss = np.array([[-1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, -1.0]])

gray16 = np.int16(gray)
emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))  #여기서는 clip을 사용해서 이제 오버, 언더플로우를 막아주는것 255까지가 아니라 128씩 더해주고 빼줘서 
#0에서 255까지 ㄱ짜르겠다 넘어가는건 이제 그냥 0이나 255가까운데로 그냥 넘긴다.
emboss_bad = np.uint8(np.filter2D(gray16, -1, femboss)+128) #그냥 오버 언더 무시하고 넘겨준다
emboss_worse = cv.filter2D(gray, -1, femboss)  # 128을 더해주지도 않고 ㄷ그냥 해본다.

cv.imshow("Emboss", emboss)
cv.imshow("Emboss_bad", emboss_bad)
cv.imshow("Emboss_wors", emboss_worse)

# 키 입력 대기 후 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()