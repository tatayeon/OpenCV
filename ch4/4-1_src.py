import cv2 as cv

img=cv.imread('soccer.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #엣지는 그레이 영상에 적용

# 소벨 에지 추출
# 소벨은 프레윗연산자에서 중앙의 값에 가중치를 더욱 크게 만들어서 만든 엣지추출기법중 하나이다.

#이건 커널 제작하는 거
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3) #x와 y를 나눠서 해주는 것은 필터가 나눠져 있기 때문에
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3) #cv.Sobel을 사용해서 넣어주면 된다.

#cv.CV_8U(numpy의 uint8)로 변환
#0보다 작으면 0, 255보다 크면 255로 바꿈
#이게 진자 적용하는 부분 convertScaleAbs사용
sobel_x = cv.convertScaleAbs(grad_x) #절댓값을 취해 양수 영상으로 변환 + numpy의 uint8로 변환 0보다 작으면 0으로 255보다 크면 255로 바꿔
sobel_y = cv.convertScaleAbs(grad_x) #절댓값을 취해서 양수 영상으로 변환

#addWeighted(i1,a,i2,b,c)는 i1*a+i2*b+c를 계산
#i1과 i2가 같은 데이터 형이면 결과는 같은 데이터 형, 다르면 오류 발생
#i1과 i2가 CV_8U인데 계산 결과가 255를 넘으면 255를 기록
edge_strength=cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)	# 에지 강도를 각각 넣어서 x축 y축을 넣는 것
# 같은 데이터형이어야만 하고 다르면 오류 그리고 255를 넘으면 255로 기록한다.

cv.imshow('Original',gray)
cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('edge strength',edge_strength)

cv.waitKey()
cv.destroyAllWindows()