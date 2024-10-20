import skimage
import numpy as np
import cv2 as cv
import time

coffee=skimage.data.coffee()

# 영역 분할 - normalized cut (정규화 절단)
# 영역이 자잘하게 분할하는 경향이 있다.
# 노드랑 그래프컷 알고리즘을 연달아 적용 (합칠지 쪼갤지) 중심에 대해서 계산한다.
#(노멀라이즈 컷)두 영역으로 분할했을 때 분할의 좋은 정도를 측정해주는 목적함수이다.
#에지 검출과 영역분할을 결합하고 계층적으로 영역을 분할하는 알고리즘이다.



start = time.time()
slic = skimage.segmentation.slic(coffee, compactness=20, n_segments=200, start_label=1)

g = skimage.graph.rag_mean_color(coffee, slic, mode = 'similarity')
ncut = skimage.graph.cut_normalized(slic, g)
print(coffee.shape, 'coffee영상 분할하는데', time.time()-start, "초 소요")

marking = skimage.segmentation.mark_boundaries(coffee,ncut)
ncut_coffee = np.uint8(marking*255.0)

cv.imshow('Normalized cut',cv.cvtColor(ncut_coffee,cv.COLOR_RGB2BGR))  

cv.waitKey()
cv.destroyAllWindows()