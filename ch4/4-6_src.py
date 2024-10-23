import skimage
import numpy as np
import cv2 as cv
import time

# 커피 이미지 데이터 로드
coffee = skimage.data.coffee()

# 영역 분할 - Normalized cut (정규화 절단)
# Normalized cut은 그래프 이론에 기반한 이미지 분할 알고리즘입니다.
# 이 방법은 영역을 과도하게 분할할 수 있지만, 
# 노드와 그래프 컷 알고리즘을 통해 영역을 나누거나 합칠지 결정합니다.
# 정규화된 절단(normalized cut) 함수는 분할된 두 영역 간의 유사성을 계산하는 방식으로,
# 좋은 분할을 찾는 목적 함수를 사용합니다. 
# 이 알고리즘은 에지 검출과 영역 분할을 결합하고 계층적으로 영역을 나눕니다.

# 시작 시간 기록
start = time.time()

# SLIC 기반의 슈퍼화소 분할
slic = skimage.segmentation.slic(coffee, compactness=20, n_segments=600, start_label=1)
# compactness=20: SLIC 알고리즘에서 슈퍼화소의 모양을 제어하는 값 (작을수록 불규칙한 모양 허용)
# n_segments=600: 600개의 슈퍼화소로 이미지를 분할
# start_label=1: 라벨링이 1부터 시작 (SLIC에서 할당된 라벨링)

# RAG (Region Adjacency Graph) 생성
g = skimage.graph.rag_mean_color(coffee, slic, mode='similarity')
# rag_mean_color: 슈퍼화소 간의 평균 색상 차이를 기반으로 그래프를 만듭니다.
# mode='similarity': 유사도를 기반으로 RAG를 생성 (다른 영역 간의 유사성을 계산)

# Normalized cut 알고리즘 적용
ncut = skimage.graph.cut_normalized(slic, g)
# cut_normalized: RAG에서 정규화된 절단을 적용하여 분할

# 소요 시간 출력
print(coffee.shape, 'coffee영상 분할하는데', time.time() - start, "초 소요")
# 분할된 커피 이미지의 크기와 알고리즘 수행에 걸린 시간을 출력

# 영역 경계 표시
#우리가 만든걸 원본사진 위에 그리는 작업
marking = skimage.segmentation.mark_boundaries(coffee, ncut)
# mark_boundaries: 분할된 영역의 경계를 원본 이미지 위에 표시

# 255로 스케일 변환 후 이미지 저장
ncut_coffee = np.uint8(marking * 255.0)
# mark_boundaries 함수는 부동소수점 이미지를 반환하므로 255 배율로 변환하여 8비트 정수형 이미지로 변환

# OpenCV 창에 분할된 이미지 디스플레이
cv.imshow('Normalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))
# cv.imshow: 'Normalized cut'이라는 창에 결과 이미지를 표시
# cv.cvtColor: RGB 형식의 이미지를 BGR로 변환하여 OpenCV에서 표시

cv.waitKey()  # 키 입력 대기
cv.destroyAllWindows()  # 모든 OpenCV 창 닫기
