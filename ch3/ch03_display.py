#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:25:37 2024

@author: imtaeyeon
"""

#이미지 슬라이스로 짤라서 보기
#색상별 요소를 뜯어서 보기
import cv2 as cv
import sys

img = cv.imread("soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

#이거 같은 경웅에는 사진을 원본에서 짤라서 보기위해서 인덱스 값을 조절한 것
cv.imshow("original_RGB", img)
cv.imshow("Upper left half", img[:img.shape[0]//2, :img.shape[1]//2])
cv.imshow("Center half", img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4])

#이거는 색상을 뜯어보기 위해서 쓰여진 코드
#이렇게 한다고 색상이 나오는 것은 아니고 그 값이 많으면 밝은 색으로 나오는 형태이다.
cv.imshow("R channel", img[:,:,2])
cv.imshow("G channel", img[:,:,1])
cv.imshow("B channel", img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()