import cv2
import numpy as np
from PIL import Image
import pyautogui
import time
from Quartz import (
    CGWindowListCreateImage, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, 
    kCGWindowImageDefault, CGRectInfinite, CGImageGetWidth, CGImageGetHeight, 
    CGImageGetBytesPerRow, CGImageGetDataProvider, CGDataProviderCopyData
)

# 템플릿 이미지 로드
template_path = 'target3.png'  # 템플릿 이미지 경로
template = cv2.imread(template_path, cv2.IMREAD_COLOR)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template_height, template_width = template_gray.shape[:2]

# 매칭 정확도 설정
threshold = 0.8

def capture_screen():
    """현재 화면을 캡처하는 함수"""
    image = CGWindowListCreateImage(CGRectInfinite, kCGWindowListOptionOnScreenOnly, kCGNullWindowID, kCGWindowImageDefault)
    
    if not image:
        print("화면 캡처 실패")
        return None

    width = CGImageGetWidth(image)
    height = CGImageGetHeight(image)
    bytes_per_row = CGImageGetBytesPerRow(image)

    # 이미지 데이터를 numpy 배열로 변환
    data_provider = CGImageGetDataProvider(image)
    data = CGDataProviderCopyData(data_provider)
    buffer = np.frombuffer(data, dtype=np.uint8)

    # PIL 이미지로 변환 (RGBA 형식)
    try:
        # PIL에서 직접 RGBA 배열로 변환
        pil_image = Image.frombytes("RGBA", (width, height), buffer)
        screen_image = np.array(pil_image)
    except Exception as e:
        print(f"이미지 변환 중 오류: {e}")
        return None

    # OpenCV BGR 형식으로 변환
    bgr_image = cv2.cvtColor(screen_image, cv2.COLOR_RGBA2BGR)
    return bgr_image

def find_and_click_target(show_screenshot=False):
    """스크린에서 템플릿을 찾아 클릭하는 함수"""
    screenshot = capture_screen()
    if screenshot is None:
        print("스크린 캡처 실패")
        return False

    # 템플릿 매칭
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # 매칭된 부분 찾기
    locations = np.where(result >= threshold)

    for loc in zip(*locations[::-1]):
        x, y = loc
        # 클릭할 위치 계산 (템플릿의 중앙 위치로 클릭)
        click_x = x + template_width // 2
        click_y = y + template_height // 2

        # 클릭 이벤트 발생 (pyautogui 사용)
        pyautogui.click(click_x, click_y)
        print(f"클릭 위치: ({click_x}, {click_y})")

        # 매칭된 부분에 빨간색 사각형 그리기 (디버깅용)
        cv2.rectangle(screenshot, (x, y), (x + template_width, y + template_height), (0, 0, 255), 2)
        cv2.imshow("Matched Result", screenshot)
        cv2.waitKey(500)  # 0.5초 대기 후 닫기
        return True

    return False

# 주기적으로 실행되는 루프
while True:
    # 스크린샷을 캡처하고 보여줌
    screenshot = capture_screen()
    if screenshot is not None:
        cv2.imshow("Captured Screenshot", screenshot)  # 캡처된 화면을 띄움

    found = find_and_click_target(show_screenshot=True)
    if found:
        print("대상이 감지되어 클릭 완료")
    else:
        print("대상 미발견")
    
    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(1)  # 1초 대기 후 다시 실행

cv2.destroyAllWindows()
