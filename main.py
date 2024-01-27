'''
!!먼저 가상환경을 생성한 뒤, which python 명령어 입력시, 가상환경 경로의 python이 나타나는지 확인해볼 것!!
그러니까..
.zshrc 파일에 python 명령어에 대한 alias를 설정했는데
이렇게 설정하면 가상환경이 실행 중임에도 가상환경의 python이 실행되는게 아니라
alias에 해당하는 python이 동작하고,
따라서 가상환경에 설치된 패키지는 인식하지 못한다.
'''


# 핵심은, pyautogui 함수 사용 시, 좌표 가져오는 것은 논리좌표로(2배), 클릭하는 마우스 좌표는 물리좌표로!
import time
import pyautogui
image_path = 'airdrop.png'

# 화면에서 이미지 찾기
time.sleep(3)
print("start!")
logical_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
print(f"logical_location: {logical_location}")

if logical_location:
    # 물리적 픽셀 좌표로 변환 (DPI 스케일링 고려)
    physical_location = (logical_location.x / 2, logical_location.y / 2)  # Retina 디스플레이의 경우 2x 스케일링
    
    # 클릭
    pyautogui.click(physical_location)
    time.sleep(1)
    pyautogui.click(physical_location)
else:
    print("이미지를 찾을 수 없습니다.")
print("end..")

