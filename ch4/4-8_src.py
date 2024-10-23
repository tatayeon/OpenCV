import skimage
import numpy as np
import cv2 as cv

#스네이크 알고리즘에서 찾아가는 에너지 기준
#이미지 → 엣지 스트랭스
#인터벌 → 둥그렇게 경계가 만든다 따라서 곡률을 써서 동그라면 좀 평평해지게
#도메인 → 변화가 많이 이루어지지 않게 (일반적으로는 잘 안씀)

# horse() 함수로 이미 이진화된 말의 실루엣 이미지를 가져옴
orig = skimage.data.horse()

# 이진화 이미지를 0과 255로 변환하여 OpenCV에서 처리할 수 있는 형식으로 변경
img = 255 - np.uint8(orig) * 255  # 이미지 반전 (배경은 검은색, 말의 실루엣은 흰색)

# 이미지 표시 (말의 실루엣)
cv.imshow('Horse', img)  # 이미 이진화 작업이 완료된 상태

# === 윤곽선 찾기 ===
# cv.findContours는 이진화된 이미지에서 윤곽선을 찾아줌
# RETR_EXTERNAL: 외부 윤곽선만 찾음
# CHAIN_APPROX_NONE: 윤곽선을 구성하는 모든 점을 저장
contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# === 윤곽선 그리기 ===
# 이진화된 이미지를 컬러 이미지로 변환 (윤곽선을 컬러로 표시하기 위해)
img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# 윤곽선 그리기
# drawContours 함수는 찾은 윤곽선을 이미지 위에 그려줌
# img2: 윤곽선을 그릴 대상 이미지
# contours: 윤곽선 좌표
# -1: 모든 윤곽선을 그림
# (255, 0, 255): 윤곽선 색상 (보라색)
# 2: 윤곽선 두께
cv.drawContours(img2, contours, -1, (255, 0, 255), 2) #우리가 찾은 외각ㅇ선으로 이미지 위에 그려준다.

# 윤곽선이 그려진 이미지 표시
cv.imshow('Horse with contour', img2)

# === 윤곽선 특징 분석 ===
# contours[0]은 첫 번째 (그리고 유일한) 윤곽선 데이터
contours = contours[0]

# 윤곽선의 중심, 면적 등을 계산하기 위해 모멘트(moment) 계산
m = cv.moments(contours)

# 면적 계산
area = cv.contourArea(contours)

# 중심 좌표(cx, cy) 계산
# m['m10']/m['m00']와 m['m01']/m['m00']는 윤곽선의 중심점 좌표 (중심값을 의미)
cx, cy = m['m10'] / m['m00'], m['m01'] / m['m00']

# 둘레(perimeter) 계산
perimeter = cv.arcLength(contours, True)  # True: 폐곡선(closed)으로 둘레 계산

# 둥근 정도(roundness) 계산
# (0.4 * pi * area) / perimeter^2은 면적과 둘레를 통해 물체의 둥근 정도를 계산하는 공식
roundness = (0.4 * np.pi * area) / (perimeter * perimeter)

# 계산된 결과를 출력
print('면적 =', area, "\n중심점 = (", cx, ',', cy, ")", "\n둘레 = ", perimeter, "\n둥근 정도 = ", roundness)

# === 다각형 근사화 및 볼록 껍질 ===
# img3: 새 이미지에서 다각형 근사화 및 볼록 껍질을 그리기 위해 사용
img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# 윤곽선 다각형 근사화
# approxPolyDP 함수는 윤곽선을 근사화된 다각형으로 변환
# contours: 근사화할 윤곽선
# 8: 근사화 정밀도를 나타내는 매개변수 (작을수록 정밀도가 높아짐)
# True: 폐곡선으로 다각형 근사화
counter_approx = cv.approxPolyDP(contours, 8, True)

# 근사화된 윤곽선(초록색)을 이미지에 그리기
cv.drawContours(img3, [counter_approx], -1, (0, 255, 0), 2)  # 초록색 윤곽선

# 윤곽선의 볼록 껍질(convex hull) 계산
# convexHull 함수는 윤곽선의 볼록 껍질을 계산
hull = cv.convexHull(contours)

# 볼록 껍질 좌표를 (1, n, 2) 형식으로 재구성 (필요한 차원 변환)
hull = hull.reshape(1, hull.shape[0], hull.shape[2])

# 볼록 껍질(빨간색)을 이미지에 그리기
cv.drawContours(img3, hull, -1, (0, 0, 255), 2)  # 빨간색 윤곽선

# 다각형 근사화 및 볼록 껍질이 그려진 이미지 표시
cv.imshow('Horse with line segments and convex hull', img3)

# 키 입력 대기 및 모든 창 닫기
cv.waitKey()
cv.destroyAllWindows()
