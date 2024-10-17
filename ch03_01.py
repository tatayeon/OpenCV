#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:45:11 2024

@author: imtaeyeon
"""
#이진화 알고리즘에 사용되는 오츄알고리즘을 알아보자
#오츄 알고리즘은 이진화를 최적화 문제로 바라봄으로써 최적의 t값을 T(임계치)로 사용한다.
#이 과정에서 0이 되는 화소의 분산 1이 되는 화소의 분산을 사용하는 개념이 들어간다.
#목적함수는 임계값의 좋음 정도를 측정한다.

## 여기에서 축구 이미지는 임계값을 계산한 결과 113.0으로 나왔고 이 113.0보다 아래면 어두운 이미지 높으면 밝은 이미지로 표현이 된다.

import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

t, bin_img = cv.threshold(img[:, :, 2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적의 임곗값: ', t)

cv.imshow("R channel", img[:, :, 2])
cv.imshow("R channel binarization", bin_img)

cv.waitKey()
cv.destroyAllWindows()