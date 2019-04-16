# get temperature
#import RPi.GPIO as GPIO
from EmulatorGUI import GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)

if GPIO.input(5) == GPIO.HIGH:
     with open('./sensors/temper.txt') as fr:
       for line in fr:
         print(line)
  time.sleep(15)
