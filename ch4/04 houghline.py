import cv2 as cv
import numpy as np

img = cv.imread('lane2.jfif')
h, w = img.shape[:2]
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,150,100)

lines = cv.HoughLines(edges,1,np.pi/180,200) #이건 선이고 원 찾는것도 따로 있다. 1은 파라미터를 조정해가면서 라인을 확인해라
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho    
    y0 = b*rho    
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv.line(img,(x1,y1),(x2,y2),(0,0,255),1)

cv.imshow('edges', edges)
cv.imshow('result', img)
cv.waitKey()
cv.destroyAllWindows()