import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup(dac, GPIO.OUT)

for i in range(len(dac)):
    GPIO.output(dac[i], number[i])

time.sleep(10)

for i in range(len(dac)):
    GPIO.output(dac[i], 0)

GPIO.cleanup()