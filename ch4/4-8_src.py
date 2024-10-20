import skimage
import numpy as np
import cv2 as cv

orig=skimage.data.horse()
img=255-np.uint8(orig)*255
cv.imshow('Horse',img)

# 영역 특징 기술

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.drawContours(img2, contours, -1, (255,0,255),2)
cv.imshow('Horse with contore', img2)

contours = contours[0]

m = cv.moments(contours)
area = cv.contourArea(contours)
cx, cy = m['m10']/m['m00'],m['m01']/m['m00']
perimrter = cv.arcLength(contours, True)
roundness=(0.4*np.pi*area)/(perimrter*perimrter)
print('면적=' , area, "\n중점 = (" , cx,',', cy,")", "\n 둘래= ", perimrter, "둥근 정도 = ", roundness)

img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

counter_approx = cv.approxPolyDP(contours, 8, True)
cv.drawContours(img3, [counter_approx], -1, (0, 255, 0), 2)

hull = cv.convexHull(contours)
hull = hull.reshape(1, hull.shape[0], hull.shape[2])
cv.drawContours(img3, hull, -1, (0, 0, 255), 2)


cv.imshow('Horse with line segments and convex hull',img3)

cv.waitKey()
cv.destroyAllWindows()