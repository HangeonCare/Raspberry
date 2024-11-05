import RPi.GPIO as GPIO
import time

# GPIO 핀 설정

PIR_PIN = 17 # OUT 핀과 연결된 GPIO 핀 번호

# GPIO 설정

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR 센서 준비 중...")

try:
while True:
if GPIO.input(PIR_PIN): # 움직임 감지 시 HIGH 신호 발생
print("움직임 감지됨!")
else:
print("움직임 없음")
time.sleep(1) # 1초 대기

except KeyboardInterrupt:
print("종료 중...")

finally:
GPIO.cleanup() # GPIO 핀 정리

python
import RPi.GPIO as GPIO
import time

PIR_PIN = 17 # GPIO pin connected to the PIR sensor's output pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR sensor initializing...")

try:
while True:
if GPIO.input(PIR_PIN):  
 print("Motion detected!")
else:
print("No motion")
time.sleep(1)

except KeyboardInterrupt:
print("Exiting...")

finally:
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

PIR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR sensor initializing...")

previous_state = False

try:
while True:
current_state = GPIO.input(PIR_PIN)

        if current_state and not previous_state:
            print("Motion detected!")
            previous_state = True

        elif not current_state and previous_state:
            previous_state = False

        time.sleep(0.1)

except KeyboardInterrupt:
print("Exiting...")

finally:
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

t = 0

try:
while True:
time.sleep(0.5)
if GPIO.input(4) == 0 and t == 1:
print("Door is open")
t = 0
if GPIO.input(4) == 1 and t == 0:
print("Door is close")
t = 1
except KeyboardInterrupt:
pass

GPIO.cleanup()

import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

t = 0
userId = 3
serialNumber = "ABC123"

try:
while True:
time.sleep(1)
if GPIO.input(4) == 0:
print("Door is open")

      req = requests.post(
      f"https://port-0-bes-m1ed5avw1d3364c3.sel4.cloudtype.app/users/{userId}/sensors",
      json={"serialNumber": serialNumber,"value": GPIO.input(4)}
      )

    if GPIO.input(4) == 1:
      print("Door is close")

      req = requests.post(
      f"https://port-0-bes-m1ed5avw1d3364c3.sel4.cloudtype.app/users/{userId}/sensors",
      json={"serialNumber": serialNumber,"value": GPIO.input(4)}
      )

except KeyboardInterrupt:
pass

GPIO.cleanup()
