import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]


GPIO.setmode(GPIO.BCM) 
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]

try:
    while(True):
        val = input()
        if val == 'q':
            break
        try:
            if float(val) % 1 != 0:
                print("Error: not natural number")
                continue
            elif int(val) < 0:
                print("Error: not natural number")
                continue
            elif int(val) > 255:
                print("Error: bigger than 255")
                continue
        except ValueError:
            print("Error: NaN")
        else:
            num = int(val)
            bin_num = decimal2binary(num)
            print(bin_num)
            GPIO.output(dac, bin_num)

            v = (3.3 * num) / 255
            print("Voltage:", v)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()