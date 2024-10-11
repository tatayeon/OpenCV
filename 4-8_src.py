import skimage
import numpy as np
import cv2 as cv

orig=skimage.data.horse()
img=255-np.uint8(orig)*255
cv.imshow('Horse',img)

# 영역 특징 기술












cv.imshow('Horse with line segments and convex hull',img3)

cv.waitKey()
cv.destroyAllWindows()