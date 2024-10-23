import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0)  # 혹은 cap = cv.VideoCapture(1)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

frames = []
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("프레임 획득 실패")
        break
    
    cv.imshow("video display", frame)
    
    key = cv.waitKey(1)  # 1밀리초 단위로 화면을 갱신
    if key == ord('c'):  # 'c' 키를 누르면 프레임 저장
        frames.append(frame)
        print("프레임 저장됨")
    elif key == ord('q'):  # 'q' 키를 누르면 종료
        break

cap.release()
cv.destroyAllWindows()

# 프레임이 저장되었는지 확인
if len(frames) > 0:
    imgs = frames[0]  # 첫 번째 이미지를 기준으로 설정
    for i in range(1, min(3, len(frames))):  # 최대 3개의 이미지만 수평으로 붙임
        imgs = np.hstack((imgs, frames[i]))  # 프레임을 수평으로 연결
    
    # 수집된 이미지를 보여줌
    cv.imshow('collected images', imgs)
    cv.waitKey()
    cv.destroyAllWindows()
else:
    print("저장된 프레임이 없습니다.")
