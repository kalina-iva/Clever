# lights off
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

GPIO.output(3, GPIO.LOW)

print("Lights off")

GPIO.cleanup()