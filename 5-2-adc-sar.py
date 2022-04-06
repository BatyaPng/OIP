import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
array = [0] * len(dac)
cad_reverse = list(reversed(dac))

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH) 
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():  
    for i in range(7, -1, -1):
        GPIO.output(cad_reverse[i], 1)
        array[7 - i] = 1
        time.sleep(0.001 )
        if(GPIO.input(comp) == 0):
            GPIO.output(cad_reverse[i], 0)
            array[7-i] = 0
    return


try:
    while(1):
        v = 0
        array = [0] * len(dac)
        GPIO.output(dac, array)
        adc()
        for j in range(8):
            v += array[j] * (2 ** (7- j))
            volt = v * 3.3 / 256
        print(decimal2binary(v), v, "  ", volt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()