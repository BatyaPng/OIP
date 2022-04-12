import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
array = [0] * len(dac)
dac_reverse = list(reversed(dac))
leds = [24, 25, 8, 7, 12, 16, 20, 21]


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def adc():
    for i in range(7, -1, -1):
        GPIO.output(dac_reverse[i], 1)
        array[7 - i] = 1
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            GPIO.output(dac_reverse[i], 0)
            array[7 - i] = 0
    return


GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        v = 0
        array = [0] * len(dac)
        GPIO.output(dac, array)
        adc()

        for i in range(8):
            v += array[i] * (2 ** (7 - i))
            volt = v * 3.3 / 256
        print(decimal2binary(v), v, '  ', volt)
        GPIO.output(leds, 0)

        for i in range(9):
            if v < i * 32 + 5:
                for j in range(i):
                    GPIO.output(leds[j], 1)
                break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
