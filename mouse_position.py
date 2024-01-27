import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f'Mouse position: x={x}, y={y}')
        time.sleep(1)  # 1초마다 위치 출력
except KeyboardInterrupt:
    print("종료되었습니다.")