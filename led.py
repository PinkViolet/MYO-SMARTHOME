import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
print("light on")
GPIO.output(21, GPIO.HIGH)
time.sleep(5)
print("light off")
GPIO.output(21, GPIO.LOW)
