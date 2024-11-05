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