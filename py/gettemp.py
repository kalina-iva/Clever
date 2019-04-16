# get temperature
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)

while True:
  if GPIO.input(5) == GPIO.HIGH:
    print("Читаем из файла температуру")
    with open('E:/temper.txt') as fr:
      for line in fr:
        print(line)
  time.sleep(15)