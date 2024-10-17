#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:49:39 2024

@author: imtaeyeon
"""
import cv2 as cv
import sys

cap = cv.VideoCapture(0)  # 혹은 cap = cv.VideoCapture(1) 카메라 연결 시도 

if not cap.isOpened():
    sys.exit("카메라 연결 실패")
    
frames=[] #프레임을 담을 공간 준비
    
while True:
    ret, frame = cap.read() #여기서 비디오를 구성하는 프레임 획득
    
    if not ret:
        print("프레임 획득 실패")
        break
    
    cv.imshow("video display", frame)
    
    key=cv.waitKey(1)
    if key==ord('c'):
        frames.append(frame) #여기가 이제 우리가 만든 빈 배열에 프레임을 저장하는 것 즉 사진찍는것
    elif key == ord('q'):#q를 입력시 빠져나가는 코드이다.
        break

cap.release()
cv.destroyAllWindows()

#아래가 만약 캡쳐한게 있으면 3장만 이에 붙여줘
if len(frames)>0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))  #hstack 함수 잘 보기 hstack은 사진을 옆으로 붙이는거
    
    cv.imshow('collected images', imgs)
    
    cv.waitKey()
    cv.destroyAllWindows()