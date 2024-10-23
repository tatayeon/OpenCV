import cv2 as cv
import numpy as np
import math

origin = cv.imread('bg.jpg')
plane = cv.imread("plane.jpg")

h, w = origin.shape[:2]

copyImg1 = origin.copy()  
copyImg2 = origin.copy()

plane_resized = cv.resize(plane, (100, 100))

copyImg1[int(h / 4):int(h / 4) + 100, int(w / 2) - 50:int(w / 2) + 50] = plane_resized
copyImg2[int(h / 4):int(h / 4) + 100, int(w / 2) - 50:int(w / 2) + 50] = plane_resized

fimg = np.zeros_like(origin)  
bimg = np.zeros_like(origin)

centerx = w // 2
centery = h // 2

angle = 25
rad = np.radians(angle)

for y in range(0, h):
    for x in range(0, w):
        dx = (x - centerx) * np.cos(rad) + (y - centery) * np.sin(rad) + centerx
        dx = round(dx) 
        dy = (x - centerx) * (-np.sin(rad)) + (y - centery) * np.cos(rad) + centery
        dy = round(dy)
        if 0 <= int(dx) < w and 0 <= int(dy) < h:
            fimg[int(dy), int(dx)] = copyImg1[y, x]

for y in range(0, h):
    for x in range(0, w):
        dx = (x - centerx) * np.cos(rad) - (y - centery) * np.sin(rad) + centerx
        a = dx - math.floor(dx)  
        dx = math.floor(dx)  
        
        dy = (x - centerx) * np.sin(rad) + (y - centery) * np.cos(rad) + centery
        b = dy - math.floor(dy)  
        dy = math.floor(dy)  

        if 0 <= dx < w - 1 and 0 <= dy < h - 1:
            if np.sum(copyImg2[dy, dx]) >= 30:
                bimg[y, x] = (1 - a) * (1 - b) * copyImg2[dy, dx] + \
                             a * (1 - b) * copyImg2[dy, dx + 1] + \
                             (1 - a) * b * copyImg2[dy + 1, dx] + \
                             a * b * copyImg2[dy + 1, dx + 1]

result = np.hstack((origin, fimg, bimg))

cv.imshow("결과", result)

cv.waitKey(0)
cv.destroyAllWindows()