import cv2 as cv
import numpy as np

#캐니에지를 사용해서 직선검출

# 이미지 읽기
img = cv.imread('soccer.jpg')  # 'soccer.jpg' 이미지를 읽어와서 img 변수에 저장

# 그레이스케일 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # BGR 색상 이미지를 그레이스케일로 변환

# Canny 에지 검출
canny = cv.Canny(gray, 50, 100)  # Canny 에지 검출 알고리즘 사용 (에지 검출을 위한 임계값은 50과 100)

# 외곽선 검출
# 에지를 명시적으로 연결해 경계선을 찾고 직선으로 변환하는 작업
# 추출된 경계선은 물체를 표현하거나 인식하는 데 유리
contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
#cv.CHAIN_APPROX_NONE은 외곽선의 모든 점을 저장합니다.
#cv.RETR_LIST는 이미지에서 발견된 모든 외곽선(contours)을 단순히 리스트로 반환하며, 계층 구조(부모-자식 관계)를 무시합니다.
 

# contour는 외곽선(또는 윤곽선)의 좌표를 저장한 리스트입니다
# hierarchy는 외곽선의 계층 구조를 표현하는 배열입니다


# 외곽선(경계선)을 검출
# cv.RETR_LIST: 모든 외곽선을 계층 구조 없이 검출
# cv.CHAIN_APPROX_NONE: 외곽선의 모든 점을 저장 (근사하지 않음)

# 조건에 맞는 외곽선을 저장할 리스트
lcontour = []

#캐니에서 검출된 모든것을 사용하는 것이 아니다.
# 검출된 외곽선 중에서 길이가 100 이상인 것만 필터링하여 저장
for i in range(len(contour)):
    if contour[i].shape[0] > 100:  # contour[i]의 길이(점의 수)가 100 이상일 경우
        lcontour.append(contour[i])  # 해당 외곽선을 lcontour 리스트에 추가

# 필터링된 외곽선을 이미지에 그리기
cv.drawContours(img, lcontour, -1, (0, 255, 0), 3)
# img 이미지 위에 lcontour에 저장된 외곽선들을 초록색(0, 255, 0)으로 그리고 두께는 3으로 설정

# 이미지 출력
cv.imshow('Original with contours', img)  # 외곽선이 그려진 원본 이미지를 화면에 표시
cv.imshow('Canny', canny)  # Canny 에지 검출 결과를 화면에 표시

# 키 입력 대기 및 창 닫기
cv.waitKey()  # 키 입력을 기다림
cv.destroyAllWindows()  # 모든 OpenCV 창을 닫음
