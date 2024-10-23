import cv2 as cv
import numpy as np

# GrabCut 알고리즘을 이용한 물체 분할
# GrabCut은 사용자가 지정한 물체 내부와 배경을 기준으로 히스토그램을 만들고 그걸 보고 유사성을 찾아서 배경인지 오브젝트인지 확인해 나가는 알고리즘이다.
# 마우스를 사용하여 물체와 배경을 직접 표시하며, 물체의 외곽선을 추정합니다.

# 이미지 읽기
img = cv.imread('soccer.jpg')  # 'soccer.jpg' 이미지를 읽어옴
img_show = np.copy(img)  # 표시용 이미지로 사용될 복사본을 만듦 (붓칠한 결과를 보여주기 위함) (원본파일의 변조를 막기 위해서)

# 마스크 초기화 영상 사이즈에 맞게 만들고 0으로 처리한다.
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
# img와 동일한 크기의 마스크 배열 생성, 초기값은 0으로 설정 (모든 화소를 배경으로 간주)
mask[:, :] = cv.GC_PR_BGD  # 모든 화소를 '배경일 가능성 있음' 상태로 초기화 = 0으로 채운다,

# 붓 크기와 색상 설정
BrushSiz = 9  # 붓 크기 (반지름)
LColor, RColor = (255, 0, 0), (0, 0, 255)  # 왼쪽 버튼은 파란색(물체), 오른쪽 버튼은 빨간색(배경)

# 마우스 이벤트 콜백 함수 정의
#사진위에 추가하고 마스크 위에도 추가를 하는 형식으로 코드를 짠다.
def painting(event, x, y, flags, param):
    # 왼쪽 마우스 버튼 클릭 시 물체(파란색)로 표시
    if event == cv.EVENT_LBUTTONDOWN:   
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)  # 이미지에 파란색 원을 그림
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)  # 해당 영역을 '물체'로 설정

    # 오른쪽 마우스 버튼 클릭 시 배경(빨간색)으로 표시
    elif event == cv.EVENT_RBUTTONDOWN: 
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)  # 이미지에 빨간색 원을 그림
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)  # 해당 영역을 '배경'으로 설정

    # 왼쪽 버튼을 누른 상태에서 마우스를 움직이면 물체 영역을 표시
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)  # 이미지에 파란색 원을 그림
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)  # 해당 영역을 '물체'로 설정

    # 오른쪽 버튼을 누른 상태에서 마우스를 움직이면 배경 영역을 표시
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)  # 이미지에 빨간색 원을 그림
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)  # 해당 영역을 '배경'으로 설정

    # 'Painting' 창에 현재 상태를 표시
    cv.imshow('Painting', img_show)

# 'Painting' 창을 생성하고 마우스 콜백을 설정
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting) #이렇게 해야지 새로운 창이 아니라 그 위에 계속

# 사용자가 마우스로 영역을 지정하는 동안 루프 실행 ('q' 키를 누르면 종료)
while(True):
    if cv.waitKey(1) == ord('q'):
        break

# GrabCut 적용
# 사용자가 지정한 마스크 정보를 기반으로 GrabCut 알고리즘 수행

# GrabCut을 위한 배경과 전경 모델 초기화 (임시 메모리)
background = np.zeros((1, 65), np.float64)  # 배경 모델 히스토그램 0으로 초기화
foreground = np.zeros((1, 65), np.float64)  # 전경 모델

# GrabCut 알고리즘 실행
cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
# img: 원본 이미지
# mask: 물체와 배경을 나타내는 마스크
# background, foreground: GrabCut 알고리즘에 필요한 임시 모델 (배경과 전경 분리)
# 5: 반복 횟수 (계산 반복을 통해 결과를 더 정확하게)
# cv.GC_INIT_WITH_MASK: 사용자 정의 마스크 기반으로 초기화

# 결과 마스크를 이용해 최종적으로 물체만 남긴 이미지 생성
mask2 = np.where((mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')
# 배경으로 분류된 부분은 0, 물체로 분류된 부분은 1로 설정
grab = img * mask2[:, :, np.newaxis]  # 원본 이미지에 마스크 적용하여 물체만 추출

# 결과 이미지 디스플레이
cv.imshow('Grab cut image', grab)

# 키 입력 대기 후 종료
cv.waitKey()
cv.destroyAllWindows()
