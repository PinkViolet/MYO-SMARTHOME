import RPi.GPIO as GPIO
import time
from myo_raw import MyoRaw, Pose


appPosition = 0;            
maxPosition = 1;
minPosition = 0;

pump = 13
led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pump, GPIO.OUT)


myo = MyoRaw()

def changeMotorOnPose(pose):
    print(pose)
    global appPosition
    
    if pose == Pose.WAVE_IN:
        appPosition -= 1
        if appPosition < minPosition:
            appPosition = minPosition
    if pose == Pose.WAVE_OUT:
        appPosition += 1
        if appPosition > maxPosition:
            appPosition = maxPosition
      
    if pose == Pose.FINGERS_SPREAD:
        if appPosition == 0:
            print("light on")
            GPIO.output(led, GPIO.HIGH)
        elif appPosition == 1:
            print("Water out")
            GPIO.output(pump, 0)
            
            
    elif pose == Pose.FIST:
        if appPosition == 0:
            print("light off")
            GPIO.output(led, GPIO.LOW)
        elif appPosition == 1:
            print("Water stop")
            GPIO.output(pump, 1)
    
    elif pose == Pose.THUMB_TO_PINKY:
        if appPosition == 0:
            print("BLINKY")
            GPIO.output(led, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led, GPIO.LOW)
            
    else: 
      pass
    

def main():
    
    # register the handler
    myo.add_pose_handler(changeMotorOnPose)

    # detect Myo and connect with it
    myo.connect()
    
    try:
       while True:
           myo.run(1) # keep running
    except KeyboardInterrupt:
        pass
    finally:
        myo.disconnect() # disconnect with the Myo 
    
    return
    
    
    
main()
    
