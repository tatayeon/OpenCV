import skimage
import numpy as np
import cv2 as cv

img=skimage.data.coffee()
cv.imshow('Coffee image',cv.cvtColor(img,cv.COLOR_RGB2BGR))

# 영역 분할 1 슈펴화소분할 SLIC
# 화소 분할 비슷한 화소를 묶여있는것 = 슈퍼화소
# 슈퍼화소는 화소보다는 크지만 물체보다 작은 자잘한 영역으로 과잉 분할하는것 
# 첫번째 예시 SLIC k-means클러스터링을 사용함(내부적으로) -> 화소할당 단계와 군집 중심 갱신하는 단계를 반복한다.


slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=200) #n_segments는 초기에 얼마나 짜를건지 compactness는 변화에 얼마나 민감한지 작을수록 민감
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
sp_img1=np.uint8(sp_img1*255.0)

slic2 = skimage.segmentation.slic(img, compactness=40, n_segments=200)
sp_img2 = skimage.segmentation.mark_boundaries(img, slic2)
sp_img2 = np.uint8(sp_img2*255.0)


cv.imshow('Super pixels (compact 20)',cv.cvtColor(sp_img1,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)',cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()