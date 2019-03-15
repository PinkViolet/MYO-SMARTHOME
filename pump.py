import time

import RPi.GPIO as GPIO


pump = 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pump, GPIO.OUT)
print("water out")
GPIO.output(pump,0)
time.sleep(5)
GPIO.output(pump,1)
print("stop")

