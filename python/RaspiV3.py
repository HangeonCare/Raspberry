#GNU nano 7.2                                                                                 3.py
import requests         # 서버 신호 전송용
import RPi.GPIO as GPIO # 도어 센서
import time             # 서버에 신호 초마다 보내기

GPIO.setmode(GPIO.BCM)

# 사용할 GPIO 슬롯(4)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

userId = 5              # 신호 전송용 ID
serialNumber = "ABC123" # 신호 전송용 시리얼 번호

# 서버 신호 전송 (0 | 1)
try:
    while True:
        time.sleep(1)
        current_state = GPIO.input(4)

        # 상태 출력
        if current_state == 0:
            print("Door is open")
        else:
            print("Door is close")

        # 상태 전송
        try:
            req = requests.post(
                f"https://port-0-bes-m1ed5avw1d3364c3.sel4.cloudtype.app/users/{userId}/sensors",
                json={"serialNumber": serialNumber, "value": current_state}
            )
            req.raise_for_status()  # 요청 실패 시 예외 발생
        except requests.exceptions.RequestException as e:
            print(f"Failed to send request: {e}")

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    GPIO.cleanup()


