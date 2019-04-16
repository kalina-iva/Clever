# lights on
#import RPi.GPIO as GPIO
from EmulatorGUI import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

GPIO.output(3, GPIO.HIGH)

print("Lights on")

GPIO.cleanup()