import cv2 as cv 

img=cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#허프라고해도 캐니로 먼저 엣지를 추출해야한다.
edges = cv.Canny(gray, 150,200)


# 허프 변환 - 원 찾기
#HOUGH_GRADIENT 함수 사용 GRADIENT이 어느정도 이상 되는것만 사용을 하겠다. 엣지 포인트를 찾는느낌, 1 = size 동일한 사이즈
#200 = 내부적으로 GRADIENT계산하기 위한 캐니 엣지를 사용 이때 스레쉬홀더? apram=1은 원이 몇개가 겹쳐야하는지에대한 설정
#파람2 = 원과원이 떨어진 정도를 찾게 하기 위함, 그 다음에는 원의 반지름의 범위를 설정한다.
#허프변환은 함수로 유독 많이 겹치는걸 찾는거?


#HoughCircles 함수 사용
apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, param2=20, minRadius=50, maxRadius=120)
# cv.HOUGH_GRADIENT: 경사도(Gradient)를 기반으로 원을 탐지하는 방법을 사용합니다.
# param1=150: Canny 에지 검출기의 상한값입니다. 이 값은 경계선을 찾는 데 사용됩니다.
# param2=20: 원 검출 임계값입니다. 이 값이 작을수록 더 많은 원이 검출되지만 정확도는 낮아집니다.


for i in apples[0]:
    cv.circle(img, (int(i[0]),int(i[1])), (int(i[2])) ,(255, 0, 0), 2) #중심좌표 두개와 반지름 한개를 가지고 한다. 라인두께 2

cv.imshow('Apple detection', img)
cv.imshow("Canny edage", edges)

cv.waitKey()
cv.destroyAllWindows()