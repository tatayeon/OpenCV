import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')	 # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,50,100) 

# 경계선 찾기 (직선 검출)
# 외곽선 검출
# 에지를 명시적으로 연결하여 경계선을 찾고 직선으로 변환
# 이후 처리 단계인 물체 표현이나인시겡 유리하다는 장점이 있다.
# 연결된 에지 화소를 연결해 경계선 contour구성


contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #여기 매개변수를 통해서 여러가지 근사 방법을 제공한다.

lcontour=[]
for i in range(len(contour)):
    if contour[i].shape[0]>100:
        lcontour.append(contour[i])
cv.drawContours(img, lcontour, -1,(0,255,0), 3)


cv.imshow('Original with contours',img)    
cv.imshow('Canny',canny)    

cv.waitKey()
cv.destroyAllWindows()