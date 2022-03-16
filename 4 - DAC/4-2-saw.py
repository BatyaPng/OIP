import RPi.GPIO as GPIO
import time

def decimal_binary(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]


def sawtooth_signal(per, pins):
    for num in range(256):
        bin_num = decimal_binary(num)
        GPIO.output(pins, bin_num)
        time.sleep(per / 255)
    GPIO.output(dac, 0)


GPIO.setmode(GPIO.BCM) 

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM) 
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        val = input("Period:")
        if val == 'q':
            break
        try:
            if int(val) < 0:
                print("Error: not a positive number")
                continue
        except ValueError:
            print("Error: NaN")
        else:
            per = float(val)
            sawtooth_signal(per, dac)
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()