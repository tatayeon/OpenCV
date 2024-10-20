import cv2 as cv

img=cv.imread('soccer.jpg')	# 영상 읽기

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 캐니 에지 추출
# 최소 오류율, 위치 정확도, 한 두께라는 세가지 기준으로 목적 함수를 정의한다
# 지금 70~80프로 정도 이 캐니 엣지추출을 사용한다.
# 하지만 물체 경계와 그림자 에지를 구별하지 못하는 한계 존재함
# 사람은 물체의 3차원 모델과 겉모슴 모델 appearance model을 사용하여 의미적으로 검출한다.

canny1=cv.Canny(gray, 50, 150) # -> 이게 좀 더 많이 찾아낸다 (Tlow=50, Thigh=150설정)
canny2=cv.Canny(gray, 100, 200)


cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()